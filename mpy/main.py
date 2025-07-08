"""
/***************************************************************
 *                                                             *
 *                    GNU GENERAL PUBLIC LICENSE               *
 *                       Version 3, 29 June 2007               *
 *                                                             *
 *  This program is free software: you can redistribute it and *
 *  or modify it under the terms of the GNU General Public     *
 *  License as published by the Free Software Foundation,      *
 *  either version 3 of the License, or (at your option) any   *
 *  later version.                                             *
 *                                                             *
 *  This program is distributed in the hope that it will be    *
 *  useful, but WITHOUT ANY WARRANTY; without even the implied *
 *  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR    *
 *  PURPOSE. See the GNU General Public License for more       *
 *  details.                                                   *
 *                                                             *
 *  You should have received a copy of the GNU General Public  *
 *  License along with this program. If not, see               *
 *  <https://www.gnu.org/licenses/>.                           *
 *                                                             *
 ***************************************************************/
 
 /* In simple terms:
 * This program is free software. You can use, share, and change it.
 * If you change it and share it, you must keep it open and use the same license.
 * The license MUST be included with the software, and also when you share it.        <----- EXTREMELY IMPORTANT. thank you very much
 * There is no warranty—if something goes wrong, it's not our responsibility.
 * See the full license at https://www.gnu.org/licenses/gpl-3.0.html
 */
"""

#import machine
import ssd1306
import time
from machine import Pin, ADC, I2C, Timer, I2S

PIN_POTENTIOMETER = 1
PIN_BUTTON_TS = 4  # Time signature button (this is on the encoder)
PIN_ENCODER_A = 2
PIN_ENCODER_B = 3
PIN_BUTTON1 = 9
PIN_BUTTON2 = 8

I2S_ID = 0       # ID of I2S Bus
I2S_BCK = 39     # Connects to BCK pin on dac
I2S_WS = 40      # Connects to LRCK pin on dac
I2S_SD = 38      # Connects to DIN pin on dac

OLED_SCL = 6
OLED_SDA = 5
OLED_WIDTH = 128
OLED_HEIGHT = 64


# Constants
ADC_MAX = 4095
AMP_MAX = 0x7FFF
OLED_UPDATE_INTERVAL = 0.05

# Global vars
bpm = 120
volume = 50
is_running = False
presets = [60, 120, 180]
preset_index = 0
last_encoder_value = 0

# Time signature logic
TIME_SIGNATURES = [
    {"name": "4/4", "pattern": ["B", "b", "b", "b"]},
    {"name": "3/4", "pattern": ["B", "b", "b"]},
    {"name": "6/8", "pattern": ["B", "b", "b", "b", "b", "b"]},
]
time_signature_index = 0
current_beat = 0

# Init peripherals
adc = ADC(PIN_POTENTIOMETER)
button1 = Pin(PIN_BUTTON1, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(PIN_BUTTON2, Pin.IN, Pin.PULL_DOWN)
time_sig_btn = Pin(PIN_BUTTON_TS, Pin.IN, Pin.PULL_DOWN)  # Active low
encoder_a = Pin(PIN_ENCODER_A, Pin.IN, Pin.PULL_UP)
encoder_b = Pin(PIN_ENCODER_B, Pin.IN, Pin.PULL_UP)
i2c = I2C(0, scl=Pin(OLED_SCL), sda=Pin(OLED_SDA))
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

# BCK  - Bit clock
# LRCK - word select (WS)
# DIN  - Serial data (SD)
i2s = I2S(
    I2S_ID,
    sck=Pin(I2S_BCK),    # BCK
    ws=Pin(I2S_WS),      # LRCK
    sd=Pin(I2S_SD),      # DIN
    mode=I2S.TX,
    bits=16,
    format=I2S.MONO,
    rate=22050,
    ibuf=4096
)

def read_volume():
    raw = adc.read()
    vol = int(raw / ADC_MAX * 100)
    return vol

def set_volume(vol):
    # Handled in metronome_tick() via amp scaling
    pass

def rotary_encoder_update():
    global bpm, last_encoder_value
    a = encoder_a.value()
    b = encoder_b.value()
    value = (a << 1) | b
    if value != last_encoder_value:
        if value == 0b01:
            bpm += 1
        elif value == 0b10:
            bpm -= 1
        bpm = max(30, min(300, bpm))
        last_encoder_value = value

def draw_oled():
    oled.fill(0)
    bpm_str = str(bpm)
    oled.text("BPM", 45, 0)
    oled.text(bpm_str, 54, 20)
    oled.rect(5, 15, 10, 40, 1)
    bar_height = int(40 * (volume / 100))
    oled.fill_rect(6, 54-bar_height, 8, bar_height, 1)
    oled.text("{}%".format(volume), 2, 56)
    for i, val in enumerate(presets):
        y = 15 + i*15
        oled.rect(110, y, 15, 12, 1)
        oled.text(str(val), 114, y+2)
        if i == preset_index:
            oled.hline(110, y+13, 15, 1)
    oled.text(TIME_SIGNATURES[time_signature_index]["name"], 54, 56)
    oled.show()

def handle_buttons():
    global is_running, preset_index, bpm, time_signature_index, current_beat
    # Debounce state
    static_btn1 = getattr(handle_buttons, "_btn1", 1)
    static_btn2 = getattr(handle_buttons, "_btn2", 1)
    static_ts = getattr(handle_buttons, "_ts", 1)

    btn1 = button1.value()
    btn2 = button2.value()
    ts_btn = time_sig_btn.value()

    # Button 1: Start/stop
    if not btn1 and static_btn1:
        is_running = not is_running
    # Button 2: Preset
    if not btn2 and static_btn2:
        preset_index = (preset_index + 1) % len(presets)
        bpm = presets[preset_index]
    # Time signature button
    if not ts_btn and static_ts:
        time_signature_index = (time_signature_index + 1) % len(TIME_SIGNATURES)
        current_beat = 0

    # Save last state for debounce
    handle_buttons._btn1 = btn1
    handle_buttons._btn2 = btn2
    handle_buttons._ts = ts_btn

def tick_pcm_buf(amp=0x4000, duration_ms=50, rate=22050):
    # Simple click: short burst of high amplitude, then silence. basically a square wave.
    n_samples = int(rate * duration_ms / 1000)
    buf = bytearray()
    for i in range(n_samples):
        sample = amp if i < n_samples // 3 else 0
        # 16-bit signed PCM, little endian
        buf += int(sample).to_bytes(2, 'little', signed=True)
    return buf

def metronome_tick(timer):
    global current_beat
    if is_running:
        pattern = TIME_SIGNATURES[time_signature_index]["pattern"]
        accent = pattern[current_beat]
        # Stressed beat: louder
        if accent == "B":
            amp = int(volume / 100 * AMP_MAX)
        else:
            amp = int(volume / 100 * (AMP_MAX // 3))
        buf = tick_pcm_buf(amp)
        try:
            i2s.write(buf)
        except Exception as e:
            print("I2S error:", e)
        current_beat = (current_beat + 1) % len(pattern)

def main():
    global volume
    metronome_timer = Timer(0)
    metronome_timer.deinit()
    last_bpm = bpm
    last_time_sig = time_signature_index
    last_volume = volume
    last_preset = preset_index
    while True:
        rotary_encoder_update()
        handle_buttons()
        volume = read_volume()
        # metronome timer
        interval_ms = int(60000 / bpm)
        if is_running:
            metronome_timer.init(period=interval_ms, mode=Timer.PERIODIC, callback=metronome_tick)
        else:
            metronome_timer.deinit()
        # Only update OLED if something changed
        if (bpm != last_bpm or time_signature_index != last_time_sig or volume != last_volume or preset_index != last_preset):
            draw_oled()
            last_bpm = bpm
            last_time_sig = time_signature_index
            last_volume = volume
            last_preset = preset_index
        time.sleep(OLED_UPDATE_INTERVAL)

if __name__ == "__main__":
    main()

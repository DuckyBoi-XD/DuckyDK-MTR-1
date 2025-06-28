import machine
import ssd1306
import time
from machine import Pin, ADC, I2C, Timer

from machine import I2S

####################### Replace these with your actual GPIO assignments!
PIN_POTENTIOMETER = 1
PIN_POWER_SWITCH = 2
PIN_ENCODER_A = 3
PIN_ENCODER_B = 4
PIN_BUTTON1 = 5
PIN_BUTTON2 = 6
###############################

##################### PCM5102A I2S pins (replace with your wiring)
I2S_ID = 0
I2S_BCK = 7     # Bit clock
I2S_WS = 8      # Word select (LRCK)
I2S_SD = 9      # Data
###############################

###################### OLED I2C config (replace with your wiring)
OLED_SCL = 10
OLED_SDA = 11
OLED_WIDTH = 128
OLED_HEIGHT = 64
################################

# global vars
bpm = 120
volume = 50
is_running = False
presets = [60, 120, 180]
preset_index = 0
time_signature = "4/4"
last_encoder_value = 0

# Init peripherals
adc = ADC(PIN_POTENTIOMETER)
button1 = Pin(PIN_BUTTON1, Pin.IN, Pin.PULL_UP)                 # chnage this if not active low
button2 = Pin(PIN_BUTTON2, Pin.IN, Pin.PULL_UP)                 # chnage this if not active low 
power_switch = Pin(PIN_POWER_SWITCH, Pin.IN, Pin.PULL_UP)       # chnage this if not active low
encoder_a = Pin(PIN_ENCODER_A, Pin.IN, Pin.PULL_UP)             # chnage this if not active low
encoder_b = Pin(PIN_ENCODER_B, Pin.IN, Pin.PULL_UP)             # chnage this if not active low
i2c = I2C(0, scl=Pin(OLED_SCL), sda=Pin(OLED_SDA))
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

# I2S config for PCM5102A
######### PLS LEAVE THIS TYSM #########
i2s = I2S(
    I2S_ID,
    sck=Pin(I2S_BCK),
    ws=Pin(I2S_WS),
    sd=Pin(I2S_SD),
    mode=I2S.TX,
    bits=16,
    format=I2S.MONO,
    rate=22050,
    ibuf=4096
)
################################

def read_volume():
    raw = adc.read()
    vol = int(raw / 4095 * 100)
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
    oled.text(time_signature, 54, 56)
    oled.show()

def handle_buttons():
    global is_running, preset_index, bpm
    if not button1.value():  # Active low
        is_running = not is_running
        time.sleep(0.2)
    if not button2.value():  # Active low
        preset_index = (preset_index + 1) % len(presets)
        bpm = presets[preset_index]
        time.sleep(0.2)

# Generate a short "tick" sound 
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
    if is_running:
        # Volume maps: 0-100 -> 0-0x7FFF
        amp = int(volume / 100 * 0x7FFF)
        buf = tick_pcm_buf(amp)
        try:
            i2s.write(buf)
        except Exception as e:
            pass  # ignore erros

def main():
    global volume
    metronome_timer = Timer(0)
    metronome_timer.deinit()
    while True:
        if not power_switch.value():
            oled.poweroff()
            continue
        else:
            oled.poweron()
        rotary_encoder_update()
        handle_buttons()
        volume = read_volume()
        # metronome timer
        interval_ms = int(60000 / bpm)
        if is_running:
            metronome_timer.init(period=interval_ms, mode=Timer.PERIODIC, callback=metronome_tick)
        else:
            metronome_timer.deinit()
        draw_oled()
        time.sleep(0.05)

if __name__ == "__main__":
    main()

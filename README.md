# DuckyDK-MTR-1

### Description
This is a Metronome device called the DuckyDK MTR-1. This is for musicians, like me, who needs a portable metronome that can be used anywhere. It is designed in a compact form to maximize space usage and portability. 

### Inspiration
This idea was thought of and inspired when I bought a new drum kit which I loved, and I wanted to think of different projects I could make which is connected to my drum kit. One idea that was obvious was to make a custom metronome. This is the result of that idea. Even though devices like laptops can do this, I wanted to make a portable, offline metronome what is not reliant on any device and can be brought along to many places. 

**Name**
The name DuckyDK MTR-1 is from many thing. **Ducky** comes from my username **Ducky**Boi_XD, **DK** is/comes from **D**rum **K**it or **D**uc**k**. **MTR** comes from **M**etronome, while the **1** indicates that this is the first version of this metronome project.

### Features 
These are the features that are implemented in the DuckyDK MTR-1:
- **Compact Design**: The device is contained in a small, portable, compact case which is custom designed to fit all the necessary components. 

- **Adjustable Tempo/Time signature**: The tempo and time signature can be adjusted to fit the user's needs. The temp can be adjusted by the rotary encoder and the time signature can be adjusted by the internal button on the rotary encoder.

- **Volume Control**: The volume of the metronome can be adjusted but the potentiometer attached to the case. This the user to adjust their preference for their volume. For example, I play drums which can be quite loud, resulting in the need of a louder metronome.

- **2 Control Buttons**: On the case is 2 buttons controlling 2 important functions of the metronome. The first buttons is the start or stop mechanism of the metronome. The second button is a preset button. This button contains 3 presets that can be selected and used by pushing the preset button.

- **Info Display**: The device contains a appropriately sized OLED display which contains many necessary information. It contains, a big indicator of the current tempo/BPM in the centre of the screen, a volume level on the right side of the screen as a bar with percentage sign underneath, a 3 boxes which is the preset indicator on left side of the screen, and lastly, the current time signature located on the bottom of the screen, under the BPM indicator.

- **Headphone Jack**: The device contains a headphone jack which allows the user to connect headphones to the device. This is currently the only way to hear th metronome. This headphone jack also contains a switch when the headphones are connected. This can be change to do whatever you want.

### BOM (Bill of Materials)

| Component | Quantity | Description | Base Price | Extra Costs | Link | 
|-----------|----------|-------------|------------|-------------|------|
| Xiao ESP32-S3 Plus | 1 | MCU (Micro controller Unit) (Digikey) | $7.99 | (GST) | https://www.digikey.co.nz/en/products/detail/seeed-technology-co-ltd/102010671/26553873 | 
| PCM5102APWR | 1 | DAC (Digital to Analog Converter) (Digikey) | $4.43 | (GST) | https://www.digikey.co.nz/en/products/detail/texas-instruments/PCM5102APWR/3727211?s=N4IgTCBcDaIAoGECyBWAjABjAQTgdQCUQBdAXyA |
| MAX9722AEUE+ | 1 | AMP (Audio Amplifier) (Digikey) | $1.52  | (GST) | https://www.digikey.co.nz/en/products/detail/analog-devices-inc-maxim-integrated/MAX9722AEUE/1495288 | 
| SJ1-3514N | 1 | 3.5mm Headphone Jack (Digikey) | $1.19  | (GST) | https://www.digikey.co.nz/en/products/detail/same-sky-formerly-cui-devices/sj1-3514n/738685 | 
| PTN092-H50115K1A | 1 | Potentiometer (Digikey) | $2.00  | (GST) | https://www.digikey.co.nz/en/products/detail/same-sky-formerly-cui-devices/PTN092-H50115K1A/24767692 |
| EC11E18244A5 | 1 | Rotary Encoder (Digikey) | $4.85 | (GST) | https://www.digikey.co.nz/en/products/detail/alps-alpine/ec11e18244a5/21721665 |
| MFR-25FRF52-4K7 | 10 | Resistor 4.7k Ohm (Digikey) | $0.39 | (GST) | https://www.digikey.co.nz/en/products/detail/yageo/MFR-25FRF52-4K7/9139057 | 
| CFR-25JB-52-470R | 10 | Resistor 470 Ohm (Digikey) | $0.34 | (GST) | https://www.digikey.co.nz/en/products/detail/yageo/CFR-25JB-52-470R/2211 | 
| C320C104K5R5TA7305 | 10 | Capacitor 0.1 uf (Digikey) | $0.22 | (GST) | https://www.digikey.co.nz/en/products/detail/kemet/C320C104K5R5TA7305/12701231 |
| C330C105M5R5TA7301 | 10 | Capacitor 1 uf (Digikey) | $3.08 | (GST) | https://www.digikey.co.nz/en/products/detail/kemet/C330C105M5R5TA7301/14681306 |
| C330C225M5U5TA7303 | 10 | Capacitor 2.2 uf (Digikey) | $4.58 | (GST) | https://www.digikey.co.nz/en/products/detail/kemet/C330C225M5U5TA7303/6562327 |
| EEA-GA1C100H | 10 | Capacitor 10 uf (Digikey) | $1.53 | (GST) | https://www.digikey.co.nz/en/products/detail/panasonic-electronic-components/EEA-GA1C100H/2513289 |
| ECE-A1AN101X | 10 | Capacitor 100 uf (Digikey) | $2.71 | (GST) | https://www.digikey.co.nz/en/products/detail/panasonic-electronic-components/ECE-A1AN101X/364922 | 
| 404070001 | 1 | ESD Safe Tweezers (Straight) (Digikey) | $2.50 | (GST) | https://www.digikey.co.nz/en/products/detail/seeed-technology-co-ltd/404070001/5488233 |
| 422 | 1 | ESD Safe Tweezers (Curved) (Digikey) | $3.95 | (GST) | https://www.digikey.co.nz/en/products/detail/adafruit-industries-llc/422/7241434 |
| 1007-24-1-2000-001-1-TD | 5 (feet) | Wires | $2.22 | (GST) | https://www.digikey.co.nz/en/products/detail/cnc-tech/1007-24-1-2000-001-1-TD/17799235 |
| 20-0600-21 | 1 (20 pins) | Male pin headers | $3.83 | (GST) | https://www.digikey.co.nz/en/products/detail/aries-electronics/20-0600-21/4207162 |
| 97791003111 | 10 | Screws | $2.24 | (GST) | https://www.digikey.co.nz/en/products/detail/w%C3%BCrth-elektronik/97791003111/10056389 | 
|





### Construction
The DuckyDK MTR-1 was mainly made using Kicad, Fusion 360, Github and Slack. I made all the PCB schematics and design of the PCB in Kicad, while I made the 3D model of the case in Fusion 360. I used Github to document my process of making the project and Slack to help me answer questions.

## Kicad Schematic

## Kicad PCB

## Fusion Case

## Fusion Production Case

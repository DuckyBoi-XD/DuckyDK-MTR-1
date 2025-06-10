---
title: "DuckyDK MTR-1"
author: "@DuckyBoi_XD"
description: "A metronome for any type of music practice which you can adjust BPM with knob and preset buttons"
created_at: "2025-06-07"
---

# June 7

I started noting down and reaserching about what componets my project before designing anything so I will understand my budget constraint and models to use. 

I decided that my metronome is going to have the features:

- Rotary Encoder + switch 1 - to adjust the BPM + Start/Stop
- Potentiometer - to adjust volume
- Switch 1 - Power Button
- Siwtch 2 - BPM preset switch
- Switch 3 - LED control
- OLED screen
- LEDs
- Battery charging
- 2000mAh battery
- Headphone jack
- USB C

### MCU (Microcontroller Unit)
I looked for a MCU to use and it was clear for me to use a ESP32 due to it's audio capablitlites. I originally looked into the TinyPICO due to it having a charging capabilites, small form factor and a DAC output. Sadly, my friend said it was way to expensive as a MCU coming in as $35 USD (including shipping). The TinyPICO also requires me to add and external DAC output due to the DAC on the TinyPICO originally for speakers. I asked for help in the awesome community of the slack hackclub and a guy named [@Ryan Green](https://hackclub.slack.com/team/U090854913L) helped me in finding a better and cheaper option than the TinyPICO and they suggested the ESP32 C series, and suggested the Seeed Studio XIAO ESP32-S3 Plus. This MCU was not only cheaper, but wnow looking at it, I seems better than the TinyPico. 

https://www.seeedstudio.com/Seeed-Studio-XIAO-ESP32S3-Plus-p-6361.html?srsltid=AfmBOooKQnAGTpSrEHZqcqBNI1Rd_LhihN7JWmB5JLmD3Lf3hoWj0AXO

PS. When signing up for the Seeed Studio, I got a $5 coupon for my first puchcuse so its even less :D.

---

<img width="425" alt="Screenshot 2025-06-10 at 5 21 27 PM" src="https://github.com/user-attachments/assets/163a0939-bcf1-40a7-81f7-4eed523d4592" />

<img width="400" alt="Screenshot 2025-06-10 at 5 34 51 PM" src="https://github.com/user-attachments/assets/1c424e47-eb16-4f9a-adc5-f1a61e42d2c4" />

<img width="252" alt="Screenshot 2025-06-10 at 6 11 41 PM" src="https://github.com/user-attachments/assets/16c840ce-fb6f-4d92-a8ad-82d3f1f5a4fd" />

---
# June 8

## Headphone Jack
This was a very simple desion due to [@Ryan Green](https://hackclub.slack.com/team/U090854913L) on slack providing me information in how to search for a headphone jack (Samesky). I found the SJ1-3514N which was a great headphone jack with an internal switch for power effecincy. The jack has, 3.5mm audio standered, it uses a through hole mounting style (for stabibility) and its horizontal which creates a low profile for it. Due to later on information I'm planning to buy it on Mouser but I'll get into it later.

https://nz.mouser.com/ProductDetail/Same-Sky/SJ1-3514N?qs=WyjlAZoYn53nY7Y2NKZXvw%3D%3D&utm_source=OEMSecrets&utm_medium=aggregator&utm_campaign=SJ1-3514N&utm_term=SJ1-3514N&utm_content=Same+Sky

---
<img width="800" alt="Screenshot 2025-06-10 at 5 57 03 PM" src="https://github.com/user-attachments/assets/de3001f7-ae82-4a50-bf99-b5090cb0afc6" />
(NZD)

---
## June 9

## OLED screen
I wanted a decently sized screen due to the amount of information I wanted on it (BPM, battery indicator, preset indicator, volume indicator) so I chose a 1.54 inch display and a resoultion of 126x64 due to its space and detail. I also made sure that the screen connector was a I2C so it will be compatable with the MCU i chose



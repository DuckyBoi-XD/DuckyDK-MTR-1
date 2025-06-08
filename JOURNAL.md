---
title: "DuckyDK MTR-1"
author: "@DuckyBoi_XD"
description: "A metronome for any type of music practice which you can adjust BPM with knob and preset buttons"
created_at: "2025-06-07"
---


## June 8 - 9

I started noting down and reaserching about what is my project going to have and especcially what MCU to use. I decided that my metronome is going to have the features:
- Knob/switch 1 - to adjust the BPM + power button
- Knob/switch 2 - to adjust volume + metronome starter/stopper
- Switch 1 - Screen control
- Siwtch 2 - BPM preset switch
- Switch 3 - LED control
- OLED screen
- LEDs
- Battery charging
- 2000mAh battery
- Headphone jack
- USB C

<img width="503" alt="Screenshot 2025-06-08 at 12 41 48 PM" src="https://github.com/user-attachments/assets/e722692c-f6e8-4200-b323-1c638b9abbb8" />

I looked for a MCU to use and it was clear for me to use a ESP32 due to it's audio capablitlites. I originally looked into the TinyPICO due to it having a charging capabilites, small form factor and a DAC output. Sadly, my friend said it was way to expensive as a MCU coming in as $35 USD (including shipping). The TinyPICO also requires me to add and external DAC output due to the DAC on the TinyPICO originally for speakers. I asked for help in the awesome community of the slack hackclub and many people helped me in finding a better and cheaper option than the TinyPICO and I they suggested the ESP32 C series Mini, and thats where I came across the ESP32 C6 Super Mini. 

The ESP32 C6 Super Mini includes, Battery pins for charging, uses USB C, 18 practical GPIOs to use, avalibility for OLED screen. I would also need ot add an external DAC and heakphone jack for the MCU but I was going to do that anyways.

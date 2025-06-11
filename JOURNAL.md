---
title: "DuckyDK MTR-1"
author: "@DuckyBoi_XD"
description: "A metronome for any type of music practice which you can adjust BPM with knob and preset buttons"
created_at: "2025-06-07"
---

# June 7

I started noting down and reaserching about what componets my project before designing anything so I will understand my budget constraint and models to use. 

I decided that my metronome is going to have the features:

- Rotary Encoder + switch 1 - to adjust the BPM + Time signiture adjuster
- Potentiometer - to adjust volume
- Switch 1 - Power Button
- Siwtch 2 - Start/Stop
- Switch 3 - LED control
- Switch 4 - BPM preset switch
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

<img width="200" alt="Screenshot 2025-06-10 at 5 21 27 PM" src="https://github.com/user-attachments/assets/163a0939-bcf1-40a7-81f7-4eed523d4592" />

<img width="200" alt="Screenshot 2025-06-10 at 5 34 51 PM" src="https://github.com/user-attachments/assets/1c424e47-eb16-4f9a-adc5-f1a61e42d2c4" />

<img width="200" alt="Screenshot 2025-06-10 at 6 11 41 PM" src="https://github.com/user-attachments/assets/16c840ce-fb6f-4d92-a8ad-82d3f1f5a4fd" />

Time spent: 12 hours
---
# June 8

## Headphone Jack
This was a very simple desion due to [@Ryan Green](https://hackclub.slack.com/team/U090854913L) on slack providing me information in how to search for a headphone jack (Samesky). I found the SJ1-3514N which was a great headphone jack with an internal switch for power effecincy. The jack has, 3.5mm audio standered, it uses a through hole mounting style (for stabibility) and its horizontal which creates a low profile for it. Due to later on information I'm planning to buy it on Mouser but I'll get into it later.

https://nz.mouser.com/ProductDetail/Same-Sky/SJ1-3514N?qs=WyjlAZoYn53nY7Y2NKZXvw%3D%3D&utm_source=OEMSecrets&utm_medium=aggregator&utm_campaign=SJ1-3514N&utm_term=SJ1-3514N&utm_content=Same+Sky

## DAC (DIgital to Anoloug Converter) + AMP (Amplifier)

For my metronome I'm planning to mainly use a headphone jack meaning I should use a AMP for the output sound and I needed a DAC to make it sound better and louder. Again this was a simple dicision because of the help of [@Ryan Green](https://hackclub.slack.com/team/U090854913L) giving me advice on which ones to use. 

https://nz.mouser.com/ProductDetail/Texas-Instruments/PCM5102APWR?qs=E2%2FxqS9xjzrfECkwEYoiyg%3D%3D
https://nz.mouser.com/ProductDetail/Texas-Instruments/TPA6139A2PWR?qs=TeC8nwD7mVr7iydXyN4ieA%3D%3D\

<img width="959" alt="Screenshot 2025-06-10 at 8 15 01 PM" src="https://github.com/user-attachments/assets/f2b52fd2-9d95-46e4-a279-3b37c79abe1b" />

(PRICES IS IN NZD)

Time spent: 3 hours
---
# June 9

## OLED screen
I wanted a decently sized screen due to the amount of information I wanted on it (BPM, battery indicator, preset indicator, volume indicator) so I chose a 1.54 inch display and a resoultion of 126x64 due to its space and detail. I also made sure that the screen connector was a I2C so it will be compatable with the MCU i chose. I was orignially going to use the waveshare 1.54 OLED screen but after taking to my friend and [@Ryan Green](https://hackclub.slack.com/team/U090854913L), they both said that they were too expensive and that there where cheaper ones on aliexpress. I discovered many OLED screen that looked the exact same so I just chose the most cheapest one which meet my requirements. This took alot of time due to the amount of back and forwarth, going between waveshare and aliexpress.

https://www.aliexpress.com/item/1005007522995297.html?spm=a2g0o.productlist.main.26.718c77e95YgPXH&algo_pvid=a7be4b24-26e1-413a-bb4c-be501f5b124d&algo_exp_id=a7be4b24-26e1-413a-bb4c-be501f5b124d-23&pdp_ext_f=%7B%22order%22%3A%2291%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%2112.52%215.95%21%21%2153.20%2125.27%21%402101c5a417495046110686580e928c%2112000041132196825%21sea%21NZ%210%21ABX&curPageLogUid=sUhAimMM6TY6&utparam-url=scene%3Asearch%7Cquery_from%3A#nav-description

<img width="350" alt="Screenshot 2025-06-10 at 7 06 51 PM" src="https://github.com/user-attachments/assets/3b3e9a2c-786d-4192-be60-6c811610bc4b" />

<img width="350" alt="Screenshot 2025-06-10 at 7 11 07 PM" src="https://github.com/user-attachments/assets/0b4aaea1-9d80-48a9-9b63-0eff744c0e7e" />

Time spent: 6 hours
---

# June 10

## GitHub + Shop

I fixed the formatting of the Journal for the porject so it is easier to read and understand. I also changed some of websites to source the parts. This is because of Mouser shipping is expensive to my country (New Zealand) but they allow free shipping if you spend over $50, so I tried to soucre as many items as possible from Mouser. I was able to source the DAC, AMP, Headphone Jack, MCU, Potentiometer and Rotary Encoder from Mouser and mabye more in the future. I've tried to source the buttons, switches and OLED screens from Mouser but there wasn't any good options that I liked and or was way to expensive. 

https://nz.mouser.com/ProductDetail/Alps-Alpine/EC11E18244A5?qs=seHrhfPpLDydI9KuruJHhA%3D%3D
https://nz.mouser.com/ProductDetail/Same-Sky/PTN091-H50115K1A?qs=IKkN%2F947nfAyOT2cVMxFFA%3D%3D

<img width="300" alt="Screenshot 2025-06-11 at 8 13 15 PM" src="https://github.com/user-attachments/assets/46923e75-e0a7-4033-abb0-986c685fc835" />
<img width="800" alt="Screenshot 2025-06-11 at 8 24 27 PM" src="https://github.com/user-attachments/assets/829590b6-f220-461a-8f86-4893c1a4d75a" />

Time spent: 6 hours
---

# June 11





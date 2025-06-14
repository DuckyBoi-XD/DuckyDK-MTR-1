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
- 3000mAh battery
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

<img width="500" alt="Screenshot 2025-06-10 at 8 15 01 PM" src="https://github.com/user-attachments/assets/f2b52fd2-9d95-46e4-a279-3b37c79abe1b" />

(PRICES IS IN NZD)

Time spent: 3 hours
---
# June 9

## OLED Screen
I wanted a decently sized screen due to the amount of information I wanted on it (BPM, battery indicator, preset indicator, volume indicator) so I chose a 1.54 inch display and a resoultion of 126x64 due to its space and detail. I also made sure that the screen connector was a I2C so it will be compatable with the MCU i chose. I was orignially going to use the waveshare 1.54 OLED screen but after taking to my friend and [@Ryan Green](https://hackclub.slack.com/team/U090854913L), they both said that they were too expensive and that there where cheaper ones on aliexpress. I discovered many OLED screen that looked the exact same so I just chose the most cheapest one which meet my requirements. This took alot of time due to the amount of back and forwarth, going between waveshare and aliexpress.


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

## Buttons + Switchs

I searched for the bottons for my project. I wanted buttons that were sleek and smooth while still being high quality. I search for a long time on Aliexpress for the right switches that met my expectations and I found a nice option. These buttons were exactly what I was looking for but it is quite expensive compared to others and due to the amount I needed (3). 
I need a separte 'button' as a power button, so I wanted to use a switch for my power button. I looked for a large switch but most of the swtiches on Aliexpress was too small. Luckliy, I found a large switch which was perfect for my power switch.

## Battery

This was really hard for me due to me not really knowing where to buy it. I ended up having to source thr battery from Aliexpress which even tho I didn't really trsut, I didn't really have any other choice. I ended up choosing a 3000 mAh LiPo 3.7v battery from a random Aliexpress store (which I still don't trust). Hopefully I can change it later on but at this moment I'll keep it for now.

<img width="400" alt="Screenshot 2025-06-12 at 8 27 15 PM" src="https://github.com/user-attachments/assets/abf72d59-bc73-4cc0-a893-d1900098b3c6" />
<img width="400" alt="Screenshot 2025-06-12 at 8 27 22 PM" src="https://github.com/user-attachments/assets/a466a519-4182-4c1a-a32e-79200c7bf756" />
<img width="400" alt="Screenshot 2025-06-12 at 8 27 30 PM" src="https://github.com/user-attachments/assets/e2e1f05f-a3f5-4013-a43c-ed77984b6682" />

Time spent: 6 hours
---
# June 12

## OLED Screen Revamp

I was fed up with the difficulty of searching for a the correct connectors of a non descriptive, skectchy OLED display so I decided to change the OLED to a more expensive but way more eaiser and descriptive OLED screen which even includes a connector SO I DONT'T NEED TO WASTE TIME FIGURING IT OUT AGAIN. I decided to go with the Waveshare 1.54inch OLED Display Module. This has an extensive description while having a wiki to answer and help with any problems I encounter. 

PS. [@Ryan Green](https://hackclub.slack.com/team/U090854913L) hasn't been online since around June 10th so i haven't gotten much help.

https://www.waveshare.com/1.54inch-oled-module.htm?sku=25512

## BOM Sheet

I started and filled out a BOM (Bill of Materials) for all the parts I was going to buy, mainly to see and understand my budget an to organise my parts. This helped me understand where the money was going into and letted me look through where I found the products. 

<img width="500" alt="Screenshot 2025-06-12 at 7 43 12 PM" src="https://github.com/user-attachments/assets/883afe7b-4d99-4595-88d7-1f6df11ef4a1" />

<img width="1197" alt="Screenshot 2025-06-12 at 8 55 00 PM" src="https://github.com/user-attachments/assets/87918fa5-630a-43cb-a25c-f2d16f1a4efc" />

Time spent: 6 hours
---

# June 13

## Resistoers + Capasitors
I stared the search for my resistors and capasitors for my pcb and project. Resistors and capasitors are really confusion for me because of all the specifications and terminology that are connected to them. After all my reserch and help from [@Ryan Green](https://hackclub.slack.com/team/U090854913L), I chose a resistors and capasitors for my project which was the most difficult part to source due to large range of different types of them and also me not really knowing what type to use. 

https://nz.mouser.com/ProductDetail/YAGEO/CFR-12JT-52-10K?qs=uYSUDLr2H%2FLcN1orUM1YfA%3D%3D
https://nz.mouser.com/ProductDetail/Vishay-BC-Components/K104K15X7RF5WH5?qs=sGAEpiMZZMvsSlwiRhF8qnONkpDJ9RVUxkyDki3dR58%3D
https://nz.mouser.com/ProductDetail/Nichicon/UFW2A330MPD?qs=kArNe9LFxXnyndxqtATAYA%3D%3D

## DigiKey
Before I used Mouser as my source for most of my parts but after talking with my friend I chose to use DigiKey as my part sourcing. This is because of the cheaper prices and appearntly quicker shipping. I searched for all of the parts on the DigiKey that was previously on Mouser and surprisingly all of them were on there, and so I can easily transition from one to the other. 

https://www.digikey.co.nz/en/products/detail/texas-instruments/PCM5102APWR/3727211?s=N4IgTCBcDaIAoGECyBWAjABjAQTgdQCUQBdAXyA
https://www.digikey.co.nz/en/products/detail/texas-instruments/tpa6139a2pwr/2552043
https://www.digikey.co.nz/en/products/detail/same-sky-formerly-cui-devices/sj1-3514n/738685
https://www.digikey.co.nz/en/products/detail/seeed-technology-co-ltd/102010671/26553873
https://www.digikey.co.nz/en/products/detail/same-sky-formerly-cui-devices/ptn091-h50115k1a/24767334
https://www.digikey.co.nz/en/products/detail/alps-alpine/ec11e18244a5/21721665

## LED
For the LED's I wasn't really sure excatly what I wanted but I chose to use the LED's used on the HackPad (SK6812 NanoPixel). I knew I wanted and RGB LED but I wasn't sure if I wanted an RGB W LED, but when looking at the options, there wasn't many, so I just stuck with the RGB LED. Since I wanted to use atleast 12+ LED, I decided to get 20 of them (2 in increments of 10).

https://www.digikey.co.nz/en/products/detail/adafruit-industries-llc/4691/13170955

<img width="400" alt="Screenshot 2025-06-14 at 12 51 58 AM" src="https://github.com/user-attachments/assets/b8f39c6f-0481-4a59-9c79-43fa75e38b54" />
<img width="400" alt="Screenshot 2025-06-14 at 12 52 01 AM" src="https://github.com/user-attachments/assets/ef464659-53cd-4768-afed-f57e208cef54" />
<img width="400" alt="Screenshot 2025-06-14 at 12 50 50 AM" src="https://github.com/user-attachments/assets/71c9860f-f465-4735-ad4a-d0c25c4ac136" />
<img width="400" alt="Screenshot 2025-06-14 at 12 41 28 AM" src="https://github.com/user-attachments/assets/416fbc80-ee42-45fc-98c8-8648f5cb7c52" />

Time spent: 8 hours
---



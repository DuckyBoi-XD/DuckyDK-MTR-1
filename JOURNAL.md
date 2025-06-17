---
title: "DuckyDK MTR-1"
author: "@DuckyBoi_XD"
description: "A metronome for any type of music practice which you can adjust BPM with knob and preset buttons, and OLED screen for information, a battery for a portable mode and more"
created_at: "2025-06-07"
---

# June 7

I started noting down and researching what components my project will need before designing anything, so I will understand my budget constraint and models to use. 

I decided that my metronome is going to have the following features:

- Rotary Encoder + switch 1 - to adjust the BPM + Time signiture adjuster
- Potentiometer - to adjust volume
- Switch 1 - Power Button
- Switch 2 - Start/Stop
- Switch 3 - LED control
- Switch 4 - BPM preset switch
- OLED screen
- LEDs
- Battery charging
- 3000mAh battery
- Headphone jack
- USB C

<img width="200" alt="Screenshot 2025-06-10 at 6 11 41 PM" src="https://github.com/user-attachments/assets/16c840ce-fb6f-4d92-a8ad-82d3f1f5a4fd" />

### MCU (Microcontroller Unit)
I looked for an MCU to use, and it was clear to me to use an ESP32 due to its audio capabilities. I originally looked into the TinyPICO due to having a charging capability, a small form factor, and a DAC output. Sadly, my friend said it was way too expensive as an MCU coming in at $35 USD (including shipping). The TinyPICO also requires me to add an external DAC output due to the DAC on the TinyPICO originally being for speakers. I asked for help in the awesome community of the Slack Hackclub, and a guy named [@Ryan Green](https://hackclub.slack.com/team/U090854913L) helped me find a better and cheaper option than the TinyPICO, and they suggested the ESP32 C series, and suggested the Seeed Studio XIAO ESP32-S3 Plus. This MCU was not only cheaper, but now looking at it, it seems better than the TinyPico. 

https://www.seeedstudio.com/Seeed-Studio-XIAO-ESP32S3-Plus-p-6361.html?srsltid=AfmBOooKQnAGTpSrEHZqcqBNI1Rd_LhihN7JWmB5JLmD3Lf3hoWj0AXO

PS. When signing up for the Seeed Studio, I got a $5 coupon for my first purchase, so it's even less :D

<img width="200" alt="Screenshot 2025-06-10 at 5 21 27 PM" src="https://github.com/user-attachments/assets/163a0939-bcf1-40a7-81f7-4eed523d4592" />
<img width="200" alt="Screenshot 2025-06-10 at 5 34 51 PM" src="https://github.com/user-attachments/assets/1c424e47-eb16-4f9a-adc5-f1a61e42d2c4" />

Time spent: 12 hours
---
# June 8

### Headphone Jack
This was a very simple decision due to [@Ryan Green](https://hackclub.slack.com/team/U090854913L) on Slack providing me information on how to search for a headphone jack (Samesky). I found the SJ1-3514N, which was a great headphone jack with an internal switch for power efficiency. The jack has, 3.5mm audio standard, it uses a through-hole mounting style (for stability) and is horizontal, which creates a low profile for it. Due to later information, I'm planning to buy it on Mouser, but I'll get into it later.

https://nz.mouser.com/ProductDetail/Same-Sky/SJ1-3514N?qs=WyjlAZoYn53nY7Y2NKZXvw%3D%3D&utm_source=OEMSecrets&utm_medium=aggregator&utm_campaign=SJ1-3514N&utm_term=SJ1-3514N&utm_content=Same+Sky

### DAC (DIgital to Anoloug Converter) + AMP (Amplifier)

For my metronome, I'm planning to mainly use a headphone, meaning I should use an AMP for the output sound, and I need a DAC to make it sound better and louder. Again, this was a simple decision because of the help of [@Ryan Green](https://hackclub.slack.com/team/U090854913L), who gave me advice on which ones to use. 

https://nz.mouser.com/ProductDetail/Texas-Instruments/PCM5102APWR?qs=E2%2FxqS9xjzrfECkwEYoiyg%3D%3D
https://nz.mouser.com/ProductDetail/Texas-Instruments/TPA6139A2PWR?qs=TeC8nwD7mVr7iydXyN4ieA%3D%3D\

<img width="500" alt="Screenshot 2025-06-10 at 8 15 01 PM" src="https://github.com/user-attachments/assets/f2b52fd2-9d95-46e4-a279-3b37c79abe1b" />

(PRICES ARE IN NZD)

Time spent: 3 hours
---
# June 9

### OLED Screen
I wanted a decently sized screen due to the amount of information I wanted on it (BPM, battery indicator, preset indicator, volume indicator), so I chose a 1.54-inch display and a resolution of 126x64 due to its space and detail. I also made sure that the screen connector was an I2C, so it will be compatible with the MCU I chose. I was originally going to use the Waveshare 1.54 OLED screen, but after talking to my friend and [@Ryan Green](https://hackclub.slack.com/team/U090854913L), they both said that they were too expensive and that there were cheaper ones on Aliexpress. I discovered many OLED screens that looked  the same, so I just chose the cheapest one that met the minimum requirements. This took a lot of time due to the amount of back and forth, going between Waveshare and Aliexpress.


<img width="350" alt="Screenshot 2025-06-10 at 7 06 51 PM" src="https://github.com/user-attachments/assets/3b3e9a2c-786d-4192-be60-6c811610bc4b" />

<img width="350" alt="Screenshot 2025-06-10 at 7 11 07 PM" src="https://github.com/user-attachments/assets/0b4aaea1-9d80-48a9-9b63-0eff744c0e7e" />

Time spent: 6 hours
---

# June 10

### GitHub + Shop

I fixed the formatting of the Journal for the project so it is easier to read and understand. I also changed some of the websites to source the parts. This is because Mouser shipping is expensive to my country (New Zealand), but they allow free shipping if you spend over $50, so I tried to source as many items as possible from Mouser. I was able to source the DAC, AMP, Headphone Jack, MCU, Potentiometer, and Rotary Encoder from Mouser and maybe more in the future. I've tried to source the buttons, switches, and OLED screens from Mouser, but there weren't any good options that I liked and they were too expensive. 

https://nz.mouser.com/ProductDetail/Alps-Alpine/EC11E18244A5?qs=seHrhfPpLDydI9KuruJHhA%3D%3D
https://nz.mouser.com/ProductDetail/Same-Sky/PTN091-H50115K1A?qs=IKkN%2F947nfAyOT2cVMxFFA%3D%3D

<img width="300" alt="Screenshot 2025-06-11 at 8 13 15 PM" src="https://github.com/user-attachments/assets/46923e75-e0a7-4033-abb0-986c685fc835" />
<img width="800" alt="Screenshot 2025-06-11 at 8 24 27 PM" src="https://github.com/user-attachments/assets/829590b6-f220-461a-8f86-4893c1a4d75a" />

Time spent: 6 hours
---

# June 11

### Buttons + Switchs

I searched for the buttons for my project. I wanted buttons that were sleek and smooth while still being high quality. I searched for a long time on Aliexpress for the right switches that met my expectations, and I found a nice option. These buttons were exactly what I was looking for, but it is quite expensive compared to others, and due to the amount I needed (3). 
I need a separate 'button' as a power button, so I wanted to use a switch for my power button. I looked for a large switch, but most of the switches on Aliexpress were too small. Luckily, I found a large switch that was perfect for my power switch.

<img width="400" alt="Screenshot 2025-06-12 at 8 27 15 PM" src="https://github.com/user-attachments/assets/abf72d59-bc73-4cc0-a893-d1900098b3c6" />
<img width="400" alt="Screenshot 2025-06-12 at 8 27 22 PM" src="https://github.com/user-attachments/assets/a466a519-4182-4c1a-a32e-79200c7bf756" />

### Battery

This was hard for me because I didn't know where to buy it. I ended up having to source the battery from Aliexpress, which, even tho I didn't trust it, I didn't have any other choice. I ended up choosing a 3000 mAh LiPo 3.7V battery from a random Aliexpress store (which I still don't trust). Hopefully, I can change it later on, but at this moment, I'll keep it for now.

<img width="400" alt="Screenshot 2025-06-12 at 8 27 30 PM" src="https://github.com/user-attachments/assets/e2e1f05f-a3f5-4013-a43c-ed77984b6682" />

Time spent: 6 hours
---
# June 12

### OLED Screen Revamp

I was fed up with the difficulty of searching for the correct connectors of a non-descriptive, sketchy OLED display, so I decided to change the OLED to a more expensive but way easier and descriptive OLED screen, which even includes a connector, so I don't need TO WASTE TIME FIGURING IT OUT AGAIN. I decided to go with the Waveshare 1.54-inch OLED Display Module. This has an extensive description, while having a wiki to answer and help with any problems I encounter. 

PS. [@Ryan Green](https://hackclub.slack.com/team/U090854913L) hasn't been online since around June 10. I haven't gotten much help.

https://www.waveshare.com/1.54inch-oled-module.htm?sku=25512

<img width="500" alt="Screenshot 2025-06-12 at 7 43 12 PM" src="https://github.com/user-attachments/assets/883afe7b-4d99-4595-88d7-1f6df11ef4a1" />

### BOM Sheet

I started and filled out a BOM (Bill of Materials) for all the parts I was going to buy, mainly to see and understand my budget and to organise my parts. This helped me understand where the money was going and let me look through where I found the products. 

<img width="1197" alt="Screenshot 2025-06-12 at 8 55 00 PM" src="https://github.com/user-attachments/assets/87918fa5-630a-43cb-a25c-f2d16f1a4efc" />

Time spent: 6 hours
---

# June 13

### Resistoers + Capasitors
I started the search for my resistors and capacitors for my PCB and project. Resistors and capacitors are confusing for me because of all the specifications and terminology that are connected to them. After all my research and help from [@Ryan Green](https://hackclub.slack.com/team/U090854913L), I chose resistors and capacitors for my project, which was the most difficult part to source due to the large range of different types of them, and also not really knowing what type to use. 

https://nz.mouser.com/ProductDetail/YAGEO/CFR-12JT-52-10K?qs=uYSUDLr2H%2FLcN1orUM1YfA%3D%3D

https://nz.mouser.com/ProductDetail/Vishay-BC-Components/K104K15X7RF5WH5?qs=sGAEpiMZZMvsSlwiRhF8qnONkpDJ9RVUxkyDki3dR58%3D

https://nz.mouser.com/ProductDetail/Nichicon/UFW2A330MPD?qs=kArNe9LFxXnyndxqtATAYA%3D%3D

<img width="400" alt="Screenshot 2025-06-14 at 12 51 58 AM" src="https://github.com/user-attachments/assets/b8f39c6f-0481-4a59-9c79-43fa75e38b54" />
<img width="400" alt="Screenshot 2025-06-14 at 12 52 01 AM" src="https://github.com/user-attachments/assets/ef464659-53cd-4768-afed-f57e208cef54" />

### DigiKey
Before, I used Mouser as my source for most of my parts, but after talking with my friend, I chose to use DigiKey as my part sourcing. This is because of the cheaper prices and quicker shipping. I searched for all of the parts on DigiKey that were previously on Mouser, and surprisingly, all of them were on there, so I can easily transition from one to the other. 

https://www.digikey.co.nz/en/products/detail/texas-instruments/PCM5102APWR/3727211?s=N4IgTCBcDaIAoGECyBWAjABjAQTgdQCUQBdAXyA
https://www.digikey.co.nz/en/products/detail/texas-instruments/tpa6139a2pwr/2552043
https://www.digikey.co.nz/en/products/detail/same-sky-formerly-cui-devices/sj1-3514n/738685
https://www.digikey.co.nz/en/products/detail/seeed-technology-co-ltd/102010671/26553873
https://www.digikey.co.nz/en/products/detail/same-sky-formerly-cui-devices/ptn091-h50115k1a/24767334
https://www.digikey.co.nz/en/products/detail/alps-alpine/ec11e18244a5/21721665

<img width="400" alt="Screenshot 2025-06-14 at 12 41 28 AM" src="https://github.com/user-attachments/assets/416fbc80-ee42-45fc-98c8-8648f5cb7c52" />

### LED
For the LED's I wasn't sure exactly what I wanted, but I chose to use the LEDs used on the HackPad (SK6812 NanoPixel). I knew I wanted an RGB LED, but I wasn't sure if I wanted an RGB W LED or an RGB LED. But when looking at the options, there weren't many, so I just stuck with the RGB LED. Since I wanted to use at least 12+ LED, I decided to get 20 of them (2 in increments of 10).

https://www.digikey.co.nz/en/products/detail/adafruit-industries-llc/4691/13170955

<img width="400" alt="Screenshot 2025-06-14 at 12 50 50 AM" src="https://github.com/user-attachments/assets/71c9860f-f465-4735-ad4a-d0c25c4ac136" />

Time spent: 8 hours
---

# June 14

### Capacitors
I went through the capacitors I chose and I realised that I didn't have enough types of capacitors for my parts. I looked through and I found a bunch of different types of capacitors that I could use, and with the right application of said capacitors. I also made sure that the capacitors were alright with my parts, but through this, I also rethought my decision on my battery from Aliexpress, and I found another option, but I wasn't sure about the laws in shipping to my country (NZ).

https://www.digikey.co.nz/en/products/detail/kemet/C320C104K5R5TA7305/12701231
https://www.digikey.co.nz/en/products/detail/cornell-dubilier-knowles/336CKE050M/6141081

<img width="400" alt="Screenshot 2025-06-14 at 6 54 36 PM" src="https://github.com/user-attachments/assets/f4711128-e0d0-42de-b594-482553d73d94" />
<img width="400" alt="Screenshot 2025-06-14 at 6 54 43 PM" src="https://github.com/user-attachments/assets/bbc23ff9-bdf7-41dd-99ab-cd11a27ecfca" />

### BOM Sheet Revemp
I updated my BOM sheet to have the updated location of DigiKey and the OLED screen that I previously changed. I also fixed the mix-up with the different Aliexpress links from when I accidentally mixed them up. At this point, looking at the price, I wonder if the reviews would accept this, given how expensive it is.

<img width="800" alt="Screenshot 2025-06-14 at 7 17 53 PM" src="https://github.com/user-attachments/assets/637b1b63-d4ba-4ca7-b3cc-9424705c91dd" />

### Thoughts 
Today I decided I should have a thoughts section where I give my thoughts about what I've done, and just curious things I'm thinking of. Today's one is 'WHY DOES IT TAKE SO LONG TO SOURCE PARTS'.
I also thought about how I was going to show how the parts are going to be connected, since some parts would be on the case and not the PCB.


Time spent: 7 hours
---

# June 15

### Models - Schematics + Footprints

I looked for the schematics and the footprints for all my parts for my project. Most of the parts I used Digikey's feature, where they provided a link forwarding to a website containing the schematics and footprints, even CAD models in some cases. Most of the footprints and schematics are from SnapMagic, but a few are from Ultra Library and the official seller. There are how however, a few I couldn't get due to being from STUPID ALIEXPRESS WITHOUT DATA SHEET. For this, because I'm not using any major parts from Aliexpress, I'm just using random unofficial schematics and footprints that match up with my parts. The parts I'm getting from Aliexpress and Waveshare are parts that are going to be implemented on the case, so an exact footprint match wouldn't be necessary.

https://www.snapeda.com/home/
https://www.ultralibrarian.com/

<img width="188" alt="Screenshot 2025-06-16 at 5 49 11 PM" src="https://github.com/user-attachments/assets/9f46f8ba-210a-4eda-adda-8074310bef2a" />

### Schematics

### Files
For the schematics, I imported all the files from the parts and set up the library. This process took a bit due to my forgetting how to do it and using trial and error to figure it out. Once I finished importing all the schematic and footprint files, I started work on the schematics part of Kicad, where I wired almost every component to its designated spot. 

### OLED Screen
The OLED screen was really simple to wire due to it only including 4 pins, 2 of them just being ground and power pins. The DAC and AMP are where it got tricky. I started by connecting all the power and simple pins, like ground and power pins. 

### LED
Another easy wiring job was the LEDs. The LEDs were simple due to my understanding of how the LEDs work and how they should be labelled from previous projects. I placed the LED pin on a random GPIO (which I later found out was a bad idea) a moved on to the next component.

### DAC + AMP
I focused on one part at a time, this being the DAC. I looked into the data sheet of the DAC and found the description of each pin and connected some of the obvious ones. I did the same to the AMP, but when looking at the pins, I realised that there wasn't a positive input for the audio. This really stumped me, so I wanted to look into the data sheet of the AMP and found that the 14-pin (the one I was using) didn't even include any positive audio inputs. I asked [@Ryan Green](https://hackclub.slack.com/team/U090854913L) about it since he helped me pick out the AMP, and he was surprised about the AMP not including the positive inputs. At this point, I decided to find a different AMP, this time being a 16-pin header.

https://www.ti.com/lit/ds/symlink/pcm5102a.pdf?HQS=dis-dk-null-digikeymode-dsf-pf-null-wwe&ts=1750061065007&ref_url=https%253A%252F%252Fwww.ti.com%252Fgeneral%252Fdocs%252Fsuppproductinfo.tsp%253FdistId%253D10%2526gotoUrl%253Dhttps%253A%252F%252Fwww.ti.com%252Flit%252Fgpn%252Fpcm5102a

https://www.ti.com/general/docs/suppproductinfo.tsp?distId=10&gotoUrl=https%3A%2F%2Fwww.ti.com%2Flit%2Fgpn%2Ftpa6139a2

<img width="300" alt="Screenshot 2025-06-16 at 8 18 07 PM" src="https://github.com/user-attachments/assets/c408e8ea-ac56-4457-bdbf-81220f48c226" />
<img width="400" alt="Screenshot 2025-06-16 at 5 49 53 PM" src="https://github.com/user-attachments/assets/0a53159b-6513-465f-b113-4aef31bbcd53" />
<img width="500" alt="Screenshot 2025-06-16 at 7 58 48 PM" src="https://github.com/user-attachments/assets/050e9057-1fc0-4ed1-a28f-01f9803e582c" />

### Thought
I have to find a new AMP that has 16 pins or at least has a positive input pin, unlike the one I was using. I figured out how to connect the components to the PCB that are in the case, yay. Still trying to figure out what all the pins mean.

Time spent: 8 hours
---

# June 16

### Schematics

### DAC
I worked on the DAC pin by researching and making sure it its place on the right place. This process was very surprising due to the amount of power going to the ground and power. There was a lot of confusion about the capacitors needed for the ground pin, but I decided to leave it out for another day to figure out. Despite the quick explanation, this process took a long time due to the research of each pin and figuring out where each pin goes.

<img width="200" alt="Screenshot 2025-06-17 at 5 10 31 PM" src="https://github.com/user-attachments/assets/a9be7c7b-890d-4605-814b-f35e37286531" />

### LED
I didn't really do much with the LED; the only thing I did was to change where the pin was located since I wasn't bothered to use a SPI pin.

<img width="1000" alt="Screenshot 2025-06-17 at 5 14 29 PM" src="https://github.com/user-attachments/assets/748ee19a-7cbb-444a-b151-c6f06c99982e" />

### Thought
I still have to find an AMP that works with the DAC. 

Time spent: 6
---

# June 17







---
title: "DuckyDK MTR-1"
author: "@DuckyBoi_XD"
description: "A metronome for any type of music practice which you can adjust BPM with knob and preset buttons, and OLED screen for information, a battery for a portable mode and more"
created_at: "2025-06-07"
---

## Total Project Hour Count: 83

# June 7

I started noting down and researching what components my project will need before designing anything, so I will understand my budget constraint and models to use. 

I decided that my metronome is going to have the following features:

- Rotary Encoder + switch 1 - to adjust the BPM + Time signature adjuster
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

### MCU (Micro-controller Unit)
I looked for an MCU to use, and it was clear to me to use an ESP32 due to its audio capabilities. I originally looked into the TinyPICO due to having a charging capability, a small form factor, and a DAC output. Sadly, my friend said it was way too expensive as an MCU coming in at $35 USD (including shipping). The TinyPICO also requires me to add an external DAC output due to the DAC on the TinyPICO originally being for speakers. I asked for help in the awesome community of the Slack Hackclub, and a guy named [@Ryan Green](https://hackclub.slack.com/team/U090854913L) helped me find a better and cheaper option than the TinyPICO, and they suggested the ESP32 C series, and suggested the Seeed Studio XIAO ESP32-S3 Plus. This MCU was not only cheaper, but now looking at it, it seems better than the TinyPico. 

https://www.seeedstudio.com/Seeed-Studio-XIAO-ESP32S3-Plus-p-6361.html?srsltid=AfmBOooKQnAGTpSrEHZqcqBNI1Rd_LhihN7JWmB5JLmD3Lf3hoWj0AXO

PS. When signing up for the Seeed Studio, I got a $5 coupon for my first purchase, so it's even less :D

<img width="200" alt="Screenshot 2025-06-10 at 5 21 27 PM" src="https://github.com/user-attachments/assets/163a0939-bcf1-40a7-81f7-4eed523d4592" />
<img width="200" alt="Screenshot 2025-06-10 at 5 34 51 PM" src="https://github.com/user-attachments/assets/1c424e47-eb16-4f9a-adc5-f1a61e42d2c4" />

Time spent: 6 hours
---
# June 8

### Headphone Jack
This was a very simple decision due to [@Ryan Green](https://hackclub.slack.com/team/U090854913L) on Slack providing me information on how to search for a headphone jack (Samesky). I found the SJ1-3514N, which was a great headphone jack with an internal switch for power efficiency. The jack has, 3.5mm audio standard, it uses a through-hole mounting style (for stability) and is horizontal, which creates a low profile for it. Due to later information, I'm planning to buy it on Mouser, but I'll get into it later.

https://nz.mouser.com/ProductDetail/Same-Sky/SJ1-3514N?qs=WyjlAZoYn53nY7Y2NKZXvw%3D%3D&utm_source=OEMSecrets&utm_medium=aggregator&utm_campaign=SJ1-3514N&utm_term=SJ1-3514N&utm_content=Same+Sky

### DAC (DIgital to Analog Converter) + AMP (Amplifier)

For my metronome, I'm planning to mainly use a headphone, meaning I should use an AMP for the output sound, and I need a DAC to make it sound better and louder. Again, this was a simple decision because of the help of [@Ryan Green](https://hackclub.slack.com/team/U090854913L), who gave me advice on which ones to use. 

https://nz.mouser.com/ProductDetail/Texas-Instruments/PCM5102APWR?qs=E2%2FxqS9xjzrfECkwEYoiyg%3D%3D
https://nz.mouser.com/ProductDetail/Texas-Instruments/TPA6139A2PWR?qs=TeC8nwD7mVr7iydXyN4ieA%3D%3D\

<img width="500" alt="Screenshot 2025-06-10 at 8 15 01 PM" src="https://github.com/user-attachments/assets/f2b52fd2-9d95-46e4-a279-3b37c79abe1b" />

(PRICES ARE IN NZD)

Time spent: 1 hour
---
# June 9

### OLED Screen
I wanted a decently sized screen due to the amount of information I wanted on it (BPM, battery indicator, preset indicator, volume indicator), so I chose a 1.54-inch display and a resolution of 126x64 due to its space and detail. I also made sure that the screen connector was an I2C, so it will be compatible with the MCU I chose. I was originally going to use the Waveshare 1.54 OLED screen, but after talking to my friend and [@Ryan Green](https://hackclub.slack.com/team/U090854913L), they both said that they were too expensive and that there were cheaper ones on Aliexpress. I discovered many OLED screens that looked  the same, so I just chose the cheapest one that met the minimum requirements. This took a lot of time due to the amount of back and forth, going between Waveshare and Aliexpress.


<img width="350" alt="Screenshot 2025-06-10 at 7 06 51 PM" src="https://github.com/user-attachments/assets/3b3e9a2c-786d-4192-be60-6c811610bc4b" />

<img width="350" alt="Screenshot 2025-06-10 at 7 11 07 PM" src="https://github.com/user-attachments/assets/0b4aaea1-9d80-48a9-9b63-0eff744c0e7e" />

Time spent: 3 hours
---

# June 10

### GitHub + Shop

I fixed the formatting of the Journal for the project so it is easier to read and understand. I also changed some of the websites to source the parts. This is because Mouser shipping is expensive to my country (New Zealand), but they allow free shipping if you spend over $50, so I tried to source as many items as possible from Mouser. I was able to source the DAC, AMP, Headphone Jack, MCU, Potentiometer, and Rotary Encoder from Mouser and maybe more in the future. I've tried to source the buttons, switches, and OLED screens from Mouser, but there weren't any good options that I liked and they were too expensive. 

https://nz.mouser.com/ProductDetail/Alps-Alpine/EC11E18244A5?qs=seHrhfPpLDydI9KuruJHhA%3D%3D
https://nz.mouser.com/ProductDetail/Same-Sky/PTN091-H50115K1A?qs=IKkN%2F947nfAyOT2cVMxFFA%3D%3D

<img width="300" alt="Screenshot 2025-06-11 at 8 13 15 PM" src="https://github.com/user-attachments/assets/46923e75-e0a7-4033-abb0-986c685fc835" />
<img width="800" alt="Screenshot 2025-06-11 at 8 24 27 PM" src="https://github.com/user-attachments/assets/829590b6-f220-461a-8f86-4893c1a4d75a" />

Time spent: 3 hours
---

# June 11

### Buttons + Switches

I searched for the buttons for my project. I wanted buttons that were sleek and smooth while still being high quality. I searched for a long time on Aliexpress for the right switches that met my expectations, and I found a nice option. These buttons were exactly what I was looking for, but it is quite expensive compared to others, and due to the amount I needed (3). 
I need a separate 'button' as a power button, so I wanted to use a switch for my power button. I looked for a large switch, but most of the switches on Aliexpress were too small. Luckily, I found a large switch that was perfect for my power switch.

<img width="400" alt="Screenshot 2025-06-12 at 8 27 15 PM" src="https://github.com/user-attachments/assets/abf72d59-bc73-4cc0-a893-d1900098b3c6" />
<img width="400" alt="Screenshot 2025-06-12 at 8 27 22 PM" src="https://github.com/user-attachments/assets/a466a519-4182-4c1a-a32e-79200c7bf756" />

### Battery

This was hard for me because I didn't know where to buy it. I ended up having to source the battery from Aliexpress, which, even tho I didn't trust it, I didn't have any other choice. I ended up choosing a 3000 mAh LiPo 3.7V battery from a random Aliexpress store (which I still don't trust). Hopefully, I can change it later on, but at this moment, I'll keep it for now.

<img width="400" alt="Screenshot 2025-06-12 at 8 27 30 PM" src="https://github.com/user-attachments/assets/e2e1f05f-a3f5-4013-a43c-ed77984b6682" />

Time spent: 3 hours
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

Time spent: 3 hours
---

# June 13

### Resistors + Capacitors
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

Time spent: 4 hours
---

# June 14

### Capacitors
I went through the capacitors I chose and I realised that I didn't have enough types of capacitors for my parts. I looked through and I found a bunch of different types of capacitors that I could use, and with the right application of said capacitors. I also made sure that the capacitors were alright with my parts, but through this, I also rethought my decision on my battery from Aliexpress, and I found another option, but I wasn't sure about the laws in shipping to my country (NZ).

https://www.digikey.co.nz/en/products/detail/kemet/C320C104K5R5TA7305/12701231
https://www.digikey.co.nz/en/products/detail/cornell-dubilier-knowles/336CKE050M/6141081

<img width="400" alt="Screenshot 2025-06-14 at 6 54 36 PM" src="https://github.com/user-attachments/assets/f4711128-e0d0-42de-b594-482553d73d94" />
<img width="400" alt="Screenshot 2025-06-14 at 6 54 43 PM" src="https://github.com/user-attachments/assets/bbc23ff9-bdf7-41dd-99ab-cd11a27ecfca" />

### BOM Sheet Revamp
I updated my BOM sheet to have the updated location of DigiKey and the OLED screen that I previously changed. I also fixed the mix-up with the different Aliexpress links from when I accidentally mixed them up. At this point, looking at the price, I wonder if the reviews would accept this, given how expensive it is.

<img width="800" alt="Screenshot 2025-06-14 at 7 17 53 PM" src="https://github.com/user-attachments/assets/637b1b63-d4ba-4ca7-b3cc-9424705c91dd" />

### Thoughts 
Today I decided I should have a thoughts section where I give my thoughts about what I've done, and just curious things I'm thinking of.

 Today's one is 'WHY DOES IT TAKE SO LONG TO SOURCE PARTS'.

I also thought about how I was going to show how the parts are going to be connected, since some parts would be on the case and not the PCB.


Time spent: 3 hours
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
Another easy wiring job was the LEDs. The LEDs were simple due to my understanding of how the LEDs work and how they should be labelled from previous projects. I placed the LED pin on a random GPIO (which I later found out was a bad idea) and moved on to the next component.

### DAC + AMP
I focused on one part at a time, this being the DAC. I looked into the data sheet of the DAC and found the description of each pin and connected some of the obvious ones. I did the same to the AMP, but when looking at the pins, I realised that there wasn't a positive input for the audio. This really stumped me, so I wanted to look into the data sheet of the AMP and found that the 14-pin (the one I was using) didn't even include any positive audio inputs. I asked [@Ryan Green](https://hackclub.slack.com/team/U090854913L) about it since he helped me pick out the AMP, and he was surprised about the AMP not including the positive inputs. At this point, I decided to find a different AMP, this time being a 16-pin header.

https://www.ti.com/lit/ds/symlink/pcm5102a.pdf?HQS=dis-dk-null-digikeymode-dsf-pf-null-wwe&ts=1750061065007&ref_url=https%253A%252F%252Fwww.ti.com%252Fgeneral%252Fdocs%252Fsuppproductinfo.tsp%253FdistId%253D10%2526gotoUrl%253Dhttps%253A%252F%252Fwww.ti.com%252Flit%252Fgpn%252Fpcm5102a

https://www.ti.com/general/docs/suppproductinfo.tsp?distId=10&gotoUrl=https%3A%2F%2Fwww.ti.com%2Flit%2Fgpn%2Ftpa6139a2

<img width="300" alt="Screenshot 2025-06-16 at 8 18 07 PM" src="https://github.com/user-attachments/assets/c408e8ea-ac56-4457-bdbf-81220f48c226" />
<img width="400" alt="Screenshot 2025-06-16 at 5 49 53 PM" src="https://github.com/user-attachments/assets/0a53159b-6513-465f-b113-4aef31bbcd53" />
<img width="500" alt="Screenshot 2025-06-16 at 7 58 48 PM" src="https://github.com/user-attachments/assets/050e9057-1fc0-4ed1-a28f-01f9803e582c" />

### Thought
I have to find a new AMP that has 16 pins or at least has a positive input pin, unlike the one I was using. 

I figured out how to connect the components to the PCB that are in the case, yay. 

Still trying to figure out what all the pins mean.

Time spent: 4 hours
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

Time spent: 3
---

# June 17

### AMP
I did my research on the new AMP, and I found a great choice after quickly adding the specs I wanted. I chose the MAX9722AEUE+ due to it being a 16 pin (actually with a +input left and right), pin extruding outwards for easy soldering access and compatibility with the potentiometer I chose. With this, I got the files of the schematic and footprint and imported it into the Kicad. 

https://www.digikey.co.nz/en/products/detail/analog-devices-inc-maxim-integrated/MAX9722AEUE/1495288

<img width="1221" alt="Screenshot 2025-06-18 at 4 19 16 PM" src="https://github.com/user-attachments/assets/ff926d70-440e-4bd7-9cd6-117f3281782d" />

### Schematics
Today, I did a little bit of research on the DAC and AMP pins, and I connected only a few of them after getting tired.

<img width="326" alt="Screenshot 2025-06-18 at 4 18 37 PM" src="https://github.com/user-attachments/assets/52a7b6bf-c556-4400-9dcd-dba3f94455e7" />

### Thoughts 
Technically, at around 11 pm I sent out a message on Slack asking for help with the wiring (because I knew it was terrible) and I did get a response, but it was at midnight, so I'm going to refer it as tomorrows work.

Time spent: 1 hour
---

June 20

### Schematics 

### DAC 
I found out from a person on Slack that the data sheet I had with the description of the part I was using had a part where it showed the schematics of the wiring of most components. This increased my productivity by 7-fold. The DAC was way easier to wire due to the design on the data sheet. There were a few things I had to change with the potentiometer being included as an analog device, but later on, I configured it with the potentiometer.

<img width="600" alt="Screenshot 2025-06-21 at 12 13 24 AM" src="https://github.com/user-attachments/assets/fea33609-dd31-4320-9f45-19b3ad5383ad" />
<img width="600" alt="Screenshot 2025-06-21 at 12 13 42 AM" src="https://github.com/user-attachments/assets/b462c1f7-2d82-4954-b57a-2e6f55ac09ac" />

### AMP
With the newfound knowledge of the schematic diagram on the data sheet, I was able to quickly finish the AMP wiring. The AMP diagram also included the schematics with a headphone jack, which helped a lot since I was using a headphone jack. There was also a lot of confusion with earth and ground pins, but after researching, I just used ground pins as ever pin. 

<img width="472" alt="Screenshot 2025-06-21 at 12 18 14 AM" src="https://github.com/user-attachments/assets/b201d8d4-40ee-442b-84ed-841267b6ce6e" />
<img width="300" alt="Screenshot 2025-06-21 at 12 25 20 AM" src="https://github.com/user-attachments/assets/0196e24c-16c1-4dc4-92e7-9a22b202297a" />

### Rotary Encoder + OLED screen + Headphone Jack
This is just a combination of a bunch of parts because they were really simple to do. The Rotary encoder was simple, I just copied what I did for my Hackpad. The OLED screen was a bit different when I think I needed a resistor and the data pins to connect them to the power pin, but I'm not really sure. The Headphone jack was also self-explanatory, with the AMP having clear directions on how to use it. The only difficulty with the headphone jack was making sure the pins were the correct ones, but this was simple to figure out by double-checking the data sheet of the headphone jack.

<img width="300" alt="Screenshot 2025-06-21 at 12 36 11 AM" src="https://github.com/user-attachments/assets/73e11acf-16a8-49bd-88ae-ac2d33aaa009" />

### Thoughts
This was the first day I did work outside my house/city. 

At the moment, I am on a short holiday, relaxing with my family, but I was still able to get some awesome work done. 

Time spent: 5 hours
---

# June 21

### Schematics

### Potentiometer
As said with the DAC, I was going to add the potentiometer directly to the DAC. This would make the connection better as well as more responsive and stable. Sadly, if there is a problem with it, there are minimal solutions for this. I connected the potentiometer between both the outputs for the DAC and the Input of the AMP. Note, I changed the potentiometer to be a stereo potentiometer, so when the output of the DAC reaches it, the potentiometer won't change it to be a mono input for the AMP.

<img width="300" alt="Screenshot 2025-06-22 at 3 54 01 PM" src="https://github.com/user-attachments/assets/26167968-9c22-4b7b-b0fe-566723d6454a" />

### Switches
I use 3 buttons and 1 switch for my metronome. For the 3 buttons, I used SW_PUSH since the buttons were momentary. I use a SPST for the switch since the switch is a SPST or toggle switch. This was very simple due to me doing the Hackpad before this, and I understood how to use switches and buttons. 

<img width="300" alt="Screenshot 2025-06-22 at 4 04 21 PM" src="https://github.com/user-attachments/assets/38676dc3-fed5-4121-9316-2f06e319d057" />

### Footprints
For each component, I had to assign them a footprint. This was again very simple due to the schematics including a file of the footprints, which made it very easy. The hardest part was to figure out the footprints of the connectors for the components on the case. This was solved by finding out the variables of the labels for the footprints.

<img width="300" alt="Screenshot 2025-06-22 at 4 04 50 PM" src="https://github.com/user-attachments/assets/e856782e-2466-4dbe-ab84-5ea604593c10" />

### MCU (Micro-Controller Unit)
For the MCU I slowly updated the schematics for it as I wired each component. This ended up building the MCU wiring looking like this.
<img width="751" alt="Screenshot 2025-06-22 at 4 05 29 PM" src="https://github.com/user-attachments/assets/1608b20a-b5c4-4770-a2ce-e8ff26bdba80" />

### Thoughts
I've now down the schematics parts of the project and I am now moving on to the PCB editor. 

I sent the schematics to the others, and to be honest wasn't much help by they said it looked good. 

Time spent: 4 hours
---

# June 22

### BOM
I had to update the BOM because I added a bunch of different capacitors and resistors, as well as change the potentiometer. This is to track the amount everything is costing and because to track what component I'm using for my project. Note, shipping and aliexpress prices might be wrong due to it changing a lot, and shipping is confusing at the moment.

<img width="500" alt="Screenshot 2025-06-23 at 4 15 10 PM" src="https://github.com/user-attachments/assets/cbb4e3b5-a4d3-4c42-9055-ae181f8b00d5" />

## BOM Updates

### Capacitors
For the project, I'm using ceramic capacitors with 0.1 uF, 1 uF, 2.2 uF, 10 uF and electrolytic capacitors with 100 uF. I found all these capacitors on Digikey and chose them due to the schematic diagram from each component.

### Resistors
I use only one type of resistor, that being a 470-ohm capacitor. This is due to the data sheet recommending it for the component. 

<img width="500" alt="Screenshot 2025-06-23 at 6 37 07 PM" src="https://github.com/user-attachments/assets/bcb27bd0-3441-4f52-ad73-da6a7a8e6c28" />

### AMP
I found out midway from doing my schematics that the recommended AMP from [@Ryan Green](https://hackclub.slack.com/team/U090854913L) didn't have a +INPUT pin for both left and right channel. This was solved by finding another AMP, which I updated in the BOM

<img width="500" alt="Screenshot 2025-06-23 at 6 37 31 PM" src="https://github.com/user-attachments/assets/a4d6812e-a220-40e0-971c-c9e0fdf6b835" />

### PCB Editor
After I finished the schematics for the metronome, I moved on to the PCB layout. This is how each component would connect in real life and what the PCB would actually look like. This process made me rethink what the metronome device would actually look like. Before I had an image of what it would look like, but after seeing the size of my components, I realised that it wouldn't actually fit in my tiny form factor that I was thinking of having for my project. This caused me to sit down and rethink how I was going to position my components to make sure it looks nice.

<img width="400" alt="Screenshot 2025-06-23 at 6 41 29 PM" src="https://github.com/user-attachments/assets/d3bb8e52-b59f-478a-8ff0-e8a6081ace94" />

### OLED Screen
Through my time rethinking about the looks of the PCB and project I realised that my OLED screen was way too big (well not way too big but just a bit to big). This made me go back into researching OLED screens and thats where I found on on Aliexpress which was 1.3 inches and looked very nice in my opinion. 

<img width="500" alt="Screenshot 2025-06-23 at 6 42 22 PM" src="https://github.com/user-attachments/assets/edea5cdd-2b09-4a8e-84da-7b967f90ee77" />

### Thoughts
For today and a bit of yesterday's journal I used a code server for the journeying due to the SOM (summer of making) and me requiring to log hours which is why I'm doing it in a code server so it can track the hours. I'm unsure if it works on the Github site but better safe than sorry (or whatever the saying is ). It is also going to be a struggle with importing screenshots of my project but I'm still figuring it out. 

I am also wondering how I am able to install the battery. Installing the battery requires connecting it to the +BAT and -BAT pin on the MCU. The problem is that the MCU will be on the pcb it would be cover the pins since the said pins are on the back side. 

Time spent: 6 hours 
---
 # June 23

 ### PCB Editor 
 For today I spent a lot of time figuring the best position to put all my input components which are; potentiometer, rotary knob, switch, buttons and head phone jack. For this I took a long time exactly measuring each component location until I realised I could of just used a temporary block which exactly measures each space between components. With this temporary block my productivity increase by a lot. I positioned my components relatively where I wanted them to be which was a really bad idea, which by the end of the day I realised that I should redo it. 

 There was many problem with this. When making my schematics, it turned the power pins into ground pins which really stumped me. There was also problems with the capacitors (smart lines? or something) choosing anywhere to go. Including the fact that my conscious made me think that with all my hard work the project wouldn't even work, This made me question my self. There was many problem which I didn't have enough experience and intelligence to fix. I realised that I jumped too high than I could reach. 
 
 ### Thoughts
 Compared to the Hackpad that I did before this, this was way more harder than I expected. Even though I learnt many things at this point, like sourcing parts, finding footprints, using data sheets, I still couldn't figure it out. 

 I texted my friend about postponing the project and working on a new one (planning to do a simple macro pad) and to be honest he wasn't much help. He was more focused on me starting on his case for his own project. So I went to sleep to rethink the project

Time spent: 2 hours
 ---
 # June 24

 ### Features

 For my friend I needed to tell my friend what features each component would have and for him to code (I don't like to code and don't know how to code).

 List might have changed due to me changing features and deleting some components (I am still changing and switching components (Mainly capacitors and resistors)).

 - Potentiometer - Controls volume directly by connecting between DAC and AMP.
 - Rotary Encoder - Controls the BPM amount with how much you twist. 
 - Power Switch - Controls the main power and turns on and off the power when switching it.
 - Button 1 - This start and stops the BPM, simple momentary switch.
 - Button 2 - Enables and changes the BPM with presets. You have to press the button to switch between presets. Potentially a feature to adjust the BPM amount of a preset by press multiple switch or something.
 - OLED screen - The OLED screen shows: 
\
BPM (large middle character)
\
Volume (Out of 100, on the left side as a rectangular bar with the percentage on the bottom)
\
Preset Indicator (3 boxes showing the prest BPM amount while having an indicator like a line under what preset is selected at the current moment. Located on the right hand side)
\
Time signature (Display what the time signature is. Located on the bottom beneath the BPM)

- Headphone jack - The only way to listen to the metronome 

### Schematics
After th trouble with the pcb the other day I knew I had to change something. There were a lot of errors internally in the schematics which I needed to fix just incase it messes up my PCB. For context, my friend showed my Github education where you get many features available to you, one of the being Github Copilot. I wanted to see if Github Copilot could accurately look through my schematics and spot out mistakes and solutions. Let me just say, it worked. I was shown a few problems with my design (most being recommendations) and instruction for how to fix it. Because I was using a AI, I didn't want to just follow the instructions, I wanted to understand how it works and why. 

<img width="500" alt="Screenshot 2025-06-24 at 9 55 49 PM" src="https://github.com/user-attachments/assets/0ff5b12f-e610-404d-a1c2-c2cb49b1d90d" />

#### Example
One of the problems were that the OLED screen didn't have pull-up resistors. This confused me because on the Hackpad Oled screens, they didn't include any resistors of any kind. I found out that pull up resistors are used for pulling power from the device because I2C draw low power, this mean the I2C lines could float, which it bad.

### Thoughts
I'm still changing a lot of the components for my project so the most acuate list for my features would be on the read me. 

After fixing the schematics with Github Copilot, and my friend helping me understand some of my problems with the pcb, I decided to continue this project and hopefully finished between the school holidays (context, NZ school holidays: 30th June - 13th July).

I have to update so much things due to me changing components its not funny.

This one is even more important but I don't know where to put it but, I decided to not use a battery. Due to my inexperience, using the plug is the best way for me to make the project to make it simpler and for me to not worry about anything else. This also reminds me about my LED which I think I have mentioned but I'll just mention it again, I will be remove the LED's for simplicity for the PCB and case design.

Time spent: 3 hours
---

# June 25

### Schematics 
I fixes some errors with my schematics. These changes were most of the errors that Github Copilot found like pull up resistors for the oled screen and grounding pins.

<img width="500" alt="Screenshot 2025-06-24 at 9 55 49 PM" src="https://github.com/user-attachments/assets/e3557424-a7b7-4bc8-85ac-5e3999135e00" />

### PCB Editor
I redid the pcb, deleting the previous version and organising the location of components and wires for every pin. I made sure to label each component for it to be easier to read and solder in the future. In the pcb editor I had to manually organise the each components like the capacitors and resistors due to the smart lines working differently. 

<img width="578" alt="Screenshot 2025-06-25 at 9 55 54 PM" src="https://github.com/user-attachments/assets/e56d4ea1-3346-41e3-b3a6-9f37c63f8208" />

### Capacitor + Resistors
While I fixed the schematics, I changed a lot of the capacitors and resistors for my project. This was due to simplicity with the data sheets and figuring out unlabeled components. Because it is difficult to properly show the different type of resistors and capacitors, I would just been putting it in the BOM in the Read.me file. 

### Thoughts
I think I have finished picking out my components for my project but I would still need other things like wires, connectors and screw etc. 

Even though this is not part of this project but my hackpad kit arrived which made me happy. Sadly my solder is still shipping and I don't have knobs or case for my pad so I would probably need to print them some how. 

Time spent: 1 hours
---

# June 26

### PCB Editor
Today I'd consider was very productive even tho I didn't get much time to work on the PCB. I think I finished every connection on the PCB for every component. I made sure to connect all the power pins individually to the MCU power which was starting to get difficult due to the amount of wires in on the PCB at this point. Then I created the ground fill zone which was quite easy due to the simplicity of what you need to do. 

Basically you just need outline an area for where you want to the ground zone to be and every ground pin inside the zone will be connected. However, after doing this, I found out that the ground pins were acting strange. They suddenly turned into DGND (Digital Ground)
which made everything worse. This forced me to redo the ground pins on every components on the schematics, which was basically just deleting them and replacing them. 

<img width="400" alt="Screenshot 2025-06-26 at 11 24 07 PM" src="https://github.com/user-attachments/assets/7366cad4-3192-41d3-b24b-33ed2272aeef" />

##### DRC
After I finished all of this I really thought that I was done with the PCB and I could start on the case design. Sadly, I forgot about the most dreadful part, DRC (Design Rule Check). The second I pressed DRC my heart dropped. I has SO MANY ERRORS. 

I found some simple ones like me forgetting to connect come pins and some wires left unconnected which was pretty easy to fix. Then there came the difficult ones. Some of them I just deleted them a redid them and some of the actually worked, that surprised me. Then there were the annoying ones. 

There were ones called, Thermal relief connection which is such a stupid error. This is because the reason that the error pops up is because the pin only has 2 connections to the ground zone. The reason this is stupid is because the pin doesn't have any more space to have a second connection and I can't do anything about it.

The next one is called Solder mask aperture bridge items with different nets. To be honest I don't actually knw what it mean or what the problem even is. I read the Kicad documents and it said that it was a problem with the solder mask or something. All I understood was that I don't really thing it was my problem. So ended up asking Highway for any help about it, but after previous 'help' messages, I doubt I would actually get any help.

<img width="400" alt="Screenshot 2025-06-26 at 11 25 37 PM" src="https://github.com/user-attachments/assets/43a566b7-30b5-4902-ab02-d61f44017515" />

### BOM
I fixed some issues with the BOM, like old information and some old components I'm not using.

<img width="5000" alt="Screenshot 2025-06-26 at 11 26 20 PM" src="https://github.com/user-attachments/assets/56a16059-1e87-48d4-bca3-180ff5ba7cc8" />

### Notes
During the project I put all my links of each component in my notes so it's easier to access on the fly. Due to this I had to update everything in my notes, which was a bit annoying but I did it anyway.

<img width="500" alt="Screenshot 2025-06-26 at 11 27 29 PM" src="https://github.com/user-attachments/assets/a0945b21-afcf-4196-a640-aa8a5b097286" />

### Thoughts
Extremely productive day. I got a lot done and even socialised with my friends and went out for a workshop for drum kit. 

I am still having difficulties with the DRC which bugs me. 

I talked with my friend and I'm planning to order smaller tips for my pinecil soldering iron, which in fact I haven't even gotten yet for my hackpad so.... yikes. Also soldering tweezers.

Time spent: 2 hours
---

### June 27 

### PCB Editor
Today was a very slow day. I didn't get to do much due to the error which prevented me from progressing. I asked help on highway and I did get an answer, but it only helped for a few of the errors and majority of the errors were still unfixable. I tried using all methods I could think of to find the solutions. I researched a bunch. On the Kicad document, the Xiao wiki, Kicad forums, yet there were no solutions. I even tried asking Github Copilot for help, but all methods failed. I tried to find the problem in this and I think I found it. It has something to do with the front mask ans back mask not being properly aligned with the footprint which causes errors I think. Another error which I think I found the cause, was that the MCU net points are not labeled properly. I ended up asking another question on Highway in luck for a solution.

<img width="400" alt="Screenshot 2025-06-27 at 7 22 41 PM" src="https://github.com/user-attachments/assets/8720ae84-2f16-4af5-9301-ae825c5289a0" />
<img width="400" alt="Screenshot 2025-06-27 at 7 22 50 PM" src="https://github.com/user-attachments/assets/87d07f6a-9c96-46fa-b467-ae7c2468979a" />

### Thoughts
The DRC has lowed my motivation to work on the project. Hopefully someone can respond and help me with the errors. 

If none respond or doesn't respond with helpful information, I might just directly dm someone who could help.

My school holidays has started so 24/7 grind baby.

Time spent: 2 hours 
---

# June 28

### PCB Editor
Recently I have been stuck with the DRC errors for my PCB board. Luckily, my respond to Person was been successful and he is currently reviewing my project. I am hoping that he is able to help my with these errors so I can continue on with my PCB.

<img width="440" alt="Screenshot 2025-06-28 at 11 01 46 PM" src="https://github.com/user-attachments/assets/afb6b6fc-6307-4800-8f01-662aa8199e57" />

### Aliexpress
While I was waiting for the response from Person, I decided to look for the last few parts I would need for my project. I looked at many things likes, wires, connectors, screws, and some other things. These are just some items that will be needed for the project and to connected everything together. I fond many items and were able to get the most cheapest ones for it. 

<img width="369" alt="Screenshot 2025-06-28 at 11 01 03 PM" src="https://github.com/user-attachments/assets/3692a07b-7f61-46f8-8558-cd2af2972427" />

### BOM
I updated the BOM with the new items I found on Aliexpress. This made my realised how expensive my BOM was and it makes me wonder if they would even accept it. I included a micro solder tip set because the project includes many surface mount components that even my friend thinks is really difficult to solder. I also included a soldering tweezers set which is also helpful for the surface mounted components.

<img width="500" alt="Screenshot 2025-06-28 at 10 54 08 PM" src="https://github.com/user-attachments/assets/ae36c43b-39ec-406b-b866-6f79348d0d61" />

### Thoughts 
This project is costing a lot more than I anticipated and I am just hoping that they would accept it. 

Time spent: 2 hours
---

# June 30

### PCB Editor

##### DRC Errors
I got a response from [@Person20020](https://hackclub.slack.com/team/U07QNKS5SKA) and he showed me exactly how to fix the DRC errors. He found out that it was an error with the footprint of the Xiao ESP32 S3 Plus where the masking points were unassigned and weren't registering as any net. He helped me solve this issue by showing me how to change the mask in the footprint editor. Once again he has helped me solve my problems and is very helpful with PCB problems.

<img width="300" alt="Screenshot 2025-06-30 at 11 59 19 PM" src="https://github.com/user-attachments/assets/05be5f3f-2ca8-4cd0-849d-9a8555757e8b" />

##### Finishes
I made some last few touches on the PCB face. I added a bunch off labels to the PCB stating the name of the project, Github repo and my name/username. I also made a few changes to the pcb silk screen component location to even them out. 

<img width="500" alt="Screenshot 2025-06-30 at 9 26 36 PM" src="https://github.com/user-attachments/assets/c4721e2a-b23b-486c-adab-66e5dc01ba25" />

### Fusion
After finishing my PCB (YAY) I moved on to the case design. I started with sketching the design of the case with the measurements I used with the PCB in the PCB editor. Using fusions 360, I created a sketch which is close to what I have thought in mind. 

<img width="300" alt="Screenshot 2025-06-30 at 11 14 02 PM" src="https://github.com/user-attachments/assets/554e7bdd-4556-4b24-87b6-367b58c47202" />

(In picture on top this is the explanation.

- Biggest rectangle in middle is the base or inside.
- Next rectangle is the side wall of the case.
- Next rectangle is the cool design im thinking of.
- Circles, holes for screw (used hackpad measurements)
- Small rectangle is the OLED screen.)

After this, I extruded every part of the sketch by the right amount. I would be creating 2 parts, 1 being the base and the other being the top. Other then some holes and maybe some text, these 2 parts will pretty much be identical.

<img width="500" alt="Screenshot 2025-06-30 at 9 25 55 PM" src="https://github.com/user-attachments/assets/f3d074f2-c7c1-429e-9e87-ef344d285f4b" />

### Thoughts 
I ACTUALLY FIXED AND FINISHED THE PCB. I was so worried that I was stuck with the DRC errors for the PCB. I'm so excited that I was actually able to finish it.

That you so much [@Person20020](https://hackclub.slack.com/team/U07QNKS5SKA) for helping me with the DRC errors.

This work was over today and a tiny bit of yesterdays work.

I talked with my friend about the pinecil tips. We were chatting about buying tips from aliexpress. I didn't really trust it because it was from Aliexpress, what do you expect. Even though it was much more cheaper than the official version, I still didn't trust it fully and I still think that the official version is better. I'd recon if I can get the official and more expensive one approved, then I'll just use that one but if they say its too expansive Ill just use the Aliexpress one.

I'm taking more breaks since it is the school holidays and I want to relax and play with friends for a bit more.

Time spent: 2 hours
---

# July 1

### Fusion
Now that I have finally finished the PCB I focused of the case design for my project. This was important since this is that my final end result would look like. After yesterday's work I had to redo the entire extrusion because of some calculation errors with the height of the case and screen. I decided to parsley design the screen part of the case due to it being less informative about its size. This took a lot of trial and error and lots of going back and forth with the measurements. The holes for the rotary encoder and potentiometer were really difficult to get right due to there being little to no information about the measurements from left or right to the knob which annoys me. I ended up just measuring and estimating a rotary encoder in real life which work a bit but I think it might be off by a bit but never or less I continued on. I noted to my self that the case might not be right and I'll just fix it later on.

<img width="400" alt="Screenshot 2025-07-02 at 8 26 19 AM" src="https://github.com/user-attachments/assets/acc9a66e-aaf5-4fe6-bdfa-e52bd007afbc" />

### Thoughts 
Fusion doesn't track time or track time well so I'm not getting much hours off this. I'm mainly getting out the time spend writing in this journal but with simple explanations like this day was really quick to type.

Time spent: 2 hours
---

# July 2

### Fusion
Today I continued on the CAD model on fusion. After polishing the main part of the case I imported the PCB model so I can understand and make sure the all the components can fit inside. The PCB was the main components and I evenly slotted it in the middle of my case. Afterwards I imported the Xiao ESP32 S3 Plus model to create and make sure the hole for the cable is correct. I also imported the headphone jack to make a hole for it too but sadly the potentiometer didn't have a cad model to use properly. Instead, I manually measure all the specs of the potentiometer and created a hole that aligned wait the measurements. I did similarly with the rotary encoder due to it not being attacked to the pcb but the case. I created a hole and indent for the OLED screen, which I don't think is correct due to the uninformative measurements given by aliexpress. After that I created the holes for the buttons but this game me a problem. THe buttons were too big and close to the pcb.

<img width="500" alt="Screenshot 2025-07-02 at 8 26 19 AM" src="https://github.com/user-attachments/assets/a2303bed-8226-4a50-a11e-aef0fe43716c" />
<img width="500" alt="Screenshot 2025-07-02 at 11 15 18 PM" src="https://github.com/user-attachments/assets/03e6d505-f80f-4288-a2c4-c81ccee33b40" />
<img width="500" alt="Screenshot 2025-07-02 at 11 15 27 PM" src="https://github.com/user-attachments/assets/d627699d-d6f4-4a9e-909f-2baa7972ebcb" />
<img width="500" alt="Screenshot 2025-07-02 at 11 15 36 PM" src="https://github.com/user-attachments/assets/d42548f7-22b9-483d-84fc-dac6354309ed" />

### Thoughts
I got my soldering iron from my hackpad and so I soldered a few components. Now I need to wait for the case.

I have to solve the problem with the buttons being too close to the PCB. 

I need to complete it soon because aliexpress has a sale which would be soo good.

Time spent: 3 hours
---

# July 3

### Fusion
Today I finished the CAD model of the case. The solution to my problem with the buttons were to cut a hole in the PCB. Not the best solutions but it works. Due to this, I had to redo the PCB model that I already had. In this I think I messed up the location of the button holes because the buttons weren't even on each side, but using the PCB model, I was aligned. I Fixed the MCU location (after deleting the previous PCB model it fell down onto the case, I don't know why) and corrected the plug's location. I polished everything and made sure it look good and great. 

<img width="500" alt="Screenshot 2025-07-03 at 12 25 30 PM" src="https://github.com/user-attachments/assets/e1453b98-fecb-4370-a23c-691f3f61fac7" />
<img width="500" alt="Screenshot 2025-07-03 at 12 25 36 PM" src="https://github.com/user-attachments/assets/c3690110-f119-43b4-ae51-335012507753" />
<img width="500" alt="Screenshot 2025-07-03 at 12 25 58 PM" src="https://github.com/user-attachments/assets/aec64761-8695-44db-9a6d-5f00e16d2206" />

### Kicad Editor
Due to me needing to change the PCB shape for the CAd model, I had to change the PCB shape. This part was a bit difficult due to me learning more about edge cutting. I basically remade the board shape because I didn't know how to make a cut in the board. Due to this, I had to reposition my title, name and repo in the corner. While I was changing the PCB shape, I also changed the pins of the button to make sure they are even. 

### BOM Update
After I finished the PCB and case design, I included some last times to time BOM and switched some items. I added stuff like foam to hold up the PCB and nano tape to hopefully hold up the OLED screen. I removed the screws that I was originally going to use but I realised that I couldn't due to the thin part of the case for the OLED screen. I also included a micro soldering stand and usb-c for my soldering iron after struggling with soldering my last project (Hackpad).

<img width="500" alt="Screenshot 2025-07-03 at 10 42 37 AM" src="https://github.com/user-attachments/assets/5588556d-77a2-4789-af30-8cabe55c1229" />

### BOM Update
After I finished the PCB and case design, I included some last touchs to time BOM and switched some items. I added stuff like foam to hold up the PCB and nano tape to hopefully hold up the OLED screen. I removed the screws that I was originally going to use but I realised that I couldn't due to the thin part of the case for the OLED screen. I also included a micro soldering stand and usb-c for my soldering iron after struggling with soldering my last project (Hackpad).

<img width="300" alt="Screenshot 2025-07-03 at 9 43 24 PM" src="https://github.com/user-attachments/assets/470f4a66-32b0-4db9-b4ce-ab50efde38ed" />
>>>>>>> de66846e65b4969b4935cf65a2a9b8242352f6ec

### Thoughts
After looking at the case, I realised that my potentiometer might not be able to fit in my case. The potentiometer is a big too short where the knob won't be able to through the case. 

I'm thinking of changing the potentiometer, which is a lot of work to be done. I'm not almost done D:

Time spent: 4 hours 
---

# July 4

### Fusion
Today I think i finished the case. I double checked every component was correct and matched up with the dimensions of the case. I checked the different items I was using like screw to make sure they would even fit (had a problem with that one). I polished the case adding some text and cleaned up some edge. After finishing it, I copied the case into a new file which would be called the production file and showed what needed to be printed. 

<img width="300" alt="Screenshot 2025-07-04 at 5 19 01 PM" src="https://github.com/user-attachments/assets/f44aa7a2-06e6-4711-bc1c-81997b296c20" />

### Final BOM Update (Hopefully)
I added my last items to my BOM (hopefully) and updated the prices of many Aliexpress items. This was really annoy because aliexpress's prices fluctuates a lot which is annoying when creating a BOM. 


### Repo Update
To submit the project, I needed to create many things in my repo. I created my README.md file and filled in the necessary information. I started creating the files and folders for the CAD and PCB showcase files and production files. 


### Thoughts 
I finally finished the case and the final PCB design so I'm basically finishing up the project's repo. 

I also made a case for my friend which took a chuck of my time. 

I really wanted to finish this project and spent an uncomfortable amount of time on it today. I'm at the home stretch and I just want to be free.... and move on to a new project.

There are problems with committing from the code server which I don't understand so the last few updates might be really weird.

P.S. This is me the next day importing the pictures (due to my power being wack due to a thunderstorm) and I realised I didn't take pictures before updating them even more.

Time spent: 6 hours
---
### July 5

### BOM Actual Final
I finally finished my last BOM changes, and I finished the BOM on the GitHub readme. I polished the BOM sheet and exported it as a CSV file as needed. 

<img width="500" alt="Screenshot 2025-07-05 at 5 21 01 PM" src="https://github.com/user-attachments/assets/c1d59efe-007b-4faa-9a1d-52f0bc480533" />

### REPO FINISH
Submitting the project requires a lot to be submitted. I double-checked that everything was complete and finished up the journal for the last day (this :D). I don't really know how to finish this part because as I do stuff, I need to add it to the journal, and I'm submitting the journal, so it gets confusing.

### Thoughts
This is the last journal, and I'm submitting this. Good luck to me waiting for this to get approved.

Also, I didn't really write much in the journal because I mainly wanted this to be finished and sent for approval.

P.S. I wrote this around 5:30 pm, and I sent a message on Slack to look over my repo, and it changed a lot, so I'm actually not finished.

Time spent (till 5:30 pm): 1 hours
---

### July 6 

### BOM Actual Finish 2
Last night, I sent out a message on the highway for people to look over my repo. I understand that there are already going to be people looking through my repo to see if it gets passed on to assigned people to review, but I knew if it was denided it would take way longer. I sent out the message, and I got a bunch of feedback back. One of them was a thought that my project might not be a 6 point project. To be fair, I understood that he might have thought that it was a 4-point project, but I did so much work for it. I also got feedback about my BOM and how the capacitors were too expensive as well as my components. This was a long rabbit hole, but in the end I only siwtched the capacitors and resistors form digikey, to capacitor and resaistor kits from Aliexpress. They weren't 'cheaper', but it was way cheaper per piece. Wait, regarding the suggestion with cheaper components, I was told that it was cheaper to buy from Aliexpress, and all compoents form Digikey that I sourced was on Aliexpress. This was probably true, for the most part. Only a few components were even on Aliexpress, and only one of them was cheaper (per piece). I decided not to switch it because I knew it was not worth it cue to the $50 free shipping and reliability. 

<img width="500" alt="Screenshot 2025-07-06 at 3 59 39 PM" src="https://github.com/user-attachments/assets/cc67c2ba-6244-4a7e-8c30-083b5c7adb1c" />

### REPO ACTUALLY FINISHED

This is my last journal and I can safely confirm that I'm acutally finshed. After I finish this log, I am going to send the form for this. I did some last touches, like creating short READMEs for each folder, and updated the main README and BOM. P.S. There is a spelling error in the BOM but I am too lazy to fix just one error.

### Thoughts
Finally, I have finished.

Time spent: 4 hours
---

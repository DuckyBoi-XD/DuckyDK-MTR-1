---
title: "DuckyDK MTR-1"
author: "@DuckyBoi_XD"
description: "A metronome for any type of music practice which you can adjust BPM with knob and preset buttons, and OLED screen for information, a battery for a portable mode and more"
created_at: "2025-06-07"
---

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

Time spent: 12 hours
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

### Buttons + Switches

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

Time spent: 8 hours
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
Another easy wiring job was the LEDs. The LEDs were simple due to my understanding of how the LEDs work and how they should be labelled from previous projects. I placed the LED pin on a random GPIO (which I later found out was a bad idea) and moved on to the next component.

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

### AMP
I did my research on the new AMP, and I found a great choice after quickly adding the specs I wanted. I chose the MAX9722AEUE+ due to it being a 16 pin (actually with a +input left and right), pin extruding outwards for easy soldering access and compatibility with the potentiometer I chose. With this, I got the files of the schematic and footprint and imported it into the Kicad. 

https://www.digikey.co.nz/en/products/detail/analog-devices-inc-maxim-integrated/MAX9722AEUE/1495288

<img width="1221" alt="Screenshot 2025-06-18 at 4 19 16 PM" src="https://github.com/user-attachments/assets/ff926d70-440e-4bd7-9cd6-117f3281782d" />

### Schematics
Today, I did a little bit of research on the DAC and AMP pins, and I connected only a few of them after getting tired.

<img width="326" alt="Screenshot 2025-06-18 at 4 18 37 PM" src="https://github.com/user-attachments/assets/52a7b6bf-c556-4400-9dcd-dba3f94455e7" />

### Thoughts 
Technically, at around 11 pm I sent out a message on Slack asking for help with the wiring (because I knew it was terrible) and I did get a response, but it was at midnight, so I'm going to refer it as tomorrows work.

Time spent: 3 hours
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
This was the first day I did work outside my house/city. At the moment, I am on a short holiday, relaxing with my family, but I was still able to get some awesome work done. 

Time spent: 10 hours
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
I've now down the schematics parts of the project and I am now moving on to the PCB editor. I sent the schematics to the others, and to be honest wasn't much help by they said it looked good. 

Time spent: 9 hours
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

Time spent: 12 hours 
---
 # June 23

 ### PCB Editor 
 For today I spent a lot of time figuring the best position to put all my input components which are; potentiometer, rotary knob, switch, buttons and head phone jack. For this I took a long time exactly measuring each component location until I realised I could of just used a temporary block which exactly measures each space between components. With this temporary block my productivity increase by a lot. I positioned my components relatively where I wanted them to be which was a really bad idea, which by the end of the day I realised that I should redo it. 

 There was many problem with this. When making my schematics, it turned the power pins into ground pins which really stumped me. There was also problems with the capacitors (smart lines? or something) choosing anywhere to go. Including the fact that my conscious made me think that with all my hard work the project wouldn't even work, This made me question my self. There was many problem which I didn't have enough experience and intelligence to fix. I realised that I jumped too high than I could reach. 
 
 ### Thoughts
 Compared to the Hackpad that I did before this, this was way more harder than I expected. Even though I learnt many things at this point, like sourcing parts, finding footprints, using data sheets, I still couldn't figure it out. 

 I texted my friend about postponing the project and working on a new one (planning to do a simple macro pad) and to be honest he wasn't much help. He was more focused on me starting on his case for his own project. So I went to sleep to rethink the project

Time spent: 5 hours
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

Time spent: 6 hours
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

Time spent: 2 hours
---




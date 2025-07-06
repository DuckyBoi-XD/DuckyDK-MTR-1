# DuckyDK-MTR-1

### Description
This is a Metronome device called the DuckyDK MTR-1. This is for musicians, like me, who need a portable metronome that can be used anywhere. It is designed in a compact form to maximize space usage and portability.

## Kicad Schematic
<img width="500" alt="Screenshot 2025-07-05 at 12 15 32 PM" src="https://github.com/user-attachments/assets/f2c3c3cd-cb48-4ade-b3a3-bd41635f7fe4" />

## Kicad PCB
<img width="500" alt="Screenshot 2025-07-05 at 12 15 48 PM" src="https://github.com/user-attachments/assets/ef771269-d041-4825-8337-2ac4c50c05bc" />

## PCB wiring (RED LINES)
<img width="500" alt="Screenshot 2025-07-05 at 12 15 48 PM" src="https://github.com/user-attachments/assets/bd7fd55f-9ef2-4590-bb66-2aebeef9a0f1" />

(I didn't know how to make this look nice.)

## Fusion Case
<img width="500" alt="Screenshot 2025-07-04 at 5 19 01 PM" src="https://github.com/user-attachments/assets/665c3d3e-0bae-4d9c-90e9-277a2d006df4" />

## Fusion Production Case
<img width="500" alt="Screenshot 2025-07-04 at 5 18 35 PM" src="https://github.com/user-attachments/assets/a01da600-e194-4737-8f38-2c91e4207637" />

### Inspiration
This idea was thought of and inspired when I bought a new drum kit which I loved, and I wanted to think of different projects I could make which is connected to my drum kit. One idea that was obvious was to make a custom metronome. This is the result of that idea. Even though devices like laptops can do this, I wanted to make a portable, offline metronome that is not reliant on any device and can be brought along to many places. The price of a drum metronome was also expensive, which I found weird, so I wanted to try to do it myself

**Name**
The name DuckyDK MTR-1 is from many things. **Ducky** comes from my username **Ducky**Boi_XD, **DK** is/comes from **D**rum **K**it or **D**uc**k**. **MTR** comes from **M**etronome, while the **1** indicates that this is the first version of this metronome project.

### Features 
These are the features that are implemented in the DuckyDK MTR-1:
- **Compact Design**: The device is contained in a small, portable, compact case which is custom designed to fit all the necessary components. 

- **Adjustable Tempo/Time signature**: The tempo and time signature can be adjusted to fit the user's needs. The temp can be adjusted by the rotary encoder and the time signature can be adjusted by the internal button on the rotary encoder.

- **Volume Control**: The volume of the metronome can be adjusted but the potentiometer is attached to the case. This the user to adjust their preference for their volume. For example, I play drums which can be quite loud, resulting in the need of a louder metronome.

- **2 Control Buttons**: On the case is 2 buttons controlling 2 important functions of the metronome. The first button is the start or stop mechanism of the metronome. The second button is a preset button. This button contains 3 presets that can be selected and used by pushing the preset button.

- **Info Display**: The device contains an appropriately sized OLED display which contains many necessary information. It contains, a big indicator of the current tempo/BPM in the centre of the screen, a volume level on the right side of the screen as a bar with percentage sign underneath, a 3 boxes which is the preset indicator on the left side of the screen, and lastly, the current time signature located on the bottom of the screen, under the BPM indicator.

- **Headphone Jack**: The device contains a headphone jack which allows the user to connect headphones to the device. This is currently the only way to hear the metronome. This headphone jack also contains a switch when the headphones are connected. This can be changed to do whatever you want.

### BOM (Bill of Materials)

#### NOTE
Aliexpress prices may change, all prices are based of no sales or coupons (except for hot plate), so this is the max price possible, and the final result of the price would be reduced.

(GST) = General sales tax, it's calculated at the last **GST** 
Tax is calculated at the last **TAX**

A few of these items from Digikey are extra components. This is because if I spend more than $50 from digikey, I get free shipping, which is really imporntnad because shipping to my country is expensive. I talked with [@acon](https://hackclub.slack.com/team/U04KEK4TS72) and he said if it is cheaper, then it's ok.

This BOM might have errors and be old, so check the BOM file in repo.

The BOM contains some items that are components that will help a huge amount with this project and could help future projects (Hot plate, small soldering tip, solderer stand and tweezers.

| Component | Quantity | Description | Base Price | Extra Costs | Link | 
|-----------|----------|-------------|------------|-------------|------|
| Xiao ESP32-S3 Plus | 1 | MCU (Microcontroller Unit) (Digikey) | $7.99 | (**GST**) | https://www.digikey.co.nz/en/products/detail/seeed-technology-co-ltd/102010671/26553873 | 
| PCM5102APWR | 1 | DAC (Digital to Analog Converter) (Digikey) | $4.43 | (**GST**) | https://www.digikey.co.nz/en/products/detail/texas-instruments/PCM5102APWR/3727211?s=N4IgTCBcDaIAoGECyBWAjABjAQTgdQCUQBdAXyA |
| MAX9722AEUE+ | 1 | AMP (Audio Amplifier) (Digikey) | $1.52  | (**GST**) | https://www.digikey.co.nz/en/products/detail/analog-devices-inc-maxim-integrated/MAX9722AEUE/1495288 | 
| SJ1-3514N | 1 | 3.5mm Headphone Jack (Digikey) | $1.19  | (**GST**) | https://www.digikey.co.nz/en/products/detail/same-sky-formerly-cui-devices/sj1-3514n/738685 | 
| PTN092-H50115K1A | 1 | Potentiometer (Digikey) | $2.00  | (**GST**) | https://www.digikey.co.nz/en/products/detail/same-sky-formerly-cui-devices/PTN092-H50115K1A/24767692 |
| EC11E18244A5 | 1 | Rotary Encoder (Digikey) | $4.85 | (**GST**) | https://www.digikey.co.nz/en/products/detail/alps-alpine/ec11e18244a5/21721665 |
| 404070001 | 1 | ESD Safe Tweezers (Straight) (Digikey) | $2.50 | (**GST**) | https://www.digikey.co.nz/en/products/detail/seeed-technology-co-ltd/404070001/5488233 |
| 422 | 1 | ESD Safe Tweezers (Curved) (Digikey) | $3.95 | (**GST**) | https://www.digikey.co.nz/en/products/detail/adafruit-industries-llc/422/7241434 |
| 1007-20-1-2000-001-1-TD | 25 feet | Wires | $11.87 | (**GST**) | https://www.digikey.co.nz/en/products/detail/cnc-tech/1007-20-1-2000-001-1-TD/17799227 |
| 20-0600-21 | 2 (20 pins each) | Male pin headers | $7.66 | (**GST**) | https://www.digikey.co.nz/en/products/detail/aries-electronics/20-0600-21/4207162 |
| 97790603211 | 10 | Screws | $2.58 | (**GST**) | https://www.digikey.co.nz/en/products/detail/w%C3%BCrth-elektronik/97790603211/10056392 |
| 97791003111 | 10 | Screws | $2.24 | (**GST**) $7.92 | https://www.digikey.co.nz/en/products/detail/w%C3%BCrth-elektronik/97791003111/10056389 | 
| 1.3 Inch Oled Module Witte Kleur | 1 | OLED screen 4 pin (Aliexpress) | $5.36 | (**TAX**) | https://www.aliexpress.com/item/1005007451015054.html?spm=a2g0o.productlist.main.3.5c94BkFLBkFLwI&algo_pvid=c05ab788-0f62-4cac-8ecf-0ac50b96f1c8&algo_exp_id=c05ab788-0f62-4cac-8ecf-0ac50b96f1c8-2&pdp_ext_f=%7B%22order%22%3A%221408%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%215.36%211.68%21%21%213.15%210.99%21%402103247917505815500323989e2c7f%2112000040806152742%21sea%21NZ%216394433987%21ABX&curPageLogUid=4GgHuLqPJwAs&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Ultra Short Switch | 2 | Buttons No LED 3-6V 16mm black momentary (Aliexpress)| $9.34 | (**TAX**) | https://www.aliexpress.com/item/1005004920346156.html?spm=a2g0o.productlist.main.7.7f7d5f2722dp5N&algo_pvid=88ea1ebf-ed98-4122-ae48-2b34d2cbcef4&algo_exp_id=88ea1ebf-ed98-4122-ae48-2b34d2cbcef4-6&pdp_ext_f=%7B%22order%22%3A%221272%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%214.19%211.70%21%21%2117.53%217.11%21%402103247417506694259818233e29c3%2112000039500055503%21sea%21NZ%216394433987%21ABX&curPageLogUid=AdxbPFQrTg6S&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Hexagon Fine Thread Thin Nuts | 1 M7 (20 pieces) | Nuts for Rotary encoders and Potentiometer (Aliexpress) | $3.84 | (**TAX**) + $5.49 (Shipping) | https://www.aliexpress.com/item/1005006173995318.html?spm=a2g0o.productlist.main.15.7dbd4ebaNansD7&algo_pvid=bbffa5d8-f689-4588-a6f6-ce0996436945&algo_exp_id=bbffa5d8-f689-4588-a6f6-ce0996436945-14&pdp_ext_f=%7B%22order%22%3A%22151%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%211.85%211.39%21%21%217.88%215.91%21%40210308a417510851180067032e73ba%2112000036120140725%21sea%21NZ%216394433987%21ABX&curPageLogUid=mVYjfbvrU5vv&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Brass melting heat insert | 1 M3 OD 5mm length 5mm (50 pieces) (Aliexpress) | Heat inserts for case and PCB (Aliexpress) | $4.71 | (**TAX**) | https://www.aliexpress.us/item/1005003582355741.html?spm=a2g0o.productlist.main.5.24ac12d7m7D9Ol&algo_pvid=870e099a-1be4-4b3b-9495-46eae48c9ac9&algo_exp_id=870e099a-1be4-4b3b-9495-46eae48c9ac9-4&pdp_ext_f=%7B%22order%22%3A%2218759%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%213.79%211.66%21%21%212.26%210.99%21%402103244b17515900105603223eeccf%2112000026370649721%21sea%21NZ%216394433987%21ABX&curPageLogUid=PvX1sJbDEX6O&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Nano Tape Double Sided Tape | 1 | Gecko tape for screen 20mm(Wide)x0.5m(Long)x1mm(Thick)(Aliexpress) | $2.84 | (**TAX**) | https://www.aliexpress.com/item/1005003517281636.html?spm=a2g0o.productlist.main.5.579eBKXiBKXiG2&algo_pvid=c1e8b79e-8d5b-4bac-90af-ffbb97b66877&algo_exp_id=c1e8b79e-8d5b-4bac-90af-ffbb97b66877-4&pdp_ext_f=%7B%22order%22%3A%22285%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%211.65%210.99%21%21%211.65%210.99%21%402101c72a17515111151351279e075c%2112000026805632505%21sea%21NZ%216394433987%21ABX&curPageLogUid=gzcBz74skv8b&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Mini Micarta Soldering Iron Stand Holder | 1 | Soldering stand for Pinecil (Aliexpress) | $3.21 | (**TAX**) | https://www.aliexpress.com/item/1005006352272696.html?spm=a2g0o.store_pc_home.promoteRecommendProducts_2004652237334.1005006352272696 | 
| PINE64 Pinecil TS101 Soldering Iron Tip | 1 | Small soldering tip for Pinecil TS-ILS (Aliexpress)| $10.01 | (**TAX**) | https://www.aliexpress.com/item/1005006125240838.html?spm=a2g0o.store_pc_home.promoteWysiwyg_2004652237333.1005006125240838 |
| Type-C Mini Hot Plate PCB SMD | 1 | Hot plate for small components (Aliexpress)| $2.85 | (**TAX**) | https://www.aliexpress.com/item/1005006511319731.html?spm=a2g0o.productlist.main.1.60d741e0IoXroY&algo_pvid=6e3b7f9e-e587-4607-8ce7-bc63e0be9c8f&algo_exp_id=6e3b7f9e-e587-4607-8ce7-bc63e0be9c8f-0&pdp_ext_f=%7B%22order%22%3A%221244%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%2147.35%212.35%21%21%21201.83%219.99%21%402103277f17516748696561900e3da4%2112000037477574263%21sea%21NZ%216394433987%21ABX&curPageLogUid=GBlzTiUO8Kkx&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Monolithic Ceramic Capacitor Kit | 1 | Ceramic Capacitor kit  0.1uf - 10uf  500 pcs (Aliexpress) | $10.93 | (**TAX**) | https://www.aliexpress.com/item/1005006772301578.html?spm=a2g0o.productlist.main.32.28fd4d9dNmQm8b&algo_pvid=481dbf38-0228-437b-89a1-11371636bc9c&aem_p4p_detail=2025070516251011559118486215700004231565&algo_exp_id=481dbf38-0228-437b-89a1-11371636bc9c-25&pdp_ext_f=%7B%22order%22%3A%2268%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%2110.93%211.66%21%21%216.50%210.99%21%402101effb17517579108254835e8b56%2112000038249154392%21sea%21NZ%216394433987%21ABX&curPageLogUid=EixJBf52480q&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=2025070516251011559118486215700004231565_7 | 
| Electrolytic Capacitor Kit | 1 | Aluminium Electrolytic Capacitors Kit 1uf - 470uf 120 pcs (Aliexpress) | $5.82 | (**TAX**) | https://www.aliexpress.com/item/1005005626707702.html?spm=a2g0o.productlist.main.1.33696zwd6zwdiq&algo_pvid=888a458f-cf4b-4112-82b8-b34241255c81&algo_exp_id=888a458f-cf4b-4112-82b8-b34241255c81-0&pdp_ext_f=%7B%22order%22%3A%221412%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%215.82%211.66%21%21%2124.81%217.08%21%402101ea7117517609208091735e0dee%2112000033796706983%21sea%21NZ%216394433987%21ABX&curPageLogUid=mk4afSyCFG9E&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Resistor Kit | 1 | Metal Film Resistor Pack Assorted Kit 10ohm - 1m ohm 300pcs (Aliexpress) | $4.47 | (**TAX**) $9.08 | https://www.aliexpress.com/item/1005005855324735.html?spm=a2g0o.productlist.main.1.1b22578fKSCLRh&algo_pvid=85089809-d842-4483-bf22-11a567e35ac0&algo_exp_id=85089809-d842-4483-bf22-11a567e35ac0-0&pdp_ext_f=%7B%22order%22%3A%223547%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%214.35%211.66%21%21%212.59%210.99%21%402101e07217517039549628903eb221%2112000034587357832%21sea%21NZ%216394433987%21ABX&curPageLogUid=GUVoHuNTQhAN&utparam-url=scene%3Asearch%7Cquery_from%3A |
| PCB | 5 | Custom PCB I made | $2.00 | $6.40 | N/A (CUSTOM JLCPCB) |

| Total: | $104.34 (BASE COMPONENTS TOTAL) | $129.69 (ALL TOTAL) | 
|--------|---------------------------------|---------------------|
### Construction
The DuckyDK MTR-1 was mainly made using Kicad, Fusion 360, Github and Slack. I made all the PCB schematics and design of the PCB in Kicad, while I made the 3D model of the case in Fusion 360. I used GitHub to document my process of making the project and Slack to help me answer questions. I spent a lot of time researching and reading through data sheets and answers to questions to figure out new things I didn't understand. I learnt a lot through this project and I hope people can see and understand.

### Credit
Cheers to all these people for helping make this project possible.

- [@Ryan Green](https://hackclub.slack.com/team/U090854913L): For helping me understand how to source parts and pick out a few parts for me to use.
- [@Person20020 (Koji)](https://hackclub.slack.com/team/U07QNKS5SKA): For helping me with PCB problems even when he's mainly helps with HackPad problems, also he helped with my HackPad.
- [@QinCai](https://hackclub.slack.com/team/U07BNRCEARM): For helping me answer questions and creating the code part of the project.
- [@Niko](https://hackclub.slack.com/team/U07960MD940): For helping answer importing questions about 3d printing and potentally printing my project.
- [Rudy](https://hackclub.slack.com/team/U079HV9PTC7): For helping with lots of different parts like questions and help picking out the Xiao ESP32 S3. Also, for giving my tips on picking out parts.
- [@alexren](https://hackclub.slack.com/team/U06PR6B8D37) and [@acon](https://hackclub.slack.com/team/U04KEK4TS72): For being great event organisers and creating Highway for me to do this.
- Whoever is looking over the project: I hope you enjoy reading all this. Thanks for your feedback once you finish.
- The Slack Community: For helping me answer strange and different questions to help me continue with my project.

Digikey's BOM part needs to be over $50 USD for free shipping. This is really important because shipping to my country is very expensive.

Side tangent, I'm still mad that my time from SoM is useless and especially because they announced it once I almost finished the project.

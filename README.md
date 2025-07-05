# DuckyDK-MTR-1

### Description
This is a Metronome device called the DuckyDK MTR-1. This is for musicians, like me, who need a portable metronome that can be used anywhere. It is designed in a compact form to maximize space usage and portability. 

### Inspiration
This idea was thought of and inspired when I bought a new drum kit which I loved, and I wanted to think of different projects I could make which is connected to my drum kit. One idea that was obvious was to make a custom metronome. This is the result of that idea. Even though devices like laptops can do this, I wanted to make a portable, offline metronome what is not reliant on any device and can be brought along to many places. 

**Name**
The name DuckyDK MTR-1 is from many things. **Ducky** comes from my username **Ducky**Boi_XD, **DK** is/comes from **D**rum **K**it or **D**uc**k**. **MTR** comes from **M**etronome, while the **1** indicates that this is the first version of this metronome project.

### Features 
These are the features that are implemented in the DuckyDK MTR-1:
- **Compact Design**: The device is contained in a small, portable, compact case which is custom designed to fit all the necessary components. 

- **Adjustable Tempo/Time signature**: The tempo and time signature can be adjusted to fit the user's needs. The temp can be adjusted by the rotary encoder and the time signature can be adjusted by the internal button on the rotary encoder.

- **Volume Control**: The volume of the metronome can be adjusted but the potentiometer is attached to the case. This the user to adjust their preference for their volume. For example, I play drums which can be quite loud, resulting in the need of a louder metronome.

- **2 Control Buttons**: On the case is 2 buttons controlling 2 important functions of the metronome. The first button is the start or stop mechanism of the metronome. The second button is a preset button. This button contains 3 presets that can be selected and used by pushing the preset button.

- **Info Display**: The device contains an appropriately sized OLED display which contains many necessary information. It contains, a big indicator of the current tempo/BPM in the centre of the screen, a volume level on the right side of the screen as a bar with percentage sign underneath, a 3 boxes which is the preset indicator on the left side of the screen, and lastly, the current time signature located on the bottom of the screen, under the BPM indicator.

- **Headphone Jack**: The device contains a headphone jack which allows the user to connect headphones to the device. This is currently the only way to hear th metronome. This headphone jack also contains a switch when the headphones are connected. This can be changed to do whatever you want.

### BOM (Bill of Materials)

#### NOTE
Aliexpress prices may change, all prices are based of no sales or coupons (except for hot plate), so the final result of the price would be less.
(GST) = General sales tax, it's calculated at the last **GST** 
Tax is calculated at the last **TAX**

| Component | Quantity | Description | Base Price | Extra Costs | Link | 
|-----------|----------|-------------|------------|-------------|------|
| Xiao ESP32-S3 Plus | 1 | MCU (Micro controller Unit) (Digikey) | $7.99 | (**GST**) | https://www.digikey.co.nz/en/products/detail/seeed-technology-co-ltd/102010671/26553873 | 
| PCM5102APWR | 1 | DAC (Digital to Analog Converter) (Digikey) | $4.43 | (**GST**) | https://www.digikey.co.nz/en/products/detail/texas-instruments/PCM5102APWR/3727211?s=N4IgTCBcDaIAoGECyBWAjABjAQTgdQCUQBdAXyA |
| MAX9722AEUE+ | 1 | AMP (Audio Amplifier) (Digikey) | $1.52  | (**GST**) | https://www.digikey.co.nz/en/products/detail/analog-devices-inc-maxim-integrated/MAX9722AEUE/1495288 | 
| SJ1-3514N | 1 | 3.5mm Headphone Jack (Digikey) | $1.19  | (**GST**) | https://www.digikey.co.nz/en/products/detail/same-sky-formerly-cui-devices/sj1-3514n/738685 | 
| PTN092-H50115K1A | 1 | Potentiometer (Digikey) | $2.00  | (**GST**) | https://www.digikey.co.nz/en/products/detail/same-sky-formerly-cui-devices/PTN092-H50115K1A/24767692 |
| EC11E18244A5 | 1 | Rotary Encoder (Digikey) | $4.85 | (**GST**) | https://www.digikey.co.nz/en/products/detail/alps-alpine/ec11e18244a5/21721665 |
| MFR-25FRF52-4K7 | 10 | Resistor 4.7k Ohm (Digikey) | $0.39 | (**GST**) | https://www.digikey.co.nz/en/products/detail/yageo/MFR-25FRF52-4K7/9139057 | 
| CFR-25JB-52-470R | 10 | Resistor 470 Ohm (Digikey) | $0.34 | (**GST**) | https://www.digikey.co.nz/en/products/detail/yageo/CFR-25JB-52-470R/2211 | 
| C320C104K5R5TA7305 | 10 | Capacitor 0.1 uf (Digikey) | $0.22 | (**GST**) | https://www.digikey.co.nz/en/products/detail/kemet/C320C104K5R5TA7305/12701231 |
| C330C105M5R5TA7301 | 10 | Capacitor 1 uf (Digikey) | $3.08 | (**GST**) | https://www.digikey.co.nz/en/products/detail/kemet/C330C105M5R5TA7301/14681306 |
| C330C225M5U5TA7303 | 10 | Capacitor 2.2 uf (Digikey) | $4.58 | (**GST**) | https://www.digikey.co.nz/en/products/detail/kemet/C330C225M5U5TA7303/6562327 |
| EEA-GA1C100H | 10 | Capacitor 10 uf (Digikey) | $1.53 | (**GST**) | https://www.digikey.co.nz/en/products/detail/panasonic-electronic-components/EEA-GA1C100H/2513289 |
| ECE-A1AN101X | 10 | Capacitor 100 uf (Digikey) | $2.71 | (**GST**) | https://www.digikey.co.nz/en/products/detail/panasonic-electronic-components/ECE-A1AN101X/364922 | 
| 404070001 | 1 | ESD Safe Tweezers (Straight) (Digikey) | $2.50 | (**GST**) | https://www.digikey.co.nz/en/products/detail/seeed-technology-co-ltd/404070001/5488233 |
| 422 | 1 | ESD Safe Tweezers (Curved) (Digikey) | $3.95 | (**GST**) | https://www.digikey.co.nz/en/products/detail/adafruit-industries-llc/422/7241434 |
| 1007-24-1-2000-001-1-TD | 5 (feet) | Wires | $2.22 | (**GST**) | https://www.digikey.co.nz/en/products/detail/cnc-tech/1007-24-1-2000-001-1-TD/17799235 |
| 20-0600-21 | 1 (20 pins) | Male pin headers | $3.83 | (**GST**) | https://www.digikey.co.nz/en/products/detail/aries-electronics/20-0600-21/4207162 |
| 97791003111 | 10 | Screws | $2.24 | (**GST**) $7.60 | https://www.digikey.co.nz/en/products/detail/w%C3%BCrth-elektronik/97791003111/10056389 | 
| 1.3 Inch Oled Module Witte Kleur | 1 | OLED screen (Aliexpress) | $5.36 | (**TAX**) | https://www.aliexpress.com/item/1005007451015054.html?spm=a2g0o.productlist.main.3.5c94BkFLBkFLwI&algo_pvid=c05ab788-0f62-4cac-8ecf-0ac50b96f1c8&algo_exp_id=c05ab788-0f62-4cac-8ecf-0ac50b96f1c8-2&pdp_ext_f=%7B%22order%22%3A%221408%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%215.36%211.68%21%21%213.15%210.99%21%402103247917505815500323989e2c7f%2112000040806152742%21sea%21NZ%216394433987%21ABX&curPageLogUid=4GgHuLqPJwAs&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Ultra Short Switch | 2 | Buttons (Aliexpress)| $9.34 | (**TAX**) | https://www.aliexpress.com/item/1005004920346156.html?spm=a2g0o.productlist.main.7.7f7d5f2722dp5N&algo_pvid=88ea1ebf-ed98-4122-ae48-2b34d2cbcef4&algo_exp_id=88ea1ebf-ed98-4122-ae48-2b34d2cbcef4-6&pdp_ext_f=%7B%22order%22%3A%221272%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%214.19%211.70%21%21%2117.53%217.11%21%402103247417506694259818233e29c3%2112000039500055503%21sea%21NZ%216394433987%21ABX&curPageLogUid=AdxbPFQrTg6S&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Hexagon Fine Thread Thin Nuts | 1 (20 pieces) | Nuts for Rotary encoders and Potentiometer (Aliexpress) | $3.84 | (**TAX**) + $5.49 (Shipping) | https://www.aliexpress.com/item/1005006173995318.html?spm=a2g0o.productlist.main.15.7dbd4ebaNansD7&algo_pvid=bbffa5d8-f689-4588-a6f6-ce0996436945&algo_exp_id=bbffa5d8-f689-4588-a6f6-ce0996436945-14&pdp_ext_f=%7B%22order%22%3A%22151%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%211.85%211.39%21%21%217.88%215.91%21%40210308a417510851180067032e73ba%2112000036120140725%21sea%21NZ%216394433987%21ABX&curPageLogUid=mVYjfbvrU5vv&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Brass melting heat insert | 1 (50 pieces) | Heat inserts for case and PCB (Aliexpress) | $4.71 | (**TAX**) | https://www.aliexpress.us/item/1005003582355741.html?spm=a2g0o.productlist.main.5.24ac12d7m7D9Ol&algo_pvid=870e099a-1be4-4b3b-9495-46eae48c9ac9&algo_exp_id=870e099a-1be4-4b3b-9495-46eae48c9ac9-4&pdp_ext_f=%7B%22order%22%3A%2218759%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%213.79%211.66%21%21%212.26%210.99%21%402103244b17515900105603223eeccf%2112000026370649721%21sea%21NZ%216394433987%21ABX&curPageLogUid=PvX1sJbDEX6O&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Nano Tape Double Sided Tape | 1 | Gecko tape for screen (Aliexpress) | $2.84 | (**TAX**) | https://www.aliexpress.com/item/1005003517281636.html?spm=a2g0o.productlist.main.5.579eBKXiBKXiG2&algo_pvid=c1e8b79e-8d5b-4bac-90af-ffbb97b66877&algo_exp_id=c1e8b79e-8d5b-4bac-90af-ffbb97b66877-4&pdp_ext_f=%7B%22order%22%3A%22285%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%211.65%210.99%21%21%211.65%210.99%21%402101c72a17515111151351279e075c%2112000026805632505%21sea%21NZ%216394433987%21ABX&curPageLogUid=gzcBz74skv8b&utparam-url=scene%3Asearch%7Cquery_from%3A |
| Mini Micarta Soldering Iron Stand Holder | 1 | Soldering stand for Pinecil | $3.21 | (**TAX**) | https://www.aliexpress.com/item/1005006352272696.html?spm=a2g0o.store_pc_home.promoteRecommendProducts_2004652237334.1005006352272696 | 
| PINE64 Pinecil TS101 Soldering Iron Tip | 1 | Small soldering tip for Pinecil | $10.01 | (**TAX**) | https://www.aliexpress.com/item/1005006125240838.html?spm=a2g0o.store_pc_home.promoteWysiwyg_2004652237333.1005006125240838 |
| Type-C Mini Hot Plate PCB SMD | 1 | Hot plate for small components | $2.85 | (**TAX**) $5.90 | https://www.aliexpress.com/item/1005006511319731.html?spm=a2g0o.productlist.main.1.60d741e0IoXroY&algo_pvid=6e3b7f9e-e587-4607-8ce7-bc63e0be9c8f&algo_exp_id=6e3b7f9e-e587-4607-8ce7-bc63e0be9c8f-0&pdp_ext_f=%7B%22order%22%3A%221244%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%2147.35%212.35%21%21%21201.83%219.99%21%402103277f17516748696561900e3da4%2112000037477574263%21sea%21NZ%216394433987%21ABX&curPageLogUid=GBlzTiUO8Kkx&utparam-url=scene%3Asearch%7Cquery_from%3A |
| PCB | 5 | Custom PCB I made | $2.00 | $6.40 | N/A (CUSTOM JLCPCB) |
| Printing Legion Sipping | 1 | Shipping money for CAD prints | $10.00 | N/A | N/A |

| Total: | $104.34 (BASE COMPONENTS TOTAL) | $129.69 (ALL TOTAL) | 
|--------|---------------------------------|---------------------|
### Construction
The DuckyDK MTR-1 was mainly made using Kicad, Fusion 360, Github and Slack. I made all the PCB schematics and design of the PCB in Kicad, while I made the 3D model of the case in Fusion 360. I used Github to document my process of making the project and Slack to help me answer questions.

## Kicad Schematic
<img width="866" alt="Screenshot 2025-07-05 at 12 15 32 PM" src="https://github.com/user-attachments/assets/f2c3c3cd-cb48-4ade-b3a3-bd41635f7fe4" />

## Kicad PCB
<img width="893" alt="Screenshot 2025-07-05 at 12 15 48 PM" src="https://github.com/user-attachments/assets/ef771269-d041-4825-8337-2ac4c50c05bc" />

## Fusion Case
<img width="574" alt="Screenshot 2025-07-04 at 5 19 01 PM" src="https://github.com/user-attachments/assets/665c3d3e-0bae-4d9c-90e9-277a2d006df4" />

## Fusion Production Case
<img width="1008" alt="Screenshot 2025-07-04 at 5 18 35 PM" src="https://github.com/user-attachments/assets/a01da600-e194-4737-8f38-2c91e4207637" />

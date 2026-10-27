---
title: Warehouse Design and Storage
created: 2026-10-27
updated: 2026-10-27
type: concept
tags: [spo, book, warehousing, spare-parts, maintenance-management, inventory-control]
sources: [spare-parts-optimization.md]
confidence: medium
contested: false
---

# Warehouse Design and Storage

การออกแบบคลังพัสดุโรงงาน (MRO warehouse) และวิธีจัดเก็บตามหนังสือ [[Spare Parts Optimization Book]] บทที่ 2 (หน้าที่และความรับผิดชอบของคลังวัสดุ) และบทที่ 7 (Warehousing) ผู้เขียนเป็นอดีตผู้จัดการคลังพัสดุโรงกลั่น จึงเน้นของหนัก ของกลางแจ้ง และสารเคมีแบบโรงงานปิโตรเคมี หน้านี้เป็นฝั่ง "physical store" ของ [[Spare Parts Management]] ส่วนการจัดหมวดวัสดุอยู่ใน [[MRO Material Classification]] และการควบคุมเครื่องมือ/ความมั่นคงอยู่ใน [[Tool Crib and Warehouse Security]]

## บทบาทของคลังวัสดุ (บทที่ 2)

- โรงงาน capital intensive มี SKU หลายหมื่นรายการ มูลค่าร้อยล้านถึงพันล้านบาท เสี่ยงวัสดุไม่เคลื่อนไหวกระทบสภาพคล่อง บทนี้ใช้เป็นแนวฝึกอบรมหรือมาตรฐานงาน QJA (Quality Job Assignment) ได้ (SPO p.20)
- ความรับผิดชอบหลักของหัวหน้าคลัง: รับ เก็บรักษา จ่าย และ **รักษาระดับคงคลัง** ผู้เขียนเห็นว่าสำหรับวัสดุโรงงาน งานระดับคงคลังควรอยู่กับคลัง ไม่ใช่บัญชีหรือ Inventory Management โดยมีเจ้าหน้าที่เทคนิคแต่ละสาขาให้คำแนะนำ และอาจตั้งคณะกรรมการบริหารวัสดุ (MMC) (SPO p.20)

### งานหลัก 7 ข้อ (Main Function) (SPO p.20-22)

| ข้อ | งาน | รายละเอียด |
|---|---|---|
| 1 | รักษาระดับคงคลัง | regular storehouse stock (SKU) เติมด้วย order control procedure; ของซื้อตรง/โครงการที่ฝากคลังเป็น custody control sub stock |
| 2 | รับและจ่าย | รับ ตรวจ เช็กเอกสาร ณ **จุดรับเดียว** ของโรงงาน (internal audit, ความปลอดภัย); จ่ายต้องมีเอกสารและลายเซ็นผู้มีอำนาจ |
| 3 | เก็บรักษาและป้องกัน | จัดพื้นที่ ทางเดิน คุมอุณหภูมิ/ความชื้น กันอุบัติเหตุ (unsafe condition / act) และการขโมยทั้งคนในคนนอก |
| 4 | บันทึกและควบคุม | บันทึกการรับและตำแหน่งเก็บ; บันทึกการจ่ายให้ตรงใบเบิก สเปก และรหัส |
| 5 | กำจัดวัสดุหมดประโยชน์ | ค้นหา obsolete แล้วดำเนินการ |
| 6 | กำจัดวัสดุเสีย/หมดอายุ | ค้นหาแล้วดำเนินการ |
| 7 | ระดับคงคลังต่ำเชิงเศรษฐศาสตร์ | พอไม่ให้งานหยุด ไม่ฟุ่มเฟือย; เกินจำเป็นเป็น dead stock |

### หัวข้อความรับผิดชอบที่สำคัญ (จาก 20 ข้อ) (SPO p.22-23)

- เลือกวิธีควบคุมระดับคงเหลือตามอัตราความต้องการ (fast / medium / slow moving) และ lead time ดู [[MRO Inventory Control Methods]]
- พัฒนารายการอะไหล่ใช้ได้หลายเครื่อง ดู [[Parts Interchangeability]]
- ประสานจัดซื้อเรื่องแหล่งและ lead time (โดยเฉพาะอะไหล่ประกัน) และร่วมพัฒนา Blanket Order ดู [[MRO Purchasing and Contracting]]
- เสนอตัดยอดวัสดุหมดประโยชน์ แต่ **ให้จัดซื้อหรือหน่วยอื่นเป็นผู้ขาย** เพราะให้คลังคัดและขายเองเปิดช่องทุจริต (แยกหน้าที่)
- ควบคุม claim ของเสียหายระหว่างรับหรือก่อนหมดประกัน
- บริหาร tool room (อาจมอบให้หน่วยซ่อมบำรุงแทน) ดู [[Tool Crib and Warehouse Security]]
- เตรียมและร่วมตรวจนับ รวม cycle count; แก้ขาด-เกินจากการตรวจนับประจำปีและรายงานตรวจสอบภายใน
- ควบคุมค่าใช้จ่ายคลังเพื่อคำนวณค่าเก็บรักษา และเก็บสถิติวัสดุคงเหลือเฉลี่ยเทียบเงินลงทุนโรงงาน ดู [[Inventory Turnover and GPI Benchmarks]]
- บริหารของราคาต่ำ-หมุนเร็วแบบ supermarket; ฝึกอบรมพนักงานคลัง
- รายงานประจำ: **Stock Status Report, Stock Movement Report, Reorder Report, On Order Report**

## ประเภทคลัง: central vs sub stock (SPO p.64)

- ควรมี **คลังส่วนกลาง** (central materials and supplies storehouse) เดียว คลังกระจายหลายแห่งทำให้สะสมเกินและเกิดสต็อกตายแต่ละแห่ง การคุมระดับ อัตราใช้ สถิติ รายงาน ควรรวมศูนย์
- **sub stock** ที่ฝ่ายซ่อมบำรุง/ผลิตยอมให้มีได้สำหรับรายการที่คัดแล้ว แต่ต้องคุมเหมือนบัญชีวัสดุคงเหลือ: ของราคาต่ำอาจเบิกขาดลงค่าใช้จ่ายหน่วยงาน ของราคาสูงต้องเป็น **controlled sub stock**
- คลังย่อยเพิ่มค่าใช้จ่าย แต่คุ้มถ้าทำให้เครื่องเดินไม่สะดุด (SPO p.74)

## อาคารคลัง (SPO p.64-65)

- **อาคารชั้นเดียว** ดีที่สุด: ติด overhead crane ตลอดแนว, ของหนักอยู่ชั้นล่าง, คุมรับ-จ่ายง่าย, ทำความสะอาดง่าย, ต้นทุนก่อสร้างต่ำ
- ช่วงเสา 5-8 m ใช้กำหนดช่องเก็บ (bay) ราว 5x5 m หรือ 8x8 m
- ความสูงราว 18 ft ซ้อนพาเลทได้ราว 4 ชั้นอย่างปลอดภัย
- พื้นคอนกรีตยกระดับเป็น dock; ประตูให้รถ 10 ล้อหรือคอนเทนเนอร์เข้าได้ มี main gate 2 แห่งขนาดเท่ากันอยู่ห่างกัน: ประตูรับใกล้ทางเข้าบริษัท ติดพื้นที่รับและ QC; ประตูจ่ายสำหรับของหนัก/จำนวนมาก ปกติปิด

### ความสว่าง (SPO p.65)

ต้องอ่าน Name Plate, Part Number, Packing List ได้ และควรติดไฟ **หลังจัดชั้นเสร็จ** เพื่อไม่ให้ชั้นบังแสง

| พื้นที่ | ตามหนังสือ | เทียบ lux (derived) |
|---|---|---|
| ชั้นวางทั่วไป | 30 foot-candle | ~323 lux |
| ห้องติดฉลาก / บรรจุหีบห่อ | 50 foot-candle | ~538 lux |

ค่า lux คำนวณเองด้วย 1 fc = 10.76 lux (ความรู้ทั่วไป ไม่มีในหนังสือ)

## การกำหนดขนาดคลัง (SPO p.65-66)

ไม่มีสูตรตายตัว หนังสือเสนอตัววัด 3 ตัวสำหรับคลัง MRO: ft² ต่อ 1 ล้าน USD ของ GPI, ft² ต่อ 1 ล้าน USD ของมูลค่าคงคลัง, และ ft² ต่อ line item แล้วเทียบข้อมูล 8 แห่งของบริษัทใหญ่แห่งหนึ่ง

| แห่ง | GPI (M USD) | Inv. Val (M USD) | Line items | พื้นที่ ft² | ft²/M GPI | ft²/M Inv | ft²/item |
|---|---|---|---|---|---|---|---|
| A Bataan, Texas | 43.7 | 1.179 | 10,544 | 16,870 | 386 | 14,300 | 1.6 |
| B ESPAC | 46 | 0.26 | 17,333 | 5,200 | 113 | 20,000 | 0.3 |
| ESPAC (Modified) | 46 | 0.27 | 20,000 | 10,000 | 217 | 37,000 | 0.5 |
| C Malaysia | 27 | 0.7 | 6,857 | 4,800 | 178 | 6,900 | 0.7 |
| D Bombay | 37 | 1.26 | 6,170 | 29,000 | 780 | 23,000 | 4.7 |
| E Australia | 16.5 | 0.4 | 3,425 | 7,535 | 456 | 19,000 | 2.2 |
| F Melbourne | 24 | 4.57 | 4,571 | 12,800 | 530 | 2,800 | 2.8 |
| G Petrochem | 30 | 0.5 | 6,000 | 6,000 | 200 | 12,000 | 1.0 |

- ตีความของหนังสือ: ESPAC พื้นที่ไม่พอแม้ขยายแล้ว (ของถูกแต่รายการมาก) ส่วน Bombay มากเกินไป
- **มาตรฐานที่เสนอ** (ใช้ Bataan กับ Australia เป็นค่ากลาง เฉพาะ MRO ในโรงงานอุตสาหกรรม): **425 ft² / 1 M USD GPI**, **16,600 ft² / 1 M USD มูลค่าคงคลัง**, **2 ft² / line item** ไม่ใช่ตัวเลขตายตัว และควรเผื่อพื้นที่ขยาย
- GPI ไม่มีคำอธิบายในหนังสือ น่าจะเป็น Gross Plant Investment (ข้อสันนิษฐานของ notes) ดู [[Inventory Turnover and GPI Benchmarks]]
- คลังกลางแจ้ง (yard) สำหรับโรงงานใหญ่ ราว **2.5 เท่า** ของคลังในร่ม (SPO p.68)

## พื้นที่รับและการดำเนินงาน (SPO p.67-68)

- **Receiving area** แยกเฉพาะ ไม่ใช้เก็บของ; ตรวจรับเสร็จนำเข้าที่ทันที ติดป้ายวันรับ/เลข PO, ลง location code, บันทึกขาด/เกิน/ชำรุดแล้วตั้ง claim, ทำ Receiving Report ให้เสร็จภายในวัน
- ของ direct purchase ส่งผู้ใช้ทันที ถ้าฝากไว้ให้ผู้ใช้ติดป้ายวันใช้และแยกเก็บ
- ก่อนเก็บพิจารณาว่าต้องกันฝุ่น คุมอุณหภูมิ คุมความชื้น ไวต่อสภาพแวดล้อม หรือเป็นอันตราย; วางบนพาเลท ทำความสะอาดและกันสนิมก่อนเก็บ
- จ่ายตามคู่มือคลัง ตรวจทุกครั้ง (บางแห่งมี checker) มีรายชื่อและลายเซ็นผู้มีอำนาจเบิก; บางแห่งกำหนดเวลาเปิดจ่ายเพื่อเหลือเวลาทำเอกสารและจัดเก็บ
- **การคืนของเข้าคลัง** แยก 3 ประเภท: (1) ใหม่/ยังไม่ใช้ (2) ซ่อมเล็กน้อยใช้ได้ (3) เสื่อม/เสีย

### Free issue / supermarket

- ของราคาต่ำจ่ายบ่อย (bolt, nut, washer, ถ่าน, กระดาษทราย, เศษผ้า) บริหารแบบซูเปอร์มาร์เก็ต ไม่ต้องใช้ใบเบิก ลงค่าใช้จ่ายผ่าน cost center อาจใช้ barcode และราคาเฉลี่ยเดียว (ตัวอย่างชิ้นละ 35 บาท) (SPO p.74) รายละเอียดการควบคุมใน [[MRO Inventory Control Methods]]
- **ข้อขัดแย้งภายในบท**: เกณฑ์ราคา Free Issue ระบุไม่เกินราว 5-10 บาท/ชิ้น (SPO p.68) แต่ Free Stock ระบุราว 10-20 บาท ไม่เกิน 50 บาท (สหรัฐฯ ไม่เกิน 1 USD) (SPO p.74) ถือเป็นความไม่สอดคล้องของหนังสือ ไม่ตั้ง contested ให้องค์กรกำหนดเกณฑ์เอง

## การวางผังภายในคลัง (SPO p.69-73)

### Popularity storage (SPO p.69)

| กลุ่ม | % ของจำนวนรายการ | ความถี่จ่าย | ตำแหน่ง |
|---|---|---|---|
| A | 20% | จ่ายบ่อย | หน้าคลังใกล้ช่องจ่าย |
| B | 60% | ปานกลาง | ส่วนกลาง |
| C | 20% | หมุนช้า | หลังคลัง |

### ทางเดิน (SPO p.69)

- **Main aisle**: แนวประตูใหญ่ ให้รถสวนกัน 12'6"-14'6" (หนังสือแปลง 3.75-4.35 m); คลังเล็กให้คิดจากรถยกและพาเลทมาตรฐาน ~48x48 นิ้ว
- **Service aisle**: ระหว่างชั้น ใช้คน/hand truck 30-48 นิ้ว (หนังสือแปลง 1.00-1.20 m)
- กฎ: **ประตูใหญ่ต้องอยู่บน main aisle เสมอ** (SPO p.70-72)

### ผัง A-F สำหรับคลังเคมี/ของหนัก (SPO p.70-72)

ใช้กับน้ำมัน catalyst, inert ball, อิฐทนไฟ, ฉนวน และของหนักวางชั้นไม่ได้ เช่น วาล์วใหญ่ หรือ insurance spares แบบสินทรัพย์ถาวร (rotor, heat exchanger tube bundle) ทางเดินหลักกว้าง ~4 m

| แบบ | อาคาร | ทางเดิน | Pileable space |
|---|---|---|---|
| A | ผืนผ้า 18x60 m | main aisle ตามยาว 1 เส้น | 76% |
| B | ผืนผ้า (28+4+28 m) | main ตามยาว + service ตามขวาง | 71% |
| C | จัตุรัส 60x60 m | main aisle กลาง | 93% |
| D | จัตุรัส (28+4+28 m) | main + cross aisle แบ่ง 4 ส่วน | 86% |
| E | 60x50 m ตามรูป | main 2 ด้าน + รอง 1 ด้าน | 83% |
| F | ตามรูป | main ผ่าทะลุ 2 ด้าน + cross 2 สาย | 78% |

ข้อสังเกต: แบบ A ถ้า main aisle 4x60 m ในอาคาร 18x60 m จะได้ ~78% ไม่ใช่ 76% (derived: (18-4)/18; หนังสืออาจรวมระยะเผื่อ) แบบ C และ D ตรวจแล้วสอดคล้อง ส่วน B, E, F ขนาดจาก OCR ไม่ครบจึงตรวจไม่ได้

### คลัง MRO (SPO p.70, 73)

ของเล็กวางชั้น ของน้ำหนักปานกลางบน pallet rack ของจ่ายบ่อยใกล้เคาน์เตอร์ องค์ประกอบในผัง: storage yard, shelving และ pallet racks, bins, chain link partition ถึงเพดาน, receiving area, sensitive items, refrigerator storage, humidity controlled room, issue counter, free stock area, tool room ติดสำนักงาน

## Yard storage (SPO p.68-69, 75-77)

- เหมาะกับของใหญ่/ของกอง (ท่อใหญ่ ท่อคอนกรีต สารพิษที่เก็บในอาคารไม่ได้); พื้นคอนกรีตเสริมเหล็ก ลาดเล็กน้อย มีทางระบาย ล้อม cyclone fence ล็อกได้ และมีรหัสที่เก็บเหมือนในอาคาร
- location ใช้ช่วงเสารั้ว (~4-5 m) เป็นช่อง รหัสอักษร+เลข เช่น B01, C01
- ห้ามวางติดพื้นแม้พื้นคอนกรีต ใช้ dunnage; ท่อ/วาล์ว/เครื่องจักรทาสารกันสนิม (rust preventative) และไม่ถอดฝาครอบปลายท่อ
- สายเคเบิลมูลค่าสูงควรทำ shed มีผ้าใบปิดข้าง เพราะน้ำซึมเข้าหน้าตัดสายทำให้เสียทั้งเส้น

## การเก็บวัสดุเฉพาะชนิด (SPO p.74-79)

| วัสดุ | แนวทาง |
|---|---|
| ท่อ | เรียงตาม schedule และขนาด; **กองพีระมิดผิด** (จุดสัมผัสเกิดสนิม ต้องจ่ายจากยอด ท่อล่างกลายเป็นสต็อกตาย) ให้แยกช่องด้วยเสา/หลักกั้นและ pipe batten ระหว่างชั้น; ท่อเล็กกว่า 4 นิ้วเก็บในอาคาร |
| วาล์ว | เล็กเก็บในอาคารตามชนิด ขนาด PSI; ใหญ่เก็บนอกได้ ปิดฝาสองด้าน ทาจาระบีเกลียว stem หุ้มพลาสติก **ตั้งตรง** ยึดเหล็กฉาก ห้ามวางนอน/พิงกัน |
| ข้อต่อท่อใหญ่ | ให้ผู้ขายทำ protection มา วางบนพาเลท เทน้ำฝนที่ขังใน elbow/tee ออก |
| เคเบิลบนรีลไม้ | ไม่วางติดพื้น มีขอนกันกลิ้ง ซีลปลายสองข้างและซีลใหม่ทุกครั้งที่ตัดจ่าย ป้ายบอกความยาวคงเหลือ นอกอาคารใช้ป้ายโลหะ |
| Cylinder ก๊าซ | ตั้งตรง ที่เก็บมีหลังคาเปิดโล่ง ไม่ถอดฝาครอบวาล์ว ท่อเปล่าแขวนป้าย "Empty"; oxygen แยกจาก acetylene และห่างน้ำมัน; acetylene ห่างความร้อน; chlorine ตั้งตรงในที่ร่มเย็น; ammonia หนังสือให้วางราบกันโยก (ควรตรวจกับ SDS ปัจจุบัน) |
| Flammable | ติดป้าย "Flammable" ห้ามถ่ายลงภาชนะไม่มีป้าย ย้ายด้วย safety cans ถังเปล่าตรวจไอก่อนทิ้ง ที่เก็บห่างอาคารและหน่วยผลิต ดีที่สุดคืออาคารแยกกันไฟ |
| Drums | ไม่วางนอนกับพื้น ไม่ตั้งตรงกลางแจ้ง (น้ำขังฝาจนผุ) ใช้พาเลทเหล็ก กองพีระมิดบนไม้รองมีไม้ประกบข้าง **ไม่เกิน 3-4 ชั้น** |
| สารพิษ/วัตถุระเบิด | แยกเก็บที่อากาศถ่ายเท อยู่ในภาชนะเดิม เปิดแล้วไม่รับคืน; สารอันตรายมากซื้อแล้วฝากผู้ขายเก็บ ส่งเมื่อใช้ |
| Sensitive items | เครื่องมือ รองเท้าเซฟตี้ ถุงมือ ของขายต่อได้ เก็บห้องแยกล็อกกุญแจ |
| คุมอุณหภูมิ/ความชื้น | ยาบางชนิด 4°C; อิเล็กทรอนิกส์และชุดซ่อม instrument ห้องปรับอากาศ; ลวดเชื่อมห้องมี dehumidifier |
| ฝุ่น | ฝุ่น+ความชื้นทำให้เกิดสนิม ใช้เครื่องดูดฝุ่นอุตสาหกรรมหรือ power sweeper แทนไม้กวาด |

## ข้อแนะนำ 20 ข้อ (SPO p.79-80)

หลักการ 2 ข้อ: (1) เป็นระเบียบตามหมวด มีระบบ location และป้ายหมายเลข-ยอดคงเหลือ (2) ป้องกันสภาพแวดล้อมและการนำออกโดยมิชอบ ข้อแนะนำสรุป:

1. ไม่กองติดพื้น 2. พื้นที่รับแยกจากพื้นที่จ่าย 3. เว้นห่างผนัง ~50 cm 4. เข้าถึงทุกกอง 5. ตีเส้นกองเก็บและทางสัญจร 6. วางประณีตนับง่าย 7. ของหนักชั้นล่าง ไม่วางทับของอื่น 8. storehouse hygiene 9. รักษาป้ายกำกับ 10. ลงรหัสที่เก็บในเอกสารรับ 11. ห้ามผู้ไม่เกี่ยวข้องเข้า พนักงานคลังหยิบจ่ายเอง 12. คลังล็อกแข็งแรง ของนอกคลังมีระบบผ่านประตู 13. เศษรวมไว้กล่องเดียว 14. หลีกเลี่ยงการขนย้ายซ้ำซ้อน (double handling) 15. ตรวจนับพร้อมตรวจคุณภาพ 16. **cycle count** สองความหมาย: นับหมุนเวียนตามความสำคัญ A ก่อน (รายสัปดาห์/เดือน/ไตรมาส) แล้ว B, C หรือนับทันทีทุกครั้งที่จ่าย 17. ตรวจความปลอดภัย (ถังดับเพลิง การระบายอากาศ แสง) 18. เลือกกระบะ/ชั้น FIFO หรือ LIFO ตามวันผลิต/หมดอายุ และ popularity storage 19. ทางสัญจรโล่ง 20. คำนึงพิกัดรับน้ำหนักพื้น (ตัน/m²) ตั้งแต่ออกแบบ

- ข้อ 7 ข้อความ OCR ขัดกันเอง ("หลีกเลี่ยงวางของหนักบนของที่หนักมาก") notes ตีความว่าไม่วางของหนักบนของเบา/เปราะ; ข้อ 13-14 ข้อความไม่สมบูรณ์ ตีความจากบริบท
- **Keep parts in pack**: ตรวจรับแล้วบรรจุกลับกล่องเดิม; พาเลทหันป้ายออก จำนวนต่อพาเลทเท่ากัน เศษกล่องอยู่พาเลทเดียว (SPO p.81)

## ชนิดชั้นวาง (SPO p.81-83)

| ชั้นวาง | ใช้กับ |
|---|---|
| Wheel tire rack | ของทรงกลม ยาง ขดลวด สายไฟ |
| Long profile (cantilever) rack | ท่อ เหล็กบาร์ยาว รับน้ำหนักมาก |
| Xmas tree rack | คล้าย cantilever รับน้ำหนักน้อยกว่า เช่น เหล็กแชนแนล ท่อ PVC |
| Push back rack | ชั้นเอียง ใช้รถยกดันเข้า มีสลักกันไหล |
| Slide racking | ของม้วน (ลวดสลิง เคเบิล) กลิ้งมาหน้าได้ |
| FIFO racking | ชั้นลาดเทให้ของเลื่อนมาหน้า คุมลำดับจ่าย |
| ตู้ลิ้นชัก | อะไหล่เล็ก |
| พาเลทเหล็กวางถัง | ถังน้ำมัน 200 ลิตร |

หนังสืออธิบาย push back rack ปนกับ flow/FIFO rack ตามหลักทั่วไป push back rack เป็น **LIFO** ไม่ใช่ FIFO (ความรู้ทั่วไป, confidence low)

## ข้อผิดพลาดของหนังสือ/OCR ที่ควรรู้

- การแปลงหน่วยไม่ตรง: 18 ft = 5.49 m (หนังสือ ~5.6 m); 12'6"-14'6" = 3.81-4.42 m (หนังสือ 3.75-4.35 m); 30-48 นิ้ว = 0.76-1.22 m (หนังสือ 1.00-1.20 m) (derived จากความรู้ทั่วไป)
- ขนาด bay เขียนเป็น "5x5 หรือ 8x8 ตารางเมตร" ควรเป็น 5x5 m หรือ 8x8 m
- ตารางขนาดคลัง: คอลัมน์ที่คำนวณสอดคล้องทุกแถว และมาตรฐาน 425 / 16,600 / 2 ใกล้ค่าเฉลี่ยของ Bataan กับ Australia (421 / 16,650 / 1.9, derived) แต่ Melbourne Inv. Val 4.57 กับ line items 4,571 ซ้ำกันอย่างน่าสงสัย
- Pileable แบบ A 76% vs ~78% (ดูข้างบน); Free issue price limit 5-10 vs 10-50 บาท (ดูข้างบน)

## เชื่อมโยงกับงานบำรุงรักษา/compressor

- การกันสนิม ซีลปลาย และเก็บตั้งตรงของวาล์ว/rotor/bundle คือการป้องกัน deterioration ของ insurance spares ซึ่ง RBMM ถือเป็นอะไหล่ค่าขาดสูง (ดู [[Spare Part Criticality and Risk]]) อะไหล่ที่เสื่อมในคลังทำให้ค่าความพร้อมที่คำนวณไว้ไม่จริง (การตีความของ wiki)
- เกณฑ์ cycle count ตาม A/B/C สอดคล้องกับ KPI ด้านความถูกต้องของคลังใน [[Maintenance KPIs]] (การตีความ)

## Triplets

- [[Warehouse Design and Storage]] [defined_in:: [[Spare Parts Optimization Book]]] chapters 2 and 7 (SPO p.20-23, p.63-83)
- [[Warehouse Design and Storage]] [part_of:: [[Spare Parts Management]]]
- [[Warehouse Design and Storage]] [related_to:: [[MRO Material Classification]]]
- [[Warehouse Design and Storage]] [related_to:: [[Tool Crib and Warehouse Security]]]
- Storekeeper Main Functions [has_value:: 7] main functions of the materials store (SPO p.20-22)
- Maintain Stock Level [part_of:: Storekeeper Main Functions] regular storehouse stock and custody control sub stock (SPO p.20-21)
- Single Receiving Point [part_of:: Storekeeper Main Functions] internal audit and safety (SPO p.21)
- Economic Low Stock Level [part_of:: Storekeeper Main Functions] excess becomes dead stock (SPO p.22)
- Stock Status Report [part_of:: Storekeeper Reports] (SPO p.23)
- Stock Movement Report [part_of:: Storekeeper Reports] (SPO p.23)
- Reorder Report [part_of:: Storekeeper Reports] (SPO p.23)
- On Order Report [part_of:: Storekeeper Reports] (SPO p.23)
- Surplus Sale [depends_on:: Segregation of Duties] purchasing, not store, sells written-off items (SPO p.22-23)
- Central Storehouse [differs_from:: Sub Stock] multiple stores accumulate excess and dead stock (SPO p.64)
- Controlled Sub Stock [applies_to:: High Value Items] (SPO p.64)
- Single Storey Warehouse [is_a:: Warehouse Building Type] preferred: overhead crane, heavy items, control, cost (SPO p.64-65)
- Column Spacing [has_value:: 5-8 m] bay about 5x5 m or 8x8 m (SPO p.64)
- Warehouse Height [has_value:: 18 ft] about 4 pallet tiers (SPO p.65)
- Warehouse Height [has_value:: 5.6 m] book conversion; correct is 5.49 m [confidence:: low]
- Shelf Area Lighting [has_value:: 30 foot-candle] about 323 lux derived (SPO p.65)
- Labeling and Packing Room Lighting [has_value:: 50 foot-candle] about 538 lux derived (SPO p.65)
- Warehouse Sizing [has_parameter:: ft2 per M USD GPI] (SPO p.65-66)
- Warehouse Sizing [has_parameter:: ft2 per M USD inventory value] (SPO p.65-66)
- Warehouse Sizing [has_parameter:: ft2 per line item] (SPO p.65-66)
- Warehouse Sizing [has_value:: 425 ft2 per 1 M USD GPI] proposed MRO standard (SPO p.66)
- Warehouse Sizing [has_value:: 16,600 ft2 per 1 M USD inventory value] proposed MRO standard (SPO p.66)
- Warehouse Sizing [has_value:: 2 ft2 per line item] proposed MRO standard (SPO p.66)
- Warehouse Sizing [uses:: 8-Site Benchmark Table] Bataan and Australia as midpoint (SPO p.66)
- [[Inventory Turnover and GPI Benchmarks]] [related_to:: Warehouse Sizing] GPI basis
- Yard Storage Area [has_value:: 2.5 times indoor store area] large plants (SPO p.68)
- Receiving Area [differs_from:: Storage Area] not used for storage (SPO p.67)
- Returns to Stock [has_category:: new unused / minor repair usable / deteriorated] 3 categories (SPO p.68)
- Free Issue [has_value:: up to 5-10 THB per piece] (SPO p.68)
- Free Stock [has_value:: 10-20 THB, max 50 THB per unit] US up to 1 USD (SPO p.74)
- Free Issue [contradicts:: Free Stock] price limit inconsistent within chapter 7 (SPO p.68, p.74)
- Free Stock [uses:: Supermarket Issue] no requisition, charged to cost center (SPO p.74)
- Popularity Storage [has_category:: A 20% fast / B 60% medium / C 20% slow] share of line items (SPO p.69)
- Main Aisle [has_value:: 12 ft 6 in - 14 ft 6 in] book converts to 3.75-4.35 m, correct 3.81-4.42 m (SPO p.69)
- Service Aisle [has_value:: 30-48 in] book converts to 1.00-1.20 m, correct 0.76-1.22 m (SPO p.69)
- Main Door [depends_on:: Main Aisle] main door always on main aisle (SPO p.70-72)
- Layout A [has_value:: 76% pileable] 18x60 m, one longitudinal main aisle (SPO p.70-72)
- Layout A [contradicts:: 78% pileable derived] 4 m aisle in 18 m width [confidence:: low]
- Layout B [has_value:: 71% pileable] (SPO p.70-72)
- Layout C [has_value:: 93% pileable] 60x60 m central main aisle (SPO p.70-72)
- Layout D [has_value:: 86% pileable] main plus cross aisle (SPO p.70-72)
- Layout E [has_value:: 83% pileable] (SPO p.70-72)
- Layout F [has_value:: 78% pileable] (SPO p.70-72)
- Pyramid Pipe Stacking [contradicts:: Pipe Storage Good Practice] contact points rust, bottom pipes become dead stock (SPO p.75-76)
- Pipe Storage [uses:: Pipe Batten] (SPO p.75-76)
- Large Valve Storage [uses:: Upright Position] end caps, greased stem, never laid flat (SPO p.76)
- Cable Reel Storage [uses:: End Sealing] reseal after every cut (SPO p.76-77)
- Gas Cylinder Storage [uses:: Upright Position] valve caps on, empties tagged Empty (SPO p.77)
- Drum Storage [has_value:: max 3-4 tiers] pyramid on dunnage with side chocks (SPO p.78)
- Welding Electrodes [applies_to:: Humidity Controlled Room] (SPO p.79)
- Cycle Count [is_a:: Storage Recommendation] A items first weekly/monthly/quarterly, or count at every issue (SPO p.80)
- Wall Clearance [has_value:: about 50 cm] (SPO p.79)
- Push Back Rack [is_a:: LIFO Rack] general knowledge; book mixes with FIFO flow rack [confidence:: low]
- FIFO Racking [is_a:: Rack Type] inclined shelves feed items forward (SPO p.82-83)
- Long Profile Rack [applies_to:: Pipe and Bar Stock] cantilever, heavy load (SPO p.82)
- Insurance Spares [related_to:: [[Spare Part Criticality and Risk]]] deterioration prevention in storage, wiki interpretation [confidence:: low]

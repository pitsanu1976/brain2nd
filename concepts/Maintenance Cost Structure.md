---
title: Maintenance Cost Structure
created: 2026-10-20
updated: 2026-10-28
type: concept
tags: [cost, budget, maintenance-management, kpi, spare-parts, book, mpm]
sources: [reliability-based-maintenance-management.md, maintenance-profit-maker.md]
confidence: medium
contested: true
---

# Maintenance Cost Structure

โครงสร้างต้นทุนบำรุงรักษาตาม RBMM แบ่งเป็น **Full Fixed Cost** (ค่าใช้จ่ายคงที่ครบถ้วนที่เห็นในรูป Man-Hrs ใน Work Order) กับ **Materials** (ค่าใช้จ่ายแปรผัน: อะไหล่ + จ้างเหมา) และมีกลไกเชื่อมคือ **Full Fixed Cost Rate** (อัตราค่าแรงมาตรฐาน) กับ **Over/(Under) Absorption** (ส่วนต่างระหว่างค่าที่คิดด้วยอัตรามาตรฐานกับค่าจริง) หน้านี้รวมเนื้อหาจากบท 3, 10 และ 11 ของหนังสือ การนำไปทำงบดู [[Maintenance Budget]] ตัวเลขทั้งหมดเป็นตัวอย่างสมมติของหนังสือ หัวข้อ 9-13 เพิ่มมุมมองจาก [[Maintenance Profit Maker Book]] (MPM บทที่ 6, 7, 10, 14) ซึ่งใช้ชุดตัวอย่างบริษัท XYZ ต่างจาก RBMM และมีข้อขัดแย้งเรื่องค่าครอบครองอะไหล่ (MPM-C1, หัวข้อ 13)

## 1. ภาพรวมโครงสร้าง (RBMM p.278-279)

```
Total Maintenance Cost
 = Full Fixed Cost (Man-Hrs ทั้ง Planned และ Unplanned)
 + Materials (Outsource + Direct Purchase Parts + Stock Parts)
 + Losses (ค่าสูญเสียที่ฝ่ายบำรุงรักษารับผิดชอบ ติดตามเป็นตัวเลขเพื่อบริหาร)
```

- Man-Hrs ใช้ไปกับงานแบบไหนก็ไม่เปลี่ยน Fixed Cost รวม เพราะจ่ายไปแล้ว ปัญหาคือเลือกงานตามแผนได้ดีแค่ไหน (RBMM p.279, 289)
- ค่าสูญเสียจาก Down Time ไม่ตัดจ่ายจากงบบัญชีโดยตรง เป็นตัวเลขคำนวณเพื่อบริหาร (RBMM p.288)

## 2. Full Fixed Cost 5 กลุ่ม (RBMM p.280, 337)

| กลุ่ม | เนื้อหา |
|---|---|
| 1 Personnel | เงินเดือน โบนัส สวัสดิการ (ลดยาก ปลดออกแพง) |
| 2 Asset | ค่าใช้ทรัพย์สินถาวร (ค่าเสื่อม ต้นทุนการเงิน ค่าซ่อมทรัพย์สิน) + ค่ามีอะไหล่คลัง |
| 3 Operating | เช่า น้ำ ไฟ โทรศัพท์ วัสดุสิ้นเปลือง |
| 4 Allocation | ค่าใช้จ่ายสนับสนุนที่กระจายมา (บัญชี HR จัดซื้อ) |
| 5 Provision | สำรอง |

ตัวอย่างงบ (RBMM p.295 และบท 3 Fig 3.4/3.5)

| รหัส | รายการ | งบ (B) | จริง (A) | A-B |
|---|---|---|---|---|
| A1 | Personnel | 20,000,000 | 25,000,000 | 5,000,000 |
| A2 | Operating | 2,400,000 | 3,500,000 | 1,100,000 |
| A3 | Asset (A3.1 + A3.2) | 23,000,000 | 19,720,000 | (3,280,000) |
| A3.1 | Long Term Asset (10% ของ 50,000,000) | 5,000,000 | 520,000 | (4,480,000) |
| A3.2 | Current Asset: อะไหล่คลัง (15% ของ 120,000,000) | 18,000,000 | 19,200,000 | 1,200,000 |
| A4 | Allocation | 500,000 | 500,000 | - |
| A5 | Total Fixed Cost | 45,900,000 | 48,720,000 | 2,820,000 |
| A6 | Parts from Stock | 52,881,818 | 54,000,000 | 1,118,182 |
| A7 | Direct Purchase Parts | 79,000,000 | 78,350,000 | (650,000) |
| A8 | Outsource | 26,763,636 | 29,550,500 | 2,786,864 |
| A9 | Material Cost | 158,645,455 | 161,900,500 | 3,255,045 |
| A10 | Total Maintenance Cost | 204,545,455 | 210,620,500 | 6,075,045 |

เครื่องหมายวงเล็บคือจริงต่ำกว่างบ [อ่านไม่ออกชัด] ค่า A3.1 จริง บท 3 ระบุว่าสองหน้าอ่านเป็น 520,000 และ 320,000 ต่างกัน ใช้ 520,000 ตามบท 10 ซึ่งสอดคล้อง A-B = (4,480,000) และผลรวม A5 = 48,720,000 (derived: 25,000,000 + 3,500,000 + 19,720,000 + 500,000)

คำถามสำคัญของ Fixed Cost คือ "ได้อะไรจากเงินก้อนนี้" คำตอบคือ Man-Hrs พร้อมใช้ ประมาณ 1,600 Man-Hrs/คน/ปี (RBMM p.280) นโยบายจ้างเหมามากทำให้ Fixed Cost ต่ำ แต่ Outsource และอะไหล่สูงขึ้น (RBMM p.280-281)

## 3. Materials (RBMM p.283-284)

| ประเภท | ใช้กับ | กติกา |
|---|---|---|
| Direct Purchase Parts | งานตามแผน (Scheduled PM) | ไม่เก็บสต็อก รู้เวลาใช้และ Lead Time CMMS ส่งไปจัดซื้อ |
| Stock Parts | งานนอกแผนเท่านั้น | สต็อกไว้สู้ CM-Unplanned ถ้าใช้ซื้อตรงกับงานนอกแผนต้องรอ Lead Time |
| Outsource | แรงงานล้น หรือต้องการความชำนาญ | งานจ้างประจำให้ถือเป็น Fixed งานนอกแผนไม่ควรมีจ้างเหมา |

- ต้องแยก Planned/Unplanned ใน Work Order แม้ part code เดียวกัน ([[CMMS]])
- เป้า 0 ที่ตั้งใจ: Stock ของงานตามแผน, Direct Purchase ของงานนอกแผน, Outsource ของงานนอกแผน; ใช้ **Blanket Order** (ผู้ขายนำอะไหล่มาเก็บในคลังเรา คิดเงินเมื่อเบิก) เป็นกลไกพิเศษ (RBMM p.289) — MPM และ SPO เรียกกลไกนี้ว่า Consignment ส่วน Blanket Order หมายถึงซื้อก้อนล่วงหน้า ดู [[MRO Purchasing and Contracting]]
- ค่าครอบครองอะไหล่คลังประมาณ 15-20% ของราคาซื้อต่อปี (บท 3 p.68; บท 10 p.314) หนังสือให้ช่วง 15-25% ที่ p.295 ควรโอนกลับไปยังหน่วยที่ขอสะสมอะไหล่ ดู [[Spare Parts Management]] (MPM ให้ค่าต่างออกไป ดูข้อขัดแย้ง MPM-C1 หัวข้อ 13)

## 4. Full Fixed Cost Rate (อัตราค่าแรงมาตรฐาน) (RBMM p.281-282, 296)

```
Full Fixed Cost Rate = Full Fixed Cost / Man-Hrs ที่ใช้ (planned)
Available Man-Hrs     = Direct Persons x วันทำงาน/ปี x ชม./วัน
Man-Hrs ที่ใช้        = Available Man-Hrs x Utilization Rate
```

ตัวอย่าง (RBMM p.296): 40 x 220 x 8 = 70,400 Man-Hrs, Utilization 60% = 42,240, Rate = 45,900,000 / 42,240 ประมาณ 1,087 บาท/Man-Hr (derived 1,086.6)

อัตราไม่คงที่แม้ Fixed Cost คงที่ ใช้ Man-Hrs มากอัตราต่ำ ใช้น้อยอัตราสูง (บท 3 p.65) ปัญหาที่พบคือคิดอัตราต่ำเกินเพราะนับแค่เงินเดือนเฉลี่ย ให้คิดตามอาชีพ/ระดับ ไม่ต้องเปิดเงินเดือนรายคน

ตัวอย่างอัตราตามระดับ (RBMM p.281): Engineer 1,200 / 900 / 600; Technician 900 / 600 / 400; Labor 300 บาท/Man-Hr (ตาราง 10.6 ใช้ Labor = 200)

### ตัวอย่าง Calculated Cost และ Absorption (RBMM รูป 10.6-10.7 p.282)

| รายการ | อัตรา | Man-Hrs จริง | ค่าคำนวณ |
|---|---|---|---|
| Engineer 1 | 1,200 | 100 | 120,000 |
| Engineer 2 | 900 | 250 | 225,000 |
| Engineer 3 | 600 | 600 | 360,000 |
| Technician 1 | 900 | 600 | 540,000 |
| Technician 2 | 600 | 500 | 300,000 |
| Technician 3 | 400 | 400 | 160,000 |
| Labor | 200 | 800 | 160,000 |
| รวม | เฉลี่ย 574 | 3,250 | 1,865,000 |

Actual Full Fixed Cost = 2,000,000 จึง Under Absorption 135,000 (derived: 2,000,000 - 1,865,000) ปรับอัตราจริงโดยคูณ 2,000,000 / 1,865,000 ประมาณ 1.0724 (เช่น Engineer 1 เป็น 1,286.86)

## 5. Over/(Under) Absorption และ Variance (RBMM p.282, 349-353; บท 3 p.72-73)

```
O/(U) Absorption = ค่าใช้จ่ายคำนวณ (Actual Man-Hrs x Standard Rate) - Actual Full Fixed Cost
Efficiency Variance (Quantity) = (Qty จริง - Qty งบ) x Standard Rate
Cost Variance = (Rate จริง - Rate มาตรฐาน) x Qty จริง  (= O/(U) Absorption)
Total Variance = Efficiency Variance + Cost Variance
```

- Over: อัตราตั้งสูงไปหรือทำงานเกินแผน; Under: ทำงานน้อยกว่าแผนหรืออัตราต่ำไป
- ตัวอย่างบท 3 (Fig 3.9): Budget 45.90M, Actual 48.72M, Calculated 44.37M, Rate งบ 1,087 vs จริง 1,193, Utilization 58% (40,832 Man-Hrs) vs 60% (42,240) ได้ Cost Variance (4.35M) Under, Efficiency Variance 1.53M Favorable (หนังสือแสดงเป็น (1,530,000) ในตารางส่วน B), Total (2.82M) Unfavorable (derived 48.72M - 45.90M)
- Utilization Factor = Man-Hrs จริง / Available Man-Hrs; 60% ถือว่าสูงแล้ว ห้ามเน้นอย่างเดียวเพราะผู้ปฏิบัติอาจบันทึกไม่ตรง (บท 3 p.73-74)
- Materials วิเคราะห์ Variance ระดับ Job ได้ตรง ส่วนค่าแรงต้องรู้ Cost Variance ระดับหน่วยก่อน (RBMM p.352-353)

## 6. Planned/Unplanned Ratio และการแบ่งต้นทุน (RBMM p.288-289, 297)

- ใช้อัตราส่วน Planned/Unplanned (Man-Hrs) แบ่ง Fixed Cost ให้งานตามแผน/นอกแผน Planned = Total x R/(R+1)
- ตัวอย่าง R = 2.0 ได้ Planned 28,160 และ Unplanned 14,080 Man-Hrs (derived จาก 42,240 x 2/3 และ x 1/3)
- ตัวอย่างค่าจริง (RBMM รูป 10.24 p.306-309): Planned/Unplanned Man-Hrs 1.90 / 2.10 / 2.20 และ Cost 1.60 / 1.80 / 2.00 สำหรับ Process 1/2/3 ควรไปทางเดียวกัน
- กฎ: ถ้า Unplanned ใช้ Direct Purchase สูง แปลว่าสต็อกไม่ถูกต้อง หรือ Unplanned เกินคาด (RBMM p.313)

## 7. ทรัพย์สินและงบดุลที่ฝ่ายบำรุงรักษารับผิดชอบ (RBMM p.277-278, 314)

| รายการ | ผลบัญชี |
|---|---|
| ปรับปรุงสมรรถนะเครื่อง | งบลงทุน ค่าเสื่อมเป็นต้นทุนผลิต ไม่ใช่ของบำรุงรักษา |
| Plant Turnaround | เฉลี่ยรายปี เฉพาะ Materials และจ้างเหมา (CMRP นับค่าแรงพนักงานโรงงานระหว่าง turnaround เป็นต้นทุน event ด้วย ดูข้อขัดแย้งที่ [[Maintenance Budget]] หัวข้อ 8) |
| เครื่องมือ โรงซ่อม คอมพิวเตอร์ | ค่าเสื่อมเป็นต้นทุนบำรุงรักษา |
| อะไหล่สะสมคลัง | ไม่มีค่าเสื่อม มีค่าครอบครอง 15-20% |

## 8. เกณฑ์การกระจาย Fixed Cost จากหน่วยสนับสนุน (RBMM p.341-342)

กระจายตามปริมาณงานบริการ (Service Base) แทนก้อนรวม เช่น ค่า HR = อัตรา x Head Count, ค่าจัดซื้อ = อัตรา/PO x จำนวน PO, ค่าจัดการอะไหล่ = อัตรา/ใบเบิก x จำนวนเบิก ดู [[Job Order Costing]]

## 9. พื้นฐานบัญชีสำหรับผู้บริหารงานบำรุงรักษา (MPM บทที่ 14, p.253-264)

MPM ให้เหตุผลว่าช่าง วิศวกร และผู้บริหารงานบำรุงรักษาต้องเข้าใจบัญชี เพราะผลงานบำรุงรักษากระทบทั้ง **งบดุล** (ฐานะการเงิน) และ **งบกำไรขาดทุน** (ผลประกอบการ) (MPM p.254)

```
Assets = Equity + Liabilities                       (MPM p.254-255)
Capital Employed (CE) = ทุน + หนี้ระยะยาว            (MPM p.256-257)
Working Capital = Current Assets - Current Liabilities = CE - Long Term Assets   (derived จากรูป)
COGS = สินค้าคงคลังต้นงวด + ผลิตเพิ่ม - สินค้าคงคลังปลายงวด   (MPM p.261)
```

| หัวข้อ | สาระ (MPM) |
|---|---|
| สินทรัพย์ถาวร | มีตัวตน (ที่ดิน อาคาร เครื่องจักร) / ไม่มีตัวตน / ลงทุนระยะยาว; มูลค่าลดทุกงวดเพราะตัดเป็นต้นทุน สภาพคล่องต่ำ (p.256) |
| สินทรัพย์หมุนเวียน | เงินสด สินค้า (รวมระหว่างผลิต) ลูกหนี้; ลดความต้องการเงินสดได้ด้วยเครดิต 2-3 เดือน (p.256) |
| หนี้สิน | ระยะยาว (> 1 ปี) คืนด้วยดอกเบี้ย + เงินต้น; ระยะสั้นควรจับคู่กับสินทรัพย์หมุนเวียน (p.256-257) |
| ส่วนของเจ้าของ | ผู้ถือหุ้นได้คืนผ่านปันผลหรือลดทุน/ขายบริษัทเท่านั้น (p.257-258) |
| บัญชีคู่ (Double entry) | ลงซ้าย = Debit, ลงขวา = Credit; เช่น ซื้อวัตถุดิบด้วยเงินสด 100,000 = Credit เงินสด / Debit วัตถุดิบ; บัญชีหลัก 5 บัญชี: ทรัพย์สิน หนี้ ทุน รายจ่าย รายรับ (p.258-260) |
| ค่าเสื่อมราคา | คิดเป็นต้นทุนสินค้า = ลูกค้าจ่ายค่าใช้เครื่องจักร ถ้ากันไว้จะซื้อเครื่องใหม่ได้ (p.261) |

ธุรกิจบริการ (MPM p.261-262)
- ค่าแรงต่องาน = อัตราค่าแรงมาตรฐาน x ชั่วโมงที่ใช้ในงาน; **WIP** = อัตรามาตรฐาน x ชั่วโมง ลงเป็นทรัพย์สินจนออกใบแจ้งหนี้ (Change in WIP คือต้นทุน) ดู [[Job Order Costing]]
- อัตรามาตรฐานต้องเป็น **Full Cost Rate** เพื่อให้ อัตรา x ชั่วโมงทำงาน **ดูดซับ (Absorb)** ค่าใช้จ่ายคงที่จริงทั้งหมด เกิน = Over Absorption, ไม่พอ = Under Absorption ตรงกับหัวข้อ 5
- แก้ Under Absorption: ถ้าไม่ขึ้นราคา ต้องขายงานมากขึ้น หรือปรับขนาดทรัพยากร (คนประจำ เครื่องมือ ค่าการเงิน)

สิ่งที่ฝ่ายบำรุงรักษารับผิดชอบในงบดุล (MPM p.264): ค่าเสื่อมโรงซ่อมและเครื่องมือ, มูลค่าอะไหล่ที่ซื้อด้วยทุน/เงินกู้ซึ่งเกิดค่าใช้จ่ายทางการเงิน (WACC), ค่าการเงินจากการครอบครองทรัพย์สินบำรุงรักษา สอดคล้องกับกลุ่ม 2 Asset ในหัวข้อ 2 และหัวข้อ 7

## 10. ตัวอย่าง XYZ: แยก Fixed / Variable และ Full Fixed Cost Rate (MPM p.107-109, 179-183)

ตัวอย่างบริษัทสมมติ XYZ หน่วยล้านบาท (M฿) ใช้ซ้ำในบทที่ 6, 7, 10, 12 ของ MPM

| รายการ | 1998 | 1999 | 2000 |
|---|---|---|---|
| ค่าบริหารจัดสรรจากส่วนกลาง | 12.0 | 15.0 | 18.0 |
| เครื่องมือ: ค่าเสื่อม + ต้นทุนการเงิน (ทรัพย์สิน 97.1) | 16.0 | 16.0 | 16.0 |
| เงินเดือนค่าแรง (ทางอ้อม 10.0 + ทางตรง) | 68.1 | 74.0 | 62.1 |
| ต้นทุนการเงินอะไหล่ (10% WACC ของคงคลัง 405.0 / 407.4 / 521.2) | 40.5 | 40.7 | 52.1 |
| **รวมค่าใช้จ่ายคงที่** | **136.6** | **145.8** | **148.2** |
| อะไหล่ใช้ (เบิกคลัง + ซื้อตรง) | 130.1 | 193.7 | 315.6 |
| จ้างเหมาค่าแรง | 16.8 | 12.7 | 11.3 |
| ซ่อมใหญ่เฉลี่ย/ปี (110 / 3 ปี) | 36.7 | 36.7 | 36.7 |
| **รวมค่าใช้จ่ายแปรผัน** | **183.6** | **243.1** | **363.6** |
| รวมค่าใช้จ่ายซ่อมบำรุง | 320 | 389 | 512 |

```
Fixed    = ค่าจัดสรร + (ค่าเสื่อม + การเงินเครื่องมือ) + เงินเดือนค่าแรง + ต้นทุนการเงินอะไหล่
Variable = อะไหล่ใช้ + จ้างเหมา + ซ่อมใหญ่เฉลี่ย/ปี
Full Fix Cost Rate = Fixed / (ชั่วโมง-คนทั้งหมด x Utilization Factor)
```

| บุคลากร/อัตรา | 1998 | 1999 | 2000 |
|---|---|---|---|
| พนักงานทางตรง (คน) | 116 | 114 | 100 |
| ชั่วโมง-คนทั้งหมด/ปี | 228,288 | 224,352 | 196,800 |
| Utilization Factor | 50% | 50% | 50% |
| อัตราเฉลี่ยค่าแรงทางตรง (บาท/ชม.-คน) | 237.1 | 265.8 | 246.7 |
| **Full Fix Cost Rate** (บาท/ชม.-คน) | **1,196.8** | **1,299.3** | **1,506.4** |
| Full rate ไม่รวมค่าครอบครองอะไหล่ (Fixed หักต้นทุนการเงินอะไหล่ = 96.1 / 105.0 / 96.1) | 841.9 | 936.1 | 976.8 |

- MPM เรียก Full Fix Cost Rate ว่าอัตรา Break Even ถ้าแยกหน่วยบำรุงรักษาเป็น Profit Center (ยังไม่รวมอะไหล่ที่เบิกใช้) ใช้เทียบ make-or-buy ดู [[Maintenance Outsourcing]]
- ตรวจ (derived): 12 + 16 + 68.1 + 40.5 = 136.6; 136.6M / 114,144 = 1,196.7; ปี 1999 องค์ประกอบรวม 145.7 (พิมพ์ 145.8); 148.2M / 98,400 = 1,506.1 (พิมพ์ 1,506.4; รูป 7.17 พิมพ์ 1,508.4 น่าจะพิมพ์ผิด)
- ข้อผิดในเล่ม (derived): ชั่วโมง-คนใช้ 1,968 ชม./คน/ปี แต่อัตราเฉลี่ย 237.1 คำนวณด้วย 8 x 22 x 12 = 2,112 ชม./คน (58.1M / (116 x 2,112) = 237.1); ถ้าใช้ 1,968 จะได้ 254.5 / 285.3 / 264.7
- ข้อความ p.183 อ้างว่าอัตราเพิ่มเพราะ "เพิ่มขนาดทรัพยากร" แต่ตัวเลขแสดงคนทางตรงลด 116 -> 100; Fixed เพิ่มเพียง 8.5% จากต้นทุนการเงินอะไหล่และค่าจัดสรร ส่วนอัตราเพิ่ม 26% ส่วนใหญ่เพราะชั่วโมงลด 14% (derived)
- ซ่อมใหญ่ถูกนับในหมวดแปรผันของตารางนี้ แม้ MPM p.114 จัด Turnaround เป็น Asset Account ตัดจ่าย ดู [[Maintenance Budget]] หัวข้อ 9.2
- Fixed ของ XYZ ไม่มีกลุ่ม Operating และ Provision แยกเหมือน 5 กลุ่มของ RBMM (หัวข้อ 2) แต่โครงสร้าง Personnel + Asset (รวมค่ามีอะไหล่) + Allocation ตรงกัน

## 11. ค่าแรงบำรุงรักษา: ชั่วโมงพร้อมทำงาน อัตราค่าแรง และ Utilization (MPM p.183-189)

### 11.1 ชั่วโมงพร้อมทำงานต่อคนต่อปี (MPM p.185-186)

| รายการ | ค่า |
|---|---|
| วันใน 1 ปี | 365 |
| หัก วันหยุดสุดสัปดาห์ / วันหยุดประจำปี / วันลา | (104) / (15) / (15) |
| วันพร้อมทำงาน | 231 วัน |
| ชั่วโมงปกติ 231 x 8 | 1,848 |
| หัก อบรม 5% และงานภายในจิปาถะ 5% | (92.4) + (92.4) |
| **ชั่วโมงพร้อมทำงานทั้งสิ้น** | **1,663.2 ชม./คน/ปี** |

- Utilization = ชั่วโมงทำงานจริง (จากระบบควบคุมงาน) / ชั่วโมงพร้อมทำงาน เช่น 1,000 / 1,663.2 = 60.1%; อัตราค่าแรงจริงต้องหารด้วยชั่วโมงที่ใช้ (1,000) ไม่ใช่ 1,663.2 หรือ 1,848
- **ความต่างของค่าสมมติ (ไม่ใช่ contested)**: MPM 1,663.2 ชม. (p.186) และตาราง XYZ ใช้ 1,968 / 2,112 ชม. (p.108, 182-183) ขณะที่ RBMM ใช้ราว 1,600 Man-Hrs/คน/ปี (RBMM p.280) และ 220 x 8 = 1,760 (RBMM p.296) — ผู้เขียนกลุ่มเดียวกันใช้ค่าตัวอย่างต่างกัน ถ้านำไปใช้ให้คำนวณจากปฏิทินและนโยบายลาของหน่วยงานเอง

### 11.2 ตัวอย่างอัตราค่าแรงแผนกไฟฟ้า 375 บาท/ชม.-คน (MPM p.186-188)

| รายการ | บาท/ปี |
|---|---|
| ทางตรง 22 คน x 20,000 บาท/คน/เดือน (รวมผลประโยชน์) x 12 | 5,280,000 |
| ทางอ้อม (หัวหน้าแผนก 1 + หัวหน้ากลุ่ม 2) | 1,080,000 |
| บริหารบำรุงรักษา + วางแผน (25% ของ 4,000,000) | 1,000,000 |
| บริหารโรงงานกระจายมา (30% ของ 3,000,000) | 900,000 |
| **รวม** | **8,260,000** |
| ชั่วโมงที่บันทึกได้ 22,000 ชม.-คน (Utilization 60%) | **375 บาท/ชม.-คน** |

| Utilization | 20% | 30% | 40% | 50% | 60% | 70% |
|---|---|---|---|---|---|---|
| บาท/ชม.-คน | 1,125.0 | 750.0 | 562.5 | 450.0 | 375.0 | 321.4 |

- ตรวจ (derived): ตาราง = 375 x 60 / Utilization ตรงทุกค่า; 22 x 1,663.2 = 36,590 ชม. -> 22,000 / 36,590 = 60.1%
- ข้อผิดในเล่ม (derived): ข้อความเขียน "20,000 บาทต่อปี" ต้องเป็นต่อเดือน (440,000/เดือน = 5,280,000/ปี); ค่าบริหารโรงงาน 900,000 เป็นส่วนของบำรุงรักษาทั้งฝ่ายแต่ใส่ให้แผนกไฟฟ้าทั้งก้อน (ถ้ากระจาย 25% จะเหลือ 225,000 และอัตรา 344.8 บาท/ชม.)

### 11.3 ธรรมชาติค่าแรงเทียบเครื่องจักร 8 ข้อ (MPM p.183-184)

1. ค่าแรงเกิดตลอดเวลาไม่ว่างานมากหรือน้อย
2. มีค่าใช้จ่ายสมทบต่อหัวไม่น้อย (รักษาพยาบาล สวัสดิการ)
3. เพิ่มทุกปีอย่างน้อย 2-6% (p.183; แต่ p.189 เขียน 5-6% ไม่สอดคล้องกันภายในเล่ม)
4. คนมีมูลค่าเพิ่ม (appreciate) ต่างจากเครื่องที่เสื่อมราคา (depreciate)
5. เครื่องขายซากได้ แต่ปลด/เกษียณพนักงานบริษัทต้องจ่าย
6. เหมือนกัน: มีวัตถุประสงค์ในการมี เครื่องต้อง maintenance คนต้องพัฒนา และมีการปลดระวาง
7. เหมือนกัน: ต้องถามว่า utilize คุ้มหรือไม่ (ชั่วโมงใช้จริง / ชั่วโมงพร้อมใช้)
8. คนไม่อยู่ในงบดุลแต่อยู่ในงบกำไรขาดทุน; เงินเดือนรวม 500,000/ปี นาน 20 ปี เสมือนมีทรัพย์สิน 10,000,000 บาทในงบดุล

ค่าใช้จ่ายบุคลากรที่แท้จริง = เงินเดือน 12 เดือน + โบนัส + สวัสดิการ + อบรม + ค่าจัดการ/ผู้บริหารที่ลงชั่วโมงไม่ได้ (MPM p.184-185); ข้อสรุปสำคัญ: ต้นทุนต่องานไม่คงที่ ขึ้นกับ Utilization ของปีนั้น และ Utilization สูงขึ้น อัตราต่อชั่วโมงต่ำลง (MPM p.188-189) สอดคล้องกับหัวข้อ 4 (RBMM บท 3 p.65)

## 12. Over/(Under) Reserved = Over/(Under) Absorption (MPM p.134-137, 262)

- MPM บทที่ 7 เรียกกลไกในหัวข้อ 5 ว่า **Over/(Under) Reserved** สูตรและเครื่องหมายเดียวกับ RBMM: ค่าคำนวณด้วยอัตรามาตรฐาน - ค่าใช้จ่ายจริง (ลบ = Under) ส่วนบทที่ 14 ใช้คำ Over/Under Absorption ตรงกับ RBMM
- ตัวอย่าง (MPM p.135): ใช้ 90,000 ชม. x 976.8 บาท = 87.91 M฿ เทียบค่าใช้จ่ายจริง 96.1 M฿ -> **(8.2) M฿ Under** (derived: = (98,400 - 90,000) x 976.8 คือชั่วโมงที่ต่ำกว่า utilization 50% ที่วางไว้)
- (Under) = ใช้ทรัพยากรไม่เต็มตาม Utilization ที่กำหนด (ส่วนมากขายชั่วโมงได้น้อยกว่างบ); Over = ใช้ทรัพยากรเกินที่กำหนด
- ค่าแรงมาตรฐาน (Full Cost Rate) แปรผันตาม Utilization Factor โดยตรง (MPM p.137) รายละเอียดการปิดบัญชี ดู [[Job Order Costing]]

## 13. Contested: ค่าครอบครองอะไหล่ (Holding Cost) — ข้อขัดแย้ง MPM-C1 (เพิ่ม 2026-10-28)

| แหล่ง | ค่า | บริบท |
|---|---|---|
| MPM (ข้อความ) | ค่าครอบครอง 20-40% ของมูลค่าคงคลัง (MPM p.84) | บทอะไหล่ |
| MPM (ตัวอย่างตัวเลข) | คิดเฉพาะต้นทุนการเงิน 6-10% (MPM p.17, p.108, p.180-181); XYZ = 10% WACC (40.5 / 405.0, 52.1 / 521.2) | ไม่รวมค่าเก็บรักษา/ล้าสมัย |
| RBMM | 15-20% ของราคาซื้อต่อปี (บท 3 p.68; บท 10 p.314) และช่วง 15-25% (p.295) | หัวข้อ 3 และ 7 |

- MPM ไม่สอดคล้องภายในเล่ม (ข้อความ 20-40% แต่ตัวอย่างใช้ 6-10%) และต่างจาก RBMM ทั้งสองทิศ
- ผลต่อการใช้งาน: Full Fix Cost Rate ของ XYZ (หัวข้อ 10) จะสูงขึ้นถ้าใช้ค่าครอบครองเต็ม เช่นที่ 15% ต้นทุนถืออะไหล่ปี 2000 จะเป็น 78.2 M฿ แทน 52.1 (derived) ดังนั้นการเทียบ make-or-buy ต้องระบุฐานที่ใช้
- **ยังไม่ resolve** ผู้ใช้ต้องเลือกอัตราที่ใช้ภายใน (แนะนำระบุแยก finance cost กับ storage/obsolescence) ตั้ง `contested: true`
- ความต่างอื่นที่ไม่ใช่ contested: สัดส่วนอะไหล่ในค่าบำรุงรักษา XYZ 41% (1998) ถึง 62% (2000) (derived: 130.1/320, 315.6/512) เทียบข้อความ RBMM 60-70%

## เชื่อมโยงกับ compressor failure hierarchy

หนังสือไม่มีข้อมูล failure หรือรหัส [[OREDA]] / [[ISO 14224]] ในส่วนต้นทุน ความเชื่อมที่ใช้งานได้:
- งาน CM-Unplanned ที่เกิดจาก failure mode ใน [[Failure Mode]] (เช่น ELU, ELP, AIR) ควรบันทึก Man-Hrs, Stock Parts และ Outsource แยกใน Work Order เพื่อสร้าง cost per failure ต่อ [[Maintainable Item]]
- [[Failure Cause Codes]] และ [[Resolution Codes]] ใช้จัดกลุ่มต้นทุนซ่อมได้ถ้ารหัสถูกผูกกับ Work Order (ข้อเสนอของ wiki ไม่ใช่ข้อความหนังสือ)
- ตัวอย่าง 8 ข้อของค่าแรงและตาราง Utilization ของ MPM ใช้คิดต้นทุนชั่วโมง-คนของงานซ่อม [[Compressor]] ได้ แต่ต้องใช้ชั่วโมงพร้อมทำงานของ rotation offshore จริง ไม่ใช่ 1,663.2 ของหนังสือ (การตีความของ wiki)
- ไม่มีข้อมูลต้นทุนจริงของ compressor ใน sources

## ดูเพิ่ม

- [[Maintenance Budget]] — การนำโครงสร้างนี้ไปตั้งงบ
- [[Job Order Costing]] — ใช้ Rate เดียวกันในธุรกิจบริการ
- [[Maintenance KPIs]]
- [[Spare Parts Management]]
- [[CMMS]]
- [[Maintenance Strategic Report]]
- [[Maintenance Profit Maker Book]]
- [[Maintenance Outsourcing]]

## Triplets

- [[Maintenance Cost Structure]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapters 3, 10, 11
- Total Maintenance Cost [has_formula:: Full Fixed Cost + Materials + Losses] (RBMM p.278-279)
- Full Fixed Cost [part_of:: Total Maintenance Cost] Man-Hrs planned and unplanned
- Materials [part_of:: Total Maintenance Cost] variable cost
- Losses [part_of:: Total Maintenance Cost] tracked for management, not booked from budget (RBMM p.288)
- Personnel [part_of:: Full Fixed Cost] group 1 (RBMM p.280, 337)
- Asset [part_of:: Full Fixed Cost] group 2, includes stock spare holding cost (RBMM p.280, 337)
- Operating [part_of:: Full Fixed Cost] group 3 (RBMM p.280, 337)
- Allocation [part_of:: Full Fixed Cost] group 4 (RBMM p.280, 337)
- Provision [part_of:: Full Fixed Cost] group 5 (RBMM p.280, 337)
- Outsource [part_of:: Materials] (RBMM p.283-284)
- Direct Purchase Parts [part_of:: Materials] (RBMM p.283-284)
- Stock Parts [part_of:: Materials] (RBMM p.283-284)
- Direct Purchase Parts [applies_to:: Planned Maintenance] Scheduled PM, not stocked (RBMM p.283-284)
- Stock Parts [applies_to:: CM-Unplanned] only (RBMM p.283-284)
- Outsource [applies_to:: Labour Overflow or Special Skill] regular contracts count as Fixed; none for unplanned (RBMM p.283-284)
- Blanket Order [related_to:: Stock Parts] vendor stores parts in our store, billed on issue (RBMM p.289)
- Full Fixed Cost [has_value:: 45,900,000 THB] A5 budget, actual 48,720,000 (RBMM p.295, Fig 3.4/3.5)
- Current Asset Spare Holding [has_value:: 18,000,000 THB] A3.2 budget, 15% of 120,000,000 (RBMM p.295)
- Long Term Asset [has_value:: 520,000 THB] A3.1 actual, chapter 10 (RBMM p.295)
- Long Term Asset [has_value:: 320,000 THB] A3.1 actual, alternate reading in chapter 3
- Materials [has_value:: 158,645,455 THB] A9 budget, actual 161,900,500 (RBMM p.295)
- Total Maintenance Cost [has_value:: 204,545,455 THB] A10 budget, actual 210,620,500, A-B 6,075,045 (RBMM p.295)
- Full Fixed Cost [produces:: Available Man-Hrs] about 1,600 Man-Hrs per person per year (RBMM p.280)
- Outsource Policy [differs_from:: Full Fixed Cost] high outsourcing lowers Fixed Cost but raises Outsource and parts (RBMM p.280-281)
- Holding Cost [has_value:: 15-20%] of purchase price per year (RBMM ch3 p.68, ch10 p.314)
- Holding Cost [has_value:: 15-25%] range at p.295 (RBMM p.295)
- Full Fixed Cost Rate [has_formula:: Full Fixed Cost / Man-Hrs used (planned)] (RBMM p.281-282, 296)
- Available Man-Hrs [has_formula:: Direct Persons x working days/year x hours/day] (RBMM p.281-282, 296)
- Man-Hrs Used [has_formula:: Available Man-Hrs x Utilization Rate] (RBMM p.281-282, 296)
- Full Fixed Cost Rate [has_value:: about 1,087 THB/Man-Hr] 40 x 220 x 8 = 70,400, 60% = 42,240 (RBMM p.296)
- Full Fixed Cost Rate [depends_on:: Man-Hrs Used] more Man-Hrs lower rate (RBMM ch3 p.65)
- Full Fixed Cost Rate [has_value:: Engineer 1,200 / 900 / 600; Technician 900 / 600 / 400; Labor 300 THB/Man-Hr] table 10.6 uses Labor 200 (RBMM p.281)
- Calculated Cost [has_value:: 1,865,000 THB] 3,250 Man-Hrs, average rate 574 (RBMM Fig 10.6-10.7 p.282)
- Over/(Under) Absorption [has_value:: Under 135,000 THB] actual Full Fixed Cost 2,000,000 - 1,865,000 (RBMM p.282)
- Over/(Under) Absorption [has_formula:: calculated cost (Actual Man-Hrs x Standard Rate) - Actual Full Fixed Cost] (RBMM p.282, 349-353)
- Efficiency Variance [has_formula:: (actual Qty - budget Qty) x Standard Rate] (RBMM p.349-353)
- Cost Variance [has_formula:: (actual Rate - standard Rate) x actual Qty] equals O/(U) Absorption (RBMM p.349-353)
- Total Variance [has_formula:: Efficiency Variance + Cost Variance] (RBMM p.349-353)
- Cost Variance [alias_of:: Over/(Under) Absorption]
- Cost Variance [has_value:: (4.35M) Under] chapter 3 Fig 3.9 example (RBMM ch3 p.72-73)
- Efficiency Variance [has_value:: 1.53M Favorable] shown as (1,530,000) in part B (RBMM ch3 Fig 3.9)
- Total Variance [has_value:: (2.82M) Unfavorable] 48.72M - 45.90M (RBMM ch3 Fig 3.9)
- Utilization Factor [has_formula:: actual Man-Hrs / Available Man-Hrs] 60% considered high (RBMM ch3 p.73-74)
- Planned Fixed Cost [has_formula:: Total x R/(R+1)] R = Planned/Unplanned Man-Hr ratio (RBMM p.288-289, 297)
- Planned Fixed Cost [has_value:: 28,160 Man-Hrs planned / 14,080 unplanned] R = 2.0 (RBMM p.297)
- Planned/Unplanned Ratio [has_value:: Man-Hrs 1.90 / 2.10 / 2.20; Cost 1.60 / 1.80 / 2.00] Process 1/2/3 actual (RBMM Fig 10.24 p.306-309)
- Direct Purchase Parts [related_to:: Stock Parts] high direct purchase in unplanned work = wrong stocking or excess unplanned (RBMM p.313)
- Improvement Maintenance [has_category:: capital budget] depreciation is production cost (RBMM p.277-278)
- Workshop Tools and Computers [has_category:: maintenance cost] depreciation (RBMM p.277-278)
- Stock Parts [has_category:: no depreciation, 15-20% holding cost] (RBMM p.314)
- Fixed Cost Allocation [uses:: Service Base] HR x Head Count, purchasing per PO, spare handling per issue (RBMM p.341-342)
- Fixed Cost Allocation [related_to:: [[Job Order Costing]]]
- [[Maintenance Cost Structure]] [defined_in:: [[Maintenance Profit Maker Book]]] chapters 6, 7, 10, 14 (MPM)
- Balance Sheet [has_formula:: Assets = Equity + Liabilities] (MPM p.254-255)
- Capital Employed [has_formula:: equity + long term liabilities] (MPM p.256-257)
- Working Capital [has_formula:: Current Assets - Current Liabilities] equals CE - Long Term Assets, derived from figure (MPM p.257)
- COGS [has_formula:: opening inventory + production - closing inventory] (MPM p.261)
- Double Entry [has_part:: Debit] left side (MPM p.259)
- Double Entry [has_part:: Credit] right side (MPM p.259)
- Main Accounts [has_value:: 5] assets, liabilities, equity, expense, revenue (MPM p.258-260)
- Service Labour Cost [has_formula:: standard labour rate x hours on job] (MPM p.261)
- WIP [has_formula:: standard labour rate x hours] asset until invoiced; change in WIP is cost (MPM p.261)
- Under Absorption [resolved_by:: sell more hours or resize resources] if price not raised (MPM p.262)
- Maintenance Balance Sheet Responsibility [has_part:: workshop and tool depreciation] (MPM p.264)
- Maintenance Balance Sheet Responsibility [has_part:: spare inventory finance cost at WACC] (MPM p.264)
- XYZ Fixed Cost [has_formula:: allocation + tool depreciation and finance + salaries + spare finance cost] (MPM p.180-181)
- XYZ Variable Cost [has_formula:: spares used + contract labour + turnaround per year] (MPM p.180-181)
- XYZ Fixed Cost [has_value:: 136.6 / 145.8 / 148.2 M THB] 1998 / 1999 / 2000 (MPM p.108, 179)
- XYZ Variable Cost [has_value:: 183.6 / 243.1 / 363.6 M THB] 1998 / 1999 / 2000 (MPM p.108, 179)
- XYZ Total Maintenance Cost [has_value:: 320 / 389 / 512 M THB] 1998 / 1999 / 2000 (MPM p.108, 179)
- Full Fix Cost Rate [has_formula:: Fixed / (total man-hours x Utilization Factor)] (MPM p.182-183)
- Full Fix Cost Rate [has_value:: 1,196.8 / 1,299.3 / 1,506.4 THB per man-hour] XYZ 1998-2000 at 50% utilization (MPM p.183)
- Full Fix Cost Rate [alias_of:: Full Fixed Cost Rate] MPM spelling
- Full Rate Excl Spare Holding [has_value:: 841.9 / 936.1 / 976.8 THB per man-hour] XYZ (MPM p.109)
- Full Fix Cost Rate [differs_from:: Direct Labour Average Rate] 1,196.8 vs 237.1 THB in 1998 (MPM p.183)
- Direct Labour Average Rate [contradicts:: Man-Hours Basis 1,968] book uses 2,112 h for rate and 1,968 h for man-hours, derived
- Available Hours per Person [has_value:: 1,663.2 h per year] 231 days x 8 less 5% training and 5% internal (MPM p.185-186)
- Available Hours per Person [has_value:: 1,600 h per year] approx (RBMM p.280)
- Available Hours per Person [has_value:: 1,760 h per year] 220 x 8 example (RBMM p.296)
- MPM Available Hours [differs_from:: RBMM Available Hours] example assumptions differ, not contested
- Labour Rate Example [has_value:: 375 THB per man-hour] electrical section, 8,260,000 / 22,000 h at 60% utilization (MPM p.186-188)
- Labour Rate Example [has_value:: 1,125.0 / 750.0 / 562.5 / 450.0 / 375.0 / 321.4 THB] at utilization 20 / 30 / 40 / 50 / 60 / 70% (MPM p.188)
- Labour Rate [depends_on:: Utilization Factor] higher utilization lower rate (MPM p.188-189)
- Labour Cost [has_value:: 8 traits vs machines] people appreciate, no salvage, off balance sheet but like an asset (MPM p.183-184)
- Labour Cost Growth [has_value:: 2-6% per year] (MPM p.183)
- Labour Cost Growth [has_value:: 5-6% per year] internal inconsistency in book (MPM p.189)
- Over/(Under) Reserved [alias_of:: Over/(Under) Absorption] same formula and sign (MPM p.134-136)
- Over/(Under) Reserved [has_value:: (8.2) M THB Under] 90,000 h x 976.8 = 87.91 vs actual 96.1 (MPM p.135)
- Spare Share of Maintenance Cost [has_value:: 41% to 62%] XYZ 1998 to 2000, derived (MPM p.108)
- Holding Cost [has_value:: 20-40%] of stock value, text (MPM p.84) [contested:: true]
- Holding Cost [has_value:: 6-10% finance cost only] book examples incl. XYZ 10% WACC (MPM p.17, p.108, p.180-181) [contested:: true]
- Holding Cost [has_value:: 15-20%] RBMM (RBMM ch3 p.68, ch10 p.314) [contested:: true]
- MPM Holding Cost [contradicts:: RBMM Holding Cost] MPM-C1, unresolved [contested:: true]

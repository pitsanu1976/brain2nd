---
title: Maintenance Cost Structure
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [cost, budget, maintenance-management, kpi, spare-parts, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Maintenance Cost Structure

โครงสร้างต้นทุนบำรุงรักษาตาม RBMM แบ่งเป็น **Full Fixed Cost** (ค่าใช้จ่ายคงที่ครบถ้วนที่เห็นในรูป Man-Hrs ใน Work Order) กับ **Materials** (ค่าใช้จ่ายแปรผัน: อะไหล่ + จ้างเหมา) และมีกลไกเชื่อมคือ **Full Fixed Cost Rate** (อัตราค่าแรงมาตรฐาน) กับ **Over/(Under) Absorption** (ส่วนต่างระหว่างค่าที่คิดด้วยอัตรามาตรฐานกับค่าจริง) หน้านี้รวมเนื้อหาจากบท 3, 10 และ 11 ของหนังสือ การนำไปทำงบดู [[Maintenance Budget]] ตัวเลขทั้งหมดเป็นตัวอย่างสมมติของหนังสือ

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
- เป้า 0 ที่ตั้งใจ: Stock ของงานตามแผน, Direct Purchase ของงานนอกแผน, Outsource ของงานนอกแผน; ใช้ **Blanket Order** (ผู้ขายนำอะไหล่มาเก็บในคลังเรา คิดเงินเมื่อเบิก) เป็นกลไกพิเศษ (RBMM p.289)
- ค่าครอบครองอะไหล่คลังประมาณ 15-20% ของราคาซื้อต่อปี (บท 3 p.68; บท 10 p.314) หนังสือให้ช่วง 15-25% ที่ p.295 ควรโอนกลับไปยังหน่วยที่ขอสะสมอะไหล่ ดู [[Spare Parts Management]]

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

## เชื่อมโยงกับ compressor failure hierarchy

หนังสือไม่มีข้อมูล failure หรือรหัส [[OREDA]] / [[ISO 14224]] ในส่วนต้นทุน ความเชื่อมที่ใช้งานได้:
- งาน CM-Unplanned ที่เกิดจาก failure mode ใน [[Failure Mode]] (เช่น ELU, ELP, AIR) ควรบันทึก Man-Hrs, Stock Parts และ Outsource แยกใน Work Order เพื่อสร้าง cost per failure ต่อ [[Maintainable Item]]
- [[Failure Cause Codes]] และ [[Resolution Codes]] ใช้จัดกลุ่มต้นทุนซ่อมได้ถ้ารหัสถูกผูกกับ Work Order (ข้อเสนอของ wiki ไม่ใช่ข้อความหนังสือ)
- ไม่มีข้อมูลต้นทุนจริงของ compressor ใน sources

## ดูเพิ่ม

- [[Maintenance Budget]] — การนำโครงสร้างนี้ไปตั้งงบ
- [[Job Order Costing]] — ใช้ Rate เดียวกันในธุรกิจบริการ
- [[Maintenance KPIs]]
- [[Spare Parts Management]]
- [[CMMS]]
- [[Maintenance Strategic Report]]

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

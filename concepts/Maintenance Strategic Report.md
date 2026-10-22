---
title: Maintenance Strategic Report
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [kpi, budget, cost, cmms, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Maintenance Strategic Report

รายงานสรุปสั้น (A4 หนึ่งถึงสองแผ่น) ที่ RBMM บทที่ 3 (book p.55-87) เสนอเป็นสะพาน Top Down ระหว่างงานบริหารกับงานเทคนิค ดึงตรงจาก CMMS/ERP ชี้ประเด็นที่น่าจะเป็นปัญหาแล้วนำไปสู่รายงานเชิงลึกเท่าที่จำเป็น โครงสร้างมี 4 ส่วนหลัก (A ถึง D) และภายหลังเพิ่มส่วน E (สมรรถนะการตั้งงบ) บทที่ 10 นำรายงานเดียวกันมาใช้ปรับงบ ข้อมูลตัวเลขเป็นตัวอย่างจากหนังสือ (หน่วยบาท)

## 1. เหตุผลและคุณสมบัติ (RBMM p.56-59)

- รายงานแบบ Bottom Up ที่มีมากเกินไป (บางแห่ง 100 รายงาน) ผู้บริหารอ่านไม่เข้าใจ
- รายงานต้องออกตรงจาก CMMS โดยไม่จัดทำซ้ำ เพื่อสร้างความร่วมมือเก็บข้อมูล ข้อมูลเดียวที่ต้องกรอกเพิ่มคือ Man-Hrs ใน Work Order (p.66)
- คุณสมบัติ: สั้น, รูปแบบเดียวทุกระดับ, แปลง Data เป็น Information เป็น Knowledge เป็น Action, เก็บเฉพาะข้อมูลที่ใช้, ผู้รับผิดชอบอธิบายผลตนเองได้ (Accountability), เป็นส่วนหนึ่งของวงจรงบ, consolidate หลายหน่วยงานและเปรียบเทียบข้ามหน่วยได้, รายงานลึกแบบ on demand
- สอดคล้องกับ "Problem of Reporting?" ใน Fig 2.4 และ 3.1 ดู [[Maintenance Efficacy Pyramid]]

## 2. โครงสร้างเนื้อหา

| ส่วน | เนื้อหา | หน้า |
|---|---|---|
| A | ขนาดองค์กรและค่าใช้จ่ายรวม (fixed cost, materials) | p.66-70 |
| B | ดัชนีชี้นำหลัก: cost/efficiency และ stock performance | p.70-75 |
| C | การกระจาย Man-Hrs/ค่าใช้จ่ายไปยัง Process/Area/Criticality และ planned vs unplanned | p.76-83 |
| D | ผลลัพธ์ต่อเครื่องจักร: ผลผลิต/OEE และ cost per unit | p.83-84 |
| E | สมรรถนะการจัดการงบ: งบสุทธิ, สำรองค่าใช้จ่าย, สำรองค่าสูญเสีย | p.84-86 |

ผัง Asset Performance Management (รูป 3.2) แบ่ง Think แล้ว Perform แล้ว Results: Maintenance Strategy (Criticality/Prioritization, Organization Sizing, Tools/Methods), Work Performance, Cost Performance, Asset Performance (Equipment: R/A/M; Component: Failure Rate; Integrity: Safety, Protection, Hidden Failures) (p.59)

## 3. Accountability (RBMM p.60)

Accountability Reporting Matrix (รูป 3.3): แถว = หน่วยงานบำรุงรักษา (Man-Hrs, Materials) คอลัมน์ = Asset ผลรวมแต่ละแกน = ต้นทุนต่อเครื่องและต่อหน่วยงาน ค่าใช้จ่ายครบถ้วนต้องรวมทางอ้อมด้วย (ค่าเสื่อมช่วงเครื่องหยุด, วัตถุดิบทิ้ง, สินค้าไม่ได้คุณภาพ, ค่าซ่อมชั่วคราว) ดู [[Maintenance Cost Structure]]

## 4. ส่วน A: ตัวอย่างตัวเลข (รูป 3.4-3.5, RBMM p.64-70)

| รหัส | รายการ | Actual (A) | Variance (A-B) | Budget (B) |
|---|---|---|---|---|
| A1 | Personnel Costs | 25,000,000 | 5,000,000 | 20,000,000 |
| A2 | Operating Costs | 3,500,000 | 1,100,000 | 2,400,000 |
| A3 | Total Asset Costs | 19,720,000 | (3,280,000) | 23,000,000 |
| A3.1 | Cost of Long Term Asset | 520,000 | (4,480,000) | 5,000,000 |
| A3.2 | Cost of Current Asset | 19,200,000 | 1,200,000 | 18,000,000 |
| A4 | Allocation Costs | 500,000 | - | 500,000 |
| A5 | Total Fixed Cost | 48,720,000 | 2,820,000 | 45,900,000 |
| A6 | Parts from Stock | 54,000,000 | 1,118,182 | 52,881,818 |
| A7 | Direct Purchase Parts | 78,350,000 | (650,000) | 79,000,000 |
| A8 | Outsource | 29,550,500 | 2,786,864 | 26,763,636 |
| A9 | Material Cost | 161,900,500 | 3,255,045 | 158,645,455 |
| A10 | Total Maintenance Cost | 210,620,500 | 6,075,045 | 204,545,455 |

ความสัมพันธ์: A3 = A3.1 + A3.2; A5 = A1+A2+A3+A4; A9 = A6+A7+A8; A10 = A5+A9 (ตรวจแล้วตรงกับตัวเลข: เช่น 25.0 + 3.5 + 19.72 + 0.5 = 48.72 ล้าน)

**ข้อควรระวังตัวเลข:** A3.1 Actual หน้า p.64 อ่านเป็น 320,000 แต่ p.66 และบทที่ 10 (รูป 10.22) เป็น 520,000 ค่า 520,000 สอดคล้องกับ A3 = 19,720,000 (520,000 + 19,200,000) จึงใช้ 520,000 (สาเหตุน่าจะเป็นภาพความละเอียดต่ำ [อ่านไม่ออกชัด] ไม่ใช่ความขัดแย้งของ source)

- A1-A4 คือ fixed cost เกิดตลอดไม่ว่ามีผลผลิตหรือไม่ ตั้งงบง่ายลดยาก (p.69)
- A3.1 ควรโอนค่าใช้จ่ายทรัพย์สินถาวรเข้าหน่วยที่ใช้ (p.67-68)
- A3.2 holding cost ประมาณ 15-20% ของราคาซื้ออะไหล่ต่อปี มักถูกรวมใน fixed cost จนผู้ขอ stock ไม่รู้สึก ควรโอนกลับหน่วยที่ขอสะสม ลดได้ด้วย PM ที่มีสัมฤทธิผล (p.68)
- A6 stock ใช้สู้ breakdown/CM-Unplanned เท่านั้น A7 ซื้อตรงควรเป็นงาน scheduled PM; ถ้าไม่สอดคล้องกับ C2 แปลว่าเลือก PM ไม่ถูก (p.70)
- ดัชนี B ดูรายละเอียดที่ [[Maintenance KPIs]]

## 5. ส่วน C และ D สรุป

- C1.1 ถึง C1.3 วัดความคืบหน้า RCM: P1/P2/P3 %Critical PM = 71.3 / 62.9 / 51.9; Critical Compliance 100.0 / 96.6 / 100.0; Non-Critical Compliance 75.9 / 99.3 / 95.0
- Planned/Unplanned ratio (Man-Hrs) 1.90 / 2.10 / 2.20; (Cost) 1.60 / 1.80 / 2.00
- Man-Hrs รวม 40,832 (10,721 / 13,525 / 16,586); Planned cost 135,942,717; Unplanned cost 74,677,783; Production loss 7,050,000 (ข้อมูล ch10: แบ่ง Planned 1,410,000 และ Unplanned 5,640,000)
- ถ้ากลยุทธ์ถูก ค่าต่อไปนี้ควรใกล้ 0: stock parts ในงานตามแผน, outsource ของงานนอกแผน, direct purchase ของงานนอกแผน, loss จากงานตามแผน (รูป 3.14, p.81)
- Unplanned non-stocked parts ที่มีค่า = เบิกแล้วไม่มีของ (service factor ต่ำกว่า 100%) แนะนำ Blanket Order กับ vendor (p.82-83)
- D: ดู cost per unit ควบกับ OEE ดู [[Availability and OEE]]

## 6. ส่วน E: สมรรถนะการจัดการงบ (รูป 3.18-3.20, RBMM p.84-86; ซ้ำใน ch10 p.309-312)

```
Net Budget = Gross Budget - Provision for Costs - Provision for Losses
```

| รหัส | รายการ | Total |
|---|---|---|
| E6 | Gross Budget (รวมสำรอง ไม่รวมซ่อมใหญ่) | 225,000,000 |
| E8 | งบสำรองรวม (10% ของสุทธิ) | 20,454,545 |
| E10 | สำรองค่าใช้จ่ายแปรปรวน (E9 ในตารางพิมพ์ 2.00% ดูหมายเหตุ) | 4,090,909 |
| E12 | สำรองค่าสูญเสีย (E11 ในตารางพิมพ์ 8.00% ดูหมายเหตุ) | 16,363,636 |
| E13 | Net Budget | 204,545,455 |
| E14 | Actual Gross | 217,670,500 |
| E17 | Actual Net | 210,620,500 |
| E18 | Variance ค่าใช้จ่าย | 6,075,045 (E19 = 2.97% ของ Net) |
| E22 | Actual ค่าสูญเสีย | 7,050,000 (E23 = 3.45% ของ Net) |

- หมายเหตุ label: หนังสือพิมพ์ E9 = 2.00% และ E11 = 8.00% "ของสำรองรวม" แต่ 4,090,909 เป็น 2% ของ Net Budget (และเป็น 20% ของสำรองรวม 20,454,545) ส่วน 16,363,636 เป็น 8% ของ Net (80% ของสำรองรวม) (derived) จึงตีความว่า 2% และ 8% คือสัดส่วนของ Net Budget (หนังสือพิมพ์ label ผิด ไม่ใช่ความขัดแย้งกับข้อมูลใน wiki)
- ตรวจ (derived): 204,545,455 + 4,090,909 + 16,363,636 = 225,000,000; 6,075,045 / 204,545,455 = 2.97%; 7,050,000 / 204,545,455 = 3.45%; รวม 6.42% = 13,125,045 / 204,545,455 (13,125,045 = 6,075,045 + 7,050,000)
- Cost variance ใช้วัด "ความสามารถบริหารค่าใช้จ่าย"; loss ใช้วัด "ความสามารถจัดกลยุทธ์และควบคุมคุณภาพ"
- ปัญหา cost มักมาจากวางแผน/ควบคุมงาน (งานล่าช้า ล่วงเวลา) ตรวจ Top Ten High Maintenance Cost และ High Man-Hrs; ปัญหา loss มาจากเลือก PM ไม่ถูก ตรวจ Top High Loss แล้วปรับแผน (p.86)

**ข้อควรระวังตัวเลข (หนังสือไม่สอดคล้องกันเอง):**

| ค่า | บทที่ 3 รูป 3.19 | บทที่ 10 รูป 10.27 |
|---|---|---|
| E15 Variance Gross รวม | (7,329,500) | 13,125,045 |
| E16 Variance Gross % รวม | -3.58% | 6.42% |
| E15 P1 / P2 / P3 | 6,242,909 / (2,897,500) / (5,584,000) | 6,242,909 / 3,920,682 / 2,961,455 |
| E16 P2 / P3 | -4.25% / -6.53% | 5.75% / 3.47% |

ค่าบทที่ 10 สอดคล้องกับข้อความ (6.42%) และเทียบ Actual Gross กับ Net Budget ส่วนค่าบทที่ 3 บางช่องเทียบกับ Gross Budget (เช่น 217,670,500 ลบ 225,000,000 = (7,329,500) ซึ่ง derived) และคลาดเคลื่อน/อ่านจากภาพความละเอียดต่ำ ใช้ค่าบทที่ 10 ตามข้อความ (หนังสือพิมพ์ผิดหรือภาพอ่านผิดที่บทที่ 3, confidence medium) นอกจากนี้ข้อความ p.86 "losses ตั้งไม่เกิน 8% แต่จริงเกิน 3.45%" ขัดสามัญสำนึก เพราะ 3.45% ต่ำกว่า 8% และรวม 6.42% ต่ำกว่าสำรอง 10% ควรตีความว่า cost variance (2.97%) เกินสำรอง 2% ส่วน losses (3.45%) ยังอยู่ในสำรอง 8%

## 7. การใช้ในงบประมาณ (บทที่ 10 p.306-309)

รายงานเดียวกันใช้ปรับงบรายงวด ร่วมกับผังงบและ Top 10/20 report: ค่าจริง พร้อม variance (A-B) แล้วเจาะลง equipment ของ process ที่ผิดปกติ ดู [[Maintenance Budget]]

## เชื่อมโยงกับ compressor failure hierarchy

- ส่วน C ต้องการให้ PM จับคู่กับ [[Failure Mode]] ได้ (p.65) และแยกประเภทงาน Scheduled PM / CM-Planned / CM-Unplanned / Breakdown ใน CMMS ดู [[CMMS]] และ [[Failure Data Recording]]
- Asset Performance ระดับ Component ใช้ Failure Rate (p.63) นำ failure rate ของ [[OREDA]] มาเป็น benchmark ได้ แต่ตัวเลขใน sources ไม่ใช่ข้อมูลของ asset Valeura
- การเจาะรายงานลง equipment ของ [[Compressor]] ที่ planned/unplanned ratio ผิดปกติ ใช้ [[Failure Hierarchy]] ระบุ [[Maintainable Item]] และ mode ที่เป็นต้นเหตุ

## ดูเพิ่ม

- [[Maintenance KPIs]]
- [[Maintenance Efficacy Pyramid]]
- [[Maintenance Budget]]
- [[Availability and OEE]]
- [[Asset Life Cycle]]

## Triplets

- [[Maintenance Strategic Report]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 3, p.55-87; reused in chapter 10
- [[Maintenance Strategic Report]] [uses:: [[CMMS]]] output directly from CMMS/ERP without re-preparation (RBMM p.56-59)
- [[Maintenance Strategic Report]] [depends_on:: Man-Hrs] only extra input needed in Work Order (RBMM p.66)
- [[Maintenance Strategic Report]] [differs_from:: Bottom Up Report] top-down, 1-2 A4 pages vs up to 100 reports (RBMM p.56-59)
- [[Maintenance Strategic Report]] [step_of:: Maintenance Improvement Cycle] Problem of Reporting? (Fig 2.4 and 3.1)
- Section A [part_of:: [[Maintenance Strategic Report]]] organization size and total cost (RBMM p.66-70)
- Section B [part_of:: [[Maintenance Strategic Report]]] key indices: cost/efficiency and stock performance (RBMM p.70-75)
- Section C [part_of:: [[Maintenance Strategic Report]]] Man-Hrs/cost by Process/Area/Criticality, planned vs unplanned (RBMM p.76-83)
- Section D [part_of:: [[Maintenance Strategic Report]]] equipment results: output/OEE and cost per unit (RBMM p.83-84)
- Section E [part_of:: [[Maintenance Strategic Report]]] budget management performance, added later (RBMM p.84-86)
- Asset Performance [has_parameter:: Failure Rate] component level; equipment R/A/M; integrity incl. hidden failures (Fig 3.2, RBMM p.59, p.63)
- Accountability Reporting Matrix [produces:: Cost per Asset] rows = maintenance units, columns = assets (Fig 3.3, RBMM p.60)
- A3 Total Asset Costs [has_formula:: A3.1 + A3.2] (Fig 3.4-3.5, RBMM p.64-70)
- A5 Total Fixed Cost [has_formula:: A1 + A2 + A3 + A4] (Fig 3.4-3.5)
- A9 Material Cost [has_formula:: A6 + A7 + A8] (Fig 3.4-3.5)
- A10 Total Maintenance Cost [has_formula:: A5 + A9] (Fig 3.4-3.5)
- A1 Personnel Costs [has_value:: 25,000,000] actual; budget 20,000,000
- A2 Operating Costs [has_value:: 3,500,000] actual; budget 2,400,000
- A3 Total Asset Costs [has_value:: 19,720,000] actual; budget 23,000,000
- A3.1 Cost of Long Term Asset [has_value:: 520,000] actual; budget 5,000,000; p.64 reads 320,000 from low-res image, 520,000 used (p.66, Fig 10.22)
- A3.2 Cost of Current Asset [has_value:: 19,200,000] actual; budget 18,000,000
- A4 Allocation Costs [has_value:: 500,000] actual; budget 500,000
- A5 Total Fixed Cost [has_value:: 48,720,000] actual; budget 45,900,000; variance 2,820,000
- A6 Parts from Stock [has_value:: 54,000,000] actual; budget 52,881,818
- A7 Direct Purchase Parts [has_value:: 78,350,000] actual; budget 79,000,000
- A8 Outsource [has_value:: 29,550,500] actual; budget 26,763,636
- A9 Material Cost [has_value:: 161,900,500] actual; budget 158,645,455
- A10 Total Maintenance Cost [has_value:: 210,620,500] actual; budget 204,545,455; variance 6,075,045
- A5 Total Fixed Cost [has_category:: Fixed Cost] A1-A4 incurred regardless of output, easy to budget, hard to cut (RBMM p.69)
- Holding Cost [has_value:: 15-20%] of spare part purchase price per year, often hidden in fixed cost (RBMM p.68)
- A6 Parts from Stock [applies_to:: CM-Unplanned] stock is for breakdown/CM-Unplanned only (RBMM p.70)
- A7 Direct Purchase Parts [applies_to:: Scheduled PM] mismatch with C2 means wrong PM selection (RBMM p.70)
- C1.1 % Critical PM per Total PM Tasks [has_value:: 71.3 / 62.9 / 51.9] P1/P2/P3
- C1.2 Critical PM Compliance [has_value:: 100.0 / 96.6 / 100.0] P1/P2/P3
- C1.3 Non-Critical PM Compliance [has_value:: 75.9 / 99.3 / 95.0] P1/P2/P3
- C5.1 Production Loss from Maintenance [has_value:: 7,050,000] planned 1,410,000 and unplanned 5,640,000 (ch10)
- Section C [depends_on:: [[Failure Mode]]] PM must map to a failure mode; separate Scheduled PM, CM-Planned, CM-Unplanned, Breakdown (RBMM p.65)
- Section D [uses:: OEE] cost per unit with OEE
- Net Budget [has_formula:: Gross Budget - Provision for Costs - Provision for Losses] (Fig 3.18-3.20, RBMM p.84-86; ch10 p.309-312)
- E6 Gross Budget [has_value:: 225,000,000] includes provisions, excludes major overhaul
- E8 Total Provision [has_value:: 20,454,545] 10% of net
- E10 Provision for Cost Variance [has_value:: 4,090,909] 2% of Net Budget; book labels E9 as % of total provision, misprint
- E12 Provision for Losses [has_value:: 16,363,636] 8% of Net Budget; book labels E11 as % of total provision, misprint
- E13 Net Budget [has_value:: 204,545,455]
- E14 Actual Gross [has_value:: 217,670,500]
- E17 Actual Net [has_value:: 210,620,500]
- E18 Cost Variance [has_value:: 6,075,045] E19 = 2.97% of Net
- E22 Actual Losses [has_value:: 7,050,000] E23 = 3.45% of Net
- E18 Cost Variance [measures:: Cost Management Capability] problems from work planning/control; check Top Ten High Cost and Man-Hrs (RBMM p.86)
- E22 Actual Losses [measures:: Strategy and Quality Control Capability] problems from wrong PM selection; check Top High Loss (RBMM p.86)
- E15 Variance Gross [has_value:: (7,329,500)] chapter 3 Fig 3.19, vs Gross Budget, likely misprint/misread
- E15 Variance Gross [has_value:: 13,125,045] chapter 10 Fig 10.27, vs Net Budget, used by wiki
- E16 Variance Gross Percent [has_value:: -3.58%] chapter 3 Fig 3.19
- E16 Variance Gross Percent [has_value:: 6.42%] chapter 10 Fig 10.27, matches text, used by wiki
- E18 Cost Variance [has_value:: 2.97%] exceeds 2% cost provision; losses 3.45% within 8% provision (wiki reading of p.86)
- [[Maintenance Strategic Report]] [input_to:: [[Maintenance Budget]]] periodic budget adjustment with Top 10/20 reports (RBMM ch10 p.306-309)

---
title: Maintenance KPIs
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [kpi, maintenance-management, spare-parts, cost, book, iso-14224]
sources: [reliability-based-maintenance-management.md, iso-14224.md]
confidence: medium
contested: false
---

# Maintenance KPIs (โครงสร้างดัชนีบริหารงานบำรุงรักษา)

RBMM เสนอให้ดัชนีเป็นต้นไม้เป้าหมายแทนการมีดัชนีมากและซ้ำ: Fig 2.9 (บทที่ 2, p.48-54) จัด 19 กิจกรรมจากข้อมูล/บุคคล ขึ้นไปกระบวนการ เครื่องจักร และองค์กร ส่วนบทที่ 3 (p.70-84) ให้ดัชนีรหัส B1-B10, C1-C5, D, E พร้อมตัวเลขตัวอย่าง หน้านี้รวมทั้งสองมุมและสูตรที่หนังสือให้

## 1. เป้าหมาย 3 ระดับ (RBMM p.48)

| ระดับ | เป้าหมาย |
|---|---|
| องค์กร | ต้นทุนบำรุงรักษาต่อหน่วยสินค้า, % Asset Utilization, สูญเสียกำไรน้อยสุด (Operational Losses, Maintenance Full Cost) |
| เครื่องจักร | ลดเวลาหยุดนอกแผน, ปรับปรุง Reliability, ลดเวลาหยุดตามแผน, ลดเวลาซ่อม, ลดจำนวนครั้งซ่อมนอกแผน |
| กิจกรรม | Stock Performance, ลด CM-Unplanned และ Optimize PM, Part Logistics, Risk/Criticality และ Reliability Analysis, ประสิทธิผล/ประสิทธิภาพแรงงาน, Planning and Scheduling, ข้อมูลและทักษะ |

## 2. ต้นไม้ 19 กิจกรรม (Fig 2.9, RBMM p.49-54)

| # | กิจกรรม | ดัชนี |
|---|---|---|
| 1 | ต้นทุนบำรุงรักษาต่อหน่วยลดลง | เป้าสูงสุด |
| 2 | ใช้เครื่องจักรได้มากขึ้น | % Asset Utilization |
| 3 | สูญเสียกำไรน้อยสุด | Operational Losses, Maintenance Full Cost |
| 4 | ลดเวลาหยุดนอกแผน | Unplanned Down Time, Availability Factor, MDT |
| 5 | ปรับปรุงความน่าเชื่อถือ | MTTF |
| 6 | ลดเวลาหยุดตามแผน | Planned Downtime |
| 7 | ลดจำนวนครั้งซ่อมนอกแผน | No. of failures, % CM-Unplanned / Total Maintenance |
| 8 | ลดเวลาซ่อม | MTTR (Repair + Wait labor), Maintainability |
| 9 | Stock Performance | Turnover, Stockout Rate, Service Factor, MWT |
| 10 | ลด CM-Unplanned และ Optimize PM | % RCM Task for Critical Equipment |
| 11 | Part Logistics | Lead Time, Price, Variance |
| 12 | Risk/Criticality Analysis | (ไม่มีดัชนีระบุ) |
| 13 | Reliability Analysis | (ไม่มีดัชนีระบุ) |
| 14 | ประสิทธิผลของงาน | Task Selection Logic, PM/CM Ratio (Man-hrs และ Cost), % RCM Task Compliance |
| 15 | Knowledge/Skill | จำนวน Reliability Engineer, Predictive Maintenance |
| 16 | Failure Records | Failure Modes, Incidence Information (วัน เวลา on/off) |
| 17 | ประสิทธิภาพแรงงาน | Full Fixed Cost rate |
| 18 | Planning and Scheduling | % Breakdown WO, Backlog, Work Overdue, MWT (Labor) |
| 19 | อบรมพนักงาน | เวลาและเงินที่ใช้อบรม |

ประเด็นเด่น: ดัชนีประสิทธิผลหลัก 2 ตัวคือ Planned/Unplanned ratio ตาม Man-Hrs และตาม Cost ถ้าไปทางเดียวกันแปลว่าเลือกงานถูก (RBMM p.52) อุดมคติ งานตามแผนมากกว่า 85% นอกแผน 15% ทำให้ schedule ง่ายและงบแม่น (RBMM p.54; ch3 p.60 ระบุ PM มากกว่า 80-85% และ breakdown 10-15% ที่ไม่วิกฤต) จัดลำดับการอบรม "Need to Know" ก่อน "Nice to Know"

## 3. ดัชนีหลักใน Strategic Report (RBMM p.70-84)

### ส่วน B: สมรรถนะการใช้จ่ายและ stock (ตัวอย่างตัวเลขบทที่ 3 รูป 3.7)

| รหัส | ดัชนี | Actual | Budget |
|---|---|---|---|
| B1 | Maintenance Cost / Plant Asset (replacement value) | 5.44% | 5.63% |
| B2 | Calculated Full Fixed Cost | 44,370,000 | 45,900,000 |
| B3 | Man-hr Cost Rate (บาท) | 1,193 | 1,087 |
| B4 | Over/(Under) Absorption | (4,350,000) | - |
| B5 | Utilization Factor | 58.0% | 60.0% |
| B6 | Total Man-hrs | 40,832 | 42,240 |
| B7 | Spare Part Inventory / Plant Asset | 2.50% | 3.00% |
| B8 | Stock Turn Ratio | 40.00% | 44.07% |
| B9 | Service Factor | 97.10% | 99.00% |
| B10 | Stock Out Rate | 2.50% | 1.00% |

สูตรและการตีความ:

```
Standard labor rate (B3) = Maintenance Full Fixed Cost / Man-Hrs ที่ใช้จริง   (p.71-72)
Utilization Factor (B5)  = Man-Hrs ที่ใช้ทำงานจริง / Available Man-Hrs        (p.73)
Cost Variance (Over/Under Absorption) = (rate x Actual Man-Hrs) เทียบ Actual Cost
Efficiency Variance = (Budget rate x Budget Man-Hrs) เทียบ (Budget rate x Actual Man-Hrs)
Total Variance = Cost Variance + Efficiency Variance              (p.72-73)
```

ตรวจเลข (derived): Actual 48.72 ล้าน, Budget 45.90, Calculated 44.37 ล้านบาท; Cost Variance 48.72 ลบ 44.37 = 4.35 (Under absorption); Efficiency Variance 45.90 ลบ 44.37 = 1.53 (Favorable); Total (2.82) U (RBMM p.72-73, ตรงกับ A5 variance 2,820,000) ค่า B3 ตรวจ: 48,720,000 / 40,832 ประมาณ 1,193 และ 45,900,000 / 42,240 ประมาณ 1,087

- B5: 60% ถือว่าสูงแล้วเพราะต้องมีเวลาอบรม/กิจกรรมที่ไม่มี WO ห้ามเน้นดัชนีนี้อย่างเดียว (บันทึก Man-Hrs ผิดจริงถ้ากลัวถูกมองว่าคนเกิน) ต้องนิยามให้ชัดว่านับอะไร (p.73-74)
- B1: ต้องมีราคาทดแทนจากบุคคลที่สาม; เตือนเรื่อง asset แบบ technology base (DCS, PLC) (p.71)
- B7-B10 ชุด Stock: B8 ต่ำ = เสี่ยง dead stock/write-off; B9 ตรวจว่าเก็บตรงรายการ; B10 รายการมีแต่ปริมาณไม่พอ ใช้ Expected PM, CM-Unplanned, CM-Planned เป็น part demand คำนวณ Max-Min, Safety Stock, Risk of Stock out, Cost Risk Ratio (p.74-75) ดู [[Spare Part Criticality and Risk]]

### ส่วน C: การกระจายงานและค่าใช้จ่าย

| ดัชนี | ความหมาย | ข้อควรระวัง |
|---|---|---|
| C1.1 % Critical PM / Total PM Tasks | สัดส่วนงานที่ผ่านการคัดด้วย RCM | งานแผนของเครื่องวิกฤติสูงควรเป็น RCM 100% (p.77) |
| C1.2 Critical PM Compliance | ทำ RCM task ครบหรือไม่ | ไม่ครบ = เสี่ยง |
| C1.3 Non-Critical PM Compliance | ทำงานไม่วิกฤติครบหรือไม่ | อย่าใช้ compliance รวมตัวเดียว เพราะไม่แยกงานสำคัญ |
| C2.1 Planned/Unplanned (Man-Hrs) | ความพยายามด้านแรงงาน | ตัวอย่าง P1/P2/P3 = 1.90 / 2.10 / 2.20 |
| C2.2 Planned/Unplanned (Cost) | ผลเป็นเงินรวม losses | ตัวอย่าง = 1.60 / 1.80 / 2.00 |
| C5.1 Production Loss from Maintenance | ค่าสูญเสียจากงานนอกแผน | รวม 7,050,000 |

การอ่าน C2 (p.78-79): ถ้าสองอัตราไม่สอดคล้อง (เช่น แรงงาน 1.5 แต่ cost 0.9) แปลว่า loss ของงานนอกแผนสูง "ขยันผิดเรื่อง" แต่ละประเภท PM ให้ผลต่างกัน: part replacement/overhaul เหมาะกับ failure mode ที่เห็นอายุ (Weibull beta มากกว่า 1) Man-Hrs ใกล้กันแต่ loss ต่างกัน; Condition Monitoring ถ้าได้ผล สองอัตราไปทางเดียวกัน; RTF สำหรับเครื่องวิกฤติต่ำ ratio ไม่มีความหมาย

เมื่อพบปัญหา (p.79-80): เจาะ equipment ใน process ที่สงสัย, Top Ten/Twenty High Man-Hrs และ High Cost, ตรวจ MTTR/MWT, compliance ของ RCM task, ทบทวน criticality profile, ราคาทรัพยากร และวิธีคำนวณ loss

### ส่วน D และ E

- D: ต้นทุนบำรุงรักษาต่อหน่วย (Actual เทียบ Budget) P1/P2/P3 = 152.00 / 151.00 / 153.50 เทียบ 147.37 / 157.89 / 164.91 (variance 4.63 / (6.89) / (11.41)) ดู [[Availability and OEE]]
- E: สำรอง cost 2% และ losses 8% ของ budget (รวม 10%) เทียบ variance ค่าใช้จ่าย 2.97% และ losses จริง 3.45% รวม 6.42% ของงบสุทธิ รายละเอียดใน [[Maintenance Strategic Report]]

## 4. เมื่อใช้ MTBF/Utilization อย่างเดียวคือไม่พอ (RBMM p.87)

ผู้บริหารมักถามแค่ MTBF หรือ Utilization Factor ทั้งที่ควรถามต้นทุนบำรุงรักษาต่อผลผลิต หน่วยต้นทุนเป็นอย่างไร Dominant Cost อยู่ที่ไหน และปรับปรุงอย่างไร ถ้าตอบไม่ได้คือปัญหา Accountability ผสมความสามารถเทคนิค

## 5. ISO 14224 Annex E: KPI และ Benchmarking (informative)

สรุปด้วยถ้อยคำของผู้เขียน wiki จาก [[ISO 14224]] Annex E (ISO 14224 cl. E.1-E.4, p.238-250)

### 5.1 วงจรและความต่างของ KPI กับ benchmark

- วงจร 5 ขั้น (Figure E.1): benchmark เทียบภายนอก -> หาพื้นที่ปรับปรุง -> สร้าง KPI พร้อมเป้า -> วัดเทียบเป้าและหาสาเหตุที่เบี่ยง -> แก้ไขแล้ววนซ้ำ (cl. E.1, p.238-239) KPI ควรเป็นแบบ SMART
- คุณค่าของ benchmark อยู่ที่การวิเคราะห์ causal factors ของ gap ไม่ใช่แค่ตัวเลข; จุดที่แย่เทียบคนอื่นไม่จำเป็นต้องแก้ก่อนถ้าไม่สำคัญต่อเป้าธุรกิจ
- ความผิดพลาดที่พบบ่อย: ใช้ benchmark เป็น scorecard มองย้อนหลัง แทนแผนที่นำทางไปข้างหน้า (cl. E.3.2, p.240-241)

| ลักษณะ | KPI | Benchmark |
|---|---|---|
| จุดประสงค์ | ติดตามความคืบหน้าเทียบเป้า | หา gap เทียบองค์กรอื่น |
| ความถี่ | ตามช่วงที่คาดว่าจะเห็นผล | ครั้งเดียวหรือไม่บ่อย |
| แหล่งข้อมูล | ภายใน | ภายนอก |
| เป้า | มี | ไม่มี |
| ความแม่น | สนใจแนวโน้ม | สนใจค่าสัมบูรณ์ |

(ISO 14224 Table E.1, p.240)

### 5.2 Peer group และ taxonomy level

- peer group แบ่งด้วยปัจจัยที่โรงงานเปลี่ยนไม่ได้ระยะสั้น-กลาง สองปัจจัยสำคัญคือ process family และ geographic region (cl. E.3.7, p.243)
- ทำ benchmark ได้ตั้งแต่ plant ลงถึง maintainable item ถ้าระดับหนึ่งชี้จุดอ่อนให้ลงไปดูระดับถัดลง (cl. E.3.3, p.241) ผู้ร่วมต้องใช้ boundary และนิยามตามมาตรฐานเดียวกัน (cl. E.3.5)
- ต้องมีตัวอย่างใหญ่พอทางสถิติ เช่น ค่า MTTF เฉลี่ยทั้งโรงงานของ bearing มีประโยชน์จำกัด (cl. E.3.2)
- ข้อมูลที่ใช้ต้องมีคุณภาพตาม [[RM Data Quality]]

### 5.3 ตัวอย่าง KPI 34 ตัว (ISO 14224 Table E.2-E.3, p.243-250) จัดกลุ่มโดยผู้เขียน wiki

| กลุ่ม | KPI (เลขตามตารางมาตรฐาน) |
|---|---|
| Reliability / maintainability | 1 METBF, 2 MTTF, 3 MTBR (subsea: MTBI), 4 MART, 5 MRT, 6 worst actors |
| Availability | 7 AO (นับ downtime CM และ PM), 8 AT (นับเฉพาะ corrective) |
| Safety critical element (SCE) | 9 สัดส่วน SCE ที่มี task ใน CMMS, 10 PM compliance, 11 CM compliance, 14 overdue SCE WO ที่ไม่มี TA อนุมัติ, 34 failure fraction |
| งานและแรงงาน | 12 PM man-hours ratio, 13 corrective man-hours ratio, 15 PM overdue, 16 PdM complete, 17 PdM overdue, 18 CM workload, 19 schedule compliance, 20 unscheduled work, 23-24 estimating accuracy (ชั่วโมง, ต้นทุน), 25 repair rework ratio, 26 เวลาปิด WO ทางเทคนิค, 27 workshop cycle time |
| Turnaround | 21 turnaround duration, 22 time between turnarounds |
| วัสดุ | 28 generic material ordering, 29 materials achieving RoS date, 30 inventory service level |
| ต้นทุน | 31 total maintenance cost, 32 maintenance productivity, 33 cost of repairs per WO |

- ไม่มี KPI ตัวเดียวที่บอกครบ ต้องใช้ basket และไม่โฟกัสแค่ 1-2 ตัว (cl. E.3.6, p.242-243) สอดคล้องกับ RBMM p.87 ในหัวข้อ 4 ข้างต้น
- footnote c ของ Table E.3: "CM" ในตารางนี้หมายถึง condition monitoring ไม่ใช่ corrective maintenance (p.244)
- AT (ISO) ไม่เท่ากับ Ai ที่ [[Availability and OEE]] อธิบายโดยอัตโนมัติ ให้ดูนิยามใน Annex C.2.3 (p.211-213)
- ศัพท์เวลา: ISO แยก MART (เวลาซ่อมจริง) MRT (เตรียม+ซ่อม) MDT; "MTTR = Repair + Wait" ของ RBMM ในหัวข้อ 2 ไม่ตรงศัพท์ ISO ดู [[Maintenance Time Definitions]]
- ชุดตัวชี้วัดงานตามแผนของ ISO ใช้คนละตัวกับ RBMM (ISO: schedule compliance top quartile มากกว่า 98%, unscheduled work น้อยกว่า 2%; RBMM: planned มากกว่า 85%) ไม่ได้ขัดกันตรง ๆ

### 5.4 ข้อควรระวัง: เป้า top quartile ที่ไม่สอดคล้องกับนิยาม

จากการอ่านของผู้บันทึก (ไม่ใช่ข้อความมาตรฐาน) ตัวเลข top quartile ใน Table E.3 บางข้อดูไม่ตรงกับนิยามของตัวเอง ควรตรวจกับต้นฉบับก่อนนำไปตั้งเป้า:

- #28: นิยามวัดความครบของ material catalogue แต่เป้าเขียน น้อยกว่า 10%
- #30: นิยามเป็น service level แต่เป้าเขียน บวกลบ 5%
- #32: นิยามเป็นสัดส่วนชั่วโมงที่ไม่สร้างคุณค่า แต่เป้าเขียน มากกว่า 50%

ถือเป็นความไม่สอดคล้องภายในมาตรฐานเอง ไม่ใช่ข้อขัดแย้งกับ wiki (contested: false)

## เชื่อมโยงกับ compressor failure hierarchy

- ดัชนีข้อ 16 Failure Records (Failure Modes + Incidence Information) คือข้อมูลที่ [[ISO 14224]] กำหนดโครงสร้างไว้ ถ้า CMMS บันทึก failure mode ตาม [[Failure Mode]] และ cause ตาม [[Failure Cause Codes]] ได้ ดัชนี No. of failures, MTTF และ % CM-Unplanned จะแยกตาม mode/maintainable item ได้
- ดัชนีระดับ Component = Failure Rate สอดคล้องกับ failure rate ต่อ [[Maintainable Item]] ใน [[OREDA]] (แต่ OREDA ใช้เป็น benchmark ไม่ใช่ข้อมูลไซต์)
- ดัชนี C1 (RCM compliance) ใช้กับ [[Compressor]] ที่ critical ผ่านการแมป failure mode ไปยัง PM task ดู [[PM Task Selection]]

## ดูเพิ่ม

- [[Maintenance Strategic Report]]
- [[Availability and OEE]]
- [[Maintenance Efficacy Pyramid]]
- [[Asset Life Cycle]]
- [[CMMS]]
- [[RM Data Quality]]
- [[Safety Critical Failure Classification]] (failure fraction, KPI #34)

## Triplets

- [[Maintenance KPIs]] [defined_in:: [[Reliability Based Maintenance Management Book]]] KPI tree Fig 2.9 (p.48-54) and codes B, C, D, E (ch3 p.70-84)
- [[Maintenance KPIs]] [defined_in:: [[ISO 14224]]] Annex E, informative (ISO 14224 cl. E.1-E.4, p.238-250)
- Maintenance Cost per Unit [is_a:: Maintenance KPI] top goal of KPI tree (Fig 2.9, RBMM p.48-49)
- % Asset Utilization [is_a:: Maintenance KPI] activity 2 (Fig 2.9)
- Availability Factor [is_a:: Maintenance KPI] activity 4, with Unplanned Down Time and MDT (Fig 2.9)
- MTTF [is_a:: Maintenance KPI] activity 5 (Fig 2.9)
- MTTF [measures:: Reliability] (Fig 2.9)
- MTTR [is_a:: Maintenance KPI] activity 8 (Fig 2.9)
- MTTR [has_formula:: Repair + Wait labor] RBMM usage (Fig 2.9)
- MTTR [differs_from:: MART] RBMM MTTR = Repair + Wait does not match ISO terms MART, MRT, MDT (ISO 14224, see Maintenance Time Definitions)
- Service Factor [is_a:: Maintenance KPI] activity 9 Stock Performance, with Turnover, Stockout Rate, MWT (Fig 2.9)
- % RCM Task for Critical Equipment [is_a:: Maintenance KPI] activity 10 (Fig 2.9)
- PM/CM Ratio [is_a:: Maintenance KPI] activity 14, by Man-hrs and Cost (Fig 2.9)
- % RCM Task Compliance [is_a:: Maintenance KPI] activity 14 (Fig 2.9)
- Full Fixed Cost Rate [is_a:: Maintenance KPI] activity 17 labour efficiency (Fig 2.9)
- Backlog [is_a:: Maintenance KPI] activity 18 Planning and Scheduling, with % Breakdown WO, Work Overdue (Fig 2.9)
- Planned Work Share [has_value:: > 85%] ideal planned, 15% unplanned (RBMM p.54)
- Planned Work Share [has_value:: > 80-85%] PM, breakdown 10-15% non-critical (RBMM ch3 p.60)
- B1 Maintenance Cost per Plant Asset [is_a:: Maintenance KPI] (Fig 3.7, RBMM p.70-71)
- B1 Maintenance Cost per Plant Asset [measures:: Maintenance Cost] relative to replacement value from third party (RBMM p.71)
- B1 Maintenance Cost per Plant Asset [has_value:: 5.44%] actual; budget 5.63% (Fig 3.7)
- B2 Calculated Full Fixed Cost [is_a:: Maintenance KPI] (Fig 3.7)
- B2 Calculated Full Fixed Cost [has_value:: 44,370,000] actual; budget 45,900,000 (Fig 3.7)
- B3 Man-hr Cost Rate [is_a:: Maintenance KPI] standard labour rate (Fig 3.7)
- B3 Man-hr Cost Rate [has_formula:: Maintenance Full Fixed Cost / Man-Hrs actually used] (RBMM p.71-72)
- B3 Man-hr Cost Rate [has_value:: 1,193 baht] actual; budget 1,087; 48,720,000/40,832 and 45,900,000/42,240 (Fig 3.7)
- B4 Over/(Under) Absorption [is_a:: Maintenance KPI] (Fig 3.7)
- B4 Over/(Under) Absorption [alias_of:: Cost Variance] (RBMM p.72-73)
- B4 Over/(Under) Absorption [has_value:: (4,350,000)] actual (Fig 3.7)
- Cost Variance [has_formula:: (rate x Actual Man-Hrs) vs Actual Cost] (RBMM p.72-73)
- Efficiency Variance [has_formula:: (Budget rate x Budget Man-Hrs) vs (Budget rate x Actual Man-Hrs)] (RBMM p.72-73)
- Total Variance [has_formula:: Cost Variance + Efficiency Variance] (RBMM p.72-73)
- Cost Variance [has_value:: 4.35 million] under absorption, 48.72 - 44.37, derived
- Efficiency Variance [has_value:: 1.53 million] favorable, 45.90 - 44.37, derived
- Total Variance [has_value:: (2.82) million] U, matches A5 variance 2,820,000, derived (RBMM p.72-73)
- B5 Utilization Factor [is_a:: Maintenance KPI] (Fig 3.7)
- B5 Utilization Factor [has_formula:: Man-Hrs actually worked / Available Man-Hrs] (RBMM p.73)
- B5 Utilization Factor [has_value:: 58.0%] actual; budget 60.0%; 60% already high, do not focus on it alone (RBMM p.73-74)
- B6 Total Man-hrs [is_a:: Maintenance KPI] (Fig 3.7)
- B6 Total Man-hrs [has_value:: 40,832] actual; budget 42,240 (Fig 3.7)
- B7 Spare Part Inventory per Plant Asset [is_a:: Maintenance KPI] (Fig 3.7)
- B7 Spare Part Inventory per Plant Asset [has_value:: 2.50%] actual; budget 3.00% (Fig 3.7)
- B8 Stock Turn Ratio [is_a:: Maintenance KPI] low = dead stock / write-off risk (RBMM p.74-75)
- B8 Stock Turn Ratio [has_value:: 40.00%] actual; budget 44.07% (Fig 3.7)
- B9 Service Factor [is_a:: Maintenance KPI] checks items stocked match demand (RBMM p.74-75)
- B9 Service Factor [has_value:: 97.10%] actual; budget 99.00% (Fig 3.7)
- B10 Stock Out Rate [is_a:: Maintenance KPI] item listed but quantity insufficient (RBMM p.74-75)
- B10 Stock Out Rate [has_value:: 2.50%] actual; budget 1.00% (Fig 3.7)
- C1.1 % Critical PM per Total PM Tasks [is_a:: Maintenance KPI] (RBMM p.76-77)
- C1.1 % Critical PM per Total PM Tasks [measures:: RCM Screened Task Share] high-criticality equipment should be 100% RCM (RBMM p.77)
- C1.2 Critical PM Compliance [is_a:: Maintenance KPI] incomplete = risk
- C1.3 Non-Critical PM Compliance [is_a:: Maintenance KPI] do not use one combined compliance figure
- C2.1 Planned/Unplanned Ratio Man-Hrs [is_a:: Maintenance KPI] labour effort
- C2.1 Planned/Unplanned Ratio Man-Hrs [has_value:: 1.90 / 2.10 / 2.20] P1/P2/P3 example
- C2.2 Planned/Unplanned Ratio Cost [is_a:: Maintenance KPI] money result including losses
- C2.2 Planned/Unplanned Ratio Cost [has_value:: 1.60 / 1.80 / 2.00] P1/P2/P3 example
- C2.1 Planned/Unplanned Ratio Man-Hrs [differs_from:: C2.2 Planned/Unplanned Ratio Cost] mismatch, e.g. 1.5 vs 0.9, means high unplanned losses; same direction = right tasks (RBMM p.52, p.78-79)
- C5.1 Production Loss from Maintenance [is_a:: Maintenance KPI] loss from unplanned work
- C5.1 Production Loss from Maintenance [has_value:: 7,050,000] total
- D Maintenance Cost per Unit [is_a:: Maintenance KPI] actual vs budget (RBMM p.83-84)
- D Maintenance Cost per Unit [has_value:: 152.00 / 151.00 / 153.50] actual P1/P2/P3; budget 147.37 / 157.89 / 164.91; variance 4.63 / (6.89) / (11.41)
- E Budget Management Performance [has_value:: 6.42%] cost variance 2.97% + losses 3.45% of net budget vs provisions 2% + 8% = 10%
- Maintenance KPI [differs_from:: Benchmark] KPI tracks progress to target with internal data and trend; benchmark finds external gap, absolute values, no target (ISO 14224 Table E.1, p.240)
- Benchmark [input_to:: Maintenance KPI] 5-step improvement cycle (ISO 14224 Figure E.1, cl. E.1, p.238-239)
- Peer Group [depends_on:: Process Family] also geographic region (ISO 14224 cl. E.3.7, p.243)
- Maintenance KPI [related_to:: KPI Basket] no single KPI suffices, use a basket (ISO 14224 cl. E.3.6, p.242-243; RBMM p.87)
- Maintenance KPI [has_value:: 34] example KPIs (ISO 14224 Table E.2-E.3, p.243-250)
- METBF [is_a:: Maintenance KPI] ISO KPI 1 (ISO 14224 Table E.2-E.3)
- MTBR [is_a:: Maintenance KPI] ISO KPI 3, subsea MTBI (ISO 14224 Table E.2-E.3)
- AO [is_a:: Maintenance KPI] ISO KPI 7, counts CM and PM downtime (ISO 14224 Table E.2-E.3)
- AT [is_a:: Maintenance KPI] ISO KPI 8, corrective downtime only (ISO 14224 Table E.2-E.3)
- AT [differs_from:: Ai] not automatically equal; see definitions (ISO 14224 Annex C.2.3, p.211-213)
- Schedule Compliance [is_a:: Maintenance KPI] ISO KPI 19
- Schedule Compliance [has_value:: > 98%] top quartile (ISO 14224 Table E.3)
- Unscheduled Work [is_a:: Maintenance KPI] ISO KPI 20
- Unscheduled Work [has_value:: < 2%] top quartile (ISO 14224 Table E.3)
- Failure Fraction [is_a:: Maintenance KPI] ISO KPI 34, see Safety Critical Failure Classification
- CM [alias_of:: Condition Monitoring] in ISO Table E.3 only, not corrective maintenance (footnote c, p.244)
- Generic Material Ordering [has_value:: < 10%] ISO KPI 28 top quartile as printed; inconsistent with definition, reader note [confidence:: low]
- Inventory Service Level [has_value:: +/- 5%] ISO KPI 30 top quartile as printed; inconsistent with definition, reader note [confidence:: low]
- Maintenance Productivity [has_value:: > 50%] ISO KPI 32 top quartile as printed; inconsistent with definition, reader note [confidence:: low]
- Component Failure Rate [related_to:: [[OREDA]]] component-level index matches OREDA failure rate per maintainable item; OREDA is benchmark, not site data

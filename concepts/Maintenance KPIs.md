---
title: Maintenance KPIs
created: 2026-10-20
updated: 2026-10-28
type: concept
tags: [kpi, maintenance-management, spare-parts, cost, book, iso-14224, work-management, cmrp, spo, mpm]
sources: [reliability-based-maintenance-management.md, iso-14224.md, cmrp.md, spare-parts-optimization.md, maintenance-profit-maker.md]
confidence: medium
contested: true
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

## 6. มุมมองของ CMRP (เพิ่ม 2026-10-25)

เนื้อหาจากหลักสูตร [[CMRP Course]] (secondary teaching source) ถอดความด้วยถ้อยคำของ wiki

### 6.1 Wrench time ไม่ใช่ Utilization Factor (B5)

| | Wrench time (CMRP) | Utilization Factor B5 (RBMM) |
|---|---|---|
| นิยาม | เวลาที่ช่างลงมือทำงานจริงกับเครื่อง ไม่รวมเดินทาง เบิกของ รอ เตรียม/เก็บ | Man-Hrs ที่ใช้ทำงานจริง (ลง WO) / Available Man-Hrs |
| ค่าตัวอย่าง | ราว 30% ของเวลาทั้งหมด (15% PM + 15% CM) หรือ 12 ชม. จาก 40 ชม./สัปดาห์ | 58% actual, 60% budget และ 60% "สูงแล้ว" |
| อ้างอิง | (CMRP CMPR-08 p.47-48) | (RBMM p.73-74) |

- สองตัววัดคนละสิ่ง: B5 นับชั่วโมงที่ลงใน WO ซึ่งรวมเวลาเดินทาง เบิกของ และรอภายในงาน ส่วน wrench time นับเฉพาะเวลาลงมือ ตัวเลข 30% กับ 60% จึง **ไม่ขัดกัน** และห้ามเทียบตรง (การตีความของ wiki; ไม่ใช่ contested)
- ผลของ planning ต่อ wrench time และการตรวจเลขตัวอย่างใน slide (ใช้ฐาน 12 กับ 15 ชม. ปนกัน) อยู่ที่ [[Maintenance Planning and Scheduling]]

### 6.2 Planning, schedule และ backlog metrics

| ตัวชี้วัด | สูตร/ค่า | อ้างอิง |
|---|---|---|
| Backlog (weeks) | ชั่วโมง WO เปิดที่ยังไม่ลงตาราง / capacity ต่อสัปดาห์; ดีที่ 2-3 สัปดาห์ (CMPR-09) หรือแถบ 3-6 สัปดาห์ (CMPR-10) | CMRP CMPR-09 p.39, p.43; CMPR-10 p.1 |
| % Planned Work | planned WO / total WO (นับจำนวน WO) | CMRP CMPR-10 p.7 |
| Planning Accuracy | Estimated Job Costs / Actual Job Costs; feedback ±15% | CMRP CMPR-10 p.7; CMPR-09 p.33 |
| % Emergency | Emergency man-hours / Total maintenance man-hours | CMRP CMPR-10 p.7 |
| Schedule Compliance | scheduled hours ที่ทำเสร็จ / scheduled hours | CMRP CMPR-10 p.8 |
| Schedule Performance | scheduled hours ที่ทำเสร็จ / available hours | CMRP CMPR-10 p.8 |
| Schedule Effectiveness | Schedule Performance x สัดส่วน direct work | CMRP CMPR-10 p.8 |

- ดัชนีเหล่านี้ขยาย activity 18 Planning and Scheduling (Backlog, Work Overdue) ของ RBMM และ ISO KPI 19-20, 23-24 ในหัวข้อ 5.3 รายละเอียด การเล่นตัวเลข compliance และเหตุของ non-compliance อยู่ที่ [[Maintenance Backlog and Schedule Compliance]]
- เป้า ISO schedule compliance มากกว่า 98% ควรอ่านคู่กับ Schedule Performance เพราะ compliance สูงได้ง่ายถ้าลงตารางเพียงส่วนน้อยของกำลังคน (CMRP CMPR-10 p.9)
- % Planned Work ของ CMRP นับเป็นจำนวน WO ส่วนเป้า planned มากกว่า 85% ของ RBMM นับเป็น man-hours/cost ฐานต่างกัน

### 6.3 การออกแบบ KPI (CMRP CMPR-03 p.31-48)

- **Goal vs objective**: goal กว้าง วัดไม่ได้; objective ตอบ who/what/when/why/to what standard ความผิดพลาดที่พบบ่อยคือเขียนเป็น activity หรือ vision หรือมีมากเกิน (CMRP CMPR-03 p.31-32)
- **SMART** = Specific, Measurable, Achievable, Realistic, Timed (p.33) ตัวอย่างแบบที่สไลด์ใช้: ลด downtime ของ critical mechanical equipment จาก 3% เป็น 2% ภายในสิ้นปี โดยระบุหน่วยงานรับผิดชอบและโปรแกรมที่ใช้ (p.34) ISO ก็แนะนำ KPI แบบ SMART (หัวข้อ 5.1)
- จุดประสงค์หลักของ KPI คือ **เปลี่ยนพฤติกรรม** รองคือบอกสภาพระบบ; ให้วัด cause ไม่ใช่ effect และดู trend ไม่ใช่ event (p.34-37)
- **KPI template** ควรมีองค์ประกอบ: title, purpose, relates to, target, formula, ความถี่การวัด, ความถี่การทบทวน, ผู้วัด, แหล่งข้อมูล, owner, ผู้ลงมือเมื่อผิดเกณฑ์, closed loop, notes (สไลด์บอก 13 องค์ประกอบ) (p.34-35)
- **Warning และ action limits**: KPI ต้องมี target ที่ท้าทายแต่ทำได้ + upper/lower warning limit + upper/lower action limit ติดตามด้วย control chart (ดู [[Statistical Process Control]]) และมี owner ที่ต้องลงมือเมื่อเกิน limit; ห้ามตั้ง target โดยไม่มีทรัพยากร ไม่มี control limit หรือมอบให้คนที่คุมไม่ได้ (p.38-39)
- **Leading vs lagging**: lagging = ผลการเงิน; leading = ลูกค้า, process, innovation (p.40) (ความรู้ทั่วไป: ในงานบำรุงรักษา ดัชนีเช่น PM compliance และ % planned work เป็น leading ส่วนต้นทุนและ availability เป็น lagging)
- ตัวอย่าง KPI sheet "Total Maintenance Cost per Installed Horsepower": industry average 35, lowest 15, highest 60, world class 12 ไม่ระบุหน่วยเงิน **ข้อสังเกต**: world class (12) ต่ำกว่า industry lowest (15) ขัดกันเชิงตรรกะ ถ้า lowest คือค่าต่ำสุดของอุตสาหกรรม (CMRP CMPR-03 p.40-41)
- **Balanced Scorecard**: แปลง mission/strategy เป็นชุด measure 4 มุม Financial, Customer, Internal Business Processes, Learning & Growth "balance" ระหว่างสั้น/ยาว การเงิน/ไม่ใช่การเงิน ภายนอก/ภายใน แล้ว cascade ลงถึงรายบุคคล (CMRP CMPR-03 p.41-45) สอดคล้องกับแนวคิดต้นไม้เป้าหมาย 3 ระดับของ RBMM (หัวข้อ 1-2) ที่ไล่จากองค์กรลงกิจกรรม
- Reporting process: KRA (Quality, Profitability, Productivity, Energy, Environment) -> เลือก KPI ต่อ KRA -> ทดสอบ -> SMART -> วัดเทียบ limit -> นอกช่วงให้พิจารณา [[Root Cause Analysis]] -> review (CMRP CMPR-03 p.46-48)

## 7. ดัชนีคลังอะไหล่จาก SPO (เพิ่ม 2026-10-27)

จาก [[Spare Parts Optimization Book]] บทที่ 10 รายละเอียด ตัวอย่าง และข้อผิดพลาดที่ตรวจพบอยู่ที่ [[Inventory Turnover and GPI Benchmarks]]

| ดัชนี | สูตร | ค่าอ้างอิง | อ้างอิง |
|---|---|---|---|
| Inventory Turnover | ยอดจ่ายทั้งปี / Average Inventory (รอบ/ปี) | ตัวอย่าง 90/30 = 3 | SPO p.112 |
| MOS (Month of Supply) | 12 / Turnover หรือ สต็อก / ความต้องการต่อเดือน | ตัวอย่าง 4 เดือน | SPO p.113, p.123 |
| DOS (Day of Supply) | On Hand / Usage per Day | ตั้งเป้ารายรายการ | SPO p.125 |
| Inventory Value % GPI | Inventory Value / GPI x 100 | spare parts 2 / 4 / 10% ตามพื้นที่; MRO รวมไม่เกิน 4% (แรงงานมาก 1.5%) | SPO p.113-115 |

- SPO ชี้ว่า turnover/MOS ใช้ได้กับของหมุนเร็วเท่านั้น คลัง MRO ที่มีของหมุนช้าปนต้องดู %GPI ด้วย (SPO p.113)
- เทียบ RBMM: B8 Stock Turn Ratio 40% = 0.40 รอบ/ปี = MOS 30 เดือน (derived) และ B7 เป้า 1-3% ของราคาเครื่องจักร ใกล้เคียงแต่ต่ำกว่า benchmark พื้นที่แบบไทยของ SPO (3-4%) ความต่างมาจากขอบเขตตัวเศษและบริบทพื้นที่ ไม่ถือเป็น contested (การตีความ ดู [[Inventory Turnover and GPI Benchmarks]])

## 8. ดัชนีของ MPM (เพิ่ม 2026-10-28, sources: maintenance-profit-maker.md)

จาก [[Maintenance Profit Maker Book]] บทที่ 8 (p.142-156), บทที่ 11 (p.202-203) และกรณีศึกษาบทที่ 12 ถอดความจาก reading notes ค่าที่ wiki คำนวณเองระบุว่า derived

### 8.1 เป้าหมาย 5 ข้อของงานบำรุงรักษา (MPM p.142)

ต้องรู้เป้าหมายก่อนจึงกำหนดดัชนีได้: (1) **Availability** สูงสุด ผลิตจะเดินเมื่อใดก็เดินได้ (2) **Reliability** เดินได้นาน ไม่หยุดบ่อย (3) **Safety** ต่อชีวิตและทรัพย์สิน (4) **Environment** ที่ดีต่อโรงงานและชุมชน (5) **Cost** ที่ "เหมาะสม" ไม่ใช่ "ต่ำสุด" เพราะขึ้นกับนโยบายของแต่ละโรงงาน

### 8.2 ดัชนีหลัก + 4 กลุ่มย่อย (รูป 8.1, MPM p.142-145)

| กลุ่ม | ดัชนีที่หนังสือยกตัวอย่าง |
|---|---|
| **ดัชนีหลัก** (ภาพรวม) | Maintenance Cost / Unit of Production; OEE; ค่าบำรุงรักษา / มูลค่าเครื่องจักร; Man Power Utilization; Spare Parts Turn Over |
| ดัชนีเครื่องจักร | Total Productivity; Planning Factor; OEE; Availability Factor; MTBF; MTTR; Mean Logistic Time; Down Time; Failure Rate |
| ดัชนีอะไหล่และการจัดหา | Inventory Turnover; Part Availability Rate / Service Level; Dead (Inactive) Stock; Urgent Purchase Requisition; Carrying Spare Part / Plant Asset |
| ดัชนีคน | Utilization Factor; Training Factor; Maintainability |
| ดัชนีการบริหาร | Actual/Budget; High Cost Areas; High Problem Areas; ประเภทปัญหา; Man-Hour จริง/แผน; Man-Hour ตามประเภทงาน; Maintenance History; Backlog; Low Utilized Tools; High Usage Parts |

แต่ละกลุ่มมีดัชนีหลัก (บอกสภาพ) และดัชนีรอง (ชี้จุดปรับปรุง); "วัดไม่ได้ก็ปรับปรุงไม่ได้" และต้องเข้าใจที่มาของตัวเลขก่อนตีความ (MPM p.156) ดัชนีเครื่องจักรดู [[Availability and OEE]] หัวข้อ 6 และ [[Reliability Metrics]]

### 8.3 การนำดัชนีไปใช้ 5 แบบ (MPM p.145)

1. เทียบมาตรฐาน/โรงงานอื่นในธุรกิจเดียวกัน (ข้อจำกัด: ข้อมูลอุตสาหกรรมไทยมีน้อยและอาจไม่ถูกต้อง)
2. เทียบกับตัวเองตามเวลา ดูแนวโน้ม
3. หา Room for Improvement อย่างต่อเนื่อง
4. ตั้ง Target หลังเริ่มเก็บข้อมูลได้
5. ดูผลกระทบทางการเงิน: ความคุ้มค่า ระยะคืนทุน ทั้งเชิงปริมาณและคุณภาพ ดู [[Maintenance Financial Impact]]

### 8.4 ค่าบำรุงรักษาต่อหน่วยผลิตแบบ Full Cost (รูป 8.2, MPM p.145-148)

```
Maintenance Cost / Unit = ค่าใช้จ่ายงานบำรุงรักษา (Full Cost) / ผลผลิตสุทธิที่ขายได้ (ตัดของเสีย)
```

ตัวอย่าง: ผลิต 1,345,601 ตัน ขาย 10,256,684,000 บาท Replacement Value 15,000 ล้านบาท WACC 10%

| รายการ | ค่าใช้จ่าย/ปี (บาท) |
|---|---|
| ค่าบริหารจัดสรรจากส่วนกลาง | 16,382,434 |
| ทรัพย์สินบำรุงรักษา (ค่าเสื่อม 17,947,280 + ค่าการเงิน 13,476,139 ของโรงซ่อม/เครื่องมือมูลค่า 134,761,388) | 31,423,419 |
| เงินเดือนค่าแรง (ทางอ้อม 15,423,378 + ทางตรง 31,764,050) | 47,187,428 |
| อะไหล่คงคลัง 350,000,000 -> ค่าการเงิน + เก็บรักษา | 35,000,000 |
| **Total Fixed Cost** | **129,993,280** (ผลรวมจริง 129,993,281 ต่างจากการปัด, derived) |
| อะไหล่ใช้สิ้น / จ้างเหมา / ซ่อมใหญ่ 152 ล้านทุก 3 ปี เฉลี่ยต่อปี | 56,741,325 / 8,512,000 / 50,666,667 |
| **Total Variable Cost** | **115,919,992** |
| **รวมทั้งสิ้น** | **245,913,272** |

| KPI | ค่า | ตรวจ (derived) |
|---|---|---|
| Maintenance cost / unit produced | **182.75 บาท/ตัน** | 245,913,272 / 1,345,601 |
| Maintenance cost / sales | 2.40% | ตรง |
| Maintenance cost / plant replacement value | 1.64% | ตรง |
| Spare part turnover rate | 16.21% | 56,741,325 / 350,000,000 |
| Full cost rate / man-hr | 1,398 บาท | 129,993,280 / (206,640 x 45%) = 1,397.96 (หนังสือไม่แสดงสูตร) |

- **ตัดส่วนที่ไม่ใช่ค่าใช้จ่ายของหน่วยงานโดยตรง** (ค่าจัดสรรส่วนกลาง + ค่าเสื่อมและค่าการเงินของทรัพย์สินที่หน่วยงานครอบครอง): 245,913,272 - 16,382,434 - 31,423,419 = 198,107,419 บาท = **147 บาท/ตัน** (147.22, derived) ส่วนต่างราว 35.5 บาท/ตัน = จัดสรร 12.17 + ค่าการเงิน 10.01 + ค่าเสื่อม 13.34 ใช้บอกว่าควรลดส่วนใดก่อน
- ข้อสังเกตเชิงนิยาม (derived): ข้อความว่าตัด "ค่าใช้จ่ายด้านการเงิน" ออก แต่ยังคง 35,000,000 ค่าการเงิน + เก็บรักษาอะไหล่คงคลังไว้ ถ้าตัดด้วยจะเหลือ 163,107,419 บาท = **121.2 บาท/ตัน**
- ตัวเลขที่ตรวจซ้ำไม่ได้: Man-Hr Rate เฉลี่ย 143 บาท [ไม่ทราบที่มา] และ Man-hours 206,640 = 105 คน x 1,968 ชม. ซึ่งไม่ตรงกับ 1,663.2 ชม./คน ที่บทเดียวกันเสนอ (derived) โครงสร้างต้นทุนเต็มดู [[Maintenance Cost Structure]]

### 8.5 ดัชนีอะไหล่และการจัดหา (MPM p.151-153)

| ดัชนี | สูตร | หมายเหตุ |
|---|---|---|
| Spare Part Turn Over | มูลค่าเบิกใช้ทั้งปี / มูลค่าคงเหลือ **สิ้นปี** | ตัวอย่าง 0.16 รอบถือว่าต่ำ; "ค่ามาตรฐานราว 1.0" (MPM p.152) ตัวหารต่างจาก SPO ที่ใช้ average inventory (หัวข้อ 7) |
| Part Availability Rate / Service Level | จำนวนอะไหล่ที่เบิกได้ / จำนวนที่ขอเบิกทั้งหมด | ตรงข้าม Stock Out; สูตรอังกฤษในเล่มพิมพ์ตัวเศษเป็น "Orders Not filled on demand" ซึ่งคือ stock out rate ตัวเศษที่ถูกของ service level คือ **Orders filled on demand** (derived) |
| Inactive Stock | มูลค่าอะไหล่ไม่เคลื่อนไหว / มูลค่าทั้งหมด | แยก Insurance Parts และของ lead time นานออกก่อนตัดสินใจลด |
| Part Usage, PM Part Requirement | รายรายการ (จำนวน/มูลค่า) | ตั้ง Max/Min, รวมความต้องการจากแผน PM ทั้งปี |
| Urgent Purchase Requisition | Line Items ของ Urgent PO / Total Line Items ของ PO | งานฉุกเฉินมาก = "ถูกงานคุม" |
| Carrying Spare Part / Plant Asset | มูลค่าอะไหล่ที่เก็บ / มูลค่าเครื่องจักร | ยิ่งต่ำยิ่งดี โดย Availability ไม่ลด; ไม่ให้ค่าเป้า (เทียบ B7 ข้างบนและ [[Inventory Turnover and GPI Benchmarks]]) |

### 8.6 ดัชนีคน (MPM p.154-155)

- **Utilization Factor** = เวลาทำงานจริง / เวลาที่พร้อมทำงาน; ชั่วโมงพร้อมทำงาน/คน/ปี = 365 - 104 (สุดสัปดาห์) - 15 (วันหยุด) - 15 (ลา) = 231 วัน x 8 = 1,848 ชม. หักอบรม 5% และงานจิปาถะ 5% = **1,663.2 ชม.** ตัวอย่างช่างทำงาน 1,000 ชม. = 60.1% (RBMM ใช้ 1,760 / ราว 1,600 ชม. เป็นค่าสมมติต่างกัน ไม่ถือเป็นข้อขัดแย้ง ดู [[Maintenance Cost Structure]])
- **Training Factor** = เวลาอบรมรวม / จำนวนพนักงาน (ชม./คน/ปี) อบรมมากไม่ได้แปลว่าเก่งขึ้น ต้องดูคู่ Maintainability
- **Maintainability (มุมคน)** ใช้ MTTR: MTTR ลดต่อเนื่องหลังอบรมอาจแสดงว่าคนเก่งขึ้น

### 8.7 ดัชนีการบริหาร (MPM p.155-156)

| ดัชนี | สูตร/รูปแบบ | ความหมาย |
|---|---|---|
| Actual / Budget | ratio | งบตั้งบนข้อมูลจริงเพียงใด |
| High Cost Areas และ High Problem Areas | รายงานจัดอันดับ | ใช้คู่กัน เพราะเครื่องค่าใช้จ่ายสูงอาจเสียไม่บ่อย |
| สรุปประเภทปัญหา | ตามสาเหตุ | คู่กับ High Problem Areas |
| Man-Hours จริง / แผน | ratio | ความแม่นของการประมาณงาน |
| Man-Hours ตามประเภทงาน / ทั้งหมด | PM : CM : [ประเภทที่ 3 อ่านไม่ออก] | งานไม่ได้วางแผนมาก = ช่าง "ถูกงานคุม" |
| Maintenance History | ข้อมูล | ข้อมูลสำคัญที่สุด |
| Backlog | Man-Hours งานที่เหลือ / Man-Hours กำลังคนที่พร้อม | งานค้างต้องใช้อีกกี่วัน (ไม่มีเป้า; CMRP นับเป็นสัปดาห์ ดู [[Maintenance Backlog and Schedule Compliance]]) |
| Low Utilized Tools | Hours ใช้งาน / Hours พร้อมใช้ รายรายการ | วางแผนลงทุนเครื่องมือ |
| High Usage Parts by Amount and Quantity | รายงาน | นโยบายอะไหล่แต่ละประเภท |

- **PM/CM Ratio ควรอยู่ที่ 2.0 ฐานชั่วโมง-คน** แต่ค่าใช้จ่ายงานซ่อมสูงกว่า PM มากกว่า 2 เท่า เพราะอะไหล่และค่าสูญเสียผลผลิต (MPM p.123-124) ตัวอย่างบริษัท XYZ มี PM/CM 1.2 ทุกปี (MPM p.232-233) สอดคล้องกับแนว C2.1/C2.2 ของ RBMM (หัวข้อ 3) ที่ต้องอ่าน ratio ทั้งฐาน man-hours และฐาน cost

### 8.8 ชุดดัชนีที่ใช้ประเมินสมรรถนะ (รูป 11.4, MPM p.202; ค่า XYZ จากรูป 12.12, MPM p.232-233)

| กลุ่ม | ดัชนี | XYZ 1998 / 1999 / 2000 |
|---|---|---|
| Maintenance Expenditure | Maintenance Expenses / Unit Produced | 640 / 920 / 966 บาท/ตัน |
| | Maintenance Expenditure / Plant Asset | 2.91 / 3.53 / 4.65% |
| | Maintenance Operating Expense / Maintenance Capital Expenses | n/a / 3.2 / 2.1 (ย้อนคำนวณไม่ได้) |
| | Maintenance Asset / Total Plant Asset | 4.56 / 4.59 / 5.62% |
| OEE | Availability, Speed, Quality Factor | OEE 89.13 / 80.45 / 79.42% |
| Inventory | Spare Part Inventory / Plant Asset | 3.7 / 3.7 / 4.7% |
| | Spare Part Turn Over rate | 20.4 / 11.4 / 10.8% |
| | Spare Part Service rate | 95 / 93 / 93% |
| | Spare Part Cost / Total Maintenance Cost | 53.3 / 60.3 / 71.8% |
| Work Control | PM/CM; PDM / Total Maintenance | 1.2; 5% |
| | MTBF, MTTR, MWT | n/a |
| | Turnaround Time (days); Turnaround Cost / Plant Asset; Mean Time Between Turnaround (years) | 35; 0.33%; 3.0 |
| Human Resource | Utilization Factor; Over Time / Normal | 50%; 30% |
| | Personnel Cost / Total Maintenance Cost | พิมพ์ 22.1 / 19.0 / 12.1% (ปี 1998 ที่ถูก 68.1/320.2 = 21.3%, derived) |
| | Direct / Indirect Head count; Contracts / Total Maintenance Cost | 7.7 / 7.6 / 6.7; 5.2 / 3.3 / 2.2% |
| Safety | Man-hours lost by accident / Total Hours Available | - |
| Maintenance Full Cost rate | Average Man-Hr Rate; Actual (full) Man-Hr Rate | 237 / 266 / 247; 1,197 / 1,299 / 1,506 บาท |

- รูป 11.4 ไม่ให้ค่าเป้า/benchmark ดัชนีส่วนใหญ่ซ้ำกับ RBMM Strategic Report (B1, B5, B7, B8, B9) ในหัวข้อ 3 ส่วนรูป 12.10 (MPM p.228) พิมพ์ชุดตัวเลขที่ขัดกับรูป 12.12 หลายแถว ให้ใช้รูป 12.12 ซึ่งตรวจแล้วตรงกับข้อมูลดิบ (derived)
- ต้องเลือก **ดัชนีหลักชัย** ก่อน ที่เหลือเป็นดัชนีเสริม เพราะดัชนีมาจากหลายระบบที่ต้องกระทบยอดกัน (MPM p.201) Utilization Factor อ่อนไหวมาก สูงแค่บอกว่าคนว่างน้อย ต้องถามด้วยว่างานควรใช้เวลาเท่านั้นหรือไม่ (MPM p.203)

### 8.9 Personnel Productivity (MPM p.203, p.242)

```
Personnel Productivity = (OEAD + ค่าใช้จ่ายทั้งสิ้นด้านบุคคล) / ค่าใช้จ่ายทั้งสิ้นด้านบุคคล
OEAD = Operational Earning After Depreciation
```

- วัดความสามารถสร้างมูลค่าเพิ่มของบุคลากร ประเมินง่ายเมื่อเป็น Profit Center ถ้าเป็น Cost Center ต้องประมาณมูลค่าเพิ่ม; การคิดหลังหักค่าเสื่อมทรัพย์สินที่บำรุงรักษาครอบครองทำให้ผู้บริหารพยายามถือทรัพย์สินให้น้อยที่สุด ค่าบุคคลรวมทั้งทางตรงและทางอ้อม
- รายงานที่หนังสือให้ศูนย์กำไรบำรุงรักษาต้องมี: Utilization Factor, Full Cost และ Full Cost rate, Over/(Under) Absorption (OCR อ่านเป็น "Reserved"), Provision for Work Due / Loss Order, ดัชนีที่เลือกทั้งหมด และ Personnel Productivity (MPM p.242)

### 8.10 เป้า Utilization Factor (ข้อขัดแย้ง MPM-C5)

| แหล่ง | มุมมอง |
|---|---|
| MPM | ตั้งเป้า **Utilization rate > 60%** บนฐานงานมาตรฐาน + work control system ซึ่งหมายถึงคนต่ำอย่างเหมาะสมและบันทึกชั่วโมงเชื่อถือได้ (MPM p.215); กรณีศึกษาบำรุงรักษารวมศูนย์สมมติปรับ UF จาก **40% -> 70%** ทำให้ต้องการคน 229 แทน 400 คน (MPM p.239) |
| RBMM | B5 ที่ **60% ถือว่าสูงแล้ว** เพราะต้องมีเวลาอบรมและงานที่ไม่มี WO และห้ามไล่ดัชนีนี้อย่างเดียว (RBMM p.73-74, หัวข้อ 3) |

- 70% ของ MPM เกินระดับที่ RBMM ถือว่าสูง ทั้งที่เป็นผู้แต่งกลุ่มเดียวกัน wiki เก็บทั้งสองมุมมองและยังไม่เลือก ฐานการนับก็ต่างได้ (MPM ใช้ 1,663.2 ชม. พร้อมทำงานหลังหัก 10%; ตัวอย่าง XYZ ใช้ 1,968 ชม.) จึงควรระบุตัวหารทุกครั้งที่ตั้งเป้า
- คำว่า Utilization Factor ใน MPM ถูกใช้สองความหมาย: UF 50% ของ XYZ (ชั่วโมงลงงาน) กับ "UF ที่คิดเป็นเนื้องาน" 35% -> 55% ในตัวอย่าง planner (MPM p.227) ซึ่งใกล้ wrench time ในหัวข้อ 6.1 มากกว่า ดู [[Maintenance Planning and Scheduling]]

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
- [[Maintenance Planning and Scheduling]] (wrench time)
- [[Maintenance Backlog and Schedule Compliance]]
- [[Turnaround Management]] (ISO KPI 21-22)
- [[Inventory Turnover and GPI Benchmarks]] (SPO stock KPIs)
- [[Maintenance Financial Impact]] (MPM, KPI -> งบการเงิน)
- [[Maintenance Profit Maker Book]]

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
- Wrench Time [differs_from:: B5 Utilization Factor] hands-on time ~30% (CMRP CMPR-08 p.47) vs man-hours booked to WO / available, 58-60% (RBMM p.73); different measures, not contested
- Wrench Time [is_a:: Maintenance KPI] (CMRP CMPR-08 p.47-48)
- Backlog [has_value:: 2-3 weeks] CMRP CMPR-09 p.43; CMPR-10 p.1 gives band 3-6 weeks
- % Planned Work [is_a:: Maintenance KPI] planned WOs / total WOs (CMRP CMPR-10 p.7)
- Planning Accuracy [is_a:: Maintenance KPI] estimated / actual job cost (CMRP CMPR-10 p.7)
- % Emergency [is_a:: Maintenance KPI] emergency / total maintenance man-hours (CMRP CMPR-10 p.7)
- Schedule Performance [is_a:: Maintenance KPI] (CMRP CMPR-10 p.8)
- Schedule Effectiveness [is_a:: Maintenance KPI] (CMRP CMPR-10 p.8)
- Schedule Performance [related_to:: Schedule Compliance] read ISO > 98% target together with performance (CMRP CMPR-10 p.9)
- SMART [applies_to:: Maintenance KPI] Specific, Measurable, Achievable, Realistic, Timed (CMRP CMPR-03 p.33; ISO 14224 cl. E.1)
- Maintenance KPI [has_value:: 13 template elements] title, purpose, target, formula, frequency, owner, closed loop etc. (CMRP CMPR-03 p.34-35)
- Maintenance KPI [has_parameter:: Warning Limit] upper and lower, plus action limits and owner (CMRP CMPR-03 p.38-39)
- Maintenance KPI [uses:: [[Statistical Process Control]]] control chart tracking (CMRP CMPR-03 p.38-39)
- Leading Indicator [differs_from:: Lagging Indicator] lagging = financial; leading = customer, process, innovation (CMRP CMPR-03 p.40)
- Total Maintenance Cost per Installed Horsepower [has_value:: world class 12] industry average 35, lowest 15, highest 60; world class below lowest is illogical (CMRP CMPR-03 p.40-41)
- Balanced Scorecard [has_part:: Financial Perspective] with Customer, Internal Business Processes, Learning and Growth (CMRP CMPR-03 p.41-45)
- Balanced Scorecard [related_to:: [[Maintenance KPIs]]] cascade strategy to individual measures (CMRP CMPR-03 p.41-45)
- Inventory Turnover [is_a:: Maintenance KPI] annual issues / average inventory (SPO p.112)
- Month of Supply [is_a:: Maintenance KPI] 12 / Inventory Turnover (SPO p.113)
- Day of Supply [is_a:: Maintenance KPI] On Hand / Usage per Day (SPO p.125)
- Inventory Value % GPI [is_a:: Maintenance KPI] spare parts 2 / 4 / 10% by area (SPO p.113-115)
- B8 Stock Turn Ratio [related_to:: Inventory Turnover] 40% = 0.4 turns = MOS 30 months, derived
- B7 Spare Part Inventory per Plant Asset [related_to:: Inventory Value % GPI] RBMM 1-3% vs SPO 3-4% Thai benchmark; not contested
- [[Maintenance KPIs]] [related_to:: [[Inventory Turnover and GPI Benchmarks]]]
- [[Maintenance KPIs]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 8 indices (MPM p.142-156) and Fig 11.4 (MPM p.202)
- Maintenance Goals MPM [has_part:: Availability] with Reliability, Safety, Environment, appropriate Cost not lowest (MPM p.142)
- MPM KPI Structure [has_part:: Main Indices] plus machine, spares and procurement, people, management sub-groups (MPM p.142-145 Fig 8.1)
- Main Indices MPM [has_part:: Maintenance Cost per Unit] with OEE, cost / asset value, manpower utilization, spare turnover (MPM p.142-145)
- Maintenance KPI [applies_to:: Benchmarking] 5 uses: benchmark, trend, room for improvement, target, financial impact (MPM p.145)
- MPM Maintenance Cost per Unit [has_formula:: Full Cost maintenance expense / net saleable output] (MPM p.145-148)
- Fig 8.2 Full Cost Example [has_value:: 182.75 baht per ton] 245,913,272 / 1,345,601 t (MPM p.147)
- Fig 8.2 Full Cost Example [has_value:: cost/sales 2.40%, cost/RV 1.64%, turnover 16.21%, full cost rate 1,398 baht/h] (MPM p.147)
- Fig 8.2 Full Cost Example [has_value:: total fixed 129,993,280; variable 115,919,992; total 245,913,272 baht] (MPM p.146-147)
- Full Cost Rate [has_formula:: Total Fixed Cost / (Man-hours x Utilization Factor)] 129,993,280 / (206,640 x 45%), derived
- Fig 8.2 Direct Cost Example [has_value:: 147 baht per ton] excludes allocation and maintenance asset cost; 147.22 derived (MPM p.147)
- Fig 8.2 Direct Cost Excluding Spare Financing [has_value:: 121.2 baht per ton] derived, also removing 35,000,000 spare financing
- MPM Spare Part Turn Over [has_formula:: annual usage value / year-end stock value] standard about 1.0 (MPM p.151-152)
- MPM Spare Part Turn Over [differs_from:: Inventory Turnover] year-end stock vs average inventory (SPO p.112)
- Service Level [has_formula:: parts issued / parts requested] opposite of Stock Out (MPM p.152)
- Service Level Printed English Formula [has_formula:: Orders Not filled on demand / total orders] actually stock out rate (MPM p.152)
- Service Level Printed English Formula [contradicts:: Service Level] book error; correct numerator Orders filled on demand, derived
- Inactive Stock [has_formula:: non-moving stock value / total stock value] exclude insurance and long lead parts (MPM p.152-153)
- Urgent Purchase Requisition [has_formula:: urgent PO line items / total PO line items] (MPM p.153)
- Carrying Spare Part per Plant Asset [is_a:: Maintenance KPI] lower is better if availability holds (MPM p.153)
- MPM Utilization Factor [has_formula:: actual working time / available time] (MPM p.154)
- MPM Available Hours [has_value:: 1,663.2 h per person per year] 231 days x 8 h less 5% training and 5% misc (MPM p.154)
- Training Factor [has_formula:: total training hours / number of employees] (MPM p.154)
- MPM Backlog [has_formula:: remaining work man-hours / available man-hours] in days, no target (MPM p.155-156)
- Low Utilized Tools [has_formula:: hours used / hours available] per tool (MPM p.156)
- High Cost Areas [related_to:: High Problem Areas] use together (MPM p.155)
- PM/CM Ratio [has_value:: 2.0] man-hour basis target; repair cost far above 2x PM (MPM p.123-124)
- XYZ Case Study [has_value:: PM/CM 1.2] all years (MPM p.232-233)
- Fig 11.4 KPI Set [has_part:: Maintenance Expenditure Indices] with OEE, Inventory, Work Control, Human Resource, Safety, Full Cost rate groups (MPM p.202)
- Fig 11.4 KPI Set [has_value:: no targets given] (MPM p.202)
- XYZ Case Study [has_value:: Maintenance Expenditure / Plant Asset 2.91 / 3.53 / 4.65%] 1998-2000 (MPM p.232-233 Fig 12.12)
- XYZ Case Study [has_value:: spare turnover 20.4 / 11.4 / 10.8%] service rate 95 / 93 / 93% (MPM p.232-233)
- XYZ Personnel Cost Share 1998 Printed [has_value:: 22.1%] book error; derived 21.3% = 68.1 / 320.2 (MPM p.233)
- Personnel Productivity [has_formula:: (OEAD + total personnel cost) / total personnel cost] OEAD = Operational Earning After Depreciation (MPM p.203, p.242)
- Personnel Productivity [measures:: Personnel Value Added] easier in profit center (MPM p.203)
- MPM Utilization Target [has_value:: > 60%] with work control system (MPM p.215) [contested:: true]
- MPM Utilization Case Study [has_value:: 40% to 70%] 400 to 229 people (MPM p.239) [contested:: true]
- RBMM Utilization View [has_value:: 60% already high] do not chase alone (RBMM p.73-74) [contested:: true]
- MPM Utilization Target [contradicts:: RBMM Utilization View] MPM-C5 [contested:: true]
- RBMM Utilization View [contradicts:: MPM Utilization Case Study] MPM-C5, 70% exceeds RBMM high level [contested:: true]
- [[Maintenance KPIs]] [related_to:: [[Maintenance Financial Impact]]]

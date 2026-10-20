---
title: Maintenance KPIs
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [kpi, maintenance-management, spare-parts, cost, book]
sources: [reliability-based-maintenance-management.md]
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

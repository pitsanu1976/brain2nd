---
title: Monte Carlo Maintenance Simulation
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [pm, statistics, weibull, cost, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Monte Carlo Maintenance Simulation

Monte Carlo Simulation คือการจำลองที่ใช้ตัวเลขสุ่มจาก input ที่เป็นการแจกแจงทางสถิติ (เช่น Weibull ของ time-to-failure, การแจกแจงของ repair time) รันหลายรอบแล้ววิเคราะห์ผลลัพธ์เชิงสถิติ RBMM ใช้เพราะสถิติแบบสมการให้ได้เพียงโอกาสเสีย F(t) และ reliability R(t) ไม่ใช่ "จำนวนครั้งที่จะเสีย" ซึ่งเป็นสิ่งที่งบประมาณ อะไหล่ และคาบ PM ต้องการ (RBMM p.194-197)

## ทำไมต้อง simulation (RBMM p.194-197)

- TTF, wait time, time to repair เป็นตัวแปรสุ่ม (รูป 7.11); ค่าเฉลี่ยคือ MTTF, MWT, MTTR
- สถิติบอกได้แค่ F(t), R(t) (ตัวอย่างโยนเหรียญ 20 เทียบ 1,000 ครั้ง กับ confidence level) จึงต้องใช้ simulation
- Deterministic/Parametric model (รูป 7.12): input x1..x3 ผ่าน f(x) ได้ output ค่าแน่นอน
- Monte Carlo (รูป 7.13): input เป็นการแจกแจง สุ่มหลายรอบ ได้ output เป็นการแจกแจง (ตัวอย่าง output reliability = 87%)
- ข้อมูลน้อยยังใช้ได้พอประมาณ เพราะ failure mode ถูกมองเป็น "man-made pre-programmed failure" (p.194) เป็นข้อสังเกตของผู้เขียน ควรระวังเรื่อง confidence
- ซอฟต์แวร์ที่หนังสือกล่าวถึง: Minitab, MathCad, CEDAR Maintenance Optimizer, Weibull Smith (p.195)

## Input และ Output ของโมเดล CM-Unplanned (RBMM p.198)

| Input | Output |
|---|---|
| ช่วงเวลาผลิต (ปี) | จำนวนครั้ง CM-Unplanned ที่คาด |
| beta, eta (ชม.) ดู [[Weibull Analysis]] | เวลาหยุดรวม |
| MTTR, MWT | Average Availability (%) |
| สภาพหลังซ่อม / restoration factor (%) | ค่าใช้จ่ายต่อหน่วยเวลาใช้งาน (บาท/ชม.) |
| ค่าเสียหายจากเครื่องหยุด (บาท/ชม.) | ค่าใช้จ่ายรวม (ล้านบาท) |
| ค่าแรง/ชม., ค่าอะไหล่/ครั้ง | |

## ตัวอย่างผล (รูป 7.18-7.20, RBMM p.199-203)

ข้อมูลฐาน: TTF 16,000, 12,000, 11,000, 8,500 ชม. ได้ beta = 3.788, eta ราว 13,130 ชม.; 3 ปี; ค่าเสียหายหยุดเครื่อง 200,000 บาท/ชม.; ค่าแรง 5,000 บาท/ชม.; ค่าอะไหล่ 30,000 บาท

| กรณี | CM-Unplanned (ครั้ง) | หยุดรวม (ชม.) | บาท/ชม. | ค่าใช้จ่ายรวม | Availability |
|---|---|---|---|---|---|
| ฐาน: MTTR 8 + MWT 2 (MDT 10), ฟื้น 100% | 1.76 | 17.57 | 139 | 3.6 ล้านบาท | 99.93% |
| ลด MTTR/MWT เหลือ 6 และ 1 (MDT 7) | 1.79 | 12.51 | 99 | 2.6 ล้านบาท | 99.95% |
| ฟื้นสภาพหลังซ่อม 75% | 2.18 | 21.76 | 171.5 | 4.5 ล้านบาท | 99.91% |

ข้อสังเกตตามหนังสือ: ลดเวลาซ่อม/รออะไหล่ให้ผลคุ้มเพราะ loss rate สูง; ซ่อมไม่สมบูรณ์หรือใช้อะไหล่ไม่ใหม่ทำให้ต้นทุนสูงขึ้น; ผลบอกว่าต้องการอะไหล่ราว 2 ชิ้นใน 3 ปี ไว้ตั้ง Max/Min ตาม lead time (p.203) ดู [[Spare Parts Management]]

## Scheduled replacement (รูป 7.23, RBMM p.204-206)

เปลี่ยนตามแผนทุก 16 เดือน, PM: MTTR 6 ชม., MWT 0, ฟื้น 100%, ค่าเสียหายตอนทำ PM 50,000 บาท/ชม.

| รายการ | ค่า |
|---|---|
| CM-Unplanned | ราว 1.0 ครั้ง, 2,120,922 บาท |
| Scheduled PM | ราว 1.0 ครั้ง, 387,360 บาท, 6.46 ชม. |
| รวม 3 ปี | 2,508,282 บาท, 96 บาท/ชม., Availability 99.94% |

เทียบกับไม่ทำ PM 3.6 ล้านบาท ลดเหลือ 2.5 ล้านบาท; อะไหล่ 1 ชิ้นสำหรับ CM + 1 ชิ้นสำหรับ PM ผลรวมของสองส่วน (2,120,922 + 387,360) เท่ากับ 2,508,282 พอดี (derived ตรวจแล้ว) การจำลองยังใช้หาคาบ ดู [[PM Interval Optimization]] และ [[P-F Interval and Condition Monitoring]]

หมายเหตุ: ตัวเลขรอบ 16 เดือนในบทที่ 7 ให้ total 2.5 ล้านบาท อยู่ระหว่างคาบ 15 และ 18 เดือนในตาราง Simulator บทที่ 8 (2.26 และ 2.99 ล้านบาท) ซึ่งสอดคล้องกัน แต่ input บางตัว (ค่าเสียหายตอนหยุด) ต่างชุดกัน จึงไม่ควรเทียบตรง ๆ

## การใช้ในงบประมาณและระบบสำรอง

- ตั้งงบตามแผนผลิตรวม/แผนหยุดซ่อมใหญ่ (ทุก 3-4 ปี) จัดลำดับ dominant failure mode ราว 80% ก่อน (p.206); ตัวอย่าง PM ทุก 10 เดือน คาด CM-Unplanned 0.35 ครั้งต่อปี งบ 1.3 ล้านบาทพอทำ PM 1 ครั้ง ดู [[Maintenance Budget]]
- ระบบ k/n: รวม reliability ของแต่ละ failure mode ด้วย Monte Carlo ดู [[Redundancy and Standby Systems]]
- อะไหล่ High/Medium criticality ใช้ Demand Simulation (บทที่ 9) ดู [[Spare Part Demand Forecasting]]
- ทางเลือกอย่างง่าย: Basic Average Method (constant failure rate) เช่น 100 หน่วย x 43,800 ชม. = 4,380,000 unit-hours, 11 ครั้ง, MTBF 398,181.82 ชม. (ตรวจแล้วตรง); ใช้ได้เฉพาะ pattern D และให้ผลคล้าย beta = 1 เสมอเมื่อรวมทุก failure mode (p.190-193)

## กฎปฏิบัติ

- ต้องมีข้อมูลต่อ failure mode: beta/eta, MTTR, MWT, cost ต่อครั้ง, loss rate
- ทดลองหลายคาบแล้วเรียง total cost หาจุดต่ำสุด
- ผล simulation เป็นการคาดการณ์เชิงสถิติ ไม่ใช่ค่าแน่นอน ตรวจคุณภาพข้อมูล CMMS ก่อน ดู [[Failure Data Recording]]

## เชื่อมโยงกับ compressor failure hierarchy

- หนึ่ง simulation ต่อหนึ่ง failure mode ของ [[Maintainable Item]] ตามระดับ [[Failure Mode]]; ใช้ [[OREDA]] เป็น prior ของอัตราเสียได้เฉพาะแบบ constant rate (ข้อสังเกตของเรา)
- ตัวเลขตัวอย่างทั้งหมดในหนังสือเป็นของเครื่องทั่วไป ไม่ใช่ compressor ของ Valeura

## ดูเพิ่ม

- [[PM Interval Optimization]]
- [[PM Task Selection]]
- [[Weibull Analysis]]
- [[Spare Part Demand Forecasting]]
- [[Statistical Distributions for Maintenance]]

## Triplets

- [[Monte Carlo Maintenance Simulation]] [is_a:: Stochastic Simulation] random numbers from distributions, many runs (RBMM p.194-197)
- [[Monte Carlo Maintenance Simulation]] [uses:: Weibull Distribution] time to failure; also repair time distribution
- [[Monte Carlo Maintenance Simulation]] [produces:: Expected Number Of Failures] equations give only F(t), R(t)
- Time to Fail [is_a:: Random Variable] mean MTTF; wait time mean MWT; repair time mean MTTR (Fig 7.11)
- Deterministic Model [differs_from:: [[Monte Carlo Maintenance Simulation]]] fixed output vs output distribution (Fig 7.12-7.13)
- Monte Carlo Illustration [has_value:: reliability 87%] example output (Fig 7.13)
- [[Monte Carlo Maintenance Simulation]] [applies_to:: Small Data Sets] failure modes seen as man-made pre-programmed failure; author note, watch confidence (p.194)
- [[Monte Carlo Maintenance Simulation]] [uses:: Minitab] also MathCad, CEDAR Maintenance Optimizer, Weibull Smith (p.195)
- CM-Unplanned Model [has_parameter:: Production Period] (RBMM p.198)
- CM-Unplanned Model [has_parameter:: Shape Parameter Beta] with Scale Parameter Eta, see [[Weibull Analysis]]
- CM-Unplanned Model [has_parameter:: Scale Parameter Eta]
- CM-Unplanned Model [has_parameter:: MTTR]
- CM-Unplanned Model [has_parameter:: MWT]
- CM-Unplanned Model [has_parameter:: Restoration Factor] condition after repair, %
- CM-Unplanned Model [has_parameter:: Downtime Loss Rate] baht/h
- CM-Unplanned Model [has_parameter:: Labor And Spare Cost] labor/h, spare per event
- CM-Unplanned Model [produces:: Expected CM-Unplanned Count]
- CM-Unplanned Model [produces:: Total Downtime]
- CM-Unplanned Model [produces:: Availability] average %
- CM-Unplanned Model [produces:: Cost Per Operating Hour] and total cost
- Simulation Base Example [has_value:: beta = 3.788, eta about 13,130 h] TTF 16,000, 12,000, 11,000, 8,500 h; 3 years (RBMM p.199-203)
- Simulation Base Example [has_value:: 200,000 baht/h loss, 5,000 baht/h labor, 30,000 baht spare] inputs
- Simulation Base Example [has_value:: 1.76 CM-Unplanned, 17.57 h, 139 baht/h, 3.6 M baht, 99.93%] MTTR 8 + MWT 2 (MDT 10), 100% restoration (Fig 7.18-7.20)
- Simulation Reduced MDT Case [has_value:: 1.79 CM-Unplanned, 12.51 h, 99 baht/h, 2.6 M baht, 99.95%] MTTR 6, MWT 1 (MDT 7)
- Simulation 75% Restoration Case [has_value:: 2.18 CM-Unplanned, 21.76 h, 171.5 baht/h, 4.5 M baht, 99.91%]
- Simulation Base Example [has_value:: about 2 spares in 3 years] for Max/Min by lead time (p.203); see [[Spare Parts Management]]
- Scheduled Replacement Simulation [has_value:: every 16 months] PM MTTR 6 h, MWT 0, 100% restoration, 50,000 baht/h PM loss (Fig 7.23, RBMM p.204-206)
- Scheduled Replacement Simulation [has_value:: CM-Unplanned about 1.0, 2,120,922 baht]
- Scheduled Replacement Simulation [has_value:: Scheduled PM about 1.0, 387,360 baht, 6.46 h]
- Scheduled Replacement Simulation [has_value:: 2,508,282 baht, 96 baht/h, Availability 99.94%] 3-year total; sum checked (derived)
- Scheduled Replacement Simulation [differs_from:: Simulation Base Example] 2.5 vs 3.6 million baht without PM
- Scheduled Replacement Simulation [related_to:: Chapter 8 Simulator Table] between 15 and 18 month results (2.26 and 2.99 M baht); inputs differ, not directly comparable
- [[Monte Carlo Maintenance Simulation]] [input_to:: [[PM Interval Optimization]]] see also [[P-F Interval and Condition Monitoring]]
- [[Monte Carlo Maintenance Simulation]] [input_to:: [[Maintenance Budget]]] dominant failure modes about 80% first (p.206)
- Budget Simulation Example [has_value:: 0.35 CM-Unplanned per year] PM every 10 months, 1.3 M baht budget for 1 PM
- [[Redundancy and Standby Systems]] [uses:: [[Monte Carlo Maintenance Simulation]]] k/n reliability combination
- Demand Simulation [applies_to:: High/Medium Criticality Spares] chapter 9; see [[Spare Part Demand Forecasting]]
- Basic Average Method [uses:: Constant Failure Rate] (p.190-193)
- Basic Average Method [has_value:: MTBF 398,181.82 h] 100 units x 43,800 h = 4,380,000 unit-hours, 11 failures (checked)
- Basic Average Method [applies_to:: Pattern D] aggregate of all modes looks like beta = 1
- [[Monte Carlo Maintenance Simulation]] [depends_on:: [[Failure Data Recording]]] per failure mode: beta/eta, MTTR, MWT, cost, loss rate; check CMMS quality
- [[Monte Carlo Maintenance Simulation]] [selects:: PM Interval] try several intervals, rank total cost
- [[Monte Carlo Maintenance Simulation]] [applies_to:: [[Failure Mode]]] one simulation per failure mode of [[Maintainable Item]]
- [[OREDA]] [input_to:: [[Monte Carlo Maintenance Simulation]]] prior for constant rate only (wiki note) [confidence:: low]
- [[Monte Carlo Maintenance Simulation]] [related_to:: [[Statistical Distributions for Maintenance]]]

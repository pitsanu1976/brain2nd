---
title: Monte Carlo Maintenance Simulation
created: 2026-10-20
updated: 2026-10-20
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

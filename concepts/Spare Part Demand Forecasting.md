---
title: Spare Part Demand Forecasting
created: 2026-10-21
updated: 2026-10-21
type: concept
tags: [spare-parts, statistics, reliability, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Spare Part Demand Forecasting

หน้านี้อธิบายวิธีที่ RBMM บทที่ 9 (และบทที่ 7, 12) ใช้คาดการณ์ "ความต้องการอะไหล่" ของงานนอกแผน มี 3 ระดับ: Basic Average Method (MTBF), Poisson (อะไหล่ใช้น้อย เป็นจำนวนเต็ม) และ Monte Carlo Simulation ที่เชื่อมแผนงาน PM กับ failure mode (beta, eta) หลักคิดคือ แม้ทำ PM เข้มเพียงใดก็ยังมีโอกาสเสีย จึงคาดจำนวน CM-Unplanned ได้ และการเตรียมอะไหล่คือการ "ซื้อความเสี่ยง" (RBMM p.256) ผลลัพธ์ป้อนไปคำนวณ Max/Min ใน [[EOQ and Reorder Point]] และ [[Spare Part Criticality and Risk]] ภาพรวมอยู่ที่ [[Spare Parts Management]]

## Demand Side ของอะไหล่ (RBMM p.241)

- ความต้องการอะไหล่นอกแผน = จำนวน CM-Unplanned ที่คาด คำนวณจากประวัติเสีย + ตัวแปรสถิติ (beta, eta ของ Weibull) + Monte Carlo ดู [[Weibull Analysis]]
- PM ลดโอกาส CM-Unplanned; เพิ่ม PM จนไม่มี CM-Unplanned ก็ได้แต่ต้นทุนรวมสูง จึงต้องหา optimum ([[PM Interval Optimization]])
- อะไหล่สำรองคลังมีไว้รับความเสี่ยงที่เหลือ
- ทางเลือกตามคาบ: ตัวอย่างในหนังสือ Part Replacement ที่คาบ optimum ประมาณ 10 เดือน ต้องการอะไหล่ประมาณ 1 ชิ้นใน 3 ปี ตามแผน (RBMM p.230)

## วิธีที่ 1: Basic Average Method (MTBF) (RBMM p.257-258)

```
MTBF = (จำนวน unit x ชั่วโมงทำงานต่อ unit) / จำนวนครั้งที่เสีย
Expected failures = (unit-hours ของกลุ่มใหม่) / MTBF
```

ตัวอย่างรูปที่ 9.14:

| รายการ | ค่า |
|---|---|
| จำนวน unit | 100 |
| ชั่วโมงต่อ unit | 43,800 h (5 ปี) |
| unit-hours รวม | 4,380,000 |
| failures | 11 |
| MTBF | 398,181.82 h |
| กลุ่มใหม่ | 15 units, 3 ปี (26,280 h) = 394,200 unit-hours |
| Expected failures | 394,200 / 398,181.82 = 0.99 ~ 1 ครั้ง |

ตรวจเลข (derived): 100 x 43,800 = 4,380,000; หาร 11 = 398,181.8 ตรงกับหนังสือ; 15 x 26,280 = 394,200 ตรง

ข้อจำกัด: สมมติ constant failure rate ซึ่งมักไม่จริง; ต้องใช้ข้อมูลเครื่องจำนวนมาก; หนังสือถือว่าวิธีดีที่สุดคือ simulation (RBMM p.258) เหมาะกับอะไหล่ Low Criticality และใช้เป็นค่าเริ่มต้น (กล่อง 3-4 ของรูปที่ 9.2)

## วิธีที่ 2: Poisson / HPP (RBMM p.258-261, p.371-373)

```
P(X = x) = e^(-D) x D^x / x!

x = จำนวนครั้งที่เกิดเหตุการณ์ (จำนวนเต็ม เริ่มจาก 0)
D = ค่าเฉลี่ยการเกิดในช่วงที่พิจารณา
```

เรียกอีกชื่อ Homogeneous Poisson Process (HPP) สมมติว่าเหตุการณ์แต่ละช่วงอิสระกัน และโอกาสเกิดในช่วงสั้น ๆ แปรผันตามความยาวช่วง (RBMM p.258); ใน Excel ใช้ POISSON(x, mean, cumulative) (FALSE = โอกาสพอดี, TRUE = สะสม) ดู [[Statistical Distributions for Maintenance]]

### ตัวอย่าง D = 3 ต่อปี (RBMM p.259-260, รูปที่ 9.17)

เฉลี่ย 3 ครั้ง/ปี โอกาสเกิดพอดี 1 ครั้ง = 14.936% (RBMM p.258)

| x | P(x) | Cumulative |
|---|---|---|
| 0 | 0.0498 | 0.0498 |
| 1 | 0.1494 | 0.1991 |
| 2 | 0.2240 | 0.4232 |
| 3 | 0.2240 | 0.6472 |
| 4 | 0.1680 | 0.8153 |
| 5 | 0.1008 | 0.9161 |
| 6 | 0.0504 | 0.9665 |
| 7 | 0.0216 | 0.9881 |

(ตัดแถว x = 8-10 ดู RBMM p.260) ตรวจ (derived): P(1) = e^-3 x 3 = 0.1494 ตรงกัน

### ตารางสะสม (รูปที่ 9.18, บางแถว)

| เฉลี่ย/ปี | x=2 | x=3 | x=4 | x=5 | x=6 | x=7 |
|---|---|---|---|---|---|---|
| 2 | 0.677 | 0.857 | 0.947 | 0.983 | 0.995 | 0.999 |
| 4 | 0.238 | 0.433 | 0.629 | 0.785 | 0.889 | 0.949 |
| 6 | 0.062 | 0.151 | 0.285 | 0.446 | 0.606 | 0.744 |

ตัวอย่างการอ่าน (RBMM p.261): ใช้เฉลี่ย 4 ชิ้น/ปี เก็บ 4 = ประมาณ 63%, เก็บ 5 = 78.5%, เก็บ 6 = 88.9%, เก็บ 7 = 94.9% ต้องการอย่างน้อย 90% จึงเก็บ 7 ชิ้น หนังสือสังเกตว่าระดับที่ได้ค่อนข้างสูงเพราะคำนวณบนฐานค่าเฉลี่ย

## ตัวอย่าง D = 5.333 และปรับตาม Lead Time (RBMM p.371-373, ch12)

ข้อมูลเบิกอะไหล่ A ย้อนหลัง 3 ปี: 5, 7, 4 ชิ้น/ปี เฉลี่ย D = 5.333 (derived: 16/3 = 5.333 ตรงกับหนังสือ)

| เบิก (ชิ้น/ปี) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| P (%) | 0.483 | 2.575 | 6.866 | 12.207 | 16.276 | 17.361 | 15.432 | 11.758 | 7.838 |
| P สะสม (%) | 0.483 | 3.058 | 9.924 | 22.131 | 38.407 | 55.768 | 71.200 | 82.958 | 90.796 |

| เบิก (ชิ้น/ปี) | 9 | 10 | 11 | 12 |
|---|---|---|---|---|
| P (%) | 4.645 | 2.477 | 1.201 | 0.534 |
| P สะสม (%) | 95.441 | 97.919 | 99.120 | 99.654 |

(ตัดแถว x = 13-15 ดูต้นฉบับ) การตีความ: ไม่เบิกเลย 0.483%; เบิก 5 ชิ้นเป็นไปได้สูงสุด 17.361%; เบิกไม่เกิน 5 ชิ้น 55.768%; ไม่เกิน 11 ชิ้น 99.12%

### ปรับเป็นช่วง Lead Time 45 วัน

```
D_LT = (อัตราใช้ต่อปี x Lead Time) / 365
     = 5.333 x 45 / 365 = 0.6575
```

(derived ตรงกับหนังสือ)

| เบิกใน Lead Time | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| P (%) | 51.813 | 34.069 | 11.201 | 2.455 | 0.404 | 0.053 |
| P สะสม (%) | 51.813 | 85.881 | 97.082 | 99.537 | 99.941 | 99.994 |

ข้อสรุปของหนังสือ: เก็บสำรอง 3 ชิ้น มั่นใจ 99.537% ว่าพอใช้ในช่วง Lead Time (RBMM p.373) ตรวจ (derived): P(0) = e^-0.6575 = 0.518 ตรงกัน ระดับสำรองจริงขึ้นกับความสำคัญของอะไหล่และความเสี่ยงที่ยอมรับ ดู [[Spare Part Criticality and Risk]]

### ข้อควรระวังเรื่องหน่วย

- ตารางแรก (D = 5.333) เป็นการแจกแจงจำนวนเบิกต่อ "ปี" ส่วนตารางที่สอง (D = 0.6575) เป็นต่อ "ช่วง Lead Time" ต้องปรับ D ให้ตรงช่วงเวลาก่อนอ่านเสมอ
- สำหรับ demand ที่กระโดดและต่ำ Poisson เหมาะกว่า Normal ใน [[EOQ and Reorder Point]]

## วิธีที่ 3: Monte Carlo Spare Part Simulation

### Medium Criticality (RBMM p.261-262, รูปที่ 9.19)

- Spare Part Model รับ input: ข้อมูลอะไหล่ (ราคา, Lead Time, ค่าเก็บ, ค่าจัดซื้อ) + ประวัติเบิก (อุปกรณ์, วันที่, ปริมาณ, stock out cost)
- ปรับ Max/Min ทีละค่า แล้วคำนวณจำนวนครั้งที่เบิกไม่ได้, stock out rate %, ระดับเฉลี่ย, Cost Ratio, ค่าใช้จ่ายรวม
- จำนวนรอบ simulation ต้องมากพอ
- ตัวเลขผลลัพธ์ดู [[Spare Part Criticality and Risk]]

### High Criticality (RBMM p.263-264, รูปที่ 9.20)

- Spare Part DSx Model f(x) รับข้อมูลงานบำรุงรักษาที่เรียกใช้อะไหล่: Equipment, Failure Mode, Beta, Eta, ประเภทงาน, Stock out Cost Rate
- model ผูกกับงานตามแผนที่เลือก ถ้าต้องการลด demand ก็ปรับนโยบาย PM ได้ (Demand Side)
- รายละเอียดวิธีจำลองทั่วไป ดู [[Monte Carlo Maintenance Simulation]]

### Demand จาก simulation ของบทที่ 7 (RBMM p.201-206)

กรณีฐาน (Weibull beta = 3.7888, eta = 13,130 h ตามบทที่ 7-8; 3 ปี; MDT = 10 h):

| กรณี | CM-Unplanned (ครั้ง/3 ปี) | ค่าใช้จ่ายรวม | อ้างอิง |
|---|---|---|---|
| ปล่อยเสีย (ไม่ทำ PM) | 1.76 (~2) | 3.6 ล้านบาท | รูปที่ 7.18 |
| ลด MTTR/MWT เหลือ 6 และ 1 h | 1.79 | 2.6 ล้านบาท | รูปที่ 7.19 |
| ซ่อมสภาพ 75% | 2.18 | 4.5 ล้านบาท | รูปที่ 7.20 |
| เปลี่ยนตามแผนทุก 16 เดือน | ประมาณ 1.0 (+ PM ประมาณ 1.0) | 2.5 ล้านบาท (2,508,282) | รูปที่ 7.23 |

- กรณีปล่อยเสียต้องการอะไหล่ 2 ชิ้นใน 3 ปี เพื่อตั้ง Max/Min ให้เหมาะกับ Lead Time (RBMM p.201-203)
- กรณีเปลี่ยนตามแผนทุก 16 เดือน ต้องการอะไหล่ 1 ชิ้นสำหรับ CM + 1 ชิ้นสำหรับ PM (ซื้อตรงตามแผน) ความต้องการสะสมลดลงราวครึ่งหนึ่ง (RBMM p.204-206)
- ตัวเลข beta/eta ชุดนี้เป็นตัวอย่างของหนังสือ ไม่ใช่ข้อมูล compressor

## เลือกวิธีตามกลุ่มอะไหล่ (สรุป)

| กลุ่ม | วิธีคาดการณ์ demand |
|---|---|
| Fast Moving | ค่าเฉลี่ย + variance (Normal) -> EOQ |
| Low Criticality | Average (MTBF) หรือ Poisson + Confidence |
| Medium Criticality | Average หรือ Monte Carlo + Cost Ratio |
| High Criticality | Monte Carlo ผูก failure mode, beta, eta + แผน PM |

(RBMM p.238)

## เชื่อมโยงกับ compressor failure hierarchy

- Spare Part DSx Model ต้องระบุ Equipment + Failure Mode + beta/eta ซึ่งตรงกับระดับ [[Failure Mode]] และ [[Maintainable Item]] ใน [[ISO 14224]]; ต้องการ beta/eta ต่อ failure mode จากประวัติซ่อม
- [[OREDA]] ให้ failure rate ระดับ item ส่วนใหญ่เป็น constant rate จึงใช้กับ Basic Average Method ได้ (เปลี่ยน failure rate เป็น MTBF แล้วคูณ unit-hours) แต่หนังสือเตือนว่าสมมติ constant rate (RBMM p.257) และใช้หาคาบ PM ไม่ได้ (RBMM p.223, p.231) ตัวเลขใน wiki นี้ไม่ใช่ข้อมูล asset ของ Valeura
- ถ้า failure mode เป็นแบบ random (เช่น เกิดจาก human error) การเปลี่ยนตามแผนไม่ลดโอกาสเสีย ต้องสต็อกอะไหล่รับ ตามข้อสรุปเรื่อง Exponential ในบทที่ 12 (ไม่ได้ระบุเลขหน้าในบันทึก ตรวจกับต้นฉบับ) ดู [[Failure Patterns and Bathtub Curve]]
- ถ้า P-F interval ของ condition monitoring สั้นกว่า Lead Time ต้องสต็อก ดู [[P-F Interval and Condition Monitoring]]

## ดูเพิ่ม

- [[Spare Parts Management]]
- [[EOQ and Reorder Point]]
- [[Spare Part Criticality and Risk]]
- [[Monte Carlo Maintenance Simulation]]
- [[Statistical Distributions for Maintenance]]
- [[Weibull Analysis]]

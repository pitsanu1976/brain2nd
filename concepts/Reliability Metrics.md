---
title: Reliability Metrics
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [reliability, statistics, weibull, kpi, failure-rate, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Reliability Metrics

รวมตัวชี้วัดความเชื่อถือได้ที่คำนวณจาก pdf ของ failure: F(t), R(t), failure rate λ(t), MTTF/MTBF, Time to Target Reliability, Conditional Reliability, Additional Operating Time, Availability และ Maintainability (MTTR) พร้อมตัวอย่างตัวเลขจาก RBMM ch6 และ ch12 หน้านี้ flag สูตรที่หนังสือพิมพ์ผิดไว้ (T(R), ขอบเขตปริพันธ์ MTTF) และให้ค่าที่ถูกต้องเทียบข้างกัน

ตัวอย่างหลักใช้ Weibull β = 3.7888, η = 13,130.8 ชม. (Y regression ของ TTF 8,500/11,000/12,000/16,000) ดูที่มาใน [[Weibull Analysis]]

## ฟังก์ชันพื้นฐาน (RBMM p.166-168, p.367-370)

```
F(t) = Q(t) = ∫0..t f(s) ds = 1 - exp(-(t/η)^β)     (unreliability / probability of failure)
R(t) = 1 - F(t) = ∫t..∞ f(s) ds = exp(-(t/η)^β)     (reliability)
f(t) = -dR(t)/dt                                     (หนังสือพิมพ์ไม่มีเครื่องหมายลบ)
λ(t) = f(t)/R(t) = (β/η)(t/η)^(β-1)                  (hazard)
```

พื้นที่ใต้ pdf รวม = 1; ที่เวลา a พื้นที่ซ้าย = F(a) พื้นที่ขวา = R(a) (RBMM p.368-370)

กรณี β = 1: R(t) = e^(-t/η), λ = 1/η คงที่ (constant failure rate) ในตัวอย่าง 1/13,130 = 0.0000761 = 0.0067%/ชม. ใช้ไม่ได้เพราะ β จริง ≈ 3.79 (RBMM p.168)

## ตัวอย่างที่ t = 10,000 ชม. (RBMM p.166-168, Fig 6.15)

| ตัวชี้วัด | ค่า |
|---|---|
| F(10,000) | 29.97% |
| R(10,000) | 70.03% |
| λ(10,000) | 0.0135% ต่อชม. (หนังสือใช้คำว่า "ต่อหน่วยเวลา") |
| MTTF | 11,865.51 ชม. |

ตรวจ derived: λ = (3.7888/13,130.8)(10,000/13,130.8)^2.7888 ≈ 1.35 x 10^-4 ต่อชม. ตรงกับ 0.0135%; MTTF = η Γ(1+1/β) ≈ 11,866 ชม. ตรงกับหนังสือ

## MTTF และ MTBF

- **MTTF** = ∫ t f(t) dt = η Γ(1 + 1/β) เป็นค่าเฉลี่ยเชิงสถิติ ไม่ใช่ค่าเฉลี่ยเลขคณิตตรง ๆ (RBMM p.168)
- **flag: ขอบเขตปริพันธ์** หนังสือเขียนปริพันธ์จาก -∞ ถึง ∞ ค่าที่ถูกคือ 0 ถึง ∞ (เวลาไม่ติดลบเมื่อ γ = 0) ผลเลขในหนังสือสอดคล้องกับสูตร Γ (หนังสือพิมพ์ผิด)
- η = MTTF/MTBF ก็ต่อเมื่อ β = 1 เท่านั้น (RBMM p.169) ตัวอย่าง β = 3.79: η = 13,131 แต่ MTTF = 11,866
- **MTBF = MTTF + MTTR + MWT** (MWT = waiting time) (RBMM p.190-193, ch7)

ตัวอย่างค่าเฉลี่ย (RBMM p.190-193): ช่วงสังเกต 47,840 ชม. เสีย 4 ครั้ง เฉลี่ย 11,960 ชม. คาดเสีย 2.20 ครั้งใน 3 ปี; อีกวิธี MTTF = 11,875, MTTR+MWT = 10, MTBF = 11,885 ชม. คาด 2.21 ครั้ง (ตัด 300 ชม. สุดท้ายที่ยังไม่เสีย) สูตรนี้ใช้ได้เฉพาะ pattern D (β = 1) และเป็นค่ารวมทุก failure mode ซึ่งมักดูเหมือน β = 1 เสมอ ดู [[Failure Patterns and Bathtub Curve]]

## Time to Target Reliability (RBMM p.169)

เวลาใช้งานที่ R ลดถึงค่าเป้าหมาย R*:

| | สูตร | ค่าที่ R* = 0.8 |
|---|---|---|
| หนังสือ | T(R) = η [1 - ln(R)]^(1/β) | 13,847.81 ชม. (Fig 6.16) |
| ถูกต้อง (derived จากการ invert R(t)) | T(R) = η (-ln R)^(1/β) | ประมาณ 8,837 ชม. |

ตรวจ: (8,837/13,130.8)^3.7888 = 0.2231 จึงได้ R(8,837) = exp(-0.2231) = 0.80 ส่วน R(13,848) ≈ 0.29 ไม่ใช่ 0.80 ดังนั้นสูตรและค่าในหนังสือ **ผิด** (หนังสือพิมพ์ผิด ตัวเลข 13,847.81 สอดคล้องกับสูตรที่พิมพ์ผิด) ห้ามนำไปใช้ ใช้สูตรถูกต้อง ตัวเลข 8,837 เป็น derived ของ wiki (confidence medium)

## Conditional Reliability (RBMM p.169-170)

```
R(t2 | t1) = R(t2) / R(t1)
```

ตัวอย่าง Fig 6.17: t1 = 10,000 (R = 70.03%), t2 = 12,000 (R = 49.12%) ได้ 70.14% ใช้ตอบว่าเครื่องที่ใช้มา 10,000 ชม. จะรอดถึง turnaround อีก 2,000 ชม. ได้กี่ % เพื่อตัดสินเปลี่ยนก่อนหยุดใหญ่

**Additional Operating Time of Survival** (Fig 6.18): ถ้าต้องการโอกาสรอดต่อ 80% หลังใช้มา 10,000 ชม. ใช้ต่อได้อีก 1,369.52 ชม. (RBMM p.170)

## Availability (RBMM p.176)

Availability = เวลาที่พร้อมใช้ / เวลาที่ต้องการ ขึ้นกับทั้ง reliability และเวลาซ่อม เครื่องที่ reliability ต่ำแต่ซ่อมเร็วอาจ availability สูงกว่าเครื่อง reliability สูงที่ซ่อมนาน

ตัวอย่าง: 3 ปี เสีย 3 ครั้ง ครั้งละ 10 ชม. สมมติ constant rate (3 ครั้ง/3 ปี) R(2 ปี) = e^(-2/3) = 51.34%; Availability(3 ปี) = 1 - (3 x 10)/(3 x 8,760) = 99.89% ดูตัวชี้วัดระดับ KPI ใน [[Availability and OEE]]

## Maintainability และ MTTR (RBMM p.176-177)

ถ้าเวลาซ่อมเป็น Exponential: M(t) = 1 - exp(-t/MTTR) ตัวอย่าง MTTR = 3.5 ชม., t = 3 ชม. ได้ M(3) = 0.5756 หมายถึงโอกาส 57.56% ที่ซ่อมเสร็จใน 3 ชม. ต้องเทียบ maintainability ภายใต้หน่วยงานบำรุงรักษาเดียวกัน เพราะเวลาซ่อมขึ้นกับ work control และทีม

## Failure Tree (RBMM p.175)

ใช้คำนวณ F รวม = 1 - R รวม ตรงข้ามกับ RBD: Ft = 1 - Π(1 - Fi) โดย Fi = 1 - Ri (อนุกรมใน RBD เทียบเท่า OR-gate; หนังสือใช้สัญลักษณ์ขนาน) ดู [[Reliability Block Diagram]]

## ใช้ในการตัดสินใจ

- PM ก่อน turnaround: ใช้ conditional reliability เทียบกับระดับ risk ที่ยอมรับ
- คาดจำนวน CM-Unplanned ใน 3 ปีสำหรับ max/min อะไหล่ (Weibull + simulation: 1.76 ครั้ง ดู [[Monte Carlo Maintenance Simulation]])
- หา PM interval ที่ต้นทุนต่ำสุด ดู [[PM Interval Optimization]]
- หนังสือเตือนว่าค่าทั้งหมดเป็นค่าประมาณและควรมี confidence bound (RBMM p.165)

## เชื่อมโยงกับ compressor failure hierarchy

- [[OREDA]] ให้ failure rate λ ต่อ 10^6 ชม. ซึ่ง MTTF = 1/λ ใช้ได้เมื่อ β = 1 เท่านั้น ถ้าโหมดมี β > 1 ใช้ MTTF = η Γ(1+1/β) แทน
- MTTR/MWT ตรงกับ downtime และ man-hours ใน maintenance record ของ [[ISO 14224]] ใช้คำนวณ availability ของ [[Compressor]] ทั้ง unit
- ตัวชี้วัดต้องคิดต่อ failure mode ใน [[Failure Mode]] ไม่ใช่ทั้งเครื่อง

## ดูเพิ่ม

- [[Weibull Analysis]]
- [[Censored Data]]
- [[Reliability Block Diagram]]
- [[Statistical Distributions for Maintenance]]
- [[Maintenance KPIs]]

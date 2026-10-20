---
title: Weibull Analysis
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [weibull, reliability, statistics, failure-rate, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Weibull Analysis

**Weibull Analysis** คือการ fit การแจกแจง Weibull กับข้อมูล Time to Fail (TTF) ของ **หนึ่ง failure mode** เพื่อได้ shape parameter β และ scale parameter η แล้วใช้ตัดสินใจเลือกประเภทงาน PM, คาบเวลา และการวางแผนอะไหล่ หนังสือ RBMM ใช้ Weibull เป็นเครื่องมือหลักแทนการสมมติ constant failure rate (RBMM p.154, p.378) หน้านี้สรุปพารามิเตอร์ วิธีประมาณ (probability plot, Y/X regression, MON สำหรับ censored data) และกระทบยอดค่า β ที่ต่างกัน (3.5 / 3.7888 / 3.94) ของตัวอย่างเดียวกัน

## พารามิเตอร์ (RBMM p.156, p.378)

| พารามิเตอร์ | ชื่อ | ความหมาย |
|---|---|---|
| β (beta) | shape | รูปร่างของการกระจาย และแนวโน้ม failure rate |
| η (eta) | scale / characteristic life | เวลาที่ F(t) = 63.2% เสมอ ไม่ว่า β เท่าใด |
| γ (gamma) | location | failure-free time; ในงาน maintenance ตั้ง γ = 0 |

```
f(t)  = (β/η) * ((t-γ)/η)^(β-1) * exp(-((t-γ)/η)^β)      (pdf)
F(t)  = 1 - exp(-(t/η)^β)                                   (γ = 0)
R(t)  = exp(-(t/η)^β)
λ(t)  = f(t)/R(t) = (β/η) * (t/η)^(β-1)                     (hazard)
```

การตีความ β (RBMM p.156-157, p.379): β < 1 failure rate ลดลง (infant mortality, hyper-exponential); β = 1 คงที่ (random, Exponential, η = MTBF); β > 1 เพิ่มขึ้น (wear-out); β >> 1 เสียเกาะกลุ่มตามอายุชัดเจน ดู [[Failure Patterns and Bathtub Curve]] สำหรับ pattern A-E และกฎเลือก task

## ข้อควรระวังสำคัญ

- วิเคราะห์ **ทีละ failure mode** เสมอ (RBMM p.158) ถ้ารวมหลาย mode แล้ว fit จะได้ β ≈ 1 เกือบเสมอ และสรุปผิดว่า random (RBMM p.186, p.190-193) ดู [[Failure Mode]]
- ผู้ผลิตไม่ให้ค่า β, η (ความลับทางการค้า) หน่วย maintenance ต้องประมาณจากประวัติของตนเอง (RBMM p.158)
- ค่าที่ได้เป็น **ค่าประมาณ** ต้องมี confidence bound เพิ่ม (RBMM p.165) หนังสือไม่แสดงวิธีคำนวณ
- ข้อมูลแบบ censored ต้องปรับตำแหน่ง rank ก่อน plot ดู [[Censored Data]]

## วิธีประมาณ β, η

1. **Weibull probability paper** (RBMM p.162-164, p.379-381): เรียง TTF น้อย→มาก ประมาณโอกาสเสียด้วย Median Rank (Benard) แล้ว plot เป็นเส้นตรง β = slope, η = เวลาที่เส้นตัด 63.2% (อ่านด้วยตา)
2. **Linear regression** (RBMM p.164, p.381-382): แปลงเป็นเส้นตรง

```
MR(j) = (j - 0.3) / (N + 0.4)          j = ลำดับ, N = จำนวนข้อมูล
x = ln(T),  y = ln(ln(1/(1 - MR)))     ->  y = a x + b,  a = β,  b = -β ln(η)

Y regression:  a = (Σy·Σx - N·Σxy) / ((Σx)^2 - N·Σx^2)
X regression:  a = ((Σy)^2 - N·Σy^2) / (Σx·Σy - N·Σxy)
η = exp( -(Σy - a·Σx) / (N·a) )
```

3. MLE ถูกกล่าวถึงเป็นอีกวิธี แต่หนังสือไม่ได้แสดงตัวอย่าง (RBMM p.158)

## ตัวอย่างหลัก TTF 8,500 / 11,000 / 12,000 / 16,000 ชม. (N = 4)

ข้อมูล (RBMM p.163-164, p.382-384):

| j | TTF (ชม.) | Median Rank | x = ln T | y |
|---|---|---|---|---|
| 1 | 8,500 | 0.159091 | 9.047821 | -1.752894 |
| 2 | 11,000 | 0.386364 | 9.305651 | -0.716717 |
| 3 | 12,000 | 0.613636 | 9.392662 | -0.050266 |
| 4 | 16,000 | 0.840909 | 9.680344 | 0.608830 |

ผลรวม: Σx = 37.426478, Σy = -1.911048, Σx² = 350.389363, Σy² = 3.959523, Σxy = -17.107843

### กระทบยอด β ที่ต่างกัน

| ค่า | η (ชม.) | วิธี | ที่มา |
|---|---|---|---|
| β ≈ 3.5 | ≈ 13,000 | อ่านจาก Weibull probability paper ด้วยตา (ป้ายบนรูปเขียน B ≈ 3.7) | RBMM p.164 (Fig 6.11) |
| β ≈ 3.7 | ≈ 13,000 | อ่านจาก probability plot | RBMM p.381 (Fig 12.14) |
| β = 3.7888 | 13,130.8 | **Y regression** (ลด error แนวแกน y) | RBMM p.164, p.384; ch7 ใช้ 3.788(8) |
| β = 3.9406 | 13,067.2 | **X regression** (ลด error แนวแกน x) | RBMM p.384 |

สรุป: ความต่างมาจาก **วิธีประมาณ** ไม่ใช่ข้อมูลต่างกัน การอ่านกราฟด้วยตาให้ค่าประมาณคร่าว ๆ (3.5-3.7), Y กับ X regression ให้ค่า 3.79 กับ 3.94 เพราะตัวแปรที่ถูกลดระยะต่างกัน ด้วยข้อมูลเพียง 4 จุดช่วงของ β กว้าง (ประมาณ 3.5-3.9) ข้อสรุปเชิงคุณภาพไม่เปลี่ยน คือ β >> 1 (wear-out, pattern A) ตัวเลขต่อเนื่องในหนังสือทั้งหมด (F, R, MTTF, conditional reliability) ใช้ **Y regression** β = 3.7888, η = 13,130.8 (บางจุดหนังสือพิมพ์ 3.7883 เป็น exponent ใน F(10000) ซึ่งเป็น rounding, RBMM p.166)

ห้ามสับสนกับ β = 3.5008 (η = 996.70 วัน) ของ **ตัวอย่างมอเตอร์ bearing** ใน ch12 (RBMM p.390) ซึ่งเป็นข้อมูลคนละชุด ใช้ MON ดู [[Censored Data]]

ค่าที่คำนวณจาก β = 3.7888, η = 13,130.8 ดู [[Reliability Metrics]]: F(10,000) = 29.97%, R = 70.03%, λ = 0.0135%/ชม., MTTF = 11,865.51 ชม. (RBMM p.166-168)

## ผลการเสียตัวอย่างอื่นในหนังสือ

- Pattern ตัวอย่าง A-E ใช้ β = 15, 3, 1.5, 1, 0.5 (RBMM p.155-158) ดู [[Failure Patterns and Bathtub Curve]]
- ตัวอย่าง impeller / bearing β = 4.352 / 3.876 (wear-out) เทียบกับ control failure β = 0.997 (random) (RBMM p.136, p.145-148, จาก ch5)
- Simulation: ใส่ β, η, MTTR, MWT ในโมเดลได้ผล CM-Unplanned = 1.76 ครั้งใน 3 ปี, Availability 99.93% (RBMM p.199-203, ch7) ดู [[Monte Carlo Maintenance Simulation]]
- ใช้ผล Weibull หา PM interval ที่ต้นทุนต่อหน่วยเวลาต่ำสุด (ตัวอย่าง bearing: ~480 วัน) ดู [[PM Interval Optimization]]

## ข้อสังเกตเรื่องความถูกต้องของหนังสือ

- สูตร **Time to Target Reliability** ที่หนังสือพิมพ์ (RBMM p.169) ผิด ดู [[Reliability Metrics]]
- ปริพันธ์ MTTF ที่หนังสือเขียนจาก -∞ ถึง ∞ ผิดขอบเขต ดู [[Reliability Metrics]]
- ตัวอย่างต้นทุน PM: ตัวส่วนในหนังสือเขียนปริพันธ์ t f(t) จาก tp ถึง ∞ ตามทฤษฎี age replacement ควรเป็น 0 ถึง tp (RBMM p.391) ดู [[PM Interval Optimization]]

## เชื่อมโยงกับ compressor failure hierarchy

- ใช้ Weibull กับ **failure mode ระดับ maintainable item** (เช่น seal, bearing ใน [[Compressor]]) ไม่ใช่ทั้งเครื่อง ตรงกับลำดับชั้นใน [[Failure Hierarchy]] และ [[Maintainable Item]]
- ตาราง [[OREDA]] ให้ failure rate คงที่ (หน่วย failures ต่อ 10^6 ชม.) เท่ากับสมมติ β = 1 หนังสือเตือนว่าใช้ไม่ได้เมื่อ β ≠ 1 จึงควรบันทึก β ของ failure mode ที่สำคัญของ site เพิ่มเติม (ไม่มีข้อมูล β ของ asset Valeura ใน sources)
- ข้อมูลที่ต้องมีจาก CMMS: failure mode, วันติดตั้ง, วันเสีย, ชั่วโมงเดินเครื่อง, แยก failure กับ scheduled replacement (ตรงกับฟิลด์ [[ISO 14224]]) ดู [[Failure Cause Codes]] และ [[Resolution Codes]]

## ดูเพิ่ม

- [[Reliability Metrics]]
- [[Censored Data]]
- [[Failure Patterns and Bathtub Curve]]
- [[Statistical Distributions for Maintenance]]
- [[Reliability Block Diagram]]

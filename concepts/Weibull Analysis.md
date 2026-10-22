---
title: Weibull Analysis
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [weibull, reliability, statistics, failure-rate, book, iso-14224]
sources: [reliability-based-maintenance-management.md, iso-14224.md]
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

## แนวทางของ ISO 14224 (sources: iso-14224.md)

Annex C.1.11 (p.209-210) ให้เกณฑ์เสริมที่ไม่ขัดกับ RBMM:

- ใช้ Weibull เมื่อ equipment type มี failure **แบบเดียวกัน อย่างน้อย 5 ครั้ง** ที่ severity class I-XII (ตาม Table C.2 ดู [[Failure Impact Classification]]) ส่วน RCA ให้ทำกับ severity I-VIII และ bad actors
- ข้อมูล failure date จำเป็นต่อ lifetime analysis (TTT-plot, Weibull) Annex D ระบุว่าไม่ควรทิ้ง (Table D.3, p.230-234)
- ISO ระบุว่า β = 1 อาจเกิดจากการรวม failure mode หรืออุปกรณ์ต่างชนิด ตรงกับคำเตือนของ RBMM ข้างบน

| β | ความหมายตาม ISO (ถอดความ) | แนวทาง |
|---|---|---|
| < 1.0 | infant mortality (ติดตั้งไม่ดี, defect ผลิต, start-up ผิด) | ตรวจ installation และ commissioning |
| = 1.0 | random (human error, foreign object หรือการรวม mode ต่างชนิด) | predictive maintenance หรือ condition monitoring |
| 1.0-4.0 | early wear-out (low-cycle fatigue, bearing ส่วนใหญ่, corrosion, erosion) | PM คุ้ม |
| >= 4.0 | old-age wear-out (เช่น stress corrosion) ยิ่งชันยิ่งทำนายได้ | กำหนดรอบ overhaul จาก "β life" บน Weibull plot |

ข้อสังเกต: RBMM แบ่ง β > 1 เป็น wear-out ก้อนเดียว (p.156-157) ISO แบ่งละเอียดขึ้นที่ 4.0 เป็นการเสริม ไม่ใช่ขัดแย้ง ดังนั้นตัวอย่าง β = 3.79 อยู่ในกลุ่ม early wear-out ของ ISO และ β = 3.94 ก็ยังต่ำกว่า 4.0 (derived) ISO ยังแนะนำ Weibull กับ component และ power law กับ repaired system เมื่อมี wear-out (cl. C.3.1.2, p.214-215) ส่วนการประมาณ λ แบบคงที่ดู [[Failure Rate Estimation]]

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

## Triplets

- [[Weibull Analysis]] [is_a:: Statistical Analysis Method] fit Weibull to TTF of one failure mode
- [[Weibull Analysis]] [uses:: Weibull Distribution]
- [[Weibull Analysis]] [uses:: Time to Fail] TTF data of one failure mode
- [[Weibull Analysis]] [applies_to:: [[Failure Mode]]] one failure mode at a time (RBMM p.158)
- [[Weibull Analysis]] [applies_to:: [[Maintainable Item]]] failure mode at maintainable item level, not whole machine
- [[Weibull Analysis]] [produces:: Shape Parameter Beta]
- [[Weibull Analysis]] [produces:: Scale Parameter Eta]
- [[Weibull Analysis]] [selects:: PM Task Type] also PM interval and spare part planning (RBMM p.154, p.378)
- Weibull Distribution [has_parameter:: Shape Parameter Beta] shape, trend of failure rate (RBMM p.156, p.378)
- Weibull Distribution [has_parameter:: Scale Parameter Eta] characteristic life (RBMM p.156, p.378)
- Weibull Distribution [has_parameter:: Location Parameter Gamma] failure-free time, set to 0 in maintenance
- Scale Parameter Eta [has_value:: F(t) = 63.2%] time at which F(t) = 63.2% regardless of beta
- Location Parameter Gamma [has_value:: 0] in maintenance work
- Weibull Distribution [has_formula:: f(t) = (β/η) * ((t-γ)/η)^(β-1) * exp(-((t-γ)/η)^β)] pdf
- Unreliability Function [has_formula:: F(t) = 1 - exp(-(t/η)^β)] Weibull, γ = 0
- Reliability Function [has_formula:: R(t) = exp(-(t/η)^β)] Weibull
- Failure Rate [has_formula:: λ(t) = f(t)/R(t) = (β/η) * (t/η)^(β-1)] Weibull hazard
- Shape Parameter Beta [has_value:: β < 1] decreasing failure rate, infant mortality, hyper-exponential (RBMM p.156-157, p.379)
- Shape Parameter Beta [has_value:: β = 1] constant failure rate, random, Exponential, η = MTBF (RBMM p.156-157)
- Shape Parameter Beta [has_value:: β > 1] increasing failure rate, wear-out (RBMM p.156-157)
- Shape Parameter Beta [related_to:: [[Failure Patterns and Bathtub Curve]]] pattern A-E and task rules
- Mixed Failure Modes [produces:: β ≈ 1] fitting several modes together gives false random conclusion (RBMM p.186, p.190-193)
- [[Weibull Analysis]] [depends_on:: Maintenance History] manufacturers do not give β, η (RBMM p.158)
- [[Weibull Analysis]] [uses:: Confidence Bound] estimates need confidence bounds, method not shown (RBMM p.165)
- [[Weibull Analysis]] [uses:: [[Censored Data]]] adjust rank positions before plotting
- Weibull Probability Paper [is_a:: Weibull Estimation Method] β = slope, η read at 63.2% (RBMM p.162-164, p.379-381)
- Weibull Probability Paper [uses:: Median Rank] Benard
- Median Rank [has_formula:: MR(j) = (j - 0.3) / (N + 0.4)] Benard (RBMM p.164, p.381-382)
- Linear Regression [is_a:: Weibull Estimation Method] (RBMM p.164, p.381-382)
- Linear Regression [has_formula:: x = ln(T),  y = ln(ln(1/(1 - MR))), y = a x + b, a = β, b = -β ln(η)]
- Y Regression [has_formula:: a = (Σy·Σx - N·Σxy) / ((Σx)^2 - N·Σx^2)] minimizes error along y axis
- X Regression [has_formula:: a = ((Σy)^2 - N·Σy^2) / (Σx·Σy - N·Σxy)] minimizes error along x axis
- Scale Parameter Eta [has_formula:: η = exp( -(Σy - a·Σx) / (N·a) )] regression estimate
- MLE [is_a:: Weibull Estimation Method] mentioned without example (RBMM p.158)
- Weibull Example TTF 8500-16000 [has_value:: 8,500 / 11,000 / 12,000 / 16,000 h] N = 4 (RBMM p.163-164, p.382-384)
- Weibull Example TTF 8500-16000 [has_value:: β ≈ 3.5, η ≈ 13,000] probability paper by eye (RBMM p.164 Fig 6.11)
- Weibull Example TTF 8500-16000 [has_value:: β ≈ 3.7, η ≈ 13,000] probability plot (RBMM p.381 Fig 12.14)
- Weibull Example TTF 8500-16000 [has_value:: β = 3.7888, η = 13,130.8] Y regression, used for all later book figures (RBMM p.164, p.384)
- Weibull Example TTF 8500-16000 [has_value:: β = 3.9406, η = 13,067.2] X regression (RBMM p.384)
- Weibull Example TTF 8500-16000 [has_category:: Pattern A] β >> 1 wear-out
- Weibull Example TTF 8500-16000 [has_value:: F(10,000) = 29.97%] also R = 70.03%, λ = 0.0135%/h (RBMM p.166-168)
- Weibull Example TTF 8500-16000 [has_value:: MTTF = 11,865.51 h] (RBMM p.166-168)
- Motor Bearing Example [has_value:: β = 3.5008, η = 996.70 days] different dataset, uses MON (RBMM p.390)
- Motor Bearing Example [uses:: MON] see Censored Data
- [[Weibull Analysis]] [defined_in:: [[ISO 14224]]] Annex C.1.11 guidance (p.209-210)
- [[Weibull Analysis]] [applies_to:: At Least 5 Failures Of Same Type] severity class I-XII (ISO 14224 Annex C.1.11)
- [[Weibull Analysis]] [uses:: Failure Date] needed for lifetime analysis (ISO 14224 Table D.3)
- Shape Parameter Beta [has_value:: β < 1.0] infant mortality, check installation and commissioning (ISO 14224 Annex C.1.11)
- Shape Parameter Beta [has_value:: β = 1.0] random, predictive maintenance or condition monitoring (ISO 14224 Annex C.1.11)
- Shape Parameter Beta [has_value:: 1.0-4.0] early wear-out, PM worthwhile (ISO 14224 Annex C.1.11)
- Shape Parameter Beta [has_value:: β >= 4.0] old-age wear-out, overhaul cycle from beta life (ISO 14224 Annex C.1.11)
- Power Law [applies_to:: Repaired System] with wear-out; Weibull for components (ISO 14224 cl. C.3.1.2)
- Impeller Example [has_value:: β = 4.352] wear-out (RBMM p.136, p.145-148)
- Bearing Example [has_value:: β = 3.876] wear-out (RBMM p.136, p.145-148)
- Control Failure Example [has_value:: β = 0.997] random (RBMM p.136, p.145-148)
- [[Weibull Analysis]] [input_to:: [[Monte Carlo Maintenance Simulation]]] β, η with MTTR, MWT; CM-Unplanned 1.76 in 3 years, Availability 99.93% (RBMM p.199-203)
- [[Weibull Analysis]] [input_to:: [[PM Interval Optimization]]] bearing example about 480 days
- [[Weibull Analysis]] [input_to:: [[Reliability Metrics]]]
- [[OREDA]] [depends_on:: Constant Failure Rate] equivalent to assuming β = 1
- [[Weibull Analysis]] [uses:: [[CMMS]]] failure mode, install date, failure date, running hours
- [[Weibull Analysis]] [related_to:: [[Statistical Distributions for Maintenance]]]

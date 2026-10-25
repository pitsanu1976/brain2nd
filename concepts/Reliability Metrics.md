---
title: Reliability Metrics
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [reliability, statistics, weibull, kpi, failure-rate, book, iso-14224, cmrp, maintainability]
sources: [reliability-based-maintenance-management.md, iso-14224.md, cmrp.md]
confidence: medium
contested: true
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

### มุมมอง ISO 14224 ต่อ MTTF และ MTBF (sources: iso-14224.md, contested)

wiki เก็บสองมุมมองไว้คู่กัน ยังไม่เลือกว่าชุดไหนเป็นนิยามหลัก

| ประเด็น | RBMM (ข้างบน) | ISO 14224 Annex C |
|---|---|---|
| ค่าเฉลี่ยระหว่างเสียของ repairable item | MTBF = MTTF + MTTR + MWT | METBF = MUT + MDT (C.46); กรณีง่าย METBF = MTTF + MTTRes (C.11, C.47) (cl. C.5.3, p.223-224) |
| MTTF | เวลาเฉลี่ยก่อนเสีย (ใช้ในสูตร MTBF) | โดยเคร่งครัดคือเวลาถึงการเสียครั้งแรกของของใหม่ เท่ากับ MUT เฉพาะเมื่อซ่อมแล้วเหมือนใหม่ (cl. C.5.4-C.5.6, p.224-225) |
| MTTF = 1/λ | ใช้เมื่อ β = 1 | ใช้เมื่อ λ คงที่ (C.48) ตรงกัน |
| เวลาหยุด | MTTR + MWT | MDT รวมทุก delay (detection, อะไหล่, logistics, standby, reinstatement) |
| ชื่อ MTBF | ใช้ MTBF | ISO ใช้ METBF (elapsed time) ส่วน IEC นิยาม MTBF เป็น operating time (cl. 3.60, p.12) |

- แนวคิดตรงกัน (เวลาเสีย + เวลาหยุด) จึงถือเป็นต่างศัพท์และขอบเขต ไม่ใช่ข้อขัดแย้งด้านตัวเลข แต่ `contested: true` ตั้งไว้เพราะ wiki เขียนสูตร MTBF ของ RBMM เป็นข้อเท็จจริงทั่วไป ขณะที่ ISO ไม่มีสูตรนี้และจำกัดความหมาย MTTF ต่างออกไป
- ในข้อมูลหลายครั้งต่อ item ที่ซ่อมแล้วเหมือนใหม่ MTTF ของ RBMM จึงใกล้ MUT ของ ISO ถ้า item เสื่อมสะสม ค่าเฉลี่ยทำให้ตัดสินใจผิดได้ (cl. C.5.1, p.223)
- ISO แยก MTTR (ซ่อม), MTTRes (รวม detection), MRT, MART รายละเอียดและการจับคู่ MTTR/MWT ของ RBMM ดู [[Maintenance Time Definitions]]
- การประมาณ λ และช่วงความเชื่อมั่นของ ISO (λ = n/τ, chi-square) ตอบข้อเตือนของ RBMM ที่ว่าต้องมี confidence bound (p.165) ดู [[Failure Rate Estimation]]

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

### มุมมอง CMRP ต่อ MTTR (เพิ่ม 2026-10-25, sources: cmrp.md)

- สไลด์ [[CMRP Course]] ใช้สูตร M(t) แบบ exponential เดียวกัน และให้ μ = 1/MTTR, λ = 1/MTBF เฉพาะกรณี exponential (CMRP CMPR-04 p.13-14, p.30)
- แต่ **MTTR ของ CMRP จำกัดที่ active repair** 7 ขั้นตาม MIL-HDBK-472 (localization ถึง checkout) ไม่รวมเวลารออะไหล่/เครื่องมือ/admin ซึ่งเป็น inactive time (CMRP CMPR-04 p.39-40) ต่างจาก MTTR ของ RBMM ที่รวมเวลารอแรงงาน (RBMM p.49-51) และใกล้ MART ของ ISO 14224 เป็นความต่างของขอบเขตศัพท์ ไม่ใช่ตัวเลขขัดกัน ดู [[Maintenance Time Definitions]]
- CMRP แนะนำ lognormal สำหรับเวลาซ่อม (MTTR = exp(t' + s²/2)) และนิยาม Mmax ที่ percentile; ถ้าเป็น exponential Mmax(95%) ≈ 3 x MTTR (derived) รายละเอียด การจัดสรร MTTR และระดับงาน NF X60-000 อยู่ใน [[Maintainability]]
- ตัวอย่างของสไลด์ (CMRP CMPR-04 p.16): MTTF ของ 10 ชิ้น = 1538/10 = 153.8 ชม.; MTBF = n·m/r = 100 x 1000/25 = 4,000 ชม. (สไลด์ p.15 เรียก t ในสูตร MTTF ว่า "failure rates" ที่ถูกคือ failure times)

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
- [[Maintainability]]

## Triplets

- [[Reliability Metrics]] [uses:: Weibull Distribution] example β = 3.7888, η = 13,130.8 h (Y regression)
- Unreliability Function [has_formula:: F(t) = Q(t) = ∫0..t f(s) ds = 1 - exp(-(t/η)^β)] (RBMM p.166-168, p.367-370)
- Reliability Function [has_formula:: R(t) = 1 - F(t) = ∫t..∞ f(s) ds = exp(-(t/η)^β)] (RBMM p.166-168)
- Probability Density Function [has_formula:: f(t) = -dR(t)/dt] book prints without minus sign
- Failure Rate [has_formula:: λ(t) = f(t)/R(t) = (β/η)(t/η)^(β-1)] hazard
- Reliability Function [has_formula:: R(t) = e^(-t/η)] β = 1
- Failure Rate [has_formula:: λ = 1/η] β = 1, constant failure rate
- Constant Failure Rate Example [has_value:: 0.0067%/h] 1/13,130, invalid because β ≈ 3.79 (RBMM p.168)
- Weibull Example TTF 8500-16000 [has_value:: F(10,000) = 29.97%] (RBMM p.166-168 Fig 6.15)
- Weibull Example TTF 8500-16000 [has_value:: R(10,000) = 70.03%]
- Weibull Example TTF 8500-16000 [has_value:: λ(10,000) = 0.0135% per h]
- Weibull Example TTF 8500-16000 [has_value:: MTTF = 11,865.51 h]
- MTTF [has_formula:: ∫ t f(t) dt = η Γ(1 + 1/β)] statistical mean (RBMM p.168)
- RBMM MTTF Integral Limits [has_value:: -∞ to ∞] as printed, wrong (RBMM p.168) [contested:: true]
- Correct MTTF Integral Limits [has_value:: 0 to ∞] wiki correction, γ = 0 [contested:: true]
- RBMM MTTF Integral Limits [contradicts:: Correct MTTF Integral Limits] misprint; book numbers match Γ formula [contested:: true]
- Scale Parameter Eta [related_to:: MTTF] η = MTTF/MTBF only when β = 1; at β = 3.79 η = 13,131 vs MTTF = 11,866 (RBMM p.169)
- MTBF [has_formula:: MTTF + MTTR + MWT] (RBMM p.190-193) [contested:: true]
- METBF [has_formula:: MUT + MDT] (ISO 14224 C.46, cl. C.5.3) [contested:: true]
- METBF [has_formula:: MTTF + MTTRes] simple case (ISO 14224 C.11, C.47) [contested:: true]
- MTBF [contradicts:: METBF] same idea, different term and scope; RBMM vs ISO 14224 [contested:: true]
- MTTF [differs_from:: MUT] ISO MTTF strictly time to first failure of new item; equals MUT only if as-good-as-new (ISO 14224 cl. C.5.4-C.5.6)
- MTTF [has_formula:: 1/λ] when β = 1 (RBMM) or constant λ (ISO 14224 C.48)
- MDT [has_part:: MTTRes] MDT includes all delays: detection, spares, logistics, standby, reinstatement
- MTBF [differs_from:: METBF] ISO uses METBF elapsed time; IEC MTBF is operating time (ISO 14224 cl. 3.60)
- Mean Value Example [has_value:: 11,960 h] 47,840 h observed, 4 failures, 2.20 failures expected in 3 years (RBMM p.190-193)
- Mean Value Example [has_value:: MTBF = 11,885 h] MTTF = 11,875, MTTR+MWT = 10, 2.21 failures expected
- MTBF [applies_to:: Pattern D] β = 1 only; aggregate of all modes looks like β = 1
- [[Reliability Metrics]] [related_to:: [[Maintenance Time Definitions]]] MTTR, MTTRes, MRT, MART
- [[Reliability Metrics]] [related_to:: [[Failure Rate Estimation]]] λ = n/τ, chi-square bounds
- RBMM Time to Target Reliability Formula [has_formula:: T(R) = η (1 - ln(R))^(1/β)] printed with square brackets, wrong; 13,847.81 h at R* = 0.8 (RBMM p.169 Fig 6.16) [contested:: true]
- Time to Target Reliability [has_formula:: T(R) = η (-ln R)^(1/β)] correct, derived by inverting R(t) [contested:: true]
- Time to Target Reliability [has_value:: about 8,837 h] R* = 0.8, derived by wiki [confidence:: medium]
- RBMM Time to Target Reliability Formula [contradicts:: Time to Target Reliability] R(13,848) ≈ 0.29 not 0.80 [contested:: true]
- Conditional Reliability [has_formula:: R(t2 | t1) = R(t2) / R(t1)] (RBMM p.169-170)
- Conditional Reliability [has_value:: 70.14%] t1 = 10,000 (R = 70.03%), t2 = 12,000 (R = 49.12%) (RBMM Fig 6.17)
- Additional Operating Time of Survival [has_value:: 1,369.52 h] 80% survival after 10,000 h (RBMM p.170 Fig 6.18)
- Availability [has_formula:: time available / time required] (RBMM p.176)
- Availability [depends_on:: Reliability Function] and repair time
- Availability [depends_on:: MTTR]
- Availability Example [has_value:: 99.89%] 1 - (3 x 10)/(3 x 8,760), 3 failures of 10 h in 3 years (RBMM p.176)
- Availability Example [has_value:: R(2 years) = 51.34%] constant rate e^(-2/3)
- Maintainability [has_formula:: M(t) = 1 - exp(-t/MTTR)] exponential repair time (RBMM p.176-177)
- Maintainability [has_value:: M(3) = 0.5756] MTTR = 3.5 h, t = 3 h
- Failure Tree [has_formula:: Ft = 1 - Π(1 - Fi)] Fi = 1 - Ri (RBMM p.175)
- Failure Tree [related_to:: [[Reliability Block Diagram]]] series in RBD equivalent to OR-gate
- Conditional Reliability [input_to:: PM Before Turnaround] compare with acceptable risk
- [[Reliability Metrics]] [input_to:: [[Monte Carlo Maintenance Simulation]]] CM-Unplanned 1.76 in 3 years
- [[Reliability Metrics]] [input_to:: [[PM Interval Optimization]]]
- [[Reliability Metrics]] [uses:: Confidence Bound] all values are estimates (RBMM p.165)
- [[OREDA]] [has_value:: λ per 10^6 h] MTTF = 1/λ valid only when β = 1
- [[ISO 14224]] [source_of:: MTTR] with MWT, from downtime and man-hours in maintenance records; used for [[Compressor]] unit availability
- [[Reliability Metrics]] [applies_to:: [[Failure Mode]]] per failure mode, not whole machine
- [[Reliability Metrics]] [related_to:: [[Availability and OEE]]]
- [[Reliability Metrics]] [related_to:: [[Maintainability]]] M(t), lognormal repair time, Mmax, allocation
- CMRP MTTR [applies_to:: Active Repair] seven MIL-HDBK-472 steps, excludes inactive waiting time (CMRP CMPR-04 p.39-40)
- CMRP MTTR [differs_from:: RBMM MTTR] RBMM includes labor wait (RBMM p.49-51); scope difference, not contested
- Repair Rate [has_formula:: μ = 1/MTTR] (CMRP CMPR-04 p.13, 17)
- Failure Rate [has_formula:: λ = 1/MTBF] only for exponential (CMRP CMPR-04 p.14)
- CMRP MTTF Example [has_value:: 153.8 h] 1538/10 for 10 units (CMRP CMPR-04 p.16)
- CMRP MTBF Example [has_value:: 4,000 h] n·m/r = 100 x 1000/25 (CMRP CMPR-04 p.16)

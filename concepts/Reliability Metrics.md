---
title: Reliability Metrics
created: 2026-10-20
updated: 2026-10-28
type: concept
tags: [reliability, statistics, weibull, kpi, failure-rate, book, iso-14224, cmrp, maintainability, mpm]
sources: [reliability-based-maintenance-management.md, iso-14224.md, cmrp.md, maintenance-profit-maker.md]
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

### มุมมอง MPM ต่อ MTBF และ MTTR (เพิ่ม 2026-10-28, sources: maintenance-profit-maker.md; ข้อขัดแย้ง MPM-C4)

หนังสือ [[Maintenance Profit Maker Book]] ของผู้แต่งกลุ่มเดียวกับ RBMM ใช้นิยามเชิงปฏิบัติที่ต่างจาก RBMM ข้างบน wiki เก็บทั้งสองไว้ ยังไม่เลือก

| ดัชนี | MPM บทที่ 8 (รูป 8.3, MPM p.149-151) | MPM บทที่ 4 (รูป 4.18, MPM p.76) | RBMM |
|---|---|---|---|
| MTBF | Total Up Time / จำนวนครั้งเสีย | (ชั่วโมงทั้งหมด - เวลาซ่อมรวม) / จำนวนครั้งเสีย (อนุมานจากตัวเลข, derived) | MTTF + MTTR + MWT (RBMM p.190-193) |
| MTTR | Total Repair Time / จำนวนครั้งเสีย (ซ่อมล้วน) | เวลาซ่อมรวม / จำนวนครั้งเสีย | Repair + Wait labor (RBMM p.49-51) |
| เวลารอ | แยกเป็น **Mean Logistic Time (MLT)** = Total Wait Time / จำนวนครั้งเสีย | ไม่แยก | MWT อยู่ใน MDT = MTTR + MWT |
| Failure Rate | 1 / MTBF | - | λ(t) จาก pdf |

- MTBF ของ MPM ทั้งสองบทจึงเป็น **เวลาเดินเฉลี่ย** ไม่รวมเวลาหยุด ใกล้ MTTF/MUT มากกว่า MTBF = MTTF + MTTR + MWT ของ RBMM (ผลต่างเล็กเมื่อเวลาหยุดน้อยเทียบเวลาเดิน) และ MTTR ของ MPM บทที่ 8 ใกล้ MART/MRT ของ ISO ดู [[Maintenance Time Definitions]]
- ความไม่สอดคล้องภายในเล่ม: MPM บทที่ 9 (p.166) จัด MWT เป็นเป้าการลด MTTR ขัดกับบทที่ 8 ที่แยกเวลารอเป็น MLT
- ตัวอย่างรูป 8.3: 720 ชม. เสีย 3 ครั้ง ซ่อม 70 ชม. รอ 20 ชม. ได้ MTBF 630/3 = 210 ชม., MTTR 23.33 ชม., MLT 6.67 ชม., Failure Rate 1/210 พิมพ์ 0.0047 (ปัดที่ถูก 0.0048 ครั้ง/ชม., derived); ข้อความในเล่มว่า Up Time 650 ชม. ค่าที่ใช้คำนวณและถูกต้องคือ 630 ชม. (derived) ดู [[Availability and OEE]] หัวข้อ 6.8

**วิธีของรายงาน MTBF-MTTR รูป 4.18 (MPM p.76)**: ชั่วโมงทั้งหมด 26,280 ชม. (= 3 x 8,760, derived) 18 เครื่อง เสียรวม 35 ครั้ง เวลาซ่อมรวม 783 ชม.

| เครื่อง | ครั้งที่เสีย | เวลาซ่อมรวม (ชม.) | MTBF | MTTR |
|---|---|---|---|---|
| PS01-FWP01 | 10 | 151 | 2,612.90 | 15.10 |
| PS02 โรงสูบ 2 | 3 | 41 | 8,746.33 | 13.67 |
| PS02-FWP01 | 4 | 337 | 6,485.75 | 84.25 |
| PS03 โรงสูบ 3 | 5 | 155 | พิมพ์ 5,255.00 ที่ถูก **5,225.00** (derived) | 31.00 |
| เครื่องที่เสีย 1 ครั้ง ซ่อม 3 ชม. | 1 | 3 | 26,277.00 | 3.00 |

- ตัวอย่างตรวจ: (26,280 - 151)/10 = 2,612.9 และ 151/10 = 15.1; PS03 (26,280 - 155)/5 = 5,225.00 ตัวเลข 5,255.00 ในเล่มจึงเป็น typo (ของหนังสือหรือ OCR)
- แถวที่เสีย 0 ครั้งแต่แสดง MTTR = 1.00 ไม่มีความหมาย ควรเป็น N/A (derived)
- ข้อควรระวัง: ค่าแบบนี้เป็นค่าเฉลี่ยรวมทุก failure mode ของทั้งเครื่อง ใช้ดูอันดับปัญหา (top 10/20) ได้ แต่ไม่แทนการวิเคราะห์ราย mode ด้วย [[Weibull Analysis]] (การตีความของ wiki)

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
- [[Maintenance Profit Maker Book]] (MTBF/MTTR/MLT แบบ MPM)

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
- MPM MTBF [has_formula:: Total Up Time / Number of Failures] (MPM p.149-151) [contested:: true]
- MPM Report MTBF [has_formula:: (total hours - total repair hours) / number of failures] inferred from Fig 4.18 figures (MPM p.76) [contested:: true]
- MTBF [has_formula:: MTTF + MTTR + MWT] RBMM view kept alongside MPM (RBMM p.190-193) [contested:: true]
- MPM MTBF [contradicts:: MTBF] MPM-C4; MPM MTBF is mean up time, excludes repair and wait [contested:: true]
- MPM MTTR [has_formula:: Total Repair Time / Number of Failures] repair only (MPM p.150-151) [contested:: true]
- MPM MTTR [contradicts:: RBMM MTTR] MPM-C4; RBMM MTTR = Repair + Wait labor (RBMM p.49-51) [contested:: true]
- Mean Logistic Time [has_formula:: Total Wait Time / Number of Failures] (MPM p.150-151)
- Mean Logistic Time [alias_of:: MWT] wait before and after repair, logistics support
- MPM Failure Rate [has_formula:: 1 / MTBF] (MPM p.151)
- Fig 8.3 Machine Index Example [has_value:: MTBF 210 h, MTTR 23.33 h, MLT 6.67 h] 720 h, 3 failures (MPM p.149-151)
- MPM Chapter 9 MTTR Usage [contradicts:: MPM MTTR] p.166 puts MWT under MTTR, internal inconsistency (MPM p.166)
- Fig 4.18 MTBF MTTR Report [has_value:: 26,280 h, 18 machines, 35 failures, 783 repair h] (MPM p.76)
- Fig 4.18 PS01-FWP01 [has_value:: MTBF 2,612.90 h, MTTR 15.10 h] 10 failures, 151 h repair (MPM p.76)
- Fig 4.18 PS03 MTBF Printed [has_value:: 5,255.00 h] (MPM p.76)
- Fig 4.18 PS03 MTBF [has_value:: 5,225.00 h] derived (26,280 - 155)/5
- Fig 4.18 PS03 MTBF Printed [contradicts:: Fig 4.18 PS03 MTBF] typo, derived correction
- MPM MTBF [related_to:: MUT] mean running time, close to MTTF/MUT, interpretation [confidence:: medium]
- [[Reliability Metrics]] [defined_in:: [[Maintenance Profit Maker Book]]] MPM chapter 4 and 8 practical definitions

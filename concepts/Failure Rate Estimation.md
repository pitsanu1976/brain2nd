---
title: Failure Rate Estimation
created: 2026-10-21
updated: 2026-10-22
type: concept
tags: [iso-14224, failure-rate, statistics, reliability, kpi]
sources: [iso-14224.md]
confidence: medium
contested: false
---

# Failure Rate Estimation

วิธีประมาณ failure rate จากข้อมูลสนามตาม Annex C ของ [[ISO 14224]] (informative ไม่ใช่ตำราสถิติเต็มรูป ให้ดู ISO/TR 12489 เพิ่ม, cl. C.1.1, p.205) สูตรเขียนเป็นสัญลักษณ์ของ wiki ถอดความจากมาตรฐาน ตัวอย่างตัวเลขทั้งหมดมาจากมาตรฐานเว้นแต่ระบุ derived

## 1. MLE ของ failure rate คงที่ (cl. C.3.2.1, p.215)

```
λ̂ = n / τ        n = จำนวน failure, τ = aggregated time in service
```

- τ เป็น surveillance time หรือ operating time รวมของทุก item ในกลุ่ม ใช้ได้เมื่อ item มี λ เท่ากันและ n >= 1
- การรวมเวลาของ item ที่ยังไม่เสียเข้า τ เป็นการใช้ข้อมูล right-censored ภายใต้สมมติ exponential (ตีความของ wiki มาตรฐานไม่ใช้คำว่า censored ใน Annex C) ดู [[Censored Data]]
- failure frequency เฉลี่ย w = n / ΣTTFi (C.16) ต่างความหมายจาก failure rate (hazard) แต่ estimator เหมือนกันเมื่อ hazard คงที่ และ 1/w = MTTF + MTTRes สำหรับ repairable item ที่ซ่อมแล้วเหมือนใหม่ ไม่ใช่ "expected time to failure" (cl. C.3.1.1, p.213-214)
- ถ้ามี wear-out แต่สมมติคงที่ จะประเมิน reliability ต่ำไปช่วงอายุน้อยและสูงไปช่วงอายุมาก ทางเลือกคือ Weibull กับ component หรือ power law กับ repaired system (cl. C.3.1.2, p.214-215) ดู [[Weibull Analysis]]
- MTTF = 1/λ ใช้ได้เฉพาะ λ คงที่ (C.48, p.224)

## 2. Confidence interval แบบ chi-square (cl. C.3.2.1, C.21-C.22, p.216)

```
λL = χ²(2n) / (2τ)            ที่ quantile ล่าง
λU = χ²(2(n+1)) / (2τ)        ที่ quantile บน
```

ตัวอย่างในมาตรฐาน: n = 6, τ = 10,000 ชม. ได้ λ̂ = 6 x 10^-4 ต่อชม. ช่วงประมาณ 2.6 x 10^-4 ถึง 1.18 x 10^-3 ต่อชม. (Fig C.2)

**ข้อสังเกตความไม่สอดคล้องภายในมาตรฐาน**: เนื้อความบอกช่วง 90% แต่ตัวอย่างและ Fig C.2 เขียน 95% ตรวจ derived ของ wiki: χ²(0.05; 12) = 5.226 ให้ 2.61 x 10^-4 และ χ²(0.95; 14) = 23.685 ให้ 1.18 x 10^-3 ตรงกับ quantile 5% และ 95% ซึ่งคือช่วง two-sided **90%** ไม่ใช่ 95% และสัญลักษณ์ z ใน C.21/C.22 ดูสลับกับคำอธิบาย จึงใช้ช่วงนี้ในฐานะ 90% และตรวจ quantile เองก่อนนำไปรายงาน (ไม่ตั้ง contested เพราะ wiki ไม่มีข้อความขัดแย้งอื่น เป็น erratum ภายในมาตรฐาน)

## 3. Zero failure (cl. C.3.3, p.218-219)

| วิธี | สูตร | หมายเหตุ |
|---|---|---|
| Bayesian non-informative prior | λ̂ = (2n+1) / (2t) (C.37) | n = 0 ได้ 1/(2t) (C.38) |
| Constant confidence-level estimator | λ̂ = (n + 0.7) / t (C.39) | ลู่เข้า MLE เมื่อ n มาก ใช้ได้แม้ n = 0 |

บางหน่วยงานกำกับ (เช่น nuclear) ไม่ยอมรับ Bayesian ให้ระวังว่าตัวประมาณใช้กับ failure mode เดียวหรือ total rate ช่วงที่ไม่มี failure ก็มีค่า ใช้ประมาณ failure rate ได้ (Annex B.1, p.176; cl. 8.3.2, p.33-34)

## 4. รวมข้อมูลหลายกลุ่ม: heterogeneous estimator (cl. C.3.2.2, p.216-218)

เมื่อรวมหลาย installation หรือหลาย fleet ที่ λ ไม่เท่ากัน ให้แบ่งเป็น k class ที่ถือว่า homogeneous แต่ละ class มีจำนวน failure ni และเวลา τi แล้วถือว่า λ เป็นตัวแปรสุ่มระหว่าง class (Bayesian, prior แบบ gamma)

```
pooled m = Σn / Στ
ประมาณ α̂, β̂ ของ gamma จากความแปรปรวนระหว่าง class (เลือกค่ามากกว่าของสองตัวประมาณ)
λ̂i = (α̂ + ni) / (β̂ + τi)          (C.36)
```

- ผลคือค่าประจำ class ที่ถูกดึงเข้าหาค่าเฉลี่ยรวม class ที่มีข้อมูลน้อยจะถูกดึงมาก พร้อม credibility interval จาก quantile ของ gamma
- แนวคิดเดียวกับ multi-sample ของ [[OREDA]] ที่รายงาน mean และ SD (ข้อเชื่อมนี้เป็นความรู้ทั่วไป ไม่ได้ระบุใน sources, confidence: low) ดู [[Compressor]] ที่ใช้ตัวเลข OREDA เป็นฐาน
- ขั้นตอนเต็ม (S1, S2, น้ำหนัก) ดูต้นฉบับ ไม่คัดลอกมาที่นี่

## 5. นับเป็นรอบหรือ demand แทนเวลา (cl. C.3.4, p.219-220)

- ถ้ารอบใช้งานเป็นตัวขับ ให้แทน t ด้วยจำนวน cycle/demand ในสูตรเดิม แปลงกลับเป็นเวลาที่ระดับระบบด้วย **MTTF = MCTF / ξ** (C.40) เมื่อ ξ = cycle ต่อหน่วยเวลา
- class เดียวอาจใช้ time model กับ mechanism หนึ่ง (corrosion) และ cycle model กับอีก mechanism (wear)
- ตัวอย่าง valve fail to open: **due to demand** = เสียเพราะการเรียกใช้ (wear จากเปิดบ่อย) กับ **on demand** = เสียอยู่ก่อนแล้วเพิ่งถูกเปิดเผยเมื่อเรียก (เช่น corrode ในตำแหน่งปิด) failure mode และ detection method เหมือนกัน ต่างที่ mechanism (ISO 14224 cl. 3.26, 3.31, p.6-7; C.3.4)
- ต้องบันทึกจำนวน demand ทั้ง test activation ใน PM และ activation จริง (cl. C.1.3, p.205-206)

### นิยาม demand ตามประเภทอุปกรณ์ (cl. C.1.3, p.205-206)

| ประเภท | 1 demand คือ |
|---|---|
| rotating, conveyor, heater | การ start-up (หยุดหรือปรับ speed ของ VSD ไม่นับ) |
| crane, loading arm, winch | การทำงานแต่ละครั้ง |
| valve | เปิดหรือปิดแต่ละครั้ง (control/choke valve นับทุกการปรับ) |
| safety หรือ standby | ทุก activation ทั้ง test และ trip จริง |
| piping, heat exchanger, riser, filter, cable | ไม่มีความหมายของ demand |

## 6. Common cause failure (cl. C.1.6-C.1.7, p.207)

- เมื่อวิเคราะห์ CCF โดยละเอียดไม่ได้ ใช้ **β-factor**: λ = (1 - β)·λ ส่วนอิสระ + β·λ ส่วน CCF
- ละเลย dependency ทำให้ผลต่ำเกินจริง (ไม่ conservative) ซึ่งรับไม่ได้ในงาน safety (cl. C.1.4-C.1.5, p.206-207)
- common mode failure (CMF) คือหลายชิ้นเสียด้วย mode เดียวกันซึ่งอาจมาจาก CCF หรือไม่ก็ได้ ต่างจาก CCF

## 7. Test interval ของอุปกรณ์ safety ที่เสียซ่อน (cl. C.6, p.225-227)

```
Required availability:  τ  = 2 · LPFD / λ                    (C.51)
Cost-benefit:           τ* = sqrt( 2·Cm / (Cf · λfto · f) )   (C.55)
```

- LPFD = PFD เฉลี่ยที่ยอมรับ ใช้เมื่อ test ไม่ก่อความเสียหายและ MRT ไม่มีนัย; Cm = ต้นทุนต่อ test, Cf = ส่วนต่างความเสียหายเมื่อระบบทำงานกับไม่ทำงาน, f = ความถี่เหตุที่ต้องเรียกระบบ, λfto = failure rate แบบ fail to operate
- ควรเก็บทั้ง failure ก่อน test (hidden จริง) และ failure ที่เกิดเพราะ test (C.6.1, p.225) ความสัมพันธ์ของ C.51 กับสูตร FFI ของ RBMM ดู [[Failure Finding Interval]]
- มาตรฐานคำนวณ PFD เป็นสัดส่วนเวลาเฉลี่ยที่อยู่ในสถานะเสีย (cl. C.1.3, p.206) การจัดกลุ่ม DU/DD ของ failure ที่เกี่ยวข้อง ดู [[Safety Critical Failure Classification]]

## เชื่อมโยงกับ compressor failure hierarchy

- ตัวเลข [[OREDA]] เป็นผลของ estimator ลักษณะนี้ (ต่อ 10^6 ชม.) ข้อมูล failure ของ site ที่เก็บตาม [[ISO 14224 Taxonomy]] ใช้คำนวณ λ̂ = n/τ ได้ต่อ failure mode ของ [[Maintainable Item]] โดยต้องมี surveillance time และจำนวน demand ที่ถูกต้อง
- ข้อมูลผู้ผลิตมัก failure rate ต่ำเกินจริง และ event ใน CMMS ไม่ใช่ reliability data โดยตรง (Annex D.5, p.235-237) ดู [[RM Data Quality]]
- โหมด start แบบ on demand (FTS) น่าจะนับด้วยจำนวน start ไม่ใช่ชั่วโมง เพราะ demand ของ rotating equipment คือ start-up (ข้อเสนอของ wiki ตีความจาก C.1.3)

## ดูเพิ่ม

- [[Reliability Metrics]]
- [[Maintenance Time Definitions]]
- [[Weibull Analysis]]
- [[Failure Mode]]

## Triplets

- [[Failure Rate Estimation]] [defined_in:: [[ISO 14224]]] Annex C, informative; see ISO/TR 12489 (cl. C.1.1, p.205)
- [[Failure Rate Estimation]] [produces:: Failure Rate]
- Constant Failure Rate MLE [has_formula:: λ̂ = n / τ] n = number of failures, τ = aggregated time in service (ISO 14224 cl. C.3.2.1, p.215)
- Constant Failure Rate MLE [applies_to:: Items With Equal λ] n >= 1
- Constant Failure Rate MLE [uses:: [[Censored Data]]] time of unfailed items in τ = right-censored data under exponential (wiki interpretation)
- Failure Frequency [has_formula:: w = n / ΣTTFi] (ISO 14224 C.16)
- Failure Frequency [differs_from:: Failure Rate] different meaning, same estimator when hazard constant (cl. C.3.1.1)
- Failure Frequency [has_formula:: 1/w = MTTF + MTTRes] repairable item restored as good as new
- Constant Failure Rate [differs_from:: Wear-out] underestimates reliability at young age, overestimates at old age (cl. C.3.1.2, p.214-215)
- [[Weibull Analysis]] [applies_to:: Component] wear-out alternative (ISO 14224 cl. C.3.1.2)
- Power Law [applies_to:: Repaired System] wear-out alternative (ISO 14224 cl. C.3.1.2)
- MTTF [has_formula:: 1/λ] constant λ only (ISO 14224 C.48, p.224)
- Chi-square Confidence Interval [has_formula:: λL = χ²(2n) / (2τ)] lower quantile (ISO 14224 C.21, p.216)
- Chi-square Confidence Interval [has_formula:: λU = χ²(2(n+1)) / (2τ)] upper quantile (ISO 14224 C.22, p.216)
- ISO Chi-square Example [has_value:: λ̂ = 6 x 10^-4 per h] n = 6, τ = 10,000 h (ISO 14224 Fig C.2)
- ISO Chi-square Example [has_value:: 2.6 x 10^-4 to 1.18 x 10^-3 per h] interval
- ISO Chi-square Example 95% Label [contradicts:: ISO Chi-square Example 90% Interval] text says 90%, example and Fig C.2 say 95%; quantiles 5%/95% give two-sided 90% (wiki check)
- ISO Chi-square Example 90% Interval [contradicts:: ISO Chi-square Example 95% Label] wiki uses 90%; erratum inside standard
- Zero Failure Bayesian Estimator [has_formula:: λ̂ = (2n+1) / (2t)] non-informative prior (ISO 14224 C.37)
- Zero Failure Bayesian Estimator [has_formula:: 1/(2t)] n = 0 (ISO 14224 C.38)
- Constant Confidence-level Estimator [has_formula:: λ̂ = (n + 0.7) / t] works for n = 0, converges to MLE (ISO 14224 C.39)
- Failure-free Period [input_to:: [[Failure Rate Estimation]]] (ISO 14224 Annex B.1, cl. 8.3.2)
- Heterogeneous Estimator [has_formula:: pooled m = Σn / Στ] (ISO 14224 cl. C.3.2.2, p.216-218)
- Heterogeneous Estimator [has_formula:: λ̂i = (α̂ + ni) / (β̂ + τi)] (ISO 14224 C.36)
- Heterogeneous Estimator [uses:: Gamma Prior] Bayesian, λ random between k classes
- Heterogeneous Estimator [applies_to:: Multiple Installations Or Fleets]
- Heterogeneous Estimator [related_to:: [[OREDA]]] multi-sample mean and SD [confidence:: low]
- MTTF [has_formula:: MCTF / ξ] ξ = cycles per unit time (ISO 14224 C.40)
- Cycle Model [applies_to:: WEAR] time model for corrosion in same class (ISO 14224 cl. C.3.4)
- Failure Due To Demand [differs_from:: Failure On Demand] same mode and detection, different mechanism; valve fail to open (ISO 14224 cl. 3.26, 3.31)
- Demand Count [input_to:: [[Failure Rate Estimation]]] include PM test activations and real activations (ISO 14224 cl. C.1.3)
- Rotating Equipment Demand [has_value:: start-up] VSD stop or speed change not counted (ISO 14224 cl. C.1.3)
- Valve Demand [has_value:: each open or close] control/choke valve every adjustment
- Safety Or Standby Demand [has_value:: every activation] test and real trip
- Beta-factor Model [has_formula:: λ = (1 - β)·λ independent + β·λ CCF] (ISO 14224 cl. C.1.6-C.1.7, p.207)
- Beta-factor Model [applies_to:: Common Cause Failure]
- Common Mode Failure [differs_from:: Common Cause Failure] same mode on several items, may or may not be CCF
- Safety Test Interval [has_formula:: τ = 2 · LPFD / λ] required availability (ISO 14224 C.51)
- Safety Test Interval [has_formula:: τ* = sqrt( 2·Cm / (Cf · λfto · f) )] cost-benefit (ISO 14224 C.55)
- Safety Test Interval [related_to:: [[Failure Finding Interval]]] C.51 vs RBMM FFI
- PFD [is_a:: Mean Fractional Downtime] (ISO 14224 cl. C.1.3, p.206)
- PFD [related_to:: [[Safety Critical Failure Classification]]] DU/DD
- [[OREDA]] [produces:: Failure Rate] per 10^6 h, from estimators of this type
- Constant Failure Rate MLE [applies_to:: [[Maintainable Item]]] per failure mode, needs surveillance time and demand count
- Manufacturer Data [has_value:: Failure Rate Too Low] CMMS events also not reliability data directly (ISO 14224 Annex D.5); see [[RM Data Quality]]
- FTS [depends_on:: Demand Count] count starts not hours (wiki proposal) [confidence:: low]
- [[Failure Rate Estimation]] [related_to:: [[Reliability Metrics]]]

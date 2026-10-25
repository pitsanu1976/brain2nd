---
title: Statistical Process Control
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [spc, statistics, reliability, cmrp]
sources: [cmrp.md]
confidence: medium
contested: false
---

# Statistical Process Control

Statistical Process Control (SPC) คือการใช้ control chart แยก variation ปกติของกระบวนการ (common/chance cause) ออกจาก variation ที่มีสาเหตุเฉพาะ (special/assignable cause) เพื่อให้รู้ตัวเร็วเมื่อกระบวนการเปลี่ยน หน้านี้สรุปจากสไลด์ CMRP: X-bar/R chart, attribute charts (p, np, c, u), run/zone rules, process capability (Cp, Cpk) และ confidence interval ของค่าเฉลี่ย พร้อมตัวเลขตัวอย่างที่ตรวจซ้ำแล้วและจุดที่สไลด์คำนวณผิด ทั้งหมดเป็นเนื้อหาจาก [[CMRP Course]] ซึ่งเป็นสื่อการสอน (secondary source)

เหตุที่ reliability engineer สนใจ SPC: reliability ของ product ขึ้นกับกระบวนการที่ผลิต จึงควรคุม characteristic ที่กระทบอายุใช้งานด้วย SPC (CMRP CMPR-06 p.47) control chart เริ่มจาก Shewhart (1931) (CMRP CMPR-06 p.48)

## หลักการ control chart (CMRP CMPR-06 p.45-47)

- center line = ค่าเฉลี่ย, control limit ที่ μ ± 3σ ของสถิติที่ plot (ตัด LCL ทิ้งได้ถ้าค่าติดลบหรือไม่มีความหมาย)
- จุดนอก limit หรือ pattern ผิดปกติ = special cause ต้องหาสาเหตุ
- **control limit ไม่ใช่ specification limit**: control limit มาจากข้อมูลของกระบวนการ (ครอบคลุม ~99.73%) ส่วน spec มาจากลูกค้า/การออกแบบ (CMRP CMPR-07 p.1)
- Central Limit Theorem รองรับการใช้ ±3σ กับค่าเฉลี่ยของ subgroup แม้ข้อมูลเดี่ยวไม่ normal และค่าเฉลี่ยไวต่อการ shift มากกว่าค่าเดี่ยว; สไลด์ระบุว่า n < 5 เหมาะเมื่อประชากร normal เท่านั้น (CMRP CMPR-06 p.7) ดู [[Statistical Distributions for Maintenance]]
- ประเภท chart: variables (X-bar/R, X-bar/s, I-MR, MX-MR, median, run chart) และ attribute (p, np, c, u) (CMRP CMPR-06 p.46)

## X-bar / R chart (CMRP CMPR-07 p.1-2)

### ศัพท์

| สัญลักษณ์ | ความหมาย |
|---|---|
| n | ขนาด subgroup |
| X | ค่าวัดแต่ละค่า |
| X-bar | ค่าเฉลี่ยของ subgroup |
| X-double-bar | ค่าเฉลี่ยของ X-bar ทุก subgroup = center line ของ X-bar chart |
| R | range ใน subgroup (max - min) |
| R-bar | ค่าเฉลี่ยของ R = center line ของ R chart |
| UCL / LCL | upper / lower control limit |

### 8 ขั้นตอนสร้าง

1. เลือกขนาด subgroup n (3, 4 หรือ 5) และความถี่การสุ่ม
2. เก็บ 20-25 subgroup เรียงตามเวลา (ราว 60-100 ค่า)
3. คำนวณ X-bar ของแต่ละ subgroup
4. คำนวณ R ของแต่ละ subgroup
5. หา X-double-bar = center line ของ X-bar chart
6. หา R-bar = center line ของ R chart
7. คำนวณ control limits
8. Plot และตีความหา special cause

```
X-bar chart:  UCL = X-double-bar + A2·R-bar     LCL = X-double-bar - A2·R-bar
R chart:      UCL = D4·R-bar                    LCL = D3·R-bar
A2 = 3 / (d2·sqrt(n))      σ-hat = R-bar / d2
```

| n | A2 | D3 | D4 | d2 |
|---|---|---|---|---|
| 2 | 1.88 | 0 | 3.27 | 1.13 |
| 3 | 1.02 | 0 | 2.57 | 1.69 |
| 4 | 0.73 | 0 | 2.28 | 2.06 |
| 5 | 0.58 | 0 | 2.11 | 2.33 |
| 6 | 0.48 | 0 | 2.00 | 2.53 |

ข้อควรอ่านให้ถูก: สไลด์เขียนว่า A2·R-bar คือ "3s" แต่ความหมายจริงคือ 3σ-hat/sqrt(n) = 3 เท่าของ standard error ของค่าเฉลี่ย ไม่ใช่ 3σ ของค่าเดี่ยว (ตรวจ n = 5: 3/(2.326 x 2.236) = 0.577 ≈ 0.58) ข้อสังเกต: ขั้นตอนแนะนำ n = 3-5 ขณะที่ CLT slide บอก n < 5 ต้องการ normality ถ้าไม่แน่ใจให้ใช้ n = 5

### ตัวอย่าง closure removal torque (CMRP CMPR-07 p.2)

21 subgroup, n = 5, spec 10-22 in-lb: ΣX-bar = 323.6, ΣR = 75 → X-double-bar = 15.41 ≈ 15.4, R-bar = 3.571 ≈ 3.57 (ตรวจซ้ำจากค่าวัดดิบแล้วตรง)

| Limit | สไลด์ | ตรวจ |
|---|---|---|
| UCL X-bar = 15.4 + 0.58 x 3.6 | 17.5 | 17.49 ถูก |
| LCL X-bar = 15.4 - 2.1 | 13.3 | 13.31 ถูก |
| UCL R = 2.11 x 3.6 | 7.5 | **7.6** |
| LCL R = 0 x 3.6 | 0 | ถูก |

**flag สไลด์:** การแทนค่า UCL R เขียน 2.11 x 3.6 = 7.5 แต่ผลคูณคือ 7.60 (ถ้าใช้ R-bar ไม่ปัด 3.571 ได้ 7.54) และกราฟในสไลด์เดียวกันเขียน 7.6 จึงไม่สอดคล้องกันเอง ใช้ 7.6 เมื่อแทนด้วย R-bar = 3.6; การตีความไม่เปลี่ยน

### สัญญาณ out of control และการคำนวณใหม่หลัง start-up

- X-bar ต่ำกว่า LCL 13.3 ที่ subgroup 1 (12.8), 4 (10.8), 6 (13.2) = special cause (derived จากตาราง)
- R ของ subgroup 9 = 8 เกิน UCL R = special cause
- subgroup 10-18 อยู่เหนือ center line ติดกัน 9 จุด = run (process shift)
- ข้อสรุปของสไลด์: เป็น start-up process ที่เริ่มนิ่งตั้งแต่ subgroup 10 ถ้าจะใช้ต่อ ต้องคำนวณ control limit ใหม่จากช่วงที่นิ่ง (ตัดช่วง special cause ออก)
- ตัวอย่างคำนวณใหม่ (derived, ไม่อยู่ในสไลด์): ใช้ subgroup 10-21 ได้ X-double-bar ≈ 16.15, R-bar ≈ 3.42 → UCL X-bar ≈ 18.1, LCL X-bar ≈ 14.2, UCL R ≈ 7.2 [confidence: low]
- control limit (13.3-17.5) แคบกว่า spec (10-22) มาก: กระบวนการ "อยู่ใน spec" แต่ "out of control" ได้

## Attribute charts (CMRP CMPR-08 p.1-2)

ข้อมูลนับแบบไม่ต่อเนื่อง (ผ่าน/ไม่ผ่าน) plot กราฟเดียว

| Chart | สิ่งที่บันทึก | Subgroup size | Distribution |
|---|---|---|---|
| p | สัดส่วนของเสีย | แปรผันได้ | Binomial |
| 100p | % ของเสีย | แปรผันได้ | Binomial |
| np | จำนวนชิ้นเสีย | คงที่ | Binomial |
| c | จำนวน defect | คงที่ | Poisson |
| u | defect ต่อหน่วย | แปรผันได้ | Poisson |

```
p chart:  p-bar = Σnp / Σn,  n-bar = Σn / k
          UCL/LCL = p-bar ± 3·sqrt( p-bar(1 - p-bar) / n-bar )
np chart: UCL/LCL = n·p-bar ± 3·sqrt( n·p-bar(1 - p-bar) )
c chart:  c-bar = Σc / k;   UCL/LCL = c-bar ± 3·sqrt(c-bar)
u chart:  u-bar = Σc / Σn;  UCL/LCL = u-bar ± 3·sqrt(u-bar / n-bar)
k = จำนวน subgroup; LCL ติดลบให้ใช้ 0
```

เงื่อนไขใช้งานตามสไลด์: p chart ปกติ subgroup > 50; ค่าเฉลี่ยของเสียต่อ subgroup ควร ≥ 4-5; ถ้าขนาด subgroup ต่างจาก n-bar เกิน ±20% ให้ตัดจุดนั้นหรือคำนวณ limit เฉพาะจุดนั้น p chart ไวที่สุดในกลุ่ม attribute ส่วน X-bar/R ไวที่สุดโดยรวมแต่แพงที่สุด

### ตัวอย่าง p chart (CMRP CMPR-08 p.2)

20 lots, Σn = 22,500, Σnp = 52 → n-bar = 1,125, p-bar = 0.231%, σ ≈ 0.143% → UCL ≈ 0.66%, LCL = -0.20% → 0 (ตรวจแล้วถูก)

**flag (สไลด์ไม่ได้ชี้):**
- กราฟแสดง lot 3 (0.89%) และ lot 13 (0.95%) เหนือ UCL 0.66% คือ out of control ตาม rule 1 แต่สไลด์ไม่ได้อภิปราย
- lot 10 มี n = 600 ต่างจาก n-bar ราว -47% เกินเกณฑ์ ±20% ที่สไลด์ตั้งเอง แต่ตัวอย่างยังใช้ limit ร่วม

## Run / zone rules (CMRP CMPR-08 p.3-8)

แบ่งช่วง 3σ แต่ละข้างเป็น zone C (0-1σ), B (1-2σ), A (2-3σ)

| ชุดกฎ | เกณฑ์ |
|---|---|
| 5 กฎทั่วไป (p.3) | 1 จุดเกิน limit; 4 ใน 5 จุดใน zone B หรือไกลกว่า ข้างเดียว; 2 ใน 3 จุดใน zone A ข้างเดียว; ≥ 8 จุดติดกันข้างเดียว; trend ≥ 6 จุดขึ้น/ลงต่อเนื่อง (บางตำราใช้ 7) |
| รูปแบบเพิ่ม (p.3) | stratification ≥ 15 จุดใน zone C; mixture (สลับไกลทั้งสองข้าง) |
| Minitab 8 กฎ (p.8) | 1 จุด > 3σ; 9 จุดข้างเดียว; 6 จุดขึ้น/ลง; 14 จุดสลับขึ้นลง; 2 ใน 3 > 2σ; 4 ใน 5 > 1σ; 15 จุดใน ±1σ; 8 จุดนอก ±1σ สองข้าง |

ข้อสังเกต: เกณฑ์ run ในแหล่งเดียวกันไม่ตรงกัน (8 จุดในชุด 5 กฎ, 9 จุดใน Minitab, 7 จุดใน CMPR-06 p.46) เป็นความต่างของ convention ไม่ใช่ข้อผิด ให้เลือกชุดเดียวแล้วใช้คงที่

Pattern → สาเหตุ → action ตัวอย่าง (p.4-7): trend (เครื่อง/tool สึก) → ซ่อม/เปลี่ยน tool; jump in level (วัตถุดิบ คน เครื่องใหม่) → คุมวัตถุดิบ calibrate; recurring cycle (อุณหภูมิ, rotation, **scheduled maintenance**) → ประเมินงานบำรุงรักษา; จุดชิด limit (over-control) → เลิกปรับเครื่องเกินเหตุ; lack of variability (limit ผิด, ไม่ได้วัดจริง) → ตรวจ limit และ subgrouping

## Process capability (CMRP CMPR-08 p.8-13)

ต้องมีกระบวนการที่ stable ก่อน แล้วเทียบ spread ของ **ค่าเดี่ยว** กับ spec (ไม่ใช่ control limit ของ X-bar ซึ่งแคบกว่า)

```
σ_R = R-bar / d2
Cp  = (USL - LSL) / 6σ_R        > 1.33 capable; 1.00-1.33 ต้องคุมแน่น; < 1.00 incapable
CR  = 6σ_R / (USL - LSL)        < 0.75 capable; 0.75-1.00 คุมแน่น; > 1.00 incapable
Cpk = min( (USL - X-bar)/3σ_R , (X-bar - LSL)/3σ_R )
```

| Cp | Z (ต่อข้าง) | ppm นอก spec (สองข้าง, centered) |
|---|---|---|
| 0.33 | 1 | 317,311 |
| 0.67 | 2 | 45,500 |
| 1.00 | 3 | 2,700 |
| 1.33 | 4 | 63 |
| 1.50 | 4.5 | 6.8 |
| 1.67 | 5 | 0.57 |
| 2.00 | 6 | 0.002 |

(CMRP CMPR-08 p.12; ตรวจกับตาราง normal แล้วถูก) สไลด์ชี้ว่างานที่ต้องการ reliability สูงต้องการ Cp 1.5-2.0 ตารางนี้ไม่ใส่ 1.5σ shift แบบ Six Sigma (3.4 ppm ที่ 6σ เป็นความรู้ทั่วไป ไม่อยู่ในสไลด์)

ตัวอย่าง: X-bar = 12, σ_R = 2, spec 4-16 → Cp = 1.0 แต่ Cpk = min(0.667, 1.33) = 0.667 เพราะไม่ center (p.13) และตัวอย่าง n = 3, R-bar = 4.0 → σ = 2.363, Z_upper 1.28 (10.0%), Z_lower 0.83 (20.3%) รวม 30.3% นอก spec; histogram 60 ค่าได้ 16/60 = 26.7% (สไลด์พิมพ์ 26.6%) (p.13)

## Confidence interval ของค่าเฉลี่ย (CMRP CMPR-08 p.14)

```
σ ไม่รู้:  X-bar ± t(α/2, n-1) · s/sqrt(n)     s = sample SD (หาร n-1)
σ รู้:     X-bar ± Z(α/2) · σ/sqrt(n)
```

ตัวอย่าง tensile 4 ค่า 28.7, 27.9, 29.2, 26.5 → X-bar = 28.08, 95% t (df 3) = 3.182

| กรณี | s ที่ใช้ | ช่วง 95% |
|---|---|---|
| สไลด์ | 1.02 (หารด้วย n) | 26.46-29.70 |
| ถูกต้อง (derived) | 1.18 (หารด้วย n-1) | **≈ 26.20-29.95** |
| σ = 2 รู้ค่า (สไลด์) | Z = 1.96 | 26.12-30.04 (ถูก) |

**flag สไลด์:** S = 1.02 คือ SD แบบ population (หาร n) แต่ t-interval ต้องใช้ sample SD (หาร n-1) ช่วงของสไลด์จึงแคบเกินจริง ประเด็นเดียวกับ flag เรื่อง N vs N-1 ของ RBMM ใน [[Statistical Distributions for Maintenance]] (ต่างทิศ: RBMM อธิบายกฎสลับ, สไลด์ใช้ตัวหารผิดในตัวอย่าง) ช่วงความเชื่อมั่นของ failure rate (chi-square) ดู [[Failure Rate Estimation]]

## การใช้ในงานบำรุงรักษา (ตีความ)

- รูปแบบ recurring cycle ที่สไลด์โยงกับ scheduled maintenance แสดงว่างาน PM เองอาจเป็นแหล่ง variation ของกระบวนการ (CMRP CMPR-08 p.4-7)
- (ความรู้ทั่วไป ไม่อยู่ในสไลด์) control chart ใช้กับค่า condition monitoring ได้ เช่น trend ของ vibration หรือ oil analysis เพื่อแยกการเปลี่ยนจริงจาก noise ดู [[P-F Interval and Condition Monitoring]] และ [[Condition Monitoring Techniques]]
- หลัก "แยก special cause ก่อนแล้วคำนวณ limit ใหม่" สอดคล้องกับหลักแยกข้อมูลต่างกลุ่มก่อนวิเคราะห์ เช่น ไม่รวมหลาย failure mode ใน [[Weibull Analysis]] (การเปรียบเทียบเชิงแนวคิด)

## ดูเพิ่ม

- [[Statistical Distributions for Maintenance]]
- [[CMRP Course]]
- [[Failure Rate Estimation]]
- [[Weibull Analysis]]

## Triplets

- [[Statistical Process Control]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-06 p.45-48, CMPR-07, CMPR-08 p.1-14)
- [[Statistical Process Control]] [uses:: Control Chart]
- Control Chart [has_value:: μ ± 3σ] control limits of the plotted statistic (CMRP CMPR-06 p.45)
- Special Cause [detected_by:: Control Chart] point outside limits or abnormal pattern
- Control Limit [differs_from:: Specification Limit] control limit from process data, about 99.73%; spec from customer or design (CMRP CMPR-07 p.1)
- Control Chart [depends_on:: Central Limit Theorem] subgroup means near normal (CMRP CMPR-06 p.7)
- Control Chart [has_category:: variables or attribute] X-bar/R, X-bar/s, I-MR, MX-MR, median, run; p, np, c, u (CMRP CMPR-06 p.46)
- Shewhart [source_of:: Control Chart] 1931 (CMRP CMPR-06 p.48)
- X-bar R Chart [is_a:: Control Chart] variables chart (CMRP CMPR-07 p.1)
- Choose Subgroup Size [step_of:: X-bar R Chart] step 1, n = 3, 4 or 5
- Collect 20-25 Subgroups [step_of:: X-bar R Chart] step 2, about 60-100 values
- Compute Control Limits [step_of:: X-bar R Chart] step 7
- Plot And Interpret [step_of:: X-bar R Chart] step 8, find special cause
- X-bar Chart UCL [has_formula:: X-double-bar + A2·R-bar] LCL = X-double-bar - A2·R-bar (CMRP CMPR-07 p.1)
- R Chart UCL [has_formula:: D4·R-bar] LCL = D3·R-bar (CMRP CMPR-07 p.1)
- A2 [has_formula:: 3 / (d2·sqrt(n))] A2·R-bar = 3 standard errors of the mean, not 3σ of individuals
- A2 [has_value:: 0.58] n = 5; D3 = 0, D4 = 2.11, d2 = 2.33 (CMRP CMPR-07 p.1)
- Torque Example [has_value:: X-double-bar 15.4, R-bar 3.57] 21 subgroups, n = 5, spec 10-22 in-lb (CMRP CMPR-07 p.2)
- Torque Example [has_value:: UCL X-bar 17.5, LCL X-bar 13.3] verified (CMRP CMPR-07 p.2)
- Torque Example [has_value:: UCL R 7.6] 2.11 x 3.6; slide arithmetic writes 7.5, its chart shows 7.6 (CMRP CMPR-07 p.2)
- Torque Example Slide UCL R 7.5 [contradicts:: Torque Example] slide arithmetic error, correct product 7.60
- Torque Example [has_value:: subgroups 1, 4, 6 below LCL; R of subgroup 9 above UCL; run 10-18] start-up process, recalculate limits from stable period
- P Chart [is_a:: Control Chart] attribute, fraction defective, variable n, Binomial (CMRP CMPR-08 p.1)
- NP Chart [is_a:: Control Chart] number defective, constant n, Binomial
- C Chart [is_a:: Control Chart] number of defects, constant n, Poisson
- U Chart [is_a:: Control Chart] defects per unit, variable n, Poisson
- P Chart [has_formula:: p-bar ± 3·sqrt( p-bar(1 - p-bar) / n-bar )] (CMRP CMPR-08 p.1)
- C Chart [has_formula:: c-bar ± 3·sqrt(c-bar)] (CMRP CMPR-08 p.1)
- U Chart [has_formula:: u-bar ± 3·sqrt(u-bar / n-bar)] (CMRP CMPR-08 p.1)
- P Chart [depends_on:: Subgroup Size Rule] n deviating more than ±20% from n-bar needs own limit (CMRP CMPR-08 p.1)
- P Chart Example [has_value:: p-bar 0.231%, UCL 0.66%, LCL 0] 20 lots, Σn 22,500, Σnp 52 (CMRP CMPR-08 p.2)
- P Chart Example [has_value:: lots 3 and 13 above UCL] 0.89% and 0.95%, not discussed by slide
- P Chart Example [contradicts:: Subgroup Size Rule] lot 10 n = 600 is -47% from n-bar but shared limit used
- Run Rule [has_value:: 8 points one side] 5-rule set (CMRP CMPR-08 p.3); Minitab 9 points (p.8); CMPR-06 p.46 says 7
- Minitab Rules [has_value:: 8 rules] (CMRP CMPR-08 p.8)
- Recurring Cycle Pattern [has_cause:: Scheduled Maintenance] also temperature, rotation (CMRP CMPR-08 p.4-7)
- Process Capability [depends_on:: Stable Process] compare spread of individuals with spec (CMRP CMPR-08 p.8-10)
- Cp [has_formula:: (USL - LSL) / 6σ_R] σ_R = R-bar / d2 (CMRP CMPR-08 p.12)
- Cpk [has_formula:: min( (USL - X-bar)/3σ_R , (X-bar - LSL)/3σ_R )] (CMRP CMPR-08 p.12)
- CR [has_formula:: 6σ_R / (USL - LSL)] (CMRP CMPR-08 p.12)
- Cp [has_value:: > 1.33 capable; 1.00-1.33 tight control; < 1.00 incapable] (CMRP CMPR-08 p.12)
- Cp [has_value:: 1.00 = 2,700 ppm; 1.33 = 63 ppm; 2.00 = 0.002 ppm] centered, two-sided, no 1.5σ shift (CMRP CMPR-08 p.12)
- Capability Example 4.46 [has_value:: Cp 1.0, Cpk 0.667] not centered (CMRP CMPR-08 p.13)
- Confidence Interval Of Mean [has_formula:: X-bar ± t(α/2, n-1) · s/sqrt(n)] s = sample SD with n-1
- Tensile CI Example [has_value:: 26.20-29.95] correct 95% t interval, s = 1.18, derived
- Tensile CI Slide 26.46-29.70 [contradicts:: Tensile CI Example] slide used SD divided by n (1.02) (CMRP CMPR-08 p.14)
- [[Statistical Process Control]] [related_to:: [[Statistical Distributions for Maintenance]]] Binomial for p/np, Poisson for c/u, Normal for capability
- [[Statistical Process Control]] [related_to:: [[Failure Rate Estimation]]] CI of mean vs chi-square CI of λ
- [[Statistical Process Control]] [applies_to:: [[P-F Interval and Condition Monitoring]]] trending CM data, general knowledge [confidence:: low]

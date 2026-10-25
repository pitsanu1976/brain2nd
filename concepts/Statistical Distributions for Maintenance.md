---
title: Statistical Distributions for Maintenance
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [statistics, reliability, weibull, spare-parts, book, spc, cmrp]
sources: [reliability-based-maintenance-management.md, cmrp.md]
confidence: medium
contested: false
---

# Statistical Distributions for Maintenance

สรุปสถิติพื้นฐานจาก RBMM ch12 (p.361-392): ขั้นตอนวิธีการทางสถิติ ค่ากลาง pdf/cdf และการเลือก distribution สำหรับงาน maintenance ได้แก่ Poisson (ปริมาณอะไหล่), Normal (wear-out), Exponential (การเสียแบบสุ่ม) และ Weibull (ยืดหยุ่นที่สุด) พร้อมตัวอย่างตัวเลขและจุดที่หนังสือพิมพ์ไม่ตรงทฤษฎี (σ ใช้ N หรือ N-1)

## ขั้นตอนวิธีการทางสถิติ (RBMM p.362)

Data Collection → Data Presentation (ตาราง กราฟ สมการ) → Data Analysis → Interpretation สถิติให้ค่าประมาณพร้อมระดับความเชื่อมั่น (ตัวอย่างมาก ความเชื่อมั่นสูง) เป้าหมายงานซ่อมบำรุงเช่น เพิ่ม availability ลดต้นทุน ยืดอายุเครื่อง

ตัวอย่างประกอบ: ผู้เข้าประชุม 20 ปี (243, 143, ..., 315 คน) แบ่งช่วงละ 50 ได้ความน่าจะเป็นสะสม 5/25/30/45/70/95/100% ที่ขอบ 100/150/200/250/300/350/400 เตรียม 100 ที่พอเพียง 5% ของครั้ง 300 ที่ 70% (RBMM p.362-365) ค่ากลาง Mean = 241.3, Median = 252.5, Mode ≈ ช่วง 251-350 (RBMM p.365-367)

## แนวคิดหลัก (RBMM p.367-371)

- **pdf f(t)**: พื้นที่ใต้กราฟระหว่าง a ถึง b = โอกาสเสียในช่วงนั้น พื้นที่รวม = 1
- **cdf F(t)** = ∫0..t f(s) ds, R(t) = 1 - F(t), hazard λ(t) = f(t)/R(t) ดู [[Reliability Metrics]]
- **Discrete** (Poisson, Binomial, Geometric, Hypergeometric) ใช้กับจำนวนเต็ม เช่น การเบิกอะไหล่ ระดับสำรอง
- **Continuous** (Normal, Exponential, Weibull, Log Normal) ใช้กับเวลาเสียและช่วง PM
- เกณฑ์เลือก: (1) ลักษณะการวิเคราะห์ (2) สมมติฐานตรงกับงานหรือไม่ (3) ข้อมูลเหมาะกับสมการหรือไม่ (ตรวจหลังหา parameter)

Binomial, Lognormal, Geometric, Hypergeometric ถูกเอ่ยชื่อแต่ไม่มีสูตรในบทนี้ (หนังสือไม่ได้ครอบคลุม) และไม่มี mean/variance ของแต่ละ distribution

(เพิ่ม 2026-10-25) สไลด์ CMRP ให้สูตร binomial, hypergeometric, lognormal พร้อม mean/σ ดูหัวข้อ "ส่วนเสริมจาก CMRP" ด้านล่าง

## Poisson (RBMM p.371-373)

สมมติฐาน: เหตุการณ์เกิดสุ่มกระจายตลอด

```
f(x) = e^(-D) D^x / x!        D = ค่าเฉลี่ยเหตุการณ์, x = จำนวนครั้ง
D(lead time) = (อัตราใช้ต่อปี x Lead Time) / 365
```

ตัวอย่างเบิกอะไหล่ A: 3 ปี 5, 7, 4 ชิ้น/ปี → D = 5.333:

| เบิก (ชิ้น) | 0 | 3 | 5 | 8 | 11 |
|---|---|---|---|---|---|
| P (%) | 0.483 | 12.207 | 17.361 | 7.838 | 1.201 |
| P สะสม (%) | 0.483 | 22.131 | 55.768 | 90.796 | 99.120 |

เบิก 5 ชิ้นมีโอกาสสูงสุด 17.361% เบิกไม่เกิน 5 ชิ้น 55.768% ไม่เกิน 11 ชิ้น 99.12% (ตารางเต็ม x = 0-15 ใน RBMM p.372)

ปรับตาม Lead Time 45 วัน: D = 5.333 x 45/365 = 0.6575 (derived)

| เบิกใน Lead Time | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| P (%) | 51.813 | 34.069 | 11.201 | 2.455 | 0.404 |
| P สะสม (%) | 51.813 | 85.881 | 97.082 | 99.537 | 99.941 |

เก็บสำรอง 3 ชิ้น → มั่นใจ 99.537% ว่าพอใน Lead Time ระดับสำรองขึ้นกับความสำคัญของอะไหล่และความเสี่ยงที่ยอมรับ ดู [[Spare Part Demand Forecasting]] และ [[EOQ and Reorder Point]]

## Normal (RBMM p.374-376)

```
pdf = [1/(σ √(2π))] exp(-1/2 ((x-μ)/σ)^2)      parameters: μ, σ
```

เหมาะกับการเสียแบบ wear-out ที่กระจุกรอบ mean สมมาตร

**flag: σ ใช้ N หรือ N-1:** หนังสือบอกว่า N น้อยใช้ σ = √(Σ(Xi-μ)²/N) และ N มาก (>20) ใช้ N-1 ซึ่งตรงข้ามกับธรรมเนียมสถิติ (N-1 สำหรับตัวอย่างขนาดเล็ก เพื่อแก้ bias; N ใช้กับประชากรทั้งหมด) และตัวอย่างถัดไปใช้ N-1 ทั้งที่ N = 9 (หนังสือพิมพ์ผิด/อธิบายสลับ)

ตัวอย่าง: เสีย 9 ครั้ง อายุ (วัน) 315, 220, 402, 307, 163, 280, 485, 293, 190 → μ = 295, σ = 101.486 (N-1) ตรวจ derived: ถ้าใช้ N จะได้ σ ≈ 95.7 ผลโอกาสเสียในหนังสือ (ใช้ 101.486): ภายใน 120 วัน 4.23%, 180 วัน 12.86%, 365 วัน 75.48% (RBMM p.375-376)

เปรียบเทียบ PM: ทุก 120 วัน (3 ครั้ง/ปี) 1-(1-0.0423)^3 = 12.17%; ทุก 180 วัน (2 ครั้ง) 1-(1-0.1286)^2 = 24.06%; ปีละครั้ง 75.48% เป็นการประมาณแบบ shortcut ที่สมมติว่า PM คืนสภาพ as-good-as-new

## Exponential (RBMM p.376-378)

```
pdf = λ e^(-λx);   cdf = 1 - e^(-λx);   λ = 1/mean = 1/MTTF
```

เหมาะกับการเสียสุ่ม memoryless (human error, อุปกรณ์ไฟฟ้า) ตัวอย่างหลอดไฟ 150, 700, 3120, 1200, 2560 ชม.: mean 1,546, λ = 0.00064683; cdf(500) = 27.63%, cdf(1000) = 47.63%, cdf(2000) = 72.57% (pdf(2000) = 0.0177%)

เปลี่ยนหลอดทุก 1,000 ชม. (2 รอบ) หรือ 500 ชม. (4 รอบ): 1-(1-0.4763)^2 = 1-(1-0.2763)^4 = 72.57% เท่าเดิม ดังนั้นสำหรับ Exponential การเปลี่ยนตามแผนหรือ overhaul ไม่ลดโอกาสเสีย (RBMM p.377-378) ดู [[Failure Patterns and Bathtub Curve]]

## Weibull (RBMM p.378-384)

ปรับรูปได้ตาม β จึงเลียนแบบ distribution อื่นได้เกือบหมด β = 1 คือ Exponential รายละเอียด วิธี regression และตัวอย่าง TTF 8,500-16,000 ชม. ดู [[Weibull Analysis]] (Y regression β = 3.7888, η = 13,130.8; X regression β = 3.9406, η = 13,067.2) ข้อมูล suspension ดู [[Censored Data]]

## ตารางเลือก distribution

| ใช้กับ | Distribution | สมมติฐาน |
|---|---|---|
| จำนวนอะไหล่ที่เบิกต่อช่วง | Poisson | เหตุการณ์สุ่ม |
| อายุ wear-out รอบ mean | Normal | สมมาตรรอบ mean |
| การเสียสุ่ม | Exponential | failure rate คงที่ |
| ทุกรูปแบบ β | Weibull | ต้องแยกราย failure mode |

## ส่วนเสริมจาก CMRP (CMRP CMPR-06, CMPR-08)

เนื้อหาจาก [[CMRP Course]] (สื่อการสอน, secondary source) เติมส่วนที่ RBMM ไม่ครอบคลุม และ flag จุดที่สไลด์ผิด

### Dispersion, กฎ normal และ CLT (CMRP CMPR-06 p.4-7)

- sample SD หารด้วย n-1, population SD หารด้วย N (p.7) **ยืนยัน** flag เรื่อง σ ของ RBMM ด้านบนว่าธรรมเนียมที่ถูกคือ n-1 สำหรับ sample
- กฎ normal: ±1σ ≈ 68.27%, ±2σ ≈ 95.45%, ±3σ ≈ 99.73% **flag สไลด์:** รูป p.4 เขียน ±2σ = 96% และรูป p.7 เขียน 99.74% และหางระหว่าง 2σ-3σ = 2.15% (ค่ามาตรฐาน 95.45%, 99.73%, 2.14%)
- **Central Limit Theorem**: ค่าเฉลี่ยของ sample กระจายใกล้ normal แม้ประชากรไม่ normal ยิ่ง n มากยิ่งดี เป็นฐานของ ±3σ limit ใน control chart ดู [[Statistical Process Control]]
- skewness 0 = สมมาตร, > 0 เบ้ขวา, < 0 เบ้ซ้าย; excess kurtosis ของ normal = 0 (p.30)
- ตัวอย่างที่สองของปัญหา N vs n-1: confidence interval แบบ t ในสไลด์ (CMRP CMPR-08 p.14) ใช้ SD หารด้วย n (1.02) แทน n-1 (1.18) ช่วง 95% ที่ถูกคือ ≈ 26.20-29.95 ไม่ใช่ 26.46-29.70 ดู [[Statistical Process Control]]

### เกณฑ์เลือก discrete distribution (CMRP CMPR-06 p.10, อ้าง Juran)

| เงื่อนไข | ใช้ |
|---|---|
| รู้จำนวน defect ใน population, สุ่มไม่คืน, n > 10% ของ N | Hypergeometric |
| n < 10% ของ N | Binomial (ประมาณ hypergeometric) |
| ใช้ Poisson แทน binomial | Poisson ด้วย μ = np |
| np > 5 | Normal ประมาณ binomial |

### Binomial (CMRP CMPR-06 p.13-14)

```
P(X = x) = n! / ( x!(n-x)! ) · p^x · (1-p)^(n-x)
μ = np,   σ = sqrt( np(1-p) )
```

ตัวอย่าง n = 6, p = 0.25: P(0..3) = 0.18, 0.36, 0.30, 0.13; μ = 1.5, σ ≈ 1.06 (ตรวจถูก) สไลด์ได้ F(2) = 0.84 จากค่าปัด ค่าจริง ≈ 0.831 ใช้กับ p chart และ np chart ดู [[Statistical Process Control]]

### Hypergeometric (CMRP CMPR-06 p.15)

สุ่มไม่คืน ความน่าจะเป็นเปลี่ยนทุกครั้งที่หยิบ

```
P(x; N, n, m) = C(m,x) · C(N-m, n-x) / C(N,n);    μ = n·m/N
```

ตัวอย่าง N = 50, n = 5, m = 4: P(0) = 0.64696, P(1) = 0.30808, P(< 2) = 0.95504 (ผลลัพธ์ถูก)

**flag สไลด์:** บรรทัดแทนค่าพิมพ์ C(46,4) = 163,135 และ C(46,5) = 1,370,740 ค่าที่ถูกคือ **C(46,4) = 163,185** และ **C(46,5) = 1,370,754** (ผลลัพธ์สุดท้ายใช้ค่าที่ถูก) และหัวสไลด์ "Hypergeometric (Geometric)" ผิด เพราะ geometric เป็นคนละ distribution (จำนวนครั้งจนสำเร็จครั้งแรก)

### Exponential: สิ่งที่ CMRP เพิ่มและจุดผิด (CMRP CMPR-06 p.17-20)

- R(MTTF) = e^-1 ≈ 0.368 คือราว 63% เสียก่อนถึง MTTF; variance = θ² เมื่อ θ = 1/λ
- **flag สไลด์ (p.18):** อ้างว่าถ้า x เป็น exponential แล้ว 1/x เป็น Poisson ซึ่ง **ผิด** ความสัมพันธ์ที่ถูกคือ ใน Poisson process เวลาระหว่างเหตุการณ์กระจายแบบ exponential และจำนวนเหตุการณ์ต่อช่วงเวลากระจายแบบ Poisson (ไม่ใช่ส่วนกลับของตัวแปรเดียวกัน)
- **flag เชิงแนวคิด:** สไลด์ตีความ f(1000) = 0.00031 ว่าเป็น "probability of failure at 1000 h" แต่ค่า pdf เป็น density ต่อชั่วโมง ไม่ใช่ความน่าจะเป็น (ตรงกับนิยาม pdf ด้านบนที่ความน่าจะเป็นคือพื้นที่ใต้กราฟ)

### ข้อแม้: "electronics มี failure rate คงที่"

- หน้านี้ (จาก RBMM) ระบุว่า Exponential เหมาะกับอุปกรณ์ไฟฟ้า และสไลด์ CMRP p.18 ก็ว่ามักใช้กับ electronics
- แต่ case study ในไฟล์เดียวกัน (CMRP CMPR-06 p.31-36) fit Weibull กับ field-return data ของ circuit board ระบบ railway signalling ได้ β = 2.37-3.85 (wear-out) และ prediction แบบ constant λ (RDF2000) ให้ MTBF สูงกว่า Weibull ราว 1.8-37 เท่า (derived จากตาราง) รายละเอียดใน [[Weibull Analysis]]
- จึงควรถือ "electronics = λ คงที่" เป็น **สมมติฐานที่ต้องตรวจด้วยข้อมูล** ไม่ใช่ข้อเท็จจริงทั่วไป ไม่ตั้ง contested เพราะ RBMM ให้เป็นแนวทางการเลือกใช้ ไม่ได้ยืนยันว่า electronics ทุกชนิดมี λ คงที่ และหลักฐานของ CMRP เองก็มีข้อจำกัด (R² ต่ำในสองโปรเจกต์)

### Normal และ Z (CMRP CMPR-06 p.23-27)

```
Z = (x - μ) / σ
Z_lower = (X-bar - LSL) / σ,   Z_upper = (USL - X-bar) / σ
```

- ตัวอย่าง μ = 150, σ = 20: P(x > 170) = 0.1587; μ = 300, σ = 5: P(x > 310) = 0.0228 (ตรวจถูก)
- **flag Example 4.16** (μ = 200, σ = 1.84, P(201 < x < 202) = 0.1567 ถูก): z ของ 201 เขียน -0.54 ที่ถูกคือ +0.54 และเรียกพื้นที่ cumulative (ทางซ้าย) ว่า "ทางขวา"
- Z_lower/Z_upper ใช้ต่อใน process capability (Cpk) ดู [[Statistical Process Control]]

### Lognormal (CMRP CMPR-06 p.27-29)

```
ln(t) ~ Normal(μ, σ)
mean = exp(μ + σ²/2)
σ_t  = sqrt( e^(2μ + σ²) · (e^(σ²) - 1) )
```

- เหมาะกับ transistor, bearing, insulation และ **เวลาซ่อม** (ดู [[Maintainability]]); เบ้ขวา ยิ่ง σ มากยิ่งเบ้; hazard เพิ่มขึ้นแล้วลดเข้าหาศูนย์
- แยก Weibull กับ lognormal ด้วยข้อมูลต้องใช้ราว 50 ตัวอย่างขึ้นไป (CMRP CMPR-06 p.21)
- ตัวอย่างหลอดไฟ 115/155/183/217 ชม.: mean ของ ln t = 5.0944 (ตรวจถูก; derived ต่อ: s ≈ 0.27, R(100) ≈ 0.965)
- **flag:** p.27 เรียก μ ว่า shape และ σ ว่า scale แต่ p.28 เรียก μ ว่า location และ σ ว่า scale ใช้คำไม่สอดคล้องกัน

## เชื่อมโยงกับ compressor failure hierarchy

- [[OREDA]] ใช้ failure rate คงที่ (Exponential, ต่อ 10^6 ชม.) ใช้ตั้งต้นได้ แต่ failure mode ที่ wear-out ควรใช้ Weibull หรือ Normal
- Poisson + lead time เหมาะกับ spare ของ compressor (seal, bearing) ดู [[Spare Parts Management]]
- ข้อมูลประเภทงานและ downtime ใน [[ISO 14224]] ใช้ประมาณ MTTR และแยก F/S ได้ ดู [[Failure Mode]]
- ปัญหาแท้จริงตามหนังสือคือขาดข้อมูลประวัติการเสียที่ถูกต้อง ไม่ใช่วิธีสถิติ (RBMM p.392)

## ดูเพิ่ม

- [[Weibull Analysis]]
- [[Statistical Process Control]]
- [[Reliability Metrics]]
- [[Censored Data]]
- [[Spare Part Demand Forecasting]]
- [[PM Interval Optimization]]

## Triplets

- Statistical Method Process [has_part:: Data Collection] then Data Presentation, Data Analysis, Interpretation (RBMM p.362)
- Data Collection [step_of:: Statistical Method Process] step 1
- Data Presentation [step_of:: Statistical Method Process] step 2, tables, graphs, equations
- Data Analysis [step_of:: Statistical Method Process] step 3
- Interpretation [step_of:: Statistical Method Process] step 4
- Meeting Attendance Example [has_value:: Mean = 241.3, Median = 252.5] Mode about 251-350 (RBMM p.365-367)
- Meeting Attendance Example [has_value:: 70%] cumulative probability that 300 seats suffice; 100 seats 5% (RBMM p.362-365)
- Probability Density Function [has_value:: total area = 1] area a to b = probability of failure in interval (RBMM p.367-371)
- Unreliability Function [has_formula:: F(t) = ∫0..t f(s) ds] cdf
- Reliability Function [has_formula:: R(t) = 1 - F(t)]
- Failure Rate [has_formula:: λ(t) = f(t)/R(t)] hazard
- Discrete Distribution [has_part:: Poisson Distribution] also Binomial, Geometric, Hypergeometric; integer counts such as spare withdrawals
- Continuous Distribution [has_part:: Normal Distribution] also Exponential, Weibull, Log Normal; failure times and PM intervals
- Continuous Distribution [has_part:: Exponential Distribution]
- Continuous Distribution [has_part:: Weibull Distribution]
- Distribution Selection [depends_on:: Analysis Type] also assumption fit and data fit checked after parameters
- Poisson Distribution [has_formula:: f(x) = e^(-D) D^x / x!] D = mean number of events (RBMM p.371-373)
- Poisson Distribution [has_formula:: D(lead time) = (annual usage x Lead Time) / 365]
- Poisson Distribution [applies_to:: Spare Part Withdrawals] random events
- Poisson Spare A Example [has_value:: D = 5.333] 5, 7, 4 pieces per year over 3 years
- Poisson Spare A Example [has_value:: 17.361%] P(5 pieces), highest; P(<= 5) = 55.768%, P(<= 11) = 99.12%
- Poisson Spare A Example [has_value:: D = 0.6575] lead time 45 days, derived
- Poisson Spare A Example [has_value:: 99.537%] stock 3 pieces sufficient within lead time
- Poisson Distribution [input_to:: [[Spare Part Demand Forecasting]]] see also [[EOQ and Reorder Point]]
- Normal Distribution [has_formula:: pdf = (1/(σ √(2π))) exp(-1/2 ((x-μ)/σ)^2)] printed with square brackets (RBMM p.374-376)
- Normal Distribution [has_parameter:: μ]
- Normal Distribution [has_parameter:: σ]
- Normal Distribution [applies_to:: Wear-out] symmetric around mean
- RBMM Sigma Rule [has_value:: small N uses N, large N (>20) uses N-1] as printed, reversed (RBMM p.374-376)
- Statistical Convention Sigma Rule [has_value:: small sample uses N-1, population uses N] general statistics convention
- RBMM Sigma Rule [contradicts:: Statistical Convention Sigma Rule] next example uses N-1 with N = 9
- Normal Failure Example [has_value:: μ = 295, σ = 101.486] 9 failures, N-1; σ ≈ 95.7 if N (derived)
- Normal Failure Example [has_value:: 4.23% / 12.86% / 75.48%] probability of failure within 120 / 180 / 365 days (RBMM p.375-376)
- Normal Failure Example [has_value:: 12.17%] PM every 120 days, 1-(1-0.0423)^3
- Normal Failure Example [has_value:: 24.06%] PM every 180 days, 1-(1-0.1286)^2; shortcut assumes as-good-as-new
- Exponential Distribution [has_formula:: pdf = λ e^(-λx);   cdf = 1 - e^(-λx);   λ = 1/mean = 1/MTTF] (RBMM p.376-378)
- Exponential Distribution [applies_to:: Random Failure] memoryless, human error, electrical equipment
- Light Bulb Example [has_value:: mean 1,546, λ = 0.00064683] 150, 700, 3120, 1200, 2560 h
- Light Bulb Example [has_value:: cdf(500) = 27.63%, cdf(1000) = 47.63%, cdf(2000) = 72.57%] pdf(2000) = 0.0177%
- Light Bulb Example [has_value:: 72.57%] replacing every 1,000 or 500 h gives same probability (RBMM p.377-378)
- Exponential Distribution [related_to:: [[Failure Patterns and Bathtub Curve]]] scheduled replacement does not reduce failure probability
- Weibull Distribution [has_parameter:: Shape Parameter Beta] flexible, mimics most distributions (RBMM p.378-384)
- Exponential Distribution [is_a:: Weibull Distribution] special case β = 1
- Weibull Example TTF 8500-16000 [has_value:: β = 3.7888, η = 13,130.8] Y regression; see [[Weibull Analysis]]
- Weibull Example TTF 8500-16000 [has_value:: β = 3.9406, η = 13,067.2] X regression
- Weibull Distribution [applies_to:: [[Failure Mode]]] all β patterns, one failure mode at a time
- [[OREDA]] [uses:: Exponential Distribution] constant failure rate per 10^6 h; wear-out modes should use Weibull or Normal
- Poisson Distribution [applies_to:: [[Compressor]]] spares such as seal, bearing with lead time; see [[Spare Parts Management]]
- [[ISO 14224]] [source_of:: MTTR] work type and downtime data, also F/S split
- Lack Of Accurate Failure History [is_a:: Root Problem] not the statistical method (RBMM p.392)
- [[Statistical Distributions for Maintenance]] [related_to:: [[Censored Data]]]
- [[Statistical Distributions for Maintenance]] [related_to:: [[PM Interval Optimization]]]
- [[Statistical Distributions for Maintenance]] [defined_in:: [[CMRP Course]]] supplementary section (CMRP CMPR-06, CMPR-08)
- Statistical Convention Sigma Rule [defined_in:: [[CMRP Course]]] sample SD uses n-1, population N (CMRP CMPR-06 p.7)
- Normal Distribution [has_value:: ±1σ 68.27%, ±2σ 95.45%, ±3σ 99.73%] standard values
- CMRP Normal Figure 96% And 99.74% [contradicts:: Normal Distribution] slide figures p.4 and p.7; correct 95.45% and 99.73%, tail 2.14% not 2.15%
- Central Limit Theorem [applies_to:: [[Statistical Process Control]]] sample means near normal (CMRP CMPR-06 p.7)
- Hypergeometric Distribution [applies_to:: Sampling Without Replacement] n > 10% of N (CMRP CMPR-06 p.10)
- Binomial Distribution [applies_to:: Sampling Without Replacement] approximation when n < 10% of N (CMRP CMPR-06 p.10)
- Normal Distribution [applies_to:: Binomial Approximation] np > 5 (CMRP CMPR-06 p.10)
- Discrete Distribution [has_part:: Binomial Distribution]
- Discrete Distribution [has_part:: Hypergeometric Distribution]
- Binomial Distribution [has_formula:: P(X = x) = n! / ( x!(n-x)! ) · p^x · (1-p)^(n-x)] μ = np, σ = sqrt( np(1-p) ) (CMRP CMPR-06 p.13-14)
- Binomial Example [has_value:: μ 1.5, σ 1.06] n = 6, p = 0.25; F(2) exact 0.831, slide 0.84 from rounding
- Binomial Distribution [input_to:: [[Statistical Process Control]]] p and np charts
- Hypergeometric Distribution [has_formula:: P(x; N, n, m) = C(m,x) · C(N-m, n-x) / C(N,n)] μ = n·m/N (CMRP CMPR-06 p.15)
- Hypergeometric Example [has_value:: P(0) 0.64696, P(1) 0.30808, P(<2) 0.95504] N 50, n 5, m 4
- Hypergeometric Example [has_value:: C(46,4) = 163,185 and C(46,5) = 1,370,754] correct values
- CMRP Combination Values 163,135 And 1,370,740 [contradicts:: Hypergeometric Example] slide substitution typo (CMRP CMPR-06 p.15)
- Exponential Distribution [has_value:: R(MTTF) = 0.368] (CMRP CMPR-06 p.17-20)
- CMRP Reciprocal Claim [contradicts:: Poisson Process Relation] slide p.18 says 1/x of exponential is Poisson, wrong
- Poisson Process Relation [has_value:: interarrival times exponential, counts per interval Poisson] correct relation
- Exponential Distribution [applies_to:: Electronics] RBMM and CMRP CMPR-06 p.18; assumption to verify with data
- Signalling Board Weibull Case [contradicts:: Exponential Distribution] β 2.37-3.85 for circuit boards, evidence against constant λ for electronics (CMRP CMPR-06 p.31-36); not contested
- Normal Distribution [has_formula:: Z = (x - μ) / σ] (CMRP CMPR-06 p.23-27)
- Example 4.16 [has_value:: P(201 < x < 202) = 0.1567] correct result; slide z sign and tail wording wrong (CMRP CMPR-06 p.26)
- Continuous Distribution [has_part:: Lognormal Distribution]
- Lognormal Distribution [has_formula:: mean = exp(μ + σ²/2)] ln t normal (CMRP CMPR-06 p.27-29)
- Lognormal Distribution [applies_to:: Repair Time] also transistor, bearing, insulation; see [[Maintainability]]
- Lognormal Distribution [differs_from:: Weibull Distribution] about 50 samples needed to distinguish (CMRP CMPR-06 p.21)

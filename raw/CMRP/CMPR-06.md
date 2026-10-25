# CMPR-06: Reliability apportionment, สถิติพื้นฐาน, distributions, Weibull case study, Markov/Monte Carlo และ SPC

Source: PETROSYNC CMRP training course slides, file CMPR-06.pdf (scanned, OCR). Reading notes ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ PDF page `(CMRP CMPR-06 p.N)`

Scope: PDF 48 หน้า (2 slide ต่อหน้า, เลขหน้าคู่มือ 207-254) เนื้อหากว้างกว่าที่คาด: apportionment มีแค่ p.1-2 ที่เหลือเป็นทบทวนสถิติ/probability, discrete และ continuous distributions, case study Weibull ของระบบ railway signaling, PM optimization, Markov, Monte Carlo และ SPC เบื้องต้น ไม่มีหัวข้อ AGREE, feasibility-of-objectives หรือ series/parallel RBD ในไฟล์นี้ OCR อ่านได้ดีในส่วนข้อความ แต่สูตรและตารางเพี้ยนมาก ตรวจจากภาพ 15 หน้า (p.2, 4, 12, 15, 19, 22, 27, 34-41) ไม่พบลายมือที่อ่านได้มีสาระ

## 1. Reliability apportionment (allocation) (CMRP CMPR-06 p.1-2)

- ข้อกำหนด reliability มักตั้งที่ระดับระบบ (failure rate หรือ MTBF) แล้วกระจายลงไป subsystem และ component ถ้าทุกระดับทำได้ตามเป้า ระบบจะผ่านเป้าด้วย ควรเริ่มทันทีที่มี preliminary design/drawing ทำให้ reliability เป็นคุณลักษณะของการออกแบบเทียบเท่า weight หรือ power
- ต้องมี system reliability model/block diagram ก่อน วิธีที่เลือกขึ้นกับระยะของการออกแบบ:
  - **Equal allocation**: ช่วงต้น แบ่งเป้าเท่ากันทุก subsystem
  - **ARINC (weighted) allocation**: เมื่อมีข้อมูลมากขึ้น ถ่วงน้ำหนักตาม failure rate ที่คาดการณ์ของแต่ละ subsystem (พัฒนาโดย ARINC Research Corp.)
- สมมติฐาน ARINC: series model และ exponential (λ คงที่) ดังนั้น λ_system = Σλi ถ้า Σλi > λ* (เป้า) ต้อง allocate ใหม่ด้วย

```
λi* = (λi / Σλi) × λ*
```

**ตัวอย่าง Example 9.3** (hydraulic flow pressure reducer, 4 subsystem อนุกรม): เป้า λ* = 20 ต่อ 10^6 ชม.; คาดการณ์ λ = 6.8, 5.4, 14.3, 3.5 รวม 30 ต่อ 10^6 ชม. > เป้า

| Subsystem | λ คาดการณ์ | Equal (20/4) | ARINC |
|---|---|---|---|
| 1 | 6.8 | 5 | 4.53 |
| 2 | 5.4 | 5 | 3.60 |
| 3 | 14.3 | 5 | 9.53 |
| 4 | 3.5 | 5 | 2.33 |

ตรวจเลขแล้วถูกต้อง (ARINC รวม = 20.0) ข้อสรุปของสไลด์: equal allocation ไม่คำนึงความซับซ้อน/stress/maturity ทำให้ subsystem 4 ไม่ต้องปรับปรุงเลย (เป้า 5 หลวมกว่าค่าปัจจุบัน 3.5) และอาจตั้งเป้าที่ทำไม่ได้ให้ subsystem 3 (ต้องลดจาก 14.3 เป็น 5) ส่วน ARINC ทุกตัวต้องลด ~33% เท่ากัน การ allocate ไม่ใช่ค่าสุดท้าย ควร reallocate เมื่อมีข้อมูลใหม่ เพราะ failure rate สูงมักลดได้ง่ายกว่าตัวที่ต่ำอยู่แล้ว

## 2. ทบทวนสถิติและ probability (p.3-9)

- Probability อยู่ระหว่าง 0-1 (ตัวอย่าง lot 100 ชิ้นเสีย 4 → 0.04) "random" = ทุกชิ้นมีโอกาสถูกเลือกเท่ากัน (p.3)
- Central tendency: mean (x̄ = Σx/n, เรียก expected value สำหรับ discrete), median (ค่ากลางหลังเรียง; จำนวนคู่ใช้ค่าเฉลี่ยสองตัวกลาง), mode (ค่าที่พบบ่อยสุด อาจมีหลายค่า) ใน normal ทั้งสามเท่ากัน ใน skewed ต่างกันมาก (p.4-5)
- Dispersion: range (ใช้แค่สองค่า เสียข้อมูล), variance s² = Σ(x-x̄)²/(n-1) (หน่วยยกกำลังสอง), standard deviation: sample ใช้ n-1, population (σ) ใช้ N (p.6-7)
- กฎ normal: ±1σ ≈ 68%, ±2σ ≈ 95.44%, ±3σ ≈ 99.73% **flag เล็ก:** รูป p.4 เขียน ±2SD = 96% และรูป p.7 เขียน 99.74% / 2.15% (ค่ามาตรฐาน 95.45%, 99.73%, 2.14%)
- **Central Limit Theorem** (p.7): ค่าเฉลี่ยของ sample กระจายใกล้ normal แม้ประชากรไม่ normal ยิ่ง n มากยิ่งดี จึงรองรับ ±3σ limits ของ x̄ chart สไลด์ระบุว่า n < 5 เหมาะเฉพาะเมื่อประชากร normal และเหตุผลหลักที่ plot ค่าเฉลี่ยคือไวต่อการ shift มากกว่าค่าเดี่ยว
- กฎ probability (p.8): complement P(not A) = 1 - P(A); special addition P(A or B) = P(A) + P(B) เมื่อ mutually exclusive; general addition หัก P(A and B)
- Contingency table สี 4 x ขนาด 3 รวม 192 ชิ้น (ตรวจผลรวมแถว/คอลัมน์ถูกต้อง) และ conditional probability P(Large | Green) = 21/54 ≈ 0.389 ถูกต้อง (p.8-9)

## 3. Discrete distributions (p.9-15)

- แผนผังประเภท: discrete (Bernoulli, binomial, negative binomial, geometric, Poisson, hypergeometric) กับ continuous (normal/standard normal, uniform ฯลฯ) (p.9)
- ตารางเลือก (p.10, อ้าง Juran): **hypergeometric** เมื่อรู้จำนวน defect ใน population, sampling ไม่คืน, n > 10% ของ N; **binomial** ประมาณ hypergeometric เมื่อ n < 10% ของ N; **Poisson** ใช้ μ = np; normal ประมาณ binomial เมื่อ np > 5
- pdf/cdf นิยาม (p.10-12) ตัวอย่าง bubble ในชิ้นไม้ 50 ชิ้น: relative frequency 0.22/0.30/0.32/0.12/0.04 สำหรับ 0-4 bubble = probability distribution (p.11)
- **Poisson** (p.12): P(X = x) = e^(-λ) λ^x / x!, cdf = ผลรวมถึง x (สไลด์เรียก "PDF" ทั้งที่เป็น pmf ของ discrete)
- **Binomial** (p.13-14): P(X = x) = n!/[x!(n-x)!] p^x (1-p)^(n-x); μ = np, σ = √(np(1-p))
  - ตัวอย่าง n = 6, p = 0.25: P(0)=0.18, P(1)=0.36, P(2)=0.30, P(3)=0.13, P(4)=0.03, P(5)=0.004, P(6)=0.0002 ตรวจแล้วถูก; μ = 1.5, σ ≈ 1.06 ถูก
  - F(2) = 0.18+0.36+0.30 = 0.84 ใช้ค่าปัดเศษ ค่าจริง ≈ 0.831 (ความคลาดจากการปัด)
- **Hypergeometric** (p.15): sampling ไม่คืน ความน่าจะเป็นเปลี่ยนทุกครั้งที่หยิบ (ตัวอย่างไพ่ 13/52 → 12/51 หรือ 13/51)

```
P(x; N, n, m) = C(m,x) C(N-m, n-x) / C(N,n);   μ = nm/N
```

  - ตัวอย่าง N = 50, n = 5, m = 4: P(1) = 0.30808, P(0) = 0.64696, P(<2) = 0.95504 ผลถูกต้อง
  - **flag:** ในสูตรแทนค่าพิมพ์ C(46,4) = 163,135 และ C(46,5) = 1,370,740 ค่าจริงคือ 163,185 และ 1,370,754 (ผลลัพธ์ใช้ค่าที่ถูก) และ P(0) เขียนสองค่า 0.64695/0.64696
  - **flag:** หัวข้อสไลด์เขียน "Hypergeometric (Geometric)" ซึ่งผิด geometric distribution เป็นคนละตัว (จำนวนครั้งจนสำเร็จครั้งแรก)

## 4. Continuous distributions และ reliability functions (p.16-30)

- ตาราง (p.16): normal (ใช้เมื่อค่าเท่ากันสองข้าง mean, ช่วยกำหนดจุดเริ่ม wear-out), exponential (λ คงที่, useful life), Weibull (η scale, β shape, γ location; ทดสอบจุดสิ้นสุด infant mortality, จำลอง exponential และใกล้ normal ได้)
- R(t) = 1 - F(t) (p.16); hazard function = instantaneous failure rate ของ item ที่รอดถึง t (p.17)
- **Exponential** (p.17-20): f(t) = λe^(-λt), F = 1 - e^(-λt), R = e^(-λt), h = λ, θ = 1/λ, variance = θ²; R(MTTF) = e^-1 ≈ 0.368 (MTBF ใช้แทนได้สำหรับ repairable)
  - ตัวอย่าง resistor λ = 0.04/ชม.: R(100) = e^-4 = 0.0183; F(25) = 1 - e^-1 = 0.632 → เสียราว 63 ใน 100 ชิ้น (ตรวจถูก)
  - ตัวอย่าง f(1000) ที่ λ = 0.00053: 0.00053 e^-0.53 ≈ 0.00031 ต่อชม. (ถูก) **flag เชิงแนวคิด:** สไลด์ตีความว่าเป็น "probability of failure at 1000 hours" ซึ่งไม่ถูก ค่า pdf เป็น density ต่อชั่วโมง ไม่ใช่ความน่าจะเป็น (mean = σ = 1/λ ≈ 1,887 ชม.)
  - **flag:** p.18 อ้างว่าถ้า x เป็น exponential แล้ว 1/x เป็น Poisson (และกลับกัน) ซึ่งผิดทางคณิตศาสตร์ ความสัมพันธ์ที่ถูกคือ เวลาระหว่างเหตุการณ์ของ Poisson process กระจายแบบ exponential ส่วนจำนวนเหตุการณ์ต่อช่วงเป็น Poisson (ส่วนท้ายของสไลด์กล่าวไว้ถูก)
  - สไลด์ระบุว่า exponential "มักใช้กับ electronics" (p.18)
- **Weibull** (p.20-23): 2-parameter และ 3-parameter (มี location เมื่อมีช่วงไม่เสีย); β = 1 เท่ากับ exponential, β = 2 = Rayleigh, β ≈ 3-4 ใกล้ normal; แยก Weibull กับ lognormal ต้องใช้ข้อมูลเกิน ~50 ตัวอย่าง; 63.2% เสียก่อน characteristic life เสมอ; location > 0 = failure-free period, < 0 = เสียก่อนเริ่มใช้ (ขนส่ง, shelf life); β < 1 hazard ลด, = 1 คงที่, > 1 เพิ่ม, β = 2 hazard เพิ่มเชิงเส้น

```
h(t) = (β/η)(t/η)^(β-1);   F(t) = 1 - exp(-(t/η)^β);   R(t) = exp(-(t/η)^β)
```

  - ตัวอย่าง (p.23): A mean 4,645 ชม., β = 0.8 → η ≈ 4,100; B mean 300 ชม., β = 3 → η ≈ 336 ที่ 100 ชม. R_A = 0.95, R_B = 0.974 แต่ที่ 1,000 ชม. R_A = 0.723, R_B ≈ 0 ตรวจด้วย MTTF = ηΓ(1+1/β) แล้วถูกทุกค่า ข้อคิด: mean อย่างเดียวเลือก component ไม่ได้ ต้องรู้รูปร่าง distribution และ mission time
- **Normal และ Z** (p.23-27): Z = (x - μ)/σ; Z_lower = (x̄ - LSL)/σ, Z_upper = (USL - x̄)/σ ตารางในคู่มือเป็นแบบพื้นที่หางขวา
  - น้ำหนักนักเรียน μ = 150, σ = 20: P(>170) = 0.1587 (ถูก)
  - extrusion μ = 300, σ = 5: P(>310) = 0.0228 (ถูก) สไลด์ถามต่อ <295 และ 295-310 แต่ไม่ได้เฉลย (derived: 0.1587 และ 0.8185)
  - **flag Example 4.16** (μ = 200, σ = 1.84, P(201 < x < 202)): ผล 0.1567 ถูก แต่ (ก) เขียน z ของ 201 เป็น -0.54 ที่ถูกคือ +0.54 (ข) ระบุว่า 0.8621 และ 0.7054 เป็นพื้นที่ "ทางขวา" ของ z ซึ่งความจริงเป็นพื้นที่ทางซ้าย (cumulative) (ค) ใช้สัญลักษณ์ n แทน μ
- **Lognormal** (p.27-29): ln(t) กระจาย normal; mean = exp(μ + σ²/2), σ_t = √(e^(2μ+σ²)(e^(σ²)-1)); เหมาะกับ transistor, bearing, insulation และเวลาซ่อม; ไม่สมมาตร skew ขวามากขึ้นเมื่อ σ เพิ่ม; hazard เพิ่มแล้วลดเข้าหาศูนย์
  - ตัวอย่างหลอดไฟ 115/155/183/217 ชม.: mean ของ ln = 5.0944 (ตรวจถูก) สไลด์ไม่ได้คำนวณ R(100) ต่อ (derived: s ≈ 0.27, z ≈ -1.81, R(100) ≈ 0.965)
  - Example 4.17 (850-2,750 cycles): mean ln ≈ 7.24 (สไลด์ปัด 7.25), s = 0.44 ตรวจถูก
  - **flag:** p.27 เรียก μ ว่า shape และ σ ว่า scale แต่ p.28 เรียก μ ว่า location และ σ ว่า scale ("บางครั้งเรียก shape") ใช้คำไม่สอดคล้องกัน
- Skewness และ kurtosis (p.30): skew = 0 สมมาตร, < 0 เบ้ซ้าย, > 0 เบ้ขวา; kurtosis (excess) ของ normal = 0, < 0 แบนกว่า, > 0 แหลมกว่า

## 5. Case study: Weibull ของระบบ railway signaling แบบ electronic (p.31-37)

- ประเด็น: ความเชื่อว่า electronics มี λ คงที่ตลอดอายุทำให้ไม่ทำ PM และประเมิน reliability ผิด จึงใช้ field-return data ของ circuit board (LRU, 11 ชนิด) มา fit Weibull
- Fit ด้วย least squares บน Weibull plot ข้อมูลส่วนใหญ่ right-censored ต้องปรับค่าเมื่อได้ข้อมูลใหม่ R² = 0.7513 (Prj1), 0.9355 (Prj2), 0.6101 (Prj3) **ข้อสังเกต:** สไลด์สรุปว่า "ข้อมูลเป็น Weibull" แม้ R² ของ Prj1/Prj3 ค่อนข้างต่ำ ข้อสรุปนี้อ่อน

| Board | Project | β | η (ชม.) | MTBF exp. (RDF2000) | MTBF Weibull | Half-life exp. (วัน) | Half-life Weibull (วัน) |
|---|---|---|---|---|---|---|---|
| Board_WS | Prj1 | 3.75 | 51,683 | 1.22 x 10^6 | 4.69 x 10^4 | 35,220 | 1,953 |
| Board_WS | Prj2 | 3.85 | 36,264 | 1.22 x 10^6 | 3.28 x 10^4 | 35,220 | 1,373 |
| Board_OB | Prj3 | 2.37 | 160,667 | 2.54 x 10^5 | 1.42 x 10^5 | 7,330 | 5,735 |

(ตัวเลขในตารางอ่านจากภาพความละเอียดต่ำ แต่ตรวจย้อนด้วยสูตรแล้วสอดคล้อง: MTBF = ηΓ(1+1/β), t½ exp = ln2/λ, t½ Weibull = η(ln2)^(1/β))

- β > 1 ทุกบอร์ด = wear-out; บอร์ดเดียวกันต่างโปรเจกต์ได้ β/η ต่างกัน แต่ exponential prediction (RDF2000) ให้ค่าเดียวกัน แสดงข้อจำกัดของ constant-λ prediction; Weibull MTBF "แย่กว่า" exponential มาก
- **flag:** สไลด์บอกว่า half-life ของ Weibull แย่กว่า exponential "สองอันดับขนาด" แต่อัตราส่วนจริงคือ 35,220/1,953 ≈ 18 และ 35,220/1,373 ≈ 26 คือราวหนึ่งอันดับขนาด (MTBF ต่างกัน ~26-37 เท่า) ส่วนที่ว่า failure rate ต่างกัน "เกือบสี่อันดับขนาด" ที่ 100,000 ชม. derived ได้ราว 550 เท่า (Prj1) ถึง 2,300 เท่า (Prj2) คือ 2.7-3.4 อันดับ
- สรุปของ case: การใช้ exponential อาจทำให้นโยบาย RCM เอนเอียง

## 6. PM optimization (as-good-as-new replacement) (p.37-39)

- เมื่อบอร์ด wear-out จึงคุ้มที่จะเปลี่ยนเชิงป้องกัน ช่วงเวลาขึ้นกับ β และอัตราส่วนต้นทุน
- สัญลักษณ์: p = ต้นทุนเปลี่ยน (สมมติเท่ากันทั้ง CM และ PM), P = ต้นทุนทางอ้อมของ failure (เช่น ค่าปรับ unavailability), θ = เวลาเปลี่ยน

```
C1 = (p + P) / MTBF                                  run-to-failure cost rate
C2(θ) = [p + P(1 - R(θ))] / m(θ),  m(θ) = ∫0..θ R(t) dt   preventive cost rate
x = θ/η,  r = P/p
C2/C1 = [1 + r(1 - e^(-x^β))] / m(x) × Γ(1+1/β) / (1 + r)
```

- ถ้า C2/C1 < 1 ควรทำ systematic PM; มี abacus ตาม β และ r (Fig.10)
- ตัวอย่าง β = 3, η = 50,000 ชม., r = 50: สไลด์ได้ θ = 10,950 ชม., C2/C1 = 0.1220 **ตรวจ (derived):** minimize สมการ (14) ได้ θ ≈ 10,780 ชม. ที่ ratio 0.1220 เท่ากัน ความต่าง ~1.6% อยู่ในช่วงที่เส้นโค้งแบนมาก ถือว่าสอดคล้อง

## 7. Markov analysis (p.40-41)

- ทำนายสถานะถัดไปจากสถานะปัจจุบันเท่านั้น (memoryless) ใช้ transition matrix; ตัวอย่างในรูป: two-state G/M, three-state และ three-state with absorption (limit ของ T^n ให้สัดส่วนระยะยาว เช่น 0.83/0.17 สำหรับ two-state ที่ T = [0.8 0.2; 1 0] ตรวจได้ 5/6, 1/6)
- ประวัติ: Markov ตีพิมพ์ปี 1906 โต้แย้ง Nekrasov เรื่องความจำเป็นของ independence ต่อ law of large numbers
- ตัวอย่างสัตว์กิน grapes/cheese/lettuce: สไลด์ถามสัดส่วนวันกิน grapes ระยะยาวแต่ไม่ได้เฉลย (derived: stationary ทั้งสามเท่ากัน = 1/3)
- การประยุกต์ที่ระบุ: ทำนายจำนวนชิ้นงานเสียจากสถานะเครื่องในสายการผลิต

## 8. Monte Carlo methods (p.42-45)

- ใช้การสุ่มซ้ำเพื่อแก้ปัญหาที่อาจ deterministic แต่วิเคราะห์ตรงไม่ได้ ใช้หลัก ๆ 3 กลุ่ม: optimization, numerical integration, สุ่มค่าจาก distribution; พูดถึง MCMC, mean-field particle methods, quasi-Monte Carlo (low-discrepancy sequences)
- รูปตัวอย่าง (p.44): thermal stress profile → lifetime model → damage distribution → lifetime distribution (Weibull) → unreliability function
- ประวัติ: Ulam/von Neumann ที่ Los Alamos ปลายทศวรรษ 1940, ENIAC, middle-square method; ชื่อจาก Monte Carlo Casino
- คุณสมบัติ simulation ที่ดี (Sawilowsky): random generator คาบยาว ผ่าน randomness test จำนวน sample พอ วิธี sampling และ algorithm ถูกต้อง

## 9. SPC และ control charts (p.45-48)

- Control chart ให้สัญญาณเร็วเมื่อ process เปลี่ยน; limit ที่ μ ± 3σ (ตัด LCL ได้ถ้าไม่มีความหมาย); จุดนอก limit หรือ pattern ผิดปกติ (เช่น 7 จุดติดกันด้านเดียวของ mean) = special cause; ชุดกฎที่นิยม: Minitab 8 ข้อ และ AIAG
- Attribute charts: p (สัดส่วนของเสีย, n แปรผัน), np (จำนวนของเสีย, n คงที่), c (จำนวน defect, n คงที่), u (defect ต่อหน่วย, n แปรผัน)
- Variables charts: x̄-R, x̄-s, I-MR, MX-MR, median, run chart
- เหตุที่ reliability engineer สนใจ: reliability ของ product ขึ้นกับ process ที่ผลิต ควรกำหนด SPC กับ characteristic ที่กระทบ life (p.47) Control chart เริ่มโดย Shewhart (1931) (p.48) รายละเอียด x̄-R อยู่ใน CMPR-07

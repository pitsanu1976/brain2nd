---
title: Reliability Allocation
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [reliability-allocation, reliability, statistics, failure-rate, cost, cmrp]
sources: [cmrp.md]
confidence: medium
contested: false
---

# Reliability Allocation

Reliability allocation (apportionment) = การกระจายเป้า reliability (หรือ failure rate / MTBF) ที่ตั้งไว้ระดับระบบลงไปยัง subsystem และ component ถ้าทุกระดับทำได้ตามเป้า ระบบก็ผ่านเป้า ควรเริ่มทันทีที่มี preliminary design เพื่อให้ reliability เป็นคุณลักษณะของการออกแบบเหมือน weight หรือ power และต้องมี system model / [[Reliability Block Diagram]] ก่อน (CMRP CMPR-06 p.1) ที่มาของหน้านี้คือสไลด์ [[CMRP Course]] (secondary teaching source) ส่วนการกระจายเป้า MTTR ดู [[Maintainability]]

## 1. วิธี allocation 3 กลุ่ม (CMRP CMPR-04 p.45; CMPR-06 p.1)

| วิธี | ใช้เมื่อ | ข้อดี / ข้อจำกัด |
|---|---|---|
| Equal | ช่วงต้นของการออกแบบ ข้อมูลน้อย | ง่าย แต่ไม่ optimal ไม่คำนึง complexity, stress, maturity |
| Weighted (ARINC) | มีค่าคาดการณ์ failure rate ราย subsystem | ถ่วงตาม λ ที่คาดการณ์ ทุกตัวต้องลดสัดส่วนเท่ากัน |
| Cost optimization | มี cost/penalty function ราย component | หาชุด R ที่ถึงเป้าด้วยต้นทุนรวมต่ำสุด (nonlinear programming) |

## 2. Equal allocation

ระบบอนุกรม n ชิ้น เป้า R_s: R_i = R_s^(1/n) หรือในรูป failure rate λi* = λ*/n

- ตัวอย่าง 5 ชิ้นอนุกรม เป้า 0.90 ได้ R_i = 0.98 ต่อชิ้น (0.98^5 = 0.904) (CMRP CMPR-04 p.46)
- ตัวอย่าง 4 subsystem เป้า λ* = 20 ต่อ 10^6 ชม. ได้ 5 ต่อ 10^6 ชม. ทุกตัว (CMRP CMPR-06 p.2)

## 3. ARINC (weighted) allocation (CMRP CMPR-06 p.1-2)

สมมติฐาน: ระบบอนุกรมและ exponential (λ คงที่) ดังนั้น λ_system = Σλi (กรณีพิเศษของ R_series = ΠRi ใน [[Reliability Block Diagram]]) พัฒนาโดย ARINC Research Corp.

```
λi* = (λi / Σλi) × λ*
```

**ตัวอย่าง** (hydraulic flow pressure reducer, 4 subsystem อนุกรม, หน่วย ต่อ 10^6 ชม.): เป้า λ* = 20; ค่าคาดการณ์รวม 30 จึงเกินเป้า

| Subsystem | λ คาดการณ์ | Equal (20/4) | ARINC |
|---|---|---|---|
| 1 | 6.8 | 5 | 4.53 |
| 2 | 5.4 | 5 | 3.60 |
| 3 | 14.3 | 5 | 9.53 |
| 4 | 3.5 | 5 | 2.33 |
| รวม | 30.0 | 20 | 20.0 |

(ตัวเลข ARINC ตรวจซ้ำแล้วถูก derived: λi x 20/30)

- Equal allocation ทำให้ subsystem 4 ไม่ต้องปรับเลย (เป้า 5 หลวมกว่าค่าปัจจุบัน 3.5) และตั้งเป้าที่อาจทำไม่ได้ให้ subsystem 3 (14.3 ลงเหลือ 5 คือลด 65%)
- ARINC ให้ทุกตัวลดราว 33% เท่ากัน
- ค่าที่ allocate ไม่ใช่ค่าสุดท้าย ควร reallocate เมื่อมีข้อมูลใหม่ เพราะตัวที่ λ สูงมักลดได้ง่ายกว่าตัวที่ต่ำอยู่แล้ว (CMRP CMPR-06 p.2)

## 4. ผลของโครงสร้างระบบต่อการเลือกชิ้นที่จะปรับ (CMRP CMPR-04 p.46-47)

- **อนุกรม** 0.70, 0.80, 0.90 ได้ R_s = 0.504 เป้า 0.85: ปรับชิ้นเดียวไม่พอแม้ทำให้เป็น 1 (สูงสุด 0.72, derived) ต้องปรับอย่างน้อย 2 ชิ้น
- **ขนาน** 0.6, 0.7, 0.8 ได้ R_s = 0.976 เป้า 0.99: ปรับชิ้นเดียวพอ (derived: R1 ≥ 0.833 หรือ R2 ≥ 0.875 หรือ R3 ≥ 0.917)
- มีหลายชุดคำตอบที่ถึงเป้า จึงต้องใช้ cost function ตัดสินว่าปรับชิ้นไหน (CMRP CMPR-05 p.3)

**Flag ข้อผิดในสไลด์ (CMPR-04 p.44)**: ตัวอย่าง RBD R1 = 0.905 อนุกรมกับ (R2 = 0.580 ขนาน R3 = 0.600) อนุกรมกับ R4 = 0.861: ส่วนขนาน 1 - (0.42 x 0.40) = 0.832 ถูก แต่ 0.905 x 0.832 x 0.861 = **0.648** ไม่ใช่ 0.541 ตามสไลด์ (ความผิดเลขคณิต ไม่ใช่ contested; RBMM ก็มีความผิดแบบเดียวกัน ดู [[Reliability Block Diagram]])

## 5. Cost / penalty function (CMRP CMPR-05 p.1-2)

ถ้ามีข้อมูลต้นทุนจริง (reliability growth program, ราคาหลายรุ่นจาก vendor) ให้สร้าง C_i = f(R_i) จากข้อมูล ถ้าไม่มี ใช้ default model ที่มีคุณสมบัติ 3 ข้อ: ถูกจำกัดระหว่าง R ปัจจุบันกับ R สูงสุด (< 1), ไม่ linear (ยิ่งสูงยิ่งยาก เช่น 99.99% เป็น 99.999% ยากกว่า 90% เป็น 91% มาก), และ asymptotic เข้าหา R สูงสุด

```
C_i(R_i) = exp[ (1 - f_i) * (R_i - R_min,i) / (R_max,i - R_i) ]
```

- **C_i เป็นค่าไม่มีหน่วย** (dimensionless weighting ของความยากในการปรับปรุง) **ไม่ใช่ต้นทุนเงิน** อย่าสับสนกับต้นทุนเงินบาทใน [[Maintenance Cost Structure]] หรือ [[Maintenance Budget]]
- f_i = feasibility (0 ถึง 1) ความง่ายในการปรับชิ้นนี้เทียบกับชิ้นอื่น; **f ต่ำ = ปรับยาก cost พุ่งเร็ว** (กราฟ f = 0.1, 0.5, 0.9 ที่ R_max = 0.99)
- R_min,i = reliability ปัจจุบัน ณ เวลาที่ optimize (ไม่ลดต่ำกว่านี้); R_max,i = ค่าสูงสุดที่ทำได้ ณ เวลาเดียวกัน cost พุ่งเข้าอนันต์เมื่อ R เข้าใกล้ R_max
- cost ขึ้นกับช่วงปรับปรุง (R_max - R_min): ยกจากค่าต่ำง่ายกว่า เช่น 70% เป็น 75% ง่ายกว่า 90% เป็น 95%
- การหา f เป็นเรื่อง subjective: ใช้ weighting factor (complexity, state of the art, operating profile, criticality) หรือ engineering judgment (คุณภาพ/ความพร้อมของ supplier); ถ้ามีข้อมูลต้นทุนจริงให้ regression หา parameter

ข้อสังเกต derived (ไม่อยู่ในสไลด์): ที่ R_i = R_min,i ได้ C = e^0 = 1 ทุกชิ้น ("ไม่ปรับ" มีต้นทุนฐาน 1 ไม่ใช่ 0) และถ้า f = 1 จะได้ C = 1 คงที่ (ไม่มี penalty) จึงควรใช้ f < 1 ตัวอย่าง R_min = 0.70, R_max = 0.99:

| R เป้า | f = 0.1 | f = 0.5 | f = 0.9 |
|---|---|---|---|
| 0.80 | 1.61 | 1.30 | 1.05 |
| 0.90 | 7.39 | 3.04 | 1.25 |
| 0.95 | 277 | 22.8 | 1.87 |
| 0.98 | 8.8e10 | 1.2e6 | 16.4 |

ความรู้ทั่วไป (confidence low): รูปสูตรนี้ตรงกับ default cost function ของซอฟต์แวร์ ReliaSoft BlockSim

## 6. Maximum achievable reliability และ mission time (CMRP CMPR-05 p.3)

- R_max ถูกจำกัดด้วยเทคโนโลยีหรือการเงิน ต้องอ้าง mission time เดียวกับเป้าระบบ (เช่น เป้าระบบ 99% ที่ 1,000 ชม. ค่า R_max ของทุกชิ้นต้องเป็นของ 1,000 ชม.) และทำหน้าที่เป็น scale parameter ของฟังก์ชัน
- ตัวอย่างสไลด์: exponential λ = 1 ต่อชม. จะเหลือ R < 1% เมื่อ mission เกิน 5 ชม. และได้ 99.9% เมื่อ mission ไม่เกินราว 4 วินาที
- **Flag ความคลาดในสไลด์**: ที่ 4 s ได้ R = e^(-4/3600) = 0.99889 (99.89%) ต่ำกว่า 99.9% เล็กน้อย; mission ที่ให้ 99.9% คือ **≤ 3.6 s** (-ln 0.999 x 3600 = 3.60 s, derived) ส่วน R ตกถึง 1% ตั้งแต่ราว 4.6 ชม. ข้อความ "เกิน 5 ชม." จึงถูกแต่หลวม

## 7. System cost และ nonlinear programming (CMRP CMPR-05 p.3)

```
minimize   C_s = C_1(R_1) + C_2(R_2) + ... + C_n(R_n)
subject to R_system(R_1..R_n) >= R_target
           R_min,i <= R_i < R_max,i
```

- ต้นทุนระบบ = ผลรวมต้นทุนชิ้นส่วนไม่ว่าฟังก์ชันรายชิ้นเป็นรูปใด
- โครงสร้างระบบ (series/parallel) เข้าสู่ constraint ผ่าน R_system จาก RBD; routine เลือกชุดที่ต้นทุนรวมต่ำสุด สไลด์ไม่แสดงผลลัพธ์ optimization เป็นตัวเลข
- ทางเลือกระหว่างยก reliability ของชิ้นเดียวกับเพิ่ม redundancy ดู [[Redundancy and Standby Systems]]

## เชื่อมโยงกับ compressor failure hierarchy

- ARINC ใช้ได้โดยตรงกับ failure rate ของ [[OREDA]] (λ คงที่ต่อ 10^6 ชม.) ราย sub unit ของ [[Compressor]] ที่ต่ออนุกรมเชิง function เช่น [[PWTR Power Transmission]], [[LUBS Lubrication System]], [[CTMN Control and Monitoring]] เพื่อตั้งเป้าปรับปรุงราย sub unit (การประยุกต์ของ wiki ไม่มีตัวอย่างใน sources, confidence low)
- ถ้า failure mode มี β > 1 สมมติฐาน exponential ของ ARINC ไม่ถือ ต้องใช้ R(t) ที่ mission time จาก [[Weibull Analysis]] แทน

## ดูเพิ่ม

- [[Reliability Block Diagram]]
- [[Fault Tree Analysis]]
- [[Maintainability]]
- [[Redundancy and Standby Systems]]
- [[Reliability Metrics]]

## Triplets

- [[Reliability Allocation]] [defined_in:: [[CMRP Course]]] distribute system target to subsystems and components (CMRP CMPR-06 p.1)
- [[Reliability Allocation]] [uses:: [[Reliability Block Diagram]]] system model required first (CMRP CMPR-06 p.1)
- Equal Allocation [is_a:: [[Reliability Allocation]]] early design, simple, not optimal (CMRP CMPR-04 p.45-46; CMPR-06 p.1)
- ARINC Allocation [is_a:: [[Reliability Allocation]]] weighted by predicted failure rate (CMRP CMPR-06 p.1)
- Cost Optimization Allocation [is_a:: [[Reliability Allocation]]] minimum total penalty subject to system target (CMRP CMPR-04 p.45; CMPR-05 p.3)
- Equal Allocation [has_formula:: R_i = R_s^(1/n)] series; λi* = λ*/n
- Equal Allocation [has_value:: 0.98 per unit] 5 units in series, target 0.90, 0.98^5 = 0.904 (CMRP CMPR-04 p.46)
- ARINC Allocation [has_formula:: λi* = (λi / Σλi) × λ*] (CMRP CMPR-06 p.1)
- ARINC Allocation [depends_on:: Constant Failure Rate] series and exponential, λ_system = Σλi
- Hydraulic Pressure Reducer Example [has_value:: target 20, predicted 30 per 10^6 h] subsystems 6.8, 5.4, 14.3, 3.5 (CMRP CMPR-06 p.2)
- Hydraulic Pressure Reducer Example [has_value:: Equal 5 / 5 / 5 / 5] per 10^6 h (CMRP CMPR-06 p.2)
- Hydraulic Pressure Reducer Example [has_value:: ARINC 4.53 / 3.60 / 9.53 / 2.33] per 10^6 h, sum 20.0, verified (CMRP CMPR-06 p.2)
- Equal Allocation [differs_from:: ARINC Allocation] equal leaves subsystem 4 unimproved and asks subsystem 3 to cut 14.3 to 5; ARINC cuts all about 33%
- [[Reliability Allocation]] [depends_on:: New Data] reallocate as data arrive; high λ easier to reduce (CMRP CMPR-06 p.2)
- Series Allocation Example [has_value:: 0.504] 0.70 x 0.80 x 0.90; target 0.85 needs at least 2 units improved (CMRP CMPR-04 p.46)
- Parallel Allocation Example [has_value:: 0.976] 0.6, 0.7, 0.8; target 0.99 reachable by one unit (CMRP CMPR-04 p.47)
- CMRP RBD Example Result [has_value:: 0.541] as printed, wrong (CMRP CMPR-04 p.44)
- Correct CMRP RBD Example Result [has_value:: 0.648] 0.905 x 0.832 x 0.861, derived
- CMRP RBD Example Result [contradicts:: Correct CMRP RBD Example Result] slide arithmetic error, not contested
- Penalty Function [has_formula:: C_i(R_i) = exp((1 - f_i)(R_i - R_min,i)/(R_max,i - R_i))] square brackets written as round (CMRP CMPR-05 p.2)
- Penalty Function [has_parameter:: Feasibility f] 0 to 1, low f = hard to improve, cost rises faster (CMRP CMPR-05 p.2)
- Penalty Function [has_parameter:: R_min] current reliability at time of optimization
- Penalty Function [has_parameter:: R_max] maximum achievable, cost tends to infinity as R approaches it (CMRP CMPR-05 p.2-3)
- Penalty Function [differs_from:: [[Maintenance Cost Structure]]] dimensionless weighting, not money
- Penalty Function [has_value:: C = 1 at R_i = R_min,i] derived; f = 1 gives no penalty [confidence:: medium]
- Penalty Function [has_value:: 3.04] R_min 0.70, R_max 0.99, R 0.90, f 0.5; derived [confidence:: medium]
- Penalty Function [related_to:: ReliaSoft BlockSim] default cost function, general knowledge [confidence:: low]
- Maximum Achievable Reliability [depends_on:: Mission Time] must use same mission time as system target (CMRP CMPR-05 p.3)
- CMRP Mission Time Example [has_value:: about 4 s for 99.9%] λ = 1/h, as printed (CMRP CMPR-05 p.3)
- Correct Mission Time For 99.9% [has_value:: ≤ 3.6 s] -ln 0.999 x 3600, derived; 4 s gives 99.89%
- CMRP Mission Time Example [contradicts:: Correct Mission Time For 99.9%] slide slip, not contested
- System Cost [has_formula:: C_s = C_1(R_1) + C_2(R_2) + ... + C_n(R_n)] (CMRP CMPR-05 p.3)
- Cost Optimization Allocation [uses:: Nonlinear Programming] minimize C_s s.t. R_system ≥ target, R_min ≤ R_i < R_max (CMRP CMPR-05 p.3)
- [[Reliability Allocation]] [related_to:: [[Maintainability]]] maintainability allocation is the MTTR counterpart
- [[Reliability Allocation]] [related_to:: [[Redundancy and Standby Systems]]] alternative to single-unit improvement
- [[Reliability Allocation]] [related_to:: [[Fault Tree Analysis]]]
- ARINC Allocation [applies_to:: [[Compressor]]] OREDA constant λ per sub unit in functional series; wiki application [confidence:: low]

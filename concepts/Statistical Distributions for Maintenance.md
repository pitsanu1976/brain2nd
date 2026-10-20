---
title: Statistical Distributions for Maintenance
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [statistics, reliability, weibull, spare-parts, book]
sources: [reliability-based-maintenance-management.md]
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

## เชื่อมโยงกับ compressor failure hierarchy

- [[OREDA]] ใช้ failure rate คงที่ (Exponential, ต่อ 10^6 ชม.) ใช้ตั้งต้นได้ แต่ failure mode ที่ wear-out ควรใช้ Weibull หรือ Normal
- Poisson + lead time เหมาะกับ spare ของ compressor (seal, bearing) ดู [[Spare Parts Management]]
- ข้อมูลประเภทงานและ downtime ใน [[ISO 14224]] ใช้ประมาณ MTTR และแยก F/S ได้ ดู [[Failure Mode]]
- ปัญหาแท้จริงตามหนังสือคือขาดข้อมูลประวัติการเสียที่ถูกต้อง ไม่ใช่วิธีสถิติ (RBMM p.392)

## ดูเพิ่ม

- [[Weibull Analysis]]
- [[Reliability Metrics]]
- [[Censored Data]]
- [[Spare Part Demand Forecasting]]
- [[PM Interval Optimization]]

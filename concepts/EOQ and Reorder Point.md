---
title: EOQ and Reorder Point
created: 2026-10-21
updated: 2026-10-21
type: concept
tags: [spare-parts, statistics, cost, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# EOQ and Reorder Point

หน้านี้รวมสูตรคำนวณระดับสต็อกอะไหล่ของ RBMM บทที่ 9: EOQ (ปริมาณสั่งซื้อประหยัดสุด), ROP/Min (จุดสั่งซื้อ) และ Safety Stock ภายใต้ความแปรปรวนของ demand และ Lead Time โดยใช้ Normal Distribution และค่า Z ตาม Confidence ที่ต้องการ ใช้กับกลุ่ม Fast Moving และ Low Criticality ตามกรอบใน [[Spare Part Criticality and Risk]] ส่วนอะไหล่ที่ demand น้อยและกระโดด (รวมกรณี Poisson) ดู [[Spare Part Demand Forecasting]] ภาพรวมอยู่ที่ [[Spare Parts Management]]

## นิยามคำ

| คำ | ความหมาย | อ้างอิง |
|---|---|---|
| Lead Time (LT) | เวลาจากออก PR จนของพร้อมในคลัง | RBMM p.247 |
| ROP / Min | ระดับสต็อกที่ต้องสั่งซื้อ | RBMM p.247-248 |
| Max | ระดับสูงสุดของสต็อก | RBMM p.239 |
| Safety Stock (SS) | สต็อกสำรองรับความผิดปกติของ demand และ supply | RBMM p.248 |
| Confidence Level | ความมั่นใจว่ามีอะไหล่ในช่วง Lead Time | RBMM p.246 |
| Z | จำนวนเท่าของ sigma ที่ให้ความมั่นใจที่กำหนด (one-sided) | RBMM p.249 |

## EOQ (RBMM p.252-253)

สมมติ Lead Time และ Demand Rate คงที่ สต็อกเฉลี่ย = Q/2 (รูปที่ 9.10)

```
Ch = ค่าเก็บต่อหน่วย (ต่อปี)
Cp = ค่าจัดซื้อต่อครั้ง
A  = ปริมาณใช้ต่อปี
Q  = ปริมาณสั่งซื้อต่อครั้ง

ค่าเก็บรวม     = (Q/2) x Ch
ค่าจัดซื้อรวม  = (A/Q) x Cp
Cost_total     = (Q/2) x Ch + (A/Q) x Cp

ต่ำสุดเมื่อค่าเก็บ = ค่าจัดซื้อ:
Q = sqrt( 2 x A x Cp / Ch )
```

- หนังสือพิมพ์ผิด: หน้า 253 เขียนค่าจัดซื้อเป็น Q/2 x Cp แต่ Cost_total และสูตร EOQ ใช้ A/Q ซึ่งถูกต้อง ใช้ A/Q
- Cp ในบทนี้ = ค่าจัดซื้อต่อครั้ง คนละความหมายกับ Cp ในบทที่ 8 ซึ่งคือค่า PM ต่อครั้ง ดู [[PM Interval Optimization]]
- Ch ได้จาก holding cost ประมาณ 15-20% ของราคาอะไหล่ต่อปี (RBMM p.16, p.234) ดังนั้น Ch = อัตราค่าถือครอง x ราคาต่อหน่วย (derived; หนังสือไม่เขียนสูตรนี้ตรง ๆ แต่เป็นความหมายของ "ค่าเก็บต่อหน่วย")
- ข้อควรระวัง Shelf Life: ถ้าราคาต่อชิ้นต่ำเทียบกับค่าจัดซื้อ EOQ จะให้ปริมาณสูง; ถ้าอายุเก็บสั้น ต้องจำกัดปริมาณเพราะอะไหล่หมดอายุก่อนใช้ (RBMM p.256)
- EOQ ใช้กับ Fast Moving Parts และ Low Criticality ในกรอบ Supply Side (RBMM p.238)

## ROP กรณีคงที่ (RBMM p.247)

```
ROP (Min) = Demand Rate x Lead Time
```

รูปที่ 9.7 เป็นกราฟฟันปลา สต็อกลดลงถึง ROP แล้วสั่ง ของมาถึงหลัง LT

## ROP กรณีแปรปรวน และ Safety Stock (RBMM p.253-255)

ในความจริง demand และ Lead Time แปรปรวน (รูปที่ 9.11) ROP เฉย ๆ อาจไม่พอ ใช้ข้อมูลเบิกจริงหา distribution ของ demand และข้อมูลส่งมอบหา distribution ของ Lead Time (รูปที่ 9.12 สมมติทั้งคู่เป็น Normal)

```
ROP            = D_avg x LT_avg + SS
SS             = z x sigma_combined
sigma_combined = sqrt( (sigma_D)^2 x LT_avg + (sigma_LT x D_avg)^2 )

D_avg    = demand เฉลี่ย (หน่วยต่อวัน)
LT_avg   = lead time เฉลี่ย (วัน)
sigma_D  = SD ของ demand rate
sigma_LT = SD ของ lead time
```

(รูปที่ 9.13) Risk of Stock out = 1 - Confidence

### ตาราง Z (RBMM p.249, รูปที่ 9.8)

| Confidence | Z |
|---|---|
| 0.841 | 1.0000 |
| 0.850 | 1.0364 |
| 0.875 | 1.1503 |
| 0.900 | 1.2816 |
| 0.925 | 1.4395 |
| 0.950 | 1.6446 |
| 0.975 | 1.9600 |
| 0.995 | 2.5758 |
| 0.9975 | 2.8070 |

## ตัวอย่าง (RBMM p.255-256)

ข้อมูล: demand เฉลี่ย 12 ชิ้น/ปี (D_avg = 12/365 ต่อวัน), LT_avg = 90 วัน, sigma_D = 0.14 ชิ้น/วัน, sigma_LT = 26.5 วัน, Confidence 90% (Z = 1.2816)

```
SS  = 1.2816 x sqrt( 0.14^2 x 90 + (26.5 x 12/365)^2 )
    = 2.035  ~ 2 ชิ้น
ROP = (12/365) x 90 + 2 = 2.95 + 2 ~ 5 ชิ้น   (ใช้เป็น Min)
```

ตรวจเลข (derived): 0.14^2 x 90 = 1.764; (26.5 x 12/365) = 0.871 จึงกำลังสองได้ประมาณ 0.759; รวม 2.523; sqrt = 1.588; คูณ 1.2816 = 2.04 ตรงกับ 2.035 ของหนังสือ; (12/365) x 90 = 2.96 หนังสือปัดเป็น 2.95 ผลรวมประมาณ 4.99 ปัดเป็น 5 ชิ้น

## ผลของ Lead Time ต่อสต็อก

- ROP และ SS โตตาม LT_avg และ sigma_LT; หนังสืออ้างว่าลด Lead Time 20% ลดสต็อกเฉลี่ยลงเหลือครึ่งหนึ่ง (RBMM p.247) เป็นข้ออ้างโดยไม่แสดงการคำนวณ
- ในตัวอย่างด้านบน เทอม demand (1.764) ใหญ่กว่าเทอม LT (ประมาณ 0.759) แต่เทอม LT ยังมีสัดส่วนประมาณ 30% ของความแปรปรวนรวม (derived: 0.759 / 2.523) แสดงว่า sigma_LT ที่ 26.5 วัน (เทียบกับ LT_avg 90 วัน) ไม่ควรมองข้าม
- การบริหาร Lead Time เชิงบวกกับผู้ขายช่วยลด sigma_LT (RBMM p.247)

## ข้อจำกัดของวิธีนี้

- สมมติ Normal Distribution; กับอะไหล่ที่ใช้น้อย (0-5 ชิ้นต่อปี) demand เป็นจำนวนเต็มไม่สมมาตร ควรใช้ Poisson หรือ Monte Carlo ดู [[Spare Part Demand Forecasting]] และ [[Statistical Distributions for Maintenance]]
- ไม่คำนึงความวิกฤติของ item; ต้องจัดกลุ่มก่อน (ดู [[Spare Part Criticality and Risk]]) อะไหล่ Medium/High ใช้ Cost Ratio และ Simulation
- รวมความต้องการตามแผนและนอกแผนเฉพาะอะไหล่ใช้ร่วมที่ตาราง PM ไม่พร้อมกัน (RBMM p.236)

## เชื่อมโยงกับ compressor failure hierarchy

- ฟิลด์ Min, Max, ROP, EOQ ถูกเก็บเป็นกลุ่มที่ 3 (ค่าจากการคำนวณ) ใน Spare Part Database ของ [[CMMS]] (RBMM p.102) ผูกกับ [[Maintainable Item]] ผ่าน BOM
- ค่า D_avg ของ item ควรมาจากประวัติเบิกที่อ้าง failure mode ใน [[Failure Mode]] ตามแนวทางข้อมูลของ [[Failure Data Recording]]
- sources ของ wiki นี้ไม่มีข้อมูลเบิก/Lead Time ของ compressor จริง ตัวอย่างข้างบนเป็นตัวอย่างของหนังสือ ไม่ใช่ข้อมูลของ [[Compressor]]

## ดูเพิ่ม

- [[Spare Parts Management]]
- [[Spare Part Criticality and Risk]]
- [[Spare Part Demand Forecasting]]
- [[Statistical Distributions for Maintenance]]

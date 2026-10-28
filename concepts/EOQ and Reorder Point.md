---
title: EOQ and Reorder Point
created: 2026-10-21
updated: 2026-10-28
type: concept
tags: [spare-parts, statistics, cost, maintenance-management, book, cmrp, spo, inventory-control, mpm]
sources: [reliability-based-maintenance-management.md, cmrp.md, spare-parts-optimization.md, maintenance-profit-maker.md]
confidence: medium
contested: true
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

## ส่วนเสริมจาก CMRP: MRO inventory (CMRP CMPR-08 p.31-45)

เนื้อหาจาก [[CMRP Course]] (สื่อการสอน) สอดคล้องกับ RBMM ข้างบน และเพิ่มแบบจำลองการเติมสต็อก 4 แบบ

### นิยามและชนิด MRO stock (CMRP CMPR-08 p.32-37)

- MRO inventory = ของในคลัง + ของที่สั่งแล้วยังไม่ส่ง ลูกค้าคือฝ่ายบำรุงรักษา/ผลิต
- ชนิด: operating spares, rotatable spares, overhaul spares, insurance spares และ consumables
- เป้าระยะสั้น (control) = มีของพอในที่ที่ถูกต้อง; ระยะยาว (management) = สมดุลต้นทุนถือครองกับความเสี่ยง stock-out; total cost = inventory cost + stock-out consequence มีจุดต่ำสุดที่ optimum stock level (หลักเดียวกับ [[Spare Part Criticality and Risk]])

### ระดับสต็อกและ safety stock (CMRP CMPR-08 p.38-41)

- 3 ระดับ: replenishment level (สูงสุด, เทียบ Max), reorder level (เทียบ ROP/Min), safety stock ใช้ safety stock กับรายการ non-insurance ของเครื่องวิกฤต
- ROP = เมื่อไรสั่ง, ROQ = สั่งเท่าไร

```
Safety stock (CMRP) = K × σ × sqrt(Lead Time)
K = safety factor (เทียบ Z),  σ = SD ของ demand ต่อหน่วยเวลา (หน่วยเดียวกับ Lead Time)
```

**เทียบกับสูตร RBMM ข้างบน:** ถ้า Lead Time คงที่ (sigma_LT = 0) สูตร sigma_combined = sqrt( (sigma_D)^2 x LT_avg ) = sigma_D x sqrt(LT_avg) ดังนั้น SS = z x sigma_D x sqrt(LT_avg) ตรงกับสูตร CMRP สูตร CMRP จึงเป็น **กรณีพิเศษ** ที่ไม่คิดความแปรปรวนของ Lead Time ไม่ใช่ความขัดแย้ง (derived) ในตัวอย่าง RBMM ข้างบน เทอม LT มีสัดส่วนราว 30% ของความแปรปรวนรวม ถ้าใช้สูตร CMRP จะได้ SS = 1.2816 x 0.14 x sqrt(90) ≈ 1.70 แทน 2.04 (derived) จึงต่ำไปเมื่อ Lead Time แปรปรวนมาก

### 4 basic inventory models (CMRP CMPR-08 p.43-45)

สัญลักษณ์ของสไลด์: **B** = ติดตามสต็อกต่อเนื่อง (continuous review), **s** = ตรวจตามรอบ (periodic review)

| Model | ปริมาณสั่ง | เวลาสั่ง | เหมาะกับ |
|---|---|---|---|
| BS (Min-Max) | แปรผัน (เติมถึง max) | แปรผัน (เมื่อถึง reorder level) | การเบิกผันผวนมาก |
| BQ | คงที่ | แปรผัน (เมื่อถึง reorder level) | การเบิกผันผวนน้อย |
| sS | แปรผัน (เติมถึง max) | คงที่ (ตามรอบ) | การเบิกผันผวนน้อย |
| sQ | คงที่ | คงที่ (ตามรอบ) | การเบิกผันผวนมาก |

**flag สไลด์:** ตาราง 2x2 สรุปใน p.42 ขัดกับสไลด์รายละเอียด p.43-45 (p.42 จัด sS/sQ เป็นปริมาณคงที่ และ BS/BQ เป็นปริมาณแปรผัน และจัด BQ/sQ เป็นจุดสั่งแปรผัน) ตารางข้างบนยึด p.43-45 ซึ่งสอดคล้องกันเองและตรงกับชื่อ model (S = เติมถึงระดับ, Q = ปริมาณคงที่)

ข้อสังเกต (ความรู้ทั่วไป ไม่อยู่ในสไลด์): สัญลักษณ์ B/s ของสไลด์ต่างจากตำรามาตรฐาน ซึ่งใช้ s = reorder point เช่น (s, Q) = continuous review ปริมาณคงที่ (ใกล้ BQ), (s, S) = min-max (ใกล้ BS), (R, S) = periodic order-up-to (ใกล้ sS) เมื่ออ่านแหล่งอื่นต้องเทียบความหมาย ไม่ใช่ตัวอักษร [confidence: low]

EOQ ของ RBMM ข้างบนให้ค่า Q ของ model แบบปริมาณคงที่ (BQ, sQ) ส่วน ROP + SS ให้ reorder level ของ BS/BQ (การเชื่อมโยง derived)

## ส่วนเสริมจาก SPO (SPO p.103-110)

[[Spare Parts Optimization Book]] บทที่ 9 ใช้สูตรเดียวกันในมุมคลังพัสดุ รายละเอียดทั้ง 6 วิธีและตารางวิธี x ประเภทพัสดุอยู่ที่ [[MRO Inventory Control Methods]]

### สัญลักษณ์ EOQ ของ SPO (SPO p.104)

```
EOQ = sqrt( 2 x A x CO / (C x I) )
A  = ความต้องการทั้งปี           (= A ของ RBMM)
CO = ค่าสั่งซื้อ 1 รายการ 1 ครั้ง  (= Cp ของ RBMM) ไทยราว 90-120 บาท
C  = ราคาต่อหน่วย
I  = Investment Factor สัดส่วนค่าเก็บต่อมูลค่าสต็อกต่อปี  (C x I = Ch ของ RBMM)
```

- สูตรเทียบเท่าสูตร RBMM ข้างบน (derived) และสนับสนุนความหมาย Ch = อัตราค่าถือครอง x ราคาต่อหน่วย ที่หน้านี้ระบุว่าเป็น derived
- SPO ให้คำนวณ I จากรายงาน **Cost of Possession (COP)** 7 รายการ: ผลประโยชน์จากเงินลงทุน, ประกันภัย, ค่าเช่าพื้นที่คลัง, ค่ายกขน, ค่าบริหาร/ควบคุม, ของล้าสมัย/เสื่อม, ของหาย (SPO p.104) SPO ไม่ให้ค่า I เป็นตัวเลข จึงไม่ขัดกับ holding cost 15-20% ต่อปีของ RBMM (RBMM p.16, p.234) ข้างบน; ต่างกันที่ RBMM รวมค่าจัดซื้อจัดหาไว้ใน holding cost (RBMM p.68) ขณะที่ SPO แยกเป็น CO (derived) ไม่ตั้ง contested
- ข้อจำกัดเหมือน RBMM: ต้องมีสถิติการใช้ เหมาะกับของหมุนเร็ว; ถ้า EOQ เล็กจนต้องสั่งบ่อยให้ใช้ Blanket Order / System Contract ดู [[MRO Purchasing and Contracting]] (SPO p.105)

### ROP และ safety stock แบบ % (SPO p.105-107)

```
ROP = (D x LT) + SS,   SS = % ของ D x LT
ตัวอย่าง: D 20/เดือน, LT 2 เดือน, SS 20% -> 40 + 8 = 48
```

- % ของ SS = % เบี่ยงเบน lead time + % เบี่ยงเบนอัตราใช้ (ตัวอย่าง 10% + 10%); ตัวอย่างก๊าซออกซิเจนใช้ 10% -> ROP = 20 + 2 = 22 (SPO p.107)
- เทียบ Min-Max: Mid = ROP = 48, Min = SS = 8, จำนวนสั่ง = EOQ (SPO p.105-106)
- **ความต่างจาก RBMM:** SS ของ SPO เป็นกฎง่าย (rule of thumb) ไม่มี confidence level กำกับ ต่างจาก SS = z x sigma_combined ข้างบนที่มาจากการกระจายของ demand และ lead time ตามความรู้ทั่วไป SS แบบ % โตเป็นเส้นตรงตาม D x LT ส่วนแบบสถิติขึ้นกับความแปรปรวนจริง (โตตาม sqrt(LT) เมื่อ LT คงที่) [confidence:: low] เป็นวิธีต่างระดับความละเอียด ไม่ใช่ข้อเท็จจริงขัดกัน ดู [[SPO vs RBMM Spare Parts Approaches]]
- High/Low Limit ของ SPO (High = D x Stockage Objective, Low = ROP) ใกล้กับ BS Model (Min-Max) ของ CMRP ข้างบน และ Periodic Review (สั่ง M - (OH + QOD) ตามรอบ) ใกล้ sS Model (การเทียบ derived)

## ส่วนเสริมจาก MPM (เพิ่ม 2026-10-28)

[[Maintenance Profit Maker Book]] บทที่ 5 ใช้ EOQ กับกลุ่ม Perpetual Inventory Model (อะไหล่เคลื่อนไหวเร็ว-ปานกลาง ราคาสูง-ปานกลาง) ในเมทริกซ์ Movement x Cost ดู [[MRO Inventory Control Methods]]

### สัญลักษณ์ EOQ ของ MPM (MPM p.88)

```
EOQ = sqrt( 2 x A x B / (C x D) )
A = ค่าใช้จ่ายในการจัดซื้อต่อหนึ่งรายการ (ordering cost ต่อครั้ง)
B = อัตราการเบิกใช้ต่อปี
C = ราคาต่อชิ้น
D = ค่าครอบครองเป็นเศษส่วนของราคาต่อหน่วย (ต่อปี)
```

| ความหมาย | MPM | SPO | RBMM |
|---|---|---|---|
| ค่าสั่งซื้อต่อครั้ง | **A** | CO | Cp |
| ปริมาณใช้ต่อปี | **B** | **A** | **A** |
| ราคาต่อหน่วย | C | C | (อยู่ใน Ch) |
| อัตราค่าครอบครองต่อปี | D | I | (อยู่ใน Ch) |
| ค่าครอบครองต่อหน่วยต่อปี | C x D | C x I | Ch |

- สูตรเทียบเท่ากันทั้งสามเล่ม (derived) แต่ **ตัวอักษร A ของ MPM หมายถึงค่าสั่งซื้อ ขณะที่ A ของ SPO และ RBMM หมายถึงปริมาณใช้ต่อปี** ต้องระวังเมื่อยกสูตรข้ามเล่ม หนังสือไม่ให้ตัวอย่างตัวเลข (MPM p.88)

### ข้อขัดแย้ง MPM-C1: ค่า D (อัตราค่าครอบครอง) (contested)

- MPM ข้อความหลัก: ค่าเก็บสำรองราว **20-40%** ของมูลค่าอะไหล่ (MPM p.84)
- MPM ตัวอย่างตัวเลข: คิดเฉพาะต้นทุนการเงิน **6-10%** (MPM p.17, p.108, p.180-181)
- RBMM: **15-20%** ต่อปี (RBMM p.16, p.234) ซึ่งเป็นที่มาของ Ch ในหัวข้อ EOQ ข้างบน
- ผล (derived): EOQ แปรผกผันกับ sqrt(D) ถ้าใช้ D = 40% แทน 15% EOQ จะเล็กลงราว sqrt(15/40) = 0.61 เท่า; ถ้าใช้ D = 6% (ดอกเบี้ยอย่างเดียว) EOQ ใหญ่ขึ้นราว sqrt(15/6) = 1.58 เท่า จึงต้องระบุขอบเขตของค่าครอบครองก่อนคำนวณ ยังไม่ resolve รายละเอียดที่ [[Spare Parts Management]]

## เชื่อมโยงกับ compressor failure hierarchy

- ฟิลด์ Min, Max, ROP, EOQ ถูกเก็บเป็นกลุ่มที่ 3 (ค่าจากการคำนวณ) ใน Spare Part Database ของ [[CMMS]] (RBMM p.102) ผูกกับ [[Maintainable Item]] ผ่าน BOM
- ค่า D_avg ของ item ควรมาจากประวัติเบิกที่อ้าง failure mode ใน [[Failure Mode]] ตามแนวทางข้อมูลของ [[Failure Data Recording]]
- sources ของ wiki นี้ไม่มีข้อมูลเบิก/Lead Time ของ compressor จริง ตัวอย่างข้างบนเป็นตัวอย่างของหนังสือ ไม่ใช่ข้อมูลของ [[Compressor]]

## ดูเพิ่ม

- [[Spare Parts Management]]
- [[Spare Part Criticality and Risk]]
- [[Spare Part Demand Forecasting]]
- [[Statistical Distributions for Maintenance]]
- [[CMRP Course]]
- [[MRO Inventory Control Methods]]
- [[Spare Parts Optimization Book]]
- [[Maintenance Profit Maker Book]]

## Triplets

- [[EOQ and Reorder Point]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 9
- [[EOQ and Reorder Point]] [part_of:: [[Spare Parts Management]]]
- EOQ [alias_of:: Economic Order Quantity]
- Reorder Point [alias_of:: Min]
- Lead Time [measures:: time from PR to part ready in store] (RBMM p.247)
- Safety Stock [measures:: buffer for demand and supply variation] (RBMM p.248)
- Z [measures:: number of sigma for required confidence] one-sided (RBMM p.249)
- EOQ [has_parameter:: Ch] holding cost per unit per year
- EOQ [has_parameter:: Cp] purchasing cost per order; differs from Cp in chapter 8 (PM cost)
- EOQ [has_parameter:: A] annual usage
- EOQ [has_parameter:: Q] order quantity
- Average Stock [has_formula:: Q/2] constant LT and demand (RBMM p.252, Fig 9.10)
- Total Inventory Cost [has_formula:: (Q/2) x Ch + (A/Q) x Cp] (RBMM p.253)
- EOQ [has_formula:: sqrt( 2 x A x Cp / Ch )] minimum when holding cost = purchasing cost (RBMM p.252-253)
- Ordering Cost Term [has_formula:: (A/Q) x Cp] book p.253 misprints Q/2 x Cp (RBMM p.253)
- Ch [has_formula:: holding rate x unit price] derived, not written in book [confidence:: low]
- Ch [depends_on:: Holding Cost] about 15-20% of part price per year (RBMM p.16, p.234) MPM-C1 [contested:: true]
- EOQ [depends_on:: Shelf Life] short shelf life limits quantity (RBMM p.256)
- EOQ [applies_to:: Fast Moving] and Low Criticality (RBMM p.238)
- Reorder Point [has_formula:: Demand Rate x Lead Time] constant case (RBMM p.247)
- Reorder Point [has_formula:: D_avg x LT_avg + SS] variable demand and LT (RBMM p.253-255)
- Safety Stock [has_formula:: z x sigma_combined] (RBMM p.253-255)
- sigma_combined [has_formula:: sqrt( (sigma_D)^2 x LT_avg + (sigma_LT x D_avg)^2 )] (RBMM p.253-255, Fig 9.13)
- Reorder Point [depends_on:: Safety Stock]
- Safety Stock [depends_on:: Confidence Level] via Z
- Risk of Stock out [has_formula:: 1 - Confidence] (RBMM Fig 9.13)
- Reorder Point [uses:: Normal Distribution] demand and LT assumed Normal (RBMM Fig 9.12)
- Z [has_value:: 1.0000] Confidence 0.841 (RBMM p.249, Fig 9.8)
- Z [has_value:: 1.2816] Confidence 0.900 (RBMM p.249, Fig 9.8)
- Z [has_value:: 1.6446] Confidence 0.950 (RBMM p.249, Fig 9.8)
- Z [has_value:: 1.9600] Confidence 0.975 (RBMM p.249, Fig 9.8)
- Z [has_value:: 2.5758] Confidence 0.995 (RBMM p.249, Fig 9.8)
- Z [has_value:: 2.8070] Confidence 0.9975 (RBMM p.249, Fig 9.8)
- Safety Stock [has_value:: 2.035 ~ 2 pieces] example D_avg 12/365 per day, LT_avg 90 d, sigma_D 0.14, sigma_LT 26.5 d, Z 1.2816 (RBMM p.255-256)
- Reorder Point [has_value:: 2.95 + 2 ~ 5 pieces] example, used as Min (RBMM p.255-256)
- Lead Time Variance Term [has_value:: about 30%] share of total variance in example, 0.759 / 2.523, derived [confidence:: low]
- Lead Time [has_value:: 20% reduction halves average stock] book claim, no calculation shown (RBMM p.247) [confidence:: low]
- Reorder Point [differs_from:: Poisson Distribution] Normal not suited to 0-5 pieces per year; use Poisson or Monte Carlo, see [[Spare Part Demand Forecasting]]
- Reorder Point [related_to:: [[Statistical Distributions for Maintenance]]]
- Reorder Point [part_of:: Spare Part Database] group 3 calculated field in [[CMMS]] (RBMM p.102)
- EOQ [part_of:: Spare Part Database] group 3 calculated field in [[CMMS]] (RBMM p.102)
- [[EOQ and Reorder Point]] [defined_in:: [[CMRP Course]]] MRO inventory supplement (CMRP CMPR-08 p.31-45)
- MRO Inventory [has_category:: operating, rotatable, overhaul, insurance spares, consumables] (CMRP CMPR-08 p.32-34)
- MRO Inventory [has_part:: Replenishment Level] also reorder level and safety stock (CMRP CMPR-08 p.38-39)
- Replenishment Level [alias_of:: Max]
- Safety Stock [has_formula:: K × σ × sqrt(Lead Time)] CMRP form, K = safety factor (CMRP CMPR-08 p.39)
- CMRP Safety Stock Formula [is_a:: Safety Stock] special case of z x sigma_combined with sigma_LT = 0, derived
- CMRP Safety Stock Formula [has_value:: 1.70 pieces] applied to RBMM example ignoring LT variation vs 2.04, derived [confidence:: low]
- BS Model [is_a:: Inventory Model] Min-Max, continuous review, variable quantity and time (CMRP CMPR-08 p.43-45)
- BQ Model [is_a:: Inventory Model] continuous review, fixed quantity, variable time
- sS Model [is_a:: Inventory Model] periodic review, order up to max, fixed time
- sQ Model [is_a:: Inventory Model] periodic review, fixed quantity, fixed time
- CMRP Inventory Model Summary Table [contradicts:: BS Model] p.42 2x2 table inconsistent with p.43-45 detail slides
- BQ Model [maps_to:: (s, Q) Policy] standard notation, general knowledge [confidence:: low]
- BS Model [maps_to:: (s, S) Policy] standard notation, general knowledge [confidence:: low]
- sS Model [maps_to:: (R, S) Policy] standard notation, general knowledge [confidence:: low]
- EOQ [input_to:: BQ Model] fixed order quantity, derived
- Total Inventory Cost [has_part:: Stock-out Consequence] optimum stock level at minimum (CMRP CMPR-08 p.37)
- [[EOQ and Reorder Point]] [related_to:: [[Spare Part Criticality and Risk]]]
- [[EOQ and Reorder Point]] [defined_in:: [[Spare Parts Optimization Book]]] SPO supplement, chapter 9 (SPO p.103-110)
- [[EOQ and Reorder Point]] [related_to:: [[MRO Inventory Control Methods]]]
- EOQ [has_formula:: sqrt( 2 x A x CO / (C x I) )] SPO notation, equivalent to RBMM form, derived (SPO p.104)
- CO [maps_to:: Cp] cost of one order line, about 90-120 baht in Thailand (SPO p.104)
- C x I [maps_to:: Ch] I = Investment Factor, holding cost fraction per year, derived (SPO p.104)
- Cost of Possession [input_to:: I] 7 items incl. investment return, insurance, rent, handling, admin, obsolescence, loss (SPO p.104)
- Cost of Possession [differs_from:: Holding Cost] SPO separates ordering cost as CO; RBMM holding cost includes procurement cost (RBMM p.68), not contested, derived
- Reorder Point [has_formula:: (D x LT) + SS] SPO form (SPO p.105)
- Safety Stock [has_formula:: percent of D x LT] SPO rule of thumb, e.g. 10% + 10% = 20% (SPO p.105)
- Safety Stock [differs_from:: z x sigma_combined] SPO percent rule vs RBMM statistical, not contested, general knowledge [confidence:: low]
- Reorder Point [has_value:: 48] SPO example D 20, LT 2 months, SS 8 (SPO p.105)
- Reorder Point [maps_to:: Min-Max] Mid = ROP, Min = SS, order quantity = EOQ (SPO p.105-106)
- [[EOQ and Reorder Point]] [defined_in:: [[Maintenance Profit Maker Book]]] MPM supplement, Perpetual Inventory Model (MPM p.88)
- EOQ [has_formula:: sqrt( 2 x A x B / (C x D) )] MPM notation, equivalent form, derived (MPM p.88)
- MPM A [maps_to:: Cp] MPM A = ordering cost per order; SPO and RBMM A = annual usage (MPM p.88)
- MPM B [maps_to:: A] annual usage (MPM p.88)
- MPM D [maps_to:: I] holding fraction of unit price per year; C x D = Ch (MPM p.88)
- MPM D [has_value:: 20-40%] MPM text holding cost of stocked value, MPM-C1 (MPM p.84) [contested:: true]
- MPM D [contradicts:: Ch] RBMM holding cost 15-20% per year (RBMM p.16, p.234); MPM examples use finance cost only 6-10% (MPM p.17, p.108, p.180-181), MPM-C1 [contested:: true]
- EOQ [depends_on:: Holding Cost] EOQ scales with 1 / sqrt(D); D 40% vs 15% gives 0.61x, derived [confidence:: low]

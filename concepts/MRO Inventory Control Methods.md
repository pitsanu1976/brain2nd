---
title: MRO Inventory Control Methods
created: 2026-10-27
updated: 2026-10-27
type: concept
tags: [spo, book, inventory-control, spare-parts, statistics, cost, maintenance-management]
sources: [spare-parts-optimization.md]
confidence: medium
contested: false
---

# MRO Inventory Control Methods

วิธีควบคุมระดับคงเหลือพัสดุโรงงาน (MRO) ตามบทที่ 9 ของ [[Spare Parts Optimization Book]] (SPO p.101-110) และนโยบายคลังในบทที่ 5 (SPO p.55-57) Inventory control คือรักษาระดับคงเหลือให้พอใช้ครั้งต่อไป โดยสั่งเติม (stock replenishment) ไม่มากหรือน้อยเกินแนวโน้มความต้องการ ตอบ 2 คำถาม: **สั่งเมื่อไร** และ **สั่งครั้งละเท่าไร** (SPO p.102) รายการที่เก็บสำรองเรียก regular stock items นับเป็น SKU และเข้าบัญชี inventory การแบ่งประเภทพัสดุดู [[MRO Material Classification]] สูตรเชิงสถิติของ RBMM ดู [[EOQ and Reorder Point]] และการจัดซื้อที่ใช้คู่กันดู [[MRO Purchasing and Contracting]]

ข้อวิจารณ์ของผู้เขียน: ซอฟต์แวร์ทั่วไปให้ผู้ใช้ตั้ง Min-Max เอง ซึ่งไม่เหมาะกับของใช้มาก มูลค่าสูง หมุนเร็ว หรือ lead time นาน ที่ต้องมีสต็อกช่วงจัดหา + ระดับปลอดภัย; Min-Max เหมาะกับของหมุนช้าที่ไม่มีสถิติ โดยใช้ Basic Practice ทางวิศวกรรมช่วย (SPO p.102)

## 6 วิธีที่นิยม (SPO p.103)

| วิธี | เมื่อไร | เท่าไร | เหมาะกับ |
|---|---|---|---|
| ROP/EOQ | เมื่อคงเหลือถึง ROP (แปรผัน) | EOQ (เกือบคงที่) | ของหมุนเร็ว มีสถิติ |
| High/Low Limit | เมื่อถึง Low Limit = ROP | High Limit - On Hand | หมุนเร็ว-ปานกลาง พยากรณ์ได้ |
| Min-Max (กำหนดเอง) | เมื่อถึง Min | เติมถึง Max | หมุนช้ามาก จำนวนน้อย |
| Periodic Review (PRM) | ตามรอบคงที่ | M - (OH + QOD) (แปรผัน) | ราคาต่ำหมุนเร็ว แบบซูเปอร์มาร์เก็ต |
| Order Up-to | ทันทีที่เบิก | เท่าที่เบิก | อะไหล่ประกัน |
| Order as Required (OAR) | เมื่อต้องใช้ | เท่าที่ต้องใช้ | ของหาง่าย lead time สั้น, งานตามแผน |

## ROP/EOQ (SPO p.103-106)

ผู้เขียนเห็นว่ามีเหตุผลที่สุดเพราะใช้หลักเศรษฐศาสตร์: สั่งครั้งละมาก ค่าเก็บและเงินลงทุนสูง; สั่งครั้งละน้อย สั่งบ่อย ค่าสั่งสูงและเสี่ยงของขาด EOQ อยู่ที่ต้นทุนรวมรายปีต่ำสุด (รูปที่ 9.1 เส้น Total Annual Cost รูปตัว U)

### EOQ (SPO p.104)

```
EOQ = sqrt( 2 x A x CO / (C x I) )

A  = ความต้องการทั้งปี (จากค่าพยากรณ์ต่องวด เช่น สัปดาห์/เดือน)
CO = Cost of Order ค่าสั่งซื้อ 1 รายการ 1 ครั้ง (ไทยราว 90-120 บาท)
C  = ราคาต่อหน่วย
I  = Investment Factor = ค่าใช้จ่ายการเก็บเป็นสัดส่วนของมูลค่าสต็อกต่อปี
```

- C x I ตรงกับ Ch ของ RBMM และ CO ตรงกับ Cp ดู [[EOQ and Reorder Point]] (เทียบสัญลักษณ์ derived)
- หน่วยต้องสอดคล้อง: A ต่อปี, I เป็นสัดส่วนต่อปี (เช่น 0.25 ไม่ใช่ 25) (derived; บทนี้ไม่มีตัวอย่างตัวเลข EOQ)
- SPO ไม่ให้ค่า I เป็นตัวเลข ให้คำนวณจากรายงาน COP ของกิจการเอง

### Cost of Possession (COP) 7 องค์ประกอบ (SPO p.104)

แบบรายงานรายปี ระบุ inventory at year end และ average inventory แล้วแจกค่าใช้จ่ายเป็นบาทและ %:

1. ผลประโยชน์จากเงินลงทุน (ดอกเบี้ย / rate of return ที่ต้องการ)
2. ประกันภัย
3. ค่าเช่าพื้นที่คลัง
4. ค่ายกขนเคลื่อนย้าย
5. ค่าบริหาร/ควบคุม
6. ความเสียหายจากล้าสมัย/เสื่อม
7. ของหาย

รวม = COP ซึ่งเป็นที่มาของ I เทียบกับองค์ประกอบ holding cost ของ RBMM (ดอกเบี้ย, ค่าจัดเก็บ, ค่าจัดซื้อจัดหา, ของเสื่อมสภาพ, Write-off) (RBMM p.68) ใน [[Spare Parts Management]]: ทั้งสองมีดอกเบี้ย ค่าเก็บ และของล้าสมัย; SPO แยกประกันภัย ยกขน และของหาย ส่วน RBMM รวมค่าจัดซื้อจัดหาไว้ใน holding cost ซึ่ง SPO แยกเป็น CO (derived)

### ข้อจำกัดของ EOQ (SPO p.105)

- ต้องมีสถิติการใช้พอสมควร จึงเหมาะกับวัสดุทั่วไป เคมี ชิ้นส่วนสิ้นเปลือง อะไหล่ใช้หลายเครื่อง และของหมุนเร็ว
- ถ้าได้จำนวนน้อยต้องสั่งบ่อย แก้ด้วย Blanket Order / System Contract
- ต้องปรับตัวแปรแบบพลวัตเมื่อราคาหรืออัตราใช้เปลี่ยน

### Reorder Point (SPO p.105-106)

```
ROP = (D x LT) + SS

D  = อัตราการใช้/ค่าพยากรณ์จากสถิติ
LT = lead time จากสถิติที่ผ่านมา
SS = % ของ D x LT  (= % เบี่ยงเบน lead time + % เบี่ยงเบนอัตราใช้)
```

ตัวอย่าง: D = 20/เดือน, LT = 2 เดือน, SS = 10% + 10% = 20%

```
D x LT = 20 x 2 = 40
SS     = 0.20 x 40 = 8
ROP    = 40 + 8 = 48
```

ตรวจเลข (derived): ถูกต้อง

**เทียบ Min-Max:** ROP มีเหตุผลกว่าการตั้ง Min ตรง ๆ ถ้าแปลงเป็นภาษา Min-Max: Mid = ROP = 48, Min = SS = 8 และจำนวนสั่งต่อครั้ง = EOQ เป็นข้อเสนอสำหรับรายการหมุนเร็ว (SPO p.105-106)

### Safety stock แบบ % (SPO) เทียบ z x sigma (RBMM)

- SPO: SS = % ของความต้องการช่วงจัดหา (ตัวอย่าง 20% หรือ 10%) เป็นกฎง่ายของผู้เขียนสำหรับ MRO ไม่มีระดับ confidence กำกับ (SPO p.105, p.107)
- RBMM: SS = z x sigma_combined จากการกระจายของ demand และ lead time พร้อมตาราง Z ตาม Confidence (RBMM p.253-255) ดู [[EOQ and Reorder Point]]
- ความต่าง (ความรู้ทั่วไป ไม่อยู่ใน sources): SS แบบ % โตเป็นเส้นตรงตาม D x LT ส่วน z x sigma โตตาม sqrt(LT) เมื่อ lead time คงที่ และขึ้นกับความแปรปรวนจริง ไม่ใช่ค่าเฉลี่ย แบบ % จึงอาจสูงเกินกับของหมุนเร็วที่ใช้สม่ำเสมอ และต่ำเกินกับของที่ใช้กระโดด เป็นวิธีต่างระดับความละเอียด ไม่ใช่ข้อเท็จจริงขัดกัน [confidence:: low] ดู [[SPO vs RBMM Spare Parts Approaches]]

## High Limit / Low Limit (SPO p.106-107)

- ไม่ใช่ Min-Max ตรง ๆ เพราะต้องคำนวณและกำหนด **Stockage Objective** ใช้ในกองทัพสหรัฐ (Busanda: Bureau Supply and Account)
- Stockage Objective = ระยะ/ปริมาณเก็บนานสุดที่ยังทำงานได้โดยไม่ต้องเบิกคลังใหญ่ (= สต็อกสูงสุด) เหมาะกับอะไหล่หมุนเร็วถึงปานกลางที่พยากรณ์ได้

```
High Limit  = D x Stockage Objective
Low Limit   = ROP = (D x LT) + SS
จำนวนสั่ง   = High Limit - On Hand ณ วันสั่ง
```

ตัวอย่างก๊าซออกซิเจน: D = 40 ท่อ/เดือน, Stockage Objective 3 เดือน, LT = 1/2 เดือน, SS = 10% ของ D x LT

```
High Limit = 40 x 3 = 120 ท่อ
D x LT     = 40 x 0.5 = 20;  SS = 0.10 x 20 = 2
Low Limit  = 20 + 2 = 22 ท่อ
สั่งเมื่อเหลือ 22 พอดี   -> 120 - 22 = 98
ใช้เลยจุดสั่งจนเหลือ 10 -> 120 - 10 = 110
```

ตรวจเลข (derived): ถูกต้อง

- High/Low เปลี่ยนทันทีเมื่ออัตราใช้เปลี่ยน ผู้เขียนว่าดีกว่า Min/Max และสะดวกกว่า ROP/EOQ; ของหมุนเร็วควรสั่งผ่าน Blanket Order (SPO p.107)
- รูปที่ 9.2 แสดง Stockage Objective/High Limit, Low Limit = ROP, ช่วง D x LT และ Safety Stock (SPO p.107)

## Min-Max กำหนดเอง (SPO p.107)

- ตั้งจาก Basic Practice ทางวิศวกรรม/ผู้ชำนาญ คาดคะเนหรือจับสถิติบ้าง ผิดพลาดสูง โดยเฉพาะเมื่อตั้งหลายพันรายการในเวลาสั้น
- แต่ได้ผลกับของหมุนช้ามาก จำนวนสำรองน้อย: ในย่านตัวเลขต่ำ Min-Max ดีกว่าสองวิธีที่คำนวณ ฐานจำนวนเริ่มต้นดู [[Spare Parts Recommendation by Equipment Type]]

## Periodic Review (PRM) (SPO p.108-109)

ตรวจนับตามรอบคงที่ (fixed periodic replenishment cycle) แล้วเติมเท่าที่หมดไป ต้องเลือก R (Review Time) และ M (Maximum Quantity)

| | เมื่อไร | เท่าไร |
|---|---|---|
| PRM | คงที่ | แปรผัน |
| EOQ | แปรผัน | คงที่ |

```
จำนวนสั่ง = M - (OH + QOD)     OH = คงเหลือ, QOD = ค้างรับ
M = 90, ค้างรับ 30, คงเหลือ 25  -> 90 - (25 + 30) = 35
ปลายเดือนเหลือ 10 ไม่มีค้างรับ -> 90 - 10 = 80
```

ตรวจเลข (derived): ถูกต้อง เหมาะกับวัสดุราคาต่ำหมุนเร็วที่บริหารแบบซูเปอร์มาร์เก็ต (บทที่ 7) ดู [[Warehouse Design and Storage]]

**flag:** ข้อความ PRM ในหนังสือว่ามี "ยอดจุดสั่งซื้ออยู่ตลอดเวลา" ขัดกับความหมาย fixed review cycle น่าจะเป็นถ้อยคำ/OCR คลาดเคลื่อน

## Order Up-to (SPO p.109)

- กำหนดจำนวนคงคลังคงที่ (ตาม Basic Practice บทที่ 5) เบิกไปเท่าไรสั่งแทนทันทีเท่านั้น
- ตัวอย่าง: เก็บ Return-bend 5 อันเสมอ เบิก 2 เหลือ 3 สั่ง 2 ทันที -> On Hand 3 + On Order 2 = 5
- เหมาะกับอะไหล่ประกัน/เตรียมพร้อม (insurance standby)

## Order as Required (OAR) (SPO p.109-110)

- อยู่ในทะเบียนสำรองคลัง (ไม่ใช่ของลงค่าใช้จ่ายตรง) แต่สต็อกปกติ = 0 ซื้อเมื่อต้องใช้ เช่น สีทาเหล็ก/ไม้ ท่อประปา
- ตัวอย่าง: คงเหลือ 0 -> สั่ง 20 -> เบิก 15 เหลือ 5 -> เบิก 5 เหลือ 0 -> ซื้อใหม่เมื่อมีความต้องการ (20 - 15 - 5 = 0, derived ถูกต้อง)
- ใน Reorder Report ใส่ "OAR" ในคอลัมน์ OAR/Min กันระบบพิมพ์รายการสั่งเมื่อยังไม่ต้องใช้
- เหมาะกับ (1) ของมีในตลาด จัดซื้อได้ใน 1 วัน/ชั่วโมงและรอได้ (2) อะไหล่ที่วางแผนจัดหาล่วงหน้าได้ เช่น งานโครงการ ซ่อมใหญ่ ดู [[Turnaround Management]] (สอดคล้องกับหลัก RBMM ที่ให้งานตามแผนใช้ซื้อตรง ใน [[Spare Parts Management]])

## Free Stock Issue

ไม่ใช่วิธีสั่งซื้อแยก แต่เป็นประเภทพัสดุ/คอลัมน์ในตารางสรุป: ของราคาต่ำจ่ายบ่อย (bolt, nut, washer, ถ่าน, กระดาษทราย) บริหารแบบซูเปอร์มาร์เก็ต ไม่ต้องใช้ใบเบิก ลงค่าใช้จ่ายผ่าน cost center (SPO p.68, p.74) เติมด้วย Periodic Review (SPO p.108-110) **flag:** เกณฑ์ราคาในบทที่ 7 ไม่ตรงกันเอง (p.68 ไม่เกินราว 5-10 บาท/ชิ้น vs p.74 ราว 10-20 ไม่เกิน 50 บาท) ดู [[Warehouse Design and Storage]] และ [[Tool Crib and Warehouse Security]]

## ตารางสรุป วิธี x ประเภทพัสดุ (SPO p.110)

| วิธี | Unique | Insurance Standby | Common Used | Capitalize | General Used / Chem-Gas | Low Value | Free Stock Issue |
|---|---|---|---|---|---|---|---|
| ROP/EOQ | | | ✓ | | ✓ | | |
| High/Low Limit | | | ✓ | | ✓ | | |
| Min-Max | ✓ | ✓ | | ✓ | | | |
| Periodic Review | | | | | | | ✓ |
| Order Up to | ✓ | ✓ | | ✓ | | | |
| Order as Required | ✓ (Planned Shutdown/Turnaround) | | | | ✓ (เฉพาะ short lead time) | | |

**flag (OCR):** คอลัมน์ Low Value ว่างทุกแถว ทั้งที่ข้อความว่า PRM เหมาะกับของราคาต่ำหมุนเร็ว เครื่องหมาย ✓ ของ PRM อาจถูก OCR วางผิดคอลัมน์ (ควรครอบ Low Value และ/หรือ Free Stock Issue) ยังไม่ได้ตรวจกับ PDF ต้นฉบับ [confidence:: low]

## วิธีควบคุมตามประเภทสต็อกในนโยบายคลัง (SPO p.55-57)

ตัวอย่างนโยบายของอุตสาหกรรมหนักแห่งหนึ่ง: มูลค่าคงคลังมาตรฐานไม่เกิน **3% ของเงินลงทุนสร้างโรงงาน** และคณะกรรมการควบคุมพัสดุกำหนดวิธีเติม (ROP, order qty, Max/Min) เทียบดัชนีใน [[Inventory Turnover and GPI Benchmarks]]

| ประเภทสต็อก | วิธีควบคุม |
|---|---|
| 6.1 Equipment spare: interchangeable (bearing, V-belt, oil seal, O-ring) หมุนเร็ว/ปานกลาง | สถิติ: EOQ/ROP หรือ Hi/Low limit; รวมเก็บที่เดียว ดู [[Parts Interchangeability]] |
| 6.1 interchangeable หมุนช้า และ insurance | Min/Max ที่คณะกรรมการอนุมัติ |
| 6.1 อะไหล่สึกเร็วเฉพาะเครื่อง (สั่ง OEM) | Min/Max ที่คิด lead time |
| 6.1 อะไหล่ประกันราคาต่ำ / ราคาสูง | คุมแบบอะไหล่สึกเร็ว / ผ่านคณะกรรมการ |
| 6.1 Instrument / Electrical / Electronic | Min/Max ที่ผู้ชำนาญแต่ละสาขาเสนอ |
| 6.2 General used (ท่อ fitting gasket ฉนวน bolt/nut) | standardize แล้ว forecast + EOQ/ROP; ซื้อน้อยแต่บ่อยด้วย Vendor Stocking / Blanket Order; ของไม่สำคัญหาง่าย (สี ท่อ PVC) ไม่สต็อก ซื้อใช้ลงค่าใช้จ่ายตรง |
| 6.3 เคมีงานซ่อมบำรุง นำเข้า | อัตราใช้รายเดือนย้อนหลัง 6 เดือน + safety level + ความต้องการช่วง lead time; สต็อกสูงสุด **3 เดือน** |
| 6.3 เคมี ซื้อในประเทศ | อัตราใช้ 6 เดือนล่าสุดคิดความต้องการทั้งปี แล้วทำ **Blanket Order ทั้งปี** |

ตารางนี้สอดคล้องกับตาราง p.110: ของหมุนเร็ว/ใช้ร่วม/ทั่วไปใช้วิธีคำนวณ ของเฉพาะเครื่องและ insurance ใช้ Min-Max (derived)

## เชื่อมโยงกับ compressor failure hierarchy

- อะไหล่สิ้นเปลืองใช้ร่วมของ compressor (O-ring, gasket, bearing, filter) อยู่กลุ่ม Common Used ใช้ ROP/EOQ หรือ High/Low ได้ ส่วนชิ้นเฉพาะเครื่องของ [[Reciprocating Compressor]] หรือ [[Centrifugal Compressor]] (rotor, diaphragm) เป็น Unique/Insurance ใช้ Min-Max หรือ Order Up-to (การตีความของ wiki ไม่ใช่ข้อมูลในหนังสือ)
- กับของวิกฤตราคาสูง แนวทางของ RBMM (Cost Ratio, Simulation) ใน [[Spare Part Criticality and Risk]] ละเอียดกว่า Min-Max แบบกำหนดเอง; ไม่มีข้อมูลเบิกจริงของ [[Compressor]] ใน sources

## ดูเพิ่ม

- [[Spare Parts Optimization Book]]
- [[EOQ and Reorder Point]]
- [[MRO Purchasing and Contracting]]
- [[MRO Material Classification]]
- [[Spare Parts Management]]
- [[Spare Part Demand Forecasting]]
- [[MRO Inventory Reduction Program]]
- [[SPO vs RBMM Spare Parts Approaches]]

## Triplets

- [[MRO Inventory Control Methods]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 9 (SPO p.101-110)
- [[MRO Inventory Control Methods]] [related_to:: [[EOQ and Reorder Point]]]
- [[MRO Inventory Control Methods]] [related_to:: [[MRO Purchasing and Contracting]]]
- Inventory Control [depends_on:: When to Order] and how much to order (SPO p.102)
- ROP/EOQ [is_a:: Inventory Control Method] one of 6 (SPO p.103)
- High/Low Limit [is_a:: Inventory Control Method] (SPO p.103)
- Min-Max [is_a:: Inventory Control Method] manually set (SPO p.103)
- Periodic Review [is_a:: Inventory Control Method] (SPO p.103)
- Order Up-to [is_a:: Inventory Control Method] (SPO p.103)
- Order as Required [is_a:: Inventory Control Method] (SPO p.103)
- EOQ [has_formula:: sqrt( 2 x A x CO / (C x I) )] SPO notation (SPO p.104)
- EOQ [has_parameter:: CO] cost of one order line, about 90-120 baht in Thailand (SPO p.104)
- EOQ [has_parameter:: I] Investment Factor, holding cost as fraction of stock value per year (SPO p.104)
- EOQ [has_parameter:: C] unit price (SPO p.104)
- C x I [maps_to:: Ch] RBMM holding cost per unit, derived
- CO [maps_to:: Cp] RBMM purchasing cost per order, derived
- Cost of Possession [has_part:: Return on Investment] also insurance, warehouse rent, handling, administration, obsolescence, loss; 7 items (SPO p.104)
- Cost of Possession [input_to:: I] (SPO p.104)
- EOQ [applies_to:: Fast Moving] needs usage statistics; general, chemicals, consumables, common parts (SPO p.105)
- Reorder Point [has_formula:: (D x LT) + SS] (SPO p.105)
- Safety Stock [has_formula:: percent of D x LT] lead-time deviation % + usage deviation %, rule of thumb (SPO p.105)
- Safety Stock [differs_from:: z x sigma_combined] SPO percent rule vs RBMM statistical formula, not contested, general knowledge [confidence:: low]
- Reorder Point [has_value:: 48] D 20, LT 2 months, SS 20% = 8 (SPO p.105)
- Reorder Point [maps_to:: Min-Max] Mid = ROP = 48, Min = SS = 8, order quantity = EOQ (SPO p.105-106)
- High Limit [has_formula:: D x Stockage Objective] (SPO p.106)
- Low Limit [alias_of:: Reorder Point] (SPO p.106)
- High/Low Limit [uses:: Stockage Objective] US military, Busanda (SPO p.106)
- High/Low Limit [has_formula:: High Limit - On Hand] order quantity (SPO p.107)
- High Limit [has_value:: 120 cylinders] oxygen, D 40 per month, 3 months (SPO p.107)
- Low Limit [has_value:: 22 cylinders] oxygen, LT 0.5 month, SS 10% = 2 (SPO p.107)
- High/Low Limit [has_value:: 98 or 110] order when on hand 22 or 10 (SPO p.107)
- Min-Max [applies_to:: Very Slow Moving] low quantities; error-prone for thousands of items (SPO p.107)
- Periodic Review [has_formula:: M - (OH + QOD)] (SPO p.108-109)
- Periodic Review [has_parameter:: R] review time; also M maximum quantity (SPO p.108)
- Periodic Review [has_value:: 35 and 80] M 90; OH 25 + QOD 30; OH 10 (SPO p.108-109)
- Periodic Review [differs_from:: ROP/EOQ] fixed time and variable quantity vs variable time and fixed quantity (SPO p.108)
- Periodic Review [applies_to:: Free Stock Issue] low-price fast movers, supermarket style (SPO p.108-110)
- Order Up-to [has_value:: 5] return-bend example, 3 on hand + 2 on order (SPO p.109)
- Order Up-to [applies_to:: Insurance Part] (SPO p.109)
- Order as Required [has_value:: 0] normal stock, buy 20, issue 15 then 5 (SPO p.109-110)
- Order as Required [applies_to:: Planned Maintenance] project, turnaround, short lead time items (SPO p.110)
- Free Stock Issue [has_value:: 5-10 or 10-50 baht per unit] inconsistent thresholds in chapter 7 (SPO p.68, p.74)
- Method by Part Type Table [contradicts:: Periodic Review] Low Value column empty though PRM text says low-price items; possible OCR misplacement [confidence:: low]
- Min-Max [applies_to:: Unique Parts] also insurance standby and capitalized (SPO p.110)
- ROP/EOQ [applies_to:: Common Used Parts] also general used and chem-gas (SPO p.110)
- Warehouse Policy [has_value:: 3% of plant investment] maximum standard inventory value (SPO p.55-57)
- Interchangeable Parts [selects:: ROP/EOQ] fast/medium moving, or Hi/Low limit; slow and insurance use Min/Max (SPO p.55-57)
- Imported Maintenance Chemicals [has_value:: 3 months] maximum stock target (SPO p.55-57)
- Domestic Maintenance Chemicals [uses:: Blanket Order] annual, from last 6 months usage (SPO p.55-57)
- General Used Items [uses:: Blanket Order] also Vendor Stocking, forecast + EOQ/ROP (SPO p.55-57)

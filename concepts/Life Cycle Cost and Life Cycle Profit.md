---
title: Life Cycle Cost and Life Cycle Profit
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [mpm, lcc, cost, maintenance-management, book]
sources: [maintenance-profit-maker.md]
confidence: medium
contested: true
---

# Life Cycle Cost and Life Cycle Profit (LCC / LCR / LCP)

**Life Cycle Cost (LCC)** หรือ Total Life Cycle Cost / Cost of Ownership คือค่าใช้จ่ายทั้งหมดในการได้มาและครอบครองเครื่องจักรตลอดอายุ ค่าเสื่อมราคาในงบดุลเป็นเพียงส่วนหนึ่งของ LCC (MPM p.38) ส่วน **Life Cycle Profit (LCP)** คือช่วงห่างระหว่างรายได้ตลอดอายุ (**LCR, Life Cycle Revenue**) กับ LCC ซึ่งตอบภารกิจหลักของธุรกิจคือการทำกำไร (MPM p.44-45) หน้านี้สรุปบทที่ 2 ของ [[Maintenance Profit Maker Book]] จาก reading notes ใน [[raw/maintenance-profit-maker]] (paraphrase ไม่ใช่ข้อความต้นฉบับ) confidence medium เพราะสังเคราะห์จาก OCR notes และมีค่าที่คำนวณซ้ำ (derived)

มุมมอง LCC 5 กลุ่มของ CMRP และวงจรชีวิตตาม RBMM อยู่ที่ [[Asset Life Cycle]] หัวข้อ 1 และ 9 เครื่องมือคิดลดเงิน (PV, WACC, NPV) อยู่ที่ [[Engineering Economics and Time Value of Money]]

## 1. ต้นทุนถูกกำหนดตั้งแต่ช่วงต้น (ข้อขัดแย้ง MPM-C2)

ยิ่งเปลี่ยนแปลงช้า ความเสียหายยิ่งมาก หลังเริ่มใช้งานแล้ว การแก้ไขกระทบทั้งค่าใช้จ่ายตรงและรายได้ที่เสียจากการหยุดเครื่อง จึงต้องนำความรู้ด้านผลิตและซ่อมบำรุงเข้าไปใช้ในช่วง Feasibility ถึง Commissioning ให้มากที่สุด (MPM p.39)

ตัวเลข % ที่ถูกกำหนดไม่ตรงกันทั้งภายใน MPM และกับ RBMM:

| แหล่ง | Feasibility | Project | Engineering | EPC / Commissioning |
|---|---|---|---|---|
| MPM ข้อความ p.39 | 70% | 80% | 90% | ใกล้ 100% |
| MPM ข้อความ p.14 | - | - | 80% (ถึงจุดนี้กำหนดราคาได้แล้ว) | - |
| MPM ป้ายรูป 1.1 / 2.1 / 13.1 | 70% | 85% | 95% | 100% |
| RBMM Fig 1.1 (RBMM p.14) | ประมาณ 70% | - | 85% ถึง 95% | 100% |

- **ข้อขัดแย้ง MPM-C2**: ยังไม่ resolve เก็บทุกมุมมองไว้ (`contested: true`) รายละเอียดและการอภิปรายอยู่ที่ [[Asset Life Cycle]] หัวข้อ 1
- ข้อสังเกต (derived): ป้ายในรูปของ MPM ตรงกับ RBMM แต่ข้อความ p.39 ให้ Engineering 90% และ p.14 ให้ 80% ผู้แต่งชุดเดียวกันจึงไม่ได้เลือกค่าเดียว ใช้เป็นแนวโน้ม "ล็อกส่วนใหญ่ก่อนเริ่มก่อสร้าง" ไม่ใช่ตัวเลขแม่นยำ

## 2. LCC 3 ช่วงค่าใช้จ่าย (MPM p.39-41)

| ช่วง | รายการ | การบันทึกบัญชี |
|---|---|---|
| 1. Acquiring, Installation, Commissioning | บริหารโครงการ; ออกแบบวิศวกรรม (ฝั่งผู้ซื้อออกแบบระบบ/spec, ฝั่งผู้ผลิตรวมในราคาอุปกรณ์); จัดหา (ประกวดราคา สัญญา); ติดตั้ง; Commissioning & start-up; ตรวจรับและทดลองใช้ (พลังงานทดลอง วัสดุสิ้นเปลือง อบรม ผู้เชี่ยวชาญผู้ผลิต ค่าแรงคุมงาน เอกสาร) | รวมเป็นทรัพย์สินแล้วตัดจ่ายรายปี (Depreciation/Amortization) |
| 2. Operation & Maintenance | Operation: พลังงานต่อหน่วย วัสดุสิ้นเปลือง ค่าแรงเดินเครื่อง/อบรม กำจัดวัสดุส่วนเกิน ใบอนุญาต/license fee; Maintenance: ซ่อมตามวาระ ซ่อมเมื่อชำรุด ซ่อมใหญ่ อบรมช่าง (รวมอะไหล่ วัสดุ ค่าแรง) | ลงบัญชีต้นทุน |
| 3. Salvage value | ค่ากำจัดซาก (เกิดแน่นอน) และรายได้ขายซาก (ไม่แน่นอน) | ให้ปลอดภัย คิดว่าไม่มีรายได้ มีแต่รายจ่าย |

- ค่าใช้จ่ายก่อนออกแบบ (ศึกษาความคุ้มทุน ที่ปรึกษา) มักไม่นับเป็นของเครื่อง จึงคิดเป็นศูนย์ (MPM p.39)
- ค่าจัดหาคิดรายอุปกรณ์ได้เฉพาะบริษัทที่ใช้ Activity Based Costing (MPM p.40)
- เทียบ CMRP 5 กลุ่ม (Capital, Operational, Maintenance, Production and quality losses, Disposal) ใน [[Asset Life Cycle]] หัวข้อ 9: MPM ไม่มีกลุ่ม production losses ใน LCC แต่ย้ายไปอยู่ฝั่งรายได้ (LCR/Availability) ในหัวข้อ 5 (การจับคู่เป็นการตีความของ wiki)

## 3. ความไม่แน่นอนของข้อมูล LCC (MPM p.41-42)

- ในทางปฏิบัติ **มากกว่า 50% ของข้อมูลมาจากผู้ผลิต** ซึ่งพิสูจน์ยาก เช่น reliability factor ที่ผู้ขายอ้าง, ชั่วโมงหยุดเปลี่ยนชิ้นส่วนที่ไม่บอกฝีมือช่างและราคาอะไหล่, อายุใช้งานที่มักไม่เป็นตามอ้าง; พลังงาน/วัสดุสิ้นเปลืองพอเทียบได้ในวันตรวจรับ
- หลักการ: ใช้เฉพาะหลักฐานที่พิสูจน์ได้ และเลือกเฉพาะประเด็นที่มีนัยสำคัญ (MPM p.44)
- ช่วงใช้งานยาวที่สุด (มากกว่า 90% ของวงจรอายุ) และเป็นตัวตัดสินการคืนทุน; เครื่องรุ่นเดียวกันที่ติดตั้งไม่ถูกต้องแต่แรกมีแนวโน้มเสียมากกว่า (MPM p.42)

## 4. ตัวอย่าง LCC 3 เครื่อง ที่ WACC 6% (MPM p.42-43)

หน่วย: พันบาท ค่าใช้จ่ายอะไหล่/ค่าแรงตามจำนวนผลิตสะสม (10,000 ถึง 1,200,000 ชิ้น) งานซ่อมทั้งหมดเป็นแบบตามการใช้งาน (usage-based) และผู้ขายรับประกันค่าแรงช่วงแรกต่างกัน (เครื่อง 1 ถึงช่วง 200,000 ชิ้น, เครื่อง 2 และ 3 ถึง 300,000 ชิ้น) ตารางรายช่วงเต็มอยู่ใน `raw/maintenance-profit-maker/ch01-03.md`

| | Equipment 1 | Equipment 2 | Equipment 3 |
|---|---|---|---|
| ราคาซื้อ | 17,500 | 12,500 | 13,500 |
| PV อะไหล่ (รวมราคาซื้อ) ตามหนังสือ | 26,578 | 33,988 | 41,041 |
| PV ค่าแรง | 3,041 | 3,976 | 3,663 |
| **รวม PV ตามหนังสือ** | **29,619** | **37,964** | **44,703** |
| PV อะไหล่ (derived) | **26,390** | 33,988 | 41,041 |
| **รวม PV (derived)** | **29,431** | 37,964 | 44,703 |

- **การตรวจซ้ำ (derived)**: ตีความว่าแต่ละแถวผลิต = 1 ปี (แถว 10,000 = ปีที่ 1, 100,000 = ปีที่ 3) คิดลด 6% แล้วบวกราคาซื้อที่ปี 0 ได้ PV ตรงกับหนังสือทุกช่องของเครื่อง 2, 3 และค่าแรงทุกเครื่อง แต่ PV อะไหล่เครื่อง 1 ได้ 26,390 ไม่ใช่ 26,578 (ต่าง 188) รวมเป็น 29,431 แทน 29,619 น่าจะมีช่องอะไหล่เครื่อง 1 พิมพ์/OCR ผิดอย่างน้อยหนึ่งช่อง **ลำดับผลไม่เปลี่ยน** การตีความ "1 แถว = 1 ปี" เป็นของผู้บันทึก หนังสือไม่ได้ระบุคาบคิดลด
- ผล: เครื่อง 1 ราคาซื้อสูงสุดแต่ PV รวมต่ำสุด; เครื่อง 2 ราคาซื้อต่ำสุด รวมปานกลาง; เครื่อง 3 รวมแพงสุด ซื้อของถูกจึงไม่ใช่ของถูกตลอดอายุ
- แม้รวมข้อมูลครบก็ **ยังตัดสินว่าควรซื้อเครื่อง 1 ไม่ได้** เพราะยังไม่รวม (1) ค่าซ่อมเมื่อเสีย (Fault Recovery) ซึ่งขึ้นกับ reliability และ MTTR ที่กระทบ OEE (2) ค่าใช้จ่ายของกลุ่มงานอื่นที่ต้องใช้เพื่อคง OEE (3) ค่าใช้จ่ายทางอ้อมในอนาคต (4) พลังงานต่อหน่วยผลิตและอื่น ๆ (MPM p.43) ดู [[Availability and OEE]]

## 5. LCR และ LCP (รูปที่ 2.2, MPM p.44-45)

```
LCP = LCR - LCC
LCC = ค่าเสื่อมราคาตลอดอายุ + ค่าผลิต + ค่าบำรุงรักษา + ค่าใช้จ่ายทางอ้อมอื่น
LCR ขึ้นกับ Availability ที่ทำได้จริง เทียบกับเป้าหมายและ 100% Availability
```

- การเลือกด้วย LCC เป็นการประเมินด้านค่าใช้จ่ายอย่างเดียว ดีกว่าซื้อของถูก แต่ทิ้ง LCR ไป
- LCC และ LCP ให้ผลทางเศรษฐศาสตร์ไม่ต่างกัน ต่างแค่มุมมอง

### ใช้หลักไหนเมื่อไร (MPM p.45)

| ใช้ LCC เมื่อ | ใช้ LCP เมื่อ |
|---|---|
| ตลาดค่อนข้างนิ่ง ข้อกำหนดทำนายได้ | ตลาดเปลี่ยนแปลง ข้อกำหนดทำนายยาก |
| หน้าที่เครื่องไม่เปลี่ยน; ดัชนี MWT, Capacity/Operating Availability, MTBF, MTTR | หน้าที่และกำลังผลิตเปลี่ยนได้; MTBF |
| Internal Efficiency, Cost Focus | External Efficiency (การตอบสนอง), Revenue Focus |

- LCC อยู่บนสมมติฐานข้อกำหนดคงที่ มุ่งลดค่าใช้จ่าย เลือกเครื่อง availability สูง; ตลาดที่เทคโนโลยีเปลี่ยนเร็ว LCP เหมาะกว่า (หนังสือเขียน TWT ในข้อความแต่ MWT ในตาราง น่าจะเป็นตัวเดียวกัน = Mean Wait Time ดู [[Maintenance Time Definitions]])
- รายละเอียดวิธีคำนวณ LCP ผู้เขียนเลื่อนไปโอกาสต่อไป (ไม่มีใน sources)

## 6. ข้อจำกัด (MPM p.46)

- LCC/LCP ควรใช้เป็น **แนวทางคิด** เท่านั้น โดยเฉพาะเครื่องอายุ 20-25 ปี ที่ทำนายเทคโนโลยี ตลาด ต้นทุน หรือการเลิกกิจการของผู้ผลิตไม่ได้
- การตัดสินใจลงทุนคาบยาวที่ไม่แน่นอนสูงอาจต้องใช้เกณฑ์อื่นที่เสี่ยงน้อยและคาบสั้น (เช่น payback ใน [[Engineering Economics and Time Value of Money]]); LCC/LCP ไม่ใช่ข้อยุติ
- ใช้ร่วมกับ business case ที่ [[Maintenance Business Case]]

## เชื่อมโยงกับ compressor failure hierarchy

การตีความของ wiki (ไม่ใช่เนื้อหาในหนังสือ ซึ่งไม่ได้พูดถึง compressor):
- เมื่อเทียบ LCC ของ [[Compressor]] หลายรุ่น ข้อมูล reliability ที่ผู้ขายอ้างควรตรวจกับข้อมูลอิสระ เช่น % failure mode ของ [[OREDA]] ต่อ [[Maintainable Item]] ตามหลัก "ใช้เฉพาะข้อมูลที่พิสูจน์ได้" (MPM p.41-42)
- ค่าอะไหล่ usage-based ในตัวอย่างหัวข้อ 4 เทียบได้กับงาน overhaul ตามชั่วโมงเดินของ [[Reciprocating Compressor]] (valve, ring, packing) ส่วนค่าเสียหายจากการหยุด (ข้อ 1 ที่หนังสือว่ายังไม่รวม) ขึ้นกับ failure mode ที่ทำให้หยุดเครื่อง

## ดูเพิ่ม

- [[Asset Life Cycle]]
- [[Engineering Economics and Time Value of Money]]
- [[Maintenance Business Case]]
- [[Availability and OEE]]
- [[Maintenance Cost Structure]]
- [[Maintenance Profit Maker Book]]

## Triplets

- [[Life Cycle Cost and Life Cycle Profit]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 2 (MPM p.37-46)
- Life Cycle Cost [alias_of:: Total Cost of Ownership] (MPM p.38)
- Depreciation [part_of:: Life Cycle Cost] only part of total LCC (MPM p.38)
- Life Cycle Cost [has_part:: Acquiring Installation Commissioning Cost] phase 1, capitalised then depreciated (MPM p.39-40)
- Life Cycle Cost [has_part:: Operation and Maintenance Cost] phase 2, booked as cost (MPM p.40-41)
- Life Cycle Cost [has_part:: Salvage Value] phase 3, assume disposal cost only, no revenue (MPM p.41)
- Procurement Cost Per Equipment [depends_on:: Activity Based Costing] (MPM p.40)
- Life Cycle Cost [depends_on:: Vendor Data] more than 50% of data from manufacturer, hard to prove (MPM p.41-42)
- Operation Phase [has_value:: more than 90%] of life cycle, decides payback (MPM p.42)
- LCC Example [has_value:: WACC 6%] three machines, usage-based maintenance (MPM p.42-43)
- LCC Example Equipment 1 [has_value:: 29,619 thousand baht] total PV as printed; purchase 17,500 (MPM p.42-43)
- LCC Example Equipment 1 [has_value:: 29,431 thousand baht] total PV recomputed, spares PV 26,390 not 26,578, derived [confidence:: low]
- LCC Example Equipment 2 [has_value:: 37,964 thousand baht] total PV; purchase 12,500 (MPM p.42-43)
- LCC Example Equipment 3 [has_value:: 44,703 thousand baht] total PV; purchase 13,500 (MPM p.42-43)
- LCC Example Equipment 1 [differs_from:: LCC Example Equipment 3] highest purchase price but lowest total PV (MPM p.43)
- Life Cycle Profit [has_formula:: LCR - LCC] (MPM p.44-45)
- Life Cycle Revenue [depends_on:: [[Availability and OEE]]] actual vs target vs 100% availability (Fig 2.2, MPM p.44)
- Life Cycle Cost [applies_to:: Stable Market] predictable requirements, cost focus, MWT MTBF MTTR (MPM p.45)
- Life Cycle Profit [applies_to:: Changing Market] unpredictable requirements, revenue focus (MPM p.45)
- Life Cycle Cost [differs_from:: Life Cycle Profit] same economics, different viewpoint (MPM p.45)
- Life Cycle Cost [related_to:: [[Engineering Economics and Time Value of Money]]] PV discounting at WACC
- MPM Text Cost Locked at Engineering [has_value:: 90%] Feasibility 70, Project 80, EPC near 100 (MPM p.39) [contested:: true]
- MPM Text Cost Locked at Engineering [contradicts:: RBMM Cost Locked at Engineering Design] MPM-C2 [contested:: true]
- RBMM Cost Locked at Engineering Design [has_value:: 85% to 95%] (RBMM Fig 1.1 p.14); MPM figure labels 70/85/95/100 agree [contested:: true]
- RBMM Cost Locked at Engineering Design [contradicts:: MPM Text Cost Locked at Engineering] MPM-C2; MPM p.14 also says 80% [contested:: true]
- Compressor LCC Vendor Data [related_to:: [[OREDA]]] check vendor reliability claims against independent data, interpretation [confidence:: low]

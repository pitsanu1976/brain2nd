---
title: Spare Parts Optimization Book
created: 2026-10-27
updated: 2026-10-27
type: entity
tags: [spo, book, spare-parts, maintenance-management, warehousing, procurement, inventory-control]
sources: [spare-parts-optimization.md, reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Spare Parts Optimization (SPO) — หนังสือ

hub ของหนังสือ "Spare Parts Optimization: การจัดการอะไหล่ให้เพิ่มผลผลิต (ฉบับปรับปรุง)" ที่ ingest เข้า wiki เมื่อ 2026-10-27 หนังสือมองการบริหารอะไหล่จาก **ฝั่งคลังพัสดุและจัดซื้อ (MRO materials management)** ต่างจาก [[Reliability Based Maintenance Management Book]] ที่มองจาก reliability และความเสี่ยง หน้านี้บอกว่าแต่ละบทไปอยู่หน้าไหนใน wiki, รวมข้อผิดพลาดของหนังสือ/OCR และอธิบายความสัมพันธ์กับ RBMM และ [[CMRP Course]] ข้อความทั้งหมดถอดความจาก reading notes ไม่ใช่ข้อความต้นฉบับ

## ข้อมูลบรรณานุกรม

- ชื่อ: Spare Parts Optimization: การจัดการอะไหล่ให้เพิ่มผลผลิต (ฉบับปรับปรุง)
- ผู้แต่ง: เรือเอก สุชาติ ศุภมงคล
- สำนักพิมพ์: SE-Education (SE-ED), พ.ศ. 2546 (2003), ISBN 974-584-871-6, ชุด Industrial Management & Technical Series; บรรณานุกรมหอสมุดแห่งชาติระบุ 144 หน้า หัวเรื่อง "การจัดการวัสดุ" เลขหมู่ 658.7 (SPO p.4)
- 12 บท ครอบคลุมการเก็บรักษา การบริหารเครื่องมือ การจัดซื้อ และการควบคุมระดับคงเหลือของวัสดุประเภท MRO (SPO p.5-6)
- raw: [[raw/spare-parts-optimization]] และ reading notes ต่อบทใน `raw/spare-parts-optimization/` ไฟล์ OCR ทั้งเล่มเก็บในเครื่องเท่านั้น (gitignored) เพราะมีลิขสิทธิ์
- การอ้างอิง: `(SPO p.NN)` ด้วยเลขหน้าที่พิมพ์ในหนังสือ (book page) ไม่ใช่ PDF page

### ประวัติผู้เขียน (เฉพาะด้านวิชาชีพ)

นายทหารพลาธิการกองทัพเรือ ผ่านหลักสูตร Supply Officer ของ US Naval Supply Corps School ต่อมาเป็นผู้จัดการคลังพัสดุโรงกลั่น Esso ศรีราชา และทำงานคลัง/จัดซื้อในบริษัทเอกชนหลายแห่ง (รวมบางจาก) และเขียนตำราการบริหารวัสดุและการจัดซื้อให้ มสธ. (SPO p.5-6, p.147)

## มุมมองและที่มาของแนวคิด

- **COSAL (Coordinated Shipboard Allowance List)** ของกองทัพเรือสหรัฐ: คู่มือกำหนดว่าเรือแต่ละลำควรสต็อกอะไหล่อะไร ผู้เขียนเปรียบว่าเรือรบที่เครื่องเสียกลางทะเลโดยไม่มีอะไหล่ก็หมดสภาพพร้อมรบ เหมือนโรงงานที่ต้องหยุดผลิต (SPO p.5-6)
- **Esso Engineering Basic Practice & Spare Parts Optimization**: คู่มือของโรงกลั่น Esso ที่ให้แนวทางสต็อกแบบเดียวกับ COSAL และเป็นที่มาของตาราง spare % ต่ออุปกรณ์ในบทที่ 5 (SPO p.5-6)
- บรรณานุกรมท้ายเล่มมี 5 รายการ: เอกสาร US Navy Supply Corps School, Storehouse Manual และ Spare Parts Procedures and Control ของ Esso, Instructions for Spare Parts Recommendation ของ Chiyoda และ Recommendation on Spare Parts Stock System ของ Mitsubishi Oil (SPO p.146)
- ปัญหาร่วมที่ผู้เขียนชี้: ฝ่ายจัดซื้อต้องการผู้ซื้อที่มีความรู้ช่าง ขณะที่ช่างไม่เข้าใจบัญชีการเงิน (SPO p.5-6) หนังสือจึงเน้นบัญชีวัสดุ การเขียนใบขอซื้อ และ KPI ของคลัง มากกว่าโมเดลสถิติ

## แผนที่บท -> หน้า wiki

| บท | Book pages | หัวข้อหลัก | หน้าใน wiki |
|---|---|---|---|
| ส่วนนำ | 1-10 | บรรณานุกรม คำนำ สารบัญ | หน้านี้ |
| 1 | 11-17 | วัสดุ 4 ประเภทสากล, ประเภทโรงงาน, การบันทึกบัญชีวัสดุ | [[MRO Material Classification]] |
| 2 | 19-23 | หน้าที่ 7 ข้อและหัวข้อความรับผิดชอบ 20 ข้อของหัวหน้าคลัง | หน้านี้ (สรุปด้านล่าง), [[Warehouse Design and Storage]], [[Tool Crib and Warehouse Security]] |
| 3 | 25-31 | MRO 9 กลุ่ม, OAR, capitalized parts, commissioning spares | [[MRO Material Classification]], [[Parts Interchangeability]] |
| 4 | 33-38 | dependent/independent demand, แผน MR/MS สำหรับซ่อมใหญ่ | [[MRO Material Classification]], [[Turnaround Management]], [[MRO Purchasing and Contracting]] |
| 5 | 39-58 | Engineering Basic Practice (spare % ต่ออุปกรณ์), นโยบายคลัง 3 ประเภท | [[Spare Parts Recommendation by Equipment Type]], [[MRO Material Classification]] |
| 6 | 59-62 | Parts Interchangeable Book | [[Parts Interchangeability]] |
| 7 | 63-83 | ขนาด รูปแบบ ผัง และการเก็บรักษาในคลัง | [[Warehouse Design and Storage]] |
| 8 | 85-100 | ใบขอซื้อ, Blanket Order, System Contract, Consignment, Vendor Stocking, Outsourcing, air freight, claims | [[MRO Purchasing and Contracting]] |
| 9 | 101-110 | วิธีควบคุมการสั่ง 6 วิธี, ROP/EOQ, COP | [[MRO Inventory Control Methods]], [[EOQ and Reorder Point]] |
| 10 | 111-132 | Turnover, MOS/DOS, %GPI, ABC, โปรแกรมลดคงคลัง, MCC, ปัจจัย 7 ข้อ | [[Inventory Turnover and GPI Benchmarks]], [[MRO Inventory Reduction Program]], [[MRO Material Classification]] |
| 11 | 133-137 | คลังเครื่องมือ (tool room) | [[Tool Crib and Warehouse Security]] |
| 12 | 139-147 | ความมั่นคงในคลัง, บันทึกท้ายเล่ม, บรรณานุกรม | [[Tool Crib and Warehouse Security]], หน้านี้ |

### สรุปบทที่ 2 (ไม่มีหน้าแยก)

- หัวหน้าคลังรับผิดชอบรับ เก็บรักษา จ่าย และ **รักษาระดับคงคลัง**; ผู้เขียนเห็นว่าระดับคงคลังของวัสดุโรงงานควรอยู่กับคลัง ไม่ใช่ฝ่ายบัญชี และอาจตั้งคณะกรรมการบริหารวัสดุช่วย (SPO p.20)
- งานหลัก 7 ข้อ: รักษาระดับคงคลัง (regular stock และ custody control sub stock ของซื้อตรง/โครงการ), รับ-จ่ายผ่านจุดรับเดียว, เก็บรักษาและป้องกัน, บันทึกและควบคุม, กำจัดของล้าสมัย, กำจัดของเสีย/หมดอายุ, รักษาระดับคงคลังให้ต่ำเชิงเศรษฐศาสตร์ (SPO p.20-22)
- หัวข้อความรับผิดชอบ 20 ข้อ (ใช้เขียน job description / QJA) รวมถึงทำรายการอะไหล่ใช้ร่วม, ร่วมทำ Blanket Order, บริหาร tool room, cycle count และรายงาน Stock Status / Stock Movement / Reorder / On Order (SPO p.22-23)

### หมายเหตุเลขหน้า (PDF vs book)

PDF สแกน 143 หน้าขาดหน้าว่างหลังปกบท offset จึงเพิ่มเป็นช่วง: ส่วนนำและบทที่ 1 = PDF+1, บทที่ 2 = +2, บทที่ 3 = +3, บทที่ 4-7 = +4, บทที่ 8-11 = +5, ตั้งแต่ PDF p133 (บทที่ 12) = +6 ช่วงสุดท้ายเป็นการอนุมานจาก running header ([[raw/spare-parts-optimization]])

## บันทึกท้ายเล่ม (SPO p.143-145)

- ผู้เขียนชี้ว่าบทที่ 9-10 เป็นหัวใจของเล่ม และบทที่ 1 (บัญชีวัสดุ) กับบทที่ 8 (ใบขอซื้อที่ผู้ซื้อเข้าใจ, "จัดซื้อเชิงรุก") สำคัญรองลงมา
- **COP (Cost of Possession) = Carrying Cost** คำนวณจากค่าใช้จ่าย 7 ชนิด แม่นกว่าใช้อัตราดอกเบี้ยตรง ๆ และเป็นตัวแปรในสูตร EOQ ดู [[MRO Inventory Control Methods]]
- อัตราหมุนเวียนแบบสินค้าสำเร็จรูปไม่เหมาะกับวัสดุโรงงานที่หมุนช้าและไม่แน่นอน แนวคิด Esso จึงวัด MRO inventory เป็น **% ของ Gross Plant Investment (GPI)** จากข้อมูลทุก 6 เดือนเป็นเวลา 3 ปีจากโรงงานทั่วโลก (โครงการ optimization ปี 1978-1980 ที่ผู้เขียนร่วมด้วย)
- ข้อเสนอสำหรับโรงงานไทย: โรงงานที่เครื่องจักรเป็นหลักใช้ benchmark **3-4% ของ GPI**; เครื่องจักรไม่ซับซ้อน (เช่น จักรเย็บผ้า) ราว **1-1.5%** รายละเอียดและตัวเลขที่ต่างกันในแต่ละบทอยู่ที่ [[Inventory Turnover and GPI Benchmarks]]

## ข้อผิดพลาดของหนังสือ / OCR (รวมทุกบท)

เป็นข้อผิดภายในหนังสือหรือ OCR ไม่ใช่ความขัดแย้งกับ RBMM หรือ CMRP จึงไม่ตั้ง contested ค่าที่ถูกส่วนใหญ่ derived (คำนวณใหม่ใน reading notes) รายละเอียดอยู่ในหน้าปลายทาง

| บท (หน้า) | หนังสือ/OCR เขียน | ค่าที่ถูก / หมายเหตุ | หน้า wiki |
|---|---|---|---|
| ส่วนนำ (p.1, p.4) | ปก OCR ผิด; บรรณานุกรมว่า 144 หน้า | ชื่อที่ถูก "การจัดการอะไหล่ให้เพิ่มผลผลิต"; PDF มี 143 หน้าเพราะขาดหน้าว่าง | หน้านี้ |
| 1 (p.15) | ตาราง 1.2 Made to Order/วัตถุดิบ "ระดับคงเหลือใกล้สูง" | ขัดกับ safety stock ต่ำ น่าจะเป็น "ต่ำ" หรือ OCR ผิด | [[MRO Material Classification]] |
| 2 (p.20) | MMC แปลเป็น "Material Central Committee" | อักษรย่อไม่ตรง น่าจะ Materials Management Committee | หน้านี้ |
| 3 (p.27) | interchangeable parts อ้าง "บทที่ 9" | เนื้อหาอยู่บทที่ 6; การอ้างข้ามบทอื่นใช้ชื่อบทไม่ตรงสารบัญ | [[Parts Interchangeability]] |
| 3 (p.27-28) | เกณฑ์ OAR ข้อ 4 ให้อะไหล่ราคาแพงลักษณะสินทรัพย์ถาวรเป็น OAR ได้ | ดูขัดกับหัวข้อ capitalized parts ที่ต้องสต็อก; น่าจะหมายถึงชิ้นที่วางแผนซ่อมล่วงหน้าได้ | [[MRO Material Classification]] |
| 4 (p.36-37) | ETD = "Estimate Time Delivery"; Brick ETD 20/7 แต่ ETA 2/7; Oil Gun ไม่มีทั้งในคลังและ PR/PO | ETD สากล = Estimated Time of Departure; วันที่ขัดกัน; Oil Gun ควรต้องจัดซื้อ | หน้านี้ |
| 4 (p.33) | ชื่อบท "...สำหรับงานโครงการ" | เนื้อหาเป็นแผนซ่อมใหญ่/turnaround | หน้านี้ |
| 5 (p.45) | Table 2 แถว spring housing gasket: 6 ชุด = 2 แต่ ≥7 = 20% | 7 x 20% = 1.4 ไม่ต่อเนื่องแบบแถวอื่น | [[Spare Parts Recommendation by Equipment Type]] |
| 5 (p.51, p.53) | coupling ของ centrifugal compressor และ blower "1%" | น่าจะหมายถึง 1 ชุดต่อชนิด/ขนาด | [[Spare Parts Recommendation by Equipment Type]] |
| 5 (p.53) | "Valve seal or guard gasket" | น่าจะเป็น valve seat or guard gasket | [[Spare Parts Recommendation by Equipment Type]] |
| 5 (p.45-54) | ตัวอย่างแบบญี่ปุ่นไม่บอกฐานของ % | สันนิษฐานว่าเทียบกับจำนวนชิ้นที่ติดตั้ง | [[Spare Parts Recommendation by Equipment Type]] |
| 6 (p.61) | ตาราง Wear Rings: code 322-26-835 อยู่แถว "Shell Head", 322-26-817 ซ้ำสองแถว, จำนวน used 212/188 | OCR ตารางเพี้ยน เชื่อถือไม่ได้ | [[Parts Interchangeability]] |
| 7 (p.68, p.74) | เกณฑ์ราคา Free Issue ≤5-10 บาท กับ 10-20 ถึง ≤50 บาท | ไม่สอดคล้องกันภายในบท | [[Warehouse Design and Storage]] |
| 7 (p.66, p.69) | แปลงหน่วย 18 ft = 5.6 m ฯลฯ; bay "5 x 5 ตารางเมตร" | 18 ft = 5.49 m; bay ควรเป็น 5x5 m (25 m²) | [[Warehouse Design and Storage]] |
| 7 (p.79-80) | "หลีกเลี่ยงวางพัสดุหนักบนพัสดุที่มีน้ำหนักมาก"; push back rack อธิบายปนกับ flow rack | ความหมายขัดกัน; push back เป็น LIFO (ความรู้ทั่วไป) | [[Warehouse Design and Storage]] |
| 8 (p.88) | ตัวอย่าง flange "ถูก" ระบุ 150 psi | Class 150 เป็น pressure class ไม่ใช่ 150 psi (ความรู้ทั่วไป) | [[MRO Purchasing and Contracting]] |
| 8 (p.86, p.90) | บทนำว่าเทคนิค 3 กลุ่ม แต่หัวข้อแจก 4 รูปแบบ | แยก Consignment กับ Vendor Stocking | [[MRO Purchasing and Contracting]] |
| 9 (p.110) | ตารางสรุปคอลัมน์ Low Value ว่างทุกแถว | Periodic Review อาจควรอยู่คอลัมน์ Low Value (OCR วาง ✓ ผิด, ไม่แน่ใจ) | [[MRO Inventory Control Methods]] |
| 9 (p.108) | Periodic Review "มียอดจุดสั่งซื้ออยู่ตลอดเวลา" | ขัดกับหลัก fixed review cycle | [[MRO Inventory Control Methods]] |
| 10 (p.111) | ปกบท "การจัดหาอะไหล่ให้พึ่งพาตนเอง" | หัวเรื่องในเนื้อหา "การจัดการอะไหล่ให้เพิ่มผลผลิต" | หน้านี้ |
| 10 (p.115) | รูป 10.1 B = 50% รายการ/15% มูลค่า, C = 30%/5% | ต่างจากแบบแผนพาเรโตทั่วไป ตัวอย่างรูป 10.2 เองได้ 30/30/40 | [[MRO Inventory Reduction Program]] |
| 10 (p.117) | กลุ่ม B "เท่ากับ 95% ของรายการทั้งหมด" | ควรเป็น 95% ของมูลค่าสะสม | [[MRO Inventory Reduction Program]] |
| 10 (p.113) | Retail: 1.4 เดือน, 11.16% | turnover 9 ได้ 1.33 เดือน และ 11.11% | [[Inventory Turnover and GPI Benchmarks]] |
| 10 (p.118) | กรณี ABC สหรัฐฯ turnover 13 รอบ = 20 วัน | 365/13 ≈ 28 วัน | [[MRO Inventory Reduction Program]] |
| 10 (p.122) | แถว MRO ควรมี 22.95, ลดได้ 23.05 (รวม 48.95/57.05) | คิดตรง 46 x 15/30 = 23.00 (รวม 49.00/57.00) หนังสือปัด 1.53 ก่อน | [[MRO Inventory Reduction Program]] |
| 10 (p.125) | ตาราง DOS item 3 = (22,000), สุทธิ 47,000 | (9-7) x 75 x 150 = (22,500), สุทธิ 47,500 | [[MRO Inventory Reduction Program]] |
| 10 (p.126) | %GPI เดือน Dec = 3.58 | 49.8/1250 = 3.98% | [[Inventory Turnover and GPI Benchmarks]] |
| 11-12 (p.138-139) | เลขหน้าบทที่ 12 | offset +6 เป็นการอนุมาน (หน้าว่าง p.138 หายจาก PDF) | หน้านี้ |

ข้อสังเกตอื่น: OCR สะกดผิดหลายจุด (เช่น "Digister" หน้าชื่อปั๊ม Chesterton, "Motors, Recording", "Hight Limi") ไม่กระทบเนื้อหา; ตัวอย่างที่ตรวจเลขแล้วถูก เช่น งบดุลรูป 1.1 (800 = 800), ตัวอย่าง ROP/PRM ในบทที่ 9, ตาราง Turnover Months และตารางลดสต็อกกลุ่ม A ในบทที่ 10

## ความสัมพันธ์กับ RBMM / CMRP

- SPO (2546) มองจากคลังและจัดซื้อ: จัดกลุ่มวัสดุ, กฎหัวแม่มือ spare % ต่ออุปกรณ์, KPI แบบ %GPI และ ABC; RBMM มองจาก reliability: แยกอะไหล่ตามประเภทงาน (planned vs unplanned) และตั้ง Max/Min ด้วย cost ratio / ความเสี่ยง ([[Spare Parts Management]], [[Spare Part Criticality and Risk]]) การเปรียบเทียบเต็มอยู่ที่ [[SPO vs RBMM Spare Parts Approaches]]
- จุดที่เห็นตรงกัน: commissioning spares เป็นความรับผิดชอบของผู้รับเหมา/EPC ไม่ใช่สต็อกบำรุงรักษา (SPO p.30-31; RBMM p.15-16, p.235) ดู [[MRO Material Classification]] และ [[Asset Life Cycle]]
- [[CMRP Course]] มีหัวข้อ MRO inventory model และ risk-based spares (CMPR-08) ที่ทับซ้อนบางส่วนกับบทที่ 9-10 ของ SPO ดู [[EOQ and Reorder Point]]
- ตัวเลข benchmark ของ SPO (%GPI) กับ RBMM (Spare Inventory / Plant Asset 1-3%) ใช้ฐานคล้ายกันแต่นิยามไม่ตรงกัน รายละเอียดที่ [[Inventory Turnover and GPI Benchmarks]] และ [[Maintenance KPIs]]

## เชื่อมโยงกับ compressor failure hierarchy

ส่วนนี้เป็นการตีความของ wiki: SPO ไม่ใช้ taxonomy ของ ISO 14224/OREDA และไม่มีข้อมูล failure rate แต่บทที่ 5 ให้ตาราง spare % สำหรับ centrifugal compressor unit (SPO p.50-52) และ reciprocating compressor unit (SPO p.52-53) ซึ่งจับคู่กับ sub unit ได้ เช่น ชิ้นส่วนวาล์ว/piston ring/rod packing กับ [[CPUN Compressor Unit]], seal และ seal oil กับ [[SHSS Shaft Seal System]], lube oil filter กับ [[LUBS Lubrication System]], coupling และ gear กับ [[PWTR Power Transmission]] การจับคู่และการเทียบกับ failure mode เด่นของ [[Reciprocating Compressor]] และ [[Centrifugal Compressor]] อยู่ที่ [[Spare Parts Recommendation by Equipment Type]] หลักการเครื่อง standby ของ SPO (insurance and standby parts) เชื่อมกับ [[Redundancy and Standby Systems]]

## ดูเพิ่ม

- [[Spare Parts Management]]
- [[Reliability Based Maintenance Management Book]]
- [[CMRP Course]]
- [[SPO vs RBMM Spare Parts Approaches]]
- [[Compressor]]

## Triplets

- SPO [alias_of:: [[Spare Parts Optimization Book]]] Spare Parts Optimization, SE-ED 2546
- [[Spare Parts Optimization Book]] [has_code:: ISBN 974-584-871-6] (SPO p.4)
- [[Spare Parts Optimization Book]] [has_value:: 12] chapters (SPO p.7-10)
- [[Spare Parts Optimization Book]] [has_value:: 144] pages per national library record; scanned PDF has 143 (SPO p.4)
- [[Spare Parts Optimization Book]] [has_category:: MRO materials management] stores and purchasing viewpoint
- [[Spare Parts Optimization Book]] [uses:: COSAL] Coordinated Shipboard Allowance List, US Navy (SPO p.5-6)
- [[Spare Parts Optimization Book]] [uses:: Esso Engineering Basic Practice] Esso Spare Parts Optimization (SPO p.5-6)
- [[Spare Parts Optimization Book]] [differs_from:: [[Reliability Based Maintenance Management Book]]] stores/purchasing view vs reliability and risk view
- [[Spare Parts Optimization Book]] [related_to:: [[CMRP Course]]] overlapping MRO inventory topics
- [[MRO Material Classification]] [defined_in:: [[Spare Parts Optimization Book]]] chapters 1, 3, 5, 10
- [[Parts Interchangeability]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 6
- [[Spare Parts Recommendation by Equipment Type]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 5
- [[Warehouse Design and Storage]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 7
- [[MRO Purchasing and Contracting]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 8
- [[MRO Inventory Control Methods]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 9
- [[Inventory Turnover and GPI Benchmarks]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 10 and afterword
- [[MRO Inventory Reduction Program]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 10
- [[Tool Crib and Warehouse Security]] [defined_in:: [[Spare Parts Optimization Book]]] chapters 11-12
- [[Turnaround Management]] [related_to:: [[Spare Parts Optimization Book]]] chapter 4 MR/MS plan
- Storehouse Head [has_value:: 7] main functions (SPO p.20-22)
- Storehouse Head [has_value:: 20] responsibility topics for job description / QJA (SPO p.22-23)
- Cost of Possession [alias_of:: Carrying Cost] 7 cost elements, EOQ input (SPO p.143-145)
- MRO Inventory Percent of GPI [defined_in:: [[Spare Parts Optimization Book]]] Esso concept, data every 6 months for 3 years, 1978-1980 project (SPO p.143-145)
- MRO Inventory Percent of GPI [has_value:: 3-4%] afterword benchmark, machinery-based Thai plants (SPO p.143-145)
- MRO Inventory Percent of GPI [has_value:: 1-1.5%] afterword benchmark, simple machinery (SPO p.143-145)
- Commissioning Spare Part [applies_to:: Contractor] SPO p.30-31 agrees with RBMM p.15-16, p.235
- Retail Months of Sale [has_value:: 1.33] derived 12/9; book prints 1.4 (SPO p.113)
- MRO Stock Reduction Example [has_value:: 23.00 million THB] derived 46 x 15/30; book prints 22.95 (SPO p.122)
- DOS Variance Example [has_value:: 47,500 THB] derived net reduction; book prints 47,000 (SPO p.125)
- GPI Report December [has_value:: 3.98%] derived 49.8/1250; book prints 3.58 (SPO p.126)
- Centrifugal Compressor Spares [related_to:: [[Centrifugal Compressor]]] spare % table (SPO p.50-52), interpretation
- Reciprocating Compressor Spares [related_to:: [[Reciprocating Compressor]]] spare % table (SPO p.52-53), interpretation

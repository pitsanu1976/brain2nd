---
title: MRO Material Classification
created: 2026-10-27
updated: 2026-10-27
type: concept
tags: [spo, book, spare-parts, inventory-control, maintenance-management, cost]
sources: [spare-parts-optimization.md, reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# MRO Material Classification

การจัดจำแนกวัสดุโรงงาน (MRO) ตาม [[Spare Parts Optimization Book]] เพื่อเลือกวิธีเก็บ จัดซื้อ และควบคุมระดับคงเหลือให้เหมาะกับแต่ละกลุ่ม หนังสือเริ่มจากนิยาม MRO และผลของประเภทโรงงาน แล้วแบ่งวัสดุโรงงานเป็น 9 กลุ่ม (บทที่ 3), ผูกกลุ่มกับชนิดความต้องการ (บทที่ 4), แบ่งพัสดุคลังเป็น 3 ประเภทในนโยบายคลัง (บทที่ 5) และให้ปัจจัย 7 ข้อสำหรับตัดสินว่าจะสต็อกรายการใด (บทที่ 10) ภาพรวมการบริหารอะไหล่ฝั่ง reliability อยู่ที่ [[Spare Parts Management]]

## นิยาม MRO (SPO p.12)

- พัสดุตามสากลมี 4 ประเภท: วัตถุดิบ (Raw Material), สินค้าสำเร็จรูป (Finished Goods), วัสดุหีบห่อ (Packaging Material) และ **MRO Items (Maintenance Repair and Operation)**
- หนังสือกล่าวเฉพาะประเภทที่ 4 ซึ่งรวมวัสดุซ่อมบำรุงเครื่องจักรและวัสดุใช้ประจำ (general hardware, office supplies, safety device) นิยามสั้น: **MRO คือวัสดุที่ไม่เป็นส่วนผสมของสินค้าสำเร็จรูป**
- หนังสือใช้คำว่า "วัสดุโรงงาน" แทน MRO และ "วัสดุคงเหลือ" สำหรับยอดคงคลังของวัสดุโรงงาน
- การบริหารพัสดุอยู่ใน inbound logistics ของ value chain (SPO p.12)

## ประเภทโรงงานกับการบริหารวัสดุ (SPO p.13-16)

ตารางที่ 1.1 ตามการใช้ทรัพยากร:

| ประเภท | ตัวอย่าง | การบริหารวัสดุโรงงาน |
|---|---|---|
| Capital Intensive (เครื่องจักรเป็นฐาน) | ปิโตรเคมี โรงแยกก๊าซ โรงไฟฟ้า โรงกลั่น | วัสดุมาก มูลค่าสูง ต้องบริหารพิถีพิถัน อาจมีปัญหาจัดซื้อ |
| Labour Intensive (แรงงานเป็นฐาน) | garment, ประกอบอิเล็กทรอนิกส์, รองเท้า | อะไหล่ไม่ซับซ้อน รายการน้อย มูลค่าต่ำ ไม่ค่อยมีปัญหาจัดซื้อ |

ตารางที่ 1.2 ตามวัตถุประสงค์การผลิต:

| ประเภท | วัตถุดิบ | วัสดุโรงงาน |
|---|---|---|
| Made to Order (pull) | dependent demand ใช้ MRP ได้, safety stock ต่ำ | independent demand (ปรับเป็นแปรตามได้บางส่วน) ต้องแบ่งประเภทอะไหล่และเลือกวิธีควบคุมอย่างเข้มงวด อาศัย engineering basic practice |
| Made to Stock (push) | independent demand ใช้การพยากรณ์และ safety stock | เหมือน Made to Order เพราะวัสดุโรงงานไม่ต่างตามประเภทการผลิต |

ข้อสังเกต: ช่อง Made to Order/วัตถุดิบ ในหนังสือเขียนว่าระดับคงเหลือ "ใกล้สูง" ซึ่งขัดกับ safety stock ต่ำ น่าจะเป็น "ต่ำ" หรือ OCR ผิด (SPO p.15) ส่วนสำคัญของตารางคือ **ความต้องการวัสดุโรงงานเป็น independent demand ไม่ว่าโรงงานจะผลิตแบบใด**

## การบันทึกบัญชีเมื่อซื้อวัสดุ (SPO p.16-17)

| ลักษณะ | บัญชี | ผลต่อค่าใช้จ่าย |
|---|---|---|
| Direct turnover (ซื้อแล้วใช้ทันที) | Expense account ตาม Cost Center (CC) + Character of Expense (CE) | ลงค่าใช้จ่ายทันที (ตัวอย่าง CC 1500 ฝ่ายผลิต, CE 333 ค่าซ่อม) |
| ซื้อเข้าสต็อก | Inventory account (แยกวัตถุดิบ/สินค้าสำเร็จรูป/วัสดุโรงงาน) | ไม่หักค่าเสื่อม ลงค่าใช้จ่ายเมื่อเบิก |
| สินทรัพย์ถาวร | Fixed asset account | หักค่าเสื่อมรายปี (เช่น 10%/ปี) เข้า CC ผู้ใช้ |

- หนังสือแนะนำให้วัสดุโรงงานเข้าสต็อกก่อน มิฉะนั้นค่าซ่อมเดือนที่ซื้อจะสูงผิดจริง และให้ระบุ CC+CE บน work order เพื่อบันทึกค่าใช้จ่ายเมื่องานเสร็จ (Just in Time Costing) (SPO p.17) เทียบ [[Job Order Costing]] และ [[Maintenance Cost Structure]]
- วัสดุคงเหลือเป็นสินทรัพย์หมุนเวียน ไม่มีค่าเสื่อม สอดคล้องกับ RBMM ที่ถืออะไหล่เป็น Current Asset (SPO p.12-13; RBMM p.16, p.70)

## วัสดุโรงงาน 9 กลุ่ม (SPO p.26-31)

| # | กลุ่ม | ลักษณะ/เกณฑ์ | การสต็อก |
|---|---|---|---|
| 1 | Unique Parts (อะไหล่เฉพาะเครื่อง) | ใช้ได้เฉพาะเครื่อง/รุ่น ต้องซื้อจาก OEM (ตัวอย่างปั๊ม Chesterton: rotating element $979, impeller $1,649) | รายการแรกที่ต้องพิจารณาเป็น regular item |
| 2 | Insurance and Standby Parts (อะไหล่ประกันเตรียมพร้อม) | อะไหล่ของเครื่อง standby และอะไหล่สำคัญที่ขาดแล้วโรงงานต้องหยุด | สต็อกประจำ; ใส่รหัสต่อท้าย เช่น **"S"** เพื่อเรียกดูกลุ่มนี้ได้ |
| 3 | Interchangeable Parts | ใช้ได้หลายเครื่อง มีผู้ผลิตหลายราย (bearing, V-belt) มี cross reference ข้ามยี่ห้อ | สต็อกประจำ รวมเก็บที่เดียว ดู [[Parts Interchangeability]] |
| 4 | Order as Required (OAR) | ซื้อเมื่อต้องการ | ไม่สร้างระดับสำรอง แม้ยอดเป็นศูนย์ |
| 5 | Capitalized Parts | อะไหล่มูลค่าสูงลักษณะสินทรัพย์ถาวร | สต็อกจำนวนหนึ่ง ลงบัญชีสินทรัพย์ถาวร |
| 6 | General Used Items | general hardware (ท่อ ฟิตติ้ง วาล์ว นอต หลอดไฟ ฟิวส์) และ consumable/supplies (ผ้าเช็ดเครื่อง ถุงมือ รองเท้าเซฟตี้) | fast/medium moving ใช้พยากรณ์ + reorder point |
| 7 | Chemical & Gas | เคมีงานซ่อม (chemical cleaning, solvent, water treatment) และก๊าซ (ออกซิเจน-อะเซทิลีน, ไนโตรเจน, ฟรีออน) ไม่รวมวัตถุดิบการผลิตและแล็บ | สต็อกมาตรฐาน; ถ้าจ้างผู้รับเหมาซ่อม ขึ้นกับสัญญา |
| 8 | Tools and Machine Tools | ส่วนใหญ่เป็นสินทรัพย์ถาวรเคลื่อนที่ได้ คุมแบบอารักขา; ราคาต่ำ (ต่ำกว่า 100 บาท เช่น ดอกสว่าน) ถือเป็นวัสดุสิ้นเปลือง | ดู [[Tool Crib and Warehouse Security]] |
| 9 | Commissioning Spares | อะไหล่ช่วง commissioning period ของผู้รับเหมา | ไม่ใช่สต็อกของเจ้าของงาน (ด้านล่าง) |

### Insurance and Standby Parts (SPO p.26-27)

- เครื่อง standby ติดตั้งคู่กับ major operating unit: หยุด A เดิน B แล้วซ่อม A จึงต้องมั่นใจว่ามีอะไหล่ และต้องสั่งของที่ใช้ไปเข้ามาแทน หน่วยสำคัญมากอาจมี standby ถึง 3 ชุด (A/B/C)
- เครื่องแบบเดียวกันมักเสียชิ้นเดิมซ้ำ จึงกำหนดรายการได้จากสถิติการเบิกเปลี่ยน
- อีกส่วนเลือกโดยวิศวกรซ่อมบำรุงร่วมกับวิศวกรฝ่ายผลิตจาก spare parts list ของเครื่อง ผู้ขายแนะนำได้แต่วิศวกรของเราตัดสิน
- ความต่างกับ RBMM: RBMM นิยาม Insurance Part ด้วยเกณฑ์ค่าขาดต่อครั้งเมื่อ cost ratio ต่ำกว่า 1 ([[Spare Part Criticality and Risk]]) ส่วน SPO นิยามจากบทบาทของอะไหล่ (เครื่อง standby / ขาดแล้วโรงงานหยุด) ไม่มีสูตร ทั้งสองเป็นมุมมองต่างกัน ไม่ใช่ข้อเท็จจริงขัดกัน (การตีความของ wiki) ดู [[Redundancy and Standby Systems]]

### เกณฑ์ OAR (SPO p.27-28, p.31)

จัดเป็น OAR เมื่อเข้าข้อใดข้อหนึ่ง:
1. มีขายทั่วไป lead time สั้น หรือทำ Blanket Order ได้
2. เสียยาก และผลิตในประเทศได้ (กลึง หล่อ ทำใหม่ได้)
3. ซ่อมได้โดยไม่ต้องปิดเครื่อง และรออะไหล่ได้ในเวลาสมควร
4. ราคาแพง เช่น ประเภทสินทรัพย์ถาวร ที่วางแผนซ่อมระยะยาวได้

- รายการ OAR ยังอยู่ในทะเบียน แต่ระบบไม่เติมสต็อกจนกว่ามีความต้องการ (ใส่ "OAR" ในคอลัมน์ OAR/Min ของ Reorder Report) ดู [[MRO Inventory Control Methods]]
- ข้อสังเกต: เกณฑ์ข้อ 4 ดูขัดกับหัวข้อ Capitalized Parts ที่ "ต้องสร้างสต็อกไว้จำนวนหนึ่ง" และสรุปท้ายบทที่นับ capitalized parts เป็นรายการสต็อกประจำ น่าจะหมายถึงเฉพาะชิ้นราคาแพงที่วางแผนซ่อมล่วงหน้าได้ (การตีความของ reading notes)

### Capitalized Parts (SPO p.28-29)

เกณฑ์ capitalize:
1. เป็นอะไหล่ประกันเตรียมพร้อมในรูป equipment หรือส่วนควบ
2. ราคาสูง เช่น **เกิน 20,000 บาทต่อหน่วย** (ตัวอย่างของหนังสือ)
3. อายุใช้งาน **เกิน 1 ปี**
4. ใช้นิยามเดียวกับการแบ่งประเภทสินทรัพย์ถาวรของบริษัท

ประโยชน์: (1) ลดวัสดุคงคลัง ทำให้ stock turn / inventory turnover สูงขึ้น (2) เพิ่มสินทรัพย์ถาวร ใช้ประโยชน์ด้านธนาคารได้ (3) กระจายค่าซ่อมตามระยะหักค่าเสื่อม ไม่กระจุกในเดือนที่เบิก ดู [[Inventory Turnover and GPI Benchmarks]]

### Commissioning Spares (SPO p.30-31)

- ผู้รับเหมาสร้างโรงงาน/ต่อเติมยูนิตต้องเตรียมไว้ช่วง commissioning period; ถ้าเดินเครื่องไม่ได้หรือผลิตภัณฑ์ไม่ได้สเปก การซ่อมเป็นหน้าที่ผู้รับเหมา
- มูลค่าเป็นค่าใช้จ่ายของผู้รับเหมา คิดกับเจ้าของงานหรือบวกในราคารับเหมาไม่ได้; จบงานผู้รับเหมาเก็บกลับ เจ้าของงานอาจเลือกซื้อตามเงื่อนไขที่ตกลง
- **สอดคล้องกับ RBMM**: RBMM ถือ Commissioning Spare Part เป็นความรับผิดชอบของผู้ผลิต/EPC ไม่ควรรับเข้าคลังบำรุงรักษา และเตือนว่าผู้ขายมักเสนออะไหล่เกินจำเป็นจนต้อง Write-off (RBMM p.15-16, p.235) ดู [[Spare Parts Management]] และ [[Asset Life Cycle]]

### สรุปรายการที่เข้าบัญชีวัสดุคงเหลือ (SPO p.31, p.102)

- เข้าสต็อกประจำ (regular storehouse items / SKU): Unique, Insurance and Standby, Interchangeable, Capitalized, General Used และ Chemical & Gas
- ตรงข้าม: ของซื้อง่าย lead time สั้น ไม่สำคัญต่อการผลิต รอได้ -> OAR; อะไหล่ที่ผลิตในประเทศได้ให้จัดซื้อกับซ่อมบำรุงสำรวจตลาด บันทึกแหล่งผลิต แล้วจัดเป็น OAR

## ชนิดความต้องการตามกลุ่มและประเภทงาน (SPO p.34-35)

ตารางที่ 4.1 (อิสระ = independent พยากรณ์ด้วยสถิติ มีคงคลังต่อเนื่อง; แปรตาม = dependent วางแผนได้ คงคลังชั่วคราว):

| Maintenance Category | Unique | Insurance & Standby | Interchangeable | OAR | General Used |
|---|---|---|---|---|---|
| Breakdown | อิสระ | อิสระ | อิสระ | แปรตาม | อิสระ |
| Predictive | อิสระ | อิสระ | อิสระ | แปรตาม | อิสระ |
| Preventive | แปรตาม | แปรตาม | อิสระ | แปรตาม | อิสระ |
| Planned Shutdown / Turnaround | แปรตาม | แปรตาม | อิสระ | แปรตาม | อิสระ |

- งานซ่อมใหญ่ที่เป็น dependent demand ใช้ system contract และตาราง MR/MS แทนการลงทุนสต็อกล่วงหน้า ดู [[Turnaround Management]] และ [[MRO Purchasing and Contracting]]
- ข้อสังเกต: หนังสือจัด Interchangeable เป็นอิสระแม้ในงาน Preventive/Turnaround และ OAR เป็นแปรตามทุกกรณีโดยไม่ให้เหตุผล เป็นมุมมองของผู้เขียน
- ความคล้ายกับ RBMM (การตีความของ wiki): แนวคิด "งานตามแผน = วางแผนได้ / งานนอกแผน = ต้องพยากรณ์" ตรงกับกฎ Direct Purchase สำหรับงานตามแผน และ Stock Parts สำหรับ CM-Unplanned ของ RBMM ([[Spare Parts Management]]) แต่ SPO แยกตามกลุ่มวัสดุด้วย

## พัสดุคลัง 3 ประเภทในนโยบายคลัง (SPO p.55-57)

ตัวอย่างนโยบายคลังของอุตสาหกรรมหนักแห่งหนึ่ง (ข้อ 6) แบ่งพัสดุคลังเป็น 3 ประเภทพร้อมวิธีควบคุม:

| ประเภท | กลุ่มย่อย | วิธีควบคุม |
|---|---|---|
| 6.1 Equipment spare parts (ยึดคำแนะนำผู้ผลิตแล้วทบทวน) | Interchangeable parts (bearing, V-belt, oil seal, O-ring) | รวมเก็บที่เดียว; fast/medium moving ใช้ EOQ/ROP, Hi/Low limit; slow moving และ insurance ใช้ Min/Max ที่คณะกรรมการอนุมัติ |
| | อะไหล่สึกเร็วเฉพาะเครื่อง (สั่งจาก OEM) | Min/Max ที่คิด lead time |
| | Insurance/standby | ราคาต่ำคุมแบบอะไหล่สึกเร็ว; ราคาสูงผ่านคณะกรรมการ |
| | Instrument / Electrical / Electronic | Min/Max เสนอโดยผู้ชำนาญแต่ละสาขา |
| 6.2 General used items (ท่อ fitting gasket ฉนวน bolt/nut) | - | standardize ให้รายการน้อยลง; forecast + EOQ/ROP; ซื้อน้อยแต่บ่อยด้วย Vendor Stocking / Blanket Order; ของไม่สำคัญ (สี ท่อ PVC) ไม่สต็อก ลงค่าใช้จ่ายตรง |
| 6.3 เคมีภัณฑ์งานซ่อมบำรุง (ไม่รวมแล็บ) | นำเข้า | อัตราใช้ย้อนหลัง 6 เดือน + safety level + ความต้องการช่วง lead time เป้าสต็อกสูงสุด **3 เดือน** |
| | ซื้อในประเทศ | อัตราใช้ 6 เดือนคิดความต้องการทั้งปี แล้วทำ Blanket Order ทั้งปี |

นโยบายเดียวกันกำหนดมูลค่าคงคลังมาตรฐาน **ไม่เกิน 3% ของเงินลงทุนสร้างโรงงาน** และให้สต็อกมีไว้เพื่อซ่อมบำรุงปกติเท่านั้น ส่วน overhaul/turnaround ต้องวางแผนล่วงหน้า (SPO p.55) ตารางสรุปวิธีควบคุม x ประเภทอะไหล่ของบทที่ 9 (รวมคอลัมน์ Low Value และ Free Stock Issue) อยู่ที่ [[MRO Inventory Control Methods]]

## ปัจจัย 7 ข้อในการตัดสินสต็อกอะไหล่แต่ละรายการ (SPO p.128-129)

1. อายุการใช้งานของชิ้นส่วน
2. จำนวนที่ติดตั้งใช้งาน
3. ต้องเปลี่ยนใหม่ หรือถอดซ่อมได้
4. ความสำคัญของเครื่องต่อการเดินโรงงานต่อเนื่อง
5. ความซับซ้อน ซ่อมเองได้หรือต้องใช้เครื่องมือพิเศษ
6. เวลาจัดหาของใหม่
7. จุดประสงค์ เก็บไว้เปลี่ยนจริง หรือเป็นอะไหล่ประกอบ

บทที่ 5 ให้ปัจจัยคล้ายกันอีกชุด (5 ข้อ: สึกหรอ/ผุกร่อนง่าย, สภาพแวดล้อม, สภาพการใช้งาน, ความยากในการจัดหา, ใช้ร่วม/มีของเทียบเคียง) สำหรับปรับ basic practice รายเครื่อง (SPO p.40) ดู [[Spare Parts Recommendation by Equipment Type]] การตีความของ wiki: ข้อ 4 และ 6 ตรงกับแกน criticality และ lead time ที่ RBMM ใช้ใน [[Spare Part Criticality and Risk]] แต่ SPO ใช้เป็น checklist เชิงคุณภาพ ไม่ได้แปลงเป็นค่าเสี่ยงหรือ cost ratio

## เชื่อมโยงกับ compressor failure hierarchy

ส่วนนี้เป็นการตีความของ wiki: หนังสือไม่ได้จัดกลุ่มตาม maintainable item แต่ใช้กับ [[Compressor]] ได้ เช่น compressor ที่ติดตั้งคู่ (A/B) ทำให้อะไหล่ของมันเข้ากลุ่ม Insurance and Standby (ใส่รหัส "S"), ชิ้นวาล์วและ packing ของ [[Reciprocating Compressor]] เป็น Unique Parts ที่สึกเร็ว (ต้องซื้อ OEM) ขณะที่ bearing, O-ring, V-belt เป็น Interchangeable Parts ส่วน rotor หรือ bundle สำรองราคาสูงอาจเข้าเกณฑ์ Capitalized Parts จำนวนแนะนำต่อชิ้นอยู่ที่ [[Spare Parts Recommendation by Equipment Type]]

## ดูเพิ่ม

- [[Spare Parts Optimization Book]]
- [[Spare Parts Management]]
- [[MRO Inventory Control Methods]]
- [[SPO vs RBMM Spare Parts Approaches]]
- [[Maintenance Cost Structure]]

## Triplets

- [[MRO Material Classification]] [defined_in:: [[Spare Parts Optimization Book]]] chapters 1, 3, 4, 5, 10
- MRO Items [is_a:: Material Type] one of 4 international types with raw material, finished goods, packaging (SPO p.12)
- MRO Items [has_label:: Maintenance Repair and Operation Items] material not part of finished goods (SPO p.12)
- Capital Intensive Plant [has_category:: many high-value MRO items] table 1.1 (SPO p.15)
- Labour Intensive Plant [has_category:: few low-value MRO items] table 1.1 (SPO p.15)
- MRO Items [has_category:: Independent Demand] regardless of made to order or made to stock (SPO p.15)
- Direct Turnover [uses:: Cost Center and Character of Expense] expense on purchase (SPO p.16-17)
- MRO Items [is_a:: Current Asset] inventory account, no depreciation (SPO p.12-13, p.16); agrees with RBMM p.16, p.70
- Unique Parts [is_a:: MRO Material Group] group 1, OEM only, first regular item candidate (SPO p.26)
- Insurance and Standby Parts [is_a:: MRO Material Group] group 2 (SPO p.26-27)
- Interchangeable Parts [is_a:: MRO Material Group] group 3 (SPO p.27)
- Order as Required [is_a:: MRO Material Group] group 4, OAR (SPO p.27-28)
- Capitalized Parts [is_a:: MRO Material Group] group 5 (SPO p.28-29)
- General Used Items [is_a:: MRO Material Group] group 6, general hardware and consumables (SPO p.29)
- Chemical and Gas [is_a:: MRO Material Group] group 7 (SPO p.30)
- Tools and Machine Tools [is_a:: MRO Material Group] group 8 (SPO p.30)
- Commissioning Spares [is_a:: MRO Material Group] group 9 (SPO p.30-31)
- Insurance and Standby Parts [has_code:: S] suffix code to filter the group (SPO p.27)
- Insurance and Standby Parts [related_to:: [[Redundancy and Standby Systems]]] standby A/B/C units (SPO p.26-27)
- Insurance and Standby Parts [differs_from:: Insurance Part] SPO defines by role; RBMM by stock-out cost when cost ratio below 1, interpretation
- Interchangeable Parts [related_to:: [[Parts Interchangeability]]]
- Order as Required [depends_on:: Lead Time] short lead time or Blanket Order possible (SPO p.27-28)
- Order as Required [has_value:: 0] normal stock level, buy only on demand (SPO p.27-28, p.109)
- Capitalized Parts [has_value:: more than 20,000 THB per unit] book example price criterion (SPO p.28)
- Capitalized Parts [has_value:: more than 1 year] service life criterion (SPO p.28)
- Capitalized Parts [produces:: higher inventory turnover] moves value from current to fixed assets (SPO p.29)
- Tools and Machine Tools [has_value:: below 100 THB] treated as consumable expense (SPO p.30)
- Commissioning Spares [applies_to:: Contractor] contractor cost, taken back at end (SPO p.30-31)
- Commissioning Spares [alias_of:: Commissioning Spare Part] RBMM term; both assign to contractor/EPC (RBMM p.15-16, p.235)
- Unique Parts [has_category:: Dependent Demand] preventive and turnaround work; independent for breakdown and predictive (SPO p.34)
- Interchangeable Parts [has_category:: Independent Demand] all maintenance categories (SPO p.34)
- Order as Required [has_category:: Dependent Demand] all maintenance categories (SPO p.34)
- Equipment Spare Parts [is_a:: Warehouse Stock Class] policy 6.1 (SPO p.55-56)
- General Used Items [is_a:: Warehouse Stock Class] policy 6.2, forecast plus EOQ/ROP (SPO p.56)
- Maintenance Chemicals [is_a:: Warehouse Stock Class] policy 6.3 (SPO p.56-57)
- Maintenance Chemicals [has_value:: 3 months] maximum stock target for imported chemicals (SPO p.57)
- Warehouse Policy [has_value:: 3%] maximum standard inventory value of plant investment (SPO p.55)
- Stock Decision [depends_on:: Equipment Criticality] factor 4 of 7 (SPO p.128-129)
- Stock Decision [depends_on:: Lead Time] factor 6 of 7 (SPO p.128-129)
- Stock Decision [depends_on:: Installed Quantity] factor 2 of 7 (SPO p.128-129)
- Stock Decision [related_to:: [[Spare Part Criticality and Risk]]] SPO qualitative checklist vs RBMM risk calculation, interpretation

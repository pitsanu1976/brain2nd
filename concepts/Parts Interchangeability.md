---
title: Parts Interchangeability
created: 2026-10-27
updated: 2026-10-27
type: concept
tags: [spo, book, spare-parts, inventory-control, warehousing, cmms]
sources: [spare-parts-optimization.md, reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Parts Interchangeability

อะไหล่ที่ใช้ได้กับหลายเครื่อง (Interchangeable Parts) และคู่มือที่บันทึกว่าแต่ละรายการใช้กับเครื่องใด (Parts Interchangeable Book) ตาม [[Spare Parts Optimization Book]] บทที่ 6 เป้าหมายคือรวมรายการที่ซ้ำกันข้ามเครื่องให้เป็นรายการคลังเดียว ลดสต็อกรวม และลดการหยุดโรงงานเพราะไม่รู้ว่ามีของอยู่ที่เครื่องอื่น เป็นกลุ่มที่ 3 ของ [[MRO Material Classification]]

## ลักษณะของ interchangeable parts (SPO p.27, p.60)

- ใช้กับเครื่องทั่วไป ส่วนใหญ่เป็น mechanical และ power transmission เช่น ball bearing, belting, V-belt, wear ring
- มีผู้ผลิตชิ้นส่วนโดยตรงหลายราย (หนังสือเรียก OPM, Original Part Manufacturing ซึ่งไม่ใช่ศัพท์มาตรฐาน) และมีระบบรหัสอ้างอิงข้ามยี่ห้อ (cross reference) จึงเลือกยี่ห้อได้ ไม่ต้องตาม OEM
- ปัญหาเมื่อไม่ทำคู่มือ: ไม่รู้ว่าชิ้นเดียวกันกระจายอยู่เครื่องใดกี่ชิ้น; ถ้าเก็บแยกตามเครื่องจะบริหารหลายจุด และอาจสั่งซื้อของเครื่องหนึ่งทั้งที่อีกเครื่องยังมีเหลือ (SPO p.60)
- ประโยชน์ที่ย้ำในบทที่ 10: ลดสต็อก และลดการหยุดโรงงานเพราะขาดอะไหล่ เพราะรู้ว่ามีชนิดเดียวกันที่เครื่องอื่น (SPO p.129) และ "ทำรายการอะไหล่ใช้ร่วมกันได้" เป็นหนึ่งในแนวทางประหยัดอะไหล่ (SPO p.128)

## ขั้นตอนจัดทำคู่มือ 6 ขั้น (SPO p.60-62)

1. สำรวจจาก SKU / รายการสำรองคลัง หรือเอกสารเสนอแนะของผู้ขายเครื่อง คัดเฉพาะรายการที่ใช้ร่วมได้ ไฮไลต์และหมายเหตุว่าโอนไปกลุ่ม interchangeable
2. จัดกลุ่มตาม type, ขนาด และ application; ใช้สมุดเทียบเบอร์ข้ามยี่ห้อ (เช่น ball bearing interchange ที่รวมผู้ผลิตมากกว่า 10 ราย) ให้วิศวกรเลือกยี่ห้ออื่นได้
3. ลงตารางคู่มือ (โครงสร้าง 7 คอลัมน์ด้านล่าง)
4. รวมอะไหล่ตาม line item จากทุกเครื่องมาเก็บชั้นเดียวกัน เช่น section "Common Used Parts"
5. ตรวจนับ (physical inventory) แล้วลงยอดในระบบ parts inventory
6. กำหนดนโยบายสต็อก/เติมของ: Min-Max, ROP/EOQ, Order-up-to หรือใช้ basic practice ดู [[MRO Inventory Control Methods]]

### โครงสร้างตาราง 7 คอลัมน์ (SPO p.61)

| # | คอลัมน์ | หมายเหตุ |
|---|---|---|
| 1 | ชื่อ part | |
| 2 | Bin location | ระบุได้หลังรวมเก็บที่เดียว (ขั้น 4) |
| 3 | คำอธิบายย่อ | |
| 4 | Commodity code ที่ออกใหม่ | ถ้าไม่ต้องซื้อจาก OEM ไม่ต้องใส่ OEM part no.; ถ้าต้องซื้อ OEM ใส่ Part # / Drawing # อ้างกลับเอกสารผู้ผลิต |
| 5 | ส่วนขยาย | เช่น วัสดุ |
| 6 | Number used | จำนวนรวมที่ใช้งานทั้งโรงงาน |
| 7 | คอลัมน์รายเครื่อง | equipment code + ส่วนขยาย (capacity, ยี่ห้อ) ทำเครื่องหมายเมื่อเครื่องนั้นใช้ part นี้ |

- วิธีอ่าน (ตัวอย่างหน้า "Wear Rings Various" จาก APC Interchangeable Book): เปิดหน้าของ part -> เลือกคอลัมน์เครื่อง (เช่น ปั๊ม P-507A) -> ไล่ลงหาเครื่องหมาย ✓ -> อ่านไปทางซ้ายได้ commodity code ทุกเครื่องที่มี ✓ ในแถวเดียวกันใช้อะไหล่นี้แทนกันได้ (SPO p.61)
- ข้อสังเกต: ตารางตัวอย่างใน OCR เพี้ยนมาก (code 322-26-835 ที่ใช้อธิบายไปอยู่แถว "Shell Head", 322-26-817 ซ้ำสองแถว, number used 212/188 ดูไม่สมเหตุผลสำหรับ wear ring) จึงไม่ควรใช้ตัวเลขในตารางนั้น

## Commodity code vs OEM part number (SPO p.61-62)

- **Commodity code = stock number ภายในบริษัท** ระบบเดียวทั้งโรงงาน ต่างจาก part number ของ OEM
- อะไหล่ที่มีผู้ผลิตโดยตรง (เช่น SKF bearing) ไม่ต้องสั่งด้วย OEM part number; ชิ้นที่ต้องซื้อจาก OEM เท่านั้นจึงเก็บ OEM part/drawing number ไว้อ้างอิง
- การตีความของ wiki: แนวคิดนี้ตรงกับหลักของ RBMM ที่ให้อะไหล่อยู่ใน BOM / Where Used แทนการฝังรหัสอะไหล่ในรหัสอุปกรณ์ เพราะอะไหล่ตัวเดียวใช้หลายอุปกรณ์ (RBMM p.98) และการเน้น codification มาตรฐานและกำจัดรายการซ้ำ (RBMM p.240) ดู [[Spare Parts Management]]

## ข้อแนะนำเชิงปฏิบัติ (SPO p.62)

- งานอาจใช้เวลานานถ้าขาดเอกสารผู้ผลิต หรือบันทึกรายการไม่ครบ (เช่น เขียนแค่ "Ball Bearing" ไม่รู้ชนิด ขนาด เครื่อง)
- ทางแก้ที่หนังสือเสนอ: รวบรวมของจริงจากที่เก็บมาไว้ที่เดียว ให้ผู้เบิกระบุชนิด/ขนาดและเครื่องที่ใช้, ให้คลังรวบรวมคู่มือเครื่องจักร, ตั้ง task force ให้เสร็จเร็ว

## ใครรับผิดชอบ

- หัวหน้าคลังมีหน้าที่พัฒนารายการอะไหล่ใช้ได้หลายเครื่องเพื่อการจัดเก็บที่ดีขึ้น (ข้อ 7 ของหัวข้อความรับผิดชอบ 20 ข้อ, SPO p.22)
- คณะกรรมการควบคุมพัสดุ (MCC) มีหน้าที่ควบคุมการทำรายการอะไหล่ใช้แทนกันได้ และกำหนดมาตรฐานวัสดุกันเก็บซ้ำซ้อน (หน้าที่ข้อ 15 และ 17, SPO p.131-132) ดู [[MRO Inventory Reduction Program]]
- ในนโยบายคลัง interchangeable parts (bearing, V-belt, oil seal, O-ring) ซื้อจากผู้ผลิตอื่นหรือในประเทศได้ ให้รวมเก็บที่เดียว และควบคุมด้วย EOQ/ROP หรือ Hi/Low limit เมื่อหมุนเร็ว/ปานกลาง (SPO p.55-56)
- ตารางชนิดความต้องการของหนังสือจัด interchangeable parts เป็น independent demand ในทุกประเภทงานซ่อม (SPO p.34) ดู [[MRO Material Classification]]

## ความสัมพันธ์กับ CMMS (RBMM)

- RBMM ระบุ "อะไหล่ทดแทน (ทางเดียว/สองทาง)" เป็นข้อมูลเสริมของ Spare Part Database ใน [[CMMS]] ร่วมกับ Where Used/BOM และประวัติผู้ขาย (RBMM p.100-102)
- การตีความของ wiki: Parts Interchangeable Book ของ SPO คือรูปแบบกระดาษของข้อมูล two-way substitute + Where Used: ทุกเครื่องในแถวเดียวกันใช้ชิ้นเดียวกันได้ทั้งสองทาง ส่วน one-way substitute (A แทน B ได้ แต่ B แทน A ไม่ได้ เช่น ชิ้นรุ่นใหม่แทนรุ่นเก่า) ไม่มีในหนังสือ SPO นิยามของ one-way/two-way เป็นความรู้ทั่วไป ไม่มีใน sources [confidence:: low]
- ใน CMMS ปัจจุบัน คู่มือนี้จึงควรเป็นความสัมพันธ์ commodity code -> equipment (Where Used) แทนตารางกระดาษ (ข้อเสนอแนะการประยุกต์)

## เชื่อมโยงกับ compressor failure hierarchy

ส่วนนี้เป็นการตีความของ wiki: ชิ้นส่วน interchangeable ส่วนใหญ่อยู่ใน maintainable item ทั่วไปของ [[Compressor]] เช่น bearing และ coupling ใน [[PWTR Power Transmission]], O-ring และ seal ใน [[SHSS Shaft Seal System]], filter ใน [[LUBS Lubrication System]] ขณะที่ชิ้นวาล์ว piston ring และ packing ของ [[Reciprocating Compressor]] มักเป็น unique parts ของ OEM การรวม bearing/O-ring ของ compressor หลายเครื่องเป็น commodity code เดียวทำให้คำนวณความต้องการรวม (consolidation) ได้ ดู [[Spare Parts Management]] และจำนวนแนะนำต่อเครื่องใน [[Spare Parts Recommendation by Equipment Type]]

## ดูเพิ่ม

- [[Spare Parts Optimization Book]]
- [[MRO Material Classification]]
- [[CMMS]]
- [[Warehouse Design and Storage]]

## Triplets

- [[Parts Interchangeability]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 6 (SPO p.59-62)
- Interchangeable Parts [is_a:: MRO Material Group] group 3 (SPO p.27)
- Interchangeable Parts [has_part:: Ball Bearing] example (SPO p.27, p.60)
- Interchangeable Parts [has_part:: V-belt] example (SPO p.27, p.60)
- Interchangeable Parts [has_part:: Wear Ring] example (SPO p.60-61)
- Interchangeable Parts [uses:: Cross Reference] brand interchange book, more than 10 bearing makers (SPO p.60)
- Parts Interchangeable Book [produces:: Common Used Parts Section] parts from all machines stored together (SPO p.61-62)
- Survey Interchangeable Items [step_of:: Parts Interchangeable Book] step 1 (SPO p.60)
- Group by Type Size Application [step_of:: Parts Interchangeable Book] step 2 (SPO p.60)
- Tabulate Book [step_of:: Parts Interchangeable Book] step 3, 7 columns (SPO p.61)
- Consolidate Storage [step_of:: Parts Interchangeable Book] step 4 (SPO p.61-62)
- Physical Inventory [step_of:: Parts Interchangeable Book] step 5 (SPO p.62)
- Set Stock Policy [step_of:: Parts Interchangeable Book] step 6, Min-Max, ROP/EOQ, Order-up-to (SPO p.62)
- Parts Interchangeable Book [has_value:: 7] columns (SPO p.61)
- Commodity Code [alias_of:: Stock Number] internal company code (SPO p.62)
- Commodity Code [differs_from:: OEM Part Number] OEM number kept only when part must be bought from OEM (SPO p.61-62)
- Parts Interchangeable Book [related_to:: [[CMMS]]] RBMM one-way/two-way substitute parts in Spare Part Database (RBMM p.100-102), interpretation
- Parts Interchangeable Book [related_to:: Where Used] interpretation
- Interchangeable Parts [has_category:: Independent Demand] all maintenance categories (SPO p.34)
- Interchangeable Parts [selects:: EOQ/ROP] fast and medium moving; Min/Max for slow moving (SPO p.55-56)
- Materials Control Committee [applies_to:: Interchangeable Parts] duty 17 controls interchangeable list (SPO p.131-132)
- Interchangeable Parts [produces:: lower stock] and fewer stock-out shutdowns (SPO p.129)

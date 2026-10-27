---
title: Tool Crib and Warehouse Security
created: 2026-10-27
updated: 2026-10-27
type: concept
tags: [spo, book, warehousing, spare-parts, maintenance-management, cost]
sources: [spare-parts-optimization.md]
confidence: medium
contested: false
---

# Tool Crib and Warehouse Security

การควบคุมคลังเครื่องมือ (tool crib / tool room) และความมั่นคงของคลังวัสดุตามหนังสือ [[Spare Parts Optimization Book]] บทที่ 11 (Tool Room Procedures and Controlling) และบทที่ 12 (Warehouse Security) เป้าหมายร่วมคือของทุกชิ้นที่ออกจากคลังต้องมีผู้รับผิดชอบและหลักฐาน ของที่หายหรือเสื่อมในคลังเป็นต้นทุนจริงที่ลดได้ ดู [[MRO Inventory Reduction Program]] ส่วนการจัดผังและวิธีเก็บอยู่ใน [[Warehouse Design and Storage]]

## คลังเครื่องมือ (บทที่ 11)

### ที่ตั้งและผู้รับผิดชอบ (SPO p.134)

- tool crib มักอยู่ใต้ Maintenance Shop บางแห่งอยู่ใต้คลังพัสดุ ข้อดีข้อเสียพอกัน เป็นการตัดสินใจของผู้บริหาร (บทที่ 2 ก็ระบุว่าการบริหาร tool room เป็นงานของหัวหน้าคลัง แต่มอบให้ซ่อมบำรุงได้ (SPO p.23))
- ไม่ว่าอยู่ใต้ใคร ต้องมี **พื้นที่แยกเฉพาะ** และ **ผู้รับผิดชอบโดยตรง** ที่มีคุณสมบัติ ดูแลให้เครื่องมือพร้อมใช้และปลอดภัย

### เครื่องมือ 4 ประเภทและการควบคุม (SPO p.134-135)

| ประเภท | ตัวอย่าง | วิธีจ่าย/ควบคุม |
|---|---|---|
| Standard Tool Kits | หีบเครื่องมือประจำตัวช่างแต่ละสาขา และโฟร์แมน | ถือประจำ เซ็นรับพร้อม tool list 2 ชุด; ตรวจตามรอบ เช่น ทุก 6 เดือนหรือ 1 ปี; หาย/ชำรุดสอบสวนแล้วเบิกใหม่ และ/หรือลงโทษ เช่น ซื้อชดใช้ |
| Special Tools | pipe wrench ใหญ่ ประแจตี เครื่องเชื่อม สว่าน/เลื่อยไฟฟ้า | ใช้หมุนเวียน จ่ายแบบ **ยืม** พร้อมบันทึก |
| Unique Special Tools | Gas Detector, Metal X-Ray, Gas Analyser, Thickness Gauge | ราคาแพงมาก ลงบัญชีเป็น **ทรัพย์สินถาวร** มอบผู้ใช้ที่ผ่านการฝึกเก็บรักษาเอง |
| Consumable Tools | ดอกสว่านเล็ก ดินสอช่าง ชอล์กหิน แผ่น/หินเจียร | ควบคุมเหมือนพัสดุทั่วไป หรือแบบ supermarket (Free Stock Issue) ตรวจยอดตามรอบ |

### การดูแลและจัดเก็บ (SPO p.135-136)

- เครื่องมือที่จ่ายต้องสมบูรณ์และปลอดภัย ชำรุดต้องหาสาเหตุ: เสื่อมตามปกติ หรือใช้ผิดวิธี/จงใจ (กรณีหลังชดใช้/ลงโทษตามระเบียบ)
- เก็บบนชั้นหรือตู้ล็อก ชิ้นเล็กในกล่องใส/ลิ้นชัก ชิ้นใหญ่บนพื้นที่ตีเส้น ชิ้นที่แขวนได้ใช้ **shadow board** มีรูปเงา หมายเลข และชื่อ
- ทำความสะอาดและหล่อลื่นก่อนเก็บ; เครื่องมือมีสายไฟหรือชิ้นส่วนด้านความปลอดภัยตรวจทุกครั้งที่คืน ชำรุดซ่อมก่อนเก็บ

### ระบบจ่ายเครื่องมือส่วนกลาง (SPO p.136-137)

| ระบบ | วิธี | ข้อดี | จุดอ่อน |
|---|---|---|---|
| Tag system (ป้ายโลหะ) | เครื่องมือมีหมายเลขถาวรและป้ายโลหะ ~10x5 cm เลขเดียวกัน; ยืมแล้วเขียนเลขพนักงานบนป้าย แขวนบนหมุดของพนักงาน; เครื่องมือบน shadow board แขวนป้ายพนักงานที่ตำแหน่งนั้นแทน; ทบทวนรายบุคคลอย่างน้อยเดือนละครั้ง | ง่าย เร็ว เห็นทันทีว่าใครยืมอะไร | ไม่มีลายเซ็น/หลักฐานการยืม ไม่เหมาะกับองค์กรคนมาก พื้นที่กว้าง หรือยังไว้ใจกันไม่ได้ |
| Loan form (ใบยืม) | ต้นฉบับ 1 + สำเนา 2: ชื่อ เลขประจำตัว รายการ วันยืม วันกำหนดคืน ลายเซ็น อาจพิมพ์เงื่อนไขค่าปรับด้านหลัง; ผู้ยืมถือสำเนา 1 ห้องเครื่องมือเก็บต้นฉบับ + สำเนา; คืนแล้วแลกต้นฉบับ อาจมีสมุดทะเบียนหรือ letter boxes | มีหลักฐานทั้งบริษัทและพนักงาน | ช้ากว่า |

- ข้อเสนอเพิ่ม: เครื่องมือมักหายช่วงผู้ยืมลา ให้คืนเครื่องมือทั้งหมด (รวม standard kit) ก่อนลากิจ/พักร้อน ตรวจสภาพและเปลี่ยนชิ้นชำรุด แล้วจ่ายชุดคืนเมื่อกลับ (SPO p.137)

### ค่าเสียหายและการตรวจนับ (SPO p.137)

- บริษัทมักไม่เรียกค่าปรับ แต่การเบิกเปลี่ยน/ซื้อใหม่ต้องให้หัวหน้างานและผู้จัดการอนุมัติ และลงบัญชี **cost center** ของหน่วยงานนั้น (ทำให้ต้นทุนเครื่องมือหายมองเห็นได้)
- ตรวจนับตามรอบเหมือนพัสดุ: เรียงตามหมายเลขพัสดุ หรือตามตัวอักษรถ้าไม่มีหมายเลข; หรือนับ **ตาม location** ไล่ทีละตำแหน่ง สะดวกกับผู้ตรวจที่ไม่รู้จักเครื่องมือ แต่ห้ามย้ายที่เก็บบ่อย
- ถ้ามี [[CMMS]] ทะเบียนเครื่องมือ การยืม-คืน และ cost center สามารถบันทึกเป็น transaction แทนสมุดได้ (การตีความของ wiki; หนังสือไม่ได้กล่าวถึง CMMS ในบทนี้)

## ความมั่นคงในคลังวัสดุ (บทที่ 12)

### หลัก 4 ข้อ (SPO p.140)

1. ไม่จ่ายพัสดุออกจากคลังโดยไม่มีเอกสารรับผิดชอบตามที่บริษัทกำหนด
2. คลังล็อกได้มั่นคง และปิดล็อกทุกครั้งที่ไม่มีเจ้าหน้าที่
3. ห้ามบุคคลที่ไม่ใช่เจ้าหน้าที่คลังอยู่ในคลังโดยลำพัง
4. ป้องกันพัสดุจากสภาพแวดล้อมอันตราย (ความร้อน น้ำหยด/ซึม ไอน้ำมัน ฝุ่น)

พื้นที่รอบโรงงานเป็นความรับผิดชอบของ รปภ./ธุรการ ซึ่งต้องวางมาตรการครอบคลุมคลังด้วย

### ใบผ่านประตู (Gate Pass) (SPO p.140)

ใบผ่านประตูมีไว้บันทึกและให้ผู้มีอำนาจอนุมัติการนำของออก สอบกลับได้ว่าออกไปเพื่ออะไรและมีใบเบิกครบ เกณฑ์ตัดสินของ รปภ.:

| กรณี | ใบผ่านประตู | เอกสารประกอบ | ผล |
|---|---|---|---|
| พัสดุออกโรงงาน | ไม่มีรายการ | - | ทุจริต |
| พัสดุออกโรงงาน | มีรายการ | ไม่มีใบเบิก/เอกสารรับผิดชอบ | ส่อทุจริต |
| สินค้าออกประตู | มีรายการ | ไม่มีใบกำกับภาษี/เอกสารอื่น | ทุจริต |
| สินค้าออกประตู | ไม่มี (ใช้สำเนาใบกำกับภาษีแทน) | ใบกำกับภาษีและเอกสารครบ | สุจริต |

กรณีที่ 4 ใช้ได้เฉพาะบริษัทที่กำหนดให้สำเนาใบกำกับภาษีใช้แทนใบผ่านประตู

### การเข้าคลัง (SPO p.140-141)

- ผู้เบิกรอที่จุดรับ-จ่าย ถ้าต้องเข้าไปตรวจของ/ช่วยขน ต้องมีพนักงานคลังไปด้วยทุกครั้ง
- ควรกำหนดเวลาบริการสูงสุดเป็นนาที (องค์กรกำหนดเอง) เพื่อให้การคุมเข้มไม่ทำให้งานช้า
- ของราคาต่ำหมุนเร็วให้หยิบเองจากสโตร์ย่อยแบบ supermarket

### การเบิกนอกเวลา (SPO p.141-142)

ถ้าคลังเปิดแค่ 08.00-17.00 น. ทางเลือก "ให้เบิกสำรองก่อนปิด" ทำให้ของไม่ถูกคืน หาย และค่าพัสดุบวม ส่วน "ไม่ให้เบิกเลย" ทำให้งานรอหลายชั่วโมง ข้อสรุปของหนังสือคือ **เปิดจ่ายยามวิกาลได้ แต่คุมรัดกุม** ด้วยมาตรการ 9 ข้อ:

1. หัวหน้ากะ (shift superintendent) เป็นผู้บังคับบัญชานอกเวลา โรงงานใหญ่อาจมีผู้จัดการกลางคืน
2. ผู้บังคับบัญชากลางคืนรับผิดชอบการเบิกจ่ายแทนผู้จัดการคลัง
3. **Log book** ทุกครั้งที่เข้าคลัง: ผู้อนุมัติ ผู้เบิก รปภ. ในฐานะพยาน รายการและจำนวน หมายเลขซีลที่ถูกทำลาย หมายเลขซีลใหม่ เวลาเข้า-ออก
4. ผู้จัดการคลังเตรียมรายงานสถานะสต็อกล่าสุดไว้ที่ทางเข้า ค้นหาตามหมายเลข/รายละเอียดและอ้างถึงที่เก็บได้
5. เตรียมใบเบิกเปล่า ผู้เบิกกรอก หัวหน้ากะ/ผู้จัดการกลางคืนเซ็นอนุมัติ
6. **Dual-key control**: เปิดคลังต้องใช้ 2 คน 2 ชุดกุญแจต่างเบอร์ (เวลาปกติ ผู้จัดการคลัง + หัวหน้า รปภ.; นอกเวลา ผู้จัดการกลางคืนหรือหัวหน้ากะ + หัวหน้ากะ รปภ.) เช้าวันถัดไปตรวจซีลร่วมกับ รปภ.:
   - ซีลเดิมเรียบร้อย = ปกติ
   - ซีลถูกทำลายและไม่มีซีลใหม่ = มีผู้เข้าโดยไม่ถูกต้อง ตรวจคลังทันที
   - ซีลถูกเปลี่ยนและมีการเบิก = ตรวจกับ log book และทำเอกสารให้ครบ
7. งานใหญ่ เช่น shutdown หรือโครงการ ให้พนักงานคลังทำงานกลางคืนด้วย (ดู [[Turnaround Management]])
8. การเบิกมูลค่าสูง/สำคัญมาก ต้องเรียกผู้จัดการคลังมาเอง
9. ไฟส่องสว่างในคลัง ทางเข้า ทางขนส่ง รอบอาคาร และลานกลางแจ้ง (floodlight) พิจารณาสปอตไลต์ส่ายได้ที่จุดขนถ่าย

ข้อสังเกต: ประโยคต้นฉบับเรื่องผู้ถือกุญแจชุดที่สองช่วงนอกเวลากำกวม (อยู่กับ รปภ. หรือหัวหน้ากะ) แต่หลักการ 2 คน 2 กุญแจชัดเจน

### การป้องกันการเสื่อมสภาพ (SPO p.142)

- ผู้จัดการคลังรับผิดชอบป้องกันพัสดุทั้งในและนอกคลัง ข้อสงสัยด้านสนิม/การกัดกร่อนให้ปรึกษาฝ่ายเทคนิค
- ใช้สารกันสนิม (เช่น Rustban); อบรมผู้ขับรถยกเรื่องความเสียหายจากความประมาท
- Good housekeeping ทำความสะอาดสม่ำเสมอ; อุปกรณ์ดับเพลิงเพียงพอและตรวจสม่ำเสมอ

## ข้อผิดพลาดของหนังสือ/OCR

- เลขหน้าบทที่ 12 เป็นการอนุมาน (PDF ขาดหน้าว่างก่อนบท) อาจคลาดได้ 1 หน้า
- OCR หลายจุดถูกตีความ: "สอทุจริต" = ส่อทุจริต, "สมุดปุ่มยืม" = สมุดปูมบันทึก, "ระบบเซอร์วิสวาร์เก็ต" ตีความเป็นระบบซูเปอร์มาร์เก็ต, "หลอดไฟล์ไลด์" ตีความเป็น floodlight
- Standard tool kit ระบุช่างประปาซ้ำกับ "ช่างปั๊ป (plumber)" น่าจะเป็นความผิดของต้นฉบับ/OCR

## เชื่อมโยงกับงานบำรุงรักษา

- Unique special tools ในรายการ (Gas Detector, Thickness Gauge) เป็นเครื่องมือ inspection/condition monitoring ที่ต้องสอบเทียบและผู้ใช้ผ่านการฝึก จึงเหมาะกับการมอบผู้ใช้ถือแบบทรัพย์สินถาวร ดู [[Condition Monitoring Techniques]] (การตีความของ wiki)
- ช่วง shutdown ปริมาณเบิกนอกเวลาสูง มาตรการข้อ 7 และ log book จึงสำคัญต่อการคุม material ของ turnaround (การตีความ)

## Triplets

- [[Tool Crib and Warehouse Security]] [defined_in:: [[Spare Parts Optimization Book]]] chapters 11 and 12 (SPO p.133-142)
- [[Tool Crib and Warehouse Security]] [related_to:: [[Warehouse Design and Storage]]]
- [[Tool Crib and Warehouse Security]] [related_to:: [[MRO Inventory Reduction Program]]] losses and deterioration
- Tool Crib [depends_on:: Management Decision] under maintenance shop or materials store (SPO p.134)
- Tool Crib [uses:: Dedicated Area and Custodian] (SPO p.134)
- Standard Tool Kits [is_a:: Tool Category] issued per craftsman, audited every 6 months or 1 year (SPO p.134)
- Special Tools [is_a:: Tool Category] issued on loan (SPO p.134)
- Unique Special Tools [is_a:: Tool Category] fixed asset, held by trained user (SPO p.135)
- Consumable Tools [is_a:: Tool Category] supermarket or Free Stock Issue (SPO p.135)
- Shadow Board [applies_to:: Hangable Tools] (SPO p.136)
- Tag System [is_a:: Tool Issue System] metal tag about 10x5 cm, review at least monthly (SPO p.136)
- Loan Form System [is_a:: Tool Issue System] original plus 2 copies, signed (SPO p.136-137)
- Tag System [differs_from:: Loan Form System] tag faster but no signature evidence (SPO p.136-137)
- Tool Return Before Leave [applies_to:: Standard Tool Kits] (SPO p.137)
- Tool Replacement Cost [depends_on:: Cost Center] supervisor and manager approval (SPO p.137)
- Tool Count by Location [differs_from:: Tool Count by Number] easy for auditors, needs stable locations (SPO p.137)
- Warehouse Security Principles [has_value:: 4] (SPO p.140)
- No Issue Without Document [part_of:: Warehouse Security Principles] (SPO p.140)
- Locked Store When Unattended [part_of:: Warehouse Security Principles] (SPO p.140)
- No Unescorted Non-store Staff [part_of:: Warehouse Security Principles] (SPO p.140)
- Environmental Protection [part_of:: Warehouse Security Principles] heat, water, oil vapour, dust (SPO p.140)
- Gate Pass [uses:: Gate Pass Decision Table] 4 cases (SPO p.140)
- Material Without Gate Pass [has_category:: fraud] (SPO p.140)
- Material With Gate Pass Without Requisition [has_category:: suspected fraud] (SPO p.140)
- Goods With Gate Pass Without Tax Invoice [has_category:: fraud] (SPO p.140)
- Goods With Tax Invoice Copy Instead of Gate Pass [has_category:: honest] only where policy allows (SPO p.140)
- After-hours Issue Controls [has_value:: 9 measures] (SPO p.141-142)
- After-hours Issue [uses:: Log Book] approver, requester, guard witness, seal numbers, times (SPO p.141)
- After-hours Issue [uses:: Dual-key Control] 2 people, 2 different keys (SPO p.142)
- Seal Check [produces:: Unauthorized Entry Alert] seal broken and no new seal (SPO p.142)
- Shutdown Night Shift Storekeeper [related_to:: [[Turnaround Management]]] (SPO p.142)
- Deterioration Prevention [uses:: Rust Preventive] e.g. Rustban (SPO p.142)
- Deterioration Prevention [uses:: Good Housekeeping] (SPO p.142)
- Unique Special Tools [related_to:: [[Condition Monitoring Techniques]]] wiki interpretation [confidence:: low]
- Tool Register [related_to:: [[CMMS]]] wiki interpretation, not in book chapter [confidence:: low]

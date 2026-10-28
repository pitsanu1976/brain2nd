---
title: MRO Purchasing and Contracting
created: 2026-10-27
updated: 2026-10-28
type: concept
tags: [spo, book, procurement, spare-parts, maintenance-management, cost, mpm, outsourcing]
sources: [spare-parts-optimization.md, maintenance-profit-maker.md]
confidence: medium
contested: false
---

# MRO Purchasing and Contracting

การจัดซื้อพัสดุโรงงาน (MRO) ตามบทที่ 8 ของ [[Spare Parts Optimization Book]] (SPO p.85-100) มุมมองฝั่งคลัง/จัดซื้อ: MRO ซื้อยากกว่าวัตถุดิบเพราะมีรายละเอียดเทคนิค ช่างเขียนศัพท์ช่างหรือคำย่อ จัดซื้อขาดความรู้วิศวกรรมจึงซื้อผิดบ่อย และของด่วนที่ไม่ได้สต็อกมักถูกโยนกลับให้ผู้ขอซื้อไปซื้อเอง (SPO p.86) หน้านี้รวม (1) การเขียน PR (2) การจัดซื้อเชิงรุก (3) เทคนิคสัญญา: Blanket Order, System Contracting, Consignment/Vendor Stocking, Outsourcing (4) การคุม air freight (5) การเรียกร้องสินค้าชำรุด ส่วนวิธีตั้งระดับสต็อกอยู่ที่ [[MRO Inventory Control Methods]] และภาพรวมอะไหล่ฝั่ง RBMM อยู่ที่ [[Spare Parts Management]]

## การเขียน Purchase Requisition (PR) (SPO p.86-88)

- ผู้เขียน PR: ซื้อเข้าสต็อก = ผู้จัดการคลังพัสดุ; ซื้อใช้เลย (direct charge) = ผู้รับผิดชอบศูนย์ค่าใช้จ่าย (SPO p.87)
- ของต่างประเทศต้องมีเลขอ้างอิงครบ และเขียน PR เป็นภาษาอังกฤษแบบสากล (SPO p.86)
- เสนอให้กิจการที่ซื้ออะไหล่/เครื่องมือมากตั้งตำแหน่ง **Purchasing Engineer** ในฝ่ายจัดซื้อ (SPO p.86)

### สาระสำคัญของ PR (SPO p.87-88)

1. **รหัสบัญชี** ตามผังบัญชี: Inventory A/C (ซื้อเข้าคลัง), รหัสค่าใช้จ่าย = ศูนย์ค่าใช้จ่าย + ลักษณะค่าใช้จ่าย (ซื้อใช้เลย), รหัสลงทุน (ทรัพย์สินถาวรที่อนุมัติแล้ว)
2. **รายละเอียดพอเพียง** ขึ้นต้นด้วยชื่อหลัก (nomenclature) แล้วตามด้วยส่วนขยาย เช่น "Flange Slip-On ... size 4"" ไม่ใช่ขึ้นต้นด้วยมาตรฐานหรือขนาด

| ข้อแนะนำ | สาระ |
|---|---|
| ชื่อ | ของช่างเรียกได้ 3 แบบ (ภาษาช่าง / ชื่อการค้า / ชื่อสากล) ใช้ชื่ออังกฤษสากล |
| ส่วนขยาย | ระบุให้ครบ; คำย่อใช้มาตรฐานสากลจาก abbreviation dictionary และแคตตาล็อก |
| เลขอ้างอิง | Stock Number / Part Number / Drawing Number; มีแคตตาล็อก + spec แล้วใช้เลขแทนรายละเอียดได้ |
| ห้ามของเทียบเท่า | เขียน "No Substitution Permit" หรือ "Do not Substitute" |
| ยอมรับของเทียบเท่า | เขียน "<ยี่ห้อ> or Equivalent" |

- ผู้ขอซื้อรับผิดชอบรายละเอียด; ควรให้จัดซื้อ OJT/ดูงาน และส่งคู่มือ แคตตาล็อกให้ศึกษา (SPO p.87)
- การตั้งชื่อหลัก/รหัสพัสดุให้เป็นระบบ ดู [[MRO Material Classification]]
- **flag:** ตัวอย่าง flange "ถูก" ของหนังสือเขียน "150 psi" แต่ตาม ASME B16.5 ค่า 150 คือ pressure class (Class 150 / 150#) ไม่ใช่ psi น่าจะเป็นความคลาดเคลื่อนของหนังสือ (ความรู้ทั่วไป ไม่อยู่ใน source) [confidence:: low]

## การจัดซื้อเชิงรุก (Up-stream Purchasing) (SPO p.88-90)

จัดซื้อต้องเข้าใจกระบวนการผลิต เครื่องจักร ไฟฟ้า และเตรียมล่วงหน้าว่าจะซื้ออะไร ที่ไหน lead time เท่าไร ตรวจรับ ขนส่ง เก็บอย่างไร

1. ใช้สถิติจัดซื้อย้อนหลัง 2-3 ปีขึ้นไป คัดรายการใช้มาก/สั่งถี่ แล้วกรองหารายการที่มีปัญหาเลือกผู้ค้า lead time ยาว หรือกำหนด spec ยาก (ตัวอย่าง: จากราว 10,000 รายการ เหลือราว 200 รายการ) (SPO p.88)
2. ทำแคตตาล็อกและ **Specification sheet** ให้รายการสำคัญเหล่านั้น (ผู้ใช้/ฝ่ายเทคนิคทำร่วมกับจัดซื้อ) แล้วอ้าง **Specification No.** ทุกครั้งที่ซื้อ ค่อยขยายไปรายการอื่น ตัวอย่างใบ spec ของสารเคมีมีหัวข้อคุณสมบัติเคมี กายภาพ และการเก็บรักษา (SPO p.89)
3. หาแหล่งขาย/ผลิตทันทีโดยไม่รอ PR: ลงทะเบียน Vendor List สืบราคา และพิจารณาสัญญาแบบ Blanket Order, System Contract, Vendor Stocking, Outsourcing สำหรับของใช้ประจำปริมาณมาก (SPO p.89-90)

แนวคิด "ซื้อน้อยแต่บ่อย" ของการบริหารพัสดุยุคใหม่ ต้องอาศัยจัดซื้อที่เตรียมการดี JIT, Stockless Purchasing และ Vendor Stocking มีรากเดียวกัน (SPO p.90)

## Blanket Order (BO) (SPO p.91-93)

- ที่มา: บริษัทใหญ่ในสหรัฐฯ เริ่มใช้ ก.พ. 1966 (พัฒนาตั้งแต่ต้น 1965) (SPO p.91)
- เหตุผล: PR มูลค่าต่ำกว่า 300 USD/ใบ มีจำนวน **60%** ของใบทั้งหมด แต่มูลค่ารวมเพียง **5%** ของถูกจำนวนมากจึงไม่ควรผ่านขั้นตอนยุ่งยากเท่าของแพง (SPO p.91)
- วิธี: ผู้ใช้พยากรณ์ความต้องการทั้งปี (ตัวอย่าง 5,000 อัน/เดือน x 12 = 60,000 อัน/ปี) PR 1 ใบต่อ 1 รายการ หรือหลายรายการถ้าเป็นของคล้ายกันจากแหล่งเดียว จัดซื้อคัดผู้ค้าด้วยราคา บริการ และความสามารถรับเงื่อนไข BO แล้วออก PO แบบ BO

### เงื่อนไขการส่งมอบ (เลือก 1 แบบ) (SPO p.91)

1. ระบุจำนวน ส่งสม่ำเสมอตามเวลา
2. ระบุจำนวน ส่งภายในกำหนดเวลา
3. กำหนดเวลา ไม่ระบุจำนวน
4. กำหนดเวลา มีประมาณการแต่ไม่ยืนยันการสั่ง
5. กำหนดเวลา ยืนยันการสั่งขั้นต่ำ

### การรับของเป็นงวด (SPO p.92-93)

- ผู้ใช้ออก **Blanket Order Release (BOR)** ระบุจำนวนงวดนั้น อ้างเลข BO + ลำดับครั้ง เช่น BO No. 0123/1 สั่งทางโทรศัพท์ได้ถ้ามีผู้ติดต่อประจำและบันทึกการโทร
- ผู้ค้าส่งของพร้อม invoice หรือ D/O ผู้ขอซื้อเซ็นรับแล้วทำ **Partial Delivery Receipt (PDR)** ส่งบัญชีจ่ายเงินตามงวด สำเนาให้จัดซื้อ update เอกสารบริษัทกับผู้ค้าต้องตรงกันเสมอ
- ตัวอย่าง PDR (สายพาน BO 60,000 เส้น):

| งวด | วันที่ | ก่อนส่ง | รับครั้งนี้ | คงเหลือ |
|---|---|---|---|---|
| BO 0123/1 | 23 มี.ค. 2546 | 60,000 | 2,500 | 57,500 |
| BO 0123/2 | 15 เม.ย. 2546 | 57,500 | 5,000 | 52,500 |

ตรวจเลข (derived): 60,000 - 2,500 = 57,500; 57,500 - 5,000 = 52,500 ถูกต้อง

### Price hold (SPO p.92)

ผู้ค้าไม่อยากยืนราคาตลอดอายุ BO แต่ผู้ซื้อต้องการความแน่นอน หนังสือเสนอ clause: ยืนราคาตามช่วงวันที่กำหนด ปรับขึ้น/ลงได้ทั้งสองฝ่ายเมื่อมีเหตุผลทางเศรษฐกิจที่ประกาศโดยสื่อหรือรับรองโดยสมาคม/หน่วยราชการ และต้องเปลี่ยนเกิน **±X%** (เว้นให้กรอก)

### Blanket Order ของ SPO เทียบ RBMM

- RBMM ใช้ Blanket Order เป็นกลไกให้งานนอกแผนมีอะไหล่โดยไม่แบกค่าถือครอง และอธิบายว่า "ผู้ขายเก็บอะไหล่ในคลังเรา คิดเงินเมื่อเบิก" (RBMM p.289, p.298) ดู [[Spare Parts Management]] และ [[Maintenance Cost Structure]] SPO เห็นตรงกันเรื่องเป้าหมาย (ลดสต็อกและงานเอกสาร) และแนะนำ BO สำหรับของหมุนเร็วและของใช้ทั่วไป (SPO p.105, p.107)
- **ความต่างของศัพท์:** BO ของ SPO คือสัญญาซื้อทั้งปีที่ทยอยรับของด้วย BOR (ของอยู่ที่ผู้ค้า จ่ายเงินตามงวดที่รับ) ส่วนกลไก "ผู้ค้านำของมาฝากในคลังผู้ซื้อ วางบิลเมื่อจ่ายออก" SPO เรียกว่า **Consignment** (SPO p.95) คำอธิบาย BO ของ RBMM จึงตรงกับ Consignment ของ SPO มากกว่า เป็นความต่างของการใช้คำ ไม่ใช่ข้อเท็จจริงขัดกัน (การตีความของ wiki; ไม่ตั้ง contested) ดู [[SPO vs RBMM Spare Parts Approaches]]
- Lead Time: RBMM นับ Lead Time จาก PR จนของพร้อมในคลัง (RBMM p.247) BO/System Contract ตัดขั้นตอนสืบราคา-ออก PO ต่อครั้งออก จึงเหลือเฉพาะเวลาส่งของตามใบสั่งย่อย (derived) ลด Lead Time และ sigma_LT ที่ใช้ใน [[EOQ and Reorder Point]]

## System Contracting (SPO p.92, p.94)

- สัญญาครอบคลุมหลายรายการในกลุ่มพัสดุเดียวกัน ระบุราคา lead time และรับประกันว่าผู้ค้ามีสต็อกพร้อมส่ง ผู้ซื้อต้องมีรายการ spec ความรับผิดชอบ จำนวน และเงื่อนไขที่ประนีประนอม
- ขั้นตอน: ผู้ใช้สั่งตรงกับผู้ค้าด้วยใบสั่งย่อย (Delivery Order Release / Partial Delivery Release) -> ผู้ค้าส่งของพร้อม D/O, packing list, invoice อ้างเลขใบสั่งย่อย -> ผู้รับตรวจคุณภาพ/จำนวนแล้วเซ็นทุกรายการ = **ใบ Tally** -> ส่งให้แผนกจ่ายเงินทุกสิ้นวันหรือตามตกลง
- แผนกจ่ายเงินทำ **3-way check**: (1) ต้นฉบับจากผู้รับของ (2) ใบเรียกเก็บของผู้ค้า (3) ราคาตามสัญญา
- ต่างจาก BO: รายการมากกว่าหรือไม่กำหนดรายการ และมีสัญญากำกับ PO
- เป็นรากฐานของ JIT: มั่นใจพอจะทำ **zero stock** รายการนั้น ใช้แพร่หลายในกลุ่มน้ำมันและรถยนต์ในสหรัฐฯ

ผลดี 5 ข้อ:
1. ลดพัสดุคงคลังมาก บางรายการไม่ต้องสต็อก
2. ลดงานจัดซื้อ ซื้อ-ส่งเร็ว
3. ราคาดีกว่าซื้อรายครั้ง เพราะต่อรองได้และรู้โครงสร้างราคา
4. รู้ความต้องการและราคาแน่นอน คำนวณต้นทุนแม่น ใช้ JIT/MRP ได้ดีขึ้น
5. ใช้ราคาสัญญาเป็นมาตรฐานสืบราคา/ประมูลงานที่โครงสร้างราคาคล้ายกัน

## Consignment vs Vendor Stocking (SPO p.95)

| | Consignment (สินค้าฝากขาย) | Vendor Stocking |
|---|---|---|
| ของอยู่ที่ | คลังผู้ซื้อ | สถานที่ผู้ค้า จนกว่าผู้ซื้อแจ้งส่ง |
| จ่ายเงิน | เฉพาะจำนวนที่จ่ายออก (ผู้ค้ามาตรวจนับแล้ววางบิล เติมให้เต็มระดับเดิม) | ตกลงซื้อแล้ว อาจจ่ายตามงวดไม่ว่าส่งแล้วหรือยัง อาจมีค่าเก็บถ้าเกินเวลา |
| ผู้คุมระดับคงคลัง | ผู้ค้า | ผู้ค้าเก็บ ผู้ซื้อสั่งปล่อย |
| เงื่อนไข/ตัวอย่าง | ใช้ได้เมื่อตลาดเป็นของผู้ซื้อ | สินค้าอันตราย, สินค้ารอส่งต่างประเทศ |

- คลังบันทึกสต็อกการ์ดว่าของ consignment จ่ายออกชาร์จบัญชีใด แล้วใส่รหัสบัญชีใน Payment Order
- SPO ถือว่า Consignment เป็น Vendor Stocking แบบหนึ่งที่ของอยู่ที่ผู้ซื้อ; สารอันตรายมากแนะนำให้ซื้อแล้วฝากผู้ขายเก็บ ดู [[Warehouse Design and Storage]]

## Outsourcing (SPO p.96-97)

- หลัก: ใช้ผู้ชำนาญภายนอกเมื่อได้คุณภาพดีกว่าและถูกกว่า เริ่มจากงานที่ไม่ใช่ core เพราะทำเองต้องลงทุนเครื่องมือและบริหารคน
- เกณฑ์ความเสี่ยง 3 ด้าน (งานที่ outsource ต้องไม่เสี่ยงด้านเหล่านี้):
  1. บริการต่อเนื่อง: ผู้รับเหมาหยุดงานแล้วกระทบกระบวนการข้างเคียงมาก
  2. การควบคุมต้นทุน/การเปิดเผยข้อมูลราคา
  3. สูตรการผลิต/คุณสมบัติพิเศษของสินค้า (เสียเปรียบทางการตลาด)
- ตัวอย่างงาน: จัดซื้อ บริหารวัสดุ คลังสินค้า กระจายสินค้า Salvage and Disposal, งานเอกสาร, พิธีการศุลกากร, ซ่อมบำรุง (เครื่องจักร ยานยนต์ อาคาร ระบบบำบัดน้ำเสีย) งานซ่อมบำรุงมีโอกาส outsource สูงเพราะมีผู้รับจ้างมาก
- ข้อแนะนำ: (1) outsource บางส่วนได้ (2) ต้องพิสูจน์ว่าดีกว่าจริง เทียบราคาผู้รับเหมากับค่าใช้จ่ายรวมของการทำเอง (3) คิดการใช้ทรัพยากรทั้งหมด (สาธารณูปโภค คน เวลา ทรัพย์สิน)
- มุมมอง RBMM: Outsource อยู่ในหมวด Materials และไม่ควรมีในงานนอกแผน ดู [[Maintenance Cost Structure]] การตัดสินใจ in-house vs outsource ของงาน turnaround ดู [[Turnaround Management]]

## การควบคุม Air Freight (SPO p.97-98)

- ผู้อนุมัติ: ผู้บริหารระดับ Management Executive ที่คุมค่าใช้จ่ายคลังและซ่อมบำรุง สูงกว่าผู้จัดการคลังและผู้จัดการซ่อมบำรุง **1 ระดับ** อนุมัติเฉพาะกรณีฉุกเฉินจากเหตุสุดวิสัยที่จะเสียหายร้ายแรงต่อโรงงาน ผลิตภัณฑ์ หรือโอกาสทางธุรกิจ
- อนุมัติเฉพาะจำนวนที่ด่วน: ต้องการ Boiler Tubes 20 เส้นจากที่สั่ง 100 เส้น ให้ air freight แค่ 20 เส้น (ส่วน 80 เส้นที่เหลือส่งทางปกติ, derived)

แนวปฏิบัติ 6 ข้อ:
1. PR ที่ขอ air freight ต้องมีเหตุผลประกอบ
2. ผู้ขอแนะนำสายการบิน; Purchasing Traffic แนะนำเที่ยวบินตรง (ต่อเครื่องเสี่ยงของหาย ส่งผิดเมือง หีบห่อเสีย ล่าช้า)
3. ผู้อนุมัติลงชื่อย่อกำกับคำว่า "Air Freight" กันการเติมคำภายหลัง
4. คลังยืนยันว่าไม่มีของในสต็อกหรือรายการค้างรับ
5. จัดซื้อตรวจตัวแทนในประเทศก่อน (อาจมีของและถูกกว่า)
6. บันทึกค่า air freight ของใหญ่/หนักรายปี เพื่อวิเคราะห์สาเหตุความเร่งด่วนและป้องกัน

## การเรียกร้องสินค้าชำรุด (Claims against Carriers & Suppliers) (SPO p.98-100)

- ผู้ค้าในประเทศ: จัดซื้อเป็นผู้เรียกร้องแทนบริษัท คลังเตรียมหลักฐาน (ข้อมูลรับ รูปถ่าย) ข้อตกลงอื่นนอกจากส่งของทดแทน (หักเงิน ยกเลิก) ต้องได้อนุมัติ คืนของต้องมีใบผ่านประตูหมายเหตุ "Returned for Credit"
- ผู้ค้าต่างประเทศ: ความรับผิดและประกันภัยดูตาม Incoterms มี 3 กรณี
  1. **ชำรุด**: ต้องพิสูจน์ว่าชำรุดก่อนถึงมือผู้ซื้อ ตรวจทันทีเมื่อพบหีบห่อเสียหาย ถ่ายรูป/วิดีโอ มีพยาน (ศุลกากร การท่าเรือ) เรียกร้องช้าหรือใช้ของแล้วอาจถูกปฏิเสธ
  2. **ของขาด**: รายงานทันที รับตามจำนวนจริง จ่ายเฉพาะของดีที่ได้รับ แจ้งผู้ค้าชดเชย
  3. **ของเกิน (over shipment)**: รับเข้าสต็อกแล้วราคาต่อหน่วยลด พัสดุ MRO ใช้วิธีเฉลี่ยราคาได้ ส่วนสินค้าซื้อมาขายไปอาจมีปัญหาบัญชีต้องส่งคืน
- การบันทึก: มี Claim Number; บัญชีได้สำเนาเพื่อระงับการจ่ายเงิน; เรียกค่าเสียหายเป็นเงินเฉพาะกรณีร้ายแรง; ไม่มีหลักฐาน = ไม่ได้ชดเชย; รายงาน **Status of Claims** รายเดือน; เรื่องมูลค่าน้อยละเว้นได้ (SPO p.99) แบบฟอร์ม Statement of Claim อยู่ที่ SPO p.100

## มุมมอง MPM: การจ้างเหมางานบำรุงรักษาและศัพท์สัญญา (เพิ่ม 2026-10-28)

- การจ้างเหมางานบำรุงรักษาทั้งระบบ (รูปแบบสัญญา Cost Plus / Lump sum + อัตราเพิ่ม / Performance Base, เมทริกซ์ Criticality x Responsibility, Off Balance Sheet Mode, 6 ขั้นตอนจ้างเหมา, make-or-buy ด้วย Full Cost Rate) อยู่ที่ [[Maintenance Outsourcing]] ตาม [[Maintenance Profit Maker Book]] บทที่ 6 — หัวข้อ Outsourcing ข้างบนเป็นมุมมองคลัง/จัดซื้อของ SPO
- ศัพท์ของ MPM ตรงกับ SPO: **Blanket Order** = ซื้อเป็นก้อนล่วงหน้า ใช้กับรายการเคลื่อนไหวเร็ว-ปานกลางแบบ Min-Max (MPM p.88); **Consignment Stock** = ผู้ขายเก็บอะไหล่ไว้ที่คลังเรา จ่ายเงินเมื่อเบิกใช้ (MPM p.90)
- จึงยืนยันว่าคำอธิบาย Blanket Order ของ RBMM (RBMM p.289, p.298) คือกลไก Consignment ของ SPO/MPM เป็นความต่างของการใช้คำในหนังสือ RBMM ไม่ใช่ข้อเท็จจริงขัดกัน (ไม่ตั้ง contested)

## เชื่อมโยงกับ compressor failure hierarchy

- อะไหล่ compressor ที่ lead time ยาวหรือ spec ซับซ้อน (เช่น valve, packing, seal ของ [[Reciprocating Compressor]]) เข้าเกณฑ์รายการสำคัญราว 200 รายการของขั้นตอนจัดซื้อเชิงรุก ที่ควรมี spec sheet และ Specification No. (การตีความของ wiki ไม่ใช่ข้อมูลในหนังสือ)
- ชิ้นส่วนสิ้นเปลืองที่ใช้ร่วมหลายเครื่อง (O-ring, gasket, bearing) เหมาะกับ BO/System Contract ส่วนของวิกฤต lead time ยาวยังต้องสต็อกเองตาม [[Spare Part Criticality and Risk]] (การตีความ) ไม่มีข้อมูลจัดซื้อจริงของ [[Compressor]] ใน sources

## ดูเพิ่ม

- [[Spare Parts Optimization Book]]
- [[MRO Inventory Control Methods]]
- [[Spare Parts Management]]
- [[EOQ and Reorder Point]]
- [[MRO Material Classification]]
- [[Warehouse Design and Storage]]
- [[SPO vs RBMM Spare Parts Approaches]]
- [[Maintenance Cost Structure]]
- [[Maintenance Outsourcing]]
- [[Maintenance Profit Maker Book]]

## Triplets

- [[MRO Purchasing and Contracting]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 8 (SPO p.85-100)
- [[MRO Purchasing and Contracting]] [related_to:: [[Spare Parts Management]]]
- [[MRO Purchasing and Contracting]] [related_to:: [[MRO Inventory Control Methods]]]
- Purchase Requisition [has_part:: Account Code] Inventory A/C, expense code, investment code (SPO p.87)
- Purchase Requisition [has_part:: Nomenclature] main name first, then modifiers (SPO p.87-88)
- No Substitution Permit [differs_from:: Or Equivalent] forbids vs allows equivalent brand on PR (SPO p.88)
- Purchasing Engineer [applies_to:: MRO Purchasing] proposed for firms buying many parts and tools (SPO p.86)
- Flange PR Example [contradicts:: ASME B16.5 Pressure Class] book writes 150 psi; 150 is a class, general knowledge [confidence:: low]
- Up-stream Purchasing [has_part:: Specification Sheet] for critical items, quoted by Specification No. (SPO p.88-89)
- Up-stream Purchasing [has_value:: about 10,000 to about 200 items] filter of purchase history to critical items (SPO p.88)
- Up-stream Purchasing [uses:: Purchase History] 2-3 years or more (SPO p.88)
- Blanket Order [has_value:: 60% of PRs, 5% of value] PRs under 300 USD each (SPO p.91)
- Blanket Order [has_value:: 1966] started by large US firms, February 1966 (SPO p.91)
- Blanket Order [has_parameter:: Delivery Option] 5 options, quantity and or time based (SPO p.91)
- Blanket Order Release [step_of:: Blanket Order] numbered BO No. + sequence, e.g. 0123/1 (SPO p.92)
- Partial Delivery Receipt [step_of:: Blanket Order] sent to accounts for payment per delivery (SPO p.92-93)
- Partial Delivery Receipt [has_value:: 60,000 to 57,500 to 52,500] example deliveries 2,500 and 5,000 (SPO p.93)
- Blanket Order [has_parameter:: Price Hold Clause] adjustable both ways beyond ±X% on published economic grounds (SPO p.92)
- Blanket Order [differs_from:: Consignment] SPO BO = annual order with releases; RBMM describes BO as vendor stock in our store billed on issue, which matches SPO Consignment; terminology, not contested (RBMM p.289, SPO p.95)
- Blanket Order [applies_to:: Fast Moving] recommended for fast movers and general items (SPO p.105, p.107)
- System Contracting [differs_from:: Blanket Order] more or open item list, governed by contract (SPO p.94)
- System Contracting [uses:: Tally Sheet] receiver signs each item of release order (SPO p.94)
- System Contracting [uses:: 3-way Check] receiver original, supplier bill, contract price (SPO p.94)
- System Contracting [produces:: Zero Stock] basis of JIT (SPO p.94)
- System Contracting [has_value:: 5 benefits] lower inventory, less purchasing work, better price, cost certainty, price benchmark (SPO p.94)
- Consignment [is_a:: Vendor Stocking] goods held at buyer site, paid on issue (SPO p.95)
- Vendor Stocking [applies_to:: Hazardous Materials] also goods awaiting export; goods held at vendor (SPO p.95)
- Outsourcing [depends_on:: Service Continuity Risk] also cost/price disclosure and formula/product secret risks (SPO p.96)
- Outsourcing [applies_to:: Non-core Work] maintenance work has high outsourcing potential (SPO p.96-97)
- Air Freight Approval [depends_on:: Management Executive] one level above store and maintenance managers (SPO p.97)
- Air Freight Approval [has_value:: 20 of 100 boiler tubes] approve only the urgent quantity (SPO p.97)
- Air Freight Control [has_value:: 6 rules] (SPO p.97-98)
- Claim Handling [uses:: Claim Number] with Status of Claims monthly report (SPO p.99)
- Claim Handling [depends_on:: Evidence] no evidence, no compensation (SPO p.99)
- Over Shipment [uses:: Average Pricing] for MRO items (SPO p.98-99)
- Blanket Order [related_to:: Lead Time] removes per-order quotation and PO steps, derived [confidence:: low]
- [[MRO Purchasing and Contracting]] [related_to:: [[Maintenance Outsourcing]]] maintenance outsourcing strategy, MPM chapter 6
- Blanket Order [has_category:: bulk purchase in advance] MPM meaning, same as SPO (MPM p.88)
- Consignment Stock [alias_of:: Consignment] vendor stock at our store, paid on issue (MPM p.90)
- RBMM Blanket Order Usage [maps_to:: Consignment] terminology difference confirmed by MPM and SPO, not contested (RBMM p.289, MPM p.90, SPO p.95)

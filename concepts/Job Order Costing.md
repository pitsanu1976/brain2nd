---
title: Job Order Costing
created: 2026-10-20
updated: 2026-10-28
type: concept
tags: [cost, budget, maintenance-management, book, mpm]
sources: [reliability-based-maintenance-management.md, maintenance-profit-maker.md]
confidence: medium
contested: false
---

# Job Order Costing

**Job Order Costing** คือระบบบัญชีเพื่อการบริหาร (Managerial Accounting) ที่เก็บต้นทุนต่อใบสั่งงาน (Job) เหมาะกับธุรกิจบริการบำรุงรักษาเพราะบริการไม่มีสินค้าคงคลัง ใช้คู่กับ Partial Invoice (RBMM p.344-345) ค่าแรงเป็นต้นทุนหลักจึงคิดผ่านอัตรา Standard Direct Labor Rate (Full Fixed Cost / Man-Hrs) แล้วเก็บส่วนต่างกับค่าจริงเป็น Over/(Under) Absorption และพักส่วนที่ยังรับรู้ไม่ครบไว้ใน WIP หรือ Provision ตัวเลขทั้งหมดเป็นตัวอย่างสมมติของหนังสือ (บาท) บริบททางธุรกิจดู [[Maintenance Business Models]] ส่วนอัตราค่าแรงดู [[Maintenance Cost Structure]] หัวข้อ 10 เพิ่มนิยามและตัวอย่างจาก [[Maintenance Profit Maker Book]] (MPM เรียก O/(U) Absorption ว่า Over/(Under) Reserved)

## 1. Direct vs Indirect และ Full Cost (RBMM p.337-338)

- Full Cost = Full Fixed Cost + ค่าใช้จ่ายแปรผันตามงาน (Spare Part Usage, Outsource, Other Material Cost)
- Direct Cost: บันทึกตรงให้ Job ได้ (วัสดุ จ้างเหมา)
- Indirect Cost: บันทึกตรงไม่ได้ (เงินเดือนช่าง ค่าน้ำไฟ ค่าเช่า) ต้องกระจายตามเกณฑ์
- ค่าใช้จ่ายแต่ละ Job มี 2 ส่วน: รับรู้ตรง (วัสดุ + จ้างเหมาภายนอก) กับรับรู้ตรงไม่ได้ (ค่าแรงและค่าใช้จ่ายภายใน = Other Production Costs) (RBMM p.345)

## 2. การกระจาย Fixed Cost (RBMM p.338-342)

ลำดับ: Corporate Administration -> Business Unit -> Profit Center (มี Crews) -> Job Budget ค่าแรง = Man-Hrs x Full Fixed Cost Rate (รูป 11.10)

ทางเลือกที่ดีกว่าการกระจายก้อนรวมคือ Service Base Cost Allocation (รูป 11.11) หน่วยสนับสนุนคิดอัตราต่อหน่วยบริการ

| บริการ | สูตร |
|---|---|
| ขายและการตลาด | อัตรา x ยอดขาย |
| IT | อัตรา x ปริมาณทรัพยากรที่ใช้ |
| HR | อัตรา x Head Count |
| จัดซื้อ | อัตราต่อ PO x จำนวน PO |
| จัดการอะไหล่ | อัตราต่อใบเบิก x จำนวนเบิก |

Standard Direct Labor Rate = Full Fixed Cost / Man-Hrs ตามแผนงบ ถ้า Man-Hrs ที่เรียกเก็บได้ตรงแผนจะดูดซับ Full Fixed Cost หมด (RBMM p.340)

## 3. Job Budget (Job Pre-cal) (RBMM p.347-348)

```
ราคาขาย
 - Gross Margin
 = ต้นทุน = Materials + Outsource (ตรง)
          + Other Production Costs
          + Professional Services (= Full Fixed Cost Rate x Man-Hrs)
 -> กำไรสุทธิก่อนภาษี -> ภาษี -> กำไรสุทธิหลังภาษี
%Gross Margin = (ราคาขาย - ต้นทุน) / ราคาขาย
```

ถ้าใช้ Full Fixed Cost Rate แล้ว ค่าขายและบริหารรวมในค่าแรงอยู่แล้ว ไม่ต้องใส่ซ้ำ

## 4. Reference Cost, WIP และ Provision (RBMM p.345, 348-349)

**Reference Cost (ต้นทุนอ้างอิงตามโครงสร้าง)** = รายได้ที่รับรู้ x (1 - %Margin) เช่น Margin 20% รายได้ 100 รับรู้ต้นทุน 80 ส่งเสริมให้ทำงบก่อนทำงานเสมอ

WIP คือสินทรัพย์หมุนเวียนสำหรับบริการ เกิดเมื่อมี order และเปิด Job Order ค่าใช้จ่ายที่ไม่มีงานรองรับบันทึกเป็น WIP ไม่ได้ = Under Absorption ผลต่างระหว่างต้นทุนคำนวณกับ Reference Cost ค้างได้ 3 แบบ

| กรณี | ความหมาย |
|---|---|
| WIP Balance | ต้นทุนรับรู้ไม่ครบ เป็นสินทรัพย์ เมื่อปิดงานโอนเข้าต้นทุนทำให้กำไรลด |
| Provision for Work Due / Accrued Cost | WIP ติดลบ รับรู้ต้นทุนเกินค่าใช้จ่ายจริง ยังมีค่าใช้จ่ายค้างจ่าย |
| Provision for Loss Order | ค่าใช้จ่ายจริงเกินรายได้รับรู้ ตั้งเท่าส่วนต่างจนปิดงาน |

## 5. Over/(Under) Absorption (RBMM p.349-350)

```
O/(U) Absorption = ค่าใช้จ่ายโดยการคำนวณรวมทุกงาน - Full Fixed Cost จริงของหน่วย
(+) = Over-absorption    (-) = Under-absorption
```

เป็นดัชนีบอกความแม่นยำของการวางแผนขนาดองค์กรและสมรรถนะ คิดที่ระดับหน่วยไม่ใช่ Job เดียว (RBMM p.353) วิธีปรับ 2 แบบ ปรับที่ COGS อย่างเดียว หรือปรับ WIP/Inventory/COGS ตามสัดส่วน

## 6. ตารางคำนวณกำไร/ขาดทุน (RBMM p.351)

| รายการ | วิธีคำนวณ |
|---|---|
| ยอดขาย (Sales Order) | คำสั่งซื้อ |
| รายได้ที่รับรู้ | ตามหลักบัญชี |
| Backlog | Sales Order - รายได้ที่รับรู้ |
| ต้นทุนคำนวณ | ปริมาณ x อัตรามาตรฐาน |
| ต้นทุนอ้างอิง | รายได้ x (1 - %Margin) |
| WIP | ต้นทุนจริง - ต้นทุนอ้างอิง ถ้าเป็นบวก |
| Provision Work Due | ส่วนเดียวกันถ้าเป็นลบ |
| กำไรคำนวณ | รายได้ - ต้นทุนรับรู้ |
| กำไรหลัง WIP/Provision | กำไรคำนวณ - WIP + Provision Work Due - Provision Loss |

## 7. ตัวอย่าง 4 เดือน (RBMM รูป 11.19 p.354)

หน่วยบาท ปิดโดยปรับ O/(U) ที่ COGS

| รายการ | เดือน 1 | เดือน 2 | เดือน 3 | เดือน 4 | สะสม |
|---|---|---|---|---|---|
| ยอดขาย | - | 500,000 | - | - | 500,000 |
| รายได้ที่รับรู้ | - | 100,000 | 100,000 | 200,000 | 400,000 |
| Planned Margin 20% | - | 20,000 | 20,000 | 40,000 | 80,000 |
| ต้นทุนคำนวณ (5.1) | - | 110,000 | 92,000 | 93,000 | 295,000 |
| ต้นทุนจริง (5.2) | 30,000 | 111,000 | 95,000 | 92,000 | 328,000 |
| Cost Variance O/(U) (5.3) | (30,000) | (1,000) | (3,000) | 1,000 | (33,000) |
| ต้นทุนอ้างอิง | - | 100,000 | 80,000 | 160,000 | 320,000 |
| กำไรก่อนปรับ WIP/Provision | (30,000) | (11,000) | 20,000 | 40,000 | 80,000 |
| WIP | - | - | 15,000 | (68,000) | 8,000 |
| สำรองขาดทุน | 30,000 | 11,000 | - | - | - |
| กำไรสุทธิ | (30,000) | (11,000) | 5,000 | 108,000 | 72,000 |

ตรวจ (derived): Backlog = 500,000 - 400,000 = 100,000; Cost Variance สะสม = 295,000 - 328,000 = (33,000); WIP สะสม = 328,000 - 320,000 = 8,000; กำไรสุดท้าย = 80,000 - 8,000 = 72,000 (18.0% ของรายได้ 400,000) ตรงกับหนังสือ [ตัวเลขบางช่องในรูปพิมพ์เล็ก เดือน 1-2 แถวกำไรก่อนปรับ และเดือน 3-4 แถว WIP อาจคลาดเล็กน้อย]

### วิธีปรับตามสัดส่วน (รูป 11.21 p.357)

ต้นทุนอ้างอิงหลังปรับ = 320,000 - (33,000) x 320,000 / 295,000 = 355,797 (derived) กำไรก่อนปรับ WIP = 400,000 - 355,797 = 44,203 (11.1%) WIP สะสม = 328,000 - 355,797 = (27,797) แต่กำไรสุทธิสุดท้ายยังเท่าเดิม 72,000 (18.0%) แปลว่าวิธีปรับต่างกันที่ผลระหว่างทางเท่านั้น

หนังสือพิมพ์ผิด: สูตรที่ p.357 พิมพ์เป็น (3,300) แต่ผลลัพธ์ 355,797 สอดคล้องกับ (33,000) ตามตาราง ใช้ 33,000 ส่วนคำอธิบายรายการ (9) ในหนังสือพิมพ์ว่า (6)-(2) ตามที่พิมพ์ ควรตรวจเทียบตารางอีกครั้งก่อนนำไปใช้ (confidence medium)

## 8. Variance Analysis (RBMM p.351-353)

```
Budget Cost     = Budget Qty x Budget Rate
Calculated Cost = Actual Qty x Standard Rate
Actual Cost     = Actual Qty x Actual Rate
Efficiency (Qty) Variance = Calculated - Budget
Cost Variance             = Actual - Calculated   (= O/(U) Absorption)
Total Variance = Efficiency + Cost Variance
```

Materials และ Outsource วิเคราะห์ถึงระดับ Job ได้ตรง ส่วนค่าแรงต้องหาอัตราจริงที่ระดับ Profit Center ก่อน

## 9. รายงานและการปิด Job (RBMM p.357-358)

- ผู้จัดการ Site รายงานรายเดือน: Order Received, Revenue, Backlog, กำไร (EBIT), Cash Flow, Utilization, O/(U) Absorption และงบดุล (Provisions, ลูกหนี้, เจ้าหนี้)
- ปิด Job = รับรู้หรือปรับ WIP/Provision ของ Job นั้นทั้งหมด เมื่อทำงานครบมูลค่าและเรียกเก็บครบ หรือยกเลิก
- ใช้ Excel ดึงข้อมูลได้ แต่ข้อมูลมากหลายระบบเสี่ยงผิดพลาด จึงแนะนำ ERP ที่มี Standard Cost หรือ ABC (RBMM p.360)

## 10. มุมมอง MPM: งบและบัญชีของ Maintenance Service Profit Center (เพิ่ม 2026-10-28)

[[Maintenance Profit Maker Book]] บทที่ 7 และ 14 อธิบายกลไกเดียวกับหัวข้อ 4-6 ด้วยคำศัพท์บางคำต่างกัน ตัวเลขเป็นตัวอย่างบริษัทสมมติ XYZ (M฿)

### 10.1 องค์ประกอบงบ/รายงาน (MPM p.133-134)

- บริการเก็บเป็นสินค้าคงคลังรอขายไม่ได้ เตรียมทรัพยากรมากขายน้อยต้นทุนสูง เตรียมน้อยขายไม่พอ ทรัพยากรที่รอให้บริการ = ค่าใช้จ่ายคงที่
- **เป้ายอดขาย** = คำสั่งซื้อที่ได้รับในงวด; **รายได้** = ค่าบริการตาม Invoice ในงวด (ตรงกับ Sales Order vs รายได้ที่รับรู้ในหัวข้อ 6); งานบริการมี **ภาษีหัก ณ ที่จ่าย** ที่ผู้จ้างหักนำส่งรัฐ
- รายงานงบดุล (เครื่องมือ, อะไหล่, ลูกหนี้การค้า), รายงานกำไรขาดทุน (รวมต้นทุนการเงิน ค่าเสื่อม) และค่าใช้จ่ายการผลิต (บริการ + วัสดุ)
- วิธีคิดต้นทุนค่าแรง 5 ขั้น: (1) ค่าแรงมาตรฐาน x ชั่วโมง-คนทั้งหมดที่ใช้ (2) คำนวณ Over/(Under) Reserved (3) ลงค่าใช้จ่ายตามสัดส่วนที่ Invoice แล้ว (4) ส่วนที่ยังไม่ Invoice เปลี่ยนเป็น WIP (5) ตั้ง Provision for Loss Orders และ Provision for Work Due

### 10.2 WIP และ Provision ตามนิยาม MPM (MPM p.136-137, 261)

| รายการ | นิยาม MPM |
|---|---|
| **WIP** | = อัตราค่าแรงมาตรฐาน x ชั่วโมง ลงเป็นทรัพย์สินหมุนเวียน; ส่วนที่ยังไม่ Invoice รอตัดเป็นรายจ่ายเมื่อออก Invoice เพิ่ม; Change in WIP คือต้นทุน (MPM p.136, 261) |
| **Provision for Work Due** | สำรองค่าใช้จ่ายที่เหลือที่น่าจะเกิดของงานที่ยังไม่เสร็จ ระบบตั้งอัตโนมัติเมื่อเทียบสัดส่วนรายได้ที่เรียกเก็บแล้ว ค่าใช้จ่ายที่รวบรวมได้ต่ำกว่าประมาณการ (MPM p.136-137) |
| **Provision for Loss Order** | ระบบตั้งอัตโนมัติเมื่อค่าใช้จ่ายที่บันทึกมากกว่ารายได้ = ตีความว่างานจะขาดทุน (MPM p.137) |

- ทั้งสองต้องมีประมาณการ (งบ) ของทุกงานล่วงหน้า; ผู้เขียนเปรียบการตั้งสำรองเป็น "เรดาร์นำทาง" ที่ทำพร้อมปิดบัญชีทุกงวด และทำให้งบดุล conservative เสมอ ถ้าไม่มีระบบงบจะตั้งสำรองไม่ได้ (MPM p.137-139)
- สอดคล้องกับหัวข้อ 4 (RBMM): Provision for Work Due ของ MPM = WIP ติดลบ / Accrued Cost ของ RBMM มองจากมุมเดียวกัน (รับรู้ต้นทุนตามรายได้แล้วค่าใช้จ่ายจริงยังเกิดไม่ครบ)
- **Disambiguation**: [[Maintenance Budget]] (RBMM บทที่ 10) ใช้ **Provision for Losses / Provision for Costs** = สำรองในงบประมาณของ Cost Center (เพดานความคลาดเคลื่อนของงบ) ไม่ใช่สำรองทางบัญชีต่อ Job แบบหน้านี้ ชื่อคล้ายกันแต่คนละกลไก

### 10.3 Over/(Under) Reserved และกำไรขาดทุน 2 วิธี (MPM p.134-136)

**Over/(Under) Reserved** ของ MPM = Over/(Under) Absorption ในหัวข้อ 5 (สูตร ค่าคำนวณด้วยอัตรามาตรฐาน - ค่าใช้จ่ายจริง, ลบ = Under) ดู [[Maintenance Cost Structure]] หัวข้อ 12

| วิธีอัตรามาตรฐาน + O/(U) | M฿ | วิธีค่าใช้จ่ายจริง | M฿ |
|---|---|---|---|
| รายได้ | 100.00 | รายได้ | 100.00 |
| ค่าใช้จ่ายคำนวณ (90,000 ชม. x 976.8) | (87.9) | ค่าใช้จ่ายจริงทั้งสิ้น | (96.1) |
| Over/(Under) Reserved | (8.2) | | |
| กำไร/(ขาดทุน) | 3.89 | กำไร/(ขาดทุน) | 3.89 |

- ข้อดี: เมื่อคำนวณ O/(U) ได้ จะหากำไร/ขาดทุนได้โดยไม่ต้องรอรู้ค่าใช้จ่ายทั้งหมด และรู้ว่าเตรียมทรัพยากรมาก/น้อยไป
- ตรวจ (derived): 90,000 x 976.8 = 87.91; 87.91 - 96.1 = (8.19); 100 - 96.1 = 3.9

### 10.4 จุดคุ้มทุนของบริษัทบริการ (MPM p.137-138)

```
Full Cost Rate     = Fixed Cost / (Available Man-Hrs x Utilization Factor)
Break-even Revenue = Utilized Man-Hrs x Full Cost Rate = Fixed Cost
```

- ลำดับ: กำหนด Utilization Factor -> คำนวณอัตราค่าแรงมาตรฐาน -> ตั้งราคาขายด้วยอัตรากำไร
- ตัวอย่าง XYZ เป็นบริษัทบริการไม่ขายอะไหล่: ค่าคงที่ 96.1 M฿/ปี, 196,800 ชม. x 50% = 98,400 ชม., อัตรา 976.8 บาท/ชม. -> ต้องขาย **98,400 ชม.** = รายได้ 96.1 M฿ จึงคุ้มทุน; ต้องการกำไรต้องขายค่าแรงสูงกว่านี้
- ค่าแรงมาตรฐานแปรผันตาม Utilization Factor โดยตรง ธรรมชาติเดียวกับธุรกิจที่กักตุนสินค้าไม่ได้ (ไฟฟ้า การบิน ขนส่ง) ผู้ที่ถูกกว่าคือผู้มีทรัพยากรถูกกว่าและ/หรือ Utilization สูงกว่า (MPM p.137)
- หัวใจงบของธุรกิจบริการคือสมมติฐาน Utilization Rate ของกำลังคน (MPM p.138-139)
- ข้อสังเกต (derived): ตัวอย่างนี้ใช้อัตรา 976.8 (ไม่รวมค่าครอบครองอะไหล่) ขณะที่ตัวอย่างทำเองใน [[Maintenance Budget]] หัวข้อ 9.9 ใช้ 1,506.4 (รวมต้นทุนการเงินอะไหล่) สองฐานต่างกันโดยเจตนา ควรระบุเมื่อนำไปใช้; รูป 7.17 พิมพ์ 1,508.4 แต่ 148.2M / 98,400 = 1,506.1

## เชื่อมโยงกับ compressor failure hierarchy

หนังสือไม่เชื่อม Job Order Costing กับ [[OREDA]] หรือ [[ISO 14224]] โดยตรง แนวใช้ประโยชน์ (ข้อเสนอของ wiki):
- Job หนึ่งงานเทียบได้กับ Work Order ซ่อม compressor หนึ่งใบ ที่ผูกกับ [[Maintainable Item]] และ [[Failure Mode]] ทำให้ได้ต้นทุนต่อ failure mode
- ต้องบันทึก Man-Hrs, อะไหล่ และ Outsource ต่อ Job เพื่อวิเคราะห์ Variance ได้ ดู [[CMMS]]

## ดูเพิ่ม

- [[Maintenance Business Models]]
- [[Maintenance Cost Structure]]
- [[Maintenance Budget]]
- [[Maintenance Strategic Report]]
- [[Reliability Based Maintenance Management Book]]
- [[Maintenance Profit Maker Book]]

## Triplets

- [[Job Order Costing]] [is_a:: Managerial Accounting] cost per Job (RBMM p.344-345)
- [[Job Order Costing]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 11
- [[Job Order Costing]] [applies_to:: Maintenance Service Business] no inventory of goods (RBMM p.344-345)
- [[Job Order Costing]] [uses:: Partial Invoice] (RBMM p.344-345)
- [[Job Order Costing]] [uses:: Standard Direct Labor Rate]
- [[Job Order Costing]] [related_to:: [[Maintenance Business Models]]]
- Full Cost [has_formula:: Full Fixed Cost + variable job cost (Spare Part Usage, Outsource, Other Material Cost)] (RBMM p.337-338)
- Direct Cost [differs_from:: Indirect Cost] direct booked to Job (materials, outsource); indirect allocated (salaries, utilities, rent) (RBMM p.337-338)
- Other Production Costs [part_of:: Job Cost] internal labour and expenses, not directly recognised (RBMM p.345)
- Fixed Cost Allocation [has_formula:: Corporate Administration -> Business Unit -> Profit Center -> Job Budget] labour = Man-Hrs x Full Fixed Cost Rate (RBMM Fig 11.10)
- Service Base Cost Allocation [differs_from:: Lump Sum Allocation] better option (RBMM Fig 11.11)
- Sales and Marketing Allocation [has_formula:: rate x sales] (RBMM p.338-342)
- IT Allocation [has_formula:: rate x resources used] (RBMM p.338-342)
- HR Allocation [has_formula:: rate x Head Count] (RBMM p.338-342)
- Purchasing Allocation [has_formula:: rate per PO x number of PO] (RBMM p.338-342)
- Spare Handling Allocation [has_formula:: rate per issue x number of issues] (RBMM p.338-342)
- Standard Direct Labor Rate [has_formula:: Full Fixed Cost / budgeted Man-Hrs] (RBMM p.340)
- Standard Direct Labor Rate [alias_of:: Full Fixed Cost Rate]
- Job Budget [alias_of:: Job Pre-cal] (RBMM p.347-348)
- Job Cost [has_formula:: Materials + Outsource + Other Production Costs + Professional Services] (RBMM p.347-348)
- Professional Services [has_formula:: Full Fixed Cost Rate x Man-Hrs] (RBMM p.347-348)
- Gross Margin [has_formula:: (selling price - cost) / selling price] %Gross Margin (RBMM p.347-348)
- Reference Cost [has_formula:: recognised revenue x (1 - %Margin)] e.g. margin 20%, revenue 100 -> cost 80 (RBMM p.345, 348-349)
- WIP [is_a:: Current Asset] for services, arises when Job Order opened (RBMM p.348-349)
- WIP Balance [has_category:: asset] cost not fully recognised (RBMM p.348-349)
- Provision for Work Due [alias_of:: Accrued Cost] negative WIP (RBMM p.348-349)
- Provision for Loss Order [depends_on:: Actual Cost] actual cost exceeds recognised revenue (RBMM p.348-349)
- Over/(Under) Absorption [has_formula:: total calculated cost of all jobs - actual Full Fixed Cost of unit] (+) Over, (-) Under (RBMM p.349-350)
- Over/(Under) Absorption [applies_to:: Unit Level] not single Job (RBMM p.353)
- Over/(Under) Absorption [measures:: accuracy of organisation sizing and performance] (RBMM p.349-350)
- Backlog [has_formula:: Sales Order - recognised revenue] (RBMM p.351)
- Calculated Cost [has_formula:: Actual Qty x Standard Rate] (RBMM p.351-353)
- WIP [has_formula:: actual cost - reference cost] if positive (RBMM p.351)
- Calculated Profit [has_formula:: revenue - recognised cost] (RBMM p.351)
- Profit After WIP/Provision [has_formula:: calculated profit - WIP + Provision Work Due - Provision Loss] (RBMM p.351)
- Budget Cost [has_formula:: Budget Qty x Budget Rate] (RBMM p.351-353)
- Actual Cost [has_formula:: Actual Qty x Actual Rate] (RBMM p.351-353)
- Efficiency Variance [has_formula:: Calculated - Budget] (RBMM p.351-353)
- Cost Variance [has_formula:: Actual - Calculated] equals O/(U) Absorption (RBMM p.351-353)
- Total Variance [has_formula:: Efficiency + Cost Variance] (RBMM p.351-353)
- 4-Month Example [has_value:: sales 500,000; revenue 400,000; backlog 100,000 THB] (RBMM Fig 11.19 p.354)
- 4-Month Example [has_value:: calculated cost 295,000; actual 328,000; Cost Variance (33,000) THB] (RBMM Fig 11.19 p.354)
- 4-Month Example [has_value:: WIP 8,000; net profit 72,000 THB (18.0%)] adjust O/(U) at COGS (RBMM Fig 11.19 p.354)
- Proportional Adjustment Example [has_value:: reference cost 355,797; profit before WIP 44,203 (11.1%); WIP (27,797) THB] same final profit 72,000 (RBMM Fig 11.21 p.357)
- Proportional Adjustment Example [has_value:: (33,000)] used by wiki, book formula misprints (3,300) (RBMM p.357)
- Site Monthly Report [uses:: Order Received, Revenue, Backlog, EBIT, Cash Flow, Utilization, O/(U) Absorption] plus balance sheet (RBMM p.357-358)
- [[Job Order Costing]] [uses:: ERP] with Standard Cost or ABC recommended over Excel (RBMM p.360)
- Materials [applies_to:: Job Level Variance] Materials and Outsource analysed per Job; labour at Profit Center first (RBMM p.351-353)
- [[Job Order Costing]] [defined_in:: [[Maintenance Profit Maker Book]]] chapters 7 and 14, service profit centre (MPM p.133-138, 261-262)
- Sales Target [differs_from:: Revenue] orders received vs invoiced in period (MPM p.133)
- Service Revenue [has_category:: withholding tax] deducted by client (MPM p.133)
- Service Labour Costing [has_value:: 5 steps] standard rate x hours, O/(U) Reserved, expense by invoiced share, rest to WIP, provisions (MPM p.134)
- WIP [has_formula:: standard labour rate x hours] asset until invoiced (MPM p.261)
- Provision for Work Due [has_formula:: expected remaining cost of unfinished work] when collected cost is below estimate for invoiced share (MPM p.136-137)
- Provision for Loss Order [depends_on:: Actual Cost] auto when recorded cost exceeds revenue (MPM p.137)
- Provision for Work Due [depends_on:: Job Estimate] every job needs a budget first (MPM p.137-139)
- Provision for Loss Order [differs_from:: Provision for Losses] MPM job provision vs RBMM budget provision in [[Maintenance Budget]]
- Over/(Under) Reserved [alias_of:: Over/(Under) Absorption] (MPM p.134-136)
- Over/(Under) Reserved [has_value:: (8.2) M THB] 90,000 h x 976.8 = 87.91 vs actual 96.1; profit 3.89 either method (MPM p.135-136)
- Break-even Revenue [has_formula:: Utilized Man-Hrs x Full Cost Rate = Fixed Cost] (MPM p.138)
- Service Break-even [has_value:: 98,400 h] x 976.8 THB = 96.1 M THB, XYZ service company without spares (MPM p.138)
- Full Cost Rate [depends_on:: Utilization Factor] directly (MPM p.137)

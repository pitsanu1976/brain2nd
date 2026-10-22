---
title: Job Order Costing
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [cost, budget, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Job Order Costing

**Job Order Costing** คือระบบบัญชีเพื่อการบริหาร (Managerial Accounting) ที่เก็บต้นทุนต่อใบสั่งงาน (Job) เหมาะกับธุรกิจบริการบำรุงรักษาเพราะบริการไม่มีสินค้าคงคลัง ใช้คู่กับ Partial Invoice (RBMM p.344-345) ค่าแรงเป็นต้นทุนหลักจึงคิดผ่านอัตรา Standard Direct Labor Rate (Full Fixed Cost / Man-Hrs) แล้วเก็บส่วนต่างกับค่าจริงเป็น Over/(Under) Absorption และพักส่วนที่ยังรับรู้ไม่ครบไว้ใน WIP หรือ Provision ตัวเลขทั้งหมดเป็นตัวอย่างสมมติของหนังสือ (บาท) บริบททางธุรกิจดู [[Maintenance Business Models]] ส่วนอัตราค่าแรงดู [[Maintenance Cost Structure]]

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

---
title: Maintenance Business Models
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [maintenance-management, cost, budget, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Maintenance Business Models

บทที่ 11 ของ RBMM เปรียบเทียบรูปแบบองค์กรบำรุงรักษา 3 แบบ ได้แก่ **Cost Center** (ศูนย์ค่าใช้จ่ายภายใน), **Profit Centered Maintenance** (หน่วยภายในที่ทำงานเชิงธุรกิจ) และ **Maintenance Service Company** (บริษัทบริการเต็มรูป) พร้อมข้อเตือนว่าการแปลงเป็นเชิงธุรกิจล้มเหลวได้ง่ายเพราะ Change Management และระบบบัญชีไม่พร้อม (RBMM p.321-329, 359) ผู้เขียนมองว่า Cost Center ที่มีระบบดีก็คุมได้ ส่วนกลไกบัญชีของแบบธุรกิจอยู่ใน [[Job Order Costing]] และอัตราค่าแรงอยู่ใน [[Maintenance Cost Structure]]

## 1. เปรียบเทียบ 3 รูปแบบ

| หัวข้อ | Cost Center | Profit Centered (ภายใน) | Service Company |
|---|---|---|---|
| วัดผลด้วย | OEE, ต้นทุนรวมต่อเครื่อง, Maintenance Cost/Unit (RBMM p.326) | กำไร/ขาดทุน ต่อ Site | กำไร/ขาดทุน (RBMM p.329) |
| รายได้ | ไม่มี (ค่าใช้จ่ายอย่างเดียว) | โอนภายในตามสัญญา | จากลูกค้า (Order) |
| งบ | Performance Budget ([[Maintenance Budget]]) | Job Budget + งบดุล/P&L | Job Budget ทุก Job |
| ความเสี่ยง | ต่ำ | สูงขึ้น: ลำดับความสำคัญหลัก/รอง สับสน | Cash Flow ค่าใช้จ่ายเกิดก่อน Order |
| ข้อเตือน | ผลตอบแทนแยกจาก cost center อื่นไม่ได้ (RBMM p.325) | ผู้เขียนเตือนว่าอาจผิดพลาดมากถ้าหวังหารายได้ภายนอก (RBMM p.327) | ต้องมี Service Business Process และ Managerial Accounting |

ข้อเสนอท้ายบท: ควรมีสัญญาจ้างรวมระยะยาวแบบ Performance Based Contract พร้อมเป้าท้าทาย Win-Win แล้วค่อยแยกเป็นบริษัทบริการเต็มรูป (RBMM p.329)

## 2. Cost Center: ระบบที่หนังสือใช้ (RBMM p.325-326)

Cost Center ขับเคลื่อนด้วย [[CMMS]] (Work Control, Scheduled PM, Spare Part Control) ป้อน 5 โมดูล

1. RCM Process (เลือก PM) — [[RCM Reliability Centered Maintenance]]
2. PM Optimization (หา interval ที่เหมาะ) — [[PM Interval Optimization]]
3. Risk Based Spare Part Optimization (Stock Max/Min) — [[Spare Part Criticality and Risk]]
4. Performance Budgeting — [[Maintenance Budget]]
5. Maintenance Strategic Report — [[Maintenance Strategic Report]]

กิจกรรมบำรุงรักษา 16 กิจกรรม (รูป 11.3 p.326) แบ่ง 4 กลุ่ม แกนตั้งคือ Criticality แกนนอนคือวงจรชีวิตงาน

| กลุ่ม | ประเภท | กิจกรรม |
|---|---|---|
| ค่าใช้จ่าย | งานนอกแผน (Breakdown) | Trouble Shooting, Component Change, Component Rebuilt, Spare Parts, Fault Recovery |
| ค่าใช้จ่าย | งานตามแผน PM | Predictive, Condition Monitoring, Preventive Maintenance, Turnaround, Preventive-Proactive |
| ลงทุน | Improvement Projects | Project Management, Commissioning, Installation, Engineering, Modification Project |
| ลงทุน | Maintenance Engineering | Audits, Reliability Improvement, Performance Improvement, Management Improvement, Maintenance Engineering |

ครึ่งแรกเป็นค่าใช้จ่าย ครึ่งหลัง (รวมระบบ CMMS) เป็นเงินลงทุน บริษัทเล็กมักลงทุนครึ่งหลังไม่ไหว (RBMM p.326)

ผลประโยชน์ที่ส่งมอบให้บริษัท 3 ข้อ: สมรรถนะเครื่องวัดเป็น OEE ([[Availability and OEE]]), ต้นทุนทั้งหมดที่ใช้กับเครื่อง (บาท), ต้นทุนบำรุงรักษาต่อหน่วยผลผลิต (RBMM p.326)

## 3. Service Business และ Service Gap (RBMM p.322-324)

- บริการไม่มีตัวตน ส่งมอบ "ความคาดหวัง" ผู้ให้บริการต้องสะสมคนและเครื่องมือล่วงหน้า ค่าใช้จ่ายคงที่เกิดก่อนมี order จึงมีมิติ "การบริหารรายได้" เพิ่ม
- Service Gap Model (รูป 11.1): Gap 1 ผู้ให้บริการไม่เข้าใจความต้องการลูกค้า (ผลรวมของ Gap 2-6), Gap 2 ผู้บริหารถ่ายทอดข้อกำหนดลงปฏิบัติไม่ได้, Gap 3 การสื่อสารภายนอกไม่ตรงความจริง, Gap 4 order คลาดเคลื่อน, Gap 5 ขาดกระบวนการควบคุมงาน, Gap 6 ผลส่งมอบไม่ตรงความคาดหวัง
- แนวแก้: ผู้ซื้อระบุ "ผลลัพธ์ (Results)" ไม่ใช่วิธีทำละเอียด เพราะรายละเอียดวิธีมากเกินทำให้ผู้ให้บริการหลบความรับผิดชอบ

## 4. Maintenance Service Company (RBMM p.329-331)

กลุ่มงานบริการ 3 ส่วน (รูป 11.4)
- In-situ: งานหน้างาน (Trouble Shooting, PM, Turnaround ฯลฯ)
- Optional Services: Installation, Engineering [ภาพจาง]
- Value Added: Plant Audits, Reliability Improvement, Performance Improvement, Maintenance Engineering

ประเด็นกลยุทธ์
- ถ้าความสามารถ engineering อยู่ที่เจ้าของโรงงาน เขาจะให้ผู้รับเหมาทำงานมูลค่าเพิ่มน้อย (ขายค่าแรง แข่งขันสูง) ถ้าอยู่ที่ผู้รับเหมาจะเสนอบริการมูลค่าเพิ่มที่ปฏิเสธยาก (Productivity ช่วงขาขึ้น, Cost Reduction ช่วงขาลง)
- รูปแบบ: Service Center, Field Services, Project/Site Management
- เรียกเก็บครั้งเดียวหรือ Partial Invoice ต้นทุนเกิดตลอด ปัญหา "ทำเกินแต่เรียกเก็บไม่ได้" แก้ด้วยบันทึกต้นทุนตามสัดส่วนที่เรียกเก็บแล้วปรับตอนสิ้นงวด
- ต้องมีทั้ง Responsibility (ทำเต็มที่) และ Accountability (ชี้แจงเหตุผลการตัดสินใจ)
- แบ่งการบริหาร: ความรู้/ข้อมูลรวมศูนย์ (Technical/Information Centralized) แต่ปฏิบัติแยกกระจาย (Operation Decentralized)

Cost Center เป็นหน่วยสนับสนุน ควบคุม Costs และ Losses; Profit Center รับผิดชอบรายได้และควบคุมต้นทุนทั้งของตนและที่รับกระจายจากหน่วยสนับสนุน (RBMM p.331-332)

## 5. ปัญหาการแปลง Cost Center -> Profit/Service (RBMM p.328, 358-360)

| ปัญหา | รายละเอียด |
|---|---|
| ขาดระบบ | ไม่มี Service Business Process และ Service Business Management Accounting |
| Change Management | ช่างรู้เทคนิค ขาดความรู้บัญชี/งบดุล ต้องสร้าง "เถ้าแก่น้อย" (Emerging Business Manager) ผ่าน Mentoring by Working Process |
| Cash Flow | รายจ่ายส่วนใหญ่เป็นเงินสดไม่ว่างานสำเร็จหรือไม่ |
| ลงทุนผิดเรื่อง | เทคโนโลยีแพงใช้ไม่คุ้ม และไม่มี Maintenance Engineering ซึ่งเป็นกุญแจ value-added |
| องค์กร | ต้องมีฝ่ายขายการตลาด (เช่น Captive Market จากบริษัทแม่) และ Productization (กำหนดสินค้า ราคา สัญญา) |
| ERP | หลายองค์กรใช้ ERP ต่ำกว่าศักยภาพ (เปรียบกับนำรถหรูมาทำ Taxi) ต้องปรับกระบวนการ ไม่ใช่ดัดแปลง ERP |

บริษัทเครือใหญ่ที่ข้ามนิติบุคคลไม่ได้ อาจตั้งหน่วยธุรกิจบำรุงรักษากลางเป็นนิติบุคคลแยกเพื่อแชร์ทรัพยากร (RBMM p.327) ระบบบัญชีที่ดีโอนค่าใช้จ่ายระหว่างหน่วยได้โดยไม่ต้องแยกนิติบุคคล

การพัฒนาผู้จัดการ Profit Center: อ่านตัวเลข Data -> Information -> Knowledge ติดตาม Cash Flow ด้วย WIP, Account Receivable-Days, Account Payable-Days; ฝ่ายบัญชีรับผิดชอบความ Complete, Accurate, In-Time ของการปิดบัญชี และบรรยากาศการประชุมควรเป็น Support/Coaching (RBMM p.358-360)

## 6. เกณฑ์เลือกรูปแบบ (สรุปจากหนังสือ ไม่ใช่สูตร)

- ถ้าเป้าคือคุมต้นทุนต่อหน่วยภายในโรงงานเดียว: Cost Center + Performance Budgeting พอเพียง
- ถ้าเป็นกลุ่มบริษัทหลายโรงงานแชร์ทรัพยากร: พิจารณา Performance Based Contract แล้วค่อยแยกบริษัท
- ถ้าจะหารายได้ภายนอก: ต้องพร้อมระบบ Job Order Costing, ERP และ Mentoring ของผู้จัดการก่อน ไม่เช่นนั้นย้อนกลับเป็น Cost Center เสียเวลาเปล่า (RBMM p.359)

## เชื่อมโยงกับ compressor failure hierarchy

หนังสือบทนี้เป็นเรื่องบัญชีและธุรกิจ ไม่มีเนื้อหาตรงกับ [[OREDA]] หรือ [[ISO 14224]] ความเชื่อมทางอ้อม:
- 16 กิจกรรมบำรุงรักษา (รูป 11.3) เป็นกรอบจัดประเภทงานและต้นทุน ไม่ใช่ taxonomy ของ failure หรืออุปกรณ์ แต่ใช้ผูกงาน Fault Recovery / Trouble Shooting / Condition Monitoring กับ [[Failure Mode]] ในการออกแบบ cost-per-failure ได้
- สัญญา Performance Based Contract สำหรับ compressor ควรนิยามผลลัพธ์ด้วยตัวชี้วัดที่วัดได้ เช่น availability หรือจำนวนครั้ง failure ตามนิยาม failure mode ของ [[ISO 14224]] (ข้อเสนอของ wiki ไม่ใช่ข้อความหนังสือ)

## ดูเพิ่ม

- [[Job Order Costing]] — กลไกบัญชีของ Profit Center และ Service Company
- [[Maintenance Budget]]
- [[Maintenance Cost Structure]]
- [[Maintenance Strategic Report]]
- [[CMMS]]
- [[Reliability Based Maintenance Management Book]]

## Triplets

- [[Maintenance Business Models]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 11 (RBMM p.321-329)
- Cost Center [is_a:: [[Maintenance Business Models]]]
- Profit Centered Maintenance [is_a:: [[Maintenance Business Models]]] internal unit run as business
- Maintenance Service Company [is_a:: [[Maintenance Business Models]]] full service company
- Cost Center [measures:: OEE, total cost per machine, Maintenance Cost/Unit] (RBMM p.326)
- Profit Centered Maintenance [measures:: profit/loss per Site]
- Maintenance Service Company [measures:: profit/loss] (RBMM p.329)
- Cost Center [uses:: [[Maintenance Budget]]] Performance Budget
- Profit Centered Maintenance [uses:: Job Budget] plus balance sheet / P&L
- Maintenance Service Company [uses:: Job Budget] every Job
- Profit Centered Maintenance [uses:: [[Job Order Costing]]]
- Maintenance Service Company [uses:: [[Job Order Costing]]]
- Cost Center [differs_from:: Profit Centered Maintenance] low risk vs confused primary/secondary priorities
- Maintenance Service Company [depends_on:: Cash Flow] costs occur before Order
- Profit Centered Maintenance [has_category:: risky if seeking external revenue] author warning (RBMM p.327)
- Performance Based Contract [step_of:: Business Model Transition] long-term, Win-Win, before full service company (RBMM p.329)
- Cost Center [uses:: [[CMMS]]] Work Control, Scheduled PM, Spare Part Control (RBMM p.325-326)
- [[RCM Reliability Centered Maintenance]] [part_of:: Cost Center] module 1 (RBMM p.325-326)
- [[PM Interval Optimization]] [part_of:: Cost Center] module 2 (RBMM p.325-326)
- [[Spare Part Criticality and Risk]] [part_of:: Cost Center] module 3, Risk Based Spare Part Optimization (RBMM p.325-326)
- [[Maintenance Budget]] [part_of:: Cost Center] module 4, Performance Budgeting (RBMM p.325-326)
- [[Maintenance Strategic Report]] [part_of:: Cost Center] module 5 (RBMM p.325-326)
- Maintenance Activities [has_value:: 16] in 4 groups, Fig 11.3 (RBMM p.326)
- Breakdown Work [is_a:: Maintenance Activities] expense; Trouble Shooting, Component Change, Component Rebuilt, Spare Parts, Fault Recovery (RBMM p.326)
- Planned PM Work [is_a:: Maintenance Activities] expense; Predictive, Condition Monitoring, Preventive Maintenance, Turnaround, Preventive-Proactive (RBMM p.326)
- Improvement Projects [is_a:: Maintenance Activities] investment; Project Management, Commissioning, Installation, Engineering, Modification Project (RBMM p.326)
- Maintenance Engineering [is_a:: Maintenance Activities] investment; Audits, Reliability, Performance and Management Improvement (RBMM p.326)
- Breakdown Work [has_category:: expense] (RBMM p.326)
- Planned PM Work [has_category:: expense] (RBMM p.326)
- Improvement Projects [has_category:: investment] (RBMM p.326)
- Maintenance Engineering [has_category:: investment] (RBMM p.326)
- Cost Center [produces:: [[Availability and OEE]]] benefit 1 of 3; also total cost per machine, maintenance cost per unit (RBMM p.326)
- Service Gap Model [has_part:: Gap 1] provider does not understand customer needs, sum of Gap 2-6 (RBMM Fig 11.1)
- Service Gap Model [has_part:: Gap 2] management cannot translate specs to operations (RBMM Fig 11.1)
- Service Gap Model [has_part:: Gap 3] external communication not true (RBMM Fig 11.1)
- Service Gap Model [has_part:: Gap 4] order mismatch (RBMM Fig 11.1)
- Service Gap Model [has_part:: Gap 5] no work control process (RBMM Fig 11.1)
- Service Gap Model [has_part:: Gap 6] delivery not matching expectation (RBMM Fig 11.1)
- Service Contract [depends_on:: Results Specification] buyer specifies results not detailed method (RBMM p.322-324)
- In-situ Services [part_of:: Maintenance Service Company] (RBMM Fig 11.4)
- Optional Services [part_of:: Maintenance Service Company] Installation, Engineering (RBMM Fig 11.4)
- Value Added Services [part_of:: Maintenance Service Company] Plant Audits, Reliability Improvement, Performance Improvement, Maintenance Engineering (RBMM Fig 11.4)
- Value Added Services [depends_on:: Engineering Capability] whoever holds engineering capability (RBMM p.329-331)
- Maintenance Service Company [uses:: Technical/Information Centralized, Operation Decentralized] (RBMM p.329-331)
- Business Model Transition [depends_on:: Service Business Process] and Service Business Management Accounting (RBMM p.328, 358-360)
- Business Model Transition [depends_on:: Change Management] Emerging Business Manager via Mentoring by Working Process (RBMM p.358-360)
- Business Model Transition [depends_on:: ERP] adapt process, not ERP (RBMM p.358-360)
- Profit Center Manager [uses:: WIP, Account Receivable-Days, Account Payable-Days] Cash Flow tracking (RBMM p.358-360)
- Single Plant Unit Cost Control [selects:: Cost Center] with Performance Budgeting
- Performance Based Contract [applies_to:: Multi-Plant Group Sharing Resources]
- [[Job Order Costing]] [applies_to:: External Revenue] prerequisite with ERP and Mentoring (RBMM p.359)

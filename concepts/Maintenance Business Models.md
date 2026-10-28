---
title: Maintenance Business Models
created: 2026-10-20
updated: 2026-10-28
type: concept
tags: [maintenance-management, cost, budget, book, mpm, outsourcing]
sources: [reliability-based-maintenance-management.md, maintenance-profit-maker.md]
confidence: medium
contested: true
---

# Maintenance Business Models

บทที่ 11 ของ RBMM เปรียบเทียบรูปแบบองค์กรบำรุงรักษา 3 แบบ ได้แก่ **Cost Center** (ศูนย์ค่าใช้จ่ายภายใน), **Profit Centered Maintenance** (หน่วยภายในที่ทำงานเชิงธุรกิจ) และ **Maintenance Service Company** (บริษัทบริการเต็มรูป) พร้อมข้อเตือนว่าการแปลงเป็นเชิงธุรกิจล้มเหลวได้ง่ายเพราะ Change Management และระบบบัญชีไม่พร้อม (RBMM p.321-329, 359) ผู้เขียนมองว่า Cost Center ที่มีระบบดีก็คุมได้ ส่วนกลไกบัญชีของแบบธุรกิจอยู่ใน [[Job Order Costing]] และอัตราค่าแรงอยู่ใน [[Maintenance Cost Structure]] หัวข้อ 7-9 เพิ่มมุมมอง [[Maintenance Profit Maker Book]] (Off Balance Sheet, กรณีบริษัทบำรุงรักษารวมศูนย์ 4 โรงงาน) และข้อขัดแย้ง MPM-C6 เรื่อง Profit Center

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

ครึ่งแรกเป็นค่าใช้จ่าย (ยกเว้น Turnaround ที่ MPM ลงเป็นทรัพย์สินตัดจ่าย ดูหัวข้อ 7) ครึ่งหลัง (รวมระบบ CMMS) เป็นเงินลงทุน บริษัทเล็กมักลงทุนครึ่งหลังไม่ไหว (RBMM p.326)

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

บริษัทเครือใหญ่ที่ข้ามนิติบุคคลไม่ได้ อาจตั้งหน่วยธุรกิจบำรุงรักษากลางเป็นนิติบุคคลแยกเพื่อแชร์ทรัพยากร (RBMM p.327) ระบบบัญชีที่ดีโอนค่าใช้จ่ายระหว่างหน่วยได้โดยไม่ต้องแยกนิติบุคคล ตัวอย่างตัวเลขของแนวทางนี้อยู่ที่หัวข้อ 8 (MPM)

การพัฒนาผู้จัดการ Profit Center: อ่านตัวเลข Data -> Information -> Knowledge ติดตาม Cash Flow ด้วย WIP, Account Receivable-Days, Account Payable-Days; ฝ่ายบัญชีรับผิดชอบความ Complete, Accurate, In-Time ของการปิดบัญชี และบรรยากาศการประชุมควรเป็น Support/Coaching (RBMM p.358-360)

## 6. เกณฑ์เลือกรูปแบบ (สรุปจากหนังสือ ไม่ใช่สูตร)

- ถ้าเป้าคือคุมต้นทุนต่อหน่วยภายในโรงงานเดียว: Cost Center + Performance Budgeting พอเพียง
- ถ้าเป็นกลุ่มบริษัทหลายโรงงานแชร์ทรัพยากร: พิจารณา Performance Based Contract แล้วค่อยแยกบริษัท
- ถ้าจะหารายได้ภายนอก: ต้องพร้อมระบบ Job Order Costing, ERP และ Mentoring ของผู้จัดการก่อน ไม่เช่นนั้นย้อนกลับเป็น Cost Center เสียเวลาเปล่า (RBMM p.359)

## 7. มุมมอง MPM: Off Balance Sheet และห่วงโซ่คุณค่า (เพิ่ม 2026-10-28)

[[Maintenance Profit Maker Book]] (ผู้เขียน 2 ใน 3 คนเดียวกับ RBMM) มองรูปแบบธุรกิจบำรุงรักษาจากมิติงบดุล รายละเอียดฝั่งผู้จ้างอยู่ที่ [[Maintenance Outsourcing]]

- **Off Balance Sheet Mode** (MPM p.103-104): ทรัพย์สินบำรุงรักษาควรอยู่ในงบดุลของ Maintenance Service Company ส่วนบริษัทอุตสาหกรรมมีน้อยที่สุดแต่บำรุงรักษาได้เสมือนมีเอง (มีค่าใช้จ่าย ไม่มีทรัพย์สิน) ถ้านโยบายเป็น Self Sufficient ต้องยอมถือทรัพย์สินและบริหารให้ใช้คุ้ม
- **ห่วงโซ่คุณค่า** (MPM p.105-106): โรงงานจ้างผู้รับเหมา -> ผู้รับเหมาส่งมอบคุณค่าของงาน; ผู้รับเหมาซื้อ/เช่าทรัพย์สินจากสถาบันการเงิน หลักการคือทรัพย์สินควรอยู่กับผู้ที่ใช้ประโยชน์ได้สูงสุด; ผู้รับเหมาที่ดีใช้ Leasing/Renting ให้งบดุลบาง และรับเงินก่อนจ่ายเงินเพื่อให้กำไรเป็นเงินสด
- **ความเสี่ยง Cost Plus กับบริษัทลูก** (MPM p.94): ถ้าตั้งบริษัทซ่อมบำรุงในเครือที่โครงสร้างผู้ถือหุ้นต่างจากบริษัทแม่ แล้วรับสัญญาแบบ Cost Plus จากแม่ กำไรตกกับผู้ถือหุ้นบางราย ค่าใช้จ่ายตกกับผู้ถือหุ้นทั้งหมด = ความไม่โปร่งใส; MPM เห็นว่าบริษัทในเครือควรใช้ Performance Based Contract แทน (MPM p.237) สอดคล้องกับข้อเสนอท้ายบท RBMM (หัวข้อ 1)

### หมายเหตุ: Turnaround เป็นทรัพย์สินตัดจ่าย (MPM p.113-114)

ตาราง 16 กิจกรรมในหัวข้อ 2 (RBMM รูป 11.3) จัด Turnaround อยู่กลุ่ม "งานตามแผน PM" ซึ่งเป็นค่าใช้จ่าย แต่ MPM ระบุชัดว่า Preventive-Proactive เป็น Expense Account **ยกเว้น Turnaround** ซึ่งลงเป็น Asset Account ตัดจ่ายจนถึงซ่อมใหญ่ครั้งถัดไป (เช่น 3 ปี ปีละ 1/3) สอดคล้องกับ RBMM เองที่กระจายค่า turnaround รายปี (RBMM p.276-279) จึงเป็นข้อยกเว้นของการจัดหมวด ไม่ใช่ข้อขัดแย้ง ดู [[Maintenance Budget]] หัวข้อ 2 และ 9.2

## 8. กรณีศึกษา 2 MPM: บริษัทบำรุงรักษารวมศูนย์ (Pooled Maintenance Company) (MPM p.237-241)

บริษัทที่มี 1 โรงงานและจะขยายเป็น 4 โรง ได้เปรียบถ้าตั้ง **บริษัทซ่อมบำรุงกลาง** เป็นนิติบุคคลแยก (บริษัทย่อย) ดูแลทุกโรงด้วย Service Business Process (MPM p.237-238):
1. มีงบดุลของตัวเองและระบบบัญชีที่สะท้อนความจริง
2. ให้บริการโรงงานในเครือด้วย Long Termed Maintenance Win-Win Performance Based Contract พร้อมบทปรับ
3. รับงานภายนอกได้แต่เป็นเรื่องเสริม เพราะแต่ละ % OEE ของบริษัทแม่มีผลมากกว่ารายได้ขายบริการภายนอกเป็นร้อยเท่า
4. ตั้งด้วยเหตุผลด้าน Management Issue (เพิ่มผลผลิต ลดต้นทุน) ไม่ใช่หารายได้; เครื่องมือ Reliability Engineering / Predictive / Spare Part Optimization ใช้ทุนไม่ต่ำกว่า 20-30 ล้านบาท ไม่คุ้มถ้าลงทุนเพื่อโรงงานเดียว
5. เปลี่ยนจาก Cost center เป็น Profit Center (Business Oriented)
6. ผลตอบแทนพนักงานผูกกับผลงานตามความรับผิดชอบ ไม่ใช่โบนัสอัตราเดียวทั้งบริษัท

### ตัวเลข: 4 โรงแยกกัน vs รวมศูนย์ (รูป 12.16, MPM p.238-240) หน่วยล้านบาท

| รายการ | 1 โรง | 4 โรงแยก | รวมศูนย์ | ประหยัดทุน | ประหยัดค่าใช้จ่าย/ปี |
|---|---|---|---|---|---|
| ทรัพย์สินบำรุงรักษา (ค่าเสื่อม 10 ปี + WACC 10%) | 120.0 | 480.0 | 150.0 | 330.0 | 66.0 |
| อะไหล่คงคลัง (WACC 10%) | 300.0 | 1,200.0 | 700.0 | 500.0 | 50.0 |
| บุคลากร (คน) ที่ 0.60 M฿/คน/ปี | 100 | 400 | 229 | 171 คน | 102.9 |
| ลงทุน Reliability Engineering System | | | 30.0 | (30.0) | (6.0) |
| **รวม (ก่อนผลพลอยได้)** | | | | **800.0** | **212.9** |
| กำไร 5% จากงานวิศวกรรม/ติดตั้งโรงใหม่ 300 M฿ หักภาษี 30% | | | | | 15.0 - 4.5 |
| Advance Payment 5% ลดเงินลงทุนในบริษัทย่อย | | | | 15.0 | |
| **รวมทั้งสิ้น** | | | | **815.0** | **223.4** |

- ตรวจ (derived): 480 - 150 = 330 x 20% = 66; 500 x 10% = 50; 400 x 40/70 = 228.6 ≈ 229 คน, 171.4 x 0.60 = 102.9; 30 x 20% = 6; 66 + 50 + 102.9 - 6 = 212.9; 212.9 + 15 - 4.5 = 223.4; 800 + 15 = 815 ตรงกับหนังสือ
- **ข้อควรระวัง (derived)**:
  - หนังสือสรุป "ประหยัดกระแสเงินสด 1,038.4 ล้านบาท" (= 815.0 + 223.4) ซึ่งรวมเงินลงทุนครั้งเดียวกับค่าใช้จ่ายรายปี เป็นมูลค่าปีแรกเท่านั้น ไม่ใช่ตัวเลขเทียบเคียงกันได้
  - รูป 12.17 พิมพ์ภาษี "15.0 x 30% = 0.45" ค่าที่ถูกคือ 4.5 (ตรงกับตาราง)
  - การลดคน 400 -> 229 สมมติว่า Utilization Factor ปรับได้จาก 40% เป็น 70% (MPM p.239) ซึ่งสูงกว่าระดับที่ RBMM ถือว่า "60% สูงแล้ว" (RBMM p.73-74) = ข้อขัดแย้ง MPM-C5 ดู [[Maintenance KPIs]]; ถ้าใช้ 60% จะได้ 267 คน ประหยัด 133 คน = 80.0 M฿/ปี (derived)
  - ตัวเลขทั้งหมดเป็นตัวอย่างสมมติ ไม่ใช่ข้อมูลจริง

### กรณีมีบริษัทในเครือหลายแห่งอยู่แล้ว (MPM p.240-241)

1. รวมหน่วยซ่อมบำรุงทั้งหมดเป็นนิติบุคคลเดียว — ยากเพราะวัฒนธรรม รายได้ ผลประโยชน์ต่างกัน ปัญหาหลักคือ Change Management (สอดคล้องกับหัวข้อ 5)
2. **Virtual new Maintenance Organization — Completely De-centralized**: เป็นนิติบุคคลใหม่หรือไม่ก็ได้ แต่ต้องเป็น **Profit Center** ใช้ Value Oriented Maintenance Budgeting and Control, Pool-Planning ทรัพยากรร่วมพร้อมตีราคาโอนระหว่างบริษัท, จัดหาทรัพยากรกองกลาง และมีงบดุล/งบกำไรขาดทุนของแต่ละศูนย์กำไร

ทรัพยากรร่วม (รูป 12.18, MPM p.241): ทีมผู้เชี่ยวชาญเคลื่อนที่, โรงซ่อมร่วม, ทีมซ่อมประจำโรงงาน (multi-skill ใกล้ชิดฝ่ายผลิต), ทีมผู้เชี่ยวชาญงานซ่อมใหญ่ ([[Turnaround Management]]) — ตรงกับหลัก Technical/Information Centralized, Operation Decentralized ของ RBMM (หัวข้อ 4)

### Profit Center ต้องมีอะไร (MPM p.242)

1. งบดุลของตัวเอง 2. งบกำไรขาดทุนของตัวเอง 3. ระบบตั้งเป้าทั้งบริหารและเทคนิค พร้อมรายงาน: Utilization Factor, Full Cost / Full Cost rate, Over/(Under) Reserved, Provision for Work Due และ Provision for Loss Order ([[Job Order Costing]]), ดัชนีที่เลือกใช้, และ **Personnel Productivity**

```
Personnel Productivity = (OEAD + ค่าใช้จ่ายบุคคลทั้งสิ้น) / ค่าใช้จ่ายบุคคลทั้งสิ้น
OEAD = Operational Earning After Depreciation
```

## 9. Contested: Profit Center ดีกว่าในทุกรูปแบบหรือไม่ — ข้อขัดแย้ง MPM-C6 (เพิ่ม 2026-10-28)

| แหล่ง | มุมมอง |
|---|---|
| MPM | ทุกรูปแบบ (บริษัทแม่มีเครือ, ขยายกำลังผลิต, service provider) การดำเนินงานแบบ **ศูนย์กำไรให้ผลดีกว่า** เพราะตั้งงบและควบคุมได้ดีกว่า และองค์กรเสมือนต้องเป็น Profit Center ไม่ใช่ Cost Center (MPM p.241-242) |
| RBMM | ใช้ Cost Center เป็นระบบหลักของหนังสือ ถ้าเป้าคือคุมต้นทุนต่อหน่วยในโรงงานเดียว Cost Center + Performance Budgeting ก็พอ และเตือนว่า Profit Center ที่มุ่งรายได้ภายนอกเสี่ยง (RBMM p.325-327) |

- ส่วนที่ตรงกัน: ทั้งสองเห็นว่ารายได้ภายนอกเป็นเรื่องรอง และกรณีหลายโรงงานควรแชร์ทรัพยากรผ่านหน่วยกลางและ Performance Based Contract
- ส่วนที่ต่าง: MPM ยกระดับเป็นข้อสรุปทั่วไป ("ทุกรูปแบบ") ขณะที่ RBMM ถือว่า Cost Center ที่มีระบบดีพอสำหรับโรงงานเดียว; บริบทของ MPM เน้นกรณีหลายโรงงาน/บริษัทในเครือ จึงอาจไม่ขัดกันโดยตรง (การตีความ)
- **ยังไม่ resolve** ผู้ใช้ต้องเลือกตามบริบทองค์กร ตั้ง `contested: true` เกณฑ์ในหัวข้อ 6 ยังเป็นมุมมอง RBMM

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
- [[Maintenance Profit Maker Book]]
- [[Maintenance Outsourcing]]
- [[Turnaround Management]]

ดูเพิ่ม (หน้าจาก MPM ingest 2026-10-28): [[Maintenance Performance Improvement]], [[Maintenance Financial Impact]]

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
- [[Maintenance Business Models]] [defined_in:: [[Maintenance Profit Maker Book]]] chapters 6, 7, 12 (MPM)
- [[Maintenance Business Models]] [related_to:: [[Maintenance Outsourcing]]]
- Off Balance Sheet Mode [applies_to:: Industrial Company] maintenance assets held by Maintenance Service Company (MPM p.103-104)
- Maintenance Service Company [has_part:: Maintenance Assets] on its own balance sheet (MPM p.103-104)
- Outsourcing Value Chain [has_part:: Financier] contractor buys or leases assets (MPM p.106)
- Cost Plus Contract [has_category:: transparency risk with subsidiary] different shareholder structure (MPM p.94)
- Plant Turnaround [has_category:: asset account] exception to Preventive-Proactive expense, amortised (MPM p.113-114)
- Pooled Maintenance Company [is_a:: [[Maintenance Business Models]]] central subsidiary serving group plants (MPM p.237-238)
- Pooled Maintenance Company [uses:: Performance Based Contract] long term Win-Win with group plants (MPM p.237)
- Pooled Maintenance Company [has_value:: 815.0 M THB investment saving] 4 plants case (MPM p.238-240)
- Pooled Maintenance Company [has_value:: 223.4 M THB per year expense saving] 4 plants case (MPM p.238-240)
- Pooled Maintenance Company [has_value:: maintenance assets 150 vs 480 M THB] (MPM p.238-240)
- Pooled Maintenance Company [has_value:: spares 700 vs 1,200 M THB] (MPM p.238-240)
- Pooled Maintenance Company [has_value:: 229 vs 400 staff] at 0.60 M THB per head per year (MPM p.238-240)
- Pooled Maintenance Company [depends_on:: Reliability Engineering Tools] at least 20-30 M THB, not worth for one plant (MPM p.237)
- Cash Flow Saving 1,038.4 M THB [contradicts:: Comparable Saving Basis] mixes one-off investment with annual expense, derived
- Utilization Factor [has_value:: 40% to 70%] assumed improvement in case 2 (MPM p.239) [contested:: true]
- Utilization Factor [has_value:: 60% already high] do not chase alone (RBMM p.73-74) [contested:: true]
- MPM Utilization Target [contradicts:: RBMM Utilization View] MPM-C5 [contested:: true]
- Virtual Maintenance Organization [is_a:: [[Maintenance Business Models]]] completely de-centralized, must be Profit Center (MPM p.240-241)
- Virtual Maintenance Organization [uses:: Pool-Planning] shared resources with transfer pricing (MPM p.241)
- Shared Maintenance Resources [has_part:: Mobile Expert Team] (MPM Fig 12.18 p.241)
- Shared Maintenance Resources [has_part:: Shared Workshop] (MPM Fig 12.18 p.241)
- Shared Maintenance Resources [has_part:: Plant Maintenance Team] multi-skill (MPM Fig 12.18 p.241)
- Shared Maintenance Resources [has_part:: Turnaround Expert Team] (MPM Fig 12.18 p.241)
- Profit Centered Maintenance [depends_on:: Own Balance Sheet and P&L] (MPM p.242)
- Profit Centered Maintenance [uses:: Personnel Productivity] (OEAD + personnel cost) / personnel cost (MPM p.242)
- Personnel Productivity [has_formula:: (OEAD + total personnel cost) / total personnel cost] OEAD = Operational Earning After Depreciation (MPM p.242)
- Profit Centered Maintenance [has_category:: better in all forms] MPM conclusion (MPM p.241-242) [contested:: true]
- Cost Center [has_category:: sufficient for single plant] with Performance Budgeting (RBMM p.325-327) [contested:: true]
- MPM Profit Center View [contradicts:: RBMM Cost Center View] MPM-C6, unresolved [contested:: true]

---
title: Maintenance Performance Audit
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [mpm, audit, maintenance-management, kpi]
sources: [maintenance-profit-maker.md]
confidence: medium
contested: false
---

# Maintenance Performance Audit (การตรวจสอบ ทบทวนสมรรถนะงานบำรุงรักษา)

การ audit สมรรถนะงานบำรุงรักษาคือการประเมินสถานะปัจจุบันของหน่วยงานแล้วสอบเทียบกับมาตรฐานทั่วไปหรือระดับโลก เป็น **บันไดขั้นแรก** ของการปรับปรุงทุกเรื่อง (ขั้นที่ 1 ของ [[Maintenance Performance Improvement]]) หนังสือ [[Maintenance Profit Maker Book]] (บทที่ 1 และ 11) ย้ำว่าคำว่า "Audit" มักถูกมองว่าเป็นการจับผิด จึงอาจไม่ได้ความร่วมมือและข้อเท็จจริง โดยเนื้อแท้คือการวัดสถานการณ์เพื่อแก้ปัญหาให้ยั่งยืน (MPM p.192) เนื้อหาหน้านี้ถอดความจาก reading notes [[raw/maintenance-profit-maker]] ไม่ใช่ข้อความต้นฉบับ

## 1. ที่มาในบทที่ 1: audit เป็นจุดเริ่มต้น (MPM p.22-25)

- Plant/Maintenance Performance Analysis (Audit) เป็น 1 ใน 4 งานของกลุ่ม Maintenance Engineering ในโครง 16 กิจกรรม (ดู [[Maintenance Business Models]]) และหนังสือถือว่าเป็นส่วนสำคัญที่สุดของกลุ่มนี้: benchmark ด้วยดัชนีมาตรฐานสากล หา gap แล้วกำหนดกิจกรรม (MPM p.22-23)
- งานซ่อม (Fault Recovery) คือ "เครื่องเรียกเรา" การเปลี่ยนเป็นฝ่ายเข้าหาเครื่องต้องเริ่มจากประเมินตนเองก่อน (รูป 1.4, MPM p.23-24)
- ผลตรวจที่พบบ่อย: ความรู้เทคนิคไม่ใช่ปัญหาใหญ่ ปัญหาจริงคือ **การขาดการบริหารจัดการ** (MPM p.24)

### หัวข้อสอบเทียบ 14 ข้อ (MPM p.24-25)

| # | หัวข้อ | # | หัวข้อ |
|---|---|---|---|
| 1 | สภาพปัจจุบันของเครื่องเทียบมาตรฐาน | 8 | Maintenance Cost and Accounting |
| 2 | OEE และตัวขับสมรรถนะ | 9 | Technical Document Management |
| 3 | Organization | 10 | Spare Part Management and Purchasing |
| 4 | Maintenance Methodology | 11 | Tool Management |
| 5 | Maintenance Planning Ability and Capacity | 12 | Human Resource Management |
| 6 | Subcontracting Management | 13 | Safety & Environment |
| 7 | Maintenance Management System | 14 | Renewal Policy |

แต่ละหัวข้อแปลงเป็นดัชนีเพื่อเทียบกับมาตรฐาน/โรงงานในธุรกิจเดียวกัน บอกขนาดช่องว่าง ห่างจาก best เท่าใด ผลทางการเงินเท่าใด และระยะคืนทุน (MPM p.25)

### Road Map to Maintenance Excellence 5 ระดับ (MPM p.25-33)

สมรรถนะประเมินได้จาก **สัดส่วน** ปริมาณงาน 16 กิจกรรม (Plant Maintenance Activity Profile): ระดับ 1 Without MMS -> 2 With MMS (ไม่มีคอมพิวเตอร์) -> 3 With CMMS (ใช้ไม่เต็มที่) -> 4 With CMMS & ME beginning -> 5 With CMMS & ME ongoing ปริมาณงานรวมลดลงเมื่อไปทางขวา ระดับ 1 วัด OEE ไม่ได้และตั้งงบโดยบวก % จากปีก่อน ระดับ 5 งานเกือบทั้งหมดวางแผนได้ ผู้เขียนย้ำว่าใช้ Reliability Engineering โดยไม่มีข้อมูลเป็นเรื่องเหลวไหล (MPM p.32-33) บทสรุปบทที่ 1 ว่าการก้าวสู่ระดับแชมเปี้ยนเริ่มที่ audit เสมอ ถ้าละเลยจะถอยกลับ (MPM p.36) เทียบกับพีระมิด 6 ชั้นของ RBMM ใน [[Maintenance Efficacy Pyramid]]

## 2. Flash Audit vs Full Audit (MPM p.192-193)

เป้าหมายของการประเมินคือเพิ่มผลผลิตทั้งสองทาง (ผลิตมากที่สุด ต้นทุนต่ำที่สุด) จึงต้องเก็บทั้งข้อมูลการผลิตและข้อมูลต้นทุน หนังสือเปรียบกับการตรวจสุขภาพ: ตรวจรายการหลักก่อน แล้วเจาะเฉพาะจุดผิดปกติ

| | Flash Audit (ประเมินขั้นต้น) | Full Audit (ประเมินละเอียด) |
|---|---|---|
| ลักษณะ | สั้นที่สุด ใช้ข้อมูลน้อยแต่มีนัยสำคัญที่สุด เหมือน "ถ่ายรูป" ภาพกว้าง | ศึกษากระบวนการซ่อมบำรุงทั้งหมด ทั้งด้านบริหารและเทคโนโลยี |
| แนวทาง | Quantitative (ตัวเลข/ดัชนี) + Qualitative (การจัดระบบงาน) ใช้สอบทานกัน | ต้องใช้ความรู้เชิงลึกเฉพาะอุตสาหกรรม (เช่น กระดาษ ปิโตรเคมี) |
| ต้นทุน/เวลา | ต่ำกว่ามาก ชี้ว่าควรเจาะ Full Audit ตรงไหน | ใช้เวลาและข้อมูลมาก |

- **มากกว่า 80% ของปัญหาเป็นเรื่องการบริหารจัดการ** เทคนิคเป็นประเด็นเสริม ดังนั้น Flash Audit มักนำไปสู่การแก้ไขได้เลยโดยไม่ต้องทำ Full Audit ความสำเร็จขึ้นกับความตั้งใจจริงและการยอมรับปัญหา (MPM p.193)
- สอดคล้องกับข้อสรุปบทที่ 1 ว่าปัญหาจริงคือการขาดการบริหาร (MPM p.24)

## 3. Flash Audit เชิงคุณภาพ: 16 หัวข้อบน radar (MPM p.193-195)

เก็บข้อเท็จจริงจากสภาพจริงและการสัมภาษณ์ ตอบแบบสอบถาม 16 รายการหลัก (มีรายการย่อยมาก) ให้คะแนนเป็น % แล้วแสดงบน radar 16 แกน (0-100%)

| Technical (9) | Management (7) |
|---|---|
| 1. สภาพโรงงาน เครื่องจักรอุปกรณ์ | 1. ความร่วมมือซ่อมบำรุง-ผลิต |
| 2. ระบบบริหารงานบำรุงรักษา | 2. วิธี/ระบบเก็บตัวเลขค่าใช้จ่ายและบัญชี |
| 3. ความสามารถทางเทคนิค | 3. การจัดทำและใช้งบประมาณ |
| 4. การจัดการจ้างเหมา | 4. ระบบข้อมูลบริหารและเทคโนโลยีคอมพิวเตอร์ |
| 5. ระบบจัดการข้อมูลเทคนิค | 5. การจัดองค์กร |
| 6. การจัดการอะไหล่และคลัง | 6. งานบริหารบุคคล |
| 7. การจัดการมาตรฐาน | 7. การควบคุมและวัดผลการทำงานทั้งหมด |
| 8. การจัดการคุณภาพ | |
| 9. ความปลอดภัยและสภาพแวดล้อม | |

- ในรูป 11.1 แกน 1-7 = Management, 8-16 = Technical; จุดต่ำผิดปกติ = สิ่งที่ปรับปรุงได้ ข้อคะแนนน้อยควรทำก่อน (MPM p.194-195)
- ตัวอย่างการตีความรูป 11.1: จุดอ่อนคือการตั้งเป้า ควบคุมและวัดผล (Measuring, Reporting & Control) โดยเฉพาะค่าใช้จ่ายและงบประมาณ ส่วนความสามารถทางเทคนิคและความร่วมมือซ่อม-ผลิตดีแล้ว (MPM p.195)
- **เกรด**: A (90-100), B (80-90), C (70-80), D (60-70), F (< 60) แล้วคิดคะแนนถ่วงน้ำหนัก เพราะแต่ละหัวข้อสำคัญไม่เท่ากัน น้ำหนักขึ้นกับกลยุทธ์ธุรกิจ (ดู [[Maintenance Master Plan]]) (MPM p.195)
- 16 หัวข้อนี้แทบตรงกับแผนแม่บท 16 แผน (บทที่ 9) และใกล้กับ 16-Topic Assessment ของ RBMM แต่รายการไม่ตรง 1:1 (ดูความต่างใน [[Maintenance Efficacy Pyramid]])

## 4. Flash Audit เชิงปริมาณ: Room for Improvement (MPM p.195-196)

ใช้ตัวเลขค่าใช้จ่ายและผลผลิตคำนวณดัชนี เทียบมาตรฐานอุตสาหกรรมเดียวกัน แบ่งสองด้าน:

- **ประสิทธิภาพ (efficiency, cost reduction)**
  - ค่าใช้จ่ายคงที่ (จาก Balance Sheet): ทรัพย์สินที่บำรุงรักษาครอบครอง รวมอะไหล่ที่บำรุงรักษาเบิกใช้ผู้เดียว; บุคลากร (ไม่อยู่ในงบดุลแต่มีผลเหมือนทรัพย์สิน เป็น "รายการแฝงในงบดุล" ที่ค่าใช้จ่ายเพิ่มทุกปี); ค่าบริหารจากหน่วยสนับสนุน
  - ค่าใช้จ่ายแปรผัน (จาก Income Statement): อะไหล่/วัสดุสิ้นเปลือง จ้างเหมา ล่วงเวลา หนังสือเปรียบเป็น "เชื้อเพลิง"
- **ประสิทธิผล (effectiveness)**: OEE (Availability, Speed, Quality) ดู [[Availability and OEE]] และความสูญเสียอื่นที่บำรุงรักษาเกี่ยวข้อง เช่น ซ่อมใหญ่นานเกินกำหนด เปลี่ยนสายการผลิตช้า พลังงานสูญเสียช่วงเดินเครื่องเปล่า ค่ากำจัดมลพิษ ค่าปรับ

```
Room for Improvement (รูป 11.2, MPM p.196)
 ├─ ประสิทธิภาพ (Cost Reduction)
 │   ├─ คงที่: ทรัพย์สินบำรุงรักษา, เงินเดือน/ค่าแรง, บริหารและสนับสนุน, อื่นๆ
 │   └─ แปรผัน: อะไหล่/วัสดุสิ้นเปลือง, จ้างเหมาภายนอก, อื่นๆ
 └─ ประสิทธิผล (ผลผลิต)
     ├─ OEE: Availability, Speed, Quality
     └─ อื่นๆ: ค่าใช้จ่ายทางตรง, พลังงาน, ค่ากำจัดของเสีย, ค่าปรับลูกค้า/สัญญา,
        ค่าแก้ไขสินค้า, ค่าล่วงเวลา, อื่นๆ
```

## 5. ข้อมูลที่ต้องใช้และแหล่งที่มา (รูป 11.3, MPM p.196-200)

ใช้ตัวเลขคู่กับคำตอบเชิงคุณภาพ เพื่อตรวจว่าตัวเลขน่าเชื่อถือหรือไม่ (ตาราง OCR เสียบางส่วน สรุปเฉพาะที่อ่านได้)

| กลุ่มข้อมูล | ตัวอย่างรายการ | แหล่ง |
|---|---|---|
| การเงินบริษัท | Asset Replacement Value, WACC, รายได้ ต้นทุนขาย กำไรขั้นต้น | งบดุล (PP&E), ฝ่ายบัญชี/การเงิน, งบกำไรขาดทุนย้อนหลัง (ระวังงบรวม Consolidated) |
| ปริมาณผลิต | ตัน/ชิ้น | บัญชีต้นทุนขาย ต้องกระทบกับปริมาณขาย + สินค้าคงเหลือ และกับ OEE, Capacity, Planning Factor |
| ค่าใช้จ่ายคงที่ | ค่าเสื่อม ดอกเบี้ย ค่าเช่า ประกัน พื้นที่ อะไหล่ บุคลากร | บัญชีแยกประเภท |
| ทรัพย์สินบำรุงรักษา | อาคาร เครื่องจักร เครื่องมือ เครื่องจักรกลหนัก | ทะเบียนคุมทรัพย์สิน ราคาที่ได้มา/ประเมิน หลังหักค่าเสื่อม |
| ค่าแรง | ทางอ้อม ทางตรง (บันทึกชั่วโมง/งาน) | บัญชี + ระบบลงเวลา |
| อะไหล่/วัสดุ | อะไหล่ที่ใช้, วัสดุอายุ < 1 ปี (เช่น น้ำมันหล่อลื่น) | รายงานเบิกจ่ายคลัง การซื้อ บัญชีต้นทุน |
| งานจ้าง | ตาม Work Order Number | ใบสั่งงาน |
| ซ่อมใหญ่ | ค่าซ่อมใหญ่ (>= 3 ปี/ครั้ง) ตัดจ่ายรายปี | ประวัติซ่อมใหญ่และคาดการณ์ |
| OEE | A, P, Q | รายงานผลผลิต (เวลาเดิน เวลาหยุด ของเสีย) DCS |
| กำลังคน | จำนวนพนักงานแต่ละระดับ ชม.-คน Utilization Factor Man-Hr Rate | รายงานกำลังคน CMMS |
| ดัชนีควบคุมงาน | เป้า PM, CM, Predictive | [[CMMS]] |

ดัชนีที่ใช้ประเมิน (รูป 11.4, MPM p.202) แบ่ง 7 กลุ่ม: Maintenance Expenditure (เช่น Expenses/Unit Produced, Expenditure/Plant Asset), OEE, Inventory Indices, Work Control Indices (PM/CM, PDM/Total, MTBF/MTTR/MWT, Turnaround), Human Resource Indices (Utilization, OT/Normal, Direct/Indirect head count, Contracts/Total), Safety Indices และ Maintenance Full Cost rate หนังสือไม่ให้ค่าเป้าของดัชนีในตารางนี้ รายละเอียดดัชนีดู [[Maintenance KPIs]]

## 6. หลักการกระทบยอด (Reconciliation) (MPM p.201)

- ตัวเลขปริมาณเดียวกันที่เก็บ/คำนวณจากหลายระบบต้องได้ค่าเดียวกันเสมอ ถ้าไม่ตรง = **ปัญหาเชิงระบบ** ต้องแก้ระบบงานก่อนจะพูดถึงสมรรถนะ
- ทุกกิจกรรมใช้ทรัพยากรใน **งบดุลเดียวกัน** ทุกรายการต้องมีที่มาที่ไปต่อเนื่อง
- "วัดอะไรไม่ได้ ต้องไปแก้ระบบก่อน": อยากลดค่าใช้จ่ายแต่ไม่มีระบบเก็บค่าใช้จ่าย หรืออยากเพิ่มผลผลิตแต่ไม่มีระบบวัดผลผลิต ต้องแก้เชิงคุณภาพก่อน
- ตัวอย่าง OEE: `สินค้าที่ผลิตได้ = OEE x Capacity x Planning Factor` ต้องกระทบกับบัญชี (ขาย − สินค้าต้นงวด + สินค้าปลายงวด แปลงเป็นปริมาณ) และสินค้า rework ต้องกระทบกับ WIP
- ดัชนีมาจากหลายระบบ จึงต้องเลือก **ดัชนีหลักชัย** ก่อน ที่เหลือเป็นดัชนีเสริม
- อะไหล่: ทุกการเบิก/คืนกระทบบัญชี ถ้าแก้ประวัติซ่อมหลังปิดงวด รายงานบำรุงรักษาจะไม่ตรงบัญชี (MPM p.203-204)
- Utilization Factor อ่อนไหวมาก ค่าสูงบอกแค่ว่าใช้เวลาในงานมาก ต้องถามว่างานนั้นควรใช้เวลาขนาดนั้นหรือไม่ จึงต้องสอบเทียบกับดัชนีอื่นทุกครั้ง (MPM p.203)

## 7. ปัญหาที่พบบ่อย (MPM p.204)

- ระบบบันทึก/รายงานไม่สมบูรณ์ กระทบยอดไม่ได้ เพราะ **เก็บข้อมูลซ้ำซ้อนหลายที่** สรุปหลายทางไม่ตรงกัน
- บุคลากรช่างเข้าใจบัญชีน้อย บางแห่งหาระบบใหม่มาลดค่าใช้จ่าย ทั้งที่ปัญหาคือการบันทึกค่าใช้จ่ายยังไม่ถูก (ค่าใช้จ่ายจริงอาจไม่สูง/ต่ำอย่างที่คิด)
- บัญชีกับ CMMS ไม่เชื่อมกัน -> งบประมาณเพี้ยน
- ด้านการผลิต: บางโรงงานไม่มีระบบบันทึกการเดินเครื่อง บางโรงงานมีหลายระบบ (**DCS, Operator Log Book, CMMS**) ให้ตัวเลขไม่ตรงกันและกระทบกับปริมาณผลิตไม่ได้ ทางแก้ไม่ใช่ยุบเหลือระบบเดียว แต่ **เลือกวิธีบันทึกที่น่าเชื่อถือที่สุดเป็นหลัก** แล้วใช้ระบบอื่นยืนยัน สอดคล้องกับ [[RM Data Quality]]
- การทบทวนสมรรถนะสำคัญที่สุดและยากที่สุดในการปรับปรุง เพราะต้องการความร่วมมือมาก โดยเฉพาะผู้บริหารบำรุงรักษา

## เชื่อมโยงกับ compressor failure hierarchy

(การตีความของ wiki ไม่ใช่เนื้อหาในหนังสือ)
- ดัชนีฝั่ง effectiveness (Availability, MTBF, MTTR, MWT) ของ [[Compressor]] ต้องอิง failure record ที่เข้ารหัสตาม [[Failure Hierarchy]] ถ้า down time บันทึกใน DCS แต่ failure mode อยู่ใน CMMS ต้องกระทบยอดสองระบบให้ตรงกันก่อนเทียบ benchmark จาก [[OREDA]]
- หลัก "เลือกระบบบันทึกหลักหนึ่งระบบแล้วใช้ระบบอื่นยืนยัน" ใช้กับ failure data ได้โดยตรง ดู [[Failure Data Recording]]

## ดูเพิ่ม

- [[Maintenance Performance Improvement]]
- [[Maintenance Master Plan]]
- [[Maintenance Efficacy Pyramid]]
- [[Maintenance KPIs]]
- [[Availability and OEE]]
- [[Maintenance Profit Maker Book]]

## Triplets

- [[Maintenance Performance Audit]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 11, also chapter 1 (MPM p.22-25, p.191-204)
- [[Maintenance Performance Audit]] [step_of:: [[Maintenance Performance Improvement]]] step 1 of 6 (MPM p.207-208)
- [[Maintenance Performance Audit]] [part_of:: Maintenance Engineering] one of 4 activities of group 4, most important of the group (MPM p.22-23)
- Flash Audit [is_a:: [[Maintenance Performance Audit]]] short, least data, most significant; points where to do full audit (MPM p.192-193)
- Full Audit [is_a:: [[Maintenance Performance Audit]]] detailed, management and technology, industry-specific knowledge (MPM p.193)
- Flash Audit [differs_from:: Full Audit] lower cost, broad picture vs detailed study (MPM p.192-193)
- Flash Audit [uses:: Quantitative Audit] figures and indices of cost and output (MPM p.195-196)
- Flash Audit [uses:: Qualitative Audit] work system setup; tells whether figures are reliable (MPM p.193-195)
- Maintenance Problems [has_value:: > 80% managerial] technical issues are secondary (MPM p.193)
- Qualitative Audit [has_value:: 16 topics] 9 technical + 7 management, radar 0-100% (MPM p.193-194)
- Qualitative Audit [produces:: Radar Chart] 16 axes, low points = room for improvement (Fig 11.1, MPM p.194-195)
- Qualitative Audit [has_category:: Grade A-F] A 90-100, B 80-90, C 70-80, D 60-70, F < 60, weighted (MPM p.195)
- Audit Topic Weighting [depends_on:: Business Strategy] maintenance strategy follows business strategy (MPM p.195)
- Quantitative Audit [measures:: Efficiency] fixed cost from balance sheet, variable cost from income statement (MPM p.195-196)
- Quantitative Audit [measures:: Effectiveness] OEE plus other maintenance-related losses (MPM p.196)
- Room for Improvement [has_part:: Efficiency] cost reduction: fixed and variable cost (Fig 11.2, MPM p.196)
- Room for Improvement [has_part:: Effectiveness] OEE and other losses (Fig 11.2, MPM p.196)
- Maintenance Personnel [is_a:: Hidden Balance Sheet Item] cost rises every year, unlike depreciating assets (MPM p.195-196)
- [[CMMS]] [source_of:: Work Control Data] PM, CM, predictive targets for audit (Fig 11.3, MPM p.196-200)
- DCS [source_of:: OEE Data] run time, stop time, rejects (Fig 11.3, MPM p.196-200)
- Reconciliation [applies_to:: [[Maintenance Performance Audit]]] same quantity from different systems must match; mismatch = system problem (MPM p.201)
- Production Output [has_formula:: OEE x Capacity x Planning Factor] must reconcile with sales minus opening plus closing stock (MPM p.201)
- [[Maintenance Performance Audit]] [uses:: [[Maintenance KPIs]]] 7 index groups in Fig 11.4, no target values given (MPM p.202)
- Personnel Productivity [has_formula:: (OEAD + Total Personnel Cost) / Total Personnel Cost] OEAD = operational earning after depreciation (MPM p.203)
- Duplicate Recording [contributes_to:: Reconciliation Failure] DCS, operator log book, CMMS give different figures (MPM p.204)
- Duplicate Recording [resolved_by:: Primary Recording System] choose most reliable as main, others verify; no need to merge to one (MPM p.204)
- 14 Audit Topics [defined_in:: [[Maintenance Profit Maker Book]]] chapter 1 precursor list (MPM p.24-25)
- Road Map to Maintenance Excellence [has_value:: 5 levels] Without MMS to With CMMS and ME ongoing (MPM p.25-33)
- Road Map to Maintenance Excellence [related_to:: [[Maintenance Efficacy Pyramid]]] parallel maturity framework to RBMM 6 levels
- Road Map to Maintenance Excellence [depends_on:: Activity Profile] proportion of 16 activities (MPM p.25-26)
- [[Maintenance Performance Audit]] [related_to:: [[RM Data Quality]]] reconciliation of multiple data systems

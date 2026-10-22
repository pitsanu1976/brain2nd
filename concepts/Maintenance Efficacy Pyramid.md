---
title: Maintenance Efficacy Pyramid
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [maintenance-management, kpi, budget, cmms, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Maintenance Efficacy Pyramid (พีระมิดสมรรถนะงานบำรุงรักษา)

กรอบประเมินวุฒิภาวะของหน่วยงานบำรุงรักษา 6 ชั้นจากบทที่ 2 ของ RBMM (Fig 2.2, p.35-40) ใช้ชี้ว่าหน่วยงานอยู่ชั้นใดและต้องสร้างอะไรก่อน หลักคือ ต้องคุมงานได้ก่อนจึงคุมเงินได้ และคุมทั้งสองได้ก่อนจึงตั้งงบและ optimize ได้ หน้านี้รวมการประเมิน 16 หัวข้อ (Fig 2.1) และวงจรปรับปรุง 5 คำถาม (Fig 2.4) ด้วย

## 1. การประเมิน 16 หัวข้อ (Fig 2.1, RBMM p.32-35)

Radar chart 16 แกน คะแนน 0-100%

| # | หัวข้อ | # | หัวข้อ |
|---|---|---|---|
| 1 | Maintenance and Production Coordination | 9 | Maintenance Policy |
| 2 | Maintenance Cost Accounting | 10 | Method and Technical Management |
| 3 | Maintenance Performance Budgeting | 11 | Outsourcing Management |
| 4 | Performance Measuring, Reporting and Control | 12 | Technical Documentation |
| 5 | Maintenance Management System | 13 | Spare Part Management |
| 6 | Management Information Systems | 14 | Standardization and Code of Conduct |
| 7 | Organization | 15 | Quality Management |
| 8 | Human Resource | 16 | SH&E Management |

- 6 ประเด็นสำคัญที่สุด: 2, 3, 4, 7, 10, 13 (RBMM p.35)
- กลุ่มคิด/บริหาร/คุมต้นทุน (2-5) ถ้าดีทั้งสี่ จุดบนกราฟจะอยู่ราว 80% รากเหตุมักอยู่ที่ (4) ระบบรายงาน (RBMM p.33-34)
- CMMS ที่ใช้แค่เปิด/ปิด Job ไม่คุ้มลงทุน ข้อมูลไม่ถูกวิเคราะห์จึงไม่น่าเชื่อถือ วนเป็น "วงจรเลว" (RBMM p.34) ดู [[CMMS]]
- Spare Part Management (13) เกี่ยวโยง 2,3,4,5,6,7,10 อะไหล่เป็นสัดส่วนมากกว่า 60-70% ของค่าใช้จ่ายบำรุงรักษา และ holding cost 15-20% ของราคาอะไหล่ (RBMM p.34) ดู [[Spare Parts Management]]

## 2. ทั้ง 6 ชั้น (Fig 2.2, RBMM p.35-40)

| ชั้น | ระดับ | คุณสมบัติ/ปัญหา |
|---|---|---|
| 1 | Reactive | Break and Fix ไม่มีหน่วยงานชัดเจน รักษาตามอาการ |
| 2 | Immature | Process ดี (มีองค์กร/CMMS) แต่ Content แย่ (ไม่วิเคราะห์งาน เก็บข้อมูลไม่ถูก) |
| 3 | Maintenance Work Control | Strategies, Work Measuring and Accountability, Planning/Scheduling, Parts and Logistics, Work Control Indices |
| 4 | Maintenance Cost Control | Cost Accounting, Full Cost, allocation to asset, Full Cost per Unit, Cost Control Indices |
| 5 | Maintenance Performance Budgeting | งบปริมาณงาน, Full Fixed Cost Rate, cost per unit produced |
| 6 | Maintenance Optimization | Planned Maintenance และ Spare Part Optimization |

ยอดพีระมิด = "Best in Class and Sustainable"

### ชั้น 3 Work Control (ควรทำเป็นอันดับแรก, p.36-38)

- Maintenance Strategies: ควบคุม downtime และ Man-Hrs, วิเคราะห์ failure mode (cause), เลือก scheduled PM อย่างวิทยาศาสตร์
- Accountability ต่างจาก Responsibility: ผู้รับงานต้องอธิบายผลและเหตุผลการตัดสินใจเมื่อถูกทวงถาม (RBMM p.37)
- Planning/Scheduling: ดัชนี Backlog และดัชนีว่าเลือกงานถูกหรือไม่
- Parts and Logistics: stock คือ "ประกัน" ต่อความเสี่ยง breakdown เหมือนเบี้ยประกัน ค่าโสหุ้ย 15-20% ควรส่งกลับให้ผู้ขอสะสม (RBMM p.37-38)

### ชั้น 4-6

- ชั้น 4 แยก Cost Control (ใช้ทรัพยากรถูกเวลา ไม่เร่งด่วน) ออกจาก Loss Control (ขึ้นกับยุทธศาสตร์ "Do the Right Thing and Do the Thing Right") งานนอกแผนมีค่าเสียหายสูงกว่ามาก (RBMM p.38-39)
- ชั้น 5 โครงงบ (Fig 2.3): Total Maintenance = Total Planned + Total Unplanned แต่ละฝั่งแยก Man-Hrs และ Materials (Outsource, Direct Purchase Parts, Stock Parts) พร้อม Planned/Unplanned Losses งบ 4 รายการ: อัตราค่าแรงต่อ Man-Hr, ค่าจ้างเหมา, ค่าอะไหล่, ค่าสูญเสีย (RBMM p.39-40) ดู [[Maintenance Budget]]
- ชั้น 6 ชั่งน้ำหนักงานตามแผน/นอกแผน ทางเลือก: Run to Failure, เปลี่ยน/Overhaul ตามกำหนด, Condition Monitoring แล้วแก้เมื่อพบ potential failure, Improvement/Modification (RBMM p.40)

## 3. วงจรปรับปรุง 5 คำถาม (Fig 2.4, RBMM p.40-42)

| คำถาม | โมดูล | ผลลัพธ์ | หน้า wiki |
|---|---|---|---|
| PM Selection? | RCM Process | RCM Scheduled PM Tasks | [[PM Task Selection]] |
| Optimum PM Interval? | PM Optimization | PM ที่ interval เหมาะสม | [[PM Interval Optimization]] |
| Stock Performance? | Risk Based Spare Part Optimization | ระดับสต็อกที่ให้ประโยชน์สูงสุด | [[Spare Part Criticality and Risk]] |
| Budgeting and Control? | Performance Budgeting | งบตามเป้า | [[Maintenance Budget]] |
| Problem of Reporting? | Maintenance Strategic Report | Strategic Reporting Items | [[Maintenance Strategic Report]] |

Fig 2.5 (Reliability Based Maintenance Selection and Optimization, RBMM p.42-43) มี 5 ขั้น: เลือกเครื่องตาม criticality, FMECA (RPN เชิงคุณภาพ), Failure Data Analysis (Weibull parameters, criticality เชิงปริมาณ), เลือกประเภท PM, หา task interval ที่เหมาะสม ดู [[FMECA]] และ [[Weibull Analysis]] ประเภท PM ที่เลือกได้ 4 อย่าง: Scheduled Replacement/Overhaul, Scheduled Condition Monitoring/Inspection, Scheduled Hidden Failure Finding, Run to Failure

## 4. 6 "โรค" ท้ายบท (RBMM p.54)

CMMS ใช้ไม่คุ้ม, เลือก PM ไม่เป็น, จัดคาบ PM ไม่เหมาะ, จัดระดับอะไหล่ไม่ได้, ตั้งงบไม่เป็น (สำคัญสุด รักษายากสุด), ไม่มีรายงานป้อนกลับที่ถูกต้อง จุดเริ่มต้นคือสอบทานสมรรถนะตนเองด้วยดัชนีใน [[Maintenance KPIs]]

## ข้อควรระวัง

- รูป Fig 2.2 อ่านจากภาพ ข้อความในช่องบางส่วนเป็นการสรุปจากบันทึกอ่านหนังสือ
- RCM "ต้นกำเนิดปี 1978" เป็นข้อความที่หนังสือระบุ (RBMM p.43) ไม่ได้ตรวจกับแหล่งอื่น

## เชื่อมโยงกับ compressor failure hierarchy

- ชั้น 2 ถึง 3 ต้องการ failure record ที่ถูกต้อง: ขั้นต่ำคือ failure mode/cause, Man-Hrs, ประเภท PM, การใช้อะไหล่, วัน-เวลาเหตุการณ์, ค่าใช้จ่าย และ equipment ที่เสียถึงระดับชิ้นส่วน (RBMM p.53) ใกล้เคียงสิ่งที่ [[ISO 14224]] และ [[OREDA]] ต้องการ แม้หนังสือไม่ได้อ้างมาตรฐานโดยตรง
- การเลือก PM ต่อ [[Failure Mode]] ของ [[Compressor]] (ชั้น 6) ต้องใช้ taxonomy ใน [[Failure Hierarchy]] เป็นฐานของ Failure Records ดู [[Failure Data Recording]]

## ดูเพิ่ม

- [[Asset Life Cycle]]
- [[Maintenance KPIs]]
- [[Maintenance Strategic Report]]
- [[RCM Reliability Centered Maintenance]]

## Triplets

- [[Maintenance Efficacy Pyramid]] [has_value:: 6 levels] maturity of maintenance organization (Fig 2.2, RBMM p.35-40)
- [[Maintenance Efficacy Pyramid]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 2
- [[Maintenance Efficacy Pyramid]] [uses:: 16-Topic Assessment] radar chart, 16 axes, 0-100% (Fig 2.1, RBMM p.32-35)
- Maintenance Cost Accounting [part_of:: 16-Topic Assessment] topic 2, one of 6 most important (RBMM p.35)
- Maintenance Performance Budgeting [part_of:: 16-Topic Assessment] topic 3, one of 6 most important (RBMM p.35)
- Performance Measuring Reporting and Control [part_of:: 16-Topic Assessment] topic 4, one of 6 most important; frequent root cause (RBMM p.33-35)
- Organization [part_of:: 16-Topic Assessment] topic 7, one of 6 most important (RBMM p.35)
- Method and Technical Management [part_of:: 16-Topic Assessment] topic 10, one of 6 most important (RBMM p.35)
- Spare Part Management [part_of:: 16-Topic Assessment] topic 13, one of 6 most important; linked to topics 2-7 and 10 (RBMM p.34-35)
- Spare Part Cost [has_value:: > 60-70%] of maintenance cost (RBMM p.34)
- Holding Cost [has_value:: 15-20%] of spare part price (RBMM p.34)
- Reactive [step_of:: [[Maintenance Efficacy Pyramid]]] level 1: break and fix (Fig 2.2)
- Immature [step_of:: [[Maintenance Efficacy Pyramid]]] level 2: good process, poor content (Fig 2.2)
- Maintenance Work Control [step_of:: [[Maintenance Efficacy Pyramid]]] level 3, do first: strategies, accountability, planning/scheduling, parts, work control indices (Fig 2.2, p.36-38)
- Maintenance Cost Control [step_of:: [[Maintenance Efficacy Pyramid]]] level 4: cost accounting, full cost per unit, cost control indices (Fig 2.2)
- Maintenance Performance Budgeting [step_of:: [[Maintenance Efficacy Pyramid]]] level 5: workload budget, full fixed cost rate, cost per unit produced (Fig 2.2)
- Maintenance Optimization [step_of:: [[Maintenance Efficacy Pyramid]]] level 6: planned maintenance and spare part optimization (Fig 2.2)
- Best in Class and Sustainable [part_of:: [[Maintenance Efficacy Pyramid]]] top of pyramid (Fig 2.2)
- Accountability [differs_from:: Responsibility] must explain results and reasons when asked (RBMM p.37)
- Cost Control [differs_from:: Loss Control] loss control depends on strategy, do the right thing and do the thing right (RBMM p.38-39)
- Total Maintenance [has_formula:: Total Planned + Total Unplanned] each split into Man-Hrs and Materials plus losses (Fig 2.3, RBMM p.39-40)
- [[PM Task Selection]] [step_of:: Maintenance Improvement Cycle] PM Selection? via RCM Process (Fig 2.4, RBMM p.40-42)
- [[PM Interval Optimization]] [step_of:: Maintenance Improvement Cycle] Optimum PM Interval? (Fig 2.4)
- [[Spare Part Criticality and Risk]] [step_of:: Maintenance Improvement Cycle] Stock Performance? risk based spare part optimization (Fig 2.4)
- [[Maintenance Budget]] [step_of:: Maintenance Improvement Cycle] Budgeting and Control? performance budgeting (Fig 2.4)
- [[Maintenance Strategic Report]] [step_of:: Maintenance Improvement Cycle] Problem of Reporting? (Fig 2.4)
- [[Criticality Assessment]] [step_of:: Reliability Based Maintenance Selection and Optimization] step 1 select equipment by criticality (Fig 2.5, RBMM p.42-43)
- [[FMECA]] [step_of:: Reliability Based Maintenance Selection and Optimization] step 2 qualitative RPN (Fig 2.5)
- [[Weibull Analysis]] [step_of:: Reliability Based Maintenance Selection and Optimization] step 3 failure data analysis, quantitative criticality (Fig 2.5)
- [[PM Task Selection]] [step_of:: Reliability Based Maintenance Selection and Optimization] step 4 select PM type (Fig 2.5)
- [[PM Interval Optimization]] [step_of:: Reliability Based Maintenance Selection and Optimization] step 5 optimal task interval (Fig 2.5)
- Reliability Based Maintenance Selection and Optimization [selects:: Scheduled Overhaul or Discard] scheduled replacement/overhaul (Fig 2.5)
- Reliability Based Maintenance Selection and Optimization [selects:: Condition Monitoring] scheduled CM/inspection (Fig 2.5)
- Reliability Based Maintenance Selection and Optimization [selects:: Scheduled Failure Finding] hidden failure finding (Fig 2.5)
- Reliability Based Maintenance Selection and Optimization [selects:: Run to Failure] (Fig 2.5)
- [[Maintenance Efficacy Pyramid]] [has_value:: 6 maintenance diseases] CMMS not worth it, poor PM selection, wrong PM interval, no stock level, no budgeting (most important), no feedback report (RBMM p.54)
- [[Maintenance KPIs]] [input_to:: [[Maintenance Efficacy Pyramid]]] self-assessment starting point (RBMM p.54)
- [[RCM Reliability Centered Maintenance]] [has_value:: 1978] origin year as stated by book, not cross-checked (RBMM p.43)
- Maintenance Work Control [uses:: [[Failure Data Recording]]] minimum record: failure mode/cause, Man-Hrs, PM type, parts, date-time, cost, equipment to part level (RBMM p.53)

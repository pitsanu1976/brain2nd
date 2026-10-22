---
title: RCM Reliability Centered Maintenance
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [rcm, pm, reliability, maintenance-management, weibull, book]
sources: [reliability-based-maintenance-management.md]
confidence: high
contested: false
---

# RCM (Reliability Centered Maintenance)

**RCM** คือกระบวนการคัดเลือกงานบำรุงรักษาตามแผน (scheduled PM) โดยแยกตาม Failure Mode และใช้ความรู้ Reliability ตัดสิน เสนอโดย Nowlan และ Heap (1978) จากงาน Boeing 747 แนวคิดหลักคือเปลี่ยนจากบำรุงรักษา "ตัวเครื่อง" เป็นบำรุงรักษา "หน้าที่ (function)" ของมัน (RBMM p.114-115) RBMM บท 5 แยก RCM เป็น 2 ส่วน: **Process** (ไม่ยาก) กับ **Contents** (ยากกว่า คือวิเคราะห์สถิติ) ผลลัพธ์คือรายการ "งานตามแผนที่ไม่ทำไม่ได้" นำไปสู่ Zero Breakdown (RBMM p.152) หนังสืออ้างมาตรฐาน SAE JA1011/JA1012

## สาระสำคัญ 4 ข้อ (RBMM p.115)

1. รู้หน้าที่ของชิ้นส่วนทุกชิ้นชัดเจน
2. จัดลำดับความสำคัญ/ความวิกฤติของหน้าที่
3. รู้ Failure Mode ที่เป็นไปได้ทั้งหมด
4. รู้พฤติกรรมการเสีย (failure rate) ของชิ้นส่วน

## 7 กระบวนการ (Fig 5.1, RBMM p.115-128)

| # | กระบวนการ | สาระ |
|---|---|---|
| 1 | Registration of Assets | ขึ้นทะเบียนใน asset register ของ [[CMMS]] |
| 2 | Criticality Assessment + Functional Performance + Operating Context | เลือก asset ตามความวิกฤติ ดู [[Criticality Assessment]] |
| 3 | Evaluation of Failure Consequences | Safety / Hidden / Operational / Non-Operational |
| 4 | Risk Based Scheduled PM Task Selection | เลือกชนิดงานและคาบ ดู [[PM Task Selection]] |
| 5 | Work Packaging, Scheduling, Executing and Control | รวม PM กับงานนอกแผนเป็นแผนรวม ใช้ทรัพยากรคุ้มสุด |
| 6 | Maintenance Analysis | Age Exploitation, Failure Consequence Analysis, Inspection Finding, Actuarial Analysis, Performance/Strategic Reports, Indices (feedback loop สำคัญสุด) |
| 7 | Modification Maintenance / Application of Engineering Standards | redesign หรือใช้เทคโนโลยีใหม่เมื่องานที่ควรทำกลับทำไม่ได้ |

กระบวนการ 2-4 มักอยู่นอก CMMS (ต้องใช้ความรู้เครื่อง) แต่ขาดไม่ได้ ไม่เช่นนั้น PM มาจาก "น่าจะทำ" (RBMM p.107)

## กระบวนการ 2: Boundary, Function และ Operating Context (RBMM p.120-124)

- Boundary: Plant (Productive Unit) > System > Sub-Subsystem > Equipment > Component (Fig 5.7) ต้องระบุว่ารวม/ไม่รวมอะไร เลือกระดับ System/Plant ต้องวิเคราะห์ทุก FM ในขอบเขต
- Primary Function ต้องมี Object, Verb ที่เห็นภาพ และ Quantity ที่วัดได้ (เช่น ตัน/ชั่วโมง); Secondary Function เช่น สิ่งแวดล้อม ความปลอดภัย ป้องกันรั่ว Protective Function Economic Efficiency
- Functional Failure = ทำหน้าที่ตาม spec ไม่ได้ (complete หรือ partial)
- Operating Context: ประเภทกระบวนการ (Batch/Process), Quality/Environment/Safety Standards, Theater of Operation, Intensity of Operation, Redundancy

ตัวอย่างปั๊ม (Fig 5.8-5.9, RBMM p.122-124): มอง physical พบ 5 FM (Bearing แตก, Coupling ลื่น, Suction line ตัน, Impeller สึก, Impeller แตก) ทุก FM ดูสำคัญเท่ากัน มอง function-centered: Functional Failure 1 (complete) = Impeller แตก, Bearing แตก; Functional Failure 2 (partial) = Suction line ตัน, Impeller สึก, Coupling ลื่น จำนวน FM เท่าเดิม (5) แต่แยกความรุนแรงได้

## กระบวนการ 3: Failure Consequence (RBMM p.124-125)

- Evident Failure: Safety / Operational (ผลิต+ซ่อม) / Non-operational (ซ่อมอย่างเดียว)
- Non-Evident (Hidden) Failure: ส่วนมากเป็นระบบป้องกัน ไม่มีผลจนเกิด **Multiple Failure** ผลมักรุนแรง

## กระบวนการ 4: Task Selection (RBMM p.125-126)

5 ประเภทงานของ Nowlan และ Heap: Scheduled Condition Monitoring, Scheduled Overhaul/Discard, Scheduled Failure Finding, Run to Failure, Re-design

| Consequence | งานที่เลือกได้ (Fig 5.10 Nowlan-Heap / Fig 5.11 SAE JA1012) |
|---|---|
| Evident Safety/Environment | Condition Monitoring, Restore/Discard, Combination of Tasks, Redesign เป็นข้อบังคับ ถ้าทำอะไรไม่ได้ |
| Evident Operational | CM, Restore/Discard, (Combination), No Scheduled Maintenance/RTF, Redesign อาจพึงประสงค์ |
| Evident Non-operational | CM, Restore/Discard, No Scheduled Maintenance/RTF, Redesign อาจพึงประสงค์ |
| Hidden | CM, Restore/Discard, Failure Finding, Redesign อาจพึงประสงค์ (Safety/Environment: Redesign compulsory) |

SAE JA1012 ให้ความสำคัญ Safety และ Environment สูงมาก (Fig 5.11) การเลือกงานต้องวิเคราะห์รูปแบบการเสียด้วยสถิติ (RBMM บท 7) ดู [[Failure Finding Interval]] และ [[P-F Interval and Condition Monitoring]]

## Practical RCM: 7 คำถาม (RBMM p.135)

1. หน้าที่ของอุปกรณ์ในกรอบคืออะไร 2. Functional Failure คืออะไร 3. สาเหตุ (Failure Modes) 4. ผลกระทบ (Effects) 5. ผลที่ตามมา (Consequences) 6. นโยบายบำรุงรักษาที่ป้องกัน/หลีกเลี่ยง/ทำนายได้ 7. ถ้า PM ป้องกันไม่ได้จะทำอย่างไร

ผู้เขียนเสนอสรุปบนกระดาษ A4 แผ่นเดียว (Fig 5.18, p.136) ตัวอย่าง Boiler Circulating Pump set X (ปั๊มหมุนเวียน boiler 5,000 ลิตร/นาที [หน่วยอ่านไม่ออกชัด]):

| Failure Mode | Weibull Beta | Eta | ตีความ (ในหนังสือ) |
|---|---|---|---|
| Impeller broke | 4.352 | 6 ปี | wear-out ชัดเจน |
| Bearing broke | 3.876 | 2.35 ปี | wear-out ชัดเจน |
| Control failure | 0.997 | 10.5 ปี | ~1 = random |

PM Task และ Interval ยังเป็น "?" (ยังไม่วิเคราะห์) ดู [[Weibull Analysis]] และ [[Failure Patterns and Bathtub Curve]]

## Classical RCM vs Fast Track RCM (RBMM p.149-151)

- Classical (Fig 5.26): Asset Selection > Function > Functional Failure > Severity > Failure Effect > Cause (FM) > Occurrence, Detect-ability ครบทุก Function ใช้เวลา/ทรัพยากรมาก
- Fast Track 7 ขั้น: (1) กำหนด Productive Unit สำคัญ (2) คัด Dominant Equipment จากผลการเสีย (3) คัด Dominant FM (4) รวบรวม PM ทั้งหมด (5) คัดงานตามแผนที่จับคู่กับงานนอกแผนได้เท่านั้น (6) ปรับ/เลือก PM ใหม่ให้ประสิทธิผลสูงสุด (7) ทบทวน PM ไม่สำคัญเพื่อยกเลิก
- Fast Track เร็วกว่าแต่เสี่ยงตกหล่นอุปกรณ์/กรอบ มุ่งที่ FM เป็นหลัก ถือว่า Severity ของ FM กระทบ function เหมือนกันหมด และ criticality ของ equipment อยู่นอกกระบวนการ (Fig 5.27, p.150) ข้อมูลวิกฤติที่ชี้ขาดความสำเร็จคือ record 5 รายการ ดู [[Failure Data Recording]]

## ตัวอย่างรถยนต์ (Fig 5.25, RBMM p.146-149)

อายุออกแบบ 300,000 กม. ตัวอย่างการกำหนดคาบ:
- Lube oil อายุเฉลี่ย 13,000 กม. ไม่เสื่อมก่อน 8,000 และไม่เกิน 15,000 -> เปลี่ยนทุก 10,000 กม.
- Timing belt อายุเฉลี่ย 110,000 กม. ไม่เสียก่อน 90,000 ไม่เกิน 130,000 -> ผู้ผลิตกำหนดเปลี่ยนที่ 80,000 กม. (safe-life)
- Water pump มีสัญญาณเตือน (ระดับน้ำพร่อง) -> inspection ทุก 10,000 กม. แทนเปลี่ยนตามเวลา
- Gear box -> Scheduled Overhaul
- งานที่พบจาก inspection แล้วเปลี่ยนล่วงหน้า = CM-Planned ลดการซ่อมนอกแผน

## RCM กับ FMECA

FMECA เป็นกระบวนการอิสระจากฝั่งออกแบบ/ผลิต RCM ดู function ของกรอบ (Productive Unit) ส่วน FMECA วิเคราะห์ระดับ equipment ว่าเสียอย่างไร RCM ใช้ FMECA database ที่มีอยู่ได้ โดยเฉพาะโรงงานใหม่ที่ไม่มีประวัติ (RBMM p.137) รายละเอียดดู [[FMECA]]

## เชื่อมโยงกับ compressor failure hierarchy

- Failure Mode ที่ RCM ต้องรู้ (ข้อ 3 ของ 4 สาระ) หาได้จาก [[Failure Mode]] 19 โหมดและ [[Failure Mechanism]] ของ [[OREDA]] ส่วนข้อ 4 (failure rate) หนังสือแนะให้หาเป็นราย FM ส่วน OREDA ใน wiki ให้ % ต่อโหมด ไม่ใช่ Weibull parameters (ไม่มีใน sources)
- เทียบ Fig 5.8-5.9 กับ compressor: จัด FM ระดับ [[Maintainable Item]] (เช่น seal, bearing, instrument) ตามผลต่อ function ของ [[Compressor]] (complete เช่น BRD/UST/FTS; partial เช่น LOO/PDE) เป็นการตีความ ไม่ใช่ข้อมูลในหนังสือ
- Hidden failure ของระบบป้องกัน (เช่น PSV, ESD, trip) -> Scheduled Failure Finding ตามหลัก (RBMM p.125-126; ตัวอย่างอุปกรณ์เป็นการตีความ)
- AIR (abnormal instrument reading) และ SER เป็นโหมดที่ % สูงใน wiki ควรระวังเมื่อใช้ record ชนิด Damage Code เป็นฐานเลือก dominant FM (การตีความ)

## ดูเพิ่ม

- [[FMECA]]
- [[Criticality Assessment]]
- [[PM Task Selection]]
- [[CMMS]]
- [[Failure Data Recording]]
- [[Redundancy and Standby Systems]]

## Triplets

- [[RCM Reliability Centered Maintenance]] [selects:: Scheduled PM Task] per failure mode, using reliability knowledge (RBMM p.114-115)
- [[RCM Reliability Centered Maintenance]] [defined_in:: Nowlan and Heap] 1978, from Boeing 747 work (RBMM p.114-115)
- [[RCM Reliability Centered Maintenance]] [defined_in:: SAE JA1011] cited by the book
- [[RCM Reliability Centered Maintenance]] [defined_in:: SAE JA1012] cited by the book
- [[RCM Reliability Centered Maintenance]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 5
- [[RCM Reliability Centered Maintenance]] [applies_to:: Function] maintains the function rather than the machine (RBMM p.114-115)
- [[RCM Reliability Centered Maintenance]] [has_part:: RCM Process] the easier part (RBMM ch5)
- [[RCM Reliability Centered Maintenance]] [has_part:: RCM Contents] the harder part, statistical analysis (RBMM ch5)
- [[RCM Reliability Centered Maintenance]] [produces:: Zero Breakdown] via list of scheduled tasks that cannot be skipped (RBMM p.152)
- [[RCM Reliability Centered Maintenance]] [uses:: Function] essential 1: know the function of every part (RBMM p.115)
- [[RCM Reliability Centered Maintenance]] [uses:: [[Criticality Assessment]]] essential 2: prioritise criticality of functions (RBMM p.115)
- [[RCM Reliability Centered Maintenance]] [uses:: [[Failure Mode]]] essential 3: know all possible failure modes (RBMM p.115)
- [[RCM Reliability Centered Maintenance]] [uses:: Failure Rate] essential 4: know failure behaviour of parts (RBMM p.115)
- Registration of Assets [step_of:: [[RCM Reliability Centered Maintenance]]] process 1 (Fig 5.1, RBMM p.115-128)
- Registration of Assets [uses:: [[CMMS]]] asset register
- [[Criticality Assessment]] [step_of:: [[RCM Reliability Centered Maintenance]]] process 2, with Functional Performance and Operating Context (Fig 5.1)
- Evaluation of Failure Consequences [step_of:: [[RCM Reliability Centered Maintenance]]] process 3: Safety, Hidden, Operational, Non-Operational (Fig 5.1)
- [[PM Task Selection]] [step_of:: [[RCM Reliability Centered Maintenance]]] process 4: Risk Based Scheduled PM Task Selection (Fig 5.1)
- Work Packaging Scheduling Executing and Control [step_of:: [[RCM Reliability Centered Maintenance]]] process 5 (Fig 5.1)
- Maintenance Analysis [step_of:: [[RCM Reliability Centered Maintenance]]] process 6, most important feedback loop (Fig 5.1)
- Modification Maintenance [step_of:: [[RCM Reliability Centered Maintenance]]] process 7, also Application of Engineering Standards (Fig 5.1)
- Primary Function [has_parameter:: Object] (RBMM p.120-124)
- Primary Function [has_parameter:: Verb] (RBMM p.120-124)
- Primary Function [has_parameter:: Quantity] measurable, e.g. tonnes per hour (RBMM p.120-124)
- Functional Failure [has_category:: Complete] (RBMM p.120-124)
- Functional Failure [has_category:: Partial] (RBMM p.120-124)
- Operating Context [has_parameter:: Redundancy] also process type, standards, theater and intensity of operation (RBMM p.120-124)
- Evident Safety Consequence [is_a:: Evident Failure] (RBMM p.124-125)
- Evident Operational Consequence [is_a:: Evident Failure] production loss plus repair (RBMM p.124-125)
- Evident Non-Operational Consequence [is_a:: Evident Failure] repair cost only (RBMM p.124-125)
- Hidden Failure [alias_of:: Non-Evident Failure] mostly protective systems (RBMM p.124-125)
- Multiple Failure [depends_on:: Hidden Failure] hidden failure has no effect until multiple failure, often severe (RBMM p.124-125)
- [[PM Task Selection]] [selects:: Condition Monitoring] Nowlan and Heap task type (RBMM p.125-126)
- [[PM Task Selection]] [selects:: Scheduled Overhaul or Discard] Nowlan and Heap task type (RBMM p.125-126)
- [[PM Task Selection]] [selects:: Scheduled Failure Finding] Nowlan and Heap task type (RBMM p.125-126)
- [[PM Task Selection]] [selects:: Run to Failure] Nowlan and Heap task type (RBMM p.125-126)
- [[PM Task Selection]] [selects:: Redesign] Nowlan and Heap task type (RBMM p.125-126)
- Redesign [applies_to:: Evident Safety Consequence] compulsory if nothing else works (Fig 5.10 Nowlan-Heap, Fig 5.11 SAE JA1012)
- Scheduled Failure Finding [applies_to:: Hidden Failure] (Fig 5.10, Fig 5.11)
- Run to Failure [applies_to:: Evident Operational Consequence] also Evident Non-Operational (Fig 5.10, Fig 5.11)
- RCM Question 1 [step_of:: [[RCM Reliability Centered Maintenance]]] what is the function of the equipment in context (RBMM p.135)
- RCM Question 2 [step_of:: [[RCM Reliability Centered Maintenance]]] what is the functional failure (RBMM p.135)
- RCM Question 3 [step_of:: [[RCM Reliability Centered Maintenance]]] causes, i.e. failure modes (RBMM p.135)
- RCM Question 4 [step_of:: [[RCM Reliability Centered Maintenance]]] effects (RBMM p.135)
- RCM Question 5 [step_of:: [[RCM Reliability Centered Maintenance]]] consequences (RBMM p.135)
- RCM Question 6 [step_of:: [[RCM Reliability Centered Maintenance]]] maintenance policy that prevents, avoids or predicts (RBMM p.135)
- RCM Question 7 [step_of:: [[RCM Reliability Centered Maintenance]]] what to do if PM cannot prevent (RBMM p.135)
- Impeller Broke [has_value:: 4.352] Weibull beta, eta 6 years, clear wear-out; Boiler Circulating Pump set X (Fig 5.18, RBMM p.136)
- Bearing Broke [has_value:: 3.876] Weibull beta, eta 2.35 years, clear wear-out (Fig 5.18, RBMM p.136)
- Control Failure [has_value:: 0.997] Weibull beta, eta 10.5 years, about 1 = random (Fig 5.18, RBMM p.136)
- Classical RCM [is_a:: [[RCM Reliability Centered Maintenance]]] covers every function, time and resource heavy (Fig 5.26, RBMM p.149-151)
- Fast Track RCM [is_a:: [[RCM Reliability Centered Maintenance]]] 7 steps (RBMM p.149-151)
- Fast Track RCM [differs_from:: Classical RCM] faster but may miss equipment; FM-focused, assumes equal FM severity, equipment criticality outside process (Fig 5.27, RBMM p.150)
- Fast Track Step 1 [step_of:: Fast Track RCM] define important Productive Unit
- Fast Track Step 2 [step_of:: Fast Track RCM] select Dominant Equipment by failure consequence
- Fast Track Step 3 [step_of:: Fast Track RCM] select Dominant Failure Mode
- Fast Track Step 4 [step_of:: Fast Track RCM] collect all existing PM
- Fast Track Step 5 [step_of:: Fast Track RCM] keep only scheduled tasks that match unplanned work
- Fast Track Step 6 [step_of:: Fast Track RCM] adjust or select new PM for maximum effectiveness
- Fast Track Step 7 [step_of:: Fast Track RCM] review unimportant PM for cancellation
- Fast Track RCM [uses:: [[Failure Data Recording]]] 5 critical records decide success (RBMM p.150)
- Lube Oil [has_value:: 10,000 km] replacement interval; mean life 13,000 km, not before 8,000, not over 15,000 (Fig 5.25, RBMM p.146-149)
- Timing Belt [has_value:: 80,000 km] manufacturer safe-life replacement; mean life 110,000 km, range 90,000-130,000 (Fig 5.25)
- Water Pump [detected_by:: Inspection] every 10,000 km, warning sign is low coolant level (Fig 5.25)
- Gear Box [resolved_by:: Scheduled Overhaul or Discard] scheduled overhaul (Fig 5.25)
- [[RCM Reliability Centered Maintenance]] [uses:: [[FMECA]]] existing FMECA database, especially new plants without history (RBMM p.137)
- [[FMECA]] [differs_from:: [[RCM Reliability Centered Maintenance]]] FMECA equipment level from design side; RCM function of Productive Unit (RBMM p.137)
- [[RCM Reliability Centered Maintenance]] [uses:: [[OREDA]]] failure modes and mechanisms; OREDA gives % per mode, not Weibull parameters
- Scheduled Failure Finding [applies_to:: Protective System] e.g. PSV, ESD, trip; equipment examples are interpretation (RBMM p.125-126) [confidence:: low]

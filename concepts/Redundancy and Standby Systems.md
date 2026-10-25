---
title: Redundancy and Standby Systems
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [pm, criticality, reliability, maintenance-management, book, iso-14224, cmrp, reliability-allocation]
sources: [reliability-based-maintenance-management.md, iso-14224.md, cmrp.md]
confidence: medium
contested: false
---

# Redundancy and Standby Systems

Redundancy (ระบบสำรอง) เป็นวิธีเพิ่มความน่าเชื่อถือของระบบนอกเหนือจากการใช้เครื่องที่ reliable สูง RBMM ชี้ว่าการมีเครื่องสำรองไม่ได้ทำให้ criticality ต่ำลงอัตโนมัติ เพราะเครื่อง standby อาจเสียแบบ Hidden Failure จนเกิด Multiple Failure เมื่อเครื่องหลักหยุด และการ optimize PM ราย equipment ไม่เท่ากับ optimize ระบบ (RBMM p.29, p.215-218, p.231)

## รูปแบบและสัญกรณ์ (RBMM p.28-29, p.215)

- k out of n: ต้องการ k จาก n หน่วย (เช่น 1 out of 2, 2 out of 3)
- Standby: ต้องใช้งาน 2 เครื่อง (2 ใน 3) อีก 1 เครื่องสำรองพร้อมใช้ทันที
- Load Sharing: ทุกเครื่องแบ่งภาระ (ตัวอย่าง 3 เครื่อง แต่ละเครื่องรับ 1/3 และรับเพิ่มได้เต็ม 50%)
- อุปกรณ์สลับเปลี่ยน (switching device, รูป 7.35) ตรวจสถานะและต่อสำรองอัตโนมัติหรือด้วยมือ
- Redundancy ระดับ process ใช้ถังเก็บผลผลิตระหว่าง process ลด criticality ภาพรวม (Fig 1.8, p.29-30) ภายใต้ขีดจำกัดปริมาณและระยะเวลาที่ป้อนได้

โครงสร้างเชิงความน่าจะเป็นของ k/n ดู [[Reliability Block Diagram]]

## Criticality ของเครื่องที่มีสำรอง (RBMM p.28-29)

- ไม่มี redundancy (เครื่องอนุกรม): ทุกเครื่อง criticality A
- มี redundancy ระดับเครื่อง: กลุ่มขนานอาจเป็น A/B/C ตามความสามารถรับภาระ แต่เครื่องก่อน/หลังกลุ่มขนานยังเป็น A
- เครื่อง standby อาจเสียซ่อน จึงยังสำคัญสูง; Load Sharing ลด criticality ได้ ขึ้นกับความสามารถรับภาระของแต่ละเครื่อง
- ดูวิธีประเมินใน [[Criticality Assessment]]

## ข้อพิจารณาด้าน PM (RBMM p.215-217, p.231)

1. แผนการใช้งาน: เครื่องที่ใช้มากเสี่ยงเสียมากกว่า ไม่ควรสลับใช้เท่า ๆ กัน (จะเสียไล่เลี่ยกัน) ควรใช้สัดส่วน 80/20 หรือ 60/40 และทดสอบเครื่องสำรองสม่ำเสมอ เพื่อให้อายุใช้งานต่างกัน
2. แผน PM ประกอบด้วยเครื่อง n เครื่อง + อุปกรณ์สลับเปลี่ยน; switching device ใช้ Failure Finding เหมือน protective device ดู [[Failure Finding Interval]]
3. เครื่อง n เครื่องเลือกงานได้ทุกประเภท โดยพิจารณา Multiple Failure เป็นหลัก ดู [[PM Task Selection]]
4. ทำ Condition Monitoring ทั้งเครื่องที่ใช้งานและ standby (Ch.1 p.29) ดู [[P-F Interval and Condition Monitoring]]
5. เป้าหมายอาจเป็นความมั่นคงของระบบมากกว่าต้นทุนต่ำสุด

## ขั้นตอนวิเคราะห์ระบบ k/n (รูป 7.36-7.37, RBMM p.217)

```
1. เริ่มจาก Dominant Failure Mode
2. วิเคราะห์ข้อมูลเสียรายเครื่อง/ราย failure mode (FM1, FM2, FM3 ... และ FMsw ของตัวสลับ)
3. เลือกงานและคาบ PM ต่อ failure mode (แต่ละ FM มี maintenance policy ของตัวเอง)
4. รวมเป็น Total R(t) ของระบบ k/n ด้วย Monte Carlo Simulation
5. ปรับคาบ PM ให้ระบบรอดตามแผนการใช้งาน
```

การรวม reliability ทำด้วย [[Monte Carlo Maintenance Simulation]] ตามหนังสือ ไม่มีสูตรปิดในบทนี้

## มุมมองของ ISO 14224 / ISO/TR 12489

สรุปด้วยถ้อยคำของผู้เขียน wiki (เสริม ไม่ขัดกับ RBMM)

- **ชนิด redundancy** (ISO 14224 cl. C.1.2, p.205): passive/cold standby (ส่วนสำรองไม่ทำงานจนถูกเรียก), active/hot standby (ทำงานพร้อมกัน), mixed วัดด้วย ERF เช่น 3 x 50% = ERF 1.5 ตรงกับตัวอย่าง Standby vs Load Sharing ข้างต้น
- **การนับ failure**: failure ของ unit ในระบบ redundant ให้นับเมื่อประเมินอะไหล่และกำลังซ่อม แต่ไม่นับเมื่อประเมิน availability ของระบบ (cl. C.1.2, p.205)
- **กฎ "critical failure" เมื่อมี redundancy** (ISO 14224 cl. F.4.1, p.253-254): ถ้า SIF มี A กับ B เป็น redundant, dangerous failure ของ A เป็น critical ตาม TR 12489 ก็ต่อเมื่อเป็น critical ตาม ISO 14224 และ B เสียแบบ dangerous critical อยู่ก่อนแล้ว นี่คือเหตุผลที่ standby ซึ่งเสียซ่อนทำให้เกิด multiple failure ตามที่ RBMM เตือน
- **CCF**: redundancy ใช้ผลได้ไม่เต็มเมื่อหลายตัวเสียจากสาเหตุร่วม (common cause) หรือ mode เดียวกัน (common mode) ถ้าสมมติอิสระต่อกัน ผลจะดีเกินจริง ซึ่งไม่ conservative; ใช้ beta-factor เมื่อวิเคราะห์ละเอียดไม่ได้ (ISO 14224 cl. C.1.4-C.1.7, p.206-207; cl. 3.5-3.6, p.3) ดู [[Safety Critical Failure Classification]]
- ความหมายของ "critical" ในหน้านี้กับ ISO ต่างกัน ดู [[Failure Impact Classification]]

## Redundancy กับการกระจายเป้า reliability (เพิ่ม 2026-10-25, sources: cmrp.md)

- เมื่อเป้า reliability ของระบบสูงกว่าที่ชิ้นส่วนเดิมทำได้ ทางเลือกคือยก reliability ของชิ้นเดียว (ผ่าน cost/penalty function) หรือเพิ่มการต่อขนาน สไลด์ [[CMRP Course]] แสดงว่าในระบบขนาน 0.6/0.7/0.8 (R = 0.976) ยกชิ้นเดียวก็ถึงเป้า 0.99 ได้ แต่ระบบอนุกรม 0.7/0.8/0.9 ยกชิ้นเดียวไม่พอถึง 0.85 (CMRP CMPR-04 p.46-47) วิธีหาชุดที่ต้นทุนรวมต่ำสุดดู [[Reliability Allocation]]
- การคำนวณ availability ของระบบด้วย RBD/FTA ต้องรวม redundancy, common cause และ dormant failure (CMRP CMPR-04 p.21) สอดคล้องกับข้อเตือนเรื่อง hidden failure และ CCF ด้านบน

## เชื่อมโยงกับ compressor failure hierarchy

- กรณี compressor A/B (1 out of 2 หรือ 2 out of 3) ตามตัวอย่างของหนังสือ ต้องแยก failure mode ราย [[Compressor]] และ failure mode ของ switching/auto-changeover; ข้อความเดิม "ISO 14224 ไม่ได้บันทึก redundancy เป็นฟิลด์ใน sources" เขียนก่อน ingest มาตรฐาน ตอนนี้ ISO 14224 อธิบายชนิด redundancy และ ERF ไว้ (ดูหัวข้อมุมมอง ISO ด้านบน) แต่ notes ที่ ingest ไม่ได้ระบุว่ามีฟิลด์ redundancy ใน equipment data ของ compressor (Table A.10)
- standby ที่เสียซ่อน ตรงกับ failure on demand เช่น FTS ใน [[Failure Mode]] (ข้อเสนอแนะ ไม่ใช่ข้อมูลใน sources)
- ข้อมูลใน [[OREDA]] เป็นระดับ item ไม่มีข้อมูล redundancy configuration ใน sources ของ wiki นี้

## ดูเพิ่ม

- [[Failure Finding Interval]]
- [[PM Interval Optimization]]
- [[Reliability Block Diagram]]
- [[Criticality Assessment]]
- [[PM Task Selection]]
- [[Reliability Allocation]]

## Triplets

- Redundancy [is_a:: System Reliability Improvement Method] besides using high-reliability machines
- Redundancy [differs_from:: Low Criticality] standby does not automatically lower criticality (RBMM p.29, p.215-218, p.231)
- Standby Unit [has_failure_mode:: Hidden Failure] can lead to Multiple Failure when main unit stops
- Equipment PM Optimization [differs_from:: System PM Optimization] optimizing each equipment is not optimizing the system
- k out of n [is_a:: Redundancy Configuration] e.g. 1 out of 2, 2 out of 3 (RBMM p.28-29, p.215)
- Standby [is_a:: Redundancy Configuration] 2 of 3 required, 1 ready immediately
- Load Sharing [is_a:: Redundancy Configuration] e.g. 3 units 1/3 load each, can take up to 50%
- Switching Device [part_of:: Redundancy] checks status, connects standby automatically or manually (Fig 7.35)
- Process Buffer Tank [is_a:: Process Level Redundancy] lowers overall criticality within volume/time limits (Fig 1.8, p.29-30)
- k out of n [related_to:: [[Reliability Block Diagram]]] probabilistic structure
- Series Equipment Without Redundancy [has_category:: Criticality A] (RBMM p.28-29)
- Parallel Group [has_category:: Criticality A/B/C] by load capacity; equipment before/after group stays A
- Load Sharing [produces:: Lower Criticality] depends on each unit's load capacity
- [[Redundancy and Standby Systems]] [related_to:: [[Criticality Assessment]]]
- Redundant Unit Operation Plan [has_value:: 80/20 or 60/40] avoid equal rotation so units do not fail together; test standby regularly (RBMM p.215-217)
- Switching Device [uses:: Failure Finding] like protective device; see [[Failure Finding Interval]]
- Redundant Units [uses:: [[PM Task Selection]]] any task type, Multiple Failure as main consideration
- Redundant Units [uses:: Condition Monitoring] both running and standby units (p.29); see [[P-F Interval and Condition Monitoring]]
- Redundant System PM [has_value:: System Security Over Minimum Cost] possible objective
- Start From Dominant Failure Mode [step_of:: k/n System Analysis] step 1 (Fig 7.36-7.37, RBMM p.217)
- Analyze Failure Data Per Unit And Mode [step_of:: k/n System Analysis] step 2, FM1..FMn and FMsw
- Select PM Task And Interval Per Failure Mode [step_of:: k/n System Analysis] step 3
- Combine Total R(t) By Monte Carlo [step_of:: k/n System Analysis] step 4
- Adjust PM Intervals To System Survival [step_of:: k/n System Analysis] step 5
- k/n System Analysis [uses:: [[Monte Carlo Maintenance Simulation]]] no closed-form formula in book chapter
- Passive Cold Standby [is_a:: Redundancy Type] (ISO 14224 cl. C.1.2, p.205)
- Active Hot Standby [is_a:: Redundancy Type] (ISO 14224 cl. C.1.2, p.205)
- Mixed Redundancy [is_a:: Redundancy Type] measured by ERF
- ERF [has_value:: 1.5] 3 x 50% (ISO 14224 cl. C.1.2)
- Redundant Unit Failure [input_to:: Spare And Repair Capacity Assessment] counted; not counted for system availability (ISO 14224 cl. C.1.2)
- Dangerous Failure Of Redundant SIF Unit A [has_category:: Critical] only if critical per ISO 14224 and B already failed dangerous critical (ISO 14224 cl. F.4.1, p.253-254)
- Common Cause Failure [depends_on:: Redundancy] limits benefit; independence assumption is non-conservative (ISO 14224 cl. C.1.4-C.1.7)
- Beta-factor Model [applies_to:: Common Cause Failure] when detailed analysis not possible; see [[Safety Critical Failure Classification]]
- Critical In RBMM [differs_from:: Critical In ISO 14224] see [[Failure Impact Classification]]
- Compressor A/B [is_a:: k out of n] 1 out of 2 or 2 out of 3; separate failure modes per [[Compressor]] and changeover
- Hidden Standby Failure [related_to:: FTS] failure on demand, wiki suggestion [confidence:: low]
- [[OREDA]] [has_value:: No Redundancy Configuration Data] item-level data in wiki sources
- Redundancy [related_to:: [[Reliability Allocation]]] alternative to raising a single unit's reliability (CMRP CMPR-04 p.46-47)
- System Availability Calculation [depends_on:: Redundancy] with common cause and dormant failure via RBD/FTA (CMRP CMPR-04 p.21)

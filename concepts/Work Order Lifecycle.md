---
title: Work Order Lifecycle
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [mpm, work-order, cmms, maintenance-management, work-management, book]
sources: [maintenance-profit-maker.md, reliability-based-maintenance-management.md, cmrp.md]
confidence: medium
contested: false
---

# Work Order Lifecycle (วงจรใบแจ้งซ่อม/ใบสั่งงาน)

วงจรของงานบำรุงรักษาตั้งแต่เกิดงานจนปิดลงประวัติและวิเคราะห์ ตามระบบบริหารงานบำรุงรักษา (Maintenance Management System, MMS) ในบทที่ 4 ของ [[Maintenance Profit Maker Book]] MMS คือการจัดกิจกรรมซ่อม/บำรุงรักษาทั้ง 16 งานให้เป็นกระบวนการต่อเนื่อง เพื่อให้เครื่องได้ผลผลิตสูงสุดตลอดอายุด้วยค่าใช้จ่ายต่ำสุด ระบบที่ดีใช้ได้ทั้งแบบมีและไม่มีคอมพิวเตอร์ ([[CMMS]]) (MPM p.60) หน้านี้สังเคราะห์จาก reading notes และเทียบกับ RBMM / CMRP ที่บันทึกไว้ใน [[CMMS]] และ [[Maintenance Planning and Scheduling]]

## 6 ขั้นของกระบวนการ (MPM p.61)

| ขั้น | ชื่อ | ผลลัพธ์หลัก |
|---|---|---|
| 1 | Work Requests | แจ้งซ่อม/รับรู้ความเสียหาย กลั่นกรองเบื้องต้น |
| 2 | Work Order Initiation and Planning | เปิด WO และประเมินขนาดงาน ทรัพยากร ค่าใช้จ่าย |
| 3 | Work Order Scheduling | กำหนดวันตามแผนผลิตและความพร้อมทรัพยากร |
| 4 | Work Order Execution and Control | ปฏิบัติงาน ติดตาม ส่งคืนเครื่อง |
| 5 | Work Completion and Close to History | ปิดงานเมื่อข้อมูลครบ ลงประวัติเครื่อง |
| 6 | Maintenance Work Analysis | วิเคราะห์เพื่อปรับปรุง |

หมายเหตุ: รายการใน p.61 พิมพ์ชื่ออังกฤษของขั้น 3 ซ้ำกับขั้น 4 ("Execution and Control") ชื่อที่ถูกตามหัวข้อในบท (p.69) คือ "Work Order Scheduling"

## Workflow และจุดอนุมัติ (Fig 4.2, Fig 4.4, MPM p.62-64)

ผังตัวอย่างมี 5 แถบ Initiation -> Planning -> Scheduling -> Execution -> Close:
- Initiation: ฝ่ายผลิตเปิดและอนุมัติ WR; PM เกิดตามเวลา/คาบ/เงื่อนไข; Predictive maintenance ใช้ปรับเงื่อนไข PM
- Planning: ตรวจ WR กับ Equipment Register -> เปิด WO หรือแจ้งยกเลิกกลับฝ่ายผลิต -> ประเมินอะไหล่ แรงงาน เครื่องมือ วิธีการ งานมาตรฐาน -> อนุมัติ
- Scheduling: กำหนดวันตามแผนผลิต และจองอะไหล่
- Execution: ขออนุญาต/รับเครื่อง พิมพ์ WO เบิก/คืนผ่านคลังและจัดซื้อ -> คืนเครื่อง ฝ่ายผลิตตรวจรับ
- Close: บันทึกอะไหล่ ชั่วโมง แรงงาน ค่าใช้จ่าย ค่าวัด แบบ ส่งข้อมูลให้บัญชี/บุคคล -> ตรวจความสมบูรณ์ -> ลงประวัติ -> วิเคราะห์

ผังมีจุด "อนุมัติ?" อย่างน้อย 3 จุด (แจ้งซ่อม, เปิด WO, แผนงาน) และจุดตรวจ "งานเสร็จ?" / "เสร็จสมบูรณ์?" 2 จุด ใบแจ้งซ่อมตัวอย่าง (Fig 4.4) มีการอนุมัติ WR 2 ชั้น (Owner Approve + Maintenance Approve) (MPM p.62-64)

| แหล่ง | จุดอนุมัติ |
|---|---|
| MPM | อย่างน้อย 3 จุด + อนุมัติ WR 2 ชั้น (MPM p.62-64) |
| RBMM | 2 จุด: อนุมัติแจ้งซ่อม และอนุมัติปิดงาน (Fig 4.10, RBMM p.104) |
| CMRP | ตามวงเงินประมาณการ หลายมิติ (CMRP CMPR-09 p.5, p.15, p.21) ดู [[CMMS]] |

เป็นความต่างของการออกแบบ workflow ตัวอย่าง ไม่ใช่ข้อเท็จจริงขัดกัน (ไม่ตั้ง contested)

## ขั้นที่ 1: Work Requests และการกลั่นกรอง (MPM p.63-67)

- ผู้ใช้เครื่อง/ฝ่ายผลิตพบอาการผิดปกติ -> ออก WR บันทึกตามที่พบ (as found); ใน CMMS แจ้งผ่านหน้าจอ และเชื่อม Plant Control and Information System ให้ระบบควบคุมแจ้งความผิดปกติเข้า CMMS ได้ (MPM p.63-65)
- **การกลั่นกรองเบื้องต้น** ลดปริมาณงาน: ประเมินความเร่งด่วน หรือยกเลิกก่อนเข้าระบบส่วนที่เหลือ (MPM p.63)
- รายงานหลัก: **Work Request Backlogs** (WR ที่ยังไม่ตอบสนอง เพื่อเร่งรัดหรือยกเลิก) และสรุปจำนวน WR ยกมา/เข้า/เสร็จ/ยกเลิก/ยกไป ตามหน่วยงานซ่อม (Fig 4.5-4.6, MPM p.63-65)
- งานที่ไม่ผ่าน WR: PM และ Condition Monitoring ตามกำหนด (calendar days, ชั่วโมง/มิเตอร์, turnaround) ระบบออก WO อัตโนมัติ เงื่อนไขต้องปรับให้ตรงสภาพปัจจุบัน; Modification/Improvement project ต้อง execute ผ่าน MMS เพื่อเก็บประวัติการเปลี่ยนแปลงเครื่อง (MPM p.65-67)
- งานเร่งด่วน: ลงมือได้ทันที ทำเอกสารคู่ขนาน (แจ้งด้วยวาจาก่อน แล้วตามด้วยเอกสารมีเลขอ้างอิง) (MPM p.67)
- **เลขอ้างอิงหลัก** = เลข WR และเลข WO ใช้ผูกกับระบบอื่น (ใบเบิก ค่าแรง งานจ้างเหมา) (MPM p.67)

## ขั้นที่ 2: เปิด WO และวางแผน (MPM p.67-69)

- บำรุงรักษากรอง WR อีกรอบ เป้าหมาย = บันทึกอาการเสียให้ถูก เพื่อให้ประวัติอาการและวิธีแก้อ้างอิงได้ ทางเลือก: เปิด WO หรือตกลงกับผู้แจ้งว่าแก้ได้โดยไม่ต้องเปิด WO; WR ที่ยกเลิกยังเก็บในแฟ้มยกเลิก (MPM p.67)
- WO ที่เปิดแล้วเข้ากลุ่ม Backlogs ทันที ระบบต้องแยกงานตามสถานะได้

### 7 สถานะของ WO (MPM p.67-68) เทียบ RBMM Work Backlog Basket

| # | MPM | RBMM Work Backlog Basket (Fig 4.12, RBMM p.106) |
|---|---|---|
| 1 | Initiated | New |
| 2 | Planned | Planning |
| 3 | Scheduled | Scheduling |
| 4 | Wait | Wait for Material / Shutdown / Others |
| 5 | Issued (พิมพ์ใบสั่งงานแล้ว) | In Progress |
| 6 | Finished (งานเสร็จ) | In Approval |
| 7 | Complete (ข้อมูลครบ พร้อมปิด) | History |

การจับคู่แถว 5-7 เป็นการตีความของ wiki โครงสร้างใกล้กัน ต่างที่ชื่อ และ MPM แยก Finished กับ Complete เป็นสองขั้น (งานเสร็จ vs ข้อมูลครบ) ตัวอย่างรายงานในบทใช้รหัสตัวเลขของซอฟต์แวร์ (เช่น "30 Scheduled", "50 In Program") ซึ่งไม่ใช่เลข 1-7 (MPM p.64, p.72-73)

### 7 คำถามของการวางแผน (MPM p.68-69)

1. ต้องใช้ทรัพยากรอะไร คนแต่ละประเภทเท่าไร ค่าใช้จ่าย ต้องจ้างเหมาหรือไม่
2. วิธีทำ มีงานมาตรฐาน แบบ ข้อมูลเทคนิคหรือไม่
3. ขั้นตอนควบคุม การตัดแยกระบบด้านความปลอดภัย สิ่งแวดล้อม เอกสารกำกับ
4. ใช้เวลากี่ชั่วโมง
5. ใช้เครื่องมือและอะไหล่อะไร อ้างอิงระบบคลังได้หรือไม่ ถ้าไม่มีต้องสร้างรหัสหรือซื้อตรง
6. ค่าใช้จ่ายรวม
7. ใช้งบหน่วยงานใด ใครอนุมัติ

ผลที่ได้ = ขนาดงานและระยะเวลา ข้อมูลต้องเป็นปัจจุบันเพราะกระทบ scheduling รายงานหลัก: WO ระหว่างวางแผน, ค่าใช้จ่ายประเมินรายงาน, รายการรออนุมัติ, รายละเอียดสาเหตุ (MPM p.69) เทียบ 6 องค์ประกอบ job plan ของ CMRP ที่ [[Maintenance Planning and Scheduling]]

## ขั้นที่ 3: Scheduling (MPM p.69-70)

- เงื่อนไขหลัก 2 ข้อ: (1) เครื่องพร้อมให้ซ่อม ตาม Production Plan หรือการตกลงหยุดเครื่อง (2) ทรัพยากรตามแผนพร้อมในวันทำงาน
- อุปสรรคใหญ่สุด = **ความพร้อมของอะไหล่** (จองให้งานได้) ถ้ากำหนดวันไม่ได้ ย้ายงานเข้าแฟ้ม **Wait** แยกหมวดตามสาเหตุเพื่อเร่งรัด:

| หมวดงานรอ (MPM p.70) | RBMM เทียบ |
|---|---|
| รออะไหล่ | Wait for Material |
| รอกำลังคน | (ไม่มีหมวดแยก) |
| รอเครื่องมือ | (ไม่มีหมวดแยก) |
| รอเครื่องจักรหยุด | Wait for Shutdown |
| อื่น ๆ | Others |

- **ประชุมประจำวันสั้น ๆ** ระหว่างหน่วยงานที่เกี่ยวข้อง ตรวจความพร้อมงานพรุ่งนี้และสัปดาห์หน้า งานของวันนี้คืองานที่ตกลงไว้เมื่อวาน ถ้าระบบนิ่งตกลงล่วงหน้าเป็นสัปดาห์/เดือนได้ (MPM p.69)
- **Resource Leveling Function** ของ CMMS เลื่อน/ปรับตารางตามข้อจำกัดทรัพยากร แต่จัดอัตโนมัติไม่ง่าย โดยเฉพาะกำลังคนที่ลาโดยไม่คาดหมาย (MPM p.69-70)
- รายงานหลัก: ผังแผนผลิตที่แสดงช่วงเครื่องว่างให้ซ่อม และงานในแฟ้มรอแยกหมวด (MPM p.70)

## ขั้นที่ 4: Execution and Control (MPM p.70-73)

- เตรียมเอกสารเป็นชุด: logistics หน้างาน (เบิกอะไหล่ เครื่องมือ), โอนเครื่องมาอยู่ในความรับผิดชอบของบำรุงรักษา (**Released for Maintenance**), ขั้นตอนความปลอดภัย **Safety Tags** และ isolation (MPM p.70-71)
- รายงานติดตาม: งานระหว่างทำพร้อม check list ความก้าวหน้า/ความปลอดภัย, งานที่ติดอุปสรรค, งานจ้างเหมาภายนอก (ควรอยู่ในระบบเดียวกันเพื่อประเมินผู้รับเหมา) (MPM p.71)
- เมื่องานเสร็จ: ปลด Safety Tags ต่อเครื่องกลับ -> คืนเครื่อง ฝ่ายผลิตตรวจรับ (**Accepted for Production**) -> รวบรวมรายละเอียดลงประวัติ โดยเฉพาะค่าใช้จ่าย; ด้านเทคนิคบันทึกค่าวัดและปรับแบบให้เป็นปัจจุบัน (MPM p.71-73)

## ขั้นที่ 5: ปิดงานลงประวัติ (MPM p.73-74)

- ฝ่ายผลิตรับเครื่องกลับ = ซ่อมเสร็จ แต่ **WO ยังไม่ปิด** จนกว่าย้ายข้อมูลครบเข้าแฟ้มประวัติประจำเครื่อง
- **Single Entry**: ข้อมูลเกิดที่ระบบเดียว MMS ต้องกระทบยอดกับระบบอื่นตลอด การแก้ข้อมูลจุดเดียวโดยพลการทำให้ข้อมูลทั้งบริษัทไม่น่าเชื่อถือ ตัวอย่าง: แก้จำนวนอะไหล่ใน WO โดยไม่แก้ใบเบิกคลัง ทำให้ค่าใช้จ่ายไม่ตรงงบการเงิน และกระทบยอดคงคลังไม่ได้ถ้าปิดงวดบัญชีแล้ว
- **การแก้งานที่ปิดแล้ว** ต้องมีขั้นตอนถูกต้องและทำโดยผู้มีอำนาจเท่านั้น จึงต้องทบทวนเอกสารอ้างอิงให้ครบก่อนปิด
- ข้อมูลสำคัญในการสรุปปิดงาน 3 อย่าง: สาเหตุการเสียตามหลักวิศวกรรม, ข้อมูลเวลา, ข้อมูลการใช้ปัจจัย (MPM p.74) ดู [[Failure Data Recording]]
- สอดคล้องกับกฎ RBMM ว่าห้ามปิด CM-Unplanned WO ถ้ายังไม่ระบุ Failure Mode (RBMM p.98, 110-111) และบทที่ 11 ของ MPM ที่ย้ำว่าการแก้ประวัติหลังปิดงวดบัญชีทำให้รายงานไม่ตรงบัญชี (MPM p.203-204)

## ขั้นที่ 6: วิเคราะห์งานบำรุงรักษา 9 เรื่อง (MPM p.74-77)

1. วิเคราะห์สาเหตุการชำรุด (FMEA/RCA) จัดสาเหตุเป็น Failure Tree ดู [[Root Cause Analysis]]
2. สมดุล Predictive / Condition Monitoring / PM และความถี่ที่เหมาะด้วย Reliability Engineering (ต้องมีข้อมูลย้อนหลังพอ)
3. รายงานค่าใช้จ่ายตามหน่วยงาน
4. ดัชนีพื้นฐาน MTBF, MTTR, MWT ดู [[Reliability Metrics]]
5. ทบทวนค่าใช้จ่าย 10 หรือ 20 อันดับแรก
6. ทบทวนปัญหา 10 หรือ 20 อันดับแรก
7. OEE ทั้งโรงงานและรายอุปกรณ์ แยก Availability / Performance / Quality losses ดู [[Availability and OEE]]
8. ค่าใช้จ่ายอะไหล่ เพื่อปรับปริมาณและรายการสำรอง ดู [[Spare Parts Management]]
9. การตั้งและใช้งบประมาณ ดู [[Maintenance Budget]]

### ตัวอย่างรายงาน (MPM p.75-80)

- **Fig 4.16 สรุป Cost และ Man Hours (MPM p.75)**: ผลรวมแนวตั้งรายคอลัมน์ถูก แต่ Total แนวนอน 2 แถวพิมพ์เกิน 900 ทำให้ Grand Total เกิน 1,800 (ค่าที่ถูก derived = Labor + Stock + Non Stock + Other):

| เครื่อง | Total (พิมพ์) | Total (derived) |
|---|---|---|
| PS03-FWP02 | 18,088.33 | 17,188.33 |
| PS03-RWP01 | 10,610.47 | 9,710.47 |
| Grand Total | 46,273.80 | 44,473.80 (= 19,670.00 + 16,013.33 + 5,570.47 + 3,220.00) |

- **Fig 4.18 MTBF-MTTR (MPM p.76)**: ชั่วโมงรวม 26,280 (= 3 x 8,760, derived) 18 เครื่อง เสีย 35 ครั้ง ซ่อม 783 ชม. สูตรที่รายงานใช้ (derived จากตัวเลข): MTBF = (ชั่วโมงทั้งหมด - เวลาซ่อม) / จำนวนครั้งเสีย ซึ่งไม่รวมเวลาซ่อม ต่างจาก RBMM ดู ข้อขัดแย้ง MPM-C4 ที่ [[Reliability Metrics]]; แถว PS03 พิมพ์ MTBF 5,255.00 ค่าที่ถูก (26,280 - 155)/5 = 5,225.00 (derived)
- Fig 4.19 ค่าซ่อมสูงสุด: ค่าใช้จ่ายสูงไม่จำเป็นต้องคู่กับ M-H สูง (FS02 480,720.00 บาท 93 M-H vs PS03 190,442.00 บาท 121 M-H) (MPM p.77)
- Fig 4.13 อัตราค่าแรงต่อ M-H ไม่สม่ำเสมอ น่าจะเป็นข้อมูลทดสอบของซอฟต์แวร์ ไม่ควรใช้เป็นอัตราอ้างอิง (MPM p.72)

## เชื่อมโยงกับ compressor failure hierarchy

(การตีความของ wiki ไม่ใช่ข้อความในหนังสือ)
- ขั้นที่ 2 (กรอง WR เพื่อบันทึกอาการให้ถูก) และขั้นที่ 5 (สาเหตุการเสียตามหลักวิศวกรรม) คือจุดที่ควรบังคับรหัส [[Failure Mode]] 3 ตัวอักษร, [[Failure Mechanism]] และ [[Failure Cause Codes]] ตาม [[Failure Hierarchy]] ก่อนเปลี่ยนสถานะ Finished -> Complete
- หมวด "รอเครื่องจักรหยุด" ของ compressor ที่มี spare/standby เกี่ยวกับ [[Redundancy and Standby Systems]] และ Wait for Shutdown ที่ผูกกับ [[Turnaround Management]]
- รายงาน top-10 cost/problem (ขั้นที่ 6 ข้อ 5-6) จัดอันดับระดับ [[Maintainable Item]] ได้ถ้า WO บันทึก Object Part

## ดูเพิ่ม

- [[CMMS]]
- [[Maintenance Planning and Scheduling]]
- [[Maintenance Backlog and Schedule Compliance]]
- [[Failure Data Recording]]
- [[Maintenance Profit Maker Book]]

## Triplets

- [[Work Order Lifecycle]] [defined_in:: [[Maintenance Profit Maker Book]]] MMS chapter 4 (MPM p.59-81)
- [[Work Order Lifecycle]] [part_of:: [[CMMS]]] MMS works with or without computer (MPM p.60)
- Work Requests [step_of:: [[Work Order Lifecycle]]] stage 1 (MPM p.61, p.63-67)
- Work Order Initiation and Planning [step_of:: [[Work Order Lifecycle]]] stage 2 (MPM p.61, p.67-69)
- Work Order Scheduling [step_of:: [[Work Order Lifecycle]]] stage 3; p.61 list misprints name as Execution and Control (MPM p.61, p.69)
- Work Order Execution and Control [step_of:: [[Work Order Lifecycle]]] stage 4 (MPM p.70-73)
- Work Completion and Close to History [step_of:: [[Work Order Lifecycle]]] stage 5 (MPM p.73-74)
- Maintenance Work Analysis [step_of:: [[Work Order Lifecycle]]] stage 6, 9 analysis areas (MPM p.74-77)
- MPM Work Flow [has_value:: at least 3 approval points] plus 2-level WR approval Owner and Maintenance (Fig 4.2, Fig 4.4, MPM p.62-64)
- MPM Work Flow [differs_from:: CMMS Work Flow] RBMM has 2 approval points (RBMM p.104); design difference, not contested
- Work Request Screening [applies_to:: Work Requests] urgency check or cancel before system (MPM p.63)
- Work Order Status [has_value:: 7] Initiated, Planned, Scheduled, Wait, Issued, Finished, Complete (MPM p.67-68)
- Work Order Status [differs_from:: Work Backlog Basket] MPM splits Finished and Complete; RBMM New to History plus Wait (RBMM p.106)
- Planning Questions [has_value:: 7] resources, method, safety and isolation, hours, tools and parts, total cost, budget and approver (MPM p.68-69)
- Work Order Scheduling [depends_on:: Spare Part Availability] biggest obstacle; parts can be reserved (MPM p.69)
- Wait Status [has_category:: Wait for Parts] also manpower, tools, machine shutdown, others (MPM p.70)
- Daily Scheduling Meeting [applies_to:: Work Order Scheduling] check readiness for tomorrow and next week (MPM p.69)
- Resource Leveling Function [part_of:: [[CMMS]]] adjusts schedule to resource limits; hard to automate (MPM p.69-70)
- Released for Maintenance [step_of:: Work Order Execution and Control] with Safety Tags and isolation (MPM p.70-71)
- Accepted for Production [step_of:: Work Order Execution and Control] production accepts returned machine (MPM p.71-72)
- Work Completion and Close to History [depends_on:: Single Entry] data born in one system only; WO not closed until history complete (MPM p.73-74)
- Closed Work Order Correction [depends_on:: Authorized Procedure] only authorized persons may change closed records (MPM p.74)
- Work Completion and Close to History [uses:: [[Failure Data Recording]]] failure cause, time data, resource usage (MPM p.74)
- Maintenance Work Analysis [uses:: [[Root Cause Analysis]]] failure tree (MPM p.74)
- Maintenance Work Analysis [uses:: [[Reliability Metrics]]] MTBF, MTTR, MWT (MPM p.75)
- Maintenance Work Analysis [uses:: [[Availability and OEE]]] plant and equipment OEE (MPM p.75)
- Fig 4.16 Grand Total [has_value:: 44,473.80] derived; printed 46,273.80 (MPM p.75)
- Fig 4.18 MTBF [has_formula:: (total hours - repair hours) / failures] derived from figures (MPM p.76)
- Fig 4.18 PS03 MTBF [has_value:: 5,225.00] derived; printed 5,255.00 (MPM p.76)
- [[Work Order Lifecycle]] [related_to:: [[Maintenance Planning and Scheduling]]]
- [[Work Order Lifecycle]] [related_to:: [[Maintenance Backlog and Schedule Compliance]]]
- [[Work Order Lifecycle]] [related_to:: [[Failure Hierarchy]]] failure codes enforced before Complete, interpretation [confidence:: low]

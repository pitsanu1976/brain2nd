---
title: CMMS
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [cmms, maintenance-management, reliability, book, iso-14224, data-quality, work-management, cmrp]
sources: [reliability-based-maintenance-management.md, iso-14224.md, cmrp.md]
confidence: high
contested: false
---

# CMMS (Computerized Maintenance Management System)

**CMMS** คือ software สำเร็จรูปสนับสนุนกิจกรรมบำรุงรักษา (housekeeping คล้ายระบบบัญชี) หนังสือ RBMM บทที่ 4 ย้ำว่า CMMS ไม่ใช่ "ยาวิเศษ" ความสำเร็จขึ้นกับ **Process** (ขั้นตอนเก็บข้อมูล) และ **Content** (คุณภาพ/ความหมายของข้อมูล) พร้อมกัน ถ้ามีแต่ระบบแต่ไม่วิเคราะห์งาน จะเก็บข้อมูลผิดตัวและได้ข้อมูลขยะ (RBMM p.90, 108, 112) ประเด็นที่เกี่ยวกับ wiki นี้โดยตรงคือ **asset hierarchy หยุดที่ระดับ Equipment** แล้วบันทึกชิ้นส่วนเป็น Object Part ในประวัติซ่อม และ **ห้ามปิด CM-Unplanned WO ถ้ายังไม่ระบุ Failure Mode** (RBMM p.98, 110-111) ดู [[Failure Data Recording]]

## สิ่งที่ CMMS ทำได้และทำไม่ได้ (RBMM p.91-92)

| ทำไม่ได้ | ทำได้ |
|---|---|
| ไม่บอกว่าควรเลือกงานแบบไหน เมื่อไหร่ กับเครื่องไหน | เก็บข้อมูลใน Register รวมประวัติซ่อม ขยายได้ |
| ไม่แยกแยะความถูกต้องของข้อมูล (เก็บขยะด้วย) | ค้นหา/ดูข้อมูลหลายรูปแบบได้เร็ว |
| ไม่รับประกันว่าบำรุงรักษาได้ดี | ควบคุมกระบวนการและสั่งงานง่ายขึ้น (ระวัง over-maintain) |
| ไม่ติดตามงานเอง ต้องมีคนป้อนข้อมูล | ออกรายงานซ้ำได้เร็ว เก็บประวัติซ่อมตามที่สั่งให้เก็บ |
| รายงานได้เท่าที่ป้อนเข้าไป | |

เหตุผลที่โรงงานนำ CMMS มาใช้: ลด down time, รู้ค่าใช้จ่ายบำรุงรักษา, ลดงานล่วงเวลา, สอดคล้อง ISO 9000, TPM Autonomous ระดับ 4, เก็บความรู้ไว้ในระบบเมื่อช่างลาออก (RBMM p.90) หนังสือประเมินว่า CMMS ส่วนใหญ่ใช้ไม่คุ้มค่า (ราวไม่ถึงครึ่ง) เพราะไม่ครบวงจร (RBMM p.90)

## 10 โมดูลทั่วไป (RBMM p.92-94)

| # | Module | ประเด็นสำคัญ |
|---|---|---|
| 1 | Master Data | ข้อมูลเริ่มต้น เช่น Cost Center |
| 2 | Access Control | กำหนดผู้ใช้/สิทธิ์ฟังก์ชัน |
| 3 | Asset Registration | ต้องทำก่อน มักใช้เวลานานที่สุด ละเอียดเกินไปงานเพิ่ม |
| 4 | Work Control System | สำคัญมาก ถ้าใช้ไม่ได้ถือว่า implement ล้มเหลว แหล่งข้อมูลวิเคราะห์ส่วนใหญ่ |
| 5 | Planned Maintenance | เตรียมงานตามแผน + เงื่อนไขออกงานส่งเข้า Work Control |
| 6 | Spare Part Management | ดู [[Spare Parts Management]] |
| 7 | Purchasing System | งานบำรุงรักษาต้องการ Purchase Requisition มากกว่า Purchasing |
| 8 | Report and KPI Analysis | ผลลัพธ์ที่จับต้องได้ ดู [[Maintenance KPIs]] |
| 9 | Maintenance Performance Budgeting | แนะนำ Activity Based Budgeting ดู [[Maintenance Budget]] |
| 10 | Turnaround Management | เฉพาะโรงงานใหญ่ ดู [[Turnaround Management]] |

Core modules ตาม Fig 4.1 (RBMM p.94): Asset Register, Work Order Backlog, Work Order History, Planned Maintenance, Spare Part Management, Report and Analysis โดย Backlog + History สำคัญสุด เพราะเป็นข้อมูลระดับ shop floor สำหรับวิเคราะห์ระยะยาว หนังสือเห็นว่า Work Control สำคัญกว่า Planned Maintenance ที่ผู้ใช้มักคิดว่าสำคัญสุด (RBMM p.93)

## โครงสร้างระบบ 3 ส่วน (Fig 4.2, RBMM p.95)

1. ฐานข้อมูล: Asset Database -> Planned Maintenance Database -> Spare Part Database
2. ระบบงานและข้อมูลประจำวัน: Work Control -> Spare Parts Control
3. ผลลัพธ์และการวิเคราะห์: Report and Analysis -> Budget และ Optimization (ผลย้อนกลับไปปรับคุณภาพส่วน 1-2)

## Asset Register และ Hierarchy (RBMM p.96-99)

- Equipment Database (สร้างครั้งแรก): Criticality -> Maintenance Strategy; Structure & Coding; Accounting Info; BOM; Technical Data (Fig 4.3, p.96) ดู [[Criticality Assessment]]
- Equipment Maintenance History (จาก transaction): Work Type; Failure Data (Failure Mode, Object Part, Cause, Effect, Consequence, Effect Cost); Resources Cost; Time (Down/Work/Wait); Work Description
- เริ่มระบบได้เมื่อมีรายการเครื่องและรหัสครบ ข้อมูล static อื่นเพิ่มทีหลังได้ (กลยุทธ์ขึ้นระบบเร็ว) (p.96)
- Hierarchy: Area -> Process -> Equipment -> Component -> Part (Fig 4.4) แบ่งเป็น Productive Unit/Location (Logical Asset จัดกลุ่มเพื่อรายงาน) กับ Equipment/Maintainable Item (Physical Asset ซ่อมได้) (p.97)
- **Hierarchy หยุดที่ระดับ Equipment** ระดับต่ำกว่าใช้ Object Part (ตำแหน่งปัญหา) ระบุในประวัติซ่อม (Fig 4.5, p.98) อะไหล่อยู่ใน BOM ไม่ใช่ใน Hierarchy

กฎการให้รหัส (RBMM p.98-99):
- Location/Productive Unit ใช้ Smart Number (ทุก digit มีความหมาย เช่น รูปแบบ XX-999-AA)
- Equipment/Maintainable ใช้ Running Number เป็นอิสระจาก Location (เช่น MOT2499) เพราะย้ายตำแหน่งบ่อย
- ไม่ฝังรหัสบัญชี/แผนก/อะไหล่ในรหัสอุปกรณ์

## Planned Maintenance และ Spare Part Database

- หลักสำคัญ: งานที่ทำแล้วบอกไม่ได้ว่าสู้กับ Failure Mode ไหน ไม่จำเป็นต้องทำ (RBMM p.99) PM database มี 3 กลุ่ม: PM Activity, ระยะเวลา PM, ทรัพยากร ดู [[PM Task Selection]]
- Spare Part Database 3 ส่วน: ข้อมูลรายการ, ข้อมูลที่เปลี่ยนจาก transaction (แก้ตรงไม่ได้), ข้อมูลระดับสต๊อก Min/Max/ROP/EOQ (RBMM p.100-102, Fig 4.8) ดู [[EOQ and Reorder Point]]
- Inventory Transaction: กระทบคงเหลือ (รับ จ่าย ปรับปรุง) และกระทบ Available (ยืม จอง PR Dock Receive) (Fig 4.9, p.103)

## Work Flow และ Backlog (RBMM p.103-106)

- Workflow Fig 4.10: Work Request -> (Breakdown ออก WO ตรง) -> Initiate WO -> Plan Resource -> Assign and Schedule -> Print WO -> Permit to Work ถ้าเป็นงานเสี่ยง -> Execute -> Finish -> Failure Information -> Approve -> Close to History มี **จุดอนุมัติเพียง 2 จุด** คืออนุมัติแจ้งซ่อมและอนุมัติปิดงาน (p.104)
- Work Backlog Basket (Fig 4.12, p.106): New -> Planning -> Scheduling -> In Progress -> In Approval -> History และสถานะรอ Wait for Material / Shutdown / Others

## CMMS ใน RAM และ Process vs Content (RBMM p.106-108)

RAM (Reliability Based Asset Management) มี 7 กระบวนการ CMMS ครอบคลุมเพียงบางส่วน: ลงทะเบียน (1), Work Packaging/Executing/Control (5), Performance Analysis (6) ส่วน Criticality Assessment, Failure Consequences, Task Selection (2-4) และ FMECA (7) มักอยู่นอก CMMS เพราะต้องใช้ความรู้เครื่อง/กระบวนการ ดู [[RCM Reliability Centered Maintenance]] และ [[FMECA]] ถ้าขาดส่วนนี้ PM จะมาจาก "น่าจะทำ" หรือคำแนะนำผู้ผลิต สร้าง Process ง่ายและลงทุนไม่มาก แต่ Content ต้องสร้างคน ใช้เวลาเป็นปี (p.108)

## ผลลัพธ์ที่ควรได้จากการวิเคราะห์ (RBMM p.112)

- จำนวนครั้งที่คาดจะทำ Scheduled PM + ค่าใช้จ่าย
- จำนวนครั้งที่คาดว่าจะเสีย (CM-Unplanned) + ค่าใช้จ่าย
- ค่าใช้จ่ายรวม Scheduled PM + CM-Unplanned
- Average Availability (%) ดู [[Availability and OEE]]
- ค่าใช้จ่ายบำรุงรักษาต่อชั่วโมงใช้งานได้

## เชื่อมโยงกับ compressor failure hierarchy

- Hierarchy ของ CMMS (Location -> Equipment -> Object Part) เทียบได้กับ taxonomy ใน [[Failure Hierarchy]] (equipment -> sub unit -> [[Maintainable Item]]) หนังสือไม่อ้าง [[ISO 14224]] หรือ [[OREDA]] ตรง ๆ ในบทนี้ และไม่ให้ตารางรหัส Failure Mode ในช่วง p.89-112 (บท 5 อ้างภายหลัง ดู [[Failure Data Recording]])
- Compressor ([[Compressor]]) ควรเป็น Equipment ที่มี Running Number ส่วน sub unit/maintainable item ที่ซ่อมได้เก็บเป็น Object Part ในประวัติ หรือเป็น Equipment ถ้าซ่อมแยกเป็นหน่วย (การตีความ ไม่ใช่ข้อความในหนังสือ)
- ฟิลด์ Failure Mode ใน WO ควรใช้รหัส 3 ตัวอักษรแบบเดียวกับ [[Failure Mode]] ใน wiki

## CMMS ในมุมของ ISO 14224 (เพิ่ม 2026-10-21)

ISO 14224 เรียกระบบนี้ว่า **CMMIS** (computerised maintenance management information system) (cl. 4 abbreviations, p.18-20)

- CMMIS ของ facility เป็นแหล่งข้อมูลหลักสำหรับเก็บ RM data และต้องรองรับการรายงานตามมาตรฐาน; แหล่งอื่นตาม Table D.5 เช่น generic data, operator-specific, manufacturer, expert judgement (ISO 14224 cl. 7.2.1, p.27)
- ใช้ **coded field เป็นหลักและมี free text เสริม**; การโอนข้อมูลกึ่งอัตโนมัติจาก CMMIS ช่วยลดปัญหาแหล่งกระจัดกระจายและการตีความต่างกัน (Table 1, cl. 7.1.4, p.27; cl. 9.2, p.35-36) ขั้นตอนทั่วไป: ดึงข้อมูลดิบลง intermediate storage -> ตีความ/แปลงเข้ารูปแบบเป้าหมาย (ส่วนใหญ่ทำมือ) -> โอนเข้า reliability data bank (cl. 7.2.2, p.27-28)
- **event ใน CMMS ไม่ใช่ reliability data ในตัวเอง** ต้องมี taxonomy/boundary ชัด, failure กับ maintenance record ที่ผูกกัน, นิยาม failure และ surveillance period/operating time ที่เป็นมาตรฐาน และ validation โดยคนที่ไม่ใช่ผู้เก็บ (cl. 7.1.2-7.1.3, p.25-27) ดู [[RM Data Quality]]
- ISO ระบุว่า active maintenance time และ downtime สำคัญต่อ RAM/RCM แต่ CMMS ยังบันทึกน้อย ต้องปรับปรุง (Table 8 note d, p.45) และ cost data อยู่นอก scope ของมาตรฐาน ให้ดึงจาก CMMIS (cl. 5.4, p.21-22)
- สอดคล้องกับ RBMM เรื่อง Process และ Content ของ CMMS: ระบบอย่างเดียวไม่พอ ต้องออกแบบฟิลด์และวินัยการป้อนข้อมูล ฟิลด์ที่ ISO แนะนำเทียบกับ Work Order ของ RBMM ที่ [[Failure Data Recording]]

## CMMS ในมุมของ CMRP: planning และ backlog (เพิ่ม 2026-10-25)

หลักสูตร [[CMRP Course]] มอง CMMS จากฝั่งผู้ใช้งาน work management รายละเอียดอยู่ที่ [[Maintenance Planning and Scheduling]] และ [[Maintenance Backlog and Schedule Compliance]]

- CMMS คือเครื่องมือสำคัญที่สุดของ planner; planner ควรเป็น **super-user** ดูแล configuration และคุณภาพข้อมูล (CMRP CMPR-09 p.10-11) สอดคล้องกับเรื่อง Content ของ RBMM ข้างบน
- WO จาก CMMS (PM, PdM, inspection ตามกฎหมาย) เป็นขั้น 2 ของ work order flow 7 ขั้น; job plan ใน CMMS มี work plan, labor, materials, tools, safety plan (CMRP CMPR-09 p.6-7, p.21) PM master เป็น template สร้าง PM รอบต่อ ๆ ไป (p.23)
- Backlog ใน CMMS ต้องแม่น: backlog ที่ไม่แม่นแทบไร้ค่า ให้ purge (WO เก่า ซ้ำ ทำเสร็จแต่ยังไม่ปิด) ทบทวน formal ทุก 3 เดือน และ informal รายเดือน (CMRP CMPR-10 p.2-3) สถานะ "Wait for Shutdown" ใน Work Backlog Basket เชื่อมกับ golden rule ของ [[Turnaround Management]] (การเชื่อมของ wiki)
- Material take-off ใช้ฟังก์ชันจอง (reserve) ของคลังใน CMMS สำหรับงานตามแผน (CMRP CMPR-09 p.30) ซึ่งตรงกับ transaction "จอง" ที่กระทบ Available ใน RBMM (Fig 4.9, p.103) แต่ต่างจากหลักการใช้ของคลังของ RBMM ดู [[Spare Parts Management]]

### จุดอนุมัติ: CMRP ต่างจาก RBMM

| แหล่ง | จุดอนุมัติ |
|---|---|
| RBMM | **2 จุด** คืออนุมัติแจ้งซ่อม และอนุมัติปิดงาน (Fig 4.10, RBMM p.104) |
| CMRP | ตรวจการอนุมัติตั้งแต่ work screening (p.15), เร่งอนุมัติตามวงเงินประมาณการหลังแตกงาน ทั้งด้าน operational, financial, engineering (p.21) และ loop ให้ผู้แจ้งยอมรับงานก่อนปิด (p.5) แปลว่าอาจมีหลายจุดตามวงเงิน |

(CMRP CMPR-09 p.5, p.15, p.21) เป็นความต่างของแนวปฏิบัติ ไม่ใช่ข้อขัดแย้งเชิงข้อเท็จจริง: RBMM เน้นลดขั้นตอนให้น้อยที่สุด ส่วน CMRP ผูกการอนุมัติกับวงเงินงาน องค์กรต้องเลือกเองว่าจะใช้ approval matrix ตามวงเงินหรือไม่ (ไม่ตั้ง contested)

## ดูเพิ่ม

- [[Failure Data Recording]]
- [[ISO 14224]]
- [[RCM Reliability Centered Maintenance]]
- [[Criticality Assessment]]
- [[Maintenance Strategic Report]]
- [[Spare Parts Management]]
- [[Maintenance Planning and Scheduling]]
- [[Maintenance Backlog and Schedule Compliance]]

## Triplets

- [[CMMS]] [has_label:: Computerized Maintenance Management System]
- [[CMMS]] [alias_of:: CMMIS] ISO 14224 term, computerised maintenance management information system (ISO 14224 cl. 4, p.18-20)
- [[CMMS]] [depends_on:: CMMS Process] data collection steps; success needs Process and Content together (RBMM p.90, 108, 112)
- [[CMMS]] [depends_on:: CMMS Content] quality/meaning of data; building content takes people and years (RBMM p.108)
- [[CMMS]] [has_value:: less than half] share of CMMS judged worth the investment, not full cycle (RBMM p.90)
- Master Data [part_of:: [[CMMS]]] module 1, e.g. Cost Center (RBMM p.92-94)
- Access Control [part_of:: [[CMMS]]] module 2 (RBMM p.92-94)
- Asset Registration [part_of:: [[CMMS]]] module 3, done first, usually longest (RBMM p.92-94)
- Work Control System [part_of:: [[CMMS]]] module 4, very important; failure here = failed implementation (RBMM p.92-94)
- Planned Maintenance [part_of:: [[CMMS]]] module 5 (RBMM p.92-94)
- Spare Part Management Module [part_of:: [[CMMS]]] module 6 (RBMM p.92-94)
- Purchasing System [part_of:: [[CMMS]]] module 7, maintenance needs Purchase Requisition more than Purchasing (RBMM p.92-94)
- Report and KPI Analysis [part_of:: [[CMMS]]] module 8 (RBMM p.92-94)
- Maintenance Performance Budgeting Module [part_of:: [[CMMS]]] module 9, Activity Based Budgeting recommended (RBMM p.92-94)
- [[Turnaround Management]] [part_of:: [[CMMS]]] module 10, large plants only (RBMM p.92-94)
- Work Order Backlog [part_of:: [[CMMS]]] core module, most important with History (Fig 4.1, RBMM p.94)
- Work Order History [part_of:: [[CMMS]]] core module, shop-floor data for long-term analysis (Fig 4.1, RBMM p.94)
- Work Control System [differs_from:: Planned Maintenance] book: Work Control more important than Planned Maintenance (RBMM p.93)
- Equipment Database [part_of:: [[CMMS]]] asset database (Fig 4.3, RBMM p.96)
- Equipment Database [has_parameter:: Criticality] linked to Maintenance Strategy; also Structure and Coding, Accounting Info, BOM, Technical Data (Fig 4.3, RBMM p.96)
- Equipment Maintenance History [has_parameter:: Failure Data] Failure Mode, Object Part, Cause, Effect, Consequence, Effect Cost (RBMM p.96-99)
- Process [part_of:: Area] CMMS hierarchy (Fig 4.4, RBMM p.97)
- Equipment [part_of:: Process] CMMS hierarchy (Fig 4.4)
- Component [part_of:: Equipment] CMMS hierarchy (Fig 4.4)
- Part [part_of:: Component] CMMS hierarchy (Fig 4.4)
- [[CMMS]] [at_level:: Equipment] hierarchy stops at Equipment; lower levels recorded as Object Part (Fig 4.5, RBMM p.98)
- Object Part [part_of:: Equipment Maintenance History] location of problem in repair history (RBMM p.98)
- Spare Part [part_of:: BOM] not in hierarchy (RBMM p.98)
- Productive Unit [has_code:: Smart Number] every digit meaningful, e.g. XX-999-AA (RBMM p.98-99)
- Equipment [has_code:: Running Number] independent of location, e.g. MOT2499 (RBMM p.98-99)
- CM-Unplanned Work Order [depends_on:: [[Failure Mode]]] must not close without failure mode (RBMM p.98, 110-111)
- Planned Maintenance Database [depends_on:: [[Failure Mode]]] task that cannot name its failure mode is not needed (RBMM p.99)
- Spare Part Database [uses:: [[EOQ and Reorder Point]]] stock level data Min/Max/ROP/EOQ (Fig 4.8, RBMM p.100-102)
- CMMS Work Flow [has_value:: 2 approval points] approve work request and approve close (Fig 4.10, RBMM p.104)
- [[CMMS]] [related_to:: [[RCM Reliability Centered Maintenance]]] covers RAM processes 1, 5, 6 only; 2-4 and FMECA (7) usually outside CMMS (RBMM p.106-108)
- [[CMMS]] [produces:: Average Availability] analysis output, also expected PM and CM-Unplanned counts and costs, cost per operating hour (RBMM p.112)
- [[CMMS]] [source_of:: RM Data] facility CMMIS is main source (ISO 14224 cl. 7.2.1, p.27)
- [[CMMS]] [uses:: Coded Field] coded fields first with free text supplement (ISO 14224 Table 1, cl. 7.1.4, p.27; cl. 9.2, p.35-36)
- CMMS Event [differs_from:: Reliability Data] needs taxonomy, boundary, linked records, standard failure definition and independent validation (ISO 14224 cl. 7.1.2-7.1.3, p.25-27)
- [[RM Data Quality]] [applies_to:: [[CMMS]]]
- [[CMMS]] [source_of:: Cost Data] cost data outside ISO 14224 scope (ISO 14224 cl. 5.4, p.21-22)
- [[CMMS]] [source_of:: Active Maintenance Time] important for RAM/RCM but poorly recorded (ISO 14224 Table 8 note d, p.45)
- [[Compressor]] [at_level:: Equipment] Running Number; sub unit/maintainable item as Object Part, interpretation [confidence:: low]
- Work Order Failure Mode Field [uses:: [[Failure Mode]]] 3-letter codes as in wiki
- Planner [uses:: [[CMMS]]] most important planner tool; planner is CMMS super-user (CMRP CMPR-09 p.10-11)
- [[CMMS]] [input_to:: [[Maintenance Planning and Scheduling]]] WOs from PM, PdM, statutory inspection; job plan fields (CMRP CMPR-09 p.6-7, p.21)
- Work Order Backlog [depends_on:: Backlog Purging] inaccurate backlog nearly useless; formal review every 3 months, informal monthly (CMRP CMPR-10 p.2-3)
- Stock Reservation [part_of:: [[CMMS]]] planner reserves stock for planned jobs (CMRP CMPR-09 p.30); RBMM reservation transaction affects Available (Fig 4.9, RBMM p.103)
- CMRP Approval Points [differs_from:: CMMS Work Flow] authorization at screening, by estimate value, requester acceptance vs RBMM 2 approval points (CMRP CMPR-09 p.5, p.15, p.21; RBMM p.104)

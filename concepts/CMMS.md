---
title: CMMS
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [cmms, maintenance-management, reliability, book]
sources: [reliability-based-maintenance-management.md]
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
| 10 | Turnaround Management | เฉพาะโรงงานใหญ่ |

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

## ดูเพิ่ม

- [[Failure Data Recording]]
- [[RCM Reliability Centered Maintenance]]
- [[Criticality Assessment]]
- [[Maintenance Strategic Report]]
- [[Spare Parts Management]]

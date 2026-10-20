---
title: Asset Life Cycle
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [maintenance-management, criticality, spare-parts, cost, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Asset Life Cycle (วงจรชีวิตทรัพย์สินและกลุ่มงานบำรุงรักษา)

หน้านี้สรุปบทที่ 1 ของ RBMM (book p.13-30): วงจรชีวิตเครื่องจักรตั้งแต่ Feasibility ถึงปลดระวาง ความเชื่อมโยงระหว่างงานเทคนิค (MTTF, MDT, Availability, OEE) กับงบการเงิน การจำแนกงานบำรุงรักษาเป็น 4 กลุ่ม พลวัตของ criticality (A/B/C) เป้าหมาย "Zero Plant Breakdown @ Minimum Cost" และผลของ redundancy ต่อ criticality ข้อความและตัวเลขมาจากบันทึกอ่านหนังสือ (paraphrase) ส่วนที่ระบุว่า "อ่านจากรูป" อาจคลาดเคลื่อน

## 1. ขั้นตอนวงจรชีวิต (Fig 1.1, RBMM p.14)

| ช่วง | กิจกรรม | ประเด็นสำคัญ |
|---|---|---|
| 1 | Feasibility Study | ราคาถูก "ล็อก" ประมาณ 70% ในช่วงต้น |
| 2 | Project Stage | |
| 3 | Engineering Design | ล็อก 85% ถึง 95% ตามลำดับขั้น |
| 4 | EPC (Engineering, Procurement, Construction) | 100% เมื่อสิ้นสุดออกแบบ/จัดซื้อ |
| 5 | Commissioning / Trial Run | เปลี่ยนชิ้นส่วนเสียมากผิดปกติ ใช้ Commissioning Spare Part |
| 6-8 | Commercial Run: เสีย/ชำรุด, ปรับปรุง/ขยาย, ซ่อมใหญ่ | จบด้วยราคาซาก |

- ตัวเลข 70/85/95/100% อ่านจาก Fig 1.1 ตัวรูป (ตามบันทึก) ยืนยันกับหนังสือต้นฉบับก่อนใช้เชิงตัวเลข
- เปลี่ยน spec ช่วง 1-3 กระทบราคาน้อย แต่ change-order หลังสั่งซื้อกระทบมาก (RBMM p.14)
- หลัง Commissioning ต้นทุนทั้งหมดโอนเข้าบัญชีสินทรัพย์และเริ่มคิด Depreciation (RBMM p.15)
- ผู้ซื้อควรถามตั้งแต่ต้นว่า โรงงานมีโอกาสเดินต่อเนื่องไม่มี breakdown จนถึง Major Overhaul/Turnaround ครั้งถัดไปกี่ % (RBMM p.16) นำไปสู่ Zero Plant Breakdown

## 2. อะไหล่ 2 ประเภทหลัง Commissioning (RBMM p.15-16)

| ประเภท | วัตถุประสงค์ | บัญชี | หมายเหตุ |
|---|---|---|---|
| Commissioning Spare Part | แก้ปัญหาจากก่อสร้าง/ติดตั้ง/ตรวจรับ (Forced Deterioration = เสียเพราะคน ไม่ใช่ตามอายุ) | ไม่ควรปนกับ stock ปกติ | อาจไม่ถูกใช้เลยในช่วงปกติ ผู้รับเหมามักโอนเป็นอะไหล่สำรองคลังอย่างไม่ถูกต้อง |
| Maintenance Spare Part | สำรองคลังไว้ใช้ตลอดอายุปกติ | Current Asset ไม่คิดค่าเสื่อม | holding cost รวมราว 15-20% ของราคาอะไหล่ (RBMM p.16) |

Long Term Asset (ตัวโรงงาน) ตัดค่าเสื่อมรายปีอัตราคงที่ เช่น 15-20-25 ปี (RBMM p.15) เครื่องจักรต้องมีอายุใช้งานตลอดช่วงตัดค่าเสื่อม ซึ่งหนังสือระบุว่าเป็นหน้าที่ของบำรุงรักษา (RBMM p.18)

## 3. เส้นแดง: งานเทคนิคเชื่อมงบการเงิน (Fig 1.2, RBMM p.16-20)

```
MTTR + MWT          -> MDT
MTTF (Reliability)  + MDT -> Availability
Availability x Speed x Quality -> OEE
OEE + Planning Factor + Plant Capacity -> Production -> Goods (งบ)
Goods -> GOGS -> Contribution Margin -> Profit
```

- ใต้ MTTR: Tools, Methods, Maintenance Proficiency, Planning/Scheduling/Control; ใต้ MWT: Logistics/Support, Spare Part Stock Performance
- ฝั่งธุรกิจ: ค่าครอบครองเครื่อง = WACC + Depreciation; ปริมาณผลิตขึ้นกับ Capacity, Production Plan, OEE (RBMM p.19)
- ตัวเลขตัวอย่าง: สินค้าคงคลังอยู่ในคลังเฉลี่ย 20 วัน หมุนเวียน 365/20 ประมาณ 18 รอบ/ปี (derived จากตัวเลขหนังสือ RBMM p.20) ใช้สื่อว่าเครื่องหยุดได้ไม่เกินระยะนี้
- รายละเอียด Availability และ OEE ดู [[Availability and OEE]]

## 4. 4 กลุ่มงานบำรุงรักษา (Fig 1.3, RBMM p.21-23)

แกนตั้ง = ความวิกฤติ (L ไป H) แกนนอน = วงจรชีวิตของงาน ฐาน = Maintenance Management System (ช่องในรูปบางช่องเบลอ [อ่านไม่ออกบางส่วน])

| กลุ่ม | ชื่อ | ตัวอย่างงาน |
|---|---|---|
| 1 | Fault Recovery (เครื่องเรียกหาเรา) | Trouble Shooting, Component Change, Component Rebuild, Spare Parts |
| 2 | Proactive (เราเข้าหาเครื่อง) | Predictive, Condition Monitoring, Preventive Maintenance, Turnaround |
| 3 | Improvement / Project | Project Management, Commissioning, Installation, Engineering, Modification |
| 4 | Maintenance Engineering | Audits, Reliability Improvement, Performance Improvement, Management Improvement |

ประเภทงานตามการวางแผน (RBMM p.22): Corrective Unplanned, Planned Part Replacement/Overhaul, Planned Condition Monitoring (อาการเปิดเผย), Planned Failure Finding Inspection (อาการซ่อนเร้น), Corrective Planned (CM-Planned) เป้าหมายรวม คือลดงานกลุ่ม 1 (unplanned) ไปเป็น planned โดยมี CMMS เป็น "แม่บ้าน" วางแผน จัดตาราง เก็บประวัติ และออกรายงาน (RBMM p.23)

## 5. พลวัตของ Criticality (Fig 1.4, RBMM p.23-25)

Criticality เปลี่ยนตาม Stress, Resistance และแผนบำรุงรักษา Fig 1.4 แบ่งเครื่องเป็น A/B/C ที่ 30% / 50% / 20% ของจำนวนเครื่อง และแสดง 3 สถานะ

| สถานะ | ลักษณะการเสีย |
|---|---|
| 1 Beginning | เสียกระจายทุกระดับ รวมกลุ่ม A โอกาสรอดถึง Turnaround ถัดไปน้อย |
| 2 Intermediate improving | เสียส่วนใหญ่ลงมาที่ B/C ไม่มี A เสีย |
| 3 Target | เสียเฉพาะ C/B ที่ไม่กระทบหยุดโรงงาน = Zero Plant Down Time |

ค่าใช้จ่ายต่ำสุดขึ้นกับยุทธศาสตร์เชิงรุก เช่น RCM, RBI (Risk Based Inspection), Condition Monitoring PM และการตั้งงบ ดู [[Criticality Assessment]] และ [[RCM Reliability Centered Maintenance]]

## 6. Zero (Plant) Breakdown @ Minimum Cost (Fig 1.5, RBMM p.25-27)

ต้องตั้งคำถามแบบมีกรอบเวลา เช่น เครื่องมีโอกาสรอดถึง Major Overhaul ถัดไปกี่ % และผูกกับต้นทุนเสมอ

| ระดับ | แนวทาง | Scheduled PM | Spare Parts |
|---|---|---|---|
| High | 100% RCM Tasks | RCM 100% ตัด unreliable incidence, failure-finding เข้ม | service level 100% stock out 0% |
| Medium | Pro-active | ตัด PM ที่ไม่ได้ผลด้วย RCM, optimal PM, RTF | ลด stock, ระบุ % service level |
| Low | Re-active | ตัด PM ที่ไม่จำเป็น, optimal PM, RTF | ลด stock, ระบุ % service level |

- ตัวเลข 50% (Medium) และ 20% (Low) เป็นสมมติฐานของหนังสือ (RBMM p.27)
- Zero Breakdown ต้องครอบคลุมตั้งแต่ Design ถึง Operator และ Maintenance = TPM (RBMM p.27)
- Medium: หาจุดต้นทุนรวม (planned + unplanned) ต่ำสุดโดยเลือก PM ให้ตรง failure mode และปรับความถี่ (ดู [[PM Interval Optimization]])

## 7. Redundancy ลด criticality ได้แค่ไหน (Fig 1.6-1.8, RBMM p.28-30)

- Fig 1.6 ไม่มี redundancy: เครื่องอนุกรมทุกตัวเป็น criticality A
- Fig 1.7 redundancy ระดับ equipment: กลุ่มขนานอาจเป็น A/B/C
- ตัวอย่างสมมติแต่ละเครื่องรับ 50% ของภาระ มี 3 เครื่อง: Standby (ใช้ 2 สำรอง 1) หรือ Load Sharing (แต่ละเครื่อง 1/3 รับเพิ่มได้ถึง 50%)
- Standby อาจมี Hidden Failure จึงเกิด Multiple Failure ได้ ความวิกฤติไม่ต่ำลงอัตโนมัติ ส่วน Load Sharing ลดลงได้ตามความสามารถรับภาระ (RBMM p.29)
- Fig 1.8 ถังเก็บคั่นระหว่าง process ลด criticality ภาพรวม ขึ้นกับปริมาณและเวลาที่ป้อนต่อได้ (RBMM p.30)
- แนวปฏิบัติ: Condition Monitoring ทั้งเครื่องใช้งานและ standby, ทดสอบ hidden failure เป็นระยะ ดู [[Failure Finding Interval]] และ [[Redundancy and Standby Systems]]

## 8. วงจรบริหารทรัพย์สิน (RBMM p.30)

Think (เป้าหมาย/ยุทธศาสตร์) แล้ว Plan & Act (บริหารงาน) แล้ว Reporting & Control (วัดผลและรายงานรวมเงิน) ฝั่งเทคนิคใช้สถิติเลือกงาน คำนวณคาบ PM และระดับสต็อก ฝั่งบริหารตั้งงบตามเป้าบริษัท

## เชื่อมโยงกับ compressor failure hierarchy

- บทนี้ไม่ได้อ้าง [[OREDA]] หรือ [[ISO 14224]] และไม่มีเนื้อหา compressor โดยตรง
- หนังสือใช้ "Failure Mode (Cause)" คู่กัน (RBMM p.23, 27) ไม่ได้แยก [[Failure Mechanism]] แบบ ISO 14224 เมื่อเลือก PM ต่อ [[Failure Mode]] ของ [[Compressor]] ควรแมป mode ไปยัง mechanism และ cause ก่อน (ดู [[Failure Cause Codes]])
- Hidden Failure/Multiple Failure ของเครื่อง standby (เช่น compressor สำรองใน train) เทียบได้กับ failure mode ประเภท fail to start (FTS) ที่ตรวจพบเมื่อสั่งใช้งาน
- ระดับ criticality A/B/C ช่วยจัดลำดับว่า [[Maintainable Item]] ใดควรทำ RCM 100% (ตัวเลข % failure rate ของ OREDA ไม่ใช่ criticality ในตัวเอง ต้องคูณ consequence)

## ดูเพิ่ม

- [[Maintenance Efficacy Pyramid]]
- [[Maintenance KPIs]]
- [[Availability and OEE]]
- [[Maintenance Strategic Report]]
- [[Failure Hierarchy]]

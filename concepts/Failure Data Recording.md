---
title: Failure Data Recording
created: 2026-10-20
updated: 2026-10-21
type: concept
tags: [cmms, failure-mode, iso-14224, taxonomy, coding, data-quality, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Failure Data Recording

หน้านี้สรุปวิธีบันทึกข้อมูลการเสียใน CMMS ตาม RBMM บท 4-5 ได้แก่ ฟิลด์ใน Work Order, record ขั้นต่ำ 5 รายการ (Equipment, Damage Code, Object Part, Cause, Action) และรหัส Failure Mode ตาม ISO 14224 ของ pump/motor (Fig 5.15, 5.17) พร้อมเทียบกับรหัส 19 โหมดใน [[Failure Mode]] ของ wiki ผลเทียบ: 18 จาก 19 รหัสตรงกันทั้งรหัสและชื่อ ส่วนต่างอยู่ที่ **SPS (หนังสือ) vs UST (wiki)** ซึ่ง resolve แล้ว 2026-10-21: ใช้ UST เป็นรหัสหลัก SPS เป็น alias (ดูหัวข้อเทียบรหัส) ส่วน [[ISO 14224]] ยังเป็น `confidence: low` เพราะหนังสือเป็น secondary source ที่ยกตัวอย่าง ไม่ใช่ตัวมาตรฐาน

## หลักการ: Failure Mode เป็นศูนย์กลางข้อมูล

- งานบำรุงรักษาทั้งหมดต่อสู้กับ Failure Mode จึงต้องวิเคราะห์และเก็บใน CMMS อย่างเป็นระบบ (RBMM p.110, 128)
- แต่ละ Failure Mode มีพฤติกรรมการเสีย (Weibull beta, eta) ของตัวเอง ถ้าไม่แยก FM จะได้ค่ารวมเฉลี่ยที่ใช้ไม่ได้ (Fig 5.12, RBMM p.130) ดู [[Weibull Analysis]]
- ไล่สาเหตุลึกเท่าที่กำหนด PM ได้คุ้มและทำได้ทางเทคนิค แล้วหยุด (RCFA, SAE JA1011/1012, RBMM p.129)
- Failure Mode ตาม SAE คือ "ระดับ causation ที่เป็น single event ที่ก่อ functional failure" (Fig 5.13, p.131) ซึ่งต่างจาก [[Failure Mechanism]] / [[Failure Cause Codes]] ใน wiki ที่แยกเป็นชั้นของตัวเอง

## ฟิลด์ข้อมูลใน Work Order (Fig 4.15, RBMM p.109)

| กลุ่ม | ฟิลด์ |
|---|---|
| แจ้งซ่อม | Work Request Number, วันที่/เวลา, Requester Dept, ผู้แจ้ง, Cost Center, Problem Description |
| สั่งงานซ่อม | Work Order Number, วันที่/เวลา, Work Priority, Productive Unit/Machine, Equipment, ประเภทงาน, Work Action, ผู้รับผิดชอบ |
| Down Time | PU Down Date/Time, PU Start Date/Time, รวม |
| Work Time | เริ่ม, เสร็จ, รวม |
| Wait Time | ประเภทการรอ, เริ่ม, สิ้นสุด, รวม |
| ความเสียหายและสาเหตุ | Failure Mode, Cause/Root Cause, Effect, Effect Cost |
| ทรัพยากร | Man Hours รายคน, Man Hours Cost, อะไหล่ Stock, อะไหล่ Non-Stock, Outsource |

ข้อมูลอื่นที่ต้องใช้วิเคราะห์: ประเภทงาน (ตามแผน/นอกแผน), ค่าเสียหายต่อครั้ง, ประวัติเสียย้อนหลังสำหรับสถิติ และจากหน่วยงานอื่น เช่น กำหนดการใช้เครื่อง อัตราค่าแรงมาตรฐาน อัตราค่าบริหารคลัง ค่าใช้จ่ายต่อการสั่งซื้อ (RBMM p.109-110)

## Record ขั้นต่ำ 5 รายการ (RBMM p.151-152)

| ฟิลด์ | ความหมายตามหนังสือ |
|---|---|
| Equipment | ขอบเขตใดก็ได้ที่ Function Failure เกิดจากการเสียของมัน ต้องระบุรูปธรรมเพื่อเชื่อมกับ spare parts |
| Damage Code | Equipment เสียหายอย่างไร/ทำอะไรไม่ได้ = Failure Mode ระดับ equipment |
| Object Part | ชิ้นส่วนต้นตอของปัญหา |
| Cause (Failure Mode) | ติดกับ Object Part คือ Failure Mode ของ Object นั้น |
| Action | จัดการอย่างไร ดีที่สุดบอกว่าทำ PM อะไร |

ลำดับชั้นใน Fig 5.12 (p.130): Plant > Process > System > Subsystem > Equipment [Damage Code] > Parts [Object Part] > Cause [Failure Mode] รหัสใน CMMS ใช้รูป Equipment_Failure Mode และ Object Part_Failure Mode

## กฎคุณภาพข้อมูล

- ห้ามปิด CM-Unplanned WO ถ้ายังไม่ระบุ Failure Mode ให้ค้างเป็น "Backlog - Failure Mode Undefined" เพราะปิดแล้วเป็นประวัติแก้ไม่ได้และกระทบบัญชี (RBMM p.111, Fig 4.16) ดู [[CMMS]]
- มี gate ตรวจความครบที่จุดอนุมัติปิดงาน (RBMM p.104)
- ข้อมูลขยะ = ไม่มีเจ้าของ ไม่มีใครใช้ ต้องรู้ก่อนว่าจะวิเคราะห์ค่าอะไร (p.109)
- Failure Mode ระดับ Component ให้ทำ Library คำสั้น ๆ ของหน่วยงานเอง เช่น แตก หลุด หลวม สึกหรอ หัก ลัดวงจร วงจรขาด ติด และเพิ่มเมื่อมีรายการใหม่จาก WO (p.134)

## ขอบเขตและรหัส ISO 14224 ในหนังสือ (RBMM p.132-134)

หนังสือระบุว่า ISO 14224 ใช้กำหนด FM ระดับ Equipment ในอุตสาหกรรม gas production plant ไม่เกี่ยวกับ RCM โดยตรง FM ค่อนไปทาง functional failure ข้อดีคือคำจำกัดความสั้นชัด (p.132)

Boundary ปั๊ม (Fig 5.14): Starting System, Driver, Power Transmission, Pump Unit, Control and Monitoring, Lubrication System (Coolant), Miscellaneous Boundary มอเตอร์ (Fig 5.16): motor + Cooling system, Lubrication system, Control and Monitoring, Miscellaneous

### เทียบรหัสกับ [[Failure Mode]] ของ wiki

| Code | Pump (Fig 5.15) | Motor (Fig 5.17) | wiki Failure Mode | ผลเทียบ |
|---|---|---|---|---|
| FTS | Fail to start on demand | มี | FTS Fail to start on demand | ตรงกัน |
| STP | Fail to stop on demand | มี | STP Fail to stop on demand | ตรงกัน |
| SPS | Spurious stop | มี | UST Spurious stop | ชื่อเดียวกัน รหัสต่าง: **ใช้ UST หลัก, SPS = alias** (resolved 2026-10-21) |
| BRD | Breakdown (serious damage: seizure, breakage, explosion) | มี | BRD Breakdown | ตรงกัน |
| HIO | High output | มี | HIO High output | ตรงกัน |
| LOO | Low output | มี | LOO Low output | ตรงกัน |
| ERO | Erratic output | มี | ERO Erratic output | ตรงกัน |
| ELP | External leakage process medium | ไม่มี | ELP External leakage - Process medium | ตรงกัน (pump เท่านั้น) |
| ELU | External leakage utility medium | มี | ELU External leakage - Utility medium | ตรงกัน |
| INL | Internal leakage | ไม่มี | INL Internal leakage | ตรงกัน (pump เท่านั้น) |
| VIB | Vibration | มี | VIB Vibration | ตรงกัน |
| NOI | Noise | มี | NOI Noise | ตรงกัน |
| OHE | Overheating | มี | OHE Overheating | ตรงกัน |
| PDE | Parameter deviation | มี | PDE Parameter deviation | ตรงกัน |
| AIR | Abnormal instrument reading | มี | AIR Abnormal instrument reading | ตรงกัน |
| STD | Structural deficiency | มี (cracks, wear, fracture) | STD Structural deficiency | ตรงกัน |
| SER | Minor in-service problems | มี | SER Minor in-service problems | ตรงกัน |
| OTH | Other | มี | OTH Other | ตรงกัน |
| UNK | Unknown | มี | UNK Unknown | ตรงกัน |
| OWD | ไม่มี | Operation without demand (undesired start) | ไม่มีใน wiki (19 โหมด compressor) | มีเฉพาะ motor |

ข้อสังเกต:
- Pump มี 19 รหัส (นับจาก Fig 5.15 ตามบันทึก) เท่ากับจำนวนโหมดใน wiki แต่ชุดต่างกัน 1 รหัส คือ SPS (pump) แทน UST (wiki) ส่วนรหัสที่เหลือ 18 ตัวเหมือนกัน
- Motor ไม่มี ELP และ INL แต่มี OWD (นับจากรายการใน Fig 5.17 ที่บันทึกไว้ มี 18 รหัส)
- **Resolved 2026-10-21 (ตัดสินโดยผู้ใช้):** ใช้ **UST** เป็นรหัสหลัก และถือ **SPS** เป็น alias (ข้อความด้านล่างเก็บไว้เป็นประวัติ)
- (ประวัติ) ความต่าง SPS/UST: wiki ใช้ UST ตาม dataset OREDA ที่ transcribe ไว้ ส่วนหนังสือใช้ SPS ตามตัวอย่าง ISO 14224 ยังไม่มีตัวมาตรฐานเทียบ จึงยัง **ไม่ตัดสิน** ว่ารหัสใดถูกต้องและไม่แก้ [[Failure Mode]] ให้ใช้ UST ต่อสำหรับข้อมูล compressor และตั้ง alias SPS = UST ไว้ในเอกสารนี้ (ข้อสันนิษฐาน จากชื่อโหมดเหมือนกัน ยังไม่ verify)
- wiki ของ compressor ไม่มีโหมดที่ pump ไม่มี และไม่มี OWD ดังนั้นใช้รายการ pump (แทน SPS ด้วย UST) เป็นแม่แบบ library ของ compressor ได้โดยตรงตามที่หนังสือแนะนำ (หนังสืออ้างว่าใช้เป็นแม่แบบ ไม่ได้พูดถึง compressor)
- หนังสือไม่มี failure descriptor, failure mechanism, resolution code รายละเอียด จึงไม่ครอบคลุมเทียบกับ [[Failure Mechanism]] หรือ [[Resolution Codes]]

## เชื่อมโยงกับ compressor failure hierarchy

- Damage Code (FM ระดับ equipment) = [[Failure Mode]] ของ compressor เช่น ELP, ELU, VIB, UST; Object Part = [[Maintainable Item]]; Cause = [[Failure Cause Codes]] / [[Failure Mechanism]] (การจับคู่เป็นการตีความ หนังสือไม่ได้เทียบตรง)
- Action = [[Resolution Codes]] ในแง่ข้อมูลที่ต้องเก็บ
- ตัวอย่าง: leak ที่ seal ของ compressor ลง Damage Code = [[ELP External Leakage Process Medium]] (หรือ [[ELU External Leakage Utility Medium]] ถ้าเป็น utility) Object Part = seal Action = เปลี่ยน/ซ่อม
- Fig 5.13 (7 ระดับ causation จนถึง design/assembly/procurement/storekeeping error) ใช้เป็นแนวแยก mechanism กับ latent cause

## ดูเพิ่ม

- [[Failure Mode]]
- [[ISO 14224]]
- [[CMMS]]
- [[RCM Reliability Centered Maintenance]]
- [[Failure Hierarchy]]

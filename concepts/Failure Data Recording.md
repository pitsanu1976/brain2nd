---
title: Failure Data Recording
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [cmms, failure-mode, iso-14224, taxonomy, coding, data-quality, book]
sources: [reliability-based-maintenance-management.md, iso-14224.md]
confidence: medium
contested: false
---

# Failure Data Recording

หน้านี้สรุปวิธีบันทึกข้อมูลการเสียใน CMMS ตาม RBMM บท 4-5 ได้แก่ ฟิลด์ใน Work Order, record ขั้นต่ำ 5 รายการ (Equipment, Damage Code, Object Part, Cause, Action) และรหัส Failure Mode ตาม ISO 14224 ของ pump/motor (Fig 5.15, 5.17) พร้อมเทียบกับรหัส 19 โหมดใน [[Failure Mode]] ของ wiki ผลเทียบ: 18 จาก 19 รหัสตรงกันทั้งรหัสและชื่อ ส่วนต่างอยู่ที่ **SPS (หนังสือ) vs UST (wiki)** ซึ่ง resolve แล้ว 2026-10-21: ใช้ UST เป็นรหัสหลัก SPS เป็น alias (ดูหัวข้อเทียบรหัส) ส่วน [[ISO 14224]] ตอนเขียนหน้านี้ยังเป็น `confidence: low` เพราะหนังสือเป็น secondary source ที่ยกตัวอย่าง ไม่ใช่ตัวมาตรฐาน (ตั้งแต่ 2026-10-21 มีตัวมาตรฐานเป็น source แล้ว ดูหัวข้อ "ฟิลด์ข้อมูลตามตัวมาตรฐาน ISO 14224")

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

## ฟิลด์ข้อมูลตามตัวมาตรฐาน ISO 14224 (เพิ่ม 2026-10-21)

ISO 14224:2016 เป็นตัวมาตรฐานเอง (primary source) ให้ฟิลด์ขั้นต่ำ 3 กลุ่ม: equipment, failure, maintenance (cl. 9.1, p.35) เครื่องหมาย (*) = minimum data ในมาตรฐาน อ้างหน้าแบบ printed ดูหลักคุณภาพข้อมูลที่ [[RM Data Quality]]

### Equipment data (Table 5, cl. 9.4, p.38-40) ที่เกี่ยวกับการผูก failure กับอุปกรณ์

- Use/location: Industry, Business category (*), Installation category, Plant/Unit category (*), Section/System (*) และ Operation category
- Equipment attributes: Equipment class (*), Equipment type (*), tag (*), serial number, Manufacturer (*), model
- Operation: normal operating state (*), start date of current service (*), surveillance time (*), operational time, จำนวน periodic test demands (*) และ operational demands (*)
- tag = function + ตำแหน่ง คงที่ ส่วน serial เปลี่ยนเมื่อสลับตัวเครื่อง (note b, p.40)

### Failure data (Table 6, cl. 9.5, p.40-41)

| กลุ่ม | ฟิลด์ |
|---|---|
| Identification | Failure record (*), Equipment identification/location (*) |
| Failure | Failure date (*, วันที่ตรวจพบ), Failure mode (*), Failure impact on equipment function (*: critical/degraded/incipient), Failure impact on plant safety และ operations |
| สาเหตุ | Failure mechanism, Failure cause, Subunit failed, Component/MI failed |
| บริบท | Detection method, Operating condition at failure (*: run-down, start-up, running, hot standby, idle, cold standby, testing), SIS failure mode (DU, DD, SU, SD) |

- mechanism/cause มักยังไม่รู้ตอนเก็บข้อมูล ต้องทำ RCA และ **ISO ระบุให้ทำ RCA บังคับ** สำหรับ failure ผลกระทบสูง, cost ซ่อม/downtime สูง หรือเกิดบ่อยผิดปกติ ("worst actors") (Table 6 note d, p.41)
- รายละเอียด detection method, impact และ safety classification ดู [[Failure Detection Method]], [[Failure Impact Classification]], [[Safety Critical Failure Classification]]

### Maintenance data (cl. 9.6, Tables 7-8, p.42-45)

- มี 2 category: **corrective** (หลังเสีย ต้องมี failure report ตาม Table 6) กับ **preventive** (รวม check/inspection/test) และ **modification ไม่ใช่ maintenance category** แม้ทีม maintenance มักเป็นผู้ทำ ต้องแยกออกเมื่อวิเคราะห์ (cl. 9.6.1-9.6.2, p.42)
- Table 7: corrective maintenance record = required; actual PM = optional; planned PM programme = optional (p.43)
- Table 8 ฟิลด์: Maintenance record (*), Equipment identification (*), Failure record (*, ไม่ใช้กับ PM), Date (*), Maintenance category (*), Priority, Interval (เฉพาะ PM), Maintenance activity (Table B.5), Impact on plant operations (zero/partial/total), Subunit maintained, Component/MI maintained, Man-hours ต่อ discipline, Maintenance equipment resources, **Active maintenance time (*)**, **Down time (*)**, Maintenance delays/problems (logistics, weather, scaffolding, ขาดอะไหล่)
- ถ้าพบ failure ระหว่าง PM ให้บันทึกเป็น failure + corrective action โดย detection method = ประเภท PM นั้น (cl. 9.6.3, p.43)
- Active time และ downtime สำคัญต่อ RAM/RCM แต่ CMMS ยังบันทึกน้อย (Table 8 note d, p.45) นิยามเวลาที่ [[Maintenance Time Definitions]]

### เทียบกับ RBMM

| ประเด็น | RBMM | ISO 14224 |
|---|---|---|
| Failure mode ระดับ | Damage Code = FM ระดับ equipment | level 6 equipment unit เป็น default (Table 3, p.32) |
| ชิ้นส่วนต้นตอ | Object Part | Component/MI failed (level 8) และ Subunit failed (level 7) |
| Action | Action | Maintenance activity (Table B.5) ใน maintenance record |
| Down/work/wait time | Down Time, Work Time, Wait Time | Down time กับ Active maintenance time; delay แยกเป็น maintenance delays |
| รหัส | Library ของหน่วยงานเอง | coded field เป็นหลักและมี free text เสริม (cl. 9.2, p.35-36) |

### ขอบเขต boundary: ปั๊มใน RBMM vs กฎ driver ของ ISO

RBMM Fig 5.14 (RBMM p.132-134) แสดง boundary ปั๊มที่มี **Starting System และ Driver เป็นส่วนของ boundary** ขณะที่ ISO 14224 ให้ **driver และ auxiliary ของ driver อยู่นอก boundary** ของปั๊ม/compressor บันทึกเป็น inventory แยกพร้อมเลขอ้างอิง และ failure ของ driver ลงที่ driver (cl. 8.1, p.29; cl. A.2.2.2.1, p.64-65 สำหรับ compressor) (boundary ปั๊มใน Annex A ของ ISO ยังไม่ได้ตรวจใน reading notes ใช้เฉพาะตัวอย่างใน cl. 8.1 และกฎของ compressor) ทั้งสองไม่ได้ขัดกันแบบต้องตัดสิน: RBMM เป็น secondary source ที่ยกตัวอย่างโครงสร้างจาก ISO ส่วนตัวมาตรฐานเป็น source ที่ถือเป็นหลักเมื่อต้องส่งออก/เทียบข้อมูลกับ ISO/OREDA การเก็บ driver เป็น equipment แยกยังเทียบ failure rate ได้ตรงกว่า (การตีความ) ดู [[ISO 14224 Taxonomy]]

### ผลเทียบรหัส Failure Mode กับตัวมาตรฐาน

ตัวมาตรฐาน ISO 14224:2016 (Annex B, Tables B.6, B.8 ฯลฯ) ใช้รหัส **UST** สำหรับ spurious stop ไม่มีรหัส SPS ในฉบับนี้ (reading notes annex-b) จึงสนับสนุนการตัดสิน 2026-10-21 ที่ใช้ UST เป็นรหัสหลัก ผลเทียบ 18 รหัสที่ตรงกันยังเป็นการเทียบกับ RBMM เท่านั้น ดู [[Failure Mode]]

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

## Triplets

- [[Failure Data Recording]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapters 4-5
- [[Failure Data Recording]] [defined_in:: [[ISO 14224]]] cl. 9, primary source since 2026-10-21
- [[Failure Data Recording]] [uses:: [[CMMS]]]
- [[Failure Mode]] [related_to:: [[Weibull Analysis]]] each FM has its own beta, eta; mixing FMs gives unusable average (Fig 5.12, RBMM p.130)
- [[Failure Mode]] [defined_in:: SAE JA1011] level of causation that is a single event causing functional failure (Fig 5.13, RBMM p.131)
- [[Failure Mode]] [differs_from:: [[Failure Mechanism]]] SAE FM vs wiki separate mechanism/cause levels
- Work Order [has_part:: Work Request Number] request group (Fig 4.15, RBMM p.109)
- Work Order [has_part:: Down Time] PU down/start date-time, total
- Work Order [has_part:: Work Time]
- Work Order [has_part:: Wait Time] wait type, start, end, total
- Work Order [has_part:: [[Failure Mode]]] damage and cause group, with Cause/Root Cause, Effect, Effect Cost
- Work Order [has_part:: Man Hours] resources group, with stock/non-stock spares, outsource
- Minimum CMMS Record [has_value:: 5] fields (RBMM p.151-152)
- Minimum CMMS Record [has_part:: Equipment]
- Minimum CMMS Record [has_part:: Damage Code] = Failure Mode at equipment level
- Minimum CMMS Record [has_part:: Object Part] originating part
- Minimum CMMS Record [has_part:: Cause] Failure Mode of the Object Part
- Minimum CMMS Record [has_part:: Action] best states which PM to do
- Damage Code [alias_of:: [[Failure Mode]]] equipment level (RBMM p.151-152)
- Damage Code [has_code:: Equipment_Failure Mode] CMMS code pattern (Fig 5.12)
- Object Part [has_code:: Object Part_Failure Mode] CMMS code pattern (Fig 5.12)
- RBMM Fig 5.12 Hierarchy [has_part:: Plant] Plant > Process > System > Subsystem > Equipment > Parts > Cause (p.130)
- CM-Unplanned WO [depends_on:: [[Failure Mode]]] cannot close without FM; held as Backlog - Failure Mode Undefined (RBMM p.111, Fig 4.16)
- Component Failure Mode Library [applies_to:: Component] organisation's own short-term library (RBMM p.134)
- [[ISO 14224]] [applies_to:: Equipment Level Failure Mode] gas production plant, not directly RCM (RBMM p.132)
- RBMM Pump Boundary [has_part:: Driver] also Starting System, Power Transmission, Pump Unit, Control and Monitoring, Lubrication System, Miscellaneous (Fig 5.14)
- RBMM Pump Boundary [differs_from:: [[ISO 14224]]] ISO puts driver and its auxiliaries outside pump/compressor boundary (cl. 8.1, p.29; cl. A.2.2.2.1, p.64-65)
- RBMM Fig 5.15 [has_value:: 19] pump failure mode codes
- RBMM Fig 5.15 [has_value:: 18] codes matching wiki [[Failure Mode]] in code and name
- RBMM Fig 5.17 [has_value:: 18] motor failure mode codes
- SPS [alias_of:: [[UST Spurious Stop]]] resolved 2026-10-21 by user; UST primary
- SPS [differs_from:: [[ISO 14224]]] not in ISO 14224:2016, which uses UST (Annex B, Tables B.6, B.8)
- Pump [has_failure_mode:: [[ELP External Leakage Process Medium]]] pump only, not motor (Fig 5.15)
- Pump [has_failure_mode:: INL] pump only, not motor (Fig 5.15)
- Motor [has_failure_mode:: OWD] Operation without demand, motor only (Fig 5.17)
- OWD [has_label:: Operation without demand]
- OWD [differs_from:: [[Failure Mode]]] not in wiki 19 compressor modes
- RBMM Fig 5.15 [input_to:: [[Failure Mode]]] pump list (SPS replaced by UST) usable as compressor library template (interpretation)
- [[Failure Data Recording]] [has_part:: Equipment Data] minimum group (cl. 9.1, p.35)
- [[Failure Data Recording]] [has_part:: Failure Data] minimum group (cl. 9.1, p.35)
- [[Failure Data Recording]] [has_part:: Maintenance Data] minimum group (cl. 9.1, p.35)
- Equipment Data [defined_in:: [[ISO 14224]]] Table 5, cl. 9.4, p.38-40
- Equipment Data [has_part:: Equipment Class] minimum data (*)
- Equipment Data [has_part:: Tag] minimum data (*); tag = function + location, serial changes on swap (note b, p.40)
- Failure Data [defined_in:: [[ISO 14224]]] Table 6, cl. 9.5, p.40-41
- Failure Data [has_part:: Failure Date] minimum data (*), date detected
- Failure Data [has_part:: [[Failure Mode]]] minimum data (*)
- Failure Data [has_part:: [[Failure Impact Classification]]] impact on equipment function (*): critical/degraded/incipient
- Failure Data [has_part:: [[Failure Mechanism]]]
- Failure Data [has_part:: [[Failure Cause Codes]]] failure cause
- Failure Data [has_part:: [[Failure Detection Method]]]
- Failure Data [has_part:: Operating Condition At Failure] minimum data (*)
- Failure Data [has_part:: [[Safety Critical Failure Classification]]] SIS failure mode DU, DD, SU, SD
- Root Cause Analysis [applies_to:: Worst Actors] required for high impact, high repair cost/downtime or unusually frequent failures (Table 6 note d, p.41)
- Maintenance Data [defined_in:: [[ISO 14224]]] cl. 9.6, Tables 7-8, p.42-45
- Maintenance Data [has_category:: corrective, preventive] (cl. 9.6.1-9.6.2, p.42)
- Modification [differs_from:: Maintenance Data] not a maintenance category (cl. 9.6.1-9.6.2, p.42)
- Corrective Maintenance Record [has_category:: required] actual PM and planned PM programme optional (Table 7, p.43)
- Maintenance Data [has_part:: [[Resolution Codes]]] maintenance activity (Table B.5)
- Maintenance Data [has_part:: Active Maintenance Time] minimum data (*)
- Maintenance Data [has_part:: Down Time] minimum data (*)
- Maintenance Data [has_part:: Maintenance Impact On Plant Operations] zero/partial/total (Table 8)
- Failure Found During PM [detected_by:: PM Type] record as failure + corrective action (cl. 9.6.3, p.43)
- Active Maintenance Time [related_to:: [[Maintenance Time Definitions]]] important for RAM/RCM but rarely recorded in CMMS (Table 8 note d, p.45)
- Damage Code [maps_to:: [[Failure Mode]]] ISO level 6 default (Table 3, p.32)
- Object Part [maps_to:: [[Maintainable Item]]] ISO Component/MI failed level 8, Subunit failed level 7; wiki interpretation
- Action [maps_to:: [[Resolution Codes]]] ISO maintenance activity Table B.5; wiki interpretation
- Cause [maps_to:: [[Failure Mechanism]]] also [[Failure Cause Codes]]; wiki interpretation
- [[Failure Data Recording]] [uses:: Coded Field] coded fields primary with free text (cl. 9.2, p.35-36)

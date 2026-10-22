---
title: Failure Impact Classification
created: 2026-10-21
updated: 2026-10-22
type: concept
tags: [iso-14224, failure-mode, criticality, taxonomy, coding]
sources: [iso-14224.md]
confidence: medium
contested: false
---

# Failure Impact Classification (การจัดระดับผลของ failure ตาม ISO 14224)

หน้านี้สรุปวิธีที่ [[ISO 14224]] จัดระดับ "ผลของ failure" ต่อ function ของ equipment ต่อการบำรุงรักษา และต่อ plant พร้อมอธิบายว่าต่างจากคำว่า "critical" ในความหมายอื่นอย่างไร สรุปด้วยถ้อยคำของผู้เขียน wiki (ไม่ใช่ข้อความต้นฉบับ)

## 1. Failure impact ต่อ function ของ equipment (ISO 14224 cl. 3.28, p.6; Table 3, p.32)

failure impact คือผลของ failure ต่อ function ของ equipment หรือต่อ plant ระดับ equipment แบ่ง 3 ชั้น

| ชั้น | ความหมาย (สรุป) | อ้างอิง |
|---|---|---|
| critical | ทำให้ equipment unit หยุดทำ required function ทันที (รวมกรณีต้องสั่งหยุดทันทีแม้ยังเดินได้ชั่วครู่) และนำไปสู่ unscheduled repair | cl. 3.9, p.3 |
| degraded | function หลักยังไม่หยุด แต่ลดทอนบางส่วน เช่น output ต่ำ/สูงผิดปกติ/ไม่นิ่ง เลื่อนซ่อมได้ แต่ถ้าปล่อยอาจกลายเป็น critical | cl. 3.11, p.4 |
| incipient | ความไม่สมบูรณ์ของสภาพที่อาจ (หรือไม่) พัฒนาเป็น degraded/critical ถ้าไม่แก้ ต้องมีเกณฑ์ชัดว่าเมื่อไรต้องบันทึก | cl. 3.40, p.9 |

- non-critical failure = degraded + incipient (cl. 3.68, p.13-14)
- Table 6 ระบุว่าบางกรณีบันทึกแค่ critical กับ non-critical ก็พอ (ISO 14224 Table 6, p.40-41)
- ข้อสังเกตภายในมาตรฐาน: note 1 ของ 3.28 บอกว่า Table 3 ครอบคลุม taxonomy level 3-5 แต่ note 2 บอก level 4-5 (p.6) ตัวหน้านี้ไม่ใช้ระดับดังกล่าวตัดสินใจอะไร

## 2. Maintenance impact (ISO 14224 cl. 3.52, p.11)

| ระดับ | ค่าที่ใช้ |
|---|---|
| Equipment | critical / non-critical |
| Plant (operations) | total / partial / zero |

ฟิลด์ "Maintenance impact on plant operations" (zero/partial/total) อยู่ใน maintenance data (ISO 14224 Table 8, p.44-45) ไม่ได้อยู่ใน failure record

## 3. ฟิลด์ที่เกี่ยวข้องใน failure record (ISO 14224 Table 6, p.40-41)

| ฟิลด์ | ค่า/หมายเหตุ |
|---|---|
| Failure impact on equipment function | critical / degraded / incipient (ฟิลด์บังคับ) |
| Failure impact on plant safety | บันทึกตามผลต่อความปลอดภัย |
| Failure impact on plant operations | ใช้ consequence class จาก Table C.2 (ISO 14224 cl. C.1.10, p.208-209) |
| Failure mode | ปกติระดับ equipment unit (taxonomy level 6) |
| Operating condition at failure | run-down, start-up, running, hot standby, idle, cold standby, testing |

Table C.2 มี 16 class: 4 แถว (Safety, Environmental, Production, Operational cost) x 4 คอลัมน์ (Catastrophic, Severe, Moderate, Minor) เลข I-XVI ไล่ตามคอลัมน์ ผู้ใช้ต้องตั้ง "acceptable limit" เองตาม application (ISO 14224 cl. C.1.10, p.208-209) Table 6 note d: ต้องทำ RCA เมื่อผลกระทบสูง ค่าซ่อม/downtime สูง หรือเสียบ่อยผิดปกติ (p.41)

## 4. Consistency check (ISO 14224 cl. 7.1.2, p.26)

รายการตรวจคุณภาพข้อมูลของมาตรฐานมีข้อ "ข้อมูลต้องสอดคล้องกัน เช่น failure mode กับ failure impact" ตัวอย่างการตรวจที่ผู้เขียน wiki ตีความเอง (ไม่ใช่ตัวอย่างในมาตรฐาน):

- failure mode ที่ทำให้เครื่องหยุด เช่น [[UST Spurious Stop]] หรือ FTS (fail to start, ดู [[Failure Mode]]) ควรได้ impact = critical เพราะ function หยุดทันที ถ้าบันทึกเป็น incipient ถือว่าไม่สอดคล้อง
- mode ที่เป็นความเบี่ยงเบนของสภาพ เช่น [[LOO Low Output]], [[PDE Parameter Deviation]], [[AIR Abnormal Instrument Reading]] มักเป็น degraded หรือ incipient แต่ถ้าถึงระดับต้องหยุดทันทีให้ถือเป็น critical
- impact ขึ้นกับสถานการณ์ ไม่ได้ผูกตายตัวกับรหัส mode ใน wiki ไม่มีตารางจับคู่ mode-impact ใน sources จึงเป็นแนวทางตรวจ ไม่ใช่กฎ

ดูกระบวนการเต็มใน [[RM Data Quality]]

## 5. สามความหมายของ "critical"

> [!warning] อย่าสับสน
> คำว่า "critical" ใน wiki นี้มี 3 ความหมายที่ต่างกัน

| ความหมาย | ตัดสินที่ | ค่า | แหล่ง |
|---|---|---|---|
| ISO 14224 failure impact class | ผลของ failure ต่อ function ของ equipment ตัวนั้น ไม่ขึ้นกับอุปกรณ์อื่น | critical / degraded / incipient | ISO 14224 cl. 3.28, 3.9 |
| ISO/TR 12489 safety critical failure | failure แบบ dangerous ที่ทำให้ safety instrumented function (SIF) ใช้ไม่ได้ทั้งหมด ถ้ามี redundancy ต้องเสียครบตามที่ทำให้ function หายไป | ใช่/ไม่ใช่ | ISO 14224 cl. F.4.1, p.253-254 ดู [[Safety Critical Failure Classification]] |
| ระดับ criticality ของเครื่อง A/B/C | ความสำคัญของ equipment จาก Consequence x Likelihood (RBMM) | A / B / C | [[Criticality Assessment]] |

ตัวอย่าง: compressor ที่เป็น criticality A (ตาม RBMM) อาจมี failure ที่เป็นเพียง incipient ในความหมาย ISO ส่วน failure แบบ critical (ISO) ของ compressor ที่มีตัวสำรองและเป็นเครื่อง C ไม่ได้แปลว่าเป็น safety critical failure ตาม TR 12489 ความต่างนี้เป็นเรื่องความหมายของคำเดียวกัน ไม่ใช่ข้อขัดแย้งของข้อมูล (contested: false)

## เชื่อมโยงกับ compressor failure hierarchy

- ISO 14224 บันทึก impact ที่ระดับ failure mode ของ equipment unit ซึ่งตรงกับระดับ [[Compressor]] ที่ OREDA ใช้ ดู [[Failure Hierarchy]]
- การจัด impact ให้ mode ในตาราง OREDA เป็นการตีความของผู้ใช้ ไม่มีข้อมูลนี้ใน dataset ของ wiki
- ดูเพิ่ม [[ISO 14224 Taxonomy]], [[Failure Data Recording]], [[Failure Cause Codes]]

## Triplets

- [[Failure Impact Classification]] [defined_in:: [[ISO 14224]]] cl. 3.28, p.6; Table 3, p.32
- Critical Failure [is_a:: [[Failure Impact Classification]]] equipment function impact class
- Critical Failure [has_label:: critical]
- Critical Failure [defined_in:: [[ISO 14224]]] immediate loss of required function, unscheduled repair (cl. 3.9, p.3)
- Degraded Failure [is_a:: [[Failure Impact Classification]]] equipment function impact class
- Degraded Failure [has_label:: degraded]
- Degraded Failure [defined_in:: [[ISO 14224]]] function partly reduced, repair can be deferred, may become critical (cl. 3.11, p.4)
- Incipient Failure [is_a:: [[Failure Impact Classification]]] equipment function impact class
- Incipient Failure [has_label:: incipient]
- Incipient Failure [defined_in:: [[ISO 14224]]] imperfection that may develop to degraded/critical; needs recording criteria (cl. 3.40, p.9)
- Non-Critical Failure [has_part:: Degraded Failure] (cl. 3.68, p.13-14)
- Non-Critical Failure [has_part:: Incipient Failure] (cl. 3.68, p.13-14)
- Failure Impact On Equipment Function [has_category:: critical / degraded / incipient] mandatory field (Table 6, p.40-41)
- Failure Impact On Equipment Function [part_of:: [[Failure Data Recording]]] failure record field (Table 6)
- Failure Impact On Equipment Function [has_category:: critical / non-critical] sufficient in some cases (Table 6)
- Maintenance Impact On Equipment [has_category:: critical / non-critical] (cl. 3.52, p.11)
- Maintenance Impact On Plant Operations [has_category:: total / partial / zero] (cl. 3.52, p.11)
- Maintenance Impact On Plant Operations [part_of:: Maintenance Data] not failure record (Table 8, p.44-45)
- Failure Impact On Plant Operations [uses:: ISO:C.2] consequence class (cl. C.1.10, p.208-209)
- Operating Condition At Failure [has_category:: run-down, start-up, running, hot standby, idle, cold standby, testing] (Table 6)
- [[Failure Mode]] [at_level:: 6] usually equipment unit level (Table 6)
- ISO:C.2 [has_value:: 16] consequence classes I-XVI, 4 rows x 4 columns (cl. C.1.10, p.208-209)
- ISO:C.2 [has_category:: Safety, Environmental, Production, Operational cost] rows
- ISO:C.2 [has_category:: Catastrophic, Severe, Moderate, Minor] columns
- ISO:C.2 [depends_on:: Acceptable Limit] user sets per application
- Root Cause Analysis [applies_to:: High Impact Failure] also high repair cost/downtime or unusually frequent (Table 6 note d, p.41)
- [[RM Data Quality]] [uses:: [[Failure Impact Classification]]] consistency of failure mode vs impact (cl. 7.1.2, p.26)
- [[UST Spurious Stop]] [related_to:: Critical Failure] wiki interpretation: stop modes should be critical [confidence:: low]
- FTS [related_to:: Critical Failure] wiki interpretation [confidence:: low]
- [[LOO Low Output]] [related_to:: Degraded Failure] wiki interpretation: usually degraded or incipient [confidence:: low]
- [[PDE Parameter Deviation]] [related_to:: Degraded Failure] wiki interpretation: usually degraded or incipient [confidence:: low]
- [[AIR Abnormal Instrument Reading]] [related_to:: Degraded Failure] wiki interpretation: usually degraded or incipient [confidence:: low]
- Critical Failure [differs_from:: [[Safety Critical Failure Classification]]] ISO 14224 impact class vs ISO/TR 12489 safety critical (cl. F.4.1, p.253-254)
- Critical Failure [differs_from:: [[Criticality Assessment]]] impact class vs RBMM equipment criticality A/B/C
- [[Criticality Assessment]] [has_category:: A / B / C] Consequence x Likelihood (RBMM)
- [[Failure Impact Classification]] [related_to:: [[Compressor]]] impact recorded at equipment unit level used by OREDA

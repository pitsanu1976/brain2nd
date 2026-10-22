---
title: Failure Hierarchy
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [taxonomy, oreda, iso-14224, failure-mode, failure-mechanism, resolution]
sources: [compressor-failure-hierarchy.md, failure-structure.md, reliability-based-maintenance-management.md, iso-14224.md]
confidence: medium
contested: true
---

# Failure Hierarchy

โครงสร้างลำดับชั้นที่ใช้จัดแจงความล้มเหลวของ [[Compressor]] ตั้งแต่ equipment ลงไปถึงการแก้ไข

## 7 ระดับ

| ระดับ | ชื่อ | จำนวน/ตัวอย่าง | หน้าที่เกี่ยวข้อง |
|---|---|---|---|
| 1 | Equipment | Compressor (centrifugal, reciprocating, screw) | [[Compressor]] |
| 2 | Sub Unit | 6 (PWTR, CPUN, CTMN, LUBS, SHSS, MISC) | [[PWTR Power Transmission]], [[CPUN Compressor Unit]], [[CTMN Control and Monitoring]], [[LUBS Lubrication System]], [[SHSS Shaft Seal System]], [[MISC Miscellaneous]] |
| 3 | Maintainable Item | 44 รหัส | [[Maintainable Item]] |
| 4 | Failure Mode | 19 โหมด | [[Failure Mode]] |
| 5 | Failure Mechanism | 37 รายการใน OREDA list (35 มีรหัส) | [[Failure Mechanism]] |
| 6 | Failure Cause | รหัส CAUSE_CODE = SubUnit-Item-Mechanism (473 รหัสไม่ซ้ำ) | [[Failure Cause Codes]], [[CAUSE_CODE Convention]] |
| 7 | Resolution | 13 ที่ใช้จริง (14 รหัสใน code sheet) | [[Resolution Codes]] |

## ลำดับการอ่านใน dataset

Dataset หลัก (sheet Failure Hierarchy, 7,882 data rows) จัดเรียง **Failure Mode > Sub Unit > Maintainable Item** แล้วขยายแบบ one-to-many:

1 failure mode/item -> หลาย mechanism -> หลาย resolution; แต่ละคู่ mechanism x resolution เป็น 1 แถว

- % ของ failure rate ผูกกับคู่ failure mode/item (OREDA ให้ค่าเดียวต่อคู่ ไม่แยกตาม sub unit)
- คอลัมน์ `Count in Total` (J) = 1 เฉพาะแถวแรกของคู่ เพื่อไม่ให้นับ % ซ้ำเมื่อรวมยอด
- Item ที่อยู่ใน Sub Unit หลายตัว (Instruments, Valves, Seals, Cooler(s), Filter(s), Piping, Reservoir) ถูกจับคู่กับ **ทุก** sub unit แต่ % นับครั้งเดียวที่ sub unit แรก

## ความขัดแย้งระหว่าง sources (contested)

สอง sources จัด item เข้า Sub Unit ต่างกัน เก็บทั้งสองมุมมอง:

| Item | compressor-failure-hierarchy.md | failure-structure.md (Sheet1) | ISO 14224 Table A.9 (p.65) |
|---|---|---|---|
| Instruments | กระจายทั้ง 5 sub unit (PWTR, CPUN, CTMN, LUBS, SHSS) | แยกเป็น Instrument, flow/general/level/pressure/speed/temperature/vibration อยู่ใน Control and Monitoring เท่านั้น | มีเฉพาะ Sensors ใน Control and monitoring |
| Valves | CPUN, CTMN, LUBS, SHSS, MISC | Miscellaneous เท่านั้น | Compressor, Control and monitoring, Lubrication system, Shaft seal system; Miscellaneous แยกเป็น Control/Isolation/Check valves |
| Internal piping | Compressor unit | Miscellaneous | Compressor subunit |
| Check valves | Compressor unit | Miscellaneous | Lubrication system และ Miscellaneous (ไม่อยู่ใน Compressor subunit) |
| Piping | Compressor unit, Lubrication system, Miscellaneous | Miscellaneous | Control and monitoring, Lubrication system; Miscellaneous ใช้ Piping, pipe support and bellows |

Notes ใน source แรกระบุว่า Table 5 ของ OREDA เป็นฐานของการจัด sub unit และบาง item ถูก "assigned by judgement" ISO 14224 (ข้อมูลเพิ่ม 2026-10-21) สนับสนุน dataset หลักเรื่อง Internal piping ใน Compressor unit และใกล้ Sheet1 เรื่อง Instruments แต่ไม่ตรงทั้งสอง source เรื่อง Valves, Check valves, Piping จึง **ยังไม่ตัดสิน** (ISO เป็น taxonomy กลางคนละ scope กับ % ของ OREDA) ดูรายการเทียบเต็มที่ [[Compressor Subdivision Wiki vs ISO 14224]] และบันทึกใน [[log]]

## เทียบกับระดับของ ISO 14224

เลขระดับ 1-7 ข้างต้นเป็นการนับภายใน dataset ไม่ใช่ taxonomy level ของ ISO 14224 ใน ISO (cl. 8.2, Figure 3, p.30-31) ระดับ 1-5 คือบริบทการใช้งาน (industry ถึง section/system) และ **wiki ระดับ 1-3 (Equipment, Sub Unit, Maintainable Item) = ISO level 6-8** (equipment unit, subunit, component/MI) ส่วน Failure Mode, Mechanism, Cause ใน ISO เป็นข้อมูลของ failure record ผูกที่ระดับ 6, 8, 8 ตาม Table 3 (p.32) และ **Resolution ไม่อยู่ใน ISO taxonomy** (ISO เก็บ maintenance activity ใน maintenance record) รายละเอียดที่ [[ISO 14224 Taxonomy]]

## หมายเหตุคุณภาพข้อมูล

Mechanism, detail และ resolution เป็น engineering judgement ของผู้จัดทำ dataset (Notes ข้อ 8) ต้อง review กับ CMMS history/RCA ก่อนใช้ใน RCM/FMEA

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความ ไม่ใช่ข้อความใน OREDA: ลำดับชั้น asset ใน CMMS ตาม RBMM (Plant > Process > System > Subsystem > Equipment > Object Part > Cause, Fig 5.12 p.130) ครอบคลุมเหนือและใต้ระดับ Equipment ของตารางนี้ ดู [[CMMS]] และ [[Failure Data Recording]] การเทียบ Object Part กับ [[Maintainable Item]] ดู [[RBMM Concepts vs Compressor Failure Hierarchy]]

## Triplets

- [[Compressor]] [at_level:: 1] Equipment; centrifugal, reciprocating, screw
- Sub Unit [at_level:: 2]
- [[Maintainable Item]] [at_level:: 3]
- [[Failure Mode]] [at_level:: 4]
- [[Failure Mechanism]] [at_level:: 5]
- [[Failure Cause Codes]] [at_level:: 6] Failure Cause
- [[Resolution Codes]] [at_level:: 7] Resolution, last level
- Sub Unit [has_value:: 6] PWTR, CPUN, CTMN, LUBS, SHSS, MISC
- [[PWTR Power Transmission]] [part_of:: [[Compressor]]] level 2 sub unit
- [[CPUN Compressor Unit]] [part_of:: [[Compressor]]] level 2 sub unit
- [[CTMN Control and Monitoring]] [part_of:: [[Compressor]]] level 2 sub unit
- [[LUBS Lubrication System]] [part_of:: [[Compressor]]] level 2 sub unit
- [[SHSS Shaft Seal System]] [part_of:: [[Compressor]]] level 2 sub unit
- [[MISC Miscellaneous]] [part_of:: [[Compressor]]] level 2 sub unit
- [[Maintainable Item]] [part_of:: Sub Unit] level 3 under level 2
- [[Maintainable Item]] [has_value:: 44] item codes
- [[Maintainable Item]] [has_failure_mode:: [[Failure Mode]]] level 3 to 4; one failure mode/item pair per % value
- [[Failure Mode]] [has_value:: 19] modes
- [[Failure Mode]] [has_mechanism:: [[Failure Mechanism]]] level 4 to 5; one mode/item to many mechanisms
- [[Failure Mechanism]] [has_value:: 37] mechanisms in OREDA list, 35 with codes
- [[Failure Mechanism]] [resolved_by:: [[Resolution Codes]]] level 5 to 7; one mechanism to many resolutions
- [[Failure Cause Codes]] [has_formula:: SubUnit-Item-Mechanism] CAUSE_CODE, see [[CAUSE_CODE Convention]]
- [[Failure Cause Codes]] [has_value:: 473] unique CAUSE_CODE
- [[Resolution Codes]] [has_value:: 13] resolutions actually used; 14 codes in code sheet
- [[Failure Hierarchy]] [has_value:: 7882] data rows in sheet Failure Hierarchy; one row per mechanism x resolution pair
- [[Failure Hierarchy]] [related_to:: Failure Mode > Sub Unit > Maintainable Item] dataset sort order
- Failure Rate Share [depends_on:: Failure Mode Item Pair] OREDA gives one value per pair, not split by sub unit
- Count in Total [has_value:: 1] column J, first row of each pair only, to avoid double counting %
- Multi Sub Unit Items [applies_to:: Sub Unit] Instruments, Valves, Seals, Cooler(s), Filter(s), Piping, Reservoir matched to every sub unit; % counted once at first sub unit
- Sub Unit Assignment [defined_in:: [[OREDA]]] Table 5 basis; some items assigned by judgement
- INST [part_of:: [[PWTR Power Transmission]]] compressor-failure-hierarchy.md [contested:: true]
- INST [part_of:: [[CPUN Compressor Unit]]] compressor-failure-hierarchy.md [contested:: true]
- INST [part_of:: [[CTMN Control and Monitoring]]] compressor-failure-hierarchy.md [contested:: true]
- INST [part_of:: [[LUBS Lubrication System]]] compressor-failure-hierarchy.md [contested:: true]
- INST [part_of:: [[SHSS Shaft Seal System]]] compressor-failure-hierarchy.md [contested:: true]
- INST [part_of:: [[CTMN Control and Monitoring]]] failure-structure.md Sheet1: only CTMN, split into Instrument flow/general/level/pressure/speed/temperature/vibration [contested:: true]
- VALV [part_of:: [[CPUN Compressor Unit]]] compressor-failure-hierarchy.md [contested:: true]
- VALV [part_of:: [[CTMN Control and Monitoring]]] compressor-failure-hierarchy.md [contested:: true]
- VALV [part_of:: [[LUBS Lubrication System]]] compressor-failure-hierarchy.md [contested:: true]
- VALV [part_of:: [[SHSS Shaft Seal System]]] compressor-failure-hierarchy.md [contested:: true]
- VALV [part_of:: [[MISC Miscellaneous]]] compressor-failure-hierarchy.md [contested:: true]
- VALV [part_of:: [[MISC Miscellaneous]]] failure-structure.md Sheet1: only MISC [contested:: true]
- IPIP [part_of:: [[CPUN Compressor Unit]]] compressor-failure-hierarchy.md [contested:: true]
- IPIP [part_of:: [[MISC Miscellaneous]]] failure-structure.md Sheet1 [contested:: true]
- CHKV [part_of:: [[CPUN Compressor Unit]]] compressor-failure-hierarchy.md [contested:: true]
- CHKV [part_of:: [[MISC Miscellaneous]]] failure-structure.md Sheet1 [contested:: true]
- PIPE [part_of:: [[CPUN Compressor Unit]]] compressor-failure-hierarchy.md [contested:: true]
- PIPE [part_of:: [[LUBS Lubrication System]]] compressor-failure-hierarchy.md [contested:: true]
- PIPE [part_of:: [[MISC Miscellaneous]]] compressor-failure-hierarchy.md [contested:: true]
- PIPE [part_of:: [[MISC Miscellaneous]]] failure-structure.md Sheet1 [contested:: true]
- Sensors [part_of:: [[CTMN Control and Monitoring]]] ISO 14224 Table A.9 p.65; ISO has only Sensors for Instruments [contested:: true]
- VALV [part_of:: [[CPUN Compressor Unit]]] ISO 14224 Table A.9 p.65 [contested:: true]
- VALV [part_of:: [[CTMN Control and Monitoring]]] ISO 14224 Table A.9 p.65 [contested:: true]
- VALV [part_of:: [[LUBS Lubrication System]]] ISO 14224 Table A.9 p.65 [contested:: true]
- VALV [part_of:: [[SHSS Shaft Seal System]]] ISO 14224 Table A.9 p.65 [contested:: true]
- VALV [part_of:: [[MISC Miscellaneous]]] ISO 14224 Table A.9 p.65: split as Control, Isolation and Check valves [contested:: true]
- IPIP [part_of:: [[CPUN Compressor Unit]]] ISO 14224 Table A.9 p.65; ISO supports dataset view [contested:: true]
- CHKV [part_of:: [[LUBS Lubrication System]]] ISO 14224 Table A.9 p.65; not in Compressor subunit [contested:: true]
- CHKV [part_of:: [[MISC Miscellaneous]]] ISO 14224 Table A.9 p.65; not in Compressor subunit [contested:: true]
- PIPE [part_of:: [[CTMN Control and Monitoring]]] ISO 14224 Table A.9 p.65 [contested:: true]
- PIPE [part_of:: [[LUBS Lubrication System]]] ISO 14224 Table A.9 p.65 [contested:: true]
- PSPB [part_of:: [[MISC Miscellaneous]]] ISO 14224 Table A.9 p.65: Piping, pipe support and bellows [contested:: true]
- [[Failure Hierarchy]] [related_to:: [[Compressor Subdivision Wiki vs ISO 14224]]] sub unit assignment not yet decided
- [[Compressor]] [at_level:: ISO 6] equipment unit; wiki level 1 = ISO level 6 (cl. 8.2, Figure 3, p.30-31)
- Sub Unit [at_level:: ISO 7] subunit; wiki level 2
- [[Maintainable Item]] [at_level:: ISO 8] component/MI; wiki level 3
- [[ISO 14224 Taxonomy]] [has_value:: 5] ISO levels 1-5 are use/location context, industry to section/system
- [[Failure Mode]] [at_level:: ISO 6] failure record data tied at ISO level 6 (Table 3, p.32)
- [[Failure Mechanism]] [at_level:: ISO 8] failure record data (Table 3, p.32)
- [[Failure Cause Codes]] [at_level:: ISO 8] failure record data (Table 3, p.32)
- [[Resolution Codes]] [differs_from:: [[ISO 14224 Taxonomy]]] Resolution not in ISO taxonomy; ISO keeps maintenance activity in maintenance record
- [[Failure Hierarchy]] [depends_on:: Engineering Judgement] mechanism, detail and resolution by dataset author (Notes item 8); review with CMMS history/RCA before RCM/FMEA
- [[CMMS]] [related_to:: [[Failure Hierarchy]]] RBMM asset hierarchy Plant > Process > System > Subsystem > Equipment > Object Part > Cause (Fig 5.12 p.130) spans above and below Equipment (interpretation) [confidence:: low]

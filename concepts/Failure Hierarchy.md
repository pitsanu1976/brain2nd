---
title: Failure Hierarchy
created: 2026-10-20
updated: 2026-10-21
type: concept
tags: [taxonomy, oreda, iso-14224, failure-mode, failure-mechanism, resolution]
sources: [compressor-failure-hierarchy.md, failure-structure.md, reliability-based-maintenance-management.md]
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

| Item | compressor-failure-hierarchy.md | failure-structure.md (Sheet1) |
|---|---|---|
| Instruments | กระจายทั้ง 5 sub unit (PWTR, CPUN, CTMN, LUBS, SHSS) | แยกเป็น Instrument, flow/general/level/pressure/speed/temperature/vibration อยู่ใน Control and Monitoring เท่านั้น |
| Valves | CPUN, CTMN, LUBS, SHSS, MISC | Miscellaneous เท่านั้น |
| Internal piping | Compressor unit | Miscellaneous |
| Check valves | Compressor unit | Miscellaneous |
| Piping | Compressor unit, Lubrication system, Miscellaneous | Miscellaneous |

Notes ใน source แรกระบุว่า Table 5 ของ OREDA เป็นฐานของการจัด sub unit และบาง item ถูก "assigned by judgement" ยังไม่มี source ที่ตัดสินว่าอันไหนถูก ดูรายละเอียดที่หน้า sub unit และบันทึกใน [[log]]

## หมายเหตุคุณภาพข้อมูล

Mechanism, detail และ resolution เป็น engineering judgement ของผู้จัดทำ dataset (Notes ข้อ 8) ต้อง review กับ CMMS history/RCA ก่อนใช้ใน RCM/FMEA

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความ ไม่ใช่ข้อความใน OREDA: ลำดับชั้น asset ใน CMMS ตาม RBMM (Plant > Process > System > Subsystem > Equipment > Object Part > Cause, Fig 5.12 p.130) ครอบคลุมเหนือและใต้ระดับ Equipment ของตารางนี้ ดู [[CMMS]] และ [[Failure Data Recording]] การเทียบ Object Part กับ [[Maintainable Item]] ดู [[RBMM Concepts vs Compressor Failure Hierarchy]]

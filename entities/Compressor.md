---
title: Compressor
created: 2026-10-20
updated: 2026-10-21
type: entity
tags: [compressor, taxonomy, oreda, failure-rate]
sources: [compressor-failure-hierarchy.md, failure-structure.md, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-failure-hierarchy__notes.csv, reliability-based-maintenance-management.md]
confidence: high
contested: false
---

# Compressor (generic)

Equipment ระดับ 1 ของ [[Failure Hierarchy]] ใน dataset ใช้ ASSET GROUP = `COCE` (compressor) สำหรับทุกแถว ตัวเลขใน dataset หลักเป็นค่า "ทุกประเภทรวม" ตาม OREDA

## ประเภทที่ sources ครอบคลุม

| ประเภท | หน้า | ลักษณะใน data |
|---|---|---|
| Centrifugal | [[Centrifugal Compressor]] | AIR และ ELU เด่น; มี Antisurge, Rotor, Dry gas seal |
| Reciprocating | [[Reciprocating Compressor]] | LOO, SER เด่น; Cylinder liner และ Filter(s) เด่น |
| Screw | [[Screw Compressor]] | AIR, ELU, PDE, UST เด่น; Valves และ instruments เด่น |

เปรียบเทียบทั้งสามที่ [[Compressor Type Failure Profiles]]

## ขนาดของ dataset หลัก

| รายการ | จำนวน |
|---|---|
| Sub Unit | 6 ([[PWTR Power Transmission]], [[CPUN Compressor Unit]], [[CTMN Control and Monitoring]], [[LUBS Lubrication System]], [[SHSS Shaft Seal System]], [[MISC Miscellaneous]]) |
| Maintainable item (รหัสไม่ซ้ำ) | 44 ([[Maintainable Item]]) |
| คู่ failure mode/item ที่ % ไม่เป็นศูนย์ | 258 |
| Failure mode | 19 ([[Failure Mode]]) |
| CAUSE_CODE ไม่ซ้ำ | 473 ([[Failure Cause Codes]]) |
| แถวข้อมูล Failure Hierarchy | 7,882 |
| Total % ที่ระบุได้ | 85.66 (ไม่รวม Other/Subunit/Unknown 13.96) |

## ภาพรวมโหมดความล้มเหลว (ทุกประเภทรวม)

AIR 17.18, SER 13.05, LOO 10.11, ELU 8.62, PDE 8.13 เป็น 5 โหมดแรก ดู [[Which failure modes dominate compressor failure rate]]

## ข้อควรระวัง

- ไม่มีข้อมูล failure rate สัมบูรณ์, population หรือ operating hours ใน sources ดู [[OREDA]]
- Dataset หลักเป็น engineering judgement สำหรับ mechanism/resolution ต้อง validate กับ CMMS/RCA ของ Valeura

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความ ไม่ใช่ข้อมูล OREDA: การวางกลยุทธ์ PM ของ compressor ตามหนังสือ RBMM เริ่มจาก [[RCM Reliability Centered Maintenance]] และ [[Criticality Assessment]] แล้วเลือกงานด้วย [[PM Task Selection]] (ไม่มีข้อมูล β หรือ P-F เฉพาะ compressor ใน sources) ดูตัวอย่างขั้นตอนที่ [[How to choose PM task for a compressor failure mode]]

---
title: Maintenance Reliability Example
created: 2026-10-20
updated: 2026-10-20
type: guide
tags: [maintenance-reliability, fleet-engineering, llm-wiki]
sources: []
confidence: medium
contested: false
---

# Maintenance Reliability Example

Worked example: wiki ของ compressor failure hierarchy (โฟลเดอร์ `15 failure hierarchy/coce/wiki` บน Desktop) ใช้โครง [[LLM Wiki Pattern]] จริง ข้อมูลด้านล่างสรุปจากการอ่าน SCHEMA/index/log ของ wiki นั้น

## Mapping

| ชั้น wiki | ตัวอย่างในงาน compressor |
|---|---|
| raw | `Compressor Failure Hierarchy.xlsx` -> 10 CSV + manifest, `failure structure.xlsx`, ภาพ OREDA ใน `raw/assets/` |
| entities | Compressor, Centrifugal/Reciprocating/Screw, Sub Unit (PWTR, CPUN, CTMN, LUBS, SHSS, MISC) |
| concepts | Failure Hierarchy, Failure Mode (hub), Failure Mechanism, Resolution Codes, OREDA, ISO 14224 |
| comparisons | เปรียบเทียบโปรไฟล์ failure ระหว่างประเภท compressor |
| queries | คำถามเช่น โหมดไหนครองสัดส่วน failure rate |

## หลักที่ใช้

- หน้ารายโหมดสร้างเฉพาะ 9 โหมด % สูง ตาม [[Page Thresholds]]
- ตัวเลข derived ต้องบอกวิธีคำนวณ
- ความขัดแย้งเรื่อง sub unit ระหว่างสอง source -> เก็บทั้งสองฝั่ง ([[Contradiction Handling]])
- Total 85.66% ไม่ใช่ 100% เพราะตัด placeholder item (อธิบายในหน้า Failure Mode ของ wiki นั้น)

## ใช้ซ้ำกับงานอื่น

เปลี่ยน raw เป็น maintenance record, RCA report, vendor bulletin แล้วใช้ entity = equipment, concept = failure mode/mechanism, query = คำถามจากหน้างาน ขั้นตอนแปลงไฟล์ดู [[Converting Excel and PDF to Raw]]

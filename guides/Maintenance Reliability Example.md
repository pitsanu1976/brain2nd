---
title: Maintenance Reliability Example
created: 2026-10-20
updated: 2026-10-21
type: guide
tags: [maintenance-reliability, fleet-engineering, llm-wiki]
sources: []
confidence: medium
contested: false
---

# Maintenance Reliability Example

Worked example ของ [[LLM Wiki Pattern]] ที่ใช้งานจริง: wiki ด้าน compressor failure hierarchy และ reliability-based maintenance management ซึ่งตอนนี้อยู่ใน vault เดียวกันนี้ (ย้ายมาจากโฟลเดอร์ `coce\wiki` เมื่อ 2026-10-21 ดู [[log]]) ไม่ใช่ตัวอย่างภายนอกอีกต่อไป

เริ่มอ่านที่ [[Compressor]], [[Failure Hierarchy]], [[Failure Mode]] และ [[Reliability Based Maintenance Management Book]]

## Mapping

| ชั้น wiki | ตัวอย่างในงาน compressor / RBMM |
|---|---|
| raw | [[raw/compressor-failure-hierarchy]] (xlsx -> 10 CSV), [[raw/failure-structure]], [[raw/reliability-based-maintenance-management]] (หนังสือ -> reading notes), ภาพ OREDA ใน `raw/assets/` |
| entities | [[Compressor]], [[Centrifugal Compressor]], [[Reciprocating Compressor]], [[Screw Compressor]], Sub Unit เช่น [[PWTR Power Transmission]] และ [[CPUN Compressor Unit]] |
| concepts | [[Failure Hierarchy]], [[Failure Mode]] (hub), [[Failure Mechanism]], [[Resolution Codes]], [[OREDA]], [[ISO 14224]] และแนวคิด RBMM เช่น [[Weibull Analysis]], [[RCM Reliability Centered Maintenance]] |
| comparisons | [[Compressor Type Failure Profiles]], [[RBMM Concepts vs Compressor Failure Hierarchy]] |
| queries | [[Which failure modes dominate compressor failure rate]], [[How to choose PM task for a compressor failure mode]] |

## หลักที่ใช้

- หน้ารายโหมดสร้างเฉพาะ 9 โหมด % สูง ตาม [[Page Thresholds]]
- ตัวเลข derived ต้องบอกวิธีคำนวณ
- ความขัดแย้งเรื่อง sub unit ระหว่างสอง source -> เก็บทั้งสองฝั่ง ([[Contradiction Handling]]) ดู [[Failure Hierarchy]]
- Total 85.66% ไม่ใช่ 100% เพราะตัด placeholder item (อธิบายใน [[Failure Mode]])
- กติกาที่ใช้ร่วมกันอยู่ใน [[SCHEMA]] (area ข)

## ใช้ซ้ำกับงานอื่น

เปลี่ยน raw เป็น maintenance record, RCA report, vendor bulletin แล้วใช้ entity = equipment, concept = failure mode/mechanism, query = คำถามจากหน้างาน ขั้นตอนแปลงไฟล์ดู [[Converting Excel and PDF to Raw]]

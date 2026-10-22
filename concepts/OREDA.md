---
title: OREDA
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [oreda, taxonomy, reliability]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__notes.csv, failure-structure.md, reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# OREDA

**OREDA** (Offshore and Onshore Reliability Data) เป็นฐานข้อมูล/handbook ความเชื่อถือได้ของอุปกรณ์ในอุตสาหกรรม oil and gas ใน wiki นี้ OREDA เป็นแหล่งของตัวเลข failure rate ทั้งหมด

## สิ่งที่ sources ระบุเกี่ยวกับ OREDA

- ข้อมูล failure mode, sub unit, maintainable item และ % ใน dataset ถูก **transcribe จากภาพตาราง OREDA** ของ compressor (Notes ข้อ 1) ภาพอยู่ใน `raw/assets/`
- Sub Unit และ item อ้างอิง **OREDA Table 5** (subdivision in maintainable items) และตาราง "Maintainable item versus failure mode"
- Failure mechanism และ resolution ใช้ **OREDA lists** (ภาพ `coce-failure-mechanism.jpg`, `coce-resolution.jpg`)
- ตารางต่อประเภท: "Failure descriptor versus failure mode" และ "Maintainable item versus failure mode" แยก Centrifugal / Reciprocating / Screw โดยตัวเลขเป็น "percentages of the total failure rate for the actual ... combination" ของประเภทนั้น
- ผลรวมต่างจาก OREDA 'Sum' เล็กน้อยเนื่องจาก rounding (Notes ข้อ 3)

## ข้อจำกัด

- sources ไม่ระบุฉบับ/ปีของ OREDA handbook, จำนวน population, operating hours หรือ failure rate เชิงสัมบูรณ์ (ต่อ 10^6 ชม.) มีแต่ % สัมพัทธ์ ดังนั้นห้ามใช้ตัวเลขเป็น failure rate สัมบูรณ์
- ตัวเลขทุกประเภทรวม (Failure Hierarchy) และต่อประเภท (ภาพ) ใช้ฐานต่างกัน ดู [[Compressor Type Failure Profiles]]

## ความสัมพันธ์

OREDA ใช้ taxonomy สอดคล้องกับมาตรฐาน [[ISO 14224]] ดูการประยุกต์เป็นลำดับชั้นที่ [[Failure Hierarchy]] และกลุ่มรหัสใน [[Failure Mode]]

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความ ไม่ใช่ข้อความใน OREDA: หนังสือ RBMM ไม่ได้กล่าวถึง OREDA โดยตรง แต่แสดงวิธีใช้ข้อมูลอัตราการเสียทั่วไปในการวิเคราะห์ คือ [[Weibull Analysis]] (ต้องมี time-to-failure) และ [[Reliability Metrics]] (MTTF, λ(t)) ซึ่งต้องการข้อมูลเวลาที่ OREDA % ใน wiki นี้ไม่มี ดู [[Failure Data Recording]] สำหรับข้อมูลที่ต้องเก็บใน CMMS เพื่อทำการวิเคราะห์ดังกล่าวกับ asset ของตนเอง

## Triplets

- [[OREDA]] [has_label:: Offshore and Onshore Reliability Data]
- [[OREDA]] [is_a:: Reliability Database] oil and gas equipment reliability handbook
- [[OREDA]] [source_of:: [[Failure Hierarchy]]] failure mode, sub unit, maintainable item and % transcribed from OREDA compressor table images (Notes 1)
- [[OREDA]] [source_of:: [[Failure Mode]]] failure rate % in this wiki
- [[OREDA]] [source_of:: [[Maintainable Item]]] OREDA Table 5 subdivision in maintainable items
- [[OREDA]] [source_of:: [[Failure Mechanism]]] OREDA list (coce-failure-mechanism.jpg)
- [[OREDA]] [source_of:: [[Resolution Codes]]] OREDA list (coce-resolution.jpg)
- [[OREDA]] [source_of:: [[Compressor Type Failure Profiles]]] per-type tables Centrifugal / Reciprocating / Screw
- [[OREDA]] [has_category:: Relative Failure Rate Percentage] % of total failure rate per combination, no absolute rate per 10^6 h
- [[OREDA]] [differs_from:: Absolute Failure Rate] sources give no edition, population, operating hours or per 10^6 h rate; do not use % as absolute rate
- [[Failure Hierarchy]] [differs_from:: [[Compressor Type Failure Profiles]]] all-type and per-type figures use different bases
- [[OREDA]] [uses:: [[ISO 14224]]] taxonomy consistent with the standard
- [[OREDA]] [related_to:: [[Weibull Analysis]]] RBMM interpretation; needs time-to-failure data OREDA % lacks [confidence:: low]
- [[OREDA]] [related_to:: [[Reliability Metrics]]] RBMM interpretation; needs time data OREDA % lacks [confidence:: low]

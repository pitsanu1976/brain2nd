---
title: Failure Detection Method
created: 2026-10-21
updated: 2026-10-22
type: concept
tags: [iso-14224, coding, taxonomy, failure-mode]
sources: [iso-14224.md]
confidence: high
contested: false
---

# Failure Detection Method

**Detection method** คือวิธีที่ทำให้ค้นพบ failure เป็นฟิลด์หนึ่งของ failure record ตาม [[ISO 14224]] (Table B.4) dataset OREDA ใน wiki นี้ **ไม่มีฟิลด์นี้** (ดู [[Failure Hierarchy]]) จึงเป็นข้อมูลที่ได้จากมาตรฐานเท่านั้น

ฟิลด์นี้ช่วยบอกว่า failure ถูกพบด้วยวิธีใด เช่น ต่อเนื่อง ตามรอบ หรือบังเอิญ ซึ่งสัมพันธ์กับการประเมินประสิทธิผลของ PM และการหา hidden failure ดู [[P-F Interval and Condition Monitoring]] และ [[Failure Data Recording]]

## Table B.4 รหัส 11 ตัว

ความหมายเขียนด้วยคำของ wiki ไม่ใช่ข้อความต้นฉบับ (ISO 14224 Table B.4, p.183)

| Code | Detection method | ความหมาย (ย่อ) | กลุ่ม |
|---|---|---|---|
| 1 | Periodic maintenance | พบระหว่างงาน PM ตามรอบ | scheduled |
| 2 | Functional testing | พบจากการทดสอบหน้าที่ เป็นวิธีหลักหา hidden failure | scheduled |
| 3 | Inspection | พบจากการตรวจตามรอบ | scheduled |
| 4 | Periodic condition monitoring | พบจากการวัด/เฝ้าระวังสภาพเป็นช่วง ๆ | scheduled |
| 5 | Pressure testing | พบจากการทดสอบความดัน | scheduled |
| 6 | Continuous condition monitoring | พบจากระบบเฝ้าระวังสภาพแบบต่อเนื่อง | continuous |
| 7 | Production interference | พบเพราะกระทบการผลิต | continuous |
| 8 | Casual observation | พบโดยบังเอิญจากการสังเกตทั่วไป | casual |
| 9 | Corrective maintenance | พบระหว่างงานซ่อมที่เกิดขึ้นอยู่แล้ว | casual |
| 10 | On demand | พบเมื่อถูกเรียกใช้งานจริง | casual |
| 11 | Other | วิธีอื่นที่ไม่เข้าข้างต้น | other |

การจัดกลุ่ม scheduled (1-5), continuous (6-7), casual (8-10), other (11) ตามตาราง (Table B.4, p.183) มี footnote ให้ตีความพิเศษสำหรับ fire/gas detector, sensor และ logic (Table B.4 fn a)

## ความไม่สอดคล้องในมาตรฐาน (B.2.4)

ข้อความ cl. B.2.4 (p.182) กล่าวถึง detection method **9 หมวด** แต่ Table B.4 (p.183) มี **11 รหัส** เป็นความไม่สอดคล้องภายในมาตรฐานเอง เมื่อใช้งานให้ยึดตารางเป็นรายการรหัส และบันทึกว่าข้อความต่างจากตาราง ยังไม่มีแหล่งอื่นมา resolve

## กติกาเมื่อพบ failure ระหว่าง PM

ถ้าพบ failure ระหว่างทำ PM ให้บันทึกเป็น failure พร้อม corrective action และใช้ **ประเภทของ PM นั้นเป็น detection method** (ISO 14224 cl. 9.6.3, p.43) ไม่ใช่รหัส Corrective maintenance ผู้ใช้ควรระบุ practice ขององค์กรว่า failure เล็ก ๆ ที่พบระหว่าง PM จะบันทึกหรือไม่

## ดูเพิ่ม

- ฟิลด์อื่นใน record: [[Failure Mode]], [[Failure Mechanism]], [[Failure Cause Codes]], [[Resolution Codes]]
- ภาพรวมมาตรฐาน: [[ISO 14224]], [[ISO 14224 Taxonomy]]

## Triplets

- [[Failure Detection Method]] [defined_in:: [[ISO 14224]]] Table B.4, p.183
- [[Failure Detection Method]] [part_of:: [[Failure Data Recording]]] field of failure record
- [[Failure Detection Method]] [has_value:: 11] codes in Table B.4 (p.183)
- [[Failure Detection Method]] [differs_from:: [[Failure Hierarchy]]] OREDA dataset has no detection method field
- ISO:B.4-1 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-1 [has_label:: Periodic maintenance]
- ISO:B.4-1 [has_category:: scheduled] (Table B.4)
- ISO:B.4-2 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-2 [has_label:: Functional testing]
- ISO:B.4-2 [has_category:: scheduled] (Table B.4)
- ISO:B.4-3 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-3 [has_label:: Inspection]
- ISO:B.4-3 [has_category:: scheduled] (Table B.4)
- ISO:B.4-4 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-4 [has_label:: Periodic condition monitoring]
- ISO:B.4-4 [has_category:: scheduled] (Table B.4)
- ISO:B.4-5 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-5 [has_label:: Pressure testing]
- ISO:B.4-5 [has_category:: scheduled] (Table B.4)
- ISO:B.4-6 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-6 [has_label:: Continuous condition monitoring]
- ISO:B.4-6 [has_category:: continuous] (Table B.4)
- ISO:B.4-7 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-7 [has_label:: Production interference]
- ISO:B.4-7 [has_category:: continuous] (Table B.4)
- ISO:B.4-8 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-8 [has_label:: Casual observation]
- ISO:B.4-8 [has_category:: casual] (Table B.4)
- ISO:B.4-9 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-9 [has_label:: Corrective maintenance]
- ISO:B.4-9 [has_category:: casual] (Table B.4)
- ISO:B.4-10 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-10 [has_label:: On demand]
- ISO:B.4-10 [has_category:: casual] (Table B.4)
- ISO:B.4-11 [is_a:: [[Failure Detection Method]]]
- ISO:B.4-11 [has_label:: Other]
- ISO:B.4-11 [has_category:: other] (Table B.4)
- ISO:B.4-2 [related_to:: Hidden Failure] main method to find hidden failures
- [[Failure Detection Method]] [related_to:: [[P-F Interval and Condition Monitoring]]] PM effectiveness and hidden failure
- ISO cl. B.2.4 [has_value:: 9] detection method categories in text (p.182)
- ISO cl. B.2.4 [contradicts:: ISO:B.4] text says 9 categories vs table 11 codes; use table
- ISO:B.4 [applies_to:: Fire and Gas Detector] special interpretation also for sensors and logic (Table B.4 fn a)
- Failure Found During PM [detected_by:: PM Type] record PM type as detection method, not Corrective maintenance (cl. 9.6.3, p.43)
- Failure Found During PM [differs_from:: ISO:B.4-9] not coded as Corrective maintenance (cl. 9.6.3)

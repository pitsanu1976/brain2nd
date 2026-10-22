---
title: Resolution Codes
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [resolution, coding, oreda, data-quality, iso-14224]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__resolution-code.csv, compressor-failure-hierarchy__notes.csv, compressor-failure-hierarchy__failure-hierarchy.csv, coce-resolution.jpg, reliability-based-maintenance-management.md, iso-14224.md]
confidence: high
contested: true
---

# Resolution Codes (14 รหัส)

**Resolution** คือการดำเนินการแก้ไข/ตอบสนอง เป็นระดับที่ 7 (ท้ายสุด) ของ [[Failure Hierarchy]] รหัสเต็มอยู่ในคอลัมน์ `Resolution_CODE` และเป็นส่วนหนึ่งของแต่ละแถวใน dataset ดู [[CAUSE_CODE Convention]]

## ตาราง 14 รหัส

"แถวใน Failure Hierarchy" = จำนวนแถวข้อมูล (จากทั้งหมด 7,882 แถว) ที่ใช้รหัสนั้น "Standard action" = ข้อความ action มาตรฐานใน `Resolution Detail`

| Code | Resolution | ใน OREDA list (13) | แถวใน Failure Hierarchy | Standard action |
|---|---|---|---|---|
| ADJ | Adjust | ใช่ | 632 | adjust / reset to restore correct condition |
| CHK | Check | ใช่ | 1,175 | check condition and confirm cause |
| NFF | No Fault Found | ใช่ | 119 | tested, no fault found - return to service |
| REF | Refit | ใช่ | 396 | remove and refit component correctly |
| REP | Repair | ใช่ | 987 | repair affected component |
| RPL | Replace | ใช่ | 1,141 | replace affected component |
| TST | Test | ใช่ | 501 | function / performance test |
| INS | Inspection | ใช่ | 794 | inspect affected component (visual / NDT) |
| SVC | Service | ใช่ | 421 | service: clean / lubricate / top up / flush |
| COM | Combination | ใช่ | 580 | combination of several activities as found |
| MOD | Modify | ใช่ | 614 | modify design, material or operating practice to prevent recurrence |
| OVH | Overhaul | ใช่ | 438 | overhaul item / sub-assembly |
| OTR | Other | ใช่ | 84 | action not covered by standard categories (record details) |
| CHG | Change | **ไม่** | 0 | (ไม่มีข้อมูล) |

ผลรวมแถวของ 13 รหัสแรก = 7,882 (ตรงกับจำนวนแถวข้อมูลทั้งหมด)

## ข้อขัดแย้ง (contested)

- Sheet "resolution code" มี **14 รหัส** รวม `CHG - Change` แต่ OREDA resolution list (Notes และภาพ `coce-resolution.jpg`) และ Resolution Matrix มี **13** (ไม่มี Change) และไม่มีแถวใดใน Failure Hierarchy ใช้ `CHG`
- การตัดสินใจ: คงทั้งสองมุมมอง ถือว่า resolution ที่ใช้จริงคือ 13 รหัส; `CHG` เป็นรหัสที่ประกาศไว้แต่ไม่ถูกใช้ (ไม่ทราบสาเหตุ source ไม่ระบุ) บันทึกใน [[log]]

## การเลือก resolution ต่อ mechanism

ทุก [[Failure Mechanism]] ได้รับเฉพาะ resolution ที่ "น่าจะเป็นไปได้" (233 จาก 37 x 13 คู่) เช่น Wear -> No Fault Found ถูกตัดออก ดูตารางเต็มที่ [[Resolution Matrix by Mechanism]] ทุกแถวระบุ `Resolution Detail Basis`: **Item-specific** (action เฉพาะ item จาก mechanism library) หรือ **Standard** (ข้อความมาตรฐานข้างบน)

หมายเหตุ: resolution ใน dataset เป็น engineering judgement ไม่ใช่ข้อมูลการซ่อมจริงของ OREDA ต้อง review กับ CMMS/RCA ก่อนใช้

## เทียบกับ ISO 14224:2016 (Table B.5 maintenance activity)

เพิ่ม 2026-10-21 ตารางและข้อขัดแย้งด้านบนเป็นของ dataset คงไว้ตามเดิม ส่วนนี้เป็นความต่างระหว่างสอง source ไม่ใช่ข้อขัดแย้งใหม่

ISO เรียกฟิลด์นี้ว่า **maintenance activity** มี **12 รหัส** (ISO 14224 Table B.5, p.183-185) C = ใช้กับ corrective, P = ใช้กับ preventive

| ISO code | Activity | ใช้ | รหัส dataset ที่ตรงกัน |
|---|---|---|---|
| 1 | Replace | C, P | RPL |
| 2 | Repair | C | REP |
| 3 | Modify | C, P | MOD |
| 4 | Adjust | C, P | ADJ |
| 5 | Refit | C, P | REF |
| 6 | Check | C | CHK (และ NFF ดูข้างล่าง) |
| 7 | Service | P | SVC |
| 8 | Test | P | TST |
| 9 | Inspection | P | INS |
| 10 | Overhaul | C, P | OVH |
| 11 | Combination | C, P | COM |
| 12 | Other | C, P | OTR |

ความต่างสำคัญ

- **NFF และ CHG ไม่ใช่รหัส ISO** ISO ไม่มี "No fault found" กรณีสืบแล้วไม่พบสาเหตุให้บันทึกเป็น **Check** (Table B.5 fn c, p.184-185) ดังนั้น NFF (119 แถวใน dataset) map เป็น Check ได้ และ `CHG - Change` ซึ่งเป็นรหัสที่ declared แต่ไม่ถูกใช้ (ดูข้อขัดแย้งด้านบน) ก็ไม่มีใน ISO ด้วย เป็นหลักฐานเสริมว่าถือ 13 รหัสที่ใช้จริงต่อไปได้ แต่ไม่ได้อธิบายว่าทำไม sheet จึงประกาศ CHG จึงคง `contested: true` ไว้ให้ผู้ใช้ตัดสิน
- **Refit ต่างความหมาย**: ISO กำหนด Refit เป็นงานเล็กน้อยให้สภาพยอมรับได้ (ขัด ทำความสะอาด ทาสี หล่อลื่น เปลี่ยนน้ำมัน) แต่ dataset ใช้ข้อความ "remove and refit component correctly" (ถอดและประกอบกลับให้ถูกต้อง) ซึ่งใกล้ความหมายการประกอบใหม่มากกว่า และงาน service/หล่อลื่นใน dataset อยู่ที่ SVC ซึ่ง ISO จัดเป็นงาน PM ตามรอบ ควรระวังเมื่อ map ข้อมูลเข้า ISO
- ISO ไม่มีรหัสที่บอกว่า restore เป็น good-as-new หรือ bad-as-old (cl. B.2.5, p.185)
- กติกา ISO: บันทึก activity ที่เด่นที่สุด Repair/Replace/Overhaul/Modify มี priority เหนือ Refit/Adjust; ถ้าเปลี่ยนทั้ง equipment unit ให้ reset เวลาเดินเครื่อง (ยกเว้นของง่าย) (p.184-185)
- ISO ใช้รหัสนี้กับ **ทั้ง corrective และ preventive** ขณะที่ dataset ผูก resolution กับ mechanism เป็น engineering judgement

ดูฟิลด์อื่นของ record ที่ [[Failure Detection Method]], [[Failure Cause Codes]] และภาพรวมที่ [[ISO 14224]]

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความ: ฟิลด์ Action ใน record ขั้นต่ำของ CMMS (RBMM p.151-152) ใกล้เคียง Resolution ในแง่ข้อมูลที่ต้องเก็บ ดู [[Failure Data Recording]] และการเลือกงานป้องกันที่ควรทำ (PM task) ดู [[PM Task Selection]]

## Triplets

- [[Resolution Codes]] [at_level:: 7] last level of [[Failure Hierarchy]]
- [[Resolution Codes]] [part_of:: [[Failure Hierarchy]]]
- [[Resolution Codes]] [has_value:: 14] codes in resolution code sheet [contested:: true]
- [[Resolution Codes]] [has_value:: 13] codes in OREDA resolution list and Resolution Matrix [contested:: true]
- [[Resolution Codes]] [has_value:: 7882] Failure Hierarchy rows, sum of 13 used codes
- ADJ [is_a:: [[Resolution Codes]]]
- ADJ [has_label:: Adjust]
- ADJ [has_value:: 632] Failure Hierarchy rows
- CHK [is_a:: [[Resolution Codes]]]
- CHK [has_label:: Check]
- CHK [has_value:: 1175] Failure Hierarchy rows
- NFF [is_a:: [[Resolution Codes]]]
- NFF [has_label:: No Fault Found]
- NFF [has_value:: 119] Failure Hierarchy rows
- REF [is_a:: [[Resolution Codes]]]
- REF [has_label:: Refit]
- REF [has_value:: 396] Failure Hierarchy rows
- REP [is_a:: [[Resolution Codes]]]
- REP [has_label:: Repair]
- REP [has_value:: 987] Failure Hierarchy rows
- RPL [is_a:: [[Resolution Codes]]]
- RPL [has_label:: Replace]
- RPL [has_value:: 1141] Failure Hierarchy rows
- TST [is_a:: [[Resolution Codes]]]
- TST [has_label:: Test]
- TST [has_value:: 501] Failure Hierarchy rows
- INS [is_a:: [[Resolution Codes]]]
- INS [has_label:: Inspection]
- INS [has_value:: 794] Failure Hierarchy rows
- SVC [is_a:: [[Resolution Codes]]]
- SVC [has_label:: Service]
- SVC [has_value:: 421] Failure Hierarchy rows
- COM [is_a:: [[Resolution Codes]]]
- COM [has_label:: Combination]
- COM [has_value:: 580] Failure Hierarchy rows
- MOD [is_a:: [[Resolution Codes]]]
- MOD [has_label:: Modify]
- MOD [has_value:: 614] Failure Hierarchy rows
- OVH [is_a:: [[Resolution Codes]]]
- OVH [has_label:: Overhaul]
- OVH [has_value:: 438] Failure Hierarchy rows
- OTR [is_a:: [[Resolution Codes]]]
- OTR [has_label:: Other]
- OTR [has_value:: 84] Failure Hierarchy rows
- CHG [is_a:: [[Resolution Codes]]] declared in resolution code sheet only [contested:: true]
- CHG [has_label:: Change]
- CHG [has_value:: 0] Failure Hierarchy rows; not in OREDA list of 13 [contested:: true]
- CHG [differs_from:: [[OREDA]]] absent from OREDA resolution list and Resolution Matrix [contested:: true]
- [[Failure Mechanism]] [resolved_by:: [[Resolution Codes]]] 233 of 37 x 13 pairs, see [[Resolution Matrix by Mechanism]]
- WEAR [differs_from:: NFF] Wear -> No Fault Found excluded from matrix
- [[Resolution Codes]] [defined_in:: [[OREDA]]] 13-code list (coce-resolution.jpg)
- [[Resolution Codes]] [maps_to:: [[ISO 14224]]] Table B.5 maintenance activity, 12 codes (p.183-185)
- RPL [maps_to:: ISO:B.5-1] Replace, C/P
- REP [maps_to:: ISO:B.5-2] Repair, C
- MOD [maps_to:: ISO:B.5-3] Modify, C/P
- ADJ [maps_to:: ISO:B.5-4] Adjust, C/P
- REF [maps_to:: ISO:B.5-5] Refit, C/P; meaning differs
- CHK [maps_to:: ISO:B.5-6] Check, C
- NFF [maps_to:: ISO:B.5-6] ISO records no fault found as Check (Table B.5 fn c, p.184-185)
- SVC [maps_to:: ISO:B.5-7] Service, P
- TST [maps_to:: ISO:B.5-8] Test, P
- INS [maps_to:: ISO:B.5-9] Inspection, P
- OVH [maps_to:: ISO:B.5-10] Overhaul, C/P
- COM [maps_to:: ISO:B.5-11] Combination, C/P
- OTR [maps_to:: ISO:B.5-12] Other, C/P
- NFF [differs_from:: [[ISO 14224]]] not an ISO code (Table B.5 fn c)
- CHG [differs_from:: [[ISO 14224]]] not an ISO code
- REF [differs_from:: ISO:B.5-5] dataset "remove and refit component correctly" vs ISO minor work to acceptable condition
- ISO:B.5 [applies_to:: Corrective and Preventive Maintenance] maintenance activity codes (Table B.5)
- [[Resolution Codes]] [related_to:: [[Failure Data Recording]]] Action field in minimum CMMS record (RBMM p.151-152)
- [[Resolution Codes]] [related_to:: [[PM Task Selection]]]

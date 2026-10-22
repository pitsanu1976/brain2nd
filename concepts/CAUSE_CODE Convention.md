---
title: CAUSE_CODE Convention
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [coding, failure-cause, taxonomy, iso-14224]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__sheet5.csv, compressor-failure-hierarchy__subunit-code.csv, compressor-failure-hierarchy__maintainable-item-code.csv, compressor-failure-hierarchy__failure-cause-code.csv, iso-14224.md]
confidence: high
contested: false
---

# CAUSE_CODE Convention

คอลัมน์ท้ายของ sheet Failure Hierarchy เป็นชุดรหัสแยกส่วนสำหรับ filter/pivot

## โครงสร้างคอลัมน์รหัส

| คอลัมน์ | ตัวอย่าง | ความหมาย |
|---|---|---|
| ASSET GROUP | `COCE` | กลุ่ม asset (compressor) ค่าเดียวทั้งไฟล์ |
| FAILURE MODE | `AIR` | รหัส 3 ตัวอักษร ดู [[Failure Mode]] |
| CAUSE_CODE | `PWTR-INST-FSIG` | `SubUnit`-`Item`-`Mechanism` |
| Resolution_CODE | `ADJ` | ดู [[Resolution Codes]] |
| Sub Unit | `PWTR` | ส่วนที่ 1 ของ CAUSE_CODE |
| Maintainable Item | `INST` | ส่วนที่ 2 ดู [[Maintainable Item]] |
| Failure Mechanism | `FSIG` | ส่วนที่ 3 ดู [[Failure Mechanism]] |
| CAUSE_DESCRIPTION | Power transmission-Instruments-Faulty signal/indication/alarm | คำอธิบายเต็ม (ตรงกับ Sheet5) |

## รูปแบบ

`<SubUnit 4 ตัว>-<Item 4 ตัว>-<Mechanism 4 ตัว>` ทุกส่วนเป็นตัวพิมพ์ใหญ่ 4 ตัวอักษร คั่นด้วย `-`

ตัวอย่างการอ่าน: `CPUN-CYLN-WEAR` = Compressor unit - Cylinder liner - Wear

## Sub Unit (6)

| Code | Sub Unit | หน้า |
|---|---|---|
| PWTR | Power transmission | [[PWTR Power Transmission]] |
| CPUN | Compressor unit | [[CPUN Compressor Unit]] |
| CTMN | Control and monitoring | [[CTMN Control and Monitoring]] |
| LUBS | Lubrication system | [[LUBS Lubrication System]] |
| SHSS | Shaft seal system | [[SHSS Shaft Seal System]] |
| MISC | Miscellaneous | [[MISC Miscellaneous]] |

## ข้อควรระวัง

- **Collision `CTMN`**: เป็นทั้งรหัส Sub Unit และรหัส mechanism (Contamination) ตัวอย่าง `CTMN-INST-CTMN` และ `CPUN-VALV-CTMN` อ่านตามตำแหน่ง ดู [[Failure Cause Codes]]
- **`MISC`** ก็ชนกันเช่นกัน: เป็น Sub Unit (Miscellaneous) และ mechanism (Miscellaneous - general) เช่น `MISC-PSPB-MISC`
- CAUSE_CODE ไม่รวม failure mode: โหมดต่างกันอาจใช้ CAUSE_CODE เดียวกัน (เช่น `PWTR-INST-FSIG` ใช้กับ AIR, PDE, UST ฯลฯ) ถ้าต้องการระบุสาเหตุ-โหมดเฉพาะ ให้ใช้ FAILURE MODE + CAUSE_CODE
- Sheet5 เป็นรายการ CAUSE_CODE ไม่ซ้ำ 473 รหัส

## เทียบกับ ISO 14224:2016

เพิ่ม 2026-10-21 ไม่เปลี่ยนโครงสร้างรหัสของ dataset

- ชื่อ "CAUSE_CODE" ทำให้เข้าใจผิดได้: `SubUnit-Item-Mechanism` ระบุว่า **ส่วนไหน (sub unit/item) เสียด้วย mechanism อะไร** จึงเป็นรหัสระดับ **mechanism** ตามนิยาม ISO ไม่ใช่ root cause (ISO Table B.2 = mechanism, Table B.3 = cause คนละฟิลด์ cl. B.2.2-B.2.3, p.178-181)
- ISO ไม่มีรหัสประกอบแบบนี้ เก็บ sub unit, maintainable item, mechanism, cause เป็นฟิลด์แยกกันใน failure record (ISO 14224 cl. 9.5, Table 6) และรหัส mechanism ของ ISO เป็นตัวเลข (เช่น 2.4 Wear) ไม่ใช่ WEAR
- ถ้าต้องการ root cause ตาม ISO (เช่น Design-related, Maintenance error) ต้องเพิ่มฟิลด์แยก ตารางรหัสดู [[Failure Cause Codes]] และ mechanism ดู [[Failure Mechanism]]
- จุด mapping รหัส sub unit ของ dataset (PWTR, CPUN ฯลฯ) กับ ISO ดู [[Compressor Subdivision Wiki vs ISO 14224]]

## Triplets

- [[CAUSE_CODE Convention]] [has_code:: SubUnit-Item-Mechanism] each part 4 uppercase letters separated by -
- [[CAUSE_CODE Convention]] [has_part:: Sub Unit] part 1
- [[CAUSE_CODE Convention]] [has_part:: [[Maintainable Item]]] part 2
- [[CAUSE_CODE Convention]] [has_part:: [[Failure Mechanism]]] part 3
- [[CAUSE_CODE Convention]] [part_of:: [[Failure Hierarchy]]] code columns at end of Failure Hierarchy sheet
- ASSET GROUP [has_code:: COCE] compressor, single value in file
- FAILURE MODE [has_code:: AIR] example 3-letter code, see [[Failure Mode]]
- Resolution_CODE [has_code:: ADJ] example, see [[Resolution Codes]]
- PWTR-INST-FSIG [has_label:: Power transmission-Instruments-Faulty signal/indication/alarm] CAUSE_DESCRIPTION matches Sheet5
- PWTR-INST-FSIG [part_of:: [[PWTR Power Transmission]]]
- PWTR-INST-FSIG [has_mechanism:: FSIG]
- CPUN-CYLN-WEAR [has_label:: Compressor unit - Cylinder liner - Wear]
- CPUN-CYLN-WEAR [part_of:: [[CPUN Compressor Unit]]]
- CPUN-CYLN-WEAR [has_mechanism:: WEAR]
- [[PWTR Power Transmission]] [has_code:: PWTR] Power transmission
- [[CPUN Compressor Unit]] [has_code:: CPUN] Compressor unit
- [[CTMN Control and Monitoring]] [has_code:: CTMN] Control and monitoring; same code as mechanism Contamination
- [[LUBS Lubrication System]] [has_code:: LUBS] Lubrication system
- [[SHSS Shaft Seal System]] [has_code:: SHSS] Shaft seal system
- [[MISC Miscellaneous]] [has_code:: MISC] Miscellaneous; same code as mechanism Miscellaneous - general
- [[CAUSE_CODE Convention]] [has_value:: 6] sub units
- CTMN-INST-CTMN [part_of:: [[CTMN Control and Monitoring]]] collision example, read by position
- CTMN-INST-CTMN [has_mechanism:: CTMN] Contamination
- CPUN-VALV-CTMN [part_of:: [[CPUN Compressor Unit]]]
- CPUN-VALV-CTMN [has_mechanism:: CTMN] Contamination
- MISC-PSPB-MISC [part_of:: [[MISC Miscellaneous]]] collision example
- MISC-PSPB-MISC [has_mechanism:: MISC] Miscellaneous - general
- [[CAUSE_CODE Convention]] [differs_from:: [[Failure Mode]]] CAUSE_CODE excludes failure mode; use FAILURE MODE + CAUSE_CODE
- PWTR-INST-FSIG [related_to:: [[AIR Abnormal Instrument Reading]]] used with AIR, PDE, UST etc.
- PWTR-INST-FSIG [related_to:: [[PDE Parameter Deviation]]]
- PWTR-INST-FSIG [related_to:: [[UST Spurious Stop]]]
- Sheet5 [has_value:: 473] unique CAUSE_CODEs
- [[CAUSE_CODE Convention]] [at_level:: mechanism] mechanism-level code per ISO, not root cause (Table B.2 vs B.3, cl. B.2.2-B.2.3, p.178-181)
- [[CAUSE_CODE Convention]] [differs_from:: [[ISO 14224]]] ISO keeps sub unit, MI, mechanism, cause as separate fields (cl. 9.5, Table 6); numeric mechanism codes e.g. 2.4 Wear
- WEAR [maps_to:: ISO:B.2-2.4] Wear
- [[CAUSE_CODE Convention]] [related_to:: [[Compressor Subdivision Wiki vs ISO 14224]]] sub unit code mapping

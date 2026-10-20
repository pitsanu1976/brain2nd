---
title: CAUSE_CODE Convention
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [coding, failure-cause, taxonomy]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__sheet5.csv, compressor-failure-hierarchy__subunit-code.csv, compressor-failure-hierarchy__maintainable-item-code.csv, compressor-failure-hierarchy__failure-cause-code.csv]
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

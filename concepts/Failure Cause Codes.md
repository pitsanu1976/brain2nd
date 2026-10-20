---
title: Failure Cause Codes
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [failure-cause, coding, taxonomy, data-quality]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-cause-code.csv, compressor-failure-hierarchy__sheet5.csv, compressor-failure-hierarchy__subunit-code.csv]
confidence: high
contested: true
---

# Failure Cause Codes

มี 2 ชั้นของรหัสสาเหตุ: (1) รหัส **mechanism 4 ตัวอักษร** (sheet "failure cause code") และ (2) รหัสเต็ม **CAUSE_CODE** = `SubUnit-Item-Mechanism` (sheet "Sheet5") รูปแบบอธิบายที่ [[CAUSE_CODE Convention]]

## 1. รหัส mechanism (35 รหัส)

| Code | Mechanism | Code | Mechanism |
|---|---|---|---|
| BLKG | Blockage/plugged | MATF | Material failure - general |
| BRKG | Breakage | MEXT | Misc. external influences |
| BRST | Burst | MISC | Miscellaneous - general |
| CAVT | Cavitation | NCFD | No cause found |
| ALGN | Clearance/ alignment failure | NPWR | No power/ voltage |
| CTMN | Contamination | NSIG | No signal/indication/alarm |
| CTRL | Control failure | OPEN | Open circuit |
| CORR | Corrosion | OTHR | Other |
| DEFM | Deformation | OADJ | Out of adjustment |
| EART | Earth/isolation fault | OVHT | Overheating |
| ELEC | Electrical failure - general | SHRT | Short circuiting |
| EROS | Erosion | SWFL | Software failure |
| EXIN | External influence - general | STCK | Sticking |
| FATG | Fatigue | UNKN | Unknown |
| FPWR | Faulty power/voltage | VIBR | Vibration |
| FSIG | Faulty signal/indication/alarm | WEAR | Wear |
| INST | Instrument failure - general | LEAK | Leakage |
| LOOS | Looseness | | |

## 2. Sheet5 = รายการ CAUSE_CODE ที่ใช้จริง

473 รหัสไม่ซ้ำ (บรรทัดที่ 474 เป็น `#N/A,--` ซึ่งเป็น artifact ของ Excel) จำแนกตาม Sub Unit:

| Sub Unit | จำนวน CAUSE_CODE |
|---|---|
| [[PWTR Power Transmission]] | 50 |
| [[CPUN Compressor Unit]] | 112 |
| [[CTMN Control and Monitoring]] | 80 |
| [[LUBS Lubrication System]] | 97 |
| [[SHSS Shaft Seal System]] | 78 |
| [[MISC Miscellaneous]] | 56 |
| รวม | 473 |

## ข้อขัดแย้งและปัญหาข้อมูล (contested)

1. **รหัส 35 vs mechanism 37**: Notes/ภาพ OREDA ระบุ 37 mechanism แต่ code sheet มี 35 รหัส ขาด `Combined causes` และ `Mechanical Failure - general` (ไม่ถูกใช้ใน Failure Hierarchy ด้วย) ดู [[Failure Mechanism]]
2. **Code collision `CTMN`**: ใช้เป็นทั้งรหัส Sub Unit (Control and monitoring) และรหัส mechanism (Contamination) ทำให้มี CAUSE_CODE เช่น `CTMN-INST-CTMN` (Control and monitoring - Instruments - Contamination) ต้องอ่านตามตำแหน่ง ไม่ใช่ตามตัวอักษร
3. **`#N/A,--`** ท้าย Sheet5 ไม่ใช่รหัสจริง

การตัดสินใจ: เก็บ data ตามต้นฉบับ ไม่ปรับรหัส บันทึกใน [[log]]

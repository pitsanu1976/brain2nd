---
title: Failure Cause Codes
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [failure-cause, coding, taxonomy, data-quality, iso-14224]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-cause-code.csv, compressor-failure-hierarchy__sheet5.csv, compressor-failure-hierarchy__subunit-code.csv, iso-14224.md]
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

## เทียบกับ ISO 14224:2016: failure cause (Table B.3)

เพิ่ม 2026-10-21 จากมาตรฐาน ข้อ 1-3 ข้างบนยังเป็นข้อขัดแย้งภายใน dataset ตามเดิม (ISO ไม่ได้ resolve)

**ข้อสังเกตสำคัญ:** ใน ISO 14224 "failure cause" (root cause, Table B.3) เป็นคนละฟิลด์กับ "failure mechanism" (Table B.2): mechanism = สาเหตุที่สังเกตได้ ส่วน cause = เหตุเริ่มต้นหรือ root cause (cl. B.2.2-B.2.3, p.178-181) รหัส 4 ตัวอักษรใน sheet "failure cause code" ของ dataset (BLKG, WEAR ฯลฯ) จึงเป็นรหัส **mechanism** ตามนิยาม ISO ไม่ใช่ root cause แม้ชื่อ sheet จะเรียก cause ดู [[Failure Mechanism]] และ [[CAUSE_CODE Convention]] ส่วน dataset OREDA ไม่มีฟิลด์ root cause ตามความหมาย ISO (ต่างขอบเขตของสอง source ไม่ใช่ความขัดแย้งของข้อมูล)

### ISO Table B.3: 5 หมวด 21 รหัส (p.181-182)

| หมวด | รหัส |
|---|---|
| 1 Design-related | 1.0 General, 1.1 Improper capacity, 1.2 Improper material |
| 2 Fabrication/installation-related | 2.0 General, 2.1 Fabrication failure, 2.2 Installation failure |
| 3 Operation/maintenance | 3.0 General, 3.1 Off-design service, 3.2 Operating error, 3.3 Maintenance error, 3.4 Expected wear and tear |
| 4 Management | 4.0 General, 4.1 Documentation error, 4.2 Management error |
| 5 Miscellaneous | 5.0 General, 5.1 No cause found, 5.2 Common cause, 5.3 Combined causes, 5.4 Other unit/cascading failure, 5.5 Other, 5.6 Unknown |

- ใช้ subdivision ก่อน general และหลีกเลี่ยง 5.5/5.6 เช่นเดียวกับ mechanism (cl. B.2.1, p.178)
- human error (Operating error, Maintenance error) อยู่ที่ฟิลด์ cause ไม่ใช่ mechanism
- มักยังไม่รู้ root cause ตอนพบ failure มาตรฐานแนะนำ RCA สำหรับ failure ที่ซับซ้อน ผลกระทบสูง เกิดถี่ผิดปกติ หรือค่าซ่อมสูง (p.181) ดู [[Failure Data Recording]]
- **Common cause failure** (cl. B.2.3.2, p.182): ถ้าเกิดที่ระดับเดียวกับหรือสูงกว่าหน่วยที่เก็บข้อมูล ให้บันทึก failure แยกทุก item แต่ใส่ cause จริงที่ item เดียว ที่เหลือใส่ 5.2 Common cause ถ้าเสียหลายจุดต่ำกว่าหน่วยข้อมูลให้บันทึก failure เดียว ส่วน failure ลูกโซ่ไม่ใช่ CCF ให้บันทึกเฉพาะตัวแรก

ดูภาพรวมที่ [[ISO 14224 Taxonomy]]

## Triplets

- [[Failure Cause Codes]] [has_part:: [[Failure Mechanism]]] layer 1: 4-letter mechanism codes (failure cause code sheet)
- [[Failure Cause Codes]] [has_part:: [[CAUSE_CODE Convention]]] layer 2: full CAUSE_CODE SubUnit-Item-Mechanism (Sheet5)
- [[Failure Cause Codes]] [has_value:: 35] mechanism codes in failure cause code sheet [contested:: true]
- [[Failure Mechanism]] [has_value:: 37] mechanisms in Notes/OREDA image [contested:: true]
- [[Failure Cause Codes]] [contradicts:: [[Failure Mechanism]]] 35 codes vs 37 mechanisms; missing Combined causes and Mechanical Failure - general [contested:: true]
- Combined causes [differs_from:: [[Failure Cause Codes]]] no code, not used in Failure Hierarchy
- Mechanical Failure - general [differs_from:: [[Failure Cause Codes]]] no code, not used in Failure Hierarchy
- Sheet5 [has_value:: 473] unique CAUSE_CODEs
- Sheet5 [has_part:: #N/A,--] line 474 Excel artifact, not a real code [contested:: true]
- [[PWTR Power Transmission]] [has_value:: 50] CAUSE_CODEs (Sheet5)
- [[CPUN Compressor Unit]] [has_value:: 112] CAUSE_CODEs (Sheet5)
- [[CTMN Control and Monitoring]] [has_value:: 80] CAUSE_CODEs (Sheet5)
- [[LUBS Lubrication System]] [has_value:: 97] CAUSE_CODEs (Sheet5)
- [[SHSS Shaft Seal System]] [has_value:: 78] CAUSE_CODEs (Sheet5)
- [[MISC Miscellaneous]] [has_value:: 56] CAUSE_CODEs (Sheet5)
- CTMN [differs_from:: [[CTMN Control and Monitoring]]] code collision: same code for mechanism Contamination and sub unit; read by position [contested:: true]
- CTMN-INST-CTMN [has_label:: Control and monitoring - Instruments - Contamination] collision example
- CTMN-INST-CTMN [part_of:: [[CTMN Control and Monitoring]]]
- CTMN-INST-CTMN [has_mechanism:: CTMN]
- [[Failure Cause Codes]] [differs_from:: [[ISO 14224]]] dataset 4-letter codes are mechanism (Table B.2), not ISO root cause (Table B.3) (cl. B.2.2-B.2.3, p.178-181)
- [[Failure Cause Codes]] [maps_to:: ISO:B.2] mechanism per ISO definition despite sheet name
- [[OREDA]] [differs_from:: ISO:B.3] dataset has no root cause field in ISO sense; scope difference, not data conflict
- ISO:B.3 [has_value:: 21] cause codes in 5 categories (p.181-182)
- ISO:B.3-1 [has_label:: Design-related]
- ISO:B.3-2 [has_label:: Fabrication/installation-related]
- ISO:B.3-3 [has_label:: Operation/maintenance]
- ISO:B.3-4 [has_label:: Management]
- ISO:B.3-5 [has_label:: Miscellaneous]
- ISO:B.3-1.1 [has_label:: Improper capacity]
- ISO:B.3-1.2 [has_label:: Improper material]
- ISO:B.3-2.1 [has_label:: Fabrication failure]
- ISO:B.3-2.2 [has_label:: Installation failure]
- ISO:B.3-3.1 [has_label:: Off-design service]
- ISO:B.3-3.2 [has_label:: Operating error]
- ISO:B.3-3.3 [has_label:: Maintenance error]
- ISO:B.3-3.4 [has_label:: Expected wear and tear]
- ISO:B.3-4.1 [has_label:: Documentation error]
- ISO:B.3-4.2 [has_label:: Management error]
- ISO:B.3-5.1 [has_label:: No cause found]
- ISO:B.3-5.2 [has_label:: Common cause]
- ISO:B.3-5.3 [has_label:: Combined causes]
- ISO:B.3-5.4 [has_label:: Other unit/cascading failure]
- ISO:B.3-5.5 [has_label:: Other] avoid when possible (cl. B.2.1, p.178)
- ISO:B.3-5.6 [has_label:: Unknown] avoid when possible (cl. B.2.1, p.178)
- ISO:B.3-3.2 [differs_from:: ISO:B.2] human error is recorded as cause, not mechanism
- [[Root Cause Analysis]] [applies_to:: High Impact Failure] complex, high impact, unusually frequent or high repair cost (p.181)
- Common Cause Failure [uses:: ISO:B.3-5.2] record each item separately, true cause on one item, others 5.2 (cl. B.2.3.2, p.182)
- Cascading Failure [differs_from:: Common Cause Failure] record only the first failure
- [[Failure Cause Codes]] [related_to:: [[Failure Data Recording]]]
- [[Failure Cause Codes]] [related_to:: [[ISO 14224 Taxonomy]]]

---
title: Failure Mechanism
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [failure-mechanism, taxonomy, oreda, coding, iso-14224, cmrp]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__notes.csv, compressor-failure-hierarchy__failure-cause-code.csv, compressor-failure-hierarchy__resolution-matrix.csv, failure-structure.md, failure-structure__sheet2.csv, coce-failure-mechanism.jpg, reliability-based-maintenance-management.md, iso-14224.md, cmrp.md]
confidence: high
contested: false
---

# Failure Mechanism

**Failure mechanism** คือกระบวนการทางกายภาพ/เคมี/ไฟฟ้าที่นำไปสู่ [[Failure Mode]] เป็นระดับที่ 5 ของ [[Failure Hierarchy]] รายชื่อมาจาก OREDA failure mechanism list (ภาพ `coce-failure-mechanism.jpg`) รวม **37 รายการ**

## กติกาใน dataset

- แต่ละ [[Maintainable Item]] เลือกเฉพาะ mechanism ที่เกี่ยวข้องทางกายภาพ (sheet "Mechanism Library") พร้อม detail เฉพาะ item (เช่น Valves x Wear = "valve plate/seat/spring wear")
- mechanism ปรากฏในแถว Failure Hierarchy ก็ต่อเมื่อสามารถทำให้เกิด failure mode นั้นกับ item นั้น
- failure mode `OTH` ใช้ mechanism `Other` และ `UNK` ใช้ `Unknown` กับทุก item (ดู [[OTH Other]])
- mechanism x [[Resolution Codes]] ที่เป็นไปได้ อยู่ใน [[Resolution Matrix by Mechanism]]
- รหัส 4 ตัวอักษรของ mechanism เป็นส่วนท้ายของ CAUSE_CODE ดู [[Failure Cause Codes]] และ [[CAUSE_CODE Convention]]

## ตาราง 37 mechanism

คอลัมน์ Category มาจาก `failure-structure__sheet2.csv` (มีเพียง 24 รายการ; "-" = ไม่มีใน sheet นั้น; "(blank)" = มีแต่ไม่ระบุ category) ค่าเขียนตามต้นฉบับ (`envir`, `electrical/constrol` ใน source สะกดว่า constrol)

| Mechanism | Code | Category (sheet2) | No. of resolutions (matrix) |
|---|---|---|---|
| Blockage/plugged | BLKG | physical | 6 |
| Breakage | BRKG | physical | 7 |
| Burst | BRST | electrical/constrol (ดูข้อสังเกต) | 6 |
| Cavitation | CAVT | - | 7 |
| Clearance/ alignment failure | ALGN | physical | 8 |
| Combined causes | (ไม่มีรหัส) | (blank) | 6 |
| Contamination | CTMN | envir | 5 |
| Control failure | CTRL | electrical/constrol | 6 |
| Corrosion | CORR | envir | 7 |
| Deformation | DEFM | physical | 6 |
| Earth/isolation fault | EART | - | 6 |
| Electrical failure - general | ELEC | - | 6 |
| Erosion | EROS | - | 6 |
| External influence - general | EXIN | - | 7 |
| Fatigue | FATG | - | 6 |
| Faulty power/voltage | FPWR | - | 5 |
| Faulty signal/indication/alarm | FSIG | electrical/constrol | 7 |
| Instrument failure - general | INST | electrical/constrol | 8 |
| Leakage | LEAK | physical | 10 |
| Looseness | LOOS | physical | 6 |
| Material failure - general | MATF | physical | 7 |
| Mechanical Failure - general | (ไม่มีรหัส) | physical | 7 |
| Misc. external influences | MEXT | - | 6 |
| Miscellaneous - general | MISC | - | 6 |
| No cause found | NCFD | (blank) | 3 |
| No power/ voltage | NPWR | electrical/constrol | 5 |
| No signal/indication/alarm | NSIG | electrical/constrol | 5 |
| Open circuit | OPEN | electrical/constrol | 5 |
| Other | OTHR | - | 5 |
| Out of adjustment | OADJ | (blank) | 4 |
| Overheating | OVHT | - | 9 |
| Short circuiting | SHRT | - | 5 |
| Software failure | SWFL | - | 5 |
| Sticking | STCK | physical | 8 |
| Unknown | UNKN | (blank) | 4 |
| Vibration | VIBR | physical | 9 |
| Wear | WEAR | physical | 9 |

รวมคู่ mechanism x resolution ที่เป็นไปได้ = 233 (ตรงกับ Notes: 233 of 37 x 13 pairs)

## ข้อสังเกตคุณภาพข้อมูล

- **Combined causes** และ **Mechanical Failure - general** อยู่ใน OREDA list และ Resolution Matrix แต่ **ไม่มีรหัสใน sheet "failure cause code"** (35 รหัส) และ **ไม่ปรากฏเลยใน sheet Failure Hierarchy** (ค้นแล้ว 0 แถว) ทั้งที่ภาพ OREDA แยกประเภท (เช่น reciprocating LOO: Mechanical Failure - general = 18.62) ใช้ descriptor นี้ นั่นคือ dataset ไม่ได้ map descriptor นี้ไปสู่ item-specific mechanism ดู [[Failure Cause Codes]]
- **Burst** ถูกจัดเป็น `electrical/constrol` ใน sheet2 ซึ่งผิดวิสัย (Burst ปกติเป็นกลไกทางกายภาพ เช่น piping/cooler) เป็นข้อสังเกตของ wiki นี้ ไม่มี source อื่นยืนยัน/ปฏิเสธ confidence ต่ำสำหรับข้อนี้
- Sheet2 มีเพียง 24 จาก 37 mechanism

## เทียบกับ ISO 14224:2016 (Table B.2)

ส่วนนี้เพิ่มจากมาตรฐาน ตารางและข้อสังเกตด้านบนเป็นของ dataset OREDA คงไว้ตามเดิม

ISO Table B.2 (p.179-180) มี **6 หมวด 38 รหัส** (1.0-6.4) ใช้รหัสตัวเลขเท่านั้น **ไม่มีรหัส 4 ตัวอักษร** (LEAK, WEAR ฯลฯ) ดังนั้นรหัสเหล่านี้เป็นรหัสของ dataset ไม่ใช่รหัสมาตรฐาน

| หมวด | รหัสย่อย (ชื่อ ISO) |
|---|---|
| 1 Mechanical failure | 1.0 General, 1.1 Leakage, 1.2 Vibration, 1.3 Clearance/alignment failure, 1.4 Deformation, 1.5 Looseness, 1.6 Sticking |
| 2 Material failure | 2.0 General, 2.1 Cavitation, 2.2 Corrosion, 2.3 Erosion, 2.4 Wear, 2.5 Breakage, 2.6 Fatigue, 2.7 Overheating, 2.8 Burst |
| 3 Instrument failure | 3.0 General, 3.1 Control failure, 3.2 No signal/indication/alarm, 3.3 Faulty signal/indication/alarm, 3.4 Out of adjustment, 3.5 Software error, 3.6 Common cause/Common mode failure |
| 4 Electrical failure | 4.0 General, 4.1 Short circuiting, 4.2 Open circuit, 4.3 No power/voltage, 4.4 Faulty power/voltage, 4.5 Earth/isolation fault |
| 5 External influence | 5.0 General, 5.1 Blockage/plugged, 5.2 Contamination, 5.3 Miscellaneous external influences |
| 6 Miscellaneous | 6.0 General, 6.1 No cause found, 6.2 Combined causes, 6.3 Other, 6.4 Unknown |

### ความต่างจากรายการ 37 ของ OREDA

- ISO มี **3.6 Common cause/Common mode failure** ซึ่งรายการ OREDA ใน wiki ไม่มี
- รายการ OREDA มี general ครบ 6 ตัว (Mechanical, Material, Instrument, Electrical, External influence, Miscellaneous) ตรงกับ x.0 ของ ISO ทั้ง 6 หมวด ส่วนต่างของจำนวน 37 vs 38 จึงเท่ากับ 3.6 หนึ่งรายการ (derived: นับจากตาราง B.2 และตารางของ wiki ไม่ได้จับคู่ทีละรายการ)
- **Burst เป็น 2.8 ภายใต้ Material failure** (ISO Table B.2, p.180) ไม่ใช่ electrical/instrument: นี่ยืนยันข้อสังเกตเดิมที่ว่า sheet2 จัด Burst เป็น `electrical/constrol` ผิดวิสัย (เดิม confidence ต่ำ ตอนนี้มีมาตรฐานรองรับ) ข้อมูลเดิมใน sheet2 คงไว้ตามต้นฉบับ
- ISO จัด Blockage/plugged และ Contamination ไว้ใน **External influence (5.1, 5.2)** และ Overheating, Cavitation, Corrosion, Erosion, Wear ใน Material failure ซึ่งต่างจากหมวด `physical`/`envir` ใน sheet2 (ที่มีเพียง 24 จาก 37 รายการ)

### กติกาการใช้ของ ISO (cl. B.2.1-B.2.2, p.178)

- เลือกรหัส **subdivision (เช่น 1.1) ก่อนรหัสหมวด general (เช่น 1.0)** ใช้ general เมื่อข้อมูลไม่พอ
- หลีกเลี่ยง 6.3 Other และ 6.4 Unknown เมื่อทำได้ ถ้ามีหลาย mechanism ให้เลือกตัวสำคัญที่สุด (Table B.2 fn a)
- **อย่าเอาอาการ (failure mode) มาบันทึกซ้ำเป็น mechanism**: ตัวอย่างในมาตรฐานคือ valve รั่ว process medium ออกภายนอกโดยไม่ทราบสาเหตุ ให้ mode = ELP และ mechanism = 6.4 Unknown ไม่ใช่ 1.1 Leakage
- **human error ไม่ใช่ mechanism** ให้บันทึกเป็น failure cause (Table B.2 fn b) ดู [[Failure Cause Codes]]
- ในทางปฏิบัติ mechanism คือ failure mode ที่ระดับ maintainable item และเป็นสาเหตุที่ "สังเกตได้" ส่วน root cause อยู่อีกฟิลด์ (cl. B.2.2, p.178)

ภาพรวมระดับ taxonomy ดู [[ISO 14224 Taxonomy]] และ [[ISO 14224]]

## กลไกการสึกเชิง tribology (CMRP)

ส่วนนี้เพิ่มจาก [[CMRP Course]] รายละเอียดอยู่ที่ [[Wear Mechanisms]] หลักสูตรแบ่งการสึกเป็น abrasive, adhesive, erosion, cavitation, fretting, contact fatigue และ corrosive พร้อมสาเหตุและวิธีควบคุม (CMRP CMPR-02 p.1-7) ทั้งหมดเป็นรายละเอียดของหมวด **2 Material failure** ของ ISO Table B.2:
- abrasive และ adhesive -> WEAR (2.4); erosion -> EROS (2.3); cavitation -> CAVT (2.1); contact fatigue -> FATG (2.6); corrosive -> CORR (2.2); fretting -> WEAR หรือ FATG (การจับคู่เป็นการตีความของ wiki)
- contamination (CTMN, 5.2) เป็นตัวเร่งของ abrasive wear และ contact fatigue ตาม slide (p.4, p.7) แต่ตามกติกา ISO ให้ลง mechanism ตามสิ่งที่เห็นที่ item แล้วบันทึก contamination เป็นสาเหตุเมื่อเหมาะสม
- การตรวจจับล่วงหน้าด้วย wear particle analysis ดู [[Lubrication and Oil Analysis]]

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความจากหนังสือ ไม่ใช่ข้อมูล OREDA: RBMM Fig 5.13 (p.131) แสดงลำดับ causation 7 ระดับจนถึง design/assembly/procurement/storekeeping error ใช้เป็นแนวแยก mechanism กับ latent cause ได้ ดู [[Failure Data Recording]] และพฤติกรรมการเสียตามอายุ (wear-out vs random) ที่ [[Failure Patterns and Bathtub Curve]]

## Triplets

- [[Failure Mechanism]] [at_level:: 5] level 5 of [[Failure Hierarchy]]
- [[Failure Mechanism]] [part_of:: [[Failure Hierarchy]]]
- [[Failure Mechanism]] [has_value:: 37] mechanisms in OREDA list (coce-failure-mechanism.jpg)
- [[Failure Mechanism]] [defined_in:: [[OREDA]]] 37-item list
- [[Failure Mechanism]] [related_to:: [[Failure Mode]]] physical/chemical/electrical process leading to failure mode
- [[Failure Mechanism]] [resolved_by:: [[Resolution Codes]]] possible pairs in [[Resolution Matrix by Mechanism]]
- [[Resolution Matrix by Mechanism]] [has_value:: 233] possible mechanism x resolution pairs of 37 x 13
- [[Failure Mechanism]] [part_of:: [[CAUSE_CODE Convention]]] 4-letter code is last segment of CAUSE_CODE
- [[OTH Other]] [has_mechanism:: OTHR] all items (see [[OTH Other]])
- UNK [has_mechanism:: UNKN] all items
- BLKG [is_a:: [[Failure Mechanism]]]
- BLKG [has_label:: Blockage/plugged]
- BLKG [has_category:: physical] sheet2
- BLKG [has_value:: 6] possible resolutions (Resolution Matrix)
- BRKG [is_a:: [[Failure Mechanism]]]
- BRKG [has_label:: Breakage]
- BRKG [has_category:: physical] sheet2
- BRKG [has_value:: 7] possible resolutions (Resolution Matrix)
- BRST [is_a:: [[Failure Mechanism]]]
- BRST [has_label:: Burst]
- BRST [has_category:: electrical/constrol] sheet2, source spelling
- BRST [has_value:: 6] possible resolutions (Resolution Matrix)
- CAVT [is_a:: [[Failure Mechanism]]]
- CAVT [has_label:: Cavitation]
- CAVT [has_value:: 7] possible resolutions (Resolution Matrix)
- ALGN [is_a:: [[Failure Mechanism]]]
- ALGN [has_label:: Clearance/ alignment failure]
- ALGN [has_category:: physical] sheet2
- ALGN [has_value:: 8] possible resolutions (Resolution Matrix)
- Combined causes [is_a:: [[Failure Mechanism]]]
- Combined causes [has_category:: (blank)] present in sheet2 without category
- Combined causes [has_value:: 6] possible resolutions (Resolution Matrix)
- CTMN [is_a:: [[Failure Mechanism]]]
- CTMN [has_label:: Contamination]
- CTMN [has_category:: envir] sheet2
- CTMN [has_value:: 5] possible resolutions (Resolution Matrix)
- CTRL [is_a:: [[Failure Mechanism]]]
- CTRL [has_label:: Control failure]
- CTRL [has_category:: electrical/constrol] sheet2, source spelling
- CTRL [has_value:: 6] possible resolutions (Resolution Matrix)
- CORR [is_a:: [[Failure Mechanism]]]
- CORR [has_label:: Corrosion]
- CORR [has_category:: envir] sheet2
- CORR [has_value:: 7] possible resolutions (Resolution Matrix)
- DEFM [is_a:: [[Failure Mechanism]]]
- DEFM [has_label:: Deformation]
- DEFM [has_category:: physical] sheet2
- DEFM [has_value:: 6] possible resolutions (Resolution Matrix)
- EART [is_a:: [[Failure Mechanism]]]
- EART [has_label:: Earth/isolation fault]
- EART [has_value:: 6] possible resolutions (Resolution Matrix)
- ELEC [is_a:: [[Failure Mechanism]]]
- ELEC [has_label:: Electrical failure - general]
- ELEC [has_value:: 6] possible resolutions (Resolution Matrix)
- EROS [is_a:: [[Failure Mechanism]]]
- EROS [has_label:: Erosion]
- EROS [has_value:: 6] possible resolutions (Resolution Matrix)
- EXIN [is_a:: [[Failure Mechanism]]]
- EXIN [has_label:: External influence - general]
- EXIN [has_value:: 7] possible resolutions (Resolution Matrix)
- FATG [is_a:: [[Failure Mechanism]]]
- FATG [has_label:: Fatigue]
- FATG [has_value:: 6] possible resolutions (Resolution Matrix)
- FPWR [is_a:: [[Failure Mechanism]]]
- FPWR [has_label:: Faulty power/voltage]
- FPWR [has_value:: 5] possible resolutions (Resolution Matrix)
- FSIG [is_a:: [[Failure Mechanism]]]
- FSIG [has_label:: Faulty signal/indication/alarm]
- FSIG [has_category:: electrical/constrol] sheet2, source spelling
- FSIG [has_value:: 7] possible resolutions (Resolution Matrix)
- Instrument failure - general [is_a:: [[Failure Mechanism]]]
- Instrument failure - general [has_category:: electrical/constrol] sheet2, source spelling
- Instrument failure - general [has_value:: 8] possible resolutions (Resolution Matrix)
- LEAK [is_a:: [[Failure Mechanism]]]
- LEAK [has_label:: Leakage]
- LEAK [has_category:: physical] sheet2
- LEAK [has_value:: 10] possible resolutions (Resolution Matrix)
- LOOS [is_a:: [[Failure Mechanism]]]
- LOOS [has_label:: Looseness]
- LOOS [has_category:: physical] sheet2
- LOOS [has_value:: 6] possible resolutions (Resolution Matrix)
- MATF [is_a:: [[Failure Mechanism]]]
- MATF [has_label:: Material failure - general]
- MATF [has_category:: physical] sheet2
- MATF [has_value:: 7] possible resolutions (Resolution Matrix)
- Mechanical Failure - general [is_a:: [[Failure Mechanism]]]
- Mechanical Failure - general [has_category:: physical] sheet2
- Mechanical Failure - general [has_value:: 7] possible resolutions (Resolution Matrix)
- MEXT [is_a:: [[Failure Mechanism]]]
- MEXT [has_label:: Misc. external influences]
- MEXT [has_value:: 6] possible resolutions (Resolution Matrix)
- MISC [is_a:: [[Failure Mechanism]]]
- MISC [has_label:: Miscellaneous - general]
- MISC [has_value:: 6] possible resolutions (Resolution Matrix)
- NCFD [is_a:: [[Failure Mechanism]]]
- NCFD [has_label:: No cause found]
- NCFD [has_category:: (blank)] present in sheet2 without category
- NCFD [has_value:: 3] possible resolutions (Resolution Matrix)
- NPWR [is_a:: [[Failure Mechanism]]]
- NPWR [has_label:: No power/ voltage]
- NPWR [has_category:: electrical/constrol] sheet2, source spelling
- NPWR [has_value:: 5] possible resolutions (Resolution Matrix)
- NSIG [is_a:: [[Failure Mechanism]]]
- NSIG [has_label:: No signal/indication/alarm]
- NSIG [has_category:: electrical/constrol] sheet2, source spelling
- NSIG [has_value:: 5] possible resolutions (Resolution Matrix)
- OPEN [is_a:: [[Failure Mechanism]]]
- OPEN [has_label:: Open circuit]
- OPEN [has_category:: electrical/constrol] sheet2, source spelling
- OPEN [has_value:: 5] possible resolutions (Resolution Matrix)
- OTHR [is_a:: [[Failure Mechanism]]]
- OTHR [has_label:: Other]
- OTHR [has_value:: 5] possible resolutions (Resolution Matrix)
- OADJ [is_a:: [[Failure Mechanism]]]
- OADJ [has_label:: Out of adjustment]
- OADJ [has_category:: (blank)] present in sheet2 without category
- OADJ [has_value:: 4] possible resolutions (Resolution Matrix)
- OVHT [is_a:: [[Failure Mechanism]]]
- OVHT [has_label:: Overheating]
- OVHT [has_value:: 9] possible resolutions (Resolution Matrix)
- SHRT [is_a:: [[Failure Mechanism]]]
- SHRT [has_label:: Short circuiting]
- SHRT [has_value:: 5] possible resolutions (Resolution Matrix)
- SWFL [is_a:: [[Failure Mechanism]]]
- SWFL [has_label:: Software failure]
- SWFL [has_value:: 5] possible resolutions (Resolution Matrix)
- STCK [is_a:: [[Failure Mechanism]]]
- STCK [has_label:: Sticking]
- STCK [has_category:: physical] sheet2
- STCK [has_value:: 8] possible resolutions (Resolution Matrix)
- UNKN [is_a:: [[Failure Mechanism]]]
- UNKN [has_label:: Unknown]
- UNKN [has_category:: (blank)] present in sheet2 without category
- UNKN [has_value:: 4] possible resolutions (Resolution Matrix)
- VIBR [is_a:: [[Failure Mechanism]]]
- VIBR [has_label:: Vibration]
- VIBR [has_category:: physical] sheet2
- VIBR [has_value:: 9] possible resolutions (Resolution Matrix)
- WEAR [is_a:: [[Failure Mechanism]]]
- WEAR [has_label:: Wear]
- WEAR [has_category:: physical] sheet2
- WEAR [has_value:: 9] possible resolutions (Resolution Matrix)
- Combined causes [differs_from:: [[Failure Cause Codes]]] no code in failure cause code sheet (35 codes), 0 rows in Failure Hierarchy
- Mechanical Failure - general [differs_from:: [[Failure Cause Codes]]] no code in failure cause code sheet (35 codes), 0 rows in Failure Hierarchy
- Mechanical Failure - general [has_value:: 18.62] reciprocating LOO in OREDA image
- Failure Structure Sheet2 [has_value:: 24] of 37 mechanisms listed
- BRST [maps_to:: ISO:B.2-2.8] Burst under Material failure (ISO Table B.2, p.180)
- BRST [has_category:: ISO:B.2-2] Material failure per ISO (Table B.2, p.180) vs sheet2 electrical/constrol
- ISO:B.2-2.8 [has_label:: Burst]
- [[ISO 14224]] [has_value:: 38] mechanism codes in 6 categories, numeric only 1.0-6.4 (Table B.2, p.179-180)
- ISO:B.2-1 [has_label:: Mechanical failure]
- ISO:B.2-2 [has_label:: Material failure]
- ISO:B.2-3 [has_label:: Instrument failure]
- ISO:B.2-4 [has_label:: Electrical failure]
- ISO:B.2-5 [has_label:: External influence]
- ISO:B.2-6 [has_label:: Miscellaneous]
- [[Failure Mechanism]] [differs_from:: [[ISO 14224]]] 4-letter codes are dataset codes, ISO uses numeric codes only (Table B.2)
- ISO:B.2-3.6 [has_label:: Common cause/Common mode failure]
- ISO:B.2-3.6 [differs_from:: [[OREDA]]] not in wiki OREDA list of 37; accounts for 37 vs 38 (derived) [confidence:: medium]
- Mechanical Failure - general [maps_to:: ISO:B.2-1.0] general per category (derived) [confidence:: medium]
- MATF [maps_to:: ISO:B.2-2.0] general per category (derived) [confidence:: medium]
- Instrument failure - general [maps_to:: ISO:B.2-3.0] general per category (derived) [confidence:: medium]
- ELEC [maps_to:: ISO:B.2-4.0] general per category (derived) [confidence:: medium]
- EXIN [maps_to:: ISO:B.2-5.0] general per category (derived) [confidence:: medium]
- MISC [maps_to:: ISO:B.2-6.0] general per category (derived) [confidence:: medium]
- BLKG [maps_to:: ISO:B.2-5.1] External influence (Table B.2)
- CTMN [maps_to:: ISO:B.2-5.2] External influence (Table B.2)
- CAVT [maps_to:: ISO:B.2-2.1] Material failure (Table B.2)
- CORR [maps_to:: ISO:B.2-2.2] Material failure (Table B.2)
- EROS [maps_to:: ISO:B.2-2.3] Material failure (Table B.2)
- WEAR [maps_to:: ISO:B.2-2.4] Material failure (Table B.2)
- OVHT [maps_to:: ISO:B.2-2.7] Material failure (Table B.2)
- ISO:B.2-6.3 [has_label:: Other] avoid when possible (Table B.2 fn a)
- ISO:B.2-6.4 [has_label:: Unknown] avoid when possible (Table B.2 fn a)
- [[ELP External Leakage Process Medium]] [has_mechanism:: ISO:B.2-6.4] ISO example: valve external leak, cause unknown, not 1.1 Leakage (cl. B.2.1-B.2.2, p.178)
- Human Error [differs_from:: [[Failure Mechanism]]] recorded as failure cause, not mechanism (Table B.2 fn b)
- [[Failure Mechanism]] [defined_in:: [[ISO 14224]]] Table B.2; select subdivision before general (cl. B.2.1, p.178)
- [[Failure Mechanism]] [related_to:: [[Failure Data Recording]]] RBMM Fig 5.13 (p.131) 7-level causation
- FATG [maps_to:: ISO:B.2-2.6] Material failure (Table B.2)
- [[Wear Mechanisms]] [part_of:: ISO:B.2-2] tribology detail of Material failure (CMRP CMPR-02 p.1-7), interpretation
- [[Failure Mechanism]] [related_to:: [[Wear Mechanisms]]] abrasive/adhesive -> WEAR, erosion -> EROS, cavitation -> CAVT, contact fatigue -> FATG, corrosive -> CORR, interpretation
- CTMN [contributes_to:: WEAR] contamination accelerates abrasive wear and fatigue (CMRP CMPR-02 p.4, p.7)

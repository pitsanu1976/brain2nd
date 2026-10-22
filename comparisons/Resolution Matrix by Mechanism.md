---
title: Resolution Matrix by Mechanism
created: 2026-10-20
updated: 2026-10-22
type: comparison
tags: [comparison, resolution, failure-mechanism, coding]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__resolution-matrix.csv, compressor-failure-hierarchy__notes.csv]
confidence: high
contested: false
---

# Resolution Matrix by Mechanism

ตารางว่า [[Failure Mechanism]] ใดจับคู่กับ [[Resolution Codes]] ใดได้ (sheet "Resolution Matrix") ใช้สร้างแถว mechanism x resolution ใน Failure Hierarchy

## กติกา

- 37 mechanism x 13 resolution = 481 คู่ที่เป็นไปได้ ถูกคัดเหลือ **233 คู่** ที่น่าจะเป็นไปได้ (Notes ข้อ 7)
- คู่ที่ไม่สมเหตุสมผลถูกตัดออก เช่น Wear -> No Fault Found, Open circuit -> Overhaul, Fatigue -> Service
- ไม่มีรหัส `CHG` (Change) ในเมทริกซ์ ดูข้อขัดแย้งที่ [[Resolution Codes]]
- ทุก mechanism มี `CHK` (Check) เสมอ (37 จาก 37)
- นี่คือ engineering judgement ของผู้จัดทำ dataset ไม่ใช่ข้อมูลจริงของ OREDA

## ตาราง (รหัสที่เป็นไปได้ต่อ mechanism)

ADJ Adjust, CHK Check, COM Combination, INS Inspection, MOD Modify, NFF No Fault Found, OTR Other, OVH Overhaul, REF Refit, REP Repair, RPL Replace, SVC Service, TST Test

| Mechanism | Resolutions | จำนวน |
|---|---|---|
| Blockage/plugged | CHK INS MOD REP RPL SVC | 6 |
| Breakage | CHK COM INS MOD OVH REP RPL | 7 |
| Burst | CHK INS MOD REP RPL TST | 6 |
| Cavitation | ADJ CHK INS MOD OVH REP RPL | 7 |
| Clearance/ alignment failure | ADJ CHK COM INS OVH REF REP RPL | 8 |
| Combined causes | CHK COM INS OVH REP RPL | 6 |
| Contamination | CHK INS MOD RPL SVC | 5 |
| Control failure | ADJ CHK MOD REP RPL TST | 6 |
| Corrosion | CHK COM INS MOD REP RPL SVC | 7 |
| Deformation | CHK COM INS MOD REP RPL | 6 |
| Earth/isolation fault | CHK INS REP RPL SVC TST | 6 |
| Electrical failure - general | CHK COM OTR REP RPL TST | 6 |
| Erosion | CHK INS MOD OVH REP RPL | 6 |
| External influence - general | CHK COM INS MOD OTR REP RPL | 7 |
| Fatigue | CHK COM INS MOD REP RPL | 6 |
| Faulty power/voltage | ADJ CHK REP RPL TST | 5 |
| Faulty signal/indication/alarm | ADJ CHK NFF REF REP RPL TST | 7 |
| Instrument failure - general | ADJ CHK COM NFF OTR REP RPL TST | 8 |
| Leakage | ADJ CHK COM INS MOD OVH REF REP RPL TST | 10 |
| Looseness | ADJ CHK INS REF REP RPL | 6 |
| Material failure - general | CHK COM INS MOD OTR REP RPL | 7 |
| Mechanical Failure - general | CHK COM INS OTR OVH REP RPL | 7 |
| Misc. external influences | CHK INS MOD REP RPL SVC | 6 |
| Miscellaneous - general | ADJ CHK OTR REP RPL SVC | 6 |
| No cause found | CHK NFF TST | 3 |
| No power/ voltage | ADJ CHK REP RPL TST | 5 |
| No signal/indication/alarm | CHK REF REP RPL TST | 5 |
| Open circuit | CHK REF REP RPL TST | 5 |
| Other | CHK COM OTR REP RPL | 5 |
| Out of adjustment | ADJ CHK RPL TST | 4 |
| Overheating | ADJ CHK COM INS MOD OVH REP RPL SVC | 9 |
| Short circuiting | CHK INS REP RPL TST | 5 |
| Software failure | ADJ CHK MOD RPL TST | 5 |
| Sticking | ADJ CHK COM OVH REP RPL SVC TST | 8 |
| Unknown | CHK INS NFF OTR | 4 |
| Vibration | ADJ CHK COM INS MOD OVH REF REP RPL | 9 |
| Wear | ADJ CHK COM INS MOD OVH REP RPL SVC | 9 |

## ข้อสังเกต

- Mechanism ที่มี resolution มากสุด: **Leakage (10)**; รองลงมา Overheating, Vibration, Wear (9)
- Mechanism ที่มีน้อยสุด: **No cause found (3)** (CHK, NFF, TST); Out of adjustment, Unknown (4)
- `NFF` ใช้ได้เฉพาะ Faulty signal/indication/alarm, Instrument failure - general, No cause found, Unknown ซึ่งสะท้อนว่า "ไม่พบความผิดปกติ" สมเหตุสมผลเฉพาะปัญหาประเภทสัญญาณ/ไม่ทราบสาเหตุ
- `OVH` (Overhaul) ใช้กับ mechanism เชิงกลที่เสื่อมสภาพ (Wear, Erosion, Cavitation, Breakage, Overheating, Vibration ฯลฯ)
- จำนวนแถวจริงใน Failure Hierarchy: ดูตารางใน [[Resolution Codes]]

## Triplets

- BLKG [resolved_by:: CHK]
- BLKG [resolved_by:: INS]
- BLKG [resolved_by:: MOD]
- BLKG [resolved_by:: REP]
- BLKG [resolved_by:: RPL]
- BLKG [resolved_by:: SVC]
- BRKG [resolved_by:: CHK]
- BRKG [resolved_by:: COM]
- BRKG [resolved_by:: INS]
- BRKG [resolved_by:: MOD]
- BRKG [resolved_by:: OVH]
- BRKG [resolved_by:: REP]
- BRKG [resolved_by:: RPL]
- BRST [resolved_by:: CHK]
- BRST [resolved_by:: INS]
- BRST [resolved_by:: MOD]
- BRST [resolved_by:: REP]
- BRST [resolved_by:: RPL]
- BRST [resolved_by:: TST]
- CAVT [resolved_by:: ADJ]
- CAVT [resolved_by:: CHK]
- CAVT [resolved_by:: INS]
- CAVT [resolved_by:: MOD]
- CAVT [resolved_by:: OVH]
- CAVT [resolved_by:: REP]
- CAVT [resolved_by:: RPL]
- ALGN [resolved_by:: ADJ]
- ALGN [resolved_by:: CHK]
- ALGN [resolved_by:: COM]
- ALGN [resolved_by:: INS]
- ALGN [resolved_by:: OVH]
- ALGN [resolved_by:: REF]
- ALGN [resolved_by:: REP]
- ALGN [resolved_by:: RPL]
- Combined causes [resolved_by:: CHK]
- Combined causes [resolved_by:: COM]
- Combined causes [resolved_by:: INS]
- Combined causes [resolved_by:: OVH]
- Combined causes [resolved_by:: REP]
- Combined causes [resolved_by:: RPL]
- CTMN [resolved_by:: CHK]
- CTMN [resolved_by:: INS]
- CTMN [resolved_by:: MOD]
- CTMN [resolved_by:: RPL]
- CTMN [resolved_by:: SVC]
- CTRL [resolved_by:: ADJ]
- CTRL [resolved_by:: CHK]
- CTRL [resolved_by:: MOD]
- CTRL [resolved_by:: REP]
- CTRL [resolved_by:: RPL]
- CTRL [resolved_by:: TST]
- CORR [resolved_by:: CHK]
- CORR [resolved_by:: COM]
- CORR [resolved_by:: INS]
- CORR [resolved_by:: MOD]
- CORR [resolved_by:: REP]
- CORR [resolved_by:: RPL]
- CORR [resolved_by:: SVC]
- DEFM [resolved_by:: CHK]
- DEFM [resolved_by:: COM]
- DEFM [resolved_by:: INS]
- DEFM [resolved_by:: MOD]
- DEFM [resolved_by:: REP]
- DEFM [resolved_by:: RPL]
- EART [resolved_by:: CHK]
- EART [resolved_by:: INS]
- EART [resolved_by:: REP]
- EART [resolved_by:: RPL]
- EART [resolved_by:: SVC]
- EART [resolved_by:: TST]
- ELEC [resolved_by:: CHK]
- ELEC [resolved_by:: COM]
- ELEC [resolved_by:: OTR]
- ELEC [resolved_by:: REP]
- ELEC [resolved_by:: RPL]
- ELEC [resolved_by:: TST]
- EROS [resolved_by:: CHK]
- EROS [resolved_by:: INS]
- EROS [resolved_by:: MOD]
- EROS [resolved_by:: OVH]
- EROS [resolved_by:: REP]
- EROS [resolved_by:: RPL]
- EXIN [resolved_by:: CHK]
- EXIN [resolved_by:: COM]
- EXIN [resolved_by:: INS]
- EXIN [resolved_by:: MOD]
- EXIN [resolved_by:: OTR]
- EXIN [resolved_by:: REP]
- EXIN [resolved_by:: RPL]
- FATG [resolved_by:: CHK]
- FATG [resolved_by:: COM]
- FATG [resolved_by:: INS]
- FATG [resolved_by:: MOD]
- FATG [resolved_by:: REP]
- FATG [resolved_by:: RPL]
- FPWR [resolved_by:: ADJ]
- FPWR [resolved_by:: CHK]
- FPWR [resolved_by:: REP]
- FPWR [resolved_by:: RPL]
- FPWR [resolved_by:: TST]
- FSIG [resolved_by:: ADJ]
- FSIG [resolved_by:: CHK]
- FSIG [resolved_by:: NFF]
- FSIG [resolved_by:: REF]
- FSIG [resolved_by:: REP]
- FSIG [resolved_by:: RPL]
- FSIG [resolved_by:: TST]
- Instrument failure - general [resolved_by:: ADJ]
- Instrument failure - general [resolved_by:: CHK]
- Instrument failure - general [resolved_by:: COM]
- Instrument failure - general [resolved_by:: NFF]
- Instrument failure - general [resolved_by:: OTR]
- Instrument failure - general [resolved_by:: REP]
- Instrument failure - general [resolved_by:: RPL]
- Instrument failure - general [resolved_by:: TST]
- LEAK [resolved_by:: ADJ]
- LEAK [resolved_by:: CHK]
- LEAK [resolved_by:: COM]
- LEAK [resolved_by:: INS]
- LEAK [resolved_by:: MOD]
- LEAK [resolved_by:: OVH]
- LEAK [resolved_by:: REF]
- LEAK [resolved_by:: REP]
- LEAK [resolved_by:: RPL]
- LEAK [resolved_by:: TST]
- LOOS [resolved_by:: ADJ]
- LOOS [resolved_by:: CHK]
- LOOS [resolved_by:: INS]
- LOOS [resolved_by:: REF]
- LOOS [resolved_by:: REP]
- LOOS [resolved_by:: RPL]
- MATF [resolved_by:: CHK]
- MATF [resolved_by:: COM]
- MATF [resolved_by:: INS]
- MATF [resolved_by:: MOD]
- MATF [resolved_by:: OTR]
- MATF [resolved_by:: REP]
- MATF [resolved_by:: RPL]
- Mechanical Failure - general [resolved_by:: CHK]
- Mechanical Failure - general [resolved_by:: COM]
- Mechanical Failure - general [resolved_by:: INS]
- Mechanical Failure - general [resolved_by:: OTR]
- Mechanical Failure - general [resolved_by:: OVH]
- Mechanical Failure - general [resolved_by:: REP]
- Mechanical Failure - general [resolved_by:: RPL]
- MEXT [resolved_by:: CHK]
- MEXT [resolved_by:: INS]
- MEXT [resolved_by:: MOD]
- MEXT [resolved_by:: REP]
- MEXT [resolved_by:: RPL]
- MEXT [resolved_by:: SVC]
- MISC [resolved_by:: ADJ]
- MISC [resolved_by:: CHK]
- MISC [resolved_by:: OTR]
- MISC [resolved_by:: REP]
- MISC [resolved_by:: RPL]
- MISC [resolved_by:: SVC]
- NCFD [resolved_by:: CHK]
- NCFD [resolved_by:: NFF]
- NCFD [resolved_by:: TST]
- NPWR [resolved_by:: ADJ]
- NPWR [resolved_by:: CHK]
- NPWR [resolved_by:: REP]
- NPWR [resolved_by:: RPL]
- NPWR [resolved_by:: TST]
- NSIG [resolved_by:: CHK]
- NSIG [resolved_by:: REF]
- NSIG [resolved_by:: REP]
- NSIG [resolved_by:: RPL]
- NSIG [resolved_by:: TST]
- OPEN [resolved_by:: CHK]
- OPEN [resolved_by:: REF]
- OPEN [resolved_by:: REP]
- OPEN [resolved_by:: RPL]
- OPEN [resolved_by:: TST]
- OTHR [resolved_by:: CHK]
- OTHR [resolved_by:: COM]
- OTHR [resolved_by:: OTR]
- OTHR [resolved_by:: REP]
- OTHR [resolved_by:: RPL]
- OADJ [resolved_by:: ADJ]
- OADJ [resolved_by:: CHK]
- OADJ [resolved_by:: RPL]
- OADJ [resolved_by:: TST]
- OVHT [resolved_by:: ADJ]
- OVHT [resolved_by:: CHK]
- OVHT [resolved_by:: COM]
- OVHT [resolved_by:: INS]
- OVHT [resolved_by:: MOD]
- OVHT [resolved_by:: OVH]
- OVHT [resolved_by:: REP]
- OVHT [resolved_by:: RPL]
- OVHT [resolved_by:: SVC]
- SHRT [resolved_by:: CHK]
- SHRT [resolved_by:: INS]
- SHRT [resolved_by:: REP]
- SHRT [resolved_by:: RPL]
- SHRT [resolved_by:: TST]
- SWFL [resolved_by:: ADJ]
- SWFL [resolved_by:: CHK]
- SWFL [resolved_by:: MOD]
- SWFL [resolved_by:: RPL]
- SWFL [resolved_by:: TST]
- STCK [resolved_by:: ADJ]
- STCK [resolved_by:: CHK]
- STCK [resolved_by:: COM]
- STCK [resolved_by:: OVH]
- STCK [resolved_by:: REP]
- STCK [resolved_by:: RPL]
- STCK [resolved_by:: SVC]
- STCK [resolved_by:: TST]
- UNKN [resolved_by:: CHK]
- UNKN [resolved_by:: INS]
- UNKN [resolved_by:: NFF]
- UNKN [resolved_by:: OTR]
- VIBR [resolved_by:: ADJ]
- VIBR [resolved_by:: CHK]
- VIBR [resolved_by:: COM]
- VIBR [resolved_by:: INS]
- VIBR [resolved_by:: MOD]
- VIBR [resolved_by:: OVH]
- VIBR [resolved_by:: REF]
- VIBR [resolved_by:: REP]
- VIBR [resolved_by:: RPL]
- WEAR [resolved_by:: ADJ]
- WEAR [resolved_by:: CHK]
- WEAR [resolved_by:: COM]
- WEAR [resolved_by:: INS]
- WEAR [resolved_by:: MOD]
- WEAR [resolved_by:: OVH]
- WEAR [resolved_by:: REP]
- WEAR [resolved_by:: RPL]
- WEAR [resolved_by:: SVC]
- BLKG [has_value:: 6] number of allowed resolutions in matrix
- BRKG [has_value:: 7] number of allowed resolutions in matrix
- BRST [has_value:: 6] number of allowed resolutions in matrix
- CAVT [has_value:: 7] number of allowed resolutions in matrix
- ALGN [has_value:: 8] number of allowed resolutions in matrix
- Combined causes [has_value:: 6] number of allowed resolutions in matrix
- CTMN [has_value:: 5] number of allowed resolutions in matrix
- CTRL [has_value:: 6] number of allowed resolutions in matrix
- CORR [has_value:: 7] number of allowed resolutions in matrix
- DEFM [has_value:: 6] number of allowed resolutions in matrix
- EART [has_value:: 6] number of allowed resolutions in matrix
- ELEC [has_value:: 6] number of allowed resolutions in matrix
- EROS [has_value:: 6] number of allowed resolutions in matrix
- EXIN [has_value:: 7] number of allowed resolutions in matrix
- FATG [has_value:: 6] number of allowed resolutions in matrix
- FPWR [has_value:: 5] number of allowed resolutions in matrix
- FSIG [has_value:: 7] number of allowed resolutions in matrix
- Instrument failure - general [has_value:: 8] number of allowed resolutions in matrix
- LEAK [has_value:: 10] number of allowed resolutions in matrix
- LOOS [has_value:: 6] number of allowed resolutions in matrix
- MATF [has_value:: 7] number of allowed resolutions in matrix
- Mechanical Failure - general [has_value:: 7] number of allowed resolutions in matrix
- MEXT [has_value:: 6] number of allowed resolutions in matrix
- MISC [has_value:: 6] number of allowed resolutions in matrix
- NCFD [has_value:: 3] number of allowed resolutions in matrix
- NPWR [has_value:: 5] number of allowed resolutions in matrix
- NSIG [has_value:: 5] number of allowed resolutions in matrix
- OPEN [has_value:: 5] number of allowed resolutions in matrix
- OTHR [has_value:: 5] number of allowed resolutions in matrix
- OADJ [has_value:: 4] number of allowed resolutions in matrix
- OVHT [has_value:: 9] number of allowed resolutions in matrix
- SHRT [has_value:: 5] number of allowed resolutions in matrix
- SWFL [has_value:: 5] number of allowed resolutions in matrix
- STCK [has_value:: 8] number of allowed resolutions in matrix
- UNKN [has_value:: 4] number of allowed resolutions in matrix
- VIBR [has_value:: 9] number of allowed resolutions in matrix
- WEAR [has_value:: 9] number of allowed resolutions in matrix
- [[Resolution Matrix by Mechanism]] [has_value:: 233] allowed mechanism x resolution pairs of 481 possible (37 x 13) (Notes item 7)
- LEAK [has_value:: 10] most allowed resolutions (max)
- NCFD [has_value:: 3] fewest allowed resolutions (min)
- CHG [differs_from:: [[Resolution Matrix by Mechanism]]] not present in matrix; see conflict at Resolution Codes
- CHK [applies_to:: [[Failure Mechanism]]] allowed for all 37 of 37 mechanisms
- OVH [applies_to:: [[Failure Mechanism]]] degrading mechanical mechanisms (Wear, Erosion, Cavitation, Breakage, Overheating, Vibration etc.)
- [[Resolution Matrix by Mechanism]] [defined_in:: compressor-failure-hierarchy.md] dataset author's engineering judgement, not OREDA data

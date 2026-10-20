---
title: Resolution Matrix by Mechanism
created: 2026-10-20
updated: 2026-10-20
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

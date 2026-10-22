---
title: Compressor Type Failure Profiles
created: 2026-10-20
updated: 2026-10-22
type: comparison
tags: [comparison, centrifugal, reciprocating, screw, failure-mode, failure-rate]
sources: [compressor-failure-hierarchy__summary-by-failure-mode.csv, failure-structure.md, failure-structure__sheet1.csv, compressor-centrifugal-failure-mode-vs-item-2.png, compressor-reciprocating-failure-mode-vs-item-2.png, compressor-screw-failure-mode-vs-item-2.png]
confidence: medium
contested: false
---

# Centrifugal vs Reciprocating vs Screw - failure profiles

เปรียบเทียบสัดส่วน failure mode ของ [[Centrifugal Compressor]], [[Reciprocating Compressor]] และ [[Screw Compressor]] เทียบกับค่าทุกประเภทรวมของ [[Compressor]]

## หมายเหตุเรื่องฐานของตัวเลข (สำคัญ)

- คอลัมน์ **All** = % ของ total failure rate ทุกประเภทรวม (รวมกัน 85.66 เพราะตัด placeholder item)
- คอลัมน์ Centrifugal / Reciprocating / Screw = Total ของแต่ละโหมดจากภาพ OREDA แต่ละประเภท แต่ละประเภทรวมกัน **100%** (รวม item Unknown/Subunit/Other)
- ดังนั้นห้ามนำ All ไปเทียบตรง ๆ กับสามคอลัมน์ที่เหลือ (ฐานต่างกัน) และห้ามเฉลี่ยประเภทเพื่อให้ได้ All เพราะไม่มีสัดส่วน population ใน sources
- ค่าต่อประเภทอ่านจากภาพ (confidence medium)

## ตารางเปรียบเทียบ 19 โหมด

| Mode | All | Centrifugal | Reciprocating | Screw |
|---|---|---|---|---|
| AIR | 17.18 | 27.52 | 9.22 | 22.68 |
| SER | 13.05 | 6.77 | 21.97 | 10.65 |
| LOO | 10.11 | 1.66 | 21.60 | 5.84 |
| ELU | 8.62 | 17.54 | 4.28 | 13.75 |
| PDE | 8.13 | 2.55 | 12.38 | 13.40 |
| OTH | 5.46 | 13.76 | 1.02 | 5.50 |
| ELP | 4.58 | 2.66 | 7.82 | 2.75 |
| OHE | 4.18 | 0.67 | 8.85 | 2.41 |
| UST | 4.16 | 6.66 | 2.79 | 11.68 |
| FTS | 2.35 | 5.55 | 1.12 | 4.12 |
| INL | 1.97 | 6.99 | 0.19 | 0.34 |
| ERO | 1.50 | 1.78 | 1.12 | 3.09 |
| VIB | 1.42 | 2.66 | 1.77 | 0.00 |
| UNK | 1.07 | 0.44 | 3.26 | 1.37 |
| STD | 0.81 | 0.55 | 1.49 | 1.72 |
| NOI | 0.44 | 0.89 | 0.56 | 0.69 |
| STP | 0.34 | 0.44 | 0.37 | 0.00 |
| HIO | 0.21 | 0.55 | 0.00 | 0.00 |
| BRD | 0.08 | 0.33 | 0.19 | 0.00 |

รายละเอียดโหมด: [[Failure Mode]]

## ข้อสังเกต

1. **Centrifugal**: ถูกครอบงำโดยโหมดสัญญาณ/รั่วของ utility (AIR 27.52, ELU 17.54) และ OTH สูง (13.76) และ INL สูง (6.99 เทียบ 0.19 ใน reciprocating) item เด่นคือ Valves, Instruments และ Antisurge system (5.11)
2. **Reciprocating**: ครอบงำโดย SER (21.97) และ LOO (21.60) ซึ่งมาจาก Filter(s) และ Cylinder liner/Valves ตามลำดับ OHE สูง (8.85) จาก Cylinder liner (7.17) Cylinder liner เดียวคิด 28.77 ของ reciprocating
3. **Screw**: AIR 22.68, ELU 13.75, PDE 13.40, UST 11.68 item เด่นคือ Valves (18.04) และ Instruments (temperature 13.75, pressure 9.97) VIB, STP, BRD, HIO เป็น 0.00 ใน data
4. **LOO** ต่างกันมากที่สุด: reciprocating 21.60 เทียบ centrifugal 1.66 (สัดส่วน ~13 เท่า derived) สอดคล้องกับ wear ของ cylinder/valve ที่เป็นลักษณะเฉพาะของ reciprocating ดู [[LOO Low Output]]
5. **AIR** ต่ำใน reciprocating (9.22) แต่สูงใน centrifugal และ screw ดู [[AIR Abnormal Instrument Reading]]

## Maintainable item เด่นต่อประเภท (Sum ทุกโหมด)

| ลำดับ | Centrifugal | Reciprocating | Screw |
|---|---|---|---|
| 1 | Unknown 11.10 | Cylinder liner 28.77 | Valves 18.04 |
| 2 | Valves 10.43 | Filter(s) 14.80 | Instrument, temperature 13.75 |
| 3 | Instrument, temperature 8.53 | Valves 10.94 | Instrument, pressure 9.97 |
| 4 | Instrument, pressure 8.31 | Unknown 5.03 | Subunit 6.53 |
| 5 | Instrument, level 7.55 | Pump w/motor 4.56 | Unknown 5.50 |
| 6 | Antisurge system 5.11 | Instrument, pressure 4.19 | Filter(s) 4.41 |

ผลรวม Instruments ทุก type (derived): centrifugal 31.87, reciprocating 14.81, screw 28.87

## ข้อจำกัด

- ภาพ failure descriptor ของแต่ละประเภทครอบคลุมเฉพาะโหมด AIR ถึง NOI ("to be continued") ส่วนที่เหลือไม่มีใน sources
- จำนวนเหตุการณ์/population ไม่มีใน sources; screw มีขั้น % ละเอียดสุด 0.34 (บ่งชี้ตัวอย่างน้อย) ดู [[Screw Compressor]]
- `failure-structure.md` ให้เพียงโครงสร้าง (คู่ mode/item/sub unit/descriptor: centrifugal 1,810 แถว, reciprocating 732, screw 512) ไม่มี % จึงใช้เปรียบเทียบ "ความหลากหลายของโครงสร้าง" ได้เท่านั้น

## Triplets

- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 17.18%] all compressor types (base 85.66)
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 27.52%] within [[Centrifugal Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 9.22%] within [[Reciprocating Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 22.68%] within [[Screw Compressor]]
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 13.05%] all compressor types (base 85.66)
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 6.77%] within [[Centrifugal Compressor]]
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 21.97%] within [[Reciprocating Compressor]]
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 10.65%] within [[Screw Compressor]]
- [[LOO Low Output]] [has_failure_rate_share:: 10.11%] all compressor types (base 85.66)
- [[LOO Low Output]] [has_failure_rate_share:: 1.66%] within [[Centrifugal Compressor]]
- [[LOO Low Output]] [has_failure_rate_share:: 21.60%] within [[Reciprocating Compressor]]
- [[LOO Low Output]] [has_failure_rate_share:: 5.84%] within [[Screw Compressor]]
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 8.62%] all compressor types (base 85.66)
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 17.54%] within [[Centrifugal Compressor]]
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 4.28%] within [[Reciprocating Compressor]]
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 13.75%] within [[Screw Compressor]]
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 8.13%] all compressor types (base 85.66)
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 2.55%] within [[Centrifugal Compressor]]
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 12.38%] within [[Reciprocating Compressor]]
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 13.40%] within [[Screw Compressor]]
- [[OTH Other]] [has_failure_rate_share:: 5.46%] all compressor types (base 85.66)
- [[OTH Other]] [has_failure_rate_share:: 13.76%] within [[Centrifugal Compressor]]
- [[OTH Other]] [has_failure_rate_share:: 1.02%] within [[Reciprocating Compressor]]
- [[OTH Other]] [has_failure_rate_share:: 5.50%] within [[Screw Compressor]]
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 4.58%] all compressor types (base 85.66)
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 2.66%] within [[Centrifugal Compressor]]
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 7.82%] within [[Reciprocating Compressor]]
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 2.75%] within [[Screw Compressor]]
- [[OHE Overheating]] [has_failure_rate_share:: 4.18%] all compressor types (base 85.66)
- [[OHE Overheating]] [has_failure_rate_share:: 0.67%] within [[Centrifugal Compressor]]
- [[OHE Overheating]] [has_failure_rate_share:: 8.85%] within [[Reciprocating Compressor]]
- [[OHE Overheating]] [has_failure_rate_share:: 2.41%] within [[Screw Compressor]]
- [[UST Spurious Stop]] [has_failure_rate_share:: 4.16%] all compressor types (base 85.66)
- [[UST Spurious Stop]] [has_failure_rate_share:: 6.66%] within [[Centrifugal Compressor]]
- [[UST Spurious Stop]] [has_failure_rate_share:: 2.79%] within [[Reciprocating Compressor]]
- [[UST Spurious Stop]] [has_failure_rate_share:: 11.68%] within [[Screw Compressor]]
- FTS [has_failure_rate_share:: 2.35%] all compressor types (base 85.66)
- FTS [has_failure_rate_share:: 5.55%] within [[Centrifugal Compressor]]
- FTS [has_failure_rate_share:: 1.12%] within [[Reciprocating Compressor]]
- FTS [has_failure_rate_share:: 4.12%] within [[Screw Compressor]]
- INL [has_failure_rate_share:: 1.97%] all compressor types (base 85.66)
- INL [has_failure_rate_share:: 6.99%] within [[Centrifugal Compressor]]
- INL [has_failure_rate_share:: 0.19%] within [[Reciprocating Compressor]]
- INL [has_failure_rate_share:: 0.34%] within [[Screw Compressor]]
- ERO [has_failure_rate_share:: 1.50%] all compressor types (base 85.66)
- ERO [has_failure_rate_share:: 1.78%] within [[Centrifugal Compressor]]
- ERO [has_failure_rate_share:: 1.12%] within [[Reciprocating Compressor]]
- ERO [has_failure_rate_share:: 3.09%] within [[Screw Compressor]]
- VIB [has_failure_rate_share:: 1.42%] all compressor types (base 85.66)
- VIB [has_failure_rate_share:: 2.66%] within [[Centrifugal Compressor]]
- VIB [has_failure_rate_share:: 1.77%] within [[Reciprocating Compressor]]
- VIB [has_failure_rate_share:: 0.00%] within [[Screw Compressor]]
- UNK [has_failure_rate_share:: 1.07%] all compressor types (base 85.66)
- UNK [has_failure_rate_share:: 0.44%] within [[Centrifugal Compressor]]
- UNK [has_failure_rate_share:: 3.26%] within [[Reciprocating Compressor]]
- UNK [has_failure_rate_share:: 1.37%] within [[Screw Compressor]]
- STD [has_failure_rate_share:: 0.81%] all compressor types (base 85.66)
- STD [has_failure_rate_share:: 0.55%] within [[Centrifugal Compressor]]
- STD [has_failure_rate_share:: 1.49%] within [[Reciprocating Compressor]]
- STD [has_failure_rate_share:: 1.72%] within [[Screw Compressor]]
- NOI [has_failure_rate_share:: 0.44%] all compressor types (base 85.66)
- NOI [has_failure_rate_share:: 0.89%] within [[Centrifugal Compressor]]
- NOI [has_failure_rate_share:: 0.56%] within [[Reciprocating Compressor]]
- NOI [has_failure_rate_share:: 0.69%] within [[Screw Compressor]]
- STP [has_failure_rate_share:: 0.34%] all compressor types (base 85.66)
- STP [has_failure_rate_share:: 0.44%] within [[Centrifugal Compressor]]
- STP [has_failure_rate_share:: 0.37%] within [[Reciprocating Compressor]]
- STP [has_failure_rate_share:: 0.00%] within [[Screw Compressor]]
- HIO [has_failure_rate_share:: 0.21%] all compressor types (base 85.66)
- HIO [has_failure_rate_share:: 0.55%] within [[Centrifugal Compressor]]
- HIO [has_failure_rate_share:: 0.00%] within [[Reciprocating Compressor]]
- HIO [has_failure_rate_share:: 0.00%] within [[Screw Compressor]]
- BRD [has_failure_rate_share:: 0.08%] all compressor types (base 85.66)
- BRD [has_failure_rate_share:: 0.33%] within [[Centrifugal Compressor]]
- BRD [has_failure_rate_share:: 0.19%] within [[Reciprocating Compressor]]
- BRD [has_failure_rate_share:: 0.00%] within [[Screw Compressor]]
- [[Compressor]] [has_value:: 85.66%] sum of All column (placeholder items excluded)
- [[AIR Abnormal Instrument Reading]] [dominant_in:: [[Centrifugal Compressor]]] 27.52%
- [[ELU External Leakage Utility Medium]] [dominant_in:: [[Centrifugal Compressor]]] 17.54%
- [[OTH Other]] [dominant_in:: [[Centrifugal Compressor]]] 13.76%
- INL [dominant_in:: [[Centrifugal Compressor]]] 6.99% vs 0.19% in reciprocating
- [[SER Minor In-Service Problems]] [dominant_in:: [[Reciprocating Compressor]]] 21.97%, mainly from Filter(s)
- [[LOO Low Output]] [dominant_in:: [[Reciprocating Compressor]]] 21.60%, mainly from Cylinder liner/Valves
- [[OHE Overheating]] [dominant_in:: [[Reciprocating Compressor]]] 8.85%
- [[AIR Abnormal Instrument Reading]] [dominant_in:: [[Screw Compressor]]] 22.68%
- [[ELU External Leakage Utility Medium]] [dominant_in:: [[Screw Compressor]]] 13.75%
- [[PDE Parameter Deviation]] [dominant_in:: [[Screw Compressor]]] 13.40%
- [[UST Spurious Stop]] [dominant_in:: [[Screw Compressor]]] 11.68%
- FILT [contributes_to:: [[SER Minor In-Service Problems]]] main source of SER within [[Reciprocating Compressor]]
- CYLN [contributes_to:: [[LOO Low Output]]] main source of LOO within [[Reciprocating Compressor]] (with Valves)
- VALV [contributes_to:: [[LOO Low Output]]] main source of LOO within [[Reciprocating Compressor]] (with Cylinder liner)
- CYLN [contributes_to:: [[OHE Overheating]]] 7.17% within [[Reciprocating Compressor]]
- [[LOO Low Output]] [has_value:: ~13x] reciprocating 21.60 vs centrifugal 1.66 share ratio (derived); largest difference between types
- [[LOO Low Output]] [has_mechanism:: WEAR] cylinder/valve wear characteristic of reciprocating (consistent with, interpretation)
- [[AIR Abnormal Instrument Reading]] [has_value:: 9.22%] low within [[Reciprocating Compressor]] vs high in centrifugal and screw
- VALV [dominant_in:: [[Centrifugal Compressor]]] dominant item with Instruments and Antisurge system
- ASRG [has_failure_rate_share:: 5.11%] within [[Centrifugal Compressor]], item rank 6 (sum all modes)
- VALV [has_failure_rate_share:: 10.43%] within [[Centrifugal Compressor]], item rank 2 (sum all modes)
- Instrument Temperature [has_failure_rate_share:: 8.53%] within [[Centrifugal Compressor]], item rank 3 (sum all modes)
- Instrument Pressure [has_failure_rate_share:: 8.31%] within [[Centrifugal Compressor]], item rank 4 (sum all modes)
- Instrument Level [has_failure_rate_share:: 7.55%] within [[Centrifugal Compressor]], item rank 5 (sum all modes)
- CYLN [dominant_in:: [[Reciprocating Compressor]]] item rank 1, 28.77% of reciprocating
- CYLN [has_failure_rate_share:: 28.77%] within [[Reciprocating Compressor]], item rank 1 (sum all modes)
- FILT [has_failure_rate_share:: 14.80%] within [[Reciprocating Compressor]], item rank 2 (sum all modes)
- VALV [has_failure_rate_share:: 10.94%] within [[Reciprocating Compressor]], item rank 3 (sum all modes)
- PMTR [has_failure_rate_share:: 4.56%] within [[Reciprocating Compressor]], item rank 5 (sum all modes)
- Instrument Pressure [has_failure_rate_share:: 4.19%] within [[Reciprocating Compressor]], item rank 6 (sum all modes)
- VALV [dominant_in:: [[Screw Compressor]]] item rank 1, 18.04%
- VALV [has_failure_rate_share:: 18.04%] within [[Screw Compressor]], item rank 1 (sum all modes)
- Instrument Temperature [has_failure_rate_share:: 13.75%] within [[Screw Compressor]], item rank 2 (sum all modes)
- Instrument Pressure [has_failure_rate_share:: 9.97%] within [[Screw Compressor]], item rank 3 (sum all modes)
- FILT [has_failure_rate_share:: 4.41%] within [[Screw Compressor]], item rank 6 (sum all modes)
- INST [has_failure_rate_share:: 31.87%] within [[Centrifugal Compressor]], sum of all instrument types (derived)
- INST [has_failure_rate_share:: 14.81%] within [[Reciprocating Compressor]], sum of all instrument types (derived)
- INST [has_failure_rate_share:: 28.87%] within [[Screw Compressor]], sum of all instrument types (derived)
- [[Centrifugal Compressor]] [has_value:: 1810] mode/item/sub unit/descriptor rows in failure-structure.md (no %)
- [[Reciprocating Compressor]] [has_value:: 732] mode/item/sub unit/descriptor rows in failure-structure.md (no %)
- [[Screw Compressor]] [has_value:: 512] mode/item/sub unit/descriptor rows in failure-structure.md (no %)
- [[Screw Compressor]] [has_value:: 0.34%] finest % step in data, suggests small sample

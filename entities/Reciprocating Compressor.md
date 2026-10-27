---
title: Reciprocating Compressor
created: 2026-10-20
updated: 2026-10-27
type: entity
tags: [compressor, reciprocating, oreda, failure-rate, spare-parts, spo]
sources: [failure-structure.md, failure-structure__sheet1.csv, compressor-reciprocating-failure-descriptor.png, compressor-reciprocating-failure-mode-vs-item-1.png, compressor-reciprocating-failure-mode-vs-item-2.png, spare-parts-optimization.md]
confidence: medium
contested: false
---

# Reciprocating Compressor

[[Compressor]] แบบ reciprocating ตัวเลขอ่านจากภาพตาราง OREDA (confidence medium) ฐานคือ % ของ failure rate **เฉพาะ reciprocating** (รวม 100.0)

## % ต่อ failure mode (Total ของแต่ละโหมด)

| Mode | % | Mode | % |
|---|---|---|---|
| SER | 21.97 | LOO | 21.60 |
| PDE | 12.38 | AIR | 9.22 |
| OHE | 8.85 | ELP | 7.82 |
| ELU | 4.28 | UNK | 3.26 |
| UST | 2.79 | VIB | 1.77 |
| STD | 1.49 | ERO | 1.12 |
| FTS | 1.12 | OTH | 1.02 |
| NOI | 0.56 | STP | 0.37 |
| BRD | 0.19 | INL | 0.19 |
| HIO | 0.00 | | |

ผลรวมบวกได้ 100.00 โหมดเด่น: [[SER Minor In-Service Problems]], [[LOO Low Output]], [[PDE Parameter Deviation]], [[OHE Overheating]]

## Maintainable item ที่เด่น (Sum ทุกโหมด)

Cylinder liner **28.77**, Filter(s) **14.80**, Valves 10.94, Unknown 5.03, Pump w/motor 4.56, Instrument pressure 4.19, Instrument temperature 3.96, Other 3.54, Subunit 3.26, Control unit 2.51, Instrument vibration 2.47, Base frame 2.14

- Cylinder liner: LOO 12.20, OHE 7.17, ELP 4.10, ELU 1.30, PDE 1.21
- Filter(s): SER 14.25 (เกือบทั้งหมดของ Filter(s))
- Instruments ทั้ง 7 type รวม = 14.81 (derived) ต่ำกว่า centrifugal/screw มาก

ค่าเหล่านี้สอดคล้องกับ dataset หลักที่ Cylinder liner (13.66 derived), Filter(s) (8.95) และ Valves (11.64) เป็น item เด่นของทุกประเภทรวม ดู [[CPUN Compressor Unit]] และ [[LUBS Lubrication System]]

## Failure descriptor (10 โหมดแรก ตามภาพ)

- LOO: Mechanical Failure - general **18.62**, Unknown 1.40
- ELP: Mechanical Failure - general 6.70
- AIR: Instrument failure - general 6.52
- ELU: Mechanical Failure - general 2.33
- ภาพครอบคลุมเฉพาะโหมด AIR ถึง NOI

ข้อสังเกต: reciprocating ใช้ descriptor "Mechanical Failure - general" สูงมาก ขณะที่ dataset หลักไม่มี mechanism นี้ในแถวใดเลย ดู [[Failure Mechanism]]

## โครงสร้างใน failure-structure.md

Sheet1 ระบุคู่ mode/item/sub unit/descriptor ของ reciprocating 732 แถว (โครงสร้างความเป็นไปได้) เปรียบเทียบที่ [[Compressor Type Failure Profiles]]

## อะไหล่แนะนำ (SPO)

ตัวอย่างแบบบริษัทญี่ปุ่นใน [[Spare Parts Optimization Book]] (% ของจำนวนชิ้นที่ติดตั้ง ตีความ) รายละเอียดเต็มที่ [[Spare Parts Recommendation by Equipment Type]]

- ชิ้นส่วนวาล์วได้ % สูงสุด: valve plate, valve spring, valve cover gasket, valve seat/guard gasket **400%**; suction/discharge valve assembly 100% (SPO p.52-53)
- Rod packing element ทุก stage 200%, packing case 100%, piston ring 100%, rider ring 200% (non-lube) (SPO p.52-53)
- Running gear สำรองเป็นชุด: main bearings, crank pin bearings, crosshead bearings, crosshead shoe อย่างละ 1 set (2 pcs.); big end bolt 50% (min.4) (SPO p.52-53)
- การตีความของ wiki: Valves (10.94% ของ failure rate) สอดคล้องกับ % สำรองสูงสุด แต่ Cylinder liner (28.77%) และ Filter(s) (14.80%) ไม่อยู่ในรายการอะไหล่ reciprocating ของ SPO

## Triplets

- [[Reciprocating Compressor]] [is_a:: [[Compressor]]]
- [[Reciprocating Compressor]] [has_failure_rate_share:: 100.00%] sum of modes within reciprocating
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 21.97%] within [[Reciprocating Compressor]]
- [[LOO Low Output]] [has_failure_rate_share:: 21.60%] within [[Reciprocating Compressor]]
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 12.38%] within [[Reciprocating Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 9.22%] within [[Reciprocating Compressor]]
- [[OHE Overheating]] [has_failure_rate_share:: 8.85%] within [[Reciprocating Compressor]]
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 7.82%] within [[Reciprocating Compressor]]
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 4.28%] within [[Reciprocating Compressor]]
- UNK [has_failure_rate_share:: 3.26%] within [[Reciprocating Compressor]]
- [[UST Spurious Stop]] [has_failure_rate_share:: 2.79%] within [[Reciprocating Compressor]]
- VIB [has_failure_rate_share:: 1.77%] within [[Reciprocating Compressor]]
- STD [has_failure_rate_share:: 1.49%] within [[Reciprocating Compressor]]
- ERO [has_failure_rate_share:: 1.12%] within [[Reciprocating Compressor]]
- FTS [has_failure_rate_share:: 1.12%] within [[Reciprocating Compressor]]
- [[OTH Other]] [has_failure_rate_share:: 1.02%] within [[Reciprocating Compressor]]
- NOI [has_failure_rate_share:: 0.56%] within [[Reciprocating Compressor]]
- STP [has_failure_rate_share:: 0.37%] within [[Reciprocating Compressor]]
- BRD [has_failure_rate_share:: 0.19%] within [[Reciprocating Compressor]]
- INL [has_failure_rate_share:: 0.19%] within [[Reciprocating Compressor]]
- HIO [has_failure_rate_share:: 0.00%] within [[Reciprocating Compressor]]
- [[SER Minor In-Service Problems]] [dominant_in:: [[Reciprocating Compressor]]]
- [[LOO Low Output]] [dominant_in:: [[Reciprocating Compressor]]]
- [[PDE Parameter Deviation]] [dominant_in:: [[Reciprocating Compressor]]]
- [[OHE Overheating]] [dominant_in:: [[Reciprocating Compressor]]]
- CYLN [has_failure_rate_share:: 28.77%] within [[Reciprocating Compressor]], all modes
- FILT [has_failure_rate_share:: 14.80%] within [[Reciprocating Compressor]], all modes
- VALV [has_failure_rate_share:: 10.94%] within [[Reciprocating Compressor]]
- Unknown [has_failure_rate_share:: 5.03%] placeholder item, within [[Reciprocating Compressor]]
- PMTR [has_failure_rate_share:: 4.56%] within [[Reciprocating Compressor]]
- Instrument Pressure [has_failure_rate_share:: 4.19%] within [[Reciprocating Compressor]]
- Instrument Temperature [has_failure_rate_share:: 3.96%] within [[Reciprocating Compressor]]
- Other [has_failure_rate_share:: 3.54%] placeholder item, within [[Reciprocating Compressor]]
- Subunit [has_failure_rate_share:: 3.26%] placeholder item, within [[Reciprocating Compressor]]
- CTUN [has_failure_rate_share:: 2.51%] within [[Reciprocating Compressor]]
- Instrument Vibration [has_failure_rate_share:: 2.47%] within [[Reciprocating Compressor]]
- BASE [has_failure_rate_share:: 2.14%] within [[Reciprocating Compressor]]
- CYLN [dominant_in:: [[Reciprocating Compressor]]] 28.77%
- FILT [dominant_in:: [[Reciprocating Compressor]]] 14.80%
- CYLN [contributes_to:: [[LOO Low Output]]] 12.20% within [[Reciprocating Compressor]]
- CYLN [contributes_to:: [[OHE Overheating]]] 7.17% within [[Reciprocating Compressor]]
- CYLN [contributes_to:: [[ELP External Leakage Process Medium]]] 4.10% within [[Reciprocating Compressor]]
- CYLN [contributes_to:: [[ELU External Leakage Utility Medium]]] 1.30% within [[Reciprocating Compressor]]
- CYLN [contributes_to:: [[PDE Parameter Deviation]]] 1.21% within [[Reciprocating Compressor]]
- FILT [contributes_to:: [[SER Minor In-Service Problems]]] 14.25% within [[Reciprocating Compressor]], nearly all of Filter(s)
- INST [has_failure_rate_share:: 14.81%] within [[Reciprocating Compressor]], all 7 instrument types (derived), much lower than centrifugal/screw
- CYLN [has_failure_rate_share:: 13.66%] all compressor types, main dataset (derived)
- FILT [has_failure_rate_share:: 8.95%] all compressor types, main dataset (derived)
- VALV [has_failure_rate_share:: 11.64%] all compressor types, main dataset (derived)
- [[LOO Low Output]] [has_mechanism:: Mechanical Failure - general] 18.62% within [[Reciprocating Compressor]]
- [[LOO Low Output]] [has_mechanism:: UNKN] 1.40% within [[Reciprocating Compressor]]
- [[ELP External Leakage Process Medium]] [has_mechanism:: Mechanical Failure - general] 6.70% within [[Reciprocating Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: Instrument failure - general] 6.52% within [[Reciprocating Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: Mechanical Failure - general] 2.33% within [[Reciprocating Compressor]]
- Mechanical Failure - general [has_value:: 0] rows in main dataset, though very high in reciprocating descriptors
- [[Reciprocating Compressor]] [has_value:: 732] rows in failure-structure.md Sheet1 (possible combinations, not events)
- [[OREDA]] [source_of:: [[Reciprocating Compressor]]] per-type table images
- [[Reciprocating Compressor]] [related_to:: [[Spare Parts Recommendation by Equipment Type]]] SPO Japanese example 3.4 (SPO p.52-53)
- Valve Plate [has_value:: 400%] recommended spare, reciprocating compressor (SPO p.52)
- Rod Packing Element [has_value:: 200%] each stage, reciprocating compressor (SPO p.52)
- Main Bearings [has_value:: 1 set (2 pcs.)] reciprocating compressor (SPO p.52)
- VALV [related_to:: Valve Plate] Valves 10.94% aligns with highest SPO spare ratio 400%, wiki interpretation [confidence:: low]

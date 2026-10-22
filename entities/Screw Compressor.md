---
title: Screw Compressor
created: 2026-10-20
updated: 2026-10-22
type: entity
tags: [compressor, screw, oreda, failure-rate]
sources: [failure-structure.md, failure-structure__sheet1.csv, compressor-screw-failure-descriptor.png, compressor-screw-failure-mode-vs-item-1.png, compressor-screw-failure-mode-vs-item-2.png]
confidence: medium
contested: false
---

# Screw Compressor

[[Compressor]] แบบ screw ตัวเลขอ่านจากภาพตาราง OREDA (confidence medium) ฐานคือ % ของ failure rate **เฉพาะ screw** (รวม 100.0)

## % ต่อ failure mode (Total ของแต่ละโหมด)

| Mode | % | Mode | % |
|---|---|---|---|
| AIR | 22.68 | ELU | 13.75 |
| PDE | 13.40 | UST | 11.68 |
| SER | 10.65 | LOO | 5.84 |
| OTH | 5.50 | FTS | 4.12 |
| ERO | 3.09 | ELP | 2.75 |
| OHE | 2.41 | STD | 1.72 |
| UNK | 1.37 | NOI | 0.69 |
| INL | 0.34 | BRD | 0.00 |
| HIO | 0.00 | STP | 0.00 |
| VIB | 0.00 | | |

ผลรวมบวกได้ 99.99 (ปัดเศษ) โหมดเด่น: [[AIR Abnormal Instrument Reading]], [[ELU External Leakage Utility Medium]], [[PDE Parameter Deviation]], [[UST Spurious Stop]]

## Maintainable item ที่เด่น (Sum ทุกโหมด)

Valves **18.04**, Instrument temperature 13.75, Instrument pressure 9.97, Subunit 6.53, Unknown 5.50, Filter(s) 4.41, Other 4.12, Shaft seals 4.12, Piping 3.89, Purge air 3.78, Pump w/motor 3.26, Control unit 2.41, Cooler(s) 2.35

Instruments ทั้ง 7 type รวม = 28.87 (derived) เป็นกลุ่มใหญ่ที่สุดร่วมกับ Valves

## Failure descriptor (10 โหมดแรก ตามภาพ)

- AIR: Instrument failure - general **12.03**, Out of adjustment 3.09
- ELU: Mechanical Failure - general 6.87, Leakage 3.44
- ELP: Leakage 1.37
- ภาพครอบคลุมเฉพาะโหมด AIR ถึง NOI

## ข้อควรระวังเรื่องความน่าเชื่อถือทางสถิติ (inference, confidence ต่ำ)

ค่า % ใน screw มีขั้นละเอียดเล็กสุด 0.34 (เช่น 0.34, 0.69, 1.03, 1.37) ขณะที่ reciprocating เล็กสุด 0.09 และ centrifugal 0.11 ซึ่งบ่งชี้ว่าจำนวนเหตุการณ์ของ screw ใน OREDA น้อยกว่ามาก (ข้อสรุปจากรูปแบบตัวเลข sources ไม่ระบุจำนวนเหตุการณ์) จึงควรระวังการสรุปจากรายการเล็ก ๆ

## โครงสร้างใน failure-structure.md

Sheet1 ระบุคู่ mode/item/sub unit/descriptor ของ screw 512 แถว (โครงสร้างความเป็นไปได้) เปรียบเทียบที่ [[Compressor Type Failure Profiles]]

## Triplets

- [[Screw Compressor]] [is_a:: [[Compressor]]]
- [[Screw Compressor]] [has_failure_rate_share:: 100.0%] sum of modes within screw (added 99.99, rounding)
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 22.68%] within [[Screw Compressor]]
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 13.75%] within [[Screw Compressor]]
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 13.40%] within [[Screw Compressor]]
- [[UST Spurious Stop]] [has_failure_rate_share:: 11.68%] within [[Screw Compressor]]
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 10.65%] within [[Screw Compressor]]
- [[LOO Low Output]] [has_failure_rate_share:: 5.84%] within [[Screw Compressor]]
- [[OTH Other]] [has_failure_rate_share:: 5.50%] within [[Screw Compressor]]
- FTS [has_failure_rate_share:: 4.12%] within [[Screw Compressor]]
- ERO [has_failure_rate_share:: 3.09%] within [[Screw Compressor]]
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 2.75%] within [[Screw Compressor]]
- [[OHE Overheating]] [has_failure_rate_share:: 2.41%] within [[Screw Compressor]]
- STD [has_failure_rate_share:: 1.72%] within [[Screw Compressor]]
- UNK [has_failure_rate_share:: 1.37%] within [[Screw Compressor]]
- NOI [has_failure_rate_share:: 0.69%] within [[Screw Compressor]]
- INL [has_failure_rate_share:: 0.34%] within [[Screw Compressor]]
- BRD [has_failure_rate_share:: 0.00%] within [[Screw Compressor]]
- HIO [has_failure_rate_share:: 0.00%] within [[Screw Compressor]]
- STP [has_failure_rate_share:: 0.00%] within [[Screw Compressor]]
- VIB [has_failure_rate_share:: 0.00%] within [[Screw Compressor]]
- [[AIR Abnormal Instrument Reading]] [dominant_in:: [[Screw Compressor]]]
- [[ELU External Leakage Utility Medium]] [dominant_in:: [[Screw Compressor]]]
- [[PDE Parameter Deviation]] [dominant_in:: [[Screw Compressor]]]
- [[UST Spurious Stop]] [dominant_in:: [[Screw Compressor]]]
- VALV [has_failure_rate_share:: 18.04%] within [[Screw Compressor]]
- Instrument Temperature [has_failure_rate_share:: 13.75%] within [[Screw Compressor]]
- Instrument Pressure [has_failure_rate_share:: 9.97%] within [[Screw Compressor]]
- Subunit [has_failure_rate_share:: 6.53%] placeholder item, within [[Screw Compressor]]
- Unknown [has_failure_rate_share:: 5.50%] placeholder item, within [[Screw Compressor]]
- FILT [has_failure_rate_share:: 4.41%] within [[Screw Compressor]]
- Other [has_failure_rate_share:: 4.12%] placeholder item, within [[Screw Compressor]]
- SHSL [has_failure_rate_share:: 4.12%] within [[Screw Compressor]]
- PIPE [has_failure_rate_share:: 3.89%] within [[Screw Compressor]]
- PAIR [has_failure_rate_share:: 3.78%] within [[Screw Compressor]]
- PMTR [has_failure_rate_share:: 3.26%] within [[Screw Compressor]]
- CTUN [has_failure_rate_share:: 2.41%] within [[Screw Compressor]]
- COOL [has_failure_rate_share:: 2.35%] within [[Screw Compressor]]
- INST [has_failure_rate_share:: 28.87%] within [[Screw Compressor]], all 7 instrument types (derived)
- VALV [dominant_in:: [[Screw Compressor]]] 18.04%
- INST [dominant_in:: [[Screw Compressor]]] largest group with Valves
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: Instrument failure - general] 12.03% within [[Screw Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: OADJ] 3.09% within [[Screw Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: Mechanical Failure - general] 6.87% within [[Screw Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: LEAK] 3.44% within [[Screw Compressor]]
- [[ELP External Leakage Process Medium]] [has_mechanism:: LEAK] 1.37% within [[Screw Compressor]]
- [[Screw Compressor]] [has_value:: 0.34%] smallest % step; reciprocating 0.09, centrifugal 0.11; suggests fewer OREDA events (inference) [confidence:: low]
- [[Screw Compressor]] [has_value:: 512] rows in failure-structure.md Sheet1 (possible combinations, not events)
- [[OREDA]] [source_of:: [[Screw Compressor]]] per-type table images

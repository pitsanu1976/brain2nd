---
title: Centrifugal Compressor
created: 2026-10-20
updated: 2026-10-22
type: entity
tags: [compressor, centrifugal, oreda, failure-rate]
sources: [failure-structure.md, failure-structure__sheet1.csv, compressor-centrifugal-failure-descriptor.png, compressor-centrifugal-failure-mode-vs-item-1.png, compressor-centrifugal-failure-mode-vs-item-2.png, compressor-centrifugal-failure-mode-vs-item-3.png, compressor-centrifugal-failure-mode-vs-item-4.png]
confidence: medium
contested: false
---

# Centrifugal Compressor

[[Compressor]] แบบ centrifugal ตัวเลขทั้งหมดอ่านจากภาพตาราง OREDA (confidence medium เพราะเป็นการอ่านภาพ) ฐานคือ % ของ failure rate **เฉพาะ centrifugal** (รวม 100.0)

## % ต่อ failure mode (Total ของแต่ละโหมด)

| Mode | % | Mode | % |
|---|---|---|---|
| AIR | 27.52 | OTH | 13.76 |
| ELU | 17.54 | SER | 6.77 |
| INL | 6.99 | UST | 6.66 |
| FTS | 5.55 | ELP | 2.66 |
| VIB | 2.66 | PDE | 2.55 |
| ERO | 1.78 | LOO | 1.66 |
| NOI | 0.89 | OHE | 0.67 |
| HIO | 0.55 | STD | 0.55 |
| STP | 0.44 | UNK | 0.44 |
| BRD | 0.33 | | |

รวม 100.0 (derived จากการบวกได้ 99.97 ปัดเศษ) โหมดเด่น: [[AIR Abnormal Instrument Reading]] และ [[ELU External Leakage Utility Medium]]

## Maintainable item ที่เด่น (Sum ทุกโหมด)

Unknown 11.10, Valves 10.43, Instrument temperature 8.53, Instrument pressure 8.31, Instrument level 7.55, Antisurge system 5.11, Control unit 4.66, Instrument vibration 4.16, Oil 3.77, Filter(s) 3.44, Pump w/motor/gear 3.44

Instruments ทั้ง 7 type รวม = 31.87 (derived) ใน centrifugal (สอดคล้องกับโหมด AIR ที่สูง) ดู [[Maintainable Item]]

## Failure descriptor (10 โหมดแรก ตามภาพ)

- AIR: Faulty signal/indication/alarm 8.10, Out of adjustment 6.88, Instrument failure - general 4.11, Control failure 1.00
- ELU: Leakage 8.99, Wear 3.11, Mechanical Failure - general 1.44
- INL: Wear 5.88 (จาก INL ทั้งหมด 6.99)
- ELP: Leakage 1.89
- ภาพ descriptor ครอบคลุมเฉพาะโหมด AIR ถึง NOI ("to be continued"); descriptor ของโหมดที่เหลือไม่มีใน sources

## โครงสร้างใน failure-structure.md

Sheet1 ของ `failure-structure.md` ระบุคู่ mode/item/sub unit/descriptor ของ centrifugal จำนวน 1,810 แถว (เป็นโครงสร้างความเป็นไปได้ ไม่ใช่จำนวนเหตุการณ์) ใช้ sub unit ตามที่ระบุใน [[Failure Hierarchy]] (มีข้อขัดแย้งบางรายการกับ dataset หลัก) เปรียบเทียบกับประเภทอื่นที่ [[Compressor Type Failure Profiles]]

## Triplets

- [[Centrifugal Compressor]] [is_a:: [[Compressor]]]
- [[Centrifugal Compressor]] [has_failure_rate_share:: 100.0%] sum of modes within centrifugal (added 99.97, rounding)
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 27.52%] within [[Centrifugal Compressor]]
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 17.54%] within [[Centrifugal Compressor]]
- [[OTH Other]] [has_failure_rate_share:: 13.76%] within [[Centrifugal Compressor]]
- INL [has_failure_rate_share:: 6.99%] within [[Centrifugal Compressor]]
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 6.77%] within [[Centrifugal Compressor]]
- [[UST Spurious Stop]] [has_failure_rate_share:: 6.66%] within [[Centrifugal Compressor]]
- FTS [has_failure_rate_share:: 5.55%] within [[Centrifugal Compressor]]
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 2.66%] within [[Centrifugal Compressor]]
- VIB [has_failure_rate_share:: 2.66%] within [[Centrifugal Compressor]]
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 2.55%] within [[Centrifugal Compressor]]
- ERO [has_failure_rate_share:: 1.78%] within [[Centrifugal Compressor]]
- [[LOO Low Output]] [has_failure_rate_share:: 1.66%] within [[Centrifugal Compressor]]
- NOI [has_failure_rate_share:: 0.89%] within [[Centrifugal Compressor]]
- [[OHE Overheating]] [has_failure_rate_share:: 0.67%] within [[Centrifugal Compressor]]
- HIO [has_failure_rate_share:: 0.55%] within [[Centrifugal Compressor]]
- STD [has_failure_rate_share:: 0.55%] within [[Centrifugal Compressor]]
- STP [has_failure_rate_share:: 0.44%] within [[Centrifugal Compressor]]
- UNK [has_failure_rate_share:: 0.44%] within [[Centrifugal Compressor]]
- BRD [has_failure_rate_share:: 0.33%] within [[Centrifugal Compressor]]
- [[AIR Abnormal Instrument Reading]] [dominant_in:: [[Centrifugal Compressor]]]
- [[ELU External Leakage Utility Medium]] [dominant_in:: [[Centrifugal Compressor]]]
- Unknown [has_failure_rate_share:: 11.10%] placeholder item, within [[Centrifugal Compressor]]
- VALV [has_failure_rate_share:: 10.43%] within [[Centrifugal Compressor]]
- Instrument Temperature [has_failure_rate_share:: 8.53%] within [[Centrifugal Compressor]]
- Instrument Pressure [has_failure_rate_share:: 8.31%] within [[Centrifugal Compressor]]
- Instrument Level [has_failure_rate_share:: 7.55%] within [[Centrifugal Compressor]]
- ASRG [has_failure_rate_share:: 5.11%] within [[Centrifugal Compressor]]
- CTUN [has_failure_rate_share:: 4.66%] within [[Centrifugal Compressor]]
- Instrument Vibration [has_failure_rate_share:: 4.16%] within [[Centrifugal Compressor]]
- OILS [has_failure_rate_share:: 3.77%] within [[Centrifugal Compressor]]
- FILT [has_failure_rate_share:: 3.44%] within [[Centrifugal Compressor]]
- PMGR [has_failure_rate_share:: 3.44%] within [[Centrifugal Compressor]]
- INST [has_failure_rate_share:: 31.87%] within [[Centrifugal Compressor]], all 7 instrument types (derived)
- INST [dominant_in:: [[Centrifugal Compressor]]] consistent with high AIR
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: FSIG] 8.10% within [[Centrifugal Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: OADJ] 6.88% within [[Centrifugal Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: Instrument failure - general] 4.11% within [[Centrifugal Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: CTRL] 1.00% within [[Centrifugal Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: LEAK] 8.99% within [[Centrifugal Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: WEAR] 3.11% within [[Centrifugal Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: Mechanical Failure - general] 1.44% within [[Centrifugal Compressor]]
- INL [has_mechanism:: WEAR] 5.88% of INL 6.99, within [[Centrifugal Compressor]]
- [[ELP External Leakage Process Medium]] [has_mechanism:: LEAK] 1.89% within [[Centrifugal Compressor]]
- [[Centrifugal Compressor]] [has_value:: 1,810] rows in failure-structure.md Sheet1 (possible mode/item/sub unit/descriptor combinations, not events)
- [[OREDA]] [source_of:: [[Centrifugal Compressor]]] per-type table images

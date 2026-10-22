---
title: SER Minor In-Service Problems
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [failure-mode, failure-rate, oreda, compressor]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-reciprocating-failure-mode-vs-item-2.png]
confidence: high
contested: false
---

# SER - Minor in-service problems

โหมดอันดับ 2 ใน [[Failure Mode]]: **13.05%** ของ total failure rate (27 คู่ failure mode/item) ปัญหาเล็กน้อยระหว่างใช้งานที่ไม่ถึงกับหยุด/ลดสมรรถนะชัดเจน

## ตัวขับหลัก (OREDA, ทุกประเภทรวม)

| Maintainable Item | Sub Unit (ที่นับ %) | % | Mechanism ที่แสดงในแถวแรก |
|---|---|---|---|
| Filter(s) | [[LUBS Lubrication System]] | 7.33 | Blockage/plugged (element clogged, high DP) |
| Valves | [[CPUN Compressor Unit]] | 1.13 | Contamination (deposits/fouling on plates) |
| Instruments | [[PWTR Power Transmission]] | 1.02 | Looseness |
| Base frame | [[MISC Miscellaneous]] | 0.88 | Corrosion |
| Cylinder liner | [[CPUN Compressor Unit]] | 0.31 | Wear |
| Internal piping | [[CPUN Compressor Unit]] | 0.26 | Corrosion |

Lube oil filter(s) เพียงตัวเดียวคิดเป็น 7.33 จาก 13.05 (derived: ประมาณ 56%) ค่านี้สอดคล้องกับ reciprocating ที่ Filter(s) x SER = 14.25 (ภาพ OREDA ของ reciprocating)

## แยกตามประเภท compressor (total ของโหมด SER)

| Centrifugal | Reciprocating | Screw |
|---|---|---|
| 6.77 | 21.97 | 10.65 |

ดู [[Compressor Type Failure Profiles]] และ [[Reciprocating Compressor]]

## Resolution ที่ dataset เสนอ

Filter ที่อุดตันจับคู่กับ Check ("investigate contamination source"), Service, Replace; Looseness จับคู่กับ Adjust (tighten/re-torque) ดู [[Resolution Codes]]

## Triplets

- [[SER Minor In-Service Problems]] [is_a:: [[Failure Mode]]]
- [[SER Minor In-Service Problems]] [has_code:: SER]
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 13.05%] all compressor types, rank 2 of 19
- [[SER Minor In-Service Problems]] [has_value:: 27] failure mode/item pairs
- LUBS-FILT [contributes_to:: [[SER Minor In-Service Problems]]] 7.33%; about 56% of SER (derived)
- CPUN-VALV [contributes_to:: [[SER Minor In-Service Problems]]] 1.13%
- PWTR-INST [contributes_to:: [[SER Minor In-Service Problems]]] 1.02%
- MISC-BASE [contributes_to:: [[SER Minor In-Service Problems]]] 0.88%
- CPUN-CYLN [contributes_to:: [[SER Minor In-Service Problems]]] 0.31%
- CPUN-IPIP [contributes_to:: [[SER Minor In-Service Problems]]] 0.26%
- [[SER Minor In-Service Problems]] [has_mechanism:: BLKG] Filter(s), element clogged / high DP (first row)
- [[SER Minor In-Service Problems]] [has_mechanism:: CTMN] Contamination; Valves, deposits/fouling on plates (first row)
- [[SER Minor In-Service Problems]] [has_mechanism:: LOOS] Instruments (first row)
- [[SER Minor In-Service Problems]] [has_mechanism:: CORR] Base frame, Internal piping (first row)
- [[SER Minor In-Service Problems]] [has_mechanism:: WEAR] Cylinder liner (first row)
- FILT [contributes_to:: [[SER Minor In-Service Problems]]] 14.25 within [[Reciprocating Compressor]] (OREDA reciprocating chart)
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 6.77%] within [[Centrifugal Compressor]]
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 21.97%] within [[Reciprocating Compressor]]
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 10.65%] within [[Screw Compressor]]
- [[SER Minor In-Service Problems]] [resolved_by:: CHK] clogged filter; investigate contamination source
- [[SER Minor In-Service Problems]] [resolved_by:: SVC] clogged filter
- [[SER Minor In-Service Problems]] [resolved_by:: RPL] clogged filter
- [[SER Minor In-Service Problems]] [resolved_by:: ADJ] Looseness; tighten/re-torque
- [[SER Minor In-Service Problems]] [defined_in:: [[OREDA]]]

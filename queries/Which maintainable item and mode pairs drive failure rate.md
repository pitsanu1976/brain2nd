---
title: Which maintainable item and mode pairs drive failure rate
created: 2026-10-20
updated: 2026-10-22
type: query
tags: [query, maintainable-item, failure-mode, failure-rate]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv]
confidence: medium
contested: false
---

# Which maintainable item / failure mode pairs drive the failure rate?

## คำตอบสั้น

คู่เดียว **Instruments x AIR = 13.54%** (ประมาณ 15.8% ของ 85.66) ใหญ่ที่สุด ตามด้วย Filter(s) x SER 7.33 และ Cylinder liner x LOO 5.78 สามคู่แรกรวม 26.65 (derived, ประมาณ 31.1%) ห้าคู่แรกรวม 33.40 (ประมาณ 39.0%)

## Top คู่ (ทุกประเภทรวม, แถวที่ `Count in Total = 1`)

| อันดับ | Item | Mode | Sub Unit | % |
|---|---|---|---|---|
| 1 | Instruments | [[AIR Abnormal Instrument Reading]] | [[PWTR Power Transmission]] | 13.54 |
| 2 | Filter(s) | [[SER Minor In-Service Problems]] | [[LUBS Lubrication System]] | 7.33 |
| 3 | Cylinder liner | [[LOO Low Output]] | [[CPUN Compressor Unit]] | 5.78 |
| 4 | Cylinder liner | [[OHE Overheating]] | [[CPUN Compressor Unit]] | 3.40 |
| 5 | Instruments | [[PDE Parameter Deviation]] | [[PWTR Power Transmission]] | 3.35 |
| 6 | Valves | LOO | CPUN | 2.21 |
| 7 | Cylinder liner | ELP | CPUN | 1.94 |
| 8= | Instruments | UST | PWTR | 1.92 |
| 8= | Valves | PDE | CPUN | 1.92 |
| 10 | Valves | OTH | CPUN | 1.37 |

## รวมต่อ item (derived: ผลรวมของแถว Count in Total = 1 ของ item นั้นทุกโหมด)

| Item | % รวม | สัดส่วนของ 85.66 |
|---|---|---|
| Instruments | 23.34 | 27.3% |
| Cylinder liner | 13.66 | 15.9% |
| Valves | 11.64 | 13.6% |
| Filter(s) | 8.95 | 10.4% |

สี่ item นี้รวม 57.59 (ประมาณ 67.2%) รายละเอียดดู [[Maintainable Item]], [[CPUN Compressor Unit]] และ [[LUBS Lubrication System]]

## ข้อควรระวัง

- Instruments มีตัวเลขสูงเพราะเป็นการรวม 7 instrument type เป็น item เดียว (Notes ข้อ 4) และ Sub Unit PWTR เป็นเพียงที่นับ % (ดู [[PWTR Power Transmission]])
- Cylinder liner เด่นเฉพาะ [[Reciprocating Compressor]] (Sum 28.77 ในภาพ reciprocating); ถ้า fleet ไม่มี reciprocating ลำดับจะต่างจากนี้
- Mechanism ที่แสดงมาจากแถวแรกของคู่ ไม่ใช่ทุก mechanism ของคู่นั้น ดู [[Failure Mechanism]]

## Triplets

- PWTR-INST [contributes_to:: [[AIR Abnormal Instrument Reading]]] 13.54% of total failure rate, pair rank 1; about 15.8% of 85.66
- LUBS-FILT [contributes_to:: [[SER Minor In-Service Problems]]] 7.33% of total failure rate, pair rank 2
- CPUN-CYLN [contributes_to:: [[LOO Low Output]]] 5.78% of total failure rate, pair rank 3
- CPUN-CYLN [contributes_to:: [[OHE Overheating]]] 3.40% of total failure rate, pair rank 4
- PWTR-INST [contributes_to:: [[PDE Parameter Deviation]]] 3.35% of total failure rate, pair rank 5
- CPUN-VALV [contributes_to:: [[LOO Low Output]]] 2.21% of total failure rate, pair rank 6
- CPUN-CYLN [contributes_to:: [[ELP External Leakage Process Medium]]] 1.94% of total failure rate, pair rank 7
- PWTR-INST [contributes_to:: [[UST Spurious Stop]]] 1.92% of total failure rate, pair rank 8=
- CPUN-VALV [contributes_to:: [[PDE Parameter Deviation]]] 1.92% of total failure rate, pair rank 8=
- CPUN-VALV [contributes_to:: [[OTH Other]]] 1.37% of total failure rate, pair rank 10
- Top 3 Item/Mode Pairs [has_failure_rate_share:: 26.65%] derived; about 31.1% of 85.66
- Top 5 Item/Mode Pairs [has_failure_rate_share:: 33.40%] about 39.0% of 85.66
- INST [has_failure_rate_share:: 23.34%] sum over all modes (derived); 27.3% of 85.66
- CYLN [has_failure_rate_share:: 13.66%] sum over all modes (derived); 15.9% of 85.66
- VALV [has_failure_rate_share:: 11.64%] sum over all modes (derived); 13.6% of 85.66
- FILT [has_failure_rate_share:: 8.95%] sum over all modes (derived); 10.4% of 85.66
- Top 4 Maintainable Items [has_failure_rate_share:: 57.59%] INST, CYLN, VALV, FILT; about 67.2% of 85.66
- INST [has_value:: 7] instrument types combined into one item (Notes item 4)
- [[PWTR Power Transmission]] [has_part:: PWTR-INST] sub unit used only as counting location for %
- CYLN [dominant_in:: [[Reciprocating Compressor]]] Sum 28.77 in reciprocating figure; ranking differs if fleet has no reciprocating

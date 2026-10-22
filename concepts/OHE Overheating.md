---
title: OHE Overheating
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [failure-mode, failure-rate, oreda, compressor]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-reciprocating-failure-mode-vs-item-2.png]
confidence: high
contested: false
---

# OHE - Overheating

**4.18%** ของ total failure rate (12 คู่ failure mode/item) อันดับ 8 ใน [[Failure Mode]] อุณหภูมิสูงผิดปกติของ item หรือของ process

## ตัวขับหลัก (OREDA, ทุกประเภทรวม)

| Maintainable Item | Sub Unit (ที่นับ %) | % | Mechanism ที่แสดงในแถวแรก |
|---|---|---|---|
| Cylinder liner | [[CPUN Compressor Unit]] | 3.40 | Wear (liner bore wear / scuffing) |
| Valves | [[CPUN Compressor Unit]] | 0.22 | Wear |
| Pump w/motor | [[LUBS Lubrication System]] | 0.11 | Wear (bearing) |
| Instruments | [[PWTR Power Transmission]] | 0.09 | Overheating |
| Internal piping | [[CPUN Compressor Unit]] | 0.09 | Blockage/plugged |
| Cooler(s) | [[LUBS Lubrication System]] | 0.09 | Blockage/plugged (tube fouling) |

Cylinder liner x OHE = 3.40 จาก 4.18 (derived: ประมาณ 81%) ผลรวม 12 คู่ = 4.18 (ตรงกับ summary) ส่วนภาพ reciprocating แสดง Cylinder liner x OHE = 7.17 ซึ่งเป็นคนละฐาน (% ของ failure rate เฉพาะ reciprocating ไม่ใช่ทุกประเภทรวม) ทั้งสองค่าจึงไม่ขัดแย้งกัน

## แยกตามประเภท compressor (total ของโหมด OHE)

| Centrifugal | Reciprocating | Screw |
|---|---|---|
| 0.67 | 8.85 | 2.41 |

OHE เด่นใน [[Reciprocating Compressor]] ดู [[Compressor Type Failure Profiles]] และความสัมพันธ์กับ lubrication/cooling ที่ [[LUBS Lubrication System]]

## Triplets

- [[OHE Overheating]] [is_a:: [[Failure Mode]]]
- [[OHE Overheating]] [has_code:: OHE]
- [[OHE Overheating]] [has_failure_rate_share:: 4.18%] all compressor types, rank 8 of 19
- [[OHE Overheating]] [has_value:: 12] failure mode/item pairs
- CPUN-CYLN [contributes_to:: [[OHE Overheating]]] 3.40%; about 81% of OHE (derived)
- CPUN-VALV [contributes_to:: [[OHE Overheating]]] 0.22%
- LUBS-PMTR [contributes_to:: [[OHE Overheating]]] 0.11%
- PWTR-INST [contributes_to:: [[OHE Overheating]]] 0.09%
- CPUN-IPIP [contributes_to:: [[OHE Overheating]]] 0.09%
- LUBS-COOL [contributes_to:: [[OHE Overheating]]] 0.09%
- [[OHE Overheating]] [has_mechanism:: WEAR] Cylinder liner, Valves, Pump w/motor
- [[OHE Overheating]] [has_mechanism:: BLKG] Internal piping, Cooler(s)
- [[OHE Overheating]] [has_mechanism:: OVHT] Instruments
- [[OHE Overheating]] [has_failure_rate_share:: 0.67%] within [[Centrifugal Compressor]]
- [[OHE Overheating]] [has_failure_rate_share:: 8.85%] within [[Reciprocating Compressor]]
- [[OHE Overheating]] [has_failure_rate_share:: 2.41%] within [[Screw Compressor]]
- [[OHE Overheating]] [dominant_in:: [[Reciprocating Compressor]]]
- [[OHE Overheating]] [related_to:: [[LUBS Lubrication System]]] lubrication/cooling
- [[OHE Overheating]] [defined_in:: [[OREDA]]]

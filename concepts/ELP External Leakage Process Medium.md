---
title: ELP External Leakage Process Medium
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [failure-mode, failure-rate, oreda, compressor]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-reciprocating-failure-descriptor.png, compressor-centrifugal-failure-descriptor.png]
confidence: high
contested: false
---

# ELP - External leakage - Process medium

**4.58%** ของ total failure rate (17 คู่ failure mode/item) อันดับ 7 ใน [[Failure Mode]] การรั่วของ process gas/medium ออกสู่ภายนอก มีนัยด้านความปลอดภัยและสิ่งแวดล้อมมากกว่า % ที่แสดง เปรียบเทียบกับ [[ELU External Leakage Utility Medium]] (utility medium)

## ตัวขับหลัก (OREDA, ทุกประเภทรวม)

| Maintainable Item | Sub Unit (ที่นับ %) | % | Mechanism |
|---|---|---|---|
| Cylinder liner | [[CPUN Compressor Unit]] | 1.94 | Wear (liner bore wear / scuffing) |
| Valves | [[CPUN Compressor Unit]] | 1.24 | Leakage (cover gasket / stem packing) |
| Packing | [[CPUN Compressor Unit]] | 0.22 | Wear (packing ring) |
| Pump w/motor | [[LUBS Lubrication System]] | 0.18 | Leakage (mechanical seal) |
| Piping, pipe support + bellows | [[MISC Miscellaneous]] | 0.18 | Corrosion |
| Seal gas | [[SHSS Shaft Seal System]] | 0.13 | Leakage |

Cylinder liner + Valves = 3.18 (derived: ประมาณ 69% ของ 4.58) ผลรวม 17 คู่ = 4.58

## แยกตามประเภท compressor (total ของโหมด ELP)

| Centrifugal | Reciprocating | Screw |
|---|---|---|
| 2.66 | 7.82 | 2.75 |

Reciprocating: Mechanical Failure - general = 6.70, Cylinder liner = 4.10; centrifugal: Leakage = 1.89; screw: Leakage = 1.37 ดู [[Reciprocating Compressor]] และ [[Compressor Type Failure Profiles]]

## Triplets

- [[ELP External Leakage Process Medium]] [is_a:: [[Failure Mode]]]
- [[ELP External Leakage Process Medium]] [has_code:: ELP]
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 4.58%] all compressor types, rank 7 of 19
- [[ELP External Leakage Process Medium]] [has_value:: 17] failure mode/item pairs
- [[ELP External Leakage Process Medium]] [differs_from:: [[ELU External Leakage Utility Medium]]] process medium vs utility medium
- [[ELP External Leakage Process Medium]] [related_to:: Safety and Environmental Impact] greater significance than the % shows
- CPUN-CYLN [contributes_to:: [[ELP External Leakage Process Medium]]] 1.94%
- CPUN-VALV [contributes_to:: [[ELP External Leakage Process Medium]]] 1.24%
- CPUN-PACK [contributes_to:: [[ELP External Leakage Process Medium]]] 0.22%
- LUBS-PMTR [contributes_to:: [[ELP External Leakage Process Medium]]] 0.18%
- MISC-PSPB [contributes_to:: [[ELP External Leakage Process Medium]]] 0.18%
- SHSS-SGAS [contributes_to:: [[ELP External Leakage Process Medium]]] 0.13%
- [[ELP External Leakage Process Medium]] [has_value:: 3.18%] Cylinder liner + Valves; about 69% of 4.58 (derived)
- [[ELP External Leakage Process Medium]] [has_mechanism:: WEAR] Cylinder liner (bore wear / scuffing), Packing (packing ring)
- [[ELP External Leakage Process Medium]] [has_mechanism:: LEAK] Valves (cover gasket / stem packing), Pump w/motor (mechanical seal), Seal gas
- [[ELP External Leakage Process Medium]] [has_mechanism:: CORR] Piping, pipe support + bellows
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 2.66%] within [[Centrifugal Compressor]]
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 7.82%] within [[Reciprocating Compressor]]
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 2.75%] within [[Screw Compressor]]
- [[ELP External Leakage Process Medium]] [has_mechanism:: Mechanical Failure - general] failure descriptor 6.70 within [[Reciprocating Compressor]]
- CYLN [contributes_to:: [[ELP External Leakage Process Medium]]] 4.10 within [[Reciprocating Compressor]]
- [[ELP External Leakage Process Medium]] [has_mechanism:: LEAK] failure descriptor 1.89 within [[Centrifugal Compressor]]
- [[ELP External Leakage Process Medium]] [has_mechanism:: LEAK] failure descriptor 1.37 within [[Screw Compressor]]
- [[ELP External Leakage Process Medium]] [defined_in:: [[OREDA]]]

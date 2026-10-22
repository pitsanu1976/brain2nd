---
title: ELU External Leakage Utility Medium
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [failure-mode, failure-rate, oreda, compressor]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-centrifugal-failure-descriptor.png, compressor-screw-failure-descriptor.png]
confidence: high
contested: false
---

# ELU - External leakage - Utility medium

อันดับ 4 ใน [[Failure Mode]]: **8.62%** ของ total failure rate กระจายมากที่สุดใน 19 โหมด คือ **33 คู่** failure mode/item (utility medium เช่น lube oil, seal oil, สาร cooling, instrument air)

## ตัวขับหลัก (OREDA, ทุกประเภทรวม)

| Maintainable Item | Sub Unit (ที่นับ %) | % | Mechanism |
|---|---|---|---|
| Valves | [[CPUN Compressor Unit]] | 1.21 | Leakage (cover gasket / stem packing) |
| Piping | [[CPUN Compressor Unit]] | 0.90 | Corrosion |
| Instruments | [[PWTR Power Transmission]] | 0.84 | Leakage (impulse line / fitting) |
| Cylinder liner | [[CPUN Compressor Unit]] | 0.62 | Leakage (liner O-ring / head gasket) |
| Shaft seals | [[CPUN Compressor Unit]] | 0.53 | Leakage (secondary seal O-ring) |
| Pump w/motor | [[LUBS Lubrication System]] | 0.49 | Leakage (mechanical seal) |
| Pump w/motor/gear | [[SHSS Shaft Seal System]] | 0.40 | Leakage (mechanical seal) |

ไม่มี item ใดเกิน 1.21 จึงเป็นโหมดแบบ "long tail" ต่างจาก AIR/SER/LOO ที่มี item เดียวครอบงำ ผลรวม 33 คู่ = 8.62

## แยกตามประเภท compressor (total ของโหมด ELU)

| Centrifugal | Reciprocating | Screw |
|---|---|---|
| 17.54 | 4.28 | 13.75 |

Descriptor สูงสุด: centrifugal = Leakage 8.99, Wear 3.11; screw = Mechanical Failure - general 6.87, Leakage 3.44; reciprocating = Mechanical Failure - general 2.33 ดู [[Centrifugal Compressor]] และ [[Compressor Type Failure Profiles]]

## Resolution ที่ dataset เสนอ

Leakage มี resolution ที่เป็นไปได้มากที่สุด (10 รายการ) เช่น Adjust (tighten), Replace (gasket/O-ring), Overhaul ดู [[Resolution Matrix by Mechanism]]

## Triplets

- [[ELU External Leakage Utility Medium]] [is_a:: [[Failure Mode]]]
- [[ELU External Leakage Utility Medium]] [has_code:: ELU]
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 8.62%] all compressor types, rank 4 of 19
- [[ELU External Leakage Utility Medium]] [has_value:: 33] failure mode/item pairs, most of the 19 modes
- CPUN-VALV [contributes_to:: [[ELU External Leakage Utility Medium]]] 1.21%
- CPUN-PIPE [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.90%
- PWTR-INST [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.84%
- CPUN-CYLN [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.62%
- CPUN-SHSL [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.53%
- LUBS-PMTR [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.49%
- SHSS-PMGR [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.40%
- [[ELU External Leakage Utility Medium]] [has_mechanism:: LEAK] Valves (cover gasket / stem packing), Instruments (impulse line / fitting), Cylinder liner (liner O-ring / head gasket), Shaft seals (secondary seal O-ring), Pump w/motor and Pump w/motor/gear (mechanical seal)
- [[ELU External Leakage Utility Medium]] [has_mechanism:: CORR] Piping
- [[ELU External Leakage Utility Medium]] [differs_from:: [[AIR Abnormal Instrument Reading]]] long tail, no item above 1.21%; AIR has one dominant item
- [[ELU External Leakage Utility Medium]] [differs_from:: [[SER Minor In-Service Problems]]] long tail vs one dominant item
- [[ELU External Leakage Utility Medium]] [differs_from:: [[LOO Low Output]]] long tail vs one dominant item
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 17.54%] within [[Centrifugal Compressor]]
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 4.28%] within [[Reciprocating Compressor]]
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 13.75%] within [[Screw Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: LEAK] failure descriptor 8.99 within [[Centrifugal Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: WEAR] failure descriptor 3.11 within [[Centrifugal Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: Mechanical Failure - general] failure descriptor 6.87 within [[Screw Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: LEAK] failure descriptor 3.44 within [[Screw Compressor]]
- [[ELU External Leakage Utility Medium]] [has_mechanism:: Mechanical Failure - general] failure descriptor 2.33 within [[Reciprocating Compressor]]
- LEAK [has_value:: 10] possible resolutions, most of any mechanism
- [[ELU External Leakage Utility Medium]] [resolved_by:: ADJ] tighten
- [[ELU External Leakage Utility Medium]] [resolved_by:: RPL] gasket/O-ring
- [[ELU External Leakage Utility Medium]] [resolved_by:: OVH]
- [[ELU External Leakage Utility Medium]] [defined_in:: [[OREDA]]]

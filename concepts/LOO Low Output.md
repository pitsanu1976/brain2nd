---
title: LOO Low Output
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [failure-mode, failure-rate, oreda, compressor]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-reciprocating-failure-mode-vs-item-1.png, compressor-reciprocating-failure-descriptor.png]
confidence: high
contested: false
---

# LOO - Low output

อันดับ 3 ใน [[Failure Mode]]: **10.11%** ของ total failure rate (12 คู่ failure mode/item) กำลัง/อัตราไหลต่ำกว่าที่ต้องการ

## ตัวขับหลัก (OREDA, ทุกประเภทรวม)

| Maintainable Item | Sub Unit (ที่นับ %) | % | Mechanism ที่แสดงในแถวแรก |
|---|---|---|---|
| Cylinder liner | [[CPUN Compressor Unit]] | 5.78 | Wear (liner bore wear / scuffing) |
| Valves | [[CPUN Compressor Unit]] | 2.21 | Wear (valve plate/seat/spring) |
| Pump w/motor | [[LUBS Lubrication System]] | 1.32 | Wear (impeller/gear/rotor) |
| Filter(s) | [[LUBS Lubrication System]] | 0.31 | Blockage/plugged |
| Pump w/motor/gear | [[SHSS Shaft Seal System]] | 0.13 | Wear |
| Instruments | [[PWTR Power Transmission]] | 0.12 | Faulty signal/indication/alarm |

อีก 6 คู่แต่ละตัว <= 0.09 ผลรวม 12 คู่ = 10.11 (ตรงกับ summary) Cylinder liner + Valves = 7.99 (derived: ประมาณ 79%) ซึ่งเป็น item ของ reciprocating เป็นหลัก

## แยกตามประเภท compressor (total ของโหมด LOO)

| Centrifugal | Reciprocating | Screw |
|---|---|---|
| 1.66 | 21.60 | 5.84 |

Reciprocating: failure descriptor Mechanical Failure - general = 18.62; item Cylinder liner = 12.20, Valves = 3.63, Pump w/motor = 2.79 ดู [[Reciprocating Compressor]] และ [[Compressor Type Failure Profiles]]

## Resolution ที่ dataset เสนอ

Wear จับคู่กับ Adjust (เช่น "optimise cylinder lube rate" สำหรับ Cylinder liner), Inspection, Overhaul, Replace ดู [[Failure Mechanism]] และ [[Resolution Codes]]

## Triplets

- [[LOO Low Output]] [is_a:: [[Failure Mode]]]
- [[LOO Low Output]] [has_code:: LOO]
- [[LOO Low Output]] [has_failure_rate_share:: 10.11%] all compressor types, rank 3 of 19
- [[LOO Low Output]] [has_value:: 12] failure mode/item pairs
- CPUN-CYLN [contributes_to:: [[LOO Low Output]]] 5.78%
- CPUN-VALV [contributes_to:: [[LOO Low Output]]] 2.21%
- LUBS-PMTR [contributes_to:: [[LOO Low Output]]] 1.32%
- LUBS-FILT [contributes_to:: [[LOO Low Output]]] 0.31%
- SHSS-PMGR [contributes_to:: [[LOO Low Output]]] 0.13%
- PWTR-INST [contributes_to:: [[LOO Low Output]]] 0.12%
- [[LOO Low Output]] [has_value:: 0.09%] max share of each of the other 6 pairs
- [[LOO Low Output]] [has_value:: 7.99%] Cylinder liner + Valves; about 79% of LOO (derived); mainly reciprocating items
- [[LOO Low Output]] [has_mechanism:: WEAR] Cylinder liner (bore wear / scuffing), Valves (plate/seat/spring), Pump w/motor (impeller/gear/rotor), Pump w/motor/gear
- [[LOO Low Output]] [has_mechanism:: BLKG] Filter(s)
- [[LOO Low Output]] [has_mechanism:: FSIG] Instruments
- [[LOO Low Output]] [has_failure_rate_share:: 1.66%] within [[Centrifugal Compressor]]
- [[LOO Low Output]] [has_failure_rate_share:: 21.60%] within [[Reciprocating Compressor]]
- [[LOO Low Output]] [has_failure_rate_share:: 5.84%] within [[Screw Compressor]]
- [[LOO Low Output]] [has_mechanism:: Mechanical Failure - general] failure descriptor 18.62 within [[Reciprocating Compressor]]
- CYLN [contributes_to:: [[LOO Low Output]]] 12.20 within [[Reciprocating Compressor]]
- VALV [contributes_to:: [[LOO Low Output]]] 3.63 within [[Reciprocating Compressor]]
- PMTR [contributes_to:: [[LOO Low Output]]] 2.79 within [[Reciprocating Compressor]]
- [[LOO Low Output]] [resolved_by:: ADJ] Wear; e.g. optimise cylinder lube rate for Cylinder liner
- [[LOO Low Output]] [resolved_by:: INS] Wear
- [[LOO Low Output]] [resolved_by:: OVH] Wear
- [[LOO Low Output]] [resolved_by:: RPL] Wear
- [[LOO Low Output]] [defined_in:: [[OREDA]]]

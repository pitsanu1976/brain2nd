---
title: PDE Parameter Deviation
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [failure-mode, failure-rate, oreda, compressor]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-screw-failure-mode-vs-item-2.png, compressor-reciprocating-failure-mode-vs-item-2.png]
confidence: high
contested: false
---

# PDE - Parameter deviation

อันดับ 5 ใน [[Failure Mode]]: **8.13%** ของ total failure rate (14 คู่ failure mode/item) ค่าที่วัดได้ (pressure, temperature, flow ฯลฯ) เบี่ยงเบนจาก setpoint/ช่วงปกติ

## ตัวขับหลัก (OREDA, ทุกประเภทรวม)

| Maintainable Item | Sub Unit (ที่นับ %) | % | Mechanism ที่แสดงในแถวแรก |
|---|---|---|---|
| Instruments | [[PWTR Power Transmission]] | 3.35 | Faulty signal/indication/alarm |
| Valves | [[CPUN Compressor Unit]] | 1.92 | Wear |
| Cylinder liner | [[CPUN Compressor Unit]] | 0.57 | Wear |
| Filter(s) | [[LUBS Lubrication System]] | 0.44 | Blockage/plugged |
| Control unit | [[CTMN Control and Monitoring]] | 0.40 | Software failure |
| Monitoring | [[CTMN Control and Monitoring]] | 0.35 | Faulty signal/indication/alarm |
| Pump w/motor | [[LUBS Lubrication System]] | 0.35 | Wear |

ผลรวม 14 คู่ = 8.13 Instruments + Valves = 5.27 (derived: ประมาณ 65%)

## แยกตามประเภท compressor (total ของโหมด PDE)

| Centrifugal | Reciprocating | Screw |
|---|---|---|
| 2.55 | 12.38 | 13.40 |

Screw: Valves 4.81, Purge air 2.06, Filter(s) 1.72, Pump w/motor 1.72; reciprocating: Valves 2.33 ดู [[Screw Compressor]] และ [[Compressor Type Failure Profiles]]

## ที่เกี่ยวข้อง

PDE มักสัมพันธ์กับ [[AIR Abnormal Instrument Reading]] (ปัญหา instrument ปะปนกับ parameter จริง) และ [[LOO Low Output]] (valve/liner wear)

## Triplets

- [[PDE Parameter Deviation]] [is_a:: [[Failure Mode]]]
- [[PDE Parameter Deviation]] [has_code:: PDE]
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 8.13%] all compressor types, rank 5 of 19
- [[PDE Parameter Deviation]] [has_value:: 14] failure mode/item pairs
- PWTR-INST [contributes_to:: [[PDE Parameter Deviation]]] 3.35%
- CPUN-VALV [contributes_to:: [[PDE Parameter Deviation]]] 1.92%
- CPUN-CYLN [contributes_to:: [[PDE Parameter Deviation]]] 0.57%
- LUBS-FILT [contributes_to:: [[PDE Parameter Deviation]]] 0.44%
- CTMN-CTUN [contributes_to:: [[PDE Parameter Deviation]]] 0.40%
- CTMN-MONI [contributes_to:: [[PDE Parameter Deviation]]] 0.35%
- LUBS-PMTR [contributes_to:: [[PDE Parameter Deviation]]] 0.35%
- [[PDE Parameter Deviation]] [has_value:: 5.27%] Instruments + Valves; about 65% of PDE (derived)
- [[PDE Parameter Deviation]] [has_mechanism:: FSIG] Instruments, Monitoring (first row)
- [[PDE Parameter Deviation]] [has_mechanism:: WEAR] Valves, Cylinder liner, Pump w/motor (first row)
- [[PDE Parameter Deviation]] [has_mechanism:: BLKG] Filter(s) (first row)
- [[PDE Parameter Deviation]] [has_mechanism:: SWFL] Control unit (first row)
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 2.55%] within [[Centrifugal Compressor]]
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 12.38%] within [[Reciprocating Compressor]]
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 13.40%] within [[Screw Compressor]]
- VALV [contributes_to:: [[PDE Parameter Deviation]]] 4.81 within [[Screw Compressor]]
- PAIR [contributes_to:: [[PDE Parameter Deviation]]] 2.06 within [[Screw Compressor]]
- FILT [contributes_to:: [[PDE Parameter Deviation]]] 1.72 within [[Screw Compressor]]
- PMTR [contributes_to:: [[PDE Parameter Deviation]]] 1.72 within [[Screw Compressor]]
- VALV [contributes_to:: [[PDE Parameter Deviation]]] 2.33 within [[Reciprocating Compressor]]
- [[PDE Parameter Deviation]] [related_to:: [[AIR Abnormal Instrument Reading]]] instrument problems mixed with real parameter deviation
- [[PDE Parameter Deviation]] [related_to:: [[LOO Low Output]]] valve/liner wear
- [[PDE Parameter Deviation]] [defined_in:: [[OREDA]]]

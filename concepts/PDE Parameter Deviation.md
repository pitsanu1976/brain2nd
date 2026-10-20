---
title: PDE Parameter Deviation
created: 2026-10-20
updated: 2026-10-20
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

---
title: LOO Low Output
created: 2026-10-20
updated: 2026-10-20
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

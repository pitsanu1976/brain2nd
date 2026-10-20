---
title: ELU External Leakage Utility Medium
created: 2026-10-20
updated: 2026-10-20
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

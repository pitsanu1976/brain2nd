---
title: ELP External Leakage Process Medium
created: 2026-10-20
updated: 2026-10-20
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

---
title: OHE Overheating
created: 2026-10-20
updated: 2026-10-20
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

---
title: UST Spurious Stop
created: 2026-10-20
updated: 2026-10-21
type: concept
tags: [failure-mode, failure-rate, oreda, compressor]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-screw-failure-mode-vs-item-2.png, compressor-centrifugal-failure-mode-vs-item-2.png, reliability-based-maintenance-management.md]
confidence: high
contested: false
---

# UST - Spurious stop

**4.16%** ของ total failure rate (22 คู่ failure mode/item) อันดับ 9 ใน [[Failure Mode]] การหยุดโดยไม่ได้สั่ง (trip) มักเกิดจากสัญญาณหรือระบบควบคุม ไม่ใช่ความเสียหายทางกลโดยตรง

## ตัวขับหลัก (OREDA, ทุกประเภทรวม)

| Maintainable Item | Sub Unit (ที่นับ %) | % | Mechanism ที่แสดงในแถวแรก |
|---|---|---|---|
| Instruments | [[PWTR Power Transmission]] | 1.92 | Faulty signal/indication/alarm |
| Control unit | [[CTMN Control and Monitoring]] | 0.53 | Software failure |
| Valves | [[CPUN Compressor Unit]] | 0.29 | Breakage (broken valve plate/spring) |
| Internal power supply | [[CTMN Control and Monitoring]] | 0.18 | No power/ voltage |
| Filter(s) | [[LUBS Lubrication System]] | 0.15 | Blockage/plugged |
| Cylinder liner | [[CPUN Compressor Unit]] | 0.13 | Overheating |

Instruments + Control unit = 2.45 (derived: ประมาณ 59% ของ 4.16) ผลรวม 22 คู่ = 4.16

## แยกตามประเภท compressor (total ของโหมด UST)

| Centrifugal | Reciprocating | Screw |
|---|---|---|
| 6.66 | 2.79 | 11.68 |

Screw: Instrument, temperature = 2.41, Unknown = 2.06, Instrument, pressure = 1.72 ดู [[Screw Compressor]] และ [[Compressor Type Failure Profiles]]

## Alias: SPS (resolved)

**Resolved 2026-10-21 (ตัดสินโดยผู้ใช้):** ใช้ **UST** เป็นรหัสหลัก และถือ **SPS** เป็น alias (ข้อความด้านล่างเก็บไว้เป็นประวัติ) เมื่อเจอรหัส SPS ในเอกสาร/CMMS ให้ map เป็น UST


- ตัวเลขทั้งหมดในหน้านี้มาจาก dataset OREDA ซึ่งใช้รหัส **UST** ส่วนหนังสือ RBMM (p.132-134, Fig 5.15/5.17 ตัวอย่าง ISO 14224 ของ pump/motor) ใช้รหัส **SPS** สำหรับ "Spurious stop" ชื่อเดียวกัน
- ยังไม่มีตัวมาตรฐานมาตัดสิน ถือ SPS เป็น alias ที่ยังไม่ verify หน้านี้ใช้ UST ต่อ ดู [[Failure Data Recording]] และ [[ISO 14224]]

## ที่เกี่ยวข้อง

โหมดที่ใกล้เคียงกันคือ [[AIR Abnormal Instrument Reading]] (instrument) เพราะ trip จาก instrument fault เป็นสาเหตุสำคัญของ UST

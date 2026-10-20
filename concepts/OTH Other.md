---
title: OTH Other
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [failure-mode, failure-rate, oreda, compressor, data-quality]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-centrifugal-failure-mode-vs-item-2.png]
confidence: high
contested: false
---

# OTH - Other

โหมดที่ไม่เข้าหมวดอื่นใน [[Failure Mode]]: **5.46%** ของ total failure rate (25 คู่ failure mode/item) อันดับ 6

## ลักษณะเฉพาะใน dataset

- ทุกแถวของ OTH ใช้ mechanism = **Other** (รหัส `OTHR`) ตามกติกาใน Notes: "OTH maps to mechanism 'Other' ... for every item"
- Resolution detail ที่ใช้คือ "investigate and record details" (Check) และ "action not covered by standard categories" (Other)
- เป็นตัวชี้วัดคุณภาพการบันทึก: ถ้าสัดส่วน OTH สูงใน CMMS แปลว่าการจำแนก failure mode ไม่ละเอียดพอ ดู [[Failure Mechanism]]

## ตัวขับหลัก (OREDA, ทุกประเภทรวม)

| Maintainable Item | Sub Unit (ที่นับ %) | % |
|---|---|---|
| Valves | [[CPUN Compressor Unit]] | 1.37 |
| Instruments | [[PWTR Power Transmission]] | 0.86 |
| Pump w/motor/gear | [[SHSS Shaft Seal System]] | 0.44 |
| Antisurge system | [[CPUN Compressor Unit]] | 0.42 |
| Control unit | [[CTMN Control and Monitoring]] | 0.31 |
| Filter(s) | [[LUBS Lubrication System]] | 0.31 |

ผลรวม 25 คู่ = 5.46

## แยกตามประเภท compressor (total ของโหมด OTH)

| Centrifugal | Reciprocating | Screw |
|---|---|---|
| 13.76 | 1.02 | 5.50 |

Centrifugal มีสัดส่วน OTH สูงผิดปกติ (Valves x OTH = 3.22 ในภาพ OREDA ของ centrifugal) ซึ่งสะท้อนการจำแนกที่ไม่ละเอียดมากกว่าปัญหาทางกายภาพ ดู [[Compressor Type Failure Profiles]] (ข้อสรุปนี้เป็นการตีความ confidence ต่ำกว่าตัวเลข)

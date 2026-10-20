---
title: Centrifugal Compressor
created: 2026-10-20
updated: 2026-10-20
type: entity
tags: [compressor, centrifugal, oreda, failure-rate]
sources: [failure-structure.md, failure-structure__sheet1.csv, compressor-centrifugal-failure-descriptor.png, compressor-centrifugal-failure-mode-vs-item-1.png, compressor-centrifugal-failure-mode-vs-item-2.png, compressor-centrifugal-failure-mode-vs-item-3.png, compressor-centrifugal-failure-mode-vs-item-4.png]
confidence: medium
contested: false
---

# Centrifugal Compressor

[[Compressor]] แบบ centrifugal ตัวเลขทั้งหมดอ่านจากภาพตาราง OREDA (confidence medium เพราะเป็นการอ่านภาพ) ฐานคือ % ของ failure rate **เฉพาะ centrifugal** (รวม 100.0)

## % ต่อ failure mode (Total ของแต่ละโหมด)

| Mode | % | Mode | % |
|---|---|---|---|
| AIR | 27.52 | OTH | 13.76 |
| ELU | 17.54 | SER | 6.77 |
| INL | 6.99 | UST | 6.66 |
| FTS | 5.55 | ELP | 2.66 |
| VIB | 2.66 | PDE | 2.55 |
| ERO | 1.78 | LOO | 1.66 |
| NOI | 0.89 | OHE | 0.67 |
| HIO | 0.55 | STD | 0.55 |
| STP | 0.44 | UNK | 0.44 |
| BRD | 0.33 | | |

รวม 100.0 (derived จากการบวกได้ 99.97 ปัดเศษ) โหมดเด่น: [[AIR Abnormal Instrument Reading]] และ [[ELU External Leakage Utility Medium]]

## Maintainable item ที่เด่น (Sum ทุกโหมด)

Unknown 11.10, Valves 10.43, Instrument temperature 8.53, Instrument pressure 8.31, Instrument level 7.55, Antisurge system 5.11, Control unit 4.66, Instrument vibration 4.16, Oil 3.77, Filter(s) 3.44, Pump w/motor/gear 3.44

Instruments ทั้ง 7 type รวม = 31.87 (derived) ใน centrifugal (สอดคล้องกับโหมด AIR ที่สูง) ดู [[Maintainable Item]]

## Failure descriptor (10 โหมดแรก ตามภาพ)

- AIR: Faulty signal/indication/alarm 8.10, Out of adjustment 6.88, Instrument failure - general 4.11, Control failure 1.00
- ELU: Leakage 8.99, Wear 3.11, Mechanical Failure - general 1.44
- INL: Wear 5.88 (จาก INL ทั้งหมด 6.99)
- ELP: Leakage 1.89
- ภาพ descriptor ครอบคลุมเฉพาะโหมด AIR ถึง NOI ("to be continued"); descriptor ของโหมดที่เหลือไม่มีใน sources

## โครงสร้างใน failure-structure.md

Sheet1 ของ `failure-structure.md` ระบุคู่ mode/item/sub unit/descriptor ของ centrifugal จำนวน 1,810 แถว (เป็นโครงสร้างความเป็นไปได้ ไม่ใช่จำนวนเหตุการณ์) ใช้ sub unit ตามที่ระบุใน [[Failure Hierarchy]] (มีข้อขัดแย้งบางรายการกับ dataset หลัก) เปรียบเทียบกับประเภทอื่นที่ [[Compressor Type Failure Profiles]]

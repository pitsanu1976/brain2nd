---
title: Compressor Type Failure Profiles
created: 2026-10-20
updated: 2026-10-20
type: comparison
tags: [comparison, centrifugal, reciprocating, screw, failure-mode, failure-rate]
sources: [compressor-failure-hierarchy__summary-by-failure-mode.csv, failure-structure.md, failure-structure__sheet1.csv, compressor-centrifugal-failure-mode-vs-item-2.png, compressor-reciprocating-failure-mode-vs-item-2.png, compressor-screw-failure-mode-vs-item-2.png]
confidence: medium
contested: false
---

# Centrifugal vs Reciprocating vs Screw - failure profiles

เปรียบเทียบสัดส่วน failure mode ของ [[Centrifugal Compressor]], [[Reciprocating Compressor]] และ [[Screw Compressor]] เทียบกับค่าทุกประเภทรวมของ [[Compressor]]

## หมายเหตุเรื่องฐานของตัวเลข (สำคัญ)

- คอลัมน์ **All** = % ของ total failure rate ทุกประเภทรวม (รวมกัน 85.66 เพราะตัด placeholder item)
- คอลัมน์ Centrifugal / Reciprocating / Screw = Total ของแต่ละโหมดจากภาพ OREDA แต่ละประเภท แต่ละประเภทรวมกัน **100%** (รวม item Unknown/Subunit/Other)
- ดังนั้นห้ามนำ All ไปเทียบตรง ๆ กับสามคอลัมน์ที่เหลือ (ฐานต่างกัน) และห้ามเฉลี่ยประเภทเพื่อให้ได้ All เพราะไม่มีสัดส่วน population ใน sources
- ค่าต่อประเภทอ่านจากภาพ (confidence medium)

## ตารางเปรียบเทียบ 19 โหมด

| Mode | All | Centrifugal | Reciprocating | Screw |
|---|---|---|---|---|
| AIR | 17.18 | 27.52 | 9.22 | 22.68 |
| SER | 13.05 | 6.77 | 21.97 | 10.65 |
| LOO | 10.11 | 1.66 | 21.60 | 5.84 |
| ELU | 8.62 | 17.54 | 4.28 | 13.75 |
| PDE | 8.13 | 2.55 | 12.38 | 13.40 |
| OTH | 5.46 | 13.76 | 1.02 | 5.50 |
| ELP | 4.58 | 2.66 | 7.82 | 2.75 |
| OHE | 4.18 | 0.67 | 8.85 | 2.41 |
| UST | 4.16 | 6.66 | 2.79 | 11.68 |
| FTS | 2.35 | 5.55 | 1.12 | 4.12 |
| INL | 1.97 | 6.99 | 0.19 | 0.34 |
| ERO | 1.50 | 1.78 | 1.12 | 3.09 |
| VIB | 1.42 | 2.66 | 1.77 | 0.00 |
| UNK | 1.07 | 0.44 | 3.26 | 1.37 |
| STD | 0.81 | 0.55 | 1.49 | 1.72 |
| NOI | 0.44 | 0.89 | 0.56 | 0.69 |
| STP | 0.34 | 0.44 | 0.37 | 0.00 |
| HIO | 0.21 | 0.55 | 0.00 | 0.00 |
| BRD | 0.08 | 0.33 | 0.19 | 0.00 |

รายละเอียดโหมด: [[Failure Mode]]

## ข้อสังเกต

1. **Centrifugal**: ถูกครอบงำโดยโหมดสัญญาณ/รั่วของ utility (AIR 27.52, ELU 17.54) และ OTH สูง (13.76) และ INL สูง (6.99 เทียบ 0.19 ใน reciprocating) item เด่นคือ Valves, Instruments และ Antisurge system (5.11)
2. **Reciprocating**: ครอบงำโดย SER (21.97) และ LOO (21.60) ซึ่งมาจาก Filter(s) และ Cylinder liner/Valves ตามลำดับ OHE สูง (8.85) จาก Cylinder liner (7.17) Cylinder liner เดียวคิด 28.77 ของ reciprocating
3. **Screw**: AIR 22.68, ELU 13.75, PDE 13.40, UST 11.68 item เด่นคือ Valves (18.04) และ Instruments (temperature 13.75, pressure 9.97) VIB, STP, BRD, HIO เป็น 0.00 ใน data
4. **LOO** ต่างกันมากที่สุด: reciprocating 21.60 เทียบ centrifugal 1.66 (สัดส่วน ~13 เท่า derived) สอดคล้องกับ wear ของ cylinder/valve ที่เป็นลักษณะเฉพาะของ reciprocating ดู [[LOO Low Output]]
5. **AIR** ต่ำใน reciprocating (9.22) แต่สูงใน centrifugal และ screw ดู [[AIR Abnormal Instrument Reading]]

## Maintainable item เด่นต่อประเภท (Sum ทุกโหมด)

| ลำดับ | Centrifugal | Reciprocating | Screw |
|---|---|---|---|
| 1 | Unknown 11.10 | Cylinder liner 28.77 | Valves 18.04 |
| 2 | Valves 10.43 | Filter(s) 14.80 | Instrument, temperature 13.75 |
| 3 | Instrument, temperature 8.53 | Valves 10.94 | Instrument, pressure 9.97 |
| 4 | Instrument, pressure 8.31 | Unknown 5.03 | Subunit 6.53 |
| 5 | Instrument, level 7.55 | Pump w/motor 4.56 | Unknown 5.50 |
| 6 | Antisurge system 5.11 | Instrument, pressure 4.19 | Filter(s) 4.41 |

ผลรวม Instruments ทุก type (derived): centrifugal 31.87, reciprocating 14.81, screw 28.87

## ข้อจำกัด

- ภาพ failure descriptor ของแต่ละประเภทครอบคลุมเฉพาะโหมด AIR ถึง NOI ("to be continued") ส่วนที่เหลือไม่มีใน sources
- จำนวนเหตุการณ์/population ไม่มีใน sources; screw มีขั้น % ละเอียดสุด 0.34 (บ่งชี้ตัวอย่างน้อย) ดู [[Screw Compressor]]
- `failure-structure.md` ให้เพียงโครงสร้าง (คู่ mode/item/sub unit/descriptor: centrifugal 1,810 แถว, reciprocating 732, screw 512) ไม่มี % จึงใช้เปรียบเทียบ "ความหลากหลายของโครงสร้าง" ได้เท่านั้น

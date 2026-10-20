---
title: Reciprocating Compressor
created: 2026-10-20
updated: 2026-10-20
type: entity
tags: [compressor, reciprocating, oreda, failure-rate]
sources: [failure-structure.md, failure-structure__sheet1.csv, compressor-reciprocating-failure-descriptor.png, compressor-reciprocating-failure-mode-vs-item-1.png, compressor-reciprocating-failure-mode-vs-item-2.png]
confidence: medium
contested: false
---

# Reciprocating Compressor

[[Compressor]] แบบ reciprocating ตัวเลขอ่านจากภาพตาราง OREDA (confidence medium) ฐานคือ % ของ failure rate **เฉพาะ reciprocating** (รวม 100.0)

## % ต่อ failure mode (Total ของแต่ละโหมด)

| Mode | % | Mode | % |
|---|---|---|---|
| SER | 21.97 | LOO | 21.60 |
| PDE | 12.38 | AIR | 9.22 |
| OHE | 8.85 | ELP | 7.82 |
| ELU | 4.28 | UNK | 3.26 |
| UST | 2.79 | VIB | 1.77 |
| STD | 1.49 | ERO | 1.12 |
| FTS | 1.12 | OTH | 1.02 |
| NOI | 0.56 | STP | 0.37 |
| BRD | 0.19 | INL | 0.19 |
| HIO | 0.00 | | |

ผลรวมบวกได้ 100.00 โหมดเด่น: [[SER Minor In-Service Problems]], [[LOO Low Output]], [[PDE Parameter Deviation]], [[OHE Overheating]]

## Maintainable item ที่เด่น (Sum ทุกโหมด)

Cylinder liner **28.77**, Filter(s) **14.80**, Valves 10.94, Unknown 5.03, Pump w/motor 4.56, Instrument pressure 4.19, Instrument temperature 3.96, Other 3.54, Subunit 3.26, Control unit 2.51, Instrument vibration 2.47, Base frame 2.14

- Cylinder liner: LOO 12.20, OHE 7.17, ELP 4.10, ELU 1.30, PDE 1.21
- Filter(s): SER 14.25 (เกือบทั้งหมดของ Filter(s))
- Instruments ทั้ง 7 type รวม = 14.81 (derived) ต่ำกว่า centrifugal/screw มาก

ค่าเหล่านี้สอดคล้องกับ dataset หลักที่ Cylinder liner (13.66 derived), Filter(s) (8.95) และ Valves (11.64) เป็น item เด่นของทุกประเภทรวม ดู [[CPUN Compressor Unit]] และ [[LUBS Lubrication System]]

## Failure descriptor (10 โหมดแรก ตามภาพ)

- LOO: Mechanical Failure - general **18.62**, Unknown 1.40
- ELP: Mechanical Failure - general 6.70
- AIR: Instrument failure - general 6.52
- ELU: Mechanical Failure - general 2.33
- ภาพครอบคลุมเฉพาะโหมด AIR ถึง NOI

ข้อสังเกต: reciprocating ใช้ descriptor "Mechanical Failure - general" สูงมาก ขณะที่ dataset หลักไม่มี mechanism นี้ในแถวใดเลย ดู [[Failure Mechanism]]

## โครงสร้างใน failure-structure.md

Sheet1 ระบุคู่ mode/item/sub unit/descriptor ของ reciprocating 732 แถว (โครงสร้างความเป็นไปได้) เปรียบเทียบที่ [[Compressor Type Failure Profiles]]

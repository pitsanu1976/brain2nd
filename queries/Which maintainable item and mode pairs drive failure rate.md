---
title: Which maintainable item and mode pairs drive failure rate
created: 2026-10-20
updated: 2026-10-20
type: query
tags: [query, maintainable-item, failure-mode, failure-rate]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv]
confidence: medium
contested: false
---

# Which maintainable item / failure mode pairs drive the failure rate?

## คำตอบสั้น

คู่เดียว **Instruments x AIR = 13.54%** (ประมาณ 15.8% ของ 85.66) ใหญ่ที่สุด ตามด้วย Filter(s) x SER 7.33 และ Cylinder liner x LOO 5.78 สามคู่แรกรวม 26.65 (derived, ประมาณ 31.1%) ห้าคู่แรกรวม 33.40 (ประมาณ 39.0%)

## Top คู่ (ทุกประเภทรวม, แถวที่ `Count in Total = 1`)

| อันดับ | Item | Mode | Sub Unit | % |
|---|---|---|---|---|
| 1 | Instruments | [[AIR Abnormal Instrument Reading]] | [[PWTR Power Transmission]] | 13.54 |
| 2 | Filter(s) | [[SER Minor In-Service Problems]] | [[LUBS Lubrication System]] | 7.33 |
| 3 | Cylinder liner | [[LOO Low Output]] | [[CPUN Compressor Unit]] | 5.78 |
| 4 | Cylinder liner | [[OHE Overheating]] | [[CPUN Compressor Unit]] | 3.40 |
| 5 | Instruments | [[PDE Parameter Deviation]] | [[PWTR Power Transmission]] | 3.35 |
| 6 | Valves | LOO | CPUN | 2.21 |
| 7 | Cylinder liner | ELP | CPUN | 1.94 |
| 8= | Instruments | UST | PWTR | 1.92 |
| 8= | Valves | PDE | CPUN | 1.92 |
| 10 | Valves | OTH | CPUN | 1.37 |

## รวมต่อ item (derived: ผลรวมของแถว Count in Total = 1 ของ item นั้นทุกโหมด)

| Item | % รวม | สัดส่วนของ 85.66 |
|---|---|---|
| Instruments | 23.34 | 27.3% |
| Cylinder liner | 13.66 | 15.9% |
| Valves | 11.64 | 13.6% |
| Filter(s) | 8.95 | 10.4% |

สี่ item นี้รวม 57.59 (ประมาณ 67.2%) รายละเอียดดู [[Maintainable Item]], [[CPUN Compressor Unit]] และ [[LUBS Lubrication System]]

## ข้อควรระวัง

- Instruments มีตัวเลขสูงเพราะเป็นการรวม 7 instrument type เป็น item เดียว (Notes ข้อ 4) และ Sub Unit PWTR เป็นเพียงที่นับ % (ดู [[PWTR Power Transmission]])
- Cylinder liner เด่นเฉพาะ [[Reciprocating Compressor]] (Sum 28.77 ในภาพ reciprocating); ถ้า fleet ไม่มี reciprocating ลำดับจะต่างจากนี้
- Mechanism ที่แสดงมาจากแถวแรกของคู่ ไม่ใช่ทุก mechanism ของคู่นั้น ดู [[Failure Mechanism]]

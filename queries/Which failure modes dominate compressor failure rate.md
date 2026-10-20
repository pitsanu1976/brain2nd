---
title: Which failure modes dominate compressor failure rate
created: 2026-10-20
updated: 2026-10-20
type: query
tags: [query, failure-mode, failure-rate]
sources: [compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-failure-hierarchy.md]
confidence: high
contested: false
---

# Which failure modes dominate compressor failure rate?

## คำตอบสั้น

ห้าโหมดแรก **AIR, SER, LOO, ELU, PDE** รวม **57.09%** ของ total failure rate (ประมาณ 66.6% ของ 85.66% ที่ระบุได้) และเก้าโหมดแรก (เพิ่ม OTH, ELP, OHE, UST) รวม 75.47% (ประมาณ 88.1%)

## ข้อมูล (ทุกประเภทรวม, sheet Summary by Failure Mode)

| อันดับ | Mode | % | สะสม % | สะสม เป็นสัดส่วนของ 85.66 (derived) |
|---|---|---|---|---|
| 1 | [[AIR Abnormal Instrument Reading]] | 17.18 | 17.18 | 20.1% |
| 2 | [[SER Minor In-Service Problems]] | 13.05 | 30.23 | 35.3% |
| 3 | [[LOO Low Output]] | 10.11 | 40.34 | 47.1% |
| 4 | [[ELU External Leakage Utility Medium]] | 8.62 | 48.96 | 57.2% |
| 5 | [[PDE Parameter Deviation]] | 8.13 | 57.09 | 66.6% |
| 6 | [[OTH Other]] | 5.46 | 62.55 | 73.0% |
| 7 | [[ELP External Leakage Process Medium]] | 4.58 | 67.13 | 78.4% |
| 8 | [[OHE Overheating]] | 4.18 | 71.31 | 83.2% |
| 9 | [[UST Spurious Stop]] | 4.16 | 75.47 | 88.1% |

โหมดที่เหลืออีก 10 โหมด (FTS 2.35, INL 1.97, ERO 1.50, VIB 1.42, UNK 1.07, STD 0.81, NOI 0.44, STP 0.34, HIO 0.21, BRD 0.08) รวม 10.19 (derived) ตาราง 19 โหมดเต็มที่ [[Failure Mode]]

## ข้อสังเกต

- AIR + PDE + UST (โหมดที่เกี่ยวกับสัญญาณ/การวัด/trip) รวม 29.47 (derived) ซึ่งเป็นส่วนที่ใหญ่ซึ่งแก้ได้ด้วย instrument reliability/calibration
- OTH 5.46 คือโหมด "Other" อันดับ 6: เป็นสัญญาณของการจำแนกที่ไม่ละเอียดใน data ต้นทาง
- ลำดับต่างกันตามประเภท compressor: centrifugal = AIR, ELU, OTH; reciprocating = SER, LOO, PDE; screw = AIR, ELU, PDE ดู [[Compressor Type Failure Profiles]]
- % ฐาน 85.66 ไม่รวม Other/Subunit/Unknown 13.96 ตามที่ Notes ระบุ
- ไม่มี failure rate สัมบูรณ์ใน sources: ตัวเลขเป็นสัดส่วนสัมพัทธ์เท่านั้น ดู [[OREDA]]

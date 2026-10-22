---
title: Which failure modes dominate compressor failure rate
created: 2026-10-20
updated: 2026-10-22
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

## Triplets

- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 17.18%] all compressor types, rank 1, cumulative 17.18% (20.1% of 85.66, derived)
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 13.05%] all compressor types, rank 2, cumulative 30.23% (35.3% of 85.66, derived)
- [[LOO Low Output]] [has_failure_rate_share:: 10.11%] all compressor types, rank 3, cumulative 40.34% (47.1% of 85.66, derived)
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 8.62%] all compressor types, rank 4, cumulative 48.96% (57.2% of 85.66, derived)
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 8.13%] all compressor types, rank 5, cumulative 57.09% (66.6% of 85.66, derived)
- [[OTH Other]] [has_failure_rate_share:: 5.46%] all compressor types, rank 6, cumulative 62.55% (73.0% of 85.66, derived)
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 4.58%] all compressor types, rank 7, cumulative 67.13% (78.4% of 85.66, derived)
- [[OHE Overheating]] [has_failure_rate_share:: 4.18%] all compressor types, rank 8, cumulative 71.31% (83.2% of 85.66, derived)
- [[UST Spurious Stop]] [has_failure_rate_share:: 4.16%] all compressor types, rank 9, cumulative 75.47% (88.1% of 85.66, derived)
- FTS [has_failure_rate_share:: 2.35%] all compressor types, among remaining 10 modes
- INL [has_failure_rate_share:: 1.97%] all compressor types, among remaining 10 modes
- ERO [has_failure_rate_share:: 1.50%] all compressor types, among remaining 10 modes
- VIB [has_failure_rate_share:: 1.42%] all compressor types, among remaining 10 modes
- UNK [has_failure_rate_share:: 1.07%] all compressor types, among remaining 10 modes
- STD [has_failure_rate_share:: 0.81%] all compressor types, among remaining 10 modes
- NOI [has_failure_rate_share:: 0.44%] all compressor types, among remaining 10 modes
- STP [has_failure_rate_share:: 0.34%] all compressor types, among remaining 10 modes
- HIO [has_failure_rate_share:: 0.21%] all compressor types, among remaining 10 modes
- BRD [has_failure_rate_share:: 0.08%] all compressor types, among remaining 10 modes
- Top 5 Failure Modes [has_failure_rate_share:: 57.09%] AIR, SER, LOO, ELU, PDE; about 66.6% of 85.66
- Top 9 Failure Modes [has_failure_rate_share:: 75.47%] top 5 plus OTH, ELP, OHE, UST; about 88.1% of 85.66
- Remaining 10 Failure Modes [has_failure_rate_share:: 10.19%] derived
- Signal/Measurement/Trip Modes [has_failure_rate_share:: 29.47%] AIR + PDE + UST (derived); addressable by instrument reliability/calibration
- [[AIR Abnormal Instrument Reading]] [dominant_in:: [[Centrifugal Compressor]]] top 3: AIR, ELU, OTH
- [[ELU External Leakage Utility Medium]] [dominant_in:: [[Centrifugal Compressor]]] top 3: AIR, ELU, OTH
- [[OTH Other]] [dominant_in:: [[Centrifugal Compressor]]] top 3: AIR, ELU, OTH
- [[SER Minor In-Service Problems]] [dominant_in:: [[Reciprocating Compressor]]] top 3: SER, LOO, PDE
- [[LOO Low Output]] [dominant_in:: [[Reciprocating Compressor]]] top 3: SER, LOO, PDE
- [[PDE Parameter Deviation]] [dominant_in:: [[Reciprocating Compressor]]] top 3: SER, LOO, PDE
- [[AIR Abnormal Instrument Reading]] [dominant_in:: [[Screw Compressor]]] top 3: AIR, ELU, PDE
- [[ELU External Leakage Utility Medium]] [dominant_in:: [[Screw Compressor]]] top 3: AIR, ELU, PDE
- [[PDE Parameter Deviation]] [dominant_in:: [[Screw Compressor]]] top 3: AIR, ELU, PDE
- Other/Subunit/Unknown Placeholders [has_failure_rate_share:: 13.96%] excluded from 85.66 base (Notes)
- [[OREDA]] [has_value:: relative shares only] no absolute failure rate in sources

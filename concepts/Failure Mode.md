---
title: Failure Mode
created: 2026-10-20
updated: 2026-10-21
type: concept
tags: [failure-mode, failure-rate, oreda, taxonomy]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__summary-by-failure-mode.csv, reliability-based-maintenance-management.md]
confidence: high
contested: false
---

# Failure Mode (hub)

**Failure mode** คือลักษณะที่ความล้มเหลวปรากฏ (สิ่งที่สังเกตเห็น) เป็นระดับที่ 4 ใน [[Failure Hierarchy]] ตาม taxonomy ของ [[OREDA]] / [[ISO 14224]] มี 19 โหมดสำหรับ compressor

## ตารางทั้ง 19 โหมด

% = สัดส่วนของ total compressor failure rate (sheet "Summary by Failure Mode") "No. of items" = จำนวนคู่ failure mode/maintainable item ที่มี % ไม่เป็นศูนย์ (ไม่ใช่จำนวน item ไม่ซ้ำ ดู [[Maintainable Item]])

| Code | Failure mode | No. of items | % of total failure rate | หน้ารายละเอียด |
|---|---|---|---|---|
| AIR | Abnormal instrument reading | 17 | 17.18 | [[AIR Abnormal Instrument Reading]] |
| SER | Minor in-service problems | 27 | 13.05 | [[SER Minor In-Service Problems]] |
| LOO | Low output | 12 | 10.11 | [[LOO Low Output]] |
| ELU | External leakage - Utility medium | 33 | 8.62 | [[ELU External Leakage Utility Medium]] |
| PDE | Parameter deviation | 14 | 8.13 | [[PDE Parameter Deviation]] |
| OTH | Other | 25 | 5.46 | [[OTH Other]] |
| ELP | External leakage - Process medium | 17 | 4.58 | [[ELP External Leakage Process Medium]] |
| OHE | Overheating | 12 | 4.18 | [[OHE Overheating]] |
| UST | Spurious stop (alias: SPS) | 22 | 4.16 | [[UST Spurious Stop]] |
| FTS | Fail to start on demand | 13 | 2.35 | (ในหน้านี้เท่านั้น) |
| INL | Internal leakage | 9 | 1.97 | (ในหน้านี้เท่านั้น) |
| ERO | Erratic output | 6 | 1.50 | (ในหน้านี้เท่านั้น) |
| VIB | Vibration | 15 | 1.42 | (ในหน้านี้เท่านั้น) |
| UNK | Unknown | 9 | 1.07 | (ในหน้านี้เท่านั้น) |
| STD | Structural deficiency | 10 | 0.81 | (ในหน้านี้เท่านั้น) |
| NOI | Noise | 5 | 0.44 | (ในหน้านี้เท่านั้น) |
| STP | Fail to stop on demand | 5 | 0.34 | (ในหน้านี้เท่านั้น) |
| HIO | High output | 4 | 0.21 | (ในหน้านี้เท่านั้น) |
| BRD | Breakdown | 3 | 0.08 | (ในหน้านี้เท่านั้น) |
| | **Total** | **258** | **85.66** | |

ค่าใน source เก็บเป็นทศนิยมยาว (เช่น AIR 17.179999...) ตารางนี้ปัด 2 ตำแหน่งให้ตรงกับ % ใน sheet Failure Hierarchy

## ข้อสังเกต

- Total = **85.66%** ไม่ใช่ ~100% เพราะ placeholder item 'Other', 'Subunit', 'Unknown' (ไม่สามารถ trace ถึง item เฉพาะ) ถูกตัดออก และ Notes ระบุว่ารวมกัน 13.96% ของ failure rate (85.66 + 13.96 = 99.62 ส่วนต่างเล็กน้อยไม่มีคำอธิบายใน source นอกจาก rounding)
- 5 โหมดแรก (AIR, SER, LOO, ELU, PDE) รวม 57.09 (derived) หรือประมาณ 66.6% ของ 85.66 ดู [[Which failure modes dominate compressor failure rate]]
- % ต่อโหมดของแต่ละประเภท compressor ต่างจากค่ารวม ดู [[Compressor Type Failure Profiles]]
- ความสัมพันธ์ mode -> mechanism -> resolution ดู [[Failure Mechanism]] และ [[Resolution Codes]]
- รหัสโหมดคือรหัส 3 ตัวอักษร ใช้เป็นคอลัมน์ `FAILURE MODE` ใน data (ดู [[CAUSE_CODE Convention]])

## ดูเพิ่ม (RBMM)

หมายเหตุ: ส่วนนี้เป็นลิงก์/การตีความจากหนังสือ RBMM ไม่ใช่ข้อมูล OREDA และไม่เปลี่ยนตัวเลขในตาราง

- RBMM p.132-134 แสดงรายการรหัส failure mode ISO 14224 ของ pump/motor ตรงกับตารางนี้ 18 จาก 19 รหัส ต่างที่ **SPS (หนังสือ) vs UST (wiki)** ชื่อ "Spurious stop" เหมือนกัน resolve แล้ว 2026-10-21: ใช้ UST เป็นรหัสหลัก SPS เป็น alias ดู [[Failure Data Recording]] และ [[UST Spurious Stop]]
- การบันทึก Failure Mode ใน CMMS และ record ขั้นต่ำ: [[Failure Data Recording]]
- การวิเคราะห์ Failure Mode เชิงระบบ: [[FMECA]] (RPN และ criticality)
- พฤติกรรมการเสียรายโหมด (β, η): [[Weibull Analysis]], [[Failure Patterns and Bathtub Curve]]
- การเลือกงาน PM ต่อ failure mode: [[PM Task Selection]]

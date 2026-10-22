---
title: Failure Mode
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [failure-mode, failure-rate, oreda, taxonomy, iso-14224]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__summary-by-failure-mode.csv, reliability-based-maintenance-management.md, iso-14224.md]
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

## เทียบกับ ISO 14224:2016 (Table B.6)

ส่วนนี้เพิ่มจากมาตรฐาน ไม่เปลี่ยนตัวเลข % ของ dataset OREDA ข้างบน

- ISO Table B.6 (p.187) กำหนด failure mode ของ compressor (CO) **20 รหัส** = 19 รหัสของตารางนี้ + **PLU (Plugged/choked)** ซึ่งไม่มีใน dataset OREDA
- รหัสเดียวในตาราง rotating equipment ที่ CO ไม่ใช้คือ **ELF** (External leakage - fuel ใช้กับ CE, GT, ST เท่านั้น)
- ตาราง B.6 มีคอลัมน์ CO เดียว ไม่แยก centrifugal/reciprocating/screw (การแยกชนิดอยู่ใน taxonomy ของ equipment) ดู [[ISO 14224 Taxonomy]]
- Table B.15 (p.202-204) รวมรหัส failure mode ทุก equipment class **62 รหัส** โดย **14 รหัส** ติดธงเป็น on-demand type (เช่น FTS, STP)
- ตามค่า default มาตรฐานให้บันทึก mode ที่ระดับ **equipment class** (subsea แนะนำให้บันทึกที่ maintainable item ด้วย) (ISO 14224 cl. B.2.6, p.185) ต่างจาก dataset OREDA ที่ผูก mode กับ maintainable item ทุกแถว นี่เป็นความต่างของขอบเขตระหว่างสอง source ไม่ใช่ข้อขัดแย้ง
- UST เป็นรหัสที่ ISO 2016 ใช้จริง (ดู [[UST Spurious Stop]]); ความต่างของ subdivision ดู [[Compressor Subdivision Wiki vs ISO 14224]]
- field อื่นของ record: [[Failure Detection Method]]

## ดูเพิ่ม (RBMM)

หมายเหตุ: ส่วนนี้เป็นลิงก์/การตีความจากหนังสือ RBMM ไม่ใช่ข้อมูล OREDA และไม่เปลี่ยนตัวเลขในตาราง

- RBMM p.132-134 แสดงรายการรหัส failure mode ISO 14224 ของ pump/motor ตรงกับตารางนี้ 18 จาก 19 รหัส ต่างที่ **SPS (หนังสือ) vs UST (wiki)** ชื่อ "Spurious stop" เหมือนกัน resolve แล้ว 2026-10-21: ใช้ UST เป็นรหัสหลัก SPS เป็น alias ดู [[Failure Data Recording]] และ [[UST Spurious Stop]]
- การบันทึก Failure Mode ใน CMMS และ record ขั้นต่ำ: [[Failure Data Recording]]
- การวิเคราะห์ Failure Mode เชิงระบบ: [[FMECA]] (RPN และ criticality)
- พฤติกรรมการเสียรายโหมด (β, η): [[Weibull Analysis]], [[Failure Patterns and Bathtub Curve]]
- การเลือกงาน PM ต่อ failure mode: [[PM Task Selection]]

## Triplets

- [[Failure Mode]] [at_level:: 4] level 4 of [[Failure Hierarchy]]
- [[Failure Mode]] [has_value:: 19] compressor failure modes
- [[Failure Mode]] [defined_in:: [[OREDA]]]
- [[Failure Mode]] [defined_in:: [[ISO 14224]]]
- [[AIR Abnormal Instrument Reading]] [is_a:: [[Failure Mode]]]
- [[AIR Abnormal Instrument Reading]] [has_label:: Abnormal instrument reading]
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 17.18%] of total compressor failure rate, rank 1 of 19
- [[AIR Abnormal Instrument Reading]] [has_value:: 17] failure mode/item pairs with non-zero %
- [[SER Minor In-Service Problems]] [is_a:: [[Failure Mode]]]
- [[SER Minor In-Service Problems]] [has_label:: Minor in-service problems]
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 13.05%] of total compressor failure rate, rank 2 of 19
- [[SER Minor In-Service Problems]] [has_value:: 27] failure mode/item pairs with non-zero %
- [[LOO Low Output]] [is_a:: [[Failure Mode]]]
- [[LOO Low Output]] [has_label:: Low output]
- [[LOO Low Output]] [has_failure_rate_share:: 10.11%] of total compressor failure rate, rank 3 of 19
- [[LOO Low Output]] [has_value:: 12] failure mode/item pairs with non-zero %
- [[ELU External Leakage Utility Medium]] [is_a:: [[Failure Mode]]]
- [[ELU External Leakage Utility Medium]] [has_label:: External leakage - Utility medium]
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 8.62%] of total compressor failure rate, rank 4 of 19
- [[ELU External Leakage Utility Medium]] [has_value:: 33] failure mode/item pairs with non-zero %
- [[PDE Parameter Deviation]] [is_a:: [[Failure Mode]]]
- [[PDE Parameter Deviation]] [has_label:: Parameter deviation]
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 8.13%] of total compressor failure rate, rank 5 of 19
- [[PDE Parameter Deviation]] [has_value:: 14] failure mode/item pairs with non-zero %
- [[OTH Other]] [is_a:: [[Failure Mode]]]
- [[OTH Other]] [has_label:: Other]
- [[OTH Other]] [has_failure_rate_share:: 5.46%] of total compressor failure rate, rank 6 of 19
- [[OTH Other]] [has_value:: 25] failure mode/item pairs with non-zero %
- [[ELP External Leakage Process Medium]] [is_a:: [[Failure Mode]]]
- [[ELP External Leakage Process Medium]] [has_label:: External leakage - Process medium]
- [[ELP External Leakage Process Medium]] [has_failure_rate_share:: 4.58%] of total compressor failure rate, rank 7 of 19
- [[ELP External Leakage Process Medium]] [has_value:: 17] failure mode/item pairs with non-zero %
- [[OHE Overheating]] [is_a:: [[Failure Mode]]]
- [[OHE Overheating]] [has_label:: Overheating]
- [[OHE Overheating]] [has_failure_rate_share:: 4.18%] of total compressor failure rate, rank 8 of 19
- [[OHE Overheating]] [has_value:: 12] failure mode/item pairs with non-zero %
- [[UST Spurious Stop]] [is_a:: [[Failure Mode]]]
- [[UST Spurious Stop]] [has_label:: Spurious stop]
- [[UST Spurious Stop]] [has_failure_rate_share:: 4.16%] of total compressor failure rate, rank 9 of 19
- [[UST Spurious Stop]] [has_value:: 22] failure mode/item pairs with non-zero %
- FTS [is_a:: [[Failure Mode]]]
- FTS [has_label:: Fail to start on demand]
- FTS [has_failure_rate_share:: 2.35%] of total compressor failure rate, rank 10 of 19
- FTS [has_value:: 13] failure mode/item pairs with non-zero %
- INL [is_a:: [[Failure Mode]]]
- INL [has_label:: Internal leakage]
- INL [has_failure_rate_share:: 1.97%] of total compressor failure rate, rank 11 of 19
- INL [has_value:: 9] failure mode/item pairs with non-zero %
- ERO [is_a:: [[Failure Mode]]]
- ERO [has_label:: Erratic output]
- ERO [has_failure_rate_share:: 1.50%] of total compressor failure rate, rank 12 of 19
- ERO [has_value:: 6] failure mode/item pairs with non-zero %
- VIB [is_a:: [[Failure Mode]]]
- VIB [has_label:: Vibration]
- VIB [has_failure_rate_share:: 1.42%] of total compressor failure rate, rank 13 of 19
- VIB [has_value:: 15] failure mode/item pairs with non-zero %
- UNK [is_a:: [[Failure Mode]]]
- UNK [has_label:: Unknown]
- UNK [has_failure_rate_share:: 1.07%] of total compressor failure rate, rank 14 of 19
- UNK [has_value:: 9] failure mode/item pairs with non-zero %
- STD [is_a:: [[Failure Mode]]]
- STD [has_label:: Structural deficiency]
- STD [has_failure_rate_share:: 0.81%] of total compressor failure rate, rank 15 of 19
- STD [has_value:: 10] failure mode/item pairs with non-zero %
- NOI [is_a:: [[Failure Mode]]]
- NOI [has_label:: Noise]
- NOI [has_failure_rate_share:: 0.44%] of total compressor failure rate, rank 16 of 19
- NOI [has_value:: 5] failure mode/item pairs with non-zero %
- STP [is_a:: [[Failure Mode]]]
- STP [has_label:: Fail to stop on demand]
- STP [has_failure_rate_share:: 0.34%] of total compressor failure rate, rank 17 of 19
- STP [has_value:: 5] failure mode/item pairs with non-zero %
- HIO [is_a:: [[Failure Mode]]]
- HIO [has_label:: High output]
- HIO [has_failure_rate_share:: 0.21%] of total compressor failure rate, rank 18 of 19
- HIO [has_value:: 4] failure mode/item pairs with non-zero %
- BRD [is_a:: [[Failure Mode]]]
- BRD [has_label:: Breakdown]
- BRD [has_failure_rate_share:: 0.08%] of total compressor failure rate, rank 19 of 19
- BRD [has_value:: 3] failure mode/item pairs with non-zero %
- [[Failure Mode]] [has_value:: 258] total failure mode/item pairs, not unique items
- [[Failure Mode]] [has_failure_rate_share:: 85.66%] total of 19 modes; placeholder items excluded
- Placeholder Items [has_failure_rate_share:: 13.96%] items Other, Subunit, Unknown excluded (Notes); 85.66 + 13.96 = 99.62, gap unexplained except rounding
- [[Failure Mode]] [has_value:: 57.09%] top 5 modes AIR, SER, LOO, ELU, PDE combined; about 66.6% of 85.66 (derived)
- [[Failure Mode]] [has_value:: 20] ISO 14224 Table B.6 compressor (CO) modes, p.187 = these 19 + PLU
- ISO:B.6-PLU [is_a:: [[Failure Mode]]] ISO compressor mode not in OREDA dataset (Table B.6, p.187)
- ISO:B.6-PLU [has_label:: Plugged/choked]
- ISO:B.6-ELF [has_label:: External leakage - fuel]
- ISO:B.6-ELF [applies_to:: CE, GT, ST] only rotating-equipment code not used for CO
- [[Failure Mode]] [related_to:: [[ISO 14224 Taxonomy]]] Table B.6 has a single CO column, no centrifugal/reciprocating/screw split
- [[ISO 14224]] [has_value:: 62] failure mode codes across all equipment classes, Table B.15 p.202-204
- [[ISO 14224]] [has_value:: 14] codes flagged as on-demand type in Table B.15
- FTS [has_category:: On-demand] ISO Table B.15 example
- STP [has_category:: On-demand] ISO Table B.15 example
- [[Failure Mode]] [at_level:: Equipment class] ISO default recording level, subsea also at maintainable item (cl. B.2.6, p.185); scope difference, not contradiction
- [[Failure Mode]] [at_level:: Maintainable item] OREDA dataset ties every mode row to a maintainable item
- [[UST Spurious Stop]] [maps_to:: ISO:B.6-UST] UST is the code ISO 2016 actually uses
- SPS [alias_of:: [[UST Spurious Stop]]] RBMM p.132-134; resolved 2026-10-21, UST primary
- [[Reliability Based Maintenance Management Book]] [related_to:: [[Failure Mode]]] p.132-134 ISO 14224 pump/motor code list matches 18 of 19 codes; differs only SPS vs UST
- [[Failure Mode]] [related_to:: [[Failure Detection Method]]] other field of the failure record
- [[FMECA]] [applies_to:: [[Failure Mode]]] systematic failure mode analysis
- [[PM Task Selection]] [applies_to:: [[Failure Mode]]] PM task selection per failure mode

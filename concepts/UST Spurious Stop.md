---
title: UST Spurious Stop
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [failure-mode, failure-rate, oreda, compressor]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-screw-failure-mode-vs-item-2.png, compressor-centrifugal-failure-mode-vs-item-2.png, reliability-based-maintenance-management.md, iso-14224.md]
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

### ยืนยันจากตัวมาตรฐาน (2026-10-21)

ตอนนี้ตัวมาตรฐานมาตัดสินแล้ว: ISO 14224:2016 ใช้ **UST** สำหรับ Spurious stop (Table B.6 p.187 ครอบคลุม CO และ rotating ทั้ง 8 class; Table B.15 p.202-204) และ **ไม่มีรหัส SPS** ในฉบับ 2016 ดังนั้น SPS ที่พบใน RBMM (p.132-134) เป็นรหัสนอก ISO 2016 หรืออาจมาจากฉบับ/ตัวอย่างเก่า (ข้อหลังเป็นข้อสันนิษฐาน ไม่มีใน sources) การตัดสินของผู้ใช้ให้ UST เป็นหลักสอดคล้องกับมาตรฐาน จึงปรับ confidence ของข้อสรุปนี้เป็นยืนยันแล้ว

หมายเหตุ: มาตรฐานไม่มีรหัส OWD เช่นกัน รหัสใกล้เคียงคือ SPO (Spurious operation) ซึ่งไม่อยู่ใน Table B.6 ของ rotating equipment ดู [[Failure Mode]]

## ที่เกี่ยวข้อง

โหมดที่ใกล้เคียงกันคือ [[AIR Abnormal Instrument Reading]] (instrument) เพราะ trip จาก instrument fault เป็นสาเหตุสำคัญของ UST

## Triplets

- [[UST Spurious Stop]] [is_a:: [[Failure Mode]]]
- [[UST Spurious Stop]] [has_code:: UST]
- [[UST Spurious Stop]] [has_failure_rate_share:: 4.16%] all compressor types, rank 9 of 19
- [[UST Spurious Stop]] [has_value:: 22] failure mode/item pairs
- [[UST Spurious Stop]] [related_to:: [[CTMN Control and Monitoring]]] usually from signal/control system, not direct mechanical damage
- PWTR-INST [contributes_to:: [[UST Spurious Stop]]] 1.92%
- CTMN-CTUN [contributes_to:: [[UST Spurious Stop]]] 0.53%
- CPUN-VALV [contributes_to:: [[UST Spurious Stop]]] 0.29%
- CTMN-IPSU [contributes_to:: [[UST Spurious Stop]]] 0.18%
- LUBS-FILT [contributes_to:: [[UST Spurious Stop]]] 0.15%
- CPUN-CYLN [contributes_to:: [[UST Spurious Stop]]] 0.13%
- [[UST Spurious Stop]] [has_value:: 2.45%] Instruments + Control unit; about 59% of 4.16 (derived)
- [[UST Spurious Stop]] [has_mechanism:: FSIG] Instruments (first row)
- [[UST Spurious Stop]] [has_mechanism:: SWFL] Control unit (first row)
- [[UST Spurious Stop]] [has_mechanism:: BRKG] Valves, broken valve plate/spring (first row)
- [[UST Spurious Stop]] [has_mechanism:: NPWR] Internal power supply (first row)
- [[UST Spurious Stop]] [has_mechanism:: BLKG] Filter(s) (first row)
- [[UST Spurious Stop]] [has_mechanism:: OVHT] Cylinder liner (first row)
- [[UST Spurious Stop]] [has_failure_rate_share:: 6.66%] within [[Centrifugal Compressor]]
- [[UST Spurious Stop]] [has_failure_rate_share:: 2.79%] within [[Reciprocating Compressor]]
- [[UST Spurious Stop]] [has_failure_rate_share:: 11.68%] within [[Screw Compressor]]
- Instrument Temperature [contributes_to:: [[UST Spurious Stop]]] 2.41 within [[Screw Compressor]] (OREDA per-type item)
- Instrument Pressure [contributes_to:: [[UST Spurious Stop]]] 1.72 within [[Screw Compressor]] (OREDA per-type item)
- Unknown [contributes_to:: [[UST Spurious Stop]]] 2.06 within [[Screw Compressor]]; page does not say whether item or descriptor [confidence:: low]
- SPS [alias_of:: [[UST Spurious Stop]]] resolved 2026-10-21 by user; UST is the primary code
- SPS [defined_in:: [[Reliability Based Maintenance Management Book]]] RBMM p.132-134, Fig 5.15/5.17 pump/motor ISO 14224 example
- [[UST Spurious Stop]] [maps_to:: ISO:B.6-UST] ISO 14224:2016 Table B.6 p.187, CO and all 8 rotating classes; also Table B.15 p.202-204
- [[UST Spurious Stop]] [defined_in:: [[ISO 14224]]] 2016 edition has no SPS code
- SPO [has_label:: Spurious operation]
- SPO [related_to:: [[UST Spurious Stop]]] closest ISO code to OWD, which ISO lacks; SPO not in Table B.6 rotating equipment
- [[UST Spurious Stop]] [related_to:: [[AIR Abnormal Instrument Reading]]] trips from instrument faults are a major cause of UST
- [[UST Spurious Stop]] [defined_in:: [[OREDA]]] dataset uses UST

---
title: AIR Abnormal Instrument Reading
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [failure-mode, failure-rate, oreda, compressor]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__summary-by-failure-mode.csv, coce-compressor-failure-mode-vs-item-1.png, compressor-centrifugal-failure-descriptor.png, compressor-reciprocating-failure-descriptor.png, compressor-screw-failure-descriptor.png]
confidence: high
contested: false
---

# AIR - Abnormal instrument reading

โหมดที่ใหญ่ที่สุดใน [[Failure Mode]]: **17.18%** ของ total failure rate (17 คู่ failure mode/item) เป็นปัญหาที่ตัว instrument/สัญญาณ ไม่จำเป็นต้องหมายถึง compressor เสียจริง

## ตัวขับหลัก (OREDA, ทุกประเภทรวม)

| Maintainable Item | Sub Unit (ที่นับ %) | % | Mechanism ที่แสดงในแถวแรก |
|---|---|---|---|
| Instruments | [[PWTR Power Transmission]] | 13.54 | Faulty signal/indication/alarm |
| Monitoring | [[CTMN Control and Monitoring]] | 0.97 | Faulty signal/indication/alarm |
| Control unit | [[CTMN Control and Monitoring]] | 0.84 | Software failure |
| Valves | [[CPUN Compressor Unit]] | 0.66 | Out of adjustment |
| Antisurge system | [[CPUN Compressor Unit]] | 0.22 | Faulty signal/indication/alarm |
| Cabling & junction boxes | [[CTMN Control and Monitoring]] | 0.22 | Open circuit |
| Internal power supply | [[CTMN Control and Monitoring]] | 0.22 | No power/ voltage |

Item ที่เหลือ (10 คู่) แต่ละตัว <= 0.13 ผลรวมทั้ง 17 คู่ = 17.18 (ตรงกับ summary)

Instruments เดียวคิดเป็น 13.54 จาก 17.18 (derived: ประมาณ 79%) ค่านี้ถูกนับที่ PWTR เพราะ Instruments ปรากฏหลาย sub unit แต่ % นับครั้งเดียว (ดู [[PWTR Power Transmission]])

## แยกตามประเภท compressor (total ของโหมด AIR)

| Centrifugal | Reciprocating | Screw |
|---|---|---|
| 27.52 | 9.22 | 22.68 |

Failure descriptor ที่สูงสุด: centrifugal = Faulty signal/indication/alarm 8.10, Out of adjustment 6.88, Instrument failure - general 4.11; reciprocating = Instrument failure - general 6.52; screw = Instrument failure - general 12.03, Out of adjustment 3.09 ดู [[Compressor Type Failure Profiles]]

## Resolution ที่ dataset เสนอ

Mechanism ฝั่ง instrument มักจับคู่กับ Adjust (recalibrate), Check (loop check), Replace (transmitter/sensor), Test; ดู [[Resolution Codes]] และ [[Resolution Matrix by Mechanism]]

## Triplets

- [[AIR Abnormal Instrument Reading]] [is_a:: [[Failure Mode]]]
- [[AIR Abnormal Instrument Reading]] [has_code:: AIR]
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 17.18%] all compressor types, largest of 19 modes
- [[AIR Abnormal Instrument Reading]] [has_value:: 17] failure mode/item pairs
- PWTR-INST [contributes_to:: [[AIR Abnormal Instrument Reading]]] 13.54%; about 79% of AIR (derived); counted once at PWTR
- CTMN-MONI [contributes_to:: [[AIR Abnormal Instrument Reading]]] 0.97%
- CTMN-CTUN [contributes_to:: [[AIR Abnormal Instrument Reading]]] 0.84%
- CPUN-VALV [contributes_to:: [[AIR Abnormal Instrument Reading]]] 0.66%
- CPUN-ASRG [contributes_to:: [[AIR Abnormal Instrument Reading]]] 0.22%
- CTMN-CBJB [contributes_to:: [[AIR Abnormal Instrument Reading]]] 0.22%
- CTMN-IPSU [contributes_to:: [[AIR Abnormal Instrument Reading]]] 0.22%
- [[AIR Abnormal Instrument Reading]] [has_value:: 0.13%] max share of each of the remaining 10 pairs
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: FSIG] Instruments, Monitoring, Antisurge system (first row)
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: SWFL] Control unit (first row)
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: OADJ] Valves (first row)
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: OPEN] Cabling & junction boxes (first row)
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: NPWR] Internal power supply (first row)
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 27.52%] within [[Centrifugal Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 9.22%] within [[Reciprocating Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 22.68%] within [[Screw Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: FSIG] failure descriptor 8.10 within [[Centrifugal Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: OADJ] failure descriptor 6.88 within [[Centrifugal Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: Instrument failure - general] Instrument failure - general, failure descriptor 4.11 within [[Centrifugal Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: Instrument failure - general] Instrument failure - general, failure descriptor 6.52 within [[Reciprocating Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: Instrument failure - general] Instrument failure - general, failure descriptor 12.03 within [[Screw Compressor]]
- [[AIR Abnormal Instrument Reading]] [has_mechanism:: OADJ] failure descriptor 3.09 within [[Screw Compressor]]
- [[AIR Abnormal Instrument Reading]] [resolved_by:: ADJ] recalibrate; instrument-side mechanisms
- [[AIR Abnormal Instrument Reading]] [resolved_by:: CHK] loop check
- [[AIR Abnormal Instrument Reading]] [resolved_by:: RPL] transmitter/sensor
- [[AIR Abnormal Instrument Reading]] [resolved_by:: TST]
- [[AIR Abnormal Instrument Reading]] [defined_in:: [[OREDA]]]

---
title: AIR Abnormal Instrument Reading
created: 2026-10-20
updated: 2026-10-20
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

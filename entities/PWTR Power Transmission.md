---
title: PWTR Power Transmission
created: 2026-10-20
updated: 2026-10-20
type: entity
tags: [sub-unit, maintainable-item, compressor, failure-rate]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__sheet5.csv, compressor-failure-hierarchy__subunit-code.csv, failure-structure__sheet1.csv]
confidence: medium
contested: true
---

# PWTR - Power transmission

Sub Unit ระดับ 2 ของ [[Failure Hierarchy]] ส่งกำลังจาก driver ไปยัง [[Compressor]] (coupling, gearbox/variable drive, bearing, seal, lubrication ของส่วนนี้) รหัส `PWTR`

## Maintainable items (7) และ mechanism codes

| Code | Item | จำนวน CAUSE_CODE | Mechanism codes |
|---|---|---|---|
| INST | Instruments | 18 | FSIG OADJ OPEN EART LEAK BLKG CTMN EROS NSIG NCFD STCK ALGN OVHT LOOS CORR OTHR UNKN VIBR |
| GBVD | Gearbox/var.drive | 8 | FSIG LEAK LOOS WEAR ALGN CTMN OTHR OVHT |
| CPDR | Coupling to driver | 5 | ALGN WEAR LEAK FATG LOOS |
| CPDN | Coupling to driven unit | 5 | LEAK ALGN WEAR FATG LOOS |
| SEAL | Seals | 4 | WEAR LEAK MATF ALGN |
| BRNG | Bearing | 8 | LEAK WEAR OVHT CTMN LOOS OTHR ALGN FATG |
| LUBR | Lubrication | 2 | LEAK FATG |

รวม 50 CAUSE_CODE ดู [[Failure Cause Codes]] และ [[CAUSE_CODE Convention]]

## Failure modes ที่เด่น (% นับที่ PWTR, derived = ผลรวมแถวที่ `Count in Total = 1`)

ผลรวมที่นับใน PWTR = **25.64** จาก 85.66 แบ่งตามโหมด: AIR 13.63, PDE 3.35, ELU 1.98, UST 1.96, SER 1.19, OTH 0.99, FTS 0.73, VIB 0.70

คู่เด่น: Instruments x AIR 13.54 (Faulty signal/indication/alarm), Instruments x PDE 3.35, Instruments x UST 1.92, Instruments x SER 1.02 (Looseness) ดู [[AIR Abnormal Instrument Reading]], [[PDE Parameter Deviation]], [[UST Spurious Stop]]

## ข้อควรระวัง (contested)

- **Instruments ถูกนับที่ PWTR ทั้งก้อน**: Instruments ปรากฏใน 5 sub unit แต่ OREDA ให้ % เดียวต่อคู่ mode/item dataset จึงนับ % ที่ sub unit แรก (PWTR) ผลรวมของ Instruments ทุกโหมด = 23.34 (derived) ดังนั้น PWTR ที่ไม่รวม Instruments = 2.30 ตัวเลข 25.64 จึงไม่ได้สะท้อน power transmission จริง
- `failure-structure.md` (Sheet1) จัด Instrument types ไว้ใน Control and Monitoring เท่านั้น ขัดกับ dataset หลัก ดู [[CTMN Control and Monitoring]] และตารางความขัดแย้งใน [[Failure Hierarchy]]
- การเปรียบเทียบ source ทั้งสอง: Bearing, Gearbox, Couplings, Seals สอดคล้องกัน (PWTR)

## Top failure mechanisms

Instruments: Faulty signal/indication/alarm; ส่วน mechanical items: Leakage (ELU: Seals Wear 0.35, Coupling to driven unit Leakage 0.24, Bearing Leakage 0.18, Gearbox Leakage 0.15), Clearance/ alignment failure (couplings; VIB/ERO), Wear (Gearbox)

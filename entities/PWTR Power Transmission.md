---
title: PWTR Power Transmission
created: 2026-10-20
updated: 2026-10-22
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

## Triplets

- [[PWTR Power Transmission]] [is_a:: Sub Unit]
- [[PWTR Power Transmission]] [part_of:: [[Compressor]]]
- [[PWTR Power Transmission]] [has_code:: PWTR]
- [[PWTR Power Transmission]] [at_level:: 2] of [[Failure Hierarchy]]
- [[PWTR Power Transmission]] [has_value:: 7] maintainable items
- [[PWTR Power Transmission]] [has_value:: 50] CAUSE_CODE
- [[PWTR Power Transmission]] [has_failure_rate_share:: 25.64%] counted at PWTR (derived), of 85.66, includes all Instruments
- [[PWTR Power Transmission]] [has_failure_rate_share:: 2.30%] excluding Instruments (derived)
- PWTR-INST [part_of:: [[PWTR Power Transmission]]] main dataset; Instruments % for all 5 sub units counted here as first sub unit [contested:: true]
- PWTR-INST [is_a:: INST]
- PWTR-INST [has_value:: 18] CAUSE_CODE
- PWTR-INST [has_mechanism:: FSIG]
- PWTR-INST [has_mechanism:: OADJ]
- PWTR-INST [has_mechanism:: OPEN]
- PWTR-INST [has_mechanism:: EART]
- PWTR-INST [has_mechanism:: LEAK]
- PWTR-INST [has_mechanism:: BLKG]
- PWTR-INST [has_mechanism:: CTMN]
- PWTR-INST [has_mechanism:: EROS]
- PWTR-INST [has_mechanism:: NSIG]
- PWTR-INST [has_mechanism:: NCFD]
- PWTR-INST [has_mechanism:: STCK]
- PWTR-INST [has_mechanism:: ALGN]
- PWTR-INST [has_mechanism:: OVHT]
- PWTR-INST [has_mechanism:: LOOS]
- PWTR-INST [has_mechanism:: CORR]
- PWTR-INST [has_mechanism:: OTHR]
- PWTR-INST [has_mechanism:: UNKN]
- PWTR-INST [has_mechanism:: VIBR]
- PWTR-GBVD [part_of:: [[PWTR Power Transmission]]] both sources agree
- PWTR-GBVD [is_a:: GBVD]
- PWTR-GBVD [has_value:: 8] CAUSE_CODE
- PWTR-GBVD [has_mechanism:: FSIG]
- PWTR-GBVD [has_mechanism:: LEAK]
- PWTR-GBVD [has_mechanism:: LOOS]
- PWTR-GBVD [has_mechanism:: WEAR]
- PWTR-GBVD [has_mechanism:: ALGN]
- PWTR-GBVD [has_mechanism:: CTMN]
- PWTR-GBVD [has_mechanism:: OTHR]
- PWTR-GBVD [has_mechanism:: OVHT]
- PWTR-CPDR [part_of:: [[PWTR Power Transmission]]] both sources agree
- PWTR-CPDR [is_a:: CPDR]
- PWTR-CPDR [has_value:: 5] CAUSE_CODE
- PWTR-CPDR [has_mechanism:: ALGN]
- PWTR-CPDR [has_mechanism:: WEAR]
- PWTR-CPDR [has_mechanism:: LEAK]
- PWTR-CPDR [has_mechanism:: FATG]
- PWTR-CPDR [has_mechanism:: LOOS]
- PWTR-CPDN [part_of:: [[PWTR Power Transmission]]] both sources agree
- PWTR-CPDN [is_a:: CPDN]
- PWTR-CPDN [has_value:: 5] CAUSE_CODE
- PWTR-CPDN [has_mechanism:: LEAK]
- PWTR-CPDN [has_mechanism:: ALGN]
- PWTR-CPDN [has_mechanism:: WEAR]
- PWTR-CPDN [has_mechanism:: FATG]
- PWTR-CPDN [has_mechanism:: LOOS]
- PWTR-SEAL [part_of:: [[PWTR Power Transmission]]] both sources agree
- PWTR-SEAL [is_a:: SEAL]
- PWTR-SEAL [has_value:: 4] CAUSE_CODE
- PWTR-SEAL [has_mechanism:: WEAR]
- PWTR-SEAL [has_mechanism:: LEAK]
- PWTR-SEAL [has_mechanism:: MATF]
- PWTR-SEAL [has_mechanism:: ALGN]
- PWTR-BRNG [part_of:: [[PWTR Power Transmission]]] both sources agree
- PWTR-BRNG [is_a:: BRNG]
- PWTR-BRNG [has_value:: 8] CAUSE_CODE
- PWTR-BRNG [has_mechanism:: LEAK]
- PWTR-BRNG [has_mechanism:: WEAR]
- PWTR-BRNG [has_mechanism:: OVHT]
- PWTR-BRNG [has_mechanism:: CTMN]
- PWTR-BRNG [has_mechanism:: LOOS]
- PWTR-BRNG [has_mechanism:: OTHR]
- PWTR-BRNG [has_mechanism:: ALGN]
- PWTR-BRNG [has_mechanism:: FATG]
- PWTR-LUBR [part_of:: [[PWTR Power Transmission]]]
- PWTR-LUBR [is_a:: LUBR]
- PWTR-LUBR [has_value:: 2] CAUSE_CODE
- PWTR-LUBR [has_mechanism:: LEAK]
- PWTR-LUBR [has_mechanism:: FATG]
- INST [part_of:: [[CTMN Control and Monitoring]]] failure-structure.md Sheet1, instrument types only in CTMN [contested:: true]
- PWTR-INST [has_failure_rate_share:: 23.34%] all modes (derived)
- [[PWTR Power Transmission]] [contributes_to:: [[AIR Abnormal Instrument Reading]]] 13.63% counted at PWTR (derived), of 85.66
- [[PWTR Power Transmission]] [contributes_to:: [[PDE Parameter Deviation]]] 3.35% counted at PWTR (derived), of 85.66
- [[PWTR Power Transmission]] [contributes_to:: [[ELU External Leakage Utility Medium]]] 1.98% counted at PWTR (derived), of 85.66
- [[PWTR Power Transmission]] [contributes_to:: [[UST Spurious Stop]]] 1.96% counted at PWTR (derived), of 85.66
- [[PWTR Power Transmission]] [contributes_to:: [[SER Minor In-Service Problems]]] 1.19% counted at PWTR (derived), of 85.66
- [[PWTR Power Transmission]] [contributes_to:: [[OTH Other]]] 0.99% counted at PWTR (derived), of 85.66
- [[PWTR Power Transmission]] [contributes_to:: FTS] 0.73% counted at PWTR (derived), of 85.66
- [[PWTR Power Transmission]] [contributes_to:: VIB] 0.70% counted at PWTR (derived), of 85.66
- PWTR-INST [contributes_to:: [[AIR Abnormal Instrument Reading]]] 13.54% (Faulty signal/indication/alarm)
- PWTR-INST [contributes_to:: [[PDE Parameter Deviation]]] 3.35%
- PWTR-INST [contributes_to:: [[UST Spurious Stop]]] 1.92%
- PWTR-INST [contributes_to:: [[SER Minor In-Service Problems]]] 1.02% (Looseness)
- PWTR-SEAL [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.35% (Wear)
- PWTR-CPDN [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.24% (Leakage)
- PWTR-BRNG [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.18% (Leakage)
- PWTR-GBVD [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.15% (Leakage)
- [[PWTR Power Transmission]] [has_mechanism:: FSIG] top mechanism; Instruments
- [[PWTR Power Transmission]] [has_mechanism:: LEAK] top mechanism; mechanical items, ELU
- [[PWTR Power Transmission]] [has_mechanism:: ALGN] top mechanism; couplings, VIB/ERO
- [[PWTR Power Transmission]] [has_mechanism:: WEAR] top mechanism; gearbox

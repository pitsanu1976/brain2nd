---
title: LUBS Lubrication System
created: 2026-10-20
updated: 2026-10-20
type: entity
tags: [sub-unit, maintainable-item, compressor, failure-rate]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__sheet5.csv, compressor-failure-hierarchy__subunit-code.csv, failure-structure__sheet1.csv]
confidence: medium
contested: true
---

# LUBS - Lubrication system

Sub Unit ของ [[Compressor]] ที่จ่ายและปรับสภาพน้ำมันหล่อลื่น (oil tank/reservoir, pump, filter, cooler, piping) รหัส `LUBS`

## Maintainable items (11) และ mechanism codes

| Code | Item | จำนวน CAUSE_CODE | Mechanism codes |
|---|---|---|---|
| INST | Instruments | 18 | FSIG OADJ OPEN EART LEAK BLKG CTMN EROS NSIG NCFD STCK ALGN OVHT LOOS CORR OTHR UNKN VIBR |
| VALV | Valves | 16 | OADJ FSIG STCK LEAK EROS CORR WEAR BRKG CAVT BLKG CTMN LOOS VIBR OTHR FATG UNKN |
| LUBE | Lube oil | 5 | CTMN FSIG LEAK MATF OTHR |
| OILS | Oil | 5 | LEAK CTMN MATF OTHR UNKN |
| RSHT | Reservoir w/heating system | 5 | ELEC FSIG LEAK CORR CTMN |
| OTHT | Oil tank w/heating system | 6 | ELEC FSIG LEAK CORR CTMN OTHR |
| FILT | Filter(s) | 9 | FSIG LEAK BLKG BRKG BRST CTMN STCK OTHR UNKN |
| PMTR | Pump w/motor | 12 | LEAK ELEC CTRL WEAR CAVT BLKG OADJ LOOS OTHR ALGN OVHT UNKN |
| PIPE | Piping | 6 | CORR FATG EROS LEAK BRST LOOS |
| COOL | Cooler(s) | 11 | CORR EROS FATG BRST WEAR LOOS OTHR BLKG ELEC OADJ MEXT |
| SEAL | Seals | 4 | WEAR LEAK MATF ALGN |

รวม 97 CAUSE_CODE ดู [[Failure Cause Codes]] (ข้อสังเกต: item `Lubrication` (LUBR) อยู่ใน [[PWTR Power Transmission]])

## Failure modes ที่เด่น (% นับที่ LUBS, derived)

ผลรวม **15.55** จาก 85.66: SER 7.85, LOO 1.72, ELU 1.39, INL 1.28, OTH 0.88, PDE 0.83, UST 0.43

คู่เด่น: **Filter(s) x SER 7.33** (Blockage/plugged, element clogged high DP) ซึ่งเป็นคู่ที่ใหญ่เป็นอันดับ 2 ของทั้ง dataset, Pump w/motor x LOO 1.32 (Wear), Oil x INL 1.24 (Contamination: process gas/water ingress จาก seal หรือ cooler tube leak) Filter(s) ทุกโหมดรวม 8.95 (derived) ดู [[SER Minor In-Service Problems]], [[LOO Low Output]]

## Top failure mechanisms

Blockage/plugged (filters), Wear (pump), Contamination (oil), Leakage (pump seals, oil, tanks), Corrosion (cooler/piping)

## ข้อควรระวัง (contested)

- Instruments และ Valves ของ LUBS ไม่มี % แยก (นับที่ PWTR และ CPUN) ผลรวม 15.55 จึงไม่รวมสองรายการนี้
- Filter(s) ถูกจับคู่กับ LUBS และ SHSS; Cooler(s) กับ LUBS และ MISC; Piping กับ CPUN, LUBS, MISC; ดู [[Maintainable Item]] `failure-structure.md` จัด Filter(s) ใน Lubrication system เหมือนกัน แต่จัด Piping ไว้ใน Miscellaneous ดู [[Failure Hierarchy]]

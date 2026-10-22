---
title: LUBS Lubrication System
created: 2026-10-20
updated: 2026-10-22
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

## Triplets

- [[LUBS Lubrication System]] [is_a:: Sub Unit]
- [[LUBS Lubrication System]] [part_of:: [[Compressor]]]
- [[LUBS Lubrication System]] [has_code:: LUBS]
- [[LUBS Lubrication System]] [has_value:: 11] maintainable items
- [[LUBS Lubrication System]] [has_value:: 97] CAUSE_CODE
- [[LUBS Lubrication System]] [has_failure_rate_share:: 15.55%] counted at LUBS (derived), of 85.66, excludes Instruments and Valves
- LUBS-INST [part_of:: [[LUBS Lubrication System]]] % counted at PWTR
- LUBS-INST [is_a:: INST]
- LUBS-INST [has_value:: 18] CAUSE_CODE
- LUBS-INST [has_mechanism:: FSIG]
- LUBS-INST [has_mechanism:: OADJ]
- LUBS-INST [has_mechanism:: OPEN]
- LUBS-INST [has_mechanism:: EART]
- LUBS-INST [has_mechanism:: LEAK]
- LUBS-INST [has_mechanism:: BLKG]
- LUBS-INST [has_mechanism:: CTMN]
- LUBS-INST [has_mechanism:: EROS]
- LUBS-INST [has_mechanism:: NSIG]
- LUBS-INST [has_mechanism:: NCFD]
- LUBS-INST [has_mechanism:: STCK]
- LUBS-INST [has_mechanism:: ALGN]
- LUBS-INST [has_mechanism:: OVHT]
- LUBS-INST [has_mechanism:: LOOS]
- LUBS-INST [has_mechanism:: CORR]
- LUBS-INST [has_mechanism:: OTHR]
- LUBS-INST [has_mechanism:: UNKN]
- LUBS-INST [has_mechanism:: VIBR]
- LUBS-VALV [part_of:: [[LUBS Lubrication System]]] % counted at CPUN
- LUBS-VALV [is_a:: VALV]
- LUBS-VALV [has_value:: 16] CAUSE_CODE
- LUBS-VALV [has_mechanism:: OADJ]
- LUBS-VALV [has_mechanism:: FSIG]
- LUBS-VALV [has_mechanism:: STCK]
- LUBS-VALV [has_mechanism:: LEAK]
- LUBS-VALV [has_mechanism:: EROS]
- LUBS-VALV [has_mechanism:: CORR]
- LUBS-VALV [has_mechanism:: WEAR]
- LUBS-VALV [has_mechanism:: BRKG]
- LUBS-VALV [has_mechanism:: CAVT]
- LUBS-VALV [has_mechanism:: BLKG]
- LUBS-VALV [has_mechanism:: CTMN]
- LUBS-VALV [has_mechanism:: LOOS]
- LUBS-VALV [has_mechanism:: VIBR]
- LUBS-VALV [has_mechanism:: OTHR]
- LUBS-VALV [has_mechanism:: FATG]
- LUBS-VALV [has_mechanism:: UNKN]
- LUBS-LUBE [part_of:: [[LUBS Lubrication System]]]
- LUBS-LUBE [is_a:: LUBE]
- LUBS-LUBE [has_value:: 5] CAUSE_CODE
- LUBS-LUBE [has_mechanism:: CTMN]
- LUBS-LUBE [has_mechanism:: FSIG]
- LUBS-LUBE [has_mechanism:: LEAK]
- LUBS-LUBE [has_mechanism:: MATF]
- LUBS-LUBE [has_mechanism:: OTHR]
- LUBS-OILS [part_of:: [[LUBS Lubrication System]]]
- LUBS-OILS [is_a:: OILS]
- LUBS-OILS [has_value:: 5] CAUSE_CODE
- LUBS-OILS [has_mechanism:: LEAK]
- LUBS-OILS [has_mechanism:: CTMN]
- LUBS-OILS [has_mechanism:: MATF]
- LUBS-OILS [has_mechanism:: OTHR]
- LUBS-OILS [has_mechanism:: UNKN]
- LUBS-RSHT [part_of:: [[LUBS Lubrication System]]]
- LUBS-RSHT [is_a:: RSHT]
- LUBS-RSHT [has_value:: 5] CAUSE_CODE
- LUBS-RSHT [has_mechanism:: ELEC]
- LUBS-RSHT [has_mechanism:: FSIG]
- LUBS-RSHT [has_mechanism:: LEAK]
- LUBS-RSHT [has_mechanism:: CORR]
- LUBS-RSHT [has_mechanism:: CTMN]
- LUBS-OTHT [part_of:: [[LUBS Lubrication System]]]
- LUBS-OTHT [is_a:: OTHT]
- LUBS-OTHT [has_value:: 6] CAUSE_CODE
- LUBS-OTHT [has_mechanism:: ELEC]
- LUBS-OTHT [has_mechanism:: FSIG]
- LUBS-OTHT [has_mechanism:: LEAK]
- LUBS-OTHT [has_mechanism:: CORR]
- LUBS-OTHT [has_mechanism:: CTMN]
- LUBS-OTHT [has_mechanism:: OTHR]
- LUBS-FILT [part_of:: [[LUBS Lubrication System]]] also mapped to SHSS; failure-structure.md Sheet1 agrees on LUBS
- LUBS-FILT [is_a:: FILT]
- LUBS-FILT [has_value:: 9] CAUSE_CODE
- LUBS-FILT [has_mechanism:: FSIG]
- LUBS-FILT [has_mechanism:: LEAK]
- LUBS-FILT [has_mechanism:: BLKG]
- LUBS-FILT [has_mechanism:: BRKG]
- LUBS-FILT [has_mechanism:: BRST]
- LUBS-FILT [has_mechanism:: CTMN]
- LUBS-FILT [has_mechanism:: STCK]
- LUBS-FILT [has_mechanism:: OTHR]
- LUBS-FILT [has_mechanism:: UNKN]
- LUBS-PMTR [part_of:: [[LUBS Lubrication System]]]
- LUBS-PMTR [is_a:: PMTR]
- LUBS-PMTR [has_value:: 12] CAUSE_CODE
- LUBS-PMTR [has_mechanism:: LEAK]
- LUBS-PMTR [has_mechanism:: ELEC]
- LUBS-PMTR [has_mechanism:: CTRL]
- LUBS-PMTR [has_mechanism:: WEAR]
- LUBS-PMTR [has_mechanism:: CAVT]
- LUBS-PMTR [has_mechanism:: BLKG]
- LUBS-PMTR [has_mechanism:: OADJ]
- LUBS-PMTR [has_mechanism:: LOOS]
- LUBS-PMTR [has_mechanism:: OTHR]
- LUBS-PMTR [has_mechanism:: ALGN]
- LUBS-PMTR [has_mechanism:: OVHT]
- LUBS-PMTR [has_mechanism:: UNKN]
- LUBS-PIPE [part_of:: [[LUBS Lubrication System]]] main dataset; also mapped to CPUN and MISC [contested:: true]
- LUBS-PIPE [is_a:: PIPE]
- LUBS-PIPE [has_value:: 6] CAUSE_CODE
- LUBS-PIPE [has_mechanism:: CORR]
- LUBS-PIPE [has_mechanism:: FATG]
- LUBS-PIPE [has_mechanism:: EROS]
- LUBS-PIPE [has_mechanism:: LEAK]
- LUBS-PIPE [has_mechanism:: BRST]
- LUBS-PIPE [has_mechanism:: LOOS]
- LUBS-COOL [part_of:: [[LUBS Lubrication System]]] also mapped to MISC
- LUBS-COOL [is_a:: COOL]
- LUBS-COOL [has_value:: 11] CAUSE_CODE
- LUBS-COOL [has_mechanism:: CORR]
- LUBS-COOL [has_mechanism:: EROS]
- LUBS-COOL [has_mechanism:: FATG]
- LUBS-COOL [has_mechanism:: BRST]
- LUBS-COOL [has_mechanism:: WEAR]
- LUBS-COOL [has_mechanism:: LOOS]
- LUBS-COOL [has_mechanism:: OTHR]
- LUBS-COOL [has_mechanism:: BLKG]
- LUBS-COOL [has_mechanism:: ELEC]
- LUBS-COOL [has_mechanism:: OADJ]
- LUBS-COOL [has_mechanism:: MEXT]
- LUBS-SEAL [part_of:: [[LUBS Lubrication System]]]
- LUBS-SEAL [is_a:: SEAL]
- LUBS-SEAL [has_value:: 4] CAUSE_CODE
- LUBS-SEAL [has_mechanism:: WEAR]
- LUBS-SEAL [has_mechanism:: LEAK]
- LUBS-SEAL [has_mechanism:: MATF]
- LUBS-SEAL [has_mechanism:: ALGN]
- PIPE [part_of:: [[MISC Miscellaneous]]] failure-structure.md Sheet1 [contested:: true]
- PWTR-LUBR [part_of:: [[PWTR Power Transmission]]] item Lubrication is not in LUBS
- [[LUBS Lubrication System]] [contributes_to:: [[SER Minor In-Service Problems]]] 7.85% counted at LUBS (derived), of 85.66
- [[LUBS Lubrication System]] [contributes_to:: [[LOO Low Output]]] 1.72% counted at LUBS (derived), of 85.66
- [[LUBS Lubrication System]] [contributes_to:: [[ELU External Leakage Utility Medium]]] 1.39% counted at LUBS (derived), of 85.66
- [[LUBS Lubrication System]] [contributes_to:: INL] 1.28% counted at LUBS (derived), of 85.66
- [[LUBS Lubrication System]] [contributes_to:: [[OTH Other]]] 0.88% counted at LUBS (derived), of 85.66
- [[LUBS Lubrication System]] [contributes_to:: [[PDE Parameter Deviation]]] 0.83% counted at LUBS (derived), of 85.66
- [[LUBS Lubrication System]] [contributes_to:: [[UST Spurious Stop]]] 0.43% counted at LUBS (derived), of 85.66
- LUBS-FILT [contributes_to:: [[SER Minor In-Service Problems]]] 7.33% (Blockage/plugged, element clogged high DP); 2nd largest pair in dataset
- LUBS-PMTR [contributes_to:: [[LOO Low Output]]] 1.32% (Wear)
- LUBS-OILS [contributes_to:: INL] 1.24% (Contamination, process gas/water ingress from seal or cooler tube leak)
- LUBS-FILT [has_failure_rate_share:: 8.95%] all modes (derived)
- [[LUBS Lubrication System]] [has_mechanism:: BLKG] top mechanism; filters
- [[LUBS Lubrication System]] [has_mechanism:: WEAR] top mechanism; pump
- [[LUBS Lubrication System]] [has_mechanism:: CTMN] top mechanism; oil
- [[LUBS Lubrication System]] [has_mechanism:: LEAK] top mechanism; pump seals, oil, tanks
- [[LUBS Lubrication System]] [has_mechanism:: CORR] top mechanism; cooler/piping

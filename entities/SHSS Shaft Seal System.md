---
title: SHSS Shaft Seal System
created: 2026-10-20
updated: 2026-10-22
type: entity
tags: [sub-unit, maintainable-item, compressor, failure-rate]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__sheet5.csv, compressor-failure-hierarchy__subunit-code.csv, failure-structure__sheet1.csv]
confidence: medium
contested: true
---

# SHSS - Shaft seal system

Sub Unit ของ [[Compressor]] ที่สนับสนุน shaft seal (seal oil, seal gas, buffer gas, dry gas seal, overhead tank, pump) รหัส `SHSS` ส่วน item `Shaft seals` (SHSL) ตัวซีลเองอยู่ใน [[CPUN Compressor Unit]]

## Maintainable items (10) และ mechanism codes

| Code | Item | จำนวน CAUSE_CODE | Mechanism codes |
|---|---|---|---|
| INST | Instruments | 18 | FSIG OADJ OPEN EART LEAK BLKG CTMN EROS NSIG NCFD STCK ALGN OVHT LOOS CORR OTHR UNKN VIBR |
| VALV | Valves | 16 | OADJ FSIG STCK LEAK EROS CORR WEAR BRKG CAVT BLKG CTMN LOOS VIBR OTHR FATG UNKN |
| RSHT | Reservoir w/heating system | 5 | ELEC FSIG LEAK CORR CTMN |
| SOIL | Seal oil | 6 | FSIG LEAK CTMN BLKG MATF OTHR |
| FILT | Filter(s) | 9 | FSIG LEAK BLKG BRKG BRST CTMN STCK OTHR UNKN |
| SGAS | Seal gas | 3 | LEAK CORR OTHR |
| PMGR | Pump w/motor/gear | 11 | LEAK ELEC CTRL WEAR CAVT BLKG OADJ LOOS ALGN OTHR OVHT |
| DGSL | Dry gas seal | 5 | LEAK WEAR CTMN BRKG OTHR |
| BFGS | Buffer gas system | 3 | LEAK BLKG OADJ |
| OHTK | Overhead tank | 2 | LEAK CORR |

รวม 78 CAUSE_CODE ดู [[Failure Cause Codes]]

## Failure modes ที่เด่น (% นับที่ SHSS, derived)

ผลรวมเพียง **2.60** จาก 85.66 (เล็กที่สุดอันดับ 2): ELU 0.96, OTH 0.61, NOI 0.18, LOO 0.17, ELP 0.13, VIB 0.13

คู่เด่น: Pump w/motor/gear x OTH 0.44, Pump w/motor/gear x ELU 0.40 (mechanical seal leak), Seal oil x ELU 0.35, Seal gas x ELP 0.13 ดู [[ELU External Leakage Utility Medium]]

## Top failure mechanisms

Leakage (seal oil, seal gas, dry gas seal, tanks), Wear (pump), Other

## ข้อควรระวัง (contested)

- Instruments และ Valves ใน SHSS ไม่มี % แยก (นับที่ [[PWTR Power Transmission]] / [[CPUN Compressor Unit]])
- % ต่ำของ SHSS สะท้อนว่า item เป็นระบบของ centrifugal เป็นหลัก ซึ่งในภาพ OREDA ต่อประเภทเป็นสัดส่วนเล็ก (เช่น Seal oil Sum 1.44, Dry gas seal Sum 0.22 ใน centrifugal) ข้อนี้เป็นการตีความ
- `failure-structure.md` จัด Pump w/motor/gear ใน Shaft seal system เหมือนกัน (สอดคล้อง)

## Triplets

- [[SHSS Shaft Seal System]] [is_a:: Sub Unit]
- [[SHSS Shaft Seal System]] [part_of:: [[Compressor]]]
- [[SHSS Shaft Seal System]] [has_code:: SHSS]
- [[SHSS Shaft Seal System]] [has_value:: 10] maintainable items
- [[SHSS Shaft Seal System]] [has_value:: 78] CAUSE_CODE
- [[SHSS Shaft Seal System]] [has_failure_rate_share:: 2.60%] counted at SHSS (derived), of 85.66, 2nd smallest sub unit
- CPUN-SHSL [part_of:: [[CPUN Compressor Unit]]] shaft seal itself is in CPUN, not SHSS
- SHSS-INST [part_of:: [[SHSS Shaft Seal System]]] % counted at PWTR
- SHSS-INST [is_a:: INST]
- SHSS-INST [has_value:: 18] CAUSE_CODE
- SHSS-INST [has_mechanism:: FSIG]
- SHSS-INST [has_mechanism:: OADJ]
- SHSS-INST [has_mechanism:: OPEN]
- SHSS-INST [has_mechanism:: EART]
- SHSS-INST [has_mechanism:: LEAK]
- SHSS-INST [has_mechanism:: BLKG]
- SHSS-INST [has_mechanism:: CTMN]
- SHSS-INST [has_mechanism:: EROS]
- SHSS-INST [has_mechanism:: NSIG]
- SHSS-INST [has_mechanism:: NCFD]
- SHSS-INST [has_mechanism:: STCK]
- SHSS-INST [has_mechanism:: ALGN]
- SHSS-INST [has_mechanism:: OVHT]
- SHSS-INST [has_mechanism:: LOOS]
- SHSS-INST [has_mechanism:: CORR]
- SHSS-INST [has_mechanism:: OTHR]
- SHSS-INST [has_mechanism:: UNKN]
- SHSS-INST [has_mechanism:: VIBR]
- SHSS-VALV [part_of:: [[SHSS Shaft Seal System]]] % counted at CPUN
- SHSS-VALV [is_a:: VALV]
- SHSS-VALV [has_value:: 16] CAUSE_CODE
- SHSS-VALV [has_mechanism:: OADJ]
- SHSS-VALV [has_mechanism:: FSIG]
- SHSS-VALV [has_mechanism:: STCK]
- SHSS-VALV [has_mechanism:: LEAK]
- SHSS-VALV [has_mechanism:: EROS]
- SHSS-VALV [has_mechanism:: CORR]
- SHSS-VALV [has_mechanism:: WEAR]
- SHSS-VALV [has_mechanism:: BRKG]
- SHSS-VALV [has_mechanism:: CAVT]
- SHSS-VALV [has_mechanism:: BLKG]
- SHSS-VALV [has_mechanism:: CTMN]
- SHSS-VALV [has_mechanism:: LOOS]
- SHSS-VALV [has_mechanism:: VIBR]
- SHSS-VALV [has_mechanism:: OTHR]
- SHSS-VALV [has_mechanism:: FATG]
- SHSS-VALV [has_mechanism:: UNKN]
- SHSS-RSHT [part_of:: [[SHSS Shaft Seal System]]]
- SHSS-RSHT [is_a:: RSHT]
- SHSS-RSHT [has_value:: 5] CAUSE_CODE
- SHSS-RSHT [has_mechanism:: ELEC]
- SHSS-RSHT [has_mechanism:: FSIG]
- SHSS-RSHT [has_mechanism:: LEAK]
- SHSS-RSHT [has_mechanism:: CORR]
- SHSS-RSHT [has_mechanism:: CTMN]
- SHSS-SOIL [part_of:: [[SHSS Shaft Seal System]]]
- SHSS-SOIL [is_a:: SOIL]
- SHSS-SOIL [has_value:: 6] CAUSE_CODE
- SHSS-SOIL [has_mechanism:: FSIG]
- SHSS-SOIL [has_mechanism:: LEAK]
- SHSS-SOIL [has_mechanism:: CTMN]
- SHSS-SOIL [has_mechanism:: BLKG]
- SHSS-SOIL [has_mechanism:: MATF]
- SHSS-SOIL [has_mechanism:: OTHR]
- SHSS-FILT [part_of:: [[SHSS Shaft Seal System]]]
- SHSS-FILT [is_a:: FILT]
- SHSS-FILT [has_value:: 9] CAUSE_CODE
- SHSS-FILT [has_mechanism:: FSIG]
- SHSS-FILT [has_mechanism:: LEAK]
- SHSS-FILT [has_mechanism:: BLKG]
- SHSS-FILT [has_mechanism:: BRKG]
- SHSS-FILT [has_mechanism:: BRST]
- SHSS-FILT [has_mechanism:: CTMN]
- SHSS-FILT [has_mechanism:: STCK]
- SHSS-FILT [has_mechanism:: OTHR]
- SHSS-FILT [has_mechanism:: UNKN]
- SHSS-SGAS [part_of:: [[SHSS Shaft Seal System]]]
- SHSS-SGAS [is_a:: SGAS]
- SHSS-SGAS [has_value:: 3] CAUSE_CODE
- SHSS-SGAS [has_mechanism:: LEAK]
- SHSS-SGAS [has_mechanism:: CORR]
- SHSS-SGAS [has_mechanism:: OTHR]
- SHSS-PMGR [part_of:: [[SHSS Shaft Seal System]]] failure-structure.md Sheet1 agrees
- SHSS-PMGR [is_a:: PMGR]
- SHSS-PMGR [has_value:: 11] CAUSE_CODE
- SHSS-PMGR [has_mechanism:: LEAK]
- SHSS-PMGR [has_mechanism:: ELEC]
- SHSS-PMGR [has_mechanism:: CTRL]
- SHSS-PMGR [has_mechanism:: WEAR]
- SHSS-PMGR [has_mechanism:: CAVT]
- SHSS-PMGR [has_mechanism:: BLKG]
- SHSS-PMGR [has_mechanism:: OADJ]
- SHSS-PMGR [has_mechanism:: LOOS]
- SHSS-PMGR [has_mechanism:: ALGN]
- SHSS-PMGR [has_mechanism:: OTHR]
- SHSS-PMGR [has_mechanism:: OVHT]
- SHSS-DGSL [part_of:: [[SHSS Shaft Seal System]]]
- SHSS-DGSL [is_a:: DGSL]
- SHSS-DGSL [has_value:: 5] CAUSE_CODE
- SHSS-DGSL [has_mechanism:: LEAK]
- SHSS-DGSL [has_mechanism:: WEAR]
- SHSS-DGSL [has_mechanism:: CTMN]
- SHSS-DGSL [has_mechanism:: BRKG]
- SHSS-DGSL [has_mechanism:: OTHR]
- SHSS-BFGS [part_of:: [[SHSS Shaft Seal System]]]
- SHSS-BFGS [is_a:: BFGS]
- SHSS-BFGS [has_value:: 3] CAUSE_CODE
- SHSS-BFGS [has_mechanism:: LEAK]
- SHSS-BFGS [has_mechanism:: BLKG]
- SHSS-BFGS [has_mechanism:: OADJ]
- SHSS-OHTK [part_of:: [[SHSS Shaft Seal System]]]
- SHSS-OHTK [is_a:: OHTK]
- SHSS-OHTK [has_value:: 2] CAUSE_CODE
- SHSS-OHTK [has_mechanism:: LEAK]
- SHSS-OHTK [has_mechanism:: CORR]
- [[SHSS Shaft Seal System]] [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.96% counted at SHSS (derived), of 85.66
- [[SHSS Shaft Seal System]] [contributes_to:: [[OTH Other]]] 0.61% counted at SHSS (derived), of 85.66
- [[SHSS Shaft Seal System]] [contributes_to:: NOI] 0.18% counted at SHSS (derived), of 85.66
- [[SHSS Shaft Seal System]] [contributes_to:: [[LOO Low Output]]] 0.17% counted at SHSS (derived), of 85.66
- [[SHSS Shaft Seal System]] [contributes_to:: [[ELP External Leakage Process Medium]]] 0.13% counted at SHSS (derived), of 85.66
- [[SHSS Shaft Seal System]] [contributes_to:: VIB] 0.13% counted at SHSS (derived), of 85.66
- SHSS-PMGR [contributes_to:: [[OTH Other]]] 0.44%
- SHSS-PMGR [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.40% (mechanical seal leak)
- SHSS-SOIL [contributes_to:: [[ELU External Leakage Utility Medium]]] 0.35%
- SHSS-SGAS [contributes_to:: [[ELP External Leakage Process Medium]]] 0.13%
- [[SHSS Shaft Seal System]] [has_mechanism:: LEAK] top mechanism; seal oil, seal gas, dry gas seal, tanks
- [[SHSS Shaft Seal System]] [has_mechanism:: WEAR] top mechanism; pump
- [[SHSS Shaft Seal System]] [has_mechanism:: OTHR] top mechanism
- [[SHSS Shaft Seal System]] [related_to:: [[Centrifugal Compressor]]] low % reflects mainly centrifugal items (interpretation) [confidence:: low]
- SOIL [has_failure_rate_share:: 1.44%] within [[Centrifugal Compressor]] (OREDA per-type image, Sum)
- DGSL [has_failure_rate_share:: 0.22%] within [[Centrifugal Compressor]] (OREDA per-type image, Sum)

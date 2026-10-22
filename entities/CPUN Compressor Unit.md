---
title: CPUN Compressor Unit
created: 2026-10-20
updated: 2026-10-22
type: entity
tags: [sub-unit, maintainable-item, compressor, failure-rate]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__sheet5.csv, compressor-failure-hierarchy__subunit-code.csv, failure-structure__sheet1.csv]
confidence: medium
contested: true
---

# CPUN - Compressor unit

Sub Unit หลักของ [[Compressor]] ที่ทำงานอัดแก๊ส (cylinder/piston, rotor, valves, casing, shaft seals, bearing ฯลฯ) รหัส `CPUN` มี CAUSE_CODE มากที่สุด (112) และ % สูงสุดที่นับ (32.30)

## Maintainable items (15) และ mechanism codes

| Code | Item | จำนวน CAUSE_CODE | Mechanism codes |
|---|---|---|---|
| INST | Instruments | 18 | FSIG OADJ OPEN EART LEAK BLKG CTMN EROS NSIG NCFD STCK ALGN OVHT LOOS CORR OTHR UNKN VIBR |
| VALV | Valves | 14 | OADJ FSIG WEAR BRKG CTMN STCK LEAK EROS CORR LOOS FATG OTHR OVHT UNKN |
| ASRG | Antisurge system | 10 | FSIG OADJ NCFD CTRL STCK LEAK EROS LOOS OTHR FATG |
| CYLN | Cylinder liner | 12 | FSIG WEAR LEAK FATG CORR STCK CTMN OTHR OVHT BLKG UNKN LOOS |
| IPIP | Internal piping | 6 | BLKG FATG LEAK CORR LOOS OTHR |
| RBRG | Radial bearing | 5 | OVHT FATG CTMN ALGN WEAR |
| THRB | Thrust bearing | 4 | OVHT WEAR CTMN ALGN |
| CASG | Casing | 5 | FATG CORR EROS LEAK LOOS |
| PSTN | Piston(s) | 5 | BRKG FATG LOOS WEAR UNKN |
| PACK | Packing | 5 | WEAR ALGN OVHT CTMN LEAK |
| INSS | Interstage seals | 5 | LEAK WEAR ALGN CTMN OTHR |
| SHSL | Shaft seals | 7 | WEAR CTMN LEAK OVHT ALGN CTRL OTHR |
| PIPE | Piping | 6 | CORR FATG EROS LEAK BRST LOOS |
| ROTR | Rotor w/ impellers | 6 | CTMN EROS CORR VIBR ALGN FATG |
| CHKV | Check valves | 4 | CTMN WEAR STCK BRKG |

รวม 112 CAUSE_CODE ดู [[Failure Cause Codes]]

## Failure modes ที่เด่น (% นับที่ CPUN, derived)

ผลรวม **32.30** จาก 85.66: LOO 8.06, ELP 3.88, OHE 3.78, ELU 3.77, PDE 2.82, SER 2.29, OTH 2.00, AIR 1.03

คู่เด่น: Cylinder liner x LOO 5.78 (Wear), Cylinder liner x OHE 3.40 (Wear), Valves x LOO 2.21 (Wear), Cylinder liner x ELP 1.94, Valves x PDE 1.92, Valves x OTH 1.37, Valves x ELP 1.24, Valves x ELU 1.21, Valves x SER 1.13 ดู [[LOO Low Output]], [[OHE Overheating]], [[ELP External Leakage Process Medium]]

ผลรวมของ Cylinder liner ทุกโหมด = 13.66 และ Valves ทุกโหมด = 11.64 (derived) รวมกัน 25.30 หรือประมาณ 78% ของ 32.30 ในภาพ OREDA ต่อประเภท Cylinder liner สูงเด่นใน [[Reciprocating Compressor]] (Sum 28.77 ของ reciprocating เทียบกับ centrifugal 0.11)

## Top failure mechanisms

Wear (cylinder liner bore wear/scuffing, valve plate/seat/spring), Leakage (cover gasket/stem packing), Contamination (valve deposits), Corrosion (piping/casing/internal piping)

## ข้อควรระวัง (contested)

- Valves ในตารางนี้คือ % ของ Valves ที่นับที่ CPUN; Valves ปรากฏใน 5 sub unit (CPUN, CTMN, LUBS, SHSS, MISC) แต่ % นับครั้งเดียว Valves นอก CPUN ใช้ mechanism set ต่างกัน (oil/seal gas/control/utility valves)
- `failure-structure.md` (Sheet1) จัด **Valves, Internal piping, Check valves และ Piping ไว้ใน Miscellaneous** ขณะที่ dataset หลักจัดไว้ใน Compressor unit (Notes ระบุว่า check valves และ internal piping เป็น "assigned by judgement") เก็บทั้งสองมุมมอง ดู [[Failure Hierarchy]]
- สัดส่วน item ใน CPUN ต่างกันมากตามประเภท compressor (เช่น Cylinder liner เด่นใน reciprocating): ดู [[Compressor Type Failure Profiles]]

## Triplets

- [[CPUN Compressor Unit]] [is_a:: Sub Unit]
- [[CPUN Compressor Unit]] [part_of:: [[Compressor]]]
- [[CPUN Compressor Unit]] [has_code:: CPUN]
- [[CPUN Compressor Unit]] [has_value:: 15] maintainable items
- [[CPUN Compressor Unit]] [has_value:: 112] CAUSE_CODE, most of any sub unit
- [[CPUN Compressor Unit]] [has_failure_rate_share:: 32.30%] counted at CPUN (derived), of 85.66, highest sub unit
- CPUN-INST [part_of:: [[CPUN Compressor Unit]]]
- CPUN-INST [is_a:: INST]
- CPUN-INST [has_value:: 18] CAUSE_CODE
- CPUN-INST [has_mechanism:: FSIG]
- CPUN-INST [has_mechanism:: OADJ]
- CPUN-INST [has_mechanism:: OPEN]
- CPUN-INST [has_mechanism:: EART]
- CPUN-INST [has_mechanism:: LEAK]
- CPUN-INST [has_mechanism:: BLKG]
- CPUN-INST [has_mechanism:: CTMN]
- CPUN-INST [has_mechanism:: EROS]
- CPUN-INST [has_mechanism:: NSIG]
- CPUN-INST [has_mechanism:: NCFD]
- CPUN-INST [has_mechanism:: STCK]
- CPUN-INST [has_mechanism:: ALGN]
- CPUN-INST [has_mechanism:: OVHT]
- CPUN-INST [has_mechanism:: LOOS]
- CPUN-INST [has_mechanism:: CORR]
- CPUN-INST [has_mechanism:: OTHR]
- CPUN-INST [has_mechanism:: UNKN]
- CPUN-INST [has_mechanism:: VIBR]
- CPUN-VALV [part_of:: [[CPUN Compressor Unit]]] main dataset; Valves % for all 5 sub units counted here once [contested:: true]
- CPUN-VALV [is_a:: VALV]
- CPUN-VALV [has_value:: 14] CAUSE_CODE
- CPUN-VALV [has_mechanism:: OADJ]
- CPUN-VALV [has_mechanism:: FSIG]
- CPUN-VALV [has_mechanism:: WEAR]
- CPUN-VALV [has_mechanism:: BRKG]
- CPUN-VALV [has_mechanism:: CTMN]
- CPUN-VALV [has_mechanism:: STCK]
- CPUN-VALV [has_mechanism:: LEAK]
- CPUN-VALV [has_mechanism:: EROS]
- CPUN-VALV [has_mechanism:: CORR]
- CPUN-VALV [has_mechanism:: LOOS]
- CPUN-VALV [has_mechanism:: FATG]
- CPUN-VALV [has_mechanism:: OTHR]
- CPUN-VALV [has_mechanism:: OVHT]
- CPUN-VALV [has_mechanism:: UNKN]
- CPUN-ASRG [part_of:: [[CPUN Compressor Unit]]]
- CPUN-ASRG [is_a:: ASRG]
- CPUN-ASRG [has_value:: 10] CAUSE_CODE
- CPUN-ASRG [has_mechanism:: FSIG]
- CPUN-ASRG [has_mechanism:: OADJ]
- CPUN-ASRG [has_mechanism:: NCFD]
- CPUN-ASRG [has_mechanism:: CTRL]
- CPUN-ASRG [has_mechanism:: STCK]
- CPUN-ASRG [has_mechanism:: LEAK]
- CPUN-ASRG [has_mechanism:: EROS]
- CPUN-ASRG [has_mechanism:: LOOS]
- CPUN-ASRG [has_mechanism:: OTHR]
- CPUN-ASRG [has_mechanism:: FATG]
- CPUN-CYLN [part_of:: [[CPUN Compressor Unit]]]
- CPUN-CYLN [is_a:: CYLN]
- CPUN-CYLN [has_value:: 12] CAUSE_CODE
- CPUN-CYLN [has_mechanism:: FSIG]
- CPUN-CYLN [has_mechanism:: WEAR]
- CPUN-CYLN [has_mechanism:: LEAK]
- CPUN-CYLN [has_mechanism:: FATG]
- CPUN-CYLN [has_mechanism:: CORR]
- CPUN-CYLN [has_mechanism:: STCK]
- CPUN-CYLN [has_mechanism:: CTMN]
- CPUN-CYLN [has_mechanism:: OTHR]
- CPUN-CYLN [has_mechanism:: OVHT]
- CPUN-CYLN [has_mechanism:: BLKG]
- CPUN-CYLN [has_mechanism:: UNKN]
- CPUN-CYLN [has_mechanism:: LOOS]
- CPUN-IPIP [part_of:: [[CPUN Compressor Unit]]] main dataset, assigned by judgement [contested:: true]
- CPUN-IPIP [is_a:: IPIP]
- CPUN-IPIP [has_value:: 6] CAUSE_CODE
- CPUN-IPIP [has_mechanism:: BLKG]
- CPUN-IPIP [has_mechanism:: FATG]
- CPUN-IPIP [has_mechanism:: LEAK]
- CPUN-IPIP [has_mechanism:: CORR]
- CPUN-IPIP [has_mechanism:: LOOS]
- CPUN-IPIP [has_mechanism:: OTHR]
- CPUN-RBRG [part_of:: [[CPUN Compressor Unit]]]
- CPUN-RBRG [is_a:: RBRG]
- CPUN-RBRG [has_value:: 5] CAUSE_CODE
- CPUN-RBRG [has_mechanism:: OVHT]
- CPUN-RBRG [has_mechanism:: FATG]
- CPUN-RBRG [has_mechanism:: CTMN]
- CPUN-RBRG [has_mechanism:: ALGN]
- CPUN-RBRG [has_mechanism:: WEAR]
- CPUN-THRB [part_of:: [[CPUN Compressor Unit]]]
- CPUN-THRB [is_a:: THRB]
- CPUN-THRB [has_value:: 4] CAUSE_CODE
- CPUN-THRB [has_mechanism:: OVHT]
- CPUN-THRB [has_mechanism:: WEAR]
- CPUN-THRB [has_mechanism:: CTMN]
- CPUN-THRB [has_mechanism:: ALGN]
- CPUN-CASG [part_of:: [[CPUN Compressor Unit]]]
- CPUN-CASG [is_a:: CASG]
- CPUN-CASG [has_value:: 5] CAUSE_CODE
- CPUN-CASG [has_mechanism:: FATG]
- CPUN-CASG [has_mechanism:: CORR]
- CPUN-CASG [has_mechanism:: EROS]
- CPUN-CASG [has_mechanism:: LEAK]
- CPUN-CASG [has_mechanism:: LOOS]
- CPUN-PSTN [part_of:: [[CPUN Compressor Unit]]]
- CPUN-PSTN [is_a:: PSTN]
- CPUN-PSTN [has_value:: 5] CAUSE_CODE
- CPUN-PSTN [has_mechanism:: BRKG]
- CPUN-PSTN [has_mechanism:: FATG]
- CPUN-PSTN [has_mechanism:: LOOS]
- CPUN-PSTN [has_mechanism:: WEAR]
- CPUN-PSTN [has_mechanism:: UNKN]
- CPUN-PACK [part_of:: [[CPUN Compressor Unit]]]
- CPUN-PACK [is_a:: PACK]
- CPUN-PACK [has_value:: 5] CAUSE_CODE
- CPUN-PACK [has_mechanism:: WEAR]
- CPUN-PACK [has_mechanism:: ALGN]
- CPUN-PACK [has_mechanism:: OVHT]
- CPUN-PACK [has_mechanism:: CTMN]
- CPUN-PACK [has_mechanism:: LEAK]
- CPUN-INSS [part_of:: [[CPUN Compressor Unit]]]
- CPUN-INSS [is_a:: INSS]
- CPUN-INSS [has_value:: 5] CAUSE_CODE
- CPUN-INSS [has_mechanism:: LEAK]
- CPUN-INSS [has_mechanism:: WEAR]
- CPUN-INSS [has_mechanism:: ALGN]
- CPUN-INSS [has_mechanism:: CTMN]
- CPUN-INSS [has_mechanism:: OTHR]
- CPUN-SHSL [part_of:: [[CPUN Compressor Unit]]]
- CPUN-SHSL [is_a:: SHSL]
- CPUN-SHSL [has_value:: 7] CAUSE_CODE
- CPUN-SHSL [has_mechanism:: WEAR]
- CPUN-SHSL [has_mechanism:: CTMN]
- CPUN-SHSL [has_mechanism:: LEAK]
- CPUN-SHSL [has_mechanism:: OVHT]
- CPUN-SHSL [has_mechanism:: ALGN]
- CPUN-SHSL [has_mechanism:: CTRL]
- CPUN-SHSL [has_mechanism:: OTHR]
- CPUN-PIPE [part_of:: [[CPUN Compressor Unit]]] main dataset [contested:: true]
- CPUN-PIPE [is_a:: PIPE]
- CPUN-PIPE [has_value:: 6] CAUSE_CODE
- CPUN-PIPE [has_mechanism:: CORR]
- CPUN-PIPE [has_mechanism:: FATG]
- CPUN-PIPE [has_mechanism:: EROS]
- CPUN-PIPE [has_mechanism:: LEAK]
- CPUN-PIPE [has_mechanism:: BRST]
- CPUN-PIPE [has_mechanism:: LOOS]
- CPUN-ROTR [part_of:: [[CPUN Compressor Unit]]]
- CPUN-ROTR [is_a:: ROTR]
- CPUN-ROTR [has_value:: 6] CAUSE_CODE
- CPUN-ROTR [has_mechanism:: CTMN]
- CPUN-ROTR [has_mechanism:: EROS]
- CPUN-ROTR [has_mechanism:: CORR]
- CPUN-ROTR [has_mechanism:: VIBR]
- CPUN-ROTR [has_mechanism:: ALGN]
- CPUN-ROTR [has_mechanism:: FATG]
- CPUN-CHKV [part_of:: [[CPUN Compressor Unit]]] main dataset, assigned by judgement [contested:: true]
- CPUN-CHKV [is_a:: CHKV]
- CPUN-CHKV [has_value:: 4] CAUSE_CODE
- CPUN-CHKV [has_mechanism:: CTMN]
- CPUN-CHKV [has_mechanism:: WEAR]
- CPUN-CHKV [has_mechanism:: STCK]
- CPUN-CHKV [has_mechanism:: BRKG]
- VALV [part_of:: [[MISC Miscellaneous]]] failure-structure.md Sheet1 [contested:: true]
- IPIP [part_of:: [[MISC Miscellaneous]]] failure-structure.md Sheet1 [contested:: true]
- CHKV [part_of:: [[MISC Miscellaneous]]] failure-structure.md Sheet1 [contested:: true]
- PIPE [part_of:: [[MISC Miscellaneous]]] failure-structure.md Sheet1 [contested:: true]
- CPUN-VALV [differs_from:: VALV] Valves in CTMN, LUBS, SHSS, MISC use different mechanism sets (oil/seal gas/control/utility valves)
- [[CPUN Compressor Unit]] [contributes_to:: [[LOO Low Output]]] 8.06% counted at CPUN (derived), of 85.66
- [[CPUN Compressor Unit]] [contributes_to:: [[ELP External Leakage Process Medium]]] 3.88% counted at CPUN (derived), of 85.66
- [[CPUN Compressor Unit]] [contributes_to:: [[OHE Overheating]]] 3.78% counted at CPUN (derived), of 85.66
- [[CPUN Compressor Unit]] [contributes_to:: [[ELU External Leakage Utility Medium]]] 3.77% counted at CPUN (derived), of 85.66
- [[CPUN Compressor Unit]] [contributes_to:: [[PDE Parameter Deviation]]] 2.82% counted at CPUN (derived), of 85.66
- [[CPUN Compressor Unit]] [contributes_to:: [[SER Minor In-Service Problems]]] 2.29% counted at CPUN (derived), of 85.66
- [[CPUN Compressor Unit]] [contributes_to:: [[OTH Other]]] 2.00% counted at CPUN (derived), of 85.66
- [[CPUN Compressor Unit]] [contributes_to:: [[AIR Abnormal Instrument Reading]]] 1.03% counted at CPUN (derived), of 85.66
- CPUN-CYLN [contributes_to:: [[LOO Low Output]]] 5.78% (Wear)
- CPUN-CYLN [contributes_to:: [[OHE Overheating]]] 3.40% (Wear)
- CPUN-VALV [contributes_to:: [[LOO Low Output]]] 2.21% (Wear)
- CPUN-CYLN [contributes_to:: [[ELP External Leakage Process Medium]]] 1.94%
- CPUN-VALV [contributes_to:: [[PDE Parameter Deviation]]] 1.92%
- CPUN-VALV [contributes_to:: [[OTH Other]]] 1.37%
- CPUN-VALV [contributes_to:: [[ELP External Leakage Process Medium]]] 1.24%
- CPUN-VALV [contributes_to:: [[ELU External Leakage Utility Medium]]] 1.21%
- CPUN-VALV [contributes_to:: [[SER Minor In-Service Problems]]] 1.13%
- CPUN-CYLN [has_failure_rate_share:: 13.66%] all modes (derived)
- CPUN-VALV [has_failure_rate_share:: 11.64%] all modes (derived); with Cylinder liner 25.30, about 78% of 32.30
- CPUN-CYLN [dominant_in:: [[Reciprocating Compressor]]] Sum 28.77 in reciprocating vs 0.11 in centrifugal (OREDA per-type image)
- [[CPUN Compressor Unit]] [has_mechanism:: WEAR] top mechanism; cylinder liner bore wear/scuffing, valve plate/seat/spring
- [[CPUN Compressor Unit]] [has_mechanism:: LEAK] top mechanism; cover gasket/stem packing
- [[CPUN Compressor Unit]] [has_mechanism:: CTMN] top mechanism; valve deposits
- [[CPUN Compressor Unit]] [has_mechanism:: CORR] top mechanism; piping/casing/internal piping
- [[CPUN Compressor Unit]] [related_to:: [[Compressor Type Failure Profiles]]] item shares in CPUN differ strongly by compressor type

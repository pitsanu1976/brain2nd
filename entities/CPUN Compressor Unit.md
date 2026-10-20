---
title: CPUN Compressor Unit
created: 2026-10-20
updated: 2026-10-20
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

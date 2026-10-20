---
title: SHSS Shaft Seal System
created: 2026-10-20
updated: 2026-10-20
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

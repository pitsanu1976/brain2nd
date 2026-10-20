---
title: MISC Miscellaneous
created: 2026-10-20
updated: 2026-10-20
type: entity
tags: [sub-unit, maintainable-item, compressor, failure-rate]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__sheet5.csv, compressor-failure-hierarchy__subunit-code.csv, failure-structure__sheet1.csv]
confidence: medium
contested: true
---

# MISC - Miscellaneous

Sub Unit ของ [[Compressor]] สำหรับส่วนประกอบที่ไม่เข้ากลุ่มอื่น (base frame, piping และ support, silencer, cooler, purge air, valves) รหัส `MISC` (หมายเหตุ: ชนกับ mechanism `MISC` = Miscellaneous - general ดู [[CAUSE_CODE Convention]])

## Maintainable items (7) และ mechanism codes

| Code | Item | จำนวน CAUSE_CODE | Mechanism codes |
|---|---|---|---|
| VALV | Valves | 16 | OADJ FSIG STCK LEAK EROS CORR WEAR BRKG CAVT BLKG CTMN LOOS VIBR OTHR FATG UNKN |
| PSPB | Piping, pipe support + bellows | 9 | CORR FATG EROS LEAK BRST LOOS OTHR MISC VIBR |
| PIPE | Piping | 6 | CORR FATG EROS LEAK BRST LOOS |
| SILN | Silencers | 4 | FATG CORR LEAK BRKG |
| COOL | Cooler(s) | 11 | CORR EROS FATG BRST WEAR LOOS OTHR BLKG ELEC OADJ MEXT |
| PAIR | Purge air | 5 | LEAK OADJ BLKG FSIG CTMN |
| BASE | Base frame | 5 | CORR LOOS FATG DEFM EXIN |

รวม 56 CAUSE_CODE ดู [[Failure Cause Codes]]

## Failure modes ที่เด่น (% นับที่ MISC, derived)

ผลรวม **2.51** จาก 85.66: SER 1.23, ELU 0.31, PDE 0.26, ELP 0.22, STD 0.17, OTH 0.09, VIB 0.08, OHE 0.07

คู่เด่น: Base frame x SER 0.88 (Corrosion), Piping/pipe support + bellows x SER 0.22 และ x ELU 0.22 (Corrosion), Purge air x PDE 0.26 (Leakage), Piping, pipe support + bellows x ELP 0.18 ดู [[SER Minor In-Service Problems]]

## Top failure mechanisms

Corrosion (base frame, piping), Fatigue/Burst (piping, cooler), Leakage (purge air)

## ข้อควรระวัง (contested)

- Valves ใน MISC ไม่มี % แยก (นับที่ [[CPUN Compressor Unit]])
- `failure-structure.md` (Sheet1) จัด **Valves, Internal piping, Check valves, Piping, Cooler(s) และ Other ไว้ใน Miscellaneous** ซึ่งกว้างกว่าใน dataset หลักมาก (ที่ MISC มีเพียง 7 item) ดู [[Failure Hierarchy]] และ [[Maintainable Item]]
- Sheet1 มี sub unit พิเศษ `Not specified (generic - applies to all subunits)` สำหรับ item Subunit/Unknown ซึ่งไม่มีใน dataset หลัก (ที่ตัด placeholder ออก)

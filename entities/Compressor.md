---
title: Compressor
created: 2026-10-20
updated: 2026-10-22
type: entity
tags: [compressor, taxonomy, oreda, failure-rate]
sources: [compressor-failure-hierarchy.md, failure-structure.md, compressor-failure-hierarchy__summary-by-failure-mode.csv, compressor-failure-hierarchy__notes.csv, reliability-based-maintenance-management.md, iso-14224.md]
confidence: high
contested: false
---

# Compressor (generic)

Equipment ระดับ 1 ของ [[Failure Hierarchy]] ใน dataset ใช้ ASSET GROUP = `COCE` (compressor) สำหรับทุกแถว ตัวเลขใน dataset หลักเป็นค่า "ทุกประเภทรวม" ตาม OREDA

## ประเภทที่ sources ครอบคลุม

| ประเภท | หน้า | ลักษณะใน data |
|---|---|---|
| Centrifugal | [[Centrifugal Compressor]] | AIR และ ELU เด่น; มี Antisurge, Rotor, Dry gas seal |
| Reciprocating | [[Reciprocating Compressor]] | LOO, SER เด่น; Cylinder liner และ Filter(s) เด่น |
| Screw | [[Screw Compressor]] | AIR, ELU, PDE, UST เด่น; Valves และ instruments เด่น |

เปรียบเทียบทั้งสามที่ [[Compressor Type Failure Profiles]]

## ขนาดของ dataset หลัก

| รายการ | จำนวน |
|---|---|
| Sub Unit | 6 ([[PWTR Power Transmission]], [[CPUN Compressor Unit]], [[CTMN Control and Monitoring]], [[LUBS Lubrication System]], [[SHSS Shaft Seal System]], [[MISC Miscellaneous]]) |
| Maintainable item (รหัสไม่ซ้ำ) | 44 ([[Maintainable Item]]) |
| คู่ failure mode/item ที่ % ไม่เป็นศูนย์ | 258 |
| Failure mode | 19 ([[Failure Mode]]) |
| CAUSE_CODE ไม่ซ้ำ | 473 ([[Failure Cause Codes]]) |
| แถวข้อมูล Failure Hierarchy | 7,882 |
| Total % ที่ระบุได้ | 85.66 (ไม่รวม Other/Subunit/Unknown 13.96) |

## ภาพรวมโหมดความล้มเหลว (ทุกประเภทรวม)

AIR 17.18, SER 13.05, LOO 10.11, ELU 8.62, PDE 8.13 เป็น 5 โหมดแรก ดู [[Which failure modes dominate compressor failure rate]]

## ตามมาตรฐาน ISO 14224 (เพิ่ม 2026-10-21)

- Compressor = equipment class **CO** (taxonomy level 6) ใน Table A.4 รวม air compressor; type code มี 4 แบบ: CE Centrifugal, RE Reciprocating, SC Screw และ **AX Axial** (Table A.8, ISO 14224 p.64) wiki/dataset ครอบคลุมเพียง 3 แบบแรก ไม่มี axial; รหัส type CE ซ้ำกับ class CE (Combustion engines) แต่คนละระดับ
- Subdivision 6 subunit ตาม Table A.9 (p.65) ชื่อและจำนวนตรงกับ dataset แต่รหัสย่อ 4 ตัวอักษรเป็นของ dataset ไม่ใช่ ISO ดู [[Compressor Subdivision Wiki vs ISO 14224]]
- Boundary (cl. A.2.2.2.1, p.64-65): **ไม่รวม** inlet/outlet valve และ driver พร้อม auxiliary ของ driver (driver เป็น inventory แยก มีเลขอ้างอิงโยง); compressor train = 1 inventory (สูงสุด 4 stage, 1 stage ปกติ = 1 casing); subunit ที่ใช้ร่วมกับ driver ให้นับเป็นของ compressor; lube oil/seal oil ร่วมระบบ ให้ลงที่ subunit ที่ได้รับผลมากที่สุด ไม่ชัดให้ลง lubrication system
- Equipment-specific data (Table A.10, p.65-66): priority high คือ compressed medium, type of driver, discharge pressure design, flow rate design, design power, number of casings, shaft seal system; ข้อมูลเฉพาะ reciprocating เช่น cylinder configuration, working principle (single/double-acting), packing type (priority low)
- ISO ไม่ได้ให้ failure rate ของ compressor ตัวเลขทั้งหมดในหน้านี้ยังมาจาก OREDA dataset ดู [[ISO 14224 Taxonomy]]

## ข้อควรระวัง

- ไม่มีข้อมูล failure rate สัมบูรณ์, population หรือ operating hours ใน sources ดู [[OREDA]]
- Dataset หลักเป็น engineering judgement สำหรับ mechanism/resolution ต้อง validate กับ CMMS/RCA ของ Valeura

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความ ไม่ใช่ข้อมูล OREDA: การวางกลยุทธ์ PM ของ compressor ตามหนังสือ RBMM เริ่มจาก [[RCM Reliability Centered Maintenance]] และ [[Criticality Assessment]] แล้วเลือกงานด้วย [[PM Task Selection]] (ไม่มีข้อมูล β หรือ P-F เฉพาะ compressor ใน sources) ดูตัวอย่างขั้นตอนที่ [[How to choose PM task for a compressor failure mode]]

## Triplets

- [[Compressor]] [at_level:: 1] equipment level of [[Failure Hierarchy]]
- [[Compressor]] [has_code:: COCE] ASSET GROUP in dataset
- [[Centrifugal Compressor]] [is_a:: [[Compressor]]]
- [[Reciprocating Compressor]] [is_a:: [[Compressor]]]
- [[Screw Compressor]] [is_a:: [[Compressor]]]
- [[Compressor]] [has_part:: [[PWTR Power Transmission]]]
- [[Compressor]] [has_part:: [[CPUN Compressor Unit]]]
- [[Compressor]] [has_part:: [[CTMN Control and Monitoring]]]
- [[Compressor]] [has_part:: [[LUBS Lubrication System]]]
- [[Compressor]] [has_part:: [[SHSS Shaft Seal System]]]
- [[Compressor]] [has_part:: [[MISC Miscellaneous]]]
- [[Compressor]] [has_value:: 6] sub units
- [[Compressor]] [has_value:: 44] unique maintainable item codes
- [[Compressor]] [has_value:: 258] failure mode/item pairs with non-zero %
- [[Compressor]] [has_value:: 19] failure modes
- [[Compressor]] [has_value:: 473] unique CAUSE_CODE
- [[Compressor]] [has_value:: 7,882] Failure Hierarchy data rows
- [[Compressor]] [has_failure_rate_share:: 85.66%] identifiable total, excludes Other/Subunit/Unknown
- Other/Subunit/Unknown [has_failure_rate_share:: 13.96%] excluded placeholders
- [[AIR Abnormal Instrument Reading]] [has_failure_rate_share:: 17.18%] all compressor types, rank 1
- [[SER Minor In-Service Problems]] [has_failure_rate_share:: 13.05%] all compressor types, rank 2
- [[LOO Low Output]] [has_failure_rate_share:: 10.11%] all compressor types, rank 3
- [[ELU External Leakage Utility Medium]] [has_failure_rate_share:: 8.62%] all compressor types, rank 4
- [[PDE Parameter Deviation]] [has_failure_rate_share:: 8.13%] all compressor types, rank 5
- [[AIR Abnormal Instrument Reading]] [dominant_in:: [[Centrifugal Compressor]]]
- [[ELU External Leakage Utility Medium]] [dominant_in:: [[Centrifugal Compressor]]]
- ASRG [part_of:: [[Centrifugal Compressor]]] present in centrifugal
- ROTR [part_of:: [[Centrifugal Compressor]]] present in centrifugal
- DGSL [part_of:: [[Centrifugal Compressor]]] present in centrifugal
- [[LOO Low Output]] [dominant_in:: [[Reciprocating Compressor]]]
- [[SER Minor In-Service Problems]] [dominant_in:: [[Reciprocating Compressor]]]
- CYLN [dominant_in:: [[Reciprocating Compressor]]]
- FILT [dominant_in:: [[Reciprocating Compressor]]]
- [[AIR Abnormal Instrument Reading]] [dominant_in:: [[Screw Compressor]]]
- [[ELU External Leakage Utility Medium]] [dominant_in:: [[Screw Compressor]]]
- [[PDE Parameter Deviation]] [dominant_in:: [[Screw Compressor]]]
- [[UST Spurious Stop]] [dominant_in:: [[Screw Compressor]]]
- VALV [dominant_in:: [[Screw Compressor]]]
- INST [dominant_in:: [[Screw Compressor]]]
- [[Compressor]] [maps_to:: ISO:A.4-CO] equipment class, includes air compressor
- [[Compressor]] [at_level:: 6] ISO 14224 taxonomy equipment class
- [[Compressor]] [defined_in:: [[ISO 14224]]] Table A.4, A.8, A.9
- [[Centrifugal Compressor]] [maps_to:: ISO:A.8-CE] (ISO 14224 Table A.8, p.64)
- [[Reciprocating Compressor]] [maps_to:: ISO:A.8-RE] (ISO 14224 Table A.8, p.64)
- [[Screw Compressor]] [maps_to:: ISO:A.8-SC] (ISO 14224 Table A.8, p.64)
- ISO:A.8-AX [is_a:: [[Compressor]]] Axial type; not covered by wiki/dataset
- ISO:A.8-CE [differs_from:: ISO:A.4-CE] type Centrifugal vs class Combustion engines, different levels
- [[Compressor]] [has_value:: 6] ISO 14224 Table A.9 subunits; names and count match dataset, 4-letter codes are dataset-only
- Compressor Boundary [applies_to:: [[Compressor]]] excludes inlet/outlet valve and driver with its auxiliaries (ISO 14224 cl. A.2.2.2.1, p.64-65)
- Compressor Train [has_value:: 4] max stages in one inventory; 1 stage normally = 1 casing
- Shared Lube Oil or Seal Oil System [part_of:: [[LUBS Lubrication System]]] when unclear; otherwise subunit most affected
- [[Compressor]] [has_parameter:: Compressed Medium] high priority (ISO 14224 Table A.10)
- [[Compressor]] [has_parameter:: Type Of Driver] high priority (ISO 14224 Table A.10)
- [[Compressor]] [has_parameter:: Discharge Pressure Design] high priority (ISO 14224 Table A.10)
- [[Compressor]] [has_parameter:: Flow Rate Design] high priority (ISO 14224 Table A.10)
- [[Compressor]] [has_parameter:: Design Power] high priority (ISO 14224 Table A.10)
- [[Compressor]] [has_parameter:: Number Of Casings] high priority (ISO 14224 Table A.10)
- [[Compressor]] [has_parameter:: Shaft Seal System] high priority (ISO 14224 Table A.10)
- [[Reciprocating Compressor]] [has_parameter:: Cylinder Configuration] (ISO 14224 Table A.10)
- [[Reciprocating Compressor]] [has_parameter:: Working Principle] single/double-acting (ISO 14224 Table A.10)
- [[Reciprocating Compressor]] [has_parameter:: Packing Type] priority low (ISO 14224 Table A.10)
- [[OREDA]] [source_of:: [[Compressor]]] all failure rate % on this page; ISO 14224 gives no compressor failure rate
- [[Compressor]] [related_to:: [[RCM Reliability Centered Maintenance]]] PM strategy per RBMM (interpretation) [confidence:: low]
- [[Compressor]] [related_to:: [[Criticality Assessment]]] PM strategy per RBMM (interpretation) [confidence:: low]
- [[PM Task Selection]] [applies_to:: [[Compressor]]] (interpretation, no compressor beta or P-F in sources) [confidence:: low]

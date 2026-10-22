---
title: Maintainable Item
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [maintainable-item, taxonomy, oreda, coding]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__maintainable-item-code.csv, compressor-failure-hierarchy__notes.csv, failure-structure.md, failure-structure__sheet1.csv, reliability-based-maintenance-management.md, iso-14224.md]
confidence: medium
contested: true
---

# Maintainable Item

**Maintainable item** คือส่วนประกอบที่ซ่อม/เปลี่ยนได้ภายใต้ sub unit เป็นระดับที่ 3 ของ [[Failure Hierarchy]] OREDA Table 5 แบ่ง [[Compressor]] ออกเป็น item ที่ผูกกับ sub unit

## รหัส 44 รายการ

| Code | Item | Code | Item |
|---|---|---|---|
| INST | Instruments | PIPE | Piping |
| GBVD | Gearbox/var.drive | PMTR | Pump w/motor |
| VALV | Valves | SGAS | Seal gas |
| ASRG | Antisurge system | PSPB | Piping, pipe support + bellows |
| CYLN | Cylinder liner | SILN | Silencers |
| IPIP | Internal piping | CPDN | Coupling to driven unit |
| MONI | Monitoring | BRNG | Bearing |
| CTUN | Control unit | LUBR | Lubrication |
| CBJB | Cabling & junction boxes | COOL | Cooler(s) |
| IPSU | Internal power supply | OILS | Oil |
| ACTD | Actuating device | PMGR | Pump w/motor/gear |
| CICV | Control-, isolating & check valves | DGSL | Dry gas seal |
| LUBE | Lube oil | BFGS | Buffer gas system |
| RSHT | Reservoir w/heating system | OHTK | Overhead tank |
| FILT | Filter(s) | PAIR | Purge air |
| OTHT | Oil tank w/heating system | ROTR | Rotor w/ impellers |
| SOIL | Seal oil | CHKV | Check valves |
| RBRG | Radial bearing | BASE | Base frame |
| CASG | Casing | THRB | Thrust bearing |
| PSTN | Piston(s) | | |
| CPDR | Coupling to driver | | |
| SEAL | Seals | | |
| PACK | Packing | | |
| INSS | Interstage seals | | |
| SHSL | Shaft seals | | |

(รวม 44 รายการ; ใน source รหัสเรียงตามลำดับที่ปรากฏ ไม่ได้เรียงตามตัวอักษร)

item แต่ละตัวสังกัด sub unit ใดดูที่หน้า sub unit: [[PWTR Power Transmission]], [[CPUN Compressor Unit]], [[CTMN Control and Monitoring]], [[LUBS Lubrication System]], [[SHSS Shaft Seal System]], [[MISC Miscellaneous]]

## กติกาพิเศษ

- Item ที่ OREDA Table 5 ระบุหลาย sub unit ถูกจับคู่กับทุก sub unit: Instruments (PWTR, CPUN, CTMN, LUBS, SHSS), Valves (CPUN, CTMN, LUBS, SHSS, MISC), Seals (PWTR, LUBS), Cooler(s) (LUBS, MISC), Filter(s) (LUBS, SHSS), Piping (CPUN, LUBS, MISC), Reservoir w/heating system (LUBS, SHSS)
- **Instruments** = OREDA instrument types (flow, general, level, pressure, speed, temperature, vibration) รวมเป็น item เดียว: % เป็นผลรวมของ type และ mechanism เป็น union
- Item ที่ไม่อยู่ใน Table 5 ถูก assign ด้วย judgement: check valves และ internal piping -> Compressor unit; control-, isolating & check valves -> Control and monitoring; couplings -> Power transmission; lube oil / oil tank -> Lubrication system; pipe supports -> Miscellaneous
- Placeholder 'Other', 'Subunit', 'Unknown' ถูกตัดออก (13.96% ของ failure rate)

## ข้อขัดแย้ง (contested)

1. **นิยามคอลัมน์**: sheet Summary by Failure Mode ตั้งชื่อคอลัมน์ "No. of Maintainable Items" รวม 258 แต่ค่านี้นับ **คู่ failure mode/item** ไม่ใช่ item ไม่ซ้ำ (ไม่ซ้ำมี 44 รหัส) ดู [[Failure Mode]]
2. **การจัดสังกัด sub unit ต่างกันระหว่าง sources** (Instruments, Valves, Internal piping, Check valves) ดูตารางใน [[Failure Hierarchy]]
3. ภาพ OREDA ต่อประเภทมี item "Instrument, flow/general/level/pressure/speed/temperature/vibration" แยกกัน ขณะที่ dataset หลักรวมเป็น Instruments (เป็นการออกแบบ ไม่ใช่ข้อผิดพลาด)

## เทียบกับ ISO 14224 (เพิ่ม 2026-10-21)

- นิยาม: ISO 14224 ให้ maintainable item (MI) เป็น part หรือ assembly ที่ปกติเป็นระดับต่ำสุดในลำดับชั้นเมื่อทำ maintenance (cl. 3.48, p.10) อยู่ที่ taxonomy **level 8** (Component/MI) ใต้ subunit (level 7) และเหนือ part (level 9, optional) (cl. 8.2, p.30-31) ดู [[ISO 14224 Taxonomy]]
- **รหัส 4 ตัวอักษรทั้ง 44 รหัสข้างต้น (GBVD, ASRG, CICV ฯลฯ) ไม่ใช่รหัสของ ISO 14224** มาตรฐานใช้ชื่อเต็มใน Table A.9 (p.65) ไม่มีรหัสย่อ จึงใช้ได้เฉพาะใน dataset/wiki นี้
- Table A.9 มี item ที่ dataset ไม่มี เช่น Belt/sheave, Balance piston, Sensors, Wiring, Pump/Motor/Gear แยก, Mechanical seal, Scrubber, Control valves, Isolation valves, Magnetic-bearing control system, Flange joints และมี item ใน dataset ที่ ISO ไม่มี เช่น Seal gas, Buffer gas system, Overhead tank, Oil, CICV รายการเต็มและตำแหน่งที่ต่างกัน (Instruments vs Sensors, CICV, Check valves, Piping, Seals, Reservoir) อยู่ที่ [[Compressor Subdivision Wiki vs ISO 14224]]
- ความต่างระหว่าง OREDA dataset กับ ISO ถือเป็นความต่างของ scope (คนละ source) ไม่เพิ่มข้อขัดแย้งใหม่ แต่ข้อขัดแย้ง 2 ข้อด้านบนยังคงอยู่
- ISO แนะนำให้เผื่อ item "Others" และ "Unknown" ในทุกตาราง subdivision (cl. A.1.1, p.46) ตรงกับ placeholder ที่ dataset ตัดออก ในการบันทึก failure ต้องเก็บ MI ที่เสียด้วย (Table 6, p.40-41) ดู [[Failure Data Recording]]

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความ ไม่ใช่ข้อความใน OREDA: RBMM ใช้คำ **Object Part** (ชิ้นส่วนต้นตอของปัญหา, RBMM p.151-152) ซึ่งตีความได้ว่าใกล้เคียง Maintainable Item แต่หนังสือไม่ได้เทียบตรง ดู [[Failure Data Recording]] และ [[RBMM Concepts vs Compressor Failure Hierarchy]] การกำหนดอะไหล่และ criticality ต่อ item ดู [[Spare Parts Management]] และ [[Spare Part Criticality and Risk]]

## Triplets

- [[Maintainable Item]] [at_level:: 3] level 3 of [[Failure Hierarchy]], under sub unit
- [[Maintainable Item]] [part_of:: Sub Unit]
- [[Maintainable Item]] [defined_in:: [[OREDA]]] Table 5 splits [[Compressor]] into items tied to sub units
- [[Maintainable Item]] [has_value:: 44] unique item codes [contested:: true]
- INST [is_a:: [[Maintainable Item]]]
- INST [has_label:: Instruments]
- GBVD [is_a:: [[Maintainable Item]]]
- GBVD [has_label:: Gearbox/var.drive]
- VALV [is_a:: [[Maintainable Item]]]
- VALV [has_label:: Valves]
- ASRG [is_a:: [[Maintainable Item]]]
- ASRG [has_label:: Antisurge system]
- CYLN [is_a:: [[Maintainable Item]]]
- CYLN [has_label:: Cylinder liner]
- IPIP [is_a:: [[Maintainable Item]]]
- IPIP [has_label:: Internal piping]
- MONI [is_a:: [[Maintainable Item]]]
- MONI [has_label:: Monitoring]
- CTUN [is_a:: [[Maintainable Item]]]
- CTUN [has_label:: Control unit]
- CBJB [is_a:: [[Maintainable Item]]]
- CBJB [has_label:: Cabling & junction boxes]
- IPSU [is_a:: [[Maintainable Item]]]
- IPSU [has_label:: Internal power supply]
- ACTD [is_a:: [[Maintainable Item]]]
- ACTD [has_label:: Actuating device]
- CICV [is_a:: [[Maintainable Item]]]
- CICV [has_label:: Control-, isolating & check valves]
- LUBE [is_a:: [[Maintainable Item]]]
- LUBE [has_label:: Lube oil]
- RSHT [is_a:: [[Maintainable Item]]]
- RSHT [has_label:: Reservoir w/heating system]
- FILT [is_a:: [[Maintainable Item]]]
- FILT [has_label:: Filter(s)]
- OTHT [is_a:: [[Maintainable Item]]]
- OTHT [has_label:: Oil tank w/heating system]
- SOIL [is_a:: [[Maintainable Item]]]
- SOIL [has_label:: Seal oil]
- RBRG [is_a:: [[Maintainable Item]]]
- RBRG [has_label:: Radial bearing]
- CASG [is_a:: [[Maintainable Item]]]
- CASG [has_label:: Casing]
- PSTN [is_a:: [[Maintainable Item]]]
- PSTN [has_label:: Piston(s)]
- CPDR [is_a:: [[Maintainable Item]]]
- CPDR [has_label:: Coupling to driver]
- SEAL [is_a:: [[Maintainable Item]]]
- SEAL [has_label:: Seals]
- PACK [is_a:: [[Maintainable Item]]]
- PACK [has_label:: Packing]
- INSS [is_a:: [[Maintainable Item]]]
- INSS [has_label:: Interstage seals]
- SHSL [is_a:: [[Maintainable Item]]]
- SHSL [has_label:: Shaft seals]
- PIPE [is_a:: [[Maintainable Item]]]
- PIPE [has_label:: Piping]
- PMTR [is_a:: [[Maintainable Item]]]
- PMTR [has_label:: Pump w/motor]
- SGAS [is_a:: [[Maintainable Item]]]
- SGAS [has_label:: Seal gas]
- PSPB [is_a:: [[Maintainable Item]]]
- PSPB [has_label:: Piping, pipe support + bellows]
- SILN [is_a:: [[Maintainable Item]]]
- SILN [has_label:: Silencers]
- CPDN [is_a:: [[Maintainable Item]]]
- CPDN [has_label:: Coupling to driven unit]
- BRNG [is_a:: [[Maintainable Item]]]
- BRNG [has_label:: Bearing]
- LUBR [is_a:: [[Maintainable Item]]]
- LUBR [has_label:: Lubrication]
- COOL [is_a:: [[Maintainable Item]]]
- COOL [has_label:: Cooler(s)]
- OILS [is_a:: [[Maintainable Item]]]
- OILS [has_label:: Oil]
- PMGR [is_a:: [[Maintainable Item]]]
- PMGR [has_label:: Pump w/motor/gear]
- DGSL [is_a:: [[Maintainable Item]]]
- DGSL [has_label:: Dry gas seal]
- BFGS [is_a:: [[Maintainable Item]]]
- BFGS [has_label:: Buffer gas system]
- OHTK [is_a:: [[Maintainable Item]]]
- OHTK [has_label:: Overhead tank]
- PAIR [is_a:: [[Maintainable Item]]]
- PAIR [has_label:: Purge air]
- ROTR [is_a:: [[Maintainable Item]]]
- ROTR [has_label:: Rotor w/ impellers]
- CHKV [is_a:: [[Maintainable Item]]]
- CHKV [has_label:: Check valves]
- BASE [is_a:: [[Maintainable Item]]]
- BASE [has_label:: Base frame]
- THRB [is_a:: [[Maintainable Item]]]
- THRB [has_label:: Thrust bearing]
- PWTR-INST [is_a:: INST] OREDA Table 5 lists several sub units; matched to all
- CPUN-INST [is_a:: INST] OREDA Table 5 lists several sub units; matched to all
- CTMN-INST [is_a:: INST] OREDA Table 5 lists several sub units; matched to all
- LUBS-INST [is_a:: INST] OREDA Table 5 lists several sub units; matched to all
- SHSS-INST [is_a:: INST] OREDA Table 5 lists several sub units; matched to all
- CPUN-VALV [is_a:: VALV] OREDA Table 5 lists several sub units; matched to all
- CTMN-VALV [is_a:: VALV] OREDA Table 5 lists several sub units; matched to all
- LUBS-VALV [is_a:: VALV] OREDA Table 5 lists several sub units; matched to all
- SHSS-VALV [is_a:: VALV] OREDA Table 5 lists several sub units; matched to all
- MISC-VALV [is_a:: VALV] OREDA Table 5 lists several sub units; matched to all
- PWTR-SEAL [is_a:: SEAL] OREDA Table 5 lists several sub units; matched to all
- LUBS-SEAL [is_a:: SEAL] OREDA Table 5 lists several sub units; matched to all
- LUBS-COOL [is_a:: COOL] OREDA Table 5 lists several sub units; matched to all
- MISC-COOL [is_a:: COOL] OREDA Table 5 lists several sub units; matched to all
- LUBS-FILT [is_a:: FILT] OREDA Table 5 lists several sub units; matched to all
- SHSS-FILT [is_a:: FILT] OREDA Table 5 lists several sub units; matched to all
- CPUN-PIPE [is_a:: PIPE] OREDA Table 5 lists several sub units; matched to all
- LUBS-PIPE [is_a:: PIPE] OREDA Table 5 lists several sub units; matched to all
- MISC-PIPE [is_a:: PIPE] OREDA Table 5 lists several sub units; matched to all
- LUBS-RSHT [is_a:: RSHT] OREDA Table 5 lists several sub units; matched to all
- SHSS-RSHT [is_a:: RSHT] OREDA Table 5 lists several sub units; matched to all
- CPUN-CHKV [is_a:: CHKV] not in Table 5; assigned by judgement
- CPUN-IPIP [is_a:: IPIP] not in Table 5; assigned by judgement
- CTMN-CICV [is_a:: CICV] not in Table 5; assigned by judgement
- PWTR-CPDR [is_a:: CPDR] not in Table 5; assigned by judgement
- PWTR-CPDN [is_a:: CPDN] not in Table 5; assigned by judgement
- LUBS-LUBE [is_a:: LUBE] not in Table 5; assigned by judgement
- LUBS-OTHT [is_a:: OTHT] not in Table 5; assigned by judgement
- MISC-PSPB [is_a:: PSPB] not in Table 5; assigned by judgement
- INST [has_value:: 7] OREDA instrument types merged into one item: flow, general, level, pressure, speed, temperature, vibration; % summed, mechanisms union
- Placeholder Items [has_failure_rate_share:: 13.96%] items Other, Subunit, Unknown excluded
- No. of Maintainable Items [has_value:: 258] sheet Summary by Failure Mode column; counts failure mode/item pairs, not unique items [contested:: true]
- No. of Maintainable Items [contradicts:: [[Maintainable Item]]] column name implies items but unique items are 44 [contested:: true]
- [[Maintainable Item]] [related_to:: [[Failure Hierarchy]]] sub unit assignment differs between sources for Instruments, Valves, Internal piping, Check valves [contested:: true]
- [[Maintainable Item]] [differs_from:: OREDA Per-Type Instrument Items] OREDA per-type charts list instrument types separately; dataset merges them by design
- [[Maintainable Item]] [defined_in:: [[ISO 14224]]] cl. 3.48 p.10: part or assembly, normally lowest level when doing maintenance
- [[Maintainable Item]] [at_level:: ISO 8] Component/MI, under subunit level 7, above part level 9 optional (cl. 8.2, p.30-31); see [[ISO 14224 Taxonomy]]
- [[Maintainable Item]] [differs_from:: [[ISO 14224]]] 44 4-letter codes are dataset/wiki only; ISO Table A.9 p.65 uses full names, no codes
- [[Maintainable Item]] [related_to:: [[Compressor Subdivision Wiki vs ISO 14224]]] items in ISO not in dataset and vice versa; scope difference, no new contradiction
- [[ISO 14224]] [applies_to:: [[Maintainable Item]]] recommends Others and Unknown items in every subdivision table (cl. A.1.1, p.46)
- [[Failure Data Recording]] [uses:: [[Maintainable Item]]] failure record must store failed MI (ISO Table 6, p.40-41)
- Object Part [related_to:: [[Maintainable Item]]] RBMM p.151-152; interpreted as close to MI, book does not equate them [confidence:: low]
- [[Spare Parts Management]] [applies_to:: [[Maintainable Item]]] spare parts and criticality per item

---
title: Maintainable Item
created: 2026-10-20
updated: 2026-10-21
type: concept
tags: [maintainable-item, taxonomy, oreda, coding]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__maintainable-item-code.csv, compressor-failure-hierarchy__notes.csv, failure-structure.md, failure-structure__sheet1.csv, reliability-based-maintenance-management.md]
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

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความ ไม่ใช่ข้อความใน OREDA: RBMM ใช้คำ **Object Part** (ชิ้นส่วนต้นตอของปัญหา, RBMM p.151-152) ซึ่งตีความได้ว่าใกล้เคียง Maintainable Item แต่หนังสือไม่ได้เทียบตรง ดู [[Failure Data Recording]] และ [[RBMM Concepts vs Compressor Failure Hierarchy]] การกำหนดอะไหล่และ criticality ต่อ item ดู [[Spare Parts Management]] และ [[Spare Part Criticality and Risk]]

---
title: Compressor Subdivision Wiki vs ISO 14224
created: 2026-10-21
updated: 2026-10-22
type: comparison
tags: [comparison, iso-14224, oreda, compressor, sub-unit, maintainable-item, taxonomy, coding]
sources: [iso-14224.md, compressor-failure-hierarchy.md, failure-structure.md]
confidence: high
contested: false
---

# Compressor Subdivision: Wiki (OREDA dataset) vs ISO 14224

เทียบการแบ่ง sub unit และ maintainable item ของ [[Compressor]] ใน dataset หลักของ wiki ([[Failure Hierarchy]], [[Maintainable Item]]) กับ Table A.9 ของ [[ISO 14224]] (ISO 14224 Table A.9, p.65) ซึ่งตรวจกับภาพหน้า PDF ที่ render แล้ว ทั้งสองเป็นคนละ source ที่ใช้ขอบเขตต่างกัน (ISO = taxonomy มาตรฐานกลาง, dataset = การจัดของ OREDA/ผู้จัดทำ) ความต่างจึงเป็น **ความต่างของ scope** ไม่ใช่ข้อขัดแย้งที่ต้องตัดสิน (ส่วน conflict ระหว่างสอง source ภายใน wiki ดู [[Failure Hierarchy]])

## ข้อสรุปหลัก

- จำนวนและชื่อ sub unit ตรงกัน 6 ตัว: Power transmission (PWTR), Compressor (CPUN), Control and monitoring (CTMN), Lubrication system (LUBS), Shaft seal system (SHSS), Miscellaneous (MISC)
- **รหัส 4 ตัวอักษรของ subunit และ item (PWTR, CPUN, GBVD, ASRG ฯลฯ) ไม่ได้มาจาก ISO 14224** มาตรฐานใช้ชื่อเต็มเท่านั้น (ISO 14224 Table A.9, p.65) รหัสเหล่านี้ใช้ได้เฉพาะภายใน dataset/wiki นี้
- Table A.9 เป็นตารางเดียวใช้กับทุก compressor type: Piston, Cylinder liner, Packing เป็นของ reciprocating ส่วน Rotor, Balance piston, Antisurge เป็นของ turbo-type (การตีความ ไม่ได้ระบุใน table)
- ISO แนะนำให้เผื่อ "Others" และ "Unknown" ในตาราง subdivision (cl. A.1.1, p.46) ตรงกับ placeholder Other/Unknown ที่ OREDA มี (dataset หลักตัดทิ้ง 13.96%)

## เทียบรายการต่อ sub unit

สัญลักษณ์: ตรง = ชื่อและ sub unit ตรงกัน; เฉพาะ ISO; เฉพาะ dataset; ต่างตำแหน่ง/รูปแบบ

### Power transmission (PWTR)

| Item | ผลเทียบ |
|---|---|
| Gearbox/variable drive (GBVD), Bearing(s) (BRNG), Coupling to driver (CPDR), Coupling to driven unit (CPDN), Lubrication (LUBR), Seals (SEAL) | ตรง |
| Belt/sheave | เฉพาะ ISO |
| Instruments (INST) | เฉพาะ dataset (ISO ไม่มี item นี้ใน PWTR) |

### Compressor (CPUN)

| Item | ผลเทียบ |
|---|---|
| Casing, Rotor w/ impellers, Interstage seals, Radial bearing, Thrust bearing, Shaft seals, Internal piping, Valves, Antisurge system, Piston(s), Cylinder liner, Packing | ตรง (12 รายการ) |
| Balance piston | เฉพาะ ISO |
| Instruments (INST), Piping (PIPE), Check valves (CHKV) | เฉพาะ dataset ใน sub unit นี้ |

หมายเหตุ: Internal piping อยู่ใน Compressor subunit ตาม ISO สนับสนุน dataset หลัก ส่วน failure-structure Sheet1 วางไว้ใน Miscellaneous (ISO Table A.9, p.65) Antisurge ใน ISO รวม recycle valve และ controller

### Control and monitoring (CTMN)

| Item | ผลเทียบ |
|---|---|
| Actuating device (ACTD), Control unit (CTUN), Cables and junction boxes (CBJB), Internal power supply (IPSU), Monitoring (MONI), Valves (VALV) | ตรง |
| Sensors (ระบุชนิด เช่น pressure, temperature, level), Wiring, Piping, Seals | เฉพาะ ISO |
| Control-, isolating & check valves (CICV) | เฉพาะ dataset: ISO แยกเป็น Control valves, Isolation valves, Check valves และวางไว้ใน Miscellaneous |
| Instruments (INST) | dataset รวมประเภท instrument เป็น item เดียว ISO ใช้ "Sensors" ใน CTMN เท่านั้น |

### Lubrication system (LUBS)

| Item | ผลเทียบ |
|---|---|
| Oil tank w/heating system (OTHT), Filter(s) (FILT), Cooler(s) (COOL), Piping (PIPE), Valves (VALV), Lube oil (LUBE) | ตรง |
| Pump w/motor (PMTR) | ต่างรูปแบบ: ISO แยก Pump กับ Motor เป็นสอง item |
| Check valves | เฉพาะ ISO ใน LUBS (dataset วาง CHKV ใน CPUN) |
| Reservoir w/heating system (RSHT), Oil (OILS), Seals (SEAL), Instruments (INST) | เฉพาะ dataset ใน LUBS: ISO มี Oil tank with heating system อย่างเดียว, ไม่มี Seals ใน LUBS (Seals อยู่ใน PWTR และ CTMN) |

### Shaft seal system (SHSS)

| Item | ผลเทียบ |
|---|---|
| Filter(s) (FILT), Valves (VALV), Seal oil (SOIL), Dry gas seal (DGSL) | ตรง |
| Reservoir w/heating system (RSHT) | ใกล้เคียง: ISO มีทั้ง Oil tank with heating และ Reservoir (ไม่มี heating) แยกกัน |
| Pump w/motor/gear (PMGR) | ต่างรูปแบบ: ISO แยก Pump, Motor, Gear |
| Oil tank with heating, Mechanical seal, Scrubber | เฉพาะ ISO |
| Seal gas (SGAS), Buffer gas system (BFGS), Overhead tank (OHTK), Instruments (INST) | เฉพาะ dataset |

### Miscellaneous (MISC)

| Item | ผลเทียบ |
|---|---|
| Base frame (BASE), Piping/pipe support + bellows (PSPB), Cooler(s) (COOL), Silencers (SILN), Purge air (PAIR) | ตรง |
| Valves (VALV) | ต่างรูปแบบ: ISO แยก Control valves, Isolation valves, Check valves |
| Magnetic-bearing control system, Flange joints | เฉพาะ ISO |
| Piping (PIPE) | เฉพาะ dataset ใน MISC (ISO ใช้ชื่อ piping, pipe support and bellows) |

## จุดที่ item อยู่ต่าง sub unit (สรุป)

| Item | dataset หลัก | ISO Table A.9 |
|---|---|---|
| Instruments | 5 sub unit (PWTR, CPUN, CTMN, LUBS, SHSS) | มีเฉพาะ "Sensors" ใน CTMN (แต่ boundary rule ให้นับ instrument ที่ติดบนเครื่องในขอบเขต cl. A.1.2, p.46-47) |
| Control/isolating/check valves | CICV ใน CTMN | Control, Isolation, Check valves ใน MISC |
| Check valves | CHKV ใน CPUN | LUBS และ MISC (ไม่อยู่ใน Compressor subunit) |
| Piping | CPUN, LUBS, MISC | Internal piping ใน Compressor; Piping ใน CTMN และ LUBS; Piping/pipe support/bellows ใน MISC |
| Seals | PWTR, LUBS | PWTR, CTMN |
| Reservoir w/heating | LUBS, SHSS | LUBS: Oil tank with heating; SHSS: Oil tank with heating และ Reservoir |

ผลต่อ wiki: ในความขัดแย้งสอง source ภายใน wiki เรื่อง Instruments ISO ใกล้มุมมอง failure-structure Sheet1 (Instrument อยู่ CTMN) มากกว่า dataset หลัก แต่เรื่อง Internal piping ISO สนับสนุน dataset หลัก และเรื่อง Valves/Check valves/Piping ISO ไม่ตรงกับทั้งสอง source (ดูตารางใน [[Failure Hierarchy]]) ISO จึงเป็นข้อมูลอ้างอิงเพิ่มไม่ใช่ตัวตัดสิน เพราะ % ของ OREDA ผูกกับการจัดแบบ dataset

## Item ที่ ISO มีแต่ dataset ไม่มี

Belt/sheave, Balance piston, Sensors, Wiring, Pump และ Motor (แยก), Gear (แยก), Mechanical seal, Scrubber, Control valves, Isolation valves, Magnetic-bearing control system, Flange joints (และ Check valves ใน LUBS/MISC, Oil tank with heating ใน SHSS)

## Item ที่ dataset มีแต่ ISO ไม่มี

Instruments (INST ใน 5 sub unit), CICV, Oil (OILS) ที่แยกจาก Lube oil, Reservoir w/heating ใน LUBS, Seal gas, Buffer gas system, Overhead tank, Seals ใน LUBS, Piping ใน CPUN/MISC, Check valves ใน CPUN (ส่วนใหญ่น่ามาจาก OREDA ที่ละเอียดกว่าในบางจุด ISO Table A.9 ไม่มีรายการเหล่านี้)

## Compressor type และ boundary

| ประเด็น | wiki | ISO 14224 |
|---|---|---|
| Type | Centrifugal, Reciprocating, Screw | CE Centrifugal, RE Reciprocating, SC Screw, **AX Axial** (Table A.8, p.64) |
| Class | compressor (COCE ใน dataset) | CO Compressors **รวม air compressor**; Blowers/fans (BL) แยก class และไม่รวม air compressor (Table A.4) |
| Driver | ไม่ได้ระบุใน dataset | อยู่นอก boundary พร้อม auxiliary; บันทึกเป็น inventory แยก (EM, GT, CE) และ compressor inventory มีเลขอ้างอิงถึง driver (cl. A.2.2.2.1, p.64-65) |
| Inlet/outlet valve | ไม่ได้ระบุ | อยู่นอก boundary (p.64-65) |
| Train | ไม่ได้ระบุ | 1 compressor train = 1 inventory ได้ถึง 4 stage; ปกติ 1 stage = 1 casing (บางครั้ง 1 casing = 2 stage) (p.64-65) |
| Subunit ที่ใช้ร่วมกับ driver | ไม่ได้ระบุ | นับเป็นของ compressor (driven unit) (p.65; cl. A.1.2, p.46-47) |
| Lube/seal oil ร่วมกัน | ไม่ได้ระบุ | ลง failure ที่ subunit ที่ได้รับผลมากที่สุด ถ้าไม่ชัดเจนลงที่ lubrication system (p.65) |

หมายเหตุ: รหัส type CE ของ compressor ซ้ำกับรหัส class CE (Combustion engines) แต่เป็นคนละระดับ (Table A.8) ข้อความ boundary ในมาตรฐานอ้าง "Figure A.2" แต่รูปที่ถูกคือ Figure A.3 (น่าจะพิมพ์ผิด) ดู [[ISO 14224 Taxonomy]] เรื่องระดับ taxonomy

## Equipment-specific data (Table A.10, p.65-66)

ISO กำหนดฟิลด์ inventory เฉพาะ compressor เพิ่มเติม เช่น compressed medium, type of driver, discharge pressure design, flow rate design, design power, number of casings in train และ shaft seal system (priority high) ซึ่ง dataset ไม่มี (ดู [[Compressor]])

## ดูเพิ่ม

- [[Failure Hierarchy]]
- [[Maintainable Item]]
- [[Compressor]]
- [[ISO 14224 Taxonomy]]
- [[ISO 14224]]
- [[PWTR Power Transmission]], [[CPUN Compressor Unit]], [[CTMN Control and Monitoring]], [[LUBS Lubrication System]], [[SHSS Shaft Seal System]], [[MISC Miscellaneous]]

## Triplets

- [[PWTR Power Transmission]] [maps_to:: ISO:A.9-Power transmission] same name; 4-letter code is dataset/wiki only, not from ISO (ISO 14224 Table A.9, p.65)
- [[CPUN Compressor Unit]] [maps_to:: ISO:A.9-Compressor] same name; 4-letter code is dataset/wiki only, not from ISO (ISO 14224 Table A.9, p.65)
- [[CTMN Control and Monitoring]] [maps_to:: ISO:A.9-Control and monitoring] same name; 4-letter code is dataset/wiki only, not from ISO (ISO 14224 Table A.9, p.65)
- [[LUBS Lubrication System]] [maps_to:: ISO:A.9-Lubrication system] same name; 4-letter code is dataset/wiki only, not from ISO (ISO 14224 Table A.9, p.65)
- [[SHSS Shaft Seal System]] [maps_to:: ISO:A.9-Shaft seal system] same name; 4-letter code is dataset/wiki only, not from ISO (ISO 14224 Table A.9, p.65)
- [[MISC Miscellaneous]] [maps_to:: ISO:A.9-Miscellaneous] same name; 4-letter code is dataset/wiki only, not from ISO (ISO 14224 Table A.9, p.65)
- PWTR-GBVD [maps_to:: ISO:A.9-Gearbox/variable drive] match, in Power transmission (ISO 14224 Table A.9, p.65)
- PWTR-BRNG [maps_to:: ISO:A.9-Bearing(s)] match, in Power transmission (ISO 14224 Table A.9, p.65)
- PWTR-CPDR [maps_to:: ISO:A.9-Coupling to driver] match, in Power transmission (ISO 14224 Table A.9, p.65)
- PWTR-CPDN [maps_to:: ISO:A.9-Coupling to driven unit] match, in Power transmission (ISO 14224 Table A.9, p.65)
- PWTR-LUBR [maps_to:: ISO:A.9-Lubrication] match, in Power transmission (ISO 14224 Table A.9, p.65)
- PWTR-SEAL [maps_to:: ISO:A.9-Seals] match, in Power transmission (ISO 14224 Table A.9, p.65)
- ISO:A.9-Belt/sheave [part_of:: ISO:A.9-Power transmission] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- PWTR-INST [differs_from:: ISO:A.9-Power transmission] dataset only in this sub unit; ISO has no Instruments item in PWTR (ISO 14224 Table A.9, p.65)
- CPUN-CASG [maps_to:: ISO:A.9-Casing] match, in Compressor (ISO 14224 Table A.9, p.65)
- CPUN-ROTR [maps_to:: ISO:A.9-Rotor w/ impellers] match, in Compressor (ISO 14224 Table A.9, p.65)
- CPUN-INSS [maps_to:: ISO:A.9-Interstage seals] match, in Compressor (ISO 14224 Table A.9, p.65)
- CPUN-RBRG [maps_to:: ISO:A.9-Radial bearing] match, in Compressor (ISO 14224 Table A.9, p.65)
- CPUN-THRB [maps_to:: ISO:A.9-Thrust bearing] match, in Compressor (ISO 14224 Table A.9, p.65)
- CPUN-SHSL [maps_to:: ISO:A.9-Shaft seals] match, in Compressor (ISO 14224 Table A.9, p.65)
- CPUN-PSTN [maps_to:: ISO:A.9-Piston(s)] match, in Compressor (ISO 14224 Table A.9, p.65)
- CPUN-CYLN [maps_to:: ISO:A.9-Cylinder liner] match, in Compressor (ISO 14224 Table A.9, p.65)
- CPUN-PACK [maps_to:: ISO:A.9-Packing] match, in Compressor (ISO 14224 Table A.9, p.65)
- CPUN-VALV [maps_to:: ISO:A.9-Valves] match, in Compressor (ISO 14224 Table A.9, p.65)
- CPUN-IPIP [maps_to:: ISO:A.9-Internal piping] match; ISO places it in Compressor subunit, supports main dataset (failure-structure Sheet1 places it in Miscellaneous) (ISO 14224 Table A.9, p.65)
- CPUN-ASRG [maps_to:: ISO:A.9-Antisurge system] match; ISO Antisurge includes recycle valve and controller (ISO 14224 Table A.9, p.65)
- ISO:A.9-Balance piston [part_of:: ISO:A.9-Compressor] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- CPUN-INST [differs_from:: ISO:A.9-Compressor] dataset only in this sub unit; ISO has no Instruments item in Compressor subunit (ISO 14224 Table A.9, p.65)
- CPUN-PIPE [differs_from:: ISO:A.9-Compressor] dataset only in this sub unit; ISO has Internal piping only (ISO 14224 Table A.9, p.65)
- CPUN-CHKV [differs_from:: ISO:A.9-Compressor] dataset only in this sub unit; ISO puts Check valves in LUBS and MISC (ISO 14224 Table A.9, p.65)
- ISO:A.9-Piston(s) [related_to:: [[Reciprocating Compressor]]] reciprocating item; one Table A.9 for all types (interpretation, not in table) [confidence:: medium]
- ISO:A.9-Cylinder liner [related_to:: [[Reciprocating Compressor]]] reciprocating item; one Table A.9 for all types (interpretation, not in table) [confidence:: medium]
- ISO:A.9-Packing [related_to:: [[Reciprocating Compressor]]] reciprocating item; one Table A.9 for all types (interpretation, not in table) [confidence:: medium]
- ISO:A.9-Rotor w/ impellers [related_to:: [[Centrifugal Compressor]]] turbo-type item (interpretation, not in table) [confidence:: medium]
- ISO:A.9-Balance piston [related_to:: [[Centrifugal Compressor]]] turbo-type item (interpretation, not in table) [confidence:: medium]
- ISO:A.9-Antisurge system [related_to:: [[Centrifugal Compressor]]] turbo-type item (interpretation, not in table) [confidence:: medium]
- CTMN-ACTD [maps_to:: ISO:A.9-Actuating device] match, in Control and monitoring (ISO 14224 Table A.9, p.65)
- CTMN-CTUN [maps_to:: ISO:A.9-Control unit] match, in Control and monitoring (ISO 14224 Table A.9, p.65)
- CTMN-CBJB [maps_to:: ISO:A.9-Cables and junction boxes] match, in Control and monitoring (ISO 14224 Table A.9, p.65)
- CTMN-IPSU [maps_to:: ISO:A.9-Internal power supply] match, in Control and monitoring (ISO 14224 Table A.9, p.65)
- CTMN-MONI [maps_to:: ISO:A.9-Monitoring] match, in Control and monitoring (ISO 14224 Table A.9, p.65)
- CTMN-VALV [maps_to:: ISO:A.9-Valves] match, in Control and monitoring (ISO 14224 Table A.9, p.65)
- ISO:A.9-Sensors [part_of:: ISO:A.9-Control and monitoring] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- ISO:A.9-Wiring [part_of:: ISO:A.9-Control and monitoring] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- ISO:A.9-Piping [part_of:: ISO:A.9-Control and monitoring] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- ISO:A.9-Seals [part_of:: ISO:A.9-Control and monitoring] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- CTMN-CICV [differs_from:: ISO:A.9-Control valves] dataset combines; ISO splits Control, Isolation, Check valves and places them in Miscellaneous (ISO 14224 Table A.9, p.65)
- CTMN-CICV [differs_from:: ISO:A.9-Isolation valves] dataset combines; ISO splits Control, Isolation, Check valves and places them in Miscellaneous (ISO 14224 Table A.9, p.65)
- CTMN-CICV [differs_from:: ISO:A.9-Check valves] dataset combines; ISO splits Control, Isolation, Check valves and places them in Miscellaneous (ISO 14224 Table A.9, p.65)
- CTMN-INST [differs_from:: ISO:A.9-Sensors] dataset lumps instrument types into one item; ISO uses Sensors in CTMN only (ISO 14224 Table A.9, p.65)
- LUBS-OTHT [maps_to:: ISO:A.9-Oil tank w/heating system] match, in Lubrication system (ISO 14224 Table A.9, p.65)
- LUBS-FILT [maps_to:: ISO:A.9-Filter(s)] match, in Lubrication system (ISO 14224 Table A.9, p.65)
- LUBS-COOL [maps_to:: ISO:A.9-Cooler(s)] match, in Lubrication system (ISO 14224 Table A.9, p.65)
- LUBS-PIPE [maps_to:: ISO:A.9-Piping] match, in Lubrication system (ISO 14224 Table A.9, p.65)
- LUBS-VALV [maps_to:: ISO:A.9-Valves] match, in Lubrication system (ISO 14224 Table A.9, p.65)
- LUBS-LUBE [maps_to:: ISO:A.9-Lube oil] match, in Lubrication system (ISO 14224 Table A.9, p.65)
- LUBS-PMTR [differs_from:: ISO:A.9-Pump] different form; ISO splits Pump and Motor into two items (ISO 14224 Table A.9, p.65)
- LUBS-PMTR [differs_from:: ISO:A.9-Motor] different form; ISO splits Pump and Motor into two items (ISO 14224 Table A.9, p.65)
- ISO:A.9-Check valves [part_of:: ISO:A.9-Lubrication system] ISO only, no dataset item in LUBS (dataset puts CHKV in CPUN) (ISO 14224 Table A.9, p.65)
- LUBS-RSHT [differs_from:: ISO:A.9-Lubrication system] dataset only in this sub unit; ISO has Oil tank with heating system only (ISO 14224 Table A.9, p.65)
- LUBS-OILS [differs_from:: ISO:A.9-Lubrication system] dataset only in this sub unit; ISO has Lube oil only (ISO 14224 Table A.9, p.65)
- LUBS-SEAL [differs_from:: ISO:A.9-Lubrication system] dataset only in this sub unit; ISO has Seals in PWTR and CTMN, not LUBS (ISO 14224 Table A.9, p.65)
- LUBS-INST [differs_from:: ISO:A.9-Lubrication system] dataset only in this sub unit; ISO has no Instruments item in LUBS (ISO 14224 Table A.9, p.65)
- SHSS-FILT [maps_to:: ISO:A.9-Filter(s)] match, in Shaft seal system (ISO 14224 Table A.9, p.65)
- SHSS-VALV [maps_to:: ISO:A.9-Valves] match, in Shaft seal system (ISO 14224 Table A.9, p.65)
- SHSS-SOIL [maps_to:: ISO:A.9-Seal oil] match, in Shaft seal system (ISO 14224 Table A.9, p.65)
- SHSS-DGSL [maps_to:: ISO:A.9-Dry gas seal] match, in Shaft seal system (ISO 14224 Table A.9, p.65)
- SHSS-RSHT [maps_to:: ISO:A.9-Reservoir] close; ISO lists Oil tank with heating and Reservoir (no heating) separately (ISO 14224 Table A.9, p.65)
- SHSS-PMGR [differs_from:: ISO:A.9-Pump] different form; ISO splits Pump, Motor, Gear (ISO 14224 Table A.9, p.65)
- SHSS-PMGR [differs_from:: ISO:A.9-Motor] different form; ISO splits Pump, Motor, Gear (ISO 14224 Table A.9, p.65)
- SHSS-PMGR [differs_from:: ISO:A.9-Gear] different form; ISO splits Pump, Motor, Gear (ISO 14224 Table A.9, p.65)
- ISO:A.9-Oil tank with heating [part_of:: ISO:A.9-Shaft seal system] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- ISO:A.9-Mechanical seal [part_of:: ISO:A.9-Shaft seal system] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- ISO:A.9-Scrubber [part_of:: ISO:A.9-Shaft seal system] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- SHSS-SGAS [differs_from:: ISO:A.9-Shaft seal system] dataset only in this sub unit; no ISO counterpart (ISO 14224 Table A.9, p.65)
- SHSS-BFGS [differs_from:: ISO:A.9-Shaft seal system] dataset only in this sub unit; no ISO counterpart (ISO 14224 Table A.9, p.65)
- SHSS-OHTK [differs_from:: ISO:A.9-Shaft seal system] dataset only in this sub unit; no ISO counterpart (ISO 14224 Table A.9, p.65)
- SHSS-INST [differs_from:: ISO:A.9-Shaft seal system] dataset only in this sub unit; no ISO counterpart (ISO 14224 Table A.9, p.65)
- MISC-BASE [maps_to:: ISO:A.9-Base frame] match, in Miscellaneous (ISO 14224 Table A.9, p.65)
- MISC-PSPB [maps_to:: ISO:A.9-Piping/pipe support + bellows] match, in Miscellaneous (ISO 14224 Table A.9, p.65)
- MISC-COOL [maps_to:: ISO:A.9-Cooler(s)] match, in Miscellaneous (ISO 14224 Table A.9, p.65)
- MISC-SILN [maps_to:: ISO:A.9-Silencers] match, in Miscellaneous (ISO 14224 Table A.9, p.65)
- MISC-PAIR [maps_to:: ISO:A.9-Purge air] match, in Miscellaneous (ISO 14224 Table A.9, p.65)
- MISC-VALV [differs_from:: ISO:A.9-Control valves] different form; ISO splits Control, Isolation, Check valves (ISO 14224 Table A.9, p.65)
- MISC-VALV [differs_from:: ISO:A.9-Isolation valves] different form; ISO splits Control, Isolation, Check valves (ISO 14224 Table A.9, p.65)
- MISC-VALV [differs_from:: ISO:A.9-Check valves] different form; ISO splits Control, Isolation, Check valves (ISO 14224 Table A.9, p.65)
- ISO:A.9-Magnetic-bearing control system [part_of:: ISO:A.9-Miscellaneous] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- ISO:A.9-Flange joints [part_of:: ISO:A.9-Miscellaneous] ISO only, no dataset item (ISO 14224 Table A.9, p.65)
- MISC-PIPE [differs_from:: ISO:A.9-Miscellaneous] dataset only in this sub unit; ISO uses piping, pipe support and bellows (ISO 14224 Table A.9, p.65)
- INST [differs_from:: ISO:A.9-Sensors] dataset: Instruments in 5 sub units (PWTR, CPUN, CTMN, LUBS, SHSS); ISO: Sensors in CTMN only (boundary rule counts mounted instruments, cl. A.1.2, p.46-47)
- CHKV [differs_from:: ISO:A.9-Check valves] dataset: CPUN; ISO: LUBS and MISC (not Compressor subunit) (ISO 14224 Table A.9, p.65)
- PIPE [differs_from:: ISO:A.9-Piping] dataset: CPUN, LUBS, MISC; ISO: Internal piping in Compressor, Piping in CTMN and LUBS, piping/pipe support/bellows in MISC (ISO 14224 Table A.9, p.65)
- SEAL [differs_from:: ISO:A.9-Seals] dataset: PWTR, LUBS; ISO: PWTR, CTMN (ISO 14224 Table A.9, p.65)
- RSHT [differs_from:: ISO:A.9-Oil tank with heating] dataset: LUBS, SHSS; ISO: LUBS Oil tank with heating, SHSS Oil tank with heating and Reservoir (ISO 14224 Table A.9, p.65)
- [[ISO 14224]] [related_to:: [[OREDA]]] recommends Others/Unknown rows in subdivision (cl. A.1.1, p.46), matching OREDA placeholders that main dataset excludes (13.96%)
- [[Centrifugal Compressor]] [maps_to:: ISO:A.8-CE] (Table A.8, p.64)
- [[Reciprocating Compressor]] [maps_to:: ISO:A.8-RE] (Table A.8, p.64)
- [[Screw Compressor]] [maps_to:: ISO:A.8-SC] (Table A.8, p.64)
- ISO:A.8-AX [has_label:: Axial] ISO only; not in wiki (Table A.8, p.64)
- ISO:A.8-CE [differs_from:: ISO:A.4-CE] same code, different level: compressor type vs class Combustion engines (Table A.8)
- [[Compressor]] [has_code:: COCE] dataset class code
- [[Compressor]] [maps_to:: ISO:A.4-CO] ISO class CO Compressors includes air compressor (Table A.4)
- ISO:A.4-BL [differs_from:: ISO:A.4-CO] Blowers/fans separate class, excludes air compressor (Table A.4)
- Driver [differs_from:: [[Compressor]]] outside ISO boundary with auxiliaries; separate inventory (EM, GT, CE) referenced from compressor inventory (cl. A.2.2.2.1, p.64-65); not specified in dataset
- Inlet/outlet valve [differs_from:: [[Compressor]]] outside ISO boundary (p.64-65); not specified in dataset
- Compressor train [has_value:: 4] max stages per inventory; usually 1 stage = 1 casing (p.64-65)
- Shared Lube/Seal Oil Failure [related_to:: [[LUBS Lubrication System]]] ISO: record at most affected subunit, if unclear at lubrication system (p.65)

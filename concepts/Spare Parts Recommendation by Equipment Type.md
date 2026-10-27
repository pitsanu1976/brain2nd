---
title: Spare Parts Recommendation by Equipment Type
created: 2026-10-27
updated: 2026-10-27
type: concept
tags: [spo, book, spare-parts, compressor, centrifugal, reciprocating, maintainable-item, maintenance-management, inventory-control]
sources: [spare-parts-optimization.md]
confidence: medium
contested: false
---

# Spare Parts Recommendation by Equipment Type

หลักปฏิบัติพื้นฐานทางวิศวกรรม (Engineering Basic Practice, BP) ในบทที่ 5 ของ [[Spare Parts Optimization Book]] ใช้กำหนด **จำนวนอะไหล่ขั้นต่ำ (minimum spare parts requirements)** ต่อชนิดอุปกรณ์ เพื่อให้ SKU ของคลังยึดหลักวิศวกรรม ไม่ใช่ความรู้สึก (SPO p.40) ตัวอย่างทั้งหมดมาจากโรงกลั่นน้ำมัน มี 2 แบบ: แบบบริษัทอเมริกัน (ตารางขั้นบันไดตามจำนวนเครื่อง) และแบบบริษัทญี่ปุ่น (% ของจำนวนชิ้นที่ติดตั้ง) หน้านี้สรุปตารางหลักและเชื่อมกับ compressor failure hierarchy ของ wiki ภาพรวมการบริหารอะไหล่ดู [[Spare Parts Management]]

## วัตถุประสงค์และขอบเขต

- BP เป็นคำแนะนำ "สต็อกขั้นต่ำ" ไม่ใช่สูตรที่การันตีว่ามีอะไหล่ทุกรายการตลอดเวลา ต้องพิจารณารายเครื่องร่วมกับคำแนะนำผู้ผลิตและสถิติการเปลี่ยนอะไหล่ (SPO p.40)
- เกณฑ์เวลา (ตัวอย่างอเมริกัน): อะไหล่สำหรับ **startup + เดินเครื่องต่อเนื่อง 1 ปี** (SPO p.40-41)
- ผู้จัดทำสมุดคู่มือการเก็บสต็อก = ฝ่ายวิศวกรรมโรงงานหรือผู้รับผิดชอบตามโครงสร้างองค์กร (SPO p.40)
- ตัวเลขในตัวอย่างอเมริกันเป็นขั้นต่ำ ปรับเพิ่มได้; BP สร้างจากสถิติการซ่อม/เปลี่ยนอะไหล่หลายปีหลายโรงงาน ครอบคลุม breakdown, condition-based, time-based replacement และ annual shutdown (SPO p.57-58)
- **ทบทวนหลังเดินเครื่องจริงประมาณ 2-3 ปี** เมื่อได้สถิติที่ดีกว่า; คำแนะนำผู้ผลิตเป็นแค่คำแนะนำ การตัดสินสุดท้ายเป็นของวิศวกรบริษัท (SPO p.57)
- ถ้าไม่มีแนวทาง: อะไหล่สำคัญขาดมือจนการผลิตหยุด หรือสต็อกเกินจนเป็น dead stock มูลค่าสูง (SPO p.57)

### อะไหล่ที่เข้าเกณฑ์ (ตัวอย่างอเมริกัน, SPO p.41)

ชิ้นที่ (1) สึกหรอ/กัดกร่อน/erosion ในการทำงานปกติ (2) เสียแล้วทำให้เครื่องหยุด (3) เสียหาย/แตกระหว่างซ่อมบำรุงหรือตรวจสภาพตามปกติ พิจารณาเพิ่มเมื่อแหล่งจัดหาอยู่ไกล, delivery นานผิดปกติ, ใช้ร่วม (common sparing) กับเครื่องเดิมได้ หรือทำ consigned stock กับ supplier ได้

ควรขอ spare parts quotation พร้อม proposal ของเครื่อง โดยมีข้อมูล 8 ข้อ: equipment ID, part no./คำอธิบาย/วัสดุ, sectional drawing, จำนวนแนะนำ, ราคาต่อหน่วยและรวม, น้ำหนัก, delivery time และ interchangeability กับเครื่องอื่น (SPO p.41) ดู [[Parts Interchangeability]]

### 5 ปัจจัยในการกำหนดรายเครื่อง (SPO p.40)

1. อะไหล่ที่สึกหรอ/ผุกร่อนง่าย
2. สภาพแวดล้อม (เช่น ใกล้ทะเล)
3. สภาพการใช้งาน (สารละลาย กรด-ด่าง อุณหภูมิสูง)
4. ความยากในการจัดหา (lead time นาน ไม่มีในตลาด ทำเทียมไม่ได้)
5. ใช้ร่วมหลายเครื่องได้หรือมีอะไหล่เทียบเคียงหรือไม่

## ตัวอย่างที่ 1: แบบบริษัทอเมริกัน (SPO p.40-45)

Compressor (centrifugal, reciprocating, rotary) อยู่ในกลุ่ม mechanical equipment 16 ประเภทที่ให้กำหนดอะไหล่ร่วมกับ vendor ตามเจตนารมณ์ BP **โดยไม่มีตารางจำนวน** (SPO p.41) ตารางจำนวนของ compressor อยู่ในตัวอย่างญี่ปุ่น

### Centrifugal pumps, Table 1 (SPO p.42)

จำนวนอะไหล่ตามจำนวนปั๊มที่ใช้ part เดียวกัน

| Part | 1 | 2 | 3 | 4 | 5 | 6 | 7 ขึ้นไป |
|---|---|---|---|---|---|---|---|
| Shaft, Impeller, Throat bushing | 1 | 1 | 1 | 2 | 2 | 2 | 30% ของจำนวนปั๊ม |
| Shaft sleeve, Bearing set, Impeller & case wearing rings | 1 | 1 | 2 | 2 | 3 | 3 | 50% |
| Gasket sets, Packing, Mech. seal non-metallic faces, O-rings | 2 | 3 | 4 | 6 | 7 | 8 | 130% |
| Mech. seal metallic faces & springs | 1 | 2 | 2 | 3 | 4 | 4 | 65% |

- Impeller สำรองให้สั่ง **เส้นผ่านศูนย์กลางสูงสุด**; ตัวเลขคิดที่ 1 ชิ้นต่อปั๊ม ถ้ามีหลายชิ้นต่อปั๊มให้ปรับตาม (SPO p.42)
- ข้อสังเกตของ wiki: ขั้นบันได 30% / 50% / 130% ใช้ซ้ำใน Table 2 สำหรับชิ้นหลัก / ชิ้นสึกหรอ / ชิ้นสิ้นเปลือง

### Air fin coolers, Table 2 (SPO p.45)

| Part | 1 | 2 | 3 | 4 | 5 | 6 | 7 ขึ้นไป |
|---|---|---|---|---|---|---|---|
| V-belt sheaves | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| V-belts | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Fan shaft bearings | 1 | 1 | 2 | 2 | 3 | 3 | 50% |
| Gear box shaft & pinion | 1 | 1 | 1 | 2 | 2 | 2 | 30% |
| Gear box bearing set | 1 | 1 | 2 | 2 | 3 | 3 | 50% |
| Gear box O-rings, seals, lock-washers, locknuts | 2 | 3 | 4 | 6 | 7 | 8 | 130% |
| Couplings (complete) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Fan assy / auto pitch hub parts | 2 | 3 | 4 | 6 | 7 | 8 | 130% |
| Bolt assemblies, fork fins, bearings | 1 | 1 | 2 | 2 | 3 | 3 | 50% |
| Flexible hose, rotary union | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| Auto/manual adjustment parts | 1 | 1 | 2 | 2 | 2 | 2 | 30% |
| Spring housing gasket, diaphragm, retainer ring, thrust cover gasket | 1 | 1 | 1 | 2 | 2 | 2 | 20% |
| Hub assembly with blades | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

นอกตาราง: tubes ปกติไม่สำรอง (ยกเว้น site ห่างไกลมาก); plugs steel 1%, brass/nonferrous 2%; plug gaskets 5%; cover plate gaskets 100%; tube support boxes 10%; motor bearings 3 ชุดต่อขนาด (SPO p.43-44)

### Electrical และ Instruments (SPO p.42-43)

- Electrical (alarms, batteries/chargers, generators, motors, protective relays สำรองทั้ง unit, switchgear, transformers) กำหนดร่วมกับ vendor ไม่มีตัวเลข
- Instruments: **10% ต่อขนาด/rating ขั้นต่ำ 1** ทั้ง complete unit spares (pressure switches/gauges, dial thermometers, solenoid & trip valves, IA filters, valve positioners, plug-in assemblies ฯลฯ) และวัสดุประกอบ (thermocouple & extension wire, thermowells, seal pots, blank orifice plates ฯลฯ); flow/level/temperature/pressure instruments, control valves, analyzers กำหนดร่วมกับ vendor

### Static equipment และเตา (SPO p.43-44)

| อุปกรณ์ | จำนวนสำรอง |
|---|---|
| Heat exchanger (shell & tube) | Tubes พอ **retube bundle ใหญ่สุด** ต่อขนาด tube; gaskets 1 ชุดต่อ exchanger; special/alloy bolts 10% |
| Boilers | Tubes 5%; handhole gaskets 1 ชุด; refractory & insulation 5%; water gauge glasses 1 ชุด |
| Jet ejectors | Nozzles และ diffusers 1 ต่อขนาด |
| Furnaces | Return bends, crossovers, arch tile, insulating block, header boxes, tube supports, tubes 5% (บางรายการขั้นต่ำ 1 ต่อชนิด); plastic insulation 10%; oil gun และ burner tile 10% |
| Pressure vessels | Gaskets 1 ชุด; special/alloy bolts 10% |

## ตัวอย่างที่ 2: แบบบริษัทญี่ปุ่น (SPO p.45-54)

- 4 หมวด: pressure vessels, air-cooled HX, pump/compressor/driver, fired heater; "min.1" = อย่างน้อย 1 ชิ้น (SPO p.54)
- หนังสือไม่ได้ระบุฐานของ % ชัดเจน ตีความว่าเป็น % ของจำนวนชิ้นที่ติดตั้งใช้งาน (การตีความของผู้จด reading notes)
- รูปแบบเด่น: **gasket/O-ring 200-300%** (vessel/exchanger gasket 300%, pump/compressor gasket และ O-ring 200%) ขณะที่ **bolts & nuts เพียง 5%** (SPO p.46, p.48-51)
- Pressure vessels: gaskets 300%, bolts & nuts 5%, tray valve 5%; exchanger tube 1 bundle ต่อวัสดุ/ขนาด/ความหนา (SPO p.46)
- Air-cooled HX: shoulder plug 3%, plug-header gasket 5%, cover-header gasket 100%, V-belt/fan-shaft bearing/motor bearing 10%, fan blade 10% (ไม่เกิน 4 ชิ้นต่อชนิด, optional) (SPO p.47)
- Fired heater: tube 5%, burner tip 20%, gasket for oil gun 300% (SPO p.54)

### Centrifugal pump, 3.1.1 (SPO p.48)

| Part | Qty | หมายเหตุ |
|---|---|---|
| Impeller wearing ring / casing wearing ring | 50% (min.1) | |
| Mechanical seal | 100% | complete set |
| Seal ring & mating ring / O-ring / gasket | 200% | parts ของ mech. seal |
| Seal spring | 100% | |
| Each bearing | 100% | |
| Shaft sleeve | 50% / 100% (min.1) | mech. seal pump / packed pump |
| Impeller lock nut, washer หรือ pin | 100% | |
| Retainer ring หรือ interstage sleeve | 50% (min.1) | multistage |
| Throat bush | 50% (min.1) | |
| Gasket & O-ring | 200% | |
| Gland packing | 200% | packed pump |
| Lantern ring | 100% | |
| Balance diaphragm & labyrinth หรือ balance disc | 50% (min.1) | multistage |
| Bearing metal | 200% | vertical pump |
| Oiler | 20% (min.1) | ต่อ vendor (แถว OCR เพี้ยน) |
| Coupling | 1 | ต่อขนาด |

Reciprocating pump: cylinder valve, valve seat, gland packing, gasket & O-ring 200%; plunger และ bearing 100% (SPO p.49) Pump driver: motor bearing 100%; turbine bearing 100%, governor 100% (complete set); speed changer gasket/O-ring 200%, bearing 100%, oil seal 50% (min.1) (SPO p.49-50)

### Centrifugal compressor unit, 3.3 (SPO p.50-52)

**3.3.1 Compressor** (SPO p.50-51)

| Part | Qty | หมายเหตุ |
|---|---|---|
| Gaskets | 200% | |
| O-rings | 200% | |
| Labyrinth for balance piston | 100% | |
| Shaft sleeve | 100% | |
| Thrust bearing pad | 100% | complete set |
| Shaft lock nut & washer | 100% | |
| Bearing liner or pad | 100% | |
| Seal contact type: rotating contact ring, carbon ring | 100% | |
| Seal contact type: springs & O-rings | 200% | |
| Seal liquid film type: seal bushes & shaft sleeves, springs | 100% | |
| Seal liquid film type: O-rings | 200% | |
| Seal restrictive type: carbon rings with garter springs | 100% | |
| Seal restrictive type: O-ring, shaft sleeve | 200% | |
| Coupling | 1% (น่าจะหมายถึง 1 ชุด) | ต่อชนิด |
| Set screw for coupling | 100% | |

**3.3.2 Turbine (driver)** (SPO p.51): 100% สำหรับ thrust bearing (complete set), adjusting liner, thrust ring, journal bearing liner/pad, gland packing และ diaphragm packing (with spring), governor drive wheel/worm gear, overspeed emergency spring, Askania pressure controller (extraction turbine), earth brush (condensing turbine), labyrinth ring + spring, thrust gauge, leakage condenser gasket, main stop valve parts, condenser ejector nozzle; O-ring และ gasket 200%; leakage condenser 5%

**3.3.3 Steam condenser** (SPO p.52): tube 5%, gasket 200%, ejector nozzle 100%

**3.3.4 Auxiliary equipment** (SPO p.52)

| Part | Qty | หมายเหตุ |
|---|---|---|
| Pumps | ตามตารางปั๊ม | |
| Lube & seal oil filter cartridge | 200% | |
| Lube & seal oil filter gasket | 200% | |
| Accumulator bladder | 50% | ค่าอยู่ในคอลัมน์ Remarks ใน OCR |
| Accumulator seal ring | 100% | |
| Seal oil system: transfer barrier bladder, accumulator bladder | 50% | ค่าอยู่ในคอลัมน์ Remarks |
| Seal oil system: transfer barrier seal ring, accumulator seal ring | 100% | |
| Auxiliary turbine | ตามตาราง pump drivers | |

### Reciprocating compressor unit, 3.4 (SPO p.52-53)

**3.4.1 Compressor**

| Part | Qty | หมายเหตุ |
|---|---|---|
| Suction valve (assembly) | 100% | |
| Discharge valve (assembly) | 100% | |
| Valve plate | **400%** | |
| Valve spring | **400%** | |
| Cross pin | 100% | |
| Cross head pin metal | 100% | |
| Piston ring (รวม tension ring) | 100% | |
| Rod packing element ทุก stage | 200% | |
| Main bearings | 1 set (2 pcs.) | |
| Rider ring | 200% | non-lube compressor |
| Crank pin bearings | 1 set (2 pcs.) | |
| Cross head bearings | 1 set (2 pcs.) | |
| Cross head pin | 1 pc. | |
| Cross head shoe | 1 set (2 pcs.) | |
| Special gasket, O-rings | 200% | |
| Packing case | 100% | |
| Valve cover gasket | **400%** | |
| Valve seat or guard gasket | **400%** | OCR พิมพ์ "valve seal" |
| Oil wiper packing element | 50% | |
| Big end bolt | 50% (min.4) | |

**3.4.2 Compressor driver** (SPO p.53): motor bearing 100%; speed changer (ถ้ามี) gear unit bearing 100%, gasket & O-rings 200%, shaft seal parts 100%; V-belts 200%

ข้อสังเกต: ชิ้นส่วนวาล์วได้ % สูงสุดในบท (400%) ส่วนชิ้นใหญ่ของ running gear (main/crank pin/crosshead bearings, shoe) สำรองเป็น "1 set" ต่อเครื่อง ไม่ใช่ %

Blower (3.5): bearing และ labyrinth 100%, seal packing และ gasket 200%, coupling "1%" ต่อขนาด (SPO p.53)

## เชื่อมโยงกับ compressor failure hierarchy

ส่วนนี้เป็น **การตีความของ wiki** หนังสือ SPO ไม่ได้ใช้รหัส OREDA/ISO การจับคู่ใช้รหัส item ของ dataset ตาม [[Maintainable Item]] และ [[Compressor Subdivision Wiki vs ISO 14224]] [confidence:: low]

| อะไหล่ SPO | Maintainable item (wiki) | Sub unit |
|---|---|---|
| Suction/discharge valve, valve plate, valve spring, valve cover/seat gasket (recip) | CPUN-VALV | [[CPUN Compressor Unit]] |
| Piston ring, rider ring (recip) | CPUN-PSTN (สึกคู่กับ CPUN-CYLN) | [[CPUN Compressor Unit]] |
| Rod packing element, packing case, oil wiper packing (recip) | CPUN-PACK | [[CPUN Compressor Unit]] |
| Bearing liner/pad (centrifugal) | CPUN-RBRG | [[CPUN Compressor Unit]] |
| Thrust bearing pad (centrifugal) | CPUN-THRB | [[CPUN Compressor Unit]] |
| Labyrinth for balance piston | CPUN-INSS (ISO มี Balance piston แยก) | [[CPUN Compressor Unit]] |
| Seal parts contact / restrictive type, shaft sleeve | CPUN-SHSL | [[CPUN Compressor Unit]] |
| Seal parts liquid film type, seal oil bladder/seal ring | SHSS-SOIL | [[SHSS Shaft Seal System]] |
| Lube & seal oil filter cartridge | LUBS-FILT, SHSS-FILT | [[LUBS Lubrication System]], [[SHSS Shaft Seal System]] |
| Coupling, set screw for coupling | PWTR-CPDR, PWTR-CPDN | [[PWTR Power Transmission]] |
| Speed changer gear unit bearing/seal | PWTR-GBVD | [[PWTR Power Transmission]] |
| Main/crank pin bearings (recip) | ไม่ชัดเจน: PWTR-BRNG หรือ CPUN-RBRG | - |
| Crosshead pin/shoe/bearings, big end bolt (recip) | ไม่มี item ตรงใน dataset/ISO Table A.9 | - |
| Motor bearing, turbine driver parts | นอก boundary ของ compressor ตาม ISO (driver เป็น inventory แยก) | - |

### เทียบกับ item เด่นใน OREDA (การตีความ)

- **Reciprocating**: OREDA item เด่นคือ Cylinder liner 28.77%, Filter(s) 14.80%, Valves 10.94% ของ failure rate เฉพาะ reciprocating (ดู [[Reciprocating Compressor]])
  - Valves สอดคล้องกับ % สำรองสูงสุดของ SPO (valve plate/spring/gaskets 400%)
  - Cylinder liner ไม่อยู่ในรายการอะไหล่ SPO เลย มีแต่ชิ้นสึกที่ทำงานกับ liner (piston ring 100%, rider ring 200%) ข้อนี้อาจเป็นช่องว่างที่ควรตรวจเมื่อตั้งสต็อกจริง
  - Filter(s) ส่วนใหญ่เป็นโหมด SER (14.25%) แต่ตาราง reciprocating ของ SPO ไม่มี filter (filter cartridge 200% อยู่ใน auxiliary ของ centrifugal เท่านั้น)
- **Centrifugal**: OREDA เด่นที่ Instruments รวม 31.87% (derived) และโหมด [[AIR Abnormal Instrument Reading]] 27.52%, [[ELU External Leakage Utility Medium]] 17.54% (ดู [[Centrifugal Compressor]])
  - ตาราง compressor ของ SPO ไม่มี instrument (ครอบคลุมด้วยกฎ instrument 10% min 1 ในตัวอย่างอเมริกัน)
  - Seal O-rings/springs 200% และ gasket 200% สอดคล้องกับโหมด leakage ที่สูง
  - Valves 10.43% และ Antisurge 5.11% ไม่มีในตาราง SPO

## เทียบกับวิธี RBMM

BP ของ SPO เป็นวิธีกำหนด **อะไหล่โครงการ/อะไหล่เริ่มต้น** (startup + 1 ปี) จากตารางสัดส่วนตามประสบการณ์ ไม่ใช้ข้อมูล failure หรือความเสี่ยงของแต่ละรายการ ขณะที่ RBMM ตั้งระดับสต็อกตามความเสี่ยงและ cost ratio ([[Spare Part Criticality and Risk]]) และเตือนว่าอะไหล่ที่มากับโครงการ (commissioning spare) อาจเกินจำเป็น 2-3 เท่า ([[Spare Parts Management]]) สองแนวทางใช้ต่อกันได้: BP เป็นจุดเริ่ม แล้วทบทวนด้วยสถิติหลัง 2-3 ปีตามที่ SPO แนะนำ รายละเอียดดู [[SPO vs RBMM Spare Parts Approaches]]

## ข้อผิดพลาด/ความไม่แน่นอนใน source

- Coupling ใน centrifugal compressor และ blower พิมพ์ "1%" น่าจะหมายถึง 1 ชุดต่อชนิด/ขนาด (เทียบ centrifugal pump ที่ระบุ "1 for each size") (SPO p.51, p.53)
- Accumulator bladder และ transfer barrier bladder: ค่า 50% อยู่ในคอลัมน์ Remarks ใน OCR (เลื่อนคอลัมน์); seal oil system ใช้ข้อ (b) ซ้ำ (SPO p.52)
- "Valve seal or guard gasket" น่าจะเป็น "valve seat or guard gasket" (SPO p.53)
- แถว Oiler ของ centrifugal pump OCR เพี้ยน; ค่า 20% (min.1) ต่อ vendor ยังไม่แน่ชัด (SPO p.48)
- Table 2 แถว spring housing gasket: 6 เครื่อง = 2 แต่ 7 เครื่องขึ้นไป = 20% (7 x 20% = 1.4) ไม่ต่อเนื่องแบบแถวอื่น (derived check)
- Electrical "Motors, Recording" น่าจะพิมพ์/OCR ผิด; Table 2 พิมพ์ "Air-Pin Coolers"; "Hub assembly with blades" อ้าง note (2) ที่ไม่มี (SPO p.42, p.45)
- ตัวอย่างญี่ปุ่นไม่ระบุฐานของ %

## ดูเพิ่ม

- [[Spare Parts Optimization Book]]
- [[Spare Parts Management]]
- [[Spare Part Criticality and Risk]]
- [[SPO vs RBMM Spare Parts Approaches]]
- [[Parts Interchangeability]]
- [[MRO Inventory Control Methods]]
- [[Compressor]]

## Triplets

- [[Spare Parts Recommendation by Equipment Type]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 5 Engineering Basic Practice (SPO p.39-58)
- [[Spare Parts Recommendation by Equipment Type]] [produces:: Minimum Spare Parts Requirements] not a guarantee of every part at all times (SPO p.40)
- [[Spare Parts Recommendation by Equipment Type]] [applies_to:: Startup And First Year Operation] American example time basis (SPO p.40-41)
- [[Spare Parts Recommendation by Equipment Type]] [depends_on:: Wear And Corrosion Prone Parts] factor 1 of 5 (SPO p.40)
- [[Spare Parts Recommendation by Equipment Type]] [depends_on:: Environment] factor 2 of 5, e.g. near sea (SPO p.40)
- [[Spare Parts Recommendation by Equipment Type]] [depends_on:: Service Conditions] factor 3 of 5 (SPO p.40)
- [[Spare Parts Recommendation by Equipment Type]] [depends_on:: Lead Time] factor 4 of 5, procurement difficulty (SPO p.40)
- [[Spare Parts Recommendation by Equipment Type]] [depends_on:: [[Parts Interchangeability]]] factor 5 of 5 (SPO p.40)
- [[Spare Parts Recommendation by Equipment Type]] [has_value:: 2-3 years] review after actual operation (SPO p.57)
- [[Spare Parts Recommendation by Equipment Type]] [differs_from:: [[Spare Part Criticality and Risk]]] SPO uses experience-based ratio tables for initial spares; RBMM sets levels by risk and cost ratio; see [[SPO vs RBMM Spare Parts Approaches]]
- [[Spare Parts Recommendation by Equipment Type]] [related_to:: [[Spare Parts Management]]]
- Centrifugal Pump Spares Table 1 [has_value:: 30% of pumps] shaft, impeller, throat bushing, 7 or more pumps (SPO p.42)
- Centrifugal Pump Spares Table 1 [has_value:: 50% of pumps] shaft sleeve, bearing set, wearing rings, 7 or more pumps (SPO p.42)
- Centrifugal Pump Spares Table 1 [has_value:: 130% of pumps] gaskets, packing, seal non-metallic faces, O-rings, 7 or more pumps (SPO p.42)
- Centrifugal Pump Spares Table 1 [has_value:: 65% of pumps] mech. seal metallic faces and springs, 7 or more pumps (SPO p.42)
- Instrument Spares [has_value:: 10% minimum 1] per size/rating, American example (SPO p.43)
- Heat Exchanger Tubes [has_value:: retube largest bundle] per tube size, American example (SPO p.43)
- Pressure Vessel Gaskets [has_value:: 300%] Japanese example (SPO p.46)
- Pressure Vessel Bolts And Nuts [has_value:: 5%] Japanese example (SPO p.46)
- [[Centrifugal Compressor]] [has_part:: Labyrinth For Balance Piston] spare 100% (SPO p.50)
- Thrust Bearing Pad [has_value:: 100%] complete set, centrifugal compressor (SPO p.50)
- Bearing Liner Or Pad [has_value:: 100%] centrifugal compressor (SPO p.50)
- Compressor Seal O-rings [has_value:: 200%] contact and liquid film type seals, centrifugal compressor (SPO p.50-51)
- Compressor Coupling [has_value:: 1 set] printed 1%, likely 1 set per type (SPO p.51) [confidence:: low]
- Lube And Seal Oil Filter Cartridge [has_value:: 200%] centrifugal compressor auxiliary (SPO p.52)
- Accumulator Bladder [has_value:: 50%] value in Remarks column in OCR (SPO p.52)
- Valve Plate [has_value:: 400%] reciprocating compressor (SPO p.52)
- Valve Spring [has_value:: 400%] reciprocating compressor (SPO p.52)
- Valve Cover Gasket [has_value:: 400%] reciprocating compressor (SPO p.53)
- Rod Packing Element [has_value:: 200%] each stage, reciprocating compressor (SPO p.52)
- Rider Ring [has_value:: 200%] non-lube reciprocating compressor (SPO p.52)
- Piston Ring [has_value:: 100%] incl. tension ring, reciprocating compressor (SPO p.52)
- Main Bearings [has_value:: 1 set (2 pcs.)] reciprocating compressor (SPO p.52)
- Big End Bolt [has_value:: 50% minimum 4] reciprocating compressor (SPO p.53)
- Valve Plate [part_of:: CPUN-VALV] wiki interpretation [confidence:: low]
- Valve Spring [part_of:: CPUN-VALV] wiki interpretation [confidence:: low]
- Piston Ring [part_of:: CPUN-PSTN] wiki interpretation [confidence:: low]
- Rider Ring [part_of:: CPUN-PSTN] wiki interpretation [confidence:: low]
- Rod Packing Element [part_of:: CPUN-PACK] wiki interpretation [confidence:: low]
- Thrust Bearing Pad [part_of:: CPUN-THRB] wiki interpretation [confidence:: low]
- Bearing Liner Or Pad [part_of:: CPUN-RBRG] wiki interpretation [confidence:: low]
- Labyrinth For Balance Piston [part_of:: CPUN-INSS] wiki interpretation; ISO lists Balance piston separately [confidence:: low]
- Compressor Seal O-rings [part_of:: CPUN-SHSL] contact and restrictive type, wiki interpretation [confidence:: low]
- Lube And Seal Oil Filter Cartridge [part_of:: LUBS-FILT] also SHSS-FILT, wiki interpretation [confidence:: low]
- Accumulator Bladder [part_of:: [[SHSS Shaft Seal System]]] seal oil system, wiki interpretation [confidence:: low]
- Compressor Coupling [part_of:: PWTR-CPDR] also PWTR-CPDN, wiki interpretation [confidence:: low]
- VALV [related_to:: Valve Plate] OREDA Valves 10.94% in reciprocating aligns with highest SPO spare ratio 400%, wiki interpretation [confidence:: low]
- CYLN [related_to:: [[Spare Parts Recommendation by Equipment Type]]] Cylinder liner 28.77% in reciprocating but not in SPO spare list, wiki interpretation [confidence:: low]

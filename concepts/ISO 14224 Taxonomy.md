---
title: ISO 14224 Taxonomy
created: 2026-10-21
updated: 2026-10-22
type: concept
tags: [iso-14224, taxonomy, coding, sub-unit, maintainable-item]
sources: [iso-14224.md]
confidence: high
contested: false
---

# ISO 14224 Taxonomy

taxonomy ของ [[ISO 14224]] คือการจัดกลุ่ม item อย่างเป็นระบบตามปัจจัยร่วม (ตำแหน่งใช้งาน, การใช้งาน, การแบ่งย่อยอุปกรณ์) มี **9 ระดับ** แบ่งเป็น 2 กลุ่มหลัก (ISO 14224 cl. 8.2, Figure 3, Table 2, p.30-31) หน้านี้สรุปโครงสร้างและเทียบกับ 7 ระดับของ [[Failure Hierarchy]] ที่ใช้ใน wiki

## 9 ระดับ

| Level | ชื่อ | กลุ่มหลัก | ตัวอย่าง |
|---|---|---|---|
| 1 | Industry | Use/location data | petroleum, natural gas, petrochemical |
| 2 | Business category | Use/location data | upstream, midstream, downstream, petrochemical |
| 3 | Installation category | Use/location data | oil/gas production, drilling, LNG, refinery (Table A.1) |
| 4 | Plant/Unit category | Use/location data | platform, semi-submersible, hydrocracker (Table A.2) |
| 5 | Section/System | Use/location data | compression, tanker loading (Table A.3, รหัส S1-S97) |
| 6 | Equipment class/unit | Equipment subdivision | compressors, pumps, gas turbines (Table A.4) |
| 7 | Subunit | Equipment subdivision | lubrication system, control and monitoring |
| 8 | Component/Maintainable item (MI) | Equipment subdivision | cooler, coupling, valve, sensor |
| 9 | Part | Equipment subdivision | seal, impeller, gasket, bolt |

- Level 1-5 คือ operating context ต้องเก็บเป็น use/location data ของทุก equipment unit เพราะอุปกรณ์ชนิดเดียวกันใช้ได้หลายบริบท (ISO 14224 cl. 8.2, p.31)
- Level 6-9 เป็น inventory แบบ parent-child; level 9 เป็น optional และมาตรฐานไม่ลงรายละเอียด; บาง class ไม่มี MI (เช่น piping ลงถึง part) (Table 2 note, p.31)
- ISO 14224 เรียก level 6-9 รวมกันว่า **item** (cl. 3.43, p.9) และนิยาม maintainable item ว่าเป็นระดับต่ำสุดในลำดับชั้นเมื่อทำ maintenance (cl. 3.48, p.10)
- จำนวนระดับที่ลงไปขึ้นกับความซับซ้อนและการใช้ข้อมูล: availability analysis อาจพอที่ level 6 ส่วน RCM หรือ root cause ต้องการ mechanism ที่ระดับ MI/part (cl. 8.2, p.31)
- ข้อสังเกต: เอกสาร ISO ขัดกันเองเล็กน้อยว่า Table 3 ครอบคลุม level 3-5 หรือ 4-5 (cl. 3.28 note 1 กับ note 2, p.6) ไม่กระทบการใช้งานหน้านี้

## ข้อมูล failure/maintenance ผูกกับระดับใด (Table 3, p.32)

ค่า default และทางเลือกในวงเล็บ

| ข้อมูล | Default level | ทางเลือก |
|---|---|---|
| Impact of failure/maintenance on safety | 4 Plant/Unit | - |
| Impact on operations | 4 | 5 |
| Failure impact on equipment | 6 | 7, 8 |
| Failure mode | 6 | 5, 7, 8 |
| Failure mechanism | 8 | 6, 7 |
| Failure cause | 8 | 7 |
| Detection method | 6 | 5, 7, 8 |
| Subunit failed / MI failed | 7 / 8 | - |
| Down time | 6 | 4, 5 |
| Active maintenance time | 6 | 7, 8 |

กฎสำคัญ: failure mode ผูกกับ equipment unit (level 6) ส่วน failure mechanism ผูกกับระดับต่ำสุดที่ทำได้ (cl. 8.2, p.31) ดูนิยามเพิ่มที่ [[Failure Mode]], [[Failure Mechanism]], [[Failure Detection Method]], [[Failure Impact Classification]] และเวลาที่ [[Maintenance Time Definitions]]

item เดียวกันอยู่ได้หลายระดับ เช่น valve/pump เป็น equipment class แต่เป็น MI ภายใน gas turbine ได้ valve subsea มักเป็น MI แต่ topside เป็น equipment unit จึงต้องระวังนับ failure ซ้ำ (cl. 8.2, p.32)

## Boundary (cl. 8.1, p.29-30)

- ต้องกำหนด boundary ให้ทุก equipment class มิฉะนั้นข้อมูลจากหลายแหล่งรวมกันไม่ได้ รูปแบบคือ boundary diagram, ข้อความ หรือทั้งสองอย่าง (p.29)
- ตัวอย่างปั๊ม: valve ขาเข้า/ขาออกและ suction strainer อยู่นอก boundary; driver และ auxiliary ของ driver อยู่นอก ให้บันทึก driver เป็น inventory แยก แล้วโยงด้วยเลขอ้างอิง failure ของ driver ลงที่ driver (p.29)
- Instrument: ระบบควบคุม/monitoring ส่วนกลางอยู่ใน subunit control and monitoring ส่วน instrument เฉพาะจุดอยู่ใน subunit ที่มันทำงานอยู่ เช่น lubrication system (p.29)
- ใช้ boundary ต่างจากมาตรฐานได้ แต่ต้องระบุ deviation; ห้าม boundary ซ้อนกันระหว่าง class (เช่น อย่านับ instrument เป็น equipment unit แยกถ้าอยู่ใน boundary ของอุปกรณ์อื่นแล้ว) (p.29-30)
- กฎทั่วไปใน Annex A (cl. A.1.2, p.46-47): ใส่เฉพาะ item ทั่วไปของ class; failure ที่ connection ที่โยงกับ item ต่อเชื่อมไม่ได้ให้นับในขอบเขต; subunit ที่ driver กับ driven unit ใช้ร่วมกันให้บันทึกกับ driven unit; ไม่รวมระบบกลางอย่าง SCADA

## Equipment class และรหัส (Table A.4, level 6, p.52-60)

Annex A เป็น informative (cl. A.1.1, p.46) Table A.4 จัด class ตามหลักการทำงานปนกับกลุ่มการใช้งาน (p.48) รหัสเป็น 2 ตัวอักษร (บาง class 3 ตัว เช่น ESP)

| Category | Class (รหัส) |
|---|---|
| Rotating | BL blowers/fans, CF centrifuges, CE combustion engines, **CO compressors**, EG electric generators, EM electric motors, GT gas turbines, LE liquid expanders, MI mixers, PU pumps, ST steam turbines, TE turboexpanders |
| Mechanical | CV conveyors, CR cranes, FS filters/strainers, HE heat exchangers, HB heaters/boilers, LA loading arms, PL onshore pipelines, PI piping, VE pressure vessels, SI silos, SE steam ejectors, TA storage tanks, SW swivels, TU turrets, WI winches |
| Electrical | FC frequency converters, PC power cables, PT power transformers, SG switchgear, UP UPS |
| Safety and control | CL control logic units, EC emergency communication, ER escape/rescue, FG fire and gas detectors, FF fire-fighting, FI flare ignition, IG inert gas, IP input devices, LB lifeboats, NO nozzles, TC telecommunications, VA valves |
| Subsea | DT, PR risers, SC subsea compressors, SD, EP, FL, SH, CI, MA, SL, CA, SV, CS, SP subsea pumps, TM, XT |
| Well completion | SS, WE, ESP, XD |
| Drilling | CG, DC, TB, DE, DI, DW, DD, DS, DM, DH, DR, MC, BO, BT, TD |
| Well intervention | W1, W2, W3, WC, OI |
| Marine | AM, IC, DP, HT, JF, MD, TH, TO |
| Utilities | AI, SU, FE, HC, HP, NI, OC (ไม่มีตัวอย่าง taxonomy ใน Annex A) |
| Auxiliaries | HV HVAC (ไม่มีตัวอย่าง) |

- class **CO Compressors** มีตัวอย่างเต็มใน Annex A.2.2.2 (type code CE/RE/SC/AX และ subdivision 6 subunit) ดู [[Compressor Subdivision Wiki vs ISO 14224]]
- รหัส class CE (Combustion engines) ซ้ำกับรหัส type CE (Centrifugal) ของ compressor แต่เป็นคนละระดับ (Table A.8, p.64)
- Table A.4 ระบุ standard อ้างอิงต่อ class เช่น compressor อ้าง ISO 10439, ISO 13631, ISO 13707, ISO 10442, API 617/618/619 (p.52)
- แต่ละ class ที่มีตัวอย่างประกอบด้วย type classification, boundary drawing, subdivision table (subunit -> MI) และ equipment-specific data (Table A.10 สำหรับ compressor) (cl. A.2.1, p.61)
- ผู้ใช้ควรสร้าง taxonomy ของ class ใหม่เองตามหลักเดียวกันเมื่อ class ไม่อยู่ในรายการ (cl. 5.1, p.20)

## เทียบกับ 7 ระดับของ wiki

| wiki level | ชื่อใน wiki | ISO 14224 |
|---|---|---|
| 1 | Equipment | level 6 equipment unit (CO) |
| 2 | Sub Unit | level 7 subunit |
| 3 | Maintainable Item | level 8 component/MI |
| 4 | Failure Mode | ไม่ใช่ taxonomy level: เป็นข้อมูลของ failure record ผูกที่ level 6 (ทางเลือก 7, 8) |
| 5 | Failure Mechanism | ข้อมูลของ failure record ผูกที่ level 8 (Table 3) |
| 6 | Failure Cause | ข้อมูลของ failure record ผูกที่ level 8 |
| 7 | Resolution | ไม่มีใน ISO taxonomy; ISO เก็บเป็น maintenance activity ใน maintenance record (Table 8, p.44) |

ข้อสังเกต
- เลข 1-7 ของ wiki เป็นการนับภายใน dataset ไม่ใช่ระดับของ ISO ใน ISO ระดับ 1-5 อยู่เหนือ equipment unit (อุตสาหกรรมถึง section/system) ซึ่ง wiki ไม่ได้เก็บ
- wiki ผูก failure mode เข้ากับคู่ item (mode x maintainable item) ละเอียดกว่า default ของ ISO ที่ผูก mode กับ level 6 แต่ ISO อนุญาต level 7-8 เป็นทางเลือก (Table 3) จึงไม่ขัดกัน
- wiki วาง mechanism/cause ต่อ item สอดคล้องกับ default level 8 ของ ISO (Table 3)
- รหัส 4 ตัวอักษรของ subunit/item (PWTR, CPUN, GBVD ฯลฯ) ไม่ใช่รหัสของ ISO 14224 (มาตรฐานใช้ชื่อเต็ม) ดู [[Compressor Subdivision Wiki vs ISO 14224]] และ [[Maintainable Item]]

## ดูเพิ่ม

- [[ISO 14224]]
- [[Failure Hierarchy]]
- [[Compressor]]
- [[Maintainable Item]]
- [[Failure Data Recording]]
- [[RM Data Quality]]

## Triplets

- [[ISO 14224 Taxonomy]] [part_of:: [[ISO 14224]]]
- [[ISO 14224 Taxonomy]] [has_value:: 9] levels in 2 main groups (cl. 8.2, Figure 3, Table 2, p.30-31)
- Industry [at_level:: 1] Use/location data
- Business Category [at_level:: 2] Use/location data
- Installation Category [at_level:: 3] Use/location data (Table A.1)
- Plant/Unit Category [at_level:: 4] Use/location data (Table A.2)
- Section/System [at_level:: 5] Use/location data (Table A.3, S1-S97)
- Equipment Class/Unit [at_level:: 6] Equipment subdivision (Table A.4)
- Subunit [at_level:: 7] Equipment subdivision
- [[Maintainable Item]] [at_level:: 8] Component/Maintainable item, equipment subdivision
- Part [at_level:: 9] Equipment subdivision, optional (Table 2 note, p.31)
- Industry [has_category:: Use/location data]
- Business Category [has_category:: Use/location data]
- Installation Category [has_category:: Use/location data]
- Plant/Unit Category [has_category:: Use/location data]
- Section/System [has_category:: Use/location data]
- Equipment Class/Unit [has_category:: Equipment subdivision]
- Subunit [has_category:: Equipment subdivision]
- [[Maintainable Item]] [has_category:: Equipment subdivision]
- Part [has_category:: Equipment subdivision]
- Equipment Class/Unit [has_part:: Subunit] parent-child inventory, levels 6-9
- Subunit [has_part:: [[Maintainable Item]]]
- [[Maintainable Item]] [has_part:: Part]
- Item [defined_in:: [[ISO 14224]]] levels 6-9 together (cl. 3.43, p.9)
- [[Maintainable Item]] [defined_in:: [[ISO 14224]]] lowest level in hierarchy when doing maintenance (cl. 3.48, p.10)
- Impact On Safety [at_level:: 4] default (Table 3, p.32)
- Impact On Operations [at_level:: 4] default; option 5 (Table 3)
- Failure Impact On Equipment [at_level:: 6] default; options 7, 8 (Table 3)
- [[Failure Mode]] [at_level:: 6] default; options 5, 7, 8 (Table 3)
- [[Failure Mechanism]] [at_level:: 8] default; options 6, 7 (Table 3)
- Failure Cause [at_level:: 8] default; option 7 (Table 3)
- [[Failure Detection Method]] [at_level:: 6] default; options 5, 7, 8 (Table 3)
- Down Time [at_level:: 6] default; options 4, 5 (Table 3)
- Active Maintenance Time [at_level:: 6] default; options 7, 8 (Table 3)
- ISO 14224 cl. 3.28 Note 1 [contradicts:: ISO 14224 cl. 3.28 Note 2] Table 3 covers levels 3-5 vs 4-5 (p.6); minor
- Boundary [applies_to:: Equipment Class/Unit] must be defined for every class (cl. 8.1, p.29)
- Driver [related_to:: Boundary] outside pump boundary, recorded as separate inventory (cl. 8.1, p.29)
- [[Compressor]] [has_code:: ISO:A.4-CO] Compressors, Rotating category (Table A.4, p.52-60)
- ISO:A.4-CO [has_label:: Compressors]
- ISO:A.4-CO [has_category:: Rotating] (Table A.4)
- ISO:A.4-CO [has_part:: ISO:A.8-CE] type code CE/RE/SC/AX (Annex A.2.2.2)
- ISO:A.4-CO [has_part:: ISO:A.8-RE] compressor type code
- ISO:A.4-CO [has_part:: ISO:A.8-SC] compressor type code
- ISO:A.4-CO [has_part:: ISO:A.8-AX] compressor type code
- ISO:A.4-CO [has_value:: 6] subunits (Annex A.2.2.2), see [[Compressor Subdivision Wiki vs ISO 14224]]
- ISO:A.4-CE [has_label:: Combustion engines]
- ISO:A.4-CE [differs_from:: ISO:A.8-CE] class CE vs compressor type CE (Centrifugal), different level (Table A.8, p.64)
- ISO:A.4-CO [defined_in:: ISO 10439] reference standards also ISO 13631, ISO 13707, ISO 10442, API 617/618/619 (Table A.4, p.52)
- [[ISO 14224 Taxonomy]] [differs_from:: [[Failure Hierarchy]]] 9 ISO levels vs 7 wiki levels; wiki 1-7 is dataset numbering
- [[Compressor]] [at_level:: 6] ISO equipment unit CO; wiki [[Failure Hierarchy]] level 1 Equipment
- Subunit [maps_to:: [[Failure Hierarchy]]] ISO level 7 = wiki level 2 Sub Unit
- [[Maintainable Item]] [at_level:: 3] wiki [[Failure Hierarchy]] level; ISO level 8
- [[Failure Mode]] [differs_from:: [[ISO 14224 Taxonomy]]] wiki level 4; ISO: failure record data, not a taxonomy level
- [[Failure Mechanism]] [differs_from:: [[ISO 14224 Taxonomy]]] wiki level 5; ISO: failure record data at level 8
- [[Resolution Codes]] [differs_from:: [[ISO 14224 Taxonomy]]] wiki level 7; not in ISO taxonomy, maintenance activity in maintenance record (Table 8, p.44)
- [[Failure Mode]] [at_level:: 8] wiki binds mode to mode x item pair; ISO option 7-8 allowed (Table 3), no conflict
- [[PWTR Power Transmission]] [differs_from:: [[ISO 14224]]] dataset 4-letter subunit/item codes (PWTR, CPUN, GBVD) are not ISO codes

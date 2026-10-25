---
title: Lubrication and Oil Analysis
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [cmrp, lubrication, cbm, maintenance-reliability]
sources: [cmrp.md, compressor-failure-hierarchy.md]
confidence: medium
contested: false
---

# Lubrication and Oil Analysis

การหล่อลื่น (lubrication) ลดแรงเสียดทานและการสึกโดยใส่ชั้นวัสดุคั่นระหว่างผิวที่เคลื่อนที่สัมพัทธ์ ส่วน oil analysis คือการตรวจน้ำมัน/จาระบีเพื่อดูทั้ง **สภาพสารหล่อลื่น** (degradation) และ **สภาพเครื่อง** (wear particle, contamination) เป็นหนึ่งในเทคนิคหลักของ [[Condition Monitoring Techniques]] และเป็น "boundary" ที่ 3 Fluid Quality and Level ของการตรวจเครื่อง (CMRP CMPR-01 p.6, p.12, p.49) สาระหลักจาก [[CMRP Course]]

## หลักการหล่อลื่น (CMRP CMPR-01 p.12-15)

- สารหล่อลื่นเป็นได้ 4 สถานะ: liquid (oil), semi-solid (grease), solid (graphite), gas (air, helium)
- ฟิล์มหนาราว 0.1-30 µm แยก asperity ของสองผิว ให้ shear ไปเกิดในฟิล์มแทนผิวโลหะ แรงเสียดทานในฟิล์มขึ้นกับ viscosity
- Viscosity = ความต้านทานการไหล (dynamic viscosity = shear stress / shear rate) ลดลงเมื่ออุณหภูมิสูงขึ้น วัดที่ 40 และ 100 °C
- หน้าที่อื่นนอกจากลด friction/wear: ระบายความร้อน, กันสนิม, คุมสิ่งปนเปื้อน, ส่งกำลังไฮดรอลิก

## องค์ประกอบ

| ส่วน | สัดส่วนตาม slide | หมายเหตุ |
|---|---|---|
| Base oil | 70-95% | |
| Additives | 5-30% | antioxidant, rust inhibitor, EP/AW ฯลฯ |
| Thickener (เฉพาะ grease) | 5-30% | เปรียบเป็นฟองน้ำอุ้มน้ำมัน |

(CMRP CMPR-01 p.15; CMPR-02 p.13) ช่วงเหล่านี้ซ้อนกันและรวมกันไม่สอดคล้อง (ถ้า base oil 95% จะไม่พอให้ thickener 5% + additive 5%) และ additive 5-30% ในจาระบีสูงกว่าที่พบทั่วไป (มักไม่เกินราว 10%; general knowledge, confidence low) ใช้เป็นช่วงคร่าว ๆ เท่านั้น

## API base oil groups I-V (CMRP CMPR-01 p.50; CMPR-02 p.8-9)

| Group | Saturates | Sulfur | VI | กระบวนการ/ชนิด |
|---|---|---|---|---|
| I | < 90% และ/หรือ | > 0.03% | 80-119 | solvent refined mineral มีโมเลกุลหลากหลาย เหลือ sulfur/wax/aromatics |
| II | ≥ 90% | ≤ 0.03% | 80-119 | hydroprocessed โมเลกุลสม่ำเสมอขึ้น |
| III | ≥ 90% | ≤ 0.03% | ≥ 120 | hydrocracked/ปรับรูปโมเลกุล เรียกกึ่ง synthetic |
| IV | - | - | - | PAO (synthetic) |
| V | - | - | - | synthetic อื่น (ester, PAG, silicone ฯลฯ) |

- slide เขียนขอบเขตเป็น ">90%" และ ">120" ซึ่งทิ้งค่าขอบไว้ นิยาม API ใช้ ≥ (general knowledge) ตารางข้างบนใช้ ≥ ตาม API
- ส่วนแบ่งตลาดตาม slide: mineral 90%, synthetic 9%, vegetable 1% (CMRP CMPR-01 p.50)
- เทียบชนิด (CMRP CMPR-02 p.10): mineral oil เด่นด้านราคาและ additive solubility แต่แคบด้านช่วง viscosity/อุณหภูมิ; PAO เด่นเกือบทุกด้านยกเว้น additive solubility/biodegradability; ester อ่อนด้าน hydrolytic stability; กลุ่มพิเศษ (phosphate ester, PAG, silicone, fluorocarbon) ราคาสูง

## Additives (CMRP CMPR-02 p.10-11)

- Mineral oil ไม่มีขั้ว จึงพึ่ง additive มีขั้ว 3 กลไก: particle enveloping (detergent, dispersant, metal deactivator), metal wetting (rust/corrosion inhibitor, AW, EP), water emulsifying
- แบ่งตามจุดทำงาน: **surface active** (AW, EP, friction modifier, tackifier, R&O, metal deactivator) และ **bulk oil active** (anti-oxidant, dispersant, detergent, foam inhibitor, demulsifier, VI improver, pour point depressant, biocide)
- additive depletion เป็นหนึ่งใน 4 มุมมองของ oil analysis (viscosity, inclusions, contamination, additive depletion) (CMRP CMPR-02 p.8)

## Contamination และ varnish (CMRP CMPR-01 p.16-17)

- ชนิดอนุภาค: silica (ฝุ่นจากภายนอก), bright metal (wear ภายใน เร่งการสึกต่อ), black metal (ferrous oxide), rust (มีน้ำในระบบ), fibers, cake of fines (silt หนาแน่นจนประเมินไม่ได้)
- ภาพ wear particle ที่บอก mechanism: fatigue spall, sliding wear, cutting wear, sand/silica, iron oxide (CMRP CMPR-02 p.11) ดู [[Wear Mechanisms]]
- **Varnish**: คราบบางแข็งไม่ละลายในน้ำมัน (lacquer, sludge) กลไก 4 ขั้น oxidation -> polymerisation -> agglomeration -> precipitation เกาะที่จุดเย็น ไหลช้า clearance ต่ำ

## การทดสอบในห้องแล็บ

| ประเภท | ให้ข้อมูล |
|---|---|
| Wear Particle Analysis | กลไกการสึก ขนาด/ความเข้มข้น ferrous ลักษณะอนุภาค |
| Particle Count | จำนวนต่อ 100 ml แยกช่วง 5-10, 10-25, 25-50, 50-100, > 100 µm |
| Spectrochemical & Physical | คุณภาพน้ำมัน, wear metal และ additive เป็น ppm |

(CMRP CMPR-01 p.18)

- น้ำมัน: viscosity, VI, specific/API gravity, flash/fire point, pour/cloud point, oxidation stability, foam/air release, AN/BN, filterability, AW/EP, demulsibility, rust และ copper corrosion (CMRP CMPR-01 p.18; CMPR-02 p.8, p.16)
- จาระบี: consistency/penetration (NLGI), dropping point, base oil viscosity, mechanical stability, water washout, corrosion (เช่น SKF EMCOR), copper corrosion, oil separation, oxidation, EP/AW, fretting, pumpability (CMRP CMPR-01 p.21; CMPR-02 p.12, p.16)

## Field tests (CMRP CMPR-01 p.19-24)

- Viscosity: viscometer แบบมือ/pocket comparator (แนะนำแบบ calibrate ที่ 40 °C) เทียบน้ำมันใหม่กับน้ำมันใช้งาน
- Patch test: ดูอนุภาค เส้นใย และ wear particle ขนาดใหญ่
- Crackle test: อุ่นตัวอย่างถึงราว 100 °C ถ้ามีเสียงปะทุแสดงว่ามีน้ำ; sedimentation: ตั้งทิ้ง 30 นาทีแล้วดูน้ำที่แยกชั้น
- Grease: bleed test (consistency) และ inclusions
- ชุดเครื่องมือ: grease test kit, patch/crackle kit, multimeter, IR thermometer, stroboscope

## การเก็บตัวอย่าง (CMRP CMPR-02 p.12)

- เก็บจากจุดที่ flow เป็น turbulent ผ่าน sampling valve บนสายที่ทำงาน อ้าง **ISO 4021:1992** (hydraulic fluid power, การดึงตัวอย่างของเหลวจากสายที่ทำงาน)
- เก็บจาก reservoir (ใช้ weighted plug) ได้แต่ต้องระวังเป็นพิเศษ เพราะตัวอย่างอาจไม่ตัวแทน
- ความถี่เก็บตัวอย่างบันทึกใน Asset Information Page ของเครื่อง (CMRP CMPR-01 p.24-27) ดู [[Condition Monitoring Techniques]]

## จาระบีและ NLGI grade (CMRP CMPR-02 p.13-15)

- จำแนกตามชนิด thickener: lithium, calcium, polyurea, PTFE; ส่วนแบ่งการใช้ lithium ราว 56%, calcium 24% (ข้อมูล NLGI ตาม slide)
- complex greases และ polyurea มี dropping point 260 °C ขึ้นไป ใช้งานได้ถึงราว 177 °C; calcium ธรรมดา dropping point ราว 96-104 °C
- NLGI grade วัดด้วย cone penetration ASTM D217 (หน่วย 0.1 mm) ยิ่งเลขสูงยิ่งแข็ง งาน bearing ส่วนใหญ่ใช้ราว grade 1-3

| NLGI | Penetration (0.1 mm) |
|---|---|
| 000 | 445-475 |
| 00 | 400-430 |
| 0 | 355-385 |
| 1 | 310-340 |
| 2 | 265-295 |
| 3 | 220-250 |
| 4 | 175-205 |
| 5 | 130-160 |
| 6 | 85-115 |

## เชื่อมโยงกับ compressor failure hierarchy

การตีความของ wiki นี้ (ไม่ใช่ข้อมูลใน CMRP):
- [[LUBS Lubrication System]] มีคู่เด่น Filter(s) x SER (Blockage/plugged, high DP) และ Oil x INL (Contamination: process gas/water ingress) particle count, crackle/water test และ varnish monitoring เป็นวิธีจับอาการล่วงหน้าของสองคู่นี้
- Lube oil degradation และ additive depletion สัมพันธ์กับ mechanism `CTMN` และ `MATF` ของ item LUBE/OILS ใน LUBS
- wear metal ใน spectrochemical analysis ชี้กลับไป item ที่สึก (bearing ใน [[PWTR Power Transmission]], pump ใน LUBS) ช่วยให้ลงรหัส mechanism ได้แม่นขึ้นตาม [[Failure Mechanism]]

## ดูเพิ่ม

- [[Wear Mechanisms]]
- [[Condition Monitoring Techniques]]
- [[P-F Interval and Condition Monitoring]]
- [[LUBS Lubrication System]]

## Triplets

- [[Lubrication and Oil Analysis]] [is_a:: Condition Monitoring] oil analysis looks at lubricant degradation and contamination (CMRP CMPR-01 p.49)
- [[Lubrication and Oil Analysis]] [part_of:: [[Condition Monitoring Techniques]]]
- Lubricant [has_part:: Base Oil] 70-95% (CMRP CMPR-01 p.15)
- Lubricant [has_part:: Additives] 5-30% per slide, ranges inconsistent (CMRP CMPR-01 p.15)
- Grease [has_part:: Thickener] 5-30% (CMRP CMPR-02 p.13)
- Lubricant Film [has_value:: 0.1-30 µm] separates asperities (CMRP CMPR-01 p.12-14)
- Viscosity [has_formula:: shear stress / shear rate] dynamic viscosity; measured at 40 and 100 °C (CMRP CMPR-01 p.14)
- API Group I [has_value:: saturates < 90% and/or sulfur > 0.03%, VI 80-119] solvent refined (CMRP CMPR-01 p.50)
- API Group II [has_value:: saturates ≥ 90%, sulfur ≤ 0.03%, VI 80-119] hydroprocessed (CMRP CMPR-01 p.50)
- API Group III [has_value:: saturates ≥ 90%, sulfur ≤ 0.03%, VI ≥ 120] hydrocracked; slide writes > 120 and > 90% (CMRP CMPR-01 p.50)
- API Group IV [has_label:: PAO] (CMRP CMPR-01 p.50)
- API Group V [has_label:: Other Synthetics] (CMRP CMPR-01 p.50)
- Base Oil Market Share [has_value:: mineral 90%, synthetic 9%, vegetable 1%] per slide (CMRP CMPR-01 p.50)
- Additives [has_category:: Surface Active] AW, EP, friction modifier, tackifier, R&O, metal deactivator (CMRP CMPR-02 p.11)
- Additives [has_category:: Bulk Oil Active] anti-oxidant, dispersant, detergent, foam inhibitor, demulsifier, VI improver (CMRP CMPR-02 p.11)
- Varnish [has_cause:: Oxidation] then polymerisation, agglomeration, precipitation (CMRP CMPR-01 p.17)
- Wear Particle Analysis [produces:: Wear Mechanism Identification] ferrous size, concentration, morphology (CMRP CMPR-01 p.18)
- Particle Count [measures:: Particles Per 100 ml] size bands 5-10 to > 100 µm (CMRP CMPR-01 p.18)
- Spectrochemical Analysis [measures:: Wear Metals And Additives] ppm (CMRP CMPR-01 p.18)
- Water In Oil [detected_by:: Crackle Test] heat to about 100 °C, crackling = water (CMRP CMPR-01 p.19-24)
- Patch Test [measures:: Particles And Fibres] field test (CMRP CMPR-01 p.19-24)
- Oil Sampling [defined_in:: ISO 4021] 1992, sample from turbulent zone of working line (CMRP CMPR-02 p.12)
- NLGI Grade [uses:: ASTM D217] cone penetration, 0.1 mm (CMRP CMPR-02 p.14)
- NLGI Grade [has_value:: 000 = 445-475 to 6 = 85-115] higher grade = stiffer (CMRP CMPR-02 p.14)
- Lithium Grease [has_value:: 56%] share of use per NLGI on slide (CMRP CMPR-02 p.15)
- Calcium Grease [has_value:: 24%] share of use per NLGI on slide (CMRP CMPR-02 p.15)
- Polyurea Grease [has_value:: dropping point 260 °C+] max use about 177 °C (CMRP CMPR-02 p.15)
- [[Lubrication and Oil Analysis]] [related_to:: [[Wear Mechanisms]]] wear particle types reveal mechanism (CMRP CMPR-02 p.11)
- LUBS-FILT [detected_by:: Particle Count] interpretation [confidence:: low]
- LUBS-OILS [detected_by:: Crackle Test] water ingress for Oil x INL, interpretation [confidence:: low]
- [[Lubrication and Oil Analysis]] [applies_to:: [[LUBS Lubrication System]]] interpretation
- [[Lubrication and Oil Analysis]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-01 p.12-27, p.50; CMPR-02 p.8-16)

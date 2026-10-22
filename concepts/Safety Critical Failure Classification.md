---
title: Safety Critical Failure Classification
created: 2026-10-21
updated: 2026-10-22
type: concept
tags: [iso-14224, failure-mode, failure-rate, reliability, criticality]
sources: [iso-14224.md]
confidence: medium
contested: false
---

# Safety Critical Failure Classification (ISO 14224 Annex F)

Annex F (informative) ของ [[ISO 14224]] ให้วิธีจำแนกและนิยาม failure ของอุปกรณ์ safety (safety instrumented system, fire and gas, ESD valve ฯลฯ) อิง IEC 61508/61511 และ ISO/TR 12489:2013 (ISO 14224 cl. F.1-F.2, p.251) สรุปด้วยถ้อยคำของผู้เขียน wiki wiki ไม่มีข้อมูลเสียของ asset ที่เกี่ยวกับ safety system

## 1. ทำไมต้องแยกเป็นพิเศษ

SIS ส่วนใหญ่ "dormant" รอถูกเรียก จึงต้องหา hidden failure ให้เจอก่อนเกิด demand (ISO 14224 cl. F.3, p.252) ตรงกับหลักของ [[Failure Finding Interval]] แต่มาตรฐานผูกกับ IEC 61508/61511 โดยตรง ขณะที่หน้า [[Failure Finding Interval]] เดิมอิง RBMM ที่ไม่อ้าง IEC 61508

## 2. Random vs systematic และ DD/DU/SD/SU (ISO 14224 cl. F.3.1-F.3.2, p.252-253)

- ศัพท์: dangerous = ขัดขวาง safety action; safe = ส่งเสริม safety action (เช่น trip เอง); no-effect = ไม่กระทบ; immediately revealed vs hidden (hidden พบได้ด้วย periodic test)
- แยก random กับ systematic ก่อน (systematic = เกิดซ้ำภายใต้เงื่อนไขเฉพาะ, ISO 14224 cl. 3.79 และ 3.90, p.15 และ p.17) แล้วแบ่ง random เป็น 4 กลุ่ม

| รหัส | ความหมาย |
|---|---|
| DD | dangerous detected (พบด้วย diagnostics) |
| DU | dangerous undetected (พบด้วย periodic test หรือเมื่อ demand) |
| SD | safe detected |
| SU | safe undetected |

- ข้อมูลที่เก็บอาจไม่มีเหตุการณ์ครบ 4 กลุ่ม ต้องตั้งสมมติฐานอย่างระวังกับกลุ่ม zero failure และต้องเข้าใจพฤติกรรมทางกายภาพจึงจัด failure mode ลงกลุ่มถูก
- สองหัวข้อที่เน้นเมื่อเก็บข้อมูล SIS: **common cause failure (CCF)** และ **periodic test interval** สำหรับหา DU failure
- CCF บางส่วนเป็น systematic จึงไม่นับในกลุ่ม random ทั้ง 4 (ISO 14224 cl. F.3.2, p.253)
- ฟิลด์ SIS failure mode classification (DU, DD, SU, SD) อยู่ใน failure record (ISO 14224 Table 6, p.41)
- Downtime: MTTRes = MFDT + MRT; กรณี DD เวลา detect เล็กมาก ถือ MTTRes ใกล้ MRT ได้ (cl. F.3.3, p.253)

## 3. CCF และ CMF (ISO 14224 cl. C.1.6-C.1.7, p.207)

- common cause = หลาย item เสียจากสาเหตุเดียว; common mode = หลาย item เสียด้วย mode เดียวกัน (สาเหตุต่างได้) (cl. 3.5-3.6, p.3)
- กลุ่ม CCF: utilities/สิ่งแวดล้อมภายนอก, internal (design/installation error, lot ชิ้นส่วนไม่ดี), cascade
- ถ้าวิเคราะห์ละเอียดไม่ได้ใช้ beta-factor: แบ่ง failure rate เป็นส่วนอิสระ (1 ลบ beta) และส่วน CCF (beta) (อ้าง ISO/TR 12489 Annex G)
- ถ้าละเลย dependency ผลคำนวณจะต่ำเกินจริง ซึ่งรับไม่ได้ในงาน safety (cl. C.1.4-C.1.5, p.206-207)
- ผลกับ redundancy ดู [[Redundancy and Standby Systems]]

## 4. Failure fraction (ISO 14224 cl. F.4.1, p.253-254)

- นิยาม: จำนวน safety critical failure ที่พบจาก periodic test หารด้วยจำนวน test
- คือ instantaneous unavailability ณ เวลาทดสอบ และเป็นค่าประมาณแบบ conservative ของ PFDavg
- **ไม่ใช่** safe failure fraction (SFF) ของ IEC 61508-4 ห้ามสับสน
- เป็น KPI ข้อ 34 ใน Annex E ติดตามรายปี (ISO 14224 Table E.3, p.250) ดู [[Maintenance KPIs]]
- ความรู้ทั่วไปที่ไม่ได้พิมพ์ใน Annex F: PFDavg แบบง่ายประมาณ lambda-DU x tau / 2 สอดคล้องกับสูตร U = 0.5 x FFI / MTBF ใน [[Failure Finding Interval]] (ใช้ low confidence ส่วนนี้) Annex C ให้สูตรตั้ง test interval จากความพร้อมที่ต้องการ และจากคุ้มทุน (ISO 14224 cl. C.6.2-C.6.3, p.225-227)

## 5. Redundancy rule ของคำว่า "critical" ตาม ISO/TR 12489

dangerous failure ที่ทำให้ SIF ใช้ไม่ได้ = safety critical failure ของ SIF นั้น ตัวอย่างในมาตรฐาน: SIF มี A และ B เป็น redundant dangerous failure ของ A เป็น "critical" ตาม TR 12489 ก็ต่อเมื่อเป็น critical ตาม ISO 14224 และ B เสียแบบ dangerous critical อยู่ก่อนแล้ว (ISO 14224 cl. F.4.1, p.253-254) ความต่างจากความหมายอื่นของ "critical" ดู [[Failure Impact Classification]] และ [[Criticality Assessment]]

## 6. Table F.1 นิยาม failure ที่พบจากการ test (ISO 14224 Table F.1, p.254-259)

42 รายการ เกณฑ์ทั่วไปคือไม่ทำงานเมื่อ test/สั่ง หรือไม่ทันเวลาที่กำหนด แมปกับรหัส failure mode ของ ISO 14224 ตัวอย่าง

| อุปกรณ์ | เกณฑ์ (สรุป) | รหัส mode |
|---|---|---|
| Fire pump | ไม่ start หรือ capacity ต่ำกว่า 90% ของ design | FTS, LOO |
| ESD valve, BOP, DHSV | ไม่ปิดตามเวลา หรือรั่วเกินเกณฑ์ | FTC, DOP, LCP |
| PSV | ไม่เปิดที่ค่าไม่เกินระหว่าง 120% ของ set pressure กับ set + 5 MPa | FTO |
| Deluge, blowdown valve | ไม่เปิดเมื่อ test; nozzle อุดเกิน 3% | FTO, DOP, PLU |
| Fire and gas detector, input devices | logic ไม่ได้รับสัญญาณหรือสัญญาณผิด | NOO, LOO, FTF |
| Emergency generator | ไม่ start หรือ output ต่ำ | FTS, LOO |

- INL (รั่ว utility fluid) ไม่เท่ากับ LCP (hydrocarbon รั่วผ่านบ่าวาล์ว) และไม่ถือ dangerous ใน fail-safe design; DHSV leak test รายงาน initial leak rate พร้อมวิธีวัด (Table F.1 footnotes)
- การใช้นิยามเดียวกันทำให้ benchmark ด้าน safety ข้ามบริษัทได้ (cl. F.4, p.253)
- รหัส FTS, LOO ฯลฯ ที่ wiki ใช้กับ compressor ดู [[Failure Mode]]; รหัสอื่นในตารางนี้ (FTC, FTO, DOP, LCP, PLU, NOO, FTF) ไม่อยู่ใน dataset compressor ของ wiki

## เชื่อมโยงกับ compressor failure hierarchy

- compressor เองไม่ใช่ safety system แต่ shutdown/trip logic และ valve ที่ผูกอยู่กับ compressor อาจเป็น SCE การตีความนี้ไม่มีใน sources
- trip ที่ไม่จำเป็น (spurious trip) เทียบได้กับ [[UST Spurious Stop]] ตามที่ Annex C ระบุ (cl. C.1.8, p.208)

## Triplets

- [[Safety Critical Failure Classification]] [defined_in:: [[ISO 14224]]] Annex F informative (cl. F.1-F.2, p.251)
- [[Safety Critical Failure Classification]] [depends_on:: IEC 61508] also IEC 61511 and ISO/TR 12489:2013 (cl. F.1-F.2, p.251)
- [[Safety Critical Failure Classification]] [applies_to:: Safety Instrumented System] also fire and gas, ESD valve
- Safety Instrumented System [related_to:: Hidden Failure] mostly dormant, hidden failures must be found before demand (cl. F.3, p.252)
- [[Safety Critical Failure Classification]] [related_to:: [[Failure Finding Interval]]] same principle; FFI page based on RBMM, not IEC 61508
- Random Failure [differs_from:: Systematic Failure] separate first; systematic recurs under specific conditions (cl. 3.79, 3.90, p.15, p.17)
- DD [is_a:: [[Safety Critical Failure Classification]]] random failure group
- DD [has_label:: dangerous detected] found by diagnostics
- DU [is_a:: [[Safety Critical Failure Classification]]] random failure group
- DU [has_label:: dangerous undetected] found by periodic test or on demand
- DU [detected_by:: Periodic Test] periodic test interval is a focus of SIS data collection
- SD [is_a:: [[Safety Critical Failure Classification]]] random failure group
- SD [has_label:: safe detected]
- SU [is_a:: [[Safety Critical Failure Classification]]] random failure group
- SU [has_label:: safe undetected]
- Random Failure [has_part:: DD] (cl. F.3.1-F.3.2, p.252-253)
- Random Failure [has_part:: DU]
- Random Failure [has_part:: SD]
- Random Failure [has_part:: SU]
- Dangerous Failure [has_label:: dangerous] prevents safety action
- Safe Failure [has_label:: safe] favours safety action, e.g. trips by itself
- SIS Failure Mode Classification [part_of:: [[Failure Data Recording]]] DU, DD, SU, SD field in failure record (Table 6, p.41)
- Common Cause Failure [differs_from:: Random Failure] some CCF are systematic, not counted in the 4 random groups (cl. F.3.2, p.253)
- Mean Time To Restoration [has_formula:: MTTRes = MFDT + MRT] for DD, MTTRes close to MRT (cl. F.3.3, p.253)
- Common Cause Failure [has_label:: common cause] several items fail from one cause (cl. 3.5-3.6, p.3)
- Common Mode Failure [has_label:: common mode] several items fail in same mode, causes may differ (cl. 3.5-3.6, p.3)
- Common Cause Failure [has_category:: utilities/external environment, internal, cascade] (cl. C.1.6-C.1.7, p.207)
- Beta-Factor Model [applies_to:: Common Cause Failure] independent part (1 - beta), CCF part (beta); ISO/TR 12489 Annex G
- Common Cause Failure [related_to:: [[Redundancy and Standby Systems]]] ignoring dependency underestimates results (cl. C.1.4-C.1.5, p.206-207)
- Failure Fraction [has_formula:: safety critical failures found in periodic tests / number of tests] (cl. F.4.1, p.253-254)
- Failure Fraction [measures:: Instantaneous Unavailability] at test time; conservative estimate of PFDavg
- Failure Fraction [differs_from:: Safe Failure Fraction] not IEC 61508-4 SFF
- Failure Fraction [is_a:: [[Maintenance KPIs]]] KPI 34 in Annex E, tracked yearly (Table E.3, p.250)
- PFDavg [has_formula:: lambda-DU x tau / 2] general knowledge, not printed in Annex F [confidence:: low]
- PFDavg [related_to:: [[Failure Finding Interval]]] consistent with U = 0.5 x FFI / MTBF [confidence:: low]
- Test Interval [defined_in:: [[ISO 14224]]] Annex C formulas from required availability and cost-benefit (cl. C.6.2-C.6.3, p.225-227)
- Safety Critical Failure [depends_on:: Redundancy] dangerous failure of A is critical per TR 12489 only if critical per ISO 14224 and redundant B already failed dangerous critical (cl. F.4.1, p.253-254)
- Safety Critical Failure [differs_from:: [[Failure Impact Classification]]] different meaning of critical
- Safety Critical Failure [differs_from:: [[Criticality Assessment]]] different meaning of critical
- ISO:F.1 [has_value:: 42] test failure definitions (Table F.1, p.254-259)
- Fire Pump [has_failure_mode:: FTS] fails to start (Table F.1)
- Fire Pump [has_failure_mode:: [[LOO Low Output]]] capacity below 90% of design
- ESD Valve [has_failure_mode:: FTC] also BOP, DHSV
- ESD Valve [has_failure_mode:: DOP] also BOP, DHSV
- ESD Valve [has_failure_mode:: LCP] leak above criterion
- PSV [has_failure_mode:: FTO] not open at max of 120% set pressure and set + 5 MPa
- Deluge Valve [has_failure_mode:: FTO] also blowdown valve
- Deluge Valve [has_failure_mode:: DOP] also blowdown valve
- Deluge Valve [has_failure_mode:: PLU] nozzles plugged above 3%
- Fire and Gas Detector [has_failure_mode:: NOO] also input devices
- Fire and Gas Detector [has_failure_mode:: [[LOO Low Output]]] also input devices
- Fire and Gas Detector [has_failure_mode:: FTF] also input devices
- Emergency Generator [has_failure_mode:: FTS]
- Emergency Generator [has_failure_mode:: [[LOO Low Output]]] low output
- INL [differs_from:: LCP] utility fluid leak vs hydrocarbon seat leak; INL not dangerous in fail-safe design (Table F.1 footnotes)
- [[Failure Mode]] [differs_from:: ISO:F.1] FTC, FTO, DOP, LCP, PLU, NOO, FTF not in wiki compressor dataset
- [[UST Spurious Stop]] [maps_to:: Spurious Trip] per Annex C (cl. C.1.8, p.208)
- [[Compressor]] [related_to:: Safety Critical Element] shutdown/trip logic and valves may be SCE; interpretation not in sources [confidence:: low]

---
title: Fault Tree Analysis
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [fta, reliability, criticality, cmrp]
sources: [cmrp.md, reliability-based-maintenance-management.md, iso-14224.md]
confidence: medium
contested: false
---

# Fault Tree Analysis

Fault Tree Analysis (FTA) คือการวิเคราะห์แบบ top-down (deductive) ที่เริ่มจากเหตุการณ์ไม่พึงประสงค์ระดับบน (top event) แล้วแตกลงไปหาเหตุการณ์ระดับล่างที่ทำให้เกิด โดยเชื่อมด้วย Boolean logic gate (CMRP CMPR-11 p.16) ต่างจาก [[FMECA]] ที่เป็น bottom-up (เริ่มจาก failure mode ของชิ้นส่วน) หน้านี้สรุป gate/สัญลักษณ์ cut set, minimal cut set, common cause และความสัมพันธ์กับ [[Reliability Block Diagram]] ส่วนใหญ่มาจาก [[CMRP Course]]

## ใช้เพื่ออะไร (CMRP CMPR-11 p.17)

- เข้าใจ logic ที่นำไปสู่ top event
- แสดงว่าระบบผ่าน safety/reliability requirement
- จัดลำดับ contributor (critical items list) และ optimize ทรัพยากร
- monitor safety performance, ใช้เป็น design tool และ diagnostic tool

## ประวัติและมาตรฐาน (CMRP CMPR-11 p.17-19)

- H.A. Watson, Bell Labs 1962 (ระบบ launch control ของ Minuteman I); Boeing/AVCO ขยายใช้ 1963-64; NASA หันไปใช้ FMEA หลังผล quantitative ของ Apollo ไม่น่าพอใจ แล้วกลับมาใช้ PRA/FTA หลัง Challenger (1986)
- OSHA Process Safety Management (1992) ยอมรับ FTA เป็นวิธีหนึ่งของ PHA **flag สไลด์:** อ้างเป็น "19 CFR 1910.119" ที่ถูกคือ 29 CFR 1910.119 (ความรู้ทั่วไป)
- มาตรฐาน/คู่มือที่สไลด์อ้าง: NUREG-0492, SAE ARP4761, MIL-HDBK-338, IEC 61025 (EN 61025)
- software: CAFTA (EPRI), SAPHIRE (INL), RiskSpectrum, SCRAM (open source) (p.21-22)
- [[ISO 14224]] Table D.1 จัด FTA อยู่ในกลุ่มการวิเคราะห์ทั่วไป (ร่วมกับ Markov, Petri net) ซึ่งต้องใช้ข้อมูล failure rate, CCF rate, PFD, repair rate, test efficiency, test interval ดู [[RM Data Quality]]

## สัญลักษณ์ (CMRP CMPR-11 p.22-23)

| กลุ่ม | สัญลักษณ์ | ความหมาย |
|---|---|---|
| Event | basic event | เหตุการณ์ระดับล่างสุดที่ไม่แตกต่อ (failure ของชิ้นส่วน) |
| Event | intermediate event | ผลของ gate ระดับกลาง |
| Event | undeveloped event | ไม่แตกต่อเพราะข้อมูลไม่พอหรือไม่สำคัญ |
| Event | external (house) event | เหตุการณ์ที่เกิดแน่นอนหรือไม่เกิดแน่นอน (prob 1 หรือ 0) ใช้เปิด/ปิดสาขา |
| Event | conditioning event | เงื่อนไขที่ใช้กับ gate (เช่น inhibit) |
| Gate | OR | output เกิดเมื่อ input ใดก็ได้เกิด |
| Gate | AND | output เกิดเมื่อ input ทุกตัวเกิด |
| Gate | exclusive OR | output เกิดเมื่อ input เกิดเพียงหนึ่งเดียว |
| Gate | priority AND | output เกิดเมื่อ input เกิดตามลำดับที่กำหนด |
| Gate | inhibit | output เกิดเมื่อ input เกิดและ conditioning event เป็นจริง |
| Other | transfer | เชื่อม sub-tree ที่อยู่หน้าอื่น |

ตัวอย่างในสไลด์ (p.20): metal stamping press top event = มือ/อวัยวะถูกกด แยก OR (ระหว่าง operation ปกติ หรือระหว่าง maintenance) และ OR (operator หรือคนอื่น) การออกแบบให้ต้องกดสองปุ่มพร้อมกันเปลี่ยน logic เป็น AND ซึ่งลดโอกาสเกิด

### การคำนวณ (ความรู้ทั่วไปบางส่วน)

```
OR gate  (events อิสระ):  P_out = 1 - Π (1 - P_i)
AND gate (events อิสระ):  P_out = Π P_i
```

สูตร OR ตรงกับ "failure tree" Ft = 1 - Π(1 - Fi) ที่ RBMM ให้ไว้เป็นด้านตรงข้ามของ RBD อนุกรม (RBMM p.172-174) ดู [[Reliability Block Diagram]] ส่วนสูตร AND และการตั้งสมมติฐานความเป็นอิสระของ event เป็นความรู้ทั่วไป ไม่ได้พิมพ์ในสไลด์ [confidence: low]

## Cut set และ minimal cut set (CMRP CMPR-11 p.21)

- **cut set** = ชุดของ basic event ที่ถ้าเกิดพร้อมกันจะทำให้เกิด top event
- **minimal cut set** = cut set ที่ตัด event ใดออกไปหนึ่งตัวแล้วจะไม่ทำให้เกิด top event อีก (ลดลงไม่ได้แล้ว)
- (ความรู้ทั่วไป) minimal cut set ที่มี event เดียว = single point of failure; ลำดับของ cut set (จำนวน event) ใช้จัดลำดับจุดอ่อนของการออกแบบ [confidence: low]
- event tree ต่างจาก fault tree: event tree เริ่มจาก initiating event แล้วไล่ไปหาผลลัพธ์หลายแบบ (inductive) (p.21)

## Common cause / common mode (CMRP CMPR-11 p.20)

event เดียวที่กระทบหลาย subsystem จะปรากฏหลายจุดใน tree ทำให้ event ไม่อิสระต่อกันและคำนวณยากขึ้น (สูตร AND แบบคูณกันใช้ตรง ๆ ไม่ได้) นิยามตาม ISO: common cause = หลาย item เสียจากสาเหตุเดียว, common mode = หลาย item เสียด้วย mode เดียวกัน และถ้าวิเคราะห์ละเอียดไม่ได้ ใช้ beta-factor แยกส่วน CCF ดู [[Safety Critical Failure Classification]]

## FTA เทียบกับ RBD (CMRP CMPR-11 p.24)

| ประเด็น | FTA | RBD |
|---|---|---|
| มุมมอง | failure (top event = ระบบเสีย) | success (เส้นทางที่ระบบทำงานได้) |
| เทียบ logic | OR gate | blocks อนุกรม |
| เทียบ logic | AND gate | blocks ขนาน |
| การแปลง | แปลง FT เป็น RBD ได้ง่ายกว่า | แปลงกลับยากกว่า |
| load sharing, standby (quiescent failure) | ไม่มีตัวเทียบตรงใน FTA คลาสสิก (priority AND แทนได้บางส่วน) | มี |
| XOR gate | มี | ไม่มีตัวเทียบ (จะหมายถึงระบบทำงานได้แม้ทุกชิ้นเสีย) |
| house event | prob 0/1 | block ที่ไม่เสียหรือเสียแน่นอน |
| transfer | sub-tree | subdiagram block |

การจับคู่ OR-อนุกรม และ AND-ขนาน สอดคล้องกับสูตร RBMM ใน [[Reliability Block Diagram]] ส่วน standby/k-out-of-n ดู [[Redundancy and Standby Systems]]

## เชื่อมโยงกับ compressor failure hierarchy (ตีความ)

- top event ระดับเครื่อง เช่น compressor trip ([[UST Spurious Stop]]) แตกลงตาม [[Failure Hierarchy]]: sub unit → [[Maintainable Item]] → failure mode เป็น basic event ได้ โดยใช้ failure rate จาก [[OREDA]] เป็นค่า input (การตีความ ไม่อยู่ในสไลด์)
- FTA ใช้คู่กับ [[FMECA]] และ [[Criticality Assessment]]: FMECA หา failure mode ทีละชิ้น ส่วน FTA รวมผลแบบหลายเหตุการณ์ร่วมกัน (รวม CCF) ที่ FMECA มองไม่เห็น
- การหาสาเหตุหลังเกิดเหตุใช้ [[Root Cause Analysis]] ซึ่งมีแผนภาพแบบ logic tree คล้ายกัน

## ดูเพิ่ม

- [[Reliability Block Diagram]]
- [[Safety Critical Failure Classification]]
- [[Redundancy and Standby Systems]]
- [[FMECA]]
- [[CMRP Course]]

## Triplets

- [[Fault Tree Analysis]] [is_a:: Deductive Analysis Method] top-down, Boolean logic to top event (CMRP CMPR-11 p.16)
- [[Fault Tree Analysis]] [differs_from:: [[FMECA]]] FTA top-down, FMECA bottom-up
- [[Fault Tree Analysis]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-11 p.16-24)
- [[Fault Tree Analysis]] [produces:: Critical Items List] ranks contributors (CMRP CMPR-11 p.17)
- H.A. Watson [source_of:: [[Fault Tree Analysis]]] Bell Labs 1962, Minuteman I (CMRP CMPR-11 p.17)
- [[Fault Tree Analysis]] [defined_in:: IEC 61025] also NUREG-0492, SAE ARP4761, MIL-HDBK-338 (CMRP CMPR-11 p.19)
- OSHA PSM Citation 19 CFR 1910.119 [contradicts:: 29 CFR 1910.119] slide typo, general knowledge (CMRP CMPR-11 p.18)
- [[Fault Tree Analysis]] [uses:: CCF Rate] also failure rate, PFD, repair rate, test interval (ISO 14224 Table D.1) see [[RM Data Quality]]
- [[Fault Tree Analysis]] [has_part:: Top Event]
- [[Fault Tree Analysis]] [has_part:: Basic Event]
- [[Fault Tree Analysis]] [has_part:: OR Gate]
- [[Fault Tree Analysis]] [has_part:: AND Gate]
- [[Fault Tree Analysis]] [has_part:: Priority AND Gate] also exclusive OR, inhibit (CMRP CMPR-11 p.22-23)
- House Event [has_value:: probability 0 or 1] (CMRP CMPR-11 p.24)
- OR Gate [has_formula:: P_out = 1 - Π (1 - P_i)] independent events; same as RBMM failure tree Ft (RBMM p.172-174)
- AND Gate [has_formula:: P_out = Π P_i] independent events, general knowledge [confidence:: low]
- Cut Set [is_a:: Basic Event Combination] causes top event (CMRP CMPR-11 p.21)
- Minimal Cut Set [is_a:: Cut Set] removing any event no longer causes top event (CMRP CMPR-11 p.21)
- Single Point Of Failure [is_a:: Minimal Cut Set] one-event cut set, general knowledge [confidence:: low]
- Event Tree [differs_from:: [[Fault Tree Analysis]]] starts from initiating event, forward to outcomes (CMRP CMPR-11 p.21)
- Common Cause Failure [depends_on:: Event Dependency] same event appears in several branches, complicates calculation (CMRP CMPR-11 p.20)
- Common Cause Failure [related_to:: [[Safety Critical Failure Classification]]] ISO definition and beta-factor
- OR Gate [maps_to:: Series Configuration] RBD equivalent (CMRP CMPR-11 p.24)
- AND Gate [maps_to:: Parallel Configuration] RBD equivalent (CMRP CMPR-11 p.24)
- [[Fault Tree Analysis]] [related_to:: [[Reliability Block Diagram]]] FT converts to RBD more easily than reverse (CMRP CMPR-11 p.24)
- XOR Gate [differs_from:: [[Reliability Block Diagram]]] no RBD equivalent (CMRP CMPR-11 p.24)
- [[Reliability Block Diagram]] [has_part:: Load Sharing] and standby, no classic FTA equivalent (CMRP CMPR-11 p.24)
- [[Fault Tree Analysis]] [applies_to:: [[Compressor]]] top event decomposed along failure hierarchy, interpretation [confidence:: low]

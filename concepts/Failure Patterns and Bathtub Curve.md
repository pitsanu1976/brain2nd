---
title: Failure Patterns and Bathtub Curve
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [reliability, weibull, failure-rate, rcm, pm, book, cmrp]
sources: [reliability-based-maintenance-management.md, cmrp.md]
confidence: medium
contested: false
---

# Failure Patterns and Bathtub Curve

รูปแบบการเสีย (failure pattern) คือรูปร่างของ failure rate เทียบกับเวลาของแต่ละ failure mode หนังสือ RBMM แบ่งเป็น 5 แบบ (A-E) และผูกกับค่า Weibull β ส่วน bathtub curve เป็นภาพรวมระดับเครื่องที่เกิดจากการรวมหลายชิ้นส่วน หน้านี้สรุปทั้งสองแนวคิด พร้อมกฎเลือกประเภทงาน PM ตามค่า β (RBMM ch7) และจุดที่หนังสือไม่สอดคล้องกันเอง

## Failure pattern A-E (RBMM p.155-158)

| Pattern | ลักษณะ failure rate | ตัวอย่างพารามิเตอร์ | β |
|---|---|---|---|
| A | ต่ำมากช่วงต้น แล้วพุ่งเร็วช่วงปลาย (wear-out ชัด) | β = 15, η = 30,000 | >> 1 |
| B | ไม่คงที่ เพิ่มค่อย ๆ | β = 3, η = 30,000 | > 1 |
| C | ต่ำช่วงแรก แล้วเพิ่มและคงที่ | β = 1.5, η = 5,000 | > 1 เล็กน้อย |
| D | คงที่ตลอด (random) | β = 1, η = 5,000 | = 1 |
| E | สูงมากช่วงแรกแล้วลดเร็ว (infant mortality) | β = 0.5, η = 5,000 | < 1 |

หน่วยของ η ไม่ระบุชัดใน notes (ตัวอย่างอายุอยู่ในช่วงชั่วโมงหรือหน่วยอายุอื่น)

β กำหนดรูปการกระจาย 3 แบบ (RBMM p.156-157):
- β > 1 รูประฆังคว่ำ ช่วงต้นยังไม่คาดว่าจะเสีย (t1) หลังช่วงปลาย (t2) ไม่เหลือรอด เมื่อ η มากขึ้น (β เท่าเดิม) ระฆังแบนและกว้างขึ้น
- β ≈ 1 เหมือน Exponential density สูงตอนต้นแล้วลด failure rate คงที่
- β < 1 hyper-exponential density สูงมากตอนต้น failure rate ลดลง

อธิบาย Weibull เต็มที่ใน [[Weibull Analysis]]

## Bathtub curve (RBMM p.145-146, ch5)

กราฟอ่างอาบน้ำของ **เครื่องจักรทั้งเครื่อง** (Fig 5.24) มี 3 ช่วง:

| ช่วง | β | คำอธิบาย |
|---|---|---|
| Infant Mortality | < 1 | อัตราเสียลดลง จากชิ้นส่วนบกพร่องจากโรงงาน ประกอบผิด หรือใช้ผิด spec ผู้ผลิตรับประกันเฉพาะความผิดของตน |
| Normal Usage Period | = 1 | เสียแบบสุ่ม แต่ยังต้อง PM เพราะเครื่องมีชิ้นส่วนหลายแบบ (A-E) ต้องพิจารณาว่าชิ้นใดสำคัญ |
| Designed Life End (wear-out) | > 1 | อัตราเสียเพิ่ม บางระบบซ่อมไม่คุ้มต้องซื้อใหม่ |

หนังสือชี้ว่าอ่างน้ำเกิดจากการรวมชิ้นส่วนหลายแบบ ระดับ **failure mode เดี่ยว** จึงควรดู pattern A-E (RBMM p.155) ใน ch12 ผู้เขียนกล่าวว่า failure rate มี 6 รูปแบบ เทียบกับ 6 pattern ของ RCM แต่ ch6 แสดง 5 แบบ และไม่ได้อธิบายแบบที่ 6 ใน notes (RBMM p.379)

## ตัวอย่างรถยนต์ (RBMM p.146-149, ch5)

- Lube oil อายุเฉลี่ย 13,000 กม. (ไม่ก่อน 8,000 ไม่เกิน 15,000) เปลี่ยนทุก 10,000 กม.
- Timing belt อายุเฉลี่ย 110,000 กม. ไม่เสียก่อน 90,000 ไม่เกิน 130,000 ผู้ผลิตกำหนดเปลี่ยนที่ 80,000 กม. (safe-life)
- Water pump มีสัญญาณเตือนล่วงหน้า ใช้ inspection ทุก 10,000 กม. แทนเปลี่ยนตามเวลา
- Gear box ออกแบบให้ชิ้นส่วนอายุใกล้กัน จึงเหมาะ scheduled overhaul
- ชิ้นที่เสียก่อน warranty (infant mortality) PM ไม่ช่วย สาเหตุคือชิ้นส่วน ประกอบ หรือ QC

## กฎเลือกประเภทงานตาม β (RBMM p.183-189, ch7)

| ช่วง β | กฎ |
|---|---|
| β < 1 | PM แก้ไม่ได้ ต้องแก้ที่สาเหตุ: อะไหล่ไม่ได้มาตรฐาน ฝีมือซ่อม การใช้งาน หรือตัวงาน PM เอง (เสียหลัง maintenance ไม่นาน) |
| β = 1 | scheduled replace/overhaul ไม่ช่วย ทางเลือกคือ condition monitoring ใช้กับชิ้นไม่สำคัญหรือ MTBF ยาวมาก อย่าให้ปนในกล่อง overhaul |
| β → 1 (ค่อนข้างเพิ่มช้า) | ทางเลือกหลักคือ condition monitoring |
| β >> 1 | condition monitoring, part replacement หรือ overhaul; ไม่ต้องตรวจเข้มช่วงต้นอายุ เริ่มตรวจก่อนถึง t1 |

**หลักฐานเชิงตัวเลขเมื่อ β = 1** (RBMM p.186-187): R(t) = exp(-t/η); ถ้าไม่เปลี่ยนตามแผนได้ R(120) = 47.0158% (conditional R(120/80) = 77.758%) ส่วนถ้าเปลี่ยนทุก 80 ชม. ได้ R(80) x R(40) = 60.4639% x 77.7585% = 47.0158% เท่ากัน ดังนั้น replacement ตามแผนไม่เพิ่ม reliability (η ในตัวอย่างอนุมานได้ราว 160 ชม. เป็น derived ไม่ได้ระบุในหน้า) ตัวอย่างหลอดไฟใน ch12 ให้ข้อสรุปเดียวกัน (เปลี่ยนทุก 1,000 หรือ 500 ชม. ยังได้ 72.57% ที่ 2,000 ชม., RBMM p.378) ดู [[Statistical Distributions for Maintenance]]

ตัวอย่างข้อมูล TTF 8,500-16,000 ชม. ได้ β ≈ 3.8 จึงเป็น pattern A (เกาะกลุ่ม) ไม่ใช่ pattern D ซึ่งทำให้สมมติ constant failure rate ผิด (RBMM p.199, ch7) ดู [[Weibull Analysis]]

## สัดส่วน failure pattern ตาม CMRP

ส่วนนี้เพิ่มจาก [[CMRP Course]] RBMM ไม่ให้สัดส่วน % ของแต่ละ pattern จึงไม่ขัดกับเนื้อหาเดิมโดยตรง

**CMPR-01 p.28** แสดง bathtub 3 ช่วง (infant, random/externally caused, wear-out) แล้วแสดง 4 รูปแบบพร้อมสัดส่วน (รวม 100%, ไม่ระบุแหล่ง):

| รูปแบบ (CMRP) | % | เทียบ Nowlan & Heap (ตีความ) | เทียบ RBMM (ตีความ) |
|---|---|---|---|
| Wear-out | 2 | B | A |
| Bathtub | 4 | A | ไม่มีใน A-E (เป็นภาพระดับเครื่อง) |
| Random | 26 | C 5 + D 7 + E 14 | C, D (บางส่วน B) |
| Infant mortality | 68 | F | E |

- คอลัมน์ Nowlan & Heap เป็นการตีความของ wiki: ตัวเลขของ Nowlan & Heap (1978, การบินพลเรือน) ที่รู้จักทั่วไปคือ A bathtub 4%, B wear-out 2%, C ค่อย ๆ เพิ่ม 5%, D ต่ำแล้วคงที่ 7%, E random 14%, F infant 68% (general knowledge, confidence low, ไม่อยู่ใน sources) slide ยุบ C+D+E = 26% เป็น "Random" โดยไม่บอก
- **ระบบตัวอักษรต่างกัน**: Nowlan & Heap ใช้ A = bathtub และ F = infant แต่ RBMM (ตารางข้างบน) ใช้ A = wear-out ชัด และ E = infant ห้ามเทียบตัวอักษรข้ามแหล่งตรง ๆ
- นัยของ slide: มีเพียงราว 6% (2 + 4) ที่มีช่วง wear-out ชัด time-based replacement จึงได้ผลกับ failure ส่วนน้อย สอดคล้องกับกฎเลือกงานตาม β ข้างบน

**CMPR-03 p.5** อ้างว่าราว **60%** ของอุปกรณ์แสดงแค่ช่วง infant และ random ไม่ถึง wear-out (ไม่ระบุแหล่ง, confidence low)
- ตัวเลขนี้ไม่สอดคล้องกับ p.28 ของหลักสูตรเดียวกัน: ถ้านับ infant + random จาก p.28 จะได้ 68 + 26 = 94% (derived) ความต่างน่าจะมาจากคนละการศึกษาหรือคนละนิยามว่า "ไม่มี wear-out"
- ความรู้ทั่วไป (confidence low, ไม่ยืนยัน): การศึกษาภายหลังของ US Navy (เช่น SUBMEPP 2001) ให้สัดส่วน pattern E + F ราว 60% ซึ่งอาจเป็นที่มาของตัวเลขนี้
- เป็นข้อไม่สอดคล้องภายใน CMRP ที่ไม่มีแหล่ง ไม่ใช่ข้อขัดแย้งกับ RBMM หรือ ISO จึงไม่ตั้ง contested

## จุดที่หนังสือไม่สอดคล้องกัน (flag)

- **Fig 6.14 (RBMM p.165-166):** จับ A กับ β >>> 1, B/C/D กับ β ≈ 1, E กับ β < 1 แต่ตัวอย่างก่อนหน้า (p.155-156) ให้ B ที่ β = 3 ซึ่งไม่ใกล้ 1 ควรใช้ตัวเลขตัวอย่างเป็นหลัก
- **การระบุ infant mortality:** ch6 ระบุว่า pattern E คือ infant mortality และ D คือ random แต่ ch5 พูดถึง "Infant Mortality แบบ D" (RBMM p.148) และ ch7 จัด A/B เป็น β >> 1 มีอาการล่วงหน้า (ขัดกับตาราง ch6 ที่ B β = 3 ซึ่งไม่ >> 1) (RBMM p.207) ใช้นิยามของ ch6 เป็นหลัก
- ทั้งหมดนี้เป็นความไม่สอดคล้องภายในหนังสือ ไม่ขัดกับข้อมูลเดิมใน wiki จึงตั้ง `contested: false`

## เชื่อมโยงกับ compressor failure hierarchy

- Bathtub ระดับ [[Compressor]] ทั้งเครื่องเป็นผลรวมของ failure mode หลายตัวในหลาย [[Maintainable Item]] ต้องแยก pattern รายโหมด
- **สมมติฐาน (hypothesis, confidence low, ไม่ใช่ข้อเท็จจริงจาก source):** AIR (abnormal instrument reading) และ SER ใน [[Failure Mode]] อาจมีลักษณะใกล้ pattern D (random) หรือ E (หลัง maintenance) แต่ sources ไม่มีค่า β ของ compressor failure mode ใด ๆ จึงยืนยันไม่ได้ ส่วน wear-out เช่น seal/bearing อาจเป็น β > 1 ก็เป็นสมมติฐานเช่นกัน ต้องยืนยันจากข้อมูล failure จริงด้วย [[Weibull Analysis]]
- [[ELP External Leakage Process Medium]] และ [[ELU External Leakage Utility Medium]] จาก seal/gasket wear อาจ monitor ด้วย condition-based task แต่ไม่มี β ใน sources
- [[OREDA]] ใน wiki นี้มีแต่ % สัมพัทธ์ ไม่มี β หรือ failure rate สัมบูรณ์ (ถ้า handbook ใช้ failure rate คงที่ ซึ่งเทียบเท่า β = 1 ก็จะบดบังรูปแบบ A-E เป็นข้อสังเกตทั่วไป ไม่มีใน sources); [[Failure Mechanism]] ที่เกิดจากการเสื่อมตามอายุ (wear, fatigue) สัมพันธ์กับ β > 1 ส่วน infant mortality สัมพันธ์กับสาเหตุ assembly/installation ใน [[Failure Cause Codes]]

## ดูเพิ่ม

- [[Weibull Analysis]]
- [[Reliability Metrics]]
- [[PM Task Selection]]
- [[Failure Mode]]
- [[Failure Finding Interval]]

## Triplets

- Failure Pattern [is_a:: Failure Rate Versus Time Shape] per failure mode
- Failure Pattern [depends_on:: Shape Parameter Beta] (RBMM p.155-158)
- Pattern A [is_a:: Failure Pattern] very low early then rises fast, clear wear-out (RBMM p.155-158)
- Pattern A [has_value:: β = 15, η = 30,000] β >> 1
- Pattern B [is_a:: Failure Pattern] gradually increasing
- Pattern B [has_value:: β = 3, η = 30,000] β > 1
- Pattern C [is_a:: Failure Pattern] low at first then increases and levels off
- Pattern C [has_value:: β = 1.5, η = 5,000] β slightly > 1
- Pattern D [is_a:: Failure Pattern] constant, random
- Pattern D [has_value:: β = 1, η = 5,000]
- Pattern E [is_a:: Failure Pattern] very high early then drops, infant mortality
- Pattern E [has_value:: β = 0.5, η = 5,000] β < 1
- Shape Parameter Beta [has_value:: β > 1] bell shape; larger η gives flatter, wider bell (RBMM p.156-157)
- Shape Parameter Beta [has_value:: β ≈ 1] like Exponential density, constant failure rate (RBMM p.156-157)
- Shape Parameter Beta [has_value:: β < 1] hyper-exponential, decreasing failure rate (RBMM p.156-157)
- Bathtub Curve [applies_to:: Whole Machine] combination of many parts (RBMM p.145-146 Fig 5.24)
- Bathtub Curve [has_part:: Infant Mortality] β < 1, decreasing rate, factory defects, wrong assembly or use
- Bathtub Curve [has_part:: Normal Usage Period] β = 1, random, still needs PM
- Bathtub Curve [has_part:: Designed Life End] β > 1, wear-out, increasing rate
- Bathtub Curve [differs_from:: Failure Pattern] bathtub is machine level; single failure mode uses pattern A-E (RBMM p.155)
- RBMM ch12 Six Failure Rate Patterns [contradicts:: RBMM ch6 Five Failure Patterns] ch12 says 6 like RCM, ch6 shows 5 (RBMM p.379)
- RBMM ch6 Five Failure Patterns [contradicts:: RBMM ch12 Six Failure Rate Patterns] internal book inconsistency (RBMM p.155-158)
- Lube Oil Car Example [has_value:: 13,000 km] mean life, changed every 10,000 km (RBMM p.146-149)
- Timing Belt Car Example [has_value:: 110,000 km] mean life, replaced at 80,000 km safe-life
- Water Pump Car Example [uses:: Inspection] every 10,000 km instead of time replacement
- Gear Box Car Example [uses:: Scheduled Overhaul] parts designed with similar life
- Infant Mortality [has_cause:: Parts, Assembly Or QC] PM does not help
- Shape Parameter Beta [selects:: Root Cause Correction] β < 1, PM cannot fix (RBMM p.183-189)
- Shape Parameter Beta [selects:: Condition Monitoring] β = 1, scheduled replace/overhaul does not help (RBMM p.183-189)
- Shape Parameter Beta [selects:: Condition Monitoring] β → 1 slowly increasing, main option
- Shape Parameter Beta [selects:: Condition Monitoring, Part Replacement Or Overhaul] β >> 1, start inspection before t1
- Constant Failure Rate Replacement Example [has_value:: 47.0158%] R(120) without replacement equals R(80) x R(40) = 60.4639% x 77.7585% (RBMM p.186-187)
- Constant Failure Rate Replacement Example [has_value:: 77.758%] conditional R(120/80)
- Constant Failure Rate Replacement Example [has_value:: 160 h] inferred η, derived [confidence:: low]
- Light Bulb Example [has_value:: 72.57%] at 2,000 h whether replaced every 1,000 or 500 h (RBMM p.378)
- Weibull Example TTF 8500-16000 [has_category:: Pattern A] β ≈ 3.8, not pattern D (RBMM p.199)
- RBMM Fig 6.14 Pattern Mapping [contradicts:: RBMM Pattern Example Parameters] Fig 6.14 puts B/C/D at β ≈ 1 but example B has β = 3 (RBMM p.155-156, p.165-166)
- RBMM Pattern Example Parameters [contradicts:: RBMM Fig 6.14 Pattern Mapping] example values preferred (RBMM p.155-156)
- RBMM ch5 Infant Mortality Type D [contradicts:: RBMM ch6 Pattern Definitions] ch5 says infant mortality type D (RBMM p.148)
- RBMM ch6 Pattern Definitions [contradicts:: RBMM ch5 Infant Mortality Type D] ch6 E = infant mortality, D = random; ch6 used as primary
- Bathtub Curve [applies_to:: [[Compressor]]] whole unit is sum of many failure modes in many maintainable items
- [[AIR Abnormal Instrument Reading]] [related_to:: Pattern D] hypothesis, no β in sources [confidence:: low]
- [[SER Minor In-Service Problems]] [related_to:: Pattern E] hypothesis, no β in sources [confidence:: low]
- [[ELP External Leakage Process Medium]] [detected_by:: Condition Monitoring] may be monitored, no β in sources [confidence:: low]
- [[ELU External Leakage Utility Medium]] [detected_by:: Condition Monitoring] may be monitored, no β in sources [confidence:: low]
- [[Failure Mechanism]] [related_to:: β > 1] age-related mechanisms such as wear, fatigue
- Infant Mortality [has_cause:: Assembly Or Installation] see [[Failure Cause Codes]]
- [[Failure Patterns and Bathtub Curve]] [related_to:: [[Weibull Analysis]]]
- [[Failure Patterns and Bathtub Curve]] [related_to:: [[PM Task Selection]]]
- CMRP Wear-Out Pattern [has_value:: 2%] (CMRP CMPR-01 p.28)
- CMRP Bathtub Pattern [has_value:: 4%] (CMRP CMPR-01 p.28)
- CMRP Random Pattern [has_value:: 26%] (CMRP CMPR-01 p.28)
- CMRP Infant Mortality Pattern [has_value:: 68%] (CMRP CMPR-01 p.28)
- CMRP Random Pattern [maps_to:: Nowlan And Heap Patterns C D E] 5 + 7 + 14 = 26%, interpretation; N&H figures general knowledge [confidence:: low]
- CMRP Wear-Out Pattern [maps_to:: Pattern A] RBMM letter, interpretation; Nowlan And Heap B
- CMRP Infant Mortality Pattern [maps_to:: Pattern E] RBMM letter, interpretation; Nowlan And Heap F
- Nowlan And Heap Pattern Letters [differs_from:: RBMM Pattern Letters] N&H A = bathtub, F = infant; RBMM A = wear-out, E = infant
- Equipment Without Wear-Out Phase [has_value:: about 60%] infant and random only, unsourced (CMRP CMPR-03 p.5) [confidence:: low]
- CMRP 60 Percent No Wear-Out Claim [contradicts:: CMRP Pattern Shares 68 26 4 2] p.28 implies 94% infant + random (derived); internal CMRP inconsistency (CMRP CMPR-03 p.5 vs CMPR-01 p.28)
- [[Failure Patterns and Bathtub Curve]] [defined_in:: [[CMRP Course]]] pattern shares (CMRP CMPR-01 p.28)

---
title: PM Interval Optimization
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [pm, cost, weibull, reliability, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# PM Interval Optimization

การหาคาบ PM ที่ทำให้ total cost ต่อหน่วยเวลา (planned + unplanned) ต่ำสุด RBMM บทที่ 8 เสนอ 2 วิธี คือแก้สมการ cost per unit time ตรง ๆ และ Monte Carlo Simulation (บทที่ 12 มีตัวอย่าง bearing ที่ได้ optimum 480 วัน) จุด optimum เกิดเฉพาะ failure mode ที่ failure rate เพิ่มตามอายุ (beta มากกว่า 1) ถ้า failure rate คงที่หาจุด optimum ไม่ได้ และต้องรู้ cost ต่อครั้งของ PM กับของ failure (RBMM p.220-232)

## หลักการ (RBMM p.220-223)

- กำหนด objective ก่อน: total cost ต่ำสุด, availability สูงสุด หรือ reliability/maintainability สูงสุด
- รวมต้นทุนทางตรง (ซ่อม) และทางอ้อม (loss จากหยุดเครื่อง ทั้งตามแผนและนอกแผน)
- รูป 8.3: planned cost ลดเมื่อคาบยาวขึ้น, unplanned cost เพิ่มขึ้น, ผลรวมเป็นรูปตัว U; จุดต่ำสุดของผลรวม = optimum และไม่ใช่จุดที่ planned = unplanned เพราะไม่เป็น linear
- ทางเลือกสุดขั้ว: Zero Breakdown (คาบสั้นมาก), Optimum PM (ยอมให้ CM-Unplanned บ้าง), Run to Failure (ไม่มี PM)
- เครื่องวิกฤติระดับ A บางกรณียอมจ่ายแพงเพื่อไม่ให้เสียเลย (p.221)

## วิธีที่ 1: สูตร cost per unit time (RBMM p.223-226)

สัญลักษณ์: Cp = ต้นทุน PM ต่อครั้ง; Cf = ต้นทุน failure (CM) ต่อครั้ง; tp = คาบ PM; R(tp) = reliability ที่ tp; M(tp) = เวลาเฉลี่ยที่เสียหากเสียก่อน tp

```
C(tp) = [Cp*R(tp) + Cf*(1-R(tp))] / [tp*R(tp) + M(tp)*(1-R(tp))]
M(tp) = (integral 0..tp of t*f(t) dt) / (1 - R(tp))
=> C(tp) = [Cp*R(tp) + Cf*(1-R(tp))] / [tp*R(tp) + integral 0..tp of t*f(t) dt]
```

ตัวเศษ = ค่าใช้จ่ายคาดหวังต่อรอบ ตัวส่วน = ความยาวรอบคาดหวัง ตัวอย่างหนังสือ: beta = 3.7888, eta = 13,130 ชม., Cf = 2,070,000 บาท, Cp = 360,000 บาท (อัตราส่วน Cf/Cp = 5.75, derived) ผลจาก MathCAD (รูป 8.5): ต่ำสุดที่ราว 10 เดือน แล้วเพิ่มและราบที่ t มากกว่า 28 เดือน (กลายเป็น run-to-failure) ข้อจำกัด: สมมติ MTTR และ MWT เป็นศูนย์ จึงไม่ถูกต้องเต็มที่ (p.226)

## วิธีที่ 2: Monte Carlo Simulation (RBMM p.227-230)

ทดลองคาบ 1-30 เดือน (เพิ่มทีละ 1 เดือน) ประเมิน 3 ปี ใช้ input เดียวกัน เพิ่ม downtime planned = 6 ชม. unplanned = 10 ชม. (MTTR+MWT) ดู [[Monte Carlo Maintenance Simulation]]

ผลรูป 8.6 (หนังสือระบุว่าอ่านจากภาพเล็ก ไม่ชัด 100%) บางแถว:

| คาบ (เดือน) | นอกแผน (ครั้ง) | ตามแผน (ครั้ง) | Total cost (บาท) |
|---|---|---|---|
| 1 | - | 35.00 | 11,551,284 |
| 3 | 0.01 | 11.00 | 3,654,825 |
| 6 | 0.09 | 5.00 | 1,833,738 |
| 8 | 0.19 | 3.83 | 1,649,337 |
| 9 | 0.28 | 2.97 | 1,559,907 (ต่ำสุดในตาราง) |
| 10 | 0.33 | 2.74 | 1,591,959 |
| 11 | 0.45 | 2.57 | 1,788,117 |
| 12 | 0.60 | 1.89 | 1,861,446 |
| 18 | 1.35 | 0.60 | 2,988,174 |
| 30 | 1.74 | - | 3,608,580 |

- หนังสือสรุป optimum ประมาณ 10 เดือน แต่ค่าต่ำสุดในตารางที่อ่านได้คือเดือน 9 (1,559,907) ต่างจากเดือน 10 เพียง 32,052 บาท (derived: 1,591,959 ลบ 1,559,907) จึงเป็นเส้นโค้งแบนรอบจุดต่ำสุด; ใช้ 9-10 เดือน และเลือกตามรอบแผนงาน ประเด็นนี้เป็นความคลาดเคลื่อนเล็กน้อยในหนังสือ ไม่ได้ขัดกับ wiki ข้อมูลอื่น
- คาบยาวมาก total cost ราบที่ราว 3.6 ล้านบาท = ระดับ run-to-failure (ตรงกับกรณีฐานบทที่ 7: 3.6 ล้านบาทต่อ 3 ปี, p.200)
- ผลสรุป: เปลี่ยนตามแผนประมาณ 3 ครั้งต่อ 3 ปี ต้องการอะไหล่ราว 1 ชิ้น (p.229)
- Item Age เทียบ System Age (รูป 8.8): Item Age (นับอายุชิ้นส่วน เปลี่ยนเมื่อครบหรือเสียแล้วนับใหม่) โดยทั่วไปดีกว่า System Age (เปลี่ยนตามอายุระบบ ชิ้นที่เพิ่งเปลี่ยนจะถูกเปลี่ยนซ้ำเมื่อครบคาบ) แต่ตัวอย่างนี้ต่างกันน้อย optimum ราว 10 เดือนเท่ากัน; System Age ที่คาบเกิน 18 เดือน ยังมีงาน planned เหลือ

## ตัวอย่างบทที่ 12: bearing ของ motor (RBMM p.391-392)

ข้อมูลประวัติ 5 เหตุการณ์ Weibull ได้ beta = 3.5 (3.5008 จาก Y Regression), eta = 996.7 วัน (หนังสือสรุป 996.69) Cp = 248,703.64 บาท, Cu = 1,118,558.88 บาท (Cu/Cp = 4.50, derived)

```
Cost per unit time = [Cu*F(tp) + Cp*R(tp)] / [tp*R(tp) + integral 0..tp of t*f(t) dt]
```

| tp (วัน) | 30 | 120 | 240 | 360 | 450 | 480 | 510 | 600 | 750 |
|---|---|---|---|---|---|---|---|---|---|
| Cost/unit time | 8,290.27 | 2,077.48 | 1,065.41 | 773.74 | 701.08 | 694.15 | 694.54 | 736.64 | 948.37 |

- ต่ำสุดที่ 480 วัน (694.15) ประมาณ 16 เดือน ในทางปฏิบัติปรับเป็น 12 หรือ 18 เดือนตามแผนงาน เพราะเส้นแบนรอบจุดต่ำสุด (480 ใกล้ 510: ต่างเพียง 0.39)
- ตรวจ: ที่ tp = 30 ค่า 8,290.27 เท่ากับ Cp/tp = 248,703.64/30 ได้ 8,290.12 โดยประมาณ (derived; R(30) ใกล้ 1)
- หนังสือพิมพ์ตัวส่วนเป็น integral จาก tp ถึง infinity (หนังสือพิมพ์ผิด); ทฤษฎี age replacement และสูตรบทที่ 8 ใช้ integral จาก 0 ถึง tp หน้านี้ใช้รูปหลัง (confidence medium) ไม่ถือเป็น source conflict ของ wiki
- ตัวเลขตาราง 480 วันเป็นค่าที่หนังสือคำนวณ ไม่ได้ตรวจคำนวณซ้ำ

## เมื่อใช้ไม่ได้ผล (RBMM p.231-232)

1. ทำไม่ได้กับทุก failure mode
2. pattern B, C, D (failure rate คงที่/ค่อนข้างคงที่) optimize ไม่ได้ ดู [[Failure Patterns and Bathtub Curve]]
3. สัดส่วน unplanned ต่อ planned cost ต่ำหรือต่างกันน้อย การปรับคาบไม่ส่งผล; งาน in-house ที่เป็น fixed cost จะกระทบแค่ utilization
4. ระบบที่มี redundancy ต้องวิเคราะห์ระดับระบบ ดู [[Redundancy and Standby Systems]]
5. ต้องมี cost ต่อครั้ง, MTTR/MWT, failure mode, failure date ที่ถูกต้องใน CMMS (p.229) ดู [[CMMS]]

จุดเริ่มต้นที่สำคัญกว่าคือกลยุทธ์ตามความวิกฤติ (p.232) และการตั้งงบตามผลวิเคราะห์ ดู [[Maintenance Budget]]

## เชื่อมโยงกับ compressor failure hierarchy

- คาบหาเป็นราย failure mode ต่อ component ไม่ใช่ราย compressor ตรงกับระดับ [[Failure Mode]] ของ [[ISO 14224]]
- [[OREDA]] ให้ failure rate คงที่ระดับ item จึงหา tp ไม่ได้ ต้องใช้ beta/eta จากประวัติซ่อม site-specific (RBMM p.223, p.231)
- ตัวอย่าง bearing ในหนังสือเป็นของ motor ไม่ใช่ compressor; ใช้เป็นตัวอย่างวิธีการเท่านั้น

## ดูเพิ่ม

- [[PM Task Selection]]
- [[Monte Carlo Maintenance Simulation]]
- [[Weibull Analysis]]
- [[Maintenance Cost Structure]]
- [[Spare Parts Management]]

## Triplets

- [[PM Interval Optimization]] [produces:: Optimum PM Interval] minimum total cost per unit time, planned + unplanned (RBMM p.220-232)
- [[PM Interval Optimization]] [uses:: Cost per Unit Time] method 1, direct formula (RBMM p.223-226)
- [[PM Interval Optimization]] [uses:: [[Monte Carlo Maintenance Simulation]]] method 2 (RBMM p.227-230)
- [[PM Interval Optimization]] [applies_to:: Wear-Out Failure] optimum exists only when failure rate rises with age, beta > 1
- [[PM Interval Optimization]] [depends_on:: Shape Parameter Beta] constant rate gives no optimum; patterns B, C, D cannot be optimized (RBMM p.231-232)
- [[PM Interval Optimization]] [depends_on:: Objective] minimum total cost, maximum availability, or maximum reliability/maintainability (RBMM p.220-223)
- [[PM Interval Optimization]] [depends_on:: Indirect Cost] direct repair plus downtime losses, planned and unplanned (RBMM p.220-223)
- Optimum PM Interval [differs_from:: Planned Equals Unplanned Point] total cost is U-shaped and nonlinear (Fig 8.3)
- [[PM Interval Optimization]] [selects:: Zero Breakdown] extreme option, very short interval (RBMM p.220-223)
- [[PM Interval Optimization]] [selects:: Optimum PM] accepts some CM-Unplanned (RBMM p.220-223)
- [[PM Interval Optimization]] [selects:: Run to Failure] no PM (RBMM p.220-223)
- Criticality A [uses:: Zero Breakdown] some cases accept high cost to avoid any failure (RBMM p.221)
- Cost per Unit Time [has_formula:: C(tp) = (Cp*R(tp) + Cf*(1-R(tp))) / (tp*R(tp) + M(tp)*(1-R(tp)))] page uses square brackets (RBMM p.223-226)
- Cost per Unit Time [has_formula:: C(tp) = (Cp*R(tp) + Cf*(1-R(tp))) / (tp*R(tp) + integral 0..tp of t*f(t) dt)] page uses square brackets (RBMM p.223-226)
- M(tp) [has_formula:: (integral 0..tp of t*f(t) dt) / (1 - R(tp))] mean time to failure if failing before tp (RBMM p.223-226)
- Cost per Unit Time [has_parameter:: Cp] PM cost per event
- Cost per Unit Time [has_parameter:: Cf] failure (CM) cost per event
- Cost per Unit Time [has_parameter:: tp] PM interval
- Cost per Unit Time [has_parameter:: R(tp)] reliability at tp
- Cost per Unit Time [has_parameter:: M(tp)] mean failure time if failing before tp
- Cost per Unit Time [depends_on:: Mean Time To Repair] limitation: assumes MTTR and MWT zero (RBMM p.226)
- Optimum PM Interval [has_value:: about 10 months] method 1 MathCAD; beta 3.7888, eta 13,130 h, Cf 2,070,000, Cp 360,000 baht; flat beyond 28 months = run-to-failure (Fig 8.5, RBMM p.223-226)
- Cf/Cp Ratio [has_value:: 5.75] method 1 example, derived
- Monte Carlo PM Example [has_parameter:: Downtime] planned 6 h, unplanned 10 h (MTTR+MWT); intervals 1-30 months over 3 years (RBMM p.227-230)
- Optimum PM Interval [has_value:: about 10 months] book conclusion from Monte Carlo (Fig 8.6, RBMM p.227-230)
- Optimum PM Interval [has_value:: 9 months] lowest readable table value 1,559,907 baht; only 32,052 below month 10, derived; flat curve, use 9-10 months (Fig 8.6)
- Run to Failure [has_value:: about 3.6 million baht] total cost plateau over 3 years at long intervals (RBMM p.200, Fig 8.6)
- Optimum PM Interval [has_value:: about 3 replacements per 3 years] needs about 1 spare (RBMM p.229)
- Item Age [differs_from:: System Age] Item Age generally better; small difference here, both about 10 months (Fig 8.8)
- Cost per Unit Time [has_formula:: (Cu*F(tp) + Cp*R(tp)) / (tp*R(tp) + integral 0..tp of t*f(t) dt)] chapter 12 form; book misprints integral tp..infinity (RBMM p.391-392)
- Optimum PM Interval [has_value:: 480 days] motor bearing, cost 694.15 per unit time, about 16 months; adjust to 12 or 18 months (RBMM p.391-392)
- Motor Bearing Example [has_value:: 3.5] Weibull beta (3.5008 Y regression), eta 996.7 days, Cp 248,703.64, Cu 1,118,558.88 baht (RBMM p.391-392)
- Cu/Cp Ratio [has_value:: 4.50] motor bearing example, derived
- [[PM Interval Optimization]] [applies_to:: [[Failure Mode]]] per failure mode per component, not per compressor; not all failure modes (RBMM p.231-232)
- [[PM Interval Optimization]] [depends_on:: Cost Ratio] low or similar unplanned/planned cost ratio makes interval change ineffective (RBMM p.231-232)
- [[PM Interval Optimization]] [depends_on:: [[Redundancy and Standby Systems]]] redundant systems need system-level analysis (RBMM p.231-232)
- [[PM Interval Optimization]] [depends_on:: [[CMMS]]] needs cost per event, MTTR/MWT, failure mode, failure date (RBMM p.229)
- [[PM Interval Optimization]] [depends_on:: [[Criticality Assessment]]] criticality-based strategy is the more important starting point (RBMM p.232)
- [[PM Interval Optimization]] [depends_on:: Site-Specific History] OREDA constant rate cannot give tp; need beta/eta from site repair history (RBMM p.223, p.231)

---
title: Reliability Based Maintenance Management Book
created: 2026-10-21
updated: 2026-10-22
type: entity
tags: [book, maintenance-management, reliability]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Reliability Based Maintenance Management (RBMM) — หนังสือ

hub ของหนังสือ "การจัดการงานบำรุงรักษาด้วย Reliability" ที่ ingest เข้า wiki เมื่อ 2026-10-21 หนังสือสอนระบบบริหารงานบำรุงรักษาตั้งแต่ CMMS, RCM/FMECA, การวิเคราะห์ข้อมูลการเสียด้วย Weibull, การเลือกและ optimize งาน PM, อะไหล่ตามความเสี่ยง จนถึงงบประมาณ รายงานเชิงกลยุทธ์ และธุรกิจบำรุงรักษา ตัวหนังสือไม่ใช่ข้อมูล compressor โดยตรง แต่ให้กรอบวิธีคิดที่เชื่อมกับ failure hierarchy ใน wiki นี้ (ดูหัวข้อสุดท้าย) ข้อมูลทั้งหมดมาจาก reading notes ที่สรุปความจากภาพสแกน ไม่ใช่ข้อความต้นฉบับ

## ข้อมูลบรรณานุกรม

- ชื่อ: การจัดการงานบำรุงรักษาด้วย Reliability (Reliability Based Maintenance Management)
- ผู้แต่ง: วัฒนา เชียงกูล, เกรียงไกร ดำรงรัตน์, ดลดิษฐ์ เมืองแมน
- สำนักพิมพ์: SE-Education (SE-ED), พ.ศ. 2553 (2010), ISBN 978-616-08-0207-4, 400 หน้า
- ชุด Industrial Management & Technical Series เล่มที่ 3 หมวดบริหารงานบำรุงรักษา
- Raw source: [[raw/reliability-based-maintenance-management]] (PDF สแกน 401 หน้า ไม่มี text layer; book page = PDF page - 2; sha256 `cbda58a3...b4f49f`) และ notes ต่อบทใน `raw/reliability-based-maintenance-management/`
- ข้อควรรู้: ตัวเลขอ่านจากภาพ บางจุดเบลอ/อ่านไม่ออก ถูก flag ไว้ในแต่ละหน้า

## กรอบแนวคิดของหนังสือ

```
CMMS (ข้อมูล + กระบวนการ)
  -> RCM / FMECA (เลือกเครื่อง, function, failure mode, criticality)
  -> วิเคราะห์ข้อมูลการเสีย (Weibull, Reliability metrics, RBD)
  -> เลือกประเภทงาน PM ต่อ failure mode
  -> optimize คาบ PM (cost ต่อหน่วยเวลาต่ำสุด, Monte Carlo)
  -> อะไหล่ตามความเสี่ยง (criticality, EOQ, safety stock)
  -> งบประมาณบำรุงรักษา (Top Down / Bottom Up, Cost/Loss control)
  -> รายงานเชิงกลยุทธ์ (KPI, variance)
  -> ธุรกิจบำรุงรักษา (Cost center / Profit center / Service company)
```

เป้าหมายกลางคือ Zero Plant Breakdown @ Minimum Cost โดยแยกกลยุทธ์ตาม criticality A/B/C ([[Asset Life Cycle]], [[Criticality Assessment]])

## 12 บท

| บท | หัวข้อ (หน้า) | สรุป | หน้าใน wiki |
|---|---|---|---|
| 1 | วงจรชีวิตและการบำรุงรักษาเครื่องจักร (p.13-30) | วงจรชีวิต asset, 4 กลุ่มงานบำรุงรักษา, criticality A/B/C และกลยุทธ์ต่อระดับ | [[Asset Life Cycle]], [[Criticality Assessment]], [[Availability and OEE]] |
| 2 | วงจรพัฒนาสมรรถนะหน่วยงานบำรุงรักษา (p.31-54) | พีระมิด 6 ชั้นจาก Reactive ถึง Optimization และการประเมินตนเอง 16 หัวข้อ | [[Maintenance Efficacy Pyramid]], [[Maintenance KPIs]] |
| 3 | รายงานเชิงกลยุทธ์ (p.55-88) | รายงาน A4 ส่วน A-E, ต้นไม้ KPI และการตรวจเลข variance | [[Maintenance Strategic Report]], [[Maintenance KPIs]], [[Availability and OEE]] |
| 4 | CMMS (p.89-112) | 10 โมดูล, Asset Register, Process vs Content, ฟิลด์ใน Work Order และกฎห้ามปิดงานถ้าไม่ระบุ Failure Mode | [[CMMS]], [[Failure Data Recording]] |
| 5 | RCM และ FMECA (p.113-152) | RCM แบบ Nowlan-Heap, RPN, criticality เชิงปริมาณ, รหัส ISO 14224 ของ pump/motor, bathtub curve | [[RCM Reliability Centered Maintenance]], [[FMECA]], [[Criticality Assessment]], [[Failure Data Recording]], [[Failure Patterns and Bathtub Curve]] |
| 6 | วิเคราะห์ข้อมูลการเสีย (p.153-178) | Weibull (β, η), pattern A-E, F(t)/R(t)/λ(t), MTTF, censored data, RBD | [[Weibull Analysis]], [[Failure Patterns and Bathtub Curve]], [[Reliability Metrics]], [[Censored Data]], [[Reliability Block Diagram]] |
| 7 | วิเคราะห์และคัดเลือกงาน PM (p.179-218) | ผังเลือกงาน Nowlan-Heap/SAE JA1012, เลือกตาม β, Condition Monitoring, P-F, Failure Finding, redundancy | [[PM Task Selection]], [[P-F Interval and Condition Monitoring]], [[Failure Finding Interval]], [[Redundancy and Standby Systems]] |
| 8 | จัดการ PM ตามแผนให้ได้ประโยชน์สูงสุด (p.219-232) | หาคาบ PM ที่ cost ต่อหน่วยเวลาต่ำสุด และ Monte Carlo simulation | [[PM Interval Optimization]], [[Monte Carlo Maintenance Simulation]] |
| 9 | ลดและจัดอะไหล่คงคลัง (p.233-272) | Stock vs ซื้อตรง, ABC และ criticality ของอะไหล่, EOQ/ROP/Safety Stock, forecast demand | [[Spare Parts Management]], [[Spare Part Criticality and Risk]], [[EOQ and Reorder Point]], [[Spare Part Demand Forecasting]] |
| 10 | บริหารงบประมาณบำรุงรักษา (p.273-320) | กรอบ Gross -> สำรอง -> Net Budget, Cost vs Loss Control, งบตาม criticality, Cost Structure | [[Maintenance Budget]], [[Maintenance Cost Structure]], [[Maintenance Strategic Report]] |
| 11 | ธุรกิจบำรุงรักษา (p.321-360) | เปรียบเทียบ Cost Center / Profit Centered / Service Company, Job Order Costing | [[Maintenance Business Models]], [[Job Order Costing]], [[Maintenance Cost Structure]] |
| 12 | สถิติพื้นฐานสำหรับงานบำรุงรักษา (p.361-392) | Poisson, Normal, Exponential, Weibull กับตัวอย่างอะไหล่/PM, ตัวอย่าง bearing | [[Statistical Distributions for Maintenance]], [[Weibull Analysis]], [[Censored Data]], [[PM Interval Optimization]] |

## ข้อผิดพลาด/ข้อควรระวังในหนังสือ

เป็นข้อผิดพลาดภายในหนังสือ (ไม่ใช่ความขัดแย้งกับ OREDA) แต่ละหน้ามีรายละเอียดและค่าที่ถูกต้อง ตัวเลข "ที่ถูก" ส่วนใหญ่เป็น derived (คำนวณใหม่โดยผู้เขียน wiki)

| หัวข้อ | ค่าที่หนังสือพิมพ์ | ค่าที่ถูกต้อง / หมายเหตุ | หน้า |
|---|---|---|---|
| T(R) สำหรับ Weibull (p.169) | สูตร eta x [1 - ln R]^(1/beta) ให้ 13,847.81 ชม. ที่ R = 0.8 | สูตรที่ถูก eta x (-ln R)^(1/beta) ให้ ประมาณ 8,837 ชม. (derived) | [[Reliability Metrics]], [[Weibull Analysis]] |
| Parallel RBD (Fig 6.22) | 0.9085 | 0.985 | [[Reliability Block Diagram]] |
| Series RBD (Fig 6.21) | ข้อความ 0.9/0.9 แต่คำนวณ 0.85 x 0.9 | 0.765 ตามที่คำนวณ | [[Reliability Block Diagram]] |
| MTTF integral (p.168) | ขอบเขต -inf ถึง inf | ควรเป็น 0 ถึง inf (11,865.51 ชม. = eta x Gamma(1+1/beta) ใช้ได้) | [[Reliability Metrics]] |
| สูตร cost ต่อหน่วยเวลา (p.391) | ตัวส่วน integral จาก tp ถึง inf | ควรเป็น 0 ถึง tp | [[PM Interval Optimization]], [[Statistical Distributions for Maintenance]] |
| ส่วนเบี่ยงเบนมาตรฐาน sigma (p.374) | สลับกฎ N กับ N-1 | ตัวอย่างใช้ N-1 ได้ sigma = 101.486 | [[Statistical Distributions for Maintenance]] |
| EOQ (p.253) | พจน์ Q/2 x Cp | ควรเป็น A/Q x Cp (Cp ในบท 9 ไม่เท่ากับ Cp ในบท 8) | [[EOQ and Reorder Point]] |
| Job Order Costing (p.357) | (3,300) | ควรเป็น (33,000); รายการ (9) พิมพ์ (6)-(2) คงตามที่พิมพ์ | [[Job Order Costing]] |
| ABC Analysis (p.242 vs Fig 9.4) | ข้อความกับป้ายในรูปไม่ตรงกัน | ไม่ resolve | [[Spare Part Criticality and Risk]] |
| Section E (ch3 Fig 3.19 vs ch10 Fig 10.27) | E15/E16 ไม่ตรงกัน (ch3 E16 total -3.58% vs ch10 6.42%) | ใช้ ch10 ซึ่งตรงกับข้อความ 2.97% + 3.45%; ch3 น่าจะพิมพ์ผิด/อ่านผิด | [[Maintenance Strategic Report]], [[Maintenance Budget]] |
| A3.1 Actual | p.64 อ่านได้ 320,000, p.66 และ ch10 ได้ 520,000 | ใช้ 520,000 | [[Maintenance Strategic Report]] |
| คาบ PM optimum (ch8) | ข้อความ ประมาณ 10 เดือน | ตาราง Fig 8.6 ต่ำสุดที่เดือน 9 (1,559,907 vs 1,591,959) | [[PM Interval Optimization]] |
| Pattern/β (ch5, ch6, ch7, ch12) | B/C/D β ประมาณ 1 ใน Fig 6.14 แต่ B β = 3; "Infant Mortality แบบ D"; 6 pattern vs 5 | ใช้ตัวเลขตัวอย่างและนิยามของ ch6 | [[Failure Patterns and Bathtub Curve]] |
| อื่น ๆ | Fig 9.19 Cost Ratio, Fig 9.20 (4/2 vs 6/4), Fig 10.20 vs 10.18, สัดส่วนอะไหล่ >half vs >60-70%, holding cost 15-20% vs 15-25% | เป็นความไม่สอดคล้องหรืออ่านจากภาพเบลอ ดูหน้าที่เกี่ยวข้อง | [[Spare Parts Management]], [[EOQ and Reorder Point]], [[Job Order Costing]] |

ข้อสังเกตเชิงขอบเขต: ไม่มี IEC 61508/SIL และไม่มีข้อมูล P-F หรือ β ของ compressor ในหนังสือ

## ความสัมพันธ์กับ compressor failure hierarchy ของ wiki นี้

ส่วนนี้เป็นการตีความของ wiki ไม่ใช่ข้อความในหนังสือ ยกเว้นข้อ 1 และ 3

1. **รหัส failure mode ISO 14224 (RBMM p.132-134, Fig 5.14-5.17)**: รายการของ pump 19 รหัส ตรงกับ [[Failure Mode]] 18 จาก 19 รหัส ต่างเฉพาะ SPS (หนังสือ) กับ UST (wiki) ซึ่ง resolve แล้ว: ใช้ UST หลัก SPS เป็น alias ส่วน motor มี OWD เพิ่ม ดู [[ISO 14224]], [[Failure Data Recording]], [[UST Spurious Stop]]
2. **Object Part ใกล้เคียง Maintainable Item** (การตีความ): record ขั้นต่ำ 5 รายการของหนังสือ (Equipment, Damage Code, Object Part, Cause, Action) เทียบได้กับ Equipment, [[Failure Mode]], [[Maintainable Item]], [[Failure Cause Codes]] / [[Failure Mechanism]], [[Resolution Codes]] ตามลำดับ ดูตารางที่ [[RBMM Concepts vs Compressor Failure Hierarchy]]
3. **ฟิลด์ข้อมูลการเสีย**: หนังสือกำหนดฟิลด์ใน Work Order (Failure Mode, Cause, Effect, Down Time, Work Time, Man Hours, อะไหล่) ที่จำเป็นต่อ [[Weibull Analysis]] และ [[Reliability Metrics]] ซึ่ง OREDA % ใน wiki นี้ไม่มี (ไม่มี time-to-failure) ดู [[Failure Data Recording]], [[CMMS]]
4. **ใช้ต่อกับ compressor**: เลือกงาน PM ราย failure mode ด้วย [[PM Task Selection]] และ [[Criticality Assessment]] ดูขั้นตอนที่ [[How to choose PM task for a compressor failure mode]]
5. **ข้อจำกัด**: wiki ไม่มีข้อมูล failure จริงของ asset Valeura, β, P-F หรือราคาอะไหล่ ตัวอย่างของหนังสือเป็นข้อมูลทั่วไป ไม่ใช่ compressor

## ดูเพิ่ม

- [[Failure Hierarchy]]
- [[Compressor]]
- [[OREDA]]
- [[ISO 14224]]

## Triplets

- RBMM [alias_of:: [[Reliability Based Maintenance Management Book]]]
- การจัดการงานบำรุงรักษาด้วย Reliability [alias_of:: [[Reliability Based Maintenance Management Book]]] Thai title
- [[Reliability Based Maintenance Management Book]] [related_to:: วัฒนา เชียงกูล] author
- [[Reliability Based Maintenance Management Book]] [related_to:: เกรียงไกร ดำรงรัตน์] author
- [[Reliability Based Maintenance Management Book]] [related_to:: ดลดิษฐ์ เมืองแมน] author
- [[Reliability Based Maintenance Management Book]] [related_to:: SE-Education] publisher (SE-ED)
- [[Reliability Based Maintenance Management Book]] [has_value:: 2010] publication year, B.E. 2553
- [[Reliability Based Maintenance Management Book]] [has_code:: ISBN 978-616-08-0207-4]
- [[Reliability Based Maintenance Management Book]] [has_value:: 400] pages
- [[Reliability Based Maintenance Management Book]] [has_category:: Industrial Management & Technical Series] vol. 3, maintenance management
- [[Reliability Based Maintenance Management Book]] [has_value:: 401] pages of scanned PDF, no text layer
- [[Reliability Based Maintenance Management Book]] [has_formula:: book page = PDF page - 2]
- [[Reliability Based Maintenance Management Book]] [has_value:: 12] chapters
- RBMM Maintenance Management Framework [defined_in:: [[Reliability Based Maintenance Management Book]]] goal Zero Plant Breakdown @ Minimum Cost, strategy by criticality A/B/C
- [[CMMS]] [step_of:: RBMM Maintenance Management Framework] step 1
- [[RCM Reliability Centered Maintenance]] [step_of:: RBMM Maintenance Management Framework] step 2
- [[FMECA]] [step_of:: RBMM Maintenance Management Framework] step 3
- [[Weibull Analysis]] [step_of:: RBMM Maintenance Management Framework] step 4
- [[PM Task Selection]] [step_of:: RBMM Maintenance Management Framework] step 5
- [[PM Interval Optimization]] [step_of:: RBMM Maintenance Management Framework] step 6
- [[Spare Parts Management]] [step_of:: RBMM Maintenance Management Framework] step 7
- [[Maintenance Budget]] [step_of:: RBMM Maintenance Management Framework] step 8
- [[Maintenance Strategic Report]] [step_of:: RBMM Maintenance Management Framework] step 9
- [[Maintenance Business Models]] [step_of:: RBMM Maintenance Management Framework] step 10
- [[Asset Life Cycle]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.1 (p.13-30)
- [[Criticality Assessment]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.1 (p.13-30)
- [[Availability and OEE]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.1 (p.13-30)
- [[Maintenance Efficacy Pyramid]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.2 (p.31-54)
- [[Maintenance KPIs]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.2 (p.31-54)
- [[Maintenance Strategic Report]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.3 (p.55-88)
- [[Maintenance KPIs]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.3 (p.55-88)
- [[Availability and OEE]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.3 (p.55-88)
- [[CMMS]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.4 (p.89-112)
- [[Failure Data Recording]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.4 (p.89-112)
- [[RCM Reliability Centered Maintenance]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.5 (p.113-152)
- [[FMECA]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.5 (p.113-152)
- [[Criticality Assessment]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.5 (p.113-152)
- [[Failure Data Recording]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.5 (p.113-152)
- [[Failure Patterns and Bathtub Curve]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.5 (p.113-152)
- [[Weibull Analysis]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.6 (p.153-178)
- [[Failure Patterns and Bathtub Curve]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.6 (p.153-178)
- [[Reliability Metrics]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.6 (p.153-178)
- [[Censored Data]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.6 (p.153-178)
- [[Reliability Block Diagram]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.6 (p.153-178)
- [[PM Task Selection]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.7 (p.179-218)
- [[P-F Interval and Condition Monitoring]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.7 (p.179-218)
- [[Failure Finding Interval]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.7 (p.179-218)
- [[Redundancy and Standby Systems]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.7 (p.179-218)
- [[PM Interval Optimization]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.8 (p.219-232)
- [[Monte Carlo Maintenance Simulation]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.8 (p.219-232)
- [[Spare Parts Management]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.9 (p.233-272)
- [[Spare Part Criticality and Risk]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.9 (p.233-272)
- [[EOQ and Reorder Point]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.9 (p.233-272)
- [[Spare Part Demand Forecasting]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.9 (p.233-272)
- [[Maintenance Budget]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.10 (p.273-320)
- [[Maintenance Cost Structure]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.10 (p.273-320)
- [[Maintenance Strategic Report]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.10 (p.273-320)
- [[Maintenance Business Models]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.11 (p.321-360)
- [[Job Order Costing]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.11 (p.321-360)
- [[Maintenance Cost Structure]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.11 (p.321-360)
- [[Statistical Distributions for Maintenance]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.12 (p.361-392)
- [[Weibull Analysis]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.12 (p.361-392)
- [[Censored Data]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.12 (p.361-392)
- [[PM Interval Optimization]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.12 (p.361-392)
- [[Reliability Metrics]] [has_value:: about 8,837 h] T(R) at R = 0.8 with correct formula eta x (-ln R)^(1/beta) (derived); book p.169 prints 13,847.81 h
- [[Reliability Metrics]] [has_value:: 11,865.51 h] MTTF = eta x Gamma(1+1/beta); book p.168 integral limits -inf to inf should be 0 to inf
- [[Reliability Block Diagram]] [has_value:: 0.985] parallel example Fig 6.22; book prints 0.9085
- [[Reliability Block Diagram]] [has_value:: 0.765] series example Fig 6.21 as calculated 0.85 x 0.9; text says 0.9/0.9
- [[PM Interval Optimization]] [has_formula:: cost per unit time denominator integral from 0 to tp] book p.391 prints tp to inf
- [[Statistical Distributions for Maintenance]] [has_value:: 101.486] sigma using N-1; book p.374 swaps N and N-1 rules
- [[EOQ and Reorder Point]] [has_formula:: A/Q x Cp] ordering cost term; book p.253 prints Q/2 x Cp; Cp in ch.9 differs from Cp in ch.8
- [[Job Order Costing]] [has_value:: (33,000)] book p.357 prints (3,300)
- ABC Analysis RBMM Text p.242 [contradicts:: ABC Analysis RBMM Fig 9.4] text vs figure labels, unresolved
- ABC Analysis RBMM Fig 9.4 [contradicts:: ABC Analysis RBMM Text p.242] figure labels vs text, unresolved
- [[Maintenance Strategic Report]] [has_value:: 6.42%] Section E16 total per ch.10 Fig 10.27 (used, matches 2.97% + 3.45%); ch.3 Fig 3.19 shows -3.58%, likely misprint
- [[Maintenance Strategic Report]] [has_value:: 520,000] A3.1 Actual (used, p.66 and ch.10); p.64 reads 320,000
- [[PM Interval Optimization]] [has_value:: 9 months] optimum PM interval, Fig 8.6 minimum (1,559,907 vs 1,591,959); text says about 10 months
- [[Failure Patterns and Bathtub Curve]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ch.6 numbers and definitions used; ch.5/6/7/12 inconsistent on pattern/beta
- [[Failure Mode]] [defined_in:: [[Reliability Based Maintenance Management Book]]] ISO 14224 pump code list p.132-134, Fig 5.14-5.17; 18 of 19 codes match wiki
- SPS [alias_of:: [[UST Spurious Stop]]] SPS in book, UST in wiki (resolved: UST primary)
- Motor [has_failure_mode:: OWD] additional code vs pump list (RBMM)
- Equipment [part_of:: RBMM Minimum Failure Record] 1 of 5 fields
- Damage Code [part_of:: RBMM Minimum Failure Record] 1 of 5 fields
- Object Part [part_of:: RBMM Minimum Failure Record] 1 of 5 fields (RBMM p.151-152)
- Cause [part_of:: RBMM Minimum Failure Record] 1 of 5 fields
- Action [part_of:: RBMM Minimum Failure Record] 1 of 5 fields
- Damage Code [maps_to:: [[Failure Mode]]] interpretation [confidence:: low]
- Object Part [maps_to:: [[Maintainable Item]]] interpretation, book makes no direct mapping [confidence:: low]
- Cause [maps_to:: [[Failure Cause Codes]]] interpretation [confidence:: low]
- Cause [maps_to:: [[Failure Mechanism]]] interpretation [confidence:: low]
- Action [maps_to:: [[Resolution Codes]]] interpretation [confidence:: low]
- Work Order Failure Fields [input_to:: [[Weibull Analysis]]] Failure Mode, Cause, Effect, Down Time, Work Time, Man Hours, spare parts
- Work Order Failure Fields [input_to:: [[Reliability Metrics]]] OREDA % in wiki has no time-to-failure
- Work Order Failure Fields [part_of:: [[CMMS]]]
- [[PM Task Selection]] [applies_to:: [[Compressor]]] per failure mode (interpretation) [confidence:: low]

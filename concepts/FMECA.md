---
title: FMECA
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [fmeca, criticality, rcm, reliability, statistics, book]
sources: [reliability-based-maintenance-management.md]
confidence: high
contested: false
---

# FMECA (Failure Mode Effect Criticality Analysis)

**FMECA** ประเมินผลของ Failure Mode ตั้งแต่ระดับ Equipment ลงไปถึง Component/Part เพื่อจัดลำดับว่า FM ใดสำคัญก่อน เป็นกระบวนการอิสระที่เกิดจากฝั่งออกแบบ/ผลิต ไม่ใช่ส่วนหนึ่งของ [[RCM Reliability Centered Maintenance]] แต่ RCM เลือกใช้ FMECA database ที่มีอยู่ได้ (RBMM p.137) RBMM บท 5 เสนอ 2 วิธี: **Qualitative** (S x O x D = RPN ใช้เมื่อไม่มี failure rate ต่อ FM) และ **Quantitative** (คำนวณ criticality จากความน่าจะเป็นที่เวลา t) ตัวเลขทุกตารางในบทเป็นความเห็นผู้ประเมิน ปรับตามมาตรฐาน FMECA อื่นได้ (RBMM p.139-140)

## ความต่างจาก RCM (RBMM p.137)

- RCM ดู Function ของกรอบ (Productive Unit) ที่ประกอบด้วย equipment หลายตัว
- FMECA ดูระดับ equipment ว่าเสียอย่างไร (เช่น มอเตอร์หมุนไม่ได้) โดยไม่ดูผลต่อกรอบใหญ่
- Fig 5.23 (p.144) เพิ่มคอลัมน์ FMECA เป็น "Optional FMECA Process" ในตาราง RCM A4 เดียวกัน ใช้ beta/eta ชุดเดียวกัน (4.352/6 ปี; 3.876/2.35 ปี; 0.997/10.5 ปี)

## Qualitative FMECA: RPN (RBMM p.138-140)

```
RPN = Severity (S) x Occurrence (O) x Detect-ability (D)
```

Occurrence (Fig 5.19, Mil-Std-1629):

| Rank | เกณฑ์ | อัตรา |
|---|---|---|
| 1 | ไม่น่าเกิด (Extremely Unlikely) | ไม่ระบุในบันทึก |
| 2 | ค่อนข้างน้อย (Remote) | 1/10,000 |
| 3 | เกิดได้บางครั้ง (Occasional) | 1/1,000 |
| 4 | น่าจะเกิดได้ (Reasonably Probable) | 1/100 |
| 5 | เกิดบ่อย (Frequent) | 1/10 (cycles, hrs ฯลฯ) |

Severity (Fig 5.20): 1 Minor ไม่มีผล; 2 Marginal ผลไม่มากไม่ทำให้ระบบเสีย; 3 Moderate รุนแรงปานกลาง อาจทำระบบเสียหาย; 4 Critical ทำระบบเสียหายมาก; 5 Catastrophic สูญเสียชีวิตได้

Detection (Fig 5.21) คะแนนสูง = ตรวจจับยาก = แย่:

| Rank | โอกาสตรวจพบล่วงหน้า |
|---|---|
| 1 สูงมาก | 80-100% |
| 2 สูง | 60-80% |
| 3 ปานกลาง | 40-60% |
| 4 ต่ำ | 20-40% |
| 5 น้อยมาก | 0-20% |

ตัวอย่าง (p.140): O = 4, S = 3, D = 2 -> RPN = 4 x 3 x 2 = 24 (ตรวจเลขแล้วถูกต้อง)

หมายเหตุ: ช่วง max ของ RPN = 5 x 5 x 5 = 125 (derived จากสเกลสูงสุดของทั้งสามตาราง หนังสือไม่ได้ระบุ) และหนังสือไม่ให้เกณฑ์ RPN ที่ยอมรับได้ ให้บริษัทกำหนดเอง

การทบทวน RPN: ทีมบำรุงรักษา ฝ่ายผลิต Safety และสิ่งแวดล้อมร่วมกัน ทบทวนตลอดเวลา ถ้าเกินเกณฑ์ต้องมี action แก้ไข ประเมินใหม่ และบันทึกติดตาม RPN เป็นความเห็น ควรใช้ข้อมูลตัวเลขจริงจากวิศวกรรมเป็นหลัก (p.140)

## Quantitative Criticality (RBMM p.141-143)

Tree (Fig 5.22): Item -> Function -> Functional Failure -> Failure Mode FM ภายใต้ functional failure เดียวกันเป็น OR logic (ต่อขนานใน failure tree)

```
FF(t)   = 1 - Product(1 - Fm_i(t))        ความน่าจะเป็นของ functional failure
FFCr(t) = FF(t) x S x MR                  Functional Failure Criticality
Cr(t)   = Sum of FFCr(t)                  Item Criticality
```

- S = Severity ขนาดความเสียหาย 0-1; MR = Failure Mode Ratio สัดส่วนของ functional failure ต่อทั้ง Item (รวมทุกอัน = 1)

ตัวอย่าง (p.141-143): Item มี 2 Function ค่า Fm(t): FM1.1.1=0.2, FM1.1.2=0.4, FM1.1.3=0.3, FM1.2.1=0.6, FM1.2.2=0.7, FM2.1=0.6

| Functional Failure | คำนวณ FF | S | MR | FFCr |
|---|---|---|---|---|
| FF1 (Function 1) | 1 - (0.8)(0.6)(0.7) = 0.664 | 1.0 | 0.6 | 0.664 x 1.0 x 0.6 = 0.3984 |
| FF2 (Function 1) | 1 - (0.4)(0.3) = 0.88 | 0.75 | 0.2 | 0.88 x 0.75 x 0.2 = 0.132 |
| Function 2 | 0.6 (FM2.1 เดี่ยว) | 0.5 | 0.2 | 0.6 x 0.5 x 0.2 = 0.06 |

- Function 1: Cr1 = 0.3984 + 0.132 = 0.5304; Function 2: Cr2 = 0.06 -> Function 1 วิกฤติกว่า
- Item: Cr(t) = 0.5304 + 0.06 = 0.5904 (ตรวจเลขทุกบรรทัดแล้วตรงกับสูตร)
- เปรียบเทียบ item ต่างกันได้เมื่อใช้สเกล Severity เดียวกัน และเปลี่ยน t เพื่อดูว่าที่เวลาใดอะไรวิกฤติกว่า
- Fm(t) มาจาก Weibull ของแต่ละ FM ดู [[Weibull Analysis]] และ [[Reliability Metrics]]; โครง OR สอดคล้องกับ series logic ใน [[Reliability Block Diagram]]

## มาตรฐานที่หนังสืออ้าง (RBMM p.140-141)

MIL-STD-1629A; RAC-HDBK-1120; MIL-HDBK-217; MIL-STD-882D; NAVAIRINST 5100.11; IEC 60812; BS 5760-5; SAE ARP 5580; SAE J1739; SEMATECH (1992) FMEA guide; SAE JA1012; NAVAIR 00-25-403

## ข้อควรระวังในการใช้

- RPN ต้องระวังการคูณเลข ordinal: ต่างคอมโบอาจได้ RPN เท่ากันแต่ความเสี่ยงต่างกัน (ข้อสังเกตทั่วไป ไม่ได้อยู่ในหนังสือ) ให้ดู Severity 4-5 แยกเสมอ
- ผล FMECA ใช้จัดลำดับ FM ไม่ได้เลือกงาน PM ให้ ต้องต่อด้วย [[PM Task Selection]]

## เชื่อมโยงกับ compressor failure hierarchy

- คอลัมน์ Equipment / Damage Code / Object Part / Failure Mode ของ FMECA (Fig 5.23) ตรงกับ record ใน [[Failure Data Recording]] และชั้น [[Failure Hierarchy]]
- Occurrence ของ RPN อาจอิงสัดส่วน failure rate ต่อโหมดจาก [[OREDA]] ใน [[Failure Mode]] ได้ (การตีความ: % ใน wiki เป็นสัดส่วนของ total failure rate ไม่ใช่ rate ต่อชั่วโมง จึงแปลงเป็น rank 1-5 ของ Fig 5.19 ตรง ๆ ไม่ได้ ต้องกำหนดเกณฑ์เอง)
- Severity ของแต่ละโหมดขึ้นกับผลต่อ [[Compressor]] เช่น BRD มักร้ายแรงกว่า NOI; wiki ไม่มีข้อมูล severity (ไม่มีใน sources)
- Detect-ability สัมพันธ์กับ [[P-F Interval and Condition Monitoring]] เช่น VIB ตรวจจับล่วงหน้าได้ดีกว่าโหมด sudden

## ดูเพิ่ม

- [[RCM Reliability Centered Maintenance]]
- [[Criticality Assessment]]
- [[Failure Mode]]
- [[Failure Data Recording]]
- [[Weibull Analysis]]

## Triplets

- [[FMECA]] [has_label:: Failure Mode Effect Criticality Analysis]
- [[FMECA]] [applies_to:: Equipment] from equipment down to component/part (RBMM p.137)
- [[FMECA]] [produces:: Failure Mode Ranking] which FM matters first (RBMM ch5)
- [[FMECA]] [differs_from:: [[RCM Reliability Centered Maintenance]]] independent process from design/manufacturing; equipment level, ignores effect on larger frame (RBMM p.137)
- [[RCM Reliability Centered Maintenance]] [uses:: [[FMECA]]] RCM may use existing FMECA database (RBMM p.137)
- [[FMECA]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 5; table values are assessor opinion (RBMM p.139-140)
- Qualitative FMECA [is_a:: [[FMECA]]] used when no failure rate per FM (RBMM p.138-140)
- Quantitative FMECA [is_a:: [[FMECA]]] criticality from probability at time t (RBMM p.141-143)
- Qualitative FMECA [uses:: RPN]
- RPN [has_formula:: S x O x D] Severity x Occurrence x Detect-ability (RBMM p.138-140)
- RPN [has_parameter:: Severity]
- RPN [has_parameter:: Occurrence]
- RPN [has_parameter:: Detect-ability]
- Occurrence [defined_in:: Mil-Std-1629] Fig 5.19
- Occurrence Rank 1 [has_label:: Extremely Unlikely] rate not given in notes (Fig 5.19)
- Occurrence Rank 2 [has_value:: 1/10,000] Remote (Fig 5.19)
- Occurrence Rank 3 [has_value:: 1/1,000] Occasional (Fig 5.19)
- Occurrence Rank 4 [has_value:: 1/100] Reasonably Probable (Fig 5.19)
- Occurrence Rank 5 [has_value:: 1/10] Frequent, per cycles, hrs etc. (Fig 5.19)
- Severity [has_value:: 1-5] 1 Minor, 2 Marginal, 3 Moderate, 4 Critical, 5 Catastrophic (Fig 5.20)
- Detect-ability [has_value:: 1-5] 1 = 80-100% chance of early detection ... 5 = 0-20%; high score = hard to detect (Fig 5.21)
- RPN [has_value:: 24] example O = 4, S = 3, D = 2 (RBMM p.140)
- RPN [has_value:: 125] max 5 x 5 x 5, derived, not stated in book [confidence:: low]
- RPN [depends_on:: Company Criteria] book gives no acceptable RPN threshold
- RPN [depends_on:: Ordinal Scale] different combinations can give equal RPN with different risk; general observation not in book [confidence:: low]
- Functional Failure Probability [has_formula:: FF(t) = 1 - Product(1 - Fm_i(t))] (RBMM p.141-143)
- Functional Failure Criticality [has_formula:: FFCr(t) = FF(t) x S x MR] (RBMM p.141-143)
- Item Criticality [has_formula:: Cr(t) = Sum of FFCr(t)] (RBMM p.141-143)
- Functional Failure Criticality [has_parameter:: Severity] scale 0-1
- Functional Failure Criticality [has_parameter:: Failure Mode Ratio] MR, all ratios sum to 1
- [[Failure Mode]] [part_of:: Functional Failure] OR logic, parallel in failure tree (Fig 5.22)
- Functional Failure [part_of:: Function] (Fig 5.22)
- Function [part_of:: Item] (Fig 5.22)
- Functional Failure Probability [has_value:: 0.664] example FF1 of Function 1 (RBMM p.141-143)
- Functional Failure Criticality [has_value:: 0.3984] example FF1, S 1.0, MR 0.6
- Functional Failure Criticality [has_value:: 0.132] example FF2, FF 0.88, S 0.75, MR 0.2
- Functional Failure Criticality [has_value:: 0.06] example Function 2, FF 0.6, S 0.5, MR 0.2
- Item Criticality [has_value:: 0.5904] example item, Cr1 0.5304 + Cr2 0.06 (RBMM p.141-143)
- Quantitative FMECA [uses:: [[Weibull Analysis]]] Fm(t) from Weibull per FM
- [[FMECA]] [defined_in:: MIL-STD-1629A] standard cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: RAC-HDBK-1120] standard cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: MIL-HDBK-217] standard cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: MIL-STD-882D] standard cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: NAVAIRINST 5100.11] standard cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: IEC 60812] standard cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: BS 5760-5] standard cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: SAE ARP 5580] standard cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: SAE J1739] standard cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: SEMATECH FMEA Guide] 1992, cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: SAE JA1012] standard cited (RBMM p.140-141)
- [[FMECA]] [defined_in:: NAVAIR 00-25-403] standard cited (RBMM p.140-141)
- [[FMECA]] [input_to:: [[PM Task Selection]]] FMECA ranks FMs but does not select PM tasks
- [[FMECA]] [uses:: [[Failure Data Recording]]] columns Equipment, Damage Code, Object Part, Failure Mode (Fig 5.23)
- Occurrence [depends_on:: [[OREDA]]] interpretation: OREDA % share cannot map directly to Fig 5.19 ranks [confidence:: low]
- Detect-ability [related_to:: [[P-F Interval and Condition Monitoring]]] e.g. VIB detectable earlier than sudden modes

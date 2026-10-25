---
title: CMRP vs RBMM FMECA Scales
created: 2026-10-25
updated: 2026-10-25
type: comparison
tags: [comparison, fmeca, criticality, rcm, book, cmrp]
sources: [cmrp.md, reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# CMRP vs RBMM FMECA Scales

หน้านี้เทียบสเกลและสูตรของ FMECA / risk matrix ระหว่างสไลด์หลักสูตร CMRP ([[CMRP Course]]) กับหนังสือ RBMM ([[Reliability Based Maintenance Management Book]]) ความต่างส่วนใหญ่เป็น **convention ของสเกล** (1-10 vs 1-5, ทิศของ severity) ไม่ใช่ข้อเท็จจริงที่ขัดกัน จึงไม่ตั้ง contested แต่ตัวเลข RPN หรือ risk score จากสองระบบ **เทียบกันตรง ๆ ไม่ได้** ต้องรู้ว่าใช้สเกลไหนก่อนตีความ ข้อผิดพลาดเลขคณิตในสไลด์ระบุไว้ท้ายหน้า รายละเอียดแต่ละฝั่งดู [[FMECA]] และ [[Criticality Assessment]]

## 1. สรุปภาพรวม

| ประเด็น | CMRP (สไลด์) | RBMM (หนังสือ) |
|---|---|---|
| สูตร RPN | S x O x D (CMRP CMPR-02 p.33, p.43) | S x O x D (RBMM p.138-140) |
| สเกล S, O, D | 1-10 (CMRP CMPR-02 p.43-46) | 1-5 (RBMM Fig 5.19-5.21) |
| RPN สูงสุด | 1,000 (CMRP CMPR-02 p.47) | 125 (derived จาก 5 x 5 x 5) |
| เกณฑ์ RPN | ให้ band None/Low/Medium/High (CMRP CMPR-02 p.33) มีช่องว่าง | ไม่ให้เกณฑ์ ให้บริษัทกำหนด (RBMM p.140) |
| Criticality index | S + P หรือ S x P ไม่มี Detection (CMRP CMPR-03 p.2) | ใช้ RPN (มี D) หรือ FFCr เชิงปริมาณ |
| Risk matrix | 5 x 5 Effect x Probability, max 25 (CMRP CMPR-02 p.32) | 5 x 6 Consequence x Likelihood, max 30 (RBMM p.116-118) |
| Quantitative | MIL-STD-1629A: Mode Criticality = Item Unreliability x Mode Ratio x Probability of Loss (CMRP CMPR-02 p.50-51) | FFCr(t) = FF(t) x S x MR; Cr(t) = ผลรวม FFCr (RBMM p.141-143) |
| ทิศของ severity | category I = Catastrophic ... IV = Negligible (เลขน้อย = รุนแรง) และสเกล 1-10 (10 = รุนแรงสุด) | 5 = Catastrophic (เลขมาก = รุนแรง) |

## 2. Occurrence / Probability scales

CMRP มี **3 สเกล occurrence ที่ต่างกันเอง** ในสไลด์ชุดเดียว ส่วน RBMM มีสเกลเดียว:

| สเกล | ระดับ | ช่วง | ที่มา |
|---|---|---|---|
| CMRP FMEA occurrence (แบบ AIAG, ความรู้ทั่วไปว่าเป็นของ AIAG) | 1-10 | 10 = 1 ใน 2 หรือมากกว่า, 9 = 1/3, 8 = 1/8, 7 = 1/20, 6 = 1/80, 5 = 1/400, 4 = 1/2,000, 3 = 1/15,000, 2 = 1/150,000, 1 = น้อยกว่า 1/1,500,000 | CMRP CMPR-02 p.43-46 |
| CMRP FMECA brief method | 4 ระดับ | 1 Extremely Remote, 2 Remote, 3 Reasonably Probable, 4 Probable (ไม่มีตัวเลข ไม่มีระดับ Frequent) | CMRP CMPR-03 p.1 |
| CMRP FMECA detailed method | 1-10 | 1 = 1/10,000, 2 = 1/5,000, 3 = 1/2,000, 4 = 1/1,000, 5 = 1/500, 6 = 1/200, 7 = 1/100, 8 = 1/50, 9 = 1/20, 10 = 1/10 ขึ้นไป | CMRP CMPR-03 p.1 |
| CMRP qualitative level (MIL-STD-1629A) | A-E | A Frequent, B Reasonably probable, C Occasional, D Remote, E Extremely unlikely | CMRP CMPR-02 p.50 |
| RBMM occurrence (Mil-Std-1629) | 1-5 | 1 Extremely Unlikely (ไม่ระบุอัตรา), 2 Remote 1/10,000, 3 Occasional 1/1,000, 4 Reasonably Probable 1/100, 5 Frequent 1/10 | RBMM Fig 5.19, p.138-140 |

ข้อสังเกต:
- ป้ายชื่อ 5 ระดับของ RBMM ตรงกับ level A-E ของ MIL-STD-1629A ใน CMRP แต่ **ทิศกลับกัน**: RBMM 5 = Frequent ส่วน CMRP A = Frequent (derived จากการเทียบป้ายชื่อ)
- detailed method ของ CMRP มีช่วงปลายเท่ากับ RBMM (1/10,000 ถึง 1/10) แต่แบ่งละเอียดกว่า; สเกล FMEA occurrence ของ CMRP กว้างกว่ามาก (ถึงราว 1 ใน 1.5 ล้าน) จึงใช้คนละบริบท (การผลิต/ชิ้นงาน vs อุปกรณ์)
- สเกล detailed ของ CMRP ไม่ระบุหน่วย (ต่อชิ้น ต่อรอบ หรือต่อชั่วโมง) และหัวตารางเขียนว่า "Effect" ทั้งที่เป็นความน่าจะเป็น (CMRP CMPR-03 p.1)

## 3. Severity scales

| สเกล | ระดับ | ที่มา |
|---|---|---|
| CMRP FMEA severity | 1-10: 10 = อันตรายโดยไม่มีเตือน, 9 = อันตรายมีเตือน, 8 = สูญเสียหน้าที่หลัก ... 1 = ไม่มีผล; S 9-10 ควรแก้ที่แบบ | CMRP CMPR-02 p.43-46 |
| CMRP severity category (MIL-STD-1629A) | I Catastrophic, II Critical, III Marginal, IV Negligible; มีแบบละเอียด 1-10 สำหรับ facility (9-10 = ประเด็น HSE) | CMRP CMPR-02 p.52 |
| RBMM severity | 1 Minor, 2 Marginal, 3 Moderate, 4 Critical, 5 Catastrophic | RBMM Fig 5.20 |
| RBMM quantitative S | 0-1 (ขนาดความเสียหาย) ใช้ใน FFCr | RBMM p.141-143 |

Detection: CMRP 1-10 (10 = design control ตรวจไม่ได้เลย, 1 = ตรวจพบแน่นอน; CMRP CMPR-02 p.43-46) vs RBMM 1-5 อิงโอกาสตรวจพบล่วงหน้า (1 = 80-100%, 5 = 0-20%; RBMM Fig 5.21) ทิศเดียวกัน: เลขมาก = ตรวจยาก

## 4. Criticality index และ quantitative criticality

- **CMRP criticality index** = ผลรวม **หรือ** ผลคูณของ Severity กับ Probability index ไม่มี Detection (CMRP CMPR-03 p.2; CMPR-02 p.49 บอกว่าใช้การบวก) ขณะที่ risk matrix และ RPN ของสไลด์เองใช้การคูณ จึงไม่สอดคล้องกันภายใน CMRP
- **MIL-STD-1629A quantitative (CMRP)**: Mode Criticality = Item Unreliability x Mode Ratio x Probability of Loss; Item Criticality = ผลรวม Mode Criticality ทุกโหมด (CMRP CMPR-02 p.50-51)
- **RBMM quantitative**: FF(t) = 1 - Product(1 - Fm_i(t)); FFCr(t) = FF(t) x S x MR; Cr(t) = ผลรวม FFCr (RBMM p.141-143)
- โครงเดียวกัน (unreliability x สัดส่วน x ความรุนแรง แล้วรวมเป็น item) แต่ต่างกัน 3 จุด: (1) RBMM รวม FM เข้าเป็น functional failure ด้วย OR logic ก่อน, (2) RBMM ใช้ severity 0-1 แทน probability of loss, (3) MR ของ RBMM คือสัดส่วนของ functional failure ต่อ item ไม่ใช่สัดส่วนของ failure mode (derived จากการเทียบสูตร)
- ความรู้ทั่วไป (ไม่มีใน sources): สูตรเต็มของ MIL-STD-1629A คือ Cm = beta x alpha x lambda_p x t (beta = probability of loss, alpha = mode ratio, lambda_p x t = ส่วน unreliability ที่ประมาณด้วย constant rate) สไลด์ใช้ "item unreliability" แทนพจน์ lambda_p x t

## 5. Risk matrix: 5 x 5 vs 5 x 6

| ประเด็น | CMRP 5 x 5 (CMRP CMPR-02 p.32-33) | RBMM 5 x 6 (RBMM p.116-118) |
|---|---|---|
| แกน | Effect 1-5 (no, negligible, marginal, critical, catastrophic) x Probability 1-5 (1/25 ปี, 1/10 ปี, 1/5 ปี, 1/ปี, 1/เดือน) | Consequence 1-5 x Likelihood 1-6 แยก Commercial, Safety, Environment |
| ช่วงคะแนน | 1-25 | 1-30 |
| Band | Low 1-3, Medium 4-9, High 10-25 | C 1-4, B 5-12, A 15-30 |
| การใช้ผล | Low = ไม่ทำ preventive; Medium/High = ทำ preventive ต่างกันที่ระดับ เช่น การสำรองอะไหล่ | A = 100% RCM tasks, B = pro-active, C = re-active |

ข้อสังเกต: band ของ CMRP 5 x 5 ต่อเนื่องกันไม่มีช่องว่าง (ต่างจาก RPN band ในหัวข้อ 6) ส่วน RBMM มีช่องว่างแค่ในรูป (13, 14) ซึ่งผลคูณ 1-5 x 1-6 ไม่มีทางได้ จึงไม่มีช่องว่างจริง (ดู [[Criticality Assessment]]); แต่ CMRP ระบายแถว "No effects" ที่ probability 1/ปี และ 1/เดือน (คะแนน 4, 5) เป็น Medium ทั้งที่ไม่มีผลกระทบ (CMRP CMPR-02 p.32)

## 6. RPN bands ของ CMRP และช่องว่าง (CMRP CMPR-02 p.33)

| Band | ช่วง RPN |
|---|---|
| None | 0 |
| Low | 8-40 |
| Medium | 80-240 |
| High | 320-1,000 |

ปัญหา:
- "None = 0" เป็นไปไม่ได้ เพราะ S, O, D ต่ำสุดคือ 1 (RPN ต่ำสุด = 1)
- ช่วง 1-7, 41-79 และ 241-319 ไม่ถูกจัดระดับ ทั้งที่เป็นผลคูณที่เกิดได้จริง (เช่น 6 = 1 x 2 x 3, 60 = 3 x 4 x 5, 252 = 6 x 6 x 7)
- ตัวเลขขอบดูเหมือนมาจากสเกลอื่น (เช่น 2 x 2 x 2 = 8) ใช้ band นี้ไม่ได้ถ้าไม่กำหนดช่วงที่หายไปเอง
- RBMM ไม่ให้ band เลย (RBMM p.140) จึงไม่มีอะไรให้เทียบตรง

## 7. ตัวอย่าง RPN = 360: ที่มาของคำเตือนเรื่องคูณเลข ordinal (CMRP CMPR-02 p.33)

- สไลด์แสดง 15 คอมโบของ S, O, D ที่ได้ **RPN = 360 เท่ากันทั้งหมด** เช่น 10 x 9 x 4, 9 x 10 x 4, 4 x 9 x 10 (ตรวจผลคูณครบ 15 แถวแล้วถูกต้อง ตาม raw notes)
- ความหมาย: RPN เท่ากันแต่ลักษณะความเสี่ยงต่างกันมาก (severity 10 ที่ตรวจจับง่าย vs severity 4 ที่ตรวจไม่ได้) เพราะ S, O, D เป็นสเกล ordinal การคูณจึงไม่รักษาลำดับความเสี่ยง
- สไลด์ยังเตือนว่า RPN เป็นเกณฑ์ threshold ไม่ใช่ตัวตัดสิน ต้องใช้วิจารณญาณเมื่อ RPN สูงแต่ severity ต่ำ และ S 9-10 ต้องแก้ที่แบบไม่ว่า RPN เท่าไร (CMRP CMPR-02 p.46)
- ก่อนหน้านี้ [[FMECA]] ระบุคำเตือนนี้ว่าเป็น "ข้อสังเกตทั่วไป ไม่ได้อยู่ในหนังสือ" ตอนนี้มี source (CMRP) รองรับแล้ว

## 8. ข้อผิดพลาดเลขคณิตในสไลด์ (PFMEA p.41)

ตัวอย่าง PFMEA งานพ่น wax ในประตูรถ (CMRP CMPR-02 p.41) ตรวจเลขแล้ว:

| แถว | สไลด์พิมพ์ | ค่าที่ถูก | หมายเหตุ |
|---|---|---|---|
| 1 หลังแก้ | S7 O2 D6 RPN = 70 | 7 x 2 x 6 = **84** | ได้ 70 ถ้า D = 5 |
| 4 ก่อนแก้ | 7 x 8 x 7 = 382 | **392** | |
| 4 หลังแก้ | 7 x 1 x 7 = 40 | **49** | |
| 1 ก่อนแก้, 2, 3 | 280, 105 -> 21, 28 | ถูกต้อง | |

ใช้ค่าที่ถูกเมื่ออ้างตัวอย่างนี้ เป็นข้อผิดพลาดของสไลด์ ไม่ใช่ข้อขัดแย้ง

## 9. แนวทางใช้งาน (ข้อเสนอของ wiki)

- ระบุสเกลทุกครั้งที่รายงาน RPN เช่น "RPN 120 (สเกล 1-10)" เพราะ RPN 120 บนสเกล 1-5 เกือบเต็ม (96% ของ 125) แต่บนสเกล 1-10 เป็นแค่ 12% ของ 1,000 (derived)
- แปลงระหว่างสเกลด้วยการ map ระดับ occurrence ตามอัตราจริง (เช่น 1/1,000 = RBMM 3 = CMRP detailed 4) ไม่ใช่คูณ 2 ตรง ๆ
- คัด severity สูงแยกก่อนเสมอ ไม่ว่าใช้สเกลไหน

## เชื่อมโยงกับ compressor failure hierarchy

- ถ้าจะทำ FMECA ต่อ [[Failure Mode]] ของ [[Compressor]] ต้องเลือกสเกลเดียวทั้งโครงการ; % failure rate จาก [[OREDA]] เป็นสัดส่วน ไม่ใช่อัตราต่อชั่วโมง จึง map เข้า occurrence ทั้งสองระบบตรง ๆ ไม่ได้ (เหมือนข้อสังเกตใน [[FMECA]])

## Triplets

- [[CMRP vs RBMM FMECA Scales]] [related_to:: [[FMECA]]] scale and formula comparison
- CMRP RPN [has_formula:: S x O x D] scales 1-10 (CMRP CMPR-02 p.33, p.43)
- CMRP RPN [has_value:: max 1,000] 10 x 10 x 10; 100 when occurrence = 1 (CMRP CMPR-02 p.47)
- RPN [has_value:: max 125] RBMM 5 x 5 x 5, derived [confidence:: low]
- CMRP RPN [differs_from:: RPN] 1-10 scales vs RBMM 1-5 scales; convention difference, not comparable directly
- CMRP FMEA Occurrence [has_value:: 1 in 2 to less than 1 in 1,500,000] rank 10 to rank 1 (CMRP CMPR-02 p.43-46)
- CMRP FMECA Brief Probability [has_value:: 4 levels] Extremely Remote, Remote, Reasonably Probable, Probable (CMRP CMPR-03 p.1)
- CMRP FMECA Detailed Probability [has_value:: 1/10,000 to 1/10 or more] 10 ranks, unit not stated (CMRP CMPR-03 p.1)
- MIL-STD-1629A Qualitative Level [has_value:: A-E] A Frequent to E Extremely unlikely (CMRP CMPR-02 p.50)
- MIL-STD-1629A Qualitative Level [differs_from:: Occurrence] same labels as RBMM 1-5 but reversed direction, derived
- MIL-STD-1629A Severity Category [has_value:: I-IV] I Catastrophic, II Critical, III Marginal, IV Negligible (CMRP CMPR-02 p.52)
- MIL-STD-1629A Severity Category [differs_from:: Severity] lower number = more severe vs RBMM 5 = Catastrophic
- CMRP FMEA Severity [has_value:: 1-10] 10 hazardous without warning, 1 no effect (CMRP CMPR-02 p.43-46)
- CMRP Criticality Index [has_formula:: S + P or S x P] no Detection (CMRP CMPR-03 p.2)
- CMRP Criticality Index [differs_from:: RPN] excludes Detection; slides also use addition, inconsistent with own multiplication (CMRP CMPR-02 p.49)
- MIL-STD-1629A Mode Criticality [has_formula:: Item Unreliability x Mode Ratio x Probability of Loss] (CMRP CMPR-02 p.50-51)
- MIL-STD-1629A Item Criticality [has_formula:: Sum of Mode Criticality] (CMRP CMPR-02 p.50-51)
- MIL-STD-1629A Mode Criticality [related_to:: Functional Failure Criticality] same structure as RBMM FFCr(t) = FF(t) x S x MR, derived
- MIL-STD-1629A Mode Criticality [has_formula:: Cm = beta x alpha x lambda_p x t] full standard form, general knowledge [confidence:: low]
- CMRP Risk Matrix [has_value:: 5 x 5, max 25] Effect x Probability (CMRP CMPR-02 p.32)
- CMRP Risk Matrix [has_value:: Low 1-3, Medium 4-9, High 10-25] (CMRP CMPR-02 p.32)
- CMRP Risk Matrix [differs_from:: Criticality Score] RBMM 5 x 6 max 30 with bands C 1-4, B 5-12, A 15-30
- CMRP Risk Matrix [has_value:: No effects row coloured Medium] cells 4 and 5, inconsistent with Risk = P x Effect (CMRP CMPR-02 p.32)
- CMRP RPN Band [has_value:: None 0, Low 8-40, Medium 80-240, High 320-1,000] (CMRP CMPR-02 p.33)
- CMRP RPN Band [has_value:: gaps 1-7, 41-79, 241-319] unclassified achievable RPN; None = 0 impossible, derived
- RPN [depends_on:: Ordinal Scale] 15 combinations all give RPN 360, e.g. 10 x 9 x 4, 4 x 9 x 10 (CMRP CMPR-02 p.33)
- CMRP RPN [depends_on:: Severity] S 9-10 needs design fix regardless of RPN; RPN is a threshold, not the decision (CMRP CMPR-02 p.46)
- PFMEA Example Row 1 After [has_value:: 84] S7 O2 D6; slide prints 70 (CMRP CMPR-02 p.41)
- PFMEA Example Row 1 Slide Value [contradicts:: PFMEA Example Row 1 After] slide error, 70 only if D = 5
- PFMEA Example Row 4 Before [has_value:: 392] 7 x 8 x 7; slide prints 382 (CMRP CMPR-02 p.41)
- PFMEA Example Row 4 Slide Before Value [contradicts:: PFMEA Example Row 4 Before] slide prints 382
- PFMEA Example Row 4 After [has_value:: 49] 7 x 1 x 7; slide prints 40 (CMRP CMPR-02 p.41)
- PFMEA Example Row 4 Slide After Value [contradicts:: PFMEA Example Row 4 After] slide prints 40
- CMRP FMECA Scales [defined_in:: [[CMRP Course]]] (CMRP CMPR-02, CMPR-03)
- RBMM FMECA Scales [defined_in:: [[Reliability Based Maintenance Management Book]]] (RBMM p.116-118, p.138-143)
- [[CMRP vs RBMM FMECA Scales]] [related_to:: [[Criticality Assessment]]] risk matrix 5 x 5 vs 5 x 6

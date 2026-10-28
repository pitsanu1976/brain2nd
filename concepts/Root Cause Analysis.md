---
title: Root Cause Analysis
created: 2026-10-25
updated: 2026-10-28
type: concept
tags: [rca, fmeca, fta, reliability, maintenance-management, failure-cause, cmrp, mpm]
sources: [cmrp.md, iso-14224.md, maintenance-profit-maker.md]
confidence: medium
contested: false
---

# Root Cause Analysis (RCA / RCFA)

**Root Cause Analysis (RCA)** หรือ Root Cause Failure Analysis (RCFA) คือแนวทางแก้ปัญหาอย่างเป็นระบบ เพื่อหา "สาเหตุราก" ของ failure หรือเหตุการณ์ แล้วเลือกมาตรการที่ป้องกันการเกิดซ้ำได้คุ้มที่สุด ไม่ใช่แค่แก้อาการ หน้านี้สรุปจากสไลด์หลักสูตร CMRP (ดู [[CMRP Course]]) เป็น secondary source ส่วนการบังคับทำ RCA และฟิลด์ root cause มาจาก [[ISO 14224]] confidence medium เพราะสไลด์เป็นสื่อการสอนที่ถอดความจาก OCR

## 1. วัตถุประสงค์: แก้ระบบ ไม่หาคนผิด (CMRP CMPR-03 p.14)

- RCFA มุ่งแก้ปัญหาที่กระทบ plant performance ไม่ใช่หาคนผิด (no blame)
- ต้องสื่อสารเป้าหมายนี้ให้ทีมและผู้เกี่ยวข้องเข้าใจตั้งแต่ต้น เพื่อลดท่าทีป้องกันตัว ซึ่งทำให้ข้อมูลจริงไม่ออกมา
- RCA ใช้ได้ทั้งกับเหตุที่เกิดแล้ว (reactive) และการศึกษาจุดอ่อนล่วงหน้า (proactive); ผลต้องวัดได้และให้ savings จริง มี 5 มุมมอง (facets): safety, production, process, failure, systems-based (CMRP CMPR-03 p.15-17)

## 2. Physics of failure: มุมมอง stress-strength (CMRP CMPR-03 p.15)

ชิ้นส่วนเสียเมื่อ stress ที่รับเกิน strength ของมัน แสดงด้วยการกระจาย (distribution) ของ stress และ strength ที่ทับกัน (stress-strength interference) และ factor of safety:

| แบบ | กลไก |
|---|---|
| Overload | load ครั้งหนึ่งสูงกว่า strength ของชิ้นที่อ่อนที่สุดในการกระจาย strength |
| Fatigue / degradation | strength ลดลงตามการใช้งาน จนการกระจาย strength เลื่อนมาทับการกระจาย stress |

หลักคิด: "ชิ้นส่วนเสียก่อน แล้วเครื่องจึงหยุด" RCA จึงต้องลงไปถึงระดับชิ้นส่วนและกลไก (ดู [[Failure Mechanism]] และ [[Wear Mechanisms]]) แล้วถามต่อว่าอะไรทำให้ stress สูงขึ้นหรือ strength ต่ำลง

## 3. กระบวนการ 4 ขั้น (CMRP CMPR-03 p.19-20)

1. **นิยามปัญหา**: เขียน problem statement พร้อมเงื่อนไข (อะไร ที่ไหน เมื่อไร มากเท่าไร)
2. **รวบรวมสาเหตุที่เป็นไปได้** พร้อมหลักฐาน จาก [[FMECA]] (FMEA), [[Fault Tree Analysis]], failure analysis, test, simulation แล้วตั้งเป็น hypothesis
3. **ประเมิน hypothesis**: ใช้สถิติ (test of hypothesis) หรือเทคนิคตัดสินใจ (decision tree, payoff table) คัดจนเหลือ true cause
4. **Validate**: ทดลองให้ปัญหาเกิดซ้ำได้ภายใต้หลายเงื่อนไข เพื่อยืนยันว่าเป็นสาเหตุจริง

เคล็ดลับจากสไลด์ (p.23): อย่าหยุดก่อนถึง root, ลงรายละเอียด และต้อง validate คำตอบเสมอ

## 4. ตัวอย่างทำงานจริง: FMEA -> Pareto -> DOE (CMRP CMPR-03 p.21-22)

- อาการ: อุปกรณ์เสียงไม่ดัง 3 ใน 100 ชิ้น พบใน region 4 เริ่มราว 2 สัปดาห์ก่อนและเพิ่มขึ้น
- ระบุสาเหตุที่เป็นไปได้ 7 ข้อด้วย fishbone แล้วจัดลำดับด้วย **FMEA** (RPN สูง: contamination, open circuit)
- ใช้ **Pareto** คัดตัวแปรหลัก แล้วใช้ **DOE** ดู main effect และ interaction
- ผล: ความชื้นจากมือ operator **ร่วมกับ** วัสดุ contact ที่ heat treat ไม่สมบูรณ์ ทำให้เกิด oxidation (สาเหตุเป็น interaction ไม่ใช่ตัวแปรเดี่ยว ซึ่ง DOE จับได้แต่ 5 Whys แบบเส้นตรงอาจพลาด: ข้อสังเกตของ wiki)
- Confirmation run ยืนยันผล; แก้ด้วยถุงมือ + ทบทวนกระบวนการ annealing

## 5. เครื่องมือ: rearward vs forward looking (CMRP CMPR-03 p.23)

| ทิศทาง | เครื่องมือ | ใช้เมื่อ |
|---|---|---|
| Rearward-looking (มองย้อนจากเหตุที่เกิดแล้ว) | 5 Whys, Why-Because Analysis, [[Fault Tree Analysis]] | สืบสวน failure/incident ที่เกิดแล้ว |
| Forward-looking (มองไปข้างหน้า) | FMEA ดู [[FMECA]] | คาด failure mode ที่อาจเกิด ก่อนเกิด |

เครื่องมือเสริมที่ปรากฏในตัวอย่าง: fishbone, Pareto, DOE (p.21-22) และ control chart ใน [[Statistical Process Control]] ใช้เป็นตัวจุด RCA เมื่อ KPI หลุด limit (CMRP CMPR-03 p.46-48)

### 5 Whys (CMRP CMPR-03 p.24-26)

- ถาม "ทำไม" ซ้ำจนถึงสาเหตุที่แก้แล้วปัญหาไม่กลับมา ตัวอย่างรถสตาร์ทไม่ติด: battery หมด -> alternator ไม่ทำงาน -> belt ขาด -> belt ใช้เกินอายุ -> ไม่ได้ทำ service ตามตาราง (= root cause)
- จำนวน "why" ไม่จำเป็นต้องเป็น 5 พอดี
- ตัวอย่าง Washington Monument: หินสึกเพราะสารเคมีล้าง -> ล้างบ่อยเพราะมูลนก -> นกมาเพราะแมงมุม -> แมงมุมมาเพราะแมลง -> แมลงมาเพราะไฟเปิดตอนพลบค่ำ; ทางแก้ระดับกลาง (สารเคมีอ่อน, ไล่นก, ยาฆ่าแมลง) แพงหรือมีผลเสีย ทางแก้ที่ root คือปรับเวลาเปิดไฟ
- ข้อจำกัด (ความรู้ทั่วไป ไม่มีใน sources): ได้สายเหตุเส้นเดียว จับหลายสาเหตุร่วมหรือ interaction ไม่ได้ จึงควรใช้ WBA/FTA เมื่อเหตุซับซ้อน

### Why-Because Analysis และ Why-Because Graph (CMRP CMPR-03 p.26-28)

- นิยมในการสืบสวนอุบัติเหตุขนส่ง เริ่มจาก incident ด้านบน แล้วไล่สาเหตุลงเป็นกราฟ (Why-Because Graph, WBG) จนถึง root
- ทุกคู่ "เหตุ -> ผล" ต้องผ่าน 2 การทดสอบ:

| Test | คำถาม | พิสูจน์อะไร |
|---|---|---|
| Counterfactual Test (CT) | ถ้าไม่มีสาเหตุนี้ ผลยังเกิดได้ไหม | สาเหตุนี้ **จำเป็น** (ถ้าผลยังเกิด สาเหตุนี้ไม่ใช่เหตุจริง ตัดออก) |
| Causal Sufficiency Test (CST) | ถ้าสาเหตุที่ระบุเกิดครบ ผลเกิดเสมอไหม | ชุดสาเหตุ **เพียงพอ** (ถ้าไม่เสมอ แปลว่ายังขาดสาเหตุ ต้องเพิ่ม) |

- WBG ถูกต้องเมื่อทุกสาเหตุจำเป็นและชุดสาเหตุเพียงพอ: ไม่ขาด ไม่เกิน

## 6. ปัจจัยความสำเร็จของโปรแกรม RCA (CMRP CMPR-03 p.18-19)

- Critical success factors: ทีมที่เหมาะสม, วิธีและเครื่องมือ, training, **trigger points** ที่ชัดว่าเมื่อไรต้องเริ่ม RCA, การเก็บรักษาข้อมูล, การติดตามการ implement มาตรการ, การสนับสนุนของผู้บริหาร
- Checklist เริ่มโปรแกรม 8 ข้อ: การอนุมัติ, ความคาดหวังและ timeline, policy/procedure, orientation ผู้บริหาร, sponsor, ทีม, training, งบและเวลาของทีม
- ระวัง **unanimity**: consensus เป็นเรื่องดี แต่ถ้าทุกคนเห็นตรงกันหมดทันทีควรสงสัยว่ามี groupthink

## 7. มุมมอง ISO 14224: trigger และฟิลด์ root cause

- ISO 14224 กำหนดให้ทำ RCA **บังคับ** สำหรับ "worst actors": failure ผลกระทบสูง, cost ซ่อม/downtime สูง หรือเกิดบ่อยผิดปกติ (ISO 14224 Table 6 note d, p.41) ดู [[Failure Data Recording]] ซึ่งตรงกับ "trigger points" ของสไลด์ CMRP (p.18) แต่ CMRP ไม่ได้ให้เกณฑ์ trigger เป็นตัวเลข
- ผลของ RCA บันทึกเป็น **failure cause** (root cause, ISO Table B.3) ซึ่งเป็นคนละฟิลด์กับ failure mechanism (Table B.2) (ISO 14224 cl. B.2.2-B.2.3, p.178-181) ดู [[Failure Cause Codes]] ข้อสังเกต: รหัส 4 ตัวอักษรใน dataset ของ wiki เป็น mechanism ไม่ใช่ root cause ดังนั้นผลลัพธ์ของ RCA ต้องลงในฟิลด์ cause แยกต่างหาก
- RCA เป็นงานกลุ่ม "Proactive" ในผัง RCM ของ CMRP (RCFA, age exploration, FMEA) และเป็นขั้น 4 ของวงล้อ RCM 7 ขั้น (หา root cause ของ FM) (CMRP CMPR-03 p.2) ดู [[RCM Reliability Centered Maintenance]]

## 8. การใช้ RCA ในมุมมอง MPM (เพิ่ม 2026-10-28)

หนังสือ [[Maintenance Profit Maker Book]] วาง RCA เป็นเครื่องมือแก้ "ต้นเหตุ" ของต้นทุน ไม่ใช่แค่ failure:

- **ลดการกินอะไหล่**: การปรับ min/max และ reorder point เป็นการบริหาร "ผล" ต้นเหตุคือพฤติกรรมการกินอะไหล่ ให้เก็บประวัติการเสีย/การแก้ไข แล้วทำ Failure Root Cause Analysis โดยใช้รายงาน CMMS **ค่าอะไหล่สูงสุด 10 อันดับ** จัดการทีละ 10 รายการ (MPM p.219) สาเหตุที่พบ เช่น ออกแบบด้อย ติดตั้งผิด ใช้งานนอกเงื่อนไข อะไหล่ไม่มีคุณภาพ คุณภาพการซ่อมไม่พอ กลยุทธ์ PM/CM/PDM ไม่เหมาะ ดู [[Maintenance Performance Improvement]] และ [[Spare Parts Management]]
- **กลยุทธ์ธุรกิจ**: ธุรกิจแบบ Cost Leadership (เน้น Availability/MTTR) ใช้ Failure Root Cause Analysis ร่วมกับลด MWT และ TPM ส่วน Product Differentiation (เน้น Reliability/MTBF) ใช้ root cause analysis ร่วมกับ PM และ Reliability Engineering (รูป 9.3, MPM p.165) ดู [[Maintenance Master Plan]]
- **สัญญาณให้ทำ RCA**: ถ้า Reliability Figure ต่ำกว่ากำหนด (failure rate สูง) แสดงว่ามี root cause ฝังอยู่ (MPM p.20) และ CMMS ต้องวางโครงสร้างประวัติซ่อมให้รองรับ RCA/FMECA (MPM p.161)

## เชื่อมโยงกับ compressor failure hierarchy

- ลำดับการสืบสวนบน [[Compressor]] ตาม [[Failure Hierarchy]]: failure mode (อาการ เช่น VIB) -> mechanism (เช่น WEAR, FATG) -> cause (root cause ตาม ISO Table B.3) RCA คือขั้นที่เติมระดับสุดท้ายนี้ (การตีความของ wiki)
- เกณฑ์ worst actors ของ ISO สามารถใช้ % failure rate ของ [[Failure Mode]] จาก [[OREDA]] ช่วยคัดว่าโหมดใดควรเป็น trigger แต่ต้องคูณ consequence ด้วย (ข้อเสนอแนะ ไม่ใช่ข้อมูลใน sources)

## ดูเพิ่ม

- [[FMECA]]
- [[Fault Tree Analysis]]
- [[Failure Cause Codes]]
- [[Failure Data Recording]]
- [[Failure Mechanism]]
- [[CMRP Course]]
- [[Maintenance Performance Improvement]]
- [[Maintenance Master Plan]]

## Triplets

- [[Root Cause Analysis]] [alias_of:: RCFA] Root Cause Failure Analysis (CMRP CMPR-03 p.14)
- [[Root Cause Analysis]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-03 p.14-28)
- [[Root Cause Analysis]] [produces:: Recurrence Prevention] systematic problem solving, not blame (CMRP CMPR-03 p.14-17)
- [[Root Cause Analysis]] [differs_from:: Blame Finding] aims at plant performance, communicate to reduce defensiveness (CMRP CMPR-03 p.14)
- [[Root Cause Analysis]] [has_category:: Safety] facet 1 of 5; also production, process, failure, systems-based (CMRP CMPR-03 p.15-17)
- [[Root Cause Analysis]] [uses:: Stress-Strength Interference] physics of failure with factor of safety (CMRP CMPR-03 p.15)
- Overload [is_a:: Stress-Strength Interference] load above strength of weakest part (CMRP CMPR-03 p.15)
- Fatigue [is_a:: Stress-Strength Interference] strength degrades with use until distributions overlap (CMRP CMPR-03 p.15)
- Problem Statement [step_of:: [[Root Cause Analysis]]] step 1, define problem and conditions (CMRP CMPR-03 p.19-20)
- Possible Causes and Hypotheses [step_of:: [[Root Cause Analysis]]] step 2, evidence from FMEA, FTA, failure analysis, test, simulation (CMRP CMPR-03 p.19-20)
- Hypothesis Evaluation [step_of:: [[Root Cause Analysis]]] step 3, hypothesis test or decision tree / payoff table (CMRP CMPR-03 p.19-20)
- Validation [step_of:: [[Root Cause Analysis]]] step 4, reproduce the problem under several conditions (CMRP CMPR-03 p.19-20)
- [[Root Cause Analysis]] [uses:: [[FMECA]]] FMEA ranks possible causes by RPN in worked example (CMRP CMPR-03 p.21-22)
- [[Root Cause Analysis]] [uses:: Pareto Analysis] worked example (CMRP CMPR-03 p.21-22)
- [[Root Cause Analysis]] [uses:: Design of Experiments] main effect and interaction (CMRP CMPR-03 p.21-22)
- RCA Worked Example [has_cause:: Operator Hand Moisture] combined with incomplete heat treatment of contact material, oxidation (CMRP CMPR-03 p.21-22)
- RCA Worked Example [has_value:: 3 in 100] units with low sound, region 4 (CMRP CMPR-03 p.21)
- 5 Whys [is_a:: Rearward-Looking Tool] (CMRP CMPR-03 p.23)
- Why-Because Analysis [is_a:: Rearward-Looking Tool] (CMRP CMPR-03 p.23)
- [[Fault Tree Analysis]] [is_a:: Rearward-Looking Tool] (CMRP CMPR-03 p.23)
- [[FMECA]] [is_a:: Forward-Looking Tool] FMEA (CMRP CMPR-03 p.23)
- 5 Whys [has_value:: not exactly 5] number of whys varies (CMRP CMPR-03 p.24-26)
- 5 Whys [related_to:: Single Causal Chain] cannot capture combined causes; general knowledge [confidence:: low]
- Why-Because Analysis [produces:: Why-Because Graph] incident at top down to root causes (CMRP CMPR-03 p.26-28)
- Why-Because Graph [uses:: Counterfactual Test] proves each cause is necessary (CMRP CMPR-03 p.26-28)
- Why-Because Graph [uses:: Causal Sufficiency Test] proves cause set is sufficient, finds missing causes (CMRP CMPR-03 p.26-28)
- [[Root Cause Analysis]] [depends_on:: Trigger Points] critical success factor (CMRP CMPR-03 p.18)
- [[Root Cause Analysis]] [depends_on:: Management Support] critical success factor; also team, tools, training, data, follow-up (CMRP CMPR-03 p.18)
- [[Root Cause Analysis]] [related_to:: Unanimity] full agreement in team should be questioned (CMRP CMPR-03 p.19)
- [[Root Cause Analysis]] [applies_to:: Worst Actors] mandatory for high impact, high cost/downtime or unusually frequent failures (ISO 14224 Table 6 note d, p.41)
- [[Root Cause Analysis]] [produces:: ISO:B.3] result recorded as failure cause, separate from mechanism Table B.2 (ISO 14224 cl. B.2.2-B.2.3, p.178-181)
- [[Root Cause Analysis]] [related_to:: [[Failure Cause Codes]]] dataset 4-letter codes are mechanism, not root cause
- [[Root Cause Analysis]] [step_of:: [[RCM Reliability Centered Maintenance]]] step 4 of CMRP 7-step RCM wheel; Proactive group (CMRP CMPR-03 p.2)
- [[Statistical Process Control]] [input_to:: [[Root Cause Analysis]]] KPI outside limits triggers RCA (CMRP CMPR-03 p.46-48)
- [[Root Cause Analysis]] [applies_to:: Top 10 Spare Part Cost Items] reduce spare consumption behaviour, CMMS report (MPM p.219)
- [[Root Cause Analysis]] [resolved_by:: Redesign] for poor original design; also reinstall, fix environment, change source, repair QC, adjust PM strategy (MPM p.219)
- Cost Leadership [uses:: [[Root Cause Analysis]]] with MWT reduction and TPM (Fig 9.3, MPM p.165)
- Product Differentiation [uses:: [[Root Cause Analysis]]] with PM and reliability engineering (Fig 9.3, MPM p.165)
- Low Reliability Figure [input_to:: [[Root Cause Analysis]]] high failure rate signals embedded root cause (MPM p.20)

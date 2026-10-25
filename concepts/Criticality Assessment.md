---
title: Criticality Assessment
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [criticality, rcm, spare-parts, maintenance-management, cost, book, iso-14224, cmrp]
sources: [reliability-based-maintenance-management.md, iso-14224.md, cmrp.md]
confidence: medium
contested: false
---

# Criticality Assessment

**Criticality Assessment** คือการจัดระดับความวิกฤติของเครื่องจักรเป็น A/B/C (High/Moderate/Low) เพื่อเลือกกลยุทธ์ PM อะไหล่ และงบ ให้ต่างกันตามระดับ ภายใต้เป้า "Zero (Plant) Breakdown @ Minimum Cost" RBMM บท 5 วัด criticality ด้วย Consequence (1-5) x Likelihood (1-6) = Score 1-30 แยก 3 ด้าน: Commercial, Safety, Environment โดยอ้างแนว FMECA Mil-1629 ส่วนเกณฑ์ตัวเลขเป็นตัวอย่างที่ปรับเองได้ (RBMM p.116-117) confidence เป็น medium เพราะมีค่า derived ที่ผู้เขียน wiki คำนวณเพิ่ม (ระบุในหน้า) และบางตัวเลขในภาพเบลอ

> [!warning] คำว่า "critical" มี 3 ความหมาย
> 1. **A/B/C ในหน้านี้**: ระดับความสำคัญของเครื่อง จาก Consequence x Likelihood (RBMM)
> 2. **ISO 14224 failure impact**: critical / degraded / incipient คือผลของ failure หนึ่งครั้งต่อ function ของ equipment ตัวนั้น (ISO 14224 cl. 3.28, p.6)
> 3. **ISO/TR 12489 safety critical failure**: dangerous failure ที่ทำให้ safety function ใช้ไม่ได้ทั้งหมด ถ้ามี redundancy ต้องคำนึงถึงตัวสำรองด้วย (ISO 14224 cl. F.4.1, p.253-254)
>
> ทั้งสามเป็นคนละแกน เครื่อง criticality A ไม่ได้แปลว่าทุก failure เป็น critical ตาม ISO ดู [[Failure Impact Classification]] และ [[Safety Critical Failure Classification]] เป็นความต่างของความหมาย ไม่ใช่ข้อขัดแย้งของข้อมูล

## สูตรและการแบ่งระดับ (RBMM p.116-118)

```
Criticality Score = Consequence (1-5) x Likelihood (1-6)     ช่วง 1-30
Score 15-30  -> Criticality 1 = A (High)
Score  5-12  -> Criticality 2 = B (Moderate)
Score  1-4   -> Criticality 3 = C (Low)
```

หมายเหตุ (derived): ผลคูณของจำนวนเต็ม 1-5 กับ 1-6 ไม่มีทางได้ 13 และ 14 จึงไม่มีช่องว่างจริงระหว่างช่วง 5-12 กับ 15-30

Criticality Matrix (Fig 5.3, p.118): แกนตั้ง Likelihood 1 (Remote) - 6 (Very High) x แกนนอน Consequence 1 (Very Low) - 5 (Very High) ค่าเซลล์คือผลคูณ ตัวอย่างในหนังสือ: L6xC3 = 18 High; L4xC4 = 16 High; L3xC4 = 12 Moderate; L2xC5 = 10 Moderate; L1xC5 = 5 Moderate; L5xC5 = 25; L6xC5 = 30

## Commercial (Fig 5.2, RBMM p.117)

Consequence:

| Score | ระดับ | เกณฑ์ |
|---|---|---|
| 5 | สูงมาก | หยุดสายผลิต > 24 ชม. หรือ ค่าผลิต+ซ่อมสูญเสีย > 500,000 |
| 4 | สูง | หยุดสายผลิต > 12 และ < 24 ชม. หรือ > 100,000 และ < 500,000 |
| 3 | ปานกลาง | หยุดผลิตบางส่วน > 8 และ < 12 ชม. หรือ > 10,000 และ < 100,000 |
| 2 | ต่ำ | หยุดผลิตบางส่วน < 8 ชม. หรือ > 1,000 และ < 10,000 |
| 1 | ต่ำมาก | ไม่กระทบสายผลิต หรือ ค่าซ่อม < 1,000 |

หน่วยเงินไม่ระบุในภาพ [อ่านไม่ออกชัด]

Likelihood (ภาพเบลอ) ใช้อายุใช้งานได้ก่อนเสีย:

| Score | ระดับ | อายุก่อนเสีย |
|---|---|---|
| 6 | สูงมาก | ไม่เกิน 3 เดือน |
| 5 | สูง | > 3 เดือน ถึง 1 ปี |
| 4 | ปานกลาง | > 1 ถึง 3 ปี |
| 3 | ต่ำ | > 3 ถึง 5 ปี |
| 2 | ต่ำมาก | > 5 ถึง 10 ปี |
| 1 | น้อยมาก | > 10 ปี |

## Safety (Fig 5.4, RBMM p.118)

| Score | Consequence | Score | Likelihood |
|---|---|---|---|
| 5 | สูญเสียชีวิต อวัยวะ พิการ | 6 | อย่างน้อย 1 ครั้ง/ปี |
| 4 | บันทึกเป็นการสูญเสียเวลา (lost-time) | 5 | มากกว่า 1 ครั้งใน 5 ปี |
| 3 | บันทึกเป็นอุบัติเหตุได้ (recordable) | 4 | N.A. |
| 2 | บาดเจ็บ ต้องปฐมพยาบาล | 3 | ครั้งเดียวใน 5 ปี |
| 1 | ไม่กระทบความปลอดภัย | 2 | N.A. |
| | | 1 | ไม่เคยมีรายงาน |

## Environment (Fig 5.5, RBMM p.119)

Consequence: 5 สารพิษอาจเกิน 500 หน่วยวัด หรือกระทบโรงงานอื่น/ผิดข้อบังคับ; 4 อาจเกิน 200 หน่วย ต้องขอความช่วยเหลือภายนอก; 3 อาจเกิน 20 หน่วย แต่หน่วยงานภายในรับมือได้; 2 สารพิษเล็กน้อย ไม่ต้องรายงาน; 1 ไม่มีผล Likelihood ใช้สเกล 1-6 เดียวกับ Safety

Fig 5.6 (p.120): ตารางสรุป 3 คอลัมน์ (Commercial, Safety, Environment แต่ละอัน 1-3) ต่อ Equipment เพื่อ sort ตามประเด็น

## กลยุทธ์ตามระดับ (Fig 1.5 RBMM p.26; Fig 10.32 p.316)

| ระดับ | แนวทาง | Scheduled PM | Spare Parts |
|---|---|---|---|
| A High | 100% RCM Tasks (Zero Breakdown) | 100% RCM tasks, ตัด unreliable incidence, intensive failure finding, ยอมรับ multiple failure probability ได้ | 100% service level, 0% stock out |
| B Medium | Pro-active | ตัด PM ที่ไม่ได้ผล, PM optimum | ลดสต๊อก, ดู % service level / stock out |
| C Low | Re-active | ตัด PM ไม่จำเป็น, PM optimum, RTF | ลดสต๊อก, ดู % service level / stock out |

ตัวเลขเพิ่มเติม (RBMM บท 10 p.315-319): A คำนวณงบ CM-Unplanned ด้วย Confidence Level > 95% ว่าจะไม่เกิดเลย; B Confidence 90% ระดับอะไหล่ปานกลาง Service Factor 100%; C Confidence 80-90% ปล่อย RTF ดู [[Maintenance Budget]] (คำว่า "ROM" ใน Fig 10.32 น่าจะหมายถึง RCM อ่านจากภาพ)

## Dynamic of Criticality (RBMM p.23-25)

- Criticality เปลี่ยนตามเวลา ขึ้นกับ Stress, Resistance และแผนบำรุงรักษา
- Fig 1.4: สัดส่วนเครื่อง A/B/C = 30% / 50% / 20% (ตัวอย่างสมมติของหนังสือ ไม่ใช่ค่ามาตรฐาน) สถานะ 1 Beginning (เสียทุกระดับ รวม A) -> 2 Intermediate (เสียที่ B/C) -> 3 Target (เสียที่ C/B ที่ไม่ทำให้โรงงานหยุด = Zero Plant Down Time)

## Boundary, Redundancy และ Process (RBMM p.28-30)

- ไม่มี redundancy: เครื่องอนุกรมทุกตัวเป็น A (Fig 1.6); มี redundancy: กลุ่มขนานอาจเป็น A/B/C (Fig 1.7)
- ตัวอย่าง 3 เครื่องรับภาระได้ 50% ต่อเครื่อง: Standby (ใช้ 2 สำรอง 1) vs Load Sharing (แต่ละเครื่อง 1/3 พร้อมรับเพิ่มถึง 50%)
- ระดับไม่ลดเป็นต่ำกว่า A อัตโนมัติ: เครื่อง Standby อาจเสียแบบ Hidden แล้วเกิด Multiple Failure
- ถังเก็บระหว่าง process ลด criticality ภาพรวม (Fig 1.8)
- ตั้งงบเป็นกรอบ process จัดลำดับในแต่ละกรอบแล้วรวม ดู [[Redundancy and Standby Systems]] และ [[Reliability Block Diagram]]

## Part Criticality สำหรับอะไหล่ (RBMM p.243-246)

- Equipment Criticality = Commercial + Safety + Environment; Part Criticality = Price, Lead Time, Failure Detect-ability (CBM) (Fig 9.5) ให้คะแนน Cost/LT/CBM 1 = สูงสุด 2 = กลาง 3 = ต่ำ (CBM ต่ำ = ตรวจอาการล่วงหน้าไม่ได้)
- กฎ: อะไหล่ใช้ร่วมเครื่องต่างระดับ -> criticality อะไหล่ = ระดับสูงสุดของเครื่องที่ใช้
- Fig 9.6 ตารางนับจำนวนชิ้นในเครื่อง A/B/C จาก BOM [ตัวเลขรายแถวอ่านไม่ออก]
- ดู [[Spare Part Criticality and Risk]] และ [[Spare Parts Management]]

## มุมมอง CMRP: risk matrix 5 x 5 และ RPN bands (เพิ่ม 2026-10-25)

สไลด์ [[CMRP Course]] ใช้ convention ต่างจาก RBMM (ความต่างของสเกล ไม่ใช่ข้อขัดแย้ง; ตารางเทียบเต็มใน [[CMRP vs RBMM FMECA Scales]])

- นิยาม: อุปกรณ์ critical เมื่อผลของ failure มีนัย ทนไม่ได้ ไม่มี redundancy หรือผลนั้นครอบงำปัจจัยอื่น; สไลด์ตั้งคำถามว่าควรให้เครดิต redundancy หรือไม่ (ตัวอย่าง level indicator 3 ตัว) (CMRP CMPR-02 p.28) สอดคล้องกับหัวข้อ Boundary, Redundancy ด้านบน
- ขั้นตอน: ไล่ทุก functional failure -> component ที่เป็นเหตุ -> FM เด่นและผล -> criticality matrix; ทนไม่ได้ = critical, ทนได้ = non-critical, บันทึกเหตุผลใน Remarks (CMRP CMPR-02 p.29)
- ตาราง importance 3 ระดับ (High/Moderate/Low) 6 มิติ: availability, production rate, quality, safety, environment, cost (CMRP CMPR-02 p.30) มากกว่า 3 มิติของ RBMM (Commercial, Safety, Environment) ข้อผิดพลาดในสไลด์: availability High = "96" และ Medium = "96-98" ขอบ 96 ซ้ำสองระดับ ควรอ่าน High ว่า "ต่ำกว่า 96"
- **Risk = Probability x Effect** โดย effect ประเมินภายใต้ "realistic scenario" ที่ทีมตกลงกัน แยก availability/safety/environment/cost (CMRP CMPR-02 p.31-32)
- **Risk matrix 5 x 5** (CMRP CMPR-02 p.32): Effect 1-5 (no, negligible, marginal, critical, catastrophic) x Probability 1-5 (1/25 ปี, 1/10 ปี, 1/5 ปี, 1/ปี, 1/เดือน) ค่าเซลล์ = ผลคูณ 1-25; band Low 1-3, Medium 4-9, High 10-25
  - เทียบ RBMM: 5 x 6 คะแนน 1-30 band C 1-4 / B 5-12 / A 15-30 จึงเทียบคะแนนข้ามระบบตรง ๆ ไม่ได้
  - ข้อบกพร่อง: แถว "No effects" ที่ probability 1/ปี และ 1/เดือน (ค่า 4, 5) ถูกระบายเป็น Medium ทั้งที่ไม่มีผลกระทบ ขัดกับความหมายของ Risk = P x Effect
- Policy ตาม band (CMRP CMPR-02 p.33): Low = ไม่ทำ preventive; Medium/High = ทำ preventive ต่างกันที่ระดับ เช่น การสำรองอะไหล่ (เทียบได้กับ A/B/C ในหัวข้อ "กลยุทธ์ตามระดับ")
- **RPN bands** (CMRP CMPR-02 p.33): None 0, Low 8-40, Medium 80-240, High 320-1,000 มีข้อบกพร่อง: "None = 0" เป็นไปไม่ได้ (RPN ต่ำสุด = 1), ช่วง 1-7, 41-79, 241-319 ไม่ถูกจัดระดับทั้งที่เกิดได้จริง (derived) จึงไม่ควรใช้ตามที่พิมพ์โดยไม่กำหนดช่วงที่หายไป
- สไลด์ใช้คำว่า criticality กับ risk/RPN สลับกันโดยไม่นิยามแยก (CMRP CMPR-02 p.31-33) เพิ่มความหมายที่ 4 ให้คำว่า "critical" นอกเหนือจาก 3 ความหมายใน callout ด้านบน: ในสไลด์ CMRP "critical" = ผลยอมรับไม่ได้ ต้องมีมาตรการ (CMRP CMPR-03 p.5) ซึ่งใกล้กับ A/B/C ของ RBMM
- Total organizational risk: Risk = Threats x Vulnerabilities x Impact และ Composite Risk Index = Impact x Probability x Detectability (CMRP CMPR-02 p.36) โครงเดียวกับ RPN

## ใช้ใน RCM

กระบวนการ 2 ของ [[RCM Reliability Centered Maintenance]]: เลือกเครื่องจักร/กรอบตาม criticality ก่อน แล้วค่อยลง Function และ FM Fast Track RCM ถือว่า criticality ของ equipment อยู่นอกกระบวนการ ผู้ใช้เลือกกรอบเอง (RBMM p.150) ระดับ equipment ละเอียดขึ้นด้วย [[FMECA]]

## ข้อควรระวัง

- ฟิลด์ Criticality ใน Equipment Database เชื่อมกับ Maintenance Strategy (Fig 4.3, RBMM p.96) ดู [[CMMS]]
- Likelihood ของ Commercial อิงอายุก่อนเสีย ต้องมีประวัติ ถ้าไม่มี (โรงงานใหม่) ใช้ความรู้ผู้ออกแบบ/ผู้ผลิต หรือ FMECA (RBMM p.137)
- คะแนน Safety/Environment ควรแยกพิจารณา ไม่ถูกกลบด้วย Commercial: ตัวอย่างหนังสือแสดงตารางแยกคอลัมน์ (Fig 5.6) แต่ไม่ระบุกฎรวมคะแนน (ไม่มีใน sources)

## เชื่อมโยงกับ compressor failure hierarchy

- Criticality ให้กับระดับ [[Compressor]] (equipment) ตาม consequence ต่อ production/safety/environment ส่วน Likelihood ประมาณจากประวัติเสีย; wiki ไม่มีข้อมูลเสียของ asset Valeura (นอกขอบเขตตาม SCHEMA) จึงยังไม่มีการจัดระดับจริง
- ในระดับ sub unit/[[Maintainable Item]] ใช้ [[Failure Mode]] ที่มี consequence สูง เช่น ELP (รั่ว process medium ที่อาจกระทบ Safety/Environment ดู [[ELP External Leakage Process Medium]]) เทียบกับ ELU ([[ELU External Leakage Utility Medium]]) เป็นการตีความ ไม่ใช่ข้อมูลในหนังสือ
- อะไหล่ของ compressor ที่ lead time ยาว/ราคาสูง/ตรวจล่วงหน้าไม่ได้ ได้ Part Criticality สูงตาม Fig 9.5

## ดูเพิ่ม

- [[RCM Reliability Centered Maintenance]]
- [[FMECA]]
- [[Spare Part Criticality and Risk]]
- [[Maintenance Budget]]
- [[Asset Life Cycle]]
- [[CMRP vs RBMM FMECA Scales]]

## Triplets

- [[Criticality Assessment]] [produces:: Criticality A] High, Criticality 1 (RBMM p.116-118)
- [[Criticality Assessment]] [produces:: Criticality B] Moderate, Criticality 2 (RBMM p.116-118)
- [[Criticality Assessment]] [produces:: Criticality C] Low, Criticality 3 (RBMM p.116-118)
- [[Criticality Assessment]] [defined_in:: Mil-Std-1629] follows FMECA approach; thresholds are adjustable examples (RBMM p.116-117)
- [[Criticality Assessment]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 5
- Criticality Score [has_formula:: Consequence (1-5) x Likelihood (1-6)] range 1-30 (RBMM p.116-118)
- Criticality Score [has_parameter:: Consequence]
- Criticality Score [has_parameter:: Likelihood]
- Criticality A [has_value:: 15-30] Criticality Score range (RBMM p.116-118)
- Criticality B [has_value:: 5-12] Criticality Score range (RBMM p.116-118)
- Criticality C [has_value:: 1-4] Criticality Score range (RBMM p.116-118)
- Criticality Score [has_value:: no 13 or 14] integer products 1-5 x 1-6 cannot equal 13 or 14, derived [confidence:: low]
- [[Criticality Assessment]] [has_category:: Commercial] (RBMM p.116-117)
- [[Criticality Assessment]] [has_category:: Safety] (RBMM p.118)
- [[Criticality Assessment]] [has_category:: Environment] (RBMM p.119)
- Criticality Matrix [has_value:: L6xC3 = 18 High] book example; also L4xC4 = 16 High, L3xC4 = 12 Moderate, L2xC5 = 10 Moderate, L1xC5 = 5 Moderate (Fig 5.3, p.118)
- Commercial Consequence 5 [has_value:: line stop > 24 h or loss > 500,000] currency not stated (Fig 5.2, RBMM p.117)
- Commercial Consequence 4 [has_value:: line stop 12-24 h or 100,000-500,000] (Fig 5.2)
- Commercial Consequence 3 [has_value:: partial stop 8-12 h or 10,000-100,000] (Fig 5.2)
- Commercial Consequence 2 [has_value:: partial stop < 8 h or 1,000-10,000] (Fig 5.2)
- Commercial Consequence 1 [has_value:: no line impact or repair < 1,000] (Fig 5.2)
- Commercial Likelihood 6 [has_value:: life before failure up to 3 months] image blurred (Fig 5.2)
- Commercial Likelihood 5 [has_value:: > 3 months to 1 year] (Fig 5.2)
- Commercial Likelihood 4 [has_value:: > 1 to 3 years] (Fig 5.2)
- Commercial Likelihood 3 [has_value:: > 3 to 5 years] (Fig 5.2)
- Commercial Likelihood 2 [has_value:: > 5 to 10 years] (Fig 5.2)
- Commercial Likelihood 1 [has_value:: > 10 years] (Fig 5.2)
- Safety Consequence [has_value:: 1-5] 5 fatality/limb loss/disability, 4 lost-time, 3 recordable, 2 first aid, 1 no safety impact (Fig 5.4, RBMM p.118)
- Safety Likelihood [has_value:: 1-6] 6 at least once per year, 5 more than once in 5 years, 3 once in 5 years, 1 never reported; 4 and 2 N.A. (Fig 5.4)
- Environment Consequence [has_value:: 1-5] 5 may exceed 500 units or affect others/regulation, 4 over 200 needs outside help, 3 over 20 handled internally, 2 minor not reportable, 1 none (Fig 5.5, RBMM p.119)
- Environment Likelihood [alias_of:: Safety Likelihood] same 1-6 scale (Fig 5.5)
- Criticality A [uses:: 100% RCM Tasks] Zero Breakdown, intensive failure finding (Fig 1.5 RBMM p.26; Fig 10.32 p.316)
- Criticality B [uses:: Pro-active] remove ineffective PM, PM optimum (Fig 1.5; Fig 10.32)
- Criticality C [uses:: Re-active] remove unnecessary PM, PM optimum, Run to Failure (Fig 1.5; Fig 10.32)
- Criticality A [has_value:: 100% service level] spare parts, 0% stock out (Fig 1.5)
- Criticality A [has_value:: > 95%] confidence level that CM-Unplanned will not occur, for budget (RBMM ch10 p.315-319)
- Criticality B [has_value:: 90%] confidence level, service factor 100% (RBMM ch10 p.315-319)
- Criticality C [has_value:: 80-90%] confidence level, Run to Failure (RBMM ch10 p.315-319)
- Criticality A [has_value:: 30%] share of machines, hypothetical book example (Fig 1.4, RBMM p.23-25)
- Criticality B [has_value:: 50%] share of machines, hypothetical (Fig 1.4)
- Criticality C [has_value:: 20%] share of machines, hypothetical (Fig 1.4)
- Equipment Criticality [depends_on:: Stress] changes over time; also Resistance and maintenance plan (RBMM p.23-25)
- Equipment Criticality [has_formula:: Commercial + Safety + Environment] (Fig 9.5, RBMM p.243-246)
- Series Equipment [has_category:: Criticality A] no redundancy (Fig 1.6, RBMM p.28-30)
- Standby Equipment [depends_on:: Hidden Failure] not automatically below A; hidden failure can lead to Multiple Failure (RBMM p.28-30)
- Load Sharing [differs_from:: Standby] 3 machines at 50% each: standby 2+1 vs each 1/3 able to take up to 50% (RBMM p.28-30)
- Buffer Tank [related_to:: Equipment Criticality] reduces overall criticality (Fig 1.8)
- Part Criticality [has_parameter:: Price] score 1 highest to 3 low (Fig 9.5, RBMM p.243-246)
- Part Criticality [has_parameter:: Lead Time] (Fig 9.5)
- Part Criticality [has_parameter:: Failure Detect-ability] CBM; low = cannot detect in advance (Fig 9.5)
- Part Criticality [depends_on:: Equipment Criticality] shared part takes highest criticality of using equipment (RBMM p.243-246)
- [[Criticality Assessment]] [differs_from:: [[Failure Impact Classification]]] A/B/C equipment importance vs ISO critical/degraded/incipient per failure (ISO 14224 cl. 3.28, p.6)
- [[Criticality Assessment]] [differs_from:: [[Safety Critical Failure Classification]]] vs ISO/TR 12489 dangerous failure of safety function (ISO 14224 cl. F.4.1, p.253-254)
- [[Criticality Assessment]] [step_of:: [[RCM Reliability Centered Maintenance]]] process 2; Fast Track RCM treats it as outside the process (RBMM p.150)
- Equipment Criticality [input_to:: Maintenance Strategy] Criticality field of Equipment Database in CMMS (Fig 4.3, RBMM p.96)
- Likelihood [depends_on:: [[FMECA]]] when no history, e.g. new plant; or designer/manufacturer knowledge (RBMM p.137)
- [[Criticality Assessment]] [applies_to:: [[Compressor]]] equipment level; no Valeura failure data so no actual ranking
- [[Criticality Assessment]] [defined_in:: [[CMRP Course]]] CMRP risk matrix and RPN bands (CMRP CMPR-02 p.28-33)
- CMRP Risk [has_formula:: Probability x Effect] effect under agreed realistic scenario (CMRP CMPR-02 p.31-32)
- CMRP Risk Matrix [has_value:: 5 x 5, max 25] Effect 1-5 x Probability 1-5, 1 per 25 years to 1 per month (CMRP CMPR-02 p.32)
- CMRP Risk Matrix [has_value:: Low 1-3, Medium 4-9, High 10-25] (CMRP CMPR-02 p.32)
- CMRP Risk Matrix [differs_from:: Criticality Score] 5 x 5 max 25 vs RBMM 5 x 6 max 30
- CMRP Risk Matrix [has_value:: No effects row coloured Medium] cells 4 and 5, slide flaw (CMRP CMPR-02 p.32)
- CMRP Low Risk [selects:: No Preventive Maintenance] Medium/High get preventive of different level, e.g. spares (CMRP CMPR-02 p.33)
- CMRP RPN Band [has_value:: None 0, Low 8-40, Medium 80-240, High 320-1,000] (CMRP CMPR-02 p.33)
- CMRP RPN Band [has_value:: gaps 1-7, 41-79, 241-319] None = 0 impossible, derived
- CMRP Importance Table [has_category:: availability, production rate, quality, safety, environment, cost] 3 levels High/Moderate/Low (CMRP CMPR-02 p.30)
- Composite Risk Index [has_formula:: Impact x Probability x Detectability] (CMRP CMPR-02 p.36)
- Organizational Risk [has_formula:: Threats x Vulnerabilities x Impact] (CMRP CMPR-02 p.36)

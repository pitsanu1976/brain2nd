---
title: CMRP Course
created: 2026-10-25
updated: 2026-10-25
type: entity
tags: [cmrp, maintenance-management, reliability, work-management]
sources: [cmrp.md, reliability-based-maintenance-management.md, iso-14224.md]
confidence: medium
contested: false
---

# CMRP Course — สไลด์หลักสูตร PETROSYNC

hub ของชุดสไลด์หลักสูตรเตรียมสอบ CMRP (Certified Maintenance & Reliability Professional) ของ PETROSYNC ที่ ingest เข้า wiki เมื่อ 2026-10-25 เนื้อหาครอบคลุมกว้างตาม SMRP Body of Knowledge ตั้งแต่ inspection, lubrication, condition monitoring, FMECA/RCM, RCA, KPI, business case, TPM, RAMS, สถิติ, SPC, อะไหล่ ไปจนถึง work management และ turnaround หน้านี้บอกว่าแต่ละไฟล์ไปอยู่หน้าไหนใน wiki, รวมข้อผิดพลาดของสไลด์ และอธิบายความสัมพันธ์กับ [[Reliability Based Maintenance Management Book]] และ [[ISO 14224]] ข้อความทั้งหมดถอดความจาก reading notes ไม่ใช่ข้อความต้นฉบับ

## ข้อมูลแหล่งที่มา

- ผู้จัดทำ: PETROSYNC ผู้ให้บริการฝึกอบรม เป็นเอกสารประกอบหลักสูตร CMRP ตาม SMRP BOK 5 pillars
- ไฟล์: 11 ไฟล์ (CMPR-01 ถึง CMPR-11; ชื่อไฟล์ต้นฉบับสะกด "CMPR") รวม 408 หน้า PDF ส่วนใหญ่ 2 slide ต่อหน้า
- รูปแบบ: สแกนจากเครื่องถ่ายเอกสาร มี OCR หยาบและลายมือเขียนทับบางหน้า ตาราง สูตร และผังตรวจจากภาพ ลายมือที่อ่านไม่ออกไม่ถูกบันทึก
- ลิขสิทธิ์: PDF เก็บในเครื่องเท่านั้น (`raw/CMRP/*.pdf` อยู่ใน `.gitignore`) เพราะ vault sync ไป GitHub ที่ sync คือ reading notes ถอดความ `raw/CMRP/CMPR-XX.md` และหน้า raw [[raw/cmrp]] (sha256 ต่อไฟล์อยู่ในตารางของหน้านั้น)
- การอ้างอิง: `(CMRP CMPR-0X p.N)` โดย N = เลขหน้า PDF ไม่ใช่เลข slide ที่พิมพ์มุมล่าง
- ลำดับไฟล์ไม่ตรงกับ pillar เสมอ หลายไฟล์ผสมหลายหัวข้อ และ CMPR-09 ขาด slide 340-343 (CMRP CMPR-09 p.33-34)

## SMRP Body of Knowledge 5 pillars (CMRP CMPR-01 p.2-3)

| Pillar | ขอบเขตโดยย่อ (ตาม slide) | หน้าใน wiki ที่ใกล้ที่สุด |
|---|---|---|
| 1 Business and Management | ทิศทางและแผนกลยุทธ์ M&R, วัดผล, สื่อสาร stakeholder, ความเสี่ยง EHS (1.1-1.6) | [[Maintenance KPIs]], [[Maintenance Business Case]], [[Maintenance Budget]] |
| 2 Manufacturing Process Reliability | เข้าใจกระบวนการ, เทคนิคปรับปรุง, MOC, คุมตามมาตรฐาน/กฎหมาย (2.1-2.4) | [[Statistical Process Control]], [[TPM and Lean Maintenance]] |
| 3 Equipment Reliability | ตั้งความคาดหวัง reliability, ประเมิน, วางแผนเครื่องเดิม/ใหม่, cost-justify, ทบทวนกลยุทธ์ (3.1-3.7) | [[RCM Reliability Centered Maintenance]], [[FMECA]], [[Weibull Analysis]], [[Reliability Allocation]] |
| 4 Organization & Leadership | ขีดความสามารถองค์กร, โครงสร้าง, พัฒนาคน, นำคน | [[Human Reliability]], [[Turnaround Management]] |
| 5 Work Management | ระบุ/อนุมัติงาน, จัดลำดับ, plan, schedule, execute, document, วัดผล, IT, วัสดุ (5.1-5.11) | [[Maintenance Planning and Scheduling]], [[Maintenance Backlog and Schedule Compliance]], [[CMMS]] |

ข้อผิดในสไลด์: pillar 4 เริ่มที่ข้อ 4.2 ไม่มีข้อ 4.1 (ยืนยันจากภาพ CMRP CMPR-01 p.2) ตาม SMRP BOK ทั่วไปข้อ 4.1 คือการกำหนดความต้องการขององค์กร (ความรู้ทั่วไป ไม่อยู่ในสไลด์, confidence low)

## AEO Model (CMRP CMPR-01 p.1)

ผังที่ผู้สอนใช้เป็นแกนของหลักสูตร มี 4 ชั้นจากบนลงล่าง และมีลูกศรป้อนกลับจากชั้นล่างขึ้นชั้นบน ทำให้โปรแกรมบำรุงรักษาเป็น "living program"

```
Maintenance Strategy   Business Goals -> Maintenance Strategy Project, Reliability Issues (Design),
                       Pre-Defined Priorities -> Plant Asset Management and Maintenance Program
                       = PM / PRM / ODR / RTF  (+ RCFA กำกับข้าง)
        |
Work Identification    PRM/ODR collection and analysis -> information integration and decision
                       -> Work Order generation  (+ Corrective Maintenance จาก operator/initiator)
        |
Work Control           Planning (standard job plans, spare parts alignment) -> Rolling Schedule
        |
Work Execution         Work Execution -> Post Maintenance Testing -> Update Program -> (กลับขึ้นบน)
```

- PM = Preventive Maintenance แบบ time based
- PRM = Proactive Reliability Maintenance (ในโมเดลนี้รวม predictive และ corrective)
- ODR = Operator Driven Reliability (จากการสังเกตของ operator แยกเป็นสายงานของตัวเอง)
- RTF = Run to Failure (เลือกอย่างเป็นทางการได้)
- RCFA = Root Cause Failure Analysis ดู [[Root Cause Analysis]]

สไลด์เดียวกันยังให้วงจร Basic Maintenance Management Process 6 ขั้น: Work Identification -> Plan -> Schedule -> Execute -> Record History -> Analyze for Improvement (CMRP CMPR-01 p.4) ซึ่งสอดคล้องกับชั้น 3 Work Control ของ [[Maintenance Efficacy Pyramid]]

ข้อระวังศัพท์: คำว่า "Proactive" ใน [[Asset Life Cycle]] (RBMM) รวม predictive + preventive แต่ PRM ของ AEO รวม predictive + corrective คำคล้ายกันแต่ขอบเขตต่างกัน และในรายการคำย่อ "RM" ถูกใช้สองความหมาย (Reactive Maintenance และ Reliability and Maintenance) (CMRP CMPR-01 p.3)

## แผนที่ไฟล์ -> หน้า wiki

| ไฟล์ | หน้า PDF | หัวข้อหลัก | หน้าใน wiki |
|---|---|---|---|
| CMPR-01 | 50 | AEO model, SMRP BOK, คำนิยาม, inspection 4 boundaries, failure pattern %, D-I-P-F curve, lubrication, vibration (ISO 10816-1) | หน้านี้, [[Lubrication and Oil Analysis]], [[Condition Monitoring Techniques]], [[P-F Interval and Condition Monitoring]], [[Failure Patterns and Bathtub Curve]], [[Reliability Metrics]] |
| CMPR-02 | 52 | wear mechanisms, base oil/additive, oil/grease tests, thermography, motor current, ultrasonic, criticality/risk matrix, LCC, FMEA types, MIL-STD-1629A | [[Wear Mechanisms]], [[Lubrication and Oil Analysis]], [[Condition Monitoring Techniques]], [[Criticality Assessment]], [[FMECA]], [[CMRP vs RBMM FMECA Scales]] |
| CMPR-03 | 50 | FMECA scale, decision tree RtF/FFM/SM/CBM/MOD, สูตรคาบ PM, spare decision, RCA (5 Whys, why-because), SMART, KPI, balanced scorecard, business case vs plan | [[FMECA]], [[CMRP vs RBMM FMECA Scales]], [[PM Task Selection]], [[P-F Interval and Condition Monitoring]], [[Failure Finding Interval]], [[Spare Part Criticality and Risk]], [[Root Cause Analysis]], [[Maintenance KPIs]], [[Maintenance Business Case]] |
| CMPR-04 | 47 | business case 6 ขั้น, Lean/TPM/5S/SMED/Six Sigma, RAMS, availability Ai/Aa/Ao, maintainability, PM/CM, NF X60-000, RBD, reliability allocation | [[Maintenance Business Case]], [[TPM and Lean Maintenance]], [[Availability and OEE]], [[Censored Data]], [[Maintainability]], [[PM Interval Optimization]], [[Reliability Block Diagram]], [[Reliability Allocation]] |
| CMPR-05 | 3 | reliability allocation ด้วย cost/penalty function, feasibility | [[Reliability Allocation]] |
| CMPR-06 | 48 | apportionment (equal, ARINC), ทบทวนสถิติ, Weibull case study, PM optimization C2/C1, Markov, Monte Carlo, SPC เบื้องต้น | [[Reliability Allocation]], [[Statistical Distributions for Maintenance]], [[Weibull Analysis]], [[PM Interval Optimization]], [[Monte Carlo Maintenance Simulation]], [[Statistical Process Control]] |
| CMPR-07 | 2 | X-bar/R control chart | [[Statistical Process Control]] |
| CMPR-08 | 50 | attribute charts, capability Cp/Cpk, CI; digitization/predictive modelling; risk-based spares, MRO inventory models; wrench time | [[Statistical Process Control]], [[Digital Maintenance and Predictive Analytics]], [[Spare Part Criticality and Risk]], [[EOQ and Reorder Point]], [[Maintenance Planning and Scheduling]] |
| CMPR-09 | 46 | planning vs scheduling, planning 7 ขั้น, span of control, estimating, priority PR1-PR4, weekly schedule, backlog | [[Maintenance Planning and Scheduling]], [[Maintenance Backlog and Schedule Compliance]] |
| CMPR-10 | 30 | backlog 3-6 สัปดาห์, schedule compliance/performance/effectiveness, turnaround strategy, work list golden rule | [[Maintenance Backlog and Schedule Compliance]], [[Maintenance KPIs]], [[Turnaround Management]] |
| CMPR-11 | 30 | turnaround 4 phases, human reliability, culture change, reliability growth (Duane, Crow-AMSAA), FTA | [[Turnaround Management]], [[Human Reliability]], [[Reliability Growth Models]], [[Fault Tree Analysis]], [[Reliability Block Diagram]] |

## ข้อผิดพลาดในสไลด์ (รวมทุกไฟล์)

เป็นข้อผิดภายในสไลด์ ไม่ใช่ความขัดแย้งกับ RBMM หรือ ISO จึงไม่ตั้ง contested ค่าที่ถูกส่วนใหญ่ derived (คำนวณใหม่ใน reading notes) รายละเอียดอยู่ในหน้าที่เกี่ยวข้อง

| ไฟล์ (หน้า) | สไลด์เขียน | ค่าที่ถูก / หมายเหตุ | หน้า wiki |
|---|---|---|---|
| CMPR-01 p.2 | SMRP pillar 4 เริ่มที่ 4.2 | ขาดข้อ 4.1 | หน้านี้ |
| CMPR-01 p.4 | สูตร maintainability พิมพ์เพี้ยน | M(t) = 1 - e^(-μt), μ = 1/MTTR | [[Reliability Metrics]], [[Maintainability]] |
| CMPR-01 p.30 | คำอธิบายขั้น Correction คัดลอกจากขั้น Analysis | ไม่มีคำอธิบาย Correction จริง | [[Condition Monitoring Techniques]] |
| CMPR-01 p.41 | upper limit 0.3 in/s คู่กับ 5.0 mm/s | 0.3 in/s = 7.6 mm/s; 5.0 mm/s = 0.2 in/s | [[Condition Monitoring Techniques]] |
| CMPR-02 p.30 | availability band High = 96, Medium = 96-98 | High ควรเป็น ต่ำกว่า 96 (ขอบ 96 ซ้ำ) | [[Criticality Assessment]] |
| CMPR-02 p.41 | PFMEA RPN 382 และ 40, แถว 1 หลังแก้ 70 | 7x8x7 = 392, 7x1x7 = 49, 7x2x6 = 84 | [[FMECA]] |
| CMPR-02 p.49 | criticality index = S + P, "3 วิธี" แต่แสดง 2 | ขัดกับการคูณใน p.32-33 ของไฟล์เดียวกัน | [[CMRP vs RBMM FMECA Scales]] |
| CMPR-03 p.1 | หัวคอลัมน์ "Effect" ในตาราง probability | ควรเป็น probability; คำอธิบายบาง rank ซ้ำกัน | [[CMRP vs RBMM FMECA Scales]] |
| CMPR-03 p.7 | decision tree กิ่ง CFI = No ไปที่ SM | ทั้งสองกิ่งได้ SM คำถาม CFI จึงไม่มีผล | [[PM Task Selection]] |
| CMPR-03 p.40-41 | world class 12 ต่ำกว่า industry lowest 15 | ขัดกันเชิงตรรกะ | [[Maintenance KPIs]] |
| CMPR-04 p.16 | ผลรวมแสดง 9 ค่า | คำตอบ MTTF 153.8 h ถูกเมื่อรวมครบ 10 ค่า | [[Reliability Metrics]] |
| CMPR-04 p.26 | แถว MTTR เขียน MTTF, mean = ∫f(t)dt | mean = ∫t·f(t)dt และ ∫t·g(t)dt | [[Maintainability]] |
| CMPR-04 p.44 | RBD ผลรวม 0.541 | 0.905 x 0.832 x 0.861 = 0.648 | [[Reliability Block Diagram]] |
| CMPR-06 p.18 | ถ้า x เป็น exponential แล้ว 1/x เป็น Poisson | เวลาระหว่างเหตุของ Poisson process เป็น exponential | [[Statistical Distributions for Maintenance]] |
| CMPR-06 (case study) | half-life ต่างกัน "สองอันดับขนาด" | ราว 18-26 เท่า คือราวหนึ่งอันดับ | [[Weibull Analysis]] |
| CMPR-07 | UCL_R = 2.11 x 3.6 = 7.5 | ผลคูณ 7.6 (chart ใช้ 7.6) | [[Statistical Process Control]] |
| CMPR-08 p.14 | CI ใช้ S = 1.02 (หาร n) | sample SD หาร n-1 ได้ s ประมาณ 1.18, CI ประมาณ 26.20-29.95 | [[Statistical Process Control]] |
| CMPR-08 p.42 | ตาราง 2x2 ของ inventory model | ขัดกับรายละเอียด p.43-45 | [[EOQ and Reorder Point]] |
| CMPR-08 p.48-49 | ฐาน wrench time 12 กับ 15 ชม. ปนกัน | ฐาน 12 ชม. ได้ +1.2 ชม./คน และ 7.5 คน | [[Maintenance Planning and Scheduling]] |
| CMPR-10 p.30 | ความรู้ "five" ประเภท | รายการมี 6 ประเภท | [[Turnaround Management]] |
| CMPR-11 p.18 | 19 CFR 1910.119 | 29 CFR 1910.119 (ความรู้ทั่วไป) | [[Fault Tree Analysis]] |

ข้อสังเกตอื่นที่ไม่ใช่ตัวเลขผิดแต่ควรระวัง: สัดส่วน failure pattern 2/4/26/68% (CMRP CMPR-01 p.28) เป็นการยุบ 6 pattern ของ Nowlan & Heap โดยไม่บอกแหล่ง และ CMPR-03 p.5 อ้างอีกตัวเลขหนึ่ง (ราว 60% มีแค่ช่วง infant + random) ดู [[Failure Patterns and Bathtub Curve]]; ตัวอย่างบางชุดไม่ใช่งานบำรุงรักษา (DMAIC เป็นงาน digital marketing, CMRP CMPR-04 p.9)

## ความสัมพันธ์กับ RBMM และ ISO 14224

**สถานะของแหล่ง:** CMRP เป็นสื่อการสอน (secondary teaching source) ความน่าเชื่อถือต่ำกว่ามาตรฐาน [[ISO 14224]] และไม่ได้มาแทน [[Reliability Based Maintenance Management Book]] ถ้าขัดกับ ISO ให้ถือ ISO เป็นหลักและบันทึกเป็น contested ตาม SCHEMA หัวข้อ 9

**สิ่งที่ CMRP เพิ่มให้ wiki:** หัวข้อที่ RBMM และ ISO ไม่มีหรือมีน้อย ได้แก่ tribology และ lubrication, เทคนิค CM, RCA, work management (planning, scheduling, backlog), turnaround, SPC, maintainability, reliability allocation, reliability growth, FTA, human reliability, TPM/Lean และ business case

**สิ่งที่ CMRP ยืนยัน:** นิยาม P-F, RPN = S x O x D และสูตร criticality เชิงปริมาณแบบ MIL-STD-1629A (ตรงกับ [[FMECA]]), สูตร Ai/Aa/Ao ที่ wiki เคยติดป้ายความรู้ทั่วไป ([[Availability and OEE]]), censored data 4 แบบ ([[Censored Data]]), ขอบเขตปริพันธ์ 0 ถึง tp ของสูตร cost rate ([[PM Interval Optimization]])

**ความต่างแบบ convention (ไม่ contested):** สเกล FMECA 1-10 (RPN สูงสุด 1,000) ของ CMRP กับ 1-5 (สูงสุด 125) ของ RBMM, ทิศของ severity category, risk matrix 5x5 กับ 5x6 ดู [[CMRP vs RBMM FMECA Scales]]; ระบบตัวอักษร failure pattern ของ RBMM กับ Nowlan & Heap; ขอบเขตของ MTTR (CMRP นับเฉพาะ active repair 7 ขั้นตาม MIL-HDBK-472 ใกล้ ISO มากกว่า RBMM ที่รวมเวลารอ, CMRP CMPR-04 p.39); ตัวเลข "ราว 70% ถูกกำหนดตั้งแต่ design" ของ CMRP (ต้นทุน M&R, CMPR-01 p.29) กับ RBMM (ราคาโครงการ, [[Asset Life Cycle]]) เป็นคนละ metric

**ประเด็นที่ขัดกันจริง (รายการ contested):** รายละเอียดและสถานะ `contested` อยู่ที่หน้าปลายทาง หน้า hub นี้เพียงรวมรายการ

| ประเด็น | CMRP | RBMM / ISO / มาตรฐานอื่น | หน้า |
|---|---|---|---|
| คาบ inspection ของ CBM | T = PF (criticality moderate), 0.75 x PF (high) (CMRP CMPR-03 p.12) | P-F/2 (RBMM p.208) | [[P-F Interval and Condition Monitoring]] |
| ตัวคูณ FFI | T = MTTF x 2 x (1 - A) หรือ x 3 x (1 - A) เมื่อ criticality สูง (CMRP CMPR-03 p.12) | FFI = 2 x U x MTBF ของอุปกรณ์ป้องกัน (SAE JA1012 ตาม RBMM) | [[Failure Finding Interval]] |
| ค่าแรงภายในใน turnaround cost | ควรนับค่าแรงพนักงานโรงงานช่วง turnaround เป็นต้นทุน event (CMRP CMPR-10 p.19) | นับเฉพาะ materials และค่าจ้างเหมาเมื่อกระจายรายปี (RBMM) | [[Maintenance Budget]], [[Turnaround Management]] |
| นิยาม availability | Uptime/Total time (CMPR-01 p.4); Ao ใช้ MTBF ที่ p.21 แต่ MTBM ที่ p.23 (CMPR-04) | นิยามและองค์ประกอบเวลาของ RBMM และ ISO 14224 | [[Availability and OEE]] |

ข้อสังเกตเพิ่ม: CMRP ใช้ λ = 1/MTBF และ A = MTBF/(MTBF + MTTR) ซึ่งสมมติ failure rate คงที่ (CMRP CMPR-01 p.4) สไลด์เองระบุเงื่อนไข exponential ไว้ที่ CMPR-04 p.14 ส่วน wiki เตือนเรื่องนี้แล้วใน [[Reliability Metrics]] และ [[Failure Rate Estimation]]

## ความเชื่อมโยงกับ compressor failure hierarchy

ส่วนนี้เป็นการตีความของ wiki: สไลด์ไม่มีข้อมูล compressor โดยตรง แต่เนื้อหา [[Wear Mechanisms]] และ [[Lubrication and Oil Analysis]] เชื่อมกับ mechanism ใน [[Failure Mechanism]] และ sub unit [[LUBS Lubrication System]] ส่วนเทคนิค CM เป็นวิธีตรวจจับตาม [[Failure Detection Method]] ไม่มีตัวเลข failure rate, β หรือ P-F ของ compressor ในสไลด์

## ดูเพิ่ม

- [[Reliability Based Maintenance Management Book]]
- [[ISO 14224]]
- [[OREDA]]
- [[Failure Hierarchy]]

## Triplets

- CMRP [alias_of:: [[CMRP Course]]] Certified Maintenance & Reliability Professional
- [[CMRP Course]] [related_to:: PETROSYNC] course provider
- [[CMRP Course]] [has_value:: 11] files CMPR-01 to CMPR-11
- [[CMRP Course]] [has_value:: 408] scanned PDF pages, OCR, PDFs kept local only (gitignored)
- [[CMRP Course]] [has_category:: secondary teaching source] lower trust than ISO 14224 (SCHEMA section 9)
- [[CMRP Course]] [uses:: SMRP Body of Knowledge] 5 pillars (CMRP CMPR-01 p.2-3)
- Business and Management [part_of:: SMRP Body of Knowledge] pillar 1
- Manufacturing Process Reliability [part_of:: SMRP Body of Knowledge] pillar 2
- Equipment Reliability [part_of:: SMRP Body of Knowledge] pillar 3
- Organization and Leadership [part_of:: SMRP Body of Knowledge] pillar 4; slide skips item 4.1
- Work Management [part_of:: SMRP Body of Knowledge] pillar 5
- AEO Model [defined_in:: [[CMRP Course]]] (CMRP CMPR-01 p.1)
- Maintenance Strategy Layer [step_of:: AEO Model] layer 1
- Work Identification [step_of:: AEO Model] layer 2
- Work Control [step_of:: AEO Model] layer 3
- Work Execution [step_of:: AEO Model] layer 4, feeds back via Post Maintenance Testing and Update Program
- Preventive Maintenance [part_of:: AEO Model] PM, time based
- Proactive Reliability Maintenance [part_of:: AEO Model] PRM, predictive plus corrective
- Operator Driven Reliability [part_of:: AEO Model] ODR
- Run to Failure [part_of:: AEO Model] RTF
- [[Root Cause Analysis]] [related_to:: AEO Model] RCFA supports the maintenance program
- Proactive Reliability Maintenance [differs_from:: Proactive Maintenance] PRM covers predictive plus corrective; RBMM proactive covers predictive plus preventive
- AEO Model [related_to:: [[Maintenance Efficacy Pyramid]]] work control layer
- [[Lubrication and Oil Analysis]] [defined_in:: [[CMRP Course]]] CMPR-01, CMPR-02
- [[Condition Monitoring Techniques]] [defined_in:: [[CMRP Course]]] CMPR-01, CMPR-02
- [[Wear Mechanisms]] [defined_in:: [[CMRP Course]]] CMPR-02
- [[CMRP vs RBMM FMECA Scales]] [defined_in:: [[CMRP Course]]] CMPR-02, CMPR-03
- [[Root Cause Analysis]] [defined_in:: [[CMRP Course]]] CMPR-03
- [[Maintenance Business Case]] [defined_in:: [[CMRP Course]]] CMPR-03, CMPR-04
- [[TPM and Lean Maintenance]] [defined_in:: [[CMRP Course]]] CMPR-04
- [[Maintainability]] [defined_in:: [[CMRP Course]]] CMPR-04
- [[Reliability Allocation]] [defined_in:: [[CMRP Course]]] CMPR-04, CMPR-05, CMPR-06
- [[Statistical Process Control]] [defined_in:: [[CMRP Course]]] CMPR-06, CMPR-07, CMPR-08
- [[Digital Maintenance and Predictive Analytics]] [defined_in:: [[CMRP Course]]] CMPR-08
- [[Maintenance Planning and Scheduling]] [defined_in:: [[CMRP Course]]] CMPR-08, CMPR-09
- [[Maintenance Backlog and Schedule Compliance]] [defined_in:: [[CMRP Course]]] CMPR-09, CMPR-10
- [[Turnaround Management]] [defined_in:: [[CMRP Course]]] CMPR-10, CMPR-11
- [[Human Reliability]] [defined_in:: [[CMRP Course]]] CMPR-11
- [[Reliability Growth Models]] [defined_in:: [[CMRP Course]]] CMPR-11
- [[Fault Tree Analysis]] [defined_in:: [[CMRP Course]]] CMPR-11
- [[CMRP Course]] [related_to:: [[Reliability Based Maintenance Management Book]]] overlapping topics; CMRP adds work management, SPC, tribology
- [[CMRP Course]] [related_to:: [[ISO 14224]]] ISO governs when they conflict
- [[Reliability Metrics]] [has_formula:: M(t) = 1 - e^(-mu t)] correct maintainability formula; CMPR-01 p.4 misprints it
- [[Reliability Block Diagram]] [has_value:: 0.648] CMPR-04 p.44 example; slide prints 0.541
- [[FMECA]] [has_value:: 392] PFMEA row 4 RPN 7x8x7; CMPR-02 p.41 prints 382
- [[Condition Monitoring Techniques]] [has_value:: 7.6 mm/s] equals 0.3 in/s; CMPR-01 p.41 pairs 0.3 in/s with 5.0 mm/s
- [[Fault Tree Analysis]] [has_code:: 29 CFR 1910.119] PSM standard; CMPR-11 p.18 prints 19 CFR (general knowledge)
- CMRP Inspection Interval [differs_from:: RBMM Inspection Interval] T = PF or 0.75 PF (CMPR-03 p.12) vs P-F/2 (RBMM p.208); see P-F page
- CMRP Failure Finding Interval [differs_from:: SAE JA1012 Failure Finding Interval] factor 2 or 3 with MTTF (CMPR-03 p.12) vs 2 x U x MTBF
- CMRP Turnaround Cost [differs_from:: RBMM Turnaround Budget] CMRP includes in-house labour (CMPR-10 p.19); RBMM counts materials and contracts only
- CMRP Availability Definitions [differs_from:: RBMM Availability Definitions] Uptime/Total time; Ao with MTBF (p.21) vs MTBM (p.23)
- [[CMRP vs RBMM FMECA Scales]] [has_category:: convention difference] not contested

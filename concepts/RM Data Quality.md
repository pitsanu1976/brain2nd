---
title: RM Data Quality
created: 2026-10-21
updated: 2026-10-22
type: concept
tags: [iso-14224, data-quality, coding, cmms, reliability]
sources: [iso-14224.md]
confidence: medium
contested: false
---

# RM Data Quality (คุณภาพข้อมูล reliability and maintenance ตาม ISO 14224)

สรุป clause 7 และ Annex D ของ [[ISO 14224]] ด้วยถ้อยคำของผู้เขียน wiki ใช้ควบคู่กับ [[Failure Data Recording]] และ [[CMMS]]

## 1. ข้อมูลคุณภาพสูงคืออะไร (ISO 14224 cl. 7.1.1, p.25)

ครบตาม spec; ตรงกับนิยามและรูปแบบ; ป้อน ส่ง เก็บถูกต้อง; population และ surveillance period พอให้มั่นใจทางสถิติ; ตรงกับความต้องการผู้ใช้

## 2. Planning measures ก่อนเริ่มเก็บ (cl. 7.1.2, p.25-26)

- ตั้งวัตถุประสงค์ (QRA, RAM, RCM, LCC, SIL) ตรวจแหล่งข้อมูล กำหนด taxonomy และ boundary ต่อ class ระบุวันติดตั้ง population ช่วงเวลาใช้งาน
- ใช้นิยาม failure และวิธีจัดประเภท failure/maintenance แบบเดียวกันทั้งหมด
- ความละเอียดข้อมูลผูกกับความสำคัญด้าน safety/production วางแผน (schedule ลำดับ วิธีโอนข้อมูล) อบรมผู้เก็บ แผน QA ทบทวนแผนหลังใช้งานระยะหนึ่ง
- แนะนำทำ **pilot run** ก่อน เพื่อดู cost-benefit

### เป้าความครบของข้อมูล (p.26)

| ระดับความสำคัญ | ความครบที่ต้องการ |
|---|---|
| HIGH | ประมาณ 100% (บังคับ) |
| MEDIUM | มากกว่า 85% |
| LOW | มากกว่า 50% |

### Checklist ตรวจข้อมูล (สรุปเป็น 9 ข้อ, p.26)

1. ตามรอยแหล่งที่มาได้
2. อุปกรณ์/เทคโนโลยี/สภาวะคล้ายกัน
3. อุปกรณ์ยังเกี่ยวข้อง ไม่ล้าสมัย
4. ตรงนิยามของมาตรฐาน
5. failure อยู่ใน boundary และ surveillance period
6. ข้อมูลสอดคล้องกัน เช่น failure mode กับ failure impact (ดู [[Failure Impact Classification]])
7. format ถูกต้อง
8. ปริมาณพอทางสถิติ และไม่ถูก outlier ลาก (ISO 14224 cl. C.3.2)
9. ให้ฝ่าย O&M ช่วย validate

## 3. Verification (cl. 7.1.3, p.26-27)

ตรวจระหว่างและหลังเก็บ (consistency การกระจายสมเหตุผล code ถูก) และบันทึกเป็นเอกสาร; รวมหลาย database ต้องมี unique ID ต่อ record; ประเมินเร็วเพื่อแก้แผนทัน; **ผู้ตรวจต้องไม่ใช่คนเดียวกับผู้เก็บ**

## 4. ปัญหาที่พบบ่อย (Table 1, p.27)

source กระจัดกระจาย; ตีความต่างกันระหว่างคน; ใช้ **coded field เป็นหลักและมี free text เสริม**; โอนข้อมูลกึ่งอัตโนมัติจาก CMMIS; ความสามารถและแรงจูงใจของผู้เก็บ

## 5. กระบวนการเก็บข้อมูล (cl. 7.2, p.27-28)

- แหล่งหลักคือ **CMMIS** ของ facility ซึ่งต้องรองรับการรายงานตามมาตรฐาน (ใน wiki เรียก [[CMMS]])
- ขั้นตอนทั่วไป: ดึง raw data ลง intermediate storage -> ตีความและแปลงเข้ารูปแบบเป้าหมาย (ส่วนใหญ่ทำมือ) -> โอนเข้า reliability data bank (อัตโนมัติคุ้มเฉพาะข้อมูลปริมาณมากและซ้ำ) -> วางแผนและทดสอบวิธีก่อนเริ่มจริง
- ต้องมีทักษะ IT สถิติ maintenance operation; มีระบบจัดการ deviation (นิยามกำกวม code ไม่พอ) ตั้งแต่ต้น; สรุป lessons learned ป้อนกลับ

## 6. แหล่งข้อมูลและข้อควรระวัง (Annex D, ISO 14224 Table D.5, p.235-237)

- ประเภทแหล่ง: generic (database/handbook เช่น [[OREDA]]), operator-specific, manufacturer, expert judgement, human error data
- generic เหมาะช่วงต้นโครงการ ช่วงหลังควรใช้ข้อมูล specific ที่มีเอกสารดี; ข้อมูล installation เดียวมักความเชื่อมั่นต่ำ ยกเว้น population มาก
- failure rate จากผู้ผลิตมักต่ำ (optimistic) เกินจริง เพราะตัด failure จาก environment, การใช้ผิด, installation, maintenance error
- event ใน CMMS **ไม่ใช่ reliability data โดยตรง** แต่ใช้สร้าง KPI ได้ ต้องจัด format ตามมาตรฐานก่อน
- expert ควรประมาณเป็นจำนวน event ที่สังเกตได้ในช่วงเวลาหนึ่ง แทนตัวเลขอัตราต่อชั่วโมง

## 7. ข้อมูลที่ต้องใช้ต่อประเภทการวิเคราะห์ (Annex D, Table D.1-D.4, p.229-234)

Table D.1 แบ่งการวิเคราะห์เป็น Safety (QRA, RBI, SIL, ESIA), LCC/optimisation/maintenance (LCC, production availability, RCM, spare part analysis, FMECA, lifetime analysis, RCA) และ general (FTA, Markov, Petri net ฯลฯ) ตาราง D.2-D.4: 1 = ปกติต้องมี, 2 = optional; parameter ที่คำนวณ (failure rate, CI, PFD, repair rate, CCF rate, test efficiency) ไม่บันทึกตรง

| การวิเคราะห์ | ข้อมูลหลักที่ต้องมี (ระดับ 1) |
|---|---|
| RCM ([[RCM Reliability Centered Maintenance]]) | ข้อมูลอุปกรณ์ครบ รวม surveillance/operating period, จำนวน demand; failure mode, impact on function, mechanism, cause, impact on plant; maintenance category, activity, down time, active time, man-hours (detection method และ failure date เป็นระดับ 2) |
| Lifetime analysis (เช่น [[Weibull Analysis]]), RCA | failure date เป็นระดับ 1 |
| Availability / production availability | down time, active maintenance time, man-hours, failure mode, impact |
| Spare part analysis | spare part, lead time, repair workshop cycle time |
| FTA / Markov | failure rate, CCF rate, PFD, repair rate, test efficiency, test interval |
| SIL | จำนวน demand, CCF rate, failure cause |

## เชื่อมโยงกับ compressor failure hierarchy

- รายการ checklist ข้อ 6 ช่วยตรวจรหัส mode/cause ใน [[Failure Mode]] และ [[Failure Cause Codes]] ว่าสอดคล้องกัน
- ตัวเลขใน [[OREDA]] เป็น generic data; ข้อมูลไซต์ต้องผ่านขั้นตอนข้างต้นก่อนเทียบกัน ดู [[Failure Rate Estimation]]
- ตัวชี้วัดที่คำนวณจากข้อมูลเหล่านี้ ดู [[Maintenance KPIs]]

## Triplets

- [[RM Data Quality]] [defined_in:: [[ISO 14224]]] Clause 7 and Annex D
- [[RM Data Quality]] [related_to:: [[Failure Data Recording]]]
- High Quality RM Data [has_category:: complete, compliant with definitions, correctly entered/stored, statistically sufficient, relevant to user] (cl. 7.1.1, p.25)
- Data Collection Planning [step_of:: [[RM Data Quality]]] before collection (cl. 7.1.2, p.25-26)
- Data Collection Planning [has_part:: Pilot Run] recommended to check cost-benefit (cl. 7.1.2)
- Data Collection Planning [applies_to:: QRA, RAM, RCM, LCC, SIL] objectives
- HIGH Importance Data [has_value:: 100%] approx. completeness, mandatory (p.26)
- MEDIUM Importance Data [has_value:: >85%] completeness (p.26)
- LOW Importance Data [has_value:: >50%] completeness (p.26)
- Data Quality Checklist [has_value:: 9] items, wiki summary (cl. 7.1.2, p.26)
- Data Quality Checklist [has_part:: Consistency Check] e.g. failure mode vs failure impact, see [[Failure Impact Classification]]
- Data Quality Checklist [has_part:: Statistical Sufficiency] not driven by outliers (cl. C.3.2)
- Data Quality Checklist [uses:: O&M Validation] item 9
- Verification [step_of:: [[RM Data Quality]]] during and after collection, documented (cl. 7.1.3, p.26-27)
- Verification [depends_on:: Independent Checker] checker must not be the collector
- Database Merge [uses:: Unique Record ID] (cl. 7.1.3)
- [[RM Data Quality]] [uses:: Coded Field] coded fields primary with free text supplement (Table 1, p.27)
- [[CMMS]] [source_of:: RM Data] CMMIS is main source, must support standard reporting (cl. 7.2, p.27-28)
- Raw Data Extraction [step_of:: Data Collection Process] to intermediate storage (cl. 7.2)
- Data Interpretation and Conversion [step_of:: Data Collection Process] mostly manual
- Data Bank Transfer [step_of:: Data Collection Process] automation pays only for large repetitive data
- Method Planning and Testing [step_of:: Data Collection Process] before starting
- Data Collection Process [has_part:: Deviation Management] ambiguous definitions, missing codes
- [[OREDA]] [is_a:: Generic Data Source] database/handbook (Table D.5, p.235-237)
- RM Data Source [has_category:: generic, operator-specific, manufacturer, expert judgement, human error data] (Table D.5)
- Generic Data Source [applies_to:: Early Project Phase] later use well-documented specific data
- Manufacturer Data [has_category:: optimistic] failure rate often too low; excludes environment, misuse, installation, maintenance error
- [[CMMS]] [differs_from:: Reliability Data] CMMS events not reliability data directly; usable for KPI after formatting
- Expert Judgement [produces:: Number of Observed Events] per period, instead of rate per hour
- ISO:D.1 [has_category:: Safety, LCC/optimisation/maintenance, general] analysis types (Table D.1, p.229-234)
- ISO:D.2 [has_category:: 1 = normally required, 2 = optional] Table D.2-D.4 data requirement levels
- [[RCM Reliability Centered Maintenance]] [uses:: [[Failure Mode]]] level 1; also impact, cause, activity, down time, active time, man-hours
- [[RCM Reliability Centered Maintenance]] [uses:: [[Failure Mechanism]]] level 1
- [[RCM Reliability Centered Maintenance]] [uses:: [[Failure Detection Method]]] level 2 (optional)
- [[Weibull Analysis]] [uses:: Failure Date] level 1 for lifetime analysis and RCA
- Production Availability Analysis [uses:: Down Time] also active maintenance time, man-hours, failure mode, impact
- Spare Part Analysis [uses:: Lead Time] also spare part, repair workshop cycle time
- FTA [uses:: CCF Rate] also failure rate, PFD, repair rate, test efficiency, test interval; Markov same
- SIL [uses:: Number of Demands] also CCF rate, failure cause
- [[RM Data Quality]] [applies_to:: [[Failure Cause Codes]]] checklist item 6 checks mode/cause consistency
- [[OREDA]] [differs_from:: Site Data] OREDA is generic; site data must pass these steps before comparison (see [[Failure Rate Estimation]])
- [[RM Data Quality]] [related_to:: [[Maintenance KPIs]]]

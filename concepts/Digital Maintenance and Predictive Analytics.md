---
title: Digital Maintenance and Predictive Analytics
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [cmrp, cbm, data-quality, cmms, statistics, maintenance-management]
sources: [cmrp.md, iso-14224.md, reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Digital Maintenance and Predictive Analytics (Maintenance 4.0 และ predictive modelling)

หน้านี้สรุปเรื่อง digitization ของงานบำรุงรักษา กรอบของ vendor/consultant และ predictive modelling ตามสไลด์ CMRP (CMRP CMPR-08 p.15-27) พร้อมข้อจำกัดของโมเดลพยากรณ์ ซึ่งเชื่อมตรงกับหลักคุณภาพข้อมูลของ ISO 14224 ใน [[RM Data Quality]] สไลด์ส่วนนี้เป็นภาพรวมเชิงแนวคิด ตัวอย่างส่วนใหญ่มาจากงานขาย/การตลาด มีเพียงส่วน predictive maintenance และ DSS ที่ผูกกับงานบำรุงรักษา ข้อความถอดความจาก reading notes ใน [[CMRP Course]]

## จุดตั้งต้น: break-out exercise (CMRP CMPR-08 p.15)

แบบฝึกหัดเลือกอุปกรณ์สำหรับ facility ใหม่ 4 ฟังก์ชันด้วยมุม RAMS ใช้เปิดประเด็นว่าการตัดสินใจ asset management ตลอด life cycle ต้องอาศัยข้อมูล (แหล่งข้อมูลและสถิติ) ดู [[Asset Life Cycle]]

## Digitization -> Digitalization -> Digital transformation (CMRP CMPR-08 p.16)

| ขั้น | ความหมายตามสไลด์ |
|---|---|
| Digitization | แปลงข้อมูล analog เป็น digital |
| Digitalization | ใช้ข้อมูล digital ปรับ process |
| Digital transformation | สร้างรูปแบบธุรกิจใหม่ |

วิวัฒนาการงานบำรุงรักษาตามสไลด์:

| ช่วง | ลักษณะ | จุดเน้น |
|---|---|---|
| ก่อน 1980 | reactive (M1.0) | cost |
| 1980-2010 | preventive, CMMS, KPI, condition monitoring, RCA (M2.0/3.0) | quality |
| หลัง 2010 | Industry 4.0, IoT, AI, cyber-physical systems, PdM, RUL (M4.0) | customization |

ช่วง 1980-2010 ตรงกับเครื่องมือที่ wiki มีอยู่แล้ว ได้แก่ [[CMMS]], [[Maintenance KPIs]], [[Condition Monitoring Techniques]] และ [[Root Cause Analysis]]

## กรอบของ vendor และ consultant ที่สไลด์อ้าง (CMRP CMPR-08 p.17-18)

- **McKinsey**: แยก "what" คือตัวโปรแกรมบำรุงรักษา (กำหนด strategy, operate, prioritize/plan/schedule, execute และ feedback) ออกจาก "how" คือ enabler (digital work management, asset strategies, performance management, reliability enablers)
- **GE**: วาง APM (Asset Performance Management) คู่กับระบบอื่นในองค์กร ได้แก่ EAM/CMMS, ERP, EH&S, EQMS, MOM
- **SAP**: ASPM (Asset Strategy and Performance Management) flow: risk and criticality -> RCM/FMEA assessment -> recommendation -> task list/maintenance plan ซึ่งเป็นการทำ [[Criticality Assessment]], [[RCM Reliability Centered Maintenance]] และ [[FMECA]] ให้เป็น digital workflow

สไลด์อ้างกรอบเหล่านี้เป็นตัวอย่าง ไม่ได้ประเมินหรือแนะนำผลิตภัณฑ์ wiki ไม่ได้ประเมิน vendor เช่นกัน

สไลด์ p.19 มีรายการข้อดีข้อเสียของ digital technology แบบทั่วไป (connectivity, data security ฯลฯ) และรายการ MCMC algorithms (Metropolis-Hastings, Gibbs, HMC ฯลฯ) ที่ไม่ได้ผูกกับงานบำรุงรักษา หน้านี้จึงไม่ลงรายละเอียด

## Predictive modelling (CMRP CMPR-08 p.20-24)

- นิยาม: ใช้ข้อมูลและสถิติสร้างโมเดลพยากรณ์ผลลัพธ์
- แหล่งข้อมูลที่สไลด์ระบุมีหลายประเภท ประเภทที่เกี่ยวกับงานบำรุงรักษาคือ machine-generated data เช่น telemetry และ sensor
- ขั้นตอนบูรณาการโมเดลเข้ากับงาน: benchmark analysis -> เก็บข้อมูล -> data cleansing -> วิเคราะห์ -> ประเมินเป้าและ KPI -> action plan -> ลงมือ -> ปรับ process ให้กระชับ
- ชนิดโมเดลที่สไลด์ระบุ: OLS, GLM, logistic regression, random forest, decision tree, neural network, MARS

### Analytics 4 ระดับ (CMRP CMPR-08 p.22)

| ระดับ | คำถาม | ตัวอย่างงานบำรุงรักษา (การตีความของ wiki) |
|---|---|---|
| Descriptive | เกิดอะไรขึ้น | จำนวน failure ต่อ failure mode จาก [[Failure Data Recording]] |
| Diagnostic | ทำไมจึงเกิด | [[Root Cause Analysis]] |
| Predictive | อะไรน่าจะเกิดต่อ | [[Weibull Analysis]], แนวโน้ม CM, RUL |
| Prescriptive | ควรทำอะไร | เลือกงานและคาบ PM ตาม [[PM Task Selection]], [[PM Interval Optimization]] |

สไลด์เน้นว่า predictive analytics พยากรณ์อนาคตไม่ได้จริง แต่บอกผลที่น่าจะเกิดจากข้อมูลที่มี และสร้างโมเดลได้เมื่อมีข้อมูลพอ

### การใช้งานในงานบำรุงรักษา (CMRP CMPR-08 p.23)

- **Predictive maintenance**: อุตสาหกรรมที่ใช้ทุนสูง (รวม oil and gas) ใช้โมเดลที่ฝึกด้วยข้อมูลการใช้งานเครื่อง ภาพ และอุณหภูมิ เพื่อบอกว่าเครื่องควรได้รับการบำรุงรักษาเมื่อไร หลีกเลี่ยงการเสียและงานซ่อมใหญ่ แนวคิดนี้คือการหาจุด P บน P-F curve ให้เร็วและแม่นขึ้น ดู [[P-F Interval and Condition Monitoring]] (การเชื่อมโยงกับ P-F เป็นการตีความของ wiki)
- **Decision Support System (DSS)**: ระบบที่รวมและแสดงข้อมูลให้ผู้ตัดสินใจ predictive model ช่วยให้เห็นผลลัพธ์ที่เป็นไปได้พร้อมโอกาสเกิด
- JIT maintenance ในสไลด์อีกไฟล์ใช้ predictive analytics เป็นฐานเช่นกัน ดู [[TPM and Lean Maintenance]] (CMRP CMPR-04 p.8)

## ข้อจำกัดของ predictive model (CMRP CMPR-08 p.24-27, อ้าง McKinsey)

| ข้อจำกัด | สาระ | เทียบกับ wiki |
|---|---|---|
| Data labelling | ข้อมูลต้องติดป้ายและจัดประเภทถูก งานนี้ใหญ่และผิดพลาดง่าย ถ้าจัดประเภทผิดโมเดลจะแย่ | ตรงกับข้อกำหนดการจัดประเภท failure mode/cause ที่สม่ำเสมอใน [[RM Data Quality]] และ [[Failure Data Recording]] |
| ต้องการ dataset ขนาดใหญ่ | ต้องมี sample size พอ ไม่เช่นนั้นโมเดลถูก noise ลาก จำนวน record ที่ต้องการอยู่ในหลักพันถึงล้าน และต้อง representative ของประชากรเป้าหมาย รวมกรณีแปลก ๆ | ตรงกับเกณฑ์ปริมาณพอทางสถิติและไม่ถูก outlier ลาก (ISO 14224 cl. C.3.2) ใน [[RM Data Quality]] |
| Explainability | โมเดลซับซ้อนอธิบายเหตุผลของผลพยากรณ์ยาก เป็นปัญหาในงานที่มีผลทางกฎหมาย/กำกับดูแล | งานที่เกี่ยวกับ safety ต้องอธิบายได้ ดู [[Safety Critical Failure Classification]] (การตีความ) |
| Generalizability | โมเดลที่สร้างสำหรับกรณีหนึ่งไม่ควรนำไปใช้กับอีกกรณี | สอดคล้องกับหลักไม่รวมข้อมูลต่างประชากร/ต่าง failure mode ใน [[Weibull Analysis]] (การตีความ) |
| Bias | ข้อมูลและอัลกอริทึมมี bias ได้ | - |

### ผลต่อการใช้ข้อมูลใน wiki นี้ (การตีความ)

- ข้อมูล OREDA ใน wiki เป็น % ของ failure rate ไม่มี time-to-failure ราย event (ดู [[Reliability Based Maintenance Management Book]] หัวข้อความสัมพันธ์กับ hierarchy) จึงพอสำหรับ descriptive analytics แต่ไม่พอสำหรับโมเดล predictive หรือ RUL
- จำนวน failure ราย failure mode ของ compressor ใน fleet หนึ่งมักอยู่หลักสิบ ห่างจากหลักพันถึงล้าน record ที่สไลด์อ้างมาก โมเดล machine learning ราย failure mode จึงเสี่ยงต่อ noise วิธีทางสถิติแบบ [[Weibull Analysis]] ร่วมกับ [[Censored Data]] หรือการใช้ข้อมูล CM ต่อเนื่อง (sensor) จะเหมาะกว่า (ข้อนี้เป็นความรู้ทั่วไป ไม่อยู่ในสไลด์, confidence low)
- ก่อนลงทุนระบบ predictive ควรตรวจคุณภาพข้อมูลใน [[CMMS]] ตาม [[RM Data Quality]] ก่อน และทำ business case ตาม [[Maintenance Business Case]]

## Triplets

- [[Digital Maintenance and Predictive Analytics]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-08 p.15-27)
- Digitization [step_of:: Digital Transformation Path] analog to digital (CMRP CMPR-08 p.16)
- Digitalization [step_of:: Digital Transformation Path] use digital data to change processes
- Digital Transformation [step_of:: Digital Transformation Path] new business models
- Maintenance 4.0 [has_category:: post-2010] Industry 4.0, IoT, AI, CPS, PdM, RUL (CMRP CMPR-08 p.16)
- Maintenance 2.0 and 3.0 [has_category:: 1980-2010] preventive, CMMS, KPIs, CM, RCA
- Maintenance 1.0 [has_category:: pre-1980] reactive, cost focus
- McKinsey Maintenance Framework [related_to:: [[Digital Maintenance and Predictive Analytics]]] what (program) vs how (enablers) (CMRP CMPR-08 p.17)
- Asset Performance Management [uses:: [[CMMS]]] GE positions APM with EAM/CMMS, ERP, EH&S, EQMS, MOM (CMRP CMPR-08 p.17-18)
- SAP ASPM [uses:: [[Criticality Assessment]]] step 1 risk and criticality
- SAP ASPM [uses:: [[RCM Reliability Centered Maintenance]]] RCM/FMEA assessment then recommendation then task list
- Predictive Modelling [uses:: Machine-Generated Data] telemetry, sensors (CMRP CMPR-08 p.20)
- Predictive Modelling [uses:: Logistic Regression] also OLS, GLM, random forest, decision tree, neural network, MARS (CMRP CMPR-08 p.21)
- Benchmark Analysis [step_of:: Predictive Model Integration] then data gathering, cleansing, analysis, KPIs, action plan, execution (CMRP CMPR-08 p.21)
- Descriptive Analytics [step_of:: Analytics Maturity] level 1 (CMRP CMPR-08 p.22)
- Diagnostic Analytics [step_of:: Analytics Maturity] level 2
- Predictive Analytics [step_of:: Analytics Maturity] level 3
- Prescriptive Analytics [step_of:: Analytics Maturity] level 4
- Predictive Modelling [applies_to:: Predictive Maintenance] capital-intensive industries incl. oil and gas (CMRP CMPR-08 p.23)
- Predictive Modelling [applies_to:: Decision Support System] (CMRP CMPR-08 p.23)
- Predictive Maintenance [related_to:: [[P-F Interval and Condition Monitoring]]] earlier detection of P, interpretation [confidence:: low]
- Predictive Maintenance [uses:: [[Condition Monitoring Techniques]]] sensor and condition data
- Predictive Modelling [depends_on:: Data Labelling] limitation (CMRP CMPR-08 p.24-25)
- Predictive Modelling [depends_on:: Sample Size] thousands to millions of records, representative (CMRP CMPR-08 p.25)
- Predictive Modelling [depends_on:: Explainability] limitation where legal/regulatory consequences (CMRP CMPR-08 p.26)
- Predictive Modelling [depends_on:: Generalizability] model built for one case should not be reused for another (CMRP CMPR-08 p.26)
- Predictive Modelling [depends_on:: Data Bias] bias in data and algorithms (CMRP CMPR-08 p.27)
- Predictive Modelling [depends_on:: [[RM Data Quality]]] sufficient quantity, consistent classification (ISO 14224 cl. C.3.2)
- [[OREDA]] [differs_from:: Predictive Modelling Data Need] OREDA percentages lack time-to-failure, interpretation [confidence:: low]
- JIT Maintenance [uses:: Predictive Analytics] (CMRP CMPR-04 p.8)

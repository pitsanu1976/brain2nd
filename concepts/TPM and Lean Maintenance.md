---
title: TPM and Lean Maintenance
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [cmrp, tpm, maintenance-management]
sources: [cmrp.md, reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# TPM and Lean Maintenance (Lean, TPM, 5S, SMED, JIT, Six Sigma)

หน้านี้สรุปแนวคิดปรับปรุงการผลิตและงานบำรุงรักษาที่สไลด์ CMRP นำเสนอเป็นชุดเดียวกันใน CMPR-04 p.5-9 ได้แก่ Lean, TPM (Total Productive Maintenance), 5S, SMED, JIT maintenance และ Six Sigma สไลด์ให้ระดับภาพรวม (ชื่อ องค์ประกอบ เป้าหมาย) ไม่มีตัวอย่างตัวเลขหรือวิธีวัดผล ส่วนที่ระบุว่าความรู้ทั่วไปไม่อยู่ในสไลด์ ข้อความถอดความจาก reading notes ใน [[CMRP Course]]

## Lean (CMRP CMPR-04 p.5-6)

- หลัก: ผลิตให้ได้มากที่สุดโดยตัด waste ซึ่งนิยามว่าเป็นสิ่งที่ลูกค้าไม่ยอมจ่ายเงินให้
- waste ในภาพของสไลด์มี 6 แบบ: processing, inventory, waiting, overproduction, motion, transportation
  - ข้อสังเกต: ไม่มี defects ซึ่งตามแนวทั่วไปเป็นหนึ่งใน 7 wastes (ความรู้ทั่วไป ไม่อยู่ในสไลด์)
- องค์ประกอบของ lean process ตามสไลด์: identify value, value stream mapping, create flow, pull system, Kaizen, quality management, employee involvement, visual management, technology/automation

## TPM (CMRP CMPR-04 p.6)

- pillars ที่อ่านได้จากสไลด์: Autonomous Maintenance, Focused Improvement, Quality Management, Early Equipment Maintenance, Office TPM, EHS
- ฐานของ pillar: OCR อ่านเป็น "6 'S'" ยืนยันจากภาพไม่ได้ ตามแบบทั่วไปฐานคือ 5S (ความรู้ทั่วไป)
- เป้า "zero" 4 ข้อ: zero accident, zero breakdown, zero small stops/changeover, zero defects
- pillar ที่พบในแบบ 8 pillars ทั่วไปแต่ไม่ปรากฏในส่วนที่อ่านได้ เช่น Planned Maintenance และ Training (ความรู้ทั่วไป, confidence low; อาจอยู่ในส่วนของภาพที่อ่านไม่ออก)

### เชื่อมกับ Zero Breakdown ของ RBMM

[[Asset Life Cycle]] (RBMM) ตั้งเป้า Zero Plant Breakdown @ Minimum Cost และบอกว่า zero breakdown ต้องครอบคลุมตั้งแต่ design ถึง operator และ maintenance คือ TPM (RBMM p.27) เป้า zero breakdown ของ TPM ในสไลด์จึงสอดคล้องกับ RBMM ไม่ขัดกัน pillar Early Equipment Maintenance ยังสอดคล้องกับหลักที่ว่าต้นทุนและ maintainability ถูกกำหนดตั้งแต่ช่วงออกแบบ (CMRP CMPR-04 p.18, p.35; ดู [[Maintainability]])

Autonomous Maintenance (operator ดูแลเครื่องพื้นฐานเอง) มีแนวคิดใกล้กับ Operator Driven Reliability (ODR) ใน AEO Model ของ [[CMRP Course]] (CMRP CMPR-01 p.1) การเทียบนี้เป็นการตีความของ wiki สไลด์ไม่ได้เชื่อมสองเรื่องนี้

## 5S และ SMED (CMRP CMPR-04 p.7)

| 5S (ญี่ปุ่น) | ความหมาย |
|---|---|
| Seiri | Sort คัดของไม่จำเป็นออก |
| Seiton | Set in Order จัดที่ให้หยิบง่าย |
| Seiso | Shine ทำความสะอาด (เป็นโอกาสตรวจสภาพเครื่อง) |
| Seiketsu | Standardize ทำให้เป็นมาตรฐาน |
| Shitsuke | Sustain รักษาวินัย |

- SMED (Single-Minute Exchange of Die): ลดเวลา changeover สไลด์แสดงเป็นภาพ 7 stages ไม่มีรายละเอียดแต่ละขั้นที่อ่านได้
- คำอธิบายในคอลัมน์ขวาของตาราง 5S เป็นการถอดความสั้น ๆ ของ wiki

## JIT Maintenance (JITM) (CMRP CMPR-04 p.8)

- ทำงานบำรุงรักษาเฉพาะเมื่อจำเป็น ใช้ predictive analytics และข้อมูลตัดสินใจ ตัดงานที่ไม่จำเป็นออก
- กลยุทธ์ 4 ด้าน: resource optimization, data-driven decision, dynamic scheduling, time precision
- แนวคิดนี้ต้องพึ่งข้อมูลสภาพเครื่องและโมเดลพยากรณ์ ดู [[Digital Maintenance and Predictive Analytics]] และ [[P-F Interval and Condition Monitoring]]

## Six Sigma (CMRP CMPR-04 p.8-9)

- เป้า: ลด defect และ variation ให้เหลือ 3.4 DPMO (defects per million opportunities)
- บทบาท belt: Master Black Belt, Black Belt, Green Belt, Yellow Belt
- วงจร DMAIC (Define, Measure, Analyze, Improve, Control)
- ข้อสังเกต: ภาพ DMAIC ในสไลด์ p.9 เป็นตัวอย่างงาน digital marketing (website, campaign) ไม่ใช่งานบำรุงรักษา
- ตัวเลข 3.4 DPMO รวม 1.5σ shift แล้ว ต่างจากตาราง Cp-ppm ในหน้า [[Statistical Process Control]] ที่ไม่ใส่ shift (ข้อสังเกตจาก CMPR-08 notes และความรู้ทั่วไป)

## การใช้กับงานบำรุงรักษา (การตีความ)

- TPM/5S ลดสาเหตุ failure ที่มาจากการดูแลพื้นฐาน (สกปรก หล่อลื่นไม่พอ ชิ้นส่วนหลวม) ซึ่งใน failure hierarchy มักปรากฏเป็น mechanism เช่น contamination และ wear ดู [[Failure Mechanism]] และ [[Lubrication and Oil Analysis]]
- Lean/JIT ในงานบำรุงรักษาต้องสมดุลกับความเสี่ยงอะไหล่ขาด การลด inventory แบบ Lean ใช้ไม่ได้ตรง ๆ กับ insurance spares ของเครื่อง criticality สูง ดู [[Spare Part Criticality and Risk]] (ข้อนี้เป็นการตีความ ไม่อยู่ในสไลด์)
- สไลด์ไม่ได้ให้ KPI ของ TPM (เช่น OEE) ในส่วนนี้ แต่ OEE ที่ใช้คู่กับ TPM อยู่ที่ [[Availability and OEE]]

## Triplets

- [[TPM and Lean Maintenance]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-04 p.5-9)
- Lean [part_of:: [[TPM and Lean Maintenance]]]
- Lean [has_parameter:: Waste] what the customer will not pay for (CMRP CMPR-04 p.5)
- Waste [has_value:: 6] types shown: processing, inventory, waiting, overproduction, motion, transportation; defects missing vs usual 7 wastes
- Value Stream Mapping [part_of:: Lean] lean process element (CMRP CMPR-04 p.6)
- Kaizen [part_of:: Lean]
- Pull System [part_of:: Lean]
- TPM [part_of:: [[TPM and Lean Maintenance]]] Total Productive Maintenance
- Autonomous Maintenance [part_of:: TPM] pillar (CMRP CMPR-04 p.6)
- Focused Improvement [part_of:: TPM] pillar
- Quality Management [part_of:: TPM] pillar
- Early Equipment Maintenance [part_of:: TPM] pillar
- Office TPM [part_of:: TPM] pillar
- EHS [part_of:: TPM] pillar
- 5S [part_of:: TPM] foundation of pillars (OCR reads 6 S, unconfirmed) [confidence:: low]
- TPM [produces:: Zero Breakdown] also zero accident, zero small stops/changeover, zero defects
- Zero Breakdown [related_to:: [[Asset Life Cycle]]] RBMM Zero Plant Breakdown needs TPM (RBMM p.27)
- Autonomous Maintenance [related_to:: Operator Driven Reliability] interpretation, slide does not link them [confidence:: low]
- Sort [step_of:: 5S] Seiri
- Set in Order [step_of:: 5S] Seiton
- Shine [step_of:: 5S] Seiso
- Standardize [step_of:: 5S] Seiketsu
- Sustain [step_of:: 5S] Shitsuke
- SMED [part_of:: [[TPM and Lean Maintenance]]] changeover time reduction, 7 stages (CMRP CMPR-04 p.7)
- JIT Maintenance [part_of:: [[TPM and Lean Maintenance]]] maintenance only when needed (CMRP CMPR-04 p.8)
- JIT Maintenance [uses:: [[Digital Maintenance and Predictive Analytics]]] predictive analytics, data-driven decisions
- Six Sigma [part_of:: [[TPM and Lean Maintenance]]]
- Six Sigma [has_value:: 3.4 DPMO] target (CMRP CMPR-04 p.8)
- DMAIC [part_of:: Six Sigma] Define, Measure, Analyze, Improve, Control; slide example is digital marketing
- Six Sigma [related_to:: [[Statistical Process Control]]] variation reduction
- TPM [related_to:: [[Availability and OEE]]] OEE commonly paired with TPM (interpretation) [confidence:: low]

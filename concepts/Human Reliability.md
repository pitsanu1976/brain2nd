---
title: Human Reliability
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [human-reliability, reliability, failure-cause, cmrp]
sources: [cmrp.md, iso-14224.md]
confidence: medium
contested: false
---

# Human Reliability

Human reliability คือความน่าจะเป็นที่คนทำงานที่ได้รับมอบหมายได้อย่างน่าพอใจ ส่วน Human Reliability Analysis (HRA) คือกระบวนการระบุ ประเมินเชิงปริมาณ และลด human error (CMRP CMPR-11 p.4-5) หน้านี้สรุปนิยาม P(HE), ประเภท error, performance shaping factors (PSF) และเรื่อง culture change จาก [[CMRP Course]] พร้อมโยงกับการบันทึก human error เป็น failure cause ตาม [[ISO 14224]]

## ทำไมสำคัญ (CMRP CMPR-11 p.4)

- สไลด์อ้าง Moore (1994) ว่าราว **65%** ของอุบัติเหตุร้ายแรงทางทะเลมาจาก human และ organisational error ในช่วง operation (ตัวเลขตามที่สไลด์อ้าง ไม่ได้ตรวจกับต้นฉบับ Moore)
- ตัวอย่างเหตุการณ์ที่สไลด์ยก: Bhopal, Three Mile Island, Chernobyl, Piper Alpha

## นิยามเชิงปริมาณ (CMRP CMPR-11 p.5)

```
P(HE) = จำนวนครั้งที่เกิด error / จำนวนโอกาสที่จะเกิด error
Human reliability = 1 - P(HE)        (derived จากนิยาม)
```

## กระบวนการ HRA (CMRP CMPR-11 p.4-5)

- 3 ขั้นหลัก: identification → quantification → reduction
- ขั้นละเอียดในแผนภาพ: problem definition, task analysis, error identification, representation, quantification, impact assessment, error reduction, quality assurance, documentation
- คำถามหลัก: อะไรผิดได้, ผลคืออะไร, PSF ใดมีผลมากที่สุด, ต้องทำอะไรเพื่อป้องกัน; การเลือกวิธี HRA ขึ้นกับ objective, ข้อมูล human error ที่มี และเวลาที่มี
- แบบจำลองพฤติกรรมคน: ข้อมูลเข้า → filter → perception → processing → response โดยมี short-term/long-term/external memory และปัจจัยงาน/สิ่งแวดล้อม (p.4)

## ประเภท error (CMRP CMPR-11 p.6-7)

| ประเภท | ความหมาย | ตัวอย่าง |
|---|---|---|
| Omission | ไม่ได้ทำขั้นตอนที่ต้องทำ | พลาด alarm, ข้ามขั้นตอนประกอบจนเครื่องเสียทันทีหลังซ่อม |
| Commission | ทำแต่ทำผิด (ปริมาณ คุณภาพ ลำดับ) | ขันแรงบิดผิด, ประกอบผิดลำดับ |
| Intentional | รู้ผลแต่ยังฝ่าฝืน | ข้าม safety procedure เพื่อให้เสร็จเร็ว |

**flag สไลด์:** แผนภาพ p.6-7 แสดงเพียง omission กับ commission (และสะกด "Ommission") ขณะที่ข้อความบรรยาย 3 ประเภทรวม intentional ให้ยึด 3 ประเภทตามข้อความ

ระดับพฤติกรรม 3 แบบ: skill-based, procedure (rule)-based, knowledge-based (p.8) (ความรู้ทั่วไป: ตรงกับ SRK model ของ Rasmussen)

## Performance shaping factors (CMRP CMPR-11 p.7-8)

| กลุ่ม | ย่อย | ตัวอย่าง |
|---|---|---|
| Internal | psychological | stress, ขาดแรงจูงใจ |
| Internal | physiological | สุขภาพ ความล้า |
| External | technological | ergonomics, procedure, เครื่องมือ (บริษัทควบคุมได้โดยตรง) |
| External | social | วัฒนธรรมองค์กร ทีมงาน |

## Culture change (CMRP CMPR-11 p.8-13)

- สไลด์เรียก "Culture Change Cycle" 4 quadrant: (1) unconscious incompetence → (2) conscious incompetence → (3) conscious competence → (4) unconscious competence (p.8) ข้อสังเกต (ความรู้ทั่วไป): นี่คือ **conscious competence learning model** ซึ่งเดิมอธิบายการเรียนรู้รายบุคคล สไลด์นำมาใช้กับการเปลี่ยนวัฒนธรรมองค์กร
- สร้าง buy-in: pitch ที่ตอบว่าทำไมต้องเปลี่ยน กระทบธุรกิจอย่างไร เป้าหมายคืออะไร พร้อม roadmap; ได้การสนับสนุนจากผู้บริหารและหัวหน้าระดับกลางตั้งแต่ต้น; โปร่งใสทั้งความสำเร็จและความล้มเหลว; เปิดช่องรับ input (รวมแบบไม่ระบุชื่อ) (p.9-10)
- ให้คนเป็นเจ้าของ reliability: operator คือด่านแรกที่จับอาการผิดปกติ ต้องฝึกให้รู้อาการเครื่อง; reliability ไม่ใช่งานของ reliability engineer คนเดียว (p.11-12)
- change cycle 6 ขั้น: ผูกกับ business goal → เข้าใจความเชื่อปัจจุบัน → สร้าง narrative ใหม่ → ให้รางวัล/แสดงความสำเร็จ → ความสัมพันธ์โปร่งใส → ยอมรับว่าเปลี่ยนแบบค่อยเป็นค่อยไป (p.12)
- change steps: ประเมินสถานะปัจจุบัน (เช่น ใช้ FMEA เพื่อ checklist หรือเพื่อตัดสินใจจริง) → vision ที่จับต้องได้ → roadmap มี milestone (p.13)

## เชื่อมโยงกับ wiki เดิม

- [[ISO 14224]] บันทึก human error (operating error, maintenance error) เป็น **failure cause** ไม่ใช่ failure mechanism ดู [[Failure Cause Codes]] และ [[Failure Mechanism]] ประเภท omission/commission ช่วยลงรายละเอียดใต้ cause กลุ่มนี้ได้ (การตีความ)
- RBMM จัด human error เป็นการเสียแบบสุ่ม (Exponential) ซึ่ง PM ตามเวลาไม่ช่วย ดู [[Statistical Distributions for Maintenance]]
- error ที่เกิดจากงานซ่อมเอง (omission แบบข้ามขั้นตอน) คือแหล่งของ infant mortality หลังซ่อม และเป็นเหตุผลหนึ่งของการลดงาน intrusive PM ดู [[Failure Patterns and Bathtub Curve]] (การตีความ)
- human error มักเป็น root cause ที่ต้องขุดถึงระดับ latent/organisational ใน [[Root Cause Analysis]]
- ข้อมูล test-induced failure (human error ระหว่าง test) ต้องเก็บแยกตาม [[Failure Finding Interval]]

## ดูเพิ่ม

- [[Root Cause Analysis]]
- [[Failure Cause Codes]]
- [[TPM and Lean Maintenance]]
- [[CMRP Course]]

## Triplets

- [[Human Reliability]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-11 p.4-13)
- [[Human Reliability]] [measures:: Probability Of Satisfactory Human Performance] (CMRP CMPR-11 p.5)
- Human Error Probability [has_formula:: P(HE) = number of errors / number of opportunities for error] (CMRP CMPR-11 p.5)
- Human Reliability Analysis [has_part:: Error Identification] then quantification, reduction (CMRP CMPR-11 p.4)
- Error Identification [step_of:: Human Reliability Analysis] step 1 of 3
- Error Quantification [step_of:: Human Reliability Analysis] step 2 of 3
- Error Reduction [step_of:: Human Reliability Analysis] step 3 of 3
- Marine Accidents [has_cause:: Human And Organisational Error] about 65%, Moore (1994) as cited by slides (CMRP CMPR-11 p.4)
- Omission Error [is_a:: Human Error] step not performed (CMRP CMPR-11 p.6-7)
- Commission Error [is_a:: Human Error] performed incorrectly in quantity, quality or sequence (CMRP CMPR-11 p.6-7)
- Intentional Error [is_a:: Human Error] violation with knowledge of consequence (CMRP CMPR-11 p.6-7)
- Error Type Diagram [contradicts:: Error Type Text] diagram shows only omission and commission, text lists three incl. intentional (CMRP CMPR-11 p.6-7)
- Performance Shaping Factor [has_category:: internal or external] internal psychological and physiological; external technological and social (CMRP CMPR-11 p.7-8)
- Human Error [depends_on:: Performance Shaping Factor]
- Human Behaviour Level [has_category:: skill-based, procedure-based, knowledge-based] (CMRP CMPR-11 p.8)
- Culture Change Cycle [alias_of:: Conscious Competence Learning Model] four quadrants, general knowledge (CMRP CMPR-11 p.8)
- Culture Change Cycle [has_part:: Unconscious Incompetence] then conscious incompetence, conscious competence, unconscious competence
- Abnormal Machine Symptoms [detected_by:: Operator] operator is the first detection layer, needs training (CMRP CMPR-11 p.11)
- Human Error [is_a:: Failure Cause] recorded as cause not mechanism (ISO 14224 Table B.2 fn b) see [[Failure Cause Codes]]
- Human Error [related_to:: [[Statistical Distributions for Maintenance]]] random failure, Exponential (RBMM via that page)
- [[Human Reliability]] [related_to:: [[Root Cause Analysis]]]
- [[Human Reliability]] [related_to:: [[Failure Finding Interval]]] human error during test recorded separately

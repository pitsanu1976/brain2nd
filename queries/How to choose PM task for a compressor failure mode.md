---
title: How to choose PM task for a compressor failure mode
created: 2026-10-21
updated: 2026-10-22
type: query
tags: [query, pm, rcm, criticality, compressor, book]
sources: [reliability-based-maintenance-management.md, compressor-failure-hierarchy.md]
confidence: low
contested: false
---

# How to choose PM task for a compressor failure mode

**คำถาม:** จะเลือกประเภทงาน PM สำหรับ failure mode ของ compressor (เช่น ELP, VIB, UST) อย่างไร

**คำตอบสั้น:** ใช้ลำดับของหนังสือ [[Reliability Based Maintenance Management Book]] ตามด้านล่าง ซึ่งสังเคราะห์จากหน้า wiki เป็นขั้นตอนทั่วไป (confidence low) เพราะ **sources ไม่มี β, P-F interval, ต้นทุน หรือประวัติการเสียของ compressor** ขั้นตอนจึงระบุวิธีตัดสินได้ แต่ยังตอบเป็นงานเฉพาะเจาะจงให้ asset ของ Valeura ไม่ได้

## ขั้นตอน

1. **ระบุหน่วยวิเคราะห์เป็น failure mode ต่อ Maintainable Item** เช่น Seals x ELP จาก [[Failure Mode]] และ [[Maintainable Item]] ไม่วิเคราะห์ราย equipment (RBMM p.185 ตาม [[PM Task Selection]])
2. **ประเมิน criticality** ของ [[Compressor]] ด้วย Consequence x Likelihood แยก Commercial, Safety, Environment ได้ A/B/C ([[Criticality Assessment]]) A ใช้ RCM tasks เต็ม B/C ตัด PM ที่ไม่ได้ผล และ C ปล่อย Run to Failure ได้
3. **จัดประเภท consequence และ Hidden/Evident** ด้วยผัง Nowlan & Heap หรือ SAE JA1012: Safety/Environment, Economic (Operational / Non-Operational) หรือ Hidden Failure ([[RCM Reliability Centered Maintenance]], [[PM Task Selection]]) ถ้า failure ซ่อนอยู่ เช่น protective device ให้ไปที่ [[Failure Finding Interval]]
4. **ดู β และ pattern ของ failure mode นั้น** ([[Weibull Analysis]], [[Failure Patterns and Bathtub Curve]]) ต้องมีข้อมูล time-to-failure ราย mode จาก CMMS ([[Failure Data Recording]]) กฎของหนังสือ: β < 1 PM แก้ไม่ได้ให้หาสาเหตุ, β = 1 time-based replace ไม่ช่วย ใช้ condition monitoring, β >> 1 ใช้ condition monitoring, replacement หรือ overhaul **ใน wiki นี้ไม่มี β ของ compressor** จึงข้ามขั้นนี้ไม่ได้จนกว่าจะมีข้อมูลของ Valeura
5. **เลือกประเภทงาน** ตามลำดับคำถามแบบง่าย (RBMM p.182-183): Condition Monitoring ทำได้และคุ้มหรือไม่ แล้ว scheduled replacement/overhaul แล้ว failure finding (ถ้า Hidden) ที่เหลือ redesign หรือ Run to Failure ดู [[P-F Interval and Condition Monitoring]]
6. **หาคาบ**: condition monitoring ใช้ (P-F)/2, failure finding ใช้ FFI = 2 x U x MTBF, งาน time-based หาคาบที่ cost ต่อหน่วยเวลาต่ำสุดด้วย Cp/Cf หรือ Monte Carlo ([[PM Interval Optimization]], [[Monte Carlo Maintenance Simulation]]) ค่า P-F ของ compressor ไม่มีใน sources ต้องมาจากประวัติหรือผู้ผลิต
7. **เตรียมอะไหล่**: ให้ Part Criticality ตามราคา lead time และตรวจล่วงหน้าได้หรือไม่ แล้วกำหนด stock/ซื้อตรง ([[Spare Part Criticality and Risk]], [[Spare Parts Management]], [[EOQ and Reorder Point]])

## ตัวอย่างการใช้ (ข้อเสนอของ wiki ไม่ใช่ข้อมูลใน sources)

| Failure mode | ข้อสังเกตจากหน้า wiki | ข้อมูลที่ยังขาด |
|---|---|---|
| [[ELP External Leakage Process Medium]] | consequence อาจสูงด้าน Safety/Environment จึงควรจัดระดับแยกจาก ELU | β ของ seal, P-F ของการรั่ว, ผลกระทบจริงของ asset |
| [[UST Spurious Stop]] | ส่วนใหญ่มาจาก Instruments/Control unit ตาม OREDA อาจเกี่ยวกับ failure finding ของ loop ป้องกัน | อัตราการเสียสัมบูรณ์ ผลต่อ production |
| VIB, OHE | อาจเหมาะกับ condition monitoring | P-F interval ของ bearing/seal |

## ดูเพิ่ม

- [[RBMM Concepts vs Compressor Failure Hierarchy]]
- [[FMECA]]
- [[Which failure modes dominate compressor failure rate]]

## Triplets

- Define Analysis Unit [step_of:: [[How to choose PM task for a compressor failure mode]]] step 1: failure mode per maintainable item, not per equipment (RBMM p.185)
- Assess Criticality [step_of:: [[How to choose PM task for a compressor failure mode]]] step 2: Consequence x Likelihood, A/B/C
- Classify Consequence And Hidden/Evident [step_of:: [[How to choose PM task for a compressor failure mode]]] step 3: Nowlan & Heap or SAE JA1012
- Check Beta And Failure Pattern [step_of:: [[How to choose PM task for a compressor failure mode]]] step 4: needs time-to-failure per mode from CMMS
- Select Task Type [step_of:: [[How to choose PM task for a compressor failure mode]]] step 5: simplified question order (RBMM p.182-183)
- Determine Interval [step_of:: [[How to choose PM task for a compressor failure mode]]] step 6
- Prepare Spare Parts [step_of:: [[How to choose PM task for a compressor failure mode]]] step 7: part criticality by price, lead time, pre-checkability
- Define Analysis Unit [uses:: [[Maintainable Item]]] e.g. Seals x ELP
- Assess Criticality [uses:: [[Criticality Assessment]]] Commercial, Safety, Environment
- [[Criticality Assessment]] [selects:: [[RCM Reliability Centered Maintenance]]] class A uses full RCM tasks
- [[Criticality Assessment]] [selects:: Run To Failure] class C may run to failure; B/C drop ineffective PM
- Classify Consequence And Hidden/Evident [uses:: [[RCM Reliability Centered Maintenance]]] Safety/Environment, Economic (Operational/Non-Operational), Hidden
- Classify Consequence And Hidden/Evident [uses:: [[Failure Finding Interval]]] when failure is hidden, e.g. protective device
- Check Beta And Failure Pattern [uses:: [[Weibull Analysis]]]
- Check Beta And Failure Pattern [uses:: [[Failure Patterns and Bathtub Curve]]]
- [[Failure Data Recording]] [input_to:: Check Beta And Failure Pattern] time-to-failure per mode from CMMS
- [[Weibull Analysis]] [selects:: Root Cause Investigation] beta < 1: PM cannot fix, find cause
- [[Weibull Analysis]] [selects:: Condition Monitoring] beta = 1: time-based replacement does not help
- [[Weibull Analysis]] [selects:: Condition Monitoring] beta >> 1: condition monitoring, replacement or overhaul
- [[Compressor]] [has_value:: no beta] wiki has no beta of compressor; step 4 blocked until Valeura data
- Select Task Type [uses:: [[P-F Interval and Condition Monitoring]]] order: condition monitoring, scheduled replacement/overhaul, failure finding (if hidden), then redesign or run to failure
- Condition Monitoring Interval [has_formula:: (P-F)/2]
- [[Failure Finding Interval]] [has_formula:: FFI = 2 x U x MTBF]
- Determine Interval [uses:: [[PM Interval Optimization]]] time-based: minimum cost per unit time with Cp/Cf
- Determine Interval [uses:: [[Monte Carlo Maintenance Simulation]]]
- Prepare Spare Parts [uses:: [[Spare Part Criticality and Risk]]]
- Prepare Spare Parts [uses:: [[Spare Parts Management]]]
- Prepare Spare Parts [uses:: [[EOQ and Reorder Point]]]
- [[How to choose PM task for a compressor failure mode]] [depends_on:: [[Reliability Based Maintenance Management Book]]] sequence from the book
- [[ELP External Leakage Process Medium]] [related_to:: [[Criticality Assessment]]] consequence may be high for Safety/Environment, rate separately from ELU (wiki proposal)
- [[UST Spurious Stop]] [related_to:: [[Failure Finding Interval]]] mostly from Instruments/Control unit; may relate to failure finding of protective loop (wiki proposal)
- VIB [related_to:: Condition Monitoring] may suit condition monitoring (wiki proposal)
- [[OHE Overheating]] [related_to:: Condition Monitoring] may suit condition monitoring (wiki proposal)

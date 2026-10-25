---
title: Maintainability
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [maintainability, reliability, statistics, kpi, maintenance-management, cmrp, iso-14224, book]
sources: [cmrp.md, iso-14224.md, reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Maintainability

Maintainability = ความง่ายและความเร็วในการคืนสภาพ item หลัง failure วัดเป็นความน่าจะเป็นที่งานซ่อมเสร็จภายในเวลาที่กำหนด ขึ้นกับ design, ทักษะช่าง, procedure, test equipment และสภาพแวดล้อม (CMRP CMPR-04 p.24) หน้านี้รวมทฤษฎี maintainability จากสไลด์ [[CMRP Course]] (secondary teaching source) และเทียบกับนิยามเวลาของ [[ISO 14224]] ใน [[Maintenance Time Definitions]] และ MTTR ของ RBMM ใน [[Reliability Metrics]]

## 1. ฟังก์ชันพื้นฐาน: คู่เทียบกับ reliability (CMRP CMPR-04 p.25-26)

| Reliability | Maintainability |
|---|---|
| f(t) = pdf ของ time to failure | g(t) = pdf ของ time to repair |
| R(t) = 1 - F(t) | M(t) = ∫0..t g(s) ds (โอกาสซ่อมเสร็จภายใน t) |
| λ(t) = f(t)/R(t) | repair rate μ(t) = g(t)/(1 - M(t)) |
| MTTF = ∫0..∞ t·f(t) dt | MTTR = ∫0..∞ t·g(t) dt |

กรณี repair rate คงที่ (exponential):

```
M(t) = 1 - exp(-μ t) = 1 - exp(-t/MTTR),   μ = 1/MTTR
```

ตรงกับสูตรของ RBMM (RBMM p.176-177; ตัวอย่าง MTTR = 3.5 ชม. ได้ M(3) = 0.5756 ดู [[Reliability Metrics]]) และ ISO 14224 (cl. C.4.2) ที่บอกว่าถ้าเวลาซ่อมไม่ exponential ต้อง fit จากข้อมูลรายครั้ง สไลด์ยกตัวอย่างการระบุเป้าเป็นฟังก์ชันเวลา เช่น M(3 h) = 0.95 (CMRP CMPR-04 p.41)

**Flag ข้อผิดในสไลด์ (p.26)**: ตารางคู่เทียบเขียน label แถว MTTR เป็น "MTTF" และเขียน mean เป็น ∫f(t)dt กับ ∫g(t)dt ซึ่งผิด ค่าที่ถูกคือ ∫t·f(t)dt และ ∫t·g(t)dt (ปริพันธ์ของ pdf เพียงอย่างเดียวได้ 1 เสมอ) ตารางด้านบนใช้รูปที่ถูกแล้ว ไม่ใช่ contested

## 2. ค่าสำคัญ 3 จุดบน M(t) (CMRP CMPR-04 p.26)

- **Mean corrective time** ของระบบ ถ่วงด้วย failure rate: M̄ct = Σ(λi·M̄cti) / Σλi (unit ที่เสียบ่อยมีน้ำหนักมาก)
- **Median** = เวลาที่งานซ่อมเสร็จ 50%
- **Mmax ct** = เวลาที่ percentile กำหนด เช่น Mmax(95%) = 1 ชม. แปลว่า 95% ของงานซ่อมต้องเสร็จใน 1 ชม.

## 3. Distribution ของเวลาซ่อม (CMRP CMPR-04 p.27-30)

ใช้ได้ทั้ง normal, lognormal, exponential แต่ **lognormal ใช้มากที่สุด** เพราะงานซ่อมประกอบด้วยงานย่อยหลายชิ้นที่ความถี่และระยะเวลาไม่เท่ากัน ทำให้กระจายเบ้ขวา (ดูรูปทรง lognormal ใน [[Statistical Distributions for Maintenance]])

Lognormal: ให้ t' = mean ของ ln(t) และ s = SD ของ ln(t)

```
MTTR (mean)  = exp(t' + s^2/2)
Median       = exp(t')
Mmax(p)      = exp(t' + z_p * s)
```

| percentile p | z_p |
|---|---|
| 0.80 | 0.8416 |
| 0.85 | 1.036 |
| 0.90 | 1.282 |
| 0.95 | 1.645 |
| 0.99 | 2.326 |

(ค่า z ในสไลด์ตรวจแล้วถูก) mean > median เสมอเมื่อ s > 0 จึงไม่ควรรายงาน median ว่าเป็น MTTR

ถ้าไม่มีข้อมูล SD สไลด์ให้ประมาณด้วย exponential M(t) = 1 - exp(-t/MTTR) (p.30) ผลที่ตามมา (derived ไม่อยู่ในสไลด์): Mmax(95%) = MTTR x ln 20 ≈ **3.0 x MTTR** และ Mmax(90%) = MTTR x ln 10 ≈ 2.3 x MTTR ดังนั้นเป้า "95% เสร็จใน X ชม." ต้องใช้ MTTR ราว X/3 ถ้าเวลาซ่อมเป็น exponential

## 4. Active repair time และ 7 ขั้นตาม MIL-HDBK-472 (CMRP CMPR-04 p.39-40)

Active repair (corrective) แบ่ง 7 ขั้น:
1. Localization (หาตำแหน่ง fault คร่าว ๆ)
2. Isolation (ระบุชิ้นที่เสีย)
3. Disassembly
4. Interchange (เปลี่ยนหรือซ่อมชิ้น)
5. Reassembly
6. Alignment (ปรับตั้ง)
7. Checkout (ทดสอบยืนยัน)

- การลด MTTR ต้องทำตั้งแต่ design; BIT (built-in test) ลดเวลา localization/isolation ได้ แต่เพิ่ม hardware ที่เสียได้เอง (p.39)
- **Inactive time** = รออะไหล่ เครื่องมือ การขนส่ง และงานธุรการ อยู่นอก active repair (p.39-40)
- PM ที่ดีช่วยลดเวลา diagnosis และเวลาจัดหา (p.41)

## 5. การแตกเวลาหยุด (downtime) ตาม CMRP และเทียบกับ ISO / RBMM

รูปสไลด์แบ่ง downtime เป็น run-down, preparation/delay, active repair, waiting/delay, start-up (CMRP CMPR-04 p.22) และนิยาม MTTR ของ CMRP จำกัดที่ active repair 7 ขั้น (p.39)

| CMRP (CMPR-04 p.22, 39) | ISO 14224 ([[Maintenance Time Definitions]]) | RBMM ([[Maintenance KPIs]]) |
|---|---|---|
| MTTR = active repair เท่านั้น | ใกล้ MART (mean active repair time) | MTTR = Repair + wait labor (RBMM p.49-51) |
| Waiting/delay, inactive time | logistic + administrative delay ส่วนหนึ่งของ MDT | MWT (รออะไหล่) |
| Downtime รวม run-down และ start-up | run-down และ start-up **ไม่นับ** เป็น down time (cl. 8.3.3, p.34) | MDT = MTTR + MWT |

- ความต่างนี้เป็น **convention/ขอบเขตศัพท์** ไม่ใช่ข้อขัดแย้งเชิงตัวเลข (ไม่ตั้ง contested) แต่ต้องระวังเมื่อเทียบ MTTR ข้ามแหล่ง: MTTR ของ CMRP สั้นกว่า MTTR ของ RBMM เพราะ RBMM รวมเวลารอแรงงาน
- การวางรูป run-down/start-up ไว้ในแผนภาพ downtime ของสไลด์ขัดกับ ISO ที่นับสองช่วงนี้เป็น up time; wiki ถือว่า ISO เป็นมาตรฐานหลักเมื่อต้องบันทึกข้อมูล ส่วนสไลด์อาจใช้มุมมองเวลาสูญเสียการผลิต (การตีความของ wiki, confidence medium)

## 6. Maintainability allocation (CMRP CMPR-04 p.30-33)

กระจายเป้า MTTR ของระบบลง subsystem (คู่ขนานกับ [[Reliability Allocation]]):

```
(1) เงื่อนไขระบบ:          M̄ct = Σ λi·M̄cti / Σ λi
(2) ตาม failure rate:       M̄cti = M̄ct · Σλ / (n · λi)
```

- (2) ทำให้ unit ที่เสียบ่อยได้เป้า MTTR สั้นกว่า สไลด์เตือนว่า "สมเหตุผลแต่อาจทำไม่ได้จริง"
- (3) ระบบ upgrade ที่ใช้ L subsystem เดิม: หัก Σλi·M̄cti ของของเดิมออกก่อน แล้วแบ่งส่วนที่เหลือให้ (n - L) subsystem ใหม่ (p.31)
- (4-5) ถ่วงด้วย design feature: แปลง complexity, accessibility, testability เป็น weight coefficient ki ร่วมกับ λi
- **Time-characteristics model** (p.32-33): แยก common repair time (ขึ้นกับ layout/การออกแบบระดับบน เช่น preparation, approaching) ออกจาก individual repair time (ขึ้นกับผู้ออกแบบ unit เช่น assembly, adjustment) หัก common ออกจาก MTTR ก่อน แล้วจัดสรร individual ลงไป ทำให้แต่ละทีมได้เป้าที่ควบคุมได้จริง

## 7. ระดับงานบำรุงรักษา NF X60-000 (CMRP CMPR-04 p.35)

| ระดับ | ลักษณะงาน |
|---|---|
| 1 | งานง่าย เข้าถึงสะดวก ไม่ต้องใช้เครื่องมือพิเศษ |
| 2 | procedure ง่าย ใช้อุปกรณ์เพิ่มเติม |
| 3 | procedure ซับซ้อน หรือเครื่องมือเฉพาะ (เช่น thermography) โดยช่างที่มีคุณวุฒิ |
| 4 | ต้องมีความรู้เทคนิคเฉพาะทาง |
| 5 | ต้องใช้ know-how ของผู้ผลิต |

ตัวอย่างในสไลด์เป็น PV plant/inverter ข้อคิดหลัก: ต้นทุนบำรุงรักษาถูกกำหนดไปมากตั้งแต่ design สอดคล้องกับ [[Asset Life Cycle]] การเลือกสถานที่ทำงาน (on site, on-site workshop, off-site workshop) พิจารณาความปลอดภัย การเข้าถึง ทักษะ turnaround time และเกณฑ์เศรษฐศาสตร์ (training, transport, spare investment) (p.40-41)

## 8. Maintainability ในภาพ availability และ trade-off

- μ = 1/MTTR เป็นตัวป้อนของ inherent availability Ai = MTBF/(MTBF + MTTR) (CMRP CMPR-04 p.13, 21) ดู [[Availability and OEE]]
- การปรับ maintainability ในช่วงออกแบบทำได้ง่ายและประมาณค่าได้แม่นกว่าการปรับ reliability (CMRP CMPR-04 p.18-19)
- Dependability (IEC TC 56) รวม availability, reliability, maintainability และ maintenance support performance (p.12-13)

## เชื่อมโยงกับ compressor failure hierarchy

- [[OREDA]] ไม่ให้ MTTR ต้องเก็บ active repair time และ down time ต่อ failure record ใน [[CMMS]] ตาม ISO 14224 Table 8 แล้ว fit lognormal ราย [[Maintainable Item]] (การประยุกต์ของ wiki ไม่ใช่ข้อมูลใน sources)
- ใช้สูตร M̄ct = Σλi·M̄cti/Σλi ระดับ [[Compressor]] โดยใช้ λ ของ item จาก OREDA เป็นน้ำหนักได้ ถ้ามี MTTR ราย item จากไซต์ (ข้อเสนอแนะ, confidence low)

## ดูเพิ่ม

- [[Maintenance Time Definitions]]
- [[Reliability Metrics]]
- [[Availability and OEE]]
- [[Reliability Allocation]]
- [[CMRP Course]]

## Triplets

- [[Maintainability]] [defined_in:: [[CMRP Course]]] ease and speed of restoring an item after failure (CMRP CMPR-04 p.24)
- [[Maintainability]] [depends_on:: Design] also skills, procedures, test equipment, environment (CMRP CMPR-04 p.24)
- Repair Time PDF g(t) [maps_to:: Probability Density Function] maintainability counterpart of f(t) (CMRP CMPR-04 p.25-26)
- [[Maintainability]] [has_formula:: M(t) = ∫0..t g(s) ds] probability repair completed by t (CMRP CMPR-04 p.25-26)
- Repair Rate [has_formula:: μ(t) = g(t)/(1 - M(t))] counterpart of hazard λ(t) (CMRP CMPR-04 p.26)
- MTTR [has_formula:: ∫0..∞ t·g(t) dt] corrected form (CMRP CMPR-04 p.26)
- [[Maintainability]] [has_formula:: M(t) = 1 - exp(-μ t) = 1 - exp(-t/MTTR)] exponential repair time (CMRP CMPR-04 p.30; RBMM p.176-177; ISO 14224 cl. C.4.2)
- CMRP Maintainability Table Mean Formula [has_formula:: ∫f(t)dt and ∫g(t)dt] as printed, wrong; MTTR row labelled MTTF (CMRP CMPR-04 p.26)
- CMRP Maintainability Table Mean Formula [contradicts:: MTTR] correct mean is ∫t·g(t)dt; slide error, not contested
- Mean Corrective Time [has_formula:: M̄ct = Σ(λi·M̄cti) / Σλi] failure-rate weighted (CMRP CMPR-04 p.26, p.30)
- Median Repair Time [has_value:: 50% of repairs completed] (CMRP CMPR-04 p.26)
- Mmax [has_value:: Mmax(95%) = 1 h means 95% of repairs within 1 h] slide example (CMRP CMPR-04 p.26)
- Lognormal Distribution [applies_to:: Repair Time] most used, repair is a mix of tasks of unequal frequency and duration (CMRP CMPR-04 p.27)
- MTTR [has_formula:: exp(t' + s^2/2)] lognormal, t' and s = mean and SD of ln t (CMRP CMPR-04 p.27-29)
- Median Repair Time [has_formula:: exp(t')] lognormal (CMRP CMPR-04 p.27-29)
- Mmax [has_formula:: exp(t' + z·s)] lognormal; z 0.90 = 1.282, 0.95 = 1.645, 0.99 = 2.326 (CMRP CMPR-04 p.28-29)
- Mmax [has_value:: Mmax(95%) ≈ 3.0 x MTTR] exponential, MTTR x ln 20, derived [confidence:: medium]
- Mmax [has_value:: Mmax(90%) ≈ 2.3 x MTTR] exponential, MTTR x ln 10, derived [confidence:: medium]
- [[Maintainability]] [has_value:: M(3 h) = 0.95] target expressed as function of time (CMRP CMPR-04 p.41)
- Localization [step_of:: Active Repair] step 1 (MIL-HDBK-472 via CMRP CMPR-04 p.39)
- Isolation [step_of:: Active Repair] step 2
- Disassembly [step_of:: Active Repair] step 3
- Interchange [step_of:: Active Repair] step 4
- Reassembly [step_of:: Active Repair] step 5
- Alignment [step_of:: Active Repair] step 6
- Checkout [step_of:: Active Repair] step 7
- Active Repair [defined_in:: MIL-HDBK-472] seven steps (CMRP CMPR-04 p.39)
- BIT [produces:: Shorter Isolation Time] but adds hardware that can fail (CMRP CMPR-04 p.39)
- Inactive Time [differs_from:: Active Repair] waiting for spares, tools, transport, admin (CMRP CMPR-04 p.39-40)
- CMRP Downtime [has_part:: Run-down] with preparation/delay, active repair, waiting/delay, start-up (CMRP CMPR-04 p.22)
- CMRP MTTR [maps_to:: MART] CMRP limits MTTR to active repair (CMRP CMPR-04 p.39); ISO MART, see [[Maintenance Time Definitions]] [confidence:: medium]
- CMRP MTTR [differs_from:: RBMM MTTR] RBMM MTTR = repair + wait labor (RBMM p.49-51); convention difference, not contested
- CMRP Downtime [differs_from:: Down Time] slide figure includes run-down and start-up; ISO 14224 cl. 8.3.3 excludes them
- Maintainability Allocation [has_formula:: M̄cti = M̄ct · Σλ / (n · λi)] failure-rate based (CMRP CMPR-04 p.30)
- Maintainability Allocation [has_parameter:: Weight Coefficient ki] complexity, accessibility, testability (CMRP CMPR-04 p.31)
- Maintainability Allocation [uses:: Common And Individual Repair Time] time-characteristics model, subtract common first (CMRP CMPR-04 p.32-33)
- Maintainability Allocation [related_to:: [[Reliability Allocation]]] parallel concept for MTTR targets
- NF X60-000 Maintenance Levels [has_value:: 5 levels] 1 simple to 5 manufacturer know-how (CMRP CMPR-04 p.35)
- Maintenance Cost [depends_on:: Design] largely fixed at design stage (CMRP CMPR-04 p.35); see [[Asset Life Cycle]]
- Repair Rate [input_to:: Inherent Availability Ai] μ = 1/MTTR, Ai = MTBF/(MTBF + MTTR) (CMRP CMPR-04 p.13, 21); see [[Availability and OEE]]
- Dependability [has_part:: [[Maintainability]]] with availability, reliability, maintenance support performance (CMRP CMPR-04 p.12-13)
- [[Maintainability]] [related_to:: [[Reliability Metrics]]]
- [[CMMS]] [source_of:: Repair Time] active repair and down time per record to fit lognormal per [[Maintainable Item]]; wiki suggestion [confidence:: low]

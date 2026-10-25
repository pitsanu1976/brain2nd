---
title: Reliability Growth Models
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [reliability-growth, reliability, statistics, weibull, cmrp]
sources: [cmrp.md, iso-14224.md]
confidence: medium
contested: false
---

# Reliability Growth Models

Reliability growth คือการที่ reliability ของระบบดีขึ้นเรื่อย ๆ ระหว่างพัฒนา/ทดสอบ เพราะพบ failure แล้วแก้ที่สาเหตุ (test-analyze-fix) model ของ reliability growth ใช้ fit ข้อมูลที่วัดได้แล้ว extrapolate ว่าเมื่อไรจะถึงเป้า เพื่อวางแผนทรัพยากรทดสอบและเจรจา requirement (CMRP CMPR-11 p.14) หน้านี้สรุป Duane postulate และ Crow-AMSAA จาก [[CMRP Course]] ส่วนสูตรเป็นความรู้ทั่วไปเพราะสไลด์ไม่ได้พิมพ์สูตร

## ข้อควรรู้เรื่องที่มาของสไลด์

เนื้อหา p.14 ยกมาจากบริบท **software reliability** (debugging, release, ROCOF): (CMRP CMPR-11 p.14)
- model แบบ equal-step สมมติว่าการแก้ fault แต่ละครั้งเพิ่ม reliability เท่ากัน ซึ่งไม่จริง
- Littlewood-Verrall (1973) ให้ขนาด step สุ่ม และยอมให้ reliability ลดลงได้เมื่อการแก้ไขสร้าง fault ใหม่ การปรับปรุงต่อครั้งเล็กลงตามเวลา

จึงต้องระวังเมื่อนำมาใช้กับอุปกรณ์ hardware/งานบำรุงรักษา ส่วน Duane และ Crow-AMSAA (p.15) เป็น model ของ hardware ที่ใช้ได้ตรงกว่า

## Duane model (CMRP CMPR-11 p.15)

- J.T. Duane (General Electric, 1962; สไลด์สะกด "General Electrical Company") พบจากข้อมูล 5 ระบบ (hydro-mechanical, aircraft generator, jet engine ฯลฯ)
- **Duane postulate**: plot cumulative failure rate เทียบ cumulative test time บน log-log จะได้เส้นตรง slope ลบ = growth rate α

```
λ_c(T) = N(T) / T = K · T^(-α)        (ความรู้ทั่วไป)
ln λ_c = ln K - α · ln T              -> เส้นตรงบน log-log, slope = -α
```

- α ยิ่งมาก reliability โตเร็ว (ความรู้ทั่วไป: ช่วงที่พบบ่อยราว 0.3-0.6 ไม่อยู่ในสไลด์) [confidence: low]
- ข้อจำกัด: เป็น empirical ไม่มีฐานสถิติสำหรับ confidence interval

## Crow-AMSAA model (CMRP CMPR-11 p.15)

- Larry H. Crow, US Army Materiel Systems Analysis Activity (AMSAA) ทศวรรษ 1970 อยู่ใน MIL-HDBK-189 (Appendix C)
- รูปแบบเดียวกับ Duane แต่มีฐานสถิติ: เป็น **non-homogeneous Poisson process (NHPP) ที่มี Weibull intensity** จึงประมาณ parameter, ทำ confidence interval และ goodness-of-fit ได้
- ใช้ติดตาม growth ภายใน test phase เดียว ให้: reliability ปัจจุบัน, ณ สิ้น phase, ถ้าขยายเวลา test และ growth rate

```
E[N(t)] = λ · t^β                     cumulative failures   (ความรู้ทั่วไป)
ρ(t)    = λ · β · t^(β-1)             failure intensity (Weibull form)
β < 1  -> intensity ลดลง = reliability growth
β = 1  -> HPP (λ คงที่)
β > 1  -> intensity เพิ่ม = เสื่อม
α (Duane) ≈ 1 - β
```

[confidence: low สำหรับสูตรชุดนี้ ไม่ได้พิมพ์ในสไลด์]

## ความสัมพันธ์กับ Weibull

- รูป intensity ของ Crow-AMSAA เหมือน hazard ของ Weibull ใน [[Weibull Analysis]] แต่ **ความหมายต่างกัน**: Weibull hazard ใช้กับ time to first failure ของ component ที่ไม่ซ่อม (แต่ละตัวอย่างเป็นอิสระ) ส่วน NHPP intensity ใช้กับเวลาสะสมของ **ระบบที่ซ่อมแล้วใช้ต่อ** (ความรู้ทั่วไป)
- สอดคล้องกับแนวทาง ISO ใน [[Weibull Analysis]] ที่ให้ใช้ Weibull กับ component และ power law กับ repaired system (ISO 14224 cl. C.3.1.2) ซึ่ง power law process คือรูปแบบเดียวกับ Crow-AMSAA
- β ของ Crow-AMSAA < 1 = ระบบดีขึ้น ตรงข้ามกับการตีความ β < 1 ของ Weibull ว่าเป็น infant mortality จึงไม่ควรเอาค่า β สองแบบมาเทียบกันตรง ๆ

## การใช้ในงานบำรุงรักษา (ตีความ)

- ใช้ติดตามผลของโครงการปรับปรุง reliability ของ bad actor (เช่น หลัง [[Root Cause Analysis]] หรือ redesign) ด้วยการ plot cumulative failure เทียบ cumulative operating time ของ asset ที่ซ่อมแล้วใช้ต่อ ถ้า slope ลดลง แสดงว่าการแก้ไขได้ผล (การตีความ ไม่อยู่ในสไลด์)
- ข้อมูลที่ต้องมี: วันที่/ชั่วโมงเดินเครื่องสะสมที่เกิด failure แต่ละครั้งของ failure mode เดียวกัน ตามฟิลด์ใน [[Failure Data Recording]]
- เป้าหมาย reliability ที่ใช้เทียบอาจมาจาก [[Reliability Allocation]]

## ดูเพิ่ม

- [[Weibull Analysis]]
- [[Failure Rate Estimation]]
- [[Reliability Allocation]]
- [[CMRP Course]]

## Triplets

- [[Reliability Growth Models]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-11 p.14-15)
- [[Reliability Growth Models]] [produces:: Time To Reach Reliability Target] fit then extrapolate, plan test resources (CMRP CMPR-11 p.14)
- Littlewood-Verrall Model [is_a:: [[Reliability Growth Models]]] software reliability, random step size, 1973 (CMRP CMPR-11 p.14)
- Littlewood-Verrall Model [applies_to:: Software Reliability] slide p.14 content is from software context
- Equal-Step Model [differs_from:: Littlewood-Verrall Model] equal reliability gain per fix, unrealistic (CMRP CMPR-11 p.14)
- Duane Model [is_a:: [[Reliability Growth Models]]] J.T. Duane, General Electric, 1962 (CMRP CMPR-11 p.15)
- Duane Model [has_formula:: ln λ_c = ln K - α · ln T] log-log linear, cumulative failure rate vs cumulative test time; formula general knowledge [confidence:: low]
- Duane Model [has_parameter:: Growth Rate Alpha] negative slope on log-log plot (CMRP CMPR-11 p.15)
- Crow-AMSAA Model [is_a:: [[Reliability Growth Models]]] Larry H. Crow, US Army AMSAA, 1970s (CMRP CMPR-11 p.15)
- Crow-AMSAA Model [is_a:: Non-Homogeneous Poisson Process] with Weibull intensity (CMRP CMPR-11 p.15)
- Crow-AMSAA Model [defined_in:: MIL-HDBK-189] Appendix C (CMRP CMPR-11 p.15)
- Crow-AMSAA Model [has_formula:: ρ(t) = λ · β · t^(β-1)] intensity; E(N(t)) = λ t^β; general knowledge [confidence:: low]
- Crow-AMSAA Model [produces:: Confidence Interval] also goodness-of-fit, current and end-of-phase reliability (CMRP CMPR-11 p.15)
- Crow-AMSAA Model [differs_from:: Duane Model] same pattern but statistical basis (CMRP CMPR-11 p.15)
- Growth Rate Alpha [has_formula:: α ≈ 1 - β] relation Duane to Crow-AMSAA, general knowledge [confidence:: low]
- Crow-AMSAA Model [related_to:: [[Weibull Analysis]]] Weibull-form intensity, but for repaired systems not time to first failure
- Crow-AMSAA Model [maps_to:: Power Law] ISO recommends power law for repaired systems (ISO 14224 cl. C.3.1.2)
- Crow-AMSAA Model [uses:: [[Failure Data Recording]]] cumulative operating time at each failure, interpretation [confidence:: low]

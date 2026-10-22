---
title: Failure Finding Interval
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [pm, rcm, reliability, maintenance-management, book, iso-14224]
sources: [reliability-based-maintenance-management.md, iso-14224.md]
confidence: medium
contested: false
---

# Failure Finding Interval (FFI)

Scheduled Failure Finding คืองานตรวจ/ทดสอบ Hidden Failure ของ protective device หรือ protective system (เช่น protective relay, overload protection, sequence protection, fire protection, breaker, switch gear) ที่เสียโดยไม่แสดงอาการ ถ้าตัวป้องกันเสียซ่อนและเครื่องที่ถูกป้องกันเสียพอดี จะเกิด Multiple Failure ที่ความเสียหายควบคุมไม่ได้ FFI คือคาบตรวจที่ทำให้ "Unavailability" ของตัวป้องกันต่ำพอ RBMM ใช้หลักของ SAE JA1012: FFI = 2 x Unavailability x MTBF ของตัวป้องกัน (RBMM p.183, p.212-215)

## นิยาม

| คำ | ความหมาย |
|---|---|
| Protective System | ตรวจจับความผิดปกติของ protected equipment แจ้งเตือน และ/หรือตัดพลังงาน/แยกระบบอัตโนมัติ เพราะรอคนไม่ทัน (p.183) |
| Hidden (non-evident) Failure | การเสียที่ไม่ปรากฏต่อผู้ใช้ในสภาพปกติ ดู [[PM Task Selection]] |
| Multiple Failure | ตัวป้องกันเสียซ่อน และ protected equipment เสียพร้อมกัน |
| FFI | คาบตรวจ failure finding (ช่วง A-C ในรูป 7.32) |
| U (Unavailability) | สัดส่วนเวลาที่ตัวป้องกันเสียโดยไม่ถูกตรวจพบ (ช่วง B-C) |

## สูตร (RBMM p.213-215)

```
U_prot  = 0.5 x FFI / M_TIVE            (ตัวป้องกันเสียเฉลี่ยกลางคาบ)
FFI     = 2 x U_prot x M_TIVE

M_TED   = MTBF ของเครื่องที่ถูกป้องกัน
M_TIVE  = MTBF ของอุปกรณ์ป้องกัน
M_MF    = MTBF ของ Multiple Failure   (ความน่าจะเป็นเสียต่อหน่วยเวลา = 1/MTBF)

1/M_MF  = (1/M_TED) x U_prot
U_prot  = M_TED / M_MF
FFI     = 2 x U_prot x M_TIVE = 2 x M_TIVE x M_TED / M_MF
```

ความหมาย: ถ้ากำหนด MTBF ของ multiple failure ที่ยอมรับได้ (M_MF) ก็คำนวณ FFI ได้จาก MTBF ของ protected equipment และของตัวป้องกัน ข้อจำกัด: ข้อมูลครบยาก และ failure rate ไม่คงที่เสมอ หนังสือจึงแนะนำ simulation ดู [[Monte Carlo Maintenance Simulation]]

## ตาราง Availability ที่ต้องการ กับ FFI (รูป 7.33, RBMM p.213)

FFI เป็น % ของ MTBF ของตัวป้องกัน (ตรงกับสูตร FFI = 2 x U คือ U = 1 ลบ Availability ตรวจแล้วสอดคล้องทุกแถว)

| Availability ของ protective function | FFI (% ของ MTBF ตัวป้องกัน) |
|---|---|
| 99.99% | 0.02% |
| 99.95% | 0.1% |
| 99.9% | 0.2% |
| 99.5% | 1% |
| 99% | 2% |
| 98% | 4% |
| 95% | 10% |

## ตัวอย่างการใช้ (derived)

ตัวอย่างต่อไปนี้ไม่ใช่ตัวเลขของหนังสือ เป็นการคำนวณประกอบ สมมติ protective device มี MTBF 20 ปี ต้องการ Availability 99.9% ตามตาราง FFI = 0.2% x 20 ปี = 0.04 ปี (ประมาณ 14.6 วัน) ถ้าลดเป้าเหลือ 99% FFI = 2% x 20 ปี = 0.4 ปี (ประมาณ 146 วัน)

## กฎปฏิบัติ

- Failure Finding ใช้เมื่อ failure mode เป็น hidden และไม่มี condition monitoring/replacement ที่คุ้มกว่า (ลำดับข้อ 3 ในรูป 7.3)
- ต้องตรวจทั้งโอกาสที่ตัวป้องกันเสียเองและโอกาสที่เครื่องถูกป้องกันเสีย
- อุปกรณ์สลับเปลี่ยนของระบบสำรอง (transfer switch) ต้องทำ Failure Finding ด้วย ดู [[Redundancy and Standby Systems]]
- ตัวอย่างในหนังสือ: ตัวป้องกันไฟรั่ว/ไฟดูดในบ้าน (p.212)

## มุมมอง ISO 14224 (sources: iso-14224.md)

- Annex C.6.2 ให้ test interval แบบ required availability: **τ = 2 · LPFD / λ** (C.51, p.225-226) เมื่อ LPFD = PFD เฉลี่ยที่ยอมรับ และ λ = failure rate ของตัวป้องกัน ถ้าแทน U = LPFD และ 1/λ = MTBF ของตัวป้องกัน จะได้ τ = 2 · U · MTBF ตรงกับ FFI = 2 x U x M_TIVE ของ RBMM (การเทียบนี้ derived โดย wiki) สมมติฐานร่วมกันคือ failure rate คงที่และ test ไม่ก่อความเสียหาย
- ISO เสริมกรณีทั่วไปที่รวม repair rate และความเสียหายจาก test (PFDavg = λτ/2 + λ/μ + γ/(μτ) เมื่อ γ = cycle failure rate, μ = repair rate (C.52, p.226 ตรวจกับภาพหน้าต้นฉบับแล้ว 2026-10-21 ต้นฉบับพิมพ์ชื่อเป็น "PDFavg") และ τopt = sqrt(2γ / (λ · μ)) (C.53, p.226)) และวิธี cost-benefit **τ\* = sqrt(2Cm / (Cf · λfto · f))** (C.55, p.226-227) สำหรับกรณีไม่มีเกณฑ์ risk สัมบูรณ์ ดู [[Failure Rate Estimation]]
- Annex F ผูกการ proof test เพื่อหา dangerous undetected (DU) failure เข้ากับ IEC 61508/61511 และ ISO/TR 12489 (cl. F.3, p.252-253) จึงยืนยันว่า FFI คือแนวคิดเดียวกับ proof-test interval ของงาน functional safety
- ต้องเก็บทั้ง failure ก่อน test (hidden จริง) และ failure ที่เกิดเพราะ test (cycle failure, human error, unavailability ระหว่าง test) (cl. C.6.1, p.225)
- failure fraction (safety critical failure ที่พบจาก test / จำนวน test) เป็นค่าประมาณแบบ conservative ของ PFDavg ไม่ใช่ safe failure fraction ของ IEC 61508 (Annex F.4, p.253-254) ดู [[Safety Critical Failure Classification]]

## เชื่อมโยงกับ compressor failure hierarchy

- ระบบ protection ของ [[Compressor]] (trip/shutdown, ESD, PSV, protective relay) เป็นผู้สมัครตรงของ Failure Finding; หนังสือไม่ได้ระบุ compressor ตรง ๆ และไม่ได้อ้าง IEC 61508 หรือ SIL (ความคล้ายกับ proof-test interval เป็นข้อสังเกตของเรา ซึ่งตอนนี้ได้ source ยืนยันแล้ว ดูหัวข้อ "มุมมอง ISO 14224" ด้านล่าง)
- failure mode ที่เกี่ยวกับ fail-to-function เช่น FTS (fail to start on demand) และ STP (fail to stop on demand) ใน [[Failure Mode]] เป็น mode แบบ on-demand ที่ปกติซ่อนอยู่จนถึงเวลาเรียกใช้ (ข้อเสนอแนะ ไม่ใช่ข้อมูลใน sources)
- OREDA ให้ failure rate ซึ่งใช้เป็น 1/M_TIVE ประมาณการได้ ดู [[OREDA]] แต่เป็นค่าคงที่ จึงตรงกับสมมติฐานของสูตร constant-rate (RBMM p.215 เตือนว่าความจริงไม่คงที่)

## ดูเพิ่ม

- [[PM Task Selection]]
- [[Redundancy and Standby Systems]]
- [[P-F Interval and Condition Monitoring]]
- [[Reliability Metrics]]
- [[Availability and OEE]]

## Triplets

- Hidden Failure [detected_by:: Scheduled Failure Finding] check/test of protective device or system (RBMM p.183, p.212-215)
- Scheduled Failure Finding [applies_to:: Protective System] (RBMM p.183)
- [[Failure Finding Interval]] [applies_to:: Scheduled Failure Finding] interval of failure finding task, span A-C in Fig 7.32
- Protective Relay [is_a:: Protective System] (RBMM p.183)
- Overload Protection [is_a:: Protective System] (RBMM p.183)
- Sequence Protection [is_a:: Protective System] (RBMM p.183)
- Fire Protection [is_a:: Protective System] (RBMM p.183)
- Breaker [is_a:: Protective System] (RBMM p.183)
- Switch Gear [is_a:: Protective System] (RBMM p.183)
- Multiple Failure [depends_on:: Hidden Failure] hidden protective failure plus protected equipment failure, uncontrolled damage (RBMM p.183)
- [[Failure Finding Interval]] [defined_in:: SAE JA1012] principle used by RBMM (RBMM p.183, p.212-215)
- [[Failure Finding Interval]] [has_formula:: FFI = 2 x U_prot x M_TIVE] (RBMM p.213-215)
- [[Failure Finding Interval]] [has_formula:: FFI = 2 x M_TIVE x M_TED / M_MF] (RBMM p.213-215)
- Unavailability [has_formula:: U_prot = 0.5 x FFI / M_TIVE] protective device fails on average mid-interval (RBMM p.213-215)
- Unavailability [has_formula:: U_prot = M_TED / M_MF] (RBMM p.213-215)
- Multiple Failure [has_formula:: 1/M_MF = (1/M_TED) x U_prot] (RBMM p.213-215)
- Unavailability [measures:: Undetected Protective Failure Time] share of time protective device is failed undetected, span B-C (Fig 7.32)
- [[Failure Finding Interval]] [has_parameter:: Unavailability] U_prot
- [[Failure Finding Interval]] [has_parameter:: M_TIVE] MTBF of protective device
- [[Failure Finding Interval]] [has_parameter:: M_TED] MTBF of protected equipment
- [[Failure Finding Interval]] [has_parameter:: M_MF] MTBF of Multiple Failure, tolerable value
- M_TIVE [is_a:: MTBF] protective device
- M_TED [is_a:: MTBF] protected equipment
- M_MF [is_a:: MTBF] multiple failure
- [[Failure Finding Interval]] [uses:: [[Monte Carlo Maintenance Simulation]]] recommended since data are hard to complete and failure rate not always constant (RBMM p.215)
- [[Failure Finding Interval]] [has_value:: 0.02%] of protective device MTBF at 99.99% availability (Fig 7.33, RBMM p.213)
- [[Failure Finding Interval]] [has_value:: 0.1%] of protective device MTBF at 99.95% availability (Fig 7.33)
- [[Failure Finding Interval]] [has_value:: 0.2%] of protective device MTBF at 99.9% availability (Fig 7.33)
- [[Failure Finding Interval]] [has_value:: 1%] of protective device MTBF at 99.5% availability (Fig 7.33)
- [[Failure Finding Interval]] [has_value:: 2%] of protective device MTBF at 99% availability (Fig 7.33)
- [[Failure Finding Interval]] [has_value:: 4%] of protective device MTBF at 98% availability (Fig 7.33)
- [[Failure Finding Interval]] [has_value:: 10%] of protective device MTBF at 95% availability (Fig 7.33)
- [[Failure Finding Interval]] [has_value:: 0.04 years] MTBF 20 years, 99.9% availability, about 14.6 days; derived example [confidence:: low]
- [[Failure Finding Interval]] [has_value:: 0.4 years] MTBF 20 years, 99% availability, about 146 days; derived example [confidence:: low]
- Scheduled Failure Finding [step_of:: [[PM Task Selection]]] question 3 of Fig 7.3, when hidden and no cheaper CM/replacement
- Scheduled Failure Finding [applies_to:: Transfer Switch] switching device of standby system
- Scheduled Failure Finding [applies_to:: Residual Current Protection] household example (RBMM p.212)
- Test Interval [has_formula:: τ = 2 · LPFD / λ] required availability method (ISO 14224 Annex C.6.2, C.51, p.225-226)
- Test Interval [alias_of:: [[Failure Finding Interval]]] with U = LPFD and 1/λ = MTBF gives τ = 2 · U · MTBF; comparison derived by wiki [confidence:: low]
- PFDavg [has_formula:: PFDavg = λτ/2 + λ/μ + γ/(μτ)] γ = cycle failure rate, μ = repair rate; original prints PDFavg (ISO 14224 C.52, p.226)
- Optimum Test Interval [has_formula:: τopt = sqrt(2γ / (λ · μ))] (ISO 14224 C.53, p.226)
- Cost-Benefit Test Interval [has_formula:: τ* = sqrt(2Cm / (Cf · λfto · f))] no absolute risk criteria (ISO 14224 C.55, p.226-227)
- [[Failure Finding Interval]] [alias_of:: Proof Test Interval] DU failure proof test (ISO 14224 cl. F.3, p.252-253)
- Proof Test Interval [defined_in:: IEC 61508] also IEC 61511 and ISO/TR 12489 (ISO 14224 cl. F.3, p.252-253)
- [[Failure Finding Interval]] [uses:: Test-Induced Failure Data] failures before test and caused by test: cycle failure, human error, test unavailability (ISO 14224 cl. C.6.1, p.225)
- Failure Fraction [differs_from:: Safe Failure Fraction] conservative estimate of PFDavg, not IEC 61508 SFF (ISO 14224 Annex F.4, p.253-254)
- Scheduled Failure Finding [applies_to:: [[Compressor]]] protection: trip/shutdown, ESD, PSV, protective relay; observation, book does not name compressor [confidence:: low]
- Scheduled Failure Finding [applies_to:: FTS] on-demand mode hidden until demand, suggestion [confidence:: low]
- Scheduled Failure Finding [applies_to:: STP] on-demand mode hidden until demand, suggestion [confidence:: low]
- M_TIVE [depends_on:: [[OREDA]]] OREDA failure rate approximates 1/M_TIVE; constant rate, RBMM p.215 warns real rate not constant

---
title: Availability and OEE
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [kpi, reliability, maintenance-management, book, iso-14224, cmrp, maintainability]
sources: [reliability-based-maintenance-management.md, iso-14224.md, cmrp.md]
confidence: medium
contested: true
---

# Availability and OEE

RBMM บทที่ 1 (Fig 1.2, p.17-20) โยง Reliability (MTTF) กับเวลาหยุด (MDT = MTTR + MWT) ไปยัง Availability แล้วคูณ Speed และ Quality ได้ OEE ซึ่งเชื่อมต่อกับปริมาณผลิตและงบการเงิน ส่วนบทที่ 3 ใช้ OEE เป็นตัวชี้ผลที่ส่วน D ของ Strategic Report หน้านี้รวบรวมนิยามและความสัมพันธ์ พร้อมแยกว่าสูตรใดอนุมานเอง

## 1. ความสัมพันธ์ตาม Fig 1.2 (RBMM p.17, 20)

```
MDT = MTTR + MWT                      (หนังสือ Fig 1.2)
Availability ~ MTTF / (MTTF + MDT)    (derived: อนุมานจากรูป ไม่ใช่สูตรพิมพ์ชัดในหน้า)
OEE = Availability x Speed x Quality  (RBMM p.19-20)
```

| ตัวแปร | ความหมาย | เจ้าของหลัก |
|---|---|---|
| MTTF | อายุเฉลี่ยที่เดินได้ก่อนเสีย (วัด Reliability) | Reliability / PM strategy |
| MTTR | เวลาซ่อมเฉลี่ย | Tools, Methods, ฝีมือ, Planning |
| MWT | เวลารอเฉลี่ย (รออะไหล่เป็นเหตุหลัก) | Logistics, Spare Part Stock Performance |
| MDT | เวลาหยุดเฉลี่ย | MTTR รวม MWT |
| Availability Factor | สัดส่วนปริมาณ/เวลาที่ผลิตได้จริงต่อที่ตั้งใจผลิต | เกือบ 100% เป็นของบำรุงรักษา (RBMM p.20) |
| Speed Factor, Quality Factor | ปัจจัยด้านการเดินเครื่อง | ส่วนใหญ่ฝั่งผลิต |

หมายเหตุ: ปริมาณผลิตขึ้นกับ Capacity, Production Plan และ OEE (RBMM p.19) ฝั่งบำรุงรักษาจึงควบคุมได้ผ่าน Availability เป็นหลัก

### ประเภทของ Availability (ความรู้ทั่วไป ไม่มีใน sources, confidence: low)

หัวข้อย่อยนี้ไม่ได้มาจาก RBMM เป็นการแบ่งที่ใช้ทั่วไปในงาน reliability engineering ความต่างอยู่ที่ว่านับเวลาหยุดประเภทใดบ้าง

> อัปเดต 2026-10-25: หัวข้อนี้เดิมเขียนจากความรู้ทั่วไป ตอนนี้มี **secondary source** แล้ว คือสไลด์ [[CMRP Course]] (CMRP CMPR-04 p.21-23) ที่ให้นิยามและสูตร Ai/Aa/Ao ชุดเดียวกัน ดูหัวข้อ "นิยามของ CMRP" ด้านล่าง ข้อความเดิมด้านล่างคงไว้เป็นประวัติ ระดับความเชื่อถือของชุดนี้ยกจาก low เป็น medium (สื่อการสอน ไม่ใช่มาตรฐาน) และยังคง contested กับชุดของ ISO 14224

| ประเภท | สูตร | นับเวลาหยุดอะไร | ใช้ทำอะไร |
|---|---|---|---|
| Inherent availability (Ai) | MTBF / (MTBF + MTTR) | เฉพาะเวลาซ่อมแก้ (corrective) | ความสามารถของการออกแบบ ไม่รวมผลของ PM และ logistics |
| Achieved availability (Aa) | MTBM / (MTBM + M) | เวลาซ่อมแก้ + เวลา PM (M = mean active maintenance time) | ผลของทั้งการออกแบบและแผน PM |
| Operational availability (Ao) | MTBM / (MTBM + MDT) | ทุกอย่าง รวมเวลารออะไหล่ รอคน และงานธุรการ | สิ่งที่หน้างานเจอจริง |

- MTBM = mean time between maintenance (รวมทั้ง corrective และ preventive)
- สูตร Availability ~ MTTF / (MTTF + MDT) ในหัวข้อ 1 ที่ใช้ MDT = MTTR + MWT จึงใกล้เคียง Ao มากที่สุด เพราะรวมเวลารอ (MWT)
- ปกติ Ai ≥ Aa ≥ Ao ถ้า Ai สูงแต่ Ao ต่ำ แปลว่าปัญหาอยู่ที่ logistics/อะไหล่หรือการวางแผน ไม่ใช่ที่ตัวเครื่อง (เชื่อมกับ MWT ใน [[Spare Parts Management]] และ MTTR ใน [[Maintenance KPIs]])
- ตัวป้อน MTBF/MTTF ดูการคำนวณใน [[Reliability Metrics]]

### นิยามของ CMRP (sources: cmrp.md, เพิ่ม 2026-10-25)

สไลด์ CMRP ให้นิยาม availability = สัดส่วนเวลาที่อยู่ในสภาพพร้อมใช้เมื่อถูกเรียกใช้ ณ เวลาสุ่ม; A = E[uptime] / (E[uptime] + E[downtime]) และถ้าไม่มี PM และซ่อมทันที A = MTBF/(MTBF + MTTR) (CMRP CMPR-04 p.17, 20)

| ประเภท (CMRP) | สูตร | downtime ที่รวม |
|---|---|---|
| Inherent Ai | MTBF / (MTBF + MTTR) | corrective เท่านั้น (ideal support) (p.21-22) |
| Achieved Aa | MTBMA / (MTBMA + MAMT) | active corrective + preventive ไม่รวม logistics/admin delay (p.22-23) |
| Operational Ao | MTBM / (MTBM + MDT) (p.23) | ทุกอย่าง รวม logistics รออะไหล่ admin |

- ชื่อตัวแปรต่างจากชุดความรู้ทั่วไปด้านบนเล็กน้อย: Aa ใช้ MTBMA (mean time between maintenance actions) และ MAMT (mean active maintenance time = เวลาเฉลี่ย corrective และ PM ถ่วงด้วยความถี่) แทน MTBM และ M; แนวคิดตรงกัน
- MTBMA = 1/(λ + f_PM) โดย f_PM = ความถี่ PM (สไลด์ p.23 อ่านไม่ชัด เขียนคล้าย "1/(λ/z)")
- **ความไม่สอดคล้องภายใน CMRP**: p.21 นิยาม Ao ด้วย MTBF/(MTBF + MDT) แต่ p.23 ใช้ MTBM/(MTBM + MDT) wiki บันทึกทั้งสองไว้ ไม่เลือก (ถ้ามี PM ตัวหารควรเป็น MTBM เพราะ PM ก็ทำให้หยุด เป็นการตีความของ wiki)
- MTTR ในสูตร Ai ของ CMRP จำกัดที่ active repair (CMRP CMPR-04 p.39) ดู [[Maintainability]] และ [[Maintenance Time Definitions]]
- นิยามเชิงเวลา (p.20): A(t) = Pr[X(t) = 1] (point availability), average availability บน [0, c] = (1/c)∫0..c A(t) dt และ limiting (steady-state) availability = limit เมื่อ c ไปอนันต์
- ระบบ high availability ระบุเป็น 99.98% หรือ 99.999% (p.18); RBD/FTA ใช้คำนวณ availability ระดับระบบโดยรวม redundancy, common cause, dormant failure, test coverage, spare stocking, logistics (p.21)
- Trade-off (p.18-19): maintenance ยก reliability ได้ไม่เกิน inherent reliability; ตัวอย่าง oil platform ยอมจ่าย cost of ownership สูงเพื่อ availability ที่เพิ่มเล็กน้อยเพราะ revenue loss สูงกว่ามาก

### นิยามของ ISO 14224 Annex C (sources: iso-14224.md)

มาตรฐาน [[ISO 14224]] กำหนดเฉพาะชุดนี้ (cl. C.2.3, p.211-213; Annex E KPI 7-8, p.243-250) ไม่มี Achieved availability (Aa) และไม่ใช้ MTBM

| ชื่อใน ISO | สูตร | นับเวลาหยุดอะไร |
|---|---|---|
| Intrinsic AI (ชื่อพ้อง technical, inherent) | MTTF / (MTTF + MTTRes) (C.10) | active maintenance time ของ corrective |
| Operational Ao | MUT / (MUT + MDT) (C.9) | down time จริงทั้งหมด รวม delay ทุกชนิด |
| Ao,y รายปี | (8760 - (tC + tP)) / 8760 (C.14) | corrective + preventive (tC, tP = ชั่วโมงหยุดต่อปี) |
| AT,y รายปี (technical) | (8760 - tC) / 8760 (C.15) | เฉพาะ corrective |
| KPI 7 AO และ KPI 8 AT (Annex E) | ระดับ taxonomy 6 | AO นับ CM+PM, AT นับเฉพาะ corrective สะท้อน intrinsic reliability |

- AI = Ao เฉพาะเมื่อ MDT = MTTRes AI เหมาะกับ reliability engineer ส่วน Ao เหมาะกับฝ่ายบำรุงรักษา และ Ao ไม่ใช่คุณสมบัติของเครื่อง แต่เป็นของเครื่องในบริบท (installation, procedure, policy, support) เพราะ MDT รวม detection, isolation, รออะไหล่, standby, ซ่อม, reinstatement (cl. C.2.3.2, p.212)
- ต้องประมาณ λ และ μ แยกกัน (λ จาก MTTF/MUT, μ จาก MTTRes หรือ MRT) สูตรเดียวไม่พอ ดู [[Failure Rate Estimation]] และ [[Maintenance Time Definitions]]
- การรวมหรือไม่รวมเวลา PM ใน Ao เป็นทางเลือก ไม่ใช่นิยามบังคับ (p.212-213)
- availability = ทำงานได้ ณ ขณะหนึ่ง ส่วน reliability = ทำงานต่อเนื่องตลอดช่วง (cl. C.2.1, p.210)

### เปรียบเทียบสองชุดนิยาม (contested: ผู้ใช้ต้องเลือก convention ของ wiki)

| ประเด็น | ความรู้ทั่วไป (ด้านบน, ไม่มีใน sources) | ISO 14224 (sourced) |
|---|---|---|
| Inherent / intrinsic | Ai = MTBF / (MTBF + MTTR) | AI = MTTF / (MTTF + MTTRes) ใช้ MTTF และ MTTRes ไม่ใช่ MTBF/MTTR |
| Achieved | Aa = MTBM / (MTBM + M) | ไม่มีนิยามนี้ ไม่มี MTBM |
| Operational | Ao = MTBM / (MTBM + MDT) | Ao = MUT / (MUT + MDT) |
| รวมเวลา PM | Aa รวม PM, Ai ไม่รวม | Ao รวม PM ได้ (ทางเลือก), AT ไม่รวม PM |
| ชื่อ "technical" | ไม่ใช้ | AT/technical = intrinsic ใช้แทนกันได้ |

อัปเดต 2026-10-25: ฝั่งซ้ายของตาราง (Ai/Aa/Ao) ตอนนี้มี source รองรับคือ CMRP CMPR-04 p.21-23 (secondary teaching source) จึงไม่ใช่ "ไม่มีใน sources" อีกต่อไป แต่ยังขัดกับ ISO 14224 (sourced standard) ในประเด็นเดิม SCHEMA ให้ถือว่า CMRP ที่ขัดกับ ISO เป็น contested จึงคง `contested: true` ไว้ ผู้ใช้ยังต้องเลือก convention

ทั้งสองชุดใช้แนวเดียวกัน (Ai/AI = ฝั่งเครื่อง, Ao = ฝั่งหน้างาน) ต่างที่ตัวแปรและการมีหรือไม่มี Aa ข้อสังเกตของ wiki (ไม่ใช่ข้อความมาตรฐาน): สูตรแบบ MTBM น่าจะมาจากธรรมเนียม MIL/DoD (ความรู้ทั่วไป, confidence: low) wiki ยังไม่เลือกว่าจะยึดชุดใด ถ้ารายงานต้องเทียบ benchmark แบบ [[OREDA]] หรือ ISO ควรใช้ AI/Ao/AT ของ ISO และระบุว่ารวม PM หรือไม่ สูตร Availability ~ MTTF / (MTTF + MDT) ในหัวข้อ 1 ใกล้เคียง Ao ของ ISO (MUT / (MUT + MDT)) มากที่สุด (derived)

## 2. ตัวอย่างสมมติ (ไม่ใช่ข้อมูลจากหนังสือ)

ใช้ตัวเลขสมมติเพื่อดูผล: MTTF = 2,000 ชม., MTTR = 20 ชม., MWT = 30 ชม. ได้ MDT = 50 ชม. Availability ประมาณ 2,000 / 2,050 = 97.6% (derived, สมมติ) ถ้าลด MWT เหลือ 10 ชม. (จัดอะไหล่ดีขึ้น) MDT = 30 ชม. Availability ประมาณ 98.5% แสดงว่าเวลารออะไหล่ส่งผลตรงต่อ Availability

## 3. Availability ในดัชนีบริหาร (Fig 2.9, RBMM p.49-51)

- กิจกรรม 2: % Asset Utilization = เวลาที่เครื่องเดินได้จริง / เวลาตามแผนผลิตทั้งสิ้น
- กิจกรรม 4 ลดเวลาหยุดนอกแผน: ดัชนี Unplanned Down Time, Unit Availability/Availability Factor, MDT
- กิจกรรม 5 ปรับปรุงความน่าเชื่อถือ: MTTF
- กิจกรรม 6 ลดเวลาหยุดตามแผน: Planned Downtime (ต้อง Maintainability สูง, Planning ดี, Optimum PM)
- กิจกรรม 8 ลดเวลาซ่อม: MTTR (Repair + Wait labor), Maintainability
- กิจกรรม 9 Stock Performance: Turnover, Stockout Rate, Service Factor, MWT
- Unplanned downtime ลดได้ 3 ทาง: MTTR สั้น, จำนวนครั้งซ่อมนอกแผนลด (Reliability สูง), MWT สั้น (RBMM p.50) ดู [[Maintenance KPIs]]

## 4. OEE ใน Strategic Report (RBMM p.63, 66, 83-84)

- ส่วน D ของรายงานแสดงผลผลิตจริงเทียบเป้า (D1, D1.2) ซึ่ง D1.2 คือ variance ของ OEE ที่ปนผลของงานผลิตกับงานบำรุงรักษา ผลลบ = OEE ต่ำกว่าเป้า ต้องตรวจว่าเกิดจากบำรุงรักษาหรือไม่
- อุดมคติคือแสดงเฉพาะส่วน OEE ที่พลาดเพราะบำรุงรักษา แต่ทำยาก จึงใช้ OEE รวม หรือแสดงเฉพาะ Availability Factor
- ตัวอย่าง P1/P2/P3: ผลผลิตจริง 376,000 / 477,500 / 576,000 variance (4,000) / 2,500 / 6,000 แต่ต้องดูควบกับ cost per unit (D2.2: 4.63 / (6.89) / (11.41)) เพราะ OEE พลาดแต่ต้นทุนต่อหน่วยต่ำกว่างบก็ชดเชยกันได้ ดู [[Maintenance Strategic Report]]
- ส่วนเชิงงบ: เพดานค่าสูญเสียอาจกำหนดเป็นจำนวนครั้ง เวลาหยุด Availability หรือ OEE แล้วแปลงเป็นเงิน (ch10) ตัวอย่างงบมี Budget OEE 95% ต่อ Process (ดู [[Maintenance Budget]]) ตัวเลข 95% นี้มาจากบันทึกบทที่ 10 ยังไม่ยืนยันกับต้นฉบับ
- ผู้บริหารควรได้ OEE (ปริมาณ), ต้นทุนทั้งหมดต่อเครื่อง และ maintenance cost ต่อหน่วยผลผลิต (RBMM บทที่ 11)

## 5. แนวคิดที่ควรจำ

- Zero Plant Down Time ได้จาก Zero Equipment Down Time ของเครื่องที่ทำให้ทั้งโรงหยุดได้ (RBMM p.27) ดู [[Asset Life Cycle]]
- ระดับอุปกรณ์ในรายงาน Asset Performance: Equipment = Reliability, Availability, Maintainability; Component = Failure Rate (RBMM p.62-63)
- ระบบ redundancy เปลี่ยนความหมายของ Availability ระดับระบบ (ดู [[Reliability Block Diagram]] และ [[Redundancy and Standby Systems]])

## เชื่อมโยงกับ compressor failure hierarchy

- Failure rate ใน [[OREDA]] เป็น constant failure rate ต่อ 10^6 ชั่วโมง (ดู [[Reliability Metrics]]) แปลงเป็น MTTF ได้เมื่อสมมติ exponential (MTTF = 1/lambda ตาม ch12) ใช้เป็นตัวป้อน MTTF ในสูตร Availability ของ [[Compressor]] ได้ แต่ OREDA ไม่ให้ MTTR/MWT ต้องใช้ข้อมูล CMMS ของไซต์ (ไม่มีใน sources)
- โหมดที่ทำให้หยุดเครื่อง เช่น spurious stop และ fail to start (UST, FTS) กระทบ Availability โดยตรง ส่วนโหมดที่เป็นแค่ degraded เช่น low output (LOO) กระทบ OEE ด้าน speed/output ดู [[Failure Mode]]
- การลด MWT ผูกกับอะไหล่ของ [[Maintainable Item]] ที่ critical ดู [[Spare Part Criticality and Risk]]

## ดูเพิ่ม

- [[Maintenance KPIs]]
- [[Reliability Metrics]]
- [[Asset Life Cycle]]
- [[Spare Parts Management]]
- [[Maintainability]]

## Triplets

- RBMM MDT [has_formula:: MTTR + MWT] (RBMM Fig 1.2, p.17-20)
- Availability [has_formula:: MTTF / (MTTF + MDT)] derived from Fig 1.2, not printed [confidence:: low]
- OEE [has_formula:: Availability x Speed x Quality] (RBMM p.19-20)
- OEE [has_part:: Availability Factor] almost 100% owned by maintenance (RBMM p.20)
- OEE [has_part:: Speed Factor] mostly production side
- OEE [has_part:: Quality Factor] mostly production side
- MTTF [measures:: Reliability] owner Reliability / PM strategy
- MTTR [depends_on:: Tools, Methods, Skill, Planning]
- MWT [depends_on:: Spare Part Stock Performance] waiting mostly for spares; logistics
- Production Output [depends_on:: OEE] also Capacity, Production Plan (RBMM p.19)
- Inherent Availability Ai [has_formula:: MTBF / (MTBF + MTTR)] general knowledge, corrective only [confidence:: low] [contested:: true]
- Achieved Availability Aa [has_formula:: MTBM / (MTBM + M)] general knowledge, M = mean active maintenance time [confidence:: low] [contested:: true]
- Operational Availability Ao General [has_formula:: MTBM / (MTBM + MDT)] general knowledge, all downtime [confidence:: low] [contested:: true]
- MTBM [has_label:: Mean Time Between Maintenance] corrective and preventive [confidence:: low]
- Availability [related_to:: Operational Availability Ao General] MTTF/(MTTF + MDT) closest to Ao because it includes MWT
- Inherent Availability Ai [has_value:: Ai ≥ Aa ≥ Ao] high Ai with low Ao means logistics/spares or planning problem [confidence:: low]
- Intrinsic Availability AI [has_formula:: MTTF / (MTTF + MTTRes)] (ISO 14224 C.10, cl. C.2.3) [contested:: true]
- Operational Availability Ao ISO [has_formula:: MUT / (MUT + MDT)] (ISO 14224 C.9) [contested:: true]
- Annual Operational Availability Ao,y [has_formula:: (8760 - (tC + tP)) / 8760] (ISO 14224 C.14)
- Annual Technical Availability AT,y [has_formula:: (8760 - tC) / 8760] corrective only (ISO 14224 C.15)
- KPI 7 AO [measures:: Operational Availability Ao ISO] CM + PM, taxonomy level 6 (ISO 14224 Annex E)
- KPI 8 AT [measures:: Intrinsic Availability AI] corrective only (ISO 14224 Annex E)
- Intrinsic Availability AI [alias_of:: Technical Availability AT] synonyms technical, inherent (ISO 14224)
- Intrinsic Availability AI [has_value:: AI = Ao when MDT = MTTRes] (ISO 14224 cl. C.2.3.2, p.212)
- Operational Availability Ao ISO [depends_on:: MDT] context property: installation, procedure, policy, support
- Availability [depends_on:: Failure Rate] λ and μ estimated separately; see [[Failure Rate Estimation]] and [[Maintenance Time Definitions]]
- Availability [differs_from:: Reliability] availability at an instant, reliability over interval (ISO 14224 cl. C.2.1, p.210)
- Inherent Availability Ai [contradicts:: Intrinsic Availability AI] general uses MTBF/MTTR, ISO uses MTTF/MTTRes [contested:: true]
- Achieved Availability Aa [contradicts:: ISO 14224 Availability Set] ISO has no Aa and no MTBM [contested:: true]
- Operational Availability Ao General [contradicts:: Operational Availability Ao ISO] MTBM/(MTBM + MDT) vs MUT/(MUT + MDT) [contested:: true]
- Operational Availability Ao ISO [contradicts:: Operational Availability Ao General] ISO sourced; preferred for OREDA/ISO benchmarking, convention not chosen [contested:: true]
- MTBM Availability Formulas [defined_in:: MIL/DoD Convention] wiki observation, general knowledge [confidence:: low]
- Hypothetical Availability Example [has_value:: 97.6%] MTTF = 2,000, MTTR = 20, MWT = 30, MDT = 50 h; assumed not from book [confidence:: low]
- Hypothetical Availability Example [has_value:: 98.5%] MWT reduced to 10 h, MDT = 30 h [confidence:: low]
- Asset Utilization [has_formula:: actual running time / total planned production time] (RBMM Fig 2.9, p.49-51)
- Unplanned Down Time [measures:: Unit Availability] activity 4 indices with Availability Factor and MDT
- MTTF [is_a:: Maintenance KPI] activity 5 reliability improvement
- MTTR [is_a:: Maintenance KPI] activity 8, Repair + Wait labor
- MWT [is_a:: Maintenance KPI] activity 9 stock performance with Turnover, Stockout Rate, Service Factor
- Unplanned Down Time [depends_on:: MTTR] also number of unplanned repairs and MWT (RBMM p.50); see [[Maintenance KPIs]]
- OEE [input_to:: [[Maintenance Strategic Report]]] section D, D1.2 OEE variance (RBMM p.63, 66, 83-84)
- Strategic Report Example [has_value:: 376,000 / 477,500 / 576,000] actual output P1/P2/P3; variance (4,000) / 2,500 / 6,000
- Strategic Report Example [has_value:: 4.63 / (6.89) / (11.41)] D2.2 cost per unit
- Budget Example [has_value:: Budget OEE 95%] per process, from ch10 notes, unverified; see [[Maintenance Budget]] [confidence:: low]
- Zero Plant Down Time [depends_on:: Zero Equipment Down Time] of plant-stopping equipment (RBMM p.27); see [[Asset Life Cycle]]
- Asset Performance Report [has_part:: Failure Rate] component level; equipment level = Reliability, Availability, Maintainability (RBMM p.62-63)
- Availability [related_to:: [[Redundancy and Standby Systems]]] redundancy changes system availability; see [[Reliability Block Diagram]]
- [[OREDA]] [input_to:: Availability] MTTF = 1/lambda for [[Compressor]]; OREDA gives no MTTR/MWT
- [[UST Spurious Stop]] [contributes_to:: Availability] stops machine; also FTS
- [[LOO Low Output]] [contributes_to:: OEE] speed/output, degraded
- MWT [related_to:: [[Spare Part Criticality and Risk]]] critical spares of [[Maintainable Item]]
- [[Availability and OEE]] [related_to:: [[Spare Parts Management]]]
- Inherent Availability Ai [has_formula:: MTBF / (MTBF + MTTR)] corrective only, ideal support; CMRP now a secondary source (CMRP CMPR-04 p.21-22) [contested:: true]
- Achieved Availability Aa [has_formula:: MTBMA / (MTBMA + MAMT)] active corrective + preventive, no logistics/admin delay (CMRP CMPR-04 p.22-23) [contested:: true]
- Operational Availability Ao General [has_formula:: MTBM / (MTBM + MDT)] all downtime (CMRP CMPR-04 p.23) [contested:: true]
- CMRP Ao Definition p.21 [has_formula:: MTBF / (MTBF + MDT)] (CMRP CMPR-04 p.21)
- CMRP Ao Definition p.21 [contradicts:: Operational Availability Ao General] internal CMRP inconsistency, p.21 MTBF vs p.23 MTBM; not resolved
- MTBMA [has_formula:: 1/(λ + f_PM)] slide text unclear (CMRP CMPR-04 p.23) [confidence:: low]
- MAMT [has_label:: Mean Active Maintenance Time] corrective and PM times weighted by frequency (CMRP CMPR-04 p.23)
- Availability [has_formula:: E(uptime) / (E(uptime) + E(downtime))] (CMRP CMPR-04 p.17, 20)
- Point Availability [has_formula:: A(t) = Pr(X(t) = 1)] (CMRP CMPR-04 p.20)
- Average Availability [has_formula:: (1/c) ∫0..c A(t) dt] over (0, c) (CMRP CMPR-04 p.20)
- Limiting Availability [is_a:: Availability] steady state, limit as c goes to infinity (CMRP CMPR-04 p.20)
- Inherent Availability Ai [depends_on:: [[Maintainability]]] MTTR limited to active repair in CMRP (CMRP CMPR-04 p.39)
- Maintenance [depends_on:: Inherent Reliability] maintenance cannot raise reliability above inherent level (CMRP CMPR-04 p.18-19)
- Availability [defined_in:: [[CMRP Course]]] Ai/Aa/Ao set, secondary teaching source (CMRP CMPR-04 p.21-23)

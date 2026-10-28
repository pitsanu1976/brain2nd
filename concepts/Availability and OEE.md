---
title: Availability and OEE
created: 2026-10-20
updated: 2026-10-28
type: concept
tags: [kpi, reliability, maintenance-management, book, iso-14224, cmrp, maintainability, mpm]
sources: [reliability-based-maintenance-management.md, iso-14224.md, cmrp.md, maintenance-profit-maker.md]
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

## 6. มุมมองของ MPM (เพิ่ม 2026-10-28, sources: maintenance-profit-maker.md)

หนังสือ [[Maintenance Profit Maker Book]] (ผู้แต่ง 2 ใน 3 คนเดียวกับ RBMM) ขยายเรื่อง OEE ในบทที่ 3, 8, 10 และ 12 ถอดความจาก reading notes ค่าที่ wiki คำนวณเองระบุว่า derived

### 6.1 Total Productivity และ Planning Factor (MPM p.48-49)

ผลผลิตรวม (Total Productivity) ของเครื่องขึ้นกับ 3 ตัวแปร: Capacity (C), Planning Factor (P) และ OEE

```
Planning Factor (Pf) = Loading Time / Theoretical Production Time
Total Productivity   = Pf x OEE
สินค้าที่ผลิตได้      = OEE x Plant Capacity x Planning Factor     (MPM p.174, p.201)
```

- ตัวอย่าง Pf: 1 ปี 8,760 ชม. เดินวันละ 8 ชม. หยุดสัปดาห์ละ 2 วัน = (365 - 104) x 8 = 2,088 ชม. ได้ Pf = 23.84% (MPM p.49) Theoretical Production Time เป็นนโยบายที่กำหนดได้ (เช่น 5 วัน/สัปดาห์ 1 กะ)
- องค์ประกอบหลักของ Pf คือ **Planned Down Time** เช่น พักระหว่างวัน เปลี่ยนสินค้าตามแผน ปรับปรุงตามแผนลงทุน ลดกำลังผลิตเพราะความต้องการลด **PM ตามแผน** ตรวจตามวาระ ประชุม อบรม ขาดวัตถุดิบ การไฟฟ้าดับไฟ (MPM p.49)
- เครื่องที่หยุดซ่อมใหญ่นานกว่ามีฐานเวลาสั้นกว่า แม้ OEE เท่ากันก็ผลิตได้น้อยกว่า; ดู OEE โดยไม่ดู Total Productivity ทำให้เข้าใจผิดว่าเครื่องถูกใช้สูง (MPM p.58, p.174) การแปลงเป็นเงิน (Hidden Plant) ดู [[Maintenance Financial Impact]]

### 6.2 Six Big Losses (MPM p.49-52)

| กลุ่ม | Loss | ตัวอย่างย่อ |
|---|---|---|
| Availability | 1. Equipment failure / Breakdown | สาเหตุใหญ่สุด ทั้งเสียทันทีและเสื่อมสภาพ |
| Availability | 2. Set up and Adjustment | ปรับตั้งหลังซ่อมหรือเปลี่ยนสินค้า |
| Speed | 3. Reduced Speed | เดินต่ำกว่า Standard Speed (ต้องกำหนดไว้แต่แรก) |
| Speed | 4. Idle and Minor Stoppage | เดินเปล่า หยุดสั้นๆ เช่นของติด |
| Quality | 5. Quality Defect | ของเสีย ต้อง rework |
| Quality | 6. Start Up Losses | สูญเสียช่วงเริ่มเดินก่อนเข้าที่ |

ความสูญเสียมีทั้งแบบเรื้อรัง (chronic) และเป็นเหตุการณ์ (sporadic) OEE เป็นเพียงส่วนหนึ่งของเครื่องมือจัดการผลิต (MPM p.49-50)

### 6.3 สูตร Af / Sf / Qf ของ MPM (MPM p.50-52, p.148)

```
Availability Factor = (Loading Time - Unplanned Down Time) / Loading Time
Speed Factor        = (จำนวนที่ผลิตได้ x Theoretical Cycle Time) / (Loading Time - Down Time)
                      หรือ ผลผลิตจริง / ผลผลิตที่ควรได้ ที่ Theoretical rate (แบบนับชิ้น, MPM p.56)
Quality Factor      = จำนวนสินค้าดี / จำนวนที่ผลิตได้
OEE                 = Af x Sf x Qf
```

แถบเวลา (รูป 3.3 และ 10.5): A คาบเวลาที่พิจารณา -> หัก Planned Down Time = B Loading/Available to Run (Pf) -> หัก Unplanned Down Time = C Actual Run Time (Af) -> หัก Speed Loss = D Net Actual Speed Time (Sf) -> หัก Quality Losses = E Net Valuable Time (Qf)

### 6.4 ตัวอย่าง 1 กะ 8 ชม. (MPM p.53-54)

| รายการ | ชม. | ดัชนี | ผล |
|---|---|---|---|
| A คาบเวลา | 8.0 | | |
| B1 หยุดตามแผน (พัก 1 + PM 0.5) -> B | 1.5 -> 6.5 | Pf = B/A | 81.25% |
| C1 หยุด (เสีย-ซ่อม 0.5 + ปรับตั้ง 0.25) -> C | 0.75 -> 5.75 | Af = C/B | 88.46% |
| D1 speed loss เทียบเวลา -> D | 0.25 -> 5.50 | Sf = D/C | 95.65% |
| E1 quality loss เทียบเวลา -> E | 0.1 -> 5.40 | Qf = E/D | 98.18% |
| | | OEE = E/B | 83.07% |
| | | Total Productivity = E/A | 67.50% |

- ตรวจเลข (derived): ทุกค่าถูก แต่ 5.4/6.5 = 83.077% ปัดจริงคือ 83.08% (หนังสือตัดทศนิยม); สูตรในเล่มพิมพ์ C = B - B1 ที่ถูกคือ **C = B - C1** (ตัวเลข 5.75 ถูก)
- แต่ละ loss แก้ต่างวิธีและต่างคน: บำรุงรักษากระทบแผนหยุด เวลาหยุดนอกแผน ความเร็ว (เครื่องบำรุงไม่ดี) และคุณภาพ (สอบเทียบเครื่องวัดไม่ดี); ฝ่ายผลิตกระทบผ่านแผนผลิตที่ทำให้เปลี่ยนสินค้าบ่อยและคุณภาพวัตถุดิบ (MPM p.54)

### 6.5 ตัวอย่างโรงงาน XYZ เดิน 24 ชม. (MPM p.55-57)

| รายการ (1 เดือน 30 วัน) | ค่า |
|---|---|
| Theoretical Production Time | 720 ชม. |
| Planned Down Time (ไม่มีคำสั่งซื้อ 0, รอวัตถุดิบ 27, หยุดทำ PM 58, หยุดตามแผน 0) | 85 ชม. -> Loading 635 ชม. |
| Unplanned Down Time (ปรับตั้ง 4, เครื่องเสีย 87, ไฟดับในโรงงาน 0) | 91 ชม. -> เดินจริง 544 ชม. |
| Theoretical rate (หนังสือเรียก Cycle Time) | 60,000 หน่วย/ชม. -> ควรได้ 32.64 ล้านหน่วย |
| ผลผลิตจริง / ของเสีย | 31.28 / 1.323 ล้านหน่วย |

| Pf | Af | Sf | Qf | OEE | Total Productivity |
|---|---|---|---|---|---|
| 88.19% | 85.67% | 95.83% | 95.77% | **78.62%** | 69.34% |

- ตรวจเลข (derived): ถูกทุกค่า; "Theoretical Cycle Time 60,000 หน่วย/ชม." ที่จริงคือ rate (cycle time = 1/60,000 ชม./หน่วย)
- ตัวอย่างนี้จัดรอวัตถุดิบเป็น planned และไฟดับในโรงงานเป็น unplanned ขณะที่ p.49 จัด "การไฟฟ้าดับไฟ" (ภายนอก) เป็น planned หนังสือไม่อธิบายการแยก (ตีความ: เหตุภายนอกที่ฝ่ายผลิต/บำรุงรักษาคุมไม่ได้อยู่นอก OEE)

### 6.6 เป้าหมายและ benchmark (MPM p.55, p.213)

- **World Class Manufacturing: OEE ไม่ต่ำกว่า 85%** จาก Availability >= 90%, Speed >= 95%, Quality >= 99% (0.90 x 0.95 x 0.99 = 84.6% ปัดเป็น 85%, derived)
- ค่าสูงสุดที่ทำได้รายอุตสาหกรรม (MPM p.55):

| อุตสาหกรรม | OEE | Total Productivity |
|---|---|---|
| Manufacturing | 85% | 60% |
| Process | > 90% | > 68% |
| โลหะ (Metallurgy) | 75% | 55% |
| กระดาษ (Paper) | 95% | > 70% |
| ปูนซีเมนต์ (Cement) | > 80% | 60% |

- ตัวอย่างการตั้งเป้าจากช่องว่าง: โรงงานปิโตรเคมีชนิดหนึ่ง OEE เฉลี่ย 90% ถ้าวัดได้ 85% ด้อย 5 จุด แปลงเป็นเงินเพื่อหาความคุ้มของการลงทุน (MPM p.213)
- ใช้ OEE ได้ทั้ง internal (trend, เทียบหลายหน่วย) และ external (เทียบอุตสาหกรรม) แต่วิธีคิดต้องเป็นมาตรฐานเดียวกัน (MPM p.54-55); Availability 100% ต้องถามว่ารวมอะไรและมี redundancy มากเกินจนมองไม่เห็นการหยุดหรือไม่ (MPM p.210)

### 6.7 กับดักการตีความ: อย่าตัดสินจาก OEE ตัวเดียว (MPM p.57-58)

| | หน่วยผลิต 1 | หน่วยผลิต 2 |
|---|---|---|
| Availability | 99% | 98% |
| Speed | 80% | 95% |
| Quality | 95% | 89% |
| OEE | 75% | 83% |

- ดู OEE อย่างเดียวจะคิดว่าหน่วย 2 ดีกว่า แต่หน่วย 2 คุณภาพต่ำมาก ซึ่งแพงที่สุด เพราะของเสียใช้วัตถุดิบ ทรัพยากร พลังงานไปแล้ว ส่วน speed loss เสียพลังงาน และ downtime เสียโอกาสเดินเครื่อง (ตรวจ derived: 75.24% และ 82.86%)
- จุดตีความอื่น: หยุดนานเท่าไรจึงบันทึก (threshold), OEE เท่ากันแต่มาจาก loss ต่างกัน, ข้อมูลต้องมาจาก operator อย่างต่อเนื่องและละเอียด (MPM p.56-58)

### 6.8 ตัวอย่างดัชนีเครื่องจักร 720 ชม. (รูป 8.3, MPM p.149-151)

1 เดือน Loading 720 ชม. หยุด 3 ครั้ง เวลาซ่อม D1+D2+D3 = 70 ชม. เวลารอ W1+W2+W3 = 20 ชม.

| ดัชนี | สูตร MPM | ผล |
|---|---|---|
| Availability Factor | (Loading - Down Time) / Loading, Down Time = ซ่อม + รอ | (720 - 90)/720 = **87.50%** |
| MTBF | Total Up Time / จำนวนครั้งเสีย | 630/3 = **210 ชม.** |
| MTTR | Total Repair Time / จำนวนครั้งเสีย (ซ่อมล้วน) | 70/3 = **23.33 ชม.** |
| Mean Logistic Time (MLT) | Total Wait Time / จำนวนครั้งเสีย | 20/3 = **6.67 ชม.** |
| Failure Rate | 1 / MTBF | พิมพ์ 0.0047 ครั้ง/ชม. |

- **แก้ตัวเลข (derived)**: ข้อความในเล่มว่า Up Time U1-U4 "รวม 650 ชม." และเขียนสูตร U1+U2+U3 แต่การคำนวณใช้ 630 ชม. = 720 - 70 - 20 = U1+U2+U3+U4 ค่าที่ถูกคือ **630 ชม.**; Failure Rate 1/210 = 0.00476 ปัดเป็น **0.0048** ครั้ง/ชม.
- ใต้ Availability มี 4 ดัชนีสำคัญคือ MTBF, MTTR, MLT, Failure Rate และ MPM ใช้ Availability เป็น **เป้าของหน่วยงานบำรุงรักษาหลังฝ่ายผลิตวางแผนผลิตแล้ว** (MPM p.148)
- **ข้อขัดแย้ง MPM-C4**: MTTR ของ MPM บทที่ 8 = เวลาซ่อมล้วน แยกเวลารอเป็น MLT (MPM p.150-151) ต่างจาก RBMM ในหัวข้อ 1 และ 3 ของหน้านี้ที่ใช้ MDT = MTTR + MWT และ MTTR = Repair + Wait labor (RBMM p.17-20, p.49-51) และ MPM บทที่ 9 (p.166) เองกลับจัด MWT เป็นเป้าการลด MTTR wiki เก็บทั้งสองนิยามไว้ ยังไม่เลือก ใน Availability ตัวเลขออกมาเท่ากันเพราะทั้งสองแหล่งนับเวลาซ่อม + รอเป็น down time รายละเอียดดู [[Maintenance Time Definitions]] และ [[Reliability Metrics]]

### 6.9 Convention ที่ต้องระบุเมื่อเทียบข้ามแหล่ง

- **PM ไม่อยู่ใน Availability ของ MPM**: MPM จัด PM เป็น planned down time ใน Planning Factor (MPM p.49, p.53, p.56) Af จึงนับเฉพาะ unplanned down time ต่างจาก Ao ของ ISO 14224 (หัวข้อ 1) ที่รวมเวลา PM ได้ตามทางเลือก และต่างจาก Aa ของ CMRP ที่รวม PM ไม่ใช่ข้อผิด แต่ต้องบอก convention ทุกครั้งที่เทียบตัวเลข (การตีความของ wiki)
- **เจ้าของ Availability**: RBMM ว่า Availability Factor "เกือบ 100% เป็นของบำรุงรักษา" (RBMM p.20) ส่วน MPM จัด Set up and Adjustment (รวมการเปลี่ยนสินค้า) ไว้ใน availability losses และบอกว่าแผนผลิตที่เปลี่ยนสินค้าบ่อยกระทบเวลาสูญเสีย (MPM p.50, p.54) และ MWT มาจากความร่วมมือระหว่างบำรุงรักษากับผลิตเป็นหลัก (MPM p.175) ฝ่ายผลิตจึงมีส่วนใน Availability ด้วย เป็นความตึงระดับการแบ่งความรับผิดชอบ ไม่ได้ตั้งเป็นข้อขัดแย้ง
- **Availability สูงไม่ได้แปลว่า Reliability สูง**: เครื่องเสียบ่อยแต่ซ่อมเร็วก็ได้ A สูง (MPM p.166) MPM ผูกกลยุทธ์ Cost Leadership กับ Availability/MTTR และ Product Differentiation กับ Reliability/MTBF (MPM p.164-166, p.229)

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
- [[Maintenance Financial Impact]] (Hidden Plant, OEE -> กำไร)
- [[Maintenance Profit Maker Book]]

ดูเพิ่ม (หน้าจาก MPM ingest 2026-10-28): [[Maintenance Master Plan]], [[Maintenance Performance Improvement]]

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
- Total Productivity [has_formula:: Planning Factor x OEE] (MPM p.48-52)
- Planning Factor [has_formula:: Loading Time / Theoretical Production Time] (MPM p.48-49)
- Planning Factor Example [has_value:: 23.84%] 2,088 / 8,760 h, 8 h/day, 2 days off per week (MPM p.49)
- Planning Factor [depends_on:: Planned Down Time] includes planned PM, breaks, planned changeover, no raw material (MPM p.49)
- Production Output [has_formula:: OEE x Plant Capacity x Planning Factor] (MPM p.174, p.201); see [[Maintenance Financial Impact]]
- Six Big Losses [has_part:: Equipment Failure Breakdown Loss] availability group (MPM p.49-52)
- Six Big Losses [has_part:: Set Up and Adjustment Loss] availability group
- Six Big Losses [has_part:: Reduced Speed Loss] speed group
- Six Big Losses [has_part:: Idle and Minor Stoppage Loss] speed group
- Six Big Losses [has_part:: Quality Defect Loss] quality group
- Six Big Losses [has_part:: Start Up Loss] quality group
- MPM Availability Factor [has_formula:: (Loading Time - Unplanned Down Time) / Loading Time] (MPM p.50-52, p.148)
- MPM Speed Factor [has_formula:: (units produced x Theoretical Cycle Time) / (Loading Time - Down Time)] (MPM p.50-52)
- MPM Quality Factor [has_formula:: good units / units produced] (MPM p.50-52)
- OEE 8 Hour Shift Example [has_value:: OEE 83.07%] Pf 81.25%, Af 88.46%, Sf 95.65%, Qf 98.18%, TP 67.50%; exact 83.077% (MPM p.53-54)
- MPM Formula C = B - B1 [contradicts:: Formula C = B - C1] book misprint, figures correct (MPM p.53)
- XYZ Monthly OEE Example [has_value:: OEE 78.62%] Pf 88.19%, Af 85.67%, Sf 95.83%, Qf 95.77%, TP 69.34%, 720 h (MPM p.55-57)
- World Class OEE [has_value:: >= 85%] Availability >= 90%, Speed >= 95%, Quality >= 99% (MPM p.55)
- Industry Best OEE [has_value:: Manufacturing 85% / Process > 90% / Metallurgy 75% / Paper 95% / Cement > 80%] Total Productivity 60 / > 68 / 55 / > 70 / 60% (MPM p.55)
- OEE Unit Comparison Example [has_value:: unit 1 OEE 75% vs unit 2 OEE 83%] unit 2 Quality 89% is costliest loss; do not judge on OEE alone (MPM p.57-58)
- Quality Loss [differs_from:: Speed Loss] quality loss wastes material, resources and energy; speed loss wastes energy; downtime wastes opportunity (MPM p.58)
- Fig 8.3 Machine Index Example [has_value:: A 87.50%, MTBF 210 h, MTTR 23.33 h, MLT 6.67 h] 720 h, 3 failures, repair 70 h, wait 20 h (MPM p.149-151)
- Fig 8.3 Up Time Printed [has_value:: 650 h] book text; calculation uses 630 h (MPM p.149)
- Fig 8.3 Up Time [has_value:: 630 h] derived 720 - 70 - 20 = U1+U2+U3+U4
- Fig 8.3 Up Time Printed [contradicts:: Fig 8.3 Up Time] book error, derived
- Fig 8.3 Failure Rate [has_value:: 0.0048 per h] derived 1/210; book prints 0.0047
- MPM Availability Factor [depends_on:: Mean Logistic Time] with MTBF, MTTR, Failure Rate (MPM p.148)
- MPM MTTR [has_formula:: Total Repair Time / Number of Failures] repair only, wait separated as MLT (MPM p.150-151) [contested:: true]
- RBMM MTTR [has_formula:: Repair + Wait labor] (RBMM p.49-51) [contested:: true]
- MPM MTTR [contradicts:: RBMM MTTR] MPM-C4; MPM p.166 itself puts MWT under MTTR [contested:: true]
- MPM Availability Factor [differs_from:: Operational Availability Ao ISO] MPM puts PM in Planning Factor, ISO Ao may include PM; convention note
- Set Up and Adjustment Loss [depends_on:: Production Planning] frequent changeover from production plan affects availability (MPM p.50, p.54)
- Availability Factor [differs_from:: Reliability] high availability does not imply high reliability (MPM p.166)
- Cost Leadership Strategy [depends_on:: MTTR] lead index Availability (MPM p.164-166)
- Product Differentiation Strategy [depends_on:: MTBF] lead index Reliability (MPM p.164-166)
- Petrochemical OEE Benchmark Example [has_value:: 90%] measured 85% = 5 point gap converted to money (MPM p.213)
- [[Availability and OEE]] [defined_in:: [[Maintenance Profit Maker Book]]] chapters 3, 8, 10, 12

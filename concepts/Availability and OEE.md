---
title: Availability and OEE
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [kpi, reliability, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
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

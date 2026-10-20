---
title: Failure Patterns and Bathtub Curve
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [reliability, weibull, failure-rate, rcm, pm, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Failure Patterns and Bathtub Curve

รูปแบบการเสีย (failure pattern) คือรูปร่างของ failure rate เทียบกับเวลาของแต่ละ failure mode หนังสือ RBMM แบ่งเป็น 5 แบบ (A-E) และผูกกับค่า Weibull β ส่วน bathtub curve เป็นภาพรวมระดับเครื่องที่เกิดจากการรวมหลายชิ้นส่วน หน้านี้สรุปทั้งสองแนวคิด พร้อมกฎเลือกประเภทงาน PM ตามค่า β (RBMM ch7) และจุดที่หนังสือไม่สอดคล้องกันเอง

## Failure pattern A-E (RBMM p.155-158)

| Pattern | ลักษณะ failure rate | ตัวอย่างพารามิเตอร์ | β |
|---|---|---|---|
| A | ต่ำมากช่วงต้น แล้วพุ่งเร็วช่วงปลาย (wear-out ชัด) | β = 15, η = 30,000 | >> 1 |
| B | ไม่คงที่ เพิ่มค่อย ๆ | β = 3, η = 30,000 | > 1 |
| C | ต่ำช่วงแรก แล้วเพิ่มและคงที่ | β = 1.5, η = 5,000 | > 1 เล็กน้อย |
| D | คงที่ตลอด (random) | β = 1, η = 5,000 | = 1 |
| E | สูงมากช่วงแรกแล้วลดเร็ว (infant mortality) | β = 0.5, η = 5,000 | < 1 |

หน่วยของ η ไม่ระบุชัดใน notes (ตัวอย่างอายุอยู่ในช่วงชั่วโมงหรือหน่วยอายุอื่น)

β กำหนดรูปการกระจาย 3 แบบ (RBMM p.156-157):
- β > 1 รูประฆังคว่ำ ช่วงต้นยังไม่คาดว่าจะเสีย (t1) หลังช่วงปลาย (t2) ไม่เหลือรอด เมื่อ η มากขึ้น (β เท่าเดิม) ระฆังแบนและกว้างขึ้น
- β ≈ 1 เหมือน Exponential density สูงตอนต้นแล้วลด failure rate คงที่
- β < 1 hyper-exponential density สูงมากตอนต้น failure rate ลดลง

อธิบาย Weibull เต็มที่ใน [[Weibull Analysis]]

## Bathtub curve (RBMM p.145-146, ch5)

กราฟอ่างอาบน้ำของ **เครื่องจักรทั้งเครื่อง** (Fig 5.24) มี 3 ช่วง:

| ช่วง | β | คำอธิบาย |
|---|---|---|
| Infant Mortality | < 1 | อัตราเสียลดลง จากชิ้นส่วนบกพร่องจากโรงงาน ประกอบผิด หรือใช้ผิด spec ผู้ผลิตรับประกันเฉพาะความผิดของตน |
| Normal Usage Period | = 1 | เสียแบบสุ่ม แต่ยังต้อง PM เพราะเครื่องมีชิ้นส่วนหลายแบบ (A-E) ต้องพิจารณาว่าชิ้นใดสำคัญ |
| Designed Life End (wear-out) | > 1 | อัตราเสียเพิ่ม บางระบบซ่อมไม่คุ้มต้องซื้อใหม่ |

หนังสือชี้ว่าอ่างน้ำเกิดจากการรวมชิ้นส่วนหลายแบบ ระดับ **failure mode เดี่ยว** จึงควรดู pattern A-E (RBMM p.155) ใน ch12 ผู้เขียนกล่าวว่า failure rate มี 6 รูปแบบ เทียบกับ 6 pattern ของ RCM แต่ ch6 แสดง 5 แบบ และไม่ได้อธิบายแบบที่ 6 ใน notes (RBMM p.379)

## ตัวอย่างรถยนต์ (RBMM p.146-149, ch5)

- Lube oil อายุเฉลี่ย 13,000 กม. (ไม่ก่อน 8,000 ไม่เกิน 15,000) เปลี่ยนทุก 10,000 กม.
- Timing belt อายุเฉลี่ย 110,000 กม. ไม่เสียก่อน 90,000 ไม่เกิน 130,000 ผู้ผลิตกำหนดเปลี่ยนที่ 80,000 กม. (safe-life)
- Water pump มีสัญญาณเตือนล่วงหน้า ใช้ inspection ทุก 10,000 กม. แทนเปลี่ยนตามเวลา
- Gear box ออกแบบให้ชิ้นส่วนอายุใกล้กัน จึงเหมาะ scheduled overhaul
- ชิ้นที่เสียก่อน warranty (infant mortality) PM ไม่ช่วย สาเหตุคือชิ้นส่วน ประกอบ หรือ QC

## กฎเลือกประเภทงานตาม β (RBMM p.183-189, ch7)

| ช่วง β | กฎ |
|---|---|
| β < 1 | PM แก้ไม่ได้ ต้องแก้ที่สาเหตุ: อะไหล่ไม่ได้มาตรฐาน ฝีมือซ่อม การใช้งาน หรือตัวงาน PM เอง (เสียหลัง maintenance ไม่นาน) |
| β = 1 | scheduled replace/overhaul ไม่ช่วย ทางเลือกคือ condition monitoring ใช้กับชิ้นไม่สำคัญหรือ MTBF ยาวมาก อย่าให้ปนในกล่อง overhaul |
| β → 1 (ค่อนข้างเพิ่มช้า) | ทางเลือกหลักคือ condition monitoring |
| β >> 1 | condition monitoring, part replacement หรือ overhaul; ไม่ต้องตรวจเข้มช่วงต้นอายุ เริ่มตรวจก่อนถึง t1 |

**หลักฐานเชิงตัวเลขเมื่อ β = 1** (RBMM p.186-187): R(t) = exp(-t/η); ถ้าไม่เปลี่ยนตามแผนได้ R(120) = 47.0158% (conditional R(120/80) = 77.758%) ส่วนถ้าเปลี่ยนทุก 80 ชม. ได้ R(80) x R(40) = 60.4639% x 77.7585% = 47.0158% เท่ากัน ดังนั้น replacement ตามแผนไม่เพิ่ม reliability (η ในตัวอย่างอนุมานได้ราว 160 ชม. เป็น derived ไม่ได้ระบุในหน้า) ตัวอย่างหลอดไฟใน ch12 ให้ข้อสรุปเดียวกัน (เปลี่ยนทุก 1,000 หรือ 500 ชม. ยังได้ 72.57% ที่ 2,000 ชม., RBMM p.378) ดู [[Statistical Distributions for Maintenance]]

ตัวอย่างข้อมูล TTF 8,500-16,000 ชม. ได้ β ≈ 3.8 จึงเป็น pattern A (เกาะกลุ่ม) ไม่ใช่ pattern D ซึ่งทำให้สมมติ constant failure rate ผิด (RBMM p.199, ch7) ดู [[Weibull Analysis]]

## จุดที่หนังสือไม่สอดคล้องกัน (flag)

- **Fig 6.14 (RBMM p.165-166):** จับ A กับ β >>> 1, B/C/D กับ β ≈ 1, E กับ β < 1 แต่ตัวอย่างก่อนหน้า (p.155-156) ให้ B ที่ β = 3 ซึ่งไม่ใกล้ 1 ควรใช้ตัวเลขตัวอย่างเป็นหลัก
- **การระบุ infant mortality:** ch6 ระบุว่า pattern E คือ infant mortality และ D คือ random แต่ ch5 พูดถึง "Infant Mortality แบบ D" (RBMM p.148) และ ch7 จัด A/B เป็น β >> 1 มีอาการล่วงหน้า (ขัดกับตาราง ch6 ที่ B β = 3 ซึ่งไม่ >> 1) (RBMM p.207) ใช้นิยามของ ch6 เป็นหลัก
- ทั้งหมดนี้เป็นความไม่สอดคล้องภายในหนังสือ ไม่ขัดกับข้อมูลเดิมใน wiki จึงตั้ง `contested: false`

## เชื่อมโยงกับ compressor failure hierarchy

- Bathtub ระดับ [[Compressor]] ทั้งเครื่องเป็นผลรวมของ failure mode หลายตัวในหลาย [[Maintainable Item]] ต้องแยก pattern รายโหมด
- **สมมติฐาน (hypothesis, confidence low, ไม่ใช่ข้อเท็จจริงจาก source):** AIR (abnormal instrument reading) และ SER ใน [[Failure Mode]] อาจมีลักษณะใกล้ pattern D (random) หรือ E (หลัง maintenance) แต่ sources ไม่มีค่า β ของ compressor failure mode ใด ๆ จึงยืนยันไม่ได้ ส่วน wear-out เช่น seal/bearing อาจเป็น β > 1 ก็เป็นสมมติฐานเช่นกัน ต้องยืนยันจากข้อมูล failure จริงด้วย [[Weibull Analysis]]
- [[ELP External Leakage Process Medium]] และ [[ELU External Leakage Utility Medium]] จาก seal/gasket wear อาจ monitor ด้วย condition-based task แต่ไม่มี β ใน sources
- [[OREDA]] ใน wiki นี้มีแต่ % สัมพัทธ์ ไม่มี β หรือ failure rate สัมบูรณ์ (ถ้า handbook ใช้ failure rate คงที่ ซึ่งเทียบเท่า β = 1 ก็จะบดบังรูปแบบ A-E เป็นข้อสังเกตทั่วไป ไม่มีใน sources); [[Failure Mechanism]] ที่เกิดจากการเสื่อมตามอายุ (wear, fatigue) สัมพันธ์กับ β > 1 ส่วน infant mortality สัมพันธ์กับสาเหตุ assembly/installation ใน [[Failure Cause Codes]]

## ดูเพิ่ม

- [[Weibull Analysis]]
- [[Reliability Metrics]]
- [[PM Task Selection]]
- [[Failure Mode]]
- [[Failure Finding Interval]]

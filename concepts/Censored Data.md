---
title: Censored Data
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [reliability, weibull, statistics, data-quality, cmms, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Censored Data

ข้อมูล Time to Fail ที่ไม่สมบูรณ์ (incomplete / censored) คือกรณีที่ไม่ทราบอายุจนเสียแน่ชัด เช่น ชิ้นส่วนถูกเปลี่ยนตาม PM ก่อนเสีย หรือยังไม่เสียเมื่อหยุดสังเกต RBMM แบ่งเป็น Complete, Right, Left และ Interval censored และสอนวิธีใช้ **Mean Order Number (MON)** ปรับ Median Rank เพื่อ fit Weibull โดยไม่ทิ้งข้อมูล suspension หน้านี้สรุปประเภท ตัวอย่างตัวเลข และข้อสังเกตว่านิยามของ left censored ในหนังสือไม่ตรงกันระหว่าง ch6 กับ ch12

## ทำไมต้องจัดการ

Time to Fail ที่เป็น Complete Data ต้องรู้จุดเริ่มใช้และเวลาเสียจริง ระบบ CMMS จึงต้องบันทึกจุดติดตั้ง เวลาเริ่มใช้ เวลาที่เสียแล้วเปลี่ยน และแยกว่า "เสียจริง" หรือ "ถอดตามแผน Scheduled PM" (RBMM p.170-172) ดู [[CMMS]] และ [[Failure Data Recording]] ถ้าตัดข้อมูล suspension ทิ้ง ผลประมาณจะเอียง (ได้อายุสั้นเกินจริง) ถ้านับ suspension เป็น failure จะผิดมากกว่า

## ประเภทข้อมูล

| ชนิด | ความหมาย | ตัวอย่าง |
|---|---|---|
| Complete (F) | ทราบเวลาเสียแน่นอน | เริ่มใช้และเสียในช่วงสังเกต |
| Right Censored (S, suspension) | ใช้มาถึงระดับหนึ่งแล้วยังไม่เสีย หรือถูกเปลี่ยนก่อนเสีย | PM แบบ part replacement ตามชั่วโมง |
| Interval Censored | รู้ว่าเสียในช่วงระหว่างตรวจสองครั้ง แต่ไม่ทราบเวลาแน่ | ตรวจตามรอบ พบว่าเสียแล้ว |
| Left Censored | ไม่ทราบจุดเริ่มหรือเวลาเสีย (ดูข้อสังเกต) | hidden failure เช่น fuse, safety device |

### Fig 6.19: 6 กรณีเทียบช่วงสังเกต (RBMM p.171-172, ch6)

1. เริ่มและเสียในช่วงสังเกต: Complete
2. ยังใช้ได้ตอนจบช่วงสังเกต หรือถูกเปลี่ยนตาม PM: Right Censored
3. เหมือนข้อ 1: Complete
4. ไม่ทราบจุดเริ่ม แต่เสียในช่วง: Left Censored
5. ไม่ทราบจุดเริ่ม และยังใช้ได้หลังช่วงสังเกต: หนังสือเรียก Left Censored (ที่จริงเป็นทั้งซ้ายและขวา)
6. รู้ว่าเสียในช่วงแต่เวลาไม่แน่ชัด: Interval Censored

ข้อ 2, 4, 5, 6 ใช้วิเคราะห์ได้แต่ต้องมีวิธีถ่วงน้ำหนักเหมาะสม

### ข้อสังเกตนิยาม left censored

ch6 (p.171) ให้ left censored = ไม่ทราบ **จุดเริ่มใช้งาน** ส่วน ch12 (p.385) ให้ left censored = ทราบว่าใช้งานไม่ได้แล้วแต่ไม่รู้ **เวลาเสีย** (hidden failure) สองนิยามคนละมุม ไม่เสียหาย ใช้ทั้งสองได้แต่ต้องระบุว่าหมายถึงแบบใด ไม่ถือเป็น source conflict กับ wiki เดิม

## วิธีประมาณ (RBMM p.384-385)

- Complete: plot ด้วย Median Rank ตรง ๆ
- Interval และ Left: ใช้ค่ากลางของช่วงเป็นเวลา
- Right censored: plot เองไม่ได้ แต่ช่วยเพิ่มความแม่นยำโดยปรับ **ลำดับ (rank)** ของ failure ด้วย MON

```
MR = (MON - 0.3) / (N + 0.4)       N = จำนวนข้อมูลทั้งหมด (F + S)
MON = ค่าเฉลี่ยถ่วงน้ำหนักของตำแหน่งที่เป็นไปได้ของ failure นั้น
```

## ตัวอย่าง 1: ข้อมูล 5 ค่า (RBMM p.385-388)

เรียง: 456 (F1), 597 (S1), 879 (F2), 1009 (S2), 1207 (F3) เนื่องจากค่าจริงของ S1 และ S2 รู้เพียงว่ามากกว่า 597 และ 1009 ลำดับของ failure จึงมีหลายแบบ

- F1: ตำแหน่ง 1 เท่านั้น MON1 = 1
- F2: ตำแหน่ง 2 ได้ 6 แบบ ตำแหน่ง 3 ได้ 2 แบบ MON2 = (2x6 + 3x2)/8 = 2.25
- F3: ตำแหน่ง 3 (2 แบบ), 4 (3 แบบ), 5 (3 แบบ) MON3 = (3x2 + 4x3 + 5x3)/8 = 4.125

| MON | TTF | MR | x | y |
|---|---|---|---|---|
| 1 | 456 | 0.12963 | 6.12249 | -1.97446 |
| 2.25 | 879 | 0.36111 | 6.77878 | -0.80291 |
| 4.125 | 1207 | 0.70833 | 7.09589 | 0.208755 |

ผล (N = 5, failures = 3): Y regression β = 2.1740, η = 1163.94; X regression β = 2.2279, η = 1152.89

## ตัวอย่าง 2: มอเตอร์ bearing แตก (RBMM p.388-392)

ประวัติเสีย 6 รายการ แยก Unplanned = Complete (F), Planned = Right Censored (S) อายุ (วัน): 555 (F1), 856 (F2), 907 (S1, planned 2001), 936 (F3), 1,126 (S2, planned 2005) รายการ 1997 เป็นจุดเริ่ม

- F3 อยู่ตำแหน่ง 3, 4, 5 อย่างละ 2 แบบ MON3 = (2x3 + 2x4 + 2x5)/6 = 4 ได้ MON = 1, 2, 4 (MR = 0.1296, 0.3148, 0.6852)
- ผล: Y regression β = 3.5008, η = 996.70 วัน (หนังสือสรุป β = 3.5, η = 996.69); X regression β = 4.108, η = 958.15 (N = 5, failures = 3)
- β 3.5 > 1 เป็น wear-out จึงคุ้มกับ time-based PM จากนั้นหา interval ที่เหมาะ ~480 วัน ดู [[PM Interval Optimization]]

β = 3.5008 นี้เป็นข้อมูลคนละชุดกับ TTF 8,500-16,000 ชม. ใน [[Weibull Analysis]]

## เชื่อมโยงกับ compressor failure hierarchy

- ข้อมูล [[OREDA]] / [[ISO 14224]] มี surveillance period และแยก failure ออกจาก planned maintenance เป็นแนวคิดเดียวกับ censoring: planned replacement ของ seal/bearing ใน [[Compressor]] ต้องลงเป็น suspension ไม่ใช่ failure
- ต้องบันทึก installation date, failure date, operating hours, ประเภทงาน (planned/unplanned) ต่อ [[Maintainable Item]] และ [[Failure Mode]] ตาม [[Failure Cause Codes]] และ [[Resolution Codes]] เพื่อสร้าง TTF ได้
- hidden failure ของ protective device (PSV, trip) เป็น left/interval censored โดยธรรมชาติ ดู [[Failure Finding Interval]]

## ดูเพิ่ม

- [[Weibull Analysis]]
- [[Reliability Metrics]]
- [[Failure Data Recording]]
- [[Statistical Distributions for Maintenance]]

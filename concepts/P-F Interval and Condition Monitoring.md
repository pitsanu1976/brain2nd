---
title: P-F Interval and Condition Monitoring
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [pm, cbm, rcm, reliability, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# P-F Interval and Condition Monitoring

Condition Monitoring (CM) หรือ on-condition task คืองานตรวจสภาพตามกำหนดเพื่อจับ Potential Failure (จุด P) ก่อนเกิด Functional Failure (จุด F) แล้วซ่อมแบบวางแผน (CM-Planned) แทนการซ่อมนอกแผน (CM-Unplanned) RBMM จัดเป็นงานที่ถูกที่สุดและถามเป็นข้อแรกในลำดับเลือกงาน (ดู [[PM Task Selection]]) คาบตรวจกำหนดจาก P-F interval ด้วยหลัก "ครึ่งหนึ่งของ P-F" และใช้ได้เมื่อ failure mode มีอาการล่วงหน้า (pattern A/B, beta สูง)

## นิยาม (RBMM p.208-209)

| คำ | ความหมาย |
|---|---|
| P (Potential Failure) | จุดที่เริ่มตรวจพบอาการ เช่น สั่นเกิน สึกหรอ |
| F (Functional Failure) | จุดที่เสียจริง |
| P-F interval | ช่วงเวลาจาก P ถึง F มีค่าสั้นสุด/ยาวสุดต่างกัน (F1 vs F2) |
| Threshold of Life | อายุที่ใช้งานมาก่อนเริ่มกระบวนการสิ้นอายุ (เป็น % ของอายุ) |

P-F curve ไม่ใช่ PDF: PDF คือการกระจายของเวลาเสีย ส่วน P-F คือเวลาจากเห็นอาการถึงเสียจริง (p.208)

## ช่วงอายุที่ควรเริ่มตรวจ (รูป 7.24, RBMM p.207-208)

แบ่งอายุเป็น 3 ช่วงตาม F(t) จาก Weibull ดู [[Weibull Analysis]]

| ช่วง | เงื่อนไข | งาน CM |
|---|---|---|
| 1 ไม่น่าเสีย | F(t) น้อยกว่า 0.01 | ไม่ต้องทำ |
| 2 เริ่มมีเสียเล็กน้อย | F(t) น้อยกว่า 0.1 | ยังไม่ต้องทำเต็มรูปแบบ |
| 3 น่าเสีย | F(t) มากกว่า 0.1 | ทำ CM เต็มรูปแบบ |

## หลักคาบตรวจ

```
คาบตรวจ (CM interval) = (P-F interval) / 2     (RBMM p.208, p.211)
```

- ตรวจห่างเกินไป: อาจเสียก่อนตรวจครั้งต่อไป; ถี่เกินไป: สิ้นเปลือง
- ปัจจัยสำคัญ 2 อย่าง: P-F period และเงื่อนไขตรวจว่ามีอาการแล้วหรือยัง
- เมื่อพบอาการต้องรีบเปลี่ยนภายใน P-F period (ที่เหลือ)
- CM ราคาถูก มักใช้แรงงานภายใน ข้อจำกัดคือ utilization และเครื่องมือ (p.208)

## ตัวอย่าง Simulator (รูป 7.28-7.30, RBMM p.209-212)

ตัวเลขจากหน้า 211 ซึ่งหนังสืออ่านจากหน้าพิมพ์ ควรตรวจกับต้นฉบับถ้าจะอ้างต่อ

| ค่า | ตัวเลข |
|---|---|
| P-F | 4 เดือน (120 วัน) |
| คาบที่ทดลอง | เริ่ม 10 วัน เพิ่มทีละ 5 วัน |
| ค่า PM (ตรวจ) | 1,600 บาท/ครั้ง |
| CM-Planned | 570,000 บาท/ครั้ง |
| CM-Unplanned | 570,000 บาท/ครั้ง |

ผล: CM-Unplanned เริ่มมีนัยสำคัญที่คาบประมาณ 45-50 วัน; คาบที่เหมาะตรงกับ (P-F)/2 = 60 วัน (derived จาก 120/2); เมื่อคาบเกิน 60 วัน CM-Unplanned เพิ่ม และพุ่งเร็วเมื่อใกล้และเกิน 120 วัน (total cost สูงขึ้น, CM-Planned ลดลง) หมายเหตุ: ค่า CM-Planned เท่ากับ CM-Unplanned ที่ 570,000 บาท ตามที่บันทึกไว้ ซึ่งแปลก เพราะปกติ planned ควรถูกกว่า อาจเป็นข้อจำกัดจากการอ่านหน้ากระดาษ (ไม่ยืนยัน)

## โครงสร้างงานรวมของโมเดล CM (รูป 7.26-7.27, RBMM p.209-210)

```
Total Maintenance = Preventive (ตรวจ) + Corrective-Planned + Corrective-Unplanned
Output: จำนวน CM-Unplanned, PM, CM-Planned, Availability,
        ค่าใช้จ่ายต่อหน่วยเวลา, ค่าใช้จ่ายรวม
```

การคำนวณใช้ [[Monte Carlo Maintenance Simulation]] และคาบหาได้ด้วยแนวทาง [[PM Interval Optimization]]

## ทางเลือกตาม beta (สรุป)

- beta เท่ากับ 1: CM คือทางเลือกที่ scheduled replace ทดแทนไม่ได้ (อิเล็กทรอนิกส์ต้องคุมสภาพแวดล้อม: อุณหภูมิ ความชื้น คุณภาพไฟ, p.185)
- beta ใกล้ 1: CM เป็นทางเลือกหลักถ้าเข้าถึงง่าย (p.187)
- beta สูงมาก: ไม่จำเป็นต้องเข้มข้นตอนต้นอายุ เริ่มช่วงหลัง (p.188)
- CM-Planned กับ lead time ของอะไหล่: ต้อง stock อะไหล่หรือไม่ขึ้นกับว่า lead time ยาวกว่าเวลาที่เหลือก่อน CM-Unplanned หรือไม่ (RBMM p.241) ดู [[Spare Parts Management]]

## เชื่อมโยงกับ compressor failure hierarchy

- CM เหมาะกับ failure mode ที่มีอาการล่วงหน้าและกลไกสึกหรอ เช่น VIB (vibration), OHE (overheating), NOI (noise), PDE (parameter deviation) ใน [[Failure Mode]] และ mechanism ใน [[Failure Mechanism]] (การจับคู่เป็นข้อเสนอแนะ ไม่ใช่ข้อมูลใน sources)
- ค่า P-F ของ [[Maintainable Item]] ของ [[Compressor]] (เช่น bearing, seal) ไม่มีใน sources ของ wiki นี้ ต้องมาจากประวัติหรือผู้ผลิต
- ความรู้ทั่วไป ไม่มีใน sources: ISO 14224 มีฟิลด์ detection method ให้บันทึกว่าเจอเหตุผ่านการตรวจ (ไม่ได้มาจาก RBMM และยังไม่ verify กับตัวมาตรฐาน) ใช้แยก CM-Planned จาก CM-Unplanned ใน [[Failure Data Recording]]

## ดูเพิ่ม

- [[PM Task Selection]]
- [[PM Interval Optimization]]
- [[Failure Finding Interval]]
- [[Monte Carlo Maintenance Simulation]]
- [[Failure Patterns and Bathtub Curve]]

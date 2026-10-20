---
title: PM Task Selection
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [pm, rcm, reliability, weibull, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# PM Task Selection (การเลือกประเภทงานบำรุงรักษาป้องกัน)

หน้านี้สรุปวิธีเลือก "ประเภท" ของงาน PM ต่อ failure mode ตาม RBMM บทที่ 7 (และผังเลือกงานในบทที่ 5) มี 3 แนวทาง ได้แก่ (1) ลำดับคำถามแบบง่ายเรียงตามต้นทุน (2) ผัง Nowlan & Heap และ SAE JA1012 ตาม failure consequence (3) ใช้ Weibull beta ของ failure mode เป็นตัวชี้ จุดสำคัญคือต้องเลือกงานรายหนึ่ง failure mode ไม่ใช่ราย equipment และ failure mode ที่ beta น้อยกว่าหรือเท่ากับ 1 แก้ด้วย time-based PM ไม่ได้ ส่วนการเลือก "คาบ" ของงาน ดู [[PM Interval Optimization]]

## 1. งาน 5 ประเภท (Nowlan & Heap, RBMM p.180)

1. Scheduled Condition Monitoring (on-condition) ดู [[P-F Interval and Condition Monitoring]]
2. Scheduled Overhaul หรือ Discard/Replace (restoration/discard)
3. Scheduled Failure Finding ดู [[Failure Finding Interval]]
4. Run to Failure (RTF)
5. Re-design

ผังเลือกงานในบทที่ 5 (Fig 5.10-5.11, RBMM p.126) เป็นเนื้อหาเดียวกับรูป 7.1-7.2 ของบทที่ 7 ใช้ต่อจาก [[FMECA]] ภายใน [[RCM Reliability Centered Maintenance]]

## 2. ผัง Nowlan & Heap (รูป 7.1, RBMM p.181)

แยก Evident กับ Hidden (non-evident) ก่อน แล้วแยก Evident เป็น Safety กับ Economic (Operational = ผลิตเสีย + ซ่อม, Non-Operational = ค่าซ่อมอย่างเดียว)

| กลุ่ม consequence | ตัวเลือกงาน |
|---|---|
| Evident Safety | Condition Monitoring, Restore/Overhaul, Discard/Replace, Combined, Redesign is Required |
| Evident Operational | Condition Monitoring, Restore/Overhaul, Discard/Replace, Run To Failure, Redesign may be desirable |
| Evident Non-Operational | เหมือน Operational |
| Hidden Failure | Condition Monitoring, Restore/Overhaul, Discard/Replace, Failure Finding, Redesign may be desirable |

## 3. SAE JA1011 / JA1012 (รูป 7.2, RBMM p.181)

- โครงสร้างคล้าย Nowlan & Heap แต่ขยาย Hidden Failure เป็น Safety และ Economic และให้น้ำหนัก Safety กับ Environment มากขึ้น
- ลำดับตัดสิน: Evident/Hidden, แล้ว Safety?, แล้ว Environment?, แล้ว Economic (Operational / Non-Operational)
- Safety และ Environment: Condition Monitoring, Restore/Discard, Combination Tasks, Redesign Compulsory (เพิ่ม Failure Finding เมื่อ Hidden; กรณี Hidden-Environment หนังสือระบุเพิ่ม Overhaul/Replace)
- Economic: Condition Monitoring, Restore/Discard, No Scheduled Maintenance, Redesign may be desirable (Hidden เพิ่ม Failure Finding และ Combination ในกรณี Operational)
- ข้อสังเกต: "Run to Failure" ของ Nowlan & Heap ถูกแทนด้วย "No Scheduled Maintenance" ใน JA1012
- หนังสือไม่ได้อ้างตัวมาตรฐานเกินรูปผัง รายละเอียดคำถาม 7 ข้อของ RCM ดู [[RCM Reliability Centered Maintenance]]

## 4. ลำดับคำถามแบบง่าย (รูป 7.3, RBMM p.182-183)

เรียงจากต้นทุนต่ำไปสูง ถามด้วยเกณฑ์ Applicable (ทำได้ทางเทคนิค) และ Feasible (คุ้มค่า)

```
1. Condition Monitoring/Inspection ทำได้และคุ้ม?   -> ใช่: Scheduled on-Condition Task (ถูกที่สุด)
2. Scheduled Replacement/Overhaul ทำได้และคุ้ม?    -> ใช่: Scheduled Discard or Restoration
3. เป็น Hidden Failure?                            -> ใช่: Failure Finding Task
4. ที่เหลือ: Redesign (บังคับถ้ากระทบ Safety/Environment รุนแรง,
             มีเงื่อนไขถ้าไม่กระทบ) หรือ Run to Failure
```

Run to Failure เลือกได้เมื่อไม่มีผลกระทบหรือไม่คุ้มทำอะไร (RBMM p.183)

## 5. เลือกตามสถิติ Weibull beta (RBMM p.183-189)

ต้องมีข้อมูลการเสียแยกราย failure mode ดู [[Weibull Analysis]] และ [[Failure Patterns and Bathtub Curve]]

| beta | ลักษณะ | ทางเลือกตามหนังสือ |
|---|---|---|
| น้อยกว่า 1 | Infant mortality (เสียผิดปกติหลัง maintenance ไม่นาน) | PM แก้ไม่ได้ ให้ทบทวนสาเหตุ: อะไหล่ไม่ได้มาตรฐาน, ฝีมือซ่อม, การใช้งานผิด; งาน PM เองอาจเป็นต้นเหตุ (p.184) |
| เท่ากับ 1 | เสียสุ่ม constant failure rate | Condition Monitoring; scheduled replace/overhaul ไม่เพิ่ม reliability (p.185-187) |
| ใกล้ 1 | ชิ้นไม่สำคัญมาก อัตราเสียเพิ่มช้า | Condition Monitoring เป็นหลัก ถ้าเข้าถึงและเปลี่ยนง่าย (p.187) |
| มากกว่า 1 มาก | wear-out เกาะกลุ่ม มีช่วงอายุ t1-t2 | Condition Monitoring, Part Replacement หรือ Overhaul (p.188) |

หมายเหตุ: ถ้ารวมหลาย failure mode แล้วนับรวม จะได้ beta ใกล้ 1 เสมอ จึงต้องแยก mode ก่อนเสมอ (RBMM p.185)

### พิสูจน์ว่า replace ตามแผนไม่ช่วยเมื่อ beta = 1 (RBMM p.186)

ตัวเลขตามหนังสือ (R(t) = exp(-t/eta); ค่า eta ไม่ได้ระบุชัดในหน้า อนุมานได้ราว 159-160 ชม. จึงเป็น derived)

| กรณี | ผล |
|---|---|
| ไม่ทำ replacement | R(120) = 47.0158%, R(80) = 60.4639%, Rc(120/80) = 0.470158/0.604639 = 77.758% |
| Replace ทุก 80 ชม. | R(80) x R(40) = 60.4639% x 77.7585% = 47.0158% |

ผลเท่ากัน เพราะ failure rate คงที่ ชิ้นใหม่ไม่ดีกว่าชิ้นเก่า

## 6. ตัวอย่าง: failure mode ที่ beta สูง (RBMM p.199)

TTF 4 ครั้ง (16,000, 12,000, 11,000, 8,500 ชม.) fit ได้ beta = 3.788 (หนังสือเขียน 3.788(8)) และ eta ราว 13,130 ชม. จัดเป็น pattern A (เกาะกลุ่ม) การสมมติ constant failure rate ผิดสำหรับกรณีนี้ จึงเลือก scheduled replacement หรือ Condition Monitoring และต้องหาคาบต่อ (ดู [[PM Interval Optimization]]) ข้อมูลเพียง 4 จุด หนังสืออธิบายว่ายังประมาณพารามิเตอร์ได้เพราะ failure mode เป็น "man-made pre-programmed failure" (p.194) ควรอ่านเป็นข้อสังเกตของผู้เขียน ไม่ใช่ข้อพิสูจน์ทางสถิติ

## 7. กฎปฏิบัติ

- เลือกงานราย failure mode และตาม consequence ก่อน แล้วค่อยใช้ beta ยืนยันว่า time-based task สมเหตุสมผล
- เริ่มจาก Dominant Failure Mode (ครอบคลุมราว 80% ของปัญหา/ต้นทุน, RBMM p.206)
- งานบน Hidden Failure ของ protective/standby ใช้ Failure Finding ไม่ใช่ replace ตามอายุ
- ถ้า failure mode เสียสุ่มและกระทบ Safety/Environment ต้อง redesign หรือ condition-based ไม่ใช่เพิ่มความถี่ PM

## เชื่อมโยงกับ compressor failure hierarchy

- หน่วยวิเคราะห์ตรงกับระดับ [[Failure Mode]] ของ [[ISO 14224]] / [[OREDA]] และต่อยอดเป็นคอลัมน์ "recommended task type" ต่อ [[Maintainable Item]] ของ [[Compressor]] ได้ (ข้อเสนอแนะ ไม่ใช่ข้อมูลใน sources)
- [[OREDA]] ใน wiki นี้มีแต่ % สัมพัทธ์ ไม่มี beta จึงบอกประเภทงานตาม beta ไม่ได้ ต้องใช้ข้อมูลประวัติ site-specific (หนังสือเน้นการใช้ข้อมูลของหน่วยงานเอง เช่น RBMM p.223, p.231)
- Failure mode ที่เกี่ยวกับ protective/instrument loop เช่น AIR (abnormal instrument reading) หรือ UST (spurious stop) อาจเข้ากับงาน Failure Finding ดู [[Failure Finding Interval]] (ข้อเสนอแนะ ไม่ใช่ข้อมูลใน sources)
- การรวมหลาย mode ทำให้ beta ใกล้ 1 จึงต้องลงรหัส failure mode และสาเหตุให้แยกชัดเจนใน CMMS ดู [[Failure Cause Codes]]

## ดูเพิ่ม

- [[PM Interval Optimization]]
- [[P-F Interval and Condition Monitoring]]
- [[Failure Finding Interval]]
- [[Redundancy and Standby Systems]]
- [[RCM Reliability Centered Maintenance]]
- [[Criticality Assessment]]

---
title: Failure Mechanism
created: 2026-10-20
updated: 2026-10-21
type: concept
tags: [failure-mechanism, taxonomy, oreda, coding]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__notes.csv, compressor-failure-hierarchy__failure-cause-code.csv, compressor-failure-hierarchy__resolution-matrix.csv, failure-structure.md, failure-structure__sheet2.csv, coce-failure-mechanism.jpg, reliability-based-maintenance-management.md]
confidence: high
contested: false
---

# Failure Mechanism

**Failure mechanism** คือกระบวนการทางกายภาพ/เคมี/ไฟฟ้าที่นำไปสู่ [[Failure Mode]] เป็นระดับที่ 5 ของ [[Failure Hierarchy]] รายชื่อมาจาก OREDA failure mechanism list (ภาพ `coce-failure-mechanism.jpg`) รวม **37 รายการ**

## กติกาใน dataset

- แต่ละ [[Maintainable Item]] เลือกเฉพาะ mechanism ที่เกี่ยวข้องทางกายภาพ (sheet "Mechanism Library") พร้อม detail เฉพาะ item (เช่น Valves x Wear = "valve plate/seat/spring wear")
- mechanism ปรากฏในแถว Failure Hierarchy ก็ต่อเมื่อสามารถทำให้เกิด failure mode นั้นกับ item นั้น
- failure mode `OTH` ใช้ mechanism `Other` และ `UNK` ใช้ `Unknown` กับทุก item (ดู [[OTH Other]])
- mechanism x [[Resolution Codes]] ที่เป็นไปได้ อยู่ใน [[Resolution Matrix by Mechanism]]
- รหัส 4 ตัวอักษรของ mechanism เป็นส่วนท้ายของ CAUSE_CODE ดู [[Failure Cause Codes]] และ [[CAUSE_CODE Convention]]

## ตาราง 37 mechanism

คอลัมน์ Category มาจาก `failure-structure__sheet2.csv` (มีเพียง 24 รายการ; "-" = ไม่มีใน sheet นั้น; "(blank)" = มีแต่ไม่ระบุ category) ค่าเขียนตามต้นฉบับ (`envir`, `electrical/constrol` ใน source สะกดว่า constrol)

| Mechanism | Code | Category (sheet2) | No. of resolutions (matrix) |
|---|---|---|---|
| Blockage/plugged | BLKG | physical | 6 |
| Breakage | BRKG | physical | 7 |
| Burst | BRST | electrical/constrol (ดูข้อสังเกต) | 6 |
| Cavitation | CAVT | - | 7 |
| Clearance/ alignment failure | ALGN | physical | 8 |
| Combined causes | (ไม่มีรหัส) | (blank) | 6 |
| Contamination | CTMN | envir | 5 |
| Control failure | CTRL | electrical/constrol | 6 |
| Corrosion | CORR | envir | 7 |
| Deformation | DEFM | physical | 6 |
| Earth/isolation fault | EART | - | 6 |
| Electrical failure - general | ELEC | - | 6 |
| Erosion | EROS | - | 6 |
| External influence - general | EXIN | - | 7 |
| Fatigue | FATG | - | 6 |
| Faulty power/voltage | FPWR | - | 5 |
| Faulty signal/indication/alarm | FSIG | electrical/constrol | 7 |
| Instrument failure - general | INST | electrical/constrol | 8 |
| Leakage | LEAK | physical | 10 |
| Looseness | LOOS | physical | 6 |
| Material failure - general | MATF | physical | 7 |
| Mechanical Failure - general | (ไม่มีรหัส) | physical | 7 |
| Misc. external influences | MEXT | - | 6 |
| Miscellaneous - general | MISC | - | 6 |
| No cause found | NCFD | (blank) | 3 |
| No power/ voltage | NPWR | electrical/constrol | 5 |
| No signal/indication/alarm | NSIG | electrical/constrol | 5 |
| Open circuit | OPEN | electrical/constrol | 5 |
| Other | OTHR | - | 5 |
| Out of adjustment | OADJ | (blank) | 4 |
| Overheating | OVHT | - | 9 |
| Short circuiting | SHRT | - | 5 |
| Software failure | SWFL | - | 5 |
| Sticking | STCK | physical | 8 |
| Unknown | UNKN | (blank) | 4 |
| Vibration | VIBR | physical | 9 |
| Wear | WEAR | physical | 9 |

รวมคู่ mechanism x resolution ที่เป็นไปได้ = 233 (ตรงกับ Notes: 233 of 37 x 13 pairs)

## ข้อสังเกตคุณภาพข้อมูล

- **Combined causes** และ **Mechanical Failure - general** อยู่ใน OREDA list และ Resolution Matrix แต่ **ไม่มีรหัสใน sheet "failure cause code"** (35 รหัส) และ **ไม่ปรากฏเลยใน sheet Failure Hierarchy** (ค้นแล้ว 0 แถว) ทั้งที่ภาพ OREDA แยกประเภท (เช่น reciprocating LOO: Mechanical Failure - general = 18.62) ใช้ descriptor นี้ นั่นคือ dataset ไม่ได้ map descriptor นี้ไปสู่ item-specific mechanism ดู [[Failure Cause Codes]]
- **Burst** ถูกจัดเป็น `electrical/constrol` ใน sheet2 ซึ่งผิดวิสัย (Burst ปกติเป็นกลไกทางกายภาพ เช่น piping/cooler) เป็นข้อสังเกตของ wiki นี้ ไม่มี source อื่นยืนยัน/ปฏิเสธ confidence ต่ำสำหรับข้อนี้
- Sheet2 มีเพียง 24 จาก 37 mechanism

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความจากหนังสือ ไม่ใช่ข้อมูล OREDA: RBMM Fig 5.13 (p.131) แสดงลำดับ causation 7 ระดับจนถึง design/assembly/procurement/storekeeping error ใช้เป็นแนวแยก mechanism กับ latent cause ได้ ดู [[Failure Data Recording]] และพฤติกรรมการเสียตามอายุ (wear-out vs random) ที่ [[Failure Patterns and Bathtub Curve]]

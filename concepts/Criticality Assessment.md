---
title: Criticality Assessment
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [criticality, rcm, spare-parts, maintenance-management, cost, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Criticality Assessment

**Criticality Assessment** คือการจัดระดับความวิกฤติของเครื่องจักรเป็น A/B/C (High/Moderate/Low) เพื่อเลือกกลยุทธ์ PM อะไหล่ และงบ ให้ต่างกันตามระดับ ภายใต้เป้า "Zero (Plant) Breakdown @ Minimum Cost" RBMM บท 5 วัด criticality ด้วย Consequence (1-5) x Likelihood (1-6) = Score 1-30 แยก 3 ด้าน: Commercial, Safety, Environment โดยอ้างแนว FMECA Mil-1629 ส่วนเกณฑ์ตัวเลขเป็นตัวอย่างที่ปรับเองได้ (RBMM p.116-117) confidence เป็น medium เพราะมีค่า derived ที่ผู้เขียน wiki คำนวณเพิ่ม (ระบุในหน้า) และบางตัวเลขในภาพเบลอ

## สูตรและการแบ่งระดับ (RBMM p.116-118)

```
Criticality Score = Consequence (1-5) x Likelihood (1-6)     ช่วง 1-30
Score 15-30  -> Criticality 1 = A (High)
Score  5-12  -> Criticality 2 = B (Moderate)
Score  1-4   -> Criticality 3 = C (Low)
```

หมายเหตุ (derived): ผลคูณของจำนวนเต็ม 1-5 กับ 1-6 ไม่มีทางได้ 13 และ 14 จึงไม่มีช่องว่างจริงระหว่างช่วง 5-12 กับ 15-30

Criticality Matrix (Fig 5.3, p.118): แกนตั้ง Likelihood 1 (Remote) - 6 (Very High) x แกนนอน Consequence 1 (Very Low) - 5 (Very High) ค่าเซลล์คือผลคูณ ตัวอย่างในหนังสือ: L6xC3 = 18 High; L4xC4 = 16 High; L3xC4 = 12 Moderate; L2xC5 = 10 Moderate; L1xC5 = 5 Moderate; L5xC5 = 25; L6xC5 = 30

## Commercial (Fig 5.2, RBMM p.117)

Consequence:

| Score | ระดับ | เกณฑ์ |
|---|---|---|
| 5 | สูงมาก | หยุดสายผลิต > 24 ชม. หรือ ค่าผลิต+ซ่อมสูญเสีย > 500,000 |
| 4 | สูง | หยุดสายผลิต > 12 และ < 24 ชม. หรือ > 100,000 และ < 500,000 |
| 3 | ปานกลาง | หยุดผลิตบางส่วน > 8 และ < 12 ชม. หรือ > 10,000 และ < 100,000 |
| 2 | ต่ำ | หยุดผลิตบางส่วน < 8 ชม. หรือ > 1,000 และ < 10,000 |
| 1 | ต่ำมาก | ไม่กระทบสายผลิต หรือ ค่าซ่อม < 1,000 |

หน่วยเงินไม่ระบุในภาพ [อ่านไม่ออกชัด]

Likelihood (ภาพเบลอ) ใช้อายุใช้งานได้ก่อนเสีย:

| Score | ระดับ | อายุก่อนเสีย |
|---|---|---|
| 6 | สูงมาก | ไม่เกิน 3 เดือน |
| 5 | สูง | > 3 เดือน ถึง 1 ปี |
| 4 | ปานกลาง | > 1 ถึง 3 ปี |
| 3 | ต่ำ | > 3 ถึง 5 ปี |
| 2 | ต่ำมาก | > 5 ถึง 10 ปี |
| 1 | น้อยมาก | > 10 ปี |

## Safety (Fig 5.4, RBMM p.118)

| Score | Consequence | Score | Likelihood |
|---|---|---|---|
| 5 | สูญเสียชีวิต อวัยวะ พิการ | 6 | อย่างน้อย 1 ครั้ง/ปี |
| 4 | บันทึกเป็นการสูญเสียเวลา (lost-time) | 5 | มากกว่า 1 ครั้งใน 5 ปี |
| 3 | บันทึกเป็นอุบัติเหตุได้ (recordable) | 4 | N.A. |
| 2 | บาดเจ็บ ต้องปฐมพยาบาล | 3 | ครั้งเดียวใน 5 ปี |
| 1 | ไม่กระทบความปลอดภัย | 2 | N.A. |
| | | 1 | ไม่เคยมีรายงาน |

## Environment (Fig 5.5, RBMM p.119)

Consequence: 5 สารพิษอาจเกิน 500 หน่วยวัด หรือกระทบโรงงานอื่น/ผิดข้อบังคับ; 4 อาจเกิน 200 หน่วย ต้องขอความช่วยเหลือภายนอก; 3 อาจเกิน 20 หน่วย แต่หน่วยงานภายในรับมือได้; 2 สารพิษเล็กน้อย ไม่ต้องรายงาน; 1 ไม่มีผล Likelihood ใช้สเกล 1-6 เดียวกับ Safety

Fig 5.6 (p.120): ตารางสรุป 3 คอลัมน์ (Commercial, Safety, Environment แต่ละอัน 1-3) ต่อ Equipment เพื่อ sort ตามประเด็น

## กลยุทธ์ตามระดับ (Fig 1.5 RBMM p.26; Fig 10.32 p.316)

| ระดับ | แนวทาง | Scheduled PM | Spare Parts |
|---|---|---|---|
| A High | 100% RCM Tasks (Zero Breakdown) | 100% RCM tasks, ตัด unreliable incidence, intensive failure finding, ยอมรับ multiple failure probability ได้ | 100% service level, 0% stock out |
| B Medium | Pro-active | ตัด PM ที่ไม่ได้ผล, PM optimum | ลดสต๊อก, ดู % service level / stock out |
| C Low | Re-active | ตัด PM ไม่จำเป็น, PM optimum, RTF | ลดสต๊อก, ดู % service level / stock out |

ตัวเลขเพิ่มเติม (RBMM บท 10 p.315-319): A คำนวณงบ CM-Unplanned ด้วย Confidence Level > 95% ว่าจะไม่เกิดเลย; B Confidence 90% ระดับอะไหล่ปานกลาง Service Factor 100%; C Confidence 80-90% ปล่อย RTF ดู [[Maintenance Budget]] (คำว่า "ROM" ใน Fig 10.32 น่าจะหมายถึง RCM อ่านจากภาพ)

## Dynamic of Criticality (RBMM p.23-25)

- Criticality เปลี่ยนตามเวลา ขึ้นกับ Stress, Resistance และแผนบำรุงรักษา
- Fig 1.4: สัดส่วนเครื่อง A/B/C = 30% / 50% / 20% (ตัวอย่างสมมติของหนังสือ ไม่ใช่ค่ามาตรฐาน) สถานะ 1 Beginning (เสียทุกระดับ รวม A) -> 2 Intermediate (เสียที่ B/C) -> 3 Target (เสียที่ C/B ที่ไม่ทำให้โรงงานหยุด = Zero Plant Down Time)

## Boundary, Redundancy และ Process (RBMM p.28-30)

- ไม่มี redundancy: เครื่องอนุกรมทุกตัวเป็น A (Fig 1.6); มี redundancy: กลุ่มขนานอาจเป็น A/B/C (Fig 1.7)
- ตัวอย่าง 3 เครื่องรับภาระได้ 50% ต่อเครื่อง: Standby (ใช้ 2 สำรอง 1) vs Load Sharing (แต่ละเครื่อง 1/3 พร้อมรับเพิ่มถึง 50%)
- ระดับไม่ลดเป็นต่ำกว่า A อัตโนมัติ: เครื่อง Standby อาจเสียแบบ Hidden แล้วเกิด Multiple Failure
- ถังเก็บระหว่าง process ลด criticality ภาพรวม (Fig 1.8)
- ตั้งงบเป็นกรอบ process จัดลำดับในแต่ละกรอบแล้วรวม ดู [[Redundancy and Standby Systems]] และ [[Reliability Block Diagram]]

## Part Criticality สำหรับอะไหล่ (RBMM p.243-246)

- Equipment Criticality = Commercial + Safety + Environment; Part Criticality = Price, Lead Time, Failure Detect-ability (CBM) (Fig 9.5) ให้คะแนน Cost/LT/CBM 1 = สูงสุด 2 = กลาง 3 = ต่ำ (CBM ต่ำ = ตรวจอาการล่วงหน้าไม่ได้)
- กฎ: อะไหล่ใช้ร่วมเครื่องต่างระดับ -> criticality อะไหล่ = ระดับสูงสุดของเครื่องที่ใช้
- Fig 9.6 ตารางนับจำนวนชิ้นในเครื่อง A/B/C จาก BOM [ตัวเลขรายแถวอ่านไม่ออก]
- ดู [[Spare Part Criticality and Risk]] และ [[Spare Parts Management]]

## ใช้ใน RCM

กระบวนการ 2 ของ [[RCM Reliability Centered Maintenance]]: เลือกเครื่องจักร/กรอบตาม criticality ก่อน แล้วค่อยลง Function และ FM Fast Track RCM ถือว่า criticality ของ equipment อยู่นอกกระบวนการ ผู้ใช้เลือกกรอบเอง (RBMM p.150) ระดับ equipment ละเอียดขึ้นด้วย [[FMECA]]

## ข้อควรระวัง

- ฟิลด์ Criticality ใน Equipment Database เชื่อมกับ Maintenance Strategy (Fig 4.3, RBMM p.96) ดู [[CMMS]]
- Likelihood ของ Commercial อิงอายุก่อนเสีย ต้องมีประวัติ ถ้าไม่มี (โรงงานใหม่) ใช้ความรู้ผู้ออกแบบ/ผู้ผลิต หรือ FMECA (RBMM p.137)
- คะแนน Safety/Environment ควรแยกพิจารณา ไม่ถูกกลบด้วย Commercial: ตัวอย่างหนังสือแสดงตารางแยกคอลัมน์ (Fig 5.6) แต่ไม่ระบุกฎรวมคะแนน (ไม่มีใน sources)

## เชื่อมโยงกับ compressor failure hierarchy

- Criticality ให้กับระดับ [[Compressor]] (equipment) ตาม consequence ต่อ production/safety/environment ส่วน Likelihood ประมาณจากประวัติเสีย; wiki ไม่มีข้อมูลเสียของ asset Valeura (นอกขอบเขตตาม SCHEMA) จึงยังไม่มีการจัดระดับจริง
- ในระดับ sub unit/[[Maintainable Item]] ใช้ [[Failure Mode]] ที่มี consequence สูง เช่น ELP (รั่ว process medium ที่อาจกระทบ Safety/Environment ดู [[ELP External Leakage Process Medium]]) เทียบกับ ELU ([[ELU External Leakage Utility Medium]]) เป็นการตีความ ไม่ใช่ข้อมูลในหนังสือ
- อะไหล่ของ compressor ที่ lead time ยาว/ราคาสูง/ตรวจล่วงหน้าไม่ได้ ได้ Part Criticality สูงตาม Fig 9.5

## ดูเพิ่ม

- [[RCM Reliability Centered Maintenance]]
- [[FMECA]]
- [[Spare Part Criticality and Risk]]
- [[Maintenance Budget]]
- [[Asset Life Cycle]]

---
title: PM Task Selection
created: 2026-10-20
updated: 2026-10-25
type: concept
tags: [pm, rcm, reliability, weibull, maintenance-management, book, cbm, cmrp]
sources: [reliability-based-maintenance-management.md, cmrp.md]
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

## 8. มุมมอง CMRP: 5 กลยุทธ์และ decision tree (เพิ่ม 2026-10-25)

สไลด์ [[CMRP Course]] ใช้ชุดกลยุทธ์ 5 แบบที่เทียบได้กับงาน 5 ประเภทของ Nowlan & Heap ในหัวข้อ 1 (CMRP CMPR-03 p.7):

| CMRP | ความหมาย | เทียบ Nowlan & Heap (RBMM p.180) |
|---|---|---|
| RtF (Run to Failure) | ซ่อมหลังเสีย | Run to Failure |
| FFM (Failure Finding Maintenance) | functional test หา hidden failure ไม่ได้ป้องกันการเสีย | Scheduled Failure Finding |
| SM (Scheduled Maintenance) | ทำตามเวลา/ชั่วโมงเดิน ไม่สนสภาพ | Scheduled Overhaul or Discard |
| CBM (Condition Based Maintenance) | วัดสภาพแล้วตัดสินว่าทำเมื่อไร | Condition Monitoring |
| MOD (Modification) | ไม่ใช่ maintenance ต้องเปลี่ยนแปลง (ไม่จำเป็นต้องเป็นเรื่องเทคนิค) | Redesign |

4 คำถามเลือกกลยุทธ์ (CMRP CMPR-03 p.4): failure ซ่อน (hidden) หรือไม่, วิกฤติ (critical) หรือไม่, มี condition indicator ใช้ได้ไหม, คาบการเสียรู้และคงที่ไหม; นิยาม hidden ผูกกับ hidden function เช่นอุปกรณ์ป้องกัน ไม่ได้ขึ้นกับว่ากลไกการเสื่อมมองเห็นยาก (p.5)

Decision tree (CMRP CMPR-03 p.7, ถอดจากภาพ):

```
Hidden failure?  Yes -> CBM ได้? Yes = CBM / No = FFM
                 No  -> Critical? No = RtF
                        Yes -> FAR (Failure Related Ageing)? No = MOD
                               Yes -> CBM ได้? Yes = CBM
                                      No -> CFI (Constant Failure Interval)? Yes = SM / No = SM (ผังผิด)
```

ข้อสังเกตและข้อผิดพลาด:
- **ผังผิด**: กิ่ง CFI = No ในภาพลากไป "SM" เช่นกัน (มีกล่อง SM สองกล่อง) ทำให้คำถาม CFI ไม่มีผล ตามตรรกะกิ่งนี้ควรไป MOD หรือทบทวนใหม่ เพราะ SM ใช้ได้เมื่อคาบการเสียคงที่เท่านั้น (raw notes CMPR-03 หัวข้อ 3)
- ไม่มี economic test: ผัง CMRP ให้ RtF เมื่อไม่ critical ทันที ขณะที่ Nowlan & Heap / RBMM ถาม applicable และ feasible (หัวข้อ 4) จึงอาจเลือก CBM ให้ failure ที่ไม่ critical แต่คุ้มทำได้ ไม่ได้ขัดกันตรง ๆ แต่เกณฑ์ต่าง
- กิ่ง FAR = No -> MOD ข้ามการถาม CBM สำหรับ failure แบบ random บนเครื่อง critical ขัดกับผัง RCM ของสไลด์เอง (p.2) ที่ให้ CBM กับ random pattern และกับ RBMM ที่ให้ condition monitoring เมื่อ beta = 1 (หัวข้อ 5) (ข้อสังเกตของ wiki derived จากการเทียบผัง)
- ผัง RCM 4 กลุ่มของสไลด์ (p.2): Reactive (ชิ้นเล็ก ไม่วิกฤติ มี redundancy), Interval/PM (wear-out, consumable, รู้ pattern), CBM (random, ไม่ wear, failure ที่ PM ก่อ), Proactive (RCFA ดู [[Root Cause Analysis]], age exploration, FMEA, acceptance testing)
- สไลด์อ้างว่าราว 60% ของอุปกรณ์มีแค่ช่วง infant และ random ของ bathtub ไม่ระบุแหล่ง (CMRP CMPR-03 p.5) ดู [[Failure Patterns and Bathtub Curve]]

คาบงานตาม criticality (CMRP CMPR-03 p.9-12): ผังไม่ได้ให้คาบ ต้องดู criticality, MTBF, redundancy, failure characteristics, กฎหมาย สไลด์ให้สูตร FFM T = MTTF x 2 x (1 - A) หรือ x 3 x (1 - A), CBM T = PF หรือ 0.75 PF, SM T = TTF หรือ 0.75 TTF (moderate / high) สูตร FFM ขัดกับสูตรมาตรฐาน ดู [[Failure Finding Interval]] (contested) และคาบ CBM ยาวกว่า P-F/2 ของ RBMM ดู [[P-F Interval and Condition Monitoring]]; กรณี moderate ที่ตั้ง SM = TTF เต็มค่า (ไม่มี safety margin) ขัดกับภาพของสไลด์เองที่ว่า SM ต้องมี margin (p.10) ส่วนกรณี high ใช้ 0.75 TTF ซึ่งมี margin 25% (ตรวจกับภาพ CMPR-03 p.12 แล้ว 2026-10-25)

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
- [[Root Cause Analysis]]

## Triplets

- [[PM Task Selection]] [applies_to:: [[Failure Mode]]] select per failure mode, not per equipment (RBMM ch7)
- [[PM Task Selection]] [selects:: Condition Monitoring] task type 1, on-condition (Nowlan and Heap, RBMM p.180)
- [[PM Task Selection]] [selects:: Scheduled Overhaul or Discard] task type 2, restoration/discard (RBMM p.180)
- [[PM Task Selection]] [selects:: Scheduled Failure Finding] task type 3 (RBMM p.180)
- [[PM Task Selection]] [selects:: Run to Failure] task type 4 (RBMM p.180)
- [[PM Task Selection]] [selects:: Redesign] task type 5 (RBMM p.180)
- [[PM Task Selection]] [step_of:: [[RCM Reliability Centered Maintenance]]] decision chart Fig 5.10-5.11 = Fig 7.1-7.2 (RBMM p.126)
- [[FMECA]] [input_to:: [[PM Task Selection]]] task selection follows FMECA (RBMM p.126)
- Nowlan and Heap Decision Chart [uses:: Evident Failure] split Evident vs Hidden first, then Safety vs Economic (Fig 7.1, RBMM p.181)
- Redesign [applies_to:: Evident Safety Consequence] Redesign is Required (Fig 7.1)
- Combination of Tasks [applies_to:: Evident Safety Consequence] (Fig 7.1)
- Run to Failure [applies_to:: Evident Operational Consequence] also Evident Non-Operational; Redesign may be desirable (Fig 7.1)
- Scheduled Failure Finding [applies_to:: Hidden Failure] (Fig 7.1)
- Condition Monitoring [applies_to:: Hidden Failure] also Restore/Overhaul, Discard/Replace; option in all groups (Fig 7.1)
- SAE JA1012 Decision Chart [differs_from:: Nowlan and Heap Decision Chart] splits Hidden into Safety and Economic, more weight on Safety and Environment (Fig 7.2, RBMM p.181)
- SAE JA1012 Decision Chart [defined_in:: SAE JA1012] also SAE JA1011
- Redesign [applies_to:: Environment Consequence] Redesign Compulsory with Safety (SAE JA1012, Fig 7.2)
- No Scheduled Maintenance [alias_of:: Run to Failure] JA1012 replaces Nowlan and Heap Run to Failure (Fig 7.2)
- [[PM Task Selection]] [uses:: Applicable and Feasible Criteria] technically possible and worth doing (Fig 7.3, RBMM p.182-183)
- Task Question 1 [step_of:: [[PM Task Selection]]] Condition Monitoring/Inspection applicable and feasible? yes = Scheduled on-Condition Task, cheapest (Fig 7.3)
- Task Question 2 [step_of:: [[PM Task Selection]]] Scheduled Replacement/Overhaul applicable and feasible? yes = Scheduled Discard or Restoration (Fig 7.3)
- Task Question 3 [step_of:: [[PM Task Selection]]] Hidden Failure? yes = Failure Finding Task (Fig 7.3)
- Task Question 4 [step_of:: [[PM Task Selection]]] remaining: Redesign (compulsory if severe Safety/Environment) or Run to Failure (Fig 7.3)
- Run to Failure [applies_to:: No Consequence] or nothing worth doing (RBMM p.183)
- Shape Parameter Beta [input_to:: [[PM Task Selection]]] needs failure data per failure mode (RBMM p.183-189)
- Infant Mortality [depends_on:: Shape Parameter Beta] beta < 1: PM cannot fix; review parts quality, workmanship, misuse; PM may be the cause (RBMM p.184)
- Random Failure [depends_on:: Shape Parameter Beta] beta = 1, constant failure rate (RBMM p.185-187)
- Condition Monitoring [applies_to:: Random Failure] beta = 1; scheduled replace/overhaul adds no reliability (RBMM p.185-187)
- Condition Monitoring [applies_to:: Shape Parameter Beta Near 1] minor part, slowly rising rate, if easy to access and replace (RBMM p.187)
- Wear-Out Failure [depends_on:: Shape Parameter Beta] beta much greater than 1, clustered life t1-t2 (RBMM p.188)
- Scheduled Overhaul or Discard [applies_to:: Wear-Out Failure] also Condition Monitoring or Part Replacement (RBMM p.188)
- Shape Parameter Beta [has_value:: near 1] when several failure modes are pooled; separate modes first (RBMM p.185)
- Scheduled Replacement [has_value:: 47.0158%] R(80) x R(40) with replace every 80 h equals R(120) without replacement at beta = 1 (RBMM p.186)
- Conditional Reliability [has_value:: 77.758%] Rc(120/80) = 0.470158/0.604639 (RBMM p.186)
- Weibull Eta [has_value:: about 159-160 h] inferred for beta = 1 proof, derived [confidence:: low]
- High Beta Example [has_value:: 3.788] beta, eta about 13,130 h, TTF 16,000/12,000/11,000/8,500 h, pattern A (RBMM p.199)
- High Beta Example [selects:: Scheduled Overhaul or Discard] scheduled replacement or Condition Monitoring; constant rate assumption wrong (RBMM p.199)
- [[PM Task Selection]] [applies_to:: Dominant Failure Mode] start here, about 80% of problems/cost (RBMM p.206)
- Scheduled Failure Finding [applies_to:: Protective Device] hidden failure of protective/standby, not age-based replacement
- Redesign [applies_to:: Random Failure] with Safety/Environment impact: redesign or condition-based, not more frequent PM
- [[PM Task Selection]] [depends_on:: Site-Specific History] OREDA has only relative %, no beta (RBMM p.223, p.231)
- [[PM Task Selection]] [uses:: [[Failure Cause Codes]]] separate mode and cause coding in CMMS, since pooling gives beta near 1
- Scheduled Failure Finding [applies_to:: [[AIR Abnormal Instrument Reading]]] protective/instrument loop, suggestion not in sources [confidence:: low]
- Scheduled Failure Finding [applies_to:: [[UST Spurious Stop]]] suggestion not in sources [confidence:: low]
- CMRP Strategy Tree [selects:: Run to Failure] RtF when not hidden and not critical (CMRP CMPR-03 p.7)
- CMRP Strategy Tree [selects:: Scheduled Failure Finding] FFM when hidden and CBM not possible (CMRP CMPR-03 p.7)
- CMRP Strategy Tree [selects:: Condition Monitoring] CBM when hidden or critical with ageing and condition indicator (CMRP CMPR-03 p.7)
- CMRP Strategy Tree [selects:: Scheduled Overhaul or Discard] SM when critical, ageing, no CBM (CMRP CMPR-03 p.7)
- CMRP Strategy Tree [selects:: Redesign] MOD when critical and no failure related ageing (CMRP CMPR-03 p.7)
- RtF [alias_of:: Run to Failure] CMRP term (CMRP CMPR-03 p.7)
- FFM [alias_of:: Scheduled Failure Finding] CMRP term (CMRP CMPR-03 p.7)
- SM [alias_of:: Scheduled Overhaul or Discard] CMRP Scheduled Maintenance, time/runtime based (CMRP CMPR-03 p.7)
- MOD [alias_of:: Redesign] CMRP Modification, not necessarily technical (CMRP CMPR-03 p.7)
- CMRP Strategy Tree [uses:: Hidden Failure] question 1 (CMRP CMPR-03 p.4, p.7)
- CMRP Strategy Tree [uses:: Criticality] question 2 (CMRP CMPR-03 p.4, p.7)
- CMRP Strategy Tree [uses:: Failure Related Ageing] FAR question (CMRP CMPR-03 p.7)
- CMRP Strategy Tree [uses:: Constant Failure Interval] CFI question; both branches go to SM in slide, chart error (CMRP CMPR-03 p.7)
- CMRP Strategy Tree [differs_from:: Nowlan and Heap Decision Chart] no applicable/feasible economic test; RtF whenever not critical
- CMRP Strategy Tree [defined_in:: [[CMRP Course]]] (CMRP CMPR-03 p.7)
- Proactive Maintenance [uses:: [[Root Cause Analysis]]] RCFA, age exploration, FMEA, acceptance testing (CMRP CMPR-03 p.2)
- CMRP Interval Rules [depends_on:: Criticality] moderate vs high, see Failure Finding Interval and P-F pages (CMRP CMPR-03 p.12)

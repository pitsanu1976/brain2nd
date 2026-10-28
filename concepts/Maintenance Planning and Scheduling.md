---
title: Maintenance Planning and Scheduling
created: 2026-10-25
updated: 2026-10-28
type: concept
tags: [work-management, maintenance-management, cmms, spare-parts, kpi, cmrp, mpm, work-order]
sources: [cmrp.md, reliability-based-maintenance-management.md, maintenance-profit-maker.md]
confidence: medium
contested: false
---

# Maintenance Planning and Scheduling

การวางแผน (planning) และจัดตาราง (scheduling) งานบำรุงรักษาตามหลักสูตร [[CMRP Course]] (เนื้อหาหลักจาก CMPR-09 และ CMPR-08 p.46-50) เป็นแกนของชั้น Work Control ใน [[Maintenance Efficacy Pyramid]] และทำงานบน work order workflow ของ [[CMMS]] ตัวชี้วัด backlog และ schedule compliance แยกไว้ที่ [[Maintenance Backlog and Schedule Compliance]] ส่วนงานหยุดใหญ่อยู่ที่ [[Turnaround Management]]

CMRP เป็นสื่อการสอน (secondary source) เนื้อหาด้านล่างถอดความด้วยถ้อยคำของ wiki ไม่ใช่ข้อความสไลด์

## 1. Planning ต่างจาก Scheduling อย่างไร

| | Planning | Scheduling |
|---|---|---|
| คำถาม | ทำงานนี้ **อย่างไร** (วิธี ทรัพยากร คน อะไหล่ เครื่องมือ) | ทำ **เมื่อไร** และ **ใคร** ทำ |
| ผลลัพธ์ | job plan / work package ต่อ WO | weekly schedule และ daily schedule |
| อ้างอิง | (CMRP CMPR-09 p.2) | (CMRP CMPR-09 p.34-35) |

- เป้าหมายพื้นฐานของ planning คือเพิ่มเวลาที่ช่างได้ลงมือทำงานจริง โดยไม่ต้องรอวัสดุ อุปกรณ์ หรือการปล่อยเครื่อง (CMRP CMPR-09 p.11)
- วงจรงานบำรุงรักษา: strategy -> planning -> scheduling -> execution -> work history -> analysis -> continuous improvement (CMRP CMPR-08 p.46)
- ระดับการวางแผน 3 ระดับ: long range 3-5 ปี (กำลังคน โครงการระยะยาว), budget 1-3 ปี (แปลงเป้าเป็นเงิน รวม turnaround), work order planning รายวัน (CMRP CMPR-09 p.12-14) ช่วง 3-5 กับ 1-3 ปีซ้อนกันที่ปี 3 ไม่ใช่ข้อผิดพลาดสำคัญ
- องค์ประกอบ 6 อย่างที่ต้องพร้อมก่อนงานจะสำเร็จ: วัสดุ/อะไหล่, ข้อมูล/แบบ, แรงงาน, เครื่องมือ, การอนุมัติ/permit, custody ของ asset (CMRP CMPR-09 p.34)

## 2. Work order flow

- 7 ขั้นหลัก: (1) work request (2) WO จาก CMMS เช่น PM, PdM, inspection ตามกฎหมาย (3) planning (4) scheduling (5) execution (6) ปิดงาน (7) feedback (CMRP CMPR-09 p.6-7)
- ก่อนปิด ต้องตรวจว่างานครบ แล้วส่งกลับผู้แจ้ง ถ้าผู้แจ้งไม่เห็นด้วยให้วนกลับ (CMRP CMPR-09 p.5) สอดคล้องกับ workflow และขั้นอนุมัติปิดงานของ RBMM ที่ [[CMMS]] (RBMM p.103-106) แต่จำนวนจุดอนุมัติต่างกัน ดูหัวข้อ CMRP ใน [[CMMS]]
- Planner ดึงข้อมูลจาก backlog, follow-up, shutdown work list, standard work database และ WO history (CMRP CMPR-09 p.7)

## 3. Planner: บทบาทและ span of control

- Span of control (ตัวอย่าง ต่อช่าง): Supervisor 1:10-15, Planner 1:20-30, Maintenance Engineer 1:40-50 สัดส่วนจริงขึ้นกับความซับซ้อนของงาน ระดับการวางแผน วิธีประมาณการ และวัฒนธรรมองค์กร (CMRP CMPR-09 p.8)
- หน้าที่: เตรียม work package, ทำ weekly/daily schedule, ดูแลข้อมูล CMMS, รวบรวมวัสดุ, บริหาร backlog, scope งานที่ไม่ใช่ emergency (CMRP CMPR-09 p.8) หลัก "right" 6 ข้อ: คน วัสดุ เครื่องมือ ข้อมูล จังหวะเวลา การอนุมัติ (p.9)
- Planner ควรเป็น "super-user" ของ CMMS ดูแล configuration และคุณภาพข้อมูล (CMRP CMPR-09 p.10-11)
- **Field time**: ราว 25% ของเวลา planner ควรอยู่หน้างานเพื่อ scope งาน (CMRP CMPR-09 p.10)
- ในองค์กรแบบ reactive บทบาท planner หดเหลือประสานงานและเก็บบทเรียน (CMRP CMPR-09 p.9)

## 4. กระบวนการวางแผน 7 ขั้น (CMRP CMPR-09 p.14-33)

| ขั้น | สาระ | หน้า |
|---|---|---|
| 1 Work screening | ไม่ซ้ำ คำอธิบายชัด ฟิลด์ครบ priority สมเหตุผล ได้อนุมัติ งานจำเป็นจริง | p.15 |
| 2 Assessing & scoping | ไปหน้างานเสมอ คุยผู้แจ้ง ระบุ job content และ job scope ถ่ายรูป ตรวจว่าต้องหยุดเครื่องไหม ประสาน safety (clearance, lockout, permit) | p.18-19 |
| 3 Job research | ดูประวัติอุปกรณ์ procedure ความต้องการ hot work, นั่งร้าน, confined space | p.20 |
| 4 Job breakdown | แตกขั้นเรียงลำดับ ระบุทักษะ ขนาดทีม ชั่วโมง เครื่องมือพิเศษ ต้นทุน และเร่งอนุมัติตามวงเงิน | p.20-21 |
| 5 Material take-off | ทำ BOM ตรวจคลังแล้ว **จอง (reserve)** และออก requisition | p.30-31 |
| 6 Assemble work package | รวม WO, job plan รายขั้น, ชั่วโมงต่อขั้น, BOM และที่ stage, permit, แบบ/spec | p.32 |
| 7 Feedback | แบบสอบถามหลังงาน เช่น ประมาณการอยู่ใน ±15% ไหม ต้องเดินกลับไปเอาของไหม | p.33 |

- Job plan ใน CMMS ประกอบด้วย work plan, labor, materials, tools และ safety plan (hazards, LOTO) (CMRP CMPR-09 p.21)
- Standard job plans 3 แบบ: preventive (PM master เป็น template), repetitive (bad actor, งานหลัง RCFA ดู [[Root Cause Analysis]]), safety plans (CMRP CMPR-09 p.22-24)

### Staging (CMRP CMPR-09 p.4, p.31)

- Staging = ย้ายวัสดุ เครื่องมือ ไปไว้ใกล้หน้างานล่วงหน้า ติดป้ายชัด ให้ช่างเริ่มได้ทันที
- ควร stage: ของซื้อตรง/non-stock, ของที่สต็อกต่ำหรือ CMMS แสดงว่าหมด, ของหมุนเร็ว; ไม่ควร stage: ของเฉพาะเครื่องเดียว, ของใหญ่ย้ายยาก, consumable ทั่วไปใน workshop
- การจองของคลังให้งานตามแผนต่างจากกฎของ RBMM ที่ให้ของคลังไว้สำหรับงานนอกแผน ดู [[Spare Parts Management]]

## 5. การประมาณการ (Estimating)

- วิธี 4 แบบ: historical records, engineered time standards, benchmarking, แตกงานย่อยแล้วใช้ experienced judgment (CMRP CMPR-09 p.25)
- เวลางานต้องรวมกิจกรรมก่อน (อ่าน WO, เบิกของ, เดินทาง, lockout) และหลัง (test run, เก็บกวาด, ลงเอกสาร) (CMRP CMPR-09 p.26)
- ใช้เวลาจริงต่อขั้น ไม่ปัดเป็น 4 หรือ 8 ชม. หรือครึ่งกะ และไม่ประมาณเกิน (CMRP CMPR-09 p.27); งานซ้ำให้จับเวลาหลายรอบแล้วเก็บเป็น standard plan (p.28)
- **Reasonable expectancy** (slide อ้าง IDCON): เวลาที่ช่างมีทักษะและแรงจูงใจใช้ทำงานให้ได้คุณภาพภายใต้สภาพเหมาะสม (CMRP CMPR-09 p.28)
- **ความแม่นยำ**: ไม่ต้องแม่นสัมบูรณ์ ความสม่ำเสมอ (consistency) สำคัญกว่าเพื่อการควบคุม (p.29); เกณฑ์ feedback คือ ±15% (p.33); ปัจจัยกระทบ: ขาดช่างเฉพาะทาง, สภาพอากาศ, พื้นที่แคบ/ที่สูง (p.29) ตัวชี้วัด Planning Accuracy อยู่ที่ [[Maintenance Backlog and Schedule Compliance]]

## 6. Prioritization PR1-PR4

Priority ต้องมาจากเป้าธุรกิจ ตกลงร่วมกันระหว่าง Operations กับ Maintenance แต่ละระดับมีกรอบเวลาเสร็จ (CMRP CMPR-09 p.15)

| ระดับ | ความหมาย | กรอบเวลา |
|---|---|---|
| PR1 Emergency | การผลิตหยุดหรือคนตกอยู่ในอันตราย OT อนุมัติอัตโนมัติ | เริ่มทันที |
| PR2 Urgent | ต้องทำเร็ว | เริ่มภายในไม่กี่ชั่วโมง |
| PR3 Routine | ลงตารางตามปกติ | ตามความสะดวกภายในเกณฑ์ |
| PR4 No action | ให้ Operations ตัดสินว่าจะทำไหม | ไม่กำหนด |

(CMRP CMPR-09 p.16)

Decision flow (อ่านจากภาพสแกน p.16 เส้นบางเส้นไม่ชัด ถือเป็นการตีความ):

```
Safety hazard ทันที?        คุมไม่ได้ -> PR1 | คุมได้ -> PR2
Safety improvement           -> PR3
Environmental impact ทันที?  คุมไม่ได้/ต้องเก็บกวาดทันที -> PR1 | มิฉะนั้น -> PR2
Environmental improvement    -> PR3
Production loss              มาก -> PR1 | ปานกลาง -> PR2 | บ้าง -> PR3 | ไม่มี -> PR4
```

- **Urgency trap**: งานด่วนไม่จำเป็นต้องสำคัญที่สุด ความด่วนบิดเบือน priority และกินทรัพยากรโดยไม่เกี่ยวกับเป้าบริษัท (CMRP CMPR-09 p.17)
- ถ้าแต่ละแผนกตั้ง priority เอง: งานวิกฤตจมใน backlog เสียชั่วโมงกับงานไม่สำคัญ และหมดความเชื่อถือ (CMRP CMPR-09 p.17)
- **ข้อสังเกต: PM ไม่อยู่ใน flow chart** p.16 ไม่มีกิ่งของ PM เลย ขณะที่ p.39 บอกว่า PM อาจถือว่า priority สูงสุด และ p.40 ให้ใส่ PM ลงตารางก่อนเสมอ การตีความที่สอดคล้อง: PM/PdM อยู่นอกระบบ PR1-PR4 และได้ที่ในตารางก่อนงานอื่น (การตีความของ wiki)
- การให้ priority สัมพันธ์กับความวิกฤตของอุปกรณ์ ดู [[Criticality Assessment]] (slide ไม่ได้ผูกกับ criticality ranking โดยตรง)

## 7. หลักการจัดตาราง

### Weekly schedule (CMRP CMPR-09 p.34-41)

- จับคู่ความต้องการงานกับทรัพยากรที่มีจริง หักวันลา อบรม ประชุม
- ประชุมประสานรายสัปดาห์สรุปตารางตาม priority และชั่วโมง (ยังไม่ระบุวัน/ตัวคน)
- **PM ใส่ก่อนเสมอ** แล้วจึงงานที่วางแผนแล้วตาม priority (p.39-40)
- ลงงานให้เต็ม 8 ชม./คน/วัน ใส่งาน priority ต่ำไว้เพื่อความยืดหยุ่น
- **อายุ WO ไม่มีสิทธิ์เหนือ priority**
- **ห้ามลงตารางงานที่ของยังไม่ครบ** และลงเฉพาะงานที่วางแผนแล้ว
- Flow: จัด priority -> ตรวจคน/อุปกรณ์/วัสดุ -> รวมงานหลายทักษะหรือหลายงานบนเครื่องเดียว -> ตั้งตาราง -> พิจารณา OT -> อนุมัติ/แจก -> ติดตาม schedule adherence (p.36)

**ข้อขัดกันใน slide p.40 (emergency time)**: slide เดียวกันบอกทั้ง "ไม่กันเวลาไว้สำหรับ emergency" และ "ต้องยืดหยุ่นพอให้มีเวลาสำหรับ emergency" การตีความที่สอดคล้อง: ลงตารางเต็ม 100% แต่ใส่งาน priority ต่ำที่ถูกเบียดออกได้ แทนการกันชั่วโมงว่าง (การตีความของ wiki ไม่ใช่ข้อความสไลด์)

### Gantt bar chart

- แสดงลำดับเวลาและงานที่ทำพร้อมกัน เหมาะกับ weekly schedule แต่ **ไม่แสดงความสัมพันธ์ (dependency) ระหว่างงาน** (CMRP CMPR-09 p.41) (ความรู้ทั่วไป: งานที่ dependency สำคัญ เช่น turnaround ใช้ network/CPM แทน)

### Daily schedule (CMRP CMPR-09 p.42-44)

- Daily meeting: ทบทวนเมื่อวาน (งานเสร็จ เหตุที่หลุดตาราง งานที่พบเพิ่ม), วันนี้ (break-in, OT), กำหนดพรุ่งนี้
- ข้อดี: ฟื้นจากงานไม่คาดคิดเร็ว ลด emergency
- Daily Work Plan (DWP) เป็นทั้งตัวแจกงานและบันทึกเวลาจริงเพื่อใช้ประมาณการครั้งหน้า
- วัดประสิทธิผลการ schedule: ประชุมตรงเวลา ทุกคนได้งาน 8 ชม. ประมาณการสมเหตุผล emergency น้อย งานเริ่ม-จบตามตาราง (p.44)

## 8. Wrench time และผลของ planning (CMRP CMPR-08 p.47-50)

**Wrench time** = เวลาที่ช่างลงมือทำงานจริงกับเครื่อง ไม่รวมเดินทาง เบิกของ รอ เตรียม/เก็บ

Breakdown ตัวอย่าง (p.47):

```
Total time 100%
 - ลา/วันหยุด 10%            -> available 90%
 - non-maintenance 30%        (admin, training, personal relief, slack)
 - maintenance 60%            (PM 30% + CM 30%)
     -> wrench time 15% + 15% = 30% ของเวลาทั้งหมด
        ที่เหลือ = travel, gather materials, prepare/put away
```

- ผลของ planning (p.50): เตรียมล่วงหน้า 1 ชม. ประหยัดเวลาทำงาน 3-5 ชม.; งานไม่วางแผนมี direct work 35% (เสียเวลา 65%) งานวางแผนแล้ว direct work 65% (เสีย 35%) ผลรวมในตารางตรวจแล้วถูก
- Wrench time ไม่ใช่ตัวเดียวกับ Utilization Factor B5 ของ RBMM ดู [[Maintenance KPIs]]

### ตัวอย่าง efficiency และความไม่สอดคล้องของเลขใน slide (p.48-49)

Slide: wrench ~30% ของ 40 ชม. = 12 ชม./คน/สัปดาห์; ถ้า planning ทำให้ดีขึ้น 10% "บนฐาน 15 ชม." ได้ +1.5 ชม./คน/สัปดาห์; โรงงาน 60 คนเทียบเท่าเพิ่มคน 6 คน (มูลค่า > €400,000/ปี ตัวเลขปี 1997)

ตรวจเลข (derived):
- ฐานไม่ตรงกัน: ข้อความบอก wrench = 12 ชม. แต่คำนวณบนฐาน 15 ชม. ถ้าใช้ 12 ชม. การดีขึ้น 10% (relative) = **+1.2 ชม./คน/สัปดาห์** (ไม่ใช่ 1.5)
- ถ้าใช้ฐานเดียวกันตลอด ได้ 6 คนเท่ากันทั้งสองฐาน: 60 x 1.5 / 15 = 6 หรือ 60 x 1.2 / 12 = 6
- ถ้าผสมฐาน คือใช้ +1.5 ชม. แต่หารด้วย wrench 12 ชม./คน ได้ 60 x 1.5 / 12 = **7.5 คน** ไม่ใช่ 6
- สรุป: ตัวเลข 6 คนถูกเมื่อใช้ฐานเดียวกัน ความผิดอยู่ที่ slide ใช้ 12 กับ 15 ชม. ปนกัน ค่าที่ควรใช้กับข้อความ "wrench 12 ชม." คือ +1.2 ชม./คน และเทียบเท่า 6 คน ตัวเลขนี้ไม่ใช่ contested (เป็นความผิดเลขคณิตของ slide)

## 9. มุมมองของ MPM: งานวางแผน งานรอ และผลของ planner (เพิ่ม 2026-10-28)

ที่มา: [[Maintenance Profit Maker Book]] บทที่ 4 และ 12 รายละเอียดวงจร WO 6 ขั้นอยู่ที่ [[Work Order Lifecycle]]

### คำถามวางแผนและเงื่อนไข scheduling (MPM p.68-70)

- งานวางแผนตอบ 7 คำถาม (ทรัพยากร, วิธีทำ, ขั้นตอนความปลอดภัย/ตัดแยกระบบ, ชั่วโมง, เครื่องมือและอะไหล่, ค่าใช้จ่ายรวม, งบและผู้อนุมัติ) ใกล้กับ 6 องค์ประกอบของ CMRP ในหัวข้อ 1 (ดูรายการเต็มที่ [[Work Order Lifecycle]])
- เงื่อนไข scheduling 2 ข้อ: เครื่องพร้อมให้ซ่อมตาม Production Plan และทรัพยากรพร้อมในวันทำงาน; อุปสรรคใหญ่ที่สุดคือความพร้อมของอะไหล่ (MPM p.69)
- ประชุมประจำวันสั้น ๆ ตรวจความพร้อมงานพรุ่งนี้และสัปดาห์หน้า สอดคล้องกับ daily meeting ของ CMRP ในหัวข้อ 7; Resource Leveling Function ของ CMMS ช่วยปรับตารางแต่จัดอัตโนมัติไม่ง่าย (MPM p.69-70)

### หมวดงานรอ (Wait) 5 หมวด (MPM p.70)

| หมวด | ความหมาย |
|---|---|
| รออะไหล่ | อะไหล่ยังไม่พร้อม/ยังไม่มาถึง |
| รอกำลังคน | ช่าง/ผู้เชี่ยวชาญไม่ว่าง |
| รอเครื่องมือ | เครื่องมือพิเศษไม่พร้อม |
| รอเครื่องจักรหยุด | ต้องรอโอกาสหยุดเครื่อง/ซ่อมใหญ่ |
| อื่น ๆ | สาเหตุอื่น |

ละเอียดกว่า RBMM ที่มี Wait for Material / Shutdown / Others (RBMM p.106) ใช้แยกติดตามเร่งรัด และสอดคล้องกับกฎ CMRP "ห้ามลงตารางงานที่ของยังไม่ครบ" ในหัวข้อ 7

### ตัวอย่างผลของ planner ต่อการใช้กำลังคน (MPM p.227)

| กรณี | คน | UF ที่เป็นเนื้องาน | เนื้องานรวม |
|---|---|---|---|
| ไม่มี planner | ช่าง 3 | 35% ต่อคน | 3 x 35% = 105% |
| มี planner 1 คน | ช่าง 3 + planner 1 | ช่าง 55%, planner 0% | 3 x 55% = 165% |

- หนังสือสรุปว่าเพิ่ม 165/105 = **1.57 เท่า** และโดยทั่วไป **ช่าง 20-30 คนต่อ planner 1 คน** (ยืนยันสัดส่วน 1:20-30 ของ CMRP ในหัวข้อ 3); ช่าง 30 คน + planner 1 คน เสมือนช่าง 30 x 1.57 = 47 คน ส่วนเกิน 17 คนนำไปทำ PM (MPM p.227)
- **ข้อควรระวัง (derived)**: 1.57 เทียบเนื้องานของช่างกลุ่มเดิมโดยไม่นับต้นทุนหัวของ planner ถ้านับต่อหัวทั้ง 4 คน = 165%/4 = 41.25% ต่อหัว เทียบ 35% ต่อหัว = ดีขึ้นเพียง **1.18 เท่า** นอกจากนี้ตัวอย่างใช้ ratio planner 1:3 แต่ข้อสรุปใช้ 1:30 จึงเป็นการสมมติว่า UF 55% ยังทำได้เมื่อ planner 1 คนดูแล 30 คน และข้อความนำพิมพ์ "ช่าง 35 คน" ขณะที่ตัวอย่างใช้ช่าง 3 คน (น่าจะพิมพ์ผิด)
- คำว่า Utilization Factor ในตัวอย่างนี้หมายถึงสัดส่วน "เนื้องาน" (35% -> 55%) ซึ่งใกล้แนวคิด wrench time ในหัวข้อ 8 มากกว่า B5 ของ RBMM; ทิศทางสอดคล้องกับ CMRP ที่งานวางแผนแล้วมี direct work 65% vs 35% (CMRP CMPR-08 p.50)

## เชื่อมโยงกับ compressor failure hierarchy

- งาน repetitive job plan และ bad actor (CMRP CMPR-09 p.22-24) ระบุได้จาก failure mode ที่เกิดซ้ำของ [[Compressor]] ตาม [[Failure Mode]] เช่นงานแก้ leakage ([[ELP External Leakage Process Medium]]) ซึ่งช่วยสร้าง standard job plan ต่อ [[Maintainable Item]] (การตีความ ไม่ใช่ข้อความสไลด์)
- Feedback และ DWP ที่บันทึกเวลาจริงเป็นแหล่ง active maintenance time ที่ ISO 14224 ต้องการ ดู [[Failure Data Recording]] และ [[Maintenance Time Definitions]]

## ดูเพิ่ม

- [[Maintenance Backlog and Schedule Compliance]]
- [[Turnaround Management]]
- [[CMMS]]
- [[Maintenance KPIs]]
- [[Spare Parts Management]]
- [[Maintenance Efficacy Pyramid]]
- [[CMRP Course]]
- [[Work Order Lifecycle]]
- [[Maintenance Profit Maker Book]]

## Triplets

- [[Maintenance Planning and Scheduling]] [defined_in:: [[CMRP Course]]] CMPR-09 and CMPR-08 p.46-50
- Planning [differs_from:: Scheduling] planning = how (method, resources); scheduling = when and who (CMRP CMPR-09 p.2, p.34)
- Planning [related_to:: Wrench Time] basic goal is more hands-on time without waiting (CMRP CMPR-09 p.11)
- Work Request [step_of:: Work Order Flow] step 1 of 7 (CMRP CMPR-09 p.6-7)
- Planning [step_of:: Work Order Flow] step 3 of 7 (CMRP CMPR-09 p.6-7)
- Scheduling [step_of:: Work Order Flow] step 4 of 7 (CMRP CMPR-09 p.6-7)
- Feedback [step_of:: Work Order Flow] step 7 of 7 (CMRP CMPR-09 p.6-7)
- Long Range Planning [has_value:: 3-5 years] (CMRP CMPR-09 p.12-13)
- Budget Planning [has_value:: 1-3 years] (CMRP CMPR-09 p.13)
- Supervisor [has_value:: 1:10-15] span of control per craftsman, example (CMRP CMPR-09 p.8)
- Planner [has_value:: 1:20-30] span of control per craftsman, example (CMRP CMPR-09 p.8)
- Maintenance Engineer [has_value:: 1:40-50] span of control per craftsman, example (CMRP CMPR-09 p.8)
- Planner [has_value:: 25%] share of time in the field for scoping (CMRP CMPR-09 p.10)
- Planner [uses:: [[CMMS]]] CMMS super-user, configuration and data quality (CMRP CMPR-09 p.10-11)
- Work Screening [step_of:: Planning Process] step 1 of 7 (CMRP CMPR-09 p.15)
- Assessing and Scoping [step_of:: Planning Process] step 2, always visit the job site (CMRP CMPR-09 p.18-19)
- Job Research [step_of:: Planning Process] step 3 (CMRP CMPR-09 p.20)
- Job Breakdown [step_of:: Planning Process] step 4 (CMRP CMPR-09 p.20-21)
- Material Take-off [step_of:: Planning Process] step 5, BOM and stock reservation (CMRP CMPR-09 p.30-31)
- Work Package [step_of:: Planning Process] step 6 assemble work package (CMRP CMPR-09 p.32)
- Planning Feedback [step_of:: Planning Process] step 7, job planning survey (CMRP CMPR-09 p.33)
- Material Take-off [uses:: Stock Reservation] planner reserves stock items for planned job (CMRP CMPR-09 p.30)
- Staging [applies_to:: Direct Purchase Parts] also low-stock and fast-moving items; not unique, bulky or common consumables (CMRP CMPR-09 p.31)
- Standard Job Plan [has_category:: preventive, repetitive, safety] (CMRP CMPR-09 p.22-24)
- Estimating [uses:: Historical Records] one of 4 methods with engineered standards, benchmarking, experienced judgment (CMRP CMPR-09 p.25)
- Estimating Accuracy [has_value:: +/- 15%] feedback criterion (CMRP CMPR-09 p.33)
- Estimating [depends_on:: Consistency] consistency more important than absolute accuracy (CMRP CMPR-09 p.29)
- Reasonable Expectancy [defined_in:: IDCON] as cited by slide (CMRP CMPR-09 p.28)
- PR1 Emergency [is_a:: Work Priority] start immediately, overtime auto-approved (CMRP CMPR-09 p.16)
- PR2 Urgent [is_a:: Work Priority] start within hours (CMRP CMPR-09 p.16)
- PR3 Routine [is_a:: Work Priority] schedule as convenient within criteria (CMRP CMPR-09 p.16)
- PR4 No Action [is_a:: Work Priority] operations decides (CMRP CMPR-09 p.16)
- Uncontrolled Safety Hazard [selects:: PR1 Emergency] decision flow, read from scan (CMRP CMPR-09 p.16)
- Major Production Loss [selects:: PR1 Emergency] decision flow (CMRP CMPR-09 p.16)
- No Production Loss [selects:: PR4 No Action] decision flow (CMRP CMPR-09 p.16)
- Urgency Trap [related_to:: Work Priority] urgent is not necessarily important (CMRP CMPR-09 p.17)
- PM [differs_from:: Work Priority] PM missing from PR flow chart; scheduled first outside PR1-PR4, wiki interpretation (CMRP CMPR-09 p.16, p.39-40)
- Weekly Schedule [uses:: PM First Rule] PM always loaded first (CMRP CMPR-09 p.40)
- Weekly Schedule [has_value:: 8 h per person per day] load fully (CMRP CMPR-09 p.40)
- Weekly Schedule [depends_on:: Material Availability] never schedule jobs without all materials (CMRP CMPR-09 p.40)
- Work Order Age [differs_from:: Work Priority] age never overrides priority (CMRP CMPR-09 p.40)
- No Emergency Reserve Rule [contradicts:: Emergency Flexibility Rule] same slide p.40; resolved as full loading with low-priority fillers, wiki interpretation
- Gantt Chart [applies_to:: Weekly Schedule] shows sequence and overlap, not dependencies (CMRP CMPR-09 p.41)
- Daily Work Plan [produces:: Actual Job Hours] reused for future estimates (CMRP CMPR-09 p.44)
- Wrench Time [has_value:: 30%] of total time, 15% PM + 15% CM (CMRP CMPR-08 p.47)
- Wrench Time [has_value:: 12 h per week] 30% of 40 h (CMRP CMPR-08 p.48)
- Planning Preparation [has_value:: 1 h saves 3-5 h] (CMRP CMPR-08 p.50)
- Planned Work [has_value:: 65% direct work] vs unplanned 35% (CMRP CMPR-08 p.50)
- Wrench Time Gain [has_value:: 1.2 h per person per week] 10% of 12 h base, derived; slide shows 1.5 h on 15 h base
- Wrench Time Gain [has_value:: 6 workers equivalent] 60 staff, same base either way, derived (CMRP CMPR-08 p.48-49)
- Slide Wrench Time Arithmetic [contradicts:: Wrench Time Gain] slide mixes 12 h and 15 h bases; mixed base gives 7.5 workers
- Wrench Time [differs_from:: B5 Utilization Factor] hands-on time vs man-hours booked to WO, see Maintenance KPIs
- [[Maintenance Planning and Scheduling]] [part_of:: [[Maintenance Efficacy Pyramid]]] level 3 work control
- [[Maintenance Planning and Scheduling]] [related_to:: [[Maintenance Backlog and Schedule Compliance]]]
- Planning Questions [applies_to:: [[Maintenance Planning and Scheduling]]] 7 questions of MPM planning stage (MPM p.68-69)
- Work Order Scheduling [depends_on:: Spare Part Availability] biggest scheduling obstacle (MPM p.69)
- Wait Status [has_category:: parts, manpower, tools, machine shutdown, others] 5 wait categories (MPM p.70)
- Wait Status [differs_from:: Work Backlog Basket] RBMM has Material, Shutdown, Others only (RBMM p.106)
- Planner [has_value:: 1:20-30] craftsmen per planner, confirms CMRP ratio (MPM p.227)
- Planner Effect [has_value:: 1.57 times] 3 x 55% / 3 x 35% work content, excludes planner head (MPM p.227)
- Planner Effect [has_value:: 1.18 times] per head incl. planner, 41.25% vs 35%, derived (MPM p.227)
- Planner Effect [has_value:: 47 equivalent craftsmen] 30 craftsmen x 1.57, 17 extra to PM (MPM p.227)
- MPM Utilization Factor Work Content [related_to:: Wrench Time] 35% to 55% work content, closer to wrench time than B5, wiki interpretation
- [[Maintenance Planning and Scheduling]] [related_to:: [[Work Order Lifecycle]]]

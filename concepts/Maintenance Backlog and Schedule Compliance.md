---
title: Maintenance Backlog and Schedule Compliance
created: 2026-10-25
updated: 2026-10-28
type: concept
tags: [work-management, kpi, maintenance-management, cmms, cmrp, mpm, work-order]
sources: [cmrp.md, reliability-based-maintenance-management.md, iso-14224.md, maintenance-profit-maker.md]
confidence: medium
contested: false
---

# Maintenance Backlog and Schedule Compliance

ตัวชี้วัดของระบบ work management ตาม [[CMRP Course]] (CMPR-09 p.37-46 และ CMPR-10 p.1-9): backlog บอกว่างานค้างมากน้อยเท่าไรเทียบกำลังคน ส่วน schedule compliance บอกว่าทำตามตารางได้จริงแค่ไหน กระบวนการวางแผนและจัดตารางที่ตัวชี้วัดเหล่านี้วัดอยู่ที่ [[Maintenance Planning and Scheduling]] ภาพรวมดัชนีอยู่ที่ [[Maintenance KPIs]]

## 1. Backlog คืออะไร

- Backlog ทำหน้าที่เหมือน **surge tank** ถ่วงสมดุลงานเข้า-ออกกับขนาดทีม (CMRP CMPR-09 p.37)
- **Ready backlog** = งานที่ของ เครื่องมือ แบบ และการอนุมัติครบ เริ่มได้ทันที; **Total backlog** = ready + งานเปิดที่ยังขาดบางอย่าง (CMRP CMPR-09 p.38)
- หน่วย: man-hours, crew-weeks, FTE ติดตามเสริมด้วยจำนวนและประเภท WO (CMRP CMPR-09 p.38)
- RBMM วาง Work Order Backlog เป็น core module ของ [[CMMS]] และมีสถานะรอ (Wait for Material / Shutdown / Others) ใน Work Backlog Basket (RBMM p.94, p.106) สถานะ "รอของ" สอดคล้องกับนิยามงานที่ไม่อยู่ใน ready backlog (การเทียบของ wiki)

### สูตร

```
Backlog (weeks) = ชั่วโมงรวมของ WO เปิดที่ยังไม่ลงตาราง / work capacity (ชม. ต่อสัปดาห์)
```

(CMRP CMPR-09 p.39) ตัวอย่าง (derived ไม่อยู่ใน slide): 1,200 ชม. / (10 คน x 40 ชม.) = 1,200 / 400 = 3 สัปดาห์

- PM/PdM ของสัปดาห์หน้าแยกพิจารณาและลงตารางก่อน ชั่วโมงที่เหลือจึงให้งานตาม priority (CMRP CMPR-09 p.39)
- CMPR-10 ใช้หน่วย "สัปดาห์" ใน planning metrics (p.7) แต่ไม่ได้ให้สูตรซ้ำ

## 2. ระดับ backlog ที่เหมาะสม: สองสไลด์ให้ค่าต่างกัน

| แหล่ง | ค่าที่ให้ | ลักษณะ |
|---|---|---|
| CMPR-09 p.43 | **2-3 สัปดาห์** ถือว่าดี | ค่าเดียวเป็นเป้า |
| CMPR-10 p.1 | แถบเป้าหมาย **3-6 สัปดาห์** บนกราฟ work load เทียบ resources เหนือแถบ = งานมากเกิน ใต้แถบ = งานน้อยเกิน | ช่วงควบคุม |

ทั้งสองมาจากหลักสูตรเดียวกันและไม่ได้อธิบายความต่าง ช่วงซ้อนกันที่ 3 สัปดาห์ wiki ไม่เลือกค่าใดค่าหนึ่ง (ความรู้ทั่วไป ไม่มีใน sources: ค่าแนะนำในวงการแตกต่างตามว่านับ total หรือ ready backlog ซึ่ง slide ไม่ได้ระบุ) ไม่ตั้ง contested เพราะเป็นความต่างภายในแหล่งเดียว ไม่ได้ขัดกับ RBMM หรือ ISO (RBMM ใช้ Backlog เป็นดัชนีใน activity 18 โดยไม่ให้เป้าตัวเลข ดู [[Maintenance KPIs]])

- **Backlog สูงเกิน**: คุมงานไม่ได้ ขวัญกำลังใจต่ำ safety แย่ ล้าจากแรงกดดัน (CMRP CMPR-10 p.1) และกราฟ CMPR-09 p.45 แสดงว่าเมื่องานที่จำเป็นทำได้น้อยลง การเสื่อมสภาพและงาน reactive จะเพิ่ม
- **Backlog ต่ำเกิน**: งานไม่พอ ถูกยืดให้เต็มวัน supervisor ต้องวิ่งหางาน (CMRP CMPR-10 p.2)
- ผู้บริหารใช้ backlog ตัดสิน: กำลังคนตามทักษะ, OT/ผู้รับเหมา, งบประจำปี, วางแผน shutdown, capacity รับงานโครงการ (CMRP CMPR-09 p.46)

## 3. Backlog purging

- ประโยชน์: ลบ WO เก่าหลายปี, งานที่ไม่สมเหตุผลแล้ว, งานที่ทำเสร็จแต่ยังไม่ปิดในระบบ, WO ซ้ำ (CMRP CMPR-10 p.2)
- backlog ที่ไม่แม่นยำแทบไร้ค่าในการบริหาร และขัดขวางการวิเคราะห์กำลังคน (CMRP CMPR-10 p.3)
- **รอบทบทวน**: formal review ทุก 3 เดือน (มีเอกสาร) และ informal review รายเดือนใน planning meeting (CMRP CMPR-10 p.3)
- ข้อควรระวัง (การตีความของ wiki): CM-Unplanned WO ที่ค้างเพราะยังไม่ระบุ failure mode ("Backlog - Failure Mode Undefined", RBMM p.111) ไม่ควรถูกปิดทิ้งตอน purge ดู [[Failure Data Recording]]

## 4. Planning metrics (CMRP CMPR-10 p.7)

```
% Planned Work      = จำนวน planned WO / จำนวน WO ทั้งหมด
Planning Accuracy   = Estimated Job Costs / Actual Job Costs
% Emergency         = Emergency man-hours / Total maintenance man-hours
Backlog size        = สัปดาห์
```

- Planning Accuracy ต่ำกว่า 1 แปลว่าใช้จริงเกินประมาณการ slide ไม่ให้เป้า; เกณฑ์ feedback ระดับงานคือ ±15% (CMRP CMPR-09 p.33)
- เทียบแหล่งอื่น: RBMM ให้อุดมคติงานตามแผนมากกว่า 85% (RBMM p.54) โดยนับเป็น man-hours/cost ส่วน % Planned Work ของ CMRP นับเป็นจำนวน WO ฐานต่างกันจึงเทียบตรงไม่ได้; ISO ให้ estimating accuracy เป็น KPI 23-24 และ unscheduled work (KPI 20) top quartile น้อยกว่า 2% (ISO 14224 Table E.3) ดู [[Maintenance KPIs]]

## 5. Schedule compliance, performance และ effectiveness (CMRP CMPR-10 p.8-9)

```
Schedule Compliance    = scheduled labor-hours ที่ทำเสร็จ / scheduled labor-hours ที่ลงตาราง
Schedule Performance   = scheduled labor-hours ที่ทำเสร็จ / labor-hours ที่มีทั้งหมด (available)
Schedule Effectiveness = Schedule Performance x สัดส่วนชั่วโมงที่ทำเสร็จที่เป็น direct work
```

- งานแทรก (schedule break, urgent job) **ไม่ได้เครดิต** ในทั้งสามตัว (p.8)
- ใช้ร่วมกันเพราะแต่ละตัวปิดช่องโหว่ของอีกตัว (p.9)

### Compliance ถูก "เล่นตัวเลข" ได้อย่างไร

| วิธี | ผล | ตัวที่จับได้ |
|---|---|---|
| ลงตารางเพียงส่วนน้อยของกำลังคน | compliance สูงง่าย | Schedule Performance (ตัวหารคือชั่วโมงที่มีทั้งหมด) |
| ใส่ indirect work (training, ยืมตัวไปช่วยงานอื่น) ลงตาราง | งานพวกนี้ comply เกือบ 100% อัตโนมัติ ดัน compliance และ performance | Schedule Effectiveness (ถ้าไม่ใส่ indirect work ลงตาราง ไม่ต้องใช้ตัวนี้) |
| นับงานแทรกเป็นผลงาน | ดูเหมือนทำได้ครบ | กฎไม่ให้เครดิต schedule break |

(CMRP CMPR-10 p.8-9) ISO ให้เป้า schedule compliance top quartile มากกว่า 98% (ISO 14224 Table E.3) ควรอ่านเป้านี้คู่กับ performance เพราะ compliance เพียงตัวเดียวสูงได้โดยไม่ได้ทำงานมากขึ้น (การเชื่อมของ wiki)

### ใครวัดและวัดเพื่ออะไร

- Planner ติดตามตลอดสัปดาห์ บันทึกสถานะ สรุป ratio และเหตุผลที่ไม่ทำตาม เป้าคือหา corrective action ไม่ใช่หาคนผิด (CMRP CMPR-10 p.4)
- Schedule เป็นเป้าที่ดีที่สุดให้ supervisor ไล่ตาม ยืดหยุ่นได้เมื่อมีงานเร่งด่วนจริง (p.5)
- Non-compliance ร้ายแรงพิเศษเมื่อคืนเครื่องให้ production ไม่ทัน ทำให้ Operations ไม่อยากปล่อยเครื่องทำ PM ครั้งหน้า (p.5)

### สาเหตุของ non-compliance (CMRP CMPR-10 p.6)

1. Operations ไม่ปล่อยเครื่องตามที่ตกลง
2. Emergency มากเกิน ช่างถูกดึงไปโดยไม่ผ่าน work management process
3. จัดคนไม่เหมาะ
4. Stock-out บ่อย หรือไม่ได้เบิกของล่วงหน้า
5. Planning package ไม่ตรงความจริง (อะไหล่ผิด ขั้นตอนไม่ครบ ไม่มีข้อมูล lockout/spec)
6. ประเมินเวลางานต่ำไป
7. ขาดงานมาก หรือ peak load ซ้อนกัน

ช่วงเริ่มใช้ scheduling ปัญหาที่ซ่อนอยู่จะโผล่ขึ้น ให้บันทึก รายงาน และดู trend (p.6)

## 6. Backlog ในมุมของ MPM (เพิ่ม 2026-10-28)

ที่มา: [[Maintenance Profit Maker Book]] ดัชนีการบริหารข้อ 5.8 และบทที่ 4

```
Backlog (MPM) = Man-Hours ที่ต้องใช้ทำงานที่เหลือ / Man-Hours กำลังคนที่พร้อม
```

- ความหมาย: งานค้างต้องใช้อีกกี่ **วัน** จึงเสร็จ (MPM p.155-156) หนังสือ **ไม่ให้เป้าตัวเลข**
- หัวข้อดัชนีเขียนว่า "ต่อสัปดาห์" และ "ต่องานที่เข้ามาทั้งหมด" แต่สูตรเป็น man-hours ที่เหลือ / man-hours ที่พร้อม และอธิบายเป็นจำนวนวัน หน่วยจึงขึ้นกับว่าใช้ man-hours พร้อมต่อวันหรือต่อสัปดาห์ (หนังสือไม่ระบุชัด)
- บทที่ 4 ให้ WO ที่เปิดแล้วเข้ากลุ่ม Backlogs ทันที และมีรายงาน Work Request Backlogs แยกต่างหากสำหรับ WR ที่ยังไม่ได้ตอบสนอง (MPM p.63-67) ดู [[Work Order Lifecycle]]

| ประเด็น | MPM | CMRP (หัวข้อ 1-2) |
|---|---|---|
| หน่วย | วัน (ไม่ชัด อาจเป็นสัปดาห์) | สัปดาห์ |
| ขอบเขตงาน | งานที่เหลือทั้งหมด | WO เปิดที่ยังไม่ลงตาราง |
| เป้า | ไม่ให้ | 2-3 หรือ 3-6 สัปดาห์ |

ต่างที่หน่วยและขอบเขต ไม่ใช่ขัดเชิงหลักการ (ไม่ตั้ง contested) เมื่อเทียบตัวเลข ให้แปลงหน่วยและตรวจขอบเขตก่อน (การตีความของ wiki)

## เชื่อมโยงกับ compressor failure hierarchy

- % Emergency และ schedule break ส่วนใหญ่มาจาก CM-Unplanned ที่ระบุ failure mode ได้ ถ้าบันทึก [[Failure Mode]] ของ [[Compressor]] ใน WO จะแยกได้ว่างานแทรกมาจาก mode ใด (เช่น [[UST Spurious Stop]]) แล้วส่งต่อให้ [[Root Cause Analysis]] (การตีความ ไม่ใช่ข้อความสไลด์)

## ดูเพิ่ม

- [[Maintenance Planning and Scheduling]]
- [[Maintenance KPIs]]
- [[CMMS]]
- [[Turnaround Management]]
- [[CMRP Course]]
- [[Work Order Lifecycle]]
- [[Maintenance Profit Maker Book]]

## Triplets

- [[Maintenance Backlog and Schedule Compliance]] [defined_in:: [[CMRP Course]]] CMPR-09 p.37-46, CMPR-10 p.1-9
- Backlog [has_formula:: open unscheduled WO hours / weekly work capacity] in weeks (CMRP CMPR-09 p.39)
- Backlog [has_value:: 3 weeks] example 1,200 h / (10 x 40 h), derived, not on slide
- Backlog [has_value:: 2-3 weeks] best level (CMRP CMPR-09 p.43)
- Backlog [has_value:: 3-6 weeks] target band, above = excessive, below = too little work (CMRP CMPR-10 p.1)
- Backlog 2-3 Weeks [differs_from:: Backlog 3-6 Weeks] two slides of the same course disagree; not contested, internal to CMRP
- Ready Backlog [part_of:: Total Backlog] ready = materials, tools, drawings, approval complete (CMRP CMPR-09 p.38)
- Backlog [has_parameter:: Man-hours] also crew-weeks, FTE, WO count and type (CMRP CMPR-09 p.38)
- Backlog [related_to:: Surge Tank] balances inflow and outflow against crew size (CMRP CMPR-09 p.37)
- Backlog [input_to:: Manpower Decision] also OT, contractors, budget, shutdown planning (CMRP CMPR-09 p.46)
- Backlog Purging [applies_to:: Backlog] removes old, duplicate, done-but-open WOs (CMRP CMPR-10 p.2)
- Backlog Formal Review [has_value:: every 3 months] documented (CMRP CMPR-10 p.3)
- Backlog Informal Review [has_value:: monthly] in planning meeting (CMRP CMPR-10 p.3)
- % Planned Work [has_formula:: planned WOs / total WOs] count basis (CMRP CMPR-10 p.7)
- % Planned Work [differs_from:: Planned Work Share] CMRP counts WOs; RBMM > 85% uses man-hours/cost (RBMM p.54)
- Planning Accuracy [has_formula:: Estimated Job Costs / Actual Job Costs] below 1 = overrun (CMRP CMPR-10 p.7)
- % Emergency [has_formula:: Emergency man-hours / Total maintenance man-hours] (CMRP CMPR-10 p.7)
- Schedule Compliance [has_formula:: scheduled labor-hours completed / scheduled labor-hours] (CMRP CMPR-10 p.8)
- Schedule Performance [has_formula:: scheduled labor-hours completed / available labor-hours] (CMRP CMPR-10 p.8)
- Schedule Effectiveness [has_formula:: Schedule Performance x direct-work share of completed hours] (CMRP CMPR-10 p.8)
- Schedule Break [has_value:: no credit] in compliance, performance, effectiveness (CMRP CMPR-10 p.8)
- Schedule Compliance Inflation [detected_by:: Schedule Performance] compliance inflated by scheduling only a small part of the workforce (CMRP CMPR-10 p.9)
- Indirect Work Inflation [detected_by:: Schedule Effectiveness] scheduled indirect work complies almost 100% automatically (CMRP CMPR-10 p.9)
- Schedule Effectiveness [related_to:: Indirect Work] needed only if indirect work is scheduled (CMRP CMPR-10 p.9)
- Schedule Compliance [has_value:: > 98%] ISO top quartile; read together with performance (ISO 14224 Table E.3)
- Operations Not Releasing Equipment [has_category:: cause of schedule non-compliance] (CMRP CMPR-10 p.6)
- Excess Emergencies [has_category:: cause of schedule non-compliance] (CMRP CMPR-10 p.6)
- Stock-outs [has_category:: cause of schedule non-compliance] (CMRP CMPR-10 p.6)
- Inaccurate Planning Package [has_category:: cause of schedule non-compliance] (CMRP CMPR-10 p.6)
- Underestimated Job Time [has_category:: cause of schedule non-compliance] (CMRP CMPR-10 p.6)
- Schedule Compliance [measures:: Schedule Adherence] tracked weekly by planner for corrective action, not blame (CMRP CMPR-10 p.4)
- [[Maintenance Backlog and Schedule Compliance]] [related_to:: [[Maintenance KPIs]]]
- MPM Backlog [has_formula:: remaining job man-hours / available man-hours] expressed in days, no target (MPM p.155-156)
- MPM Backlog [differs_from:: Backlog] MPM days and all remaining work vs CMRP weeks and unscheduled WOs with 2-3 or 3-6 week target
- Work Request Backlogs [related_to:: [[Work Order Lifecycle]]] unanswered WR report for expediting or cancelling (MPM p.63-64)

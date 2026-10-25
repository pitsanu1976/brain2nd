---
title: Turnaround Management
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [turnaround, work-management, maintenance-management, budget, cost, cmrp]
sources: [cmrp.md, reliability-based-maintenance-management.md, iso-14224.md]
confidence: medium
contested: false
---

# Turnaround Management

**Turnaround** (shutdown, major overhaul) คือเหตุการณ์ทางวิศวกรรมที่หยุดโรงงานเพื่อติดตั้งของใหม่ overhaul ของเดิม และรื้อของที่เลิกใช้ออก (CMRP CMPR-10 p.12) หน้านี้สรุปเนื้อหา turnaround ของ [[CMRP Course]] (CMPR-10 p.9-30 กลยุทธ์ scope องค์กร และ CMPR-11 p.1-3 phases) งานวางแผนรายวันทั่วไปอยู่ที่ [[Maintenance Planning and Scheduling]]

หมายเหตุแหล่ง: สไลด์ส่วนนี้ใช้ถ้อยคำแบบตำรา ("this book", "the author") แต่ไม่ระบุชื่อเล่ม (ความรู้ทั่วไป confidence ต่ำ: น่าจะเป็น T. Lenahan, *Turnaround Management*, 1999) เนื้อหาด้านล่างถอดความด้วยถ้อยคำของ wiki

## 1. ทำไม turnaround เป็นเรื่องเสี่ยง

- จำเป็นทางธุรกิจสำหรับอุปกรณ์ใหญ่/ซับซ้อน แต่แพง ไม่พึงประสงค์ และ **อาจลด reliability** ได้ (CMRP CMPR-10 p.12)
- ต้นทุนมีทั้ง downtime และค่าดำเนินงาน การกระจายต้นทุนหลายปีไม่ได้ทำให้ผลกระทบรวมลดลง (CMRP CMPR-10 p.13) เทียบกับวิธีกระจายต้นทุนรายปีของ RBMM ที่ [[Maintenance Budget]]
- เป็นภัยต่อ reliability จากแผนไม่ดี ตัดสินใจผิด ฝีมือแย่ วัสดุผิด และความเสียหายช่วง shutdown/start-up (CMRP CMPR-10 p.14)
- ความเสี่ยงอุบัติเหตุสูงขึ้นมาก เพราะกลับด้านจากงานปกติ: คนแปลกหน้าจำนวนมาก งานอันตรายไม่คุ้นเคย จึงต้องมี safe system of work (CMRP CMPR-10 p.14)
- งบและเวลามักบานปลายจากความไม่แน่นอนทางเทคนิค ควรมี contingency ทั้งเวลาและเงิน (CMRP CMPR-10 p.15)
- ความไม่แน่นอนเป็นธรรมชาติ: วางแผนขณะเครื่องยังเดิน ความผิดปกติซ่อนอยู่จนเปิดเครื่อง (CMRP CMPR-10 p.28)

## 2. กลยุทธ์ระดับผู้บริหาร: eliminate first

- **เป้าพื้นฐานคือกำจัด maintenance turnaround** ถ้าจำเป็นจริงจึงจัดให้สอดคล้องกับเป้า maintenance, production และธุรกิจ (CMRP CMPR-10 p.15)
- ปรัชญา: เปลี่ยนจาก preventive maintenance (ขับด้วยเทคนิค) ไปเป็น **maintenance prevention** (ขับด้วยธุรกิจ) ตั้งคำถามกับทุกกิจกรรมว่ากำจัดได้ไหม เริ่มจากกิจกรรมใหญ่สุดคือ turnaround (CMRP CMPR-10 p.17)
- **Steering group** ของผู้บริหารระดับสูง ประชุมเป็นระยะทั้งปี ดูแลกลยุทธ์ระยะยาว และมองหลาย turnaround เป็นลำดับต่อเนื่องใน asset management ไม่ใช่เหตุการณ์แยก (CMRP CMPR-10 p.16)
- ที่มาของงานใน work list ที่อาจไม่เกี่ยวกับ reliability: ritual task, chronic problem ที่ไม่เคยทำ RCA (ดู [[Root Cause Analysis]]), corrosion/fouling ที่เลี่ยงได้, ข้อบกพร่องจาก design/ติดตั้ง, เดินเครื่องผิดวิธี, PM ระหว่างปีไม่พอ (CMRP CMPR-10 p.18)
- เป้า (objectives) ที่ควรตั้ง: ทำเมื่อจำเป็นจริง, ระยะห่างระหว่าง event สูงสุด, scope ที่ validate แล้ว, duration ต่ำสุด, ต้นทุนต่ำสุด (CMRP CMPR-10 p.27) ตรงกับ ISO KPI 21 turnaround duration และ 22 time between turnarounds ที่ [[Maintenance KPIs]]

### Golden rule ของ work list

- การลดคนทำให้ PM/CM ค้าง แล้วมักโยนเข้า turnaround ทั้งที่ทำใน turnaround แพงกว่า (CMRP CMPR-10 p.19-20)
- **Golden rule: work list รับเฉพาะงานที่ทำช่วงอื่นไม่ได้** เว้นแต่มีเหตุผลเหนือกว่า (maintainability, hazard) และ turnaround ต้องไม่ใช้กลบจุดอ่อนของ maintenance philosophy (CMRP CMPR-10 p.20)
- เชื่อมกับสถานะ backlog "Wait for Shutdown" ใน [[CMMS]] (RBMM p.106) ซึ่งเป็นแหล่ง initial work list (การเชื่อมของ wiki) golden rule คือเกณฑ์กรองงานในสถานะนี้

### ด้านการเงิน (CMRP CMPR-10 p.18-19)

- บริษัทมักนับเฉพาะ direct cost; ต้องประมาณต้นทุนคร่าว ๆ แต่เนิ่น ๆ เทียบงบ ถ้าไม่พอให้เพิ่มงบ ตัด scope หรือหากลยุทธ์อื่น
- นับกำไรที่เสียทั้งช่วงหยุดและช่วงหลัง start-up ที่ rate/คุณภาพยังไม่ถึงเป้า
- **ค่าแรงพนักงานโรงงานช่วง turnaround ควรนับเป็นต้นทุนของ event** มิฉะนั้น event ดูถูกกว่าจริงและต้นทุนผลิตดูสูงเกินจริง ซึ่งต่างจากวิธีของ RBMM ที่ไม่รวมค่าแรงภายในในต้นทุน turnaround รายปี ดูหัวข้อ contested ใน [[Maintenance Budget]]

### Emergent work และประวัติ

- **Emergent work** = งานที่โผล่หลังเริ่ม execution: ปกติ **5-10%** ของงบที่วางแผน, แย่สุด **มากกว่า 45%** ถ้าสูงต้องปรับคุณภาพ technical specification ใน work request (CMRP CMPR-10 p.21)
- หลัง turnaround โรงงานต้องดีเท่าเดิมหรือดีกว่า; คาดหวังให้ต้นทุนแต่ละครั้งลดลงแม้เครื่องเก่าลง และ benchmark กับ best in field (CMRP CMPR-10 p.21-22)

## 3. Work scope

- **Project work**: ประเมิน necessity, desirability (จังหวะเวลา), payback ต้องคุ้มเชิงธุรกิจ; สัดส่วน maintenance:project (เช่น 90:10 กับ 10:90) เปลี่ยนวิธีบริหาร แต่ทุกงานต้องอยู่ใน **single plan** (CMRP CMPR-10 p.23-24)

| ประเภทงาน maintenance | ลักษณะ | ตัวอย่าง |
|---|---|---|
| Major task | ต้องมี engineering input ผู้บริหารต้อง challenge ทุกงาน (ตัด/เลื่อน) และดูงานบน critical path ด้วย risk analysis | overhaul เครื่องใหญ่, re-tray column |
| Minor task | ระบุ spec งานก็พอ | ล้าง/ตรวจ heat exchanger เล็ก |
| Bulk work | ของเล็กจำนวนมาก แค่ schedule แต่มักเป็นตัวทำให้เสียเวลาเพราะกระจายตัว | valve, ปั๊มเล็ก |

(CMRP CMPR-10 p.25-26)

## 4. Organization: in-house หรือ outsource

| ทางเลือก | คำถามที่ต้องตอบ |
|---|---|
| ใช้คนในบริษัททั้งหมด | คนพอไหม ความสามารถเหมาะไหม (มักจัดคนตามที่ว่าง ไม่ใช่ตามความสามารถ) |
| Outsource ทั้งก้อนให้ contractor | ประวัติ claim/variation ต้องมีทีมคุมอีกชั้นหรือไม่ ซึ่งวนกลับไปคำถามว่าทำไมไม่บริหารเอง |

(CMRP CMPR-10 p.26-27)

- ความขัดแย้งเชิงจิตวิทยา: ทีมโรงงานรู้สึกว่าเครื่องเดินดีอยู่แต่ถูกรื้อโดยคนแปลกหน้า ต้อง integrate ด้วย briefing, training และการสื่อสาร (CMRP CMPR-10 p.29-30)
- ความรู้ที่ต้องรวมกัน: local (plant), work management (turnaround planner/engineer), supervision, craft, specialist (vendor), management of discrete projects (CMRP CMPR-10 p.30)

## 5. Phases ของ turnaround (CMRP CMPR-11 p.1-3)

| Phase | ระยะเวลา (figure p.3) | งานสำคัญ (ย่อ) |
|---|---|---|
| 1 Initiation | "หลายเดือน" (ข้อความ p.1: เริ่มได้ 2 ปีหรือมากกว่าก่อน event) | ตั้ง steering group, แต่งตั้ง turnaround manager, ตั้งทีมเตรียมงาน, กำหนด objective/policy, plant team ออก initial work list |
| 2 Preparation | 3-18 เดือน ตามขนาด | challenge/validate แล้ว **freeze work list**, job specification packages, pre-shutdown work, long-lead items, contracts, logistics, schedule/resource profile, cost control, safe system of work, ส่งแผนให้ steering group อนุมัติ, briefing |
| 3 Execution | ปกติ 2-8 สัปดาห์ | คุม planned และ emergent work (control team กำหนดและคิดราคา emergent work), duration, expenditure, safety, quality |
| 4 Termination | ปกติ 1-2 สัปดาห์ | เก็บพื้นที่, plant manager ตรวจรับ handover, de-brief เก็บ lessons learned, close-out report |

- Figure ชี้ว่า **work list คือรากฐาน** ของ safety, quality, cost, materials, resources, logistics และ duration (CMRP CMPR-11 p.3)
- **Contingency analysis** ใน preparation ถาม 4 ข้อ: fault อะไรน่าจะเจอ, แก้นานเท่าไร, ค่าใช้จ่าย, กระทบ duration อย่างไร คำตอบเป็นค่าประมาณแต่มักเป็นแนวทางเดียวที่มี (CMRP CMPR-11 p.1)
- **Execution 8 sub-phases** ตามลำดับ (CMRP CMPR-11 p.2):
  1. Shutdown (เอา inventory ออก, decontaminate, cool, isolate)
  2. Open up
  3. Inspect
  4. Install / overhaul / remove
  5. Box up
  6. Test (pressure, system, trip/alarm)
  7. Start up
  8. Clean up / final inspection
- **Single point responsibility**: ทุกจุดส่งต่องาน ผู้รับผิดชอบต้อง (1) ตรวจว่าขั้นก่อนหน้าเสร็จถูกต้องก่อนรับ (2) ทำส่วนของตนตาม spec (3) ส่งต่อเร็วที่สุด (4) รายงานการส่งต่อ; turnaround manager รับผิดชอบรวม (CMRP CMPR-11 p.2)
- การคุม scope ไม่มีหัวข้อแยกในสไลด์ อยู่ที่ golden rule (CMPR-10 p.20), freeze work list และการ define/cost emergent work (CMPR-11 p.3)

## 6. ความไม่สอดคล้องในสไลด์

- **Initiation 2+ ปี vs "หลายเดือน"**: ข้อความ CMPR-11 p.1 บอก initiation อาจเริ่ม 2 ปีหรือมากกว่าก่อน event แต่ figure p.3 บอกว่ากินเวลา "a period of months" ตีความให้สอดคล้องได้ว่าเริ่มเร็วแต่กิจกรรมจริงกินเวลาหลายเดือน แต่สไลด์ไม่ได้อธิบาย (การตีความของ wiki)
- **"five" vs 6 ประเภทความรู้**: CMPR-10 p.30 บอกว่ารวมความรู้ห้าประเภท แต่รายการมี 6 (ดูหัวข้อ 4) ใช้รายการ 6 ข้อเป็นหลัก
- **นิยาม risk = probability อย่างเดียว**: CMPR-10 p.25 นิยาม risk เป็นความน่าจะเป็นเชิงตัวเลขที่จะเกิดความสูญเสีย ไม่รวม consequence ต่างจากนิยามทั่วไป risk = likelihood x consequence และต่างจากไฟล์เดียวกันของหลักสูตร CMPR-09 p.3 ที่นิยาม risk = ผลกระทบ x ความน่าจะเป็น และจาก [[Criticality Assessment]] / [[FMECA]] ที่ใช้ consequence ร่วมด้วย ถือเป็นความคลาดเคลื่อนของสไลด์ ใช้นิยาม likelihood x consequence เมื่อทำ risk analysis ของ major task

## เชื่อมโยงกับ compressor failure hierarchy

- Major task ของ turnaround เช่น overhaul [[Compressor]] ขนาดใหญ่ ควรถูก challenge ด้วยข้อมูล failure mode และ conditional reliability ถึงรอบหยุดถัดไป (ดู [[Reliability Metrics]] ที่ใช้ตอบว่าเครื่องจะรอดถึง turnaround หรือไม่) แทนการ overhaul ตามรอบแบบ ritual (การตีความ ไม่ใช่ข้อความสไลด์)
- Emergent work ที่สูงชี้ว่าการตรวจสภาพก่อนหยุดไม่พอ เทคนิค CBM ช่วยให้ work list แม่นขึ้น ดู [[P-F Interval and Condition Monitoring]] และ [[Condition Monitoring Techniques]]

## ดูเพิ่ม

- [[Maintenance Planning and Scheduling]]
- [[Maintenance Backlog and Schedule Compliance]]
- [[Maintenance Budget]]
- [[CMMS]] (module 10 Turnaround Management)
- [[Maintenance KPIs]] (ISO KPI 21-22)
- [[CMRP Course]]

## Triplets

- [[Turnaround Management]] [defined_in:: [[CMRP Course]]] CMPR-10 p.9-30 and CMPR-11 p.1-3
- Turnaround [is_a:: Engineering Event] install new, overhaul existing, remove redundant (CMRP CMPR-10 p.12)
- Turnaround [related_to:: Reliability] can reduce reliability through poor execution and start-up damage (CMRP CMPR-10 p.12-14)
- Turnaround Strategy [selects:: Eliminate Turnaround] basic goal; align with business if unavoidable (CMRP CMPR-10 p.15)
- Maintenance Prevention [differs_from:: Preventive Maintenance] business-driven vs technically driven (CMRP CMPR-10 p.17)
- Steering Group [part_of:: [[Turnaround Management]]] senior management, meets periodically through the year (CMRP CMPR-10 p.16)
- Golden Rule [applies_to:: Turnaround Work List] only work that cannot be done at another time, unless maintainability or hazard (CMRP CMPR-10 p.20)
- Turnaround Work List [depends_on:: Wait for Shutdown Backlog] CMMS backlog status as initial source, wiki link (RBMM p.106)
- Emergent Work [has_value:: 5-10%] normal share of planned budget (CMRP CMPR-10 p.21)
- Emergent Work [has_value:: > 45%] worst case (CMRP CMPR-10 p.21)
- Emergent Work [depends_on:: Work Request Specification Quality] high emergent work = improve technical specification (CMRP CMPR-10 p.21)
- Plant Staff Wages During Turnaround [part_of:: Turnaround Event Cost] CMRP view; differs from RBMM, see Maintenance Budget (CMRP CMPR-10 p.19)
- Major Task [is_a:: Turnaround Maintenance Work] needs engineering input; challenge every one (CMRP CMPR-10 p.25)
- Minor Task [is_a:: Turnaround Maintenance Work] specification only (CMRP CMPR-10 p.25)
- Bulk Work [is_a:: Turnaround Maintenance Work] many small items, often causes delay (CMRP CMPR-10 p.25-26)
- Project Work [depends_on:: Payback] also necessity and desirability; all work in a single plan (CMRP CMPR-10 p.23-24)
- In-house Turnaround Team [differs_from:: Outsourced Turnaround] capacity and competence vs claims and need for control team (CMRP CMPR-10 p.26-27)
- Initiation [step_of:: [[Turnaround Management]]] phase 1, may start 2+ years before event (CMRP CMPR-11 p.1)
- Preparation [step_of:: [[Turnaround Management]]] phase 2, 3-18 months (CMRP CMPR-11 p.3)
- Execution [step_of:: [[Turnaround Management]]] phase 3, typically 2-8 weeks (CMRP CMPR-11 p.3)
- Termination [step_of:: [[Turnaround Management]]] phase 4, typically 1-2 weeks (CMRP CMPR-11 p.3)
- Work List Freeze [step_of:: Preparation] after challenge and validation (CMRP CMPR-11 p.3)
- Contingency Analysis [part_of:: Preparation] likely faults, time, cost, impact on duration (CMRP CMPR-11 p.1)
- Shutdown [step_of:: Execution] sub-phase 1: remove inventory, decontaminate, cool, isolate (CMRP CMPR-11 p.2)
- Box Up [step_of:: Execution] sub-phase 5 of 8 (CMRP CMPR-11 p.2)
- Start Up [step_of:: Execution] sub-phase 7 of 8 (CMRP CMPR-11 p.2)
- Execution [has_value:: 8 sub-phases] shutdown, open up, inspect, install/overhaul/remove, box up, test, start up, clean up (CMRP CMPR-11 p.2)
- Single Point Responsibility [applies_to:: Execution] check previous step, do own part, hand over fast, report (CMRP CMPR-11 p.2)
- De-brief [part_of:: Termination] lessons learned (CMRP CMPR-11 p.3)
- Turnaround Work List [input_to:: Turnaround Cost Forecast] foundation of safety, quality, cost, logistics, duration (CMRP CMPR-11 p.3)
- Initiation 2+ Years [contradicts:: Initiation Period of Months] text p.1 vs figure p.3, slide inconsistency (CMRP CMPR-11 p.1, p.3)
- Turnaround Knowledge Integration [has_value:: 6 knowledge types] slide says five but lists six (CMRP CMPR-10 p.30)
- Slide Risk Definition [differs_from:: Risk] CMPR-10 p.25 probability only vs likelihood x consequence (CMPR-09 p.3, Criticality Assessment)
- [[Turnaround Management]] [related_to:: [[Maintenance KPIs]]] ISO KPI 21 duration, 22 time between turnarounds

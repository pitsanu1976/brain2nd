---
title: Maintenance Performance Improvement
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [mpm, maintenance-management, cost]
sources: [maintenance-profit-maker.md, reliability-based-maintenance-management.md]
confidence: medium
contested: true
---

# Maintenance Performance Improvement (การปรับปรุงสมรรถนะบำรุงรักษา)

บทที่ 12 ของ [[Maintenance Profit Maker Book]] ถือว่าเป็น "หัวใจ" ของเล่ม: การปรับปรุงสำเร็จขึ้นกับ (1) การยอมรับว่ามีปัญหา และ (2) การแยกแยะปัญหาเชิงซ้อนได้ถูก มากกว่าความรู้เทคนิคที่ซื้อหาได้ หาโจทย์ให้ถูกคือทำได้ครึ่งทาง แล้วกำจัดปัจจัยหลักก่อน ไล่ไปปัจจัยรองเท่าที่คุ้มค่า (MPM p.205-206) เนื้อหาถอดความจาก reading notes [[raw/maintenance-profit-maker]]

## 1. เป้าหมาย 2 ข้อ: OEE ขึ้น ฿ ลง (MPM p.206-207)

- เป้าหมาย = **เพิ่มผลผลิต (OEE)** และ **ลดต้นทุน (฿)** ควรทำเป็น **โครงการ** ที่ประเมินความคุ้มทุนได้ชัด ไม่ใช่งานปกติในงบค่าใช้จ่าย ยกเว้นกิจกรรมต้นทุนต่ำ เช่น performance analysis ที่ทำได้ทันที
- รูป 12.1 แบ่งกิจกรรมเป็นซีกงบค่าใช้จ่าย (Fault Recovery, Preventive-Proactive) กับซีกงบเงินทุน (Modification/Renewal, Maintenance Engineering) ซีกขวาคือกลุ่มที่ยก OEE และลด ฿ ดู [[Maintenance Business Models]]
- ลดต้นทุน = **Cost Side Management** เห็นผลเร็วแต่ลดได้ถึงระดับหนึ่ง; เพิ่มผลผลิต = **Revenue Side Management**; ได้ผลสูงสุดเมื่อทำทั้งสอง ปลายทางคือ Sustainable Performance
- ตัวอย่างความล้มเหลว: สั่งลดอะไหล่คงคลังด้วยการตัดจำหน่ายของไม่เคยใช้ ดัชนีดีขึ้นชั่วคราว แต่ไม่นานก็กลับมาสะสมอีก เพราะไม่ได้แก้ระบบบริหารงานบำรุงรักษา (MPM p.207)

### Efficiency vs Effectiveness (MPM p.208)

| | Efficiency (ประสิทธิภาพ) | Effectiveness (ประสิทธิผล) |
|---|---|---|
| มุ่งที่ | ค่าใช้จ่าย (Cost-Side) = ต้นทุนงานซ่อม | ผล/รายได้ (Revenue-Side) |
| วัดด้วย | Life Cycle Costs (LCC) | Plant OEE, Life Cycle Revenue / Life Cycle Profit (LCP) |

LCC ตามกรอบเดิมของ wiki อยู่ใน [[Asset Life Cycle]] และ OEE ใน [[Availability and OEE]]

## 2. กระบวนการ 6 ขั้น (MPM p.207)

| ขั้น | ชื่อ | สาระ | หน้า wiki |
|---|---|---|---|
| 1 | Audit (Maintenance Performance Analysis) | เชิงปริมาณ + เชิงคุณภาพ | [[Maintenance Performance Audit]] |
| 2 | Benchmarking | เทียบ Best in class / World Class ธุรกิจเดียวกัน หาช่องว่าง = เป้าสูงสุด | [[Maintenance KPIs]] |
| 3 | Benefits & Feasibility Analysis | ตั้งเป้าที่เป็นไปได้และคุ้มค่า คำนวณผลตอบแทน | [[Maintenance Business Case]] |
| 4 | Master Plan | พิจารณาปัจจัยหลัก 16 รายการร่วมกับ Business Strategy | [[Maintenance Master Plan]] |
| 5 | Action Plans & Schedule | ทำเป็นโครงการ มีเป้าและเวลา อาจข้ามปีงบประมาณ | - |
| 6 | Implement, Control, Evaluate, Adjust | ดำเนินการเป็นโครงการ ไม่ใช่งานปกติ เพราะเป็นการเปลี่ยนแปลงที่ต้องให้ทุกคนตื่นตัว | - |

## 3. ขั้นที่ 2: ดัชนีขับต้นทุน (รูป 12.2, MPM p.209)

| รายการต้นทุน | ดัชนีเปรียบเทียบ |
|---|---|
| ค่าใช้จ่ายคงที่ (ค่าส่วนกลาง, ทรัพย์สินบำรุงรักษา, เงินเดือนทางอ้อม/ทางตรง, OT, อะไหล่คงคลัง) | Maintenance Asset/Total Plant Asset; Direct/Indirect Head count; Over Time/Normal; Utilization Factor; Spare Part Inventory/Plant Asset; Store Management Indices |
| ค่าใช้จ่ายแปรผัน (อะไหล่ใช้, วัสดุ, เบิกคลัง, ซื้อตรง, จ้างเหมา, ซ่อมใหญ่) | Spare Part Turn Over rate; Spare Part Service rate; Contracts/Total In-house; Turnaround Time, Turnaround Cost/Plant Asset, Turnaround Frequency; Work Order Indices |
| รวมค่าใช้จ่ายซ่อมบำรุง | Maintenance Expenditure/Plant Asset; Maintenance Expenses/Unit Produced |
| + ความสูญเสีย OEE | OEE ระดับ plant/equipment; MTBF, MTTR, MWT; Capacity Factor |
| + ความสูญเสียทางอ้อมอื่น | (ระบุทั่วไป) |
| = ค่าใช้จ่ายทั้งสิ้น | Safety Indices |

### กับดักทางบัญชีเมื่อเทียบ benchmark (MPM p.209-210)

- ต้องเทียบ "สิ่งเดียวกัน" cost per unit ต้องรวมรายการเหมือนกัน
- **Capitalize vs Expense**: บางแห่งกำหนดให้ค่าซ่อม **เกิน 10,000 บาท** บันทึกเป็นทรัพย์สินแล้วตัดค่าเสื่อม ทำให้ค่าใช้จ่ายบำรุงรักษาต่ำกว่าจริง ตัวอย่าง ซ่อมมอเตอร์ใหญ่ 10 ล้านบาทถูกบันทึกเป็นทรัพย์สิน ตัดค่าเสื่อมปีนั้นเพียง 1 ล้าน ผู้เขียนแนะนำหลัก **อนุรักษ์นิยม** ให้ลงเป็นค่าใช้จ่าย; ถ้าดัชนีออกมาดีกว่า World Class ต้องตรวจว่าจริงหรือไม่
- Maintenance cost/Total asset **ต่ำเกินไป** = under maintenance (อายุเครื่องสั้นลงผิดปกติ) หรือเก็บค่าใช้จ่ายไม่ครบ
- **อะไหล่ราคา 1 บาท**: อะไหล่ที่มากับโครงการมักบันทึกราคา 1 บาท/รายการเพื่อให้มีในระบบเท่านั้น ต้องตรวจความครบและราคาจริง; อะไหล่ส่วนใหญ่เป็นทรัพย์สินหมุนเวียน (ไม่คิดค่าเสื่อม) แต่บางประเภทเป็นทรัพย์สินถาวร
- **Redundancy ทำให้ availability ดูดี**: Availability Factor 100% ต้องถามว่ารวม/ไม่รวมอะไร และมีอุปกรณ์สำรองมากจนมองไม่เห็นเครื่องหยุดหรือไม่ โรงงานที่สำรองมากแพงกว่าที่กำลังผลิตเท่ากัน ทำให้ Maintenance Expenditure/Plant Asset ต่ำลงอีก บางแห่งพบค่าใช้จ่ายจริงเป็น **2 เท่า** ดู [[Redundancy and Standby Systems]]
- OEE ต้องดูคู่กับ Planning Factor ให้ฐานเดียวกัน

## 4. ขั้นที่ 3: Benefits & Feasibility (MPM p.210-214)

### เมทริกซ์ 2x2 Improvement Task Priorities (รูป 12.3)

| | Feasibility ต่ำ | Feasibility สูง |
|---|---|---|
| **Benefit สูง** | (2) ทำต่อไป: คุ้มแต่โอกาส/จังหวะยังไม่มี | (1) **Highest Priority**: ไม่ต้องใช้เงิน (เปลี่ยนวิธีการ) หรือใช้เงินแต่ประเมินความคุ้มได้ชัด |
| **Benefit ต่ำ** | (4) ไม่ทำ: ไม่คุ้ม ไม่มีโอกาส หรือไม่มีความรู้ | (3) ทำต่อไป: อาจไม่คุ้มทันทีแต่คุ้มระยะยาว |

- เริ่มจากรายการต้นทุนที่น้ำหนักมากที่สุด ใน XYZ อะไหล่ (เบิกใช้ + ต้นทุนการเงินของสต็อก) = 53.3% / 60.3% / 71.8% ของค่าบำรุงรักษาปี 1998-2000 จึงเป็นโครงการ Benefit สูง Feasibility สูง (รูป 12.4, MPM p.212)
- ทิศทาง (รูป 12.5, MPM p.213-214): ยอม **เพิ่ม** ค่าใช้จ่ายคงที่บางส่วน (การบริหาร, CMMS, อบรม, PM และงานเชิงรุก, วิศวกรรมบำรุงรักษา, งานปรับปรุง) เพื่อ **ลด** อะไหล่คงคลัง ค่าใช้จ่ายแปรผัน และความสูญเสีย OEE รวมถึงยืดรอบซ่อมใหญ่ 3 -> 4 ปี; ค่าใช้จ่ายทั้งสิ้นต้องรวมความสูญเสีย OEE เทียบค่ามาตรฐาน เช่น ปิโตรเคมีชนิดหนึ่ง OEE เฉลี่ย 90% ถ้าวัดได้ 85% ด้อย 5% แปลงเป็นเงินได้

### ทางแก้รายรายการ (MPM p.214-223, สรุป)

- **ค่าส่วนกลาง**: ต่อรองได้ โดยเฉพาะเมื่อใช้ Activity Based Costing (จัดซื้อต่อรายการ, HR ต่อหัว, IT ต่อเครื่อง, พื้นที่แบบค่าเช่า) ดู [[Maintenance Cost Structure]]
- **ค่าแรง**: เป็นทรัพย์สินแฝงในงบดุล ค่าแรงคงที่ปีละ 10 ล้านบาทเสมือนทรัพย์สิน 200 ล้านบาทที่ไม่ลดค่าลงเอง ต้องวางกำลังพลตั้งแต่ผังองค์กร, ตั้งเป้า Utilization บนงานมาตรฐานและ work control system, กำหนด make-or-buy ตั้งแต่ต้น, ผังแบน; เมื่อขยายธุรกิจให้เพิ่ม Utilization ก่อนเพิ่มคน (MPM p.215-216) ดูข้อขัดแย้ง MPM-C5 หัวข้อ 7
- **อะไหล่**: เป้าลด 10-20% (> 20% ถ้าไม่เคยจัดการ), สัดส่วน 20% fast-moving / 60% optimizable / 20% insurance, แก้ต้นเหตุด้วย Failure Root Cause Analysis ของอะไหล่ต้นทุนสูงสุด 10 อันดับ ดู [[Spare Parts Management]], [[MRO Inventory Reduction Program]], [[Root Cause Analysis]]
- **จ้างเหมา**: ต่อรองเป็นก้อนใหญ่หลายปี ลดได้เริ่มที่ 5%/ปี; ถ้าลดไม่ได้มากให้ใช้สัญญาแบบแบ่งผลประโยชน์จาก OEE ดู [[MRO Purchasing and Contracting]]
- **ซ่อมใหญ่**: ดัชนี Mean Time Between Turnaround, Turnaround Time, Turnaround Cost/Plant Asset; ลดปริมาณงานด้วย RBI และ Reliability Engineering ดู [[Turnaround Management]]
- **Planner**: ช่าง 3 คน UF เนื้องาน 35% = 105%; เพิ่ม planner 1 คน ช่าง 3 x 55% = 165% = 1.57 เท่า ทั่วไปช่าง 20-30 คนต่อ planner 1 คน (MPM p.227) ดู [[Maintenance Planning and Scheduling]] (ข้อสังเกต: ฐานเทียบปนกัน ถ้านับหัว planner ด้วยจะดีขึ้นเพียงราว 1.18 เท่าต่อหัว, derived)

## 5. ความสูญเสีย OEE: สาเหตุ availability loss และทางแก้ (รูป 12.9, MPM p.223-227)

ขั้นตอนปรับปรุง OEE: วัด OEE ปัจจุบัน -> benchmark กับโรงงานประเภทเดียวกัน -> สืบหาเหตุของ Availability/Speed/Quality loss -> ประเมินความคุ้มทุนและเลือกตามความเร่งด่วน/เป็นไปได้ (MPM p.224) ธุรกิจราคาตามวัฏจักรต้องไม่พลาดช่วงราคาขึ้น และวางแผนซ่อมช่วงราคาขาลง

| หมวด | สาเหตุ | ทางแก้ |
|---|---|---|
| ระบบ | วัด Availability ไม่ได้/ไม่ถูก (MDT, MTBF, MWT); ไม่มีบันทึกการหยุดที่แม่นยำ; ไม่มีคู่มือ; ขั้นตอนส่งมอบ/แยกระบบ/ตรวจรับไม่ดี; ร่วมมือกับผลิตไม่พอ | audit ที่มาของตัวเลขให้ฐานเดียวกัน; เชื่อมระบบควบคุมการผลิตกับ CMMS/บัญชี; ทำคู่มือ; ผูกผลประโยชน์ร่วมที่ OEE; ลดข้อมูลซ้ำซ้อน (**Entry Once Basis**) |
| คน | ขาดความรู้ระบบผลิต/เครื่อง; ขาดความร่วมมือ | อบรมเทคนิคโดยเฉพาะช่วงก่อสร้างโรงงาน; เป้าร่วม OEE |
| ความปลอดภัย | การตรวจ/ควบคุมความปลอดภัย | เพิ่มผู้รับผิดชอบและระบบงาน |
| อะไหล่ | ไม่พร้อม ระดับต่ำไป รายการไม่เหมาะ จัดซื้อ/ผู้ขาย/การส่งไม่ดี | ปรับสมรรถนะคลัง ดัชนี Spare Part Availability Rate, Spare Part Logistic Time |
| งานวางแผน | ไม่มีทะเบียนเครื่อง ไม่มีประวัติซ่อม PM/เชิงรุกน้อย วางแผนล่วงหน้าไม่ได้ | เพิ่ม/ประเมิน CMMS (มีข้อมูลว่า CMMS ได้ผล **ไม่ถึง 25%** ของที่ตั้งใจ หนังสือไม่ระบุแหล่ง); ประชุมวางแผนร่วมเป็นประจำ; ลดรายงาน "เพื่อทราบ"; เพิ่ม ad-hoc reporting |
| เครื่องมือ/เทคโนโลยี | เครื่องมือไม่พอ ไม่มีงานมาตรฐาน | เพิ่มเครื่องมือ เครื่องมือวิเคราะห์ reliability ระบบมาตรฐาน |
| ตัวเครื่องจักร | ซับซ้อน ออกแบบไม่เหมาะ เข้าถึงยาก | ทบทวนการออกแบบติดตั้ง สภาพแวดล้อม 5ส |
| กลยุทธ์งานซ่อม | PM น้อย/มากไป งานซ่อมมาก เชิงรุกน้อย | ปรับ Work Control Indices |

## 6. กรณีศึกษา 1: การวินิจฉัยบริษัท XYZ (MPM p.230-236)

ข้อมูลจาก audit เชิงปริมาณ (รูป 12.11) และดัชนี (รูป 12.12) ปี 1998 / 1999 / 2000:

| ดัชนี | 1998 | 1999 | 2000 |
|---|---|---|---|
| Maintenance Expenses/Unit Produced (บาท/ตัน) | 640 | 920 | 966 |
| Maintenance Expenditure/Plant Asset | 2.91% | 3.53% | 4.65% |
| OEE | 89.13% | 80.45% | 79.42% |
| Spare Part Inventory/Plant Asset | 3.7% | 3.7% | 4.7% |
| Spare Part Turn Over rate | 20.4% | 11.4% | 10.8% |
| Spare Part Cost/Total Maintenance Cost | 53.3% | 60.3% | 71.8% |
| Utilization Factor | 50% | 50% | 50% |
| Man-Hr Rate ที่แท้จริง (Full Cost rate, บาท) | 1,197 | 1,299 | 1,506 |

การวินิจฉัย 10 ข้อ (MPM p.233-235) สรุป:
1-2. Maintenance Expenditure/Plant Asset และต่อหน่วยผลิต สูงกว่าที่รับรู้และเพิ่มขึ้น
3. OEE ลด เสียโอกาสกำไรขั้นต้น **161.84 ล้าน (1999)** และ **489.17 ล้าน (2000)** เทียบปี 1998; ลงทุน 489.17 ล้านเพื่อคง OEE ก็คืนทุนใน 1 ปี เป้า: เพิ่ม OEE อีก 10.6% ภายใน 2 ปี (79.42 + 10.6 ≈ 90.0%, derived)
4. ค่าอะไหล่เพิ่ม (ซื้อตรงพุ่ง 47.4 -> 259.5 ล้าน ขณะเบิกคลังลด) -> ใช้ Spare Part Optimization
5. อัตราค่าแรงจริงสูงมากเทียบผู้รับเหมา ตั้งเป้าลดค่าใช้จ่าย 5%
6-8. ค่าส่วนกลางไม่มีรายงานชัด (ทบทวน Budgeting & Control), ปรับการเชื่อม CMMS กับบัญชีหลัก, CMMS ยังรายงานดัชนีอะไหล่ไม่ชัด
9. เพิ่มสัดส่วน predictive maintenance
10. ธุรกิจวัฏจักร: การลงทุนที่ยืดรอบซ่อมใหญ่จาก 3 เป็น 4 ปีคุ้มได้ไม่ยาก
- สรุป: รายได้ผันตามราคาวัฏจักร ต้องเน้นด้านรายได้มากกว่าการลดค่าใช้จ่าย

วิธีแปลง OEE เป็นกำไร (รูป 12.13, ย้อนคำนวณ derived): กำไรขั้นต้นที่ OEE 100% = กำไรขั้นต้น / OEE; กำไรต่อ OEE 1% = ค่านั้น / 100; ความสูญเสีย = (OEE ฐาน − OEE ปีนั้น) x กำไรต่อ 1% สมมติฐานแฝงคือกำไรแปรผันเชิงเส้นกับ OEE

### ข้อผิดพลาดของหนังสือที่ตรวจพบ (derived)

| จุด | ที่พิมพ์ | ค่าที่ถูก (derived) |
|---|---|---|
| รูป 12.13 ปี 1999 กำไรขั้นต้นที่ OEE 100% / ต่อ 1% | 1,579 / 15.79 | 1,500/0.8045 = **1,864.5 / 18.65** (ค่านี้ให้ 161.84 ตรงกับหนังสือ) |
| รูป 12.13 ปี 1998 | 1,944 / 19.44 | 3,000/0.8913 = **3,365.9 / 33.66** |
| Personnel Cost/Total Maintenance Cost 1998 (รูป 12.12) | 22.1% | 68.1/320.2 = **21.3%** (ตรงกับรูป 12.4) |
| รูป 12.10 vs รูป 12.12 (ข้อมูล XYZ ชุดเดียวกัน) | รูป 12.10: Expenses/Unit 628/886/1,092, Turnover 20.4/47.5/60.6%, Spare cost/Total 55.4/62.5/74.3%, Turnaround 45/45/40 วัน, Full Man-Hr Rate 2,700.1/3,400.5/5,845.3 | ใช้ **รูป 12.12**: 640/920/966, 20.4/11.4/10.8%, 53.3/60.3/71.8%, 35 วัน, 1,197/1,299/1,506 (ตรวจกับข้อมูลรูป 12.11 แล้วถูก) |
| Man-Hr Rate เฉลี่ยและที่แท้จริง | 237.1 / 1,196.8 ฯลฯ | ย้อนคำนวณจากตารางไม่ได้ตรง (ไม่สามารถตรวจสอบได้) |
| คน-ชั่วโมงในตาราง XYZ | 116 x 1,968 = 228,288 | ใช้ 1,968 ชม./คน/ปี ต่างจาก 1,663.2 ชม. ที่หนังสือเสนอเอง (ความต่าง ไม่ใช่ contested) |

ข้อสังเกต: Spare Part Inventory/Plant Asset ปี 2000 = 4.7% เกินเกณฑ์ SPO ไม่เกิน 4% GPI ที่ผู้ใช้เลือกไว้ใน [[Inventory Turnover and GPI Benchmarks]] (ใช้ประกอบการตีความ ไม่ใช่ข้อขัดแย้งของแหล่ง)

แผนแม่บทที่เกี่ยวข้องและ Gantt 3 ปีของ XYZ อยู่ที่ [[Maintenance Master Plan]] หัวข้อ 6 ส่วนกรณีศึกษา 2 (บริษัทบำรุงรักษารวมศูนย์ 4 โรงงาน) อยู่ที่ [[Maintenance Business Models]]

## 7. ข้อขัดแย้ง MPM-C5: เป้า labour utilization

| มุมมอง | ข้อความ | แหล่ง |
|---|---|---|
| MPM | ตั้งเป้า **Utilization rate > 60%** (หมายถึงคนต่ำอย่างเหมาะสม มีมาตรฐานงาน และบันทึกชั่วโมงเชื่อถือได้); กรณีศึกษา 2 สมมติปรับ UF จาก **40% -> 70%** ทำให้ต้องการ 229 คนแทน 400 คน | MPM p.215, p.239 |
| RBMM | B5 Utilization **60% ถือว่าสูงแล้ว** เพราะต้องมีเวลาอบรม/กิจกรรมที่ไม่มี WO และห้ามเน้นดัชนีนี้อย่างเดียว | RBMM p.73-74 ใน [[Maintenance KPIs]] |

- ผู้แต่งชุดเดียวกันแต่ให้ระดับต่างกัน: 70% ของ MPM เกินระดับที่ RBMM ถือว่าสูง ยังไม่ resolve (`contested: true`) รอผู้ใช้ตัดสิน
- MPM เองก็เตือนว่า Utilization Factor อ่อนไหวและต้องสอบเทียบกับดัชนีอื่น (MPM p.203) ซึ่งใกล้กับข้อเตือนของ RBMM
- หมายเหตุ: ตัวอย่าง planner (MPM p.227) ใช้ "UF เนื้องาน" 35-55% ซึ่งใกล้แนวคิด wrench time มากกว่า B5 คำว่า Utilization Factor ในบทนี้จึงมีสองความหมาย (ดู [[Maintenance Planning and Scheduling]])

## เชื่อมโยงกับ compressor failure hierarchy

(การตีความของ wiki)
- หมวด "ระบบ" ในรูป 12.9 (วัด MDT/MTBF/MWT ไม่ได้) คือปัญหาเดียวกับการไม่มี failure record ที่เข้ารหัสตาม [[Failure Hierarchy]] สำหรับ [[Compressor]] หากไม่มี failure mode/mechanism ก็หา availability loss รายสาเหตุไม่ได้
- หลัก "แก้ที่ต้นเหตุการกินอะไหล่ด้วย RCA ของ top-10 cost" ใช้กับ maintainable item ของ compressor ได้ เช่น จัดลำดับด้วยต้นทุนอะไหล่แล้วเทียบกับ % failure rate ของ [[Failure Mode]] จาก [[OREDA]]

## ดูเพิ่ม

- [[Maintenance Performance Audit]]
- [[Maintenance Master Plan]]
- [[Availability and OEE]]
- [[Maintenance KPIs]]
- [[Maintenance Cost Structure]]
- [[Maintenance Business Case]]
- [[Maintenance Profit Maker Book]]

ดูเพิ่ม (หน้าจาก MPM ingest 2026-10-28): [[Life Cycle Cost and Life Cycle Profit]], [[Maintenance Financial Impact]]

## Triplets

- [[Maintenance Performance Improvement]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 12 (MPM p.205-242)
- [[Maintenance Performance Improvement]] [produces:: OEE Increase] goal 1 (MPM p.206)
- [[Maintenance Performance Improvement]] [produces:: Cost Reduction] goal 2 (MPM p.206)
- Cost Side Management [differs_from:: Revenue Side Management] cost side fast but limited; best to do both (MPM p.207)
- Efficiency [measures:: Life Cycle Cost] cost-side (MPM p.208)
- Effectiveness [measures:: OEE] revenue-side, also Life Cycle Profit (MPM p.208)
- [[Maintenance Performance Audit]] [step_of:: [[Maintenance Performance Improvement]]] step 1 (MPM p.207)
- Benchmarking [step_of:: [[Maintenance Performance Improvement]]] step 2, best in class same business (MPM p.207)
- Benefits and Feasibility Analysis [step_of:: [[Maintenance Performance Improvement]]] step 3 (MPM p.207)
- [[Maintenance Master Plan]] [step_of:: [[Maintenance Performance Improvement]]] step 4, 16 factors with business strategy (MPM p.207)
- Action Plan [step_of:: [[Maintenance Performance Improvement]]] step 5, as projects (MPM p.207, p.227)
- Implement Control Evaluate [step_of:: [[Maintenance Performance Improvement]]] step 6, as project not routine (MPM p.227)
- Improvement Task Priorities [has_category:: Highest Priority] high benefit, high feasibility (Fig 12.3, MPM p.210)
- Improvement Task Priorities [has_category:: Do Not Do] low benefit, low feasibility (Fig 12.3, MPM p.210)
- Spare Part Cost [has_value:: 53.3% / 60.3% / 71.8%] of XYZ maintenance cost 1998-2000 (Fig 12.4, MPM p.212)
- Spare Part Project [has_category:: Highest Priority] XYZ example (MPM p.212)
- Repair Capitalization [contributes_to:: Understated Maintenance Cost] repairs > 10,000 baht booked as assets (MPM p.209)
- Repair Capitalization [resolved_by:: Conservative Expensing] author recommends expensing (MPM p.209)
- One Baht Spare Parts [contributes_to:: Understated Spare Inventory] project spares booked at 1 baht per item (MPM p.210)
- Redundancy [contributes_to:: Inflated Availability] hides stops; real cost found up to 2 times (MPM p.210)
- Redundancy [related_to:: [[Redundancy and Standby Systems]]]
- Maintenance Cost Drivers [uses:: [[Maintenance KPIs]]] cost line to index map (Fig 12.2, MPM p.209)
- Availability Loss [has_cause:: No Accurate Downtime Recording] system category (Fig 12.9, MPM p.224-227)
- Availability Loss [has_cause:: Spare Part Unavailability] spares category (Fig 12.9)
- Availability Loss [has_cause:: No Repair History] planning category (Fig 12.9)
- Availability Loss [resolved_by:: Entry Once Basis] reduce duplicate data (Fig 12.9)
- Availability Loss [resolved_by:: Joint OEE Target] production and maintenance share benefit (Fig 12.9)
- [[CMMS]] [has_value:: < 25%] results achieved vs intended, source not given (MPM p.226) [confidence:: low]
- Planner Effect [has_value:: 1.57 times] 3 x 55% vs 3 x 35% work content (MPM p.227)
- Planner Effect [has_value:: 1.18 times per head] counting planner, derived [confidence:: low]
- XYZ OEE [has_value:: 89.13% / 80.45% / 79.42%] 1998-2000 (Fig 12.12, MPM p.232)
- XYZ Lost Gross Profit [has_value:: 161.84 / 489.17 million baht] 1999 / 2000 vs 1998 OEE (MPM p.234)
- Lost Gross Profit From OEE [has_formula:: (OEE base - OEE year) x Gross Profit / OEE / 100] derived from Fig 12.13
- XYZ Maintenance Cost per Ton [has_value:: 640 / 920 / 966 baht] 1998-2000 (Fig 12.12)
- XYZ Spare Turnover [has_value:: 20.4% / 11.4% / 10.8%] issues from store / stock (Fig 12.12)
- XYZ Fig 12.10 [contradicts:: XYZ Fig 12.12] same company data differ; Fig 12.12 verified correct (derived)
- XYZ Fig 12.13 1999 [has_value:: 1,864.5 / 18.65] derived; book prints 1,579 / 15.79
- XYZ Fig 12.13 1999 Printed [contradicts:: XYZ Fig 12.13 1999] book typo, final 161.84 correct
- XYZ Personnel Cost Share 1998 [has_value:: 21.3%] derived; Fig 12.12 prints 22.1%
- XYZ Target [has_value:: OEE +10.6% in 2 years] to about 90% (MPM p.234)
- Turnaround Interval Extension [has_value:: 3 to 4 years] worthwhile for cyclical business (MPM p.235)
- Labour Utilization Target [has_value:: > 60%] MPM target; case 2 assumes 40% to 70% (MPM p.215, p.239) [contested:: true]
- Labour Utilization Target [has_value:: 60% already high] RBMM, do not chase alone (RBMM p.73-74) [contested:: true]
- MPM Utilization Target [contradicts:: RBMM Utilization Guidance] MPM-C5 [contested:: true]
- [[Root Cause Analysis]] [applies_to:: Top 10 Spare Part Cost Items] reduce spare consumption behaviour (MPM p.219)

---
title: Maintenance Budget
created: 2026-10-20
updated: 2026-10-22
type: concept
tags: [budget, cost, maintenance-management, kpi, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Maintenance Budget (Maintenance Performance Budgeting)

**Maintenance Budget** ตาม RBMM คือการตั้งงบบำรุงรักษาอย่างมีเหตุผลแบบ Top Down + Bottom Up โดยหลักคิดคือ "คุมงานได้ก่อน จึงคุมเงินได้" (RBMM p.274) งบแบ่งเป็นงบลงทุนกับงบทำการ (Fixed Cost + Materials) หักสำรอง 2 ก้อน (Provision for Losses และ Provision for Costs) เพื่อได้ Net Budget แล้วใช้ [[Maintenance Strategic Report]] ปรับงบเป็นวงจร หน้านี้สรุปกรอบวิธีและตัวอย่างตัวเลขของหนังสือ (บทที่ 10) ส่วนโครงสร้างต้นทุนอยู่ที่ [[Maintenance Cost Structure]]

ตัวเลขทั้งหมดในหน้านี้เป็นตัวอย่างสมมติของหนังสือ (หน่วยบาท) ไม่ใช่ข้อมูล Valeura หรือ OREDA ค่าที่คำนวณซ้ำโดย wiki ติดป้าย derived

## 1. เป้าหมายของงบ 2 สถานการณ์ (RBMM p.274)

| สถานการณ์ | เป้างบ | เงื่อนไข |
|---|---|---|
| ขาลง / สินค้า Commodity | Maintenance Cost/Unit | Availability สูง หยุดซ่อมนอกแผนให้สั้น |
| ขาขึ้น / สินค้าพิเศษ | Zero Down Time @ Minimum Cost | Reliability สูง หยุดเฉพาะตามแผน |

Zero Down Time ต้องมีเป้า Minimum Cost กำกับเสมอ (RBMM p.316)

## 2. ประเภทของงบ (RBMM p.276-279)

- **Capital Expenses** — ทรัพย์สินถาวรสำหรับงานบำรุง (โรงซ่อม เครื่องมือ คอมพิวเตอร์) ตัดเป็นค่าเสื่อมราคา ไม่ตัดทีเดียว
  - ลงทุนเพิ่มสมรรถนะเครื่อง (Improvement Maintenance) ค่าเสื่อมเป็นต้นทุนผลิต ไม่ใช่ต้นทุนบำรุงรักษา (RBMM p.277-278)
  - อะไหล่คลังเป็นทรัพย์สินหมุนเวียน ค่าครอบครองอยู่ในความรับผิดชอบฝ่ายบำรุงรักษา
  - ค่า Plant Turnaround ทุก 3-4 ปี กระจายเป็นรายปี (เช่น 3 ปีหาร 3) เฉพาะ Materials และค่าจ้างเหมา ไม่รวมค่าแรงภายใน
- **Operating Expenses Budget** — Fixed Cost (Man-Hrs) + ค่าใช้จ่ายแปรผัน (Materials: Stock Parts, Direct Purchase Parts, Outsource) ดู [[Maintenance Cost Structure]]

## 3. สูตรลำดับการคำนวณงบสุทธิ (RBMM p.291-294)

```
เป้าผลิตสุทธิ (units) = Planned Production x Budget OEE
เป้าต้นทุนไม่รวมซ่อมใหญ่ต่อหน่วย = เป้า Maintenance Cost/Unit รวมซ่อมใหญ่ - (ซ่อมใหญ่ตัดจ่ายต่อปี / เป้าผลิตสุทธิ)
Gross Budget (ไม่รวมซ่อมใหญ่) = เป้าต่อหน่วยไม่รวมซ่อมใหญ่ x เป้าผลิตสุทธิ
สำรองรวม = Gross x X% / (1 + X%)          (X% = สำรอง % ของต้นทุนสุทธิ)
  - Provision for Losses  = Y% ของสำรองรวม
  - Provision for Costs   = (1 - Y%) ของสำรองรวม
Net Maintenance Budget = Gross - สำรองรวม
Materials = Net Budget - Full Fixed Cost
```

OEE ในสูตรนี้ดู [[Availability and OEE]]

### ตัวอย่าง Top Down 3 Process (RBMM รูป 10.14 p.293)

| รายการ | Process 1 | Process 2 | Process 3 | Total |
|---|---|---|---|---|
| Planned Production (units) | 400,000 | 500,000 | 600,000 | |
| Budget OEE | 95% | 95% | 95% | |
| เป้าผลิตสุทธิ (units) | 380,000 | 475,000 | 570,000 | |
| ซ่อมใหญ่ตัดจ่ายต่อปี | 20,000,000 | 20,000,000 | 20,000,000 | 60,000,000 |
| เป้ารวมซ่อมใหญ่ต่อหน่วย | 200.00 | 200.00 | 200.00 | |
| เป้าไม่รวมซ่อมใหญ่ต่อหน่วย | 147.37 | 157.89 | 164.91 | |
| Gross Budget | 56,000,000 | 75,000,000 | 94,000,000 | 225,000,000 |
| สำรองรวม (10%) | 5,090,909 | 6,818,182 | 8,545,455 | 20,454,545 |
| Provision for Losses (80% ของสำรอง) | 4,072,727 | 5,454,545 | 6,836,364 | 16,363,636 |
| Provision for Costs (20% ของสำรอง) | 1,018,182 | 1,363,636 | 1,709,091 | 4,090,909 |
| Net Maintenance Budget | 50,909,091 | 68,181,818 | 85,454,545 | 204,545,455 |
| Net Cost/Unit | 133.97 | 143.54 | 149.92 | |

ตรวจ (derived): 225,000,000 x 0.10 / 1.10 = 20,454,545 และ 225,000,000 - 20,454,545 = 204,545,455 ตรงกับหนังสือ

หมายเหตุหนังสือ: ตาราง E (RBMM p.310) เขียน Provision for Costs เป็น 2.00% และ Provision for Losses เป็น 8.00% ซึ่งเป็น % ของ Net Budget (4,090,909 / 204,545,455 = 2.0% derived) ขณะที่รูป 10.14 เขียนเป็น 20%/80% ของสำรองรวม สองแบบเป็นเรื่องเดียวกัน

Provision for Losses แบ่งต่อเป็นจากงานตามแผน 20% และงานนอกแผน 80% (Total 3,272,727 และ 13,090,909) (RBMM p.293)

## 4. ลำดับ 5 ขั้นของวงจรจัดตั้งงบ (RBMM p.290)

1. Top Down Overall Targets (ปริมาณผลิต, Maintenance Cost/Unit, สำรอง)
2. Full Fixed Costs และ Total Material Costs
3. Man-Hrs Utilization และ Rate (Utilization Target, Planned/Unplanned Man-Hr Ratio)
4. Planned, Unplanned และ Total Full Costs
5. Unit Cost Distribution และรายละเอียดต่อ Asset (Equipment -> System -> Process)

จากนั้นทำ Budget Consolidation แล้วเข้า Budget Correction Loop (RBMM p.285)

### ตัวอย่างขั้น 2-4 (RBMM p.295-299)

| รายการ | ค่า |
|---|---|
| Full Fixed Cost รวม (Personnel 20.0M + Operating 2.4M + Asset 23.0M + Allocation 0.5M) | 45,900,000 |
| Materials = Net - Fixed | 158,645,455 |
| Direct Persons x วันทำงาน x ชม./วัน | 40 x 220 x 8 = 70,400 Man-Hrs |
| Utilization Rate 60% | 42,240 Man-Hrs |
| Full Fixed Cost Rate | 45,900,000 / 42,240 ประมาณ 1,087 บาท/Man-Hr |
| Planned/Unplanned Ratio (Man-Hrs) R = 2.0 | Planned 28,160 / Unplanned 14,080 Man-Hrs |
| Planned Maintenance Cost = Net x R/(R+1) | 136,363,636 |
| Unplanned Maintenance Cost = Net - Planned | 68,181,818 |
| Planned Direct Purchase Parts / Outsource | 79,000,000 / 26,763,636 |
| Unplanned Stock Parts | 52,881,818 |

เป้าที่ตั้งเป็น 0 โดยตั้งใจ (RBMM p.289, 298, 301): Stock Parts ของงานตามแผน, Direct Purchase ของงานนอกแผน (ยกเว้น Blanket Order), Outsource ของงานนอกแผน

ตัวเลขช่วงแนะนำของหนังสือ (RBMM p.295): อะไหล่คลัง 1-3% ของราคาเครื่อง, ค่ามีทรัพย์สินพร้อมใช้ 15-20% ของราคาเครื่อง, ค่าครอบครองอะไหล่ 15-25% ของมูลค่าอะไหล่ (ตัวอย่างใช้ 3%, 10%, 15%)

## 5. Budget Proficiency: Cost Control กับ Loss Control (RBMM p.286-288, 309-312)

| ด้าน | ตัวชี้ | ตรวจกับ |
|---|---|---|
| Cost Control | Variance ค่าใช้จ่าย (Fixed + Materials) | Provision for Costs |
| Loss Control | Losses due to Maintenance | Provision for Losses |

ตัวอย่างผลจริง (RBMM รูป 10.27-10.28 p.310-312): Actual Gross 217,670,500 = Actual Net 210,620,500 + Actual Losses 7,050,000

| รายการ | งบสำรอง | จริง |
|---|---|---|
| Cost Variance | 4,090,909 (2.0%) | 6,075,045 (2.97%) |
| Losses | 16,363,636 (8.0%) | 7,050,000 (3.45%) |
| รวมเทียบ Net Budget | 10% | 6.42% (13,125,045) |

ตีความ: 2.97% + 3.45% = 6.42% (derived) ยังไม่เกินสำรองรวม 10% แต่ Cost Variance เกินสำรองค่าใช้จ่ายของตัวเอง และมาจาก Materials ทุก Process (Variance Fixed Cost 2,820,000; Materials 3,255,045) (RBMM p.311) สำรองคือเพดานความคลาดเคลื่อน ไม่ใช่ที่สบายใจ ควรตั้งเป้าให้ลดลงจากปีก่อน

หนังสือพิมพ์ไม่สอดคล้องกัน: บท 3 (Fig 3.19 E15) แสดง Variance Gross รวม (7,329,500) หรือ -3.58% (= 217,670,500 - 225,000,000, derived) แต่บท 10 (RBMM p.310) แสดง 13,125,045 / 6.42% (= 217,670,500 - 204,545,455, derived เทียบกับ Net Budget) และ Variance รายโปรเซส P1 6,242,909 ตรงกับฐาน Net แปลว่าบท 3 ผสมฐานเปรียบเทียบ ใช้ค่าบท 10 (เทียบ Net) เป็นหลัก เป็นปัญหาภายในหนังสือ ไม่ใช่ conflict กับข้อมูลเดิมใน wiki

## 6. งบตามระดับ Criticality: Zero Breakdown @ Minimum Cost (RBMM p.315-319)

| กลุ่ม | กลยุทธ์ | Scheduled PM | อะไหล่และ Confidence |
|---|---|---|---|
| A (High) | Zero Breakdown | 100% RCM Tasks, Failure Finding เข้ม, ปรับปรุง Reliability | Service Level 100%, Stock-out 0%, Confidence มากกว่า 95% |
| B (Medium) | Optimum | PM Optimization ตัด PM ที่ไร้ผล | Confidence 90%, Service Factor 100% |
| C (Low) | Minimum / Run to Failure | ตัด PM ที่ไม่จำเป็น RTF | Confidence 80-90% |

สำหรับกลุ่ม A งบลงทุนปรับปรุง (Modification, Improvement Maintenance) ตั้งเมื่อ Scheduled PM แก้ไม่ได้ และอาจลดความวิกฤติด้วย [[Redundancy and Standby Systems]] โดยตรวจ System Reliability ด้วย simulation ([[Monte Carlo Maintenance Simulation]]) เพราะไม่มี 100% (RBMM p.318) หนังสือสรุปว่าถ้างานตามแผนเกิน 80-85% งบจะเป็นจริงได้ (RBMM p.320)

## 7. Budget Consolidation และ Correction Loop (RBMM p.303-306)

- รวมงบจาก Equipment -> Process/Area -> ฝ่าย -> โรงงาน โดยระดับสูงกำหนด Guideline
- ปัญหา: ทุกหน่วยเผื่อสำรองงานนอกแผนด้วย Constant Failure Rate ทำให้งบรวมบวม
- แก้: คำนวณเชิงวิทยาศาสตร์ทุกหน่วย, ตั้งสำรองตามกรอบ Top Down, หรือตั้ง **งบกองกลาง** ขนาดสำรองให้ได้ Confidence Level เช่น 95% จากสถิติเบิกนอกแผนย้อนหลัง
- Correction Loop: ทบทวน [[Maintenance Strategic Report]] -> เลือก Process/Equipment ที่ค่าใช้จ่ายสูงสุด (Top 10/20 ที่ครอบคลุมงบ 80%) -> Failure Data Analysis และเลือก PM ใหม่ ([[RCM Reliability Centered Maintenance]]) -> ทบทวน Stock Max/Min ([[Spare Parts Management]]) -> อนุมัติ

### ดัชนีตัวอย่างจริงเทียบงบ (RBMM รูป 10.23 p.306-309)

| ดัชนี | จริง | งบ |
|---|---|---|
| Maintenance Cost / Asset Replacement Value | 5.44% | 5.63% |
| Full Fixed Cost Rate | 1,193 | 1,087 |
| Utilization Factor | 58.0% | 60.0% |
| Total Man-Hrs | 40,832 | 42,240 |
| Spare Inventory / Asset | 2.50% | 3.00% |
| Service Factor | 97.10% | 99.00% |
| Stock-out Rate | 2.50% | 1.00% |

หมายเหตุ: ต้นทุนต่อหน่วยจริง P1 152.00 เทียบงบ 147.37 (variance 4.63) P2 151.00 เทียบ 157.89 และ P3 153.50 เทียบ 164.91 (RBMM รูป 10.25 p.306-309) ค่า Variance ที่เป็นวงเล็บในหนังสือหมายถึงจริงต่ำกว่างบ

## เชื่อมโยงกับ compressor failure hierarchy

หนังสือไม่มีเนื้อหาตรงเกี่ยวกับ [[OREDA]] หรือ [[ISO 14224]] ความเชื่อมทางอ้อม:
- งบ Unplanned และอะไหล่ของ Criticality A ต้องคิด "ทุก Failure Mode" ด้วยสถิติ (RBMM p.317) ตรงกับตาราง [[Failure Mode]] ของ compressor เช่น AIR, SER, LOO ที่เป็นแหล่งจำนวนครั้งเกิดโดยประมาณ
- ลำดับ Asset Equipment -> System -> Process (RBMM p.286) คล้าย hierarchy ระดับ [[Maintainable Item]] ใน ISO 14224 ใช้ผูกต้นทุนต่ออุปกรณ์
- ตัวเลข OREDA เป็น failure rate ทั่วไป ใช้เป็นข้อมูลตั้งต้นของงาน CM-Unplanned ได้เฉพาะเมื่อไม่มีสถิติของโรงงานเอง (ความรู้เสริม ไม่ใช่ข้อความในหนังสือ)

## ดูเพิ่ม

- [[Maintenance Cost Structure]] — Fixed Cost, Materials, Full Fixed Cost Rate
- [[Maintenance Strategic Report]] — รายงานที่ใช้ปรับงบ
- [[Maintenance KPIs]]
- [[Criticality Assessment]]
- [[Spare Part Criticality and Risk]]
- [[Maintenance Business Models]]
- [[Reliability Based Maintenance Management Book]]

## Triplets

- [[Maintenance Budget]] [alias_of:: Maintenance Performance Budgeting]
- [[Maintenance Budget]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 10
- [[Maintenance Budget]] [uses:: Top Down] combined with Bottom Up (RBMM p.274)
- [[Maintenance Budget]] [uses:: [[Maintenance Strategic Report]]] budget correction cycle
- [[Maintenance Budget]] [related_to:: [[Maintenance Cost Structure]]]
- Maintenance Cost/Unit [applies_to:: Downturn or Commodity Product] needs high Availability (RBMM p.274)
- Zero Down Time @ Minimum Cost [applies_to:: Upturn or Specialty Product] needs high Reliability (RBMM p.274)
- Zero Down Time [depends_on:: Minimum Cost] always paired (RBMM p.316)
- Capital Expenses [is_a:: Budget Type] depreciated, not expensed at once (RBMM p.276-279)
- Operating Expenses Budget [is_a:: Budget Type] (RBMM p.276-279)
- Full Fixed Cost [part_of:: Operating Expenses Budget] Man-Hrs
- Materials [part_of:: Operating Expenses Budget] Stock Parts, Direct Purchase Parts, Outsource
- Improvement Maintenance [has_category:: production cost] depreciation not maintenance cost (RBMM p.277-278)
- Plant Turnaround [has_formula:: turnaround cost / years in cycle] every 3-4 years, Materials and contract only, excludes internal labour (RBMM p.276-279)
- Net Production Target [has_formula:: Planned Production x Budget OEE] (RBMM p.291-294)
- Unit Cost Target Excl Overhaul [has_formula:: Maintenance Cost/Unit incl overhaul - (annual overhaul amortisation / Net Production Target)] (RBMM p.291-294)
- Gross Budget [has_formula:: Unit Cost Target Excl Overhaul x Net Production Target] (RBMM p.291-294)
- Total Provision [has_formula:: Gross x X% / (1 + X%)] X% = provision % of net cost (RBMM p.291-294)
- Provision for Losses [has_formula:: Y% of Total Provision] (RBMM p.291-294)
- Provision for Costs [has_formula:: (1 - Y%) of Total Provision] (RBMM p.291-294)
- Net Maintenance Budget [has_formula:: Gross - Total Provision] (RBMM p.291-294)
- Materials [has_formula:: Net Budget - Full Fixed Cost] (RBMM p.291-294)
- Provision for Losses [part_of:: Total Provision]
- Provision for Costs [part_of:: Total Provision]
- Net Production Target [depends_on:: [[Availability and OEE]]]
- Gross Budget [has_value:: 225,000,000 THB] 3 processes, book example (RBMM Fig 10.14 p.293)
- Total Provision [has_value:: 20,454,545 THB] 10% (RBMM Fig 10.14 p.293)
- Provision for Losses [has_value:: 16,363,636 THB] 80% of provision (RBMM Fig 10.14 p.293)
- Provision for Costs [has_value:: 4,090,909 THB] 20% of provision (RBMM Fig 10.14 p.293)
- Net Maintenance Budget [has_value:: 204,545,455 THB] (RBMM Fig 10.14 p.293)
- Provision for Costs [has_value:: 2.00%] of Net Budget, table E; same as 20% of provision (RBMM p.310)
- Provision for Losses [has_value:: 8.00%] of Net Budget, table E (RBMM p.310)
- Provision for Losses [has_value:: 20% planned / 80% unplanned] 3,272,727 / 13,090,909 THB (RBMM p.293)
- Top Down Overall Targets [step_of:: Budget Setting Cycle] step 1 (RBMM p.290)
- Full Fixed Costs and Total Material Costs [step_of:: Budget Setting Cycle] step 2 (RBMM p.290)
- Man-Hrs Utilization and Rate [step_of:: Budget Setting Cycle] step 3 (RBMM p.290)
- Planned, Unplanned and Total Full Costs [step_of:: Budget Setting Cycle] step 4 (RBMM p.290)
- Unit Cost Distribution [step_of:: Budget Setting Cycle] step 5, Equipment -> System -> Process (RBMM p.290)
- Budget Consolidation [step_of:: Budget Setting Cycle] after step 5, then Budget Correction Loop (RBMM p.285)
- Full Fixed Cost [has_value:: 45,900,000 THB] Personnel 20.0M + Operating 2.4M + Asset 23.0M + Allocation 0.5M (RBMM p.295-299)
- Materials [has_value:: 158,645,455 THB] Net - Fixed (RBMM p.295-299)
- Full Fixed Cost Rate [has_value:: about 1,087 THB/Man-Hr] 45,900,000 / 42,240 Man-Hrs, utilization 60% (RBMM p.295-299)
- Planned Maintenance Cost [has_formula:: Net x R/(R+1)] R = Planned/Unplanned Man-Hr Ratio (RBMM p.295-299)
- Planned Maintenance Cost [has_value:: 136,363,636 THB] R = 2.0 (RBMM p.295-299)
- Unplanned Maintenance Cost [has_value:: 68,181,818 THB] Net - Planned (RBMM p.295-299)
- Stock Parts [has_value:: 0] intentional target for planned work (RBMM p.289, 298, 301)
- Direct Purchase Parts [has_value:: 0] intentional target for unplanned work, except Blanket Order (RBMM p.289, 298, 301)
- Outsource [has_value:: 0] intentional target for unplanned work (RBMM p.289, 298, 301)
- Spare Inventory / Asset [has_value:: 1-3%] recommended of machine price, example 3% (RBMM p.295)
- Asset Readiness Cost [has_value:: 15-20%] recommended of machine price, example 10% (RBMM p.295)
- Holding Cost [has_value:: 15-25%] recommended of spare value, example 15% (RBMM p.295)
- Cost Control [uses:: Provision for Costs] variance of Fixed + Materials (RBMM p.286-288)
- Loss Control [uses:: Provision for Losses] Losses due to Maintenance (RBMM p.286-288)
- Cost Variance [has_value:: 6,075,045 THB (2.97%)] actual vs provision 4,090,909 (2.0%) (RBMM Fig 10.27-10.28 p.310-312)
- Losses due to Maintenance [has_value:: 7,050,000 THB (3.45%)] actual vs provision 16,363,636 (8.0%) (RBMM p.310-312)
- Total Budget Variance [has_value:: 13,125,045 THB (6.42%)] vs Net Budget, chapter 10 (RBMM p.310)
- Total Budget Variance [has_value:: 7,329,500 THB (-3.58%)] vs Gross Budget, chapter 3 Fig 3.19 E15 mixes bases; use chapter 10
- Criticality A [selects:: Zero Breakdown] 100% RCM tasks, Service Level 100%, Stock-out 0%, Confidence more than 95% (RBMM p.315-319)
- Criticality B [selects:: Optimum] PM Optimization, Confidence 90%, Service Factor 100% (RBMM p.315-319)
- Criticality C [selects:: Run to Failure] minimum PM, Confidence 80-90% (RBMM p.315-319)
- Criticality A [uses:: [[Redundancy and Standby Systems]]] reduce criticality, verify with [[Monte Carlo Maintenance Simulation]] (RBMM p.318)
- Planned Work Share [has_value:: more than 80-85%] budget becomes realistic (RBMM p.320)
- Central Contingency Budget [depends_on:: Confidence Level] e.g. 95% from unplanned issue history (RBMM p.303-306)
- Budget Correction Loop [uses:: [[RCM Reliability Centered Maintenance]]] Top 10/20 covering 80% of budget (RBMM p.303-306)
- Budget Correction Loop [uses:: [[Spare Parts Management]]] review Stock Max/Min (RBMM p.303-306)
- Maintenance Cost / Asset Replacement Value [has_value:: 5.44%] actual vs budget 5.63% (RBMM Fig 10.23 p.306-309)
- Full Fixed Cost Rate [has_value:: 1,193 THB/Man-Hr] actual vs budget 1,087 (RBMM Fig 10.23 p.306-309)
- Utilization Factor [has_value:: 58.0%] actual vs budget 60.0% (RBMM Fig 10.23 p.306-309)
- Service Factor [has_value:: 97.10%] actual vs budget 99.00% (RBMM Fig 10.23 p.306-309)
- Stock out Rate [has_value:: 2.50%] actual vs budget 1.00% (RBMM Fig 10.23 p.306-309)

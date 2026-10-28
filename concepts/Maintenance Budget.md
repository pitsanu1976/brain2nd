---
title: Maintenance Budget
created: 2026-10-20
updated: 2026-10-28
type: concept
tags: [budget, cost, maintenance-management, kpi, book, turnaround, cmrp, mpm]
sources: [reliability-based-maintenance-management.md, cmrp.md, maintenance-profit-maker.md]
confidence: medium
contested: true
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
  - ค่า Plant Turnaround ทุก 3-4 ปี กระจายเป็นรายปี (เช่น 3 ปีหาร 3) เฉพาะ Materials และค่าจ้างเหมา ไม่รวมค่าแรงภายใน (CMRP เห็นต่างเรื่องค่าแรงภายใน ดูหัวข้อ 8)
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

## 8. Contested: ค่าแรงพนักงานภายในในต้นทุน turnaround (เพิ่ม 2026-10-25)

สองแหล่งให้แนวทางต่างกันว่าค่าแรงพนักงานโรงงานช่วง turnaround เป็นต้นทุนของ turnaround หรือไม่

| แหล่ง | แนวทาง | เหตุผล |
|---|---|---|
| RBMM | ต้นทุน Plant Turnaround ที่กระจายรายปีนับ **เฉพาะ Materials และค่าจ้างเหมา ไม่รวมค่าแรงภายใน** (RBMM p.276-279) | ค่าแรงภายในอยู่ใน Full Fixed Cost ที่คิดผ่าน Man-Hr rate อยู่แล้ว (การตีความของ wiki จากโครงสร้าง [[Maintenance Cost Structure]]) |
| CMRP | ค่าแรงพนักงานโรงงานช่วง turnaround **ควรนับเป็นต้นทุนของ event** (CMRP CMPR-10 p.19) | ถ้าไม่นับ event จะดูถูกกว่าความจริง และต้นทุนผลิตช่วงนั้นดูสูงเกินจริง |

- มุมมองต่างกันที่จุดประสงค์: RBMM ทำ budget allocation (เลี่ยงนับ fixed cost ซ้ำ) ส่วน CMRP ต้องการ total cost visibility ของ event เพื่อตัดสินใจเชิงกลยุทธ์ เช่นการเลือกทำหรือกำจัด turnaround ดู [[Turnaround Management]]
- ผลต่อการใช้งาน: ถ้าใช้วิธี RBMM แล้วเทียบต้นทุน turnaround ระหว่างโรงงานหรือกับ contractor จะต่ำกว่าวิธี CMRP; ถ้าใช้วิธี CMRP ในงบ ต้องหัก Man-Hrs ช่วง turnaround ออกจาก Full Fixed Cost ปกติเพื่อไม่ให้นับซ้ำ (การตีความของ wiki)
- **ยังไม่ resolve** ผู้ใช้ต้องเลือกนโยบายบัญชีต้นทุน turnaround ขององค์กร ตั้ง `contested: true`
- ส่วนที่สอดคล้องกัน: ทั้งสองแหล่งยอมรับว่ากระจายต้นทุนหลายปีได้ แต่ CMRP ย้ำว่าการกระจายไม่ได้ลดผลกระทบรวม (CMRP CMPR-10 p.13) และควรนับกำไรที่เสียทั้งช่วงหยุดและช่วงหลัง start-up (CMRP CMPR-10 p.18-19)
- MPM (เพิ่ม 2026-10-28) ไม่พูดเรื่องค่าแรงภายในใน turnaround จึงไม่ตัดสินประเด็นนี้ แต่ในตาราง XYZ ค่าแรงภายในอยู่ใน "เงินเดือนค่าแรง" แยกจากซ่อมใหญ่เฉลี่ย 36.7 M฿/ปี (MPM p.107-108) ซึ่งใกล้แนว RBMM โดยนัย (การตีความ)

## 9. มุมมอง MPM: Maintenance Budgeting & Control (เพิ่ม 2026-10-28)

บทที่ 7 ของ [[Maintenance Profit Maker Book]] (ผู้เขียน 2 ใน 3 คนเดียวกับ RBMM) แบ่งการบริหารงบเป็น **Maintenance Budgeting** (จัดตั้งงบ) และ **Budget Spending Control** (คุมการใช้จ่าย) (MPM p.112) ตัวเลขเป็นตัวอย่างบริษัทสมมติ XYZ หน่วยล้านบาท (M฿)

### 9.1 รหัสงบ 4 มิติ (MPM p.112-115)

| มิติ | เนื้อหา |
|---|---|
| 1. โครงสร้างเครื่องจักรสายการผลิต | Hierarchical Plant / Productive Unit / Equipment Structure ใช้เป็น **Cost Collector** แต่ละโหนดผูก OEE, หน่วยรับผิดชอบ, กิจกรรม, จำนวนเงิน |
| 2. ผังความรับผิดชอบ (Responsibility Chart of Account) | ตามโครงสร้างองค์กร เช่น แผนกไฟฟ้า เครื่องกล เครื่องมือวัด = ผู้คุมค่าใช้จ่าย |
| 3. ประเภทค่าใช้จ่ายตามลักษณะงาน | 16 กิจกรรม 4 กลุ่ม แยก Expense vs Asset Account (ดู 9.2) |
| 4. ประเภททรัพยากร | แรงงาน, อะไหล่และวัสดุสิ้นเปลือง, ค่าจ้างเหมา, อื่น ๆ |

ถ้าแบ่งเครื่องตามหน้าที่ถูก (เช่น Boiler, Turbine, Generator) จะได้ดัชนีที่สอบเทียบกับเครื่องชนิดเดียวกันได้ เช่น ค่าซ่อม/ราคาเครื่อง, ค่าซ่อม/หน่วยสินค้า, OEE ระดับเครื่อง (MPM p.112, 115)

### 9.2 Expense vs Asset Account (MPM p.113-114)

| ประเภทบัญชี | ความหมาย | กลุ่มงาน |
|---|---|---|
| Expense Account | ใช้ทรัพยากรหมดในคราวเดียว ได้ประโยชน์คราวเดียว | Fault Recovery และ Preventive-Proactive **ยกเว้น Turnaround** |
| Asset Account (รอตัดจ่ายรายปี) | ใช้ครั้งเดียว ได้ประโยชน์ต่อเนื่อง ต้องประเมินความคุ้มตลอดอายุ | Modification Project, Maintenance Engineering/Improvement และ **Turnaround** |

- **Turnaround** ลงเป็นทรัพย์สิน ตัดจ่ายเฉลี่ยจนถึงซ่อมใหญ่ครั้งถัดไป เช่น ทุก 3 ปี ปีละ 1/3 (MPM p.114) สอดคล้องกับ RBMM หัวข้อ 2 (ตัวอย่าง XYZ: 110 M฿ / 3 = 36.7 M฿/ปี) ดู [[Turnaround Management]]
- ข้อสังเกต: ตาราง XYZ นับ "ซ่อมใหญ่เฉลี่ย/ปี" อยู่ใน "รวมค่าใช้จ่ายแปรผัน" ไม่ใช่หมวดตัดจ่าย — ตัวเลขถูก แต่การจัดหมวดไม่สอดคล้องกับ p.114 (derived)
- อะไหล่: เบิกใช้ = ค่าใช้จ่าย; สะสมในคลัง = ทรัพย์สินหมุนเวียน; อะไหล่ใช้ในงวด = คงคลังต้นงวด + ซื้อเพิ่ม - คงคลังปลายงวด (MPM p.114)

### 9.3 Reactive vs Proactive Value Oriented Budgeting (MPM p.115-117)

| แบบ | ลักษณะ |
|---|---|
| Reactive Budgeting | งบปีหน้า = ค่าใช้จ่ายปีที่แล้วบวกเพิ่ม ไม่มีโจทย์สร้างสรรค์; อาการเด่น: งบลงทุนต่ำมากเทียบงบค่าใช้จ่าย |
| Proactive Value Oriented Budgeting | ใช้หลัก Profit Center เป้าคือต้นทุนบำรุงรักษาต่อหน่วยสินค้าต่ำสุด = **B/OEE ต่ำสุด** (Budget / OEE) |

- เป้าอีกทางคือค่าซ่อม / Replacement Value ซึ่งง่ายกว่าเพราะค่อนข้างคงที่ แต่สุดท้ายคือต้นทุน/หน่วยเหมือนกัน (MPM p.117, 125-126)
- "Creative COST-PLUS": ตั้งเป้าเสมือนทีมบำรุงรักษาเป็นผู้รับเหมา แต่ผูกกับดัชนี OEE และค่าใช้จ่าย พร้อมผลตอบแทนจูงใจและบทปรับทั้งสองทาง (MPM p.125-126) ต่างจาก Cost Plus ที่วิจารณ์ใน [[Maintenance Outsourcing]]

```
Target Production = Capacity x Planning Factor x OEE     (MPM p.125, 128)
```

สอดคล้องกับ "เป้าผลิตสุทธิ = Planned Production x Budget OEE" ของ RBMM หัวข้อ 3 (MPM แยก Capacity x Planning Factor = Planned Production)

### 9.4 งบลงทุน (MPM p.117-121)

ปัจจัยหลักที่ผลักงบ 3 ด้าน: งบลงทุน, การผลิต, งบทำการ (MPM p.117-118) รายการงบลงทุน:
1. **Maintenance Performance Audits** — หา Room for improvement เทียบ best/world class แบ่ง quartile (ขั้นสำคัญที่สุด)
2. **โครงการปรับปรุงระบบบริหาร (CMMS)** — กวดขันวางแผน ติดตามงาน และวัด Utilization Factor ที่กำหนด Full Fix Cost Rate ซึ่งใช้ตัดสินจ้างเหมา; ผู้เขียนอ้างว่า CMMS ที่ใช้งานเต็มที่ไม่ถึง 25% (ไม่ระบุแหล่ง) ดู [[CMMS]]
3. **Spare Part Stock** — ลดคงคลัง เพิ่ม turnover เลือกรายการถูก เพิ่ม OEE ดู [[Spare Parts Management]]
4. **ทรัพย์สินใช้งานบำรุงรักษา** — Reliability System, Predictive Maintenance Tools, ระบบวัด OEE
5. **Turnaround** — ทุก 3, 4 หรือ 5 ปี
6. **Modification Projects** — energy efficiency และพฤติกรรมการเสียจากออกแบบ/ติดตั้ง อาจจ้างแบบแบ่งผลประโยชน์
7. **ระบบเก็บ/รายงานค่าใช้จ่าย** — Single Entry System กระทบยอดได้ทุกทาง; ถ้าไม่ใช้ ERP ทำ interface ระหว่างระบบย่อย ปัจจัยสำเร็จคือวินัยมากกว่าขนาด/ราคา

### 9.5 งบทำการ: Fixed vs Variable (MPM p.122-124)

- **ส่วนคงที่** (ไม่นับค่าเสื่อม ค่าบริหาร) = PM ที่กำหนดได้ทั้งปีจากฐานข้อมูล PM -> แผนอะไหล่ กำลังคน (M-H) เครื่องมือ (U-H) รายปี; เป้าคือ Optimization
- **ส่วนแปรผัน** = งานซ่อมที่ยังเกิด ประมาณได้จากปริมาณ PM (intervention) และคุณภาพ PM ("Do The Right Thing" + "Do The Thing Right"); ดัชนี MTBF, MTTR, PM/CM Ratio
- **PM/CM Ratio ควรอยู่ที่ 2.0 ฐานชั่วโมง-คน** แต่ค่าใช้จ่ายงานซ่อมสูงกว่า PM มากกว่า 2 เท่า เพราะอะไหล่และความสูญเสียทางอ้อม (MPM p.124) สอดคล้องกับตัวอย่าง R = 2.0 ของ RBMM หัวข้อ 4

### 9.6 ตารางค่าใช้จ่าย-ดัชนี-การตั้งงบ (MPM p.125)

| รายการค่าใช้จ่าย | ดัชนีอ้างอิง | ตั้งงบเพื่อปรับดัชนี |
|---|---|---|
| ค่าคงที่ (ค่าบริหารส่วนกลาง, ทรัพย์สินบำรุงรักษา, เงินเดือนค่าแรง, อะไหล่คงคลัง) | Maintenance Asset/Total Plant Asset; Direct/Indirect Head count; Over Time/Normal; Utilisation Factor; Spare Part Inventory/Plant asset; Store Management Indices | ซื้อ/ขายทรัพย์สิน, จัดองค์กร, งบปรับปรุงงานวางแผน, เพิ่ม/ลดคน, โครงการปรับคลังอะไหล่ |
| ค่าแปรผัน (อะไหล่ใช้, เบิกคลัง, ซื้อตรง, จ้างเหมา, ซ่อมใหญ่) | Spare Part Turn Over rate; Service rate; Contracts/Total In-house; Turnaround Time, Cost/Plant Asset, Frequency; Work Order Indices | ลด/ปรับคลังอะไหล่, งบงานเชิงรุก, งบปรับ CMMS, ปรับสัดส่วนงานกลุ่ม 1 และ 2 |
| ค่าใช้จ่ายซ่อมบำรุงทั้งสิ้น | Maintenance Expenditure/Plant Asset; Maintenance Expenses/Unit Produced | งบฝึกอบรม, งบวางระบบบัญชี |
| ความสูญเสียจาก OEE | OEE Plant/Equipment; MTBF, MTTR, MWT; Planning Factor | งบปรับระบบวัด OEE |
| ความสูญเสียทางอ้อมอื่น ๆ | Safety Indices | งบปรับระบบวัด |

ดัชนีเหล่านี้ดูเพิ่มที่ [[Maintenance KPIs]]

### 9.7 ข้อมูลที่ต้องใช้ 10 ข้อ (MPM p.126-127)

1. ผังองค์กรที่อ้างอิงเป็นศูนย์ค่าใช้จ่ายได้ 2. โครงสร้างบัญชีที่รองรับ 3. งบดุล/งบกำไรขาดทุนของบริษัท 4. แผนการผลิต (= แผนใช้เครื่อง) 5. รายงานค่าใช้จ่ายแยก 16 งานต่อเครื่องปีที่ผ่านมา 6. Standard jobs (ขนาด เวลา ทรัพยากร) 7. รายงาน OEE ปีที่ผ่านมา 8. รายงาน energy efficiency 9. ดัชนีบำรุงรักษาของระบบสำคัญ 10. เป้าต้นทุนต่อหน่วย/OEE ของปีหน้า

### 9.8 หน้าที่ผู้จัดการบริหารงานบำรุงรักษา 5 ข้อ (MPM p.127)

1. แปลงเป้าร่วมของบริษัทเป็นดัชนี แล้วทำแผนและงบ
2. รวมงบค่าคงที่ที่จัดสรรจากส่วนกลางกับของหน่วยตน แล้วจัดสรรต่อให้หน่วยย่อย
3. รับและจัดสรรค่าทางอ้อมจากงบดุล เช่น ต้นทุนการเงินอะไหล่คงคลัง ค่าบริหารคลัง ค่าเสื่อมเครื่องมือ
4. กระจายเป้า หน้าที่ และผลประโยชน์ลงถึงระดับเครื่อง
5. จัดทำ ทบทวน อนุมัติงบที่มีแผนปฏิบัติการรองรับ และควบคุมการดำเนินงาน

### 9.9 ตัวอย่าง XYZ ปี 2000 แบบ Result Oriented (MPM p.127-131)

| ขั้น | เนื้อหา | ตัวเลข |
|---|---|---|
| 1 | แผนผลิต = Planning Factor x Capacity x OEE | Planning Factor จากฝ่ายผลิต |
| 2 | เป้าประสิทธิภาพ: ค่าบำรุงรักษาต่อหน่วย | 511.8 M฿ / 530,000 ตัน = **965.7 บาท/ตัน** |
| 3 | เป้าประสิทธิผล: OEE (แนะนำเพิ่มไม่เกิน 1-2%) | OEE 79.4%; กำไรขั้นต้น 4,000 M฿; +1% OEE = +50.37 M฿ |
| 4 | เป้าค่าใช้จ่าย (แยกรายการ) | ดูตารางด้านล่าง |
| 5 | Full Cost Rate | 148.2 M฿ / (196,800 x 50% = 98,400 ชม.) = 1,506.4 บาท/ชม.-คน |
| 6 | สัดส่วนงานที่มีผลต่อ OEE | Reactive 39% / Preventive-Predictive 46% / Modification 10% / Maint. Engineering 5% ของ 98,400 ชม. |

ขั้น 4 ค่าใช้จ่ายปี 2000 (MPM p.128-130)

| รายการ | M฿ | % |
|---|---|---|
| ค่าบริหารจัดสรรจากส่วนกลาง | 18.0 | 3.5% |
| ค่าเสื่อม + ต้นทุนการเงินเครื่องมือ (ทรัพย์สิน 97.1) | 16.0 | 3.1% |
| เงินเดือนค่าแรง | 62.1 | 12.1% |
| ค่าใช้จ่ายด้านอะไหล่ (ต้นทุนการเงิน 52.1 + เบิกคลัง 56.1 + ซื้อตรง 259.5; คงคลัง 521.2) | 367.7 | 71.8% |
| จ้างเหมาค่าแรง | 11.3 | 2.2% |
| ซ่อมใหญ่เฉลี่ย/ปี | 36.7 | 7.2% |
| **รวม** | **511.8** | 100% |

- ตรวจ (derived): 18.0 + 16.0 + 62.1 + 367.7 + 11.3 + 36.7 = 511.8; 511.8M / 530,000 = 965.66; OEE +1% = 4,000 / 0.794 / 100 = 50.38 (สมมติกำไรขั้นต้นแปรผันตรงกับ OEE)
- ค่าอะไหล่โตจาก 53.3% (1998) เป็น 71.8% (2000) ขับโดย "สั่งซื้อตรง" ที่โตจาก 47.4 เป็น 259.5 M฿ (MPM p.129-130)
- ต้นทุนการเงินอะไหล่ของ XYZ คิด 10% ของมูลค่าคงคลัง (52.1 / 521.2) ต่ำกว่าค่าครอบครอง 15-25% ของ RBMM หัวข้อ 4 ดูข้อขัดแย้ง MPM-C1 ที่ [[Maintenance Cost Structure]]
- ขั้น 6 คิดด้วย Full Cost Rate 1,506.4 ซึ่งรวมต้นทุนการเงินอะไหล่ไว้ในอัตรา (38,018 ชม. x 1,506.4 = 57.3 M฿ ฯลฯ derived) จ้างเหมา 11.3 M฿ ใช้กับงาน Modification ทั้งหมด

### 9.10 Budget Spending Control (MPM p.131-133)

"อะไรที่วัดไม่ได้ ย่อมควบคุมไม่ได้" รายงานหลัก
1. **รายงานงบดุล** — ทรัพย์สินระยะยาว (เครื่องมือ) และหมุนเวียน (อะไหล่, ลูกหนี้ถ้ารับงานนอก)
2. **รายงานการใช้งบ** (หรือกำไรขาดทุน) รวมต้นทุนการเงินและค่าเสื่อม เทียบจริงกับงบ: ส่วนคงที่ (Variance จากฐาน PM เทียบ Work Control), ส่วนแปรผัน (ฐานข้อมูลงานซ่อม), ส่วนโครงการ (ระบบควบคุมโครงการ)
3. **รายงานจาก Work Control** — Utilization Rate (ใช้คำนวณ Full Costs), ค่าใช้จ่ายตามประเภทต่องาน, ข้อมูลเดิน/หยุดเพื่อ OEE, ดัชนีเป้า

ตัวอย่าง Plan vs Actual PM ปี 2003 (MPM p.132, หน่วยไม่ระบุในรูป): Plan 67,060 vs Actual 62,419 ต่ำกว่าแผน 4,641 = 6.9% (derived) ต่ำกว่าแผนทุกเดือนยกเว้น NOV

- ในบัญชีทั่วไปหน่วยบำรุงรักษาเป็น Cost Center รายงานทรัพย์สินจึงออกเป็นรายงานตามหน่วยงานแทนงบดุล (MPM p.133)
- ธุรกิจบริการ หัวใจงบคือสมมติฐาน Utilization Rate ของกำลังคน; ธุรกิจผลิต หัวใจงบคือแผนการผลิต (MPM p.138-139) การตั้งงบแบบศูนย์กำไร/บริษัทบริการ (Over/(Under) Reserved, WIP, Provision) ดู [[Job Order Costing]]

### 9.11 Disambiguation: Provision สองบริบท

- RBMM (หัวข้อ 3) ใช้ **Provision for Losses / Provision for Costs** = สำรองในงบ Cost Center (เพดานความคลาดเคลื่อนของงบ)
- MPM และ [[Job Order Costing]] ใช้ **Provision for Work Due / Provision for Loss Order** = สำรองทางบัญชีของงานบริการต่อ Job (MPM p.136-137)
- ชื่อคล้ายกันแต่คนละกลไก ไม่ขัดกัน

## เชื่อมโยงกับ compressor failure hierarchy

หนังสือไม่มีเนื้อหาตรงเกี่ยวกับ [[OREDA]] หรือ [[ISO 14224]] ความเชื่อมทางอ้อม:
- งบ Unplanned และอะไหล่ของ Criticality A ต้องคิด "ทุก Failure Mode" ด้วยสถิติ (RBMM p.317) ตรงกับตาราง [[Failure Mode]] ของ compressor เช่น AIR, SER, LOO ที่เป็นแหล่งจำนวนครั้งเกิดโดยประมาณ
- ลำดับ Asset Equipment -> System -> Process (RBMM p.286) คล้าย hierarchy ระดับ [[Maintainable Item]] ใน ISO 14224 ใช้ผูกต้นทุนต่ออุปกรณ์
- ตัวเลข OREDA เป็น failure rate ทั่วไป ใช้เป็นข้อมูลตั้งต้นของงาน CM-Unplanned ได้เฉพาะเมื่อไม่มีสถิติของโรงงานเอง (ความรู้เสริม ไม่ใช่ข้อความในหนังสือ)
- รหัสงบ 4 มิติของ MPM (Equipment Structure เป็น Cost Collector) วางให้โหนด Equipment ตรงกับ [[Compressor]] -> sub unit ได้ ทำให้ดัชนีค่าซ่อม/ราคาเครื่อง สอบเทียบระหว่าง compressor ชนิดเดียวกันได้ (การตีความของ wiki; MPM ไม่ได้ยกตัวอย่าง compressor)

## ดูเพิ่ม

- [[Maintenance Cost Structure]] — Fixed Cost, Materials, Full Fixed Cost Rate
- [[Maintenance Strategic Report]] — รายงานที่ใช้ปรับงบ
- [[Maintenance KPIs]]
- [[Criticality Assessment]]
- [[Spare Part Criticality and Risk]]
- [[Maintenance Business Models]]
- [[Reliability Based Maintenance Management Book]]
- [[Turnaround Management]]
- [[Maintenance Profit Maker Book]]
- [[Maintenance Outsourcing]]
- [[Job Order Costing]]

ดูเพิ่ม (หน้าจาก MPM ingest 2026-10-28): [[Maintenance Financial Impact]]

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
- Plant Turnaround Cost [has_value:: excludes internal labour] annual amortised cost, Materials and contract only (RBMM p.276-279) [contested:: true]
- Plant Turnaround Cost [has_value:: includes plant staff wages] counted as event cost (CMRP CMPR-10 p.19) [contested:: true]
- CMRP Turnaround Cost View [contradicts:: RBMM Turnaround Cost View] total cost visibility vs budget allocation; unresolved [contested:: true]
- Plant Turnaround [related_to:: [[Turnaround Management]]] spreading cost over years does not reduce total impact (CMRP CMPR-10 p.13)
- [[Maintenance Budget]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 7 Maintenance Budgeting and Control (MPM p.111-139)
- [[Maintenance Budget]] [has_part:: Budget Spending Control] with Maintenance Budgeting (MPM p.112)
- Budget Code [has_parameter:: Equipment Hierarchy] Cost Collector, dimension 1 (MPM p.112, 115)
- Budget Code [has_parameter:: Responsibility Chart of Account] dimension 2 (MPM p.113, 115)
- Budget Code [has_parameter:: Expense or Asset Account by activity] dimension 3, 16 activities (MPM p.113-115)
- Budget Code [has_parameter:: Resource Type] labour, spares and consumables, contracts, other; dimension 4 (MPM p.115)
- Expense Account [applies_to:: Fault Recovery and Preventive-Proactive] except Turnaround (MPM p.113-114)
- Asset Account [applies_to:: Modification, Maintenance Engineering and Turnaround] amortised yearly (MPM p.113-114)
- Plant Turnaround [has_formula:: turnaround cost / years to next turnaround] e.g. 1/3 per year for 3-year cycle (MPM p.114)
- Spare Usage in Period [has_formula:: opening stock + purchases - closing stock] (MPM p.114)
- Reactive Budgeting [differs_from:: Proactive Value Oriented Budgeting] last year plus vs value target (MPM p.115-117)
- Proactive Value Oriented Budgeting [uses:: B/OEE] minimise Budget / OEE, Profit Center principle (MPM p.116-117)
- Creative COST-PLUS [depends_on:: [[Availability and OEE]]] internal target tied to OEE and cost indices (MPM p.125-126)
- Target Production [has_formula:: Capacity x Planning Factor x OEE] (MPM p.125, 128)
- Investment Budget [has_part:: Maintenance Performance Audits] most important step (MPM p.119)
- Investment Budget [has_part:: CMMS Improvement Project] (MPM p.119)
- Investment Budget [has_part:: Spare Part Stock] (MPM p.120)
- Investment Budget [has_part:: Maintenance Tools and Systems] Reliability System, Predictive Tools, OEE measurement (MPM p.120)
- Investment Budget [has_part:: Turnaround] every 3, 4 or 5 years (MPM p.120)
- Investment Budget [has_part:: Modification Projects] (MPM p.120-121)
- Investment Budget [has_part:: Cost Reporting System] Single Entry System (MPM p.121)
- [[CMMS]] [has_value:: under 25% fully used] author claim, no source given (MPM p.119) [confidence:: low]
- Operating Budget Fixed Part [depends_on:: PM Plan] yearly PM from PM database (MPM p.122-123)
- Operating Budget Variable Part [depends_on:: PM Quantity and Quality] MTBF, MTTR, PM/CM Ratio (MPM p.123-124)
- PM/CM Ratio [has_value:: 2.0] man-hour basis target (MPM p.124)
- Budget Input Data [has_value:: 10 items] organisation, accounts, financial statements, production plan, cost by 16 activities, standard jobs, OEE, energy efficiency, indices, targets (MPM p.126-127)
- Maintenance Manager Budget Duties [has_value:: 5 duties] targets, allocate fixed cost, allocate indirect cost, cascade to equipment, approve and control (MPM p.127)
- XYZ Budget 2000 [has_value:: 965.7 THB per tonne] 511.8 M THB / 530,000 t (MPM p.128)
- XYZ Budget 2000 [has_value:: OEE +1% = +50.37 M THB gross profit] OEE 79.4%, gross profit 4,000 M THB (MPM p.128-129)
- XYZ Budget 2000 [has_value:: spares 367.7 M THB = 71.8% of 511.8] (MPM p.129-130)
- XYZ Budget 2000 [has_value:: Full Cost Rate 1,506.4 THB per man-hour] 148.2 M THB / 98,400 h (MPM p.130)
- OEE Target Increase [has_value:: at most 1-2%] recommended per year (MPM p.128)
- Budget Spending Control [uses:: Balance Sheet Report] (MPM p.131-132)
- Budget Spending Control [uses:: Budget Usage Report] fixed, variable and project parts vs budget (MPM p.132)
- Budget Spending Control [uses:: Work Control Report] Utilization Rate for Full Costs (MPM p.132)
- Plan vs Actual PM 2003 [has_value:: 67,060 plan vs 62,419 actual] 6.9% below plan, derived (MPM p.132)
- Provision for Losses [differs_from:: Provision for Loss Order] RBMM budget provision vs MPM service job provision
- Holding Cost [has_value:: 10% finance cost only] XYZ spare finance cost 52.1 / 521.2 (MPM p.108, 129-130) [contested:: true]
- Holding Cost [has_value:: 15-25%] RBMM recommended range (RBMM p.295) [contested:: true]
- MPM Holding Cost Example [contradicts:: RBMM Holding Cost Range] MPM-C1 [contested:: true]

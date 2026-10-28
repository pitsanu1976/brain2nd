---
title: Maintenance Profit Maker Book
created: 2026-10-28
updated: 2026-10-28
type: entity
tags: [mpm, book, maintenance-management, cost, budget, kpi]
sources: [maintenance-profit-maker.md, reliability-based-maintenance-management.md, spare-parts-optimization.md]
confidence: medium
contested: true
---

# Maintenance: The Profit Maker (MPM) — หนังสือ

hub ของหนังสือ "Maintenance: The Profit Maker — บำรุงรักษา : งานเพิ่มกำไรบริษัท" ที่ ingest เข้า wiki เมื่อ 2026-10-28 หนังสือมองงานบำรุงรักษาจาก **มุมการเงินและผลกำไรของบริษัท**: งานบำรุงรักษากระทบทั้งรายได้ (OEE, availability, "Hidden Plant") และรายจ่าย (full cost, อะไหล่, งบประมาณ) และเชื่อมงบดุล/งบกำไรขาดทุนเข้ากับดัชนีเทคนิค ผู้แต่ง 2 คนเป็นผู้แต่งร่วมของ [[Reliability Based Maintenance Management Book]] เนื้อหาหลายส่วนจึงซ้อนกัน แต่ตัวเลขสมมติฐานบางจุดต่างกัน (ดูหัวข้อข้อขัดแย้ง) ข้อความทั้งหมดถอดความจาก reading notes ไม่ใช่ข้อความต้นฉบับ

## ข้อมูลบรรณานุกรม

- ชื่อ: Maintenance: The Profit Maker — บำรุงรักษา : งานเพิ่มกำไรบริษัท
- ผู้แต่ง: วัฒนา เชียงกูล, เกรียงไกร ดำรงรัตน์ (ประสบการณ์รวมราว 30 ปี เช่น EGAT, Hitachi, GE, Westinghouse, ABB) (MPM p.5-7)
- สำนักพิมพ์: ซีเอ็ดยูเคชั่น (SE-ED), พ.ศ. 2556 (2013), ISBN (e-book) 978-616-08-1057-4, เลขหมู่ 658.202, ชุด Industrial Management and Technical Series (MPM p.4, p.8)
- 15 บท: หลัก 5 บท (บทบาทต่อผลประกอบการ, ดัชนี, ตรวจสอบ, ปรับปรุง, แผนแม่บท), รอง 8 บท, เสริม 2 บท (บัญชี, เศรษฐศาสตร์วิศวกรรม) (MPM p.5-7)
- raw: [[raw/maintenance-profit-maker]] และ reading notes 7 ไฟล์ใน `raw/maintenance-profit-maker/` ไฟล์ OCR ทั้งเล่มเก็บในเครื่องเท่านั้น (gitignored) เพราะมีลิขสิทธิ์
- การอ้างอิง: `(MPM p.NN)` ด้วยเลขหน้าที่พิมพ์ในหนังสือ (marker ใน OCR ผิดบางช่วง ดูหน้า raw)

## แนวคิดหลักของเล่ม

- ตัวเลขระดับประเทศ (สมมติฐานผู้เขียน): ทรัพย์สินผลิตอุตสาหกรรมไทย 10,000,000 ล้านบาท ค่าบำรุงรักษา 2.5% ของมูลค่าซื้อทดแทน = 250,000 ล้านบาท/ปี ลด 1% ประหยัด 2,500 ล้านบาท; อะไหล่สะสมราว 4% ของมูลค่าเครื่องจักร = 400,000 ล้านบาท ลด 1% ได้สภาพคล่อง 4,000 ล้านบาท (MPM p.5)
- โจทย์ที่ถูกคือ ไม่ให้เสีย เสียแล้วซ่อมไม่แพง และไม่เกิดซ้ำ; ต้องมีระบบวัดค่าใช้จ่าย/ผลผลิตที่เชื่อถือได้ ไม่เช่นนั้นคุมไม่ได้ (MPM p.5-7)
- กรณีศึกษาโรงงานสมมติ **XYZ** (ปี 1998-2000) ใช้ข้ามบทที่ 7, 8, 10, 12: OEE ลดจาก 89.13% เป็น 79.42% และเสียโอกาสกำไรขั้นต้น 161.84 / 489.17 ล้านบาท ([[Maintenance Financial Impact]])

## แผนที่บท -> หน้า wiki

| บท | Book pages | หัวข้อหลัก | หน้าใน wiki |
|---|---|---|---|
| ส่วนนำ | 3-12 | บรรณานุกรม คำนำ สารบัญ | หน้านี้ |
| 1 | 13-36 | 16 กิจกรรม (4 กลุ่ม x 4), ความสูญเสีย 8 ข้อ, failure pattern, audit 14 หัวข้อ, road map 5 ระดับ | [[Maintenance Business Models]], [[Failure Patterns and Bathtub Curve]], [[Maintenance Performance Audit]], [[CMMS]], [[Turnaround Management]] |
| 2 | 37-46 | LCC 3 ช่วง, LCR, LCP, ตัวอย่าง 3 เครื่อง | [[Life Cycle Cost and Life Cycle Profit]], [[Asset Life Cycle]] |
| 3 | 47-58 | OEE, Planning Factor, Total Productivity, Six Big Losses | [[Availability and OEE]] |
| 4 | 59-81 | ข้อกำหนดระบบ 9 ข้อ, 6 ขั้น work order, 7 สถานะ, รายงานวิเคราะห์ | [[Work Order Lifecycle]], [[CMMS]], [[Maintenance Planning and Scheduling]] |
| 5 | 83-90 | เป้าหมายอะไหล่, service level, ABC ตามปริมาณ, matrix movement x cost | [[Spare Parts Management]], [[MRO Inventory Control Methods]], [[EOQ and Reorder Point]], [[Spare Part Criticality and Risk]] |
| 6 | 91-110 | outsourcing: 3 แบบสัญญา, matrix criticality x responsibility, full cost rate | [[Maintenance Outsourcing]], [[MRO Purchasing and Contracting]] |
| 7 | 111-139 | budget code 4 มิติ, reactive vs proactive budget, ตัวอย่าง XYZ 2000 | [[Maintenance Budget]], [[Maintenance Cost Structure]], [[Job Order Costing]] |
| 8 | 140-156 | เป้าหมาย 5 ข้อ, KPI หลัก + 4 กลุ่มย่อย, full cost ต่อตัน | [[Maintenance KPIs]], [[Availability and OEE]], [[Reliability Metrics]] |
| 9 | 157-166 | แผนแม่บท 16 แผน, กลยุทธ์ Cost Leadership vs Differentiation | [[Maintenance Master Plan]] |
| 10 | 167-190 | งบดุล/งบกำไรขาดทุน, Hidden Plant, OEE -> กำไร, labour cost | [[Maintenance Financial Impact]], [[Maintenance Cost Structure]] |
| 11 | 191-204 | Flash/Full audit, 16 หัวข้อ radar A-F, Room for Improvement, reconciliation | [[Maintenance Performance Audit]], [[Maintenance KPIs]] |
| 12 | 205-242 | กระบวนการปรับปรุง 6 ขั้น, อะไหล่ 20/60/20, planner, turnaround, กรณีศึกษา 2 เรื่อง | [[Maintenance Performance Improvement]], [[Spare Parts Management]], [[Turnaround Management]], [[Maintenance Business Models]] |
| 13 | 243-252 | physical asset management, criticality 7 เกณฑ์ 30/50/20 | [[Criticality Assessment]], [[Asset Life Cycle]] |
| 14 | 253-264 | บัญชีพื้นฐาน: งบดุล, ค่าเสื่อม, COGS, WIP, absorption | [[Maintenance Cost Structure]], [[Job Order Costing]] |
| 15 | 265-280 | ค่าของเงินตามเวลา 6 factor, WACC, NPV/IRR/payback, บรรณานุกรม | [[Engineering Economics and Time Value of Money]], [[Maintenance Business Case]] |

## ข้อขัดแย้งกับแหล่งอื่น (รอผู้ใช้ตัดสิน)

ทุกข้อเก็บทั้งสองมุมมองในหน้าที่เกี่ยวข้อง และตั้ง `contested: true`

| ID | ประเด็น | MPM | แหล่งอื่น | หน้า |
|---|---|---|---|---|
| MPM-C1 | holding cost ของอะไหล่ | 20-40% ของมูลค่าสต็อก (MPM p.84); ตัวอย่างคิดเฉพาะต้นทุนการเงิน 6-10% (MPM p.17, p.108, p.180-181) | RBMM 15-20% ต่อปี | [[Spare Parts Management]], [[Maintenance Cost Structure]], [[EOQ and Reorder Point]] |
| MPM-C2 | สัดส่วนต้นทุนที่ถูกกำหนดในช่วง engineering/design | ไม่คงที่ในเล่ม: p.14 = 80%, p.39 Engineering 90% / Project 80%, รูป 70/85/95/100 | RBMM Fig 1.1 85-95% | [[Asset Life Cycle]], [[Life Cycle Cost and Life Cycle Profit]] |
| MPM-C3 | ตัวอักษร failure pattern | ตามระบบ Nowlan & Heap (F = infant mortality 68%) (MPM p.20) | RBMM A = wear-out, E = infant | [[Failure Patterns and Bathtub Curve]] |
| MPM-C4 | นิยาม MTTR / MTBF | บทที่ 8: MTTR = เวลาซ่อมอย่างเดียว เวลารอแยกเป็น Mean Logistic Time (MPM p.150-151); บทที่ 4: MTBF = (ชม.รวม - ชม.ซ่อม)/จำนวนเสีย (MPM p.76); บทที่ 9 กลับรวมเวลารอใน MTTR (MPM p.166) | RBMM MTTR = ซ่อม + รอ, MTBF = MTTF + MTTR + MWT | [[Reliability Metrics]], [[Maintenance Time Definitions]], [[Availability and OEE]] |
| MPM-C5 | เป้า labour utilization | เป้า > 60%, ตัวอย่าง 40% -> 70% (MPM p.215, p.239) | RBMM 60% ถือว่าสูงแล้ว อย่าไล่ดัชนีนี้ตัวเดียว (RBMM p.73-74) | [[Maintenance KPIs]], [[Maintenance Performance Improvement]] |
| MPM-C6 | profit centre | ดีกว่าในทุกรูปแบบ (MPM p.241-242) | RBMM: โรงงานเดียว cost center + performance budgeting ก็พอ (RBMM p.325-327) | [[Maintenance Business Models]] |
| MPM-C7 | อายุค่าเสื่อมราคา | 10-20 ปีตามกฎหมาย (MPM p.256) | RBMM 15-20-25 ปี (RBMM p.15) | [[Asset Life Cycle]] |

### ความต่างที่ไม่ถือว่าขัดแย้ง

- มูลค่าสต็อกอะไหล่ 3-5% ของราคาเครื่องจักร เป็นค่าเฉลี่ยประเทศอุตสาหกรรม (MPM p.84-85) ไม่ใช่เป้า เป้าที่ผู้ใช้เลือกแล้ว (2026-10-27) ยังคงเป็น SPO ไม่เกิน 4% ของ GPI ([[Inventory Turnover and GPI Benchmarks]])
- สัดส่วน criticality สูง/กลาง/ต่ำ 20/50/30% (MPM p.85) กลับกับ 30/50/20% ของ MPM p.250 และ RBMM (ตัวอย่างประกอบทั้งคู่)
- ABC ตามปริมาณการใช้ 70/20/10% (MPM p.87) vs ตามมูลค่า (SPO/RBMM) ผู้ใช้ตัดสินแล้วว่ากลุ่ม A = มูลค่าใช้สูง
- turnover ของ MPM เป็น % ของสต็อกสิ้นปี (Used/Stock) ต่างหน่วยกับ turns ต่อปีบนสต็อกเฉลี่ยของ SPO
- ชั่วโมงทำงานต่อคนต่อปี 1,663.2 ชม. (MPM p.154, p.186) vs RBMM 1,760 / ราว 1,600 และในตาราง XYZ เองใช้ 1,968 / 2,112
- "Blanket Order" ของ MPM มีความหมายเดียวกับ SPO (ซื้อเหมาล่วงหน้า) ส่วน Consignment Stock = ของผู้ขายฝากไว้ ยืนยันว่าความต่างกับ RBMM เป็นเรื่องศัพท์

## ข้อผิดพลาดของหนังสือ/OCR ที่ flag (ตรวจคำนวณซ้ำ, derived)

รายละเอียดเต็มอยู่ท้ายแต่ละไฟล์ notes ตัวอย่างสำคัญ:

- ตัวย่อผิด: RBI เขียนเป็น "Reliability Based Inspection" (MPM p.223, p.252; ที่ถูก Risk-Based Inspection ตาม API 580, ความรู้ทั่วไป) และ FMECA เขียนเป็น "Failure Mode Effect and Cost Analysis" (MPM p.236); MTTR เขียนเป็น "Mean Time Between Repair" (MPM p.75)
- LCC เครื่องที่ 1: PV อะไหล่คำนวณได้ 26,390 ไม่ใช่ 26,578 (รวม 29,431 ไม่ใช่ 29,619) อันดับไม่เปลี่ยน (MPM p.42-44)
- Fig 4.16: ยอดรวม 2 แถวเกิน 900 ทำให้ grand total 46,273.80 ควรเป็น 44,473.80; Fig 4.18 MTBF 5,255.00 ควรเป็น 5,225.00 (MPM p.75-76)
- Fig 8.3: up time ในข้อความ 650 ชม. แต่รูปและเลขได้ 630 ชม.; failure rate 1/210 = 0.0048 (พิมพ์ 0.0047); สูตร service level ตัวเศษควรเป็น "filled" (MPM p.149-152)
- ตัวอย่าง 147 บาท/ตัน ยังรวมต้นทุนการเงินของอะไหล่ 35 ล้าน ถ้าตัดออกด้วยได้ 121.2 บาท/ตัน (MPM p.147)
- Fig 10.2: อะไหล่ 512,200,000 ควรเป็น 521,200,000; Fig 10.10 maintenance cost/ARV 2.7/3.3/4.4% ควรเป็น 2.9/3.5/4.65% (MPM p.172, p.178)
- Fig 12.13: กำไรที่ OEE 100% ปี 1999 ควรเป็น 1,864.5 (พิมพ์ 1,579) และปี 1998 ควรเป็น 3,366 (พิมพ์ 1,944) ตัวเลขสุดท้าย 161.84 ถูก; Fig 12.10 กับ 12.12 ขัดกันราว 12 ดัชนี ข้อมูลดิบยืนยัน Fig 12.12 (MPM p.228-234)
- ตัวอย่าง planner: setup ว่า 35 คนแต่คำนวณใช้ 3; ผลคูณ 1.57 ไม่หักหัว planner เอง ต่อหัวได้ราว 1.18 (MPM p.227)
- ยอด 1,038.4 ล้าน รวมเงินลงทุนครั้งเดียวกับเงินประหยัดรายปี (MPM p.240)
- WACC: แถวหนี้พิมพ์ "3.5 x 2/3 = 0.33" ที่ถูก 2.33 (ผลรวม 5.10% ยังถูก); ฟังก์ชัน Excel ใช้ `PMT()` กับทั้ง 6 factor ทั้งที่ถูกแค่ A/F และ A/P; ตัวอย่าง NPV นับปีแรกเป็น t=0 (MPM p.269-276)
- อัตราค่าแรงตรงแถว 30 ของ XYZ (237.1) คำนวณจากแถว 28 ได้ 254.5 ตัวเลขของหนังสือได้เมื่อใช้ 2,112 ชม./คน (MPM p.108)

## ความสัมพันธ์กับแหล่งอื่นใน wiki

- **RBMM**: ผู้แต่งร่วมกัน กรอบ 16 กิจกรรม, OEE = A x S x Q, fixed/variable cost, absorption, radar chart ตรงกัน MPM ขยายด้านการเงิน (งบดุล, WACC, LCC/LCP, NPV/IRR) และการตรวจสอบ/ปรับปรุงสมรรถนะ แต่ตัวเลขสมมติฐานต่างกันหลายจุด (MPM-C1, C2, C4, C5, C6, C7)
- **SPO** ([[Spare Parts Optimization Book]]): เรื่องอะไหล่ MPM เน้นเป้าหมายการเงิน (service level, carrying cost, payback) ส่วน SPO เน้นปฏิบัติการคลัง/จัดซื้อ ศัพท์ Blanket Order/Consignment ตรงกัน
- **CMRP** ([[CMRP Course]]): backlog ของ MPM นับเป็นวันไม่มีเป้า ส่วน CMRP นับเป็นสัปดาห์ (2-3 / 3-6 สัปดาห์)
- **ISO 14224** ([[ISO 14224]]): MPM ไม่ได้อ้างมาตรฐานรหัส failure

## เชื่อมโยงกับ compressor failure hierarchy

หนังสือไม่มีข้อมูล compressor โดยตรง (การตีความ): สูตร OEE/availability และนิยาม MTTR/MTBF ของ MPM ใช้คำนวณ availability ของ compressor train ได้ แต่ต้องเลือกนิยามให้ตรงกับ [[Maintenance Time Definitions]] ก่อน (MPM-C4) ส่วน criticality 30/50/20 และ service level อะไหล่ 100% / 95-98% ใช้กำหนดนโยบายสต็อกอะไหล่ของ maintainable item ที่เด่นใน [[Compressor]] เช่น valves และ cylinder liner

## Triplets

- MPM [alias_of:: [[Maintenance Profit Maker Book]]] Maintenance: The Profit Maker, SE-ED 2556
- [[Maintenance Profit Maker Book]] [has_code:: ISBN 978-616-08-1057-4] e-book (MPM p.4)
- [[Maintenance Profit Maker Book]] [has_value:: 15] chapters (MPM p.9-12)
- [[Maintenance Profit Maker Book]] [has_value:: 277] pages of scanned PDF
- [[Maintenance Profit Maker Book]] [has_category:: maintenance financial management] maintenance as profit maker
- [[Maintenance Profit Maker Book]] [related_to:: [[Reliability Based Maintenance Management Book]]] shared authors
- [[Maintenance Profit Maker Book]] [related_to:: [[Spare Parts Optimization Book]]] spare parts topics
- [[Maintenance Profit Maker Book]] [related_to:: [[CMRP Course]]] backlog, KPI topics
- [[Life Cycle Cost and Life Cycle Profit]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 2
- [[Availability and OEE]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 3
- [[Work Order Lifecycle]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 4
- [[Maintenance Outsourcing]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 6
- [[Maintenance Budget]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 7
- [[Maintenance KPIs]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 8
- [[Maintenance Master Plan]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 9
- [[Maintenance Financial Impact]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 10
- [[Maintenance Performance Audit]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 11
- [[Maintenance Performance Improvement]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 12
- [[Criticality Assessment]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 13
- [[Engineering Economics and Time Value of Money]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 15
- Spare Part Holding Cost [has_value:: 20-40%] of stock value, MPM p.84 [contested:: true]
- Spare Part Holding Cost [has_value:: 15-20%] per year, RBMM [contested:: true]
- Mean Time To Repair [has_formula:: repair time only, waiting as Mean Logistic Time] MPM p.150-151 [contested:: true]
- Labour Utilization [has_value:: >60% target] MPM p.215 [contested:: true]
- Depreciation Life [has_value:: 10-20 years] MPM p.256 [contested:: true]
- Reliability Based Inspection [differs_from:: Risk-Based Inspection] book error for RBI in MPM p.223, p.252

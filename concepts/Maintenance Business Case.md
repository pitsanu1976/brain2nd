---
title: Maintenance Business Case
created: 2026-10-25
updated: 2026-10-28
type: concept
tags: [cmrp, business-case, cost, budget, kpi, maintenance-management, mpm, engineering-economics]
sources: [cmrp.md, reliability-based-maintenance-management.md, maintenance-profit-maker.md]
confidence: medium
contested: false
---

# Maintenance Business Case (การทำ business case สำหรับการลงทุนด้านบำรุงรักษา)

Business case คือเอกสารที่ใช้ขออนุมัติการลงทุนเฉพาะโครงการ โดยแสดงว่าโครงการมีคุณค่า คุ้มทุน สอดคล้องกับกลยุทธ์ และทำได้จริง สไลด์ CMRP นำเสนอขั้นตอนทำ business case (CMRP CMPR-04 p.1-5) และความต่างระหว่าง business case กับ business plan (CMRP CMPR-03 p.49-50) ในงานบำรุงรักษาใช้กับการลงทุนเช่น modification, redundancy, ระบบ CM/CMMS ใหม่ หรือ capital spares ข้อความถอดความจาก reading notes ใน [[CMRP Course]]

**ข้อจำกัดของแหล่ง:** สไลด์กล่าวถึง DCF, IRR และ hurdle rate เป็นชื่อเท่านั้น **ไม่มีสูตร NPV, IRR, ROI, payback และไม่มีตัวอย่างตัวเลข** (CMRP CMPR-04 p.1-5) หน้านี้จึงไม่ใส่สูตรการเงิน ถ้าต้องการสูตรต้องใช้แหล่งอื่น

**อัปเดต 2026-10-28:** ข้อจำกัดข้างบนยังจริงสำหรับสไลด์ CMRP แต่ตอนนี้ wiki มีแหล่งสูตรแล้ว: บทที่ 15 ของ [[Maintenance Profit Maker Book]] ให้ 6 interest factors, WACC, IRR, NPV และ payback พร้อมตัวอย่างที่ตรวจซ้ำแล้ว สรุปไว้ที่ [[Engineering Economics and Time Value of Money]] (MPM p.265-277) ส่วน ROI, benefit-cost ratio, annual worth และ replacement analysis ยังไม่มีใน sources

## Business case vs business plan (CMRP CMPR-03 p.49-50)

| | Business case | Business plan |
|---|---|---|
| ขอบเขต | โครงการเดียว (CAPEX, IT project, ย้ายโรงงาน ฯลฯ) | ทั้งธุรกิจ ระยะยาว |
| คำถามหลัก | ควรลงทุนไหม: value, profitability, alignment, feasibility | ธุรกิจจะไปทางไหน: ตลาด ลูกค้า forecast |
| ผู้ใช้ | ผู้อนุมัติการลงทุน / sponsor | ผู้บริหาร นักลงทุน |

## 6 ขั้นของ business case (CMRP CMPR-04 p.1-5)

1. **Confirm the opportunity**: บรรยายสถานการณ์ปัจจุบันและโอกาส (background, investment logic) ผูกกับ strategic objectives และให้ sponsor อนุมัติก่อนทำต่อ
2. **Analyze and shortlist options**: ทำ long list ของทางเลือก ตั้งเกณฑ์ประเมิน เก็บข้อมูล แล้วคัดเหลือ 3-4 ทาง เสนอเป็น comparison matrix (ข้อดี/ข้อเสีย)
3. **Evaluate options** (p.2-3): ดูความสอดคล้องกับกลยุทธ์; quantify benefit ทั้งที่เป็นเงินและไม่เป็นเงิน (cost savings, revenue growth, operational efficiency, ROI); ทำ cash flow และ **DCF analysis** แล้วตรวจว่าผ่าน **IRR ขั้นต่ำ หรือ hurdle rate**; ประเมินความเสี่ยงและมาตรการลด; ทำ **scenario analysis**; ฟังความเห็น stakeholder
4. **Implementation strategy** (p.3-4): objectives และ milestones, ทรัพยากรผูกกับ milestone, roles, ความเสี่ยง, cost breakdown ต่อ milestone, KPI ของการ implement, communication plan และ change management
5. **Recommendation and approval** (p.4-5): เปิดด้วย executive summary และเตรียมตอบคำถามของผู้ตัดสินใจ ได้แก่ ความเสี่ยง, upside, **cost of not proceeding** (ต้นทุนของการไม่ลงทุน) และความสอดคล้องกับกลยุทธ์
6. **Follow-up**: ระบุ next steps และผู้รับผิดชอบ สื่อสารต่อเนื่องตลอดอายุโครงการ

ความไม่สอดคล้องระหว่างไฟล์: CMPR-03 p.49-50 พูดถึง "5 ขั้น" (หัวข้อที่อ่านได้บางส่วน: confirm the opportunity, high-level requirements, strategic logic) ส่วน CMPR-04 p.1-5 แสดง 6 ขั้นข้างบน หน้านี้ยึด 6 ขั้นของ CMPR-04 เพราะครบกว่า เป็นความต่างภายในแหล่งเดียว ไม่ใช่ contested

## แนวคิดการเงินที่สไลด์ใช้ (ไม่มีสูตรในสไลด์)

คำอธิบายในวงเล็บเป็นความรู้ทั่วไปเพื่อให้อ่านเข้าใจ ไม่อยู่ในสไลด์ (confidence low)

- **DCF (Discounted Cash Flow)**: นำ cash flow ในอนาคตมาคิดเป็นมูลค่าปัจจุบัน (ความรู้ทั่วไป)
- **IRR และ hurdle rate**: โครงการผ่านเมื่อผลตอบแทนภายในไม่ต่ำกว่าอัตราขั้นต่ำที่องค์กรตั้ง (ความรู้ทั่วไป)
- **Scenario analysis**: ดูผลเมื่อสมมติฐานหลักเปลี่ยน เช่น ราคา ปริมาณ failure rate (ความรู้ทั่วไป)
- **Cost of not proceeding**: ในงานบำรุงรักษามักเป็น risk cost ของการเดินต่อแบบเดิม เช่น downtime และ production loss ที่คาดว่าจะเกิด (การตีความของ wiki) แนวคิด risk cost = probability x penalty ปรากฏในเรื่องอะไหล่ (CMRP CMPR-03 p.13) ดู [[Spare Part Criticality and Risk]]

### สูตรจาก MPM สำหรับขั้น Evaluate options (เพิ่ม 2026-10-28)

ใช้แทนคำอธิบายความรู้ทั่วไปข้างบน รายละเอียดและตัวอย่างเต็มอยู่ที่ [[Engineering Economics and Time Value of Money]]

| เครื่องมือ | นิยาม/สูตรตาม MPM | ข้อควรระวัง |
|---|---|---|
| Discount rate | WACC = Kd x (1 - ภาษี) ถ่วงหนี้ + Ke ถ่วงทุน; ตัวอย่าง 5.10% (MPM p.269-271) | Kd หลังภาษีใช้ได้เฉพาะบริษัทที่มีกำไร |
| NPV (DCF) | PV ของกระแสเงินทุกงวดที่ WACC (MPM p.274-276) | ตัวอย่างหนังสือไม่คิดลดงวดแรก (t = 0) ถ้าใช้ Excel `NPV()` ตรง ๆ จะได้ค่าต่ำลงหนึ่งงวด |
| IRR / hurdle rate | อัตราที่ NPV = 0 (MPM p.272-274) ผ่านเมื่อ IRR ไม่ต่ำกว่า hurdle rate | ทางเลือกขนาดต่างกันอาจได้ผล IRR ขัดกับ NPV (ตัวอย่าง IRR 11.88% vs 10.82% แต่ NPV 906,434 vs 1,029,712) |
| Payback | จำนวนปีที่กระแสเงินสะสมกลับเป็นบวก (MPM p.276-277) | ตัวอย่างหนังสือเป็น simple payback ไม่คิดลด |

- ผู้เขียน MPM ว่า "มักใช้ IRR มากกว่า" (MPM p.276) แต่หลักการเงินทั่วไปให้ตัดสินทางเลือก mutually exclusive ด้วย NPV หรือ incremental IRR (ความรู้ทั่วไป, confidence low) ดูการวิเคราะห์ที่ [[Engineering Economics and Time Value of Money]]
- การเทียบเครื่องจักรด้วยต้นทุนตลอดอายุ (LCC) และกำไรตลอดอายุ (LCP) ดู [[Life Cycle Cost and Life Cycle Profit]]

ตัวอย่างเชิงแนวคิดจากสไลด์: oil platform ยอมรับ cost of ownership ที่สูงขึ้นเพื่อแลก availability เพิ่มเล็กน้อย เพราะ revenue loss จาก downtime สูงกว่ามาก (CMRP CMPR-04 p.19) ดู [[Availability and OEE]]

## SMART objectives และ KPI ของ business case

- objective ที่ดีต้องเป็น **SMART**: Specific, Measurable, Achievable, Realistic, Timed ต่างจาก goal ที่กว้างและวัดไม่ได้ (CMRP CMPR-03 p.31-33)
- ตัวอย่าง objective ในสไลด์: ลด downtime ของ critical mechanical equipment จาก 3% เหลือ 2% ภายในกำหนดเวลา โดยหน่วยงานที่ระบุ ผ่านโปรแกรม RCFA (CMRP CMPR-03 p.34) ดู [[Root Cause Analysis]]
- ขั้น implementation ต้องมี KPI ของตัวเอง (CMRP CMPR-04 p.3-4) หลักการออกแบบ KPI (target, warning/action limit, owner) อยู่ที่ [[Maintenance KPIs]] ซึ่ง ISO 14224 ก็แนะนำให้ KPI เป็นแบบ SMART

## เชื่อมกับงบประมาณและโมเดลธุรกิจของ RBMM

- [[Maintenance Budget]] (RBMM) แยกงบลงทุนกับงบทำการ งานปรับปรุง (Improvement Maintenance, Modification) เป็นงบลงทุนที่ค่าเสื่อมนับเป็นต้นทุนผลิต (RBMM p.277-278) และตั้งเมื่อ Scheduled PM แก้ปัญหาเครื่อง criticality A ไม่ได้ (RBMM p.318) business case คือเครื่องมือขออนุมัติงบประเภทนี้ ไม่ขัดกัน
- การเลือกว่าจะลงทุนยก reliability ของชิ้นไหนให้ระบบถึงเป้าด้วยต้นทุนต่ำสุด ดู [[Reliability Allocation]] (cost/penalty function, CMPR-04/05)
- ทางเลือก redundancy เทียบกับการยก reliability ชิ้นเดียว ดู [[Redundancy and Standby Systems]]
- business case ใช้กับการตัดสินใจลงทุนรายโครงการ ส่วนโครงสร้างธุรกิจของหน่วยงานบำรุงรักษา (cost center, profit center) อยู่ที่ [[Maintenance Business Models]]

## Triplets

- [[Maintenance Business Case]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-04 p.1-5; CMPR-03 p.49-50)
- Confirm the Opportunity [step_of:: [[Maintenance Business Case]]] step 1, sponsor approval
- Analyze and Shortlist Options [step_of:: [[Maintenance Business Case]]] step 2, 3-4 options, comparison matrix
- Evaluate Options [step_of:: [[Maintenance Business Case]]] step 3
- Implementation Strategy [step_of:: [[Maintenance Business Case]]] step 4
- Recommendation and Approval [step_of:: [[Maintenance Business Case]]] step 5
- Follow-up [step_of:: [[Maintenance Business Case]]] step 6
- Evaluate Options [uses:: Discounted Cash Flow] DCF named, no formula in slides (CMRP CMPR-04 p.2-3)
- Evaluate Options [uses:: Hurdle Rate] minimum IRR, no formula in slides
- Evaluate Options [uses:: Scenario Analysis]
- Recommendation and Approval [uses:: Cost of Not Proceeding] (CMRP CMPR-04 p.4-5)
- [[Maintenance Business Case]] [differs_from:: Business Plan] single project investment decision vs whole-business long-term plan (CMRP CMPR-03 p.49-50)
- CMRP Business Case Steps CMPR-03 [differs_from:: CMRP Business Case Steps CMPR-04] 5 steps vs 6 steps, page uses CMPR-04
- SMART Objective [input_to:: [[Maintenance Business Case]]] Specific, Measurable, Achievable, Realistic, Timed (CMRP CMPR-03 p.33)
- Implementation Strategy [uses:: [[Maintenance KPIs]]] implementation KPIs (CMRP CMPR-04 p.3-4)
- [[Maintenance Business Case]] [applies_to:: Improvement Maintenance] capital budget item (RBMM p.277-278)
- [[Maintenance Business Case]] [related_to:: [[Maintenance Budget]]] capital vs operating budget
- [[Maintenance Business Case]] [related_to:: [[Reliability Allocation]]] lowest-cost reliability investment
- [[Maintenance Business Case]] [related_to:: [[Availability and OEE]]] oil platform accepts higher cost for availability (CMRP CMPR-04 p.19)
- Cost of Not Proceeding [related_to:: Risk Cost] interpretation; risk cost = probability x penalty (CMRP CMPR-03 p.13) [confidence:: low]
- Evaluate Options [uses:: [[Engineering Economics and Time Value of Money]]] NPV, IRR, payback, WACC formulas (MPM p.265-277)
- Discounted Cash Flow [depends_on:: WACC] discount rate, example 5.10% (MPM p.269-271)
- Hurdle Rate [related_to:: Internal Rate of Return] IRR = rate where NPV = 0 (MPM p.272)
- [[Maintenance Business Case]] [related_to:: [[Life Cycle Cost and Life Cycle Profit]]] equipment selection by LCC/LCP (MPM p.37-46)

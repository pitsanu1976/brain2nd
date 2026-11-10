---
title: ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)
created: 2026-11-10
updated: 2026-11-10
type: concept
tags: [kpi, arms, backlog, availability, reliability, internal-standard, scorecard]
sources: [arms-kpi-standard-kpp-0002.md]
confidence: high
contested: false
---

# ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)

มาตรฐานวัดผล **Asset Reliability and Maintenance Management System (ARMS)** ของ Valeura, Rev **R8 (ส.ค. 2026)** — 15 ดัชนี พร้อมนิยาม tolerance แหล่งข้อมูล และ scorecard ให้คะแนน 5 ระดับ ใช้รายงานรายเดือนต่อ Production Manager

คู่กับ [[Valeura Maintenance Philosophy]] (นโยบาย) — เอกสารนี้คือ "ไม้วัด"; หลักวิชาเบื้องหลังดู [[Maintenance KPIs]]

## 1. โครงสร้างการกำกับ

| บทบาท | หน้าที่ |
|---|---|
| Production Manager | Owner — อนุมัติ, ออก Rev, กำกับการใช้ทั่วทุกสินทรัพย์ |
| Team Leader, Maintenance | Custodian — ชี้ข้อบกพร่อง/โอกาสปรับปรุง, ดูแล revision register |
| Production Manager + Operation Managers + maintenance team lead | ทบทวน **รายเดือน** และตั้งเป้ารายสินทรัพย์จาก baseline หรือ benchmark |

**กติกาสำคัญ:** KPI แบ่งเป็น **CONTROL** (ตกเป้าแล้วทีม offshore + onshore ต้องสอบสวนและส่ง action plan รายเดือน) กับ **MONITOR** (เฝ้าแนวโน้ม) และทุกตัวระบุว่าเป็น **LEADING** หรือ **LAGGING** — เอกสารย้ำว่าให้เน้น leading เพื่อให้ lagging บรรลุได้อย่างปลอดภัย

## 2. นิยามที่ต้องแม่นก่อนใช้

- **BACKLOG** = งานที่ยังไม่เสร็จหรือกำลังทำ และเลย target complete date แล้ว → วัด "ของที่ค้าง"
- **PM OVERDUE COMPLIANCE** = งานที่ **เสร็จแล้ว** แต่ช้ากว่า tolerance → วัด "ความตรงเวลา"

สองตัวนี้คนละอย่างและต้องรายงานคู่กัน ไม่งั้นตัวเลขจะขัดกันเอง (backlog ต่ำแต่ overdue สูง)

## 3. สิบห้าดัชนีและ tolerance

| # | KPI | ชนิด | เกณฑ์ |
|---|---|---|---|
| 1 | % SCE PM backlog | CONTROL, LEADING | ปิดภายใน **1 เดือน** จาก target date |
| 2 | % PM backlog HIGH criticality | CONTROL, LEADING | 1 เดือน |
| 3 | % PM backlog MEDIUM criticality | MONITOR, LEADING | **3 เดือน** |
| 4 | % SCE PM overdue compliance | CONTROL, LEADING | เสร็จช้ากว่า 1 เดือน |
| 5 | % PM overdue compliance HIGH | CONTROL, LEADING | 1 เดือน |
| 6 | % PM overdue compliance MEDIUM | MONITOR, LEADING | 3 เดือน |
| 7 | % SCE PM backlog overdue | CONTROL, LEADING | ค้างและเลย 1 เดือน |
| 8 | % CM/BM overdue compliance SCE + HIGH | CONTROL, LEADING | ปิดภายใน **3 เดือน**; ถ้า SCE เสียสมรรถนะ → deviation control จนกลับปกติ |
| 9 | % maintenance manpower utilization | MONITOR, LEADING | man-hour = **wrench time เท่านั้น**; available 8 ชม./คน/วัน |
| 10 | % material usage vs plan | MONITOR, LAGGING | เป้า **> 90 %** ของวัสดุที่วางแผน |
| 11 | PM : CM/BM ratio (SCE + HIGH) | MONITOR | ไม่มี target band — ใช้ดูสัดส่วนทรัพยากร |
| 12 | % production deferment จาก unplanned downtime | CONTROL, LAGGING | รายงานรายเดือน + ใช้หา bad actor |
| 13 | % maintenance budget | CONTROL, LAGGING | อยู่ใน approved BWP; เป้าที่ต้องการ **ต่ำกว่า BWP 10 %** |
| 14 | % availability | MONITOR, LAGGING | เวลาพร้อมใช้งาน |
| 15 | Reliability (λ = 1/MTBF) | MONITOR, LAGGING | MTBF สูง = λ ต่ำ = reliability สูง |

**แหล่งข้อมูล:** Oracle — MP backlog work order & history report (กรอง PM/CM/BM + criticality), financial report (งบ), field downtime report (deferment) แหล่งเดียวกับที่ [[Work Order Lifecycle]] เก็บสถานะ

## 4. Scorecard

**Maintenance KPI = 0.5 × Workorder Performance + 0.5 × Asset Performance Management** (เต็ม 5 คะแนน)

- **Workorder Performance** = (2·PMB SCE + 2·PMB Hi + 1·PMB Me + 2·PMO SCE + 2·PMO Hi + 1·PMO Me + 2·PMBO SCE + 1.5·CMO SCE/Hi) ÷ 13.5
- เกณฑ์ทุกตัว: ≤1 % = 5 | 1–3 % = 4 | 3–4 % = 3 | 4–5 % = 2 | >5 % = 1
- **Asset Performance** = 0.5 × Availability + 0.5 × Reliability
- Availability/Reliability คำนวณเฉพาะ 4 อุปกรณ์: Generator (น้ำหนัก 3), Water Injection (2), Crane (3), Air Compressor (2) ÷ 10
- Availability: ≥95 % = 5 | 90–95 % = 4 | 80–90 % = 3 | 60–80 % = 2 | <60 % = 1
- Reliability ใช้ failure rate ของ 4 อุปกรณ์เดียวกัน (≤0.002 = 5 … >0.005 = 1)

**ผลต่อการบริหาร:** น้ำหนักของ SCE (2) สูงกว่า MEDIUM (1) และงาน CM overdue ของ SCE/HIGH ได้ 1.5 — สะท้อนลำดับความสำคัญด้านความปลอดภัย แต่ก็ทำให้คะแนนรวมแกว่งตาม SCE เพียงไม่กี่ใบ

## 5. ข้อบกพร่องที่พบในมาตรฐาน (ต้องแก้ก่อนใช้ตัดสินคน)

1. **% SCE PM backlog overdue นิยามผิดมิติ** — เศษเป็นงาน "ยังไม่เสร็จ" แต่ส่วนเป็น "งานที่เสร็จแล้วทั้งปี" → ค่าเกิน 100 % ได้ ควรเปลี่ยนส่วนเป็นงาน SCE PM ที่ครบกำหนดในปี
2. **ช่วงคะแนน Reliability มีรูและซ้ำ** — Fair กับ Good ใช้ช่วง 0.004–0.005 เหมือนกัน และไม่มีช่วง 0.003–0.004 → ค่าที่ตกช่วงนี้ให้คะแนนไม่ได้
3. **Reliability = 1/MTBF สมมติ exponential** — ใช้ได้กับ failure แบบสุ่ม; อุปกรณ์ wear-out (β > 1) จะอ่านค่าผิดทาง ควรเสริม Weibull/β หรือ B10 ดู [[Weibull Analysis]]
4. **Backlog คิดเป็น % ของงานที่ครบกำหนดในเดือน** — 4 % ที่งานครบกำหนดน้อยดูดีทั้งที่ของค้างเป็นร้อยใบ ควรคู่กับจำนวน/ชั่วโมง absolute
5. **ไม่มี KPI วัดคุณภาพของ PM** — วัด "ทำครบ" ไม่ได้วัด "ทำถูก/ได้ผล" (ไม่มี repeat failure, rework, PM yield)
6. PM:CM ratio ไม่มีเกณฑ์คะแนน — ถ้าจะใช้บริหารต้องมี target band
7. สูตรในต้นฉบับเป็น **equation object** (อ่านด้วยเครื่องไม่ได้) — ต้องเปิด Word ดูต้นฉบับ

## 6. ใช้งานร่วมกับเอกสารอื่น

- [[Valeura Maintenance Philosophy]] — นโยบายที่ KPI เหล่านี้วัด (bad actor 500 ชม./ไตรมาส อยู่นอกชุด KPI นี้ เป็นการวิเคราะห์แยก)
- [[Maintenance Inventory Control SOP (TH-GEN-PROD-162)]] — KPI คลังอะไหล่ (line fill, stock-out, inventory % GPI) เป็นคนละชุด ต้องรายงานคู่กันไม่ให้ขัด
- [[Maintenance Backlog and Schedule Compliance]] — ทฤษฎี backlog/schedule compliance
- [[Reliability Metrics]] — MTBF, availability, failure rate

## ดูเพิ่ม

- [[Maintenance KPIs]] — ชุดดัชนีตาม RBMM/ISO 14224/MPM เพื่อเทียบว่า ARMS ครอบอะไรและขาดอะไร
- [[Work Order Lifecycle]] — ที่มาของข้อมูล WO ใน Oracle
- [[Maintenance Planning and Scheduling]] — ตัวขับเคลื่อน backlog

## Triplets

- [[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]] [has_value:: 15] KPIs, mix of CONTROL/MONITOR and LEADING/LAGGING
- [[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]] [has_value:: 3] overdue tolerance: 1 month for SCE/HIGH PM, 3 months for MEDIUM PM and CM/BM
- [[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]] [depends_on:: [[Work Order Lifecycle]]] data from Oracle MP backlog and history reports
- [[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]] [uses:: scorecard] Maintenance KPI = 0.5 workorder performance + 0.5 asset performance
- [[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]] [applies_to:: [[Valeura Maintenance Philosophy]]] measures the policy defined in PHI-0001
- Reliability metric [differs_from:: [[Weibull Analysis]]] ARMS uses failure rate 1/MTBF assuming exponential, no beta
- [[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]] [has_value:: 90] percent target for material usage versus plan
- Maintenance budget KPI [has_value:: 10] percent below approved business work plan is the desired target

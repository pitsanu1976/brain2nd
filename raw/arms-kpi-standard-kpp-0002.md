---
title: ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)
created: 2026-11-10
updated: 2026-11-10
type: source
tags: [internal-standard, kpi, arms, backlog, availability, reliability]
sources: []
confidence: high
contested: false
provenance: internal
verbatim_sha256: ad11ea892124a7b2da7269507f34587cbaa51b9617d5b50b27ba5aa10bbfff13
doc_number: TH-GEN-MT-GE-KPP-0002
revision: R8 (Aug 2026)
---

# ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)

**อะไร:** มาตรฐาน KPI ของ Asset Reliability and Maintenance Management System (ARMS) Valeura — กำหนด 15 ดัชนี นิยาม แหล่งข้อมูล ความคลาดเคลื่อนที่ยอมรับได้ (tolerance) และ scorecard ให้คะแนน 5 ระดับ สำหรับใช้รายงานรายเดือนต่อProduction Manager

**สถานะไฟล์:** เอกสารภายใน **ไม่ขึ้น repo สาธารณะ** — `.docx` เก็บที่ `/opt/data/home/docs_incoming/TH-GEN-MT-GE-KPP-0002 Rev R8.docx` (713,116 bytes, sha256 `ad11ea89…bfff13`); ไฟล์นี้เป็น paraphrase

**วิธีอ้าง:** `(ARMS KPI §% SCE PM BACKLOG)`

**Revision:** R1 พ.ย. 2016 → R7 ก.ค. 2023; **R8 ส.ค. 2026 เพิ่ม Availability & Reliability และปรับ KPI เดิม** (originator: Pitsanu P.)

**ผู้รับผิดชอบ:** Owner = Production Manager (อนุมัติ/ออกRev/กำกับ); Custodian = Team Leader, Maintenance (หาโอกาสปรับปรุง/ดูแล revision register); ทบทวนรายเดือนโดย Production Manager + Operation Managers + maintenance team lead

## โครงสร้าง KPI

- **CONTROL** = ถ้าต่ำกว่าเป้า ทีม offshore และ onshore ต้องสอบสวนและทำ action plan รายเดือน
- **MONITOR** = เฝ้าดูแนวโน้ม
- ทุกตัวมี LEADING/LAGGING กำกับ; เป้าหมายรายสินทรัพย์ตั้งจาก baseline หรือ international benchmark พร้อมแผนปรับปรุงรายปีและงบปีถัดไป

## นิยามหลัก

- **BACKLOG** = งานที่ยังไม่เสร็จ/กำลังทำ และเลย target complete date แล้ว
- **PM OVERDUE COMPLIANCE** = งานที่ **เสร็จแล้ว** แต่เสร็จช้ากว่า tolerance ที่กำหนด

## 15 KPI + tolerance

| # | KPI | ชนิด | Tolerance / เกณฑ์ |
|---|---|---|---|
| 1 | % SCE PM backlog | control, leading | งาน SCE PM ค้าง ต้องปิดภายใน 1 เดือนจาก target date |
| 2 | % PM backlog of HIGH criticality | control, leading | เช่นเดียวกับ SCE |
| 3 | % PM backlog of MEDIUM criticality | monitoring, leading | ต้องปิดภายใน 3 เดือน |
| 4 | % SCE PM overdue compliance | control, leading | นับงานที่เสร็จแต่ช้ากว่า 1 เดือน |
| 5 | % PM overdue compliance HIGH | control, leading | ช้ากว่า 1 เดือน |
| 6 | % PM overdue compliance MEDIUM | monitoring, leading | ช้ากว่า 3 เดือน |
| 7 | % SCE PM backlog overdue | control, leading | งาน SCE ที่ยังไม่เสร็จและเลย 1 เดือน |
| 8 | % CM/BM overdue compliance ของ SCE และ HIGH | control, leading | ต้องปิดภายใน 3 เดือน; ถ้า SCE เสียสมรรถนะตาม performance standard ต้องเปิด deviation control จนกลับปกติ |
| 9 | % maintenance manpower utilization | monitor, leading | man-hour ที่บันทึก = wrench time เท่านั้น (ไม่รวมงานธุรการ); available = 8 ชม./คน/วัน |
| 10 | % material usage vs plan | monitor, lagging | เป้า > 90 % ของวัสดุที่วางแผน |
| 11 | PM over CM/BM ratio (SCE + HIGH) | monitor | วัดสัดส่วนทรัพยากรที่ใช้กับงานวางแผน vs งานแก้ไข — เฉพาะ SCE/HIGH |
| 12 | % production deferment จาก unplanned downtime | control, lagging | รายงานรายเดือน, ใช้หา bad actor |
| 13 | % maintenance budget | control, lagging | อยู่ใน approved Business Work Plan; เป้าที่ต้องการ = ต่ำกว่า BWP 10 % |
| 14 | % availability | monitor, lagging | สัดส่วนเวลาที่พร้อมใช้งาน |
| 15 | Reliability (failure rate = 1/MTBF) | monitor, lagging | MTBF สูง = failure rate ต่ำ = reliability สูง |

## Scorecard (ให้คะแนน 5 ระดับ)

- Maintenance KPI = 0.5 × Maintenance Workorder Performance + 0.5 × Asset Performance Management
- **Workorder Performance** = (2·PMB SCE + 2·PMB Hi + 1·PMB Me + 2·PMO SCE + 2·PMO Hi + 1·PMO Me + 2·PMBO SCE + 1.5·CMO SCE/Hi) ÷ 13.5
- **เกณฑ์คะแนน** (ทุก KPI ด้าน backlog/overdue): ≤1 % = 5 (excellent), 1–3 % = 4, 3–4 % = 3, 4–5 % = 2, >5 % = 1
- **Asset Performance** = 0.5 × Availability + 0.5 × Reliability
- **Availability ของ critical equipment** = (3·Generator + 2·Water Injection + 3·Crane + 2·Air Compressor) ÷ 10; ≥95 % = 5, 90–95 % = 4, 80–90 % = 3, 60–80 % = 2, <60 % = 1
- **Reliability** ใช้ failure rate ของ 4 อุปกรณ์เดียวกัน น้ำหนัก 3/2/3/2

## ข้อสังเกตและข้อบกพร่องที่พบ (สำคัญ)

1. **นิยาม % SCE PM BACKLOG OVERDUE ไม่สอดคล้องมิติ** — ตัวเศษเป็น "งานที่ยังไม่เสร็จและเลย 1 เดือน" แต่ตัวส่วนเขียนว่า "total complete SCE work order ในปี" → ค่าที่ได้อาจเกิน 100 % และตีความไม่ได้ ควรแก้ตัวส่วนเป็นงาน SCE PM ที่ครบกำหนดในปี
2. **ช่วงคะแนน Reliability มีรูและซ้ำ** — ตารางให้ Fair และ Good เป็นช่วงเดียวกัน (0.004 < x ≤ 0.005) และไม่มีช่วง 0.003–0.004 → ค่าที่ตกในช่วงนี้ให้คะแนนไม่ได้
3. **Reliability = 1/MTBF เป็นสมมติฐาน exponential** — ใช้ได้กับ failure แบบสุ่มเท่านั้น; อุปกรณ์ wear-out (β>1) จะได้ตัวเลขที่ทำให้เข้าใจผิด ควรเสริม Weibull/β หรือ B10 ในรายงาน
4. **Backlog เป็น % ของงานที่ครบกำหนดในเดือน** — backlog 4 % ที่มีงานครบกำหนดน้อยจะดูดีทั้งที่มีงานค้างจริงจำนวนมาก ควรคู่กับตัวเลข absolute (จำนวน WO/ชั่วโมง)
5. **ไม่มี KPI วัดคุณภาพของ PM** — compliance วัด "ทำครบ" ไม่ได้วัด "ทำถูก/ได้ผล"; ไม่มี repeat failure, rework, หรือ PM yield → ควรเพิ่ม
6. **PM:CM ratio กำหนดเฉพาะ SCE/HIGH** ซึ่งถูกต้องตามเหตุผลในเอกสาร แต่ไม่มีเกณฑ์คะแนน (เป็น monitor เท่านั้น) — ถ้าจะใช้บริหารต้องมี target band
7. สูตรทั้งหมดในเอกสารเป็น **equation object (รูปสมการ)** ไม่ใช่ข้อความ — ต้นฉบับอ่านด้วยเครื่องไม่ได้ ต้องเปิด Word ดู; ไฟล์นี้จึงสรุปเป็นความหมาย ไม่ได้ลอกสูตรตัวเลข

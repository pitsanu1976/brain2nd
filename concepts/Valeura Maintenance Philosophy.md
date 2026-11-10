---
title: Valeura Maintenance Philosophy
created: 2026-11-10
updated: 2026-11-10
type: concept
tags: [maintenance-strategy, cmms, criticality, planning, kpi, internal-standard, governance]
sources: [valeura-maintenance-philosophy.md]
confidence: high
contested: false
---

# Valeura Maintenance Philosophy

เอกสารแม่บทของระบบบริหารงานบำรุงรักษา Valeura Energy เลขที่ **TH-GEN-MT-GE-PHI-0001 Rev 7 (พ.ค. 2023)** — กำหนดว่าองค์กร "คิด" เรื่อง maintenance อย่างไร แล้วแปลงเป็นโครงสร้าง กลยุทธ์ งานใน CMMS และตัววัด หน้านี้สรุปสาระที่ใช้ตัดสินใจได้จริง พร้อมชี้จุดที่ต้องระวัง

อ้างแบบ `(VMP §ชื่อหัวข้อ)` — เอกสารภายใน ไม่ใช่มาตรฐานสากล

## 1. ปรัชญาและวัตถุประสงค์

Maintenance เป็นส่วนหนึ่งของ life cycle ของ facility วัตถุประสงค์ 6 ข้อ: (1) HSE ตามเป้าองค์กร (2) ส่งมอบผลิตภัณฑ์ตามคุณภาพ/ปริมาณและสัญญา ด้วยต้นทุนดำเนินการต่ำ (3) รักษาความสมบูรณ์ของ well/production facility/topside (ยกเว้น x-mas tree) (4) แสวงหาโอกาสทางธุรกิจจากการจัดซื้อ (5) บรรลุเป้า reliability และ compliance (6) บรรลุ performance standard และ KPI

หลักการที่ตามมา: ทุก maintainable item ต้องมี **maintenance strategy ของตัวเอง** (ตาม TH-GEN-MT-GE-KPP-0001) โดยอิง risk-based technique + กฎหมาย; competence ของช่างเป็นปัจจัยชี้ขาด; **planning ต้องทำให้งานเสร็จถูกต้องตั้งแต่ครั้งแรกและทันเวลา**

## 2. ขอบเขต — สิ่งที่ maintenance ไม่ได้ทำ

Piping/pressure inspection & repair → AIM; โครงสร้าง → AIM + Engineering; modification → Engineering; lifesaving + passive firefighting → HSSE; accommodation/vehicle/logistics → Logistics; IT; FSO/FPSO → เจ้าของ contractors; rental equipment → เจ้าของงาน; drilling/well service → service provider; drilling rig/BOP/ยานพาหนะ/ subsurface อยู่นอก scope เอกสาร

**ผลต่อการออกแบบ failure hierarchy:** ขอบเขตนี้ต้องสะท้อนใน asset register และการเลือก WO type ไม่ใช่ปล่อยให้ boundary ขึ้นกับคนเปิด WO

## 3. Maintainability และ standardization

Maintainability = ความสามารถในการซ่อมโดยหยุดระบบอื่น/การผลิตน้อยที่สุด นิยามคู่กับ availability (ไม่รวม planned/unplanned downtime และ ramp up/down) ปัจจัยออกแบบ 13 ข้อ ตั้งแต่กำหนดพารามิเตอร์ condition monitoring, วัสดุ/coatings กันการกัดกร่อน, เลือก equipment + vendor ที่ผ่าน function test, **standardization เพื่อใช้ spare ร่วมกัน**, accessibility, isolation, fail-safe/backup, ลด special tools, จนถึง indicator ที่เห็นความผิดปกติได้ชัด — ใช้ได้ทั้งตอน project และตอน operate ถ้าคุ้มในระยะยาว ดู [[Maintainability]]

## 4. Maintenance strategy — หลักการเลือก

- ใช้ PM, CM, BM, CBM และงาน engineering ร่วมกันเพื่อลด unpredictable failure
- ตัวกำหนดคือ **criticality และ failure consequence** ไม่ใช่ความเคยชินหรือ vendor package
- **CBM ถูกระบุว่าพึงปรารถนากว่า intrusive maintenance** เพราะงานบำรุงรักษาเองเป็นอันตราย (isolation, ไฟฟ้า, ยกของ, เสียง) — ลดการรื้อโดยไม่จำเป็น
- CBM = first line maintenance, function test, inspection, vibration, lube oil analysis ฯลฯ และต้องกำหนด parameter + เกณฑ์ให้จับ early failure ได้
- intrusive maintenance ทำเมื่อมีข้อกำหนดกฎหมาย/risk-based analysis/warranty ของผู้ผลิต
- **criticality ต่ำ + ต้นทุนบำรุงสูง → ลด PM หรือ run-to-failure** เหลือแค่ basic maintenance (greasing, visual, tightening, cleaning)
- **CM ที่ความเสี่ยงสูงต้องแก้ root cause** ไม่ใช่แค่คืนสภาพ (5 Whys, fishbone, fault tree) — ตรงกับ [[Root Cause Analysis]]

## 5. ประเภทงาน 7 รหัส (Maintenance Types)

| Code | ชื่อ | ใช้เมื่อ | ตัวอย่าง |
|---|---|---|---|
| **BM** | Breakdown Maintenance | หลัง absolute failure / สูญเสีย primary function ทั้งหมด | ปั๊มติด ไม่มี flow; เพลากวนหัก |
| **CM** | Corrective Maintenance | หลังตรวจพบ fault แต่ **ยังไม่ต้องทำทันที** — จัดตารางได้ | มอเตอร์สั่นสูง; ปั๊ม flow ต่ำ; วาล์วรั่ว |
| **PM** | Preventive Maintenance | ตามรอบ/เกณฑ์/vendor และรวม function test, calibration, inspection เพื่อจับ **hidden failure** | overhaul compressor, เปลี่ยน bearing, calibration, SIL function test, explosion-proof inspection |
| **CB** | Condition Based | วัดพารามิเตอร์เพื่อวินิจฉัยสภาพ | vibration, lube oil, thermography, borescope, performance analysis, UT |
| **RE** | Refurbishment | คืนสภาพเมื่อ **ต้นทุน < 70 % ของของใหม่** หรือ lead time ของใหม่ยาวจนกระทบ uptime | overhaul ปั๊ม, rebuild winch |
| **IN** | Inspection | ตรวจความสมบูรณ์ของ static equipment | pressure equipment, piping, subsea structure |
| **MO** | Modification | เปลี่ยนฟังก์ชัน/ปรับปรุงสมรรถนะ — **ต้องมี MOC อนุมัติก่อน** | เปลี่ยน mesh filter, เพิ่ม interlock |

**ข้อควรระวังเชิงระบบ (สำคัญกับงาน CMMS):** "maintenance type" ของเอกสารนี้ผสม 2 มิติเข้าด้วยกัน — *สาเหตุ/จังหวะที่ทำงาน* (BM/CM/PM/CB) กับ *ลักษณะงาน* (RE/IN/MO) ขณะที่ ISO 14224 Table B.5 แยกเป็น **activity** 12 รหัส (Replace, Repair, Modify, Adjust, Refit, Check, Service, Test, Inspection, Overhaul, Combination, Other) และ Oracle eAM แยกเป็น **WO type** (Routine, PM, Rebuild, Easy) + `MTL_EAM_ACTIVITY_TYPE`

ถ้าจะทำให้ข้อมูลวิเคราะห์ได้ ต้องแมปให้ชัด เช่น BM/CM → activity Repair/Replace; PM → Service/Test/Inspection/Overhaul; CB → Inspection/Test; RE → Overhaul; IN → Inspection; MO → Modify + MOC — ดู [[Failure Hierarchy]] และ `data/oracle-eam/maintenance_activity_codes.csv` ห้ามใช้ field เดียวเก็บทั้ง "ทำไม" และ "ทำอะไร"

## 6. Equipment criticality

ทุก equipment ใน CMMS ต้องมี criticality จาก **consequence × probability** ตาม risk matrix ของบริษัท ครอบ safety, environment, production, property cost, reputation + พิจารณา redundancy, utilization, operating context

- high critical → ใช้ risk-based technique เพิ่ม: **RCM (rotating)**, **SIL (instrument)**, **RBI (static/pressure)**
- equipment ที่ failure แล้วผลกระทบสูง เช่น **diesel generator, process pump** ต้องมี **recovery plan** และ call-off contract ต้องพร้อมใช้ตลอด operate phase
- SCE ต้อง flag ชัดใน CMMS
- เกณฑ์ละเอียดอยู่ใน TH-GEN-MT-GN-GUI-0001 (ยังไม่ ingest) — ดู [[Criticality Assessment]] สำหรับวิธีเชิงปริมาณ

## 7. Instrument calibration ตาม criticality

| Criticality | งานขั้นต่ำ | ความถี่ |
|---|---|---|
| SCE | sensor + transmitter calibration + loop test ถึง SIS | ปีละครั้ง หรือตาม SIL proof-test interval |
| HIGH | sensor + transmitter calibration (+ loop test ถ้ามี) | ปีละครั้ง หรือตาม SIL |
| Medium | transmitter calibration | 3–5 ปี หรือตาม vendor |
| Low | run to failure | – |

ฟอร์ม calibration ตาม TH-GEN-MT-IN-PRC-0003 ต้องเซ็นโดย supervisor และแนบใน WO — ตัวอย่างของการบังคับ evidence ใน CMMS

## 8. Maintenance plan และการจัดตาราง

**กฎที่มักถูกมองข้าม:** ในช่วง **warranty** แผนต้องอิง **คำแนะนำผู้ผลิต + statutory เท่านั้น**; RCM/FMECA/RBI/SIL เริ่มใช้ได้หลังพ้น warranty — เป็นข้อจำกัดเชิงสัญญา ไม่ใช่หลักวิศวกรรม (ดูข้อ 12)

แผนต้องระบุ 4W: what (task, scope, tools, spares), where (tag/maintainable item), when (ความถี่ + ระยะเวลา), who (discipline + จำนวนคน); "how" อยู่ใน procedure แยก

- **Statutory maintenance** ต้องมีลำดับความสำคัญและบันทึกใน CMMS พร้อมใบรับรองจาก verifier แนบ WO เพื่อ audit
- **Weekly schedule** จัดโดย offshore planner เรียงตาม integrity, criticality, accessibility, กฎหมาย, production, condition, resource, งาน opportunistic, และอายุ backlog
- **Shutdown 4 ระดับ:** not required (ผลิตเต็ม) / unit (ผลิตเต็ม) / platform (ผลิตบางส่วน) / field (หยุดทั้งหมด); งานที่ต้องแยกเตรียมล่วงหน้า **≥ 2 เดือน** และทุก WO ต้องระบุ shutdown type
- ดู [[Maintenance Planning and Scheduling]], [[Turnaround Management]]

## 9. Backlog และ overdue governance

overdue = เกิน expected complete date และนับเป็น backlog; **เปลี่ยนวันที่ได้เฉพาะ planner หรือ maintenance supervisor**; ถ้าเกิน threshold ที่เกี่ยวกับ regulatory compliance ต้องออก **deviation control** อนุมัติโดย asset owner พร้อม risk assessment — เป็นการควบคุมที่เข้มกว่าหลายองค์กร ดู [[Maintenance Backlog and Schedule Compliance]]

## 10. Spares 3 ประเภท

| ประเภท | ลักษณะ | การจัดการ |
|---|---|---|
| **Commissioning spares** | ใช้ช่วง construction/commissioning (gasket, fastener, seal, filter) + cover infant failure | ซื้อพร้อม equipment |
| **Operating spares** | ชิ้นส่วนใช้งานตามแผน/สึกหรอ — **รวมทั้งชุดปั๊ม/transmitter/valve สำรอง** | min/max ภายใต้ warehouse; อุปกรณ์ใหม่ตั้งต้น **2 ปี** |
| **Critical spares** | lead time ยาว ราคาสูง failure แล้วกระทบ production/safety มาก (ปั๊มทั้งชุด, mechanical seal, heat exchanger, crane winch/cylinder) | insurance spare, ระบุและจัดการใน CMMS |

- ตัดสิน **ซ่อม vs เปลี่ยน** จากต้นทุนซ่อม + risk cost เทียบ replacement cost
- **Rebuildable spares** ต้องระบุใน Equipment Maintenance Plan, เก็บเป็น rebuildable grade, ซ่อมที่ location ที่คุ้มที่สุด, มี QC + functional test + certificate
- ดู [[Spare Parts Management]], [[Maintenance Inventory Control SOP (TH-GEN-PROD-162)]]

## 11. งบประมาณและ KPI

- ต้นทุนซ่อมเก็บผ่าน CMMS: inventory allocation + direct purchase; account code ผูกกับ asset number (812510–812590); วัสดุคงคลังอยู่ที่ **14001 suspended CAPEX** และตัดเป็น expense เมื่อเบิกเข้า WO
- KPI ตัวอย่าง: SCE backlog, high-critical equipment availability, plant availability, maintenance cost, ตำแหน่ง safety-critical ที่ว่าง, **PM/CM ratio**, จำนวน deviation control — ต้องมีทั้ง leading และ lagging
- **Bad actor analysis รายไตรมาส** — เกณฑ์: criticality SCE/High/Medium + downtime สะสม > **500 ชั่วโมงต่อเครื่องในไตรมาส** + WO type corrective/breakdown; action ติดตามใน Maintenance Action Tracking
- ดู [[Maintenance KPIs]], [[Maintenance Budget]]

## 12. Audit, obsolescence, ageing

- ทบทวนแผน maintenance & inspection **ทุก 3 ปี** ด้วยประวัติโรงงาน + service bulletin + FMECA/RAM/SIL/RBI/RCM
- ทบทวน obsolescence **ทุก 5 ปี** โดยใช้ failure rate จาก CMMS + ข้อมูล vendor และสะท้อนใน CAPEX
- Ageing asset: แยก **material degradation** (เสื่อมสภาพ/เปลี่ยนสภาวะใช้งาน → replace หรือ overhaul ตาม lead time, capability, cost, field life) กับ **obsolescence** (อะไหล่ critical เลิกผลิต/ข้อกำหนดเปลี่ยน → เปลี่ยนทั้งชุด/บางส่วน/เพิ่ม stock ครอบ field life)

## 13. ระดับทักษะ 5 ชั้น

| ระดับ | ใคร | งาน |
|---|---|---|
| 1 | Operator / junior | first-line: ตรวจด้วยตา, หล่อลื่น, เติมน้ำมัน, ขัน, ทำความสะอาด, อ่านเกจ |
| 2 | Skilled maintainer | PM รายเดือน–ปี, ใช้เครื่องมือมาตรฐาน, เปลี่ยนแบบ like-for-like |
| 3 | Specialized maintainer | งาน intrusive: overhaul, ถอดตรวจ, ต้องใช้ special tool/workshop |
| 4 | Manufacturer / certified contractor | เทคนิคเฉพาะ, งานที่ต้องใบรับรอง (pressure vessel, FM200, explosion-proof) |
| 5 | Regulatory maintainer | ตรวจรับรองตามกฎหมาย เช่น lifting certification |

 Offshore core ทำได้ 1–2 และบางส่วนของ 3; 4–5 เป็น call-off service — ใช้กำหนดขอบเขตสัญญาและการวางแผน resources

## 14. ข้อสังเกตและช่องว่าง (สำคัญ)

- **ไม่มีวิธีคำนวณเชิงปริมาณ** — ไม่มี MTBF/Weibull/B10 แม้อ้าง "asset reliability target"; reliability target ไม่ถูกนิยามเป็นตัวเลข
- เกณฑ์ criticality อยู่ในเอกสารแยก (TH-GEN-MT-GN-GUI-0001) และ **Maintenance Strategy แยกเล่ม** (TH-GEN-MT-GE-KPP-0001) — ทั้งสองยังไม่ ingest; หน้านี้จึงเป็น "ปรัชญา" ไม่ใช่ "วิธี"
- **กฎ warranty (OEM + statutory only)** ทำให้ช่วง 1–2 ปีแรกของอุปกรณ์ใหม่ไม่มี PM optimization — ยอมรับได้ทางสัญญา แต่ทำให้ PM ที่ไม่สร้างคุณค่าไหลเข้าฐานข้อมูลตั้งแต่ต้น และแก้ยากภายหลัง ควรบันทึกเป็น company deviation เมื่อเทียบกับ [[PM Task Selection]]
- **bad actor threshold 500 ชม./ไตรมาส** จับได้เฉพาะ failure ก้อนใหญ่ — failure เล็กที่กระจายหลายเครื่องจะไม่ถูกจับ ควรเสริม Pareto ตาม failure mode/ข้อ 500 ชม. ปรับตามขนาดโรง
- **PM/CM ratio** เป็นตัวชี้วัดที่ตีความยาก (ratio สูงไม่ได้แปลว่าดี) — ใช้คู่กับ SCE backlog และ availability
- เอกสารไม่กล่าวถึง **rotable/repairable pool** และ **CBM program design** (เลือก parameter/เกณฑ์) — ช่องว่างที่ต้องเติมจาก RBMM/ISO 17359

## ดูเพิ่ม

- [[Maintainable Item]] และ [[Maintainability]] — นิยามและปัจจัยออกแบบ
- [[Criticality Assessment]] — วิธีให้คะแนนเชิงปริมาณ
- [[PM Task Selection]] — เลือกงานตาม failure characteristics (ใช้หลังพ้น warranty)
- [[Maintenance Planning and Scheduling]], [[Maintenance Backlog and Schedule Compliance]]
- [[Work Order Lifecycle]] — สถานะและ WO type ใน Oracle eAM
- [[Spare Parts Management]], [[Maintenance Inventory Control SOP (TH-GEN-PROD-162)]]
- [[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]] — ชุด KPI ที่วัดนโยบายหน้านี้ (Rev R8)
- [[Maintenance KPIs]], [[Maintenance Budget]], [[Root Cause Analysis]]

## Triplets

- [[Valeura Maintenance Philosophy]] [defined_in:: TH-GEN-MT-GE-PHI-0001] Rev 7, May 2023
- [[Valeura Maintenance Philosophy]] [has_value:: 7] maintenance types: BM, CM, PM, CB, RE, IN, MO
- [[Valeura Maintenance Philosophy]] [has_value:: 5] maintenance skill levels; offshore core covers 1-2 and partly 3
- [[Valeura Maintenance Philosophy]] [applies_to:: [[Maintenance Planning and Scheduling]]] weekly schedule by offshore planner, 4W plan contents
- [[Valeura Maintenance Philosophy]] [differs_from:: [[RCM Reliability Centered Maintenance]]] warranty period allows OEM and statutory tasks only, no RCM before warranty end
- Bad actor analysis [depends_on:: downtime threshold] 500 cumulative hours per equipment per quarter, criticality SCE/High/Medium
- [[Valeura Maintenance Philosophy]] [has_value:: 3] formal review of maintenance and inspection plans every 3 years; obsolescence every 5 years

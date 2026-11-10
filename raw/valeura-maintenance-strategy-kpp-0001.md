---
title: Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)
created: 2026-11-10
updated: 2026-11-10
type: source
tags: [internal-standard, maintenance-strategy, rcm, sil, rbi, cmms, spares]
sources: []
confidence: high
contested: false
provenance: internal
verbatim_sha256: 7692e80ec51f5ad235635dd3969d5be39d951394eb264d37486d47097405db14
doc_number: TH-GEN-MT-GE-KPP-0001
revision: R2 (May 2023)
---

# Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)

**อะไร:** เอกสารกลยุทธ์ ระดับองค์กร — กำหนดว่าจะเลือกใช้เครื่องมือ/กระบวนการใดในการสร้าง maintenance program ของแต่ละสินทรัพย์ (OEM manual, criticality, RCM, SIL, RBI, SIB, CMMS, CBM, RCFA, spares, audit) เป็นชั้นกลางระหว่าง [[raw/valeura-maintenance-philosophy]] (นโยบาย) และ [[raw/arms-kpi-standard-kpp-0002]] (ตัววัด)

**สถานะไฟล์:** เอกสารภายใน **ไม่ขึ้น repo สาธารณะ** — `.docx` เก็บที่ `/opt/data/home/docs_incoming/TH-GEN-MT-GE-KPP-0001 MAINT STRAGETY.docx` (750,657 bytes, sha256 `7692e80e…05db14`); ไฟล์นี้เป็น paraphrase

**วิธีอ้าง:** `(VMS §RCM)`, `(VMS §Spare Part Management)`

**Revision:** R1 เม.ย. 2016 → **R2 พ.ค. 2023** (ปรับชื่อบริษัทและทบทวนเนื้อหา)

## โครงสร้างเอกสาร (17 หัวข้อ)

Purpose → Scope & objectives (6 ข้อ) → Reference (risk matrix) → Maintenance Strategy (รายการกระบวนการ 14 ข้อ + OEM manual) → Criticality Analysis → RCM → SIL → RBI → CMMS → CBM → RCFA → Central planning → Spare part management → Pre-startup audit → Implementation → Onshore support → SCE → People & training → KPIs

## สาระสำคัญ (paraphrase)

**หลักการ:** strategy = กระบวนการ optimize แบบ risk-based จากความสำคัญของ equipment และ consequence ของ failure; เอกสารนี้เป็น high-level — guideline/ขั้นตอนเฉพาะของแต่ละ facility พัฒนาแยกและควบคุมใน CMMS

**กระบวนการที่ใช้สร้าง strategy (อย่างน้อยหนึ่งอย่าง):** OEM manual เป็นขั้นต่ำ | criticality assessment | RCM สำหรับ SCE/high | SIL สำหรับ instrument protective | RBI (API 580) สำหรับ piping/vessel/tank | structural integrity management (topside/platform/subsea) | CMMS (Oracle) | condition monitoring program | RCA | onshore support ดูแล CMMS master data | critical-spares ตาม criticality | inventory optimization | continuous improvement + audit + KPI

**OEM manual:** ใช้เป็น minimum ในช่วง warranty และใช้เป็น strategy ของ equipment criticality ต่ำ — effort เชิงลึกสงวนไว้ให้ SCE/high เท่านั้น

**Criticality → run-to-failure** เมื่อต้นทุน consequence ต่ำกว่าต้นทุนบำรุงรักษา และอาจนำไปสู่การถือ spare ครบชุดถ้าคุ้ม

**RCM:** ใช้กับ equipment ซับซ้อนที่สร้างความเสี่ยงสูง โดยเฉพาะ **rotating equipment** ผลลัพธ์มักออกมาเป็นงาน CBM มากกว่า PM แบบเดิม

**SIL:** กำหนด reliability ของ protective device; drive การจัดซื้อตอน project และ **proof-test interval** ตอน operate — loop test/calibration ของ input device, ESD cause & effect test ของ controller, SDV stroke test + วัด closure time ตอน ESD

**RBI:** กระบวนการ dynamic ที่อัปเดตตามสภาวะ process และประวัติ ผลกระทบที่สนใจคือ loss of containment จากการกัดกร่อน/สูญเสียวัสดุ; ใช้ API 580; ขอบเขต topside piping, pressure vessel, storage tank

**CMMS (Oracle) ต้องมี:** asset register ตาม P&ID (รวม package P&ID), asset criticality ทุกตัว, PM plan (task, interval, spare, manpower), BOM 2 ระดับ (equipment BOM + activity BOM) เพื่อให้ WO ที่ออกจาก standard activity ผูกวัสดุอัตโนมัติและพยากรณ์วัสดุล่วงหน้าเพื่อต่อรองราคา

**CBM เป็นงานที่บริษัทให้ความสำคัญอันดับแรก** — ลด man-hour, ลด spare สำหรับ intrusive inspection, ลด downtime; เทคนิค: oil analysis, vibration, thermography, **motor current analysis**, performance monitoring; ต้องมาจากผล RCM

**RCFA:** สำหรับ failure ซ้ำหรือ failure เดี่ยวที่ consequence สูง; เครื่องมือ 5 whys, fault tree, incident timeline; ผลลัพธ์แก้ได้ 3 ทาง — เปลี่ยน strategy, modify equipment, design out (เทียบ risk กับเงินลงทุน)

**Central planning:** ทุกงานต้องมี WO และอนุมัติโดย maintenance supervisor ก่อนลงมือ; ปิดงานโดยช่างแล้ว verify โดย supervisor; วัสดุเบิกจาก WO เท่านั้น (ทั้ง stock และ direct purchase); ประชุม look-ahead **30 และ 90 วัน** เพื่อจับงานที่ต้องใช้ external resource/long-lead spare และ refine **7 วัน**; เป้า planned work overdue = **0 %**

**Spares:**
- อะไหล่ที่อยู่ใน PM program **ต้องเป็น stock item** และตั้ง min-max จาก consumption rate ที่ simulate จาก look-ahead ใน CMMS
- อะไหล่นอก PM program: ตัดสินจาก failure mode + criticality + ประวัติใน CMMS + RCM + RCFA + คำแนะนำผู้ผลิต
- ไม่มี workshop offshore → assembly ต้องซ่อม onshore ที่ร้าน contractor และต้องมี **swing unit ครบชุด** ระหว่างรอ refurbish: crane winch, crane luffing cylinder, process/utility pump, diesel engine, **electrical generator**, engine radiator, fuel pump, water pump

**Pre-startup audit (Pre-ORR):** ตรวจ 13 หัวข้อ (strategy, competency, CMMS, planning, resource leveling, KPI, contracts, availability target, CI, failure investigation, spares, HSE compliance, audit program) โดยผู้ตรวจอย่างน้อยต้องเป็น maintenance professional ที่เป็นอิสระจากทีม offshore

**SCE:** master register ใน CMMS ต้องตรงกับ SCE identification report; ผลงาน SCE เข้า asset KPI รายเดือน; การเลื่อน/ยกเว้นงาน SCE ต้องอนุมัติโดยผู้มีอำนาจพร้อม risk assessment ผ่าน deviation control

**People:** competency matrix + refresh interval/ใบรับรองสำหรับงานเสี่ยงสูง

**KPI ขั้นต่ำที่ระบุ:** SCE PM backlog, SCE PM backlog overdue, PM backlog, PM backlog overdue, CM work lead time, maintenance cost — **รายการในต้นฉบับจบกลางคันที่คำว่า "Maintenance cost,"** (เอกสารขาดรายการที่เหลือ)

## ข้อสังเกตของผู้ ingest

- เอกสารนี้ **ไม่ระบุวิธีเลือก task ราย failure mode** (นั่นอยู่ที่ RCM/PM Task Selection) — เป็นกรอบ "ใช้เครื่องมืออะไรกับ equipment กลุ่มไหน"
- ไม่มีตัวเลข tolerance/เป้า (อยู่ที่ [[raw/arms-kpi-standard-kpp-0002]] และ [[raw/valeura-maintenance-philosophy]])
- KPI list ขาดกลางคัน — ควรอ้างอิง KPP-0002 แทนเมื่อต้องใช้รายการเต็ม
- ไม่กล่าวถึง **rotable pool** แยกจาก swing unit และไม่กล่าวถึง **spare part criticality classification** (อยู่ที่ SOP 162)

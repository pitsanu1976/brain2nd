---
title: Valeura Maintenance Philosophy (TH-GEN-MT-GE-PHI-0001)
created: 2026-11-10
updated: 2026-11-10
type: source
tags: [internal-standard, maintenance-philosophy, strategy, cmms, criticality, kpi]
sources: []
confidence: high
contested: false
provenance: internal
verbatim_sha256: 3fb118eee9cdaca99d4121fd8f2d50d39b4d7dca4e22fd3d0c5524f2a899a6f9
doc_number: TH-GEN-MT-GE-PHI-0001
revision: R7 (May 2023)
---

# Valeura Maintenance Philosophy (TH-GEN-MT-GE-PHI-0001)

**อะไร:** เอกสารแม่บท (governing document) ของระบบบริหารงานบำรุงรักษา Valeura Energy — กำหนดปรัชญา ขอบเขต โครงสร้างความรับผิดชอบ กลยุทธ์ ประเภทงาน แผนงาน CMMS criticality spares KPI audit และสมรรถนะบุคลากร

**สถานะไฟล์:** เอกสารภายใน **ไม่ขึ้น repo สาธารณะ** — `.docx` เก็บที่ `/opt/data/home/docs_incoming/TH-GEN-MT-GE-PHI-0001 MAINT PHILOSOPHY.docx` (754,649 bytes, sha256 `3fb118ee…99a6f9`); ไฟล์นี้เป็น **paraphrase + ตารางกฎ** ไม่ใช่ข้อความเต็ม

**วิธีอ้าง:** `(VMP §Maintenance Types and Schemes)`, `(VMP §Instrument and Calibration Works)`

**Revision ล่าสุด:** R7 พ.ค. 2023 (ย้ายมาอยู่ Valeura) — ก่อนหน้า R1 เม.ย. 2016; R2–R3 พ.ย. 2016 เพิ่มงาน instrument/calibration; R4 ม.ค. 2019 เพิ่ม ageing/obsolescence; R5–R6 มิ.ย. 2021 ตัด BOM ออกจาก asset register และเพิ่มเกณฑ์ bad actor (500 ชั่วโมงที่ location เดียว)

## แผนผังเอกสาร

| ส่วน | เนื้อหาที่ ingest |
|---|---|
| Purpose / Scope | วัตถุประสงค์ 6 ข้อ, ข้อยกเว้น 9 ประเภท, นิยาม shall/should/may |
| Referenced documents | TH-GEN-MT-GE-KPP-0001 Maintenance Strategy, TH-GEN-MT-GN-GUI-0001 Equipment Criticality Guideline, TH-GEN-MT-IN-PRC-0003 Instrument Calibration Procedure |
| Maintenance Philosophy | ปรัชญาและหลักการ |
| Scope of maintenance dept | สิ่งที่ maintenance ไม่รับผิดชอบ (AIM, Engineering, HSSE, logistics, IT, FSO/FPSO, rental, drilling) |
| Organization & responsibilities | 5 พื้นที่งาน + 10 หน้าที่ของ maintenance engineer |
| Design of maintainability | 13 ปัจจัยออกแบบ + นิยาม maintainability/availability + standardization/vendor selection |
| Maintenance strategy | PM/CM/BM/CBM + engineering; criticality & consequence; CBM เพื่อเลี่ยง intrusive work; RtF สำหรับ criticality ต่ำ; CM ต้องแก้ root cause |
| Maintenance types & schemes | 7 รหัสงาน (BM, CM, PM, CB, RE, IN, MO) |
| CMMS | 5 วัตถุประสงค์ของ Oracle CMMS |
| Asset register | functional location hierarchy, physical tag only, SCE flag, criticality ของ non-SCE |
| Equipment criticality | consequence × probability ตาม risk matrix + redundancy/utilization; RCM/SIL/RBI สำหรับ high critical; recovery plan |
| Instrument & calibration | ตารางความถี่ตาม criticality (SCE/HIGH/Medium/Low) |
| Planning & scheduling | mantenance plan (what/where/when/who), warranty rule, statutory, weekly schedule, shutdown 4 ระดับ |
| Task execution | compliance, backlog, overdue deviation control |
| Spares | 3 ประเภท (commissioning/operating/critical) + rebuildable + repair-vs-replace |
| Maintenance control | work order, work request approval, time writing |
| Maintenance budget | account codes 812xxx, inventory ที่ 14001 (suspended CAPEX) |
| Performance monitoring | KPI ตัวอย่าง 7 ตัว + bad actor analysis รายไตรมาส |
| Audit & review | แผนทบทวนทุก 3 ปี, obsolescence ทุก 5 ปี |
| MIS / skill level / ageing | ข้อมูล, ระดับทักษะ 1–5, material degradation vs obsolescence |

## กฎที่มีตัวเลข/เกณฑ์ชัด (paraphrase)

| หัวข้อ | กฎ |
|---|---|
| Refurbishment | ทำเมื่อต้นทุน refurbish < 70 % ของราคาของใหม่ หรือ lead time ของใหม่ยาวจนกระทบ uptime |
| Instrument calibration | SCE: sensor+transmitter calibration + loop test ถึง SIS ปีละครั้ง (หรือตาม SIL proof-test interval); HIGH: เหมือน SCE ปีละครั้ง; Medium: transmitter calibration ทุก 3–5 ปี; Low: run to failure |
| Maintenance plan | ในช่วง warranty ใช้ **คำแนะนำผู้ผลิต + statutory เท่านั้น**; RCM/FMECA/RBI/SIL ใช้ได้หลังพ้น warranty |
| Shutdown | 4 ระดับ: not required / unit / platform / field; งานที่ต้องแยกเตรียมล่วงหน้า **อย่างน้อย 2 เดือน** |
| Backlog | overdue นับจาก expected complete date; เปลี่ยนวันที่ได้เฉพาะ planner/supervisor; เกิน threshold ที่เกี่ยวกับ compliance ต้องมี deviation control อนุมัติโดย asset owner |
| Bad actor | วิเคราะห์รายไตรมาส: criticality SCE/High/Medium + downtime สะสม > 500 ชั่วโมงต่อเครื่องในไตรมาส + WO type corrective/breakdown; ติดตาม action ใน Maintenance Action Tracking |
| Spares | operating spares ตั้งต้น **2 ปี** สำหรับอุปกรณ์ใหม่ (ตาม vendor rec, interchangeability, warranty, lead time, service contract) |
| Audit | ทบทวนแผน maintenance & inspection **ทุก 3 ปี**; obsolescence **ทุก 5 ปี** |
| Skill | 5 ระดับ; offshore core ทำได้ level 1–2 และบางส่วนของ 3; level 4–5 เป็น call-off contractor |

## ข้อสังเกตของผู้ ingest

- เอกสารนี้เป็น **นโยบาย** ไม่มีวิธีคำนวณ — criticality ต้องไปดู TH-GEN-MT-GN-GUI-0001 ซึ่งยังไม่ ingest
- ระบุว่ามี TH-GEN-MT-GE-KPP-0001 **Maintenance Strategy** แยกเล่ม — ยังไม่ ingest (ช่องว่างที่ควรปิด)
- กฎ "warranty ใช้ OEM + statutory เท่านั้น" ขัดกับหลัก RCM ที่สอนใน RBMM/PETROSYNC (เลือกงานจาก failure characteristics) — เป็น **ข้อจำกัดเชิงสัญญา** ไม่ใช่ความขัดแย้งทางวิศวกรรม แต่ต้องบันทึกไว้
- ไม่มีตัวชี้วัด reliability เชิงปริมาณ (MTBF, Weibull, B10) ในเอกสาร — "asset reliability target" ถูกอ้างแต่ไม่นิยาม

---
title: "Oracle 11i Enterprise Asset Management Fundamentals — Student Guide (Vol.1 + Vol.2)"
type: raw-source
source_url: "file:///opt/data/home/Documents/brain2nd/raw/oracle-manual/eAM_TrainingMaterial_v1.pdf + eAM_TrainingMaterial_v2.pdf"
ingested: 2026-11-02
sha256_vol1: 42bf9dc292cdc57cb1fd17e98d414abfea1a882eb967ada299167b3f6f4ded5a
sha256_vol2: 0387d355f734080c0260cc9a4380849c4a1d711fd1d377bf31975f0f44ec1edd
format: PDF 2 เล่ม มี text layer (490 + 448 = 938 หน้า) → ข้อความเต็มรวม `raw/oracle_manual.md` (เก็บในเครื่องเท่านั้น) + source note นี้
immutable: true
---

# Oracle 11i Enterprise Asset Management Fundamentals — Student Guide (Vol.1 + Vol.2)

Raw source — ห้ามแก้ไขหลัง ingest (sha256 คิดจากไฟล์ PDF ต้นฉบับแต่ละเล่ม)

- หลักสูตร: **D14149GC31 · Edition 3.1 · October 2005 · Oracle University**
- เล่ม: **Volume 1** (Student Guide D22272, 490 หน้า, Chapters 1–5) + **Volume 2** (D22273, 448 หน้า, Chapters 6–20)
- รูปแบบ: สไลด์ประกอบการสอน 938 หน้า มี text layer ครบทั้งสองเล่ม → **ไม่ต้อง OCR**
- ไฟล์: `raw/oracle-manual/eAM_TrainingMaterial_v1.pdf` (6.0 MB) และ `..._v2.pdf` (6.1 MB); ข้อความเต็มรวมที่ `raw/oracle_manual.md` (895 KB)
- **มีลิขสิทธิ์ Oracle → gitignore ทั้ง PDF และข้อความเต็ม** (vault sync ขึ้น GitHub สาธารณะ)

## โครงสร้าง (Chapter → เล่ม + PDF page)

| Chapter | หัวข้อ | เล่ม | PDF page |
|---|---|---|---|
| 1 | 11i Enterprise Asset Management Overview | 1 | 19 |
| 2 | 11i Setting Up Oracle Enterprise Asset Management | 1 | 57 |
| 3 | 11i eAM Collection Plans | 1 | 263 |
| 4 | 11i eAM Work Management | 1 | 303 |
| 5 | 11i eAM Preventive Maintenance | 1 | 441 |
| 6 | 11i eAM Planning and Scheduling | 2 | 19 |
| 7 | 11i Direct Item Procurement for eAM Work Orders | 2 | 53 |
| 8 | 11i eAM Cost Management | 2 | 95 |
| 9 | 11i eAM Contractor Services | 2 | 121 |
| 10 | 11i eAM Property Manager | 2 | 143 |
| 11 | 11i eAM Service | 2 | 159 |
| 12 | 11i eAM Process and Discrete Manufacturing | 2 | 185 |
| 13 | 11i eAM Project Manufacturing | 2 | 211 |
| 14 | 11i eAM Work Order Billing | 2 | 233 |
| 15 | 11i eAM Oracle Time and Labor | 2 | 287 |
| 16 | 11i Self-Service Work Requests | 2 | 305 |
| 17 | 11i Maintenance User Workbench | 2 | 331 |
| 18 | 11i Maintenance Super User | 2 | 349 |
| 19 | 11i Stores | 2 | 417 |
| 20 | 11i eAM Reports and Processes | 2 | 439 |

## วิธีอ้างอิง

ข้อความเต็มมี marker ทุกหน้า: `<!-- vol: V | page: N | ch: C-P -->`
V = เล่ม (1 หรือ 2), N = ลำดับหน้าใน PDF ของเล่มนั้น, C-P = เลข Chapter-Page ที่พิมพ์บนสไลด์ (เช่น `4-8`)

อ้างแบบ: `(eAM 11i SG vol.1 ch.4 p.4-8)` — และเปิด PDF ประกอบเสมอเมื่อต้องดูหน้าจอ UI เพราะเป็นสไลด์ ภาพหน้าจอไม่ได้ถูกเก็บเป็นข้อความ

## ทำไมมีไฟล์นี้ใน vault

ใช้กับงาน CMMS ที่เป็น Oracle eAM/EBS: โครงสร้าง work request → work order, PM template/meter, collection plans, stores/พัสดุ, cost management, contractor services, maintenance workbench, self-service request — เป็นคู่มือเชิงปฏิบัติการ (operational) ต่างจากหนังสือ reliability ที่เป็นเชิงวิธีวิเคราะห์

Volume 1 คือส่วนที่ vault ยังขาดตอนมี Vol.2 อย่างเดียว: **Chapter 2 setup** (organization, eAM parameters, area, department, resource, asset group) และ **Chapter 4 work management** (work request/order lifecycle, operation, material, resource) ซึ่งเป็นฐานให้งาน failure hierarchy/OREDA mapping ใน Oracle

**ข้อควรระวัง:** เอกสารปี 2005 ของ Oracle 11i — เมนู/หน้าจอบางส่วนต่างจาก EBS R12 และต่างจาก Oracle Cloud EAM มาก ใช้เป็น "แนวคิดและลำดับขั้นตอน" ไม่ใช่คู่มือหน้าจอของระบบที่ใช้อยู่จริง

## ข้อสังเกต

- ชื่อผู้ถือ licence (Vichaya Jiraalongkorn) พิมพ์เป็นลายน้ำทุกหน้า — ลบออกจากข้อความที่ถอดแล้ว แต่ยังอยู่ใน PDF ต้นฉบับ
- หน้าสไลด์หลายหน้ามีแต่ภาพหน้าจอ ข้อความจึงสั้น (เช่น `Agenda`) — ไม่ใช่ข้อมูลหาย
- สารบัญรวมในแต่ละเล่มครอบคลุมบท 1–20 ทั้งหลักสูตร จึงใช้ระบุ "บทไหนอยู่เล่มไหน" ไม่ได้ — ใช้ตารางข้างบนแทน (ตรวจกับหัวสไลด์จริงแล้วทุกบท)
- ไม่มี `## Triplets` เพราะเป็น raw source ไม่ใช่หน้า wiki (area ข)

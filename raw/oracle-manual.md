---
title: "Oracle 11i Enterprise Asset Management Fundamentals — Volume 2 (Student Guide)"
type: raw-source
source_url: "file:///opt/data/home/Documents/brain2nd/raw/oracle-manual/eAM_TrainingMaterial_v2.pdf"
ingested: 2026-11-02
sha256: 0387d355f734080c0260cc9a4380849c4a1d711fd1d377bf31975f0f44ec1edd
format: PDF มี text layer (448 หน้า) → ข้อความเต็ม `raw/oracle_manual.md` (เก็บในเครื่องเท่านั้น) + source note นี้
immutable: true
---

# Oracle 11i Enterprise Asset Management Fundamentals — Volume 2 (Student Guide)

Raw source — ห้ามแก้ไขหลัง ingest (sha256 คิดจากไฟล์ PDF ต้นฉบับ)

- หลักสูตร: **D14149GC31 · Edition 3.1 · October 2005 · Oracle University**
- ชื่อเต็ม: *11i Enterprise Asset Management Fundamentals — Volume 2 — Student Guide* (D22273)
- รูปแบบ: สไลด์ประกอบการสอน 448 หน้า (PDF text layer ไม่ต้อง OCR) แบ่งเป็น Chapter 6–20
- **Volume 2 เริ่มที่ Chapter 6** — Chapter 1–5 (ภาพรวม eAM, การ setup องค์กร/พารามิเตอร์/area/resource/department, asset group) อยู่ใน Volume 1 ซึ่งยังไม่มีใน vault; สารบัญรวมของหลักสูตรในไฟล์ครอบคลุมบท 1–20 จึงใช้เป็นดัชนีอ้างอิงได้บางส่วน
- ไฟล์ PDF เก็บที่ `raw/oracle-manual/eAM_TrainingMaterial_v2.pdf` และข้อความเต็ม `raw/oracle_manual.md` — **มีลิขสิทธิ์ Oracle จึง gitignore ทั้งคู่** (vault sync ขึ้น GitHub สาธารณะ)

## โครงสร้าง (Chapter → PDF page)

| Chapter | หัวข้อ | PDF page |
|---|---|---|
| 6 | 11i eAM Planning and Scheduling | 19 |
| 7 | 11i Direct Item Procurement for eAM Work Orders | 53 |
| 8 | 11i eAM Cost Management | 95 |
| 9 | 11i eAM Contractor Services | 121 |
| 10 | 11i eAM Property Manager | 143 |
| 11 | 11i eAM Service | 159 |
| 12 | 11i eAM Process and Discrete Manufacturing | 185 |
| 13 | 11i eAM Project Manufacturing | 211 |
| 14 | 11i eAM Work Order Billing | 233 |
| 15 | 11i eAM Oracle Time and Labor | 287 |
| 16 | 11i Self-Service Work Requests | 305 |
| 17 | 11i Maintenance User Workbench | 331 |
| 18 | 11i Maintenance Super User | 349 |
| 19 | 11i Stores | 417 |
| 20 | 11i eAM Reports and Processes | 439 |

## วิธีอ้างอิง

ข้อความเต็มมี marker ทุกหน้า: `<!-- page: N | ch: C-P -->`
โดย N = ลำดับหน้าใน PDF, C-P = เลขChapter-Page ที่พิมพ์บนสไลด์ (เช่น `6-12`)

อ้างแบบ: `(eAM 11i SG vol.2 ch.6 p.6-12)` + ระบุ PDF page เมื่อต้องเปิดดูภาพสไลด์ — หน้านี้เป็นสไลด์ จึงมีภาพหน้าจอ UI ที่ข้อความไม่เก็บ ต้องเปิด PDF ประกอบ

## ทำไมมีไฟล์นี้ใน vault

ใช้กับงาน CMMS ที่เป็น Oracle eAM/EBS: โครงสร้าง work order, PM scheduling, stores/พัสดุ, cost management, contractor services, maintenance workbench — เป็นคู่มืออ้างอิงเชิงปฏิบัติการ (operational) ต่างจากหนังสือ reliability ที่เป็นเชิงวิธีวิเคราะห์

**ข้อควรระวัง:** เป็นเอกสารปี 2005 ของ Oracle 11i — เส้นทางเมนู/หน้าจอบางส่วนต่างจาก EBS R12 และต่างจาก Oracle Cloud EAM มาก ใช้เป็น "แนวคิดและลำดับขั้นตอน" ไม่ใช่คู่มือหน้าจอของระบบที่ใช้อยู่จริง

## ข้อสังเกต

- ชื่อผู้ถือ license (Vichaya Jiraalongkorn) ถูกพิมพ์เป็นลายน้ำทุกหน้า — ลบออกจากข้อความที่ถอดแล้ว แต่ยังอยู่ใน PDF ต้นฉบับ
- หน้าสไลด์หลายหน้ามีแต่ภาพหน้าจอ ข้อความจึงสั้น (เช่น `Agenda`) — ไม่ใช่ข้อมูลหาย
- ไม่มี `## Triplets` เพราะเป็น raw source ไม่ใช่หน้า wiki (area ข)

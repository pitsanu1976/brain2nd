---
title: "Reliability Based Maintenance Management — full-text OCR (vision OCR) และผลตรวจเทียบ reading notes"
type: raw-source
source_url: "file:///.claude/llm-wiki/raw/reliability_base_maintenance_management_master.md (OCR full text kept local only, gitignored)"
ingested: 2026-10-27
sha256: 9bc7dfdc3a583c6a11cfeba79345d390a33f8c0057d967de21329d9c25e562e5
format: vision OCR Markdown (deepseek-flash, 150 dpi) ของ PDF สแกน 401 หน้า → ไฟล์ตรวจเทียบ (ocr-check) ต่อช่วงบท (Thai, paraphrased)
immutable: true
---

# RBMM full-text OCR และ OCR check

Raw source — ห้ามแก้ไขหลัง ingest (sha256 คิดจากไฟล์ OCR ทั้งไฟล์ `raw/reliability_base_maintenance_management_master.md`)

- หนังสือเล่มเดียวกับ [[raw/reliability-based-maintenance-management]] (วัฒนา เชียงกูล และคณะ, SE-ED 2553) เดิม reading notes ทำจากการอ่านภาพสแกนทีละหน้า ไฟล์นี้เป็น OCR ข้อความเต็มที่ได้มาภายหลัง (ocr_date 2026-10-27) ใช้ **ตรวจทาน** notes เดิม ไม่แทนที่
- ไฟล์ OCR เป็นข้อความเต็มของหนังสือมีลิขสิทธิ์ ถูก auto-sync push ขึ้น GitHub ไปแล้ว 1 ครั้ง (commit 406c8d4, 2026-10-27) ก่อนเพิ่มใน `.gitignore` และ `git rm --cached`; ไฟล์ยังอยู่ในเครื่อง ส่วน history เดิมผู้ใช้เลือกไม่ rewrite
- เลขหน้า: printed book page = PDF page − 2 (ตรงกับ notes เดิม) อ้างแบบ `(RBMM p.NNN)` เหมือนเดิม
- OCR เป็นของเครื่อง อาจอ่านตัวเลขผิด เมื่อ OCR กับ notes ต่างกัน ไฟล์ ocr-check ตัดสินด้วยการคำนวณซ้ำ/ผลรวม และระบุจุดที่ยังต้องตรวจกับภาพสแกน
- notes เดิมใน `reliability-based-maintenance-management/` ไม่ถูกแก้ (immutable) ผลตรวจอยู่ในไฟล์ใหม่ `reliability-based-maintenance-management/ocr-check/`

| ช่วง | OCR lines | Notes ที่ตรวจ | ไฟล์ผลตรวจ | sha256 |
|---|---|---|---|---|
| บทที่ 1-3 | 1-2264 | `ch01-02.md`, `ch03.md` | `reliability-based-maintenance-management/ocr-check/ch01-03.md` | 94631e91babb85f54cbaa98c406132a1b4a099b95f480510e403c91f95736647 |
| บทที่ 4-5 | 2265-3996 | `ch04.md`, `ch05.md` | `reliability-based-maintenance-management/ocr-check/ch04-05.md` | ac56677727cf3c4faa77b2a666c0f2cfe92dbc5be5ca5d6ca648a777f97120d6 |
| บทที่ 6-7 | 3997-5547 | `ch06.md`, `ch07.md` | `reliability-based-maintenance-management/ocr-check/ch06-07.md` | e497fdeb02e619ee8fc4c5ab557424ec921744fa820b84c86850b7c675012533 |
| บทที่ 8-9 | 5548-6835 | `ch08-09.md` | `reliability-based-maintenance-management/ocr-check/ch08-09.md` | c486ddf4e1a325992ab38641838a4cb58d36cb3413cbfa49fcd307965d8ebdb8 |
| บทที่ 10 | 6836-8169 | `ch10.md` | `reliability-based-maintenance-management/ocr-check/ch10.md` | 3cbbc05363ce0a1e37b3563acb27c6c3bdf33da20b690db2cfb1faed83fec99e |
| บทที่ 11-12 | 8170-10406 | `ch11.md`, `ch12.md` | `reliability-based-maintenance-management/ocr-check/ch11-12.md` | ee98459f02dfbe22eceb7321465855a8e9cf9eb5130912bcbcc15359f4467b57 |

แต่ละไฟล์ผลตรวจมี 6 ส่วน: จุด `[อ่านไม่ออก]` ที่ OCR อ่านได้, ข้อผิดพลาดที่ notes flag (ยืนยัน/แก้), จุดที่ notes ต่างจาก OCR, เนื้อหาที่ notes ไม่ได้บันทึก, และผลกระทบต่อหน้า wiki

หน้า hub ใน wiki: [[Reliability Based Maintenance Management Book]]

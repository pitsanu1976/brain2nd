---
title: Converting Excel and PDF to Raw
created: 2026-10-20
updated: 2026-10-20
type: guide
tags: [ingest, llm-wiki, maintenance-reliability]
sources: []
confidence: medium
contested: false
---

# Converting Excel and PDF to Raw

LLM อ่าน Markdown/CSV ได้ดีกว่า xlsx/pdf ไบนารี จึงแปลงเป็นข้อความก่อนเก็บใน `raw/`

## Excel (xlsx)

1. คำนวณ **sha256 ของไฟล์ xlsx ต้นฉบับ** (Windows PowerShell: `Get-FileHash -Algorithm SHA256 <file>`)
2. export แต่ละ sheet เป็น CSV (UTF-8) ไปที่ `raw/datasets/<ชื่อ>__<sheet>.csv`
3. สร้างไฟล์ `raw/<ชื่อ>.md` เป็น manifest: frontmatter + ตาราง sheet -> CSV, จำนวนแถว, จำนวนคอลัมน์
4. ห้ามแก้ CSV หลัง ingest

ตัวอย่างจริง: wiki compressor ส่งออก 10 sheet, manifest บอกจำนวนแถวของแต่ละ sheet ([[Maintenance Reliability Example]])

## PDF

1. sha256 ของ PDF
2. แปลงเป็น Markdown/ข้อความ (เครื่องมือขึ้นกับที่มี) ตรวจตาราง/ตัวเลขที่มักเพี้ยน
3. รูปภาพสำคัญเก็บใน `raw/assets/`
4. ใส่ `source_url` เป็น path/URL ต้นฉบับ

## Frontmatter ของ raw

```yaml
---
title: "Compressor Failure Hierarchy.xlsx"
type: raw-source
source_url: "file:///..."
ingested: 2026-10-20
sha256: <64 hex>
format: xlsx
immutable: true
---
```

ตัวเลขที่อ่านจากภาพหรือคำนวณเอง ตั้ง `confidence: medium` ในหน้า wiki และบอกว่า derived ต่อด้วย ingest ตาม [[Using Claude Code on a Vault]] และดู spec ที่ [[Frontmatter Spec]]

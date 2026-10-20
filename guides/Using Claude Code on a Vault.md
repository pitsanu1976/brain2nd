---
title: Using Claude Code on a Vault
created: 2026-10-20
updated: 2026-10-20
type: guide
tags: [claude-code, llm-wiki, ingest, lint, workflow]
sources: []
confidence: medium
contested: false
---

# Using Claude Code on a Vault

Vault คือโฟลเดอร์ Markdown ธรรมดา Claude Code (หรือ llm-wiki agent) จึงอ่าน/เขียนได้ตรง ๆ ตั้ง working directory ที่ `50 Wiki` (หรือ root ของ vault) ตามงาน

## เริ่ม session ทุกครั้ง

สั่งให้อ่าน `SCHEMA.md`, `index.md` และ 20–30 entry ล่าสุดของ `log.md` ก่อนทำงาน ([[LLM Wiki Pattern]])

## Ingest

1. วาง source ใน `raw/articles|papers|transcripts` พร้อม frontmatter (`source_url`, `ingested`, `sha256`)
2. ให้ Claude ตรวจ [[Page Thresholds]] แล้วสร้าง/อัปเดตหน้า
3. เพิ่มหน้าใหม่ใน `index.md`
4. ตรวจความขัดแย้ง ([[Contradiction Handling]])
5. append `log.md`

ไฟล์ Excel/PDF: [[Converting Excel and PDF to Raw]]

## Query

ถามคำถาม แล้วให้ตอบจาก wiki ก่อน raw ถ้าคำตอบมีคุณค่าให้บันทึกเป็นหน้าใน `queries/` พร้อม sources และ log (ตัวอย่าง [[FAQ Obsidian Second Brain and LLM Wiki]])

## Lint

| ตรวจ | วิธี |
|---|---|
| Broken link | ดึงทุก wikilink แล้วเทียบชื่อหน้า |
| Orphan | หน้าที่ไม่อยู่ใน index หรือไม่มี inbound link |
| Frontmatter ขาด | ครบ 8 field ตาม [[Frontmatter Spec]] |
| Stale | `updated` เก่า / source ใหม่กว่า |
| Contested | มี entry ใน log |

## ข้อควรระวัง

- ให้ Claude สำรองก่อนแก้ไฟล์เดิม ห้ามลบ ห้ามแก้ `raw/`
- ห้ามให้ติดตั้ง community plugin โดยไม่ได้รับอนุญาต
- ตรวจ diff/ผลงานเอง โดยเฉพาะตัวเลขที่ส่งต่อไปรายงาน

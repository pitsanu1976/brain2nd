---
title: LLM Wiki Pattern
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [llm-wiki, claude-code, workflow]
sources: []
confidence: medium
contested: false
---

# LLM Wiki Pattern

รูปแบบที่ให้ LLM สร้างและดูแล wiki ส่วนตัวที่ **เชื่อมโยงกัน** จาก source ดิบ แทนการค้นหาแบบ RAG ทุกครั้ง แนวคิดเผยแพร่โดย Andrej Karpathy (อธิบายนี้อิงความเข้าใจทั่วไป ไม่ใช่การอ้างข้อความต้นฉบับ จึงตั้ง `confidence: medium`)

## 3 ชั้น

| Layer | ที่อยู่ในไฟล์ | กติกา |
|---|---|---|
| 1. Raw sources | `raw/` | immutable หลัง ingest (ต้องมี `source_url`, `ingested`, `sha256`) |
| 2. Wiki pages | `entities/`, `concepts/`, `comparisons/`, `queries/` ฯลฯ | LLM สังเคราะห์ เชื่อมด้วย wikilink |
| 3. Schema | `SCHEMA.md` | กำหนด convention, frontmatter, taxonomy, workflow |

ไฟล์เสริมสองตัว: `index.md` (แค็ตตาล็อกทุกหน้า) และ `log.md` (ประวัติ append-only)

## 3 operations

- **Ingest**: เพิ่ม source ใหม่ -> สร้าง/อัปเดตหลายหน้า -> อัปเดต index -> log
- **Query**: ถามโดยอ่าน index แล้วตามลิงก์ ถ้าคำตอบดีให้บันทึกกลับเป็นหน้าใน `queries/` (ความรู้สะสม)
- **Lint**: ตรวจ broken link, orphan, frontmatter ขาด, หน้า stale, ข้อขัดแย้ง

## ทำไมได้ผล

งานบำรุงรักษา (cross-reference, อัปเดตหลายหน้า) คือส่วนที่มนุษย์เบื่อ แต่ LLM ทำได้ไม่เหนื่อย มนุษย์เลือก source และตั้งคำถาม

## เรื่องที่เกี่ยวข้อง

- [[Contradiction Handling]] และ [[Page Thresholds]] คือกติกาหลักใน schema
- การรวมกับ [[Second Brain]] ใน vault เดียว: [[Second Brain vs LLM Wiki]]
- ขั้นตอนปฏิบัติ: [[Using Claude Code on a Vault]]
- ตัวอย่างจริง: [[Maintenance Reliability Example]]

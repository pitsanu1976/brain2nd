---
title: Frontmatter Spec
created: 2026-10-20
updated: 2026-10-20
type: reference
tags: [frontmatter, reference, convention]
sources: []
confidence: high
contested: false
---

# Frontmatter Spec

YAML block ที่ต้นไฟล์ คั่นด้วย `---` Obsidian แสดงเป็น Properties ([[Obsidian Core Plugins]])

## Wiki page (8 field บังคับ)

| Field | ชนิด | ความหมาย |
|---|---|---|
| `title` | string | ชื่อหน้า (ตรงชื่อไฟล์) |
| `created` | date `YYYY-MM-DD` | วันสร้าง |
| `updated` | date | วันแก้ล่าสุด (อัปเดตทุกครั้งที่แก้) |
| `type` | enum | `concept`, `guide`, `reference`, `query` (หรือ `entity`, `comparison` ถ้ามีโฟลเดอร์นั้น) |
| `tags` | list | ตาม taxonomy ใน [[SCHEMA]] |
| `sources` | list | ไฟล์ใน `raw/` ที่ใช้ (ว่าง `[]` ได้) |
| `confidence` | enum | `high`, `medium`, `low` |
| `contested` | boolean | `true` เมื่อมีข้อขัดแย้งที่ยังไม่ resolve ([[Contradiction Handling]]) |

```yaml
---
title: Failure Mode
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [failure-mode, taxonomy]
sources: [example.md]
confidence: high
contested: false
---
```

## Raw source

| Field | ความหมาย |
|---|---|
| `title` | ชื่อต้นฉบับ |
| `type` | `raw-source` |
| `source_url` | URL หรือ path ต้นฉบับ |
| `ingested` | วัน ingest |
| `sha256` | hash ของ body (หรือไฟล์ต้นฉบับถ้าเป็นไบนารี) |
| `immutable` | `true` |

## ข้อควรระวัง YAML

- string ที่มี `:` หรือขึ้นต้นด้วยอักขระพิเศษ ให้ใส่เครื่องหมายคำพูด
- list ใช้ `[a, b]` หรือขึ้นบรรทัดละ `- item`
- ห้ามมี tab
- ค่าใน frontmatter ไม่เป็น wikilink ถ้าไม่จำเป็น (Obsidian รองรับแต่ควรอ้างในเนื้อหา)

ดูต่อที่ [[Templates Reference]] และ [[Tags vs Links vs Folders]]

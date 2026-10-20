---
title: Naming Conventions
created: 2026-10-20
updated: 2026-10-20
type: reference
tags: [naming, convention]
sources: []
confidence: high
contested: false
---

# Naming Conventions

| สิ่งที่ตั้งชื่อ | รูปแบบ | ตัวอย่าง |
|---|---|---|
| Top-level folder | เลข 2 หลัก + ช่องว่าง + ชื่อ | `10 Projects` |
| Daily note | `YYYY-MM-DD` | `2026-10-20` |
| Wiki page | ชื่อภาษาอังกฤษ เว้นวรรคได้ ตรงกับ `title` | `Failure Mode` |
| Query page | ประโยคคำถาม | `Which failure modes dominate ...` |
| Project note | `<Project> - <สั้น ๆ>` | `Comp Trip RCA` |
| Meeting note | `YYYY-MM-DD <หัวข้อ>` | `2026-10-20 PM Review` |
| Raw source | kebab-case + นามสกุลเดิม | `compressor-failure-hierarchy.md` |
| Dataset CSV | `<source>__<sheet>.csv` | `compressor-failure-hierarchy__notes.csv` |
| Tag | ตัวพิมพ์เล็ก ขีดกลาง | `failure-mode` |

## ห้าม

- อักขระ `| # ^ [ ] : / \ ? * " < >` ในชื่อไฟล์
- ชื่อซ้ำกันข้าม folder (ทำให้ wikilink กำกวม) เช่น `README.md` หลายไฟล์ ให้ลิงก์ด้วย path หรือหลีกเลี่ยง
- เปลี่ยนชื่อไฟล์นอก Obsidian (link อาจไม่อัปเดต)

ดู [[Wikilinks vs Markdown Links]] และ [[Vault Setup for Fleet Engineering]]

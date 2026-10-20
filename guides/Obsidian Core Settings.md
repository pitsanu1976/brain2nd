---
title: Obsidian Core Settings
created: 2026-10-20
updated: 2026-10-20
type: guide
tags: [obsidian, settings, setup]
sources: []
confidence: medium
contested: false
---

# Obsidian Core Settings

ชื่อ menu และ key อาจต่างตามเวอร์ชัน Obsidian (`confidence: medium`) ตรวจใน Settings จริงก่อนยืนยัน

## ตั้งค่าที่ต้องการ

| ต้องการ | ตำแหน่งใน Settings (โดยประมาณ) | ค่า |
|---|---|---|
| New notes ไป Inbox | Files and links > Default location for new notes | In the folder specified below = `01 Inbox` |
| Internal links เป็น wikilink | Files and links > Use Wikilinks | เปิด |
| Auto update links | Files and links > Automatically update internal links | เปิด |
| Attachment folder | Files and links > Default location for new attachments | In the folder specified below = `50 Wiki/raw/assets` |
| Live Preview | Editor > Default editing mode | Live Preview |
| Line numbers | Editor > Show line number | เปิด |
| Daily Notes | Core plugins > Daily notes | Folder `02 Daily`, Date format `YYYY-MM-DD`, Template `90 Templates/Daily Note` |
| Templates | Core plugins > Templates | Template folder location = `90 Templates` |

## ไฟล์ config ใน `.obsidian/` (confidence: low-medium)

ชื่อ key ด้านล่างจำจากความรู้ทั่วไป อาจเปลี่ยนตามเวอร์ชัน ควรให้ Obsidian เขียนเองผ่าน UI แล้วตรวจไฟล์

| ไฟล์ | key ที่น่าจะใช้ |
|---|---|
| `app.json` | `newFileLocation`, `newFileFolderPath`, `attachmentFolderPath`, `useMarkdownLinks`, `alwaysUpdateLinks`, `livePreview`, `showLineNumber` |
| `daily-notes.json` | `folder`, `format`, `template` |
| `templates.json` | `folder` |
| `core-plugins.json` | รายการ core plugin ที่เปิด |

## ข้อห้าม

- ห้ามคัดลอก `workspace.json` จากเครื่องอื่น (เก็บ layout เฉพาะเครื่อง)
- ห้ามติดตั้ง community plugin โดยไม่ได้รับอนุญาต
- ตรวจว่า JSON ทุกไฟล์ parse ได้หลังแก้
- ไฟล์ attachment ที่ผู้ใช้จัดเอง ใช้ `99 Attachments`

ดู [[Vault Setup for Fleet Engineering]], [[Obsidian Core Plugins]], [[Wikilinks vs Markdown Links]]

---
title: Vault Setup for Fleet Engineering
created: 2026-10-20
updated: 2026-10-20
type: guide
tags: [setup, obsidian, para, llm-wiki, fleet-engineering]
sources: []
confidence: high
contested: false
---

# Vault Setup for Fleet Engineering

โครงสร้าง vault ที่รวม [[PARA Method]] กับ [[LLM Wiki Pattern]]

## โครงสร้าง

```
00 Home.md
01 Inbox/Inbox.md
02 Daily/Daily Notes.md
10 Projects/Projects.md
20 Areas/Areas.md
30 Resources/Resources.md
40 Archive/Archive.md
50 Wiki/
  SCHEMA.md  index.md  log.md
  raw/ articles/ papers/ transcripts/ assets/
  entities/ concepts/ comparisons/ queries/ _archive/
90 Templates/  Daily Note.md  Project Note.md  Meeting Note.md  Wiki Page.md  Raw Source.md
99 Attachments/
```

## หน้าที่ของแต่ละส่วน

| ส่วน | หน้าที่ |
|---|---|
| `00 Home` | MOC สูงสุด ลิงก์ทุกส่วน + อธิบาย workflow ([[Maps of Content]]) |
| `01 Inbox` | จุด capture ทุกอย่าง (new notes ไปที่นี่) |
| `02 Daily` | daily note รูปแบบ `YYYY-MM-DD` |
| `10`-`40` | PARA |
| `50 Wiki` | LLM Wiki; `raw/` immutable |
| `90 Templates` | template ([[Templates Reference]]) |
| `99 Attachments` | ไฟล์ทั่วไปที่ผู้ใช้จัดเก็บเอง (ไม่ใช่ที่ default ของ Obsidian) |

## ขั้นตอน

1. ตรวจโฟลเดอร์เป้าหมายก่อน ห้ามเขียนทับไฟล์เดิมโดยไม่สำรองหรือขออนุญาต
2. สร้างโฟลเดอร์และไฟล์หลัก (MOC ของแต่ละหมวดอย่างน้อยหนึ่งไฟล์)
3. สร้าง `SCHEMA.md`, `index.md`, `log.md` ใน `50 Wiki`
4. สร้าง 5 template
5. ตั้งค่า Obsidian ตาม [[Obsidian Core Settings]]
6. ตรวจ JSON config และ wikilink ทุกลิงก์

หมายเหตุ: Windows/OneDrive: vault ที่อยู่ใน OneDrive sync ได้ แต่ระวัง conflict ถ้าเปิดสองเครื่อง และห้ามคัดลอก `workspace.json` ข้ามเครื่อง ดู [[Naming Conventions]] สำหรับการตั้งชื่อ

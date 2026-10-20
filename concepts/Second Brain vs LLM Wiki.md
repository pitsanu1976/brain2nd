---
title: Second Brain vs LLM Wiki
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [second-brain, llm-wiki, para]
sources: []
confidence: medium
contested: false
---

# Second Brain vs LLM Wiki

สองระบบแก้ปัญหาคนละด้าน และอยู่ร่วม vault เดียวได้

| มิติ | [[Second Brain]] (PARA) | [[LLM Wiki Pattern]] |
|---|---|---|
| จัดตาม | ความ actionable (Project/Area) | หัวข้อและความสัมพันธ์ |
| ผู้เขียนหลัก | มนุษย์ | LLM (มนุษย์ตรวจ) |
| หน่วย | note ตามงาน | wiki page ที่มี frontmatter ตาม schema |
| อายุ | โปรเจกต์จบแล้ว archive | สะสมและอัปเดตต่อเนื่อง |
| กติกา | หลวม | เข้มงวด (`SCHEMA.md`, index, log) |
| ผลลัพธ์ | งานที่ส่งมอบ | ฐานความรู้ที่ query ได้ |

## ผสมใน vault เดียว

- `01`-`40` = Second Brain: capture และงานของมนุษย์
- `50 Wiki` = LLM Wiki: โซนที่ LLM เขียน มี `raw/` immutable
- Project note ลิงก์ไปหน้า wiki เพื่อดึงความรู้ (ไม่คัดลอก)
- ข้อสรุปที่ใช้ซ้ำได้จากโปรเจกต์ที่ปิดแล้ว ให้ distill เป็นหน้า wiki ก่อน archive (ขั้น Distill ของ CODE)
- หลีกเลี่ยงให้ LLM แก้ `01`-`40` โดยไม่สั่ง; หลีกเลี่ยงให้มนุษย์แก้ `raw/`

โครง folder ดู [[Vault Setup for Fleet Engineering]] การเลือกใช้ tag/link/folder ดู [[Tags vs Links vs Folders]]

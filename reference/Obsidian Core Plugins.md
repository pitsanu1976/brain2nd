---
title: Obsidian Core Plugins
created: 2026-10-20
updated: 2026-10-20
type: reference
tags: [plugins, obsidian]
sources: []
confidence: medium
contested: false
---

# Obsidian Core Plugins

Core plugin มากับ Obsidian เปิด/ปิดที่ Settings > Core plugins (ไม่ใช่ community plugin จึงไม่ต้องขออนุญาตติดตั้ง แต่รายการและชื่ออาจต่างตามเวอร์ชัน)

| Plugin | ใช้ทำอะไร | ความมั่นใจ |
|---|---|---|
| Daily notes | สร้าง daily note ตาม format/folder/template | สูง |
| Templates | แทรก template จาก template folder ({{title}}, {{date}}, {{time}}) | สูง |
| Backlinks | แสดงหน้าที่ลิงก์มาหาหน้านี้ | สูง |
| Graph view | แผนภาพความสัมพันธ์ ช่วยหา orphan | สูง |
| Outline | โครงหัวข้อของหน้า | สูง |
| Properties view / Properties | แก้ frontmatter เป็นฟอร์ม | กลาง (ชื่อและพฤติกรรมเปลี่ยนตามเวอร์ชัน) |
| Canvas | กระดานภาพ วางโน้ตและเชื่อมกัน | กลาง |
| Bases | มุมมองฐานข้อมูลจาก properties | ต่ำ-กลาง (ฟีเจอร์ค่อนข้างใหม่ ตรวจว่ามีในเวอร์ชันที่ใช้) |

## ใช้อย่างไรกับ wiki

- Backlinks + Graph view ช่วย lint: หน้าไม่มี inbound link = orphan
- Properties ช่วยตรวจ frontmatter ครบ ([[Frontmatter Spec]])
- Templates + Daily notes ตั้งค่าตาม [[Obsidian Core Settings]]; เนื้อหา template ใน [[Templates Reference]]

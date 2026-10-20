---
title: Wikilinks vs Markdown Links
created: 2026-10-20
updated: 2026-10-20
type: reference
tags: [links, obsidian, convention]
sources: []
confidence: high
contested: false
---

# Wikilinks vs Markdown Links

| | Wikilink | Markdown link |
|---|---|---|
| รูปแบบ | ชื่อหน้าในวงเล็บเหลี่ยมคู่ | ข้อความในวงเล็บเหลี่ยม ตามด้วย path ในวงเล็บกลม |
| Alias | ใช้ตัวคั่น pipe (ห้ามใช้ในตาราง Markdown เพราะชนกับตัวคั่นคอลัมน์) | ข้อความลิงก์เป็น alias อยู่แล้ว |
| Heading/Block | ใช้ `#heading`, `#^block` | ใช้ได้ แต่ต้อง URL-encode ช่องว่าง |
| ย้ายไฟล์ | Obsidian อัปเดตให้ถ้าเปิด automatic link updates | อัปเดตให้ถ้าเปิดเช่นกัน |
| เปิดนอก Obsidian | ไม่ทำงาน | ทำงานในเครื่องมือทั่วไป |

## กติกา vault นี้

- **Internal link ใช้ wikilink เท่านั้น** (ตั้ง "Use Wikilinks" เปิด ใน [[Obsidian Core Settings]])
- Markdown link ใช้เฉพาะ URL ภายนอก
- ชื่อหน้าไม่ซ้ำกันทั้ง vault (shortest path ใช้ได้) ถ้าซ้ำใช้ path เต็ม เช่น `folder/ชื่อ`
- ชื่อหน้าที่มี `|` `#` `^` `[` `]` ห้ามใช้ ([[Naming Conventions]])
- ใช้ลิงก์ไปหน้าที่ยังไม่มีเฉพาะใน template (placeholder)

เหตุผล: wikilink อ่านง่ายสำหรับ LLM และสร้าง backlink/graph ให้อัตโนมัติ

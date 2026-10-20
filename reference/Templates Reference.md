---
title: Templates Reference
created: 2026-10-20
updated: 2026-10-20
type: reference
tags: [templates, obsidian, reference]
sources: []
confidence: medium
contested: false
---

# Templates Reference

ข้อความเต็มของ 5 template ใน `90 Templates/` ใช้ตัวแปรของ core Templates plugin: `{{title}}` (ชื่อไฟล์), `{{date}}` (วันนี้ รูปแบบเริ่มต้น `YYYY-MM-DD`), `{{time}}`, และ `{{date:FORMAT}}` (ตัวแปรเหล่านี้เป็นของ core plugin; รูปแบบ format ที่รองรับตรวจกับเวอร์ชันที่ใช้ จึง `confidence: medium`)

Link ใน template ตั้งใจเป็นข้อความธรรมดา เพื่อไม่ให้เกิด broken link ผู้ใช้เติม wikilink เองหลังสร้าง ([[Wikilinks vs Markdown Links]])

## Daily Note.md

```markdown
---
title: {{title}}
created: {{date}}
type: daily
tags: [daily]
---

# {{title}}

## เป้าหมายวันนี้
- [ ] 

## Log งาน
- 

## ข้อสังเกต / ไอเดีย
- 

## ลิงก์
- Project: (ใส่ wikilink)
- Meeting: (ใส่ wikilink)
```

## Project Note.md

```markdown
---
title: {{title}}
created: {{date}}
updated: {{date}}
type: project
status: active
tags: [project]
---

# {{title}}

## เป้าหมาย
 
## Deadline
 
## ขอบเขต / ผู้เกี่ยวข้อง
- 

## Tasks
- [ ] 

## ความคืบหน้า
- {{date}}: 

## อ้างอิง (wikilink ไป wiki / meeting)
- 

## บทเรียน (distill ก่อน archive)
- 
```

## Meeting Note.md

```markdown
---
title: {{title}}
created: {{date}}
type: meeting
tags: [meeting]
---

# {{title}}

- วันที่: {{date}} {{time}}
- ผู้เข้าร่วม: 
- Project ที่เกี่ยวข้อง: (ใส่ wikilink)

## วาระ
1. 

## สรุป / ข้อตกลง
- 

## Action items
- [ ] ผู้รับผิดชอบ / กำหนดส่ง: 
```

## Wiki Page.md

```markdown
---
title: {{title}}
created: {{date}}
updated: {{date}}
type: concept
tags: []
sources: []
confidence: medium
contested: false
---

# {{title}}

คำอธิบายสั้น

## เนื้อหา

## ดูเพิ่ม
- (ใส่ wikilink อย่างน้อย 2 รายการ)
```

## Raw Source.md

```markdown
---
title: {{title}}
type: raw-source
source_url: 
ingested: {{date}}
sha256: 
immutable: true
---

# {{title}}

(วางเนื้อหาต้นฉบับที่นี่ แล้วคำนวณ sha256 ของ body แก้ได้เฉพาะก่อน ingest เสร็จ)
```

หลัง ingest raw source ห้ามแก้ ([[Frontmatter Spec]]) การตั้งค่า template folder ดู [[Obsidian Core Settings]]

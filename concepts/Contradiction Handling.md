---
title: Contradiction Handling
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [llm-wiki, convention]
sources: []
confidence: high
contested: false
---

# Contradiction Handling (contested flag)

เมื่อ source ใหม่ขัดกับเนื้อหาที่มีอยู่ **ห้ามเขียนทับเงียบ ๆ**

## ขั้นตอน

1. เก็บ **ทั้งสองมุมมอง** ในหน้าเดียวกัน พร้อมระบุ source ของแต่ละฝั่ง
2. ตั้ง `contested: true` ใน frontmatter และอัปเดต `updated`
3. บันทึกใน `log.md` ว่าขัดแย้งเรื่องอะไร ระหว่าง source ใด
4. เมื่อ resolve: คงข้อความประวัติ ตั้ง `contested: false` และ log การตัดสินใจและเหตุผล

## รูปแบบในหน้า

```markdown
## ข้อขัดแย้ง
- มุมมอง A (source: a.md): ...
- มุมมอง B (source: b.md): ...
- สถานะ: ยังไม่ resolve
```

## ตัวอย่างจริง

ใน wiki compressor (worked example) ความจำนวน sub unit ต่างกันระหว่างสอง source จึงบันทึกเป็น contested ดู [[Maintenance Reliability Example]]

Lint ต้องตรวจว่าทุกหน้า `contested: true` มี entry ใน log ดู [[Using Claude Code on a Vault]] และ [[Frontmatter Spec]]

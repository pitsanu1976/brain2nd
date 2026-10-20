---
title: PARA Method
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [para, second-brain, taxonomy]
sources: []
confidence: high
contested: false
---

# PARA Method

**PARA** = Projects, Areas, Resources, Archive ระบบจัดหมวดของ [[Second Brain]] โดยเรียงตามความ actionable

| หมวด | นิยาม | ตัวอย่าง fleet engineering | Folder |
|---|---|---|---|
| Projects | งานมีเป้าหมายและ deadline | RCA ของ compressor trip, Turnaround scope review | `10 Projects` |
| Areas | ความรับผิดชอบต่อเนื่อง ไม่มีวันจบ | Reliability monitoring, Spare parts, Vendor management | `20 Areas` |
| Resources | หัวข้อที่สนใจ/อ้างอิง | ISO 14224, OREDA, vendor manual | `30 Resources` |
| Archive | ของที่ไม่ active | โปรเจกต์ที่ปิดแล้ว | `40 Archive` |

## กฎย้ายหมวด

- Project จบ -> ย้ายไป Archive (ไม่ลบ)
- Area ที่เลิกรับผิดชอบ -> Archive
- Resource ที่กลายเป็นงานเฉพาะกิจ -> เชื่อมเข้า Project ด้วย wikilink แทนการคัดลอก

## ข้อควรระวัง

เลขนำหน้า (`10`, `20`...) เป็นแบบ Johnny.Decimal-style เพื่อเรียงลำดับใน file explorer ไม่ใช่ส่วนหนึ่งของ PARA ดั้งเดิม ใน vault นี้ `50 Wiki` อยู่นอก PARA และเป็นที่อยู่ของ [[LLM Wiki Pattern]] ดู [[Vault Setup for Fleet Engineering]] และ [[Tags vs Links vs Folders]]

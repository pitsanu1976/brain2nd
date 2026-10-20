---
title: FAQ Obsidian Second Brain and LLM Wiki
created: 2026-10-20
updated: 2026-10-20
type: query
tags: [query, faq, obsidian, llm-wiki]
sources: []
confidence: medium
contested: false
---

# FAQ: Obsidian Second Brain and LLM Wiki

**ถาม: ต้องมีทั้ง PARA และ LLM Wiki ไหม?**
ตอบ: ไม่จำเป็น แต่ใช้ร่วมกันได้ดี PARA จัดงานของมนุษย์ ส่วน wiki เก็บความรู้ที่สะสม ดู [[Second Brain vs LLM Wiki]]

**ถาม: ไฟล์ attachment ไปที่ไหน?**
ตอบ: ที่เพิ่มผ่าน Obsidian ไป `50 Wiki/raw/assets` ส่วนไฟล์ทั่วไปที่จัดเองใช้ `99 Attachments` ([[Obsidian Core Settings]])

**ถาม: ข้อมูลขัดแย้งทำอย่างไร?**
ตอบ: เก็บสองมุมมอง ตั้ง `contested: true` และ log ([[Contradiction Handling]])

**ถาม: ใช้ Claude Code ทำอะไรกับ vault ได้บ้าง?**
ตอบ: ingest, query, lint ([[Using Claude Code on a Vault]])

**ถาม: ควรติดตั้ง community plugin ไหม?**
ตอบ: ไม่ติดตั้งโดยไม่ได้รับอนุญาต core plugin เพียงพอสำหรับ workflow นี้ ([[Obsidian Core Plugins]])

**ถาม: ย้าย vault ไปเครื่องอื่นต้องระวังอะไร?**
ตอบ: ห้ามคัดลอก `workspace.json` (layout เฉพาะเครื่อง) ไฟล์ config อื่นใน `.obsidian/` ย้ายได้ แต่ตรวจ JSON หลังย้าย (ตรวจกับเวอร์ชันจริง)

---
title: Page Thresholds
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [llm-wiki, convention]
sources: []
confidence: high
contested: false
---

# Page Thresholds

กฎกันไม่ให้ wiki บวมเป็นหน้าเล็กไร้ค่า

## สร้างหน้าใหม่เมื่อ

1. หัวข้อเป็น **แกนหลักของ source หนึ่ง** หรือ
2. หัวข้อปรากฏใน **อย่างน้อยสอง sources**

## ไม่สร้างเมื่อ

- ถูกกล่าวถึงผ่าน ๆ ใน source เดียว -> รวมไว้ในหน้า hub
- เป็นรายละเอียดเล็กที่ตัวเลขต่ำ

## เกณฑ์เสริม

- หน้าใหม่มี outbound wikilink อย่างน้อย 2 ลิงก์เมื่อทำได้
- ต้องเพิ่มใน `index.md` และ log
- หน้าที่ยาวเกินและมีหลายแนวคิด ให้แตกตามหลัก atomic ([[Zettelkasten and Atomic Notes]])

## ตัวอย่าง

wiki compressor สร้างหน้ารายโหมดเฉพาะ 9 โหมดที่ % สูง ส่วนโหมดเล็กอยู่ใน hub ([[Maintenance Reliability Example]]) กติกาเต็มอยู่ใน [[LLM Wiki Pattern]] และ schema

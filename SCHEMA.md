# SCHEMA — Obsidian Second Brain + LLM Wiki (User-level Knowledge Base)

กติกากลางของ wiki นี้ (Layer 3) อ่านไฟล์นี้ก่อนทำงานทุก session ร่วมกับ [[index]] และ [[log]]

## 1. Domain

- หัวข้อ: **การใช้ Obsidian เพื่อรัน Second Brain + LLM Wiki** (PARA, Zettelkasten, MOC, LLM Wiki pattern, vault setup, workflow กับ Claude Code)
- ผู้ใช้: Fleet / Maintenance-Reliability engineer, Valeura Energy ที่ทำงานกับ Claude Code
- ขอบเขต: แนวคิด, วิธีตั้งค่า vault, workflow รายวัน, การใช้ Claude Code/llm-wiki agent กับ vault, reference (frontmatter, template, naming, core plugins)
- นอกขอบเขต: community plugin (ห้ามติดตั้งโดยไม่ได้รับอนุญาต), ข้อมูล asset จริงของ Valeura
- Worked example: wiki ด้าน compressor failure hierarchy (ดู [[Maintenance Reliability Example]])
- ไม่มี raw source ภายนอก: เนื้อหาเขียนจากความรู้ทั่วไป จึงใช้ `confidence` บอกระดับความมั่นใจ (ดูหัวข้อ 4)

## 2. สถาปัตยกรรม 3 ชั้น

| Layer | ที่อยู่ | สถานะ |
|---|---|---|
| 1. Raw sources | `raw/` | **IMMUTABLE** หลัง ingest (ตอนนี้มีแค่ README) |
| 2. Wiki pages | `concepts/`, `guides/`, `reference/`, `queries/` | LLM เขียนและดูแล |
| 3. Rules | `SCHEMA.md`, `index.md`, `log.md`, `README.md` | กติกาและแค็ตตาล็อก |

`_archive/` เก็บหน้าที่เลิกใช้ (ห้ามลบ ให้ย้ายมาและบันทึกใน [[log]])

### โครงสร้างที่เลือก (reconcile)

โครงสร้างมาตรฐานของ LLM Wiki มี `entities/`, `concepts/`, `comparisons/`, `queries/` แต่หัวข้อนี้เป็นความรู้เชิงวิธีการ จึงใช้ `concepts/`, `guides/` (how-to), `reference/` (cheat sheet, template), `queries/` แทน และตัด `entities/`, `comparisons/` ออก (ไม่มีวัตถุรูปธรรม; การเปรียบเทียบอยู่ใน concept เช่น [[Second Brain vs LLM Wiki]]) ถ้าอนาคตมี source จริงที่ต้องใช้ ให้เพิ่มโฟลเดอร์แล้วอัปเดตหัวข้อนี้และ [[log]]

## 3. Conventions

- Markdown UTF-8 ชื่อไฟล์ = ชื่อหน้า ภาษาอังกฤษ เว้นวรรคได้ (ดู [[Naming Conventions]])
- ลิงก์ภายในใช้ **Obsidian wikilinks เท่านั้น** (เหตุผลใน [[Wikilinks vs Markdown Links]])
- ห้ามใส่ alias `|` ในตาราง
- คำอธิบายเป็นภาษาไทยกระชับ; ชื่อเทคนิค ชื่อโฟลเดอร์/ไฟล์ ชื่อ setting คงเป็นภาษาอังกฤษ
- ชื่อ menu / setting key ที่อาจต่างตามเวอร์ชัน Obsidian ให้ตั้ง `confidence: medium` หรือ `low`
- วันที่ `YYYY-MM-DD`
- หน้าใหม่ควรมี outbound wikilinks อย่างน้อย 2 ลิงก์
- ไม่สร้างไฟล์นอกโฟลเดอร์ `llm-wiki/`
- ไม่ใส่ตัวอย่าง wikilink ที่ไม่มีหน้าจริงนอก code block (ตัวอย่างใน code block ถูกยกเว้นจาก link check)

## 4. Frontmatter

ดูรายละเอียดเต็มใน [[Frontmatter Spec]]

### 4.1 Wiki page

```yaml
---
title: ชื่อหน้า
created: 2026-10-20
updated: 2026-10-20
type: concept | guide | reference | query
tags: [tag1, tag2]
sources: []
confidence: high | medium | low
contested: true | false
---
```

- `sources` = ชื่อไฟล์ใน `raw/` ที่ใช้เขียน (ว่างได้เมื่อเขียนจากความรู้ทั่วไป)
- `confidence`: high = แนวคิดที่นิยามชัดและเสถียร; medium = รายละเอียดที่ขึ้นกับเวอร์ชัน/ตีความ/จำจากความรู้; low = ไม่แน่ใจ ต้องตรวจกับ Obsidian จริง
- `contested: true` เมื่อข้อมูลขัดแย้งและยังไม่ resolve ([[Contradiction Handling]])

### 4.2 Raw source

```yaml
---
title: ชื่อต้นฉบับ
type: raw-source
source_url: ...
ingested: 2026-10-20
sha256: <hash ของ body>
immutable: true
---
```

## 5. Taxonomy

### 5.1 Folder และ page type

| Folder | type | เนื้อหา |
|---|---|---|
| `concepts/` | concept | แนวคิด: Second Brain, PARA, Zettelkasten, MOC, LLM Wiki |
| `guides/` | guide | how-to เป็นขั้นตอน |
| `reference/` | reference | cheat sheet, spec, template |
| `queries/` | query | คำถาม-คำตอบที่บันทึกไว้ |
| `_archive/` | - | หน้าที่เลิกใช้ |

### 5.2 Tag taxonomy (ตัวพิมพ์เล็ก ขีดกลาง)

- Method: `second-brain`, `para`, `zettelkasten`, `moc`, `llm-wiki`, `code-method`
- Obsidian: `obsidian`, `settings`, `plugins`, `templates`, `frontmatter`, `links`, `naming`
- Workflow: `workflow`, `setup`, `claude-code`, `ingest`, `lint`
- Domain: `maintenance-reliability`, `fleet-engineering`
- Meta: `guide`, `reference`, `query`, `convention`, `faq`

ต้องการ tag ใหม่ ให้เพิ่มในหัวข้อนี้ก่อนใช้

## 6. Page thresholds

สร้างหน้าใหม่เมื่อ (1) เป็นแกนหลักของ source หนึ่ง หรือ (2) ปรากฏในอย่างน้อยสอง sources รายละเอียดและตัวอย่างใน [[Page Thresholds]]

## 7. Update policy

- ก่อนแก้หน้าเดิม ให้อ่านทั้งหน้า แล้วอัปเดต `updated`
- **ข้อมูลขัดแย้ง ห้ามเขียนทับเงียบ ๆ** เก็บทั้งสองมุมมอง ตั้ง `contested: true` และ log ([[Contradiction Handling]])
- หน้าที่เลิกใช้ย้ายไป `_archive/` (ไม่ลบ) และอัปเดต [[index]]
- หน้าใหม่ทุกหน้าต้องอยู่ใน [[index]] และมี outbound wikilinks อย่างน้อย 2 ลิงก์
- ทุก action ต้อง **append** ใน [[log]] (append-only)
- ห้ามสร้าง broken link

## 8. Maintenance workflow

### 8.1 เริ่ม session
1. อ่าน `SCHEMA.md`
2. อ่าน [[index]]
3. อ่าน 20–30 entry ล่าสุดของ [[log]]

### 8.2 Ingest
1. วางไฟล์ใน `raw/` พร้อม `source_url`, `ingested`, `sha256` ของ body
2. ตรวจ threshold แล้วสร้าง/อัปเดตหน้า
3. เพิ่มใน [[index]]
4. ตรวจความขัดแย้ง
5. append [[log]]

ขั้นตอนเต็มใน [[Using Claude Code on a Vault]] และ [[Converting Excel and PDF to Raw]]

### 8.3 Query
ตอบจาก wiki ก่อน แล้ว raw ถ้าจำเป็น ถ้าคำตอบมีคุณค่าให้บันทึกใน `queries/`

### 8.4 Lint
- ทุก wikilink ชี้ไปหน้าที่มีจริง
- ทุกหน้าอยู่ใน [[index]] (ไม่มี orphan)
- frontmatter ครบ 8 field
- หน้า stale (`updated` เก่ามาก) ให้ทบทวน
- หน้า `contested: true` มี entry ใน [[log]]

## 9. Raw source ปัจจุบัน

ยังไม่มี (มีเฉพาะ `raw/README.md`) ดู [[LLM Wiki Pattern]] สำหรับหลักการ

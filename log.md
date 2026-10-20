# Log

บันทึก action แบบ **append-only** (ห้ามแก้ entry เก่า) รูปแบบ: `## [วันที่] action | รายละเอียด` ดู [[SCHEMA]] และ [[index]]

## [2026-10-20] init | สร้างโครงสร้าง wiki 3 ชั้น
- สร้าง `SCHEMA.md`, `index.md`, `log.md`, `README.md`, `raw/README.md`, `_archive/README.md`, `queries/README.md` และโฟลเดอร์ `concepts/`, `guides/`, `reference/`, `queries/`, `raw/`, `_archive/`
- Reconcile โครงสร้าง: ใช้ guides/reference แทน entities/comparisons (เหตุผลใน [[SCHEMA]])
- ไม่มี raw source: เขียนจากความรู้ทั่วไป ใช้ `confidence` บอกความมั่นใจ

## [2026-10-20] create | concepts 8 หน้า
- Pages: [[Second Brain]], [[PARA Method]], [[Zettelkasten and Atomic Notes]], [[Maps of Content]], [[LLM Wiki Pattern]], [[Second Brain vs LLM Wiki]], [[Contradiction Handling]], [[Page Thresholds]]
- [[LLM Wiki Pattern]] ตั้ง medium (อธิบายจากความเข้าใจทั่วไปของแนวคิด Karpathy)

## [2026-10-20] create | guides 6 หน้า
- Pages: [[Vault Setup for Fleet Engineering]], [[Obsidian Core Settings]], [[Daily Workflow]], [[Using Claude Code on a Vault]], [[Converting Excel and PDF to Raw]], [[Maintenance Reliability Example]]
- [[Obsidian Core Settings]] ชื่อ menu/key อาจต่างตามเวอร์ชัน (medium)

## [2026-10-20] create | reference 6 หน้า
- Pages: [[Frontmatter Spec]], [[Wikilinks vs Markdown Links]], [[Tags vs Links vs Folders]], [[Templates Reference]], [[Naming Conventions]], [[Obsidian Core Plugins]]
- [[Obsidian Core Plugins]] Bases/Properties/Canvas ความมั่นใจต่ำ-กลาง

## [2026-10-20] create | queries 1 หน้า
- Pages: [[FAQ Obsidian Second Brain and LLM Wiki]]

## [2026-10-20] lint | ตรวจ wikilink และ frontmatter
- ตรวจทุก wikilink ชี้หน้าที่มีจริง และ frontmatter ครบ 8 field (ผลดูรายงานส่งมอบ)
- Pages: [[index]], [[SCHEMA]]

## [2026-10-20] config | ตั้ง auto-sync ไป GitHub
- repo นี้ push ไป https://github.com/pitsanu1976/brain2nd อัตโนมัติผ่าน hook `~/.claude/hooks/llm-wiki-sync.sh` (SubagentStop/Stop)
- Pages: [[SCHEMA]]

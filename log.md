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

## [2026-10-21] migrate | ย้าย Maintenance Reliability wiki เข้า vault นี้
- ผู้ใช้ตัดสินใจย้าย wiki จาก `coce\wiki` (OneDrive Desktop\23 Claude\15 failure hierarchy\coce\wiki) มาไว้ใน knowledge base หลักนี้
- ย้ายมา: entities 11 หน้า, concepts 48 หน้า (ร่วมกับของเดิม 8 หน้า รวม 56), comparisons 3 หน้า, queries 3 หน้า (ร่วมกับ FAQ เดิม), raw sources 3 ชุด (`raw/compressor-failure-hierarchy.md`, `raw/failure-structure.md`, `raw/reliability-based-maintenance-management.md` + notes ต่อบท) พร้อม `raw/datasets/` และ `raw/assets/`; ไม่มีชื่อหน้าชนกัน
- Merge ไฟล์ที่ชนกัน: [[SCHEMA]] (รวม domain 2 area, type เพิ่ม entity/comparison, tag union จัดกลุ่มตาม area, raw source list, ยกเลิกข้อความ "ไม่มี raw source" และ note ที่ตัด entities/comparisons), [[index]], README, [[queries/README]], [[_archive/README]]; แก้ [[Maintenance Reliability Example]] ให้ลิงก์ไปหน้าจริงใน vault
- ประวัติ log เดิมของ wiki นั้น (2026-10-20 ถึง 2026-10-21 รวม entry contested/resolve สถานะ UST vs SPS) เก็บเต็มที่ [[_archive/log-maintenance-reliability-2026-10-20]] ไม่ถูกแก้
- `raw/README.md` (เดิมระบุว่า raw ว่าง) ไม่ได้แก้เพราะ raw immutable; ใช้ [[SCHEMA]] หัวข้อ 9 เป็นหลัก
- Pages: [[SCHEMA]], [[index]], [[Compressor]], [[Failure Hierarchy]], [[Reliability Based Maintenance Management Book]]

## [2026-10-21] lint | ตรวจ vault หลัง merge
- หน้า wiki 86 หน้า (entities 11, concepts 56, comparisons 3, guides 6, reference 6, queries 4) + `queries/README.md`: frontmatter ครบ 8 field ทุกหน้า, `type` อยู่ใน [[SCHEMA]] 5.1, tag ทุกตัวอยู่ใน 5.2, ทุกหน้าอยู่ใน [[index]], ไม่มี alias `|` หรือ Markdown link ภายใน, path-style link 5 รายการชี้ไฟล์ที่มีจริง
- แก้: [[Frontmatter Spec]] เพิ่มรายการ type ให้ตรง [[SCHEMA]]
- Pages: [[index]], [[SCHEMA]]

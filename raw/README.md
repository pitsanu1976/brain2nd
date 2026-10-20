# raw/ — Layer 1 (immutable)

โฟลเดอร์นี้ใช้เก็บ source ภายนอกในอนาคต (articles, เอกสาร, transcripts) ตอนนี้ยังว่าง เพราะเนื้อหา wiki เขียนจากความรู้ทั่วไป

กติกา:
- ทุกไฟล์ต้องมี frontmatter: `source_url`, `ingested`, `sha256` (hash ของ body), `type: raw-source`, `immutable: true`
- หลัง ingest **ห้ามแก้หรือลบ** ถ้าต้นฉบับเปลี่ยน ให้ ingest เป็นไฟล์ใหม่ (versioned) และ log
- ไฟล์ไบนารี (xlsx/pdf) ให้แปลงเป็น Markdown/CSV แล้วเก็บ sha256 ของไฟล์ต้นฉบับ
- ห้ามเขียน wiki page ลงที่นี่

ดู `SCHEMA.md` หัวข้อ 4.2 และ 8.2

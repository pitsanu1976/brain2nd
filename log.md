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

## [2026-10-21] update | เพิ่มประเภทของ Availability
- เพิ่มหัวข้อย่อย "ประเภทของ Availability" ใน [[Availability and OEE]]: Inherent (Ai), Achieved (Aa), Operational (Ao) พร้อมสูตรและการตีความ Ai >= Aa >= Ao
- ที่มา: ความรู้ทั่วไป ไม่มีใน sources ระบุ confidence: low ในหัวข้อย่อย ส่วน confidence ของทั้งหน้าคง medium
- ผู้ใช้อนุมัติหลังถามเรื่อง availability (ตามกติกา propose-then-approve ใน ~/.claude/CLAUDE.md)
- Pages: [[Availability and OEE]], [[index]]

## [2026-10-21] ingest | ISO 14224:2016
- Raw: [[raw/iso-14224]] (sha256 475ee12e…37a4) + reading notes ถอดความ 6 ส่วนใน `raw/iso-14224/` (cl01-07, cl08-09, annex-a, annex-b, annex-c-d, annex-e-f) PDF เป็นสำเนา licensed จึงไม่เก็บ PDF/ข้อความต้นฉบับใน vault Table A.9 และสูตร C.52 ตรวจกับภาพหน้า PDF ที่ render แล้ว
- หน้าใหม่ 8 หน้า: [[ISO 14224 Taxonomy]], [[Compressor Subdivision Wiki vs ISO 14224]], [[Failure Detection Method]], [[Failure Impact Classification]], [[Safety Critical Failure Classification]], [[RM Data Quality]], [[Maintenance Time Definitions]], [[Failure Rate Estimation]]
- เขียนใหม่ [[ISO 14224]] เป็น hub (confidence low -> medium) ความรู้ทั่วไปเดิมยืนยันแล้ว เก็บประวัติ SPS/UST ไว้
- ยืนยันจากมาตรฐาน: spurious stop = UST ไม่มี SPS และไม่มี OWD ในฉบับ 2016; compressor (CO) มี 20 failure mode = 19 ของ dataset + PLU; mechanism Table B.2 มี 38 รหัส (wiki ขาด 3.6 Common cause/mode; Burst = 2.8 Material failure); failure cause Table B.3 (21 รหัส) แยกจาก mechanism ทำให้ CAUSE_CODE ของ dataset เป็นรหัสระดับ mechanism; maintenance activity Table B.5 มี 12 รหัส (ไม่มี NFF/CHG); subunit compressor 6 ตัวตรงกับ dataset แต่ item หลายตัวจัดคนละ subunit และรหัส 4 ตัวอักษรไม่ใช่รหัส ISO; taxonomy 9 ระดับ (wiki ระดับ 1-3 = ISO 6-8)
- อัปเดต: [[Failure Mode]], [[UST Spurious Stop]], [[Failure Mechanism]], [[Failure Cause Codes]], [[CAUSE_CODE Convention]], [[Resolution Codes]], [[Failure Hierarchy]], [[Maintainable Item]], [[Compressor]], [[Failure Data Recording]], [[CMMS]], [[Availability and OEE]], [[Reliability Metrics]], [[Weibull Analysis]], [[Censored Data]], [[Failure Finding Interval]], [[Maintenance KPIs]], [[Criticality Assessment]], [[Redundancy and Standby Systems]]
- **Contested ใหม่ (รอผู้ใช้ตัดสิน):** [[Availability and OEE]] หัวข้อ Ai/Aa/Ao (ความรู้ทั่วไป ใช้ MTBF/MTBM) ขัดกับ ISO Annex C ที่มีเฉพาะ AI = MTTF/(MTTF+MTTRes), Ao = MUT/(MUT+MDT), Ao,y, AT ไม่มี Aa/MTBM; [[Reliability Metrics]] MTBF = MTTF + MTTR + MWT ของ RBMM เทียบ METBF = MUT + MDT ของ ISO
- Contested เดิมที่ยังคงอยู่ (ISO ไม่ได้ตัดสิน): [[Failure Hierarchy]], [[Maintainable Item]] (dataset vs failure-structure Sheet1 เพิ่มคอลัมน์ ISO), [[Failure Cause Codes]], [[Resolution Codes]] (CHG)
- ข้อผิดพลาดภายในมาตรฐานที่ flag: B.2.4 บอก 9 detection categories แต่ Table B.4 มี 11 รหัส; ตัวอย่าง chi-square ใน Annex C ระบุ 95% แต่ตัวเลขเป็นช่วง 90%; top-quartile target ของ KPI #28/#30/#32 ไม่ตรงนิยาม; note 2 ของ 3.29 อ้าง Table B.2 เป็น cause
- อัปเดต [[SCHEMA]] หัวข้อ 1, 2, 9 (raw source ชุดที่ 4) และ [[index]] (94 หน้า)
- Lint หลัง ingest: 122 ไฟล์ ไม่มี broken link, frontmatter ครบ, tag อยู่ใน SCHEMA, ทุกหน้าอยู่ใน index, ไม่มี alias ในตาราง
- Pages: [[ISO 14224]], [[raw/iso-14224]], [[index]], [[SCHEMA]]

## [2026-10-22] update | Knowledge Graph Triplets (area ข)
- ผู้ใช้ขอแปลงความรู้เดิมเป็น Knowledge Graph Triplet เลือกแบบ "Both" (section `## Triplets` ในหน้า + `graph/triplets.csv`) และขอบเขต area ข เท่านั้น
- หน้าใหม่ [[Knowledge Graph Triplet]] (สเปก syntax, node naming, predicate vocabulary 35 ตัว) และโฟลเดอร์ใหม่ `graph/` (`build_triplets.py`, `triplets.csv` ที่ generate)
- เพิ่ม `## Triplets` ใน 73 หน้า area ข (entities 11, concepts 55, comparisons 4, queries 3) ตั้ง `updated: 2026-10-22` ไม่แก้เนื้อหาส่วนอื่น triplet สะท้อนเฉพาะข้อเท็จจริงที่อยู่ในหน้านั้น
- ผล: 4,421 triplets, 0 error, ทุกหน้า area ข มี section รวม mechanism x resolution ครบ 233 คู่ และ item -> sub unit -> mechanism ของทั้ง 6 sub unit
- Normalize: mechanism `INST` -> `Instrument failure - general` (ชนกับ item INST), failure mode ที่มีหน้าเป็น wikilink, ชื่อ instrument subtype และ Shape Parameter Beta ให้ตรงกัน, ถอด `contested` ระดับ triplet ใน 13 หน้าที่ frontmatter `contested: false` (36 triplet ส่วนใหญ่เป็นคำพิมพ์ผิดที่ resolve แล้ว)
- ข้อสังเกตจากการสกัด (ไม่ได้แก้เนื้อหา): [[CMMS]] ระบุ RAM process 7 = FMECA แต่ [[RCM Reliability Centered Maintenance]] ระบุ = Modification Maintenance; [[Spare Part Criticality and Risk]] ABC group A (p.242 vs Fig 9.4) และ [[Maintenance Strategic Report]] E15/E16 ch3 vs ch10 เป็นข้อขัดแย้งที่หน้าไม่ได้ตั้ง contested
- อัปเดต [[SCHEMA]] หัวข้อ 2 (`graph/`), 5.2 (tag `knowledge-graph`), 8.4 (lint triplet), 10 (ใหม่) และ [[index]] (95 หน้า)
- Pages: [[Knowledge Graph Triplet]], [[SCHEMA]], [[index]]

## [2026-10-23] query | How does Weibull help reliability
- ผู้ใช้ถาม "Weibull ช่วย reliability ยังไง" คำตอบสังเคราะห์จากหน้าใน wiki แล้วบันทึกตามคำขอ
- เนื้อหา: β → รูปแบบการเสียและประเภทงาน PM, η, ตัวอย่าง RBMM (β 3.7888, η 13,130.8 ชม., R/MTTF/conditional R), T(R=0.8) ≈ 8,837 ชม. derived (หนังสือพิมพ์ 13,847.81 ผิด), การใช้ต่อใน PM optimization/simulation/อะไหล่, ISO 14224 แนะนำ Weibull เมื่อ λ ไม่คงที่
- เพิ่ม `## Triplets` 18 บรรทัด และ rebuild `graph/triplets.csv`
- Pages: [[How does Weibull help reliability]], [[index]]

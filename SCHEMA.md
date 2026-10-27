# SCHEMA — User-level Knowledge Base (Obsidian Second Brain + LLM Wiki และ Maintenance Reliability)

กติกากลางของ wiki นี้ (Layer 3) อ่านไฟล์นี้ก่อนทำงานทุก session ร่วมกับ [[index]] และ [[log]]

## 1. Domain

wiki นี้ครอบคลุม 2 พื้นที่ (area) ในโฟลเดอร์เดียว ใช้กติกาชุดเดียวกัน

### (ก) Obsidian Second Brain + LLM Wiki method

- หัวข้อ: **การใช้ Obsidian เพื่อรัน Second Brain + LLM Wiki** (PARA, Zettelkasten, MOC, LLM Wiki pattern, vault setup, workflow กับ Claude Code)
- ขอบเขต: แนวคิด, วิธีตั้งค่า vault, workflow รายวัน, การใช้ Claude Code/llm-wiki agent กับ vault, reference (frontmatter, template, naming, core plugins)
- แหล่งความรู้: เขียนจากความรู้ทั่วไป ไม่มี raw source ภายนอก จึงใช้ `confidence` บอกระดับความมั่นใจ (ดูหัวข้อ 4)
- หน้าอยู่ใน `concepts/` (method), `guides/`, `reference/` และ `queries/` (FAQ)

### (ข) Maintenance Reliability

หัวข้อ 2 แกน:
1. **Compressor failure hierarchy** ตาม taxonomy ของ [[OREDA]] / [[ISO 14224]]: ประเภท compressor (centrifugal, reciprocating, screw), sub unit, maintainable item, failure mode, failure mechanism, failure cause, resolution และรหัสที่เกี่ยวข้อง
2. **Reliability-based maintenance management**: RCM, FMECA, Weibull/สถิติ reliability, การเลือกและ optimize PM, อะไหล่, งบประมาณ/ต้นทุนบำรุงรักษา, CMMS และ KPIs (ที่มา: หนังสือ [[Reliability Based Maintenance Management Book]]) และฝั่งคลังพัสดุ/จัดซื้อ MRO (ที่มา: หนังสือ [[Spare Parts Optimization Book]])

- แหล่งความรู้: raw sources 6 ชุด (ดูหัวข้อ 9) ตัวเลข failure rate ของ compressor ทั้งหมดมาจาก OREDA ที่ transcribe ไว้ใน raw ส่วนรหัสและนิยามมาตรฐานยึด ISO 14224:2016
- ตัวอย่างในหนังสือ RBMM เป็นข้อมูลทั่วไป ไม่ใช่ compressor ให้เชื่อมกับ hierarchy ผ่านหัวข้อ "เชื่อมโยงกับ compressor failure hierarchy" ในแต่ละหน้า และระบุว่าเป็นการตีความ
- หน้าอยู่ใน `entities/`, `concepts/`, `comparisons/`, `queries/`
- ตัวอย่างการใช้วิธีของ (ก) กับงานจริง: [[Maintenance Reliability Example]]

### ผู้ใช้และนอกขอบเขต

- ผู้ใช้: Fleet / Maintenance-Reliability engineer, Valeura Energy ที่ทำงานกับ Claude Code
- นอกขอบเขต: community plugin (ห้ามติดตั้งโดยไม่ได้รับอนุญาต), ข้อมูล failure จริงของ asset Valeura (ยังไม่มีใน sources)

## 2. สถาปัตยกรรม 3 ชั้น

| Layer | ที่อยู่ | สถานะ |
|---|---|---|
| 1. Raw sources | `raw/` (`raw/datasets/`, `raw/assets/`, `raw/reliability-based-maintenance-management/`, `raw/iso-14224/`, `raw/CMRP/`, `raw/spare-parts-optimization/`) | **IMMUTABLE** หลัง ingest อ่านอย่างเดียว ห้ามแก้/ลบ |
| 2. Wiki pages | `entities/`, `concepts/`, `comparisons/`, `guides/`, `reference/`, `queries/` | LLM เขียนและดูแล |
| 3. Rules | `SCHEMA.md`, `index.md`, `log.md`, `README.md` | กติกาและแค็ตตาล็อก |

`graph/` เก็บ knowledge graph ที่ generate จากหัวข้อ `## Triplets` ของหน้า wiki (`triplets.csv`) และสคริปต์ `build_triplets.py` (ดูหัวข้อ 10) ไม่ใช่ Layer ใหม่ หน้า wiki ยังเป็น source of truth

`_archive/` เก็บหน้าที่เลิกใช้และประวัติ log ที่แยกเก็บ (ห้ามลบ ให้ย้ายมาและบันทึกใน [[log]])

### โฟลเดอร์ที่ใช้ (reconcile)

- `concepts/`, `queries/` ใช้ร่วมกันทั้งสอง area
- `guides/` (how-to) และ `reference/` (cheat sheet, template) ใช้กับ area (ก)
- `entities/` และ `comparisons/` ใช้กับ area (ข) เพราะมีวัตถุรูปธรรม (compressor, sub unit, หนังสือ) และการเปรียบเทียบข้าม entity/concept ส่วน area (ก) เปรียบเทียบภายใน concept เช่น [[Second Brain vs LLM Wiki]]
- ถ้าต้องเพิ่มโฟลเดอร์ใหม่ ให้แก้หัวข้อนี้และ append [[log]]

## 3. Conventions

- Markdown UTF-8 ชื่อไฟล์ = ชื่อหน้า ภาษาอังกฤษ เว้นวรรคได้ (ดู [[Naming Conventions]])
- ลิงก์ภายในใช้ **Obsidian wikilinks เท่านั้น** (เหตุผลใน [[Wikilinks vs Markdown Links]]) ห้ามใช้ Markdown link สำหรับลิงก์ภายใน
- ห้ามใส่ alias `|` ในตาราง (ทำให้ตารางพัง)
- คำอธิบายเป็นภาษาไทยกระชับ; ชื่อเทคนิค รหัส ชื่อโฟลเดอร์/ไฟล์ ชื่อ setting คงเป็นภาษาอังกฤษ
- ชื่อ menu / setting key ที่อาจต่างตามเวอร์ชัน Obsidian ให้ตั้ง `confidence: medium` หรือ `low`
- (area ข) ตัวเลข (% failure rate ฯลฯ) ต้องตรงกับ source ถ้าเป็นค่าที่คำนวณเอง ให้ระบุว่า "derived" และบอกวิธีคำนวณ
- (area ข) ถ้าข้อมูลไม่มีใน sources ให้เขียนว่าไม่มีใน sources หรือตั้ง `confidence: low`
- วันที่ `YYYY-MM-DD`
- หน้าใหม่ควรมี outbound wikilinks อย่างน้อย 2 ลิงก์เมื่อทำได้
- ไม่สร้างไฟล์นอกโฟลเดอร์ `llm-wiki/`
- ไม่ใส่ตัวอย่าง wikilink ที่ไม่มีหน้าจริงนอก code block (ตัวอย่างใน code block ถูกยกเว้นจาก link check)
- ห้ามเขียนข้อมูลลับ (password, token, ข้อมูลส่วนบุคคล) ลง wiki นี้

## 4. Frontmatter

ดูรายละเอียดเต็มใน [[Frontmatter Spec]]

### 4.1 Wiki page (ทุกหน้าใน entities, concepts, comparisons, guides, reference, queries)

```yaml
---
title: ชื่อหน้า
created: 2026-10-20
updated: 2026-10-20
type: entity | concept | comparison | guide | reference | query
tags: [tag1, tag2]
sources: [compressor-failure-hierarchy.md, failure-structure.md]
confidence: high | medium | low
contested: true | false
---
```

- `sources` = ชื่อไฟล์ใน `raw/` ที่ใช้เขียน (ว่างได้เมื่อเขียนจากความรู้ทั่วไป เช่น หน้า area ก)
- `confidence` (area ก): high = แนวคิดที่นิยามชัดและเสถียร; medium = รายละเอียดที่ขึ้นกับเวอร์ชัน/ตีความ/จำจากความรู้; low = ไม่แน่ใจ ต้องตรวจกับ Obsidian จริง
- `confidence` (area ข): high = ตัวเลข/รหัสคัดลอกตรงจาก data; medium = สังเคราะห์/คำนวณ derived หรืออ่านจากภาพ; low = ความรู้ทั่วไปที่ไม่มีใน sources
- `contested: true` เมื่อข้อมูลขัดแย้งและยังไม่ resolve ([[Contradiction Handling]])
- `README.md` ในโฟลเดอร์ย่อยและไฟล์ rules ไม่บังคับ frontmatter ยกเว้น `queries/README.md` (มี frontmatter ครบ)
- หน้าของ area ข ที่ใช้หนังสือ RBMM ใช้ `sources: [reliability-based-maintenance-management.md]` และอ้างหน้าหนังสือแบบ `(RBMM p.NNN)`

### 4.2 Raw source (อยู่ใน `raw/`)

```yaml
---
title: ชื่อต้นฉบับ
type: raw-source
source_url: ...
ingested: 2026-10-20
sha256: <hash ของ body หรือของไฟล์ต้นฉบับ (ไบนารี)>
immutable: true
---
```

- ไฟล์ข้อความ: sha256 ของ body; ไฟล์ไบนารี (xlsx/pdf): sha256 ของไฟล์ต้นฉบับ แล้วแปลงเป็น Markdown/CSV
- หลัง ingest ห้ามแก้ไข ถ้าต้นฉบับเปลี่ยน ให้ ingest เป็นไฟล์ใหม่ (versioned) และบันทึกใน [[log]]

## 5. Taxonomy

### 5.1 Folder และ page type

| Folder | type | เนื้อหา |
|---|---|---|
| `entities/` | entity | (ข) สิ่งรูปธรรม: ประเภท compressor, Sub Unit (PWTR, CPUN, CTMN, LUBS, SHSS, MISC) และ hub ของหนังสือ/แหล่งข้อมูล (เช่น [[Reliability Based Maintenance Management Book]]) |
| `concepts/` | concept | (ก) Second Brain, PARA, Zettelkasten, MOC, LLM Wiki; (ข) failure hierarchy, failure mode (hub + หน้ารายโหมด), mechanism, cause codes, resolution codes, OREDA, ISO 14224 และแนวคิดบริหารงานบำรุงรักษา (RCM, FMECA, Weibull, PM, อะไหล่, งบประมาณ, CMMS, KPIs) |
| `comparisons/` | comparison | (ข) เปรียบเทียบข้าม entity/concept |
| `guides/` | guide | (ก) how-to เป็นขั้นตอน |
| `reference/` | reference | (ก) cheat sheet, spec, template |
| `queries/` | query | คำถาม-คำตอบที่บันทึกไว้ ตอบจากข้อมูลใน wiki/raw |
| `_archive/` | - | หน้าที่เลิกใช้และ log ประวัติที่แยกเก็บ |

### 5.2 Tag taxonomy (ตัวพิมพ์เล็ก ขีดกลาง จัดกลุ่มตาม area)

**Area ก: Obsidian Second Brain + LLM Wiki**
- Method: `second-brain`, `para`, `zettelkasten`, `moc`, `llm-wiki`, `code-method`
- Obsidian: `obsidian`, `settings`, `plugins`, `templates`, `frontmatter`, `links`, `naming`
- Workflow: `workflow`, `setup`, `claude-code`, `ingest`, `lint`
- Meta: `guide`, `reference`, `convention`, `faq`, `knowledge-graph`

**Area ข: Maintenance Reliability**
- Equipment: `compressor`, `centrifugal`, `reciprocating`, `screw`, `sub-unit`, `maintainable-item`
- Failure: `failure-mode`, `failure-mechanism`, `failure-cause`, `resolution`, `failure-rate`
- Standard: `oreda`, `iso-14224`, `taxonomy`, `coding`
- Meta: `comparison`, `data-quality`, `reliability`, `book`
- Maintenance strategy: `rcm`, `fmeca`, `criticality`, `pm`, `cbm`, `maintenance-management`
- Reliability statistics: `statistics`, `weibull`
- Spares, systems และ KPI: `spare-parts`, `cmms`, `kpi`
- Budget/cost: `budget`, `cost`
- CMRP topics (เพิ่ม 2026-10-25): `cmrp` (source tag), `work-management`, `turnaround`, `rca`, `lubrication`, `vibration`, `spc`, `maintainability`, `reliability-allocation`, `reliability-growth`, `fta`, `human-reliability`, `tpm`, `business-case`
- Spare Parts Optimization topics (เพิ่ม 2026-10-27): `spo` (source tag), `warehousing`, `procurement`, `inventory-control`

**ใช้ร่วม**
- Domain: `maintenance-reliability`, `fleet-engineering`
- Meta: `query`

ต้องการ tag ใหม่ ให้เพิ่มในหัวข้อนี้ก่อนใช้

## 6. Page thresholds

สร้างหน้าใหม่เมื่อ (1) หัวข้อเป็น **แกนหลักของ source หนึ่ง** หรือ (2) ปรากฏใน **อย่างน้อยสอง sources** รายละเอียดและตัวอย่างใน [[Page Thresholds]]

ไม่สร้างหน้าสำหรับหัวข้อที่เป็นแค่การกล่าวถึงผ่าน ๆ (area ข: failure mode เล็ก ๆ ที่ % ต่ำมากให้รวมอยู่ใน [[Failure Mode]]; หน้ารายโหมดสร้างสำหรับ 9 โหมดที่ % สูง: AIR, SER, LOO, ELU, PDE, OTH, ELP, OHE, UST)

## 7. Update policy

- ก่อนแก้หน้าเดิม ให้อ่านทั้งหน้า แล้วอัปเดต `updated`
- **ข้อมูลขัดแย้ง ห้ามเขียนทับเงียบ ๆ** เก็บทั้งสองมุมมองพร้อมระบุ source ตั้ง `contested: true` และ log ([[Contradiction Handling]])
- เมื่อ resolve แล้ว ให้คงข้อความประวัติไว้ ตั้ง `contested: false` และ log การตัดสินใจ
- หน้าที่เลิกใช้ย้ายไป `_archive/` (ไม่ลบ) และอัปเดต [[index]]
- หน้าใหม่ทุกหน้าต้องอยู่ใน [[index]] และมี outbound wikilinks อย่างน้อย 2 ลิงก์
- ทุก action ต้อง **append** ใน [[log]] (append-only ห้ามแก้ entry เก่า)
- ห้ามสร้าง broken link
- การ "เพิ่ม knowledge" โดยไม่ระบุ path ให้เขียนลงที่นี่ (repo นี้ sync ไป GitHub อัตโนมัติผ่าน hook ไม่ต้อง commit เอง)

## 8. Maintenance workflow

### 8.1 เริ่ม session
1. อ่าน `SCHEMA.md`
2. อ่าน [[index]]
3. อ่าน 20–30 entry ล่าสุดของ [[log]]

### 8.2 Ingest
1. วางไฟล์ใน `raw/` พร้อม `source_url`, `ingested`, `sha256`
2. ตรวจ threshold (หัวข้อ 6) แล้วสร้าง/อัปเดตหน้า
3. เพิ่มใน [[index]]
4. ตรวจความขัดแย้ง (หัวข้อ 7)
5. append [[log]]

ขั้นตอนเต็มใน [[Using Claude Code on a Vault]] และ [[Converting Excel and PDF to Raw]]

### 8.3 Query
ตอบจาก wiki ก่อน แล้ว raw ถ้าจำเป็น ถ้าคำตอบมีคุณค่าให้บันทึกใน `queries/`

### 8.4 Lint
- ทุก wikilink ชี้ไปหน้าที่มีจริง
- ทุกหน้าอยู่ใน [[index]] (ไม่มี orphan)
- frontmatter ครบ 8 field และ `type`/tag อยู่ในกติกานี้
- (area ข) ตัวเลขตรงกับ raw (สุ่มตรวจกับ `raw/datasets/`)
- หน้า stale (`updated` เก่ามาก) ให้ทบทวน
- หน้า `contested: true` มี entry ใน [[log]]
- (area ข) ทุกหน้ามีหัวข้อ `## Triplets` และ `python -I graph/build_triplets.py --check` ไม่มี ERROR/MISSING

## 9. Raw source ปัจจุบัน (area ข)

Area ก ไม่มี raw source ดู [[LLM Wiki Pattern]] สำหรับหลักการ

- [[raw/compressor-failure-hierarchy]] และ CSV ใน `raw/datasets/compressor-failure-hierarchy__*.csv`
- [[raw/failure-structure]] และ `raw/datasets/failure-structure__sheet1.csv`, `__sheet2.csv`
- `raw/assets/` ภาพ OREDA (failure descriptor, failure mode vs maintainable item, failure mechanism, resolution)
- [[raw/reliability-based-maintenance-management]] (ingest 2026-10-21; PDF สแกน -> reading notes สรุปความ ไม่ใช่ข้อความต้นฉบับ) และ notes ต่อบทใน `raw/reliability-based-maintenance-management/` (`ch01-02.md`, `ch03.md`, `ch04.md`, `ch05.md`, `ch06.md`, `ch07.md`, `ch08-09.md`, `ch10.md`, `ch11.md`, `ch12.md`) ใช้ `sources: [reliability-based-maintenance-management.md]` และอ้างหน้าหนังสือแบบ `(RBMM p.NNN)`
- [[raw/reliability-based-maintenance-management-ocr]] (ingest 2026-10-27; OCR ข้อความเต็มของหนังสือ RBMM `raw/reliability_base_maintenance_management_master.md` เก็บในเครื่องเท่านั้น gitignored) ใช้ตรวจทาน reading notes เดิม ผลตรวจอยู่ใน `raw/reliability-based-maintenance-management/ocr-check/` (`ch01-03.md`, `ch04-05.md`, `ch06-07.md`, `ch08-09.md`, `ch10.md`, `ch11-12.md`) หน้าที่แก้ตามผลตรวจเพิ่ม `reliability-based-maintenance-management-ocr.md` ใน `sources` และอ้างเลขหน้าแบบเดิม `(RBMM p.NNN)`
- [[raw/iso-14224]] (ingest 2026-10-21; ISO 14224:2016 PDF licensed ไม่เก็บใน vault -> reading notes ถอดความต่อส่วนใน `raw/iso-14224/`: `cl01-07.md`, `cl08-09.md`, `annex-a.md`, `annex-b.md`, `annex-c-d.md`, `annex-e-f.md`) ใช้ `sources: [iso-14224.md]` และอ้างแบบ `(ISO 14224 cl. X.Y, p.NN)` หรือ `(ISO 14224 Table B.6, p.NN)` ด้วยเลข printed page
- [[raw/cmrp]] (ingest 2026-10-25; สไลด์หลักสูตร CMRP ของ PETROSYNC 11 ไฟล์ 408 หน้า สแกน + OCR, PDF มีลิขสิทธิ์ เก็บในเครื่องเท่านั้น gitignored) reading notes ถอดความต่อไฟล์ `raw/CMRP/CMPR-01.md` ถึง `CMPR-11.md` ใช้ `sources: [cmrp.md]` และอ้างแบบ `(CMRP CMPR-0X p.N)` ด้วยเลข PDF page; เป็นสื่อการสอน (secondary source) ระดับความเชื่อถือต่ำกว่ามาตรฐาน ISO ถ้าขัดกับ ISO ให้ถือเป็น contested และระบุ
- [[raw/spare-parts-optimization]] (ingest 2026-10-27; หนังสือ Spare Parts Optimization ของ เรือเอก สุชาติ ศุภมงคล, SE-ED 2546, 143 หน้า; OCR ทั้งเล่ม `raw/sparepart_optimizaton.md` มีลิขสิทธิ์ เก็บในเครื่องเท่านั้น gitignored) reading notes ถอดความต่อบทใน `raw/spare-parts-optimization/` (`ch01-04.md`, `ch05-06.md`, `ch07.md`, `ch08.md`, `ch09.md`, `ch10.md`, `ch11-12.md`) ใช้ `sources: [spare-parts-optimization.md]` และอ้างแบบ `(SPO p.NN)` ด้วยเลขหน้าที่พิมพ์ในหนังสือ; มุมมองฝั่งคลังพัสดุ/จัดซื้อ ถ้าขัดกับ RBMM ให้เก็บทั้งสองมุมมอง

หมายเหตุ: `raw/README.md` เป็นไฟล์เดิมของ area ก ที่ระบุว่า raw ยังว่าง ข้อความนั้นล้าสมัยแล้ว (ไฟล์ immutable ไม่แก้) ให้ยึดหัวข้อนี้เป็นหลัก ประวัติ log ของ area ข ก่อนรวม vault อยู่ที่ [[_archive/log-maintenance-reliability-2026-10-20]]

## 10. Knowledge graph triplets (area ข)

สเปกเต็ม (syntax, node naming, predicate vocabulary) อยู่ใน [[Knowledge Graph Triplet]]

- ทุกหน้า area ข (`entities/`, `comparisons/`, หน้า area ข ใน `concepts/` และ `queries/`) ต้องมีหัวข้อ `## Triplets` เป็นหัวข้อสุดท้ายของหน้า
- หนึ่งบรรทัดต่อหนึ่ง triplet: `- <subject> [<predicate>:: <object>] <qualifier>` ใช้เฉพาะ predicate ใน vocabulary
- triplet สะท้อนเนื้อหาที่เขียนในหน้านั้นเท่านั้น เมื่อแก้เนื้อหาหน้า ให้แก้ triplet ให้ตรงกันในครั้งเดียวกัน
- ข้อมูล contested ใส่ `[contested:: true]` ทั้งสองมุมมอง ตามหัวข้อ 7
- หลังแก้ triplet ให้รัน `python -I graph/build_triplets.py` เพื่อสร้าง `graph/triplets.csv` ใหม่ (ไฟล์ generate ห้ามแก้ด้วยมือ)
- เพิ่ม predicate ใหม่: เพิ่มแถวในตาราง vocabulary ของ [[Knowledge Graph Triplet]] ก่อนใช้ และ append [[log]]
- area ก ไม่บังคับ triplet

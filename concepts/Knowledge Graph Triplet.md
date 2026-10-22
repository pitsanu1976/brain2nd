---
title: Knowledge Graph Triplet
created: 2026-10-22
updated: 2026-10-22
type: concept
tags: [knowledge-graph, llm-wiki, convention]
sources: []
confidence: medium
contested: false
---

# Knowledge Graph Triplet

Triplet = ข้อเท็จจริงหนึ่งข้อในรูป **subject – predicate – object** เช่น `OHE Overheating – dominant_in – Reciprocating Compressor` ทำให้ความรู้ในหน้า wiki ถูก query เป็นกราฟได้ (หา path, นับความสัมพันธ์, ตรวจความครบ) แทนการอ่านข้อความทีละหน้า เป็นส่วนเสริมของ [[LLM Wiki Pattern]]: หน้า wiki ยังเป็น source of truth ส่วน triplet เป็นดัชนีแบบมีโครงสร้างของเนื้อหาในหน้านั้น

ใช้กับหน้า area ข (Maintenance Reliability) ทั้งหมด: `entities/`, `concepts/` (area ข), `comparisons/`, `queries/` (area ข) กติกาอยู่ใน [[SCHEMA]] หัวข้อ 10

## Syntax ในหน้า wiki

ท้ายหน้ามีหัวข้อ `## Triplets` หนึ่งบรรทัดต่อหนึ่ง triplet:

```markdown
## Triplets

- [[OHE Overheating]] [is_a:: [[Failure Mode]]]
- [[OHE Overheating]] [has_code:: OHE]
- [[OHE Overheating]] [has_failure_rate_share:: 4.18%] all compressor types
- Cylinder liner [contributes_to:: [[OHE Overheating]]] 3.40% of total failure rate
- [[OHE Overheating]] [dominant_in:: [[Reciprocating Compressor]]] 8.85% [confidence:: high]
```

- รูปแบบ: `- <subject> [<predicate>:: <object>] <qualifier> [confidence:: x]`
- subject/object ที่มีหน้าใน wiki ใช้ wikilink ถ้าไม่มีหน้าใช้ข้อความธรรมดา (เช่น maintainable item, mechanism, รหัส) ห้ามสร้าง wikilink ไปหน้าที่ไม่มีจริง
- object ที่เป็นค่า (ตัวเลข, รหัส, สูตร) เป็น literal ได้ ใส่หน่วยหรือ % ด้วย ห้ามมี `]` ใน object (parser ตัดที่ `]`) สูตรที่มีวงเล็บเหลี่ยมให้เขียนเป็น `( )` และบอกใน qualifier
- qualifier = ข้อความสั้นหลัง `]` ระบุบริบท (ฐานของ %, ประเภท compressor, เลขหน้า source เช่น `(ISO 14224 Table B.6, p.NN)`)
- `confidence` และ `sources` ของ triplet ใช้ค่าจาก frontmatter ของหน้าเป็นค่าเริ่มต้น ใส่ `[confidence:: low]` เมื่อ triplet นั้นเป็นความรู้ทั่วไปหรือ derived ต่ำกว่าระดับหน้า
- triplet ที่มาจากข้อมูลขัดแย้งใส่ `[contested:: true]` และต้องมีทั้งสองมุมมองเป็นสอง triplet พร้อม qualifier บอก source ใช้ได้เฉพาะหน้าที่ frontmatter `contested: true` ส่วนคำพิมพ์ผิดที่หน้า resolve แล้ว ให้เก็บค่าที่ถูกเป็น triplet หลัก และค่าที่พิมพ์ผิดเป็น `contradicts` โดยไม่ตั้ง contested
- triplet ต้องสะท้อนสิ่งที่เขียนในหน้านั้นแล้วเท่านั้น ไม่เพิ่มข้อเท็จจริงใหม่ใน section นี้
- syntax `[key:: value]` คือ inline field ของ community plugin Dataview จึง query ได้ถ้าผู้ใช้ติดตั้งเอง (ยังไม่ได้ติดตั้ง; SCHEMA ห้ามติดตั้ง plugin โดยไม่ได้รับอนุญาต) ถ้าไม่มี Dataview ข้อความยังอ่านได้ตามปกติ

## Node naming

ชื่อ node ต้องเหมือนกันทุกหน้า มิฉะนั้นกราฟจะแตกเป็นหลาย node ที่หมายถึงสิ่งเดียวกัน

| ชนิด node | รูปแบบ | ตัวอย่าง |
|---|---|---|
| สิ่งที่มีหน้าใน wiki | wikilink ชื่อหน้า | `[[CPUN Compressor Unit]]`, `[[OHE Overheating]]`, `[[Weibull Analysis]]` |
| Failure mode ที่ไม่มีหน้า | รหัส 3 ตัวอักษรของ dataset | `BRD`, `INL`, `PLU` |
| Failure mechanism | รหัส 4 ตัวอักษรของ dataset (ไม่มีรหัสใช้ชื่อตาม [[Failure Mechanism]]); ยกเว้น `INST` ที่ชนกับรหัส item Instruments ให้ใช้ชื่อ `Instrument failure - general` | `WEAR`, `BLKG`, `Combined causes`, `Instrument failure - general` |
| Resolution | รหัส 3 ตัวอักษรของ dataset | `RPL`, `CHK`, `CHG` |
| Maintainable item (class) | รหัส 4 ตัวอักษรของ dataset | `INST`, `CYLN` |
| Maintainable item ใน sub unit | `<SUBUNIT>-<ITEM>` | `CPUN-CYLN`, `LUBS-FILT` |
| CAUSE_CODE | รหัสเต็มตาม [[CAUSE_CODE Convention]] (ใส่เฉพาะที่หน้าระบุ ไม่ enumerate ทั้ง 473) | `CPUN-CYLN-WEAR` |
| รหัสของ ISO 14224 | `ISO:<table>-<code>` (ตัวตารางเองใช้ `ISO:<table>`) | `ISO:B.6-PLU`, `ISO:B.2-3.6`, `ISO:A.4-CO`, `ISO:A.8-CE`, `ISO:A.9-Valves` |
| Item ตาม OREDA ต่อประเภทที่ไม่มีรหัส | ชื่ออังกฤษ Title Case | `Instrument Temperature`, `Unknown` (placeholder) |
| แนวคิด/ค่าที่ไม่มีหน้า | ชื่ออังกฤษ Title Case ตามที่หน้าใช้ | `Mean Time To Repair`, `Holding Cost` |

ชื่อเต็มของรหัสให้ใส่ครั้งเดียวที่หน้า hub ของรหัสนั้นด้วย `has_label` (เช่น `WEAR [has_label:: Wear]` ที่ [[Failure Mechanism]], `CYLN [has_label:: Cylinder liner]` ที่ [[Maintainable Item]])

## Predicate vocabulary

ใช้เฉพาะ predicate ในตารางนี้ (snake_case ภาษาอังกฤษ) ต้องการเพิ่ม ให้เพิ่มแถวในตารางนี้ก่อนและ append [[log]] สคริปต์ `graph/build_triplets.py` อ่านตารางนี้เป็นรายการที่อนุญาต

| predicate | inverse | domain -> range | ความหมาย |
|---|---|---|---|
| is_a | - | any -> class | เป็นชนิดหนึ่งของ / เป็นสมาชิกของกลุ่ม |
| part_of | has_part | part -> whole | เป็นส่วนประกอบของ (item -> sub unit -> equipment) |
| has_part | part_of | whole -> part | มีส่วนประกอบ |
| has_code | - | any -> literal | รหัสของสิ่งนี้ |
| has_label | - | code -> literal | ชื่อเต็มของรหัส (เช่น `WEAR` -> Wear) |
| alias_of | - | name -> name | ชื่อ/รหัสอื่นที่หมายถึงสิ่งเดียวกัน |
| maps_to | - | code -> code | เทียบได้กับ (ข้ามระบบรหัส เช่น dataset -> ISO) |
| differs_from | - | any -> any | ต่างกันอย่างมีนัย (ระบุความต่างใน qualifier) |
| at_level | - | class -> literal | อยู่ระดับใดของ hierarchy/taxonomy |
| has_failure_mode | failure_mode_of | equipment/item -> mode | เกิด failure mode นี้ได้ |
| failure_mode_of | has_failure_mode | mode -> equipment/item | เป็น failure mode ของ |
| has_mechanism | - | mode/item -> mechanism | เกิดจาก failure mechanism นี้ |
| has_cause | - | mechanism/mode -> cause | มี failure cause นี้ |
| resolved_by | - | mechanism/mode -> resolution | แก้ไขด้วย resolution/maintenance activity นี้ |
| detected_by | - | mode/failure -> method | ตรวจพบด้วยวิธีนี้ |
| contributes_to | - | item/sub unit -> mode/metric | มีสัดส่วนต่อ (ค่า % ใน qualifier) |
| dominant_in | - | mode/item -> equipment type | เด่น/สัดส่วนสูงในประเภทนี้ |
| has_failure_rate_share | - | any -> literal | % ของ total failure rate (ระบุฐานใน qualifier) |
| has_value | - | any -> literal | ค่าตัวเลข/จำนวนอื่น (ระบุความหมายใน qualifier) |
| has_category | - | any -> literal/class | หมวดหมู่ตามการจัดกลุ่มของ source |
| has_parameter | - | model/method -> parameter | มีพารามิเตอร์ |
| has_formula | - | metric -> literal | สูตรคำนวณ |
| measures | - | KPI/metric -> quantity | วัดสิ่งนี้ |
| uses | - | method/system -> method/data | ใช้/ต้องใช้ |
| input_to | - | data/result -> method | เป็น input ของ |
| produces | - | method -> output | ให้ผลลัพธ์ |
| depends_on | - | any -> any | ขึ้นกับ / ถูกกำหนดโดย |
| selects | - | method -> option | ใช้เลือก (เช่น task selection -> ประเภทงาน PM) |
| applies_to | - | method/rule -> scope | ใช้กับ / มีขอบเขตที่ |
| step_of | - | step -> process | เป็นขั้นตอนของกระบวนการ |
| defined_in | - | concept -> source | นิยามไว้ใน (มาตรฐาน/หนังสือ/dataset) |
| source_of | - | source -> data | เป็นแหล่งข้อมูลของ |
| contradicts | - | claim -> claim | ขัดแย้งกับ (คู่กับ `contested:: true`) |
| related_to | - | any -> any | เกี่ยวข้อง (ใช้เมื่อไม่มี predicate ที่เจาะจงกว่า) |

ทิศทางมาตรฐาน: ถ้ามี inverse สคริปต์จะแปลง `has_part` -> `part_of` และ `failure_mode_of` -> `has_failure_mode` (สลับ subject/object) ก่อนเขียน CSV เพื่อไม่ให้มี edge ซ้ำ

## ไฟล์กราฟรวม

- `graph/build_triplets.py` อ่าน section `## Triplets` ของทุกหน้า area ข ตรวจ predicate และ wikilink แล้วเขียน `graph/triplets.csv`
- คอลัมน์: `subject, predicate, object, qualifier, confidence, contested, sources, page`
- `graph/triplets.csv` เป็นไฟล์ที่ generate ห้ามแก้ด้วยมือ แก้ที่หน้า wiki แล้วรันสคริปต์ใหม่

```bash
python -I graph/build_triplets.py
```

รัน `python -I graph/build_triplets.py --check` เพื่อตรวจอย่างเดียว (ไม่เขียนไฟล์) เป็นส่วนหนึ่งของ lint

## ตัวอย่าง query (Dataview, ถ้าติดตั้ง)

````markdown
```dataview
TABLE WITHOUT ID L.text AS triplet, file.link AS page
FROM "concepts" OR "entities"
FLATTEN file.lists AS L
WHERE L.dominant_in
```
````

หรือเปิด `graph/triplets.csv` ใน Excel / pandas / Neo4j (`LOAD CSV`) เพื่อวิเคราะห์ path เช่น Compressor -> sub unit -> item -> mode -> mechanism -> resolution ตาม [[Failure Hierarchy]]

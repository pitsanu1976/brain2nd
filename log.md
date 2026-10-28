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

## [2026-10-23] query | How to set up CMMS failure structure to support FMECA
- ผู้ใช้ถาม "ตั้ง failure structure ใน CMMS ให้ support FMECA" และอนุมัติให้บันทึกเป็นหน้า query (ตามกติกา propose-then-approve ใน ~/.claude/CLAUDE.md)
- เนื้อหา: โครง 3 ชั้น (master data: hierarchy ISO level 1-9 + catalog ISO Table B.2-B.6, C.2 + valid combination; FMECA library 1 แถวต่อ failure mode ต่อ MI ต่อ equipment class; WO failure report) และการปิด loop ให้ WO ปรับ O/S/D
- ส่วนที่เป็นข้อเสนอ/ความรู้ทั่วไปติด confidence: low: valid combination จาก OREDA matrix, การ map detection method -> คะแนน D, ตัวอย่าง SAP catalog profile / Maximo failure hierarchy
- เพิ่ม `## Triplets` 27 บรรทัด และ rebuild `graph/triplets.csv` (4,466 triplets, 0 error)
- Pages: [[How to set up CMMS failure structure to support FMECA]], [[index]], [[queries/README]]

## [2026-10-25] ingest | CMRP course slides (PETROSYNC)
- Raw: [[raw/cmrp]] + reading notes ถอดความ 11 ไฟล์ `raw/CMRP/CMPR-01.md` ถึง `CMPR-11.md` (408 หน้าสแกน + OCR; render ภาพหน้าที่ OCR อ่านไม่ได้) PDF เป็นสื่อการสอนที่มีลิขสิทธิ์ จึงเพิ่ม `raw/CMRP/*.pdf` ใน `.gitignore` (เก็บในเครื่องเท่านั้น) และพบ `raw/iso-14224/ISO 14224.pdf` ที่ถูกคัดลอกเข้ามาภายหลัง จึงเพิ่ม `raw/iso-14224/*.pdf` ใน `.gitignore` ด้วย ตามที่ [[raw/iso-14224]] ระบุว่าไม่เก็บ PDF ใน vault
- [[SCHEMA]]: เพิ่ม tag กลุ่ม CMRP topics ใน 5.2 และ raw source ชุดที่ 5 ในหัวข้อ 1, 2, 9 (CMRP เป็น secondary teaching source ถ้าขัดกับ ISO ให้ถือ contested)
- หน้าใหม่ 18 หน้า: [[CMRP Course]] (hub), [[Wear Mechanisms]], [[Lubrication and Oil Analysis]], [[Condition Monitoring Techniques]], [[Root Cause Analysis]], [[CMRP vs RBMM FMECA Scales]], [[Maintenance Planning and Scheduling]], [[Maintenance Backlog and Schedule Compliance]], [[Turnaround Management]], [[Maintainability]], [[Reliability Allocation]], [[Statistical Process Control]], [[Fault Tree Analysis]], [[Reliability Growth Models]], [[Human Reliability]], [[TPM and Lean Maintenance]], [[Maintenance Business Case]], [[Digital Maintenance and Predictive Analytics]]
- อัปเดตหน้าเดิม 31 หน้า เช่น [[FMECA]], [[Criticality Assessment]], [[PM Task Selection]], [[P-F Interval and Condition Monitoring]], [[Failure Finding Interval]], [[Availability and OEE]], [[Maintenance KPIs]], [[CMMS]], [[Maintenance Budget]], [[Spare Parts Management]], [[Spare Part Criticality and Risk]], [[EOQ and Reorder Point]], [[Statistical Distributions for Maintenance]], [[Weibull Analysis]], [[PM Interval Optimization]], [[Reliability Metrics]], [[Maintenance Time Definitions]], [[Reliability Block Diagram]], [[Failure Patterns and Bathtub Curve]], [[Asset Life Cycle]] พร้อม `## Triplets`
- **Contested ใหม่ (รอผู้ใช้ตัดสิน):** [[P-F Interval and Condition Monitoring]] คาบตรวจ CMRP T = PF / 0.75 PF vs RBMM (P-F)/2; [[Failure Finding Interval]] CMRP MTTF x 3 x (1-A) ที่ criticality สูง vs มาตรฐาน 2 x U x MTBF (กรณี moderate ตรงกับมาตรฐาน; ตรวจการจับคู่กับภาพ CMPR-03 p.12 แล้ว); [[Maintenance Budget]] ค่าแรงพนักงานระหว่าง turnaround (CMRP นับ vs RBMM ไม่นับ)
- [[Availability and OEE]] ยัง contested: CMRP (CMPR-04 p.21-23) เป็น source ของฝั่ง Ai/Aa/Ao ที่เดิมเป็นความรู้ทั่วไป แต่ยังต่างจาก ISO AI/Ao/AT และ CMRP เองใช้ MTBF/MTBM ไม่ตรงกันระหว่าง p.21 กับ p.23
- ยืนยันจาก CMRP: คำเตือน RPN คูณเลข ordinal (CMPR-02 p.33), กฎ n-1 ของ sample SD, ปริพันธ์ PM cost 0..tp, ความหมายของ β ใน Weibull
- ข้อผิดพลาดในสไลด์ที่ flag (ไม่ contested) เช่น RPN 382→392, 40→49, 70→84; 0.541→0.648; UCL_R 7.5→7.6; confidence interval ใช้ SD หาร n; 0.3 in/s ≠ 5.0 mm/s; 29 CFR 1910.119; wrench time ปนฐาน 12 กับ 15 ชม. (ฐานเดียวกันได้ 6 คน); รายการเต็มใน [[CMRP Course]]
- แก้ตามการตรวจภาพ: คาบ SM ของ CMRP = TTF (moderate) / 0.75 TTF (high) ไม่ใช่ "ไม่มี margin ทั้งหมด" ([[PM Task Selection]], [[P-F Interval and Condition Monitoring]]); เปลี่ยน node `Root Cause Analysis` เป็น wikilink ใน [[Failure Cause Codes]], [[Failure Data Recording]]; เพิ่ม pointer ใน [[Maintenance Cost Structure]]
- Lint: 155 ไฟล์ ไม่มี broken link, frontmatter/tag ครบ, ทุกหน้าอยู่ใน index; `graph/triplets.csv` 5,350 triplets 0 error
- Pages: [[CMRP Course]], [[raw/cmrp]], [[index]], [[SCHEMA]]

## [2026-10-27] ingest | Spare Parts Optimization (SPO) book
- Raw: [[raw/spare-parts-optimization]] หนังสือ "Spare Parts Optimization: การจัดการอะไหล่ให้เพิ่มผลผลิต (ฉบับปรับปรุง)" ของ เรือเอก สุชาติ ศุภมงคล (SE-ED 2546, ISBN 974-584-871-6, 143 PDF pages) ผู้ใช้วางไฟล์ OCR ทั้งเล่ม `raw/sparepart_optimizaton.md` (sha256 59e43f9c...) เป็นข้อความเต็มของหนังสือมีลิขสิทธิ์ จึงเพิ่มใน `.gitignore` (เก็บในเครื่องเท่านั้น) และไม่แก้ไฟล์นั้น
- Reading notes ถอดความ 7 ไฟล์ใน `raw/spare-parts-optimization/` (`ch01-04`, `ch05-06`, `ch07`, `ch08`, `ch09`, `ch10`, `ch11-12`) อ้างแบบ `(SPO p.NN)` ด้วยเลขหน้าที่พิมพ์ (PDF ขาดหน้าว่างหลังปกบท: offset +1 ถึง +6 ตามช่วงบท) แก้เครื่องหมาย offset ใน `ch09.md` (+5) ก่อนปิด ingest
- [[SCHEMA]]: tag ใหม่ `spo`, `warehousing`, `procurement`, `inventory-control` (5.2); raw source ชุดที่ 6 ในหัวข้อ 1, 2, 9
- หน้าใหม่ 11 หน้า: [[Spare Parts Optimization Book]] (hub), [[MRO Material Classification]], [[Parts Interchangeability]], [[Spare Parts Recommendation by Equipment Type]], [[Warehouse Design and Storage]], [[Tool Crib and Warehouse Security]], [[MRO Purchasing and Contracting]], [[MRO Inventory Control Methods]], [[Inventory Turnover and GPI Benchmarks]], [[MRO Inventory Reduction Program]], [[SPO vs RBMM Spare Parts Approaches]]
- อัปเดตหน้าเดิม 7 หน้า: [[Spare Parts Management]], [[Spare Part Criticality and Risk]], [[EOQ and Reorder Point]], [[Maintenance KPIs]], [[Turnaround Management]], [[Centrifugal Compressor]], [[Reciprocating Compressor]] พร้อม `## Triplets`
- **Contested ใหม่ (รอผู้ใช้ตัดสิน):** (C1) ABC กลุ่ม A: SPO และข้อความ RBMM p.242 = มูลค่าใช้สูง vs รูปที่ 9.4 ของ RBMM ติดป้าย A = Very Slow ([[SPO vs RBMM Spare Parts Approaches]], [[Spare Part Criticality and Risk]]); (C2) เป้ามูลค่าสต็อก: SPO ไม่เกิน 4% GPI / 3-4% สำหรับโรงงานไทย vs RBMM 1-3% ของราคาเครื่องจักร ([[SPO vs RBMM Spare Parts Approaches]], [[Spare Parts Management]], [[Inventory Turnover and GPI Benchmarks]])
- ไม่ contested (ต่างบริบท/ศัพท์): holding cost SPO ตัวอย่าง 30% vs RBMM 15-20%; safety stock % ของ D×LT vs z·σ; "Blanket Order" ของ RBMM ตรงกับ Consignment/Vendor Stocking ของ SPO; commissioning spares เห็นตรงกัน (ผู้รับเหมารับผิดชอบ)
- ข้อผิดพลาดในหนังสือที่ flag (ตรวจคำนวณซ้ำ) เช่น DOS variance 22,000→22,500 (สุทธิ 47,500), %GPI ธ.ค. 3.58→3.98, retail 1.4/11.16→1.33/11.11, 13 รอบ ≈ 28 วัน ไม่ใช่ 20, "95% ของรายการ" ควรเป็นของมูลค่า, Table 2 air fin 7 เครื่อง 1.4, coupling "1%"; รายการเต็มใน [[Spare Parts Optimization Book]]
- Lint: ไม่มี broken link, frontmatter/tag ครบ, ทุกหน้าอยู่ใน [[index]] (126 หน้า); `graph/triplets.csv` rebuild 0 error
- Pages: [[Spare Parts Optimization Book]], [[raw/spare-parts-optimization]], [[index]], [[SCHEMA]]

## [2026-10-27] resolve | ABC กลุ่ม A (C1)
- ผู้ใช้ตัดสิน: ABC กลุ่ม A ยึดตาม SPO คือ "มูลค่าใช้สูง" (ตรงกับข้อความ RBMM p.242) ป้าย "Very Slow" ในรูปที่ 9.4 ของ RBMM ถือเป็นความผิดพลาดของรูป
- คงข้อความประวัติไว้ และเพิ่มบรรทัดผลตัดสิน; [[Spare Part Criticality and Risk]] ตั้ง `contested: false` (ไม่มีข้อขัดแย้งอื่นในหน้า) แก้คำอธิบายกลุ่ม A ในตาราง ABC; triplet ป้าย Very Slow เปลี่ยนเป็น `contradicts` และถอด `[contested:: true]`
- [[SPO vs RBMM Spare Parts Approaches]] ยัง `contested: true` เพราะ C2 (เป้ามูลค่าสต็อก) ยังรอผู้ใช้ตัดสิน; เพิ่มหมายเหตุผลตัดสินใน [[MRO Inventory Reduction Program]] และอัปเดต [[index]]
- Pages: [[Spare Part Criticality and Risk]], [[SPO vs RBMM Spare Parts Approaches]], [[MRO Inventory Reduction Program]], [[index]]

## [2026-10-27] resolve | เป้ามูลค่าสต็อก (C2)
- ผู้ใช้ตัดสิน: เป้ามูลค่าสต็อกอะไหล่ยึดตาม SPO คือไม่เกิน 4% ของ GPI (3-4% สำหรับโรงงานเน้นเครื่องจักรในไทย, 1-1.5% สำหรับเครื่องจักรไม่ซับซ้อน) ค่า 1-3% ของราคาเครื่องจักรของ RBMM เก็บไว้เป็นข้อมูลอ้างอิง ไม่ใช้เป็นเป้า
- คงข้อความประวัติไว้ และเพิ่มบรรทัดผลตัดสิน; ตั้ง `contested: false` ใน [[SPO vs RBMM Spare Parts Approaches]], [[Spare Parts Management]], [[Inventory Turnover and GPI Benchmarks]] และถอด `[contested:: true]` ของ triplet ที่เกี่ยวข้อง; อัปเดต [[index]]
- ข้อขัดแย้งจากการ ingest SPO ทั้ง 2 ข้อ (C1, C2) resolve ครบ
- Pages: [[SPO vs RBMM Spare Parts Approaches]], [[Spare Parts Management]], [[Inventory Turnover and GPI Benchmarks]], [[index]]

## [2026-10-28] ingest | Maintenance: The Profit Maker (MPM) book
- Raw: [[raw/maintenance-profit-maker]] หนังสือ "Maintenance: The Profit Maker — บำรุงรักษา : งานเพิ่มกำไรบริษัท" ของ วัฒนา เชียงกูล, เกรียงไกร ดำรงรัตน์ (SE-ED 2556, ISBN e-book 978-616-08-1057-4, 277 หน้า) ผู้ใช้วางไฟล์ OCR ทั้งเล่ม `raw/maintenance_profit_maker.md` (sha256 c3a5cc19...) เป็นข้อความเต็มของหนังสือมีลิขสิทธิ์ จึงเพิ่มใน `.gitignore` (เก็บในเครื่องเท่านั้น) และไม่แก้ไฟล์นั้น
- Reading notes ถอดความ 7 ไฟล์ใน `raw/maintenance-profit-maker/` (`ch01-03`, `ch04-05`, `ch06-07`, `ch08-09`, `ch10-11`, `ch12`, `ch13-15`) อ้างแบบ `(MPM p.NN)` ด้วยเลขหน้าที่พิมพ์; marker `printed:` ของ OCR ผิด 3 ช่วง notes ใช้เลขที่แก้แล้ว; แก้หัวตารางสารบัญที่ขาดใน `ch01-03.md` ก่อนปิด ingest
- [[SCHEMA]]: tag ใหม่ `mpm`, `outsourcing`, `lcc`, `engineering-economics`, `audit`, `work-order` (5.2); raw source ชุดที่ 7 ในหัวข้อ 1, 2, 9
- หน้าใหม่ 9 หน้า: [[Maintenance Profit Maker Book]] (hub), [[Life Cycle Cost and Life Cycle Profit]], [[Engineering Economics and Time Value of Money]], [[Work Order Lifecycle]], [[Maintenance Outsourcing]], [[Maintenance Financial Impact]], [[Maintenance Performance Audit]], [[Maintenance Master Plan]], [[Maintenance Performance Improvement]]
- อัปเดตหน้าเดิม 26 หน้า: [[Asset Life Cycle]], [[Availability and OEE]], [[Reliability Metrics]], [[Maintenance Time Definitions]], [[Maintenance KPIs]], [[Failure Patterns and Bathtub Curve]], [[Criticality Assessment]], [[CMMS]], [[Maintenance Planning and Scheduling]], [[Maintenance Backlog and Schedule Compliance]], [[Turnaround Management]], [[Spare Parts Management]], [[Spare Part Criticality and Risk]], [[EOQ and Reorder Point]], [[MRO Inventory Control Methods]], [[Inventory Turnover and GPI Benchmarks]], [[MRO Inventory Reduction Program]], [[MRO Purchasing and Contracting]], [[Maintenance Budget]], [[Maintenance Cost Structure]], [[Job Order Costing]], [[Maintenance Business Models]], [[Maintenance Business Case]], [[Maintenance Efficacy Pyramid]], [[FMECA]], [[Root Cause Analysis]] พร้อม `## Triplets`
- **Contested ใหม่ (รอผู้ใช้ตัดสิน):** MPM-C1 holding cost อะไหล่ 20-40% (ตัวอย่างคิดแค่ต้นทุนการเงิน 6-10%) vs RBMM 15-20% ([[Spare Parts Management]], [[EOQ and Reorder Point]], [[Maintenance Cost Structure]], [[Maintenance Budget]], [[Maintenance Financial Impact]]); MPM-C2 % ต้นทุนที่ถูกกำหนดช่วง engineering ไม่คงที่ในเล่ม vs RBMM 85-95% ([[Asset Life Cycle]], [[Life Cycle Cost and Life Cycle Profit]]); MPM-C3 ตัวอักษร failure pattern ระบบ Nowlan & Heap vs RBMM ([[Failure Patterns and Bathtub Curve]]); MPM-C4 นิยาม MTTR/MTBF ไม่รวมเวลารอ vs RBMM ([[Reliability Metrics]], [[Maintenance Time Definitions]], [[Availability and OEE]]); MPM-C5 เป้า utilization > 60% / 40→70% vs RBMM 60% สูงแล้ว ([[Maintenance KPIs]], [[Maintenance Performance Improvement]], [[Maintenance Business Models]]); MPM-C6 profit centre ดีกว่าทุกรูปแบบ vs RBMM cost center พอสำหรับโรงงานเดียว ([[Maintenance Business Models]]); MPM-C7 อายุค่าเสื่อม 10-20 vs 15-20-25 ปี ([[Asset Life Cycle]]); ตารางรวมใน [[Maintenance Profit Maker Book]]
- ไม่ contested (ต่างบริบท/หน่วย): สต็อกอะไหล่ 3-5% ของราคาเครื่องจักรเป็นค่าเฉลี่ย (เป้ายังเป็น SPO ≤ 4% GPI ตามที่ผู้ใช้ตัดสิน 2026-10-27); criticality 20/50/30 vs 30/50/20; ABC ตามปริมาณ vs มูลค่า; turnover เป็น % ของสต็อกสิ้นปี; ชั่วโมงทำงาน 1,663.2 vs 1,760; ความหมาย Blanket Order ตรงกับ SPO
- ข้อผิดพลาดในหนังสือที่ flag (ตรวจคำนวณซ้ำ) เช่น ตัวย่อ RBI "Reliability Based Inspection" และ FMECA "...Cost Analysis", LCC เครื่อง 1 26,578→26,390, Fig 4.16 grand total 46,273.80→44,473.80, MTBF 5,255→5,225, up time 650→630, Fig 12.13 กำไรที่ OEE 100% 1,579→1,864.5, WACC แถวหนี้ 0.33→2.33, ฟังก์ชัน Excel PMT ใช้ผิดกับ 4 factor; รายการเต็มใน [[Maintenance Profit Maker Book]] และท้ายแต่ละไฟล์ notes
- Lint: ไม่มี broken link, frontmatter/tag ครบ, ทุกหน้าอยู่ใน [[index]] (135 หน้า); `graph/triplets.csv` rebuild 6,602 triplets 0 error
- Pages: [[Maintenance Profit Maker Book]], [[raw/maintenance-profit-maker]], [[index]], [[SCHEMA]]

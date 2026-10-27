---
title: "Spare Parts Optimization — การจัดการอะไหล่ให้เพิ่มผลผลิต (ฉบับปรับปรุง)"
type: raw-source
source_url: "file:///.claude/llm-wiki/raw/sparepart_optimizaton.md (OCR full text kept local only, gitignored)"
ingested: 2026-10-27
sha256: 59e43f9c6af4e5c85adf3164de4673829debe3b2a0c375b9c8defc7176606e82
format: OCR Markdown of scanned book (143 PDF pages, LLM OCR "deepseek-flash") → reading notes per chapter (Thai, paraphrased)
immutable: true
---

# Spare Parts Optimization: การจัดการอะไหล่ให้เพิ่มผลผลิต (ฉบับปรับปรุง)

Raw source — ห้ามแก้ไขหลัง ingest (sha256 คิดจากไฟล์ OCR ต้นฉบับ `raw/sparepart_optimizaton.md` ทั้งไฟล์)

- ผู้แต่ง: เรือเอก สุชาติ ศุภมงคล (นายทหารพลาธิการ กองทัพเรือ, อดีตผู้จัดการคลังพัสดุโรงกลั่น ESSO ศรีราชา และงานพัสดุ/จัดซื้อในบริษัทน้ำมัน)
- สำนักพิมพ์: SE-Education (SE-ED), พ.ศ. 2546 (2003), ISBN 974-584-871-6, ชุด Industrial Management & Technical Series (ร่วมกับ Productivity Associates)
- มุมมองของหนังสือ: **ฝั่งคลังพัสดุ/จัดซื้อ (MRO materials management)** ต่างจาก [[raw/reliability-based-maintenance-management]] ที่มองจาก reliability/ความเสี่ยง; ที่มาของแนวคิดคือ COSAL ของกองทัพเรือสหรัฐ และ Esso Spare Parts Optimization
- ไฟล์ OCR ทั้งเล่ม `raw/sparepart_optimizaton.md` (ชื่อไฟล์สะกด "optimizaton" ตามต้นฉบับที่ผู้ใช้วางไว้) เป็นข้อความเต็มของหนังสือมีลิขสิทธิ์ จึง **เก็บในเครื่องเท่านั้น** (`.gitignore`) เพราะ vault sync ไป GitHub
- เนื้อหาใน `spare-parts-optimization/` เป็น **reading notes ที่ถอดความ** ต่อบท ไม่ใช่การคัดลอกต้นฉบับ OCR เป็นของเครื่อง อาจผิด จุดที่อ่านไม่ออกระบุ `[อ่านไม่ออก]` และข้อผิดพลาด (OCR หรือหนังสือ) อยู่ในหัวข้อ "ข้อสังเกต / ข้อผิดพลาดที่พบ" ท้ายแต่ละไฟล์
- อ้างอิงแบบ `(SPO p.NN)` ด้วยเลขหน้าที่พิมพ์ในหนังสือ (book page) ไม่ใช่ PDF page; PDF ขาดหน้าว่างหลังปกบท ทำให้ offset เพิ่มทีละช่วง: บทที่ 1 = PDF+1, บทที่ 2 = +2, บทที่ 3 = +3, บทที่ 4-7 = +4, บทที่ 8-11 = +5, ตั้งแต่ PDF p133 (บทที่ 12) = +6 (ช่วงสุดท้ายเป็นการอนุมาน)

| บท | หัวข้อ | Book pages | PDF pages | Notes file | sha256 (notes) |
|---|---|---|---|---|---|
| - | ส่วนนำ: บรรณานุกรม คำนำ สารบัญ | 1-10 | 1-9 | `spare-parts-optimization/ch01-04.md` | 44976d186878bbff1c7cadccf073794e04631537ce26f77a88b91ab5e6ab37d3 |
| 1 | บทนำ: ประเภทวัสดุ, ประเภทโรงงาน, การบันทึกบัญชีวัสดุ | 11-17 | 10-16 | `spare-parts-optimization/ch01-04.md` | (เดียวกัน) |
| 2 | หน้าที่และความรับผิดชอบของคลังวัสดุ | 19-23 | 17-21 | `spare-parts-optimization/ch01-04.md` | (เดียวกัน) |
| 3 | การจัดจำแนกวัสดุโรงงานเพื่อการบริหารจัดการ (9 กลุ่ม) | 25-31 | 22-28 | `spare-parts-optimization/ch01-04.md` | (เดียวกัน) |
| 4 | การจัดทำแผนสำรองอะไหล่สำหรับงานโครงการ (MR/MS Plan) | 33-38 | 29-34 | `spare-parts-optimization/ch01-04.md` | (เดียวกัน) |
| 5 | หลักปฏิบัติพื้นฐานทางวิศวกรรม (spare % ต่ออุปกรณ์) และนโยบายคลังพัสดุ | 39-58 | 35-54 | `spare-parts-optimization/ch05-06.md` | a9ae7dcd16d8eb5b4f62a37b814c3f5e150804bfd6318b4a7a9b831858f05a12 |
| 6 | คู่มืออะไหล่ที่ใช้ได้กับเครื่องหลายเครื่อง (Parts Interchangeable Book) | 59-62 | 55-58 | `spare-parts-optimization/ch05-06.md` | (เดียวกัน) |
| 7 | การคลังพัสดุโรงงาน (Warehousing) | 63-83 | 59-79 | `spare-parts-optimization/ch07.md` | a593163f0d0a7751fb2eb475bdfcf781d9cb7b186d7300d7e236c58fa4bb9989 |
| 8 | การจัดซื้อพัสดุโรงงาน (Procurement for MRO) | 85-100 | 80-95 | `spare-parts-optimization/ch08.md` | 1a70940eedb84f0b3b81b9385f4f13113ac4225d93e13b73347354b8a71f9548 |
| 9 | การบริหารระดับคงเหลือพัสดุโรงงาน (Inventory Control for MRO) | 101-110 | 96-105 | `spare-parts-optimization/ch09.md` | 887c2723a00b889bfdb400b3358f01e02002def0fe62775843bc179c7965a732 |
| 10 | การจัดการอะไหล่ให้เพิ่มผลผลิต (MRO Optimization: KPI, ABC, ลดสต็อก, MCC) | 111-132 | 106-127 | `spare-parts-optimization/ch10.md` | ea12ff3439bc3ae82bf6d87b8da17cc832bfd3e563b219c25d535b38d9c3e8a4 |
| 11 | คลังเครื่องมือและการควบคุม (Tool Room) | 133-137 | 128-132 | `spare-parts-optimization/ch11-12.md` | f16a8c41693dde0ab307917a234238d11fb0ca45de5f8402fb9b9c52fb058f67 |
| 12 | ความมั่นคงในคลังวัสดุ (Warehouse Security) + บันทึกท้ายเล่ม + บรรณานุกรม | 139-147 | 133-141 | `spare-parts-optimization/ch11-12.md` | (เดียวกัน) |

หน้า hub ใน wiki: [[Spare Parts Optimization Book]]

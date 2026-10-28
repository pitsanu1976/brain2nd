---
title: "Maintenance: The Profit Maker — บำรุงรักษา : งานเพิ่มกำไรบริษัท"
type: raw-source
source_url: "file:///.claude/llm-wiki/raw/maintenance_profit_maker.md (OCR full text kept local only, gitignored)"
ingested: 2026-10-28
sha256: c3a5cc19ab2740d63ecc3a3a13be4f9f0c17a17a1e004a3a5fe99c37337ccb1c
format: OCR Markdown of scanned book (277 pages, vision OCR "deepseek-flash", 150 dpi) → reading notes per chapter group (Thai, paraphrased)
immutable: true
---

# Maintenance: The Profit Maker — บำรุงรักษา : งานเพิ่มกำไรบริษัท

Raw source — ห้ามแก้ไขหลัง ingest (sha256 คิดจากไฟล์ OCR ต้นฉบับ `raw/maintenance_profit_maker.md` ทั้งไฟล์)

- ผู้แต่ง: วัฒนา เชียงกูล, เกรียงไกร ดำรงรัตน์ (2 ใน 3 ผู้แต่งของหนังสือ RBMM, ดู [[Reliability Based Maintenance Management Book]])
- สำนักพิมพ์: ซีเอ็ดยูเคชั่น (SE-ED), พ.ศ. 2556 (2013), ISBN (e-book) 978-616-08-1057-4, เลขหมู่ 658.202, ชุด Industrial Management and Technical Series (ร่วมกับ Productivity Associates)
- มุมมองของหนังสือ: งานบำรุงรักษาเป็น "ผู้สร้างกำไร" ผ่านทั้งรายได้ (OEE, availability) และรายจ่าย (full cost, อะไหล่, งบ) เชื่อมโลกบัญชี-การเงินกับโลกเทคนิค มีกรณีศึกษาโรงงานสมมติ "XYZ" ปี 1998-2000 ใช้ซ้ำหลายบท
- ไฟล์ OCR ทั้งเล่ม `raw/maintenance_profit_maker.md` เป็นข้อความเต็มของหนังสือมีลิขสิทธิ์ จึง **เก็บในเครื่องเท่านั้น** (`.gitignore`) เพราะ vault sync ไป GitHub
- เนื้อหาใน `maintenance-profit-maker/` เป็น **reading notes ที่ถอดความ** ไม่ใช่การคัดลอกต้นฉบับ OCR เป็นของเครื่อง อาจผิด จุดที่อ่านไม่ออกระบุ `[อ่านไม่ออก]` ข้อผิดพลาด (OCR หรือหนังสือ) และการเทียบกับ wiki อยู่ท้ายแต่ละไฟล์ (หัวข้อ "ข้อสังเกต / ข้อผิดพลาดที่พบ" และ "เทียบกับ wiki")
- อ้างอิงแบบ `(MPM p.NN)` ด้วยเลขหน้าที่พิมพ์ในหนังสือ (printed page)
  - offset PDF → printed ไม่คงที่: ส่วนหน้าถึงบทที่ 3 printed = PDF + 1; บทที่ 4 ถึงต้นบทที่ 8 = PDF + 1 ถึง +2; ตั้งแต่บทที่ 8 (หลัง p.141 ที่หายจากสแกน) printed = PDF + 3
  - marker `printed:` ใน OCR ผิดบางช่วง (PDF p69-73 ติด 69-73 แต่จริงคือ p.70-74; PDF p81-82 ติด 82-83 แต่จริงคือ p.83-84; PDF p189-192 ติด 182-185 แต่จริงคือ p.192-195) notes ใช้เลขที่แก้แล้ว

| บท | หัวข้อ | Book pages | Notes file | sha256 (notes) |
|---|---|---|---|---|
| - | ส่วนนำ: บรรณานุกรม คำนำ สารบัญ | 3-12 | `maintenance-profit-maker/ch01-03.md` | af7af482b69304999851256ae148cb30b4226776bbeb04077a2c1bb5f3487960 |
| 1 | ทรัพย์สินและกิจกรรมงานบำรุงรักษา (16 กิจกรรม, failure pattern, audit, road map) | 13-36 | `maintenance-profit-maker/ch01-03.md` | (เดียวกัน) |
| 2 | ค่าใช้จ่ายกับรายได้ตลอดอายุของทรัพย์สิน (LCC / LCP) | 37-46 | `maintenance-profit-maker/ch01-03.md` | (เดียวกัน) |
| 3 | OEE : ประสิทธิผลโดยรวมของเครื่องจักร | 47-58 | `maintenance-profit-maker/ch01-03.md` | (เดียวกัน) |
| 4 | ระบบบริหารงานบำรุงรักษา (work order lifecycle) | 59-81 | `maintenance-profit-maker/ch04-05.md` | ebdbe7e60bd050c2a85efabdcc5679503459959ddaddb0586432666fc72e2737 |
| 5 | การจัดการวัสดุอะไหล่ | 83-90 | `maintenance-profit-maker/ch04-05.md` | (เดียวกัน) |
| 6 | การจ้างเหมางานบำรุงรักษา | 91-110 | `maintenance-profit-maker/ch06-07.md` | b13b8f7a6183e1a70466e1c848fa369a520a1d2c527082f3580381504a262f14 |
| 7 | การบริหารงบประมาณงานบำรุงรักษา | 111-139 | `maintenance-profit-maker/ch06-07.md` | (เดียวกัน) |
| 8 | ดัชนีสมรรถนะงานบำรุงรักษา | 140-156 | `maintenance-profit-maker/ch08-09.md` | 0b6395f0e04759332bf7ef224710251a6a27cdba1a06d94de3769915b18de844 |
| 9 | แผนแม่บทและกลยุทธ์การบริหารงานบำรุงรักษา | 157-166 | `maintenance-profit-maker/ch08-09.md` | (เดียวกัน) |
| 10 | ผลกระทบของบำรุงรักษาต่อประสิทธิผลของบริษัท | 167-190 | `maintenance-profit-maker/ch10-11.md` | 46e3b902a2dcf81c86b6523c25eb6e12e664258aec573cd3295d91cee96284fd |
| 11 | การตรวจสอบ ทบทวน สมรรถนะงานบำรุงรักษา (audit) | 191-204 | `maintenance-profit-maker/ch10-11.md` | (เดียวกัน) |
| 12 | การปรับปรุงสมรรถนะบำรุงรักษา (+ กรณีศึกษา XYZ และบริษัทบำรุงรักษากลาง) | 205-242 | `maintenance-profit-maker/ch12.md` | 47ba68c275d2a4487f1308d7c07dfd843d688684476ba174511af60e285e6178 |
| 13 | การบริหารการใช้และบำรุงรักษาทรัพย์สิน (physical asset management) | 243-252 | `maintenance-profit-maker/ch13-15.md` | 061fa74d07cc550fb4c97ea0e69f8fa333f733edbb29320e206f5c4fcb8065a9 |
| 14 | บัญชีสำหรับผู้บริหารงานบำรุงรักษา | 253-264 | `maintenance-profit-maker/ch13-15.md` | (เดียวกัน) |
| 15 | เศรษฐศาสตร์วิศวกรรม (+ บรรณานุกรม ประวัติผู้เขียน) | 265-280 | `maintenance-profit-maker/ch13-15.md` | (เดียวกัน) |

หน้า hub ใน wiki: [[Maintenance Profit Maker Book]]

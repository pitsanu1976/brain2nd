> Archived log: ประวัติ action ของ Maintenance Reliability wiki (ต้นทาง `coce\wiki`) ช่วง 2026-10-20 ถึง 2026-10-21 ก่อนรวมเข้า vault นี้ เก็บไว้ตามเดิม (ห้ามแก้) entry ใหม่ต่อจากนี้อยู่ใน [[log]]

# Log

บันทึก action แบบ **append-only** (ห้ามแก้ entry เก่า) รูปแบบ: `## [วันที่] action | รายละเอียด` ตามด้วย pages affected ดู [[SCHEMA]] และ [[index]]

## [2026-10-20] init | สร้างโครงสร้าง wiki 3 ชั้น
- สร้าง `SCHEMA.md`, `index.md`, `log.md`, `README.md` และโฟลเดอร์ `entities/`, `concepts/`, `comparisons/`, `queries/`, `_archive/`
- Pages: [[SCHEMA]], [[index]], [[log]], [[README]]

## [2026-10-20] ingest | raw source 1: Compressor Failure Hierarchy.xlsx
- ไฟล์: `raw/compressor-failure-hierarchy.md` + `raw/datasets/compressor-failure-hierarchy__*.csv` (10 sheet) sha256 `0aabcf9e...5613` (immutable, อ่านอย่างเดียว)
- อ่าน: Notes, code sheets (subunit, resolution, failure cause, maintainable item), Summary by Failure Mode, Resolution Matrix, Sheet5, ตัวอย่าง Failure Hierarchy (7,885 บรรทัด)
- Pages affected: [[Failure Hierarchy]], [[Failure Mode]], [[Failure Mechanism]], [[Failure Cause Codes]], [[Resolution Codes]], [[Maintainable Item]], [[CAUSE_CODE Convention]]

## [2026-10-20] ingest | raw source 2: failure structure.xlsx
- ไฟล์: `raw/failure-structure.md` + `raw/datasets/failure-structure__sheet1.csv`, `__sheet2.csv` sha256 `54975d27...4433a0550` (immutable)
- อ่าน: Sheet1 (3,055 บรรทัด: centrifugal 1,810, reciprocating 732, screw 512 + header), Sheet2 (24 mechanism categories) และภาพ OREDA ใน `raw/assets/`
- Pages affected: [[Compressor Type Failure Profiles]], [[Centrifugal Compressor]], [[Reciprocating Compressor]], [[Screw Compressor]]

## [2026-10-20] create | entities: Compressor และประเภท compressor
- Pages: [[Compressor]], [[Centrifugal Compressor]], [[Reciprocating Compressor]], [[Screw Compressor]]

## [2026-10-20] create | entities: Sub Unit 6 หน้า
- Pages: [[PWTR Power Transmission]], [[CPUN Compressor Unit]], [[CTMN Control and Monitoring]], [[LUBS Lubrication System]], [[SHSS Shaft Seal System]], [[MISC Miscellaneous]]
- ตัวเลข "% นับที่ sub unit" เป็น derived: ผลรวมแถว `Count in Total = 1`; รวม 6 sub unit = 85.66 (PWTR 25.64, CPUN 32.30, CTMN 7.06, LUBS 15.55, SHSS 2.60, MISC 2.51) ตรงกับ summary

## [2026-10-20] create | concepts: hierarchy, failure mode hub และรหัส
- Pages: [[Failure Hierarchy]], [[Failure Mode]], [[Failure Mechanism]], [[Failure Cause Codes]], [[Resolution Codes]], [[Maintainable Item]], [[CAUSE_CODE Convention]]

## [2026-10-20] create | concepts: หน้ารายโหมด 9 หน้า
- Pages: [[AIR Abnormal Instrument Reading]], [[SER Minor In-Service Problems]], [[LOO Low Output]], [[ELU External Leakage Utility Medium]], [[PDE Parameter Deviation]], [[OTH Other]], [[ELP External Leakage Process Medium]], [[OHE Overheating]], [[UST Spurious Stop]]

## [2026-10-20] create | concepts: OREDA และ ISO 14224
- Pages: [[OREDA]], [[ISO 14224]]
- หมายเหตุ: [[ISO 14224]] ไม่มีใน sources เลย ตั้ง `confidence: low`, `sources: []` และระบุ to-do ให้ ingest มาตรฐาน

## [2026-10-20] create | comparisons
- Pages: [[Compressor Type Failure Profiles]], [[Resolution Matrix by Mechanism]]

## [2026-10-20] create | queries
- Pages: [[queries/README]], [[Which failure modes dominate compressor failure rate]], [[Which maintainable item and mode pairs drive failure rate]]
- `_archive/README.md` สร้างเป็นไฟล์ README บรรทัดเดียว

## [2026-10-20] contested | Sub Unit assignment ขัดกันระหว่างสอง sources
- compressor-failure-hierarchy: Instruments กระจาย 5 sub unit, Valves 5 sub unit, Internal piping/Check valves = Compressor unit, Piping = CPUN/LUBS/MISC
- failure-structure Sheet1: Instrument types = Control and Monitoring เท่านั้น, Valves/Internal piping/Check valves/Piping = Miscellaneous
- การตัดสินใจ: เก็บทั้งสองมุมมอง ไม่เขียนทับ ตั้ง `contested: true`
- Pages: [[Failure Hierarchy]], [[Maintainable Item]], [[PWTR Power Transmission]], [[CPUN Compressor Unit]], [[CTMN Control and Monitoring]], [[LUBS Lubrication System]], [[SHSS Shaft Seal System]], [[MISC Miscellaneous]]

## [2026-10-20] contested | Resolution codes 14 vs 13
- sheet resolution code มี 14 รหัส (รวม CHG Change) แต่ OREDA list (Notes, ภาพ), Resolution Matrix และข้อมูลจริง (0 แถว) ใช้ 13
- การตัดสินใจ: เก็บทั้งสองมุมมอง ถือว่าใช้จริง 13 รหัส
- Pages: [[Resolution Codes]], [[Resolution Matrix by Mechanism]]

## [2026-10-20] contested | Mechanism codes 35 vs 37 mechanism
- code sheet ขาด Combined causes และ Mechanical Failure - general ซึ่งอยู่ใน OREDA list/Resolution Matrix แต่ไม่ถูกใช้ใน Failure Hierarchy (0 แถว) ขณะที่ภาพ OREDA ต่อประเภทใช้ descriptor นี้ (เช่น reciprocating LOO 18.62)
- Pages: [[Failure Cause Codes]], [[Failure Mechanism]], [[Reciprocating Compressor]]

## [2026-10-20] data-quality | ข้อสังเกตอื่นที่บันทึกโดยไม่ resolve
- รหัส `CTMN` และ `MISC` ชนกันระหว่าง sub unit และ mechanism: [[CAUSE_CODE Convention]]
- Sheet5 มีบรรทัด `#N/A,--` ท้ายไฟล์: [[Failure Cause Codes]]
- คอลัมน์ "No. of Maintainable Items" (รวม 258) จริงคือจำนวนคู่ mode/item: [[Failure Mode]], [[Maintainable Item]]
- Total 85.66 + placeholder 13.96 = 99.62 ไม่ถึง 100 (ส่วนต่าง 0.38 ไม่มีคำอธิบาย): [[Failure Mode]]
- failure-structure Sheet1 มี 215 แถวที่ descriptor ว่าง และ Sheet2 จัด Burst เป็น electrical/constrol: [[Failure Mechanism]], [[Centrifugal Compressor]]
- Instruments นับ % ที่ PWTR ทั้งก้อน (23.34 จาก 25.64): [[PWTR Power Transmission]]

## [2026-10-20] lint | ตรวจ wikilinks, frontmatter และ index
- ตรวจว่าทุก wikilink ชี้ไปหน้าที่มีจริง, ทุกหน้า wiki 33 หน้ามี frontmatter ครบ 8 field และอยู่ใน [[index]]
- ไม่มีการแก้ไข/ลบไฟล์ใต้ `raw/`
- Pages: [[index]], [[SCHEMA]]

## [2026-10-21] ingest | raw source 3: Reliability Based Maintenance Management (หนังสือ, SE-ED 2553)
- ไฟล์: `raw/reliability-based-maintenance-management.md` + notes ต่อบท 10 ไฟล์ใน `raw/reliability-based-maintenance-management/` sha256 (ของ PDF ต้นฉบับ) `cbda58a3...b4f49f` (immutable)
- วิธี: PDF สแกน 401 หน้า (ไม่มี text layer) -> แปลงเป็นภาพหน้า -> อ่านและสรุปความเป็น reading notes 10 passes แบบขนาน -> เขียนหน้า wiki 6 writers แบบขนาน -> integration (hub, SCHEMA, index, log, lint)
- Pages created (33): hub [[Reliability Based Maintenance Management Book]]; concepts 30 หน้า: [[Asset Life Cycle]], [[Maintenance Efficacy Pyramid]], [[Maintenance KPIs]], [[Availability and OEE]], [[Maintenance Strategic Report]], [[CMMS]], [[Failure Data Recording]], [[RCM Reliability Centered Maintenance]], [[FMECA]], [[Criticality Assessment]], [[Weibull Analysis]], [[Failure Patterns and Bathtub Curve]], [[Reliability Metrics]], [[Censored Data]], [[Reliability Block Diagram]], [[Statistical Distributions for Maintenance]], [[PM Task Selection]], [[P-F Interval and Condition Monitoring]], [[Failure Finding Interval]], [[Redundancy and Standby Systems]], [[PM Interval Optimization]], [[Monte Carlo Maintenance Simulation]], [[Spare Parts Management]], [[Spare Part Criticality and Risk]], [[EOQ and Reorder Point]], [[Spare Part Demand Forecasting]], [[Maintenance Budget]], [[Maintenance Cost Structure]], [[Maintenance Business Models]], [[Job Order Costing]]; comparison [[RBMM Concepts vs Compressor Failure Hierarchy]]; query [[How to choose PM task for a compressor failure mode]]
- Pages updated: [[ISO 14224]], [[Failure Mode]], [[UST Spurious Stop]], [[Failure Mechanism]], [[Failure Hierarchy]], [[Maintainable Item]], [[OREDA]], [[Compressor]], [[Resolution Codes]] (เพิ่มหัวข้อ "ดูเพิ่ม (RBMM)" หรือส่วนใหม่ และ bump `updated`); [[Failure Patterns and Bathtub Curve]] (ปรับข้อความ AIR/SER เป็น hypothesis, confidence low และลดข้อความเรื่อง OREDA failure rate คงที่); [[P-F Interval and Condition Monitoring]] (ติดป้ายฟิลด์ detection method เป็นความรู้ทั่วไป ไม่มีใน sources); [[PM Task Selection]] (ลดข้อความที่อ้างว่า OREDA ให้ failure rate คงที่); [[SCHEMA]] (ขยาย Domain, tag ใหม่ 14 ตัว, entities/concepts, raw source ข้อ 9), [[index]], README
- ผลสำคัญต่อ wiki เดิม: รายการรหัส failure mode ใน RBMM p.132-134 ตรงกับ [[Failure Mode]] 18 จาก 19 รหัส (ยกระดับความมั่นใจเฉพาะส่วนรายการรหัสเป็น medium; หน้า [[ISO 14224]] ระดับรวมยังเป็น low)

## [2026-10-21] contested | รหัส Spurious stop: SPS (RBMM) vs UST (dataset OREDA)
- RBMM Fig 5.15/5.17 (p.133-134, ตัวอย่าง ISO 14224 ของ pump/motor) ใช้รหัส SPS "Spurious stop" ขณะที่ dataset ใน wiki (OREDA) ใช้ UST ชื่อเดียวกัน; อีก 18 รหัสของ pump ตรงกันทุกตัว; motor มี OWD (Operation without demand) ที่ wiki ไม่มี
- การตัดสินใจ: เก็บทั้งสองมุมมอง ไม่แก้ [[Failure Mode]] ใช้ UST ต่อสำหรับข้อมูล compressor ถือ SPS เป็น alias ที่ยังไม่ verify (ไม่มีตัวมาตรฐาน ISO 14224 ใน sources) ตั้ง `contested: true`
- Pages: [[Failure Data Recording]], [[ISO 14224]], [[UST Spurious Stop]], [[Failure Mode]], [[RBMM Concepts vs Compressor Failure Hierarchy]]

## [2026-10-21] data-quality | ข้อผิดพลาดและความไม่สอดคล้องภายในหนังสือ RBMM
- ข้อผิดพลาดที่พบ (ไม่ใช่ความขัดแย้งกับ OREDA; ค่าที่ถูกเป็น derived): T(R) p.169 สูตร eta x [1 - ln R]^(1/beta) ให้ 13,847.81 ชม. ที่ R = 0.8 ขณะที่สูตรที่ถูก eta x (-ln R)^(1/beta) ให้ประมาณ 8,837 ชม.; Parallel RBD Fig 6.22 พิมพ์ 0.9085 ควรเป็น 0.985; Series RBD Fig 6.21 ข้อความ 0.9/0.9 แต่คำนวณ 0.85 x 0.9 = 0.765; MTTF integral p.168 ขอบเขต -inf ถึง inf ควรเป็น 0 ถึง inf; cost ต่อหน่วยเวลา p.391 ตัวส่วน integral tp..inf ควรเป็น 0..tp; sigma p.374 สลับกฎ N กับ N-1 (ตัวอย่างใช้ N-1 ได้ 101.486); EOQ p.253 พจน์ Q/2 x Cp ควรเป็น A/Q x Cp; Job Order Costing p.357 (3,300) ควรเป็น (33,000)
- ความไม่สอดคล้องภายในหนังสือ: E15/E16 ใน ch3 Fig 3.19 กับ ch10 Fig 10.27 (ใช้ ch10 ที่ตรงกับข้อความ 2.97% + 3.45%); A3.1 Actual 320,000 (p.64) vs 520,000 (p.66, ch10) ใช้ 520,000; คาบ PM optimum ข้อความ ประมาณ 10 เดือน vs ตาราง Fig 8.6 ต่ำสุดเดือน 9; ABC Analysis p.242 vs ป้ายใน Fig 9.4; Pattern/beta (Fig 6.14, ch5 p.148 "Infant Mortality แบบ D", 6 pattern vs 5 ใน ch12); นิยาม left-censored ต่างกัน ch6 vs ch12; >85% planned (ch2 p.54) vs 80-85% (ch3 p.60); สัดส่วนอะไหล่ >half (ch9) vs >60-70% (ch2); holding cost 15-20% vs 15-25%; Fig 9.19, 9.20, 10.20 vs 10.18 ไม่สอดคล้อง/ภาพเบลอ
- ข้อสังเกต: ตัวเลขที่อ่านจากภาพเบลอและค่า derived ถูกติดป้ายในแต่ละหน้า; ไม่มี β/P-F เฉพาะ compressor และไม่มี IEC 61508/SIL ในหนังสือ
- Pages: [[Reliability Based Maintenance Management Book]], [[Reliability Metrics]], [[Reliability Block Diagram]], [[PM Interval Optimization]], [[EOQ and Reorder Point]], [[Job Order Costing]], [[Maintenance Strategic Report]], [[Failure Patterns and Bathtub Curve]], [[Spare Part Criticality and Risk]]

## [2026-10-21] lint | ตรวจ wikilinks, frontmatter, index หลัง ingest RBMM
- ตรวจ wikilink แบบ simple 1,190 รายการ (รวม index/log ก่อน entry นี้) + path-style 10 รายการ (`raw/...`, `queries/README`, `_archive/README`): broken 0, ไม่มี alias `|`, ไม่มี Markdown link ภายใน
- หน้า wiki 66 หน้า (entities 11, concepts 48, comparisons 3, queries 4) มี frontmatter ครบ 8 field ทุกหน้า และอยู่ใน [[index]] ครบ; tag ทุกตัวอยู่ใน [[SCHEMA]] ข้อ 5.2; ไม่มีการแก้ไขไฟล์ใต้ `raw/`
- หน้า `contested: true` ใหม่/ที่เปลี่ยน (Failure Data Recording, ISO 14224, UST Spurious Stop, RBMM comparison) มีรายการใน log ข้างบน
- Pages: [[index]], [[SCHEMA]]

## [2026-10-21] resolve | รหัส Spurious stop: ใช้ UST หลัก, SPS เป็น alias
- การตัดสินใจ (โดยผู้ใช้): ใช้ **UST** เป็นรหัสหลักของ "Spurious stop" ทั้ง wiki และถือ **SPS** (รหัสในตัวอย่าง ISO 14224 ของ RBMM Fig 5.15/5.17) เป็น alias เมื่อพบ SPS ในเอกสาร/CMMS ให้ map เป็น UST
- ปิดประเด็นจาก entry "[2026-10-21] contested | รหัส Spurious stop: SPS (RBMM) vs UST (dataset OREDA)" โดยคงข้อความประวัติไว้ในหน้า ตั้ง `contested: false`
- Pages: [[UST Spurious Stop]], [[ISO 14224]], [[Failure Data Recording]], [[RBMM Concepts vs Compressor Failure Hierarchy]], [[Failure Mode]], [[Reliability Based Maintenance Management Book]]

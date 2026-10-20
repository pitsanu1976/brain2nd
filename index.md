# Index — Obsidian Second Brain + LLM Wiki และ Maintenance Reliability

แค็ตตาล็อกของทุกหน้า อัปเดตทุกครั้งที่เพิ่ม/ย้ายหน้า (กติกาใน [[SCHEMA]], ประวัติใน [[log]])

อัปเดตล่าสุด: 2026-10-21 | จำนวนหน้า wiki: 86 (entities 11, concepts 56, comparisons 3, guides 6, reference 6, queries 4; ไม่นับ `queries/README.md`)

Area ก = Obsidian Second Brain + LLM Wiki method | Area ข = Maintenance Reliability (compressor failure hierarchy และ RBMM)

## Raw sources (Layer 1, immutable; area ข)

- [[raw/compressor-failure-hierarchy]] — Compressor Failure Hierarchy.xlsx ส่งออกเป็น 10 sheet CSV (Failure Hierarchy 7,885 บรรทัด ฯลฯ)
- [[raw/failure-structure]] — failure structure.xlsx (Sheet1 โครงสร้าง mode/item/sub unit/descriptor ต่อประเภท, Sheet2 category ของ mechanism)
- `raw/assets/` — ภาพตาราง OREDA (failure descriptor, failure mode vs maintainable item, failure mechanism, resolution)
- [[raw/reliability-based-maintenance-management]] — หนังสือ Reliability Based Maintenance Management (SE-ED 2553, 400 หน้า) reading notes 12 บทใน `raw/reliability-based-maintenance-management/`
- Area ก ไม่มี raw source (เขียนจากความรู้ทั่วไป)

## entities/ (area ข)

- [[Compressor]] — ภาพรวม compressor (generic), ขนาด dataset และลิงก์ไปทุกประเภท/sub unit
- [[Centrifugal Compressor]] — โปรไฟล์ failure ของ centrifugal: AIR 27.52, ELU 17.54, item เด่น Valves/Instruments/Antisurge
- [[Reciprocating Compressor]] — โปรไฟล์ reciprocating: SER 21.97, LOO 21.60, Cylinder liner 28.77 และ Filter(s) 14.80
- [[Screw Compressor]] — โปรไฟล์ screw: AIR 22.68, ELU 13.75, PDE 13.40, Valves 18.04
- [[PWTR Power Transmission]] — Sub Unit PWTR 7 item, 50 CAUSE_CODE, ข้อควรระวังเรื่อง Instruments
- [[CPUN Compressor Unit]] — Sub Unit CPUN 15 item, 112 CAUSE_CODE, Cylinder liner/Valves เด่น
- [[CTMN Control and Monitoring]] — Sub Unit CTMN 8 item, 80 CAUSE_CODE, AIR/UST จาก control unit
- [[LUBS Lubrication System]] — Sub Unit LUBS 11 item, 97 CAUSE_CODE, Filter(s) x SER 7.33
- [[SHSS Shaft Seal System]] — Sub Unit SHSS 10 item, 78 CAUSE_CODE, สัดส่วนต่ำ (2.60)
- [[MISC Miscellaneous]] — Sub Unit MISC 7 item, 56 CAUSE_CODE, Base frame/piping/corrosion
- [[Reliability Based Maintenance Management Book]] — hub หนังสือ RBMM: ข้อมูลบรรณานุกรม ตาราง 12 บท กรอบ CMMS ถึงธุรกิจบำรุงรักษา ข้อผิดพลาดในหนังสือ และความสัมพันธ์กับ compressor hierarchy

## concepts/

### Area ก: Second Brain + LLM Wiki method

- [[Second Brain]] — CODE: Capture, Organize, Distill, Express
- [[PARA Method]] — Projects, Areas, Resources, Archive และกฎย้ายหมวด
- [[Zettelkasten and Atomic Notes]] — โน้ตอะตอมและโครงข่ายลิงก์
- [[Maps of Content]] — MOC เป็นสารบัญ ใช้ใน vault อย่างไร
- [[LLM Wiki Pattern]] — 3 ชั้น, index/log, ingest/query/lint
- [[Second Brain vs LLM Wiki]] — เปรียบเทียบและการรวมใน vault เดียว
- [[Contradiction Handling]] — contested flag และขั้นตอน
- [[Page Thresholds]] — เกณฑ์สร้างหน้าใหม่

### Area ข: Compressor failure hierarchy (OREDA / ISO 14224)

- [[Failure Hierarchy]] — ลำดับชั้น 7 ระดับ Equipment ถึง Resolution และความขัดแย้งเรื่อง sub unit ระหว่าง sources
- [[Failure Mode]] — hub ตาราง 19 โหมด พร้อม % failure rate (total 85.66)
- [[AIR Abnormal Instrument Reading]] — AIR 17.18%, Instruments x AIR 13.54
- [[SER Minor In-Service Problems]] — SER 13.05%, Filter(s) x SER 7.33
- [[LOO Low Output]] — LOO 10.11%, Cylinder liner x LOO 5.78
- [[ELU External Leakage Utility Medium]] — ELU 8.62%, 33 คู่ item แบบ long tail
- [[PDE Parameter Deviation]] — PDE 8.13%, Instruments x PDE 3.35
- [[OTH Other]] — OTH 5.46%, mechanism = Other ทุกแถว
- [[ELP External Leakage Process Medium]] — ELP 4.58%, Cylinder liner/Valves เด่น
- [[OHE Overheating]] — OHE 4.18%, Cylinder liner x OHE 3.40
- [[UST Spurious Stop]] — UST 4.16%, Instruments/Control unit เด่น
- [[Failure Mechanism]] — 37 mechanism พร้อมรหัส, category และจำนวน resolution
- [[Failure Cause Codes]] — รหัส mechanism 35 ตัวและ CAUSE_CODE 473 รหัส พร้อมข้อขัดแย้ง
- [[Resolution Codes]] — 14 รหัส resolution พร้อมจำนวนแถวใช้งานและข้อขัดแย้ง CHG
- [[Maintainable Item]] — 44 รหัส item และกติกาจับคู่หลาย sub unit
- [[OREDA]] — แหล่งข้อมูลต้นทางและข้อจำกัด (ไม่มี absolute rate)
- [[ISO 14224]] — มาตรฐาน taxonomy (ไม่มีใน sources, confidence ต่ำ)
- [[CAUSE_CODE Convention]] — รูปแบบ SubUnit-Item-Mechanism และ code collision

### Area ข: Reliability Based Maintenance Management (RBMM)

หน้าสังเคราะห์จากหนังสือ [[Reliability Based Maintenance Management Book]] (ingest 2026-10-21)

- [[Asset Life Cycle]] — วงจรชีวิตทรัพย์สิน, 4 กลุ่มงาน, criticality A/B/C, Zero Plant Breakdown @ Minimum Cost
- [[Maintenance Efficacy Pyramid]] — พีระมิด 6 ชั้นและการประเมิน 16 หัวข้อ จาก Reactive ถึง Optimization
- [[Maintenance KPIs]] — ต้นไม้ดัชนี 19 กิจกรรม และดัชนี B/C/D พร้อมสูตร variance
- [[Availability and OEE]] — MTTF/MTTR/MWT/MDT ถึง Availability และ OEE กับการใช้ในรายงาน
- [[Maintenance Strategic Report]] — รายงาน A4 ส่วน A-E พร้อมตัวเลขตัวอย่างและการตรวจเลข
- [[CMMS]] — ระบบบริหารงานบำรุงรักษา: 10 โมดูล, Asset Register หยุดที่ Equipment + Object Part, Process vs Content, ห้ามปิด WO ถ้ายังไม่ระบุ Failure Mode
- [[Failure Data Recording]] — ฟิลด์ใน Work Order, record ขั้นต่ำ 5 รายการ และตารางเทียบรหัส Failure Mode ISO 14224 (pump/motor) กับ wiki (UST หลัก, SPS = alias)
- [[RCM Reliability Centered Maintenance]] — RCM ตาม Nowlan-Heap: 7 กระบวนการ, task selection ตาม consequence, 7 คำถาม, Classical vs Fast Track
- [[FMECA]] — RPN (S x O x D) และ criticality เชิงปริมาณ FF/FFCr/Cr(t) พร้อมตัวอย่างคำนวณ
- [[Criticality Assessment]] — Consequence x Likelihood = 1-30 แบ่ง A/B/C ใน 3 ด้าน (Commercial, Safety, Environment) และกลยุทธ์ PM/อะไหล่/งบตามระดับ
- [[Weibull Analysis]] — พารามิเตอร์ β/η/γ, วิธีประมาณ (probability plot, Y/X regression), ตัวอย่าง TTF 8,500-16,000 ชม. และกระทบยอด β 3.5/3.79/3.94
- [[Failure Patterns and Bathtub Curve]] — pattern A-E, bathtub curve และกฎเลือกงาน PM ตามค่า β
- [[Reliability Metrics]] — F(t), R(t), λ(t), MTTF/MTBF, conditional reliability, availability, MTTR พร้อมสูตรที่หนังสือพิมพ์ผิด
- [[Censored Data]] — ข้อมูล complete/right/left/interval censored และวิธี MON ปรับ rank ก่อน fit Weibull
- [[Reliability Block Diagram]] — RBD แบบ series/parallel/mixed, failure tree และตัวเลขที่หนังสือคำนวณผิด
- [[Statistical Distributions for Maintenance]] — Poisson, Normal, Exponential, Weibull กับตัวอย่างอะไหล่และ PM
- [[PM Task Selection]] — เลือกประเภทงาน PM ต่อ failure mode: ผัง Nowlan & Heap, SAE JA1012, ลำดับคำถามแบบง่าย และการเลือกตาม Weibull beta
- [[P-F Interval and Condition Monitoring]] — Condition Monitoring, P-F interval และหลักคาบตรวจ = (P-F)/2 พร้อมตัวอย่าง simulator
- [[Failure Finding Interval]] — คาบตรวจ Hidden Failure ของ protective device: FFI = 2 x U x MTBF และตาราง Availability ต่อ FFI
- [[Redundancy and Standby Systems]] — k out of n, standby, load sharing, Multiple Failure และข้อควรทำของ PM กับ criticality
- [[PM Interval Optimization]] — หาคาบ PM ที่ cost ต่อหน่วยเวลาต่ำสุด: สูตร Cp/Cf, Monte Carlo (ประมาณ 10 เดือน) และตัวอย่าง bearing 480 วัน
- [[Monte Carlo Maintenance Simulation]] — ทำไมต้องจำลอง, input/output ของโมเดล และผลตัวอย่างกรณี 3 ปี (3.6 / 2.6 / 4.5 / 2.5 ล้านบาท)
- [[Spare Parts Management]] — hub การบริหารอะไหล่: Commissioning vs Maintenance spare, Stock vs ซื้อตรง, Demand/Supply Side, KPI B7-B10, Spare Part Database ใน CMMS, holding cost 15-20%
- [[Spare Part Criticality and Risk]] — ABC Analysis, Part/Equipment Criticality, Confidence Level และ Cost Ratio พร้อมโซน Mandatory/Approval/No Stock/Insurance Part
- [[EOQ and Reorder Point]] — สูตร EOQ, ROP, Safety Stock = z x sigma_combined, ตาราง Z และตัวอย่างคำนวณ SS ประมาณ 2, ROP ประมาณ 5
- [[Spare Part Demand Forecasting]] — คาดการณ์ demand อะไหล่ด้วย MTBF average, Poisson (D=3, D=5.333) และ Monte Carlo
- [[Maintenance Budget]] — กรอบตั้งงบบำรุงรักษา Top Down/Bottom Up: Gross -> สำรอง (Losses/Costs) -> Net Budget, Cost Control vs Loss Control, งบตาม Criticality A/B/C
- [[Maintenance Cost Structure]] — Full Fixed Cost 5 กลุ่ม, Materials (Stock/Direct Purchase/Outsource), Full Fixed Cost Rate, Over/(Under) Absorption และ Variance
- [[Maintenance Business Models]] — เปรียบเทียบ Cost Center / Profit Centered / Service Company, Service Gap, 16 กิจกรรมบำรุงรักษา และปัญหาการแปลงเป็นธุรกิจ
- [[Job Order Costing]] — บัญชีต้นทุนตามใบสั่งงานสำหรับธุรกิจบริการ: Job Budget, Reference Cost, WIP/Provision, Absorption, ตัวอย่าง 4 เดือน

## comparisons/ (area ข)

- [[Compressor Type Failure Profiles]] — เปรียบเทียบ % 19 โหมดของ centrifugal vs reciprocating vs screw
- [[Resolution Matrix by Mechanism]] — 37 mechanism x 13 resolution (233 คู่ที่เป็นไปได้)
- [[RBMM Concepts vs Compressor Failure Hierarchy]] — ตารางเทียบแนวคิดหนังสือ (Object Part, Damage Code, criticality, task, Weibull, spares) กับ 7 ระดับของ hierarchy พร้อมที่มา

## guides/ (area ก)

- [[Vault Setup for Fleet Engineering]] — โครงโฟลเดอร์ 00-99
- [[Obsidian Core Settings]] — new note, daily note, templates, attachments, links
- [[Daily Workflow]] — capture, triage, daily note, project
- [[Using Claude Code on a Vault]] — ingest, query, lint
- [[Converting Excel and PDF to Raw]] — CSV export และ sha256
- [[Maintenance Reliability Example]] — worked example: wiki compressor/RBMM ใน vault นี้ และ mapping เป็น LLM Wiki pattern

## reference/ (area ก)

- [[Frontmatter Spec]] — field ของ wiki page และ raw source
- [[Wikilinks vs Markdown Links]] — กติกาลิงก์
- [[Tags vs Links vs Folders]] — เลือกกลไกจัดระเบียบ
- [[Templates Reference]] — ข้อความเต็ม 5 template
- [[Naming Conventions]] — ชื่อไฟล์/โฟลเดอร์/tag
- [[Obsidian Core Plugins]] — core plugin ที่ควรรู้

## queries/

- [[queries/README]] — กติกาของโฟลเดอร์ (ไม่นับเป็นหน้า content)
- [[FAQ Obsidian Second Brain and LLM Wiki]] — คำถามที่พบบ่อย (area ก)
- [[Which failure modes dominate compressor failure rate]] — 5 โหมดแรกรวม 57.09%, 9 โหมดแรก 75.47% (area ข)
- [[Which maintainable item and mode pairs drive failure rate]] — Instruments x AIR 13.54 ใหญ่สุด; 4 item รวม 57.59 (area ข)
- [[How to choose PM task for a compressor failure mode]] — ขั้นตอน 7 ข้อ: criticality, consequence/hidden, beta/pattern, ประเภทงาน, คาบ, อะไหล่ (ไม่มี beta/P-F ของ compressor ใน sources) (area ข)

## _archive/

- [[_archive/README]] — กติกาโฟลเดอร์
- [[_archive/log-maintenance-reliability-2026-10-20]] — log ประวัติของ Maintenance Reliability wiki ก่อนรวม vault (ไม่นับเป็นหน้า content)

## ไฟล์ rules

- [[SCHEMA]] — กติกา wiki
- [[log]] — บันทึก action แบบ append-only
- [[README]] — ตัวชี้เริ่มต้น

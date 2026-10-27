# Index — Obsidian Second Brain + LLM Wiki และ Maintenance Reliability

แค็ตตาล็อกของทุกหน้า อัปเดตทุกครั้งที่เพิ่ม/ย้ายหน้า (กติกาใน [[SCHEMA]], ประวัติใน [[log]])

อัปเดตล่าสุด: 2026-10-27 | จำนวนหน้า wiki: 126 (entities 13, concepts 89, comparisons 6, guides 6, reference 6, queries 6; ไม่นับ `queries/README.md`)

Area ก = Obsidian Second Brain + LLM Wiki method | Area ข = Maintenance Reliability (compressor failure hierarchy, RBMM, ISO 14224, CMRP และ SPO)

## Raw sources (Layer 1, immutable; area ข)

- [[raw/compressor-failure-hierarchy]] — Compressor Failure Hierarchy.xlsx ส่งออกเป็น 10 sheet CSV (Failure Hierarchy 7,885 บรรทัด ฯลฯ)
- [[raw/failure-structure]] — failure structure.xlsx (Sheet1 โครงสร้าง mode/item/sub unit/descriptor ต่อประเภท, Sheet2 category ของ mechanism)
- `raw/assets/` — ภาพตาราง OREDA (failure descriptor, failure mode vs maintainable item, failure mechanism, resolution)
- [[raw/reliability-based-maintenance-management]] — หนังสือ Reliability Based Maintenance Management (SE-ED 2553, 400 หน้า) reading notes 12 บทใน `raw/reliability-based-maintenance-management/`
- [[raw/iso-14224]] — ISO 14224:2016 (280 หน้า, licensed ไม่เก็บ PDF) reading notes ถอดความ 6 ส่วนใน `raw/iso-14224/` (clauses 1-7, 8-9, Annex A, B, C-D, E-F)
- [[raw/cmrp]] — สไลด์หลักสูตร CMRP ของ PETROSYNC 11 ไฟล์ 408 หน้า (สแกน, PDF เก็บในเครื่องเท่านั้น) reading notes ถอดความใน `raw/CMRP/CMPR-01.md` ถึง `CMPR-11.md`
- [[raw/spare-parts-optimization]] — หนังสือ Spare Parts Optimization (สุชาติ ศุภมงคล, SE-ED 2546, 143 หน้า; OCR ทั้งเล่มเก็บในเครื่องเท่านั้น) reading notes ถอดความ 7 ไฟล์ใน `raw/spare-parts-optimization/`
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
- [[CMRP Course]] — hub สไลด์ CMRP (PETROSYNC): SMRP BOK 5 pillars, AEO model, แผนที่ไฟล์ไปยังหน้า wiki, ข้อผิดพลาดในสไลด์ 21 จุด และ 4 ข้อ contested กับ RBMM/ISO
- [[Spare Parts Optimization Book]] — hub หนังสือ SPO (มุมมองคลังพัสดุ/จัดซื้อ MRO, ที่มา COSAL + Esso): ตาราง 12 บทไปยังหน้า wiki, offset หน้า PDF/book, ข้อผิดพลาด OCR/หนังสือประมาณ 28 จุด

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
- [[Knowledge Graph Triplet]] — สเปก triplet subject-predicate-object: syntax `## Triplets`, node naming, predicate vocabulary และ `graph/triplets.csv`

### Area ข: Compressor failure hierarchy (OREDA / ISO 14224)

- [[Failure Hierarchy]] — ลำดับชั้น 7 ระดับ Equipment ถึง Resolution, ความขัดแย้งเรื่อง sub unit ระหว่าง sources และการเทียบเลขระดับกับ ISO 14224
- [[Failure Mode]] — hub ตาราง 19 โหมด พร้อม % failure rate (total 85.66); ISO Table B.6 ให้ compressor 20 โหมด (+PLU)
- [[AIR Abnormal Instrument Reading]] — AIR 17.18%, Instruments x AIR 13.54
- [[SER Minor In-Service Problems]] — SER 13.05%, Filter(s) x SER 7.33
- [[LOO Low Output]] — LOO 10.11%, Cylinder liner x LOO 5.78
- [[ELU External Leakage Utility Medium]] — ELU 8.62%, 33 คู่ item แบบ long tail
- [[PDE Parameter Deviation]] — PDE 8.13%, Instruments x PDE 3.35
- [[OTH Other]] — OTH 5.46%, mechanism = Other ทุกแถว
- [[ELP External Leakage Process Medium]] — ELP 4.58%, Cylinder liner/Valves เด่น
- [[OHE Overheating]] — OHE 4.18%, Cylinder liner x OHE 3.40
- [[UST Spurious Stop]] — UST 4.16%, Instruments/Control unit เด่น; ISO 14224:2016 ใช้ UST ไม่มี SPS
- [[Failure Mechanism]] — 37 mechanism พร้อมรหัส, category และจำนวน resolution; เทียบ ISO Table B.2 (38 รหัส)
- [[Failure Cause Codes]] — รหัส mechanism 35 ตัวและ CAUSE_CODE 473 รหัส พร้อมข้อขัดแย้ง; ISO failure cause Table B.3 (21 รหัส)
- [[Resolution Codes]] — 14 รหัส resolution พร้อมจำนวนแถวใช้งานและข้อขัดแย้ง CHG; เทียบ ISO maintenance activity Table B.5 (12 รหัส)
- [[Maintainable Item]] — 44 รหัส item และกติกาจับคู่หลาย sub unit
- [[OREDA]] — แหล่งข้อมูลต้นทางและข้อจำกัด (ไม่มี absolute rate)
- [[ISO 14224]] — hub มาตรฐาน ISO 14224:2016: สาระแต่ละส่วนและข้อสรุปที่เปลี่ยนความเข้าใจเดิม (UST, PLU, 9 ระดับ)
- [[ISO 14224 Taxonomy]] — taxonomy 9 ระดับ, failure data ผูกกับระดับใด, กติกา boundary, equipment class (CO = compressor) และการเทียบกับ 7 ระดับของ wiki
- [[Failure Detection Method]] — รหัส detection method 11 ตัว (Table B.4) และกติกา failure ที่พบระหว่าง PM
- [[Failure Impact Classification]] — critical/degraded/incipient, maintenance impact และความหมาย "critical" 3 แบบ
- [[Safety Critical Failure Classification]] — Annex F: DD/DU/SD/SU, CCF, test interval, failure fraction
- [[RM Data Quality]] — คุณภาพข้อมูล RM: วางแผน, checklist ตรวจสอบ, เกณฑ์ความครบถ้วน และข้อมูลที่ต้องใช้ต่อประเภทการวิเคราะห์ (Annex D)
- [[CAUSE_CODE Convention]] — รูปแบบ SubUnit-Item-Mechanism และ code collision

### Area ข: Reliability Based Maintenance Management (RBMM)

หน้าสังเคราะห์จากหนังสือ [[Reliability Based Maintenance Management Book]] (ingest 2026-10-21)

- [[Asset Life Cycle]] — วงจรชีวิตทรัพย์สิน, 4 กลุ่มงาน, criticality A/B/C, Zero Plant Breakdown @ Minimum Cost
- [[Maintenance Efficacy Pyramid]] — พีระมิด 6 ชั้นและการประเมิน 16 หัวข้อ จาก Reactive ถึง Optimization
- [[Maintenance KPIs]] — ต้นไม้ดัชนี 19 กิจกรรม และดัชนี B/C/D พร้อมสูตร variance; ISO Annex E KPI 34 ตัวและ KPI vs benchmark
- [[Availability and OEE]] — MTTF/MTTR/MWT/MDT ถึง Availability และ OEE กับการใช้ในรายงาน และประเภท Ai/Aa/Ao (ความรู้ทั่วไป) เทียบนิยาม ISO AI/Ao/AT (contested)
- [[Maintenance Strategic Report]] — รายงาน A4 ส่วน A-E พร้อมตัวเลขตัวอย่างและการตรวจเลข
- [[CMMS]] — ระบบบริหารงานบำรุงรักษา: 10 โมดูล, Asset Register หยุดที่ Equipment + Object Part, Process vs Content, ห้ามปิด WO ถ้ายังไม่ระบุ Failure Mode
- [[Failure Data Recording]] — ฟิลด์ใน Work Order, record ขั้นต่ำ 5 รายการ และตารางเทียบรหัส Failure Mode ISO 14224 (pump/motor) กับ wiki (UST หลัก, SPS = alias)
- [[RCM Reliability Centered Maintenance]] — RCM ตาม Nowlan-Heap: 7 กระบวนการ, task selection ตาม consequence, 7 คำถาม, Classical vs Fast Track
- [[FMECA]] — RPN (S x O x D) และ criticality เชิงปริมาณ FF/FFCr/Cr(t) พร้อมตัวอย่างคำนวณ
- [[Criticality Assessment]] — Consequence x Likelihood = 1-30 แบ่ง A/B/C ใน 3 ด้าน (Commercial, Safety, Environment) และกลยุทธ์ PM/อะไหล่/งบตามระดับ
- [[Weibull Analysis]] — พารามิเตอร์ β/η/γ, วิธีประมาณ (probability plot, Y/X regression), ตัวอย่าง TTF 8,500-16,000 ชม. และกระทบยอด β 3.5/3.79/3.94
- [[Failure Patterns and Bathtub Curve]] — pattern A-E, bathtub curve และกฎเลือกงาน PM ตามค่า β
- [[Reliability Metrics]] — F(t), R(t), λ(t), MTTF/MTBF, conditional reliability, availability, MTTR พร้อมสูตรที่หนังสือพิมพ์ผิด; MTBF ของ RBMM เทียบ METBF ของ ISO (contested)
- [[Maintenance Time Definitions]] — แยกเวลาตาม ISO (up/down, planned/unplanned) และ MTTR/MTTRes/MRT/MART/MDT/METBF เทียบ MTTR/MWT ของ RBMM
- [[Failure Rate Estimation]] — ISO Annex C: λ = n/τ, ช่วงความเชื่อมั่น chi-square, กรณีไม่มี failure, รวมข้อมูลหลายแหล่ง, on-demand failure, CCF และสูตร test interval
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

### Area ข: CMRP (PETROSYNC course)

หน้าสังเคราะห์จาก [[CMRP Course]] (ingest 2026-10-25) หน้าเดิมหลายหน้าได้หัวข้อเสริมจาก CMRP ด้วย (ดู hub)

- [[Wear Mechanisms]] — กลไกการสึก 7 แบบ, Archard, การควบคุม และการจับคู่กับรหัส ISO Table B.2
- [[Lubrication and Oil Analysis]] — ส่วนประกอบสารหล่อลื่น, API base oil group I-V, additive, contamination/varnish, การทดสอบน้ำมัน/จาระบี, ISO 4021, NLGI
- [[Condition Monitoring Techniques]] — inspection boundaries, vibration (ISO 10816-1), thermography, motor current, ultrasonic, optimization matrix, D-I-P-F
- [[Root Cause Analysis]] — RCA/RCFA 4 ขั้น, 5 Whys, why-because graph, stress-strength, ปัจจัยความสำเร็จ และ RCA บังคับของ ISO
- [[Maintenance Planning and Scheduling]] — planning vs scheduling, 7 ขั้นวางแผน, span of control, estimating, priority PR1-PR4, กติกาจัดตาราง, wrench time
- [[Maintenance Backlog and Schedule Compliance]] — backlog เป็นสัปดาห์ (2-3 vs 3-6 สัปดาห์), ready/total, purging, schedule compliance/performance/effectiveness
- [[Turnaround Management]] — กลยุทธ์ eliminate-first, golden rule ของ work list, emergent work, 4 phase, single point responsibility
- [[Maintainability]] — M(t), lognormal repair time, MIL-HDBK-472 7 ขั้น, maintainability allocation, maintenance level NF X60-000
- [[Reliability Allocation]] — equal, ARINC, penalty function ตาม feasibility index และ NLP
- [[Statistical Process Control]] — X-bar/R, p/np/c/u, run rules, Cp/Cpk, confidence interval (พร้อมข้อผิดพลาดในสไลด์)
- [[Fault Tree Analysis]] — gate, cut set, minimal cut set, common cause, เทียบ RBD
- [[Reliability Growth Models]] — Duane postulate, Crow-AMSAA (NHPP)
- [[Human Reliability]] — P(HE), ประเภท error, performance shaping factors, culture change
- [[TPM and Lean Maintenance]] — Lean, TPM pillars, 5S, SMED, JIT, Six Sigma
- [[Maintenance Business Case]] — 6 ขั้น business case, DCF/IRR/hurdle rate, business case vs business plan
- [[Digital Maintenance and Predictive Analytics]] — Maintenance 4.0, framework ผู้ขาย, predictive modelling และข้อจำกัด

### Area ข: Spare Parts Optimization (SPO)

หน้าสังเคราะห์จาก [[Spare Parts Optimization Book]] (ingest 2026-10-27) หน้าเดิมที่ได้หัวข้อเสริม: [[Spare Parts Management]], [[Spare Part Criticality and Risk]], [[EOQ and Reorder Point]], [[Maintenance KPIs]], [[Turnaround Management]], [[Centrifugal Compressor]], [[Reciprocating Compressor]]

- [[MRO Material Classification]] — วัสดุ 4 ประเภท, นิยาม MRO, ประเภทโรงงาน, การบันทึกบัญชี, อะไหล่ 9 กลุ่ม (Insurance/Standby รหัส S, OAR 4 เกณฑ์, Capitalized, Commissioning) และปัจจัย 7 ข้อว่าควรสต็อกไหม
- [[Parts Interchangeability]] — คู่มืออะไหล่ใช้ร่วมหลายเครื่อง 6 ขั้น, ตาราง 7 คอลัมน์, commodity code vs OEM part number
- [[Spare Parts Recommendation by Equipment Type]] — หลักปฏิบัติวิศวกรรม: สต็อกขั้นต่ำ startup + 1 ปี, % อะไหล่ต่ออุปกรณ์ (pump, centrifugal/reciprocating compressor, valve plates 400%, gaskets 200%) และการจับคู่กับ maintainable item
- [[Warehouse Design and Storage]] — หน้าที่คลัง, ขนาดคลัง (425 ft² ต่อ 1 M USD GPI), แสง 30/50 fc, popularity storage 20/60/20, aisle, layout A-F, การเก็บท่อ/วาล์ว/ถังก๊าซ, free issue
- [[Tool Crib and Warehouse Security]] — ประเภทเครื่องมือ 4 กลุ่ม, ระบบยืม tag/shadow board vs ใบยืม, หลักความมั่นคง 4 ข้อ, gate pass, การเบิกนอกเวลา
- [[MRO Purchasing and Contracting]] — PR ที่ดี, proactive purchasing 10,000→200 รายการ, Blanket Order (BOR/PDR), System Contracting, Consignment vs Vendor Stocking, outsourcing, air freight, claims
- [[MRO Inventory Control Methods]] — EOQ แบบ SPO (CO 90-120 บาท/รายการ), COP 7 องค์ประกอบ, ROP = D×LT + SS (%), High/Low, Periodic Review, Order Up-to, OAR, ตารางวิธีต่อประเภทอะไหล่
- [[Inventory Turnover and GPI Benchmarks]] — turnover, MOS/DOS, Inventory % GPI benchmark 2/4/10%, ≤4% (≤1.5% labour intensive), ตัวเลข Esso และการเทียบกับ B7 ของ RBMM
- [[MRO Inventory Reduction Program]] — ABC/ABU (A = มูลค่าใช้สูง), obsolete 3 ปี, danger signals, ตัวอย่าง 3→5 รอบประหยัด 3 ล้านบาท, Materials Control Committee 18 หน้าที่

## comparisons/ (area ข)

- [[Compressor Type Failure Profiles]] — เปรียบเทียบ % 19 โหมดของ centrifugal vs reciprocating vs screw
- [[Resolution Matrix by Mechanism]] — 37 mechanism x 13 resolution (233 คู่ที่เป็นไปได้)
- [[Compressor Subdivision Wiki vs ISO 14224]] — subunit และ maintainable item ของ dataset เทียบ ISO Table A.9 รายตัว, type code CE/RE/SC/AX, boundary
- [[CMRP vs RBMM FMECA Scales]] — สเกล FMECA 1-10 vs 1-5, matrix 5x5 vs 5x6, RPN band และเลขผิดในสไลด์
- [[SPO vs RBMM Spare Parts Approaches]] — เทียบหนังสือ SPO กับ RBMM 10 ประเด็น (มุมมอง, การจำแนก, ตัดสินสต็อก, safety stock, ABC, holding cost, เป้ามูลค่าสต็อก, planned vs unplanned, Blanket Order, KPI); contested 1 ข้อ (เป้ามูลค่าสต็อก; ABC กลุ่ม A resolve แล้ว)
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
- [[How does Weibull help reliability]] — β บอกรูปแบบการเสียและประเภทงาน PM, η, ตัวอย่าง R/MTTF/conditional R, T(R=0.8) ≈ 8,837 ชม. (หนังสือพิมพ์ผิด 13,848) (area ข)
- [[How to set up CMMS failure structure to support FMECA]] — โครง 3 ชั้น: hierarchy + catalog ISO (B.2-B.6, C.2) + valid combination, FMECA library (S/O/D, task) และ WO ที่ปิด loop ปรับ O/S/D (area ข)

## graph/ (generated)

- `graph/triplets.csv` — knowledge graph รวม triplet ของทุกหน้า area ข (generate ด้วย `graph/build_triplets.py` ห้ามแก้ด้วยมือ) สเปกใน [[Knowledge Graph Triplet]]

## _archive/

- [[_archive/README]] — กติกาโฟลเดอร์
- [[_archive/log-maintenance-reliability-2026-10-20]] — log ประวัติของ Maintenance Reliability wiki ก่อนรวม vault (ไม่นับเป็นหน้า content)

## ไฟล์ rules

- [[SCHEMA]] — กติกา wiki
- [[log]] — บันทึก action แบบ append-only
- [[README]] — ตัวชี้เริ่มต้น

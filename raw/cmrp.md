---
title: "PETROSYNC CMRP training course slides (CMPR-01 to CMPR-11)"
type: raw-source
source_url: "file:///.claude/llm-wiki/raw/CMRP/ (PDF kept local only, gitignored)"
ingested: 2026-10-25
sha256: "per file, see table"
format: scanned PDF slides (Apeos copier, OCR text layer, 408 pages, 2 slides per page in most files) → reading notes per file (Thai, paraphrased)
immutable: true
---

# PETROSYNC CMRP (Certified Maintenance & Reliability Professional) course slides

Raw source — ห้ามแก้ไขหลัง ingest

- ผู้จัดทำ: PETROSYNC ("operational excellence experts, since 2014") เอกสารประกอบหลักสูตรเตรียมสอบ CMRP ตาม SMRP Body of Knowledge 5 pillars
- ไฟล์ต้นฉบับเป็นสไลด์ที่มีลิขสิทธิ์ สแกนจากเครื่องถ่ายเอกสาร มี OCR หยาบและมีลายมือเขียนทับบางหน้า จึง **ไม่เก็บ PDF ใน git** (`.gitignore`: `raw/CMRP/*.pdf`, vault sync ไป GitHub) PDF อยู่ในเครื่องที่ `raw/CMRP/` เท่านั้น
- เนื้อหาใน `raw/CMRP/CMPR-XX.md` เป็น **reading notes ที่ถอดความ** อ่านจาก OCR และ render ภาพหน้าที่ OCR อ่านไม่ได้ (ตาราง รูป สูตร) ลายมือที่อ่านไม่ออกไม่ถูกบันทึก
- อ้างอิงแบบ `(CMRP CMPR-0X p.N)` โดย N = PDF page (ไม่ใช่เลขสไลด์ที่พิมพ์มุมล่าง)
- ข้อผิดพลาดในสไลด์ (เลขคำนวณผิด ข้อความซ้ำ หน่วยผิด) ถูก flag ไว้ใน notes ของแต่ละไฟล์ ชื่อไฟล์ต้นฉบับสะกด "CMPR" (ไม่ใช่ CMRP) คงไว้ตามเดิม
- ลำดับไฟล์ไม่ตรงกับ pillar เสมอ หลายไฟล์ผสมหลายหัวข้อ (ดูตาราง)

| File | PDF pages | หัวข้อหลัก | sha256 | Notes |
|---|---|---|---|---|
| CMPR-01 | 50 | AEO model (PM/PRM/ODR/RTF), SMRP BOK 5 pillars, definitions, machine inspection boundaries, failure patterns %, D-I-P-F curve, lubrication and oil analysis, vibration basics (ISO 10816-1) | b8250b9c4b2a5e1d718c9280f1847c2fb3635b5e0e2b55b3ea58d5d6b54041b5 | `CMRP/CMPR-01.md` |
| CMPR-02 | 52 | wear mechanisms (Archard), base oil groups, additives, oil/grease tests, ISO 4021 sampling, NLGI, thermography, motor current, ultrasonic, maintenance optimization matrix, criticality/risk matrix, life cycle cost, FMEA types, MIL-STD-1629A | f51a4f86c2043cd5ec4ea3eb32abc0bf03b399905120394cd0ac2fd139f9529a | `CMRP/CMPR-02.md` |
| CMPR-03 | 50 | FMECA probability/severity scales and criticality, strategy decision tree (RtF/FFM/SM/CBM/MOD), PM interval formulas, spare decision, RCA/RCFA (5 Whys, why-because, stress-strength), SMART objectives, KPI design, balanced scorecard, business case vs plan | 7b64a0dca5d71b2de055629b544abe368f484c792db4afb3b231a3cfeee3881b | `CMRP/CMPR-03.md` |
| CMPR-04 | 47 | business case steps (DCF, IRR, scenario), Lean/TPM/5S/SMED/Six Sigma, RAMS, availability Ai/Aa/Ao, maintainability (MIL-HDBK-472, lognormal), PM/CM analysis, renewal, RBD, maintenance levels NF X60-000, reliability allocation | fa0b12a5f03dd56d0e67a1cab33fec8d573d55f289830327b211ee55f71dfbd8 | `CMRP/CMPR-04.md` |
| CMPR-05 | 3 | reliability target allocation with cost/penalty function, feasibility index | bcc16e963fa70f45d4a4a6a55a25104dd42ff1a1ee82e4da71a1e6309d5d8a36 | `CMRP/CMPR-05.md` |
| CMPR-06 | 48 | reliability apportionment (equal, ARINC), statistics revision (discrete/continuous distributions, CLT, z), Weibull case study (signalling boards), PM optimization C2/C1, Markov, Monte Carlo, SPC intro | 05653ff45e25e8b315e3a44ab0d834ec73c62a940c39c7a2dec95b0cbbbd059d | `CMRP/CMPR-06.md` |
| CMPR-07 | 2 | X-bar and R control chart terms, constants, torque example | 430a1f8c6ebfe7e66a0e1cf644c366f37aaffd96bca46bad1a9bc21043b4a657 | `CMRP/CMPR-07.md` |
| CMPR-08 | 50 | SPC attribute charts (p, np, c, u), run rules, process capability Cp/Cpk, confidence interval; digitization and predictive modelling; risk-based spares and MRO inventory models; wrench time and planning effectiveness | ac313f6cdd7131a6d3d1cb589d46fa9d25a58bea75e9cd8aa8ccae134c150e66 | `CMRP/CMPR-08.md` |
| CMPR-09 | 46 | work management: planning vs scheduling, 7-step planning process, span of control, estimating, priority PR1-PR4, weekly scheduling rules, backlog in weeks, staging | 33a6cd72c379c672eed3e073ec03f1be72b970937aee9c0c6976145d5a070849 | `CMRP/CMPR-09.md` |
| CMPR-10 | 30 | backlog band 3-6 weeks and purging, planning/schedule metrics (compliance, performance, effectiveness), turnaround strategy, work list golden rule, emergent work, organisation | 5382676e0765e97b09496b33f73f8e71d2b8f860fc09a442113f4632c32570d9 | `CMRP/CMPR-10.md` |
| CMPR-11 | 30 | turnaround phases (initiation, preparation, execution, termination), human reliability (P(HE), PSF), culture change, reliability growth (Duane, Crow-AMSAA), fault tree analysis, dependency/state diagrams | bea35e5ded50a8b407805f2f4a8d26c992828b48a2883c3f33ba2d8887244243 | `CMRP/CMPR-11.md` |

หน้า wiki ที่สรุปจาก source นี้: [[CMRP Course]] (hub)

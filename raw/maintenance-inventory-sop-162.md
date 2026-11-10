---
title: Maintenance Inventory Control SOP (TH-GEN-PROD-162)
created: 2026-11-10
updated: 2026-11-10
type: source
tags: [internal-sop, spare-parts, inventory, min-max, criticality, kpi]
sources: []
confidence: high
contested: false
provenance: internal
verbatim_sha256: 976b885fe04afa779151597b996685ccdd15040e5bd02165995359633b4c65d6
doc_number: TH-GEN-PROD-162-REP-0001
revision: R2
---

# Maintenance Inventory Control SOP (TH-GEN-PROD-162)

**อะไร:** SOP ภายในของ Thailand Production เรื่องการควบคุมอะไหล่คงคลัง เลขที่ **TH-GEN-PROD-162-REP-0001 Rev 2** — ครอบวงจรตั้งแต่จัดชั้นความวิกฤตของอะไหล่ → ตัดสินว่าจะสต็อกหรือไม่ → ตั้ง Min/Max และ safety stock → เลือก control model → วัด KPI → ขั้นตอนงานและบทบาทผู้รับผิดชอบ

**สถานะไฟล์:** เอกสารภายในองค์กร **ไม่ขึ้น repo สาธารณะ** — ตัว .docx เก็บในเครื่องที่ `/opt/data/home/docs_incoming/TH_GEN_PROD_162_REP_0001_Maintenance_Inventory_R2_min_max_revise.docx` (420,821 bytes, sha256 `976b885f…4c65d6`); ไฟล์นี้สรุปเป็น **paraphrase + ตารางกฎ** ไม่ใช่ข้อความเต็ม ห้าม quote ยาว

**วิธีอ้าง:** `(SOP 162 §5.1)`, `(SOP 162 §5.4)`

**ประวัติ Rev:** Rev 2 (2026-11-10) แก้เฉพาะ §5.2 Min-Max — เดิมใช้ `MAX = MAX(SS + PM usage × LT, MOQ)` ซึ่งให้ Max ≤ Min ได้ และใช้ LT เดี่ยวแทน protection interval; Rev 2 เปลี่ยนเป็น `Max = Min + Q`, `P = LT + R` และเพิ่มตัวอย่างคำนวณ 5 เคส

## แผนผังเอกสาร

| ส่วน | หัวข้อ | เนื้อหาที่ ingest |
|---|---|---|
| §5.1 | Spare part criticality classification | C1/C2/NC + asset criticality link + ตัวอย่าง |
| §5.2 | Min-Max & ROP | Min/Max definition, ตาราง factor, ตัวอย่างคำนวณ |
| §5.3 | Spare part stocking decision | 5 เงื่อนไข stock/OAR + โซน cost ratio |
| §5.4 | Statistical safety stock and demand forecast | service level ต่อ class, σc, z, วิธีพยากรณ์ต่อกลุ่ม |
| §5.5 | Inventory control model | movement × cost → 4 โมเดล |
| §5.6 | Inventory performance KPIs | 7 KPI + benchmark |
| §5.7 | Periodic review, obsolete and surplus | รอบทบทวน, dead stock |
| §5.8, §6 | Work flow, RESPONSIBILITIES | ขั้นตอน new item / RFQ / approval, บทบาท |

## ตารางกฎที่ ingest (paraphrase)

### Criticality (§5.1)

| Code | ชั้น | เกณฑ์ | Asset criticality link | Stocking strategy |
|---|---|---|---|---|
| C1 | Critical-Vital | ทันทีและรุนแรงต่อ production หรือ safety, ยอมรับความเสี่ยง stock ไม่ได้ | SCE / High | safety stock บังคับ |
| C2 | Critical-Essential | กระทบ continuous operation แต่ยอมรับความเสี่ยงได้ถ้ามี capacity/redundancy | High / Medium | stock, โดยเฉพาะ LT > 3 เดือน |
| NC | Non-Critical | ไม่กระทบทันที ไม่มีความเสี่ยง safety | Low | ไม่มี safety stock, OAR |

### Stocking decision (§5.3)

5 เงื่อนไข: (1) ซ่อมได้โดยไม่ต้องใช้ part นี้ → ไม่สต็อก (2) NC → OAR (3) redundancy → ไม่สต็อก เว้นแต่ LT > 3 เดือน (4) LT ยาวกว่า P–F interval → สต็อก (5) กระทบ production/safety (C1 หรือ C2 ไม่มี redundancy) → สต็อก
โซน cost ratio: > ~9 สต็อกได้โดยไม่ต้องอนุมัติเพิ่ม | 1–9 สต็อกแต่ต้องอนุมัติ | ≤ 1 ไม่สต็อก | ≤ 1 แต่ single stock-out ยอมไม่ได้ → insurance spare อนุมัติโดย management

### Service level (§5.4)

C1: 95–99.5 % (z 1.645–2.576) | C2: 90–95 % (z 1.282–1.645) | NC: ไม่มี SS (OAR); fixed default ในตาราง Min-Max = C1 1, C2 1, NC 0 เมื่อยังไม่มีประวัติ

### Forecast method (§5.4)

fast moving → normal (mean/σ), ROP + statistical SS, EOQ | slow + low criticality → MTBF หรือ Poisson ตาม target SL | slow + medium → Poisson/simulation + cost ratio | high criticality → reliability analysis (Weibull, failure mode) ผูกกับแผน PM + risk-based/insurance

### Control model (§5.5)

perpetual ROP/EOQ: fast-high, fast-medium, medium-high | Min-Max + blanket order: fast-low, medium-medium | two-bin: medium-low, slow-medium, slow-low | one-for-one: slow-high

### KPI (§5.6)

line fill ≥ 95 % รวม และ ~100 % สำหรับ C1 | stock-out ≤ 1 % | stock turnover ดู trend | inventory value % GPI ≤ 4 % (อ้าง SPO) และ 1–3 % (อ้าง RBMM) | months of supply ดู trend | inactive 12 เดือน ลดลง | emergency purchase ratio ลดลง

## ข้อจำกัดที่ต้องระวัง

- service level เป็น **ช่วง** ไม่ใช่ค่าเดียว — ต้องเลือกภายในช่วงด้วยการวิเคราะห์ consequence ไม่ใช่หยิบ mid-point
- fixed SS default (1/1/0) หยาบ; SOP เองกำหนดให้ใช้ statistical เมื่อมีประวัติ ≥ 3 ปี
- ไม่ครอบ **rotable/repairable pool** (อะไหล่ซ่อมได้ใช้จำนวน pool + repair lead time ไม่ใช่ Min-Max)
- asset criticality link เป็นค่า default ระดับ equipment — part ระดับล่างต้องตัดสินด้วยผลกระทบจริง (เช่น generator อยู่ C2 แต่ emergency generator ที่ป้อน SCE ควรถูกยกเป็น C1)
- เอกสารเป็น internal procedure ไม่ใช่มาตรฐานภายนอก — ใช้เป็น "นโยบายองค์กร" ไม่ใช่หลักฐานทางวิศวกรรม

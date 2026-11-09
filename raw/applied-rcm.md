---
title: "Applied Reliability Centred Maintenance — PETROSYNC course material (Nov 2025)"
type: raw-source
source_url: "file:///opt/data/home/Documents/brain2nd/raw/applied-rcm/Applied_RCM_PETROSYNC_2025.pdf"
ingested: 2026-11-02
sha256: cdfe2737ab18bf22eae283294b1e9dac7df0d5e0009d1bc08fb910867aa01935
format: PDF สแกน 173 สไลด์ (text layer เดิมเป็น OCR จากเครื่องถ่ายเอกสาร คุณภาพต่ำ) → ถอดใหม่ด้วย vision OCR เป็น `raw/applied_reliability_centered_maintenance.md`
immutable: true
---

# Applied Reliability Centred Maintenance — PETROSYNC (3–5 พ.ย. 2025)

Raw source — ห้ามแก้ไขหลัง ingest

- หลักสูตร: **Applied Reliability Centered Maintenance** · PETROSYNC (Mechanical Engineering Series)
- จัดอบรม: **3–5 พฤศจิกายน 2025** · Amari Bangkok Hotel, Phanfa Room 7F
- เอกสาร: course material **173 สไลด์** — เป็นสแกน ไม่มี text layer ที่ใช้ได้ (text layer เดิมมาจาก OCR ของเครื่องถ่ายเอกสาร อ่านไม่ได้ในหลายหน้า) จึงถอดใหม่ด้วย vision OCR ทั้งเล่ม
- ไฟล์: PDF `raw/applied-rcm/Applied_RCM_PETROSYNC_2025.pdf` (6.7 MB) · ข้อความเต็ม `raw/applied_reliability_centered_maintenance.md` (152 KB) — **gitignore ทั้งคู่** (ลิขสิทธิ์ PETROSYNC)

## โครงหลักสูตร (Module index)

| Module | หัวข้อ | slide |
|---|---|---|
| 1–2 | ปูพื้น: RCM terminology, function/functional failure, FMECA | 1–22 |
| 3 | Identify What Is Important | 23 |
| 4 | Define What Should Be Done | 55 |
| 5 | RCM Customization and Requirements | 92 |
| 6 | Change the Existing Program | 109 |
| 7 | RCM Project | 140 |
| 8 | Risk Based Inspection (RBI) Integration | 167 |

กรอบคิดหลักที่สไลด์เน้น (Course Outline, sl.6): RCM มี 3 แนวคิด —
**identify what is important → define what should be done → change the existing program**

## สาระที่ใช้ได้กับงานเรา

- **Criticality / failure severity** — วิธีกำหนดระดับจากต้นทุนซ่อมเทียบค่า X/Y และ "acceptable cost without superior approval" (sl.30–31)
- **Failure characteristics ที่ใช้เลือกยุทธศาสตร์** — ซ่อนได้ไหม / critical ไหม / มี condition indicator ไหม / interval รู้และคงที่ไหม (sl.60)
- **Hidden และ Critical failure** — นิยามและผลต่อการเลือกงาน (sl.60)
- **FMECA และ practical session** — ใช้เป็นโครง workshop กับทีมช่างได้ (Module 3–4)
- **ISO 14224 Table B.4 / B.5** (sl.100) — ตาราง failure mode ของ rotating equipment พร้อมรหัส (ELP, FTS, STP, ERV, KGP, ELU, MIB, OHE, PLU, PUE, AR, STD, SER, UNK) และตาราง maintenance activity 12 รหัส (Replace, Repair, Modify, …, Combination, Other) — **หน้านี้เชื่อมตรงกับงาน failure hierarchy ใน CMMS**
- **แหล่งข้อมูล failure rate** (sl.100 ท้ายหน้า): MIL-HDBK-217, Telcordia/Bellcore TR-332, RDF 2000, PRISM, IEEE Gold Book 493, NPRD-95, **OREDA**, NSWC-94/L07
- **RBI integration** (Module 8) — เชื่อม risk-based inspection เข้ากับ RCM ผ่าน AMST tool

## ระดับความน่าเชื่อถือและข้อจำกัด

- เป็น **สื่ออบรม (secondary source)** — ต่ำกว่า ISO 14224 และต่ำกว่าหนังสือ RBMM ในเชิงหลักการ; ถ้าขัดกับ ISO หรือ RBMM ให้ยึด ISO/RBMM และบันทึกเป็น contested
- **คุณภาพ OCR**: เนื้อหา bullet อ่านได้ดี แต่ **ชื่อสไลด์หลายหน้าถอดเพี้ยน** (เช่น "pa j| ure characteristics") และ **ตาราง B.4 คอลัมน์ matrix เป็น `[?]`** — ตัวรหัสและชื่อ failure mode ได้ครบ แต่ถ้าต้องใช้ matrix เต็มให้เปิด PDF หน้า 100
- สไลด์มีโลโก้/ลายน้ำ PETROSYNC ทุกหน้า — ตัดออกจากข้อความแล้ว
- ไม่มี `## Triplets` (raw source ไม่ใช่หน้า wiki)

## วิธีอ้าง

`(PETROSYNC RCM 2025 sl.N)` — N = ลำดับสไลด์ใน PDF (marker `<!-- page: N -->` ในข้อความเต็ม)

## เกี่ยวข้อง

[[RCM Reliability Centered Maintenance]] (หลักการจาก RBMM) · [[Failure Hierarchy]] · [[ISO 14224 Taxonomy]] · [[FMECA]] · [[Criticality Assessment]] · [[PM Task Selection]]

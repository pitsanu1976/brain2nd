---
title: "Oracle eAM User's Guide 11i — concept note (object model & work management)"
type: raw-source
source_url: "file:///opt/data/home/Documents/brain2nd/raw/oracle-eam-ug/A95930-01_eAM_User_Guide_11i.pdf"
ingested: 2026-11-02
sha256: 3bfd24c4534c360dfd4aa1d71f885867155b4beb242f33d49a24c7b68105cc37
format: PDF text layer (234 หน้า) → ข้อความเต็ม `raw/oracle_concept.md` (เก็บในเครื่องเท่านั้น) + concept note นี้
immutable: true
---

# Oracle eAM User's Guide 11i — concept note

- เอกสาร: **Oracle Enterprise Asset Management User's Guide, Release 11i** · Part No. **A95930-01** · กุมภาพันธ์ 2002 · 234 หน้า · 7 บท
- ข้อความเต็ม: `raw/oracle_concept.md` (marker `<!-- page: N | ch: C-P -->`) · PDF: `raw/oracle-eam-ug/A95930-01_eAM_User_Guide_11i.pdf` — **มีลิขสิทธิ์ Oracle, gitignore ทั้งคู่**
- ต่างจาก [[raw/oracle-manual]] (สไลด์อบรม D14149GC31 Vol.1+2): เล่มนี้คือ **functional reference จริง** — ละเอียดระดับ field/form, ลำดับขั้นตอน, และโมเดลข้อมูล ใช้คู่กันได้ (สไลด์ = ภาพรวม/ลำดับการสอน, guide = รายละเอียดการตั้งค่า)

## 1. โมเดลข้อมูล eAM (Ch.2 Setting Up)

ลำดับการ setup ที่เอกสารบังคับ (สร้างของล่างก่อนเสมอ):

`Organization (enable eAM) → eAM Parameters → Asset Area → Department/Resource → Lookups → Category Set/Code → Asset Group → Asset Attributes → Asset Number (parent/child) → Asset Activity (+ BOM + Route) → Rebuildable Item → Collection Plan`

| Object | ความหมาย (ตามเอกสาร) | หน้า |
|---|---|---|
| Organization | แต่ละ org ตั้ง eAM เองได้ (parameters, lookups, asset attributes) | 2-5, 2-7 |
| eAM Parameters | ค่าตั้งระดับ org | 2-9 |
| **Asset Area** | lookup ที่ผู้ใช้กำหนด ใช้แบ่งโรงงานเป็นโซนเพื่อ track/account asset | 2-11 |
| **Department / Crew** | พื้นที่ในองค์กรที่มีคน/เครื่อง/ผู้รับเหมา ใช้เก็บต้นทุน ปันส่วน overhead เทียบ load กับ capacity; ผูก resource (craft) พร้อมกะและ capacity ได้ | 2-12 |
| Department Approver | ผู้อนุมัติ work request ระดับแผนก | 2-14 |
| Lookups | activity type, activity cause, asset criticality code, work request status, note type ฯลฯ | 2-16 |
| Category Codes / Sets | จัดกลุ่ม asset เพิ่มจาก asset group | 2-27 |
| **Asset Group** | การจำแนกประเภทเครื่องจักร เช่น Trucks, Pumps, Towers, Buildings, Storage Tanks, Turbines — สร้างจาก **Master Item form** ต้องมีก่อนสร้าง asset number | 2-30 |
| Asset Attributes | คุณลักษณะร่วมของ asset group เช่น Nameplate, Facility Information, Engineering Specifications, Regulation Requirements, Horsepower, Voltage, Square Footage | 2-33 |
| **Asset Number** | ตัว asset จริง สร้างได้ 4 วิธี (เดี่ยว, copy, multiple entry, interface); รองรับ **parent/child hierarchy** เช่น BUILDING → Building 100 → Floor 1 | 2-37 |
| **Asset Activity** | template มาตรฐานของ "งาน" (job) ที่เอาไปผูกกับ asset number หรือ rebuildable item; ต้องมี activity BOM (วัตถุดิบ) + activity route (ขั้นตอน/resource) | 2-43, 2-53, 2-57 |
| Asset Route | เส้นทางตรวจของหลาย asset ในรอบเดียว | 2-48 |
| **Rebuildable Item** | ชิ้นส่วนที่ซ่อมกลับมาใช้ใหม่ (เช่น motor) — เก็บประวัติติดตั้ง/ถอด/rebuild และ genealogy | 2-59, 2-62 |
| Collection Plan | แผนเก็บข้อมูลคุณภาพ (quality data) ระหว่างทำงาน | 2-64 |

## 2. Work management (Ch.3)

- **Work request → work order**: พนักงานแจ้งปัญหาเป็น work request, หัวหน้างานอนุมัติ/พัก/ปฏิเสธ, อนุมัติแล้ว link เข้า work order (1-3, 7-18)
- **ประเภท work order**: Routine (3-7) · Preventive Maintenance (3-12) · **Rebuild** (3-13 — เกิดอัตโนมัติเมื่อเอา rebuildable item ใส่กลับ) · Easy (3-18 — สร้างเป็น Released เลย ข้าม Draft)
- **Lifecycle**: `Draft → Released → Complete → Closed` (ดู 3-19) — ที่ Draft จอง/เบิกของและ charge labor ไม่ได้; ข้อจำกัด: work order หลายใบของ asset activity เดียวกัน **ห้ามมีสถานะเดียวกัน**
- Operations & tasks (3-21) · material requirements (3-26) · resource requirements (3-31) · operation/WO completion (3-37, 3-40) · transact material/resource (3-45, 3-46) · Maintenance Workbench (3-49)

## 3. Preventive maintenance (Ch.4)

- **Meter** (4-3) → associate กับ asset (4-5) → บันทึกค่าวัด (4-7) หรือผ่าน interface (4-9)
- **PM Scheduling Definition** อยู่บนคู่ **Asset Number × Asset Activity** หรือบน **Asset Route** ใช้กติกา **runtime interval** และ **daytime interval**
- **PM Scheduler** สร้าง work order ล่วงหน้าเป็น "forecast" แล้ว planner จึง generate จริง (4-12, 4-18) · suppression activity ใช้ระงับงานที่ไม่ต้องการ (4-17)

## 4. บทที่เหลือ

- **Ch.5 Planning & Scheduling** — ใช้ Oracle Manufacturing Scheduling + MRP; Scheduler Workbench (5-3, 5-7)
- **Ch.6 Direct Item Procurement** — requisition/PO ส่งของตรงเข้า work order + accounting (6-2 … 6-14)
- **Ch.7 Self-Service Maintenance** — web UI: Home, Assets, Work Requests, Work Orders, Work Plans (7-2 … 7-25)

## 5. จุดที่เกี่ยวกับปัญหาของเรา (สำคัญ)

**eAM แยก "ประเภทงาน" ออกจาก "สาเหตุ" ชัดเจน** — ซึ่งเป็นสิ่งที่ทีมมักยุบรวมกันจนข้อมูลเพี้ยน:

- **Activity Type** = ชนิดของงานบำรุงรักษา: Inspection, Overhaul, Lubrication, Repair, Servicing, Cleaning — เอกสารระบุว่า *"should remain generic, and should not describe in detail the job to be done"* (2-48)
- **Activity Cause** = สาเหตุที่งานนี้เกิดขึ้น: Breakdown, Vandalism, Normal Wear, Settings (2-48)
- **Work Order type** = หมวดการดำเนินงาน: routine / PM / rebuild / easy (3-7 … 3-18)

→ เวลาจะแก้ปัญหา "technician เลือก WO type ผิดระหว่าง corrective / CBM / breakdown" ให้แยก 3 แกนนี้ใน CMMS ไม่ใช่ยัดรวมในฟิลด์เดียว: `WO type` (กระบวนการ) × `Activity Type` (ชนิดงาน) × `Activity Cause` (สาเหตุ) และเพิ่มแกนที่ 4 คือ **failure mode/mechanism ตาม ISO 14224** ซึ่ง eAM ไม่มีให้

**สิ่งที่ eAM ไม่มี (ต้องทำนอกระบบ):**
- ไม่มี taxonomy failure mode/mechanism แบบ OREDA/ISO 14224 — ต้องสร้าง lookup เองหรือ map เข้า activity cause (มีแค่ Breakdown/Wear/Vandalism/Settings ซึ่งหยาบเกินวิเคราะห์)
- ไม่มี reliability analytics (MTBF/Weibull/B10) — เก็บประวัติ work order และ meter แต่ไม่คำนวณ
- Collection plan ใช้เก็บ condition data ได้ แต่ไม่มี logic ตัดสินใจแบบ condition monitoring

**ข้อควรระวัง:** เอกสารปี 2002 ของ 11i — โมเดลข้อมูลหลักยังเหมือนเดิมใน R12 แต่หน้าจอ/เมนูเปลี่ยนไปมาก และ Oracle Cloud EAM ต่างกว่าเดิมมาก

## 6. วิธีอ้าง

`(eAM UG 11i ch.2 p.2-43)` — รูปแบบ `ch.N p.N-M` ตามเลขที่พิมพ์ท้ายหน้า; เปิด PDF ประกอบเมื่อต้องดูหน้าจอ/form layout

## ข้อสังเกต

- บางหน้าในเอกสารมีอักขระเพี้ยนจาก font encoding (เช่น `OracleΓ` แทน `Oracle®`, `的描述` ปนในต้นฉบับหน้า 3-19) — คงไว้ตามต้นฉบับ ไม่แก้เดา
- ไม่มี `## Triplets` เพราะเป็น raw source ไม่ใช่หน้า wiki (area ข)

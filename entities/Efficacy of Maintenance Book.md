---
title: Efficacy of Maintenance Book
created: 2026-11-09
updated: 2026-11-09
type: entity
tags: [eom, book, maintenance-management, cmms, budget, kpi, rcm, spare-parts]
sources: [efficacy-of-maintenance.md, maintenance-profit-maker.md, reliability-based-maintenance-management.md]
confidence: medium
contested: true
---

# สัมฤทธิผลของงานบำรุงรักษา (Efficacy of Maintenance) — หนังสือ

hub ของหนังสือ "สัมฤทธิผลของงานบำรุงรักษา (Efficacy of Maintenance)" ที่ ingest เข้า wiki เมื่อ 2026-11-09 หนังสือเล่มนี้เป็น **คู่มือสร้างระบบบริหารงานบำรุงรักษาทีละชั้น** ตั้งแต่คำศัพท์ไปจนถึงต้นทุนบริการ — ต่างจาก [[Maintenance Profit Maker Book]] ที่เน้นผลต่อกำไร และ [[Reliability Based Maintenance Management Book]] ที่เน้นทฤษฎี reliability

## บรรณานุกรม

- ชื่อ: สัมฤทธิผลของงานบำรุงรักษา (Efficacy of Maintenance)
- ผู้เขียน: สุพัฒน์ เชยศิริวัฒนนา, วัฒนา เชียงกูล, เกรียงไกร ดำรงรัตน์ (EOM p.3, p.6)
- สำนักพิมพ์: ซีเอ็ดยูเคชั่น (SE-EDUCATION), พ.ศ. 2556, ISBN (e-book) 978-616-08-1054-3, เลขหมู่ 658.202, ชุด Industrial Management and Technical Series (EOM p.3)
- 360 หน้า, 17 บท (EOM p.4-11)
- raw: [[raw/efficacy-of-maintenance]] + reading notes ใน `raw/efficacy-of-maintenance/` (ข้อความเต็ม OCR เก็บในเครื่องเท่านั้น เพราะมีลิขสิทธิ์)
- การอ้างอิง: `(EOM p.NN)` ด้วย printed page

## แก่นของเล่ม

- งานบำรุงรักษาเป็น **ระบบบริหาร 6 ชั้น** ([[Maintenance Efficacy Pyramid]]) และ "ข้ามขั้นไม่ได้" — RCM/optimization จะไร้ความหมายถ้ายังไม่มีประวัติ ระบบควบคุมงาน และต้นทุนที่ถูกต้อง (EOM p.298-299)
- แกนที่วิ่งผ่านทุกบทคือ **criticality 4 ระดับ** (EOM p.73-77) ใช้กำหนดกิจกรรม PM (บทที่ 5), อะไหล่สำรอง (บทที่ 9), การจ้างเหมา (บทที่ 10)
- ทุกบทจบที่ "ระบบย่อยต้องมีเป้าหมายและผลลัพธ์อะไร" ไม่ใช่แค่ความรู้ — ทำให้ใช้เป็น checklist ประเมินโรงงานได้

## แผนที่บท -> หน้า wiki

| บท | Book pages | หัวข้อหลัก | หน้าใน wiki |
|---|---|---|---|
| 1 | 13-30 | คำศัพท์ 5 กลุ่ม | หน้านี้, [[CMMS]] |
| 2 | 31-52 | 4 กลุ่มงาน 16 กิจกรรม, ME 5 หน้าที่ | [[Maintenance Business Models]], [[RCM Reliability Centered Maintenance]] |
| 3 | 53-68 | โครงสร้าง 5 แบบ, นโยบายเชิงยุทธศาสตร์ | โครงสร้างหน่วยงานบำรุงรักษา, หน้านี้ |
| 4 | 69-80 | ทะเบียน, criticality 4 ระดับ, เอกสาร | [[Criticality Assessment]], [[CMMS]] |
| 5 | 81-94 | ตารางกิจกรรม x ระดับความสำคัญ | [[Maintenance Planning and Scheduling]] |
| 6 | 95-110 | PM-Program, กฎการทับซ้อน, 12 สัปดาห์ | [[Maintenance Planning and Scheduling]] |
| 7 | 111-126 | Work Control 6 ขั้น + backlog | [[Work Order Lifecycle]] |
| 8 | 127-148 | Planned Outage 3 package | [[Turnaround Management]] |
| 9 | 149-170 | อะไหล่ demand/supply, insurance vs necessary | [[Spare Parts Management]], [[Spare Part Criticality and Risk]] |
| 10 | 171-192 | จ้างเหมา 5 ระดับความรับผิดชอบ | [[Maintenance Outsourcing]] |
| 11 | 193-220 | งบ 3 กลุ่ม, FFCR, absorption | [[Maintenance Budget]] |
| 12 | 221-244 | MMMP 9+7 แผน, 3 ระดับความเร่งด่วน | [[Maintenance Master Plan]] |
| 13 | 245-254 | ระบบย่อย 7 ระบบ, ตัวอย่างรายงาน | [[Maintenance KPIs]], หน้านี้ |
| 14 | 255-274 | CMMS: ประโยชน์ เลือก ขึ้นระบบ | [[CMMS]] |
| 15 | 275-312 | สมรรถนะ 6 ระดับ + เงื่อนไขขึ้นชั้น | [[Maintenance Efficacy Pyramid]] |
| 16 | 313-350 | Optimization, RCM 3 ขั้น, C(tp), อะไหล่ | [[RCM Reliability Centered Maintenance]], [[Weibull Analysis]] |
| 17 | 351-366 | ABC เต็มรูปแบบสำหรับธุรกิจบริการ | [[Maintenance Budget]], หน้านี้ |

## สิ่งที่เล่มนี้เพิ่มจากเล่มอื่นในชุด

- **ตารางกิจกรรม PM x criticality** (รูปที่ 5.2, EOM p.84) — policy matrix ที่ implement ใน CMMS ได้ตรง ๆ ไม่มีใน MPM/RBMM
- **กฎแก้ตารางทับซ้อน C > B > A** (EOM p.100) — หลักปฏิบัติที่หาไม่ได้ในเล่มอื่น
- **ขอบเขตผู้รับเหมา = จำนวนขั้นของ Work Control ที่โอน** (EOM p.173) — กรอบเจรจาสัญญาที่ใช้ได้จริง
- **FFCR + over/under absorption** พร้อมตัวอย่างรายงานครบ (EOM p.205-207, p.253)
- **MMMP 9 แผนเทคนิค + 7 แผนระบบจัดการ พร้อมลำดับความเร่งด่วน 3 ชั้น** (EOM p.223-224) — CMMS อยู่ชั้นสาม ซึ่งอธิบายว่าทำไม "ซื้อ CMMS ก่อน" ล้มเหลว
- **เงื่อนไขขึ้นชั้นของพีระมิด** (EOM p.277-300) — พีระมิดที่ RBMM/MPM วาดไว้ ที่นี่บอกว่า "ต้องมีอะไรจึงจะขึ้นได้"
- **สูตร C(tp)** พร้อมนิยาม M(tp) (EOM p.342) และเงื่อนไขความสำเร็จ 6 ข้อ (EOM p.341)

## ข้อขัดแย้ง / ข้อสังเกต

- **ชื่อผู้นำ**: หน้าลิขสิทธิ์ "สุพัฒณ์ เซียศิริวัฒนา" vs บรรณานุกรมหอสมุด "สุพัฒน์ เชยศิริวัฒนนา" (EOM p.3, p.6) [contested:: true]
- **ชื่อชั้นที่ 3 ของพีระมิด**: EOM ใช้ "Maintenance Systematic Work Control" (p.279) ขณะที่ RBMM ใช้ "Maintenance Work Control" — ชั้นเดียวกัน ชื่อต่าง [contested:: true]
- **ขอบเขต RCM**: EOM ระบุชัดว่ารูปที่ 16.3 "ไม่มีการทำ Optimization และ CMMS" (p.320) ขณะที่ PETROSYNC วาง RCM เป็น process model 11 กล่องรวม business goals และ living program — EOM มอง RCM แคบกว่า (เป็นกระบวนการเลือกงาน)
- **OEE กับต้นทุนต่อหน่วย**: ตัวอย่าง p.253 ให้ Line 3 มี OEE ต่ำสุด (82.79%) แต่ต้นทุนต่อหน่วยต่ำสุด (9.90) เพราะ plan factor 100% — เตือนว่าอย่าใช้ OEE เดี่ยว ๆ ตัดสินต้นทุน
- ตัวเลขทุกตัวในบทที่ 11, 13, 15, 16 เป็นตัวอย่างสมมติของผู้เขียน

## Triplets

- [[Maintenance Efficacy Pyramid]] [defined_in:: [[Efficacy of Maintenance Book]]] chapter 15
- [[Maintenance Budget]] [defined_in:: [[Efficacy of Maintenance Book]]] chapter 11
- [[Maintenance Master Plan]] [defined_in:: [[Efficacy of Maintenance Book]]] chapter 12
- [[Turnaround Management]] [defined_in:: [[Efficacy of Maintenance Book]]] chapter 8
- [[Maintenance Outsourcing]] [defined_in:: [[Efficacy of Maintenance Book]]] chapter 10
- [[Spare Parts Management]] [defined_in:: [[Efficacy of Maintenance Book]]] chapter 9
- [[CMMS]] [defined_in:: [[Efficacy of Maintenance Book]]] chapter 14
- [[RCM Reliability Centered Maintenance]] [defined_in:: [[Efficacy of Maintenance Book]]] chapter 16
- [[Work Order Lifecycle]] [defined_in:: [[Efficacy of Maintenance Book]]] chapter 7
- Spare Part Service Factor [has_value:: >98%] EOM p.250
- Spare Part Turnover [has_value:: >50%, satisfactory ~100%] EOM p.250
- Maintenance Full Fixed Cost Rate [has_formula:: full fixed cost / total man-hours] EOM p.205-207
- Optimal Replacement Interval [has_formula:: C(tp) = [Cp*R(tp)+Cf*(1-R(tp))] / [tp*R(tp)+M(tp)*(1-R(tp))] ] EOM p.342
- Maintenance Systematic Work Control [differs_from:: Maintenance Work Control] naming, EOM p.279 [contested:: true]
- [[RCM Reliability Centered Maintenance]] [contradicts:: PETROSYNC RCM process model] EOM scopes RCM to task selection, no optimization/CMMS (Fig 16.3), EOM p.320 [contested:: true]

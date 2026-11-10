---
title: Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)
created: 2026-11-10
updated: 2026-11-10
type: concept
tags: [maintenance-strategy, rcm, sil, rbi, cbm, cmms, spares, internal-standard]
sources: [valeura-maintenance-strategy-kpp-0001.md]
confidence: high
contested: false
---

# Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)

ชั้นกลางของระบบเอกสาร Valeura: [[Valeura Maintenance Philosophy]] บอก *ทำให้ได้อะไร* → **เอกสารนี้บอกว่าจะสร้าง maintenance program ด้วยเครื่องมืออะไร** → [[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]] วัดผล

Rev **R2 (พ.ค. 2023)**; ขอบเขต: process & utility equipment บน topside ตั้งแต่ downstream ของ X-mas tree ถึง export valve

## 1. หลักการและวัตถุประสงค์

Strategy = กระบวนการ **optimize แบบ risk-based** จากความสำคัญของ equipment และ consequence ของ failure ไม่ใช่การทำ PM ให้ครบทุกตัว

วัตถุประสงค์ 6: ลดต้นทุนโดยตัดงานที่ไม่สร้างคุณค่าและโฟกัสงาน critical | เพิ่ม availability ด้วยการกำจัด breakdown ของเครื่องหลัก | บริหาร/optimize สต็อกอะไหล่ | คุ้มครอง ESG | ยืดอายุเครื่องด้วยการตรวจจับแต่เนิ่น ๆ | trade-off ระหว่างเงินลงทุน life cycle กับอายุแหล่งผลิต

หลักที่ตามมา: ต้องมี roles/authority ชัด, แลกเปลี่ยน best practice ข้าม facility, ใช้ KPI โฟกัส critical success factor, audit ภายใน/ภายนอกเป็นระยะ, และป้อนข้อมูลวิกฤตทั้งหมดลง CMMS

## 2. เมนูเครื่องมือ — ใช้อะไรกับอะไร

| เครื่องมือ | ใช้กับ | ผลลัพธ์ |
|---|---|---|
| **OEM maintenance manual** | ขั้นต่ำของทุกเครื่อง; เป็น strategy หลักของ criticality ต่ำ | PM program ตามผู้ผลิต |
| **Criticality assessment** | ทุก equipment | ระดับความเข้มของ program + เหตุผลของ run-to-failure |
| **RCM** | SCE / high criticality โดยเฉพาะ **rotating equipment** | task ที่มักเป็น CBM แทน PM แบบเดิม |
| **SIL** | instrument-based protective systems (SIF loop) | proof-test interval, loop test, ESD cause & effect, SDV stroke/closure time |
| **RBI (API 580)** | static: topside piping, pressure vessel, storage tank | แผนตรวจตามความเสี่ยง loss of containment |
| **Structural integrity management** | topside, platform, subsea structure | แผนตรวจโครงสร้าง |
| **CMMS (Oracle)** | ทั้งองค์กร | ควบคุมงาน วัสดุ ต้นทุน จัดซื้อ + ประวัติ |
| **Condition monitoring program** | ทุก facility ที่จำเป็น | CBM |
| **RCFA** | failure ซ้ำ หรือ failure เดี่ยวที่ consequence สูง | แก้ strategy / modify / design out |
| **Onshore support** | CMMS master data, overhaul, turnaround, contracts | คุณภาพข้อมูลและงานวิศวกรรม |
| **Criticality-based critical spares** | อะไหล่ที่ consequence สูง | ระบุ critical/insurance spare |
| **Inventory optimization** | ทั้งคลัง | ลดต้นทุนโดยไม่เพิ่ม downtime/backlog |

## 3. OEM manual และ warranty

ช่วง **warranty ใช้คู่มือผู้ผลิตเป็นขั้นต่ำ** เพื่อไม่ให้เสียสิทธิ์เคลม — และ equipment criticality ต่ำสามารถใช้ strategy นี้ต่อได้เลยเพราะใช้แรงน้อยในการพัฒนาแผน ส่วนความพยายามเชิงลึก (RCM ฯลฯ) **สงวนไว้ให้ SCE/high เท่านั้น**

## 4. Criticality → run-to-failure → complete spare set

ถ้าต้นทุน consequence ของการเสีย **ต่ำกว่าต้นทุนบำรุงรักษา** ใช้ run-to-failure เพื่อเก็บกำลังคนไว้กับงาน critical — และผล criticality อาจนำไปสู่การถือ **อะไหล่ครบชุด** ถ้าคุ้ม (เช่นเครื่องที่ซ่อมหน้างานไม่ได้)

## 5. RCM / SIL / RBI

- **RCM**: สำหรับเครื่องซับซ้อนที่เสี่ยงสูง — ศึกษา failure mechanism และหาว่าป้องกันอย่างไร; เหมาะกับ rotating; ผลลัพธ์เอียงไปทาง CBM ดู [[RCM Reliability Centered Maintenance]] และ [[PM Task Selection]]
- **SIL**: กำหนดระดับ reliability ของ protective device → ขับการจัดซื้อตอน project และ proof-test interval ตอน operate; input device ใช้ loop test + calibration ตาม SIL verification; controller ทดสอบ ESD cause & effect; final element (SDV) ทำ stroke test + วัด closure time
- **RBI**: dynamic, อัปเดตตามสภาวะ_processและประวัติ; เป้าวิเคราะห์ loss of containment จาก corrosion/material loss; มาตรฐานอ้างอิง **API 580**; ขอบเขต piping/vessel/tank

## 6. CBM — งานที่บริษัทให้น้ำหนักที่สุด

"CBM คือ **preferred maintenance task**" เพราะลด man-hour, ลดอะไหล่สำหรับ intrusive inspection และลด downtime พร้อมจับสภาพจริงได้ก่อน catastrophic

เทคนิคที่ใช้: oil analysis, vibration, thermography, **motor current analysis**, performance monitoring — เลือกตาม failure mode ที่คาด ดู [[Condition Monitoring Techniques]], [[P-F Interval and Condition Monitoring]]

## 7. CMMS ต้องมีอะไร

1. **Asset register** ครบตาม P&ID (รวม package P&ID)
2. **Asset criticality** ทุกตัว
3. **Planned PM** — task, interval, spare, manpower ต่อ equipment
4. **BOM 2 ระดับ: equipment BOM + activity BOM** — เพื่อให้ WO ที่ออกจาก standard activity ผูกวัสดุอัตโนมัติ และพยากรณ์การใช้วัสดุล่วงหน้าเพื่อต่อรองราคา/ซื้อแบบ bulk

ข้อ 4 สำคัญต่อการออกแบบข้อมูล: ถ้า BOM ผูกที่ activity ไม่ใช่แค่ equipment จะทำให้ material planning แม่นและต้นทุนลงถูก activity ดู [[CMMS]] และ [[Work Order Lifecycle]]

## 8. RCFA

ใช้กับ failure ซ้ำหรือ consequence สูง; เครื่องมือ 5 Whys, fault tree, incident timeline; ผลลัพธ์ 3 ทาง: เปลี่ยน maintenance strategy, modify equipment, หรือ design out — ตัดสินด้วย risk เทียบเงินลงทุน ดู [[Root Cause Analysis]]

## 9. การวางแผนและควบคุมงาน

- ทุกงานต้องมี **WO + อนุมัติจาก maintenance supervisor** ก่อนลงมือ; ปิดงานโดยช่างแล้ว supervisor verify; วัสดุเบิกจาก WO เท่านั้น (ทั้ง stock และ direct purchase)
- ทบทวน look-ahead **30 วันและ 90 วัน** เพื่อจับงานที่ต้องใช้ external resource/long-lead spare และ refine ตาราง **7 วัน**
- เป้า **planned work overdue = 0 %** ของงานวางแผนทั้งหมด (เข้มกว่า KPI ใน KPP-0002 ที่ยอม 1–3 %)

## 10. อะไหล่

- อะไหล่ที่อยู่ใน **PM program ต้องเป็น stock item** และตั้ง min-max จาก **consumption rate ที่ simulate จาก look-ahead ใน CMMS**
- อะไหล่นอก PM: ตัดสินจาก failure mode + criticality + ประวัติ CMMS + RCM + RCFA + vendor
- **ไม่มี workshop offshore** → assembly ต้องส่งซ่อม onshore ที่ร้าน contractor และต้องมี **swing unit ครบชุด** ระหว่างรอ: crane winch, crane luffing cylinder, process/utility pump, diesel engine, **electrical generator**, engine radiator, fuel pump, water pump

## 11. SCE / Pre-ORR / onshore support / people

- **SCE:** master register ใน CMMS ต้องตรงกับ SCE identification report; ผลงานรายเดือนเข้า asset KPI; เลื่อน/ยกเว้นงานต้องอนุมัติ + risk assessment ผ่าน deviation control ดู [[Safety Critical Failure Classification]]
- **Pre-startup audit (Pre-ORR)** 13 หัวข้อ: strategy, competency, CMMS, planning & scheduling, resource leveling, KPI, contracts, availability target, CI process, failure investigation, spares, HSE compliance, audit program — ผู้ตรวจต้องเป็น maintenance professional ที่เป็นอิสระจากทีม offshore
- **Onshore support:** troubleshoot, ป้อน best practice เข้า CMMS, overhaul/refurbish, วางแผนงาน major, campaign maintenance, turnaround, และ **เป็นเจ้าของ maintenance contracts**
- **People:** competency matrix + refresh/ใบรับรองสำหรับงานเสี่ยงสูง

## 12. ข้อสังเกตและช่องว่าง

1. **KPI list ในต้นฉบับขาดกลางคัน** — จบที่ "Maintenance cost," ต้องใช้[[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]] เป็นรายการอ้างอิงแทน
2. **ไม่มีวิธีเลือก task ระดับ failure mode** — เอกสารนี้เป็นกรอบ "ใช้เครื่องมือไหนกับ equipment กลุ่มไหน" ไม่ใช่ขั้นตอน RCM; ต้องใช้ [[PM Task Selection]]
3. **min-max จาก look-ahead 90 วัน** ไม่ใช่ consumption history — สำหรับ slow-moving part วิธีนี้ให้ค่าต่ำเกินจริง เพราะ look-ahead ไม่มีข้อมูลความต้องการระยะยาว ควรใช้ Poisson/MTBF ตาม [[Min-Max Stock Policy for Slow-Moving Spares]] หรือแยกสองวิธีตาม [[Maintenance Inventory Control SOP (TH-GEN-PROD-162)]]
4. **swing unit ≠ rotable pool** — เอกสารกำหนดชุดสำรองสำหรับ assembly ที่ส่งซ่อม แต่ไม่ได้กำหนดจำนวน pool, repair lead time หรือ rotable tracking
5. **เป้า overdue 0 %** ในเอกสารนี้ขัดกับ tolerance 1–3 % ใน KPP-0002 — ใช้ 0 % เป็น aspiration และ 1–3 % เป็นเกณฑ์ให้คะแนน; ต้องระบุให้ชัดในรายงานรายเดือน
6. ไม่มีตัวเลขความถี่ CBM หรือ interval ของ RBI — อยู่ใน procedure/study เฉพาะ
7. ไม่กล่าวถึง spare criticality C1/C2/NC — อยู่ที่ SOP 162

## ดูเพิ่ม

- [[Valeura Maintenance Philosophy]] — นโยบายแม่บท
- [[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]] — ตัววัด
- [[Criticality Assessment]] — วิธีจัดระดับ
- [[RCM Reliability Centered Maintenance]], [[PM Task Selection]]
- [[Condition Monitoring Techniques]], [[P-F Interval and Condition Monitoring]]
- [[CMMS]], [[Work Order Lifecycle]], [[Maintenance Planning and Scheduling]]
- [[Spare Parts Management]], [[Maintenance Inventory Control SOP (TH-GEN-PROD-162)]]
- [[Root Cause Analysis]]

## Triplets

- [[Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)]] [applies_to:: [[Valeura Maintenance Philosophy]]] implements the policy of PHI-0001
- [[Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)]] [has_value:: 14] strategic processes from OEM manual to inventory optimization
- [[Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)]] [uses:: [[RCM Reliability Centered Maintenance]]] for SCE and high criticality rotating equipment
- [[Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)]] [uses:: [[Condition Monitoring Techniques]]] CBM is the preferred task type
- [[Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)]] [depends_on:: [[CMMS]]] asset register, criticality, PM plan and two-level BOM
- [[Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)]] [has_value:: 0] percent planned work overdue target, stricter than KPP-0002 tolerance
- Swing unit [applies_to:: electrical generator] complete spare assembly held while failed unit is refurbished onshore
- [[Valeura Maintenance Strategy (TH-GEN-MT-GE-KPP-0001)]] [differs_from:: [[ARMS KPI Standard (TH-GEN-MT-GE-KPP-0002)]]] 0 percent overdue aspiration versus 1-3 percent scoring band

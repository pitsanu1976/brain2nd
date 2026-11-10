---
title: Maintenance Inventory Control SOP (TH-GEN-PROD-162)
created: 2026-11-10
updated: 2026-11-10
type: concept
tags: [spare-parts, inventory, min-max, criticality, service-level, kpi, internal-policy]
sources: [maintenance-inventory-sop-162.md]
confidence: high
contested: false
---

# Maintenance Inventory Control SOP (TH-GEN-PROD-162)

หน้าสรุป **นโยบายภายในองค์กร** สำหรับควบคุมอะไหล่คงคลัง (SOP เลขที่ TH-GEN-PROD-162-REP-0001 Rev 2, Thailand Production) ใช้เป็น "กติกาองค์กร" ประกอบกับหลักวิชาจาก [[Spare Parts Management]], [[Spare Part Criticality and Risk]] และ [[Min-Max Stock Policy for Slow-Moving Spares]]

**ลำดับการใช้:** จัดชั้น criticality (§5.1) → ตัดสินว่าจะสต็อกหรือไม่ (§5.3) → ตั้ง Min/Max + SS (§5.2, §5.4) → เลือก control model (§5.5) → วัดผล (§5.6)

## 1. จัดชั้นอะไหล่ 3 ระดับ (§5.1)

| Code | ชั้น | เกณฑ์ตัดสิน | Asset criticality link | Stocking strategy |
|---|---|---|---|---|
| **C1** | Critical-Vital | ทำให้สูญเสีย production ทันทีและรุนแรง หรือทำให้การทำงานไม่ปลอดภัย — **ยอมรับความเสี่ยง stock ไม่ได้** | SCE / High | safety stock บังคับ |
| **C2** | Critical-Essential | กระทบ continuous operation แต่ยอมรับความเสี่ยงได้เมื่อมี spare capacity / design redundancy หรือ production loss ไม่สูง | High / Medium | stock required โดยเฉพาะ lead time > 3 เดือน |
| **NC** | Non-Critical | ไม่กระทบการทำงานทันที ไม่มีความเสี่ยง safety | Low | ไม่มี safety stock → OAR |

ตัวอย่างใน SOP: C1 = ESD, F&G, NAV-AID, crane, closed drain (ไม่มี redundancy), flare & vent, DCS/PLC controller ไม่มี redundancy, main switchgear, main UPS; C2 = air compressor, **generator**, crude pump, water injection, HVAC, choke valve, electrical distribution, diesel storage; NC = general consumables, tools

**ข้อควรระวังที่ต้องใช้ดุลยพินิจ:** link นี้เป็นค่า default ระดับ equipment — generator อยู่ใน C2 แต่ถ้าเป็น emergency generator ที่จ่ายไฟให้ SCE (ESD/F&G/nav aids/emergency lighting) และไม่มีเครื่องสำรอง ต้องยกเป็น C1 ตามเกณฑ์ "main process equipment without standby" ดู [[Criticality Assessment]]

## 2. ตัดสินว่าจะสต็อกหรือไม่ (§5.3)

| # | เงื่อนไข | การตัดสิน |
|---|---|---|
| 1 | ซ่อมได้โดยไม่ต้องใช้ part นี้ | ไม่สต็อก |
| 2 | NC — ไม่กระทบ production/safety/environment | ไม่สต็อก → OAR |
| 3 | มี standby ที่ทำงานแทนได้ (redundancy) | ไม่สต็อก เว้นแต่ LT > 3 เดือน (ตอน standby ทำงานจะไม่มีตัวสำรอง) |
| 4 | LT ยาวกว่า P–F interval (ตรวจจับไม่ทันก่อนเสีย) | สต็อก |
| 5 | กระทบ production/safety/environment (C1 หรือ C2 ไม่มี redundancy) | สต็อก |

### โซนตาม cost ratio (§5.3)

| โซน | เงื่อนไข | การกระทำ |
|---|---|---|
| Mandatory stock | cost ratio > ~9 | สต็อกได้โดยไม่ต้องอนุมัติเพิ่ม |
| Stock with approval | cost ratio ~1–9 | สต็อกตามระดับที่ policy กำหนด แต่อนุมัติ |
| No stock | cost ratio ≤ 1 (holding ≥ stock-out) | ไม่สต็อก |
| Insurance | cost ratio ≤ 1 แต่ loss จาก stock-out ครั้งเดียวรับไม่ได้ | สต็อกแบบ insurance spare + อนุมัติ management |

หลักการเดียวกับ [[Spare Part Criticality and Risk]] หัวข้อ Cost Ratio (RBMM p.246-251) แต่ SOP ล็อกตัวเลขโซนไว้ใช้ปฏิบัติ

## 3. Safety stock และ service level (§5.4)

| ชั้น | Target service level | z |
|---|---|---|
| C1 | 95 % – 99.5 % | 1.645 – 2.576 |
| C2 | 90 % – 95 % | 1.282 – 1.645 |
| NC | ไม่มี safety stock (OAR) | – |

- **Fixed default** ในตาราง Min-Max: C1 = 1, C2 = 1, NC = 0 ชิ้น — ใช้เฉพาะเมื่อยังไม่มีประวัติ
- **Statistical SS** เมื่อมีประวัติ ≥ 3 ปี: `σc = √(σD²·LT + (σLT·D)²)`, `SS = z·σc`, `Min/ROP = D·LT + SS` — วิธีเดียวกับ [[Spare Part Criticality and Risk]] (RBMM) และ [[EOQ and Reorder Point]]
- ช่วง SL กว้าง (C1 ต่างกันถึง 4.5 จุด) — **ต้องเลือกจาก consequence** (production loss ต่อชั่วโมง, safety) ไม่ใช่หยิบกลางช่วง

### วิธีพยากรณ์ตามกลุ่มอะไหล่ (§5.4)

| กลุ่ม | วิธี |
|---|---|
| Fast moving | ค่าเฉลี่ย + ส่วนเบี่ยงเบน (normal), ROP + statistical SS, EOQ |
| Slow moving + criticality ต่ำ | ค่าเฉลี่ยจาก MTBF หรือ Poisson ตาม target SL |
| Slow moving + criticality กลาง | Poisson หรือ simulation + cost ratio |
| Criticality สูง | Reliability analysis (failure mode, Weibull) ผูกกับแผน PM + risk-based / insurance spare |

ตารางนี้คือคำตอบเชิงนโยบายของคำถาม "ควรใช้ Poisson เมื่อไร" — Poisson ใช้กับ slow-moving ที่ criticality ไม่สูงถึงขั้นต้องวิเคราะห์ reliability เชิงลึก ดู [[Min-Max Stock Policy for Slow-Moving Spares]] และ [[Spare Part Demand Forecasting]]

## 4. Min-Max (§5.2 — Rev 2)

สรุปสูตรที่ใช้ (รายละเอียดและตัวอย่างคำนวณอยู่ใน [[Min-Max Stock Policy for Slow-Moving Spares]]):

- `P = LT + R` (protection interval = lead time + review period)
- `Min = CEILING(D_P + SS, 1)` สำหรับ demand ที่รู้แน่ (PM BOM) หรือ `Min = k` โดย `P(X≤k) ≥ CSL` สำหรับ Poisson
- `Max = Min + Q` โดย `Q = MAX(MOQ, EOQ)` ปัดขึ้นเป็นจำนวนเท่าของ pack

**สิ่งที่ Rev 1 ทำผิดและ Rev 2 แก้:** `MAX = MAX(SS + PM usage × LT, MOQ)` ทำให้ Max ≤ Min ได้ (ไม่เหลือจำนวนให้สั่ง) และใช้ LT เดี่ยวซึ่งขาด demand ช่วง review period — องค์กรที่ยังใช้ Rev 1 อยู่ต้องแก้ก่อนใช้ตั้งค่าใน CMMS

## 5. Control model ตาม movement × cost (§5.5)

| โซน (movement–cost) | โมเดล |
|---|---|
| Fast-High, Fast-Medium, Medium-High | Perpetual inventory: ROP + EOQ (continuous review) |
| Fast-Low, Medium-Medium | Min-Max + blanket order (ลดภาระสั่งซื้อ) |
| Medium-Low, Slow-Medium, Slow-Low | Two-bin (bin สำรอง = ROP) |
| Slow-High | Issue replacement (one-for-one) ตามจำนวนติดตั้ง |

## 6. KPI (§5.6)

| KPI | สูตร | เป้า |
|---|---|---|
| Service level (line fill rate) | line items issued in full ÷ requested × 100 | ≥ 95 % รวม, ~100 % สำหรับ C1 |
| Stock-out rate | qty not available ÷ qty requested × 100 | ≤ 1 % |
| Stock turnover | annual issue value ÷ average stock value | ดู trend (MRO หมุนช้า — เทียบ like with like) |
| Inventory value % GPI | stock value ÷ GPI × 100 | ≤ 4 % (SPO), 1–3 % (RBMM) |
| Months of supply | stock value × 12 ÷ annual issue value | ดู trend ตาม item class |
| Inactive stock | มูลค่าที่ไม่มีการเบิก 12 เดือน ÷ มูลค่าสต็อก | ลดลง (ยกเว้น insurance/long-lead) |
| Emergency purchase ratio | urgent PO ÷ PO ทั้งหมด × 100 | ลดลง |

นิยาม GPI ใน SOP = มูลค่าปัจจุบันของสินทรัพย์ผลิต (ไม่รวมที่ดินและอาคาร) ตรงกับ [[Inventory Turnover and GPI Benchmarks]]

## 7. บทบาทและขั้นตอน (§5.8, §6)

- **ขั้นตอน:** new stock item request → criticality review (Discipline Engineer, Review 2, เป็นผู้กำหนด C1/C2/NC) → คำนวณ Min/Max → RFQ/quotation → อนุมัติ → ตั้งค่าใน Oracle → ทบทวนตามรอบหรือเมื่อ lead time/MOQ/PM BOM เปลี่ยน
- **บทบาท:** Requester/Planner (ตั้งเรื่องและคำนวณ), Warehouse (รับเข้า-เบิก), Procurement (RFQ, expedite C1/long-lead), Discipline Engineer (criticality), Management (อนุมัติ insurance spare)
- เอกสารอ้างอิงภายใน: Oracle CMMS เป็นระบบที่ตั้ง Min/Max และออก PR อัตโนมัติเมื่อถึง Min — ดู [[CMMS]] และ [[Failure Hierarchy]]

## 8. ข้อจำกัดของ SOP

- เป็น **procedure ภายใน** ไม่ใช่มาตรฐาน — ใช้เป็นนโยบายองค์กร ไม่ใช่หลักฐานเชิงวิศวกรรม; เมื่อขัดกับ ISO/RBMM ให้บันทึกว่าเป็น company deviation
- ไม่ครอบ **rotable/repairable pool** — อะไหล่ซ่อมได้ต้องใช้จำนวน pool + repair lead time ไม่ใช่ Min-Max
- Fixed SS default (1/1/0) หยาบกว่าวิธี statistical มาก; เสี่ยง stock-out กับ C1 ที่ lead time ยาว
- SL เป็นช่วง ไม่ได้กำหนดค่าต่อ item — การเลือกค่าจริงยังขึ้นกับดุลยพินิจและการอนุมัติ
- ไม่มีข้อกำหนดเรื่อง **การทบทวนหลังเปลี่ยน lead time/MOQ** เป็นรอบเวลา (เขียนไว้แบบ general) — ควรผูกกับ KPI inactive stock และ emergency purchase ratio

## ดูเพิ่ม

- [[Spare Parts Management]] — ภาพรวมเชิงกลยุทธ์
- [[Spare Part Criticality and Risk]] — หลัก Cost Ratio / Confidence Level ที่ SOP อ้าง
- [[Min-Max Stock Policy for Slow-Moving Spares]] — สูตรและตัวอย่างคำนวณ
- [[MRO Inventory Control Methods]] — ROP/EOQ, periodic review, OAR
- [[Inventory Turnover and GPI Benchmarks]] — KPI และ benchmark
- [[Spare Part Demand Forecasting]] — วิธีพยากรณ์เชิงลึก
- [[Criticality Assessment]] — criticality ระดับ equipment

## Triplets

- [[Maintenance Inventory Control SOP (TH-GEN-PROD-162)]] [applies_to:: [[Spare Parts Management]]] นโยบายภายในของ Thailand Production, Rev 2
- [[Maintenance Inventory Control SOP (TH-GEN-PROD-162)]] [has_category:: internal-procedure] ไม่ใช่มาตรฐานภายนอก
- C1 spare criticality [depends_on:: asset criticality SCE/High] safety stock บังคับ
- C2 spare criticality [depends_on:: asset criticality High/Medium] stock required, especially LT > 3 months
- [[Maintenance Inventory Control SOP (TH-GEN-PROD-162)]] [uses:: [[Min-Max Stock Policy for Slow-Moving Spares]]] สูตร Min = D_P + SS หรือ Poisson k, Max = Min + Q
- Service level [depends_on:: spare criticality] C1 95-99.5%, C2 90-95%, NC no safety stock

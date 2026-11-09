---
title: Min-Max Stock Policy for Slow-Moving Spares
created: 2026-11-09
updated: 2026-11-09
type: concept
tags: [spare-parts, inventory, poisson, min-max, slow-moving, cmms, reliability]
sources: [gemini-minmax-poisson.md, reliability-based-maintenance-management.md, spare-parts-optimization.md, maintenance-profit-maker.md]
confidence: medium
contested: false
---

# Min-Max Stock Policy for Slow-Moving Spares

วิธีกำหนด Min/Max ของอะไหล่ที่เบิกน้อยและไม่สม่ำเสมอ (slow-moving / intermittent demand) ซึ่งสูตร ROP แบบ normal approximation ใน [[EOQ and Reorder Point]] ใช้ไม่ได้ เพราะ demand เป็นจำนวนเต็มและมีช่วงที่เป็นศูนย์หลายช่วง และมีการเบิกเป็นศูนย์หลายช่วง — ใช้ **Poisson** แทน

หน้านี้สรุปจาก transcript [[raw/gemini-minmax-poisson]] (AI conversation) แล้ว **ตรวจตัวเลขซ้ำด้วย Python** และเพิ่มส่วนที่ transcript มองข้าม (protection interval, CSL vs fill rate, การประมาณ λ)

## 1. เลือกวิธีตาม demand pattern ก่อน

| Pattern | เกณฑ์แยก | วิธีคำนวณ | Min (ROP) | Max |
|---|---|---|---|---|
| **Deterministic** | ผูก PM BOM / แผนผลิต รู้จำนวนต่อรอบ | `LTD = usage rate × protection interval` | LTD + เผื่อความล่าช้าของแผน | Min + lot size |
| **Intermittent** | corrective ล้วน, λ < ~5 ครั้ง/ปี, เบิกเป็นจำนวนเต็ม | Poisson | k ต่ำสุดที่ `P(X ≤ k) ≥ CSL` | Min + order quantity |
| **Mixed** | ใช้ทั้ง PM และ CM | Shifted Poisson | `D_PM + k_Poisson(λ_corr)` | Min + order quantity |
| **Insurance / capital** | ราคาสูงมาก อัตราเสีย < 1 ครั้ง/5-10 ปี | Risk-based / newsvendor (ไม่ใช้ Poisson) | 0 หรือ 1 ตาม downtime cost | เท่ากับ Min |
| **Repairable (rotable)** | ซ่อมกลับได้ | Rotable pool + repair lead time | จำนวน pool ไม่ใช่ stock ใหม่ | pool size |

- **Insurance spare** ให้ใช้กรอบเดียวกับ [[Spare Part Criticality and Risk]] และ [[Spare Parts Management]] — เทียบ holding cost กับ downtime cost ไม่ใช่คำนวณจาก λ
- อะไหล่ที่ซ่อมได้ (seal, valve, pump ที่ส่งซ่อม) ไม่ควรใช้สูตรนี้ตรง ๆ เพราะของกลับเข้าคลังได้หลัง repair lead time

## 2. Poisson — ขั้นตอนและตัวอย่าง

`P(X = k) = e^(−λ) · λ^k / k!` โดย λ = ความต้องการเฉลี่ย **ในช่วงป้องกัน** (protection interval)

ตัวอย่าง: mechanical seal, λ = 0.4 ต่อ lead time 3 เดือน, CSL 95%

| k | P(X = k) | P(X ≤ k) |
|---|---|---|
| 0 | 0.6703 | 67.03% |
| 1 | 0.2681 | 93.84% |
| 2 | 0.0536 | **99.21%** ← ตัวแรกที่ ≥ 95% |
| 3 | 0.0072 | 99.92% |

→ ROP (Min) = **2**, Safety stock = 2 − 0.4 = 1.6 ≈ 2, Max = ROP + EOQ (สมมติ 2) = **4**

### ตาราง k สำหรับ λ และ CSL ที่พบบ่อย (คำนวณเอง)

| λ (ต่อช่วงป้องกัน) | CSL 90% | CSL 95% | CSL 98% | CSL 99% |
|---|---|---|---|---|
| 0.1 | 0 | 1 | 1 | 1 |
| 0.2 | 1 | 1 | 1 | 2 |
| 0.4 | 1 | 2 | 2 | 2 |
| 0.5 | 1 | 2 | 2 | 3 |
| 1.0 | 2 | 3 | 3 | 4 |
| 2.0 | 4 | 5 | 5 | 6 |

- Safety stock = `max(0, k − λ)` และ **ปัดแยกจาก ROP** — อย่าเอา ROP ไปลบ λ แล้วปัดซ้ำ เพราะ ROP ต้องเป็นจำนวนเต็มอยู่แล้ว
- อ่านตารางนี้ให้เห็นว่า λ = 0.4 ที่ CSL 95% ต้องถือ 2 ชิ้น = 5 เท่าของค่าเฉลี่ย — ต้นทุนถือครองต่อชิ้นสูงมากเมื่อเทียบกับของที่หมุนเร็ว

## 3. กรณี mixed demand (ใช้ทั้ง PM และ CM)

```
ROP = D_PM + k_Poisson(λ_corr, CSL)
Max = ROP + order quantity
```

ตัวอย่าง: bearing ใช้ใน PM 1 ตัวต่อ 3 เดือน (เท่ากับ lead time) + corrective λ = 0.4, CSL 95%
→ ROP = 1 + 2 = **3** (1 สำหรับ PM ที่กำลังมาถึง + 2 สำหรับ corrective)

## 4. CSL ตาม criticality

| ระดับ | CSL | เหตุผล |
|---|---|---|
| Critical (หยุดผลิต/กระทบ safety) | 98-99% | downtime cost สูงกว่า holding cost มาก |
| ทั่วไป | 95% | ค่า default ที่สมดุล |
| Non-critical / มี redundancy | 85-90% | ลด holding cost |

## 5. สิ่งที่ต้องแก้/เสริมจาก transcript

1. **Protection interval = lead time + review period** ไม่ใช่ lead time เดี่ยว — min-max เป็น periodic review (ตรวจนับทุก R วัน) ของที่สั่งไปต้องพอใช้ตลอด LT + R จึงต้องใช้ `λ_eff = λ × (LT + R)/LT` หรือคำนวณ λ ใหม่บนช่วง LT+R
2. **CSL ≠ fill rate** — CSL 95% วัด "มีของพอทุกครั้งที่สั่ง" ไม่ได้วัด "จำนวนครั้งที่ขาดของ" (fill rate) ของแพง/เบิกน้อยควรใช้ critical ratio ของ newsvendor: `CSL* = C_shortage / (C_shortage + C_holding)` ซึ่งมักให้ค่าต่างจาก 95% มาก
3. **λ จากประวัติสั้นหรือเป็นศูนย์** — Poisson ที่ λ ประมาณจาก 0-2 เหตุการณ์มีความไม่แน่นอนสูงมาก ใช้ gamma-Poisson (empirical Bayes) กับ pool ของอะไหล่ชนิดเดียวกัน หรือประมาณจาก MTBF ของ OEM: `λ_LT = (LT / MTBF) × จำนวนตัวที่ติดตั้ง × จำนวนชิ้นต่อการซ่อม`
4. **Lead time แปรผัน** — Poisson ฐานสมมติ LT คงที่ ถ้า LT แกว่ง (นำเข้า/offshore) ใช้ compound Poisson / negative binomial หรือเพิ่ม safety lead time **แยกก้อน** (อย่าบวกซ้ำกับ safety stock)
5. **Double counting ใน CMMS** — ถ้า PM BOM จองของไว้แล้ว และ λ_corr คำนวณจากประวัติที่รวมงาน PM จะนับซ้ำ ต้องแยก job type ตอนดึงประวัติ
6. **PM compliance drift** — ถ้าแผนเลื่อนบ่อย D_PM ต้องปรับตามอัตราเลื่อนจริง ไม่งั้นของกอง
7. **Kitting สำหรับ outage** — งาน overhaul ควรจัดชุดล่วงหน้า 1-2 lead time แทนการถือ stock ลอยตลอดปี

## 6. ใช้งานกับ CMMS

- ระบบส่วนใหญ่ (รวม Oracle Inventory/eAM) มี **field Min/Max แต่ไม่มีตัวคำนวณ Poisson** — คำนวณนอกระบบ (สคริปต์/Excel) แล้วป้อนค่า พร้อมบันทึก λ, CSL, วันที่คำนวณ ไว้ใน description หรือ DFF เพื่อให้ตรวจย้อนได้
- ต้องมีข้อมูล: ประวัติเบิกแยกตาม job type, lead time จริงจากจัดซื้อ, จำนวนติดตั้ง, MTBF/OREDA ของ item นั้น
- ทบทวนปีละครั้ง หรือเมื่อ λ เปลี่ยน > 30%

## ข้อจำกัด

- Poisson เหมาะเมื่อการเสียเป็นอิสระต่อกันและอัตราคงที่ — ถ้าเสียพร้อมกันเป็นชุด (common cause, batch ของ seal ทั้งชุด) ต้องใช้ compound model
- ตัวเลขใน transcript ตรวจแล้วถูก (P(X≤2) = 0.9921 ไม่ใช่ 0.9920 ตามการปัดเศษ) แต่ transcript ไม่ได้อ้างแหล่งและมองข้ามข้อ 1-7 ข้างบน
- ยังไม่ทดสอบกับข้อมูล CMMS จริงของ Valeura — ต้องรันกับ export 12 เดือนก่อนใช้ตั้งค่า

## Triplets

- [[Min-Max Stock Policy for Slow-Moving Spares]] [applies_to:: [[Spare Parts Management]]] intermittent demand items
- Poisson Min-Max [has_formula:: ROP = smallest k where P(X<=k) >= CSL] lambda over protection interval
- Protection Interval [has_formula:: lead time + review period] min-max is periodic review
- Min-Max Policy [depends_on:: [[Criticality Assessment]]] CSL 98-99 critical, 85-90 non-critical
- Insurance Spare Part [differs_from:: Poisson Min-Max] risk-based, not demand-based, [[Spare Part Criticality and Risk]]
- [[Min-Max Stock Policy for Slow-Moving Spares]] [related_to:: [[EOQ and Reorder Point]]] normal approximation fails below ~5 demands/year

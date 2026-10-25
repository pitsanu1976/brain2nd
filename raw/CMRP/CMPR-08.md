# CMPR-08: SPC (attribute charts, capability), Digitization/Predictive Modelling, MRO Inventory, Planning & Wrench Time

Source: PETROSYNC CMRP training course slides, file CMPR-08.pdf (scanned, OCR). Reading notes ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ PDF page `(CMRP CMPR-08 p.N)`

ขอบเขต: CMPR-08.pdf 50 หน้า (2 slides ต่อหน้า, เลขหน้าหนังสือ 257-306) เนื้อหาแบ่ง 4 ช่วงที่ไม่ต่อเนื่องกัน: (1) SPC p.1-14, (2) break-out + Digitization/Predictive modelling p.15-27, (3) spare/MRO inventory p.28-45, (4) Work management/planning p.46-50 OCR อ่านได้ดีในส่วนข้อความ แต่สูตร (p.1, p.12-14, p.31) และกราฟ/ตาราง (p.2-3, p.30, p.42, p.47) เพี้ยน ต้องดูภาพ (ตรวจด้วยภาพแล้ว p.1, 2, 3, 13, 17, 28, 30, 31, 39, 42, 47) slide ส่วน SPC อิง CRE/CMRP primer (เลข Table 4.41-4.48) สูตร capital spares p.31 ส่วนเงื่อนไข n systems อ่านไม่ออก

## 1. Attribute charts (CMRP CMPR-08 p.1)

- Attribute = ข้อมูลนับแบบไม่ต่อเนื่อง (ผ่าน/ไม่ผ่าน, ดี/เสีย) ต่างจาก variables chart ตรงที่ plot เพียงกราฟเดียว ใช้ติดตาม trend/cycle และประเมินผลการเปลี่ยนแปลงกระบวนการ
- 5 แบบ (Table 4.41):

| Chart | สิ่งที่บันทึก | Subgroup size | Distribution |
|---|---|---|---|
| p | สัดส่วนของเสีย (fraction defective) | แปรผันได้ | Binomial |
| 100p | % ของเสีย | แปรผันได้ | Binomial |
| np | จำนวนชิ้นเสีย (defectives) | คงที่ | Binomial |
| c | จำนวนจุดบกพร่อง (defects) | คงที่ | Poisson |
| u | defects ต่อหน่วย | แปรผันได้ | Poisson |

- เงื่อนไขใช้งาน: p chart ปกติ subgroup > 50; ค่าเฉลี่ย defect/defective ควร ≥ 4-5; ถ้า subgroup ของ p chart ต่างจากค่าเฉลี่ยเกิน ±20% ให้ตัดจุดนั้นทิ้งหรือคำนวณ limit เฉพาะจุดนั้น
- p chart ไวที่สุดในกลุ่ม attribute; X-bar–R chart ไวที่สุดแต่แพงที่สุดโดยรวม ข้อมูลของเสียมักจัดแบบ Pareto หา vital few และการลดของเสียจริงมักต้องเปลี่ยนระบบ

สูตร control limit (3σ) (p.1 slide ล่าง):

```
p chart:  p̄ = Σnp / Σn,  n̄ = Σn / k
          UCL/LCL = p̄ ± 3·sqrt( p̄(1-p̄) / n̄ )
np chart: UCL/LCL = n·p̄ ± 3·sqrt( n·p̄(1-p̄) )
c chart:  c̄ = Σc / k;     UCL/LCL = c̄ ± 3·sqrt(c̄)
u chart:  ū = Σc / Σn;    UCL/LCL = ū ± 3·sqrt(ū / n̄)
k = จำนวน samples; LCL ติดลบให้ใช้ 0
```

### ตัวอย่าง p chart (p.2)

20 lots, Σn = 22,500, Σnp = 52 → n̄ = 1,125, p̄ = 52/22,500 = 0.231% σ = sqrt(0.00231·0.99769/1125) ≈ 0.143% → UCL ≈ 0.66%, LCL = -0.20% → 0
ตรวจเลขแล้ว (derived): ผลรวม n = 22,500 และผลรวมของเสีย = 52 ถูก; σ และ UCL ถูก

**flag (slide ไม่ได้ชี้):**
- กราฟ p.2 แสดง lot 3 (0.89%) และ lot 13 (0.95%) อยู่เหนือ UCL 0.66% คือ out of control ตาม Rule 1 แต่ slide ไม่ได้อภิปราย
- lot 10 มี n = 600 ต่างจาก n̄ 1,125 ราว -47% เกินเกณฑ์ ±20% ที่ slide p.1 ตั้งเอง แต่ตัวอย่างยังใช้ limit ร่วม

## 2. การตีความ control chart (p.3-8)

แบ่ง 3σ เป็น zone A (2-3σ), B (1-2σ), C (0-1σ) ทั้งสองข้างของ center line

5 กฎทั่วไป (p.3): (1) จุดเกิน control limit; (2) 4 ใน 5 จุดอยู่ zone B (หรือไกลกว่า) ข้างเดียวกัน; (3) 2 ใน 3 จุดอยู่ zone A; (4) ≥ 8 จุดติดกันข้างเดียวของ center line; (5) trend ≥ 6 จุดขึ้นหรือลงต่อเนื่อง (บางตำราใช้ 7 สำหรับกฎ 4 และ 5) รูปแบบอื่น: (6) stratification ≥ 15 จุดใน zone C; (7) mixture/systematic variation (สลับไกลทั้งสองข้าง)

ตาราง "สาเหตุใน X chart / R chart + corrective action" (p.4-7) สรุป:

| Pattern | สาเหตุตัวอย่าง | Action ตัวอย่าง |
|---|---|---|
| In control | ดูดีแต่ไม่ดีเกินไป | - |
| Trend | เครื่องเสื่อม, tool wear, ผู้ปฏิบัติงานล้า, วัตถุดิบเปลี่ยน | ซ่อม/เปลี่ยนเครื่อง, เปลี่ยน tool, หมุนเวียนคน |
| Jump in level | แหล่งวัตถุดิบ, คน/เครื่องใหม่, เปลี่ยนวิธี/เครื่องมือตรวจ | คุมวัตถุดิบ, ตรวจ machine capability, calibrate |
| Recurring cycle | อุณหภูมิ/ความชื้น, rotation, **scheduled maintenance** | ปรับสภาพแวดล้อม, ประเมินงานบำรุงรักษา |
| จุดใกล้/เกิน limit | over-control, วัสดุ/วิธีทดสอบต่างกันมาก | ตรวจ limit, เลิกปรับเครื่องเกินเหตุ |
| Lack of variability | คำนวณ limit ผิด, กระบวนการดีขึ้น, ไม่ได้วัดจริง | ตรวจ limit, ตรวจ subgrouping |

หมายเหตุ: p.5 และ p.6 เป็น slide ซ้ำกัน (Jumps, Recurring cycles)

8 กฎของ Minitab (p.8): 1 จุด > 3σ; 9 จุดข้างเดียว; 6 จุดขึ้น/ลงต่อเนื่อง; 14 จุดสลับขึ้นลง; 2 ใน 3 จุด > 2σ ข้างเดียว; 4 ใน 5 จุด > 1σ ข้างเดียว; 15 จุดใน ±1σ; 8 จุดนอก ±1σ (สองข้าง) สังเกตว่าเกณฑ์ run ต่างกัน: slide 5 กฎใช้ 8 จุด, Minitab ใช้ 9

## 3. Process capability (p.8-13)

- ต้องมีกระบวนการที่ stable (ปกติรูประฆัง) แล้วเทียบ chance variation กับ spec; capable = spread แคบกว่า USL-LSL ขั้นตอน: วางแผนเก็บข้อมูล → เก็บ → plot/วิเคราะห์ (p.8)
- ทางเลือกเมื่อเทียบ natural limit กับ spec (p.9): ไม่ทำอะไร, แก้ spec (คุยกับลูกค้า), center process, ลด variability (ยากสุด อาจใช้ DOE), ยอมรับ loss ชั่วคราว
- การใช้อื่น: ตั้ง variables chart, ประเมินเครื่องใหม่, ทบทวน tolerance, จัดเครื่องที่ capable กับงานยาก, audit
- Control limit ของ X-bar มาจากค่าเฉลี่ย จึงแคบกว่า spread ของค่าเดี่ยว ต้องเทียบ spread ของค่าเดี่ยวกับ spec (Fig 4.45, p.10)
- แหล่ง variability (p.10-11, Fig 4.46): stream-to-stream, time-to-time (lot-to-lot), within-piece, piece-to-piece (inherent capability), error of measurement (คน+อุปกรณ์), และ interaction คน-เครื่อง

สูตร (p.12):

```
σ_R  = R̄ / d2         (d2 จากตารางตามขนาด subgroup; n=3 → 1.693)
Cp   = (USL - LSL) / 6σ_R      >1.33 capable; 1.00-1.33 ต้องคุมแน่น; <1.00 incapable
CR   = 6σ_R / (USL - LSL)      <0.75 capable; 0.75-1.00 คุมแน่น; >1.00 incapable
Cpk  = min[ (USL - X̄)/3σ_R , (X̄ - LSL)/3σ_R ]
```

ตาราง Cp → ppm (Table 4.48, p.12; process centered, two-sided, normal, ไม่มี shift): Cp 0.33/0.67/1.00/1.33/1.50/1.67/2.00 ↔ Z 1/2/3/4/4.5/5/6 ↔ 317,311 / 45,500 / 2,700 / 63 / 6.8 / 0.57 / 0.002 ppm (ตรวจกับตาราง normal สองหาง ถูกต้อง) slide ชี้ว่าความต้องการ reliability สูงต้องการ Cp 1.5-2.0 ตารางนี้ไม่ใส่ 1.5σ shift แบบ Six Sigma (3.4 ppm ที่ 6σ) — เป็นข้อสังเกตจากความรู้ทั่วไป

### Example 4.46 (p.13)
X̄ = 12, σ_R = 2, USL 16, LSL 4 → Cp = 12/12 = 1.0; Cpk upper = 4/6 = 0.667, lower = 8/6 = 1.33 → Cpk = 0.667 (ถูกต้อง; process ไม่ center ทำให้ Cpk < Cp)

### Example 4.47 (p.13)
USL 8.5, LSL 3.5, n = 3, X̄ = 5.465, R̄ = 4.0 → σ = 4.0/1.693 = 2.363; Z_upper = 3.035/2.363 = 1.28 → 10.0% สูงเกิน; Z_lower = 1.965/2.363 = 0.83 → 20.3% ต่ำเกิน รวม 30.3% (ตรวจแล้วถูก) เทียบ histogram 60 ค่า: 5/60 = 8.3% สูง, 11/60 = 18.3% ต่ำ รวม 16/60 = 26.7% (slide พิมพ์ 26.6% — ปัดเศษผิดเล็กน้อย) และจากค่าเดี่ยวด้วย s ได้ 9.3% + 19.5% = 28.8% slide สรุปว่า histogram คือความจริงระยะสั้น ส่วนอีกสองวิธีเป็นค่าประมาณระยะยาว

## 4. Point & interval estimation (p.14)

Example 4.48: tensile 4 ค่า 28.7, 27.9, 29.2, 26.5 → X̄ = 28.08 (point estimate) CI 95% แบบ t (df 3, t = 3.182): 28.08 ± 3.182·(s/√4) → slide ได้ 26.46-29.70 โดยใช้ S = 1.02 ถ้ารู้ σ = 2: 28.08 ± 1.96·(2/2) = 26.12-30.04 (ถูก) เหตุที่ใช้ σ/√n คือ CI เป็นของค่าเฉลี่ยประชากร (central limit theorem)

**flag:** S = 1.02 คือ SD แบบหารด้วย n (population) ถ้าใช้ sample SD (หาร n-1) ซึ่งเป็นค่าที่ถูกสำหรับ t-interval จะได้ s ≈ 1.18 และ CI ≈ 26.20-29.95 (derived) slide จึงแคบเกินจริง

## 5. Break-out และ Digitization / Predictive modelling (p.15-27)

- Break-out (p.15): เลือกอุปกรณ์ facility ใหม่ 4 ฟังก์ชันด้วยมุม RAMS ต้องใช้ข้อมูล (แหล่ง, สถิติ) และการตัดสินใจ asset management ตลอด life cycle
- Digitization (แปลง analog → digital, data) → Digitalization (ปรับ process) → Digital transformation (สร้าง business) (p.16)
- ประวัติ: pre-1980 reactive (M1.0 cost focus) → 1980-2010 preventive, CMMS, KPIs, CM, RCA (M2.0/3.0 quality) → post-2010 digital: Industry 4.0, IoT, AI, CPS, PdM, RUL (M4.0 customization) (p.16)
- กรอบ vendor/consultant: McKinsey แยก "what" (program: กำหนด strategy, operate, prioritize/plan/schedule, execute + feedback) กับ "how" (digital work management, asset strategies, performance management, reliability enablers); GE วาง APM คู่กับ EAM/CMMS, ERP, EH&S, EQMS, MOM; SAP แสดง ASPM flow: risk & criticality → RCM/FMEA assessment → recommendation → task list/plan (p.17-18)
- Pros/cons ของ digital technology แบบทั่วไป (p.19) และรายการ MCMC algorithms (Metropolis-Hastings, Gibbs, HMC ฯลฯ) ซึ่งไม่ผูกกับ maintenance (p.19)
- Predictive modelling (p.20-24): ใช้ข้อมูล+สถิติพยากรณ์; แหล่งข้อมูลรวม machine/sensor data; ขั้นตอนบูรณาการ: benchmark, เก็บ, cleansing, วิเคราะห์, KPI, action plan; ชนิดโมเดล OLS, GLM, logistic regression, random forest, decision tree, neural network, MARS; analytics 4 ระดับ descriptive → diagnostic → predictive → prescriptive; การใช้งาน predictive maintenance และ DSS
- ข้อจำกัด (อ้าง McKinsey, p.24-27): data labelling, ต้องการ dataset ใหญ่และ representative (หลักพันถึงล้าน record), explainability, generalizability (โมเดลไม่ควรใช้ข้ามกรณี), bias ในข้อมูล

## 6. Risk-based spare review และ capital spares (p.28-31)

- กระบวนการเชื่อม Maintenance Strategy Review (MSR): MEL → failure + BOM → ประเมินความเสี่ยง/critical equipment + จัดชั้นอะไหล่ → strategy/task → MTA ↔ Level of Repair Analysis → order quantity → integrated planning (p.28)
- ผังตัดสินใจง่าย "ควรสต็อกไหม" (p.28): แก้ได้โดยไม่ใช้อะไหล่ → ไม่สต็อก; ไม่วิกฤตต่อ production/safety/environment → ไม่สต็อก; ต้องสลับไป standby → ขึ้นกับ lead time (> 2 สัปดาห์ สต็อก); วิกฤต → สต็อก
- แนวทางขั้นสูง: ตีค่าเป็นเงินจาก risked cost (production, safety, environment, secondary damage) สำหรับอะไหล่ราคาสูง lead time ยาว สมมติฐานทั่วไป: exponential, อะไหล่ที่เสียไม่ซ่อม, ไม่คิด discounting; input: demand rate, lead time, standby configuration, จำนวนที่ติดตั้ง, ราคา, ค่าคลัง, consequential cost, repair lead time (p.29-30) กราฟ p.30: จำนวนสต็อก 1 มี risk cost สูงมาก (~19,500) ต่ำสุดที่ 2 แล้วต้นทุน interest/warehouse/write-off โตเชิงเส้น
- Capital spares (p.31): non-availability cost = c_na·F(T); storage cost = c_l·∫0..T R(t)dt; dead stock cost = c_s·R(T) สต็อกเมื่อ c_na·F(T) > ค่าเก็บ + dead stock (สัญลักษณ์บน slide อ่านยาก; เงื่อนไขกรณีใช้ได้กับ n systems อ่านไม่ออก)

## 7. MRO inventory management (p.31-45)

- MRO inventory = ของในคลัง + ที่สั่งแล้วยังไม่ส่ง; ชนิด: operating, rotatable, overhaul, insurance spares และ consumables (p.32, 34) ลูกค้าของ MRO คือฝ่ายบำรุงรักษา/ผลิต
- เป้าระยะสั้น (control): มีของพอในที่ที่ถูกต้อง; ระยะยาว (management): สมดุลต้นทุนถือครอง vs ความเสี่ยง stock-out, ลงทุนต่ำ service สูง (p.35-37) กราฟ total cost = inventory cost + stock-out consequence มีจุดต่ำสุด = optimum stock level (p.37)
- Stock levels 3 ระดับ (p.38-39): replenishment (สูงสุด), reorder, safety; replenishment/reorder รองรับความแปรปรวนปกติ, safety stock ลดความเสี่ยง stock-out ใช้กับรายการ non-insurance ของเครื่องวิกฤต
- **Safety stock = K × σ × √(delivery time)** (K = safety factor, σ = SD ของ demand) (p.39)
- ROP = เมื่อไรสั่ง, ROQ = สั่งเท่าไร (p.40-41)
- 4 basic models (p.43-45): B = continuous monitoring, s = periodic review

| Model | Reorder quantity | Reorder time | เหมาะกับ |
|---|---|---|---|
| BS (Min-Max) | แปรผัน | แปรผัน (เมื่อถึง reorder level) | issue ผันผวนมาก |
| BQ | คงที่ | แปรผัน | issue ผันผวนน้อย |
| sS | แปรผัน (เติมถึง max) | คงที่ (ตามรอบ) | ผันผวนน้อย |
| sQ | คงที่ | คงที่ | ผันผวนมาก |

**flag:** ตาราง 2x2 ใน p.42 ขัดกับ slide รายละเอียด p.43-45 (ตาราง p.42 จัด sS/sQ เป็น quantity คงที่ และ BS/BQ เป็น quantity แปรผัน, BQ/sQ เป็น reorder point แปรผัน) ตารางข้างบนยึด p.43-45 ซึ่งสอดคล้องกันเอง นอกจากนี้สัญลักษณ์ B/s ต่างจากตำรามาตรฐาน (s มักหมายถึง reorder point, ใช้ (s,Q), (s,S), (R,S)) — ข้อสังเกตจากความรู้ทั่วไป

## 8. Work management, planning และ wrench time (p.46-50)

- วงจร: strategy → planning → scheduling → execution → work history → analysis → continuous improvement (p.46)
- Breakdown เวลา (p.47): total 100% → ลา/วันหยุด 10% → available 90% → maintenance 60% (PM 30% + CM 30%) + non-maintenance 30% (admin, training, personal relief, slack) → wrench time 15% + 15% = 30% (ที่เหลือคือ travel, gather materials, prepare/put away)
- Efficiency (p.48-49): available จริง 30-32 ชม./สัปดาห์; wrench ~30% ของ 40 ชม. = 12 ชม.; ถ้า planning ทำให้ดีขึ้น 10% บนฐาน 15 ชม. ได้ +1.5 ชม./คน/สัปดาห์; โรงงาน 60 คน ≈ เพิ่มคน 6 คน (มูลค่า > €400,000/ปี, ตัวเลขปี 1997)
  **flag:** ฐานไม่สอดคล้อง (12 ชม. vs 15 ชม.) ถ้าใช้ 12 ชม. จะได้ +1.2 ชม./คน; 60 × 1.5 = 90 ชม. หาร 15 = 6 คน แต่หาร 12 = 7.5 คน
- ผัง "Planning อยู่ตรงไหน" (p.49): planning เตรียม scope, skill, ชั่วโมง, parts, tools, procedure, history file ก่อนงาน ร่วมกับ RCM (PM/PdM), storeroom, CMMS work order system, feedback
- Impact (p.50): เตรียมล่วงหน้า 1 ชม. ประหยัดเวลาทำงาน 3-5 ชม.; งานที่วางแผนใช้เวลาครึ่งหนึ่งของงานไม่วางแผน ตาราง direct work: unplanned เสียเวลา 65% (direct work 35%) vs planned 35% (direct work 65%) — รายการ instructions, tools/materials, travel, coordination delays, idle, late start/early quit, breaks, excess personal time ตรวจผลรวม 65% และ 35% ถูกต้อง

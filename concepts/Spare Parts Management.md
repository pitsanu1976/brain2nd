---
title: Spare Parts Management
created: 2026-10-20
updated: 2026-10-28
type: concept
tags: [spare-parts, maintenance-management, cmms, kpi, cost, book, work-management, cmrp, spo, warehousing, procurement, inventory-control, mpm]
sources: [reliability-based-maintenance-management.md, cmrp.md, spare-parts-optimization.md, maintenance-profit-maker.md]
confidence: medium
contested: true
---

# Spare Parts Management

การบริหารอะไหล่ตามหนังสือ RBMM (บทที่ 9 เป็นหลัก) มองอะไหล่เป็น "การซื้อความเสี่ยง": สต็อกน้อยไปเสี่ยงหยุดผลิต สต็อกมาก/ผิดตัวเสี่ยง Write-off แนวคิดหลักคือแยกอะไหล่ตามประเภทงาน (ตามแผน = ซื้อตรง, นอกแผน = สำรองคลัง) แล้วบริหารสองฝั่งคู่กัน ได้แก่ Demand Side (เลือกงาน PM และคาบ) กับ Supply Side (ตั้ง Max/Min ตามความเสี่ยงที่ฝ่ายบริหารยอมรับ) หน้านี้เป็น hub ของอะไหล่ ส่วนรายละเอียดอยู่ใน [[Spare Part Criticality and Risk]], [[EOQ and Reorder Point]] และ [[Spare Part Demand Forecasting]]

## ทำไมอะไหล่เป็นเรื่องเชิงกลยุทธ์

- ต้นทุนบำรุงรักษามากกว่าครึ่งเป็นค่าอะไหล่ (RBMM p.234); บทที่ 2 ระบุว่าอะไหล่เป็นสัดส่วนมากกว่า 60-70% ของค่าใช้จ่ายบำรุงรักษาทั้งทางตรงและทางอ้อม (RBMM p.34) ตัวเลขสองจุดไม่ตรงกันเป๊ะ (มากกว่าครึ่ง vs 60-70%) ให้ใช้เป็นระดับความสำคัญ ไม่ใช่ค่าแม่นยำ
- Holding cost ประมาณ 15-20% ของมูลค่าอะไหล่ต่อปี (RBMM p.16, p.34, p.234); ตัวอย่างหนังสือ สต็อก 500 ล้านบาท เท่ากับ 75-100 ล้านบาทต่อปี (RBMM p.234) ไม่รวมต้นทุนสภาพคล่อง
  - หมายเหตุ: บทที่ 10 ตั้งเป้าอัตราค่าครอบครองอะไหล่ไว้ 15-25% ของมูลค่าอะไหล่รวม (RBMM บทที่ 10) ช่วง 15-20% กับ 15-25% เป็นช่วงที่หนังสือใช้ต่างบริบท ไม่ถือเป็น contested
  - องค์ประกอบ holding cost: ดอกเบี้ยจากยอดคงคลัง, ค่าจัดเก็บ, ค่าจัดซื้อจัดหา, อะไหล่เสื่อมสภาพต้องทิ้ง, Write-off ของที่ไม่เคลื่อนไหว (RBMM p.68)
  - อะไหล่เป็น Current Asset ไม่มีค่าเสื่อมราคา แต่มี overhead (RBMM p.16, p.70)
- ค่าขาดอะไหล่ปรากฏเป็น MWT (Mean Wait Time) ซึ่งกระทบ MDT และ [[Availability and OEE]] (RBMM p.20)
- ค่าถือครองมักถูกรวมใน fixed cost อื่นจนผู้ขอสต็อกไม่รู้สึก; หนังสือแนะนำให้โอนค่าใช้จ่ายกลับหน่วยที่ขอสะสม และกระจาย common spare ตามหน่วยที่ใช้ร่วม (Accountability) (RBMM p.37-38, p.68)

## ประเภทอะไหล่

| ประเภท | ความหมาย | การบริหาร | อ้างอิง |
|---|---|---|---|
| Commissioning Spare Part | อะไหล่ช่วงทดสอบเดินเครื่อง แก้ปัญหาจากการก่อสร้าง/ติดตั้ง (forced deterioration) | เป็นความรับผิดชอบผู้ผลิต/EPC ไม่ควรรับเข้าคลังบำรุงรักษา | RBMM p.15-16, p.235 |
| Maintenance Spare Part ซื้อตรง (Non-stock, Planned) | ใช้กับงานตามแผน รู้เวลาและ Lead Time ล่วงหน้า | Just in Time ไม่เข้า Max/Min ไม่นับใน Turnover Rate | RBMM p.236, p.239 |
| Maintenance Spare Part สำรองคลัง (Stock Item, Unplanned) | ใช้กับ CM-Unplanned ที่ไม่ทราบเวลาเกิด | Max/Min, ROP, EOQ, Safety Stock ตามความเสี่ยง | RBMM p.236, p.239 |
| Insurance Part | ค่าขาดต่อครั้งสูงมาก เก็บแม้ Cost Ratio ต่ำกว่า 1 | ขออนุมัติระดับบริหาร | RBMM p.251 |

### Commissioning vs Maintenance Spare

- ช่วง commissioning เครื่องเพิ่งประกอบ ความเสียหายส่วนใหญ่มาจากฝีมือประกอบ ไม่ใช่การสึกหรอตามอายุ จึงอาจไม่ถูกใช้เลยในช่วงใช้งานปกติ (RBMM p.15, p.235)
- ผู้ขายอาจเสนอขายอะไหล่เกินจำเป็น (อาจเกิน 2-3 เท่า) แล้วสุดท้ายต้อง Write-off เป็นต้นทุนจริง (RBMM p.235)
- ข้อควรทำ: เรียกอะไหล่ที่มากับโครงการว่า Commissioning Spare Part และให้บำรุงรักษาตรวจทุกรายการก่อนรับเข้าคลัง (RBMM p.235) ดู [[Asset Life Cycle]]

### กฎเหล็กเรื่อง Stock vs Direct Purchase

- อะไหล่สำรองคลังมีไว้ตอบงานนอกแผนเท่านั้น; งานตามแผนใช้ซื้อตรง (RBMM p.45, p.236)
- ถ้า CMMS เห็นอะไหล่ซื้อตรงใช้ในงานนอกแผนสูง แปลว่าการสำรองสต็อกทำไม่ถูกหรืองานนอกแผนเกินคาด (RBMM p.307, ch10)
- ควรแยก Turnover ของอะไหล่ซื้อตรงออกจากอะไหล่คลัง มิฉะนั้นสับสนและ On Hand จะสูงกว่า Max (RBMM p.243)
- ข้อยกเว้น: อะไหล่ใช้ร่วมหลายเครื่องที่ตาราง PM ไม่พร้อมกัน (ตัวอย่างรถ 30 คัน PM ทุก 10,000 km) ต้องรวมความต้องการตามแผนและนอกแผน แล้วตั้ง Max/Min ด้วยสถิติ (RBMM p.236)

### มุมมอง CMRP: planner จองของคลังให้งานตามแผน (เพิ่ม 2026-10-25)

- ในขั้น material take-off ของ [[Maintenance Planning and Scheduling]] planner ทำ BOM ตรวจของในคลังแล้ว **จอง (reserve)** และออก stock requisition ให้งานตามแผน ส่วนของที่ไม่มีจึงวางแผนจัดหากับ Purchasing (CMRP CMPR-09 p.30)
- ของที่ควร stage ใกล้หน้างาน: ของซื้อตรง/non-stock, ของที่สต็อกต่ำหรือ CMMS แสดงว่าหมด, ของหมุนเร็ว; ไม่ควร stage: ของเฉพาะเครื่องเดียว, ของใหญ่ย้ายยาก, consumable ทั่วไป (CMRP CMPR-09 p.31)
- เทียบกับกฎของ RBMM ข้างบน: CMRP ไม่ได้แยกแหล่งอะไหล่ตามประเภทงาน งานตามแผนใช้ได้ทั้งของคลังและของซื้อตรง ขณะที่ RBMM ตั้งเป้าให้ Stock Parts ของงานตามแผนเป็น 0 (ดู [[Maintenance Budget]]) ความต่างนี้เป็นเรื่องนโยบายการจัดอะไหล่ ไม่ใช่ข้อเท็จจริงขัดกัน: กฎ RBMM เป็นข้อเสนอของหนังสือพร้อมข้อยกเว้นอะไหล่ใช้ร่วม และในทางปฏิบัติ ถ้าใช้กฎ RBMM การจองของคลังแบบ CMRP จะเหลือเฉพาะอะไหล่ใช้ร่วมตามข้อยกเว้น (การตีความของ wiki; ไม่ตั้ง contested)
- ทั้งสองแหล่งเห็นตรงกันว่าขาดของทำให้งานล่าช้า เสียเงิน คุณภาพงานตก (CMRP CMPR-09 p.30) และ stock-out บ่อยเป็นสาเหตุหนึ่งของ schedule non-compliance ดู [[Maintenance Backlog and Schedule Compliance]]

## Demand Side และ Supply Side

- Demand Side: เริ่มจาก RCM เลือกงาน PM (RBMM p.237) แล้ว PM Optimization จัดคาบ; งานตามแผนส่งผลต่อปริมาณ CM-Unplanned ซึ่งกำหนดปริมาณอะไหล่ที่จะใช้ ดู [[PM Task Selection]], [[PM Interval Optimization]], [[RCM Reliability Centered Maintenance]]
- Supply Side: Risk Based Spare Part Optimization ตั้งระดับสต็อกภายใต้ความเสี่ยงที่กำหนด (RBMM p.238, p.241-242)
- การลดอะไหล่ต้องทำคู่กับ Planned Maintenance Optimization (RBMM p.234)
- Condition Monitoring ตรวจจับ potential failure ล่วงหน้า กลายเป็น CM-Planned; จะต้องสะสมอะไหล่หรือไม่ขึ้นกับ Lead Time เทียบกับเวลาที่เหลือก่อนเสียนอกแผน ถ้า Lead Time ยาวกว่า ต้องสะสม (RBMM p.241) ดู [[P-F Interval and Condition Monitoring]]

### กระบวนการ Supply Side 6 กล่อง (RBMM p.238)

| กลุ่ม | วิธีคำนวณ | ผลลัพธ์ | หน้ารายละเอียด |
|---|---|---|---|
| Fast Moving | Fast Moving Method, demand with variance | Max/Min, Safety Stock, Confidence Level, EOQ | [[EOQ and Reorder Point]] |
| Low Criticality | Fast Moving Method หรือ Average Usage Method | Max/Min, Safety Stock, Confidence Level | [[Spare Part Demand Forecasting]] |
| Medium Criticality | Average Usage Method หรือ Demand Simulation | Max/Min, Cost Ratio | [[Spare Part Criticality and Risk]] |
| High Criticality | Demand Simulation Extended (เชื่อมแผนงานบำรุงรักษา) | Max/Min, Cost Ratio | [[Monte Carlo Maintenance Simulation]] |
| Consolidation | รวมความต้องการหลายผู้ใช้/หลายคลัง | ระดับสะสมรวม | ด้านล่าง |

กล่องที่ 1 คือการประเมินความวิกฤติ (เครื่องจักร, อะไหล่, รวม) เพื่อจัดกลุ่ม; กล่องที่ 6 คือ Consolidation (RBMM p.238)

## Spare KPIs

| ดัชนี | สูตร/ความหมาย | อ้างอิง |
|---|---|---|
| Stock Turnover Rate | มูลค่าอะไหล่ที่เบิกออก / มูลค่าอะไหล่ทั้งหมดในคลัง; ต่ำ = เสี่ยง Write-off | RBMM p.239 |
| Stock Service Rate (Service Factor) | จำนวนรายการที่เบิกได้ / จำนวนรายการที่ขอเบิก | RBMM p.239 |
| Stock out Rate | ปริมาณที่เบิกไม่ได้ / ปริมาณที่ขอเบิกทั้งหมด | RBMM p.239 |
| Stock Value / Asset Replacement Value | มูลค่าอะไหล่รวม / มูลค่าซื้อทดแทนทรัพย์สิน | RBMM p.239 |

### ตัวอย่างค่า B7-B10 ใน Maintenance Strategic Report (ตัวอย่างในหนังสือ ไม่ใช่ข้อมูล Valeura)

| รหัส | ดัชนี | Actual | Var (A-B) | Budget |
|---|---|---|---|---|
| B7 | Spare Part Inventory / Plant Asset | 2.50% | -0.50% | 3.00% |
| B8 | Stock Turn Ratio | 40.00% | -4.07% | 44.07% |
| B9 | Service Factor | 97.10% | -1.90% | 99.00% |
| B10 | Stock Out Rate | 2.50% | 1.50% | 1.00% |

(RBMM p.74-75, รูปที่ 3.7) แนวทางอ่านผล:

- B7: สะสมมากเกินไปหรือไม่ ใช้เป็นแนวทาง ไม่ใช่ตัวชี้ขาด ต้องเทียบประเภทเดียวกันและใช้มาตรฐานประเมินราคาเดียวกัน; ระวังทรัพย์สินที่ราคาใหม่ลดลง (RBMM p.74); ตั้งเป้า 1-3% ของราคาเครื่องจักร (RBMM บทที่ 10 p.295, p.314)
- B8: ต่ำ = เสี่ยง Dead Stock และ Write-off ให้ทบทวนระดับสะสมรายรายการตามนโยบายความเสี่ยง อำนาจอนุมัติ และการคำนวณความเสี่ยงที่ทำซ้ำได้ (RBMM p.74-75)
- B9: เก็บตรงรายการที่ต้องการหรือไม่ ทบทวนการจับคู่ Scheduled PM กับ CM-Unplanned (RBMM p.75)
- B10: รายการมีแต่ปริมาณไม่พอ ทบทวน Max/Min, Safety Stock, Cost Risk (RBMM p.75)

เป้าตาม criticality ในบทที่ 10: เครื่องกลุ่ม A Confidence มากกว่า 95%, B 90%, C 80-90% (RBMM p.317-319) ดู [[Maintenance KPIs]], [[Maintenance Strategic Report]]

## Spare Part Database ใน CMMS

ฐานข้อมูลอะไหล่ใน [[CMMS]] แบ่งเป็น 3 กลุ่มฟิลด์ (RBMM p.100-102, รูปที่ 4.8):

| กลุ่ม | ที่มา | ฟิลด์ |
|---|---|---|
| 1 | สร้างครั้งแรก | Part Number, Part Name, Spec/วิธีเก็บ, ประเภท/กลุ่ม, Bin Location |
| 2 | เปลี่ยนจาก Transaction (ซื้อ รับ จ่าย ปรับปรุง) | On hand Qty, Unit Cost, Amount, วันที่เบิกล่าสุด, Lead Time, อายุอะไหล่ |
| 3 | จากการคำนวณ (Spare Optimization Recommendation) | Min Qty, Max Qty, Re-Order Point, EOQ |

- ฟิลด์กลุ่ม 2 แก้โดยตรงไม่ได้ ต้องผ่าน transaction เพื่อตรวจสอบย้อนกลับ (RBMM p.101)
- ข้อมูลเสริม: Where Used/BOM, ผู้ขายและประวัติซื้อ, อะไหล่ทดแทน (ทางเดียว/สองทาง)
- อะไหล่ไม่ควรอยู่ใน equipment hierarchy ให้ไปอยู่ใน BOM เพราะอะไหล่ตัวเดียวใช้หลายอุปกรณ์; ไม่ฝังรหัสอะไหล่ในรหัสอุปกรณ์ (RBMM p.98)
- เป้าหมายขัดกัน 4 ข้อ: Stock Level ต่ำสุด, Service Level สูงสุด, Stock Turnover สูงสุด, Plant Availability สูงสุด ต้อง optimize หาจุดสมดุล (RBMM p.101)
- ข้อมูล failure (Failure Mode, Object Part, Cause) ใน Work Order ป้อน Spare Optimization (RBMM p.96) ดู [[Failure Data Recording]]
- หนังสือเน้น codification มาตรฐานและกำจัดรายการซ้ำเป็นฐานราก (RBMM p.240)

## Lead Time

- นับจาก Purchase Requisition จนอะไหล่พร้อมในคลัง: กำหนด Specification, สืบราคา/ประมูล, พิจารณาข้อเสนอ, ออก PO, รับของ (RBMM p.247)
- ข้ออ้างของหนังสือ: ลด Lead Time 20% ลดสต็อกเฉลี่ยลงเหลือครึ่งหนึ่ง (RBMM p.247) เป็นข้ออ้างที่ไม่มีการพิสูจน์ในบันทึก
- บริหาร Lead Time เชิงบวก (ให้รางวัลผู้ขายที่ส่งเร็ว) ดีกว่าเชิงลบ เพราะการปรับเข้มทำให้ผู้ขายยืด Lead Time ครั้งต่อไป เกิดวงจรสั่งทีละมาก ๆ (RBMM p.247)
- Blanket Order (ผู้ขายเก็บอะไหล่ในคลังเรา คิดเงินเมื่อเบิก) เป็นกลไกให้งานนอกแผนมีอะไหล่โดยไม่แบกค่าถือครอง (RBMM p.289, p.298)

## Consolidation

- หลายหน่วยงานใช้อะไหล่ตัวเดียวกัน เช่น ผู้ใช้ A = 4/2, B = 3/1, C = 3/2 รวม Max/Min ตรง ๆ ไม่ได้ ต้องคำนวณ Consolidation ใหม่ (Monte Carlo ได้) (RBMM p.265-266)
- รูปที่ 9.21: User 1..n ประเมิน Max/Min -> Same Store Consolidation -> Multi-Store Consolidation; หน่วยรับผิดชอบไม่จำเป็นต้องเป็นหน่วยคลัง

## กระบวนการ Work Process ครบวงจร (RBMM p.267-270)

- รูปที่ 9.22: ฐานข้อมูลกลาง Maintenance and Spare Part Database เชื่อม Part Demand Side Optimization (RCM, Failure Data Analysis, Task Selection/Interval, Task Grouping เป็น PM Packages) กับ Part Supply Side Optimization (ประเมิน criticality -> คำนวณระดับ -> ปรับ Demand Side? -> Consolidation? -> ขออนุมัติตามนโยบายความเสี่ยง -> สะสมและจัดหา)
- รูปที่ 9.23 ใช้ข้อมูลจาก ERP: Criticality Review -> เลือกวิธี -> คำนวณ -> ปรับ Demand Side? -> Consolidation? -> วิเคราะห์ผล -> อนุมัติ -> Upload
- ปัจจัยสำเร็จ (RBMM p.265-266): การคิดค่าใช้จ่ายครบถ้วน, ดัชนีและรายงาน, ระบบ Maintenance Management แข็งแรง, เครื่องมือ, เลือกงาน/คาบ PM ถูกต้อง, เข้าใจ Risk Based Stock Recommendation และความร่วมมือระหว่างบำรุงรักษา คลัง จัดซื้อ
- Accountability: ต้องอธิบายได้ว่าทำไมสั่ง/เก็บเท่านั้น; ฝ่ายบริหารต้องชี้ขาดว่ากลุ่มอะไหล่ไหนใครกำหนดระดับ; คำนวณมืออาจไม่มีประสิทธิภาพ ควรใช้เครื่องมือ (RBMM p.271)

## มุมมองจาก SPO (เพิ่ม 2026-10-27)

หนังสือ [[Spare Parts Optimization Book]] (SPO, สุชาติ ศุภมงคล 2546) มองอะไหล่จากฝั่ง **คลังพัสดุ จัดซื้อ และบัญชี** ซึ่ง RBMM แตะน้อย จึงเสริมกันมากกว่าขัดกัน การเทียบทีละประเด็นอยู่ที่ [[SPO vs RBMM Spare Parts Approaches]] สิ่งที่ SPO เพิ่มเข้ามาในหัวข้ออะไหล่:

| เรื่อง | สาระที่ SPO เพิ่ม | หน้ารายละเอียด |
|---|---|---|
| ขอบเขต MRO และการจัดประเภท | MRO = วัสดุที่ไม่เป็นส่วนผสมของสินค้า; 9 ประเภท เช่น Insurance and Standby (รหัส "S"), OAR, Capitalized Parts, Commissioning spares (SPO p.12, p.26-31) | [[MRO Material Classification]] |
| อะไหล่ใช้ร่วม | คู่มือ Interchangeable Book รวมของจากหลายเครื่องไว้ที่เดียว ใช้ commodity code แทน OEM part no. (SPO p.59-62) | [[Parts Interchangeability]] |
| จำนวนแนะนำตามชนิดเครื่อง | Engineering Basic Practice: ตาราง % ต่อจำนวนเครื่อง (30/50/130%) และ % ต่อชิ้นติดตั้ง รวม compressor (SPO p.40-54) | [[Spare Parts Recommendation by Equipment Type]] |
| คลังและการจัดเก็บ | หน้าที่คลัง 7 ข้อ, จุดรับเดียว, การวางผังและเก็บรักษา (SPO p.20-23, บทที่ 7) | [[Warehouse Design and Storage]] |
| เครื่องมือและความมั่นคง | tool crib, กุญแจ 2 ชุด, log book การเข้าคลังนอกเวลา (บทที่ 11-12) | [[Tool Crib and Warehouse Security]] |
| จัดซื้อ | Blanket Order, System Contract, Consignment/Vendor Stocking, Outsourcing (SPO p.90-95) | [[MRO Purchasing and Contracting]] |
| ควบคุมระดับคงเหลือ | 6 วิธี: ROP/EOQ, High/Low Limit, Min-Max, Periodic Review, Order Up-to, OAR และตารางวิธี x ประเภทอะไหล่ (SPO p.102-110) | [[MRO Inventory Control Methods]] |
| KPI และ benchmark | Turnover, MOS/DOS, Inventory Value % GPI (2/4/10%) (SPO p.112-115, p.126-129) | [[Inventory Turnover and GPI Benchmarks]] |
| ลดสต็อก | ABC ด้วย ABU, ไม่เคลื่อนไหว 3 ปี = ล้าสมัย, เป้า MOS/DOS, Materials Control Committee (SPO p.115-132) | [[MRO Inventory Reduction Program]] |
| Turnaround | แผน MR/MS แยกจากสต็อกประจำ (SPO p.33-38) | [[Turnaround Management]] |

ประเด็นเทียบกับเนื้อหา RBMM ในหน้านี้:

- **Holding cost**: SPO ใช้ 30% เป็นตัวอย่าง (SPO p.120) และให้คำนวณ COP (Cost of Possession) จาก 7 รายการ: ผลตอบแทนเงินลงทุน, ประกันภัย, ค่าเช่าคลัง, ค่ายกขน, ค่าบริหาร, ล้าสมัย/เสื่อม, ของหาย (SPO p.104) ต่างจาก 15-20% ของ RBMM ในฐานะสมมติฐานตัวอย่าง ไม่ใช่ข้อขัดแย้ง; RBMM นับค่าจัดซื้อไว้ใน holding cost แต่ SPO แยกเป็นค่าสั่งซื้อ (CO ราว 90-120 บาทต่อรายการต่อครั้ง) ในสูตร EOQ
- **Commissioning spares**: ตรงกับ RBMM ว่าเป็นภาระผู้รับเหมา เจ้าของงานอาจเลือกซื้อเมื่อจบงานตามเงื่อนไข (SPO p.30-31)
- **งานตามแผน**: SPO ให้สต็อกมีไว้ซ่อมปกติ ส่วน overhaul/turnaround วางแผนแยก (SPO p.55) สอดคล้องกับกฎ Stock vs Direct Purchase ของ RBMM แต่ยอมให้จองของที่มีในคลังให้ turnaround (SPO p.36-37)
- **Blanket Order**: SPO ใช้คำนี้กับสัญญาซื้อทั้งปีที่ทยอยรับ (SPO p.91-92) ส่วนกลไก "ผู้ขายเก็บของในคลังเรา คิดเงินเมื่อเบิก" ที่ RBMM เรียก Blanket Order (หัวข้อ Lead Time ข้างบน) SPO เรียกว่า Consignment / Vendor Stocking (SPO p.95) ต่างที่ศัพท์
- **KPI**: SPO เห็นว่า turnover ใช้ได้กับของหมุนเร็วเท่านั้น จึงวัด MRO เป็น % ของ GPI (Gross Plant Investment มูลค่าปัจจุบันของเครื่องจักรผลิตหลักและ infrastructure ไม่รวมที่ดิน/อาคารสำนักงาน) (SPO p.113-115) เทียบได้กับ B7 และ Stock Value / Asset Replacement Value ของ RBMM
- **ตัดสินระดับสต็อก**: SPO ใช้ Basic Practice + ปัจจัย 7 ข้อ (อายุ, จำนวนติดตั้ง, เปลี่ยน/ซ่อมได้, ความสำคัญของเครื่อง, ความซับซ้อน, lead time, จุดประสงค์) (SPO p.129) และคณะกรรมการ แล้วปรับด้วยสถิติหลังเดินเครื่อง 2-3 ปี (SPO p.57-58, p.112) ส่วน RBMM ใช้ criticality + Cost Ratio ตั้งแต่ต้น

### ข้อขัดแย้ง: เป้ามูลค่าอะไหล่ต่อมูลค่าโรงงาน (resolved 2026-10-27)

- มุมมอง RBMM (reliability-based-maintenance-management.md): เป้า B7 = 1-3% ของราคาเครื่องจักร (RBMM p.295, p.314)
- มุมมอง SPO (spare-parts-optimization.md): ไม่เกิน 4% ของ GPI สำหรับโรงงานเน้นเครื่องจักร (SPO p.115); ท้ายเล่มแนะนำ 3-4% GPI สำหรับโรงงานไทย (SPO p.143-145); นโยบายตัวอย่าง 3% ของเงินลงทุนสร้างโรงงาน (SPO p.55)
- สถานะ: ยังไม่ resolve (ช่วงทับกันที่ 3%; ตัวหารใกล้เคียงแต่ไม่เหมือนกัน) รายละเอียดและสาเหตุที่เป็นไปได้ดู [[SPO vs RBMM Spare Parts Approaches]] หัวข้อ C2 (ข้อความเดิมก่อน resolve)
- ผู้ใช้ตัดสิน 2026-10-27: ยึดเป้ามูลค่าสต็อกตาม SPO คือไม่เกิน 4% ของ GPI (3-4% สำหรับโรงงานเน้นเครื่องจักรในไทย, 1-1.5% สำหรับเครื่องจักรไม่ซับซ้อน) ค่า 1-3% ของ RBMM เก็บไว้เป็นข้อมูลอ้างอิง (resolved)

## มุมมองจาก MPM (เพิ่ม 2026-10-28)

หนังสือ [[Maintenance Profit Maker Book]] (MPM, ผู้แต่ง 2 ใน 3 คนเดียวกับ RBMM) บทที่ 5 และ 12 มองอะไหล่เป็นทั้งทรัพย์สินหมุนเวียนในงบดุลและค่าใช้จ่ายในงบกำไรขาดทุน (MPM p.90)

### ความสำคัญและระดับสต็อกเฉลี่ย (MPM p.84-85)

- ประเทศอุตสาหกรรมเก็บสำรองอะไหล่เฉลี่ยราว **3-5% ของราคาเครื่องจักร** ใช้เป็นดัชนีสอบทานสำหรับโรงงานใหม่ (MPM p.84-85) เป็น **ค่าเฉลี่ยที่พบ ไม่ใช่เป้า** และฐานต่างกัน (ราคาเครื่องจักร vs GPI) จึงไม่ใช่ข้อขัดแย้ง; เป้าที่ผู้ใช้ตัดสินแล้ว (2026-10-27) ยังคงเป็นไม่เกิน 4% ของ GPI ตาม SPO (ดูหัวข้อข้อขัดแย้ง resolved ข้างบน) ปลายบน 5% ของ MPM เกินเกณฑ์นี้
- MPM เน้นว่า % รวมไม่ใช่ประเด็นหลัก สิ่งสำคัญคือ **การกระจายของอะไหล่** ตามความวิกฤตของเครื่อง (MPM p.85)
- ต้นทุนอะไหล่มี 2 ด้าน: ต้นทุนการมีและเก็บ + ต้นทุนการขาด; ในไทยอะไหล่ส่วนใหญ่นำเข้า lead time นาน จึงต้องเก็บมาก; ปัญหาที่ทำให้ส่วนน้อยได้ผลคุ้ม: อุปกรณ์หลากหลาย อะไหล่เดียวกันถูกตั้งรหัส/ชื่อต่างกัน อัตราใช้และ lead time ไม่คงที่ (MPM p.84) ดู [[Parts Interchangeability]]

### ข้อขัดแย้ง MPM-C1: Holding cost (contested)

| มุมมอง | ค่า | แหล่ง |
|---|---|---|
| MPM ข้อความหลัก | ค่าใช้จ่ายเก็บสำรองราว **20-40%** ของมูลค่าอะไหล่ที่เก็บ (ไม่ระบุว่าต่อปี แต่บริบทคือรายปี) | MPM p.84 |
| MPM ตัวอย่างตัวเลข | คิดเฉพาะต้นทุนการเงิน **6%** (สต็อก 500 ล้าน ลด 10% ประหยัดดอกเบี้ย 3 ล้าน/ปี) และ **10%** (WACC, XYZ) | MPM p.17, p.108, p.180-181 |
| RBMM | **15-20%** ของมูลค่าอะไหล่ต่อปี | RBMM p.16, p.34, p.234 |
| SPO | 30% เป็นตัวอย่าง และให้คำนวณ COP | SPO p.104, p.120 |

- ตัวอย่างของ MPM ใช้ขอบเขตแคบ (ดอกเบี้ยอย่างเดียว) จึงต่ำกว่าข้อความหลักของเล่มเองมาก และช่วง 20-40% สูงกว่า 15-20% ของ RBMM ทั้งที่ผู้แต่งซ้อนกัน สถานะ: ยังไม่ resolve ข้อแนะนำเชิงปฏิบัติ (การตีความของ wiki): ระบุขอบเขตของ holding cost ทุกครั้ง (เฉพาะดอกเบี้ย vs COP เต็ม) ก่อนใช้ใน EOQ หรือ business case ดู [[EOQ and Reorder Point]]
- ตัวอย่าง p.17 ต่อ: ประหยัด 3 ล้าน/ปี = งบปรับปรุงงานอะไหล่ได้ 3 ล้าน (ค่าใช้จ่าย) หรือ 15 ล้าน (งบลงทุนตัดค่าเสื่อม 5 ปี) (derived ตรวจแล้ว: 500 x 6% x 10% = 3; 3 x 5 = 15)

### เป้าหมาย 4 ข้อ (MPM p.84)

Stock Level ต่ำสุด, Stock Availability / Service Level สูงสุด, Stock Turnover สูงสุด โดย Plant Availability สูงสุด ตรงกับเป้าหมายขัดกัน 4 ข้อของ RBMM (RBMM p.101) สูตร Service Level ของ MPM = จำนวนรายการที่เบิกได้ครบ / จำนวนรายการที่เบิกทั้งหมด (line fill rate) เป็นดัชนีสำคัญแต่ใช้คุมน้อยเกินไป (MPM p.86) เป้าเชิงตัวเลขของ turnover และ service level อยู่ที่ [[Inventory Turnover and GPI Benchmarks]]

### อะไหล่ตามความวิกฤตของเครื่อง (Fig 5.1, MPM p.85)

กลุ่มวิกฤตสูงสุด (~20% แรก) สนับสนุนด้วยอะไหล่เกือบ 100% ร่วมกับ Inspection/RBI, RCM/FMEA; กลาง (~50%) เน้นงานเชิงรุกและทำนายการเสียมากกว่าสะสมอะไหล่; ต่ำ (~30%) จัดหาเมื่อต้องการหรือจ้างเหมา รายละเอียดและการเทียบสัดส่วนกับ RBMM ที่ [[Spare Part Criticality and Risk]]

### กลยุทธ์ตามอายุโรงงาน (MPM p.84-90)

| ช่วง | แนวทาง |
|---|---|
| โรงงานใหม่ | ใช้ข้อมูลโรงงานคล้ายกัน/คำแนะนำผู้ผลิต สอบทานกับดัชนี 3-5%; วิเคราะห์ความวิกฤตก่อนจัดปริมาณ; คุมระบบเบิกให้เคร่งครัดตั้งแต่เริ่ม |
| เดินเครื่องเข้าที่ | ทบทวนความวิกฤต, ABC, วิเคราะห์ราคาและการเคลื่อนไหว ([[MRO Inventory Control Methods]]); หมุนเร็ว -> Quantitative, ที่เหลือ -> Qualitative |
| ผลิตมานาน | Spare Part Inventory Management Performance Analysis/Audit (สำรวจ ประเมิน SWOT ข้อแนะนำ) แล้ว optimize ต่อเนื่อง |

**กลยุทธ์ปรับปรุง 5 ข้อหลังประเมิน (MPM p.89-90)**:
1. ปรับปรุงการใช้: PM พยากรณ์ความต้องการล่วงหน้า จัดหาเมื่อต้องการ (ต้องมี MMS ที่ดี)
2. ปรับปรุงการเก็บสำรอง: ใช้ประวัติการเบิกรวมรายการที่ขาด ตัวอย่างลดยอดสำรองได้ 16% (ดู [[MRO Inventory Reduction Program]])
3. ปรับปรุงการจัดหา: แก้ lead time ร่วมกับผู้ขาย หรือ Consignment Stock ดู [[MRO Purchasing and Contracting]]
4. การวัดสมรรถนะ: โยงกับผลผลิต รายงานผู้บริหารรายเดือน
5. วัดและประเมินผล: วางดัชนี ข้อมูล และวิธีวัดตั้งแต่ต้น

### ตัวอย่างความคุ้มค่า (MPM p.90)

- โรงงานใหญ่ค่าบำรุงรักษารวม > 50 ล้านบาท อะไหล่ไม่ต่ำกว่า 60-70% = > 30 ล้านบาท; ถ้าไม่เคยปรับปรุง ลดได้ 10-15%; ลงทุนปรับปรุง 3-5 ล้านบาท คืนทุนใน 1 ปี
- ตรวจเลข (derived): 10-15% x 30 ล้าน = 3-4.5 ล้าน/ปี คืนทุน 1 ปีเฉพาะเมื่อลงทุนไม่เกินราว 4.5 ล้าน ปลายบน 5 ล้านต้องใช้ฐาน 70% x 50 = 35 ล้าน (ได้ 3.5-5.25 ล้าน) สอดคล้องโดยประมาณ ดู [[Maintenance Business Case]]

### สัดส่วนอะไหล่ต่อค่าบำรุงรักษา (หมายเหตุ ไม่ใช่ contested)

MPM ให้ทั้ง "ไม่ต่ำกว่า 60-70%" (MPM p.90) และ "> 50%" (MPM p.159, p.216) ตรงกับคู่ "มากกว่าครึ่ง" vs "60-70%" ของ RBMM ข้างบน; ตัวอย่างตัวเลขในบทที่ 8 ของ MPM เองให้อะไหล่ใช้สิ้นเพียง 23% (หรือ 46% เมื่อรวมอะไหล่ซ่อมใหญ่และค่าถือครองคลัง, derived) จึงใช้เป็นระดับความสำคัญ ไม่ใช่ค่าแม่นยำ

### สัดส่วน 20/60/20 และเป้าการลด (Fig 12.6-12.7, MPM p.87, p.217-218)

| กลุ่ม | สัดส่วน | วิธี |
|---|---|---|
| เคลื่อนไหวเร็ว | 20% | Quantitative Inventory Management (ข้อมูลการใช้มากพอ) |
| Optimizable | 60% | Qualitative Inventory Management (ใช้น้อย ประวัติไม่พอ) วิเคราะห์ราคาและความวิกฤต |
| Insurance Items | 20% | ปรับปรุงไม่ค่อยได้ (ต้องมีตามเงื่อนไข) |

- 80% ที่ไม่ใช่ fast-moving เป็นต้นเหตุสะสมเกิน/ขาดและค่าใช้จ่ายสูง หัก insurance 20% เหลือ 60% ที่ต้อง optimize; หนังสือไม่ระบุว่า % เป็นของจำนวนรายการหรือมูลค่า และ 20% ของกลุ่มหมุนเร็วไม่ตรงกับ A = 10% ของรายการใน ABC หน้าเดียวกัน (MPM p.87)
- เป้าหมาย 3 ระดับ: หลัก = อะไหล่เคลื่อนไหว (ปรับ Min/ROP, Re-order Quantity, Max) ลด **10-20%**; รอง = insurance items; เสริม = ของล้าสมัย/หมดอายุและวัสดุสิ้นเปลือง; ถ้าไม่เคยจัดการมาก่อน ลดได้ **> 20%** (MPM p.217)
- ข้อมูลการใช้/ซื้อจำเป็นแม้ไม่ถูก 100% ดึงจาก CMMS/ERP ลง Excel ได้ (MPM p.217-218)

### ลดที่ต้นเหตุ: พฤติกรรมการกินอะไหล่ (MPM p.219)

การปรับระดับสต็อกคือการบริหาร "ผล" ต้นเหตุคือการ consume อะไหล่ผิดปกติ ใช้ประวัติการเสีย/การแก้ทำ Failure Root Cause Analysis ([[Root Cause Analysis]]) บนรายงาน CMMS **ค่าอะไหล่สูงสุด 10 อันดับ** แล้วจัดการทีละ 10 รายการ

| สาเหตุ | การแก้ |
|---|---|
| ออกแบบด้อยตั้งแต่ต้น | วิศวกรรม/ออกแบบใหม่ ปรับข้อกำหนดจัดซื้อ |
| ติดตั้งไม่ถูกต้อง | ติดตั้งใหม่ |
| ใช้งาน/สภาพแวดล้อมไม่ตามกำหนด | ปรับสภาพแวดล้อม |
| อะไหล่ไม่มีคุณภาพ | เปลี่ยนแหล่ง ปรับการคัดสรร |
| คุณภาพการซ่อมไม่พอ | ปรับกระบวนการควบคุมคุณภาพ |
| กลยุทธ์ PM/CM/PDM ยังไม่เหมาะ | ปรับกลยุทธ์ ดู [[PM Task Selection]] |

สอดคล้องกับหลัก Demand Side ของ RBMM ข้างบน (ลดอะไหล่ต้องทำคู่กับ PM optimization)

### Spare Part Optimization System (SOS) 5 โซน (MPM p.219-221)

เครื่องมือที่ต้องลงทุนมี 4 อย่าง: CMMS/ERP ที่มี Inventory Management Module, **SOS**, Reliability Engineering Program (ต้องมีประวัติครบ มิฉะนั้นลงทุนเปล่า), เครื่องมือวิเคราะห์ เช่น vibration; SOS ต่างจาก CMMS/ERP ตรงที่ต้องใช้ข้อมูลความเชื่อมโยงอะไหล่-เครื่อง ผลกระทบการผลิต และความสำคัญ ผลคือบอกความเสี่ยงของการไม่มีอะไหล่ ส่วนการตัดสินใจเป็นของผู้บริหาร:

| โซน | การตัดสินใจทั่วไป |
|---|---|
| ความเสี่ยงต่ำ ผลกระทบน้อย | ไม่เก็บ ยอมรับความเสี่ยง (fair risk) |
| ความเสี่ยงต่ำ ผลกระทบสูง | ถ้าราคาสูงมาก อาจซื้อ **ประกันภายนอก (external insurance policy)** แทน |
| ความเสี่ยงปานกลาง ผลกระทบสูง | มักซื้อประกันไม่ได้ จัดเป็น insurance spares เอง |
| ความเสี่ยงปานกลาง ผลกระทบต่ำ | ปกติเก็บสำรอง |
| ความเสี่ยงสูง | ต้องเก็บสำรอง |

ตัวอย่างหน้าจอ Stock Cost/Risk Assessment (Fig 12.8) ใช้แกนอัตราส่วน Risk ต่อ Cost of Stock และ Cost of Stockout รายละเอียดเทียบกับ Cost Ratio ของ RBMM ที่ [[Spare Part Criticality and Risk]]


## เชื่อมโยงกับ compressor failure hierarchy

- Spare demand เป็นฟังก์ชันของ failure mode ต่อ equipment: Spare Part DSx Model (RBMM p.263) ต้องรู้ Equipment, Failure Mode, Beta, Eta ซึ่งตรงกับระดับ [[Failure Mode]] และ [[Maintainable Item]] ใน ISO 14224/OREDA ([[ISO 14224]], [[OREDA]])
- BOM/Where Used ผูกอะไหล่กับ maintainable item ของ [[Compressor]] ได้ ตามแนวทางตาราง criticality อะไหล่-เครื่อง (RBMM p.245-246)
- OREDA ให้ failure rate ระดับ item ซึ่งเป็น constant rate (ใช้กับ Basic Average Method ได้ แต่ใช้หา PM interval ไม่ได้ ดู [[Spare Part Demand Forecasting]]); ไม่มีข้อมูล failure จริงของ asset Valeura ใน sources
- ผู้ใช้งานจริงควรแปลงเป็นรายการ: failure mode ที่เกิดบ่อยใน [[Failure Mode]] (เช่น leakage [[ELP External Leakage Process Medium]], [[ELU External Leakage Utility Medium]]) คือจุดที่ควรตรวจว่าอะไหล่ที่เกี่ยวข้องมีระดับสะสมเหมาะสมหรือไม่ (ข้อเสนอแนะการประยุกต์ ไม่ใช่ข้อมูลในหนังสือ)
- ในระบบ compressor แบบ standby ต้องวิเคราะห์ Hidden Failure และ Redundancy ของทั้งระบบก่อนตั้งระดับอะไหล่ ดู [[Redundancy and Standby Systems]]

## ดูเพิ่ม

- [[Spare Part Criticality and Risk]]
- [[EOQ and Reorder Point]]
- [[Spare Part Demand Forecasting]]
- [[Maintenance Budget]]
- [[Maintenance Cost Structure]]
- [[CMMS]]
- [[Maintenance KPIs]]
- [[Maintenance Planning and Scheduling]]
- [[Spare Parts Optimization Book]]
- [[SPO vs RBMM Spare Parts Approaches]]
- [[MRO Material Classification]]
- [[Parts Interchangeability]]
- [[Spare Parts Recommendation by Equipment Type]]
- [[Warehouse Design and Storage]]
- [[Tool Crib and Warehouse Security]]
- [[MRO Purchasing and Contracting]]
- [[MRO Inventory Control Methods]]
- [[Inventory Turnover and GPI Benchmarks]]
- [[MRO Inventory Reduction Program]]
- [[Maintenance Profit Maker Book]]
- [[Root Cause Analysis]]

ดูเพิ่ม (หน้าจาก MPM ingest 2026-10-28): [[Maintenance Performance Improvement]], [[Maintenance Financial Impact]]

## Triplets

- [[Spare Parts Management]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 9
- [[Spare Parts Management]] [has_part:: Demand Side] PM task selection and interval
- [[Spare Parts Management]] [has_part:: Supply Side] Max/Min under accepted risk
- Demand Side [uses:: [[RCM Reliability Centered Maintenance]]] (RBMM p.237)
- Demand Side [uses:: [[PM Interval Optimization]]]
- Supply Side [uses:: Risk Based Spare Part Optimization] (RBMM p.238, p.241-242)
- Spare Parts [has_value:: more than half] share of maintenance cost (RBMM p.234)
- Spare Parts [has_value:: more than 60-70%] share of direct and indirect maintenance cost (RBMM p.34); differs in wording from p.234, use as order of magnitude
- Holding Cost [has_value:: 15-20%] of spare value per year (RBMM p.16, p.34, p.234) MPM-C1 [contested:: true]
- Holding Cost [has_value:: 15-25%] chapter 10 target of total spare value, different context, not contested (RBMM ch10)
- Holding Cost [has_value:: 75-100 million THB per year] book example, 500 million THB stock (RBMM p.234)
- Interest on Inventory [part_of:: Holding Cost] (RBMM p.68)
- Storage Cost [part_of:: Holding Cost] (RBMM p.68)
- Procurement Cost [part_of:: Holding Cost] (RBMM p.68)
- Obsolete Parts Disposal [part_of:: Holding Cost] (RBMM p.68)
- Write-off [part_of:: Holding Cost] non-moving items (RBMM p.68)
- Spare Parts [is_a:: Current Asset] no depreciation, has overhead (RBMM p.16, p.70)
- Mean Wait Time [related_to:: [[Availability and OEE]]] spare shortage shows as MWT, affects MDT (RBMM p.20)
- Commissioning Spare Part [is_a:: Spare Part Type] responsibility of vendor/EPC, not taken into maintenance store (RBMM p.15-16, p.235)
- Direct Purchase Parts [is_a:: Spare Part Type] non-stock, planned work, Just in Time, excluded from Max/Min and Turnover Rate (RBMM p.236, p.239)
- Stock Parts [is_a:: Spare Part Type] stock item for CM-Unplanned, managed with Max/Min, ROP, EOQ, Safety Stock (RBMM p.236, p.239)
- Insurance Part [is_a:: Spare Part Type] kept even when Cost Ratio below 1, management approval (RBMM p.251)
- Direct Purchase Parts [applies_to:: Planned Maintenance] (RBMM p.45, p.236)
- Stock Parts [applies_to:: CM-Unplanned] (RBMM p.45, p.236)
- Shared Parts With Staggered PM [selects:: Max/Min] combine planned and unplanned demand, statistical setting (RBMM p.236)
- Condition Monitoring [produces:: CM-Planned] (RBMM p.241)
- Stock Decision [depends_on:: Lead Time] stock if Lead Time longer than time left before unplanned failure (RBMM p.241)
- Fast Moving [selects:: [[EOQ and Reorder Point]]] Fast Moving Method, Max/Min, Safety Stock, Confidence Level, EOQ (RBMM p.238)
- Low Criticality [selects:: [[Spare Part Demand Forecasting]]] Fast Moving or Average Usage Method (RBMM p.238)
- Medium Criticality [selects:: Average Usage Method] or Demand Simulation; Max/Min, Cost Ratio (RBMM p.238)
- High Criticality [selects:: [[Monte Carlo Maintenance Simulation]]] Demand Simulation Extended linked to maintenance plan (RBMM p.238)
- Consolidation [step_of:: Supply Side] box 6 (RBMM p.238)
- Criticality Assessment Box [step_of:: Supply Side] box 1, equipment and part criticality (RBMM p.238)
- Stock Turnover Rate [has_formula:: value of parts issued / total value of parts in store] low = Write-off risk (RBMM p.239)
- Stock Service Rate [has_formula:: items issued / items requested] alias Service Factor (RBMM p.239)
- Stock Service Rate [alias_of:: Service Factor]
- Stock out Rate [has_formula:: quantity not issued / total quantity requested] (RBMM p.239)
- Stock Value / Asset Replacement Value [has_formula:: total spare value / asset replacement value] (RBMM p.239)
- Stock Turnover Rate [is_a:: [[Maintenance KPIs]]]
- Stock Service Rate [is_a:: [[Maintenance KPIs]]]
- Stock out Rate [is_a:: [[Maintenance KPIs]]]
- B7 Spare Part Inventory / Plant Asset [has_value:: 2.50%] actual vs budget 3.00%, book example (RBMM p.74-75)
- B8 Stock Turn Ratio [has_value:: 40.00%] actual vs budget 44.07% (RBMM p.74-75)
- B9 Service Factor [has_value:: 97.10%] actual vs budget 99.00% (RBMM p.74-75)
- B10 Stock Out Rate [has_value:: 2.50%] actual vs budget 1.00% (RBMM p.74-75)
- B7 Spare Part Inventory / Plant Asset [has_value:: 1-3%] target of machine price (RBMM p.295, p.314)
- B7 Spare Part Inventory / Plant Asset [part_of:: [[Maintenance Strategic Report]]]
- Criticality A [has_value:: more than 95%] target Confidence Level (RBMM p.317-319)
- Criticality B [has_value:: 90%] target Confidence Level (RBMM p.317-319)
- Criticality C [has_value:: 80-90%] target Confidence Level (RBMM p.317-319)
- Spare Part Database [part_of:: [[CMMS]]] 3 field groups (RBMM p.100-102)
- Min Qty [part_of:: Spare Part Database] group 3, calculated field
- Max Qty [part_of:: Spare Part Database] group 3, calculated field
- Reorder Point [part_of:: Spare Part Database] group 3, calculated field
- EOQ [part_of:: Spare Part Database] group 3, calculated field
- Spare Parts [part_of:: BOM] not in equipment hierarchy (RBMM p.98)
- [[Failure Data Recording]] [input_to:: Spare Optimization] Failure Mode, Object Part, Cause from Work Order (RBMM p.96)
- Lead Time [has_value:: 20% reduction halves average stock] book claim, unproven (RBMM p.247) [confidence:: low]
- Blanket Order [applies_to:: CM-Unplanned] vendor stock in our store, billed on issue (RBMM p.289, p.298)
- Consolidation [uses:: [[Monte Carlo Maintenance Simulation]]] multi-user Max/Min cannot be summed (RBMM p.265-266)
- Spare Part DSx Model [uses:: [[Failure Mode]]] needs Equipment, Failure Mode, Beta, Eta (RBMM p.263)
- [[OREDA]] [input_to:: Basic Average Method] constant item failure rate, not for PM interval
- Spare Level Setting [depends_on:: [[Redundancy and Standby Systems]]] standby compressors, hidden failure
- Material Take-off [uses:: Stock Reservation] CMRP planner reserves stock items for planned jobs and stages them (CMRP CMPR-09 p.30-31)
- Stock Reservation [differs_from:: Stock Parts] CMRP allows stock for planned work; RBMM reserves stock for CM-Unplanned (RBMM p.45, p.236); policy difference, not contested
- Staging [applies_to:: Direct Purchase Parts] also low-stock and fast-moving items (CMRP CMPR-09 p.31)
- [[Spare Parts Management]] [related_to:: [[Spare Parts Optimization Book]]] stores, purchasing and accounting viewpoint (SPO)
- [[Spare Parts Management]] [related_to:: [[SPO vs RBMM Spare Parts Approaches]]]
- [[MRO Material Classification]] [part_of:: [[Spare Parts Management]]] SPO 9 categories (SPO p.26-31)
- [[Parts Interchangeability]] [part_of:: [[Spare Parts Management]]] SPO chapter 6 (SPO p.59-62)
- [[Spare Parts Recommendation by Equipment Type]] [input_to:: Stock Decision] Engineering Basic Practice starting quantities (SPO p.40-54)
- [[Warehouse Design and Storage]] [part_of:: [[Spare Parts Management]]] SPO chapters 2 and 7
- [[Tool Crib and Warehouse Security]] [part_of:: [[Spare Parts Management]]] SPO chapters 11-12
- [[MRO Purchasing and Contracting]] [part_of:: [[Spare Parts Management]]] SPO chapter 8 (SPO p.90-95)
- [[MRO Inventory Control Methods]] [part_of:: Supply Side] SPO 6 reorder control methods (SPO p.102-110)
- [[Inventory Turnover and GPI Benchmarks]] [related_to:: [[Maintenance KPIs]]] SPO turnover, MOS, % GPI (SPO p.112-115)
- [[MRO Inventory Reduction Program]] [uses:: ABC Analysis] ABU basis (SPO p.115-118)
- Holding Cost [has_value:: 30%] SPO example, not contested; SPO recommends computing COP (SPO p.104, p.120)
- Cost of Possession [alias_of:: Holding Cost] 7 cost items (SPO p.104, p.143-145)
- Commissioning Spare Part [defined_in:: [[Spare Parts Optimization Book]]] contractor responsibility, owner may buy at end (SPO p.30-31)
- Stock Parts [applies_to:: Routine Maintenance] SPO warehouse policy; overhaul and turnaround planned separately (SPO p.55)
- Blanket Order [differs_from:: Consignment] SPO terminology; RBMM Blanket Order matches SPO consignment (SPO p.91-95; RBMM p.289, p.298)
- Stock Decision [depends_on:: 7 Stocking Factors] SPO (SPO p.129)
- B7 Spare Part Inventory / Plant Asset [has_value:: 1-3%] RBMM target of machine price (RBMM p.295, p.314); reference only, not adopted
- Inventory Value % GPI [has_value:: not above 4%] SPO target for capital intensive plants (SPO p.115); adopted by user 2026-10-27
- Inventory Value % GPI [contradicts:: B7 Spare Part Inventory / Plant Asset] SPO 3-4% vs RBMM 1-3%; resolved 2026-10-27, follow SPO (SPO p.143-145)
- [[Spare Parts Management]] [related_to:: [[Maintenance Profit Maker Book]]] chapters 5 and 12 (MPM p.83-90, p.216-221)
- Spare Parts Stock [has_value:: 3-5% of machine price] average in industrial countries, review index not target; user target stays SPO not above 4% GPI (MPM p.84-85)
- Holding Cost [has_value:: 20-40%] of stocked spare value, MPM-C1 (MPM p.84) [contested:: true]
- MPM Holding Cost 20-40% [contradicts:: Holding Cost] RBMM 15-20% per year (RBMM p.16, p.34, p.234); MPM-C1 [contested:: true]
- MPM Finance Cost Example [has_value:: 6-10%] finance cost only, 6% (p.17), 10% WACC (p.108, p.180-181); narrower scope than holding cost, MPM-C1 [contested:: true]
- MPM Spare Goals [has_value:: 4 goals] min stock level, max service level, max turnover, max plant availability (MPM p.84; RBMM p.101)
- Service Level [has_formula:: lines fully issued / total lines requested] MPM line fill rate (MPM p.86)
- Spare Parts Distribution [depends_on:: [[Criticality Assessment]]] distribution matters more than total % (MPM p.85)
- Spare Part Improvement Strategy [has_value:: 5 strategies] usage, stocking, procurement, performance measurement, evaluation (MPM p.89-90)
- Spare Improvement Payback [has_value:: 1 year] invest 3-5 M THB, save 10-15% of > 30 M THB spares; 3-4.5 M per year derived (MPM p.90)
- Spare Parts [has_value:: 60-70%] share of maintenance cost, also > 50% elsewhere in MPM (MPM p.90, p.159, p.216)
- Fast Moving Spares [has_value:: 20%] Quantitative Inventory Management (Fig 12.7, MPM p.218)
- Optimizable Spares [has_value:: 60%] Qualitative Inventory Management (Fig 12.7, MPM p.218)
- Insurance Items [has_value:: 20%] hard to improve (Fig 12.7, MPM p.87, p.218)
- Spare Optimization Saving [has_value:: 10-20%] main target moving items; > 20% if never managed (MPM p.217)
- Abnormal Spare Consumption [has_cause:: Poor Original Design] also wrong installation, off-spec operation, poor part quality, poor repair quality, unsuitable PM/CM/PdM strategy (MPM p.219)
- Abnormal Spare Consumption [resolved_by:: [[Root Cause Analysis]]] failure RCA on CMMS top-10 spare cost report (MPM p.219)
- Spare Part Optimization System [has_value:: 5 zones] risk vs impact; decision belongs to management (MPM p.219-221)
- Low Risk High Impact Zone [selects:: External Insurance Policy] when part very expensive (MPM p.220)
- Medium Risk High Impact Zone [selects:: Insurance Part] insurance usually unavailable (MPM p.220)
- High Risk Zone [selects:: Stock Parts] must stock (MPM p.220)
- Spare Part Optimization System [differs_from:: [[CMMS]]] needs part-machine links, production impact, criticality (MPM p.219-220)

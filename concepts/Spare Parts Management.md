---
title: Spare Parts Management
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [spare-parts, maintenance-management, cmms, kpi, cost, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
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

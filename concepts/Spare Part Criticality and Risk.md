---
title: Spare Part Criticality and Risk
created: 2026-10-20
updated: 2026-10-28
type: concept
tags: [spare-parts, criticality, cost, maintenance-management, book, cmrp, spo, inventory-control, mpm]
sources: [reliability-based-maintenance-management.md, cmrp.md, spare-parts-optimization.md, maintenance-profit-maker.md]
confidence: medium
contested: false
---

# Spare Part Criticality and Risk

หน้านี้สรุปวิธีของ RBMM บทที่ 9 ในการตัดสินว่า "อะไหล่ตัวไหนควรสต็อก และสต็อกเท่าไรจึงคุ้มความเสี่ยง" เริ่มจาก ABC Analysis ตาม turnover, จัด Part Criticality (Price, Lead Time, ตรวจจับอาการเสียได้หรือไม่) ร่วมกับ Equipment Criticality (Commercial, Safety, Environment) แล้วใช้ Confidence Level และ Cost Ratio ตัดสินระดับสต็อกภายใต้ policy ที่ฝ่ายบริหารกำหนด ภาพรวมของการบริหารอะไหล่อยู่ใน [[Spare Parts Management]]

## ขั้นตอน Supply Side 5 ข้อ (RBMM p.241-242)

1. คัดกรองตาม Turnover ด้วย ABC Analysis
2. จัดอะไหล่ตาม Part Criticality
3. ทำตารางความสัมพันธ์ criticality อะไหล่-เครื่องจักร
4. ประเมินความเสี่ยงและบริหารความเสี่ยง
5. คำนวณระดับสะสม (EOQ; ค่าเฉลี่ย + Safety Stock; Simulation) ดู [[EOQ and Reorder Point]], [[Spare Part Demand Forecasting]]

## ABC Analysis ตาม Turnover (RBMM p.242-243)

Turnover = Qty x Unit Price (มูลค่าเบิกใช้)

| กลุ่ม | ความหมายตามหนังสือ | สัดส่วนมูลค่า turnover |
|---|---|---|
| A | มูลค่า turnover สูง (รูปที่ 9.4 ติดป้าย very slow ซึ่ง resolve แล้วว่าผิด ดูด้านล่าง) | ส่วนแรกถึง 80% ของ total |
| B | หมุนเวียนปานกลาง | 15% ถัดไป (สะสมถึง 95%) |
| C | หมุนเวียนเร็ว (fast moving) | 5% สุดท้าย (หลายรายการมูลค่าต่ำ) |

- ข้อควรระวังความไม่สอดคล้องในต้นฉบับ: ข้อความหน้า 242 บอกว่า A คือรายการที่มีมูลค่า turnover สูงสุด 80% แต่รูปที่ 9.4 ติดป้าย A = Very Slow และ C = fast moving จึงต้องอ่านว่า "A = กลุ่มมูลค่าสูงที่หมุนช้า" อย่างระวัง (คำอธิบายนี้เป็นการตีความ confidence medium) ชื่อ A/B/C ในหัวข้อนี้เป็นเรื่อง turnover คนละเรื่องกับ criticality A/B/C ของเครื่องจักร
  - ผู้ใช้ตัดสิน 2026-10-27: ยึดตาม SPO คือ A = มูลค่าใช้สูง ป้าย Very Slow ในรูปที่ 9.4 ของ RBMM ถือเป็นความผิดพลาดของรูป (resolved)
- ABC ไม่คำนึงถึงความวิกฤติ; turnover มี 2 ตัวแปร (qty, price) รายการหมุนสูงราคาต่ำหรือหมุนต่ำราคาสูงอาจอยู่ผิดกลุ่ม
- ควรคิดแยกอะไหล่ซื้อตรง (PM) ออกจากอะไหล่สำรองคลัง

## Part Criticality และ Equipment Criticality

### Part Criticality (RBMM p.243)

เกณฑ์ 3 ข้อ เป็นความสำคัญของตัวอะไหล่เอง ไม่คำนึงว่าใช้ที่ไหน:

| เกณฑ์ | ความหมาย | คะแนน |
|---|---|---|
| Price (COST) | ราคาสูงต้องหาแหล่งซื้อถูก | 1 = สูงสุด, 2 = กลาง, 3 = ต่ำ |
| Lead Time (LT) | ยาว = ต้องเร่งกระบวนการจัดซื้อ | 1 = สูงสุด, 2 = กลาง, 3 = ต่ำ |
| Failure Detect-ability (CBM) | คะแนนต่ำ = ตรวจอาการล่วงหน้าไม่ได้ เสียโดยไม่มีสัญญาณ | 1 = สูงสุด, 2 = กลาง, 3 = ต่ำ |

คะแนนตาม RBMM p.245 รูปที่ 9.6 ตามที่เขียนในหนังสือ ทิศทางของคะแนน CBM ในบันทึกอธิบายว่า "คะแนนต่ำ = ตรวจล่วงหน้าไม่ได้" จึงควรยืนยันกับหน้าหนังสือก่อนนำไปใช้

### Equipment Criticality (RBMM p.243-244)

| กลุ่ม | ความวิกฤติ | ผลเมื่อเสีย |
|---|---|---|
| A | สูงมาก | กระบวนการผลิตหยุด เสียหายสูง |
| B | ปานกลาง | เสียหายปานกลาง |
| C | ต่ำ | เสียหายต่ำ |

ประกอบด้วย 3 มิติ: Commercial, Safety, Environment (รูปที่ 9.5, RBMM p.244) ดู [[Criticality Assessment]] และ [[FMECA]]

### อะไหล่ใช้เฉพาะ vs ใช้ร่วม (RBMM p.244)

- Specific usage (อะไหล่ X, Y, Z ใช้เฉพาะเครื่อง High/Medium/Low): แยกบริหารงานตามแผน (JIT) กับนอกแผน (ตามความเสี่ยง)
- Common usage (อะไหล่ P, Q, R ใช้ร่วมสองระดับ; W ใช้ทุกระดับ): ตั้ง Max/Min, Safety Stock รวมงานตามแผนและนอกแผนได้ แต่ต้องตอบสนองเครื่องวิกฤติเป็นอย่างน้อย
- กฎ: อะไหล่ใช้ร่วมเครื่องที่ criticality ต่างกัน ใช้ criticality ของเครื่องที่สูงสุด; ที่ระดับเครื่องเท่ากัน ใช้ criticality ของตัวอะไหล่เปรียบเทียบกัน

### ตารางความสัมพันธ์อะไหล่-เครื่องจักร (RBMM p.245-246, รูปที่ 9.6)

- คอลัมน์: Code, Description, EQ Criticality (A, B, C = จำนวนชิ้นที่ใช้ในเครื่องวิกฤติระดับนั้น สร้างจาก BOM), Part Criticality (COST, LT, CBM), On hand, Unit cost, Max, Min (ตัวเลขรายแถวในภาพอ่านไม่ออก)
- ใช้ sort ตามต้องการ (ราคา -> LT -> CBM) หรือเริ่มที่ Equipment Criticality A
- คอลัมน์ A/B/C ไม่เป็นศูนย์ = ใช้ในเครื่องวิกฤตินั้น; CBM = ตรวจว่ามีงาน Condition Monitoring PM ครบหรือยัง
- เป็นขั้นตอนพื้นฐานที่ต้องทำก่อนวิเคราะห์ระดับอะไหล่

## จัดกลุ่มเพื่อเลือกวิธีคำนวณ (RBMM p.238)

| กลุ่ม | วิธี | เครื่องมือ |
|---|---|---|
| Fast Moving | EOQ + demand variance | [[EOQ and Reorder Point]] |
| Low Criticality | Average Usage / Poisson / Confidence | [[Spare Part Demand Forecasting]] |
| Medium Criticality | Average Usage หรือ Monte Carlo | Cost Ratio |
| High Criticality | Monte Carlo เชื่อมแผน PM (DSx) | Cost Ratio ดู [[Monte Carlo Maintenance Simulation]] |

## เครื่องมือวัดความเสี่ยง 2 แบบ (RBMM p.246-251)

เพิ่มระดับสะสม ลดความเสี่ยง แต่เพิ่ม fixed cost

### 1) Confidence Level

เปอร์เซ็นต์ความมั่นใจว่าในช่วง Lead Time ที่เบิกแต่ละครั้งจะมีอะไหล่ใช้ (RBMM p.246)

```
Risk of Stock out = 1 - Confidence
```

(RBMM p.249) ตัวอย่างค่า Z ดูใน [[EOQ and Reorder Point]]

เป้า Confidence ตาม criticality ของเครื่องจากบทที่ 10: A มากกว่า 95%, B 90%, C 80-90% (RBMM p.317-319); เครื่อง High ในบทที่ 1 ตั้งเป้า 100% service level, 0% stock out (RBMM p.24-26)

### 2) Cost Ratio

```
Cost Ratio = Expected Cost of Stock out / Expected Cost of Stock
```

(RBMM p.246, p.249) ตัวอย่างจุด C ในรูปที่ 9.9: Max/Min = 3/2, stock out cost 600,000 บาท/ครั้ง, expected cost of stock = 98,360.65 บาท ได้ Cost Ratio = 600,000 / 98,360.65 = 6.1 (ตรวจเลขแล้วตรงกับหนังสือ)

- ลดสต็อก -> Cost Ratio สูงขึ้น (โอกาสขาดเพิ่ม); เพิ่มสต็อก -> ratio ลดเข้าหา 1.0
- ratio = 1: ค่าขาด = ค่าเก็บ ไม่คุ้มสะสมเพิ่ม; ต่ำกว่า 1 = เหลือค้างมาก
- ratio < 1 ไม่ควรเก็บ ยกเว้นค่าสูญเสียต่อครั้งสูงมากจนบริษัทรับไม่ได้ = Insurance Part

### โซนในรูปที่ 9.9 (RBMM p.249-251)

| โซน | เงื่อนไข | ผู้ปฏิบัติตาม policy |
|---|---|---|
| Mandatory Stock Zone | Cost Ratio สูง (ประมาณมากกว่า 9) | สะสมได้เลย ไม่ต้องขออนุมัติ |
| Stock with Approval Zone (Risk Based Optimum Zone) | ratio ระดับกลาง | สะสมโดยอนุมัติตามระดับบริหารที่ policy กำหนด |
| No Stock Zone | ratio ไม่เกิน 1 (stock cost มากกว่าหรือเท่ากับ stock out cost) | ไม่ควรสะสม |
| Insurance Part | ค่าขาดต่อครั้งเกินเกณฑ์ (ตัวอย่าง 1,100,000 บาท) แม้ ratio < 1 | สะสมได้โดยขออนุมัติระดับบริหาร |

เกณฑ์ ratio ประมาณ 9 และ 1.1 ล้านบาท อ่านจากกราฟในหนังสือ (ค่าประมาณ ไม่ใช่ข้อกำหนดตายตัว) การ implement ต้องมี 4 ข้อ: นโยบายความเสี่ยง, เครื่องมือคำนวณเชิงสถิติจากข้อมูลจริง, กระบวนการอนุมัติ, กระบวนการจัดหา/เติม (RBMM p.252) (หนังสือติดป้าย ISO ที่ข้อ 2-4 แต่ไม่ได้อธิบาย)

## ตัวอย่างผล Monte Carlo ของอะไหล่

### High Criticality (RBMM p.263-264, รูปที่ 9.20)

| Max/Min | ครั้งขาด | สต็อกเฉลี่ย | Cost Ratio | ค่ามีอะไหล่ | ค่าขาด | รวม (บาท) |
|---|---|---|---|---|---|---|
| 3/2 | 3.12 | 1.04 | 20.30 | 10,859.96 | 220,475.56 | 440,535.90 |
| 4/2 | 1.10 | 1.67 | 3.80 | 17,104.75 | 65,065.59 | 283,018.01 |
| 5/4 | 0.51 | 2.47 | 1.07 | 26,808.45 | 28,664.06 | 258,502.81 |
| 5/3 | 0.40 | 2.45 | 0.85 | 25,960.40 | 22,104.61 | 251,209.31 |
| 6/4 | 0.19 | 3.34 | 0.30 | 36,692.15 | 11,085.00 | 248,470.42 |

(เลือกบางแถวจาก 7 แถว; แถว 6/- และ 6/5 ดูต้นฉบับ) ตรวจ Cost Ratio = ค่าขาด / ค่ามีอะไหล่ ตรงกับหนังสือทุกแถวที่เลือก (derived check) ข้อเสนอของหนังสือ:

- ไม่ควรเก็บ Max/Min ใต้กลุ่มแรเงา (ratio ต่ำกว่า 1) เว้นแต่เป็น Insurance Part
- ถ้าถือเป็น Insurance Part เก็บ 5/2 (ratio ลดเหลือใกล้ 1.0)
- ถ้าค่าขาดต่อครั้งไม่เกินกำหนด น่าเก็บ 4/2 เพราะต้นทุนรวมต่ำสุด (ratio 3.8) แต่ต้องเช็คว่า policy ให้ใครอนุมัติที่ ratio 3.8
- (หมายเหตุ: ใน 7 แถว ต้นทุนรวมต่ำสุดที่อ่านได้คือ 6/4 = 248,470.42 ขัดกับข้อความ "4/2 ต้นทุนรวมต่ำสุด" เล็กน้อย เป็นข้อสังเกตของผู้สรุป ตัวเลขอ่านจากภาพความละเอียดต่ำ ให้ยึดข้อความหนังสือเป็นหลักและตรวจกับต้นฉบับ)

### Medium Criticality (RBMM p.261-262, รูปที่ 9.19)

ตัวอย่างบางแถว:

| Max/Min | ครั้งที่ขาด | Cost Ratio | ค่ามีอะไหล่ | ค่าขาด |
|---|---|---|---|---|
| 4/1 | 2.45 | 36.69 | 9,191.56 | 559,097.90 |
| 5/2 | 0.26 | 2.17 | 18,223.64 | 45,720.86 |
| 6/2 | 0.18 | 1.77 | 18,431.48 | 40,515.35 |
| 6/5 | 0.03 | 0.01 | 25,549.04 | 248.87 |

- หนังสือแนะนำ 5/2 (กลุ่มน่าสนใจ 5/4, 5/3, 5/2, 6/2; ratio มากกว่า 1.0 พอสมควร อนุมัติง่ายกว่า ต้นทุนรวมไม่ต่างกันมาก)
- ข้อควรระวังข้อมูล: อัตราส่วน ค่าขาด / ค่ามีอะไหล่ ที่คำนวณเองไม่ตรงกับคอลัมน์ Cost Ratio ในหลายแถว (เช่น 4/1 ได้ประมาณ 60.8 vs 36.69; 5/2 ได้ประมาณ 2.51 vs 2.17) ขณะที่แถว 6/5 ตรง (ประมาณ 0.01) อาจเป็นเพราะ Cost Ratio ใช้นิยาม expected cost คนละฐาน หรืออ่านภาพผิด ต้องตรวจกับต้นฉบับ ตัวเลขนี้ derived confidence low
- คอลัมน์ "รวมค่าใช้จ่ายทั้งสิ้น" ในต้นฉบับสูงกว่าผลรวมสองคอลัมน์มาก น่าจะรวมค่าอะไหล่ที่ใช้ด้วย จึงไม่ลงในตารางนี้

## ข้อสังเกตเชิงปฏิบัติ

- ถ้า P-F interval ของ failure mode สั้นกว่า Lead Time ของอะไหล่ ต้องสต็อกอะไหล่ (RBMM p.241)
- ตารางอะไหล่-เครื่องจักรต้องสร้างจาก BOM จึงต้องมี codification มาตรฐานและกำจัดรายการซ้ำ (RBMM p.240)
- ต้องมีนโยบายและอำนาจอนุมัติตามโซน มิฉะนั้นตัวเลขความเสี่ยงไม่ถูกนำไปใช้ (Accountability RBMM p.271)

## มุมมอง CMRP: ผังตัดสินสต็อกและ risk cost vs holding cost (เพิ่ม 2026-10-25)

สไลด์ [[CMRP Course]] ให้แนวทางที่สอดคล้องกับ RBMM ในหลักการ (ชั่งความเสี่ยงขาดของกับต้นทุนถือครอง) แต่ใช้กฎง่ายกว่า ไม่ขัดกัน

### Top-down และผังตัดสินใจ "ควรสต็อกไหม" (CMRP CMPR-03 p.12-13; ซ้ำใน CMPR-08 p.28)

- Top-down: criticality study -> critical systems -> critical equipment -> critical failures -> spares required (CMRP CMPR-03 p.12)

| กรณี | ผล |
|---|---|
| ซ่อมได้โดยไม่ใช้อะไหล่ | ไม่สต็อก |
| ไม่วิกฤติต่อ availability (production)/safety/environment | ไม่สต็อก |
| failure ทำให้ต้องสลับไปตัวสำรอง (standby) | ไม่สต็อก **เว้นแต่** lead time มากกว่า 2 สัปดาห์ จึงสต็อก |
| วิกฤติต่อ availability/safety/environment | สต็อก |

- กรณีสลับตัวสำรอง: เหตุผลโดยนัยคือ ระหว่างรออะไหล่ ระบบเดินบนตัวสำรองตัวเดียวโดยไม่มี redundancy ถ้า lead time ยาว ความเสี่ยงที่ตัวสำรองจะเสียด้วยสูงขึ้น (การตีความของ wiki) ดู [[Redundancy and Standby Systems]]
- เกณฑ์ 2 สัปดาห์เป็นตัวเลขตัวอย่างของสไลด์ ไม่มีที่มา ควรปรับตาม MTBF ของตัวสำรอง
- เทียบ RBMM: กฎ "ถ้า P-F interval สั้นกว่า lead time ต้องสต็อก" (RBMM p.241) ใช้ lead time เป็นตัวตัดสินเช่นกัน แต่เทียบกับ P-F แทนเกณฑ์คงที่

### Total stock cost = risk cost + holding cost (CMRP CMPR-03 p.13)

- เส้นโค้ง total cost = **risk cost** (ลดลงเมื่อสต็อกมากขึ้น) + **holding cost** (เพิ่มขึ้น) มีจุดต่ำสุดที่ระดับสต็อกเหมาะสม
- Risk Cost = Probability x Penalty ของการไม่มีของเมื่อต้องการ; Holding Cost = f(cost of capital, depreciation, supply base overhead); สไลด์อ้าง SPARO (Spare Parts Alignment Rationalization and Optimization)
- Optimisation อื่น: level of repair analysis (สต็อกอะไร), interchangeability (OEM), sharing/pooling, risk-based analysis ตั้งระดับสต็อก
- เทียบ RBMM: Cost Ratio = expected cost of stock out / expected cost of stock (หัวข้อ "เครื่องมือวัดความเสี่ยง") คือการเทียบสองพจน์เดียวกันในรูปอัตราส่วน ส่วน CMRP หาจุดต่ำสุดของผลรวม (การเทียบเป็น derived) จุด ratio = 1 ใน RBMM เป็นจุดที่ค่าขาดเท่ากับค่าเก็บ ไม่จำเป็นต้องเป็นจุด total cost ต่ำสุด

### Risk-based spares และ capital spares model (CMRP CMPR-08 p.28-31)

- เชื่อมกับ Maintenance Strategy Review: MEL -> failure + BOM -> ประเมินความเสี่ยงและจัดชั้นอะไหล่ -> strategy/task -> Level of Repair Analysis -> order quantity -> integrated planning (CMRP CMPR-08 p.28)
- อะไหล่ราคาสูง lead time ยาว: ตีค่าเป็นเงินจาก risked cost (production, safety, environment, secondary damage) สมมติฐาน exponential, อะไหล่ที่เสียไม่ซ่อม, ไม่คิด discounting; input: demand rate, lead time, standby configuration, จำนวนติดตั้ง, ราคา, ค่าคลัง, consequential cost, repair lead time (p.29-30)
- กราฟตัวอย่าง (p.30): สต็อก 1 ชิ้นมี risk cost สูงมาก (ราว 19,500) ต่ำสุดที่ 2 ชิ้น จากนั้นต้นทุน interest/warehouse/write-off โตเชิงเส้น
- **Capital spares** (p.31) ช่วงเวลา T: non-availability cost = c_na x F(T); storage cost = c_l x ∫0..T R(t)dt; dead stock cost = c_s x R(T); สต็อกเมื่อ c_na x F(T) มากกว่า storage + dead stock cost (สัญลักษณ์บนสไลด์อ่านยาก และเงื่อนไขกรณี n systems อ่านไม่ออก confidence ต่ำ) เป็นรูปแบบต่อเนื่องของ Insurance Part ในโซนของ RBMM: อะไหล่ที่ใช้ไม่บ่อยแต่ค่าขาดสูง
- รายละเอียด MRO inventory ดู [[Spare Parts Management]]

## มุมมอง SPO: insurance/standby และ ABC (เพิ่ม 2026-10-27)

ส่วนเสริมจาก [[Spare Parts Optimization Book]] (SPO) การเทียบเต็มดู [[SPO vs RBMM Spare Parts Approaches]]

### Insurance and Standby Parts (SPO p.26-27)

- ที่มา 2 ทาง: (ก) อะไหล่ของ **เครื่อง standby ที่ติดตั้งคู่** กับเครื่องหลัก หยุด A เปิด B แล้วนำ A ไปซ่อม จึงต้องมั่นใจว่ามีอะไหล่แน่นอน ซ่อมเสร็จ A กลายเป็น standby และต้องสั่งอะไหล่ที่ใช้ไปเข้าแทน; หน่วยที่สำคัญมากอาจมี standby ถึง 3 ชุด (A/B/C) (ข) อะไหล่สำคัญที่ขาดแล้วซ่อมไม่ได้จนโรงงานหยุด เลือกโดยวิศวกรซ่อมบำรุงร่วมกับฝ่ายผลิต ผู้ขายแนะนำได้แต่วิศวกรของเราตัดสิน
- เครื่องแบบเดียวกันมักเสียชิ้นเดิมซ้ำ จึงกำหนดรายการจากสถิติการเบิกเปลี่ยนได้
- ใส่ **รหัสต่อท้าย "S"** ในรายการวัสดุ เพื่อเรียกดูเฉพาะอะไหล่ประกันได้ตลอด
- การควบคุม: Order Up-to (เบิกเท่าไรสั่งแทนเท่านั้น) หรือ Min-Max ที่คณะกรรมการอนุมัติ (SPO p.109-110); ราคาสูงต้องผ่านคณะกรรมการ (SPO p.55-57, p.131-132); ถ้าราคาสูงและอายุเกิน 1 ปีอาจ capitalize (SPO p.28-29)
- เทียบ RBMM: Insurance Part ของ RBMM นิยามแคบกว่า (ค่าขาดต่อครั้งสูงจนเก็บแม้ Cost Ratio ต่ำกว่า 1) แต่ทั้งสองเล่มให้ระดับบริหารอนุมัติ; เทียบ CMRP: ผังตัดสินของ CMRP ไม่สต็อกกรณีสลับตัว standby เว้นแต่ lead time มากกว่า 2 สัปดาห์ (หัวข้อ CMRP ข้างบน) ต่างจาก SPO ที่ให้มีอะไหล่ของคู่ A/B เสมอ อธิบายได้ด้วยบริบท lead time ยาวของอะไหล่นำเข้าในโรงงานไทย (การตีความของ wiki; ไม่ contested) ดู [[Redundancy and Standby Systems]]

### ABC ของ SPO และความขัดแย้งเรื่องป้ายกลุ่ม A (SPO p.115-118)

- SPO ใช้ฐาน **ABU (Annual Baht Usage) = จำนวนเบิกต่อปี x ราคาต่อหน่วย** ซึ่งเท่ากับ Turnover ของ RBMM และใช้สัดส่วน 80/15/5 เหมือนกัน (ปรับเป็น 75/20/5 หรือ 70/20/10 ได้)
- ตัวอย่าง 10 รายการของ SPO: กลุ่ม A (3 รายการแรก, ราว 80% ของมูลค่า) มีรายการที่เบิก 200,000 และ 1,210,000 หน่วยต่อปี จึงเป็นกลุ่ม **มูลค่าใช้สูง** ไม่ได้แปลว่าหมุนช้า
- SPO ใช้ ABC เพื่อลดสต็อก (กลุ่ม C จำนวนมากเปลี่ยนเป็น OAR, รายการไม่เคลื่อนไหว 3 ปีถือว่าล้าสมัย) ไม่ได้ใช้คัดกรอง criticality ดู [[MRO Inventory Reduction Program]]
- **ข้อขัดแย้ง (resolved 2026-10-27)**:
  - มุมมอง SPO (spare-parts-optimization.md): A = มูลค่าใช้สูง (SPO p.115-117)
  - มุมมอง RBMM (reliability-based-maintenance-management.md): ข้อความ p.242 ให้ A = มูลค่า turnover สูงสุด (ตรงกับ SPO) แต่รูปที่ 9.4 ติดป้าย A = Very Slow (RBMM p.243) ตามที่บันทึกในหัวข้อ ABC ข้างบน
  - สถานะ: ยังไม่ resolve; ข้อความของสองเล่มตรงกัน ป้ายในรูป RBMM น่าจะผิด แต่ยังไม่ได้ตรวจกับต้นฉบับ RBMM ระหว่างนี้ให้อ่าน A ว่า "มูลค่าใช้สูง" (ข้อความเดิมก่อน resolve)
  - ผู้ใช้ตัดสิน 2026-10-27: ยึดตาม SPO คือ A = มูลค่าใช้สูง ป้าย Very Slow ในรูปที่ 9.4 ของ RBMM ถือเป็นความผิดพลาดของรูป (resolved)

## มุมมอง MPM: บทบาทอะไหล่ตามความวิกฤต และ SOS (เพิ่ม 2026-10-28)

ที่มา: [[Maintenance Profit Maker Book]] บทที่ 5, 10, 12

### สัดส่วนเครื่องตามความวิกฤตและระดับการสนับสนุน (Fig 5.1, MPM p.85)

| กลุ่มเครื่อง | สัดส่วน | บทบาทของอะไหล่ |
|---|---|---|
| วิกฤตสูงสุด | ~20% แรก | สนับสนุนด้วยอะไหล่ **เกือบ 100%** + Inspection/RBI, RCM/FMEA |
| วิกฤตปานกลาง | ~50% | เน้นงานเชิงรุก วิเคราะห์ ทำนายการเสียด้วย Reliability Engineering มากกว่าสะสมอะไหล่ |
| วิกฤตต่ำ | ~30% | ไม่สะสมมาก จัดหาเมื่อต้องการหรือจ้างเหมา (บางเครื่องให้ OEM) ซ่อมเชิงรับ |

- ผัง (อ่านจากรูป): Asset Register -> วิเคราะห์ความวิกฤต -> จัดอันดับ (ทบทวนสม่ำเสมอ) -> แยกตามความแน่นอนของอายุ/เงื่อนไข -> โปรแกรมบริหารอะไหล่และพยากรณ์ -> reliability/availability/maintainability ดีขึ้น; ความสัมพันธ์ลูกศรบางส่วนอ่านไม่ออกจาก OCR
- **สัดส่วนต่างกัน (ไม่ใช่ contested)**: MPM p.85 ให้ สูง/กลาง/ต่ำ = 20/50/30 ขณะที่ MPM p.250 ของเล่มเดียวกันและ RBMM Fig 1.4 ให้ A/B/C = 30/50/20 (RBMM p.23-25) ทั้งหมดเป็นตัวอย่าง ไม่ใช่มาตรฐาน สัดส่วนจริงต้องมาจากการประเมินของโรงงานเอง ดู [[Criticality Assessment]]
- การสนับสนุน "เกือบ 100%" ของกลุ่มสูงสุดสอดคล้องกับเป้า 100% service level ของเครื่อง High ใน RBMM บทที่ 1 (RBMM p.24-26) ข้างบน

### Service level ที่ MPM ตั้งเป้า (MPM p.86, p.170)

- สูตร: จำนวนรายการที่เบิกได้ครบ / จำนวนรายการที่เบิกทั้งหมด (MPM p.86) = Stock Service Rate ของ RBMM
- เป้าทั้งคลัง: ความพร้อมอะไหล่ **> 95%** ภายใต้เงื่อนไขคงคลังต่ำสุดและหมุนเวียน > 90% (MPM p.170) ซึ่งเป็นเป้ารวม ไม่แยกตาม criticality ต่างจาก RBMM ที่ตั้ง confidence ตามกลุ่ม (A > 95%, B 90%, C 80-90%) ดู [[Inventory Turnover and GPI Benchmarks]]

### Spare Part Optimization System (SOS) 5 โซน (MPM p.219-221)

MPM เสนอ SOS ที่ใช้ความเชื่อมโยงอะไหล่-เครื่อง ผลกระทบการผลิต และความสำคัญ เพื่อบอกความเสี่ยงของการไม่มีอะไหล่ แบ่ง 5 โซน (ตารางเต็มที่ [[Spare Parts Management]]): ต่ำ/ผลกระทบน้อย = ไม่เก็บ; ต่ำ/ผลกระทบสูง = อาจซื้อ **ประกันภายนอก (external insurance policy)** แทนถ้าอะไหล่แพงมาก; ปานกลาง/ผลกระทบสูง = insurance spares; ปานกลาง/ผลกระทบต่ำ = เก็บปกติ; สูง = ต้องเก็บ

เทียบกับโซนของ RBMM Fig 9.9 ข้างบน (การเทียบของ wiki):

| แนวคิด | RBMM (Cost Ratio) | MPM (SOS) |
|---|---|---|
| ไม่เก็บ | No Stock Zone (ratio ไม่เกิน 1) | ความเสี่ยงต่ำ ผลกระทบน้อย |
| ต้องเก็บ | Mandatory Stock Zone | ความเสี่ยงสูง |
| ค่าขาดต่อครั้งสูงมาก | Insurance Part (ขออนุมัติระดับบริหาร) | insurance spares เอง หรือ **ประกันภายนอก** (ทางเลือกใหม่ที่ RBMM/SPO/CMRP ไม่มี) |
| ผู้ตัดสิน | ตาม policy อำนาจอนุมัติ | ผู้บริหาร (ระบบบอกความเสี่ยงเท่านั้น) |

- ตัวอย่างหน้าจอ Stock Cost/Risk Assessment (Fig 12.8): แกน X = อัตราส่วน Risk ต่อ Cost of Stock (50:1, 10:1, 2:1, 1:1, 0.1), แกน Y = Cost of Stockout (< 50K ถึง > 50M) ตัวอย่าง Cost of Stock $30,000, Assessment Period 10 ปี (MPM p.220-221) แกน X ใกล้แนวคิด Cost Ratio ของ RBMM (derived)
- SOS ต้องการ Reliability Engineering และประวัติเสีย/ซ่อมครบ มิฉะนั้นลงทุนเปล่า (MPM p.221)

## เชื่อมโยงกับ compressor failure hierarchy

- Part Criticality ข้อ CBM/detect-ability คล้ายแนวคิด detectability ใน [[FMECA]] และ detection method ของ [[ISO 14224]]; Equipment Criticality (Commercial, Safety, Environment) สอดคล้องกับการจัด criticality ของเครื่อง เช่น [[Compressor]] ที่หยุดแล้วกระทบการผลิต
- จับคู่ [[Maintainable Item]] กับอะไหล่ผ่าน BOM แล้วใช้ failure mode ใน [[Failure Mode]] ระบุว่า item ใดมีการเสียโดยไม่มีสัญญาณ (detect-ability ต่ำ) เป็นแนวทางประยุกต์ ไม่ใช่ค่าที่หนังสือให้
- ใน sources ของ wiki ไม่มี Lead Time หรือราคาอะไหล่จริงของ compressor จึงไม่สามารถจัด Part Criticality ให้ item ใดได้ตอนนี้

## ดูเพิ่ม

- [[Spare Parts Management]]
- [[Criticality Assessment]]
- [[EOQ and Reorder Point]]
- [[Spare Part Demand Forecasting]]
- [[Monte Carlo Maintenance Simulation]]
- [[Failure Mode]]
- [[Redundancy and Standby Systems]]
- [[SPO vs RBMM Spare Parts Approaches]]
- [[MRO Inventory Reduction Program]]
- [[MRO Material Classification]]
- [[Maintenance Profit Maker Book]]

## Triplets

- [[Spare Part Criticality and Risk]] [defined_in:: [[Reliability Based Maintenance Management Book]]] chapter 9
- [[Spare Part Criticality and Risk]] [part_of:: [[Spare Parts Management]]] Supply Side
- ABC Analysis [step_of:: Supply Side] step 1, screen by turnover (RBMM p.241-242)
- Part Criticality [step_of:: Supply Side] step 2 (RBMM p.241-242)
- Part-Equipment Criticality Table [step_of:: Supply Side] step 3 (RBMM p.241-242)
- Risk Assessment [step_of:: Supply Side] step 4 (RBMM p.241-242)
- Stock Level Calculation [step_of:: Supply Side] step 5, EOQ / average + Safety Stock / simulation (RBMM p.241-242)
- Turnover [has_formula:: Qty x Unit Price] issue value (RBMM p.242-243)
- ABC Turnover Group A [is_a:: ABC Analysis] high turnover value, first 80% of total turnover value (RBMM p.242-243)
- ABC Turnover Group B [is_a:: ABC Analysis] medium, next 15% (cumulative 95%) (RBMM p.242-243)
- ABC Turnover Group C [is_a:: ABC Analysis] fast moving, last 5% (RBMM p.242-243)
- ABC Turnover Group A [has_category:: high value] text p.242 (RBMM p.242); resolved 2026-10-27 by user, follow SPO
- ABC Turnover Group A [contradicts:: Very Slow] label in Fig 9.4 judged wrong (RBMM p.243)
- ABC Turnover Group A [differs_from:: Criticality A] turnover grouping vs equipment criticality
- ABC Analysis [differs_from:: Part Criticality] ABC ignores criticality
- Price [part_of:: Part Criticality] COST, score 1 = highest, 2 = medium, 3 = low (RBMM p.243)
- Lead Time [part_of:: Part Criticality] LT, score 1-3 (RBMM p.243)
- Failure Detect-ability [part_of:: Part Criticality] CBM, low score = no advance warning, verify direction with book (RBMM p.243, p.245) [confidence:: low]
- Criticality A [is_a:: Equipment Criticality] very high, production stops (RBMM p.243-244)
- Criticality B [is_a:: Equipment Criticality] medium (RBMM p.243-244)
- Criticality C [is_a:: Equipment Criticality] low (RBMM p.243-244)
- Commercial [part_of:: Equipment Criticality] (RBMM p.244, Fig 9.5)
- Safety [part_of:: Equipment Criticality] (RBMM p.244, Fig 9.5)
- Environment [part_of:: Equipment Criticality] (RBMM p.244, Fig 9.5)
- Equipment Criticality [related_to:: [[Criticality Assessment]]]
- Common Usage Part [depends_on:: Equipment Criticality] use highest equipment criticality; equal level -> compare Part Criticality (RBMM p.244)
- Specific Usage Part [differs_from:: Common Usage Part] separate planned (JIT) vs unplanned (risk) management (RBMM p.244)
- Part-Equipment Criticality Table [uses:: BOM] columns EQ Criticality A/B/C, COST, LT, CBM, On hand, Unit cost, Max, Min (RBMM p.245-246, Fig 9.6)
- Fast Moving [selects:: EOQ] with demand variance (RBMM p.238)
- Low Criticality [selects:: Poisson Distribution] Average Usage / Poisson / Confidence (RBMM p.238)
- Medium Criticality [selects:: Cost Ratio] Average Usage or Monte Carlo (RBMM p.238)
- High Criticality [selects:: [[Monte Carlo Maintenance Simulation]]] linked to PM plan (DSx), Cost Ratio (RBMM p.238)
- Confidence Level [measures:: availability of part during Lead Time] (RBMM p.246)
- Risk of Stock out [has_formula:: 1 - Confidence] (RBMM p.249)
- Cost Ratio [has_formula:: Expected Cost of Stock out / Expected Cost of Stock] (RBMM p.246, p.249)
- Cost Ratio [has_value:: 6.1] point C Fig 9.9, Max/Min 3/2, 600,000 / 98,360.65 THB (RBMM p.249)
- Criticality A [has_value:: more than 95%] target Confidence Level (RBMM p.317-319)
- Criticality B [has_value:: 90%] target Confidence Level (RBMM p.317-319)
- Criticality C [has_value:: 80-90%] target Confidence Level (RBMM p.317-319)
- High Criticality [has_value:: 100% service level, 0% stock out] chapter 1 target (RBMM p.24-26)
- Mandatory Stock Zone [depends_on:: Cost Ratio] ratio above about 9 (approximate, read from graph), stock without approval (RBMM p.249-251)
- Stock with Approval Zone [depends_on:: Cost Ratio] middle ratio, approval per policy (RBMM p.249-251)
- Stock with Approval Zone [alias_of:: Risk Based Optimum Zone]
- No Stock Zone [depends_on:: Cost Ratio] ratio not above 1 (RBMM p.249-251)
- Insurance Part [depends_on:: Stock out Cost] above threshold e.g. 1,100,000 THB per event even if ratio below 1, approximate from graph (RBMM p.249-251)
- Risk Policy [part_of:: Risk Based Spare Part Optimization] implementation requirement 1 of 4 (RBMM p.252)
- Statistical Calculation Tool [part_of:: Risk Based Spare Part Optimization] requirement 2 of 4 (RBMM p.252)
- Approval Process [part_of:: Risk Based Spare Part Optimization] requirement 3 of 4 (RBMM p.252)
- Replenishment Process [part_of:: Risk Based Spare Part Optimization] requirement 4 of 4 (RBMM p.252)
- High Criticality Example [has_value:: Max/Min 4/2, Cost Ratio 3.80, total 283,018.01 THB] book recommendation if stock out cost within limit (RBMM p.263-264, Fig 9.20)
- High Criticality Example [has_value:: Max/Min 5/2] if treated as Insurance Part (RBMM p.263-264)
- High Criticality Example [has_value:: lowest total cost 4/2] book text (RBMM p.263-264)
- High Criticality Example [has_value:: lowest total cost 6/4 = 248,470.42 THB] read from table by wiki, low-res figure (RBMM Fig 9.20)
- Medium Criticality Example [has_value:: Max/Min 5/2, Cost Ratio 2.17] book recommendation (RBMM p.261-262, Fig 9.19)
- Medium Criticality Example [has_value:: Cost Ratio column mismatch] stock out / stock cost e.g. 4/1 about 60.8 vs 36.69, derived (RBMM Fig 9.19) [confidence:: low]
- Stock Decision [depends_on:: [[P-F Interval and Condition Monitoring]]] stock if P-F interval shorter than Lead Time (RBMM p.241)
- Failure Detect-ability [related_to:: [[FMECA]]] similar to detectability
- Stock Decision [depends_on:: Repair Without Spare] repairable without spare = do not stock (CMRP CMPR-03 p.13; CMPR-08 p.28)
- Stock Decision [depends_on:: Equipment Criticality] not critical to availability/safety/environment = do not stock; critical = stock (CMRP CMPR-03 p.13)
- Switch to Standby Case [depends_on:: Lead Time] stock only if lead time more than 2 weeks (CMRP CMPR-03 p.13; CMPR-08 p.28)
- Switch to Standby Case [related_to:: [[Redundancy and Standby Systems]]] running without redundancy while waiting, interpretation [confidence:: low]
- Total Stock Cost [has_formula:: Risk Cost + Holding Cost] curve with minimum at optimum stock level (CMRP CMPR-03 p.13)
- Risk Cost [has_formula:: Probability x Penalty] of not having the part when needed (CMRP CMPR-03 p.13)
- Holding Cost [depends_on:: Cost of Capital] also depreciation and supply base overhead (CMRP CMPR-03 p.13)
- Total Stock Cost [related_to:: Cost Ratio] same two terms; CMRP minimises sum, RBMM uses ratio, derived
- Risk Based Spare Review [uses:: Level of Repair Analysis] linked to Maintenance Strategy Review, MEL and BOM (CMRP CMPR-08 p.28)
- Risk Based Spare Review [has_value:: minimum at 2 spares] example graph, 1 spare risk cost about 19,500 (CMRP CMPR-08 p.30)
- Capital Spares Non-Availability Cost [has_formula:: c_na x F(T)] (CMRP CMPR-08 p.31) [confidence:: low]
- Capital Spares Storage Cost [has_formula:: c_l x integral 0..T of R(t)dt] (CMRP CMPR-08 p.31) [confidence:: low]
- Capital Spares Dead Stock Cost [has_formula:: c_s x R(T)] stock if c_na x F(T) exceeds storage plus dead stock cost (CMRP CMPR-08 p.31) [confidence:: low]
- Capital Spares [related_to:: Insurance Part] rarely used, high stock out cost, interpretation
- Insurance and Standby Parts [related_to:: Insurance Part] SPO broader: standby A/B equipment parts and critical parts (SPO p.26-27)
- Insurance and Standby Parts [has_code:: S] suffix in material list (SPO p.27)
- Insurance and Standby Parts [applies_to:: Standby Equipment] A/B pair, up to 3 sets A/B/C for very important units (SPO p.26-27)
- Insurance and Standby Parts [selects:: Order Up-to] or committee-approved Min-Max (SPO p.109-110)
- Insurance and Standby Parts [depends_on:: Materials Control Committee] high-value items need committee approval (SPO p.55-57, p.131-132)
- Insurance and Standby Parts [related_to:: [[Redundancy and Standby Systems]]]
- Insurance and Standby Parts [differs_from:: Switch to Standby Case] CMRP stocks only if lead time more than 2 weeks; context difference, not contested (CMRP CMPR-03 p.13)
- ABU [has_formula:: annual issue qty x unit cost] same basis as RBMM Turnover (SPO p.116)
- ABC Turnover Group A [has_category:: high usage value] SPO, about 80% of ABU (SPO p.115-117)
- ABC Turnover Group A [has_value:: 80 / 15 / 5 split] same in SPO and RBMM; SPO allows 75/20/5 or 70/20/10 (SPO p.115)
- ABC Analysis [related_to:: [[MRO Inventory Reduction Program]]] SPO uses ABC to cut stock and move C items to OAR (SPO p.117-118)
- [[Spare Part Criticality and Risk]] [related_to:: [[Maintenance Profit Maker Book]]] chapters 5, 10, 12
- MPM Highest Criticality Group [has_value:: about 20%] of equipment, spare support nearly 100% plus Inspection/RBI and RCM/FMEA (Fig 5.1, MPM p.85)
- MPM Medium Criticality Group [has_value:: about 50%] proactive maintenance over stocking (Fig 5.1, MPM p.85)
- MPM Low Criticality Group [has_value:: about 30%] buy when needed or outsource (Fig 5.1, MPM p.85)
- MPM Criticality Split 20/50/30 [differs_from:: Criticality Split 30/50/20] MPM p.85 vs MPM p.250 and RBMM Fig 1.4 (RBMM p.23-25); examples, not contested
- MPM Service Level [has_value:: > 95%] whole-store target, not by criticality (MPM p.170)
- Spare Part Optimization System [has_value:: 5 zones] risk of not having part vs impact (MPM p.219-221)
- Low Risk High Impact Zone [selects:: External Insurance Policy] alternative to Insurance Part when part very expensive (MPM p.220)
- External Insurance Policy [differs_from:: Insurance Part] transfer risk to insurer instead of stocking, MPM only (MPM p.220)
- Spare Part Optimization System [related_to:: Cost Ratio] risk to cost of stock axis similar to RBMM Cost Ratio, derived (MPM p.220-221)

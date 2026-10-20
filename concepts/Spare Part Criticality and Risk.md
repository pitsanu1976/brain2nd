---
title: Spare Part Criticality and Risk
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [spare-parts, criticality, cost, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
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
| A | หมุนเวียนช้า (very slow) | ส่วนแรกถึง 80% ของ total |
| B | หมุนเวียนปานกลาง | 15% ถัดไป (สะสมถึง 95%) |
| C | หมุนเวียนเร็ว (fast moving) | 5% สุดท้าย (หลายรายการมูลค่าต่ำ) |

- ข้อควรระวังความไม่สอดคล้องในต้นฉบับ: ข้อความหน้า 242 บอกว่า A คือรายการที่มีมูลค่า turnover สูงสุด 80% แต่รูปที่ 9.4 ติดป้าย A = Very Slow และ C = fast moving จึงต้องอ่านว่า "A = กลุ่มมูลค่าสูงที่หมุนช้า" อย่างระวัง (คำอธิบายนี้เป็นการตีความ confidence medium) ชื่อ A/B/C ในหัวข้อนี้เป็นเรื่อง turnover คนละเรื่องกับ criticality A/B/C ของเครื่องจักร
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

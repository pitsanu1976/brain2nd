# CMPR-07: X̄-R control chart (terms, construction, worked example)

Source: PETROSYNC CMRP training course slides, file CMPR-07.pdf (scanned, OCR). Reading notes ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ PDF page `(CMRP CMPR-07 p.N)`

Scope: PDF 2 หน้า (4 slide, เลขหน้าคู่มือ 255-256 / 509-512) เป็นส่วนต่อจาก SPC ท้าย CMPR-06 OCR อ่านข้อความได้ แต่สัญลักษณ์ขีดบน (X̄, R̄, X̿) หายหมด และสูตร control limits เพี้ยน ตรวจจากภาพทั้ง 2 หน้า ตารางข้อมูล 21 sample ถอดได้ครบและคำนวณซ้ำแล้ว

## 1. ศัพท์ของ X̄-R chart (CMRP CMPR-07 p.1)

| สัญลักษณ์ | ความหมาย (ถอดความ) |
|---|---|
| n | ขนาด subgroup (จำนวนค่าวัดต่อ sample) |
| X | ค่าวัดแต่ละค่า |
| X̄ | ค่าเฉลี่ยของค่าวัดใน sample หนึ่ง |
| X̿ | ค่าเฉลี่ยของ X̄ ทุก sample = center line ของ X̄ chart |
| R | range = ค่ามากสุด - ค่าน้อยสุด ใน sample |
| R̄ | ค่าเฉลี่ยของ R = center line ของ R chart |
| UCL / LCL | ขอบเขตควบคุมครอบคลุม ~99.73% ของ population **ไม่ใช่ specification limit** |

รูปตัวอย่าง (Fig 4.38): X̄ chart X̿ = 18.9, UCL = 20.0, LCL = 17.8; R chart R̄ = 1.9, UCL = 4.0, LCL = 0 ตรวจแล้วสอดคล้องกับ n = 5 (0.58 x 1.9 ≈ 1.1; 2.11 x 1.9 ≈ 4.0)

## 2. ขั้นตอนสร้าง (p.1)

1. เลือก n (3, 4 หรือ 5) และความถี่การสุ่ม
2. เก็บ 20-25 subgroup เรียงตามเวลา (ราว 60-100 ค่า)
3. คำนวณ X̄ ของแต่ละ subgroup
4. คำนวณ R ของแต่ละ subgroup
5. X̿ = center line ของ X̄ chart
6. R̄ = center line ของ R chart
7. คำนวณ control limits (ด้านล่าง)
8. Plot และตีความหา special/assignable cause

```
X̄ chart:  UCL = X̿ + A2·R̄     LCL = X̿ - A2·R̄
R chart:  UCL = D4·R̄          LCL = D3·R̄
```

| n | A2 | D3 | D4 | d2 |
|---|---|---|---|---|
| 2 | 1.88 | 0 | 3.27 | 1.13 |
| 3 | 1.02 | 0 | 2.57 | 1.69 |
| 4 | 0.73 | 0 | 2.28 | 2.06 |
| 5 | 0.58 | 0 | 2.11 | 2.33 |
| 6 | 0.48 | 0 | 2.00 | 2.53 |

ค่าคงที่ตรงกับตารางมาตรฐาน (D3 = 0 จนถึง n = 6) สไลด์มีหมายเหตุว่า A2·R̄ เท่ากับ "3s" ซึ่งต้องอ่านให้ถูก: A2 = 3/(d2√n) ดังนั้น A2·R̄ = 3σ̂/√n คือ 3 เท่าของ standard error ของค่าเฉลี่ย ไม่ใช่ 3σ ของค่าเดี่ยว (σ̂ = R̄/d2) ตรวจ n = 5: 3/(2.326 x 2.236) = 0.577 ≈ 0.58

ข้อสังเกต: CMPR-06 p.7 (Central Limit Theorem) บอกว่า n < 5 เหมาะเฉพาะเมื่อ population เป็น normal ขณะที่ขั้นตอนนี้แนะนำ n = 3-5 ควรใช้ n = 5 ถ้าไม่แน่ใจเรื่อง normality

## 3. Worked example: closure removal torque (in-lb) (p.2)

ข้อมูล 21 sample, n = 5, spec LSL = 10, USL = 22 lb (จากหัวฟอร์มในรูป Fig 4.40)

ผลรวม ΣX̄ = 323.6, ΣR = 75 → X̿ = 323.6/21 = 15.41 ≈ 15.4, R̄ = 75/21 = 3.571 ≈ 3.6 (คำนวณซ้ำจากค่าวัดดิบทุกแถว ตรงกับตาราง)

| Limit | สไลด์ | ตรวจ |
|---|---|---|
| UCL_X̄ = 15.4 + 0.58 x 3.6 | 17.5 | 17.49 ถูก |
| LCL_X̄ = 15.4 - 2.1 | 13.3 | 13.31 ถูก |
| UCL_R = 2.11 x 3.6 | 7.5 | **2.11 x 3.6 = 7.60** |
| LCL_R = 0 x 3.6 | 0 | ถูก |

**flag:** การแทนค่า UCL_R เขียน 2.11 x 3.6 = 7.5 แต่ผลคูณคือ 7.6 (ถ้าใช้ R̄ ไม่ปัด 3.571 จะได้ 7.54 ≈ 7.5) และในรูป chart Fig 4.40 เส้น UCL_R เขียน 7.6 จึงไม่สอดคล้องกันภายในสไลด์ ผลการตีความไม่เปลี่ยน

### การตีความ (รูป Fig 4.40 มีป้าย "special" และ "run")

- X̄ ต่ำกว่า LCL 13.3: sample 1 (12.8), 4 (10.8), 6 (13.2) = special cause (derived จากตาราง; รูปทำเครื่องหมาย special ไว้ช่วงต้น)
- R ของ sample 9 = 8 เกิน UCL_R = special cause
- sample 10-18 อยู่เหนือ center line ติดกัน 9 จุด = run (สัญญาณ process shift ตามกฎ run เช่น 7 จุดติดกันด้านเดียวใน CMPR-06 p.46)
- สรุปของสไลด์: เป็น start-up process ที่เริ่มนิ่งตั้งแต่ sample 10 ถ้าใช้ต่อ ต้องคำนวณ control limits ใหม่จากช่วงนั้น
- ตัวอย่างการคำนวณใหม่ (derived, ไม่อยู่ในสไลด์): ใช้ sample 10-21 ได้ X̿ ≈ 16.15, R̄ ≈ 3.42 → UCL_X̄ ≈ 18.1, LCL_X̄ ≈ 14.2, UCL_R ≈ 7.2
- ข้อควรแยก: control limit (13.3-17.5) แคบกว่า spec (10-22) มาก process อาจ "อยู่ใน spec" แต่ "out of control" ได้ ซึ่งเป็นเหตุที่สไลด์ย้ำว่า control limit ไม่ใช่ spec limit

# CMPR-05: Reliability target allocation ด้วย cost/penalty function

Source: PETROSYNC CMRP training course slides, file CMPR-05.pdf (scanned, OCR). Reading notes ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ PDF page `(CMRP CMPR-05 p.N)`

ขอบเขต: PDF p.1-3 (slide 204-206) เป็นส่วนต่อจาก CMPR-04 p.45-47 (reliability allocation) OCR ข้อความดีมาก แต่สูตรหลักเพี้ยน จึงเปิดภาพ p.2 และ p.3 ยืนยันสูตรและกราฟ ไม่มี handwriting ไฟล์สั้น เรื่อง "reliability growth costs" มีเพียงการกล่าวถึงหนึ่งประโยค

## 1. ทำไมต้องมี cost function (p.1)
- ถ้ามีโครงการ reliability growth หรือมีราคาจาก vendor/รุ่นชิ้นส่วนต่างกัน ก็สร้างต้นทุนเป็นฟังก์ชันของ reliability จากข้อมูลจริงได้ แต่หลายกรณีไม่มีข้อมูล จึงต้องมีแบบจำลอง default ที่ใช้ได้กว้างในซอฟต์แวร์ reliability optimization (CMRP CMPR-05 p.1)
- ต้องกำหนด C_i = f(R_i) ให้แต่ละชิ้น โดยดู R ปัจจุบัน (R_current), R สูงสุดที่ทำได้ (R_max) และความยากของการปรับปรุง (design, supplier, เทคโนโลยี, time-to-market) (p.1)
- เงื่อนไขของฟังก์ชัน 3 ข้อ (p.1):
  1. ถูกจำกัดระหว่าง R ต่ำสุด (ปัจจุบัน) กับ R สูงสุด (น้อยกว่า 1)
  2. ไม่ linear: ยิ่งสูงยิ่งยาก เช่น 90% เป็น 91% ง่ายกว่า 99.99% เป็น 99.999% มาก แม้ส่วนเพิ่มแรกจะมากกว่า
  3. asymptotic เข้าหา R สูงสุด

## 2. Default penalty function (p.2)
สูตร (ยืนยันจากภาพ p.2):

```
C_i(R_i) = exp[ (1 - f_i) * (R_i - R_min,i) / (R_max,i - R_i) ]
```

- C_i = penalty/cost ไม่มีหน่วย (dimensionless) ทำหน้าที่เป็น weighting factor ของความยากในการปรับปรุง
- f_i = feasibility (cost index) ของการปรับปรุงชิ้นนี้เทียบกับชิ้นอื่น ค่าระหว่าง 0 ถึง 1
- R_min,i = reliability ปัจจุบัน ณ เวลาที่ optimize; R_max,i = ค่าสูงสุดที่ทำได้ ณ เวลาเดียวกัน
- สมมติฐาน exponential เพราะความยากควรเพิ่มแบบ exponential

ข้อสังเกตจาก slide (p.2):
- cost เพิ่มเมื่อ R ห่างจาก R_min (reliability ไม่ถูกลดต่ำกว่าปัจจุบัน แต่อาจไม่ต้องเพิ่ม)
- cost พุ่งเข้าหาอนันต์เมื่อ R เข้าใกล้ R_max (ไม่มีวันถึง)
- cost ขึ้นกับช่วงการปรับปรุง (R_max - R_min); ยกจากค่าต่ำง่ายกว่า เช่น 70% เป็น 75% ง่ายกว่า 90% เป็น 95%

ข้อสังเกตเพิ่ม (คำนวณ/ตีความเอง ไม่อยู่ใน slide):
- ที่ R_i = R_min,i ได้ C = e^0 = 1 ทุกชิ้น ดังนั้น "ไม่ปรับ" มีต้นทุนฐาน 1 ไม่ใช่ 0
- ถ้า f = 1 exponent เป็น 0 และ C = 1 คงที่ คือไม่มี penalty เลย ซึ่งไม่สมจริง ค่า f ใช้งานจริงจึงควรน้อยกว่า 1
- ตัวอย่าง R_min = 0.70, R_max = 0.99:

| R เป้า | f = 0.1 | f = 0.5 | f = 0.9 |
|---|---|---|---|
| 0.80 | 1.61 | 1.30 | 1.05 |
| 0.90 | 7.39 | 3.04 | 1.25 |
| 0.95 | 277 | 22.8 | 1.87 |
| 0.98 | 8.8e10 | 1.2e6 | 16.4 |

## 3. Feasibility term f (p.2)
- f คงที่ต่อชิ้น สะท้อนความยากเชิง design complexity, ข้อจำกัดเทคโนโลยี ฯลฯ; ยิ่งยากยิ่งแพง
- กราฟ p.2 (f = 0.1, 0.5, 0.9, R_max = 0.99): **f ยิ่งต่ำ cost ยิ่งพุ่งเร็ว** (f ต่ำ = ปรับปรุงยาก)
- วิธีหา f: weighting factor ของ reliability allocation จากหลายผู้เขียน (complexity, state of the art, operating profile, criticality), engineering judgment (supplier quality/availability) โดยรวมเป็นเรื่อง subjective; ถ้ามีข้อมูลต้นทุนจริงให้ใช้ regression ประมาณค่า parameter แทน

## 4. Maximum achievable reliability (p.3)
- เป็นค่าที่เข้าใกล้ได้แต่ไม่ถึง ถูกกำหนดโดยข้อจำกัดเทคโนโลยีหรือการเงิน ต้องใช้ judgment และ state of the art
- ต้องอ้างเวลาเดียวกับเป้าระบบ: เช่น เป้าระบบ 99% ที่ 1,000 h ค่า R_max ของแต่ละชิ้นก็ต้องเป็นของ mission 1,000 h
- ตัวอย่างความสำคัญของ mission time: exponential λ = 1/h จะเหลือต่ำกว่า 1% เมื่อ mission เกิน 5 h (e^-5 = 0.67%) แต่ได้ 99.9% ถ้า mission ไม่เกินราว 4 วินาที
- **ความคลาดเล็กน้อยใน slide**: ที่ 4 s ได้ e^(-4/3600) = 0.99889 (99.89%) ต่ำกว่า 99.9% เล็กน้อย เวลาที่ถูกคือ ≤ 3.6 s (และ R ตกถึง 1% ตั้งแต่ราว 4.6 h ข้อความ "เกิน 5 h" จึงถูกแต่หลวม)
- R_max ทำหน้าที่ scale parameter: ลด R_max แล้วฟังก์ชันถูกบีบระหว่าง R_min กับ R_max (slide อ้างรูปที่ไม่ปรากฏใน p.3)

## 5. System cost และการ optimize (p.3)
- ต้นทุนระบบ = ผลรวมต้นทุนของชิ้นส่วน: C_s = C_1(R_1) + C_2(R_2) + ... + C_n(R_n) ไม่ว่าฟังก์ชันรายชิ้นเป็นรูปแบบใด
- ปัญหาคือ minimize C_s ภายใต้ constraint: R ระบบ ≥ เป้า และ R_min,i ≤ R_i < R_max,i ใช้ **nonlinear programming**
- โครงสร้างระบบ (series/parallel) ถูกนำเข้าการคำนวณ ผลของ 3 ชิ้นอนุกรมต่างจาก 3 ชิ้นขนาน มีหลายชุดคำตอบที่ถึงเป้า routine จะเลือกชุดที่ต้นทุนรวมต่ำสุด
- เชื่อมกับตัวอย่าง CMPR-04 p.46-47: อนุกรม 0.7/0.8/0.9 เป้า 0.85 ต้องยกอย่างน้อย 2 ชิ้น ส่วนขนาน 0.6/0.7/0.8 เป้า 0.99 ยกชิ้นเดียวพอ cost function เป็นตัวตัดสินว่าชิ้นไหน

ความรู้ทั่วไป (ไม่อยู่ใน slide, confidence ต่ำ): รูปแบบสูตรนี้ตรงกับ default cost function ของ ReliaSoft BlockSim และ slide ไม่ได้แสดงผลลัพธ์ optimization เป็นตัวเลข

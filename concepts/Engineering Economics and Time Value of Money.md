---
title: Engineering Economics and Time Value of Money
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [mpm, engineering-economics, cost, business-case, budget, book]
sources: [maintenance-profit-maker.md]
confidence: medium
contested: false
---

# Engineering Economics and Time Value of Money (เศรษฐศาสตร์วิศวกรรม)

หน้านี้สรุปบทที่ 15 ของ [[Maintenance Profit Maker Book]] (MPM p.265-277) จาก reading notes ใน [[raw/maintenance-profit-maker]]: ค่าของเงินตามเวลา, 6 interest factors, ต้นทุนเงิน (WACC) และการประเมินการลงทุนด้วย IRR, NPV, Payback ตัวเลขตัวอย่างทุกตัวตรวจซ้ำแล้ว ค่าที่หนังสือพิมพ์ผิดระบุพร้อมค่าที่ถูก (derived) confidence medium เพราะสังเคราะห์จาก OCR notes

**ข้อจำกัดของแหล่ง:** บทนี้ **ไม่มี** สูตรค่าเสื่อมราคา (straight-line, declining balance), annual worth / equivalent annual cost, replacement analysis หรือ benefit-cost ratio ถ้าต้องการต้องใช้แหล่งอื่น (ไม่มีใน sources)

ใช้กับ: คิด PV ของ [[Life Cycle Cost and Life Cycle Profit]], ทำ cash flow / DCF ใน [[Maintenance Business Case]], ต้นทุนถือครองเครื่อง (WACC + Depreciation) ใน [[Asset Life Cycle]] และต้นทุนการเงินของอะไหล่คลังใน [[Spare Parts Management]]

## 1. ค่าของเงินตามเวลา (MPM p.266)

- เงิน 1 บาทวันนี้มีค่ามากกว่า 1 บาทในอนาคต เพราะนำไปลงทุนได้ผลตอบแทน ยิ่งรอนาน PV ของเงินอนาคตยิ่งต่ำ
- ตัวแปร: **i** = อัตราผลตอบแทน/ดอกเบี้ยต่อช่วง, **n** = จำนวนช่วง, **PV** ที่เวลา 0, **FV** ที่เวลา n, **A** = งวดเท่ากันปลายทุกช่วง

## 2. 6 interest factors (MPM p.266-269)

| ชื่อ | สัญลักษณ์ (ความรู้ทั่วไป) | สูตร | Excel ที่ถูกต้อง |
|---|---|---|---|
| Compound amount (FV of PV) | F/P | FV = (1+i)^n x PV | `FV(rate,nper,0,-pv)` |
| Present worth (PV of FV) | P/F | PV = FV / (1+i)^n | `PV(rate,nper,0,-fv)` |
| Compound amount (FV of A) | F/A | FV = [((1+i)^n - 1) / i] x A | `FV(rate,nper,-A)` |
| Sinking fund (A for FV) | A/F | A = [i / ((1+i)^n - 1)] x FV | `PMT(rate,nper,0,-fv)` |
| Present worth (PV of A) | P/A | PV = [((1+i)^n - 1) / (i(1+i)^n)] x A | `PV(rate,nper,-A)` |
| Capital recovery (A of PV) | A/P | A = [i(1+i)^n / ((1+i)^n - 1)] x PV | `PMT(rate,nper,-pv)` |

- **ข้อผิดพลาดของหนังสือ**: MPM p.269 เขียน `PMT(rate, nper, pv, fv, type)` กำกับทั้ง 6 สูตร ซึ่งถูกเฉพาะ A/F และ A/P; F/P และ F/A ต้องใช้ `FV()` ส่วน P/F และ P/A ต้องใช้ `PV()` (derived/ความรู้ทั่วไปเรื่อง Excel)
- หนังสือเขียนสูตรบรรทัดเดียวไม่มีวงเล็บครบ ตารางนี้ใส่วงเล็บตามความหมายที่ถูก; เครื่องหมายลบใน Excel เป็นธรรมเนียม cash out/cash in ของ Excel (ผลของ PMT/PV/FV ติดลบถ้าไม่ใส่ลบที่ input)

### ตัวอย่างที่ตรวจแล้ว (MPM p.266-269)

| ตัวอย่าง | ข้อมูล | ผล |
|---|---|---|
| F/P เงินก้อนเดียว | PV 100,000 บาท, i 5%, n 10 | FV = **162,889.46** บาท |
| F/A และ A/F (sinking fund) | ฝาก 10,000 บาทปลายปี 5 ปี, i 5% | FV = **55,256.31** บาท (factor 5.52563); กลับกัน ต้องการ 55,256.31 ต้องฝาก 10,000/งวด |
| F/P จากเงินกู้ | PV 1,000,000, i 5%, n 5 คืนครั้งเดียว | **1,276,281.56** บาท |
| A/P (capital recovery) | PV 1,000,000, i 5%, n 5 ผ่อนงวดเท่ากัน | A = **230,974.80** บาท/งวด (factor 0.2309748) |

- ตัวอย่าง A/P: งวดเท่ากันแต่ PV ของแต่ละงวดไม่เท่ากัน (219,976.00 ที่ปีที่ 1 ลดลงถึง 180,974.80 ที่ปีที่ 5 รวม 1,000,000) และ FV ที่ปีที่ 5 ของทุกงวดรวม 1,276,281.56 เท่ากับคืนครั้งเดียว (MPM p.268-269)

## 3. ต้นทุนเงินและ WACC (MPM p.269-271)

ต้นทุนเงินของบริษัทมี 2 ส่วน รวมถ่วงน้ำหนักตามสัดส่วนหนี้/ทุนเป็น **WACC (Weighted Average Cost of Capital)** ใช้เป็น discount rate ประเมินโครงการ

```
Kd (หลังภาษี) = อัตราดอกเบี้ย x (1 - อัตราภาษี)
Ke            = ปันผลต่อหุ้น / ราคาหุ้น + อัตราการเติบโตของราคาหุ้น
WACC          = Kd x (หนี้ / เงินทุนรวม) + Ke x (ทุน / เงินทุนรวม)
```

- **Kd**: ตัวอย่าง ดอกเบี้ย 50,000 บนหนี้ 1,000,000 = 5%, ภาษี 30% -> 5% x (1 - 30%) = **3.5%** ไม่ได้แปลว่าจ่ายดอกเบี้ยน้อยลง แต่ดอกเบี้ยเป็นค่าใช้จ่ายทำให้ภาษีลด **ใช้ได้เฉพาะบริษัทที่มีกำไร** (MPM p.270)
- **Ke**: ปันผล 1.0 บาท ราคาหุ้น 20 บาท คาดเติบโต 5% -> 1.0/20 + 5% = **10%** (MPM p.270-271) รูปแบบเดียวกับ dividend growth (Gordon) model (ความรู้ทั่วไป)

### ตัวอย่าง WACC (MPM p.271)

ทุน 10,000,000 หนี้ 20,000,000 ปันผล 5 บาท/หุ้น ราคา 60 บาท ไม่คาดว่าจะขึ้น ดอกเบี้ย 5% ภาษี 30% -> Kd = 3.5%, Ke = 5/60 = 8.3%

| ประเภทเงิน | จำนวน | สัดส่วน | ต้นทุนหลังภาษี | ถ่วงน้ำหนัก ตามหนังสือ | ถ่วงน้ำหนัก (derived) |
|---|---|---|---|---|---|
| ทุน | 10,000,000 | 1/3 | 8.3% | 2.77 | 2.78 (8.333 x 1/3) |
| หนี้ | 20,000,000 | 2/3 | 3.5% | **0.33 (พิมพ์ผิด)** | **2.33** |
| รวม | 30,000,000 | 3/3 | | **5.10%** | 5.10% (ใช้ Ke ปัด 8.3%) หรือ 5.11% (Ke 8.333%) |

- ยอดรวม 5.10% ของหนังสือถูก เพราะ 2.77 + 2.33 = 5.10 มีแต่ช่องหนี้ที่พิมพ์ 0.33 ผิด (derived)

## 4. การประเมินการลงทุน: IRR, NPV, Payback (MPM p.271-277)

### ข้อมูลตัวอย่าง 2 ทางเลือก (13 งวด, บาท)

แถว 1-3 เป็นช่วงลงทุน (ที่ดิน, โรงงาน/เครื่องจักร, ก่อสร้าง/ติดตั้ง) แถว 4-13 เป็นกระแสเงินสุทธิจากการดำเนินงาน (ตารางเงินเข้า/ออกแยกอยู่ใน `raw/maintenance-profit-maker/ch13-15.md`)

| แถว | ทางเลือก 1 สุทธิ | ทางเลือก 2 สุทธิ |
|---|---|---|
| 1 | (300,000) | (500,000) |
| 2 | (800,000) | (1,000,000) |
| 3 | (650,000) | (850,000) |
| 4-5 | 200,000 ต่อปี | 250,000 ต่อปี |
| 6-7 | 280,000 ต่อปี | 350,000 ต่อปี |
| 8 | 320,000 | 400,000 |
| 9-12 | 400,000 ต่อปี | 500,000 ต่อปี |
| 13 | 1,000,000 | 1,350,000 |
| รวมไม่คิดลด (derived) | 2,130,000 | 2,600,000 |

### ผล

| เกณฑ์ | ทางเลือก 1 | ทางเลือก 2 | เลือก |
|---|---|---|---|
| IRR (MPM p.272-274) | **11.88%** | **10.82%** | 1 |
| NPV ที่ WACC 5% (MPM p.274-276) | **906,434** | **1,029,712** | 2 |
| Simple payback (MPM p.276-277) | **9.175 ปี** (9 + 70,000/400,000) | **9.5 ปี** (9 + 250,000/500,000) | 1 |
| Discounted payback ที่ 5% (derived) | ประมาณ 10.53 ปี | ประมาณ 11.05 ปี | 1 |

- **IRR** = อัตราที่ทำให้ PV เงินเข้า = PV เงินออก (NPV = 0) หาโดย trial and error หรือ Excel `IRR(values, guess)`; ตรวจแล้ว 11.875% และ 10.822%
- **NPV** = คิดกระแสเงินทุกงวดเป็นค่าปัจจุบันที่ต้นทุนเงินที่กำหนด; ตรวจแล้ว 906,433.50 และ 1,029,712.01
- **Payback**: หนังสือนิยามว่าใช้ต้นทุนเงินที่กำหนด แต่ตัวอย่างจริงเป็น simple (ไม่คิดลด) payback; discounted payback ที่ 5% (derived, interpolation เชิงเส้นตามแถว) ยาวขึ้น 1.4-1.6 ปี ลำดับเหมือนเดิม
- ทางเลือก 2 ลงทุนมากกว่าและได้เงินรวมมากกว่า แต่ IRR ต่ำกว่า

### ข้อควรระวัง: ธรรมเนียมการคิดลด (derived)

- ตารางในหนังสือ **ไม่คิดลดแถวที่ 1** (ถือเป็น t = 0) แถวที่ k คิดลดด้วย (1+r)^(k-1)
- ถ้าใช้ Excel `NPV(5%, แถว1:แถว13)` ตรง ๆ จะคิดลดทุกแถวหนึ่งงวด ได้ประมาณ **863,270** และ **980,678** (= ค่าหนังสือ / 1.05) ต้องใช้ `แถว1 + NPV(5%, แถว2:แถว13)` จึงได้ตัวเลขของหนังสือ; IRR ไม่ได้รับผลกระทบ
- ก่อนเทียบ NPV จากหลายแหล่ง ให้ตรวจว่ากระแสเงินแรกอยู่ที่ t = 0 หรือ t = 1

### NPV vs IRR ให้ผลขัดกัน (MPM p.275-276)

- มุมมองผู้เขียน: ไม่มีทางใดถูก/ผิด ที่ discount rate ต่ำกว่า IRR NPV เป็นบวก (ดึงเงินออกน้อยกว่าที่โครงการคืนได้) สูงกว่า IRR ติดลบ; เงินเหลือต่างกันเพราะลงทุนไม่เท่ากัน และยังไม่ได้รวม **ความเสี่ยง**; ผู้เขียนว่าโดยทั่วไป "มักใช้ IRR มากกว่า"
- **ความรู้ทั่วไป (confidence low, ไม่อยู่ใน sources)**: หลักการเงินทั่วไปให้ใช้ **NPV** ที่ต้นทุนเงินของบริษัทเป็นเกณฑ์หลักเมื่อทางเลือกแยกกัน (mutually exclusive) และขนาดลงทุนต่างกัน หรือใช้ **incremental IRR** ของกระแสเงินส่วนต่าง
- ในตัวอย่างนี้ (derived): กระแสเงินส่วนต่าง (ทาง 2 - ทาง 1) มี IRR ประมาณ **7.7%** สูงกว่า WACC 5% และ NPV ส่วนต่าง = 1,029,712 - 906,434 = 123,278 จึงควรเลือกทางเลือก 2 ตามหลักทั่วไป ข้อเสนอ "มักใช้ IRR" ของผู้เขียนจึงเป็นความเห็นของหนังสือ ไม่ใช่เกณฑ์ตัดสินที่แนะนำ (เป็นความต่างระหว่าง source กับความรู้ทั่วไป ไม่ได้ตั้ง contested เพราะไม่มี source ที่สองใน wiki)

## 5. การนำไปใช้ในงานบำรุงรักษา

- ฝ่ายบำรุงรักษารับผิดชอบงบดุลด้วย: ค่าเสื่อมโรงซ่อมและเครื่องมือ, อะไหล่ที่ซื้อด้วยทุน/เงินกู้มีต้นทุนการเงินเป็น WACC (MPM p.264) ตรงกับ "Machine Ownership Cost = WACC + Depreciation" ใน [[Asset Life Cycle]] (RBMM p.19)
- เทียบ LCC ของเครื่องหลายรุ่นด้วย PV ที่ WACC ดู [[Life Cycle Cost and Life Cycle Profit]] (ตัวอย่าง WACC 6%)
- โครงการปรับปรุง (modification, redundancy, CM system) ที่ขอเป็นงบลงทุน ใช้ NPV/IRR/payback ในขั้น Evaluate options ของ [[Maintenance Business Case]] และงบลงทุนใน [[Maintenance Budget]]
- capital recovery (A/P) แปลงราคาซื้อเครื่องเป็นต้นทุนรายปีเทียบเท่า ใช้เทียบกับค่าบำรุงรักษารายปีได้ (การตีความของ wiki; หนังสือไม่ได้ทำ annual worth / replacement analysis)

## เชื่อมโยงกับ compressor failure hierarchy

การตีความของ wiki (หนังสือไม่มีตัวอย่าง compressor):
- business case ลดความถี่ failure mode เด่นของ [[Compressor]] (เช่น ติดตั้ง condition monitoring) ใช้ PV ของ downtime cost ที่ลดลงเป็นเงินเข้า และค่าติดตั้ง/บำรุงระบบเป็นเงินออก แล้วคิด NPV ที่ WACC ของบริษัท
- สัดส่วน failure mode จาก [[OREDA]] บอกได้เพียงว่าโหมดไหนสำคัญ ไม่ได้ให้ความถี่สัมบูรณ์ จึงต้องใช้ข้อมูลเสียจริงของ asset (ยังไม่มีใน sources) ก่อนแปลงเป็นกระแสเงิน

## ดูเพิ่ม

- [[Life Cycle Cost and Life Cycle Profit]]
- [[Maintenance Business Case]]
- [[Asset Life Cycle]]
- [[Maintenance Budget]]
- [[Spare Parts Management]]
- [[Maintenance Profit Maker Book]]

## Triplets

- [[Engineering Economics and Time Value of Money]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 15 (MPM p.265-277)
- Time Value of Money [depends_on:: Interest Rate] i per period and n periods (MPM p.266)
- Compound Amount Factor [has_formula:: FV = (1+i)^n x PV] F/P, Excel FV(rate,nper,0,-pv) (MPM p.266-269)
- Present Worth Factor [has_formula:: PV = FV / (1+i)^n] P/F, Excel PV(rate,nper,0,-fv) (MPM p.269)
- Uniform Series Compound Amount Factor [has_formula:: FV = ((1+i)^n - 1) / i x A] F/A, Excel FV(rate,nper,-A) (MPM p.269)
- Sinking Fund Factor [has_formula:: A = i / ((1+i)^n - 1) x FV] A/F, Excel PMT(rate,nper,0,-fv) (MPM p.267-269)
- Uniform Series Present Worth Factor [has_formula:: PV = ((1+i)^n - 1) / (i(1+i)^n) x A] P/A, Excel PV(rate,nper,-A) (MPM p.269)
- Capital Recovery Factor [has_formula:: A = i(1+i)^n / ((1+i)^n - 1) x PV] A/P, Excel PMT(rate,nper,-pv) (MPM p.268-269)
- MPM Excel Function Table [contradicts:: Correct Excel Interest Functions] book labels all 6 factors PMT; only A/F and A/P use PMT, derived
- Compound Interest Example [has_value:: 162,889.46 baht] PV 100,000 at 5% for 10 years (MPM p.266-267)
- Sinking Fund Example [has_value:: 55,256.31 baht] 10,000 per year for 5 years at 5% (MPM p.267-268)
- Capital Recovery Example [has_value:: 230,974.80 baht per period] PV 1,000,000 at 5% for 5 years; lump sum 1,276,281.56 (MPM p.268-269)
- WACC [has_formula:: Kd x D/(D+E) + Ke x E/(D+E)] weighted by debt and equity (MPM p.269-271)
- Cost of Debt [has_formula:: interest rate x (1 - tax rate)] only for profitable companies (MPM p.270)
- Cost of Equity [has_formula:: dividend / share price + growth] dividend growth form, general knowledge name Gordon model (MPM p.270-271)
- Cost of Debt Example [has_value:: 3.5%] 5% interest, 30% tax (MPM p.270)
- Cost of Equity Example [has_value:: 10%] dividend 1.0, price 20, growth 5% (MPM p.270-271)
- WACC Example [has_value:: 5.10%] equity 10M at 8.3%, debt 20M at 3.5% (MPM p.271)
- WACC Example Debt Weighted Cost [has_value:: 2.33] book prints 0.33, derived correction; 5.11% with exact Ke 8.333%
- WACC [input_to:: Net Present Value] discount rate for projects (MPM p.271)
- [[Engineering Economics and Time Value of Money]] [has_part:: Internal Rate of Return] (MPM p.271-274)
- [[Engineering Economics and Time Value of Money]] [has_part:: Net Present Value] (MPM p.274-276)
- [[Engineering Economics and Time Value of Money]] [has_part:: Payback Period] (MPM p.276-277)
- Internal Rate of Return [has_formula:: rate where NPV = 0] PV revenues = PV costs, Excel IRR (MPM p.272)
- IRR Example Option 1 [has_value:: 11.88%] (MPM p.272-274)
- IRR Example Option 2 [has_value:: 10.82%] (MPM p.272-274)
- NPV Example Option 1 [has_value:: 906,434 baht] at WACC 5%, row 1 undiscounted (MPM p.274-276)
- NPV Example Option 2 [has_value:: 1,029,712 baht] at WACC 5%, row 1 undiscounted (MPM p.274-276)
- Payback Example Option 1 [has_value:: 9.175 years] simple undiscounted (MPM p.276-277)
- Payback Example Option 2 [has_value:: 9.5 years] simple undiscounted (MPM p.276-277)
- Discounted Payback Example [has_value:: about 10.53 and 11.05 years] option 1 and 2 at 5%, derived [confidence:: low]
- MPM Payback Definition [contradicts:: MPM Payback Example] definition uses cost of money, example is undiscounted (MPM p.276)
- NPV Example Option 1 [has_value:: about 863,270 baht] if Excel NPV discounts all 13 rows; option 2 about 980,678, derived [confidence:: low]
- Net Present Value [depends_on:: Discounting Convention] first cash flow at t = 0 vs t = 1
- Net Present Value [differs_from:: Internal Rate of Return] NPV picks option 2, IRR picks option 1 (MPM p.275-276)
- MPM IRR Preference [differs_from:: NPV Rule for Mutually Exclusive Projects] author says IRR more used; general knowledge prefers NPV or incremental IRR [confidence:: low]
- Incremental IRR Example [has_value:: about 7.7%] option 2 minus option 1, above WACC 5%, favours option 2, derived [confidence:: low]
- [[Engineering Economics and Time Value of Money]] [input_to:: [[Maintenance Business Case]]] DCF, IRR, hurdle rate step
- [[Engineering Economics and Time Value of Money]] [input_to:: [[Life Cycle Cost and Life Cycle Profit]]] PV of life cycle costs
- Machine Ownership Cost [depends_on:: WACC] with depreciation (RBMM p.19; MPM p.264)

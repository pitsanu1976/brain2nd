---
title: Maintenance Financial Impact
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [mpm, cost, maintenance-management, kpi]
sources: [maintenance-profit-maker.md, reliability-based-maintenance-management.md]
confidence: medium
contested: true
---

# Maintenance Financial Impact (ผลกระทบของงานบำรุงรักษาต่องบการเงินและกำไร)

หนังสือ [[Maintenance Profit Maker Book]] (MPM บทที่ 10 และกรณีศึกษาบทที่ 12) เชื่อมงานบำรุงรักษาเข้ากับงบการเงินของบริษัทโดยตรง: ทรัพยากรที่บำรุงรักษาถือครองอยู่ใน **งบดุล** ส่วนค่าใช้จ่ายจากการใช้ทรัพยากรและผลผลิตที่เครื่องสร้างได้อยู่ใน **งบกำไรขาดทุน** (MPM p.168, p.190) หน้านี้สรุปกรอบคิด ตัวอย่างบริษัท XYZ และวิธีแปลง OEE เป็นกำไรขั้นต้นที่เสียโอกาส ถอดความจาก reading notes [[raw/maintenance-profit-maker]] ไม่ใช่ข้อความต้นฉบับ ค่าที่ wiki คำนวณเองระบุว่า derived

## 1. สองด้านของผลกระทบ (MPM p.168-172)

| ด้าน | งบ | สิ่งที่บำรุงรักษากระทบ |
|---|---|---|
| ฐานะการเงิน | งบดุล (Balance Sheet) | ทรัพย์สินระยะยาวของบำรุงรักษา และอะไหล่คงคลัง (ทรัพย์สินหมุนเวียน) |
| ผลประกอบการ | งบกำไรขาดทุน (Income Statement) | ทางตรง: ค่าใช้จ่ายบำรุงรักษาในต้นทุนสินค้า; ทางอ้อม: ปริมาณ/คุณภาพผลผลิต (OEE, Hidden Plant) |

- บริษัทที่ทำธุรกิจขนาดเดียวกันแต่ใช้ทรัพย์สินน้อยกว่าถือว่ามีประสิทธิภาพกว่า ทรัพย์สินมาจากหนี้ (มีดอกเบี้ย) และทุนผู้ถือหุ้น (ต้องทำผลตอบแทนเกินดอกเบี้ยเงินฝาก) จึงต้องวัดผลตอบแทนต่อการลงทุนเสมอ (MPM p.168-169)
- ปัญหาที่พบบ่อย: งบดุลรวมรายการไว้จนแยกไม่ได้ว่าทรัพย์สินใดเป็นของบำรุงรักษา หนังสือเสนอให้มีงบดุลและงบกำไรขาดทุน **ระดับหน่วยงาน** ทุกงวดปิดบัญชี และให้บำรุงรักษารับผิดชอบค่าครอบครองทรัพย์สินที่ตนใช้ (MPM p.169, p.190)
- ผู้จะเป็นผู้บริหารงานซ่อมบำรุงต้องได้รับการอบรมบัญชีและการเงิน (MPM p.190) ดูการคิดต้นทุนใน [[Maintenance Cost Structure]] และ [[Job Order Costing]]

### 1.1 งบดุล: ทรัพย์สินในความรับผิดชอบของบำรุงรักษา (MPM p.169-170)

- **ทรัพย์สินระยะยาว** 4 กลุ่ม: โรงซ่อม (workshop), เครื่องมือ/เครื่องจักรหนักเบาที่ติดตั้งประจำ, เครื่องมืออุปกรณ์อื่น (คอมพิวเตอร์ เครื่องมือพิเศษ), ระบบงานที่ใช้ร่วม เช่น [[CMMS]] ระบบบริหารอะไหล่ ระบบบัญชี ทรัพย์สินเหล่านี้สร้างค่าใช้จ่ายประจำไม่ว่าใช้มากหรือน้อย และการลงทุน (capital expense) ทั้งในเครื่องมือบำรุงรักษาและการปรับปรุงเครื่องผลิตต้องวิเคราะห์ผลตอบแทนทุกครั้ง การเปลี่ยนเงินสดเป็นเครื่องจักรทำให้เสียสภาพคล่อง
- **ทรัพย์สินหมุนเวียน = อะไหล่คงคลัง** มักถูกมองว่าไม่ใช่ความรับผิดชอบของบำรุงรักษา ทั้งที่บำรุงรักษาเป็นผู้กำหนดระดับสต็อกและรายการ เป้าที่หนังสือยกตัวอย่าง: คงคลังต่ำสุด, อะไหล่หมุนเวียน > 90% ของระดับคงคลัง, ความพร้อมอะไหล่ > 95% และเครื่องหยุดรออะไหล่น้อยที่สุด ต้นทุนการเงินของสต็อกเป็น "จุดบอดของฝ่ายบริหาร" ดู [[Spare Parts Management]]

### 1.2 งบกำไรขาดทุน: ค่าใช้จ่ายทางตรง 4 กลุ่ม (MPM p.171)

| กลุ่ม | รายการย่อย |
|---|---|
| 1.1 Maintenance Personnel Cost | ค่าแรงทางตรง; ค่าแรงทางอ้อมและการจัดการ |
| 1.2 Spare Part and Consumable | Spare Part Usage (อะไหล่ที่ใช้ซ่อม); Spare Part Carrying Cost (ค่ามีอะไหล่คงคลัง) |
| 1.3 Cost of Ownership of Maintenance Asset | ค่าเสื่อมราคาโรงซ่อม เครื่องจักรกล เครื่องมือ; ค่าลิขสิทธิ์/amortization ตลอดสัญญา |
| 1.4 Financial Cost | ดอกเบี้ยของเงินทุนส่วนที่กู้ |

## 2. ตัวอย่างบริษัท XYZ: งบดุลและงบกำไรขาดทุนโดยย่อ (รูป 10.2-10.3, MPM p.172)

บริษัทสมมติผลิตสินค้าอุตสาหกรรมขนาดใหญ่ ยอดขายส่วนใหญ่ส่งออก ราคาตามวัฏจักรตลาดโลก ตัวเลขชุดนี้สอดคล้องกับปี 2000 ของกรณีศึกษา (หัวตาราง OCR อ่านไม่ออก)

| รายการ | ค่า |
|---|---|
| หนี้ / ทุน / ทรัพย์สินรวม | 8,600 / 13,400 / 22,000 ล้านบาท |
| Plant Asset (ARV, เครื่องจักรผลิต) | 11,000 ล้านบาท (50.0% ของทรัพย์สินรวม) |
| D/E | 0.64 |
| ทรัพย์สินใช้งานบำรุงรักษา | 618,329,389 บาท = 5.6% ของ Plant Asset (อะไหล่ 4.7% + เครื่องมือ 0.9%) |
| ยอดขาย / ต้นทุนขาย / กำไรขั้นต้น | 14,000 / 10,000 / 4,000 ล้านบาท (กำไรขั้นต้น 28.6%) |
| กำไรก่อนภาษี / หลังภาษี | 2,320 ล้าน (16.6%) / 1,972 ล้าน (14.1%) |
| ROTA / ROE / Sales ต่อ Total Asset | 8.96% / 14.72% / 0.64 |
| ค่าใช้จ่ายซ่อมบำรุง | 511,829,606 บาท = 3.66% ของยอดขาย = 4.65% ของ ARV |

สูตรที่ตัวเลขสอดคล้อง (derived, หนังสือไม่ได้เขียนสูตร):

```
ROTA = กำไรสุทธิหลังภาษี / ทรัพย์สินรวม = 1,972 / 22,000 = 8.96%
ROE  = กำไรสุทธิหลังภาษี / ทุน        = 1,972 / 13,400 = 14.72%
ROTA = Net margin 14.1% x Asset turnover 0.64;  ROE = ROTA x (Assets/Equity 1.64)   (DuPont, ความรู้ทั่วไป)
ภาษี implied = (2,320 - 1,972) / 2,320 = 15%
```

**ข้อผิดพลาดในเล่ม**: อะไหล่พิมพ์ 512,200,000 บาท แต่ 512,200,000 + 97,129,389 = 609,329,389 ไม่ใช่ 618,329,389 ค่าที่บวกครบคือ **521,200,000 บาท (4.74%, derived)** ซึ่งตรงกับอะไหล่คงคลัง 521.2 ล้านในรูป 10.11

### 2.1 ผลของการลดค่าใช้จ่ายบำรุงรักษา (รูป 10.4, MPM p.173)

| ลดค่าใช้จ่ายได้ | -1% | -5% | -10% | -15% |
|---|---|---|---|---|
| กำไรเพิ่ม (บาท) | 5,118,296 | 25,591,480 | 51,182,961 | 76,774,441 |

- หนังสือเสนอให้ใช้เป็นกรอบงบ: ลงทุนโครงการลดค่าใช้จ่ายได้ถึงจำนวนนี้โดยคืนทุนใน 1 ปี กลับกัน ถ้าค่าใช้จ่ายเพิ่มเท่ากัน กำไรก็ลดเท่ากัน ประเด็นคือความสัมพันธ์ ไม่ใช่ขนาดตัวเลข
- กำไรที่เพิ่มเป็นกำไร **ก่อนภาษี** (หลังภาษี 15% ราว 65.3 ล้านที่ระดับ -15%, derived) หนังสือไม่ระบุ

## 3. Hidden Plant และสูตรผลผลิต (MPM p.173-176, p.201)

- บริษัท "ซื้อกำลังผลิต" มาแล้วตั้งแต่ซื้อเครื่อง ส่วนที่จ่ายเงินแล้วแต่ใช้ไม่ได้เพราะความสูญเสีย = **กำลังผลิตซ่อนเร้น (Hidden Plant)** บำรุงรักษาและการเดินเครื่องที่ดีคืนส่วนนี้ได้ และสำคัญที่สุดในช่วงตลาดดีที่ต้องเร่งผลิต

```
สินค้าที่ผลิตได้ = OEE x Plant Capacity x Planning Factor      (MPM p.174, p.201)
OEE = Af x Sf x Qf
```

- OEE ไม่รวมการหยุดซ่อม/ซ่อมใหญ่ตามกำหนด (อยู่ใน Planning Factor) เครื่องที่หยุดซ่อมใหญ่นานกว่าจึงผลิตได้น้อยกว่าแม้ OEE เท่ากัน และ OEE เท่ากันความสูญเสียรวมอาจต่างกันตามว่าตัวไหนใน A/S/Q ต่ำ รายละเอียดนิยามดู [[Availability and OEE]]
- ปัจจัยของ Availability 3 ตัวคือ MTBF, MTTR, MWT; MTBF และ MTTR ขึ้นตรงกับฝีมือบำรุงรักษา ส่วน MWT มาจากกระบวนการและความร่วมมือระหว่างบำรุงรักษากับผลิตเป็นหลัก (MPM p.174-175) Quality loss รุนแรงที่สุดเพราะเสียทั้งวัตถุดิบและงานทำซ้ำ (MPM p.175-176)
- การกระทบยอด (MPM p.201): ปริมาณที่ได้จากสูตรนี้ต้องตรงกับบัญชี (ปริมาณขาย หักสินค้าต้นงวด บวกสินค้าปลายงวด) และงาน rework ต้องตรงกับ WIP ถ้าไม่ตรง = ปัญหาเชิงระบบที่ต้องแก้ก่อนพูดถึงสมรรถนะ

### 3.1 ผลของ OEE ต่อต้นทุนต่อชิ้น (MPM p.176-177)

| รายการ | ค่า |
|---|---|
| เครื่องจักร 100 ล้านบาท อายุ 20 ปี | ค่าเสื่อม 5,000,000 บาท/ปี |
| กำลังผลิต (หักหยุดซ่อมตามกำหนดแล้ว) 500,000 ชิ้น/ปี | ต้นทุนคงที่ **10 บาท/ชิ้น** |
| OEE 80% -> ผลิตได้ 400,000 ชิ้น/ปี | ต้นทุนคงที่ **12.50 บาท/ชิ้น** (+2.50 บาท = +25%) |
| ถ้าต้นทุนเครื่องจักรเป็น 10% ของต้นทุนทั้งหมด | ต้นทุนรวมสูงขึ้น 2.5% |

## 4. กรณีศึกษา XYZ: แปลง OEE เป็นกำไรขั้นต้นที่เสียโอกาส (รูป 10.9-10.10 MPM p.177-178; รูป 12.11-12.13 MPM p.230-235)

| รายการ (ล้านบาท ยกเว้นระบุ) | 1998 | 1999 | 2000 |
|---|---|---|---|
| ARV / WACC | 11,000 / 10% | 11,000 / 10% | 11,000 / 10% |
| รายได้จากการขาย | 11,000 | 9,000 | 14,000 |
| กำไรขั้นต้น (% ยอดขาย) | 3,000 (27.3%) | 1,500 (16.7%) | 4,000 (28.6%) |
| ปริมาณผลิต (ตัน) | 500,000 | 422,749 | 530,000 |
| Availability / Performance / Quality | 91.50 / 98.00 / 99.40% | 87.50 / 99.40 / 92.50% | 88.50 / 99.60 / 90.10% |
| **OEE** | **89.13%** | **80.45%** | **79.42%** |
| ค่าบำรุงรักษารวม / ต่อตัน | 320 / 640 บาท | 389 / 920 บาท | 512 / 966 บาท |
| กำไรขั้นต้นที่ OEE 100% | 3,366 | 1,864 | 5,037 |
| กำไรขั้นต้นต่อ OEE 1 จุด | 33.66 (derived; รูป 10.10 พิมพ์ 33.60) | 18.64 | **50.37** |
| เสียโอกาสกำไรขั้นต้นเทียบปี 1998 | - | **161.84** | **489.17** |

วิธีคำนวณ (derived จากการย้อนคำนวณ ตรงกับผลของหนังสือ):

```
กำไรขั้นต้นที่ OEE 100% = กำไรขั้นต้น / OEE                 เช่น 4,000 / 0.7942 = 5,037
กำไรต่อ OEE 1 จุด         = ค่าข้างบน / 100                   เช่น 50.37
เสียโอกาส (ปี n)          = (OEE 1998 - OEE ปี n) x กำไรต่อ 1 จุด
  1999: (89.13 - 80.45) x 18.645 = 161.84      2000: (89.13 - 79.42) x 50.37 = 489.1
```

- **Sensitivity**: ที่ระดับปี 2000 OEE เพิ่ม 1 จุด = กำไรขั้นต้นเพิ่มราว **50.37 ล้านบาท** สมมติฐานแฝงคือกำไรขั้นต้นแปรผันเชิงเส้นกับ OEE (ไม่แยกต้นทุนผันแปรของการผลิตเพิ่ม และสมมติว่าขายได้หมด)
- การตีความของหนังสือ (MPM p.178, p.233-235): ปี 2000 กำไรสูงเพราะราคาตลาดโลกขึ้น ไม่ใช่เพราะการผลิตดี ถ้าตลาดกลับทิศบริษัทจะลำบาก; 489.17 ล้านนำไปลดหนี้และต้นทุนการเงินปีถัดไปได้; ลงทุน 489.17 ล้านเพื่อคืน OEE ระดับปี 1998 ก็คืนทุนใน 1 ปี แต่ควรตั้งเป้าสูงกว่า คือเพิ่ม OEE อีก 10.6 จุดภายใน 2 ปี (79.42 + 10.6 ≈ 90.0%, derived) และธุรกิจวัฏจักรควรเน้นด้านรายได้ (OEE) มากกว่าการลดค่าใช้จ่าย
- หนังสือว่า 489.17 ล้านเพิ่มกำไรก่อนภาษีปี 2000 ได้ 24.4% โดยใช้ฐาน 2,000 ล้าน แต่รูป 10.3 ให้กำไรก่อนภาษี 2,320 ล้าน ถ้าใช้ฐานนั้นจะได้ราว 21.1% (derived) ฐานในเล่มไม่สอดคล้องกัน
- อาการประกอบที่สอดคล้องกัน (MPM p.179-182, p.212): ค่าบำรุงรักษารวมเพิ่ม 320 -> 389 -> 512 ล้าน, อะไหล่คงคลังเพิ่ม 405.0 / 407.4 -> 521.2 ล้าน (ต้นทุนการเงิน 10% WACC เพิ่มตาม) ขณะที่ซื้อตรงพุ่ง 47.4 -> 259.5 ล้าน ชี้ว่าของที่เก็บไม่ตรงกับที่ต้องใช้ โครงสร้าง fixed/variable และ Full Fix Cost Rate (1,196.8 / 1,299.3 / 1,506.4 บาท/ชม.-คน) ดู [[Maintenance Cost Structure]] และดัชนีชุดเต็มใน [[Maintenance KPIs]]

### 4.1 ข้อผิดพลาดในตัวเลขของเล่ม (derived)

| จุด | พิมพ์ | ค่าที่สอดคล้อง | หมายเหตุ |
|---|---|---|---|
| รูป 12.13 ปี 1998 กำไรที่ OEE 100% / ต่อ 1 จุด | 1,944 / 19.44 | 3,365.9 / 33.66 | 3,000 / 0.8913; ไม่กระทบผลเพราะ 1998 เป็นฐาน |
| รูป 12.13 ปี 1999 | 1,579 / 15.79 | 1,864.5 / 18.65 | 1,500 / 0.8045; ถ้าใช้ 15.79 จะได้ 137.1 ไม่ใช่ 161.84 ดังนั้นผลสุดท้ายของหนังสือถูก แต่ค่ากลางพิมพ์ผิด |
| รูป 10.10 ส่วนคำนวณ OEE รายได้ / กำไรขั้นต้น | 9,000 / 8,000 / 14,000 และ 1,733 / 1,270 / 4,000 | 11,000 / 9,000 / 14,000 และ 3,000 / 1,500 / 4,000 | แถว "กำไรที่ OEE 100%" ของรูปเดียวกันคำนวณจากชุดหลัง |
| รูป 10.10 ค่าบำรุงรักษา / ราคาเครื่องจักร | 2.7 / 3.3 / 4.4% | 2.9 / 3.5 / 4.65% | 320, 389, 512 หารด้วย 11,000; รูป 12.11-12.12 พิมพ์ 2.9 / 3.5 / 4.7% และ 2.91 / 3.53 / 4.65% |
| รูป 10.2 อะไหล่ | 512,200,000 | 521,200,000 | ดูหัวข้อ 2 |

## 5. ต้นทุนการเงินของอะไหล่ในตัวอย่าง (ข้อขัดแย้ง MPM-C1)

- ตัวอย่าง XYZ คิดต้นทุนถืออะไหล่คงคลังเฉพาะ **ต้นทุนการเงิน = WACC 10%** ของมูลค่าสต็อก (40.5 / 40.7 / 52.1 ล้านบาท, MPM p.180-181)
- RBMM ใช้ holding cost **15-20%** ต่อปี (RBMM p.34) และ MPM บทที่ 5 เองให้ 20-40% ของมูลค่าสต็อก (MPM p.84) ดังนั้นตัวอย่างนี้น่าจะประเมินค่าถือครองต่ำกว่าจริงเพราะไม่รวมค่าเก็บรักษา/ล้าสมัย (การตีความ) wiki เก็บทั้งสองมุมมองและยังไม่เลือกค่า รายละเอียดข้อขัดแย้งอยู่ที่ [[Maintenance Cost Structure]] และ [[Spare Parts Management]]

## เชื่อมโยงกับ compressor failure hierarchy

การตีความของ wiki (หนังสือไม่มีข้อมูล compressor):
- เมื่อ [[Compressor]] เป็นเครื่องคอขวดของสายผลิต การหยุดจาก [[UST Spurious Stop]] หรือ fail to start ลด Availability Factor โดยตรง ส่วน [[LOO Low Output]] ลด Speed Factor ทั้งสองเป็น Hidden Plant ที่แปลงเป็นเงินได้ด้วยวิธีหัวข้อ 4 (กำไรต่อ OEE 1 จุด x จุดที่เสีย)
- การจัดลำดับโครงการปรับปรุงต่อ failure mode ควรเทียบ "กำไรที่ได้คืน" กับเงินลงทุนแบบที่หนังสือทำ (คืนทุนใน 1 ปี) ดู [[Maintenance Business Case]]
- อะไหล่ของ maintainable item ที่ critical (เช่น valves, cylinder liner ของ [[Reciprocating Compressor]]) ถือครองแล้วมีต้นทุนการเงินทุกปี ต้องชั่งกับ MWT ที่ลดได้ ดู [[Spare Part Criticality and Risk]]

## ดูเพิ่ม

- [[Maintenance Profit Maker Book]]
- [[Availability and OEE]]
- [[Maintenance Cost Structure]]
- [[Maintenance KPIs]]
- [[Maintenance Budget]]
- [[Maintenance Business Case]]
- [[Asset Life Cycle]]

ดูเพิ่ม (หน้าจาก MPM ingest 2026-10-28): [[Maintenance Performance Improvement]], [[Maintenance Performance Audit]], [[Life Cycle Cost and Life Cycle Profit]]

## Triplets

- [[Maintenance Financial Impact]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 10 and chapter 12 case study (MPM p.167-190, p.230-236)
- [[Maintenance Financial Impact]] [has_part:: Balance Sheet Impact] long term maintenance assets and spare part inventory (MPM p.168-170)
- [[Maintenance Financial Impact]] [has_part:: Income Statement Impact] direct cost and indirect output effect (MPM p.171-176)
- Maintenance Long Term Assets [has_part:: Workshop] also installed tools/machines, other equipment, shared systems such as CMMS (MPM p.169-170)
- Spare Part Inventory [is_a:: Current Asset] managed and used by maintenance (MPM p.170)
- Spare Part Inventory [has_value:: turnover > 90% of stock level] example target with availability > 95% (MPM p.170)
- Direct Maintenance Cost [has_part:: Maintenance Personnel Cost] direct and indirect labour (MPM p.171)
- Direct Maintenance Cost [has_part:: Spare Part and Consumable Cost] usage and carrying cost (MPM p.171)
- Direct Maintenance Cost [has_part:: Cost of Ownership of Maintenance Asset] depreciation and amortization (MPM p.171)
- Direct Maintenance Cost [has_part:: Financial Cost] interest on borrowed capital (MPM p.171)
- ROTA [has_formula:: net profit after tax / total assets] derived from XYZ figures (MPM p.172)
- ROE [has_formula:: net profit after tax / equity] derived from XYZ figures (MPM p.172)
- XYZ Company 2000 [has_value:: ROTA 8.96%] ROE 14.72%, sales/total asset 0.64, D/E 0.64 (MPM p.172 Fig 10.3)
- XYZ Company 2000 [has_value:: maintenance cost 511,829,606 baht] 3.66% of sales, 4.65% of ARV 11,000 million (MPM p.172)
- XYZ Company 2000 [has_value:: maintenance assets 5.6% of plant asset] spares 4.7% + tools 0.9% (MPM p.172 Fig 10.2)
- XYZ Spare Part Value Printed [has_value:: 512,200,000 baht] does not add to total 618,329,389 (MPM p.172)
- XYZ Spare Part Value [has_value:: 521,200,000 baht] derived, 4.74% of plant asset, matches Fig 10.11
- XYZ Spare Part Value Printed [contradicts:: XYZ Spare Part Value] book error, digit swap
- Maintenance Cost Reduction [has_value:: -15% = +76,774,441 baht profit] -1% 5,118,296; -5% 25,591,480; -10% 51,182,961; pre-tax (MPM p.173 Fig 10.4)
- Hidden Plant [has_label:: capacity already paid for but lost to OEE losses] (MPM p.173-174)
- Hidden Plant [depends_on:: OEE] recovered by good maintenance and operation (MPM p.174)
- Production Output [has_formula:: OEE x Plant Capacity x Planning Factor] (MPM p.174, p.201)
- Production Output [depends_on:: Planning Factor] scheduled turnaround is outside OEE
- Availability Factor [depends_on:: MTBF] with MTTR and MWT (MPM p.174-175)
- MWT [depends_on:: Maintenance and Production Cooperation] mainly process and cooperation (MPM p.175)
- Quality Loss [has_category:: most severe loss] wastes material and rework (MPM p.175-176)
- Production Output [related_to:: Inventory Reconciliation] output must match sales minus opening plus closing stock (MPM p.201)
- OEE Unit Cost Example [has_value:: 10 to 12.50 baht per piece] 100 M baht machine, 20 years, 500,000 pcs/yr, OEE 80% gives +25% (MPM p.176-177)
- OEE Unit Cost Example [has_value:: +2.5% total cost] if machine cost is 10% of total cost (MPM p.177)
- XYZ Case Study [has_value:: OEE 89.13% / 80.45% / 79.42%] 1998 / 1999 / 2000 (MPM p.178, p.232)
- XYZ Case Study [has_value:: lost gross profit 161.84 / 489.17 million baht] 1999 / 2000 vs 1998 OEE (MPM p.178, p.234)
- Lost Gross Profit from OEE [has_formula:: (OEE base - OEE year) x (gross profit / OEE / 100)] derived from book figures
- OEE Profit Sensitivity [has_value:: 50.37 million baht per OEE point] XYZ 2000, 4,000 / 0.7942 / 100 (MPM p.178)
- Lost Gross Profit from OEE [depends_on:: Linear Profit Assumption] gross profit assumed proportional to OEE, derived [confidence:: low]
- XYZ Case Study [has_value:: target +10.6 OEE points in 2 years] to about 90% (MPM p.233-235)
- Fig 12.13 Printed 1999 Values [has_value:: 1,579 / 15.79] book error (MPM p.234)
- Fig 12.13 Corrected 1999 Values [has_value:: 1,864.5 / 18.65] derived; gives the printed result 161.84
- Fig 12.13 Printed 1999 Values [contradicts:: Fig 12.13 Corrected 1999 Values] book error, final result unaffected
- Fig 12.13 Printed 1998 Values [has_value:: 1,944 / 19.44] book error; derived 3,365.9 / 33.66
- Fig 10.10 Maintenance Cost per Plant Asset Printed [has_value:: 2.7 / 3.3 / 4.4%] book error; derived 2.9 / 3.5 / 4.65% (MPM p.178)
- XYZ Profit Increase Claim [has_value:: 24.4%] on base 2,000 million; Fig 10.3 PBT 2,320 gives about 21.1%, derived
- XYZ Case Study [has_value:: direct purchase 47.4 to 259.5 million baht] while spare stock rose 405.0 to 521.2 (MPM p.179-182, p.212)
- MPM Spare Holding Cost Example [has_value:: 10% WACC finance cost only] XYZ spares (MPM p.180-181) [contested:: true]
- RBMM Holding Cost [has_value:: 15-20% per year] (RBMM p.34) [contested:: true]
- MPM Spare Holding Cost Example [contradicts:: RBMM Holding Cost] MPM-C1; MPM p.84 also gives 20-40% [contested:: true]
- [[Maintenance Financial Impact]] [related_to:: [[Availability and OEE]]] Hidden Plant, OEE to profit
- [[Maintenance Financial Impact]] [related_to:: [[Maintenance Cost Structure]]] fixed/variable, full fix cost rate
- [[Maintenance Financial Impact]] [related_to:: [[Maintenance Business Case]]] payback within 1 year logic
- [[UST Spurious Stop]] [contributes_to:: Hidden Plant] compressor stop lowers Availability Factor, interpretation [confidence:: low]
- [[LOO Low Output]] [contributes_to:: Hidden Plant] lowers Speed Factor, interpretation [confidence:: low]

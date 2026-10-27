---
title: SPO vs RBMM Spare Parts Approaches
created: 2026-10-27
updated: 2026-10-27
type: comparison
tags: [comparison, spare-parts, inventory-control, criticality, kpi, cost, book, spo, cmrp]
sources: [spare-parts-optimization.md, reliability-based-maintenance-management.md, cmrp.md]
confidence: medium
contested: false
---

# SPO vs RBMM Spare Parts Approaches

หน้านี้เทียบแนวทางบริหารอะไหล่ของหนังสือไทยสองเล่ม: **SPO** ([[Spare Parts Optimization Book]], สุชาติ ศุภมงคล 2546) กับ **RBMM** ([[Reliability Based Maintenance Management Book]], บทที่ 9-10) และอ้าง [[CMRP Course]] เมื่อเกี่ยวข้อง สองเล่มมอง "อะไหล่" จากคนละฝั่งขององค์กร: SPO เขียนจากมุม **คลังพัสดุ/จัดซื้อ** (อดีตผู้จัดการคลังโรงกลั่น อิงคู่มือ Esso และ COSAL ของกองทัพเรือสหรัฐฯ) ส่วน RBMM เขียนจากมุม **reliability/ความเสี่ยง** (RCM, Weibull, Monte Carlo) ความต่างส่วนใหญ่จึงเป็นเรื่องบริบทหรือตัวหาร ไม่ใช่ข้อเท็จจริงที่ขัดกัน แต่มี 2 ประเด็นที่ขัดกัน (C1 และ C2 resolve แล้ว 2026-10-27 โดยยึด SPO) (ดูหัวข้อ "ข้อขัดแย้ง (contested)") รายละเอียดแต่ละฝั่งดู [[Spare Parts Management]] และ [[Spare Part Criticality and Risk]]

## 1. สรุปภาพรวม

| ประเด็น | SPO | RBMM | ผลเทียบ |
|---|---|---|---|
| มุมมองหลัก | คลัง/จัดซื้อ/บัญชี: รักษาระดับคงคลังให้ต่ำเชิงเศรษฐศาสตร์แต่ไม่ขาด (SPO p.20-22) | การซื้อความเสี่ยง: Demand Side (PM) + Supply Side (risk based) (RBMM p.234-238) | มุมต่างกัน เสริมกัน |
| การจัดประเภทอะไหล่ | 9 ประเภท (SPO p.26) | 4 ประเภท: commissioning, ซื้อตรง, สำรองคลัง, insurance (RBMM p.15-16, p.235-236, p.251) | ต่างความละเอียด; commissioning ตรงกัน |
| เกณฑ์ตัดสินว่าจะสต็อก | Engineering Basic Practice (ตาราง % ต่อจำนวนเครื่อง) + ปัจจัย 5 ข้อ / 7 ข้อ + คณะกรรมการ (SPO p.40-54, p.129) | Criticality + Confidence Level + Cost Ratio + Monte Carlo (RBMM p.238-264) | ต่างวิธี (กฎเชิงประสบการณ์ vs เชิงสถิติ) |
| Safety stock | % ของ D x LT (ตัวอย่าง 20%) (SPO p.105) | z x sigma_combined (RBMM p.253-255) | ต่างวิธี ไม่ขัดกัน |
| ABC | ABU = จำนวนเบิกต่อปี x ราคา; A = มูลค่าใช้สูง (SPO p.115-117) | Turnover = Qty x Unit Price; ข้อความ A = มูลค่าสูง แต่รูปที่ 9.4 ป้าย A = Very Slow (RBMM p.242-243) | resolved: ยึด SPO (A = มูลค่าใช้สูง) |
| Holding cost | ตัวอย่าง 30%; ให้คำนวณ COP 7 รายการ (SPO p.104, p.120) | 15-20%/ปี (RBMM p.16, p.234); เป้าบทที่ 10 15-25% | ต่างสมมติฐานตัวอย่าง ไม่ใช่ข้อขัดแย้ง |
| เป้ามูลค่าสต็อก | 3% ของเงินลงทุนสร้างโรงงาน (นโยบายตัวอย่าง), ไม่เกิน 4% GPI, benchmark 2/4/10%, ท้ายเล่ม 3-4% GPI (SPO p.55, p.113-115, p.128, p.143-145) | 1-3% ของราคาเครื่องจักร (RBMM p.295, p.314); B7 budget 3% (RBMM p.74) | resolved: ยึด SPO (ไม่เกิน 4% GPI) |
| งานตามแผน vs นอกแผน | สต็อกมีไว้ซ่อมปกติ; turnaround ทำแผน MR/MS แยก (SPO p.35-38, p.55) | ตามแผน = ซื้อตรง, นอกแผน = สต็อก (RBMM p.45, p.236) | สอดคล้องในหลักการ ต่างรายละเอียด |
| Blanket Order | standing PO + ทยอยรับด้วย BOR (SPO p.91-92); consignment แยกต่างหาก (SPO p.95) | ผู้ขายเก็บของในคลังเรา คิดเงินเมื่อเบิก (RBMM p.289, p.298) | ต่างนิยามศัพท์ |
| KPI | Turnover, MOS/DOS, Inventory Value % GPI (SPO p.112-115, p.123-127) | Stock Turnover Rate, Service Factor, Stock out Rate, Stock Value / ARV (RBMM p.239) | นิยาม turnover ตรงกัน; ชุด KPI ต่างกัน |

## 2. การจัดประเภทอะไหล่

| SPO (SPO p.26-31) | ใกล้เคียงใน RBMM / CMRP | ความเห็น |
|---|---|---|
| Unique Parts (เฉพาะเครื่อง ซื้อจาก OEM) | Specific usage part (RBMM p.244) | ตรงกัน |
| Insurance and Standby Parts | Insurance Part (RBMM p.251); CMRP insurance spares (CMRP CMPR-08 p.32-34) | SPO กว้างกว่า (ดูด้านล่าง) |
| Interchangeable Parts | Common usage part (RBMM p.244) | ตรงกัน ดู [[Parts Interchangeability]] |
| Order as Required (OAR) | Direct Purchase Parts / non-stock (RBMM p.236) | คล้ายกัน แต่ OAR อยู่ในทะเบียนคลังโดยสต็อก = 0 (SPO p.109-110) |
| Capitalized Parts | RBMM ไม่มี; CMRP capital spares (CMRP CMPR-08 p.31) | ต่างเรื่องบัญชี (ดูด้านล่าง) |
| General Used Items, Chemical & Gas, Tools | ไม่แยกใน RBMM | SPO ครอบคลุม MRO ทั้งหมด ไม่ใช่เฉพาะอะไหล่ |
| Commissioning spares | Commissioning Spare Part (RBMM p.15-16, p.235) | **ตรงกัน**: เป็นภาระผู้รับเหมา/EPC ไม่ควรเข้าคลังบำรุงรักษาโดยอัตโนมัติ |

รายละเอียดประเภทของ SPO ดู [[MRO Material Classification]]

- **Insurance**: SPO นิยามจาก (ก) อะไหล่ของเครื่อง standby ที่ติดตั้งคู่ A/B (หยุด A เปิด B แล้วซ่อม A ต้องมีอะไหล่แน่นอน) และ (ข) อะไหล่สำคัญที่ขาดแล้วโรงงานหยุด เลือกโดยวิศวกร ติดรหัสต่อท้าย "S" (SPO p.26-27) ส่วน RBMM นิยามแคบกว่าในเชิงความเสี่ยง: เก็บแม้ Cost Ratio ต่ำกว่า 1 เพราะค่าขาดต่อครั้งสูงเกินรับได้ (RBMM p.251) ทั้งสองเล่มให้ระดับบริหาร/คณะกรรมการอนุมัติ (SPO p.55-57, p.131-132; RBMM p.251) จึงสอดคล้องด้าน governance
- **Standby กับ CMRP**: ผังของ CMRP บอกว่า failure ที่สลับไปตัว standby "ไม่สต็อก เว้นแต่ lead time มากกว่า 2 สัปดาห์" (CMRP CMPR-03 p.13) ขณะที่ SPO ให้มั่นใจว่ามีอะไหล่ของคู่ A/B เสมอ ความต่างอธิบายได้ด้วยบริบท: SPO เขียนสำหรับโรงงานไทยที่อะไหล่ส่วนใหญ่นำเข้าและ lead time ยาว ซึ่งเข้าเงื่อนไขข้อยกเว้นของ CMRP อยู่แล้ว (การตีความของ wiki; ไม่ตั้ง contested) ดู [[Redundancy and Standby Systems]]
- **Capitalized Parts vs Current Asset**: RBMM ระบุว่าอะไหล่เป็น Current Asset ไม่มีค่าเสื่อม (RBMM p.16, p.70) SPO เห็นตรงกันสำหรับของสต็อกทั่วไป (SPO p.16-17) แต่เสนอให้ capitalize อะไหล่ประกันราคาสูง (ตัวอย่างเกิน 20,000 บาทต่อหน่วย อายุเกิน 1 ปี) แล้วหักค่าเสื่อมรายปี (SPO p.28-29) เป็นทางเลือกทางบัญชีสำหรับกลุ่มย่อย ไม่ใช่ข้อขัดแย้ง แต่มีผลต่อ KPI: การย้ายมูลค่าออกจากบัญชีวัสดุทำให้ turnover ดูสูงขึ้น (SPO p.29) จึงเทียบ turnover ข้ามองค์กรที่ใช้นโยบายต่างกันไม่ได้

## 3. การตัดสินใจสต็อก

| ขั้น | SPO | RBMM |
|---|---|---|
| จุดเริ่ม | Basic Practice แบบบริษัทอเมริกัน (สต็อกพอ startup + เดินต่อเนื่อง 1 ปี) และแบบญี่ปุ่น (% ของชิ้นที่ติดตั้ง) (SPO p.40-54) ดู [[Spare Parts Recommendation by Equipment Type]] | ประเมิน criticality ของเครื่องและอะไหล่ (กล่องที่ 1) (RBMM p.238, p.243-246) |
| เกณฑ์รายรายการ | 5 ปัจจัย (สึกง่าย, สภาพแวดล้อม, สภาพใช้งาน, ความยากจัดหา, ใช้ร่วม) (SPO p.40); 7 ปัจจัย (อายุ, จำนวนติดตั้ง, เปลี่ยน/ซ่อมได้, ความสำคัญของเครื่อง, ความซับซ้อน, lead time, จุดประสงค์) (SPO p.129) | Price, Lead Time, Failure Detect-ability + Equipment Criticality (RBMM p.243-244) |
| ตัวตัดสินระดับ | Min-Max / Order Up-to ตามคณะกรรมการสำหรับของหมุนช้าและ insurance; ROP/EOQ หรือ High/Low Limit สำหรับของหมุนเร็ว (SPO p.107-110) ดู [[MRO Inventory Control Methods]] | Confidence Level (เป้า A มากกว่า 95%, B 90%, C 80-90%) และ Cost Ratio zone; Monte Carlo สำหรับ high criticality (RBMM p.246-264, p.317-319) |
| ผู้อนุมัติ | Materials Control Committee 18 หน้าที่ (SPO p.131-132) | อำนาจอนุมัติตามโซน Cost Ratio และ risk policy (RBMM p.249-252, p.271) |
| การปรับภายหลัง | ใช้ Basic Practice ก่อน แล้วปรับเมื่อเดินเครื่องจริง 2-3 ปี (SPO p.57-58, p.112) | คำนวณซ้ำได้จากข้อมูลเบิกและ failure data (RBMM p.96, p.267-270) |

- จุดร่วม: ทั้งสองเล่มเห็นว่าคำแนะนำของผู้ผลิตเชื่อถือไม่ได้ทั้งหมด (SPO p.57, p.112: บางรายการไม่เคยเบิก; RBMM p.235: ผู้ขายเสนออะไหล่เกินจำเป็น) และให้วิศวกรของบริษัทตัดสิน
- ความต่าง: SPO ไม่มีแบบจำลองความน่าจะเป็นของการขาด (ไม่มี Poisson/Confidence) ใช้กฎ % และวิจารณญาณ ส่วน RBMM ไม่มีตารางจำนวนอะไหล่ต่อชนิดเครื่อง สองแนวทางจึงใช้ต่อกันได้: Basic Practice ของ SPO เป็นค่าเริ่มต้นเมื่อยังไม่มีสถิติ แล้วเปลี่ยนไปใช้วิธีของ RBMM เมื่อมีข้อมูล (ข้อเสนอของ wiki)
- CMRP อยู่กลางทาง: ผังตัดสินแบบ qualitative + เส้นโค้ง risk cost + holding cost (CMRP CMPR-03 p.12-13)

## 4. Safety stock และ ROP

| | SPO | RBMM | CMRP |
|---|---|---|---|
| ROP | (D x LT) + SS (SPO p.105) | D_avg x LT_avg + SS (RBMM p.253-255) | reorder level (CMRP CMPR-08 p.38-41) |
| SS | % ความผิดพลาดช่วงจัดหา = ความเบี่ยงเบน LT + ความเบี่ยงเบนอัตราใช้ เช่น 10% + 10% = 20% ของ D x LT (SPO p.105) | z x sigma_combined รวม sigma ของ demand และ lead time (RBMM p.253-255) | K x sigma x sqrt(LT) (CMRP CMPR-08 p.41) |
| ตัวอย่าง | D 20, LT 2 เดือน -> ROP = 40 + 8 = 48 (SPO p.105) | ROP ประมาณ 5 ชิ้น ที่ Confidence 90% (RBMM p.255) | - |

- ไม่ขัดกัน: SS แบบ % ของ SPO เป็นกฎง่ายที่ไม่ต้องมีข้อมูลความแปรปรวน แต่ไม่ผูกกับ service level ที่กำหนดได้ ส่วนสูตร z x sigma ให้ Confidence ตรงตามเป้า (ความรู้ทั่วไป) สูตร CMRP เป็นกรณีพิเศษของ RBMM เมื่อ lead time คงที่ ดู [[EOQ and Reorder Point]]
- EOQ: ทั้งสองเล่มใช้สูตรคลาสสิกเดียวกัน; SPO ให้ค่าสั่งซื้อต่อรายการต่อครั้งในไทยราว 90-120 บาท (SPO p.104)

## 5. ABC Analysis

| | SPO (SPO p.115-118) | RBMM (RBMM p.242-243) |
|---|---|---|
| ฐาน | ABU = จำนวนเบิกต่อปี x ราคาต่อหน่วย | Turnover = Qty x Unit Price |
| สัดส่วนมูลค่า | 80 / 15 / 5 (ปรับเป็น 75/20/5 หรือ 70/20/10 ได้) | 80 / 15 / 5 |
| ความหมายของ A | มูลค่าใช้สูง; ตัวอย่างรวมรายการที่เบิกมาก (200,000 หน่วย/ปี) | ข้อความ: มูลค่าสูงสุด 80%; รูปที่ 9.4 ป้าย A = Very Slow, C = fast moving |
| การใช้ | หาเป้าลดสต็อก, ทำ MOS/DOS, เปลี่ยน C เป็น OAR, กลุ่มไม่เคลื่อนไหว 3 ปี = ล้าสมัย | คัดกรองขั้นแรกของ Supply Side; ไม่คำนึง criticality |

- ฐานคำนวณและสัดส่วน **ตรงกัน** ทั้งคู่เตือนว่า ABC ต้องคิดร่วมกับเกณฑ์อื่น (RBMM: criticality; SPO: ABC สองชุด ตามมูลค่าใช้และมูลค่าคงเหลือ SPO p.122-123)
- ป้ายกลุ่ม A ดูหัวข้อ contested ด้านล่าง รายละเอียดโปรแกรมลดสต็อกของ SPO ดู [[MRO Inventory Reduction Program]]

## 6. Holding / carrying cost

| | SPO | RBMM |
|---|---|---|
| อัตรา | ตัวอย่างค่าเก็บรักษา 30% ในการคำนวณผลประหยัด: ลดสต็อกจาก 25 เป็น 15 ล้าน ประหยัด 3 ล้านบาท/ปี (SPO p.120) | ประมาณ 15-20% ต่อปี (RBMM p.16, p.34, p.234); เป้าบทที่ 10 15-25% (RBMM ch10) |
| องค์ประกอบ | COP 7 รายการ: ผลตอบแทนเงินลงทุน, ประกันภัย, ค่าเช่าคลัง, ค่ายกขน, ค่าบริหาร/ควบคุม, ล้าสมัย/เสื่อม, ของหาย (SPO p.104) | ดอกเบี้ย, ค่าจัดเก็บ, ค่าจัดซื้อจัดหา, อะไหล่เสื่อมสภาพ, Write-off (RBMM p.68) |
| ใน EOQ | I = Investment Factor (% ของมูลค่าต่อปี) แยกจาก CO (ค่าสั่งซื้อ) (SPO p.104) | Ch = อัตราค่าถือครอง x ราคาต่อหน่วย (derived ที่ [[EOQ and Reorder Point]]) |

- **ไม่ถือเป็นข้อขัดแย้ง**: 30% ของ SPO เป็นตัวเลขตัวอย่าง และหนังสือแนะนำให้คำนวณ COP จริงของบริษัทแทนการใช้อัตราดอกเบี้ย (SPO p.104, p.143-145) ส่วน 15-20% ของ RBMM เป็นค่าประมาณทั่วไป ทั้งสองเป็นสมมติฐานที่ต้องแทนด้วยค่าจริงขององค์กร
- ข้อควรระวังเชิงนิยาม: RBMM นับ "ค่าจัดซื้อจัดหา" ไว้ใน holding cost ขณะที่ SPO แยกเป็น CO ในสูตร EOQ ถ้าใช้องค์ประกอบของ RBMM ใน EOQ อาจนับค่าสั่งซื้อซ้ำ (ข้อสังเกตของ wiki)

## 7. เป้ามูลค่าสต็อกเทียบมูลค่าโรงงาน

| แหล่ง | ค่า | ตัวหาร | ขอบเขตของตัวตั้ง |
|---|---|---|---|
| SPO นโยบายคลังตัวอย่าง | ไม่เกิน 3% | เงินลงทุนสร้างโรงงาน | มูลค่าคงคลังมาตรฐาน (SPO p.55) |
| SPO บทที่ 10 benchmark (โรงปุ๋ย) | อะไหล่ 2% (ยุโรป/อเมริกา/ญี่ปุ่น), 4% (average เช่น ไทย), 10% (overseas); อื่น ๆ 1/3/8% | GPI มูลค่าปัจจุบัน ไม่รวมที่ดิน/อาคารสำนักงาน | แยกอะไหล่กับอื่น ๆ (SPO p.113-115) |
| SPO บทที่ 10 เกณฑ์ | ไม่เกิน 4% (เน้นเครื่องจักร), ไม่เกิน 1.5% (เน้นแรงงาน) | GPI | MRO ทุกประเภทรวม (SPO p.115) |
| SPO บทที่ 10 บริษัทอเมริกัน | 2-4% (เอเชียตะวันออก); เครื่องหมุนต่อเนื่อง 5-10%; พัสดุซ่อมทั่วไป 1% | เงินลงทุนสร้างโรงงาน | MRO รวมเคมีและพัสดุทั่วไป (SPO p.128) |
| SPO ท้ายเล่ม | 3-4% (เครื่องจักรเป็นหลัก), 1-1.5% (เครื่องไม่ซับซ้อน) | GPI | MRO (SPO p.143-145) |
| RBMM | 1-3% | ราคาเครื่องจักร | อะไหล่ (RBMM p.295, p.314); B7 budget 3%, actual 2.5% (RBMM p.74) |
| RBMM KPI | Stock Value / Asset Replacement Value | มูลค่าซื้อทดแทน | อะไหล่ (RBMM p.239) |

- ตัวหารใกล้กัน (GPI มูลค่าปัจจุบัน vs ราคาเครื่องจักร/มูลค่าซื้อทดแทน) แต่ไม่เหมือนกันเป๊ะ: GPI ของ SPO รวม infrastructure (สาธารณูปโภค ถนน ท่อ) ด้วย (SPO p.113-115) ทำให้ % ของ SPO ควรต่ำกว่าเมื่อตัวตั้งเท่ากัน ไม่ใช่สูงกว่า
- ภายใน SPO เองไม่สอดคล้องทั้งหมด: ตาราง benchmark ให้อะไหล่ 4% + อื่น ๆ 3% ในพื้นที่ average (รวม 7%) แต่เกณฑ์ข้อความให้ MRO รวมไม่เกิน 4% (SPO p.113-115); นโยบายตัวอย่าง 3% vs เกณฑ์ 4% vs ท้ายเล่ม 3-4% ให้ใช้เป็นช่วง ไม่ใช่ค่าเดียว
- ตัวอย่างรายงาน %GPI รายเดือนของ SPO ตั้งเป้า 4% (SPO p.126) ดู [[Inventory Turnover and GPI Benchmarks]]

## 8. งานตามแผน vs นอกแผน และ turnaround

- RBMM: อะไหล่สำรองคลังมีไว้เฉพาะงานนอกแผน งานตามแผนใช้ซื้อตรง (Just in Time) ไม่นับใน Max/Min และ turnover ยกเว้นอะไหล่ใช้ร่วมที่ตาราง PM ไม่พร้อมกัน (RBMM p.45, p.236, p.243)
- SPO: นโยบายคลังให้สต็อกมีไว้ซ่อมบำรุงปกติเท่านั้น overhaul/turnaround ต้องวางแผนความต้องการล่วงหน้า (SPO p.55); ตาราง 4.1 จัด Unique และ Insurance เป็น dependent demand ในงาน Preventive และ Turnaround (SPO p.34) และแผน MR/MS ซื้อผ่าน system contract ตาม ETD/ETA (SPO p.35-38) ดู [[Turnaround Management]]
- **สอดคล้องในหลักการ** (งานตามแผน = วางแผนจัดหา ไม่พึ่งสต็อก) ต่างรายละเอียด: SPO ยอมให้ **จอง (reserve) ของที่มีในคลัง** ให้ turnaround แล้วสั่งแทนที่ (คอลัมน์ Ex Stock, SPO p.36-37) ใกล้กับ stock reservation ของ CMRP (CMRP CMPR-09 p.30) ขณะที่ RBMM ตั้งเป้าให้สต็อกของงานตามแผนเป็น 0 ความต่างเป็นนโยบาย ไม่ใช่ข้อเท็จจริงขัดกัน (เหมือนข้อสรุปเรื่อง CMRP ใน [[Spare Parts Management]])
- SPO ยังมี "custody control sub stock" = ของซื้อตรงเพื่อโครงการที่คลังยังต้องดูแลยอด (SPO p.20-21) เทียบได้กับการแยก turnover ของอะไหล่ซื้อตรงออกจากอะไหล่คลังใน RBMM (RBMM p.243)

## 9. Blanket Order และการจัดซื้อ

| | SPO | RBMM |
|---|---|---|
| Blanket Order | PO แบบ standing ทั้งปีสำหรับของใช้ประจำปริมาณมาก ทยอยรับด้วย Blanket Order Release แล้วจ่ายตามงวดด้วย Partial Delivery Receipt (SPO p.91-93) | ผู้ขายเก็บอะไหล่ในคลังเรา คิดเงินเมื่อเบิก ใช้ให้งานนอกแผนมีของโดยไม่แบกค่าถือครอง (RBMM p.289, p.298) |
| ของฝากขาย | Consignment / Vendor Stocking: ผู้ค้าฝากของในคลังผู้ซื้อ วางบิลเฉพาะที่จ่ายออก (SPO p.95) | ไม่แยกศัพท์ |
| เป้าหมาย | ลดงานเอกสาร (PR ต่ำกว่า 300 USD เป็น 60% ของใบแต่มูลค่า 5%), ราคาแน่นอน, รากฐาน JIT (SPO p.91-94) | ลดค่าถือครอง |

- **ต่างนิยามศัพท์**: สิ่งที่ RBMM เรียก Blanket Order ตรงกับสิ่งที่ SPO เรียก Consignment / Vendor Stocking ส่วน Blanket Order ของ SPO คือสัญญาซื้อระยะยาวที่ทยอยรับของ (ซึ่งตรงกับความหมายทั่วไปของคำนี้ ความรู้ทั่วไป) เป้าหมายร่วมกันคือย้ายภาระสต็อกไปที่ผู้ขาย จึงไม่ใช่ข้อขัดแย้งทางเนื้อหา แต่เวลาเขียนสัญญาต้องระบุกลไกให้ชัด ไม่ใช่อ้างแค่ชื่อ ดู [[MRO Purchasing and Contracting]]

## 10. KPI และนิยาม turnover

| KPI | SPO | RBMM |
|---|---|---|
| Turnover | ยอดจ่าย(ขาย)ทั้งปี / คงคลังเฉลี่ย (เฉลี่ยจากยอดปลายงวด) เป็น "เท่า" เช่น 90/30 = 3 (SPO p.112) | มูลค่าอะไหล่ที่เบิกออก / มูลค่าอะไหล่ทั้งหมดในคลัง เป็น % เช่น B8 = 40% (RBMM p.74-75, p.239) |
| ระยะเวลา | MOS = 12 / Turnover, Days = 360 / Turnover; DOS = On Hand / Usage per Day (SPO p.113, p.125) | ไม่มี |
| เทียบมูลค่าโรงงาน | Inventory Value % GPI (SPO p.113-115) | Stock Value / Asset Replacement Value; B7 (RBMM p.74, p.239) |
| ระดับบริการ | ไม่มีสูตร (กล่าวถึง "ไม่ลด % บริการ" SPO p.143-145) | Service Factor, Stock out Rate (RBMM p.239) |

- นิยาม turnover **โดยหลักตรงกัน** (มูลค่าใช้ต่อมูลค่าคงคลัง) ต่างที่หน่วย: SPO เป็นจำนวนรอบ/ปี ใช้คงคลังเฉลี่ย, RBMM เป็น % ไม่ระบุว่าใช้คงคลังเฉลี่ยหรือ ณ จุดเวลา (derived: B8 = 40% เท่ากับ 0.4 รอบ/ปี หรือ MOS 30 เดือน)
- ทั้งสองเห็นว่า turnover เดี่ยว ๆ ไม่พอสำหรับอะไหล่: SPO บอกว่าใช้ได้กับของหมุนเร็วเท่านั้น จึงใช้ %GPI แทน และตัวอย่าง MOS รวม 4.9 เดือนบดบังอะไหล่ที่ 41 เดือน (SPO p.113, p.127); RBMM ให้แยก turnover ของอะไหล่ซื้อตรงออก (RBMM p.243) และอ่านคู่กับ B7, B9, B10 ดู [[Maintenance KPIs]]

## ข้อขัดแย้ง (contested, resolved 2026-10-27)

### C1. ความหมายของกลุ่ม A ใน ABC (resolved 2026-10-27)

- มุมมอง SPO (spare-parts-optimization.md): A = รายการมูลค่าใช้ต่อปี (ABU) สูงสุดราว 80% ตัวอย่างกลุ่ม A รวมรายการที่เบิก 200,000 หน่วย/ปี จึงไม่ได้หมายถึงหมุนช้า (SPO p.115-117)
- มุมมอง RBMM (reliability-based-maintenance-management.md): ข้อความหน้า 242 ให้ A = มูลค่า turnover สูงสุด 80% (ตรงกับ SPO) แต่รูปที่ 9.4 ติดป้าย A = Very Slow และ C = fast moving (RBMM p.242-243)
- สถานะ: ยังไม่ resolve ข้อความของทั้งสองเล่มตรงกัน แต่ป้ายในรูปของ RBMM ขัดกับทั้งข้อความ RBMM เองและ SPO น่าจะเป็นความผิดพลาดของรูป แต่ยังไม่ได้ตรวจกับหน้าหนังสือ RBMM ต้นฉบับ (ข้อเสนอ: ใช้ความหมาย "A = มูลค่าใช้สูง" ไปก่อน) (ข้อความเดิมก่อน resolve)
- ผู้ใช้ตัดสิน 2026-10-27: ยึดตาม SPO คือ A = มูลค่าใช้สูง ป้าย Very Slow ในรูปที่ 9.4 ของ RBMM ถือเป็นความผิดพลาดของรูป (resolved)

### C2. ระดับเป้ามูลค่าสต็อกอะไหล่ต่อมูลค่าโรงงาน (resolved 2026-10-27)

- มุมมอง SPO (spare-parts-optimization.md): โรงงานเน้นเครื่องจักรในพื้นที่แบบไทย ใช้ 4% ของ GPI (benchmark อะไหล่ 4%, เกณฑ์ MRO รวมไม่เกิน 4%, ท้ายเล่ม 3-4%) (SPO p.113-115, p.143-145) และอาจถึง 5-10% สำหรับเครื่องหมุนต่อเนื่อง (SPO p.128)
- มุมมอง RBMM (reliability-based-maintenance-management.md): เป้า 1-3% ของราคาเครื่องจักร (RBMM p.295, p.314) และตัวอย่าง budget B7 = 3% (RBMM p.74)
- สถานะ: ยังไม่ resolve ช่วงทับกันที่ 3% แต่ค่าแนะนำหลักของ SPO (4%) สูงกว่าขอบบนของ RBMM ความต่างอาจมาจาก (1) ข้อมูลของ SPO มาจากโครงการ Esso ปี 1978-1980 และโรงปุ๋ย (SPO p.113, p.143-145) (2) ตัวตั้งของ SPO บางจุดรวม MRO ทั้งหมด (3) ตัวหารต่างกันเล็กน้อย แต่ไม่มีเล่มใดอธิบายความต่างนี้ ควรใช้เป็นช่วง 1-4% และเทียบกับ benchmark ของอุตสาหกรรมเดียวกันเอง (ข้อความเดิมก่อน resolve)
- ผู้ใช้ตัดสิน 2026-10-27: ยึดเป้ามูลค่าสต็อกตาม SPO คือไม่เกิน 4% ของ GPI (3-4% สำหรับโรงงานเน้นเครื่องจักรในไทย, 1-1.5% สำหรับเครื่องจักรไม่ซับซ้อน) ค่า 1-3% ของ RBMM เก็บไว้เป็นข้อมูลอ้างอิง (resolved)

## เชื่อมโยงกับ compressor failure hierarchy

- SPO มีตารางจำนวนอะไหล่แนะนำต่อชิ้นของ [[Centrifugal Compressor]] และ [[Reciprocating Compressor]] (เช่น ชิ้นวาล์ว 400%) (SPO p.50-53) ซึ่งเป็นจุดเริ่มแบบ Basic Practice ส่วน RBMM ให้วิธีปรับจำนวนด้วยข้อมูล failure mode รายเครื่อง แนวทางผสมคือเริ่มจากตาราง SPO แล้วปรับด้วย failure rate ของ [[Maintainable Item]] จาก [[OREDA]] (ข้อเสนอของ wiki ไม่ใช่ข้อความในหนังสือ)
- compressor standby (A/B) เป็นกรณี Insurance and Standby ของ SPO และเป็นกรณีสลับตัวสำรองของ CMRP ดูหัวข้อ 2

## ดูเพิ่ม

- [[Spare Parts Management]]
- [[Spare Part Criticality and Risk]]
- [[EOQ and Reorder Point]]
- [[MRO Inventory Control Methods]]
- [[Inventory Turnover and GPI Benchmarks]]
- [[MRO Inventory Reduction Program]]
- [[MRO Purchasing and Contracting]]
- [[CMRP vs RBMM FMECA Scales]]

## Triplets

- [[SPO vs RBMM Spare Parts Approaches]] [related_to:: [[Spare Parts Management]]] comparison of SPO and RBMM
- [[SPO vs RBMM Spare Parts Approaches]] [related_to:: [[Spare Parts Optimization Book]]]
- [[SPO vs RBMM Spare Parts Approaches]] [related_to:: [[Reliability Based Maintenance Management Book]]]
- [[Spare Parts Optimization Book]] [differs_from:: [[Reliability Based Maintenance Management Book]]] stores/purchasing viewpoint vs reliability/risk viewpoint
- SPO Spare Part Classification [has_value:: 9 categories] unique, insurance and standby, interchangeable, OAR, capitalized, general used, chemical and gas, tools, commissioning (SPO p.26)
- SPO Spare Part Classification [differs_from:: RBMM Spare Part Types] 9 categories vs commissioning, direct purchase, stock, insurance (RBMM p.235-236, p.251)
- Commissioning Spare Part [related_to:: Commissioning Spares] contractor responsibility in both books (SPO p.30-31; RBMM p.235); agreement
- Insurance and Standby Parts [related_to:: Insurance Part] SPO broader (standby A/B parts and critical parts), RBMM risk-based Cost Ratio below 1 (SPO p.26-27; RBMM p.251)
- Insurance and Standby Parts [differs_from:: Switch to Standby Case] SPO always stock for A/B pairs; CMRP stock only if lead time more than 2 weeks; context difference, not contested (CMRP CMPR-03 p.13)
- Order as Required [related_to:: Direct Purchase Parts] OAR kept in stock register with zero stock (SPO p.109-110; RBMM p.236)
- Capitalized Parts [differs_from:: Current Asset] SPO capitalizes high-value insurance spares above 20,000 THB and life above 1 year; RBMM treats spares as current asset (SPO p.28-29; RBMM p.16, p.70)
- Capitalized Parts [related_to:: Stock Turnover Rate] capitalization raises turnover, KPI comparability issue (SPO p.29)
- SPO Stocking Decision [uses:: Engineering Basic Practice] percentage tables per number of installed units (SPO p.40-54)
- SPO Stocking Decision [depends_on:: 7 Stocking Factors] life, installed qty, replace or repair, criticality, complexity, lead time, purpose (SPO p.129)
- RBMM Stocking Decision [uses:: Cost Ratio] with Confidence Level and Monte Carlo (RBMM p.246-264)
- SPO Stocking Decision [differs_from:: RBMM Stocking Decision] experience rules vs statistical risk; complementary
- SPO Safety Stock [has_formula:: percent of D x LT] example 10% + 10% = 20% (SPO p.105)
- SPO Reorder Point [has_value:: 48] D 20, LT 2 months, SS 8 (SPO p.105)
- SPO Safety Stock [differs_from:: Safety Stock] RBMM z x sigma_combined (RBMM p.253-255); method difference, not contested
- ABU [has_formula:: annual issue qty x unit cost] (SPO p.116)
- ABU [related_to:: Turnover] same basis as RBMM Qty x Unit Price (RBMM p.242-243)
- ABC Turnover Group A [has_category:: high usage value] SPO, about 80% of ABU (SPO p.115-117); resolved 2026-10-27 by user
- ABC Turnover Group A [contradicts:: Very Slow] RBMM Fig 9.4 label judged wrong (RBMM p.243)
- Holding Cost [has_value:: 30%] SPO example in inventory reduction saving (SPO p.120)
- Holding Cost [has_value:: 15-20%] RBMM per year (RBMM p.16, p.234); differs from SPO example, assumption not contradiction
- Cost of Possession [has_part:: 7 cost items] return on investment, insurance, rent, handling, administration, obsolescence, loss (SPO p.104)
- Cost of Possession [alias_of:: Holding Cost] SPO afterword calls COP carrying cost (SPO p.143-145)
- Procurement Cost [part_of:: Holding Cost] RBMM includes it; SPO keeps order cost separate in EOQ, possible double count (RBMM p.68; SPO p.104)
- Inventory Value % GPI [has_value:: 4%] SPO target for capital intensive plants in average area (SPO p.115, p.126); adopted by user 2026-10-27
- Inventory Value % GPI [has_value:: 3-4%] SPO afterword recommendation for Thai machinery plants (SPO p.143-145); adopted by user 2026-10-27
- Standard Inventory Value [has_value:: not above 3% of plant construction investment] SPO warehouse policy example (SPO p.55)
- B7 Spare Part Inventory / Plant Asset [has_value:: 1-3%] RBMM target of machine price (RBMM p.295, p.314); reference only, not adopted
- Inventory Value % GPI [contradicts:: B7 Spare Part Inventory / Plant Asset] SPO 4% above RBMM upper 3%; denominators close but not identical; resolved 2026-10-27, follow SPO
- Inventory Value % GPI [related_to:: Stock Value / Asset Replacement Value] similar denominator, GPI current value including infrastructure
- Direct Purchase Parts [applies_to:: Planned Maintenance] RBMM rule (RBMM p.45, p.236)
- MR/MS Table [applies_to:: Turnaround] SPO plans turnaround materials separately from regular stock (SPO p.35-38, p.55)
- MR/MS Table [uses:: Stock Reservation] Ex Stock items reserved then replenished (SPO p.36-37); policy difference from RBMM, not contested
- Blanket Order [differs_from:: Consignment] SPO Blanket Order = standing PO with releases; SPO consignment = vendor stock billed on issue (SPO p.91-95)
- Blanket Order [alias_of:: Consignment] RBMM usage, vendor stock in our store billed on issue (RBMM p.289, p.298); terminology difference
- Stock Turnover Rate [has_formula:: value of parts issued / total value of parts in store] RBMM, percent (RBMM p.239)
- Inventory Turnover [has_formula:: annual usage / average inventory] SPO, times per year (SPO p.112)
- Inventory Turnover [related_to:: Stock Turnover Rate] same concept, different unit and averaging
- Month of Supply [has_formula:: 12 / Inventory Turnover] (SPO p.113)
- Month of Supply [has_value:: 41.17 months] maintenance and repair materials vs total 4.9 months, aggregate hides slow movers (SPO p.127)

---
title: Inventory Turnover and GPI Benchmarks
created: 2026-10-27
updated: 2026-10-27
type: concept
tags: [spo, book, spare-parts, kpi, inventory-control, cost]
sources: [spare-parts-optimization.md, reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Inventory Turnover and GPI Benchmarks (ดัชนีความเหมาะสมของคลังอะไหล่ MRO)

หน้านี้สรุปดัชนีวัด "คลังอะไหล่/วัสดุ MRO มากหรือน้อยเกินไปหรือไม่" จากบทที่ 10 ของ [[Spare Parts Optimization Book]] (SPO) ได้แก่ Inventory Turnover, MOS/Days Inventory/DOS และ Inventory Value % GPI พร้อม benchmark ที่หนังสือให้ และเทียบกับดัชนี B7/B8 ของ RBMM ใน [[Maintenance KPIs]] และ [[Spare Parts Management]] การนำดัชนีไปใช้ลดคงคลังอยู่ที่ [[MRO Inventory Reduction Program]]

ผู้เขียนแนะนำให้เริ่มวัดดัชนีหลังเดินโรงงานราว 3 ปี เมื่อเครื่องผ่านช่วง burn-in และมีสถิติการเบิกพอคำนวณ เพราะรายการสต็อกตามคำแนะนำผู้ผลิตมักผิด บางรายการไม่เคยเบิก บางรายการนอกรายการกลับต้องสั่งด่วน (SPO p.112)

## 1. Inventory Turnover Ratio (Stock Turn) (SPO p.112-113)

```
Inventory Turnover = Annual Sale (หรือยอดจ่ายทั้งปี) / Average Inventory
Average Inventory  = ผลรวมยอดคงเหลือปลายงวด (เช่น ทุกสิ้นเดือน) / จำนวนงวดในปี
```

- สำหรับคลัง MRO ใช้ "ยอดจ่าย" แทน "ยอดขาย"
- ตัวอย่าง: ยอดขาย 90 ล้าน/ปี คงเหลือเฉลี่ย 30 ล้าน -> Turnover = 3 รอบ/ปี (SPO p.112)

## 2. ระยะเวลาของคงคลัง: MOS, Days Inventory, DOS (SPO p.113, p.123, p.125)

```
MOS (Month of Supply)  = 12 / Inventory Turnover          -> 12/3 = 4 เดือน
Days Inventory         = 360 / Inventory Turnover         -> 360/3 = 120 วัน
MOS (รายรายการ)        = สต็อกที่มี / ความต้องการต่อเดือน
DOS (Day of Supply)    = On Hand / Usage per Day
Turnover Months (MOS)  = Inventory at Year End x 12 / Usage During Year
```

- ค่า MOS/DOS ยิ่งสูงยิ่งหมุนช้า (ตรงข้ามกับ turnover ratio) หนังสือบางตอนเรียก MOS ว่า "อัตราหมุนเวียนเป็นเดือน" ซึ่งชวนสับสน (SPO p.122)
- หนังสือใช้ปี 360 วัน; ถ้าใช้ 365 วัน ตัวเลขวันจะต่างเล็กน้อย (หมายเหตุ wiki)

### ค่ามาตรฐานสินค้าสำเร็จรูป (US Dept. of Commerce, Bureau of Economic Analysis) (SPO p.113)

| ประเภทบริษัท | Month Sale | % of Annual Sale | Inventory Turnover |
|---|---|---|---|
| Manufacturing | 1.5 | 12.5 | 8 |
| Retail | 1.4 | 11.16 | 9 |
| Wholesale | 1.2 | 10.0 | 10 |

- ตรวจเลข (derived): Manufacturing 12/8 = 1.5 และ 1/8 = 12.5% ตรง; Wholesale 12/10 = 1.2 และ 10% ตรง; **Retail turnover 9 ควรได้ 12/9 = 1.33 เดือน และ 1/9 = 11.11%** แต่หนังสือพิมพ์ 1.4 และ 11.16 (ไม่สอดคล้องภายในแถว)
- ข้อจำกัด: ดัชนี turnover และ MOS ใช้ได้กับพัสดุทั่วไปและอะไหล่หมุนเร็วเท่านั้น คลัง MRO มีหมุนเร็ว/ปานกลาง/ช้าปนกัน จึงต้องวัดเทียบเงินลงทุนโรงงานด้วย %GPI (SPO p.113) บันทึกท้ายเล่มย้ำว่า turnover แบบสินค้าสำเร็จรูปไม่เหมาะกับวัสดุโรงงานที่เคลื่อนไหวไม่แน่นอนและหมุนช้า (SPO p.143-145)

### ตัวอย่างรายงาน Month of Supply (บริษัทผลิตน้ำมันเครื่อง, หน่วย 1,000 บาท) (SPO p.127)

| หมวด | Inventory 31 Dec | Usage/Year | Turnover Months |
|---|---|---|---|
| Maintenance and Repair | 20,070 | 5,850 | 41.17 |
| General Supplies | 6,450 | 7,230 | 10.70 |
| Catalysts | 5,230 | 4,800 | 13.07 |
| Chemical | 5,010 | 67,320 | 0.89 |
| Containers Packings | 512 | 8,412 | 0.73 |
| Commissary | - | - | - |
| Surplus Remaining | 1,050 | ไม่ระบุ | ไม่ระบุ |
| Total | 38,322 | 93,612 | 4.9 |

- ทุกแถวคำนวณถูก รวมได้ 4.91 เดือน (derived) ข้อสังเกต: อะไหล่ซ่อมบำรุงค้างราว 41 เดือน ขณะที่เคมี/บรรจุภัณฑ์ไม่ถึง 1 เดือน ตัวเลขรวม 4.9 เดือนจึงบดบังปัญหาอะไหล่หมุนช้า ควรรายงานแยกหมวด

### ตาราง DOS ปัจจุบันเทียบเป้า (SPO p.125)

```
Variance = (Target DOS - Current DOS) x Usage/day x Unit Value
```

| Item | On Hand | Usage/Day | Unit Value | DOS Current / Target | Variance (บาท) ตามหนังสือ | ทิศทาง |
|---|---|---|---|---|---|---|
| 1 | 800 | 100 | 200 | 8 / 5 | (60,000) | ลด |
| 2 | 300 | 50 | 300 | 6 / 7 | 15,000 | เพิ่ม |
| 3 | 675 | 75 | 150 | 9 / 7 | (22,000) | ลด |
| 4 | 2,000 | 200 | 50 | 10 / 12 | 20,000 | เพิ่ม |
| สุทธิ | | | | | คาดลดได้ 47,000 | |

- **ข้อผิดพลาดในหนังสือ** (derived): Item 3 = (7 - 9) x 75 x 150 = **(22,500)** ไม่ใช่ (22,000) ยอดลดสุทธิที่ถูกคือ **47,500** (หนังสือ 47,000 สอดคล้องกับค่า 22,000 ที่ผิด จึงน่าจะผิดตั้งแต่ต้นฉบับ) แถวอื่นถูก
- ตารางนี้แสดงว่าการตั้งเป้า DOS รายรายการอาจ "เพิ่ม" สต็อกบางรายการได้ ไม่ใช่ลดอย่างเดียว

## 3. Inventory Value % GPI (SPO p.113-115)

```
Inventory Value % GPI = Inventory Value / GPI x 100
```

- **GPI (Gross Plant Investment)** = เงินลงทุนสร้างโรงงาน คิดเฉพาะเครื่องจักรที่ใช้ผลิตหลัก: Power Plant (Boiler, Generator, Pump, Compressor), Infrastructure (ไฟฟ้า ประปา ท่อส่งเชื้อเพลิง/ผลิตภัณฑ์ ถนน), Equipment (เครื่องมือ เครื่องยนต์ อาคารเครื่องจักร เช่น Power House, Control Room)
- **ไม่รวมที่ดินและอาคารสำนักงาน** และใช้ **มูลค่าปัจจุบัน** ไม่ใช่มูลค่าทางบัญชีหรือราคาซื้อครั้งแรก
- คำนวณจากมูลค่าคงคลัง ณ วันใดวันหนึ่ง (สิ้นเดือน/สิ้นปี) เทียบ GPI ณ วันเดียวกัน ตัวอย่าง 68 / 600 x 100 = 11.33% (ตรวจแล้วถูก)
- ที่มาของแนวคิด: Esso วัด MRO inventory เป็น % ของ GPI เก็บข้อมูลทุก 6 เดือนนาน 3 ปีจากโรงงานทั่วโลก ในโครงการ optimization ปี 1978-1980 ที่ผู้เขียนร่วมด้วย เป้าคือลดสต็อกโดยไม่ลด % บริการ (SPO p.143-145)

### Benchmark ตามพื้นที่ (Fertilizer Plant MRO Inventory Level, %) (SPO p.114)

| กลุ่ม | Europe/USA/Japan | Average area | Overseas |
|---|---|---|---|
| Spare Parts | 2 | 4 | 10 |
| Other | 1 | 3 | 8 |

- Europe/USA/Japan = ประเทศอุตสาหกรรม ส่งกำลังบำรุงพร้อม
- Average area = มีตัวแทนจำหน่ายและสต็อกตัวแทน เช่น ไทย มาเลเซีย อินโดนีเซีย สิงคโปร์
- Overseas = ห่างศูนย์กระจายสินค้า ไม่มีตัวแทน หรือห่างทะเล ขนส่งลำบาก เช่น ลาว พม่า กัมพูชา มองโกเลีย ทิเบต คาซัคสถาน
- (ตารางต้นฉบับมีแถว Machinery เป็นหัวกลุ่มไม่มีตัวเลข)

### เกณฑ์อื่นในเล่ม (รวบรวมไว้ที่เดียว)

| เกณฑ์ | ค่า | ขอบเขตตัวเศษ | อ้างอิง |
|---|---|---|---|
| โรงงานเน้นเงินลงทุนเครื่องจักร | ไม่เกิน 4% ของ GPI | MRO ทุกประเภท (หมุนเร็ว+ปานกลาง+ช้า) | SPO p.115 |
| โรงงานใช้แรงงานคนมาก | ไม่เกิน 1.5% หรือน้อยกว่า | MRO ทุกประเภท | SPO p.115 |
| บริษัทอเมริกันแห่งหนึ่ง สาขาเอเชียตะวันออก | 2-4% ของเงินลงทุนสร้างโรงงาน | MRO รวมเคมีและพัสดุทั่วไป | SPO p.128-129 |
| อะไหล่เครื่องจักรหมุน/เดินต่อเนื่องที่สึกหรอ | อาจสูงถึง 5-10% | อะไหล่กลุ่มนี้ | SPO p.128-129 |
| พัสดุซ่อมทั่วไป (วาล์ว ท่อ อุปกรณ์ท่อ) | 1% หรือน้อยกว่า | หาง่าย lead time สั้น | SPO p.128-129 |
| นโยบายคลังของอุตสาหกรรมหนักแห่งหนึ่ง | ไม่เกิน 3% ของเงินลงทุนสร้างโรงงาน | มูลค่าคงคลังมาตรฐาน | SPO p.55-57 |
| ข้อเสนอสำหรับโรงงานไทย (บันทึกท้ายเล่ม) | 3-4% ของ GPI | โรงงานเครื่องจักร/เครื่องยนต์เป็นหลัก | SPO p.143-145 |
| ข้อเสนอสำหรับโรงงานไทย (บันทึกท้ายเล่ม) | ราว 1-1.5% | เครื่องจักรไม่ซับซ้อน เช่น จักรเย็บผ้า | SPO p.143-145 |

- กลุ่ม 5-10% และ 1% หนังสือไม่ได้ระบุชัดว่าเป็น % ของฐานใด (GPI ทั้งโรงงาน หรือมูลค่าเครื่องกลุ่มนั้น) การอ่านว่าเป็น % ของเงินลงทุนส่วนที่เกี่ยวข้องเป็นการตีความ [confidence:: low]
- ตัวเลขในเล่มเองไม่เป็นค่าเดียว (3%, 4%, 3-4%, 2-4%) แต่สอดคล้องกันเป็นช่วง 2-4% สำหรับโรงงานเครื่องจักรในพื้นที่แบบไทย ความต่างมาจากขอบเขตตัวเศษ (อะไหล่อย่างเดียว vs MRO รวม) และบริบท (นโยบายภายใน vs benchmark)
- เลือกหรือหาค่าเองด้วยวิธีในบทที่ 10 ได้ (SPO p.143-145)

### ตัวอย่างรายงานรายเดือนเทียบเป้า 4% (SPO p.126)

| เดือน | OH Value | GPI | %/GPI ตามหนังสือ | Target |
|---|---|---|---|---|
| Jan | 65.1 | 1000 | 6.51 | 4 |
| Feb | 72.3 | 1100 | 6.57 | 4 |
| Mar | 71.5 | 1200 | 5.96 | 4 |
| Apr | 68.4 | 1200 | 5.70 | 4 |
| May | 60.3 | 1200 | 5.02 | 4 |
| Jun | 59.6 | 1200 | 4.97 | 4 |
| Jul | 60.7 | 1200 | 5.05 | 4 |
| Aug | 55.3 | 1200 | 4.60 | 4 |
| Sept | 52.1 | 1200 | 4.34 | 4 |
| Oct | 51.5 | 1200 | 4.29 | 4 |
| Nov | 49.8 | 1250 | 3.98 | 4 |
| Dec | 49.8 | 1250 | 3.58 | 4 |

- **ข้อผิดพลาดในหนังสือ** (derived): Dec 49.8 / 1250 = **3.98%** แต่พิมพ์ 3.58 (ถ้า OH = 44.8 จะได้ 3.58) แปลว่าค่า OH หรือ % ของ Dec ผิดอย่างใดอย่างหนึ่ง; May 5.025, Jul 5.058, Aug 4.608 ถูกตัดทศนิยมแทนการปัด
- ข้อสังเกต: GPI โต (1000 -> 1250) ทำให้ % ลดลงแม้ OH คงที่ ควรดู OH Value คู่กัน

## 4. เทียบกับ RBMM: B7 และ Stock Turnover

| ประเด็น | SPO | RBMM |
|---|---|---|
| ดัชนีมูลค่าคลังต่อทรัพย์สิน | Inventory Value % GPI (SPO p.113-115) | B7 Spare Part Inventory / Plant Asset; Stock Value / Asset Replacement Value (RBMM p.74, p.239) |
| ตัวหาร | GPI = มูลค่าปัจจุบันของเครื่องจักรผลิตหลัก + infrastructure + equipment ไม่รวมที่ดิน/สำนักงาน | Plant asset ที่มูลค่าซื้อทดแทน (replacement value) / ราคาเครื่องจักร |
| ตัวเศษ | มูลค่าคงคลัง MRO (บางเกณฑ์รวมเคมีและพัสดุทั่วไป) หรือเฉพาะ spare parts | มูลค่าอะไหล่ในคลัง |
| เป้า/benchmark | spare parts 2 / 4 / 10% ตามพื้นที่; MRO รวม ไม่เกิน 4% (1.5% แรงงานมาก); 3% (นโยบาย ch5); 3-4% (ข้อเสนอไทย) | เป้า 1-3% ของราคาเครื่องจักร (RBMM p.295, p.314); ตัวอย่าง actual 2.50% budget 3.00% (RBMM p.74-75) |
| Turnover | Annual usage / Average Inventory เป็น "รอบ/ปี" (SPO p.112) | มูลค่าที่เบิกออก / มูลค่าอะไหล่ทั้งหมดในคลัง แสดงเป็น % เช่น B8 40% (RBMM p.239, p.74-75) |
| การใช้ turnover กับอะไหล่หมุนช้า | ใช้ไม่ได้ ให้ใช้ %GPI แทน | ใช้ B8 คู่กับ B7, B9, B10 และ turnover ต่ำ = เสี่ยง dead stock/write-off |
| ต้นทุนการถือครอง | ตัวอย่างใช้ค่าเก็บรักษา 30% (SPO p.120); COP 7 ชนิด (SPO บทที่ 9) | holding cost 15-20% ต่อปี (RBMM p.16, p.34, p.234) |

ข้อสรุปของ wiki (การตีความ):

- **Turnover: ไม่ขัดกัน** เป็นแนวคิดเดียวกัน ต่างหน่วย (รอบ vs %) และตัวหาร (ค่าเฉลี่ยทั้งปี vs ยอด ณ จุดเวลา) แปลงได้: B8 40% = 0.40 รอบ/ปี = MOS 12/0.40 = 30 เดือน (derived) ซึ่งใกล้กับตัวอย่าง MRO ของ SPO (30 เดือนในตารางลดสต็อก p.121-122, 41 เดือนในรายงาน p.127) สอดคล้องกับข้อสังเกตของ SPO ว่าอะไหล่ซ่อมบำรุงหมุนช้ามาก
- **มูลค่าคลังต่อทรัพย์สิน: ไม่ใช่ข้อขัดแย้งแท้** ตัวหารใกล้เคียงกัน (ทั้งคู่ใช้มูลค่าปัจจุบัน/ทดแทนของเครื่องจักร) แต่ SPO ไม่รวมที่ดิน/อาคารสำนักงานชัดเจน ส่วน RBMM ใช้ "plant asset" ตัวเศษของ SPO หลายเกณฑ์รวม MRO ทั้งหมด ส่วน RBMM นับอะไหล่อย่างเดียว ช่วงตัวเลขซ้อนกันที่ 2-3%: RBMM 1-3% ตรงกับช่วง "ประเทศอุตสาหกรรม 2%" ถึง "นโยบาย 3%" ของ SPO แต่ benchmark พื้นที่แบบไทยของ SPO (4%, 3-4%) สูงกว่าเพดาน 3% ของ RBMM ผลในทางปฏิบัติ: โรงงานในไทยที่ 3.5% จะ "เกินเป้า" ตาม RBMM แต่ "อยู่ใน benchmark" ตาม SPO ให้ระบุว่าเทียบกับเกณฑ์ใดและนับตัวเศษอะไร
- ทั้งสองเล่มเตือนตรงกันว่าดัชนีนี้เป็นแนวทาง ไม่ใช่ตัวชี้ขาด (RBMM p.74; SPO ให้หาค่าเองได้ p.143-145)
- เรื่องอัตราค่าถือครอง 30% vs 15-20% ดูการวิเคราะห์ที่ [[MRO Inventory Reduction Program]] (สรุป: 30% ของ SPO เป็นค่าสมมติในตัวอย่าง ไม่ขัดแท้)
- ภาพรวมการเทียบสองเล่มอยู่ที่ [[SPO vs RBMM Spare Parts Approaches]]

## เชื่อมโยงกับ compressor failure hierarchy

- GPI นับ [[Compressor]] (ใน Power Plant) เป็นส่วนของเงินลงทุนหลัก ดังนั้นมูลค่าทดแทนของ compressor เข้าตัวหาร (ตีความจาก SPO p.114)
- อะไหล่ compressor เป็นเครื่องจักรหมุน/เดินต่อเนื่องที่สึกหรอ ซึ่ง SPO ยอมให้สัดส่วนสูงถึง 5-10% (SPO p.128-129) การตัดสินรายรายการยังต้องใช้ criticality ตาม [[Spare Part Criticality and Risk]] (การตีความของ wiki)

## ดูเพิ่ม

- [[MRO Inventory Reduction Program]]
- [[MRO Inventory Control Methods]]
- [[Maintenance KPIs]]
- [[Spare Parts Management]]
- [[EOQ and Reorder Point]]

## Triplets

- [[Inventory Turnover and GPI Benchmarks]] [defined_in:: [[Spare Parts Optimization Book]]] chapter 10 (SPO p.112-127)
- Inventory Turnover [is_a:: Maintenance KPI] stock turn for MRO inventory (SPO p.112)
- Inventory Turnover [has_formula:: Annual Sale or Issues / Average Inventory] (SPO p.112)
- Average Inventory [has_formula:: sum of period-end balances / number of periods per year] (SPO p.112)
- Inventory Turnover [has_value:: 3] example 90 / 30 million (SPO p.112)
- Month of Supply [has_formula:: 12 / Inventory Turnover] example 12/3 = 4 months (SPO p.113)
- Days Inventory [has_formula:: 360 / Inventory Turnover] example 120 days (SPO p.113)
- Day of Supply [has_formula:: On Hand / Usage per Day] (SPO p.125)
- DOS Variance [has_formula:: (Target DOS - Current DOS) x Usage per day x Unit Value] (SPO p.125)
- DOS Variance [has_value:: 47,500 baht reduction] derived; book prints 47,000 because item 3 printed (22,000) instead of (22,500)
- Month of Supply [differs_from:: Inventory Turnover] higher MOS = slower; book calls MOS a monthly turnover rate (SPO p.122)
- Inventory Turnover [applies_to:: Fast Moving Parts] not valid for slow-moving MRO, use % GPI (SPO p.113)
- Inventory Turnover [has_value:: 8] manufacturing, 1.5 months, 12.5% (US Dept of Commerce, SPO p.113)
- Inventory Turnover [has_value:: 9] retail; book prints 1.4 months and 11.16%, derived 1.33 and 11.11% (SPO p.113)
- Inventory Turnover [has_value:: 10] wholesale, 1.2 months, 10.0% (SPO p.113)
- Maintenance and Repair Inventory [has_value:: 41.17 months] MOS example, total 4.9 months hides slow spares (SPO p.127)
- Inventory Value % GPI [is_a:: Maintenance KPI] (SPO p.113-115)
- Inventory Value % GPI [has_formula:: Inventory Value / GPI x 100] (SPO p.113)
- Inventory Value % GPI [depends_on:: Gross Plant Investment] (SPO p.113-114)
- Gross Plant Investment [has_part:: Power Plant] with Infrastructure and Equipment; excludes land and office buildings; current value (SPO p.114)
- Gross Plant Investment [has_part:: [[Compressor]]] inside Power Plant group (SPO p.114)
- Inventory Value % GPI [has_value:: 11.33%] example 68 / 600 (SPO p.114)
- Inventory Value % GPI [defined_in:: Esso] MRO optimization 1978-1980, data every 6 months for 3 years (SPO p.143-145)
- Inventory Value % GPI [has_value:: 2% / 4% / 10%] spare parts, Europe-USA-Japan / average area / overseas (SPO p.114)
- Inventory Value % GPI [has_value:: 1% / 3% / 8%] other MRO, same areas (SPO p.114)
- Inventory Value % GPI [has_value:: max 4%] all MRO, capital-intensive plant (SPO p.115)
- Inventory Value % GPI [has_value:: max 1.5%] labour-intensive plant (SPO p.115)
- Inventory Value % GPI [has_value:: 2-4%] East Asia branches of a US company, incl. chemicals and general supplies (SPO p.128-129)
- Inventory Value % GPI [has_value:: 5-10%] rotating or continuous wear spares, base unclear (SPO p.128-129) [confidence:: low]
- Inventory Value % GPI [has_value:: 1% or less] general repair materials (SPO p.128-129)
- Inventory Value % GPI [has_value:: max 3%] warehouse policy of a heavy-industry plant (SPO p.55-57)
- Inventory Value % GPI [has_value:: 3-4%] suggestion for Thai machinery plants (SPO p.143-145)
- Inventory Value % GPI [has_value:: 1-1.5%] suggestion for simple-machine plants (SPO p.143-145)
- Inventory Value % GPI [has_value:: 3.98%] December example derived 49.8/1250; book prints 3.58 (SPO p.126)
- Inventory Value % GPI [related_to:: B7 Spare Part Inventory per Plant Asset] similar denominator; SPO 2-4% vs RBMM 1-3%; not a true conflict, different numerator scope and region
- B7 Spare Part Inventory per Plant Asset [has_value:: 1-3%] target of machine price (RBMM p.295, p.314)
- Inventory Turnover [related_to:: B8 Stock Turn Ratio] same concept, times per year vs percent; 40% = 0.4 turns = MOS 30 months, derived
- Inventory Turnover [differs_from:: Stock Turnover Rate] SPO uses average inventory, RBMM uses total store value (RBMM p.239)
- [[Inventory Turnover and GPI Benchmarks]] [related_to:: [[Maintenance KPIs]]]
- [[Inventory Turnover and GPI Benchmarks]] [related_to:: [[Spare Parts Management]]]
- [[Inventory Turnover and GPI Benchmarks]] [input_to:: [[MRO Inventory Reduction Program]]]

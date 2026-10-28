---
title: Asset Life Cycle
created: 2026-10-20
updated: 2026-10-28
type: concept
tags: [maintenance-management, criticality, spare-parts, cost, book, cmrp, mpm, lcc]
sources: [reliability-based-maintenance-management.md, cmrp.md, maintenance-profit-maker.md]
confidence: medium
contested: true
---

# Asset Life Cycle (วงจรชีวิตทรัพย์สินและกลุ่มงานบำรุงรักษา)

หน้านี้สรุปบทที่ 1 ของ RBMM (book p.13-30): วงจรชีวิตเครื่องจักรตั้งแต่ Feasibility ถึงปลดระวาง ความเชื่อมโยงระหว่างงานเทคนิค (MTTF, MDT, Availability, OEE) กับงบการเงิน การจำแนกงานบำรุงรักษาเป็น 4 กลุ่ม พลวัตของ criticality (A/B/C) เป้าหมาย "Zero Plant Breakdown @ Minimum Cost" และผลของ redundancy ต่อ criticality ข้อความและตัวเลขมาจากบันทึกอ่านหนังสือ (paraphrase) ส่วนที่ระบุว่า "อ่านจากรูป" อาจคลาดเคลื่อน

## 1. ขั้นตอนวงจรชีวิต (Fig 1.1, RBMM p.14)

| ช่วง | กิจกรรม | ประเด็นสำคัญ |
|---|---|---|
| 1 | Feasibility Study | ราคาถูก "ล็อก" ประมาณ 70% ในช่วงต้น |
| 2 | Project Stage | |
| 3 | Engineering Design | ล็อก 85% ถึง 95% ตามลำดับขั้น |
| 4 | EPC (Engineering, Procurement, Construction) | 100% เมื่อสิ้นสุดออกแบบ/จัดซื้อ |
| 5 | Commissioning / Trial Run | เปลี่ยนชิ้นส่วนเสียมากผิดปกติ ใช้ Commissioning Spare Part |
| 6-8 | Commercial Run: เสีย/ชำรุด, ปรับปรุง/ขยาย, ซ่อมใหญ่ | จบด้วยราคาซาก |

- ตัวเลข 70/85/95/100% อ่านจาก Fig 1.1 ตัวรูป (ตามบันทึก) ยืนยันกับหนังสือต้นฉบับก่อนใช้เชิงตัวเลข
- เปลี่ยน spec ช่วง 1-3 กระทบราคาน้อย แต่ change-order หลังสั่งซื้อกระทบมาก (RBMM p.14)
- หลัง Commissioning ต้นทุนทั้งหมดโอนเข้าบัญชีสินทรัพย์และเริ่มคิด Depreciation (RBMM p.15)
- ผู้ซื้อควรถามตั้งแต่ต้นว่า โรงงานมีโอกาสเดินต่อเนื่องไม่มี breakdown จนถึง Major Overhaul/Turnaround ครั้งถัดไปกี่ % (RBMM p.16) นำไปสู่ Zero Plant Breakdown

### แหล่งที่สอง: MPM รูป 1.1 / 2.1 / 13.1 และข้อขัดแย้ง MPM-C2 (เพิ่ม 2026-10-28)

[[Maintenance Profit Maker Book]] (ผู้แต่ง 2 ใน 3 คนเดียวกับ RBMM) ใช้รูปวงจรชีวิตเดียวกันซ้ำ 3 ครั้ง (รูป 1.1 MPM p.14, รูป 2.1 MPM p.38, รูป 13.1 MPM p.244) ลำดับ Feasibility -> Project -> Engineering -> EPC -> Commissioning -> warranty -> ช่วงผลิตและซ่อมบำรุง (เสีย/ชำรุด, ซ่อมใหญ่, โครงการขยาย/ปรับปรุง) -> ราคาซาก พร้อมป้าย 70/85/95/100% จึงยืนยัน Fig 1.1 ของ RBMM เป็นแหล่งที่สอง (ป้ายในรูปอ่านจาก OCR ไม่ครบทุกจุด)

**ข้อขัดแย้ง MPM-C2 (% ต้นทุนที่ถูกล็อกตั้งแต่ engineering/design):** ข้อความของ MPM ไม่ตรงกับป้ายในรูปของตัวเองและไม่ตรงกับ RBMM ยังไม่ resolve

| มุมมอง | Feasibility | Project | Engineering | EPC / Commissioning |
|---|---|---|---|---|
| RBMM Fig 1.1 (RBMM p.14) | ประมาณ 70% | - | 85% ถึง 95% | 100% |
| MPM ข้อความ p.39 | 70% | 80% | 90% | ใกล้ 100% |
| MPM ข้อความ p.14 | - | - | 80% ("ถึงจุดนี้กำหนดราคาได้แล้ว") | - |

- ป้ายในรูป MPM 1.1 / 2.1 / 13.1 คือ 70 / 85 / 95 / 100% เหมือน RBMM (ตำแหน่งที่ผูกกับแต่ละช่วงอ่านจาก OCR ได้ไม่ชัด) ขัดกับข้อความ p.39 และ p.14 ของเล่มเดียวกัน
- ทุกมุมมองเห็นตรงกันว่าต้นทุนส่วนใหญ่ถูกกำหนดก่อนก่อสร้าง ต่างกันที่ตัวเลขของช่วง Project/Engineering ใช้เป็นแนวโน้ม ไม่ใช่ค่าแม่นยำ
- เนื้อหา LCC 3 ช่วงของ MPM อยู่ที่ [[Life Cycle Cost and Life Cycle Profit]]

## 2. อะไหล่ 2 ประเภทหลัง Commissioning (RBMM p.15-16)

| ประเภท | วัตถุประสงค์ | บัญชี | หมายเหตุ |
|---|---|---|---|
| Commissioning Spare Part | แก้ปัญหาจากก่อสร้าง/ติดตั้ง/ตรวจรับ (Forced Deterioration = เสียเพราะคน ไม่ใช่ตามอายุ) | ไม่ควรปนกับ stock ปกติ | อาจไม่ถูกใช้เลยในช่วงปกติ ผู้รับเหมามักโอนเป็นอะไหล่สำรองคลังอย่างไม่ถูกต้อง |
| Maintenance Spare Part | สำรองคลังไว้ใช้ตลอดอายุปกติ | Current Asset ไม่คิดค่าเสื่อม | holding cost รวมราว 15-20% ของราคาอะไหล่ (RBMM p.16) |

Long Term Asset (ตัวโรงงาน) ตัดค่าเสื่อมรายปีอัตราคงที่ เช่น 15-20-25 ปี (RBMM p.15) เครื่องจักรต้องมีอายุใช้งานตลอดช่วงตัดค่าเสื่อม ซึ่งหนังสือระบุว่าเป็นหน้าที่ของบำรุงรักษา (RBMM p.18)

**ข้อขัดแย้ง MPM-C7 (อายุตัดค่าเสื่อม):** MPM ระบุว่าสินทรัพย์ถาวรทั่วไปตัดเป็นค่าใช้จ่ายได้ **10-20 ปีตามกฎหมาย** (MPM p.256) ขณะที่ RBMM ให้ 15-20-25 ปี (RBMM p.15) ผู้แต่งชุดเดียวกันให้ช่วงต่างกัน น่าจะเป็นค่าตัวอย่างทั้งคู่ (MPM ยังเขียนการตัดค่าเสื่อมงานปรับปรุงเป็น 1/5, 1/10 หรือ 1/15 ต่อปี MPM p.22) ยังไม่ resolve; อายุจริงต้องยึดนโยบายบัญชีของบริษัท (ไม่มีใน sources) ส่วนการจัด Maintenance Spare Part เป็น Current Asset นั้น MPM ยืนยันตรงกัน (รูป 14.6, MPM p.262-263)

## 3. เส้นแดง: งานเทคนิคเชื่อมงบการเงิน (Fig 1.2, RBMM p.16-20)

```
MTTR + MWT          -> MDT
MTTF (Reliability)  + MDT -> Availability
Availability x Speed x Quality -> OEE
OEE + Planning Factor + Plant Capacity -> Production -> Goods (งบ)
Goods -> GOGS -> Contribution Margin -> Profit
```

- ใต้ MTTR: Tools, Methods, Maintenance Proficiency, Planning/Scheduling/Control; ใต้ MWT: Logistics/Support, Spare Part Stock Performance
- ฝั่งธุรกิจ: ค่าครอบครองเครื่อง = WACC + Depreciation; ปริมาณผลิตขึ้นกับ Capacity, Production Plan, OEE (RBMM p.19)
- ตัวเลขตัวอย่าง: สินค้าคงคลังอยู่ในคลังเฉลี่ย 20 วัน หมุนเวียน 365/20 ประมาณ 18 รอบ/ปี (derived จากตัวเลขหนังสือ RBMM p.20) ใช้สื่อว่าเครื่องหยุดได้ไม่เกินระยะนี้
- รายละเอียด Availability และ OEE ดู [[Availability and OEE]]

## 4. 4 กลุ่มงานบำรุงรักษา (Fig 1.3, RBMM p.21-23)

แกนตั้ง = ความวิกฤติ (L ไป H) แกนนอน = วงจรชีวิตของงาน ฐาน = Maintenance Management System (ช่องในรูปบางช่องเบลอ [อ่านไม่ออกบางส่วน])

| กลุ่ม | ชื่อ | ตัวอย่างงาน |
|---|---|---|
| 1 | Fault Recovery (เครื่องเรียกหาเรา) | Trouble Shooting, Component Change, Component Rebuild, Spare Parts |
| 2 | Proactive (เราเข้าหาเครื่อง) | Predictive, Condition Monitoring, Preventive Maintenance, Turnaround |
| 3 | Improvement / Project | Project Management, Commissioning, Installation, Engineering, Modification |
| 4 | Maintenance Engineering | Audits, Reliability Improvement, Performance Improvement, Management Improvement |

ประเภทงานตามการวางแผน (RBMM p.22): Corrective Unplanned, Planned Part Replacement/Overhaul, Planned Condition Monitoring (อาการเปิดเผย), Planned Failure Finding Inspection (อาการซ่อนเร้น), Corrective Planned (CM-Planned) เป้าหมายรวม คือลดงานกลุ่ม 1 (unplanned) ไปเป็น planned โดยมี CMMS เป็น "แม่บ้าน" วางแผน จัดตาราง เก็บประวัติ และออกรายงาน (RBMM p.23)

## 5. พลวัตของ Criticality (Fig 1.4, RBMM p.23-25)

Criticality เปลี่ยนตาม Stress, Resistance และแผนบำรุงรักษา Fig 1.4 แบ่งเครื่องเป็น A/B/C ที่ 30% / 50% / 20% ของจำนวนเครื่อง และแสดง 3 สถานะ

| สถานะ | ลักษณะการเสีย |
|---|---|
| 1 Beginning | เสียกระจายทุกระดับ รวมกลุ่ม A โอกาสรอดถึง Turnaround ถัดไปน้อย |
| 2 Intermediate improving | เสียส่วนใหญ่ลงมาที่ B/C ไม่มี A เสีย |
| 3 Target | เสียเฉพาะ C/B ที่ไม่กระทบหยุดโรงงาน = Zero Plant Down Time |

ค่าใช้จ่ายต่ำสุดขึ้นกับยุทธศาสตร์เชิงรุก เช่น RCM, RBI (Risk Based Inspection), Condition Monitoring PM และการตั้งงบ ดู [[Criticality Assessment]] และ [[RCM Reliability Centered Maintenance]]

- **หมายเหตุชื่อ RBI**: MPM p.248 เขียน "Risk Base Inspection" ตรงกับหน้านี้ แต่ MPM p.252 เขียน "Reliability Based Inspection (RBI)" ซึ่งเป็นความคลาดเคลื่อนของหนังสือ ชื่อที่ถูกคือ **Risk-Based Inspection** (API 580/581, ความรู้ทั่วไป) MPM เพิ่มว่า RBI ได้ผลเมื่อมีกฎหมายรองรับการลดความถี่/เวลาหยุด และใช้กับ stationary equipment (ท่อ, ภาชนะความดัน, pipe hanger, heater, heat exchanger) (MPM p.248)
- MPM รูป 13.4 แสดงพลวัตเดียวกันด้วยการแบ่ง 30/50/20% (MPM p.247) รายละเอียดที่ [[Criticality Assessment]]

## 6. Zero (Plant) Breakdown @ Minimum Cost (Fig 1.5, RBMM p.25-27)

ต้องตั้งคำถามแบบมีกรอบเวลา เช่น เครื่องมีโอกาสรอดถึง Major Overhaul ถัดไปกี่ % และผูกกับต้นทุนเสมอ

| ระดับ | แนวทาง | Scheduled PM | Spare Parts |
|---|---|---|---|
| High | 100% RCM Tasks | RCM 100% ตัด unreliable incidence, failure-finding เข้ม | service level 100% stock out 0% |
| Medium | Pro-active | ตัด PM ที่ไม่ได้ผลด้วย RCM, optimal PM, RTF | ลด stock, ระบุ % service level |
| Low | Re-active | ตัด PM ที่ไม่จำเป็น, optimal PM, RTF | ลด stock, ระบุ % service level |

- ตัวเลข 50% (Medium) และ 20% (Low) เป็นสมมติฐานของหนังสือ (RBMM p.27)
- Zero Breakdown ต้องครอบคลุมตั้งแต่ Design ถึง Operator และ Maintenance = TPM (RBMM p.27)
- Medium: หาจุดต้นทุนรวม (planned + unplanned) ต่ำสุดโดยเลือก PM ให้ตรง failure mode และปรับความถี่ (ดู [[PM Interval Optimization]])

## 7. Redundancy ลด criticality ได้แค่ไหน (Fig 1.6-1.8, RBMM p.28-30)

- Fig 1.6 ไม่มี redundancy: เครื่องอนุกรมทุกตัวเป็น criticality A
- Fig 1.7 redundancy ระดับ equipment: กลุ่มขนานอาจเป็น A/B/C
- ตัวอย่างสมมติแต่ละเครื่องรับ 50% ของภาระ มี 3 เครื่อง: Standby (ใช้ 2 สำรอง 1) หรือ Load Sharing (แต่ละเครื่อง 1/3 รับเพิ่มได้ถึง 50%)
- Standby อาจมี Hidden Failure จึงเกิด Multiple Failure ได้ ความวิกฤติไม่ต่ำลงอัตโนมัติ ส่วน Load Sharing ลดลงได้ตามความสามารถรับภาระ (RBMM p.29)
- Fig 1.8 ถังเก็บคั่นระหว่าง process ลด criticality ภาพรวม ขึ้นกับปริมาณและเวลาที่ป้อนต่อได้ (RBMM p.30)
- แนวปฏิบัติ: Condition Monitoring ทั้งเครื่องใช้งานและ standby, ทดสอบ hidden failure เป็นระยะ ดู [[Failure Finding Interval]] และ [[Redundancy and Standby Systems]]

## 8. วงจรบริหารทรัพย์สิน (RBMM p.30)

Think (เป้าหมาย/ยุทธศาสตร์) แล้ว Plan & Act (บริหารงาน) แล้ว Reporting & Control (วัดผลและรายงานรวมเงิน) ฝั่งเทคนิคใช้สถิติเลือกงาน คำนวณคาบ PM และระดับสต็อก ฝั่งบริหารตั้งงบตามเป้าบริษัท

## 9. มุมมอง CMRP: Life Cycle Cost และ economic optimum (เพิ่ม 2026-10-25)

สไลด์ [[CMRP Course]] เสริมด้านต้นทุนตลอดอายุ ซึ่งบทที่ 1 ของ RBMM ไม่ได้แจกแจง

### Asset lifecycle (CMRP CMPR-02 p.34)
เมื่ออายุ/การใช้งานเพิ่ม condition ลดลง ค่าบำรุงรักษาประจำเพิ่มขึ้น มี mid-life overhaul และสุดท้ายคือ renewal การตัดสินใจต้องชั่ง risk, condition และ cost ร่วมกัน

### Life Cycle Cost 5 กลุ่ม (CMRP CMPR-02 p.35)

| กลุ่ม | ตัวอย่างรายการ |
|---|---|
| Capital | design, purchase, installation, commissioning, training, documentation, facilities |
| Operational | labor, energy, water, raw materials, feedstock |
| Maintenance | labor, materials, spares, workshop, contractors, overhead |
| Production and quality losses | non-availability, malfunction |
| Disposal | cost of disposal ลบ residual value |

เทียบ RBMM: Commissioning Spare Part อยู่ในกลุ่ม Capital ส่วน Maintenance Spare Part และ holding cost อยู่ในกลุ่ม Maintenance ราคาซากในช่วง 6-8 ของหัวข้อ 1 ตรงกับ residual value ของกลุ่ม Disposal (การจับคู่เป็นการตีความของ wiki)

### Economic optimum ของคาบบำรุงรักษา (CMRP CMPR-02 p.35)
- direct cost ลดลงเมื่อเว้นคาบห่างขึ้น ส่วน risk cost เพิ่มขึ้น total business impact เป็นเส้นโค้งที่มีจุดต่ำสุด = "economic optimum" (ในกราฟตัวอย่างราว 4 สัปดาห์)
- ซ้ายของจุดนี้ = จ่ายเกินเพื่อเป้า reliability; ขวา = จ่ายเกินเพื่อเป้าต้นทุน
- แกน x ของกราฟเขียนว่า "frequency (weeks)" แต่ความหมายจริงคือ interval (ข้อผิดพลาดของป้ายแกน)
- หลักเดียวกับจุดต้นทุนรวม planned + unplanned ต่ำสุดของ criticality Medium ในหัวข้อ 6 ดู [[PM Interval Optimization]]

### "~70% ของต้นทุน M&R ถูกกำหนดตั้งแต่ design" (CMRP CMPR-01 p.29)
- กราฟประกอบ P-F curve ในสไลด์ระบุว่าประมาณ 70% ของต้นทุน maintenance and repair (M&R) ถูกกำหนดตั้งแต่ช่วง design; ยิ่งใกล้จุด F ต้นทุนและ OEE losses ยิ่งสูง ดู [[P-F Interval and Condition Monitoring]]
- **อย่ารวมกับตัวเลข 70% ของ RBMM** (หัวข้อ 1): RBMM วัด "ราคา/ต้นทุนการลงทุนที่ถูกล็อก" ในช่วง Feasibility Study (อ่านจาก Fig 1.1) ส่วน CMRP วัด "ต้นทุน M&R ตลอดอายุที่ถูกกำหนดโดยการออกแบบ" คนละฐาน คนละช่วงเวลา ตัวเลขเท่ากันโดยบังเอิญ จึงไม่ใช่การยืนยันกันและไม่ใช่ข้อขัดแย้ง ทั้งสองแหล่งไม่ได้อ้างที่มาของ 70%

## 10. มุมมอง MPM: Physical Asset Management (เพิ่ม 2026-10-28)

[[Maintenance Profit Maker Book]] บทที่ 13 สรุปงานบำรุงรักษาทั้งเล่มเป็นภาพเดียว: Physical Asset Management คือทำให้ทรัพย์สินที่ครอบครอง "ทำงานคุ้มค่า" เต็มศักยภาพ แบบองค์รวม (เทคนิค + การจัดการ) โดยพิจารณาค่าครอบครอง ค่าบำรุงรักษา และคุณค่าที่คาดหวัง (MPM p.244, p.252)

### 3 ช่วงของทรัพย์สินในงบดุล (MPM p.244-245)

| ช่วง | สถานะในงบดุล | ประเด็น |
|---|---|---|
| 1. Acquisition | กำลังจะเข้างบดุล | สำคัญมาก เพราะเป็นการ implement กลยุทธ์ธุรกิจและกำหนดกิจกรรมที่ตามมาทั้งหมด ต้องใช้ข้อมูลในอดีตกำหนด spec |
| 2. ช่วงใช้งาน | เป็นทรัพย์สินในงบดุล มีค่าใช้จ่ายและรายได้ | เป้าคือผลผลิตสูงสุดเท่าที่เครื่องทำได้ ปรับปรุงตามจำเป็น |
| 3. Disposal | ออกจากงบดุล | อาจมีรายได้ขายซากหรือค่ากำจัด |

ตรงกับ 3 ช่วงค่าใช้จ่ายของ LCC ใน [[Life Cycle Cost and Life Cycle Profit]]

### กรอบ Strategy -> Plan -> Implement ของช่วงใช้งาน (MPM p.245-251)

1. **Strategy**: เป้าหมาย = ลดผลกระทบของการชำรุดต่อธุรกิจ; หลักคิด 5 ข้อ: ปรัชญาการบริหาร, ธรรมชาติของกระบวนการ/เครื่องจักร, เงื่อนไขตลาด/ที่มารายได้, ความสำคัญด้านคุณภาพสินค้า, ความสำคัญด้านความปลอดภัย (MPM p.245-246)
2. **Plan (แยกกลุ่มตามความวิกฤติ)**: ขึ้นทะเบียนทรัพย์สินใน [[CMMS]] -> วิเคราะห์ความวิกฤติ 7 เกณฑ์ -> จัดอันดับ (ทบทวนสม่ำเสมอ) -> แบ่ง 30/50/20% แล้วเลือกกลยุทธ์และ service level อะไหล่ต่อกลุ่ม (รูป 13.2, MPM p.245-250) รายละเอียดที่ [[Criticality Assessment]]
3. **Implement**: ให้ทุกฝ่ายมีส่วนร่วมผ่าน 3 แนวทาง TPM (เพิ่ม OEE), คุณภาพ (รวมความปลอดภัยและสิ่งแวดล้อม) และการปฏิบัติการผลิต (เทียบเงื่อนไขออกแบบกับที่ทำได้จริง); ทุกระดับเลือก outsource ได้; มี focused team, benchmarking และ 5ส กำกับ (รูป 13.8, MPM p.250-251) ดู [[TPM and Lean Maintenance]] และ [[Availability and OEE]]

- ผลลัพธ์ปลายทางในรูป 13.2: Improved Reliability / Availability / Maintainability
- ผู้เขียนมองว่า Reliability Engineering / RCM จะเป็นบรรทัดฐานในอนาคตอันใกล้ แต่ได้ผลเมื่อมีประวัติชำรุด/ซ่อมสมบูรณ์ต่อเนื่องและโมเดลค่าใช้จ่ายของบริษัทที่ถูกต้อง (MPM p.252)
- เทียบวงจร Think -> Plan & Act -> Reporting & Control ของ RBMM ในหัวข้อ 8: โครงคล้ายกัน แต่ MPM ไม่มีขั้น Reporting & Control แยก (การเทียบเป็นการตีความของ wiki)

## เชื่อมโยงกับ compressor failure hierarchy

- บทนี้ไม่ได้อ้าง [[OREDA]] หรือ [[ISO 14224]] และไม่มีเนื้อหา compressor โดยตรง
- หนังสือใช้ "Failure Mode (Cause)" คู่กัน (RBMM p.23, 27) ไม่ได้แยก [[Failure Mechanism]] แบบ ISO 14224 เมื่อเลือก PM ต่อ [[Failure Mode]] ของ [[Compressor]] ควรแมป mode ไปยัง mechanism และ cause ก่อน (ดู [[Failure Cause Codes]])
- Hidden Failure/Multiple Failure ของเครื่อง standby (เช่น compressor สำรองใน train) เทียบได้กับ failure mode ประเภท fail to start (FTS) ที่ตรวจพบเมื่อสั่งใช้งาน
- ระดับ criticality A/B/C ช่วยจัดลำดับว่า [[Maintainable Item]] ใดควรทำ RCM 100% (ตัวเลข % failure rate ของ OREDA ไม่ใช่ criticality ในตัวเอง ต้องคูณ consequence)

## ดูเพิ่ม

- [[Maintenance Efficacy Pyramid]]
- [[Maintenance KPIs]]
- [[Availability and OEE]]
- [[Maintenance Strategic Report]]
- [[Failure Hierarchy]]
- [[PM Interval Optimization]]
- [[CMRP Course]]
- [[Life Cycle Cost and Life Cycle Profit]]
- [[Engineering Economics and Time Value of Money]]
- [[Maintenance Profit Maker Book]]

## Triplets

- Feasibility Study [step_of:: [[Asset Life Cycle]]] stage 1 (Fig 1.1, RBMM p.14)
- Project Stage [step_of:: [[Asset Life Cycle]]] stage 2 (Fig 1.1)
- Engineering Design [step_of:: [[Asset Life Cycle]]] stage 3 (Fig 1.1)
- EPC [step_of:: [[Asset Life Cycle]]] stage 4, Engineering Procurement Construction (Fig 1.1)
- Commissioning [step_of:: [[Asset Life Cycle]]] stage 5, trial run, abnormal part replacement (Fig 1.1)
- Commercial Run [step_of:: [[Asset Life Cycle]]] stages 6-8: failures, improvement/expansion, major repair; ends with salvage value (Fig 1.1)
- Feasibility Study [has_value:: about 70%] of cost locked early; read from Fig 1.1, verify [confidence:: low]
- Engineering Design [has_value:: 85% to 95%] of cost locked by sub-stage; read from Fig 1.1 [confidence:: low]
- EPC [has_value:: 100%] of cost locked at end of design/procurement; read from Fig 1.1 [confidence:: low]
- Depreciation [depends_on:: Commissioning] all costs move to asset account after commissioning (RBMM p.15)
- Commissioning Spare Part [is_a:: Spare Part] (RBMM p.15-16)
- Maintenance Spare Part [is_a:: Spare Part] (RBMM p.15-16)
- Commissioning Spare Part [differs_from:: Maintenance Spare Part] should not mix with normal stock; contractors often transfer wrongly (RBMM p.15-16)
- Commissioning Spare Part [applies_to:: Forced Deterioration] failure caused by people during construction/installation, not age (RBMM p.15-16)
- Maintenance Spare Part [has_category:: Current Asset] not depreciated (RBMM p.15-16)
- Holding Cost [has_value:: 15-20%] of spare part price (RBMM p.16)
- Long Term Asset [has_value:: 15-20-25 years] straight-line annual depreciation (RBMM p.15)
- MDT [has_formula:: MTTR + MWT] (Fig 1.2, RBMM p.16-20)
- Availability [depends_on:: MTTF] with MDT (Fig 1.2)
- Availability [depends_on:: MDT] (Fig 1.2)
- OEE [has_formula:: Availability x Speed x Quality] (Fig 1.2)
- Production [depends_on:: OEE] also Planning Factor and Plant Capacity (Fig 1.2)
- Profit [depends_on:: Contribution Margin] Goods to GOGS to Contribution Margin to Profit (Fig 1.2)
- MTTR [depends_on:: Maintenance Proficiency] also Tools, Methods, Planning/Scheduling/Control (Fig 1.2)
- MWT [depends_on:: Spare Part Stock Performance] also Logistics/Support (Fig 1.2)
- Machine Ownership Cost [has_formula:: WACC + Depreciation] (RBMM p.19)
- Inventory Turnover [has_value:: about 18 per year] 365/20 with 20 days average in store, derived (RBMM p.20)
- Fault Recovery [is_a:: Maintenance Work Group] group 1, machine calls us: Trouble Shooting, Component Change/Rebuild, Spare Parts (Fig 1.3, RBMM p.21-23)
- Proactive [is_a:: Maintenance Work Group] group 2, we go to machine: Predictive, Condition Monitoring, PM, Turnaround (Fig 1.3)
- Improvement and Project [is_a:: Maintenance Work Group] group 3: Project Management, Commissioning, Installation, Engineering, Modification (Fig 1.3)
- Maintenance Engineering [is_a:: Maintenance Work Group] group 4: Audits, Reliability/Performance/Management Improvement (Fig 1.3)
- Condition Monitoring [part_of:: Proactive] (Fig 1.3)
- Planned Condition Monitoring [applies_to:: Evident Failure] evident symptoms (RBMM p.22)
- Planned Failure Finding Inspection [applies_to:: Hidden Failure] hidden symptoms (RBMM p.22)
- [[CMMS]] [uses:: Maintenance History] housekeeper that plans, schedules, keeps history, reports; goal shifts group 1 unplanned to planned (RBMM p.23)
- Equipment Criticality [depends_on:: Stress] also Resistance and maintenance plan (Fig 1.4, RBMM p.23-25)
- Criticality A [has_value:: 30%] share of machines (Fig 1.4, RBMM p.23-25)
- Criticality B [has_value:: 50%] share of machines (Fig 1.4)
- Criticality C [has_value:: 20%] share of machines (Fig 1.4)
- Zero Plant Down Time [depends_on:: Criticality A] target state: failures only at C/B that do not stop plant; beginning state fails at all levels (Fig 1.4)
- Zero Breakdown [depends_on:: TPM] covers design to operator and maintenance (RBMM p.27)
- Criticality A [uses:: 100% RCM Tasks] High; failure finding intensive; service level 100%, stock out 0% (Fig 1.5, RBMM p.25-27)
- Criticality B [uses:: Pro-active] Medium; remove ineffective PM with RCM, optimal PM, RTF (Fig 1.5)
- Criticality C [uses:: Re-active] Low; remove unnecessary PM, optimal PM, RTF (Fig 1.5)
- Criticality B [depends_on:: [[PM Interval Optimization]]] Medium finds minimum total planned+unplanned cost
- Series Equipment [has_category:: Criticality A] no redundancy (Fig 1.6, RBMM p.28-30)
- Standby Equipment [depends_on:: Hidden Failure] may cause Multiple Failure, criticality not lowered automatically (RBMM p.29)
- Load Sharing [differs_from:: Standby] load sharing criticality can drop with load capacity (RBMM p.29)
- Buffer Tank [related_to:: Equipment Criticality] lowers overall criticality depending on volume and feed time (Fig 1.8, RBMM p.30)
- Think [step_of:: Asset Management Cycle] goals/strategy (RBMM p.30)
- Plan and Act [step_of:: Asset Management Cycle] manage work (RBMM p.30)
- Reporting and Control [step_of:: Asset Management Cycle] measure and report with money (RBMM p.30)
- Standby Compressor [has_failure_mode:: FTS] hidden/multiple failure of standby detected on demand, interpretation [confidence:: low]
- Asset Condition [depends_on:: Asset Age] condition falls, routine maintenance cost rises, mid-life overhaul then renewal (CMRP CMPR-02 p.34)
- Life Cycle Cost [has_part:: Capital Cost] design, purchase, installation, commissioning, training, documentation, facilities (CMRP CMPR-02 p.35)
- Life Cycle Cost [has_part:: Operational Cost] labor, energy, water, raw materials, feedstock (CMRP CMPR-02 p.35)
- Life Cycle Cost [has_part:: Maintenance Cost] labor, materials, spares, workshop, contractors, overhead (CMRP CMPR-02 p.35)
- Life Cycle Cost [has_part:: Production and Quality Losses] non-availability, malfunction (CMRP CMPR-02 p.35)
- Life Cycle Cost [has_part:: Disposal Cost] cost of disposal minus residual value (CMRP CMPR-02 p.35)
- Economic Optimum Interval [depends_on:: Risk Cost] total business impact = direct cost + risk cost, minimum about 4 weeks in example (CMRP CMPR-02 p.35)
- Economic Optimum Interval [related_to:: [[PM Interval Optimization]]] same minimum total cost principle
- M&R Cost Fixed at Design [has_value:: about 70%] of maintenance and repair cost determined at design (CMRP CMPR-01 p.29)
- M&R Cost Fixed at Design [differs_from:: Feasibility Study] RBMM 70% is investment cost locked at feasibility; different measure, do not merge
- [[Asset Life Cycle]] [defined_in:: [[Maintenance Profit Maker Book]]] same life cycle figure reused (MPM Fig 1.1 p.14, Fig 2.1 p.38, Fig 13.1 p.244)
- MPM Life Cycle Figure Labels [has_value:: 70/85/95/100%] confirms RBMM Fig 1.1 labels (MPM p.14, p.244)
- MPM Text Cost Locked at Engineering [has_value:: 90%] Feasibility 70, Project 80, EPC near 100 (MPM p.39) [contested:: true]
- MPM Text Cost Locked at Engineering [contradicts:: RBMM Cost Locked at Engineering Design] MPM-C2; MPM p.14 says 80% [contested:: true]
- RBMM Cost Locked at Engineering Design [has_value:: 85% to 95%] (RBMM Fig 1.1 p.14) [contested:: true]
- RBMM Cost Locked at Engineering Design [contradicts:: MPM Text Cost Locked at Engineering] MPM-C2 [contested:: true]
- MPM Depreciation Life [has_value:: 10-20 years] by law (MPM p.256) [contested:: true]
- MPM Depreciation Life [contradicts:: RBMM Depreciation Life] MPM-C7 [contested:: true]
- RBMM Depreciation Life [has_value:: 15-20-25 years] (RBMM p.15) [contested:: true]
- RBMM Depreciation Life [contradicts:: MPM Depreciation Life] MPM-C7 [contested:: true]
- Maintenance Spare Part [has_category:: Current Asset] also MPM Fig 14.6 (MPM p.262-263)
- Risk-Based Inspection [alias_of:: RBI] MPM p.252 Reliability Based Inspection is a book error (MPM p.248, p.252)
- Risk-Based Inspection [applies_to:: Stationary Equipment] piping, pressure vessels, heaters, heat exchangers; needs legal backing (MPM p.248)
- Physical Asset Management [has_part:: Acquisition] asset entering balance sheet, implements business strategy (MPM p.244-245)
- Physical Asset Management [has_part:: Operation Phase] asset on balance sheet (MPM p.244-245)
- Physical Asset Management [has_part:: Disposal] asset leaves balance sheet, salvage revenue or disposal cost (MPM p.244-245)
- Strategy [step_of:: Physical Asset Management] goal reduce failure impact on business; 5 principles (MPM p.245-246)
- Plan [step_of:: Physical Asset Management] register, criticality, rank, 30/50/20 groups (MPM p.245-250)
- Implement [step_of:: Physical Asset Management] TPM, quality, production operation (MPM p.250-251)
- Implement [uses:: [[TPM and Lean Maintenance]]] raise OEE (MPM p.250-251)
- Physical Asset Management [produces:: Improved Reliability Availability Maintainability] (Fig 13.2, MPM p.245)
- Physical Asset Management [related_to:: Asset Management Cycle] similar to RBMM Think/Plan and Act/Reporting and Control, interpretation [confidence:: low]
- [[Asset Life Cycle]] [related_to:: [[Life Cycle Cost and Life Cycle Profit]]]

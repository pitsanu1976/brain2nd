---
title: Maintenance Master Plan
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [mpm, maintenance-management]
sources: [maintenance-profit-maker.md]
confidence: medium
contested: false
---

# Maintenance Master Plan (แผนแม่บทการบริหารงานบำรุงรักษา, MMMP)

แผนแม่บท (Maintenance Management Master Plan, MMMP) คือแนวคิดภาพรวมทั้งหมดของการบริหารงานบำรุงรักษา ใช้เป็นแนวทางวางกลยุทธ์และ "มองการณ์ไกล" ว่างานบำรุงรักษาควรมีหน้าตาอย่างไร ตามบทที่ 9 ของ [[Maintenance Profit Maker Book]] (MPM p.158-166) แผนแม่บทเป็นขั้นที่ 4 ของ [[Maintenance Performance Improvement]] ซึ่งประมวลผลจากผล audit ([[Maintenance Performance Audit]]), benchmark และการประเมินความคุ้มค่า (MPM p.207, p.227) เนื้อหาถอดความจาก reading notes [[raw/maintenance-profit-maker]]

คำว่า MMMP ปรากฏครั้งแรกในบทที่ 1: ต้องคิดกลยุทธ์ตั้งแต่ต้นว่าสัดส่วนกำลังคนแต่ละประเภทเป็นอย่างไร และงานใดจ้างภายนอกได้ เพราะถ้าวางกำลังคนเกินตั้งแต่ต้น เมื่อระบบดีขึ้นงานลดลง คนจะเหลือและค่าใช้จ่ายบุคลากรลดไม่ได้ (MPM p.33-34)

## 1. 16 แผนใน 2 กลุ่ม (รูป 9.1, MPM p.158)

| แผนแม่บทงานด้านเทคนิค (9) | แผนแม่บทงานระบบจัดการ (7) |
|---|---|
| 1. เทคนิคการซ่อมบำรุง (Maintenance Technology) | 10. ความร่วมมือผลิตและซ่อมบำรุง |
| 2. งานอะไหล่ (Spare Part Inventory) | 11. งานบุคคล (Human Resource) |
| 3. มาตรฐาน (Standardization) | 12. ระบบบัญชี (Accounting) |
| 4. ความปลอดภัยและสภาพแวดล้อม (H&E) | 13. ระบบประเมินสมรรถนะ (Performance Measuring) |
| 5. งานจ้างเหมา (Outsource) | 14. บริหารงบประมาณ (Budgeting & Control) |
| 6. นโยบายการเปลี่ยนเครื่องจักร (Investment and Renewal Policy) | 15. ระบบข้อมูล (Management Information System) |
| 7. งานคุณภาพ (Quality) + TPM | 16. ผังองค์กร (Organization Structure) |
| 8. งานเอกสารเทคนิค (Technical Documentation) | |
| 9. CMMS | |

(เลข 1-16 ใส่เพื่ออ้างอิงตาม reading notes หนังสือไม่ได้ใส่เลข) รายการเดียวกันซ้ำในรูป 12.14 ของกรณีศึกษา XYZ (MPM p.235)

- ด้านเทคนิคสำคัญพอๆ กับด้านบริหาร แต่ **คล่องตัวน้อยกว่า**: ตัดสินใจแล้วเปลี่ยนยาก เพราะผูกกับทรัพยากรที่อยู่ในงบดุล (MPM p.158)
- สองกลุ่มสัมพันธ์กันแบบ **ประเด็นนำ / ประเด็นตาม** (lead/follow) แล้วแต่กรณี (MPM p.158)

## 2. สาระของแต่ละแผน (MPM p.159-164)

### แผนด้านเทคนิค

- **Maintenance Technology**: กำหนด/ทบทวนแผนบำรุงรักษา 16 ประเภทใน 4 กลุ่ม (ดู [[Maintenance Business Models]]) หลีกเลี่ยงทั้ง over-maintenance และ insufficient maintenance ประเด็นรองคือทำเองหรือจ้างเหมา
- **Spare Part Inventory**: ค่าซ่อมบำรุง **มากกว่า 50%** มาจากอะไหล่ จึงทบทวนนโยบายเริ่มจากรายการวิกฤตลงมา (MPM p.159) ดู [[Spare Parts Management]]
- **Standardization**: ทำงานให้ทำซ้ำได้ และเลือกรายการที่ควรเป็นมาตรฐานเดียวทุกโรงงานเพื่อแลกเปลี่ยนกันได้ (อะไหล่ เครื่องจักร ความรู้) ดู [[Parts Interchangeability]]
- **H&E** และ **Quality + TPM**: สภาพแวดล้อมการทำงาน ความปลอดภัย 5ส TPM (คำอธิบายสองแผนซ้ำกันในเล่ม) ดู [[TPM and Lean Maintenance]]
- **Outsource**: แบ่งบทบาทหน่วยภายในกับผู้รับเหมา ตัดสินบน **คุณค่า** ตามการคุ้มทุน ใช้ทรัพยากรที่มีให้เต็มก่อน ต้องมีความสามารถบริหารสัญญา เป็น **ประเด็นตาม** ของ Maintenance Technology, Budgeting & Control และ Human Resource
- **Investment and Renewal Policy**: ประเด็นนำคือ ระบบเอกสารเทคนิคที่มีประวัติซ่อมตลอดอายุ, การวิเคราะห์รากเหง้าและผลกระทบของปัญหา (หนังสือใช้คำว่า Failure Mode Effect Cause Analysis ดู [[FMECA]] และ [[Root Cause Analysis]]), มาตรฐานติดตั้ง/ตรวจรับที่ส่งเอกสาร As Built เข้าระบบได้ในคราวเดียว และให้หน่วยบำรุงรักษาร่วมกำหนด spec เครื่อง (MPM p.160) ดู [[Asset Life Cycle]]
- **Technical Documentation**: ข้อมูลซ่อมและ spec ต้องพร้อม ถูกต้อง และ **กระทบยอดตรงกัน** ไม่ว่ามาจากระบบใด (CMMS เชื่อมบัญชี การเงิน ระบบควบคุมการผลิต)
- **CMMS**: CMMS จำนวนมากใช้ไม่เต็มที่เพราะเข้าใจผิดว่าเป็นโปรแกรมสำเร็จรูป ที่จริงซื้อ CMMS = ซื้อ **ระบบงาน** ความสำเร็จอยู่ที่การ implement: วางโครงสร้างข้อมูลเครื่องจักร/อะไหล่, กำหนดงานบำรุงรักษาทุกรายการ, โครงสร้างประวัติซ่อมเพื่อทำ Failure Root Cause Analysis/FMECA, เชื่อมระบบบัญชี บุคคล โครงการ, ต้องมี Planning Function, ผู้บริหารต้องใช้เอง; IT เป็นฝ่ายสนับสนุน ไม่ใช่หลักนำ (MPM p.160-161) ดู [[CMMS]]

### แผนด้านระบบจัดการ

- **ความร่วมมือผลิต-ซ่อมบำรุง**: ใช้ **OEE** เป็นดัชนีหลักร่วม แล้วจัดลำดับดัชนีย่อยที่ขึ้นกับสองฝ่าย เช่น Mean Wait Time (ขั้นตอนตัดแยกระบบและตรวจรับเครื่อง) และ Speed Loss (ลองเครื่อง อุ่นเครื่อง) (MPM p.161) ดู [[Availability and OEE]]
- **Human Resource**: เทียบความสามารถปัจจุบันกับอนาคตแล้วทำแผนพัฒนา มักเป็นประเด็นตาม ส่วนประเด็นนำของ HR คือ **การเติบโตในสายอาชีพ**
- **Accounting** (ประเด็นนำ เพราะ "วัดค่าใช้จ่ายไม่ได้ ก็ควบคุมไม่ได้"): นโยบายแยกรายจ่าย/ทรัพย์สินที่อนุรักษ์นิยม, พิจารณารายงานแบบศูนย์กำไร, ABC costing และ Over/Under Absorption, Accountability Reports, ระบบบำรุงรักษาต้องเชื่อมบัญชีและกระทบยอดได้ตัวเลขเดียวกัน (MPM p.162) ดู [[Maintenance Cost Structure]] และ [[Job Order Costing]]
- **Performance Measuring**: ดัชนีอ่านสถานการณ์ได้เร็วที่สุด ต้อง **ไม่ใช้ตัวเดียว** แต่ให้กระทบยืนยันกัน การเลือกขึ้นกับกลยุทธ์ธุรกิจ ดัชนีหลักในการสอบเทียบ = **ต้นทุนบำรุงรักษาต่อสินค้า 1 หน่วย** และบริษัทหลายโรงงานต้องใช้มาตรฐานการวัดเดียวกัน (MPM p.162-163) ดู [[Maintenance KPIs]]
- **Budgeting & Control**: ตั้งงบเชิงคุณค่า ไม่ใช่ "งบปีก่อนบวก %" ดูหัวข้อ 4
- **Management Information System**: ข้อมูลเทคนิคต้องเป็นเนื้อเดียวกับข้อมูลการเงิน รองรับดัชนีทุกชนิด CMMS เป็นประเด็นนำ
- **Organization Structure**: ผังต้องตอบยุทธศาสตร์ธุรกิจ ประเด็นหลักคือ **ความสามารถในการวางแผน** ต้องมีงานวางแผนชัดเจนที่ใดที่หนึ่งพร้อมระบบข้อมูล (MPM p.163-164) ดู [[Maintenance Planning and Scheduling]]

### ความสัมพันธ์ประเด็นนำ/ตามที่หนังสือระบุ (MPM p.159-164)

| แผน | เป็นประเด็นตามของ | เป็นประเด็นนำของ / ประเด็นนำภายใน |
|---|---|---|
| Outsource | Maintenance Technology, Budgeting & Control, Human Resource | - |
| Investment and Renewal Policy | - | เอกสารเทคนิค, วิเคราะห์รากเหง้า, As Built, ร่วมกำหนด spec |
| Human Resource | (มักเป็นประเด็นตาม เช่น ความรู้ต้องเป็นของเราเองหรือไม่) | การเติบโตในสายอาชีพ |
| Accounting | - | เป็นประเด็นนำโดยตัวเอง |
| Management Information System | Organization Structure | CMMS เป็นประเด็นนำ |
| Organization Structure | Business Strategy, Maintenance Technology, Human Resource, Performance Measuring | Management Information System |

รูป 9.2 (MPM p.164) แสดงว่าแผนแม่บทเป็นเหตุปัจจัยผลักดัน 4 หัวหลัก: Production, Maintenance Performance, Maintenance Cost และ Current Asset (บางคำย่อในรูปไม่มีคำอธิบาย)

## 3. กลยุทธ์บำรุงรักษาต้องตอบกลยุทธ์ธุรกิจ (รูป 9.3, MPM p.164-166)

กลยุทธ์ = การจัดน้ำหนักแผนแม่บท 16 รายการให้เหมาะกับธุรกิจ ปัจจัยภายนอกได้แก่ ตลาด ผู้ถือหุ้น กฎระเบียบ และเป้าธุรกิจรวม Sustainability ด้วย

| | Cost Leadership (ผู้นำราคา) | Product Differentiation (ผู้นำความเชื่อถือได้/แบรนด์) |
|---|---|---|
| ลักษณะสินค้า | ผลิตแล้ว **เก็บสต๊อกได้** ต้นทุนต่ำ OEE สูง | **เก็บไว้ขายไม่ได้** (ไฟฟ้า โทรศัพท์ การบิน ร้านอาหาร ขนส่ง) หรือราคาตามฤดูกาลที่หยุดแล้วกลับมาผลิตยาก |
| ดัชนีนำใน OEE | **Availability** | **Reliability** |
| ตัวขับ | **MTTR** (ซ่อมเร็ว) | **MTBF** (ไม่ค่อยเสีย) |
| เป้าปรับปรุงแผนแม่บท | ลด MWT (ความพร้อมอะไหล่ คน เครื่องมือ), วิธีแก้ปัญหา, TPM, Failure Root Cause Analysis | PM และงานเชิงรุก, Reliability Engineering, Root cause analysis, วิศวกรรมในงานปรับปรุง |

- ทั้งสองทาง ดัชนีหลักยังเป็น OEE
- **Availability สูงไม่ได้แปลว่า Reliability สูง**: เครื่องอาจเสียบ่อยแต่ซ่อมเร็ว จึงได้ A สูง (MPM p.166)
- รูป 12.10 ในบทที่ 12 ใช้ตารางเดียวกัน เพิ่มเป้า เช่น Cost Leadership: รักษากำลังผลิต ป้องกันของเสีย; Differentiation: ภาพลักษณ์ ความพึงพอใจลูกค้า (MPM p.228-229)
- ข้อสังเกต: p.166 จัด MWT เป็นเป้าของการลด MTTR ขณะที่บทที่ 8 นิยาม MTTR เป็นเวลาซ่อมล้วนและแยกเวลารอเป็น Mean Logistic Time ดู ข้อขัดแย้ง MPM-C4 ใน [[Maintenance Time Definitions]] และ hub

## 4. Budgeting & Control: จุดอ่อนอันดับต้น (MPM p.163, p.166)

- เป็น **จุดอ่อนอันดับต้นๆ** ของการพัฒนาสมรรถนะ เพราะต้องใช้ความรู้บัญชี/การเงินที่บุคลากรเทคนิคขาด
- การอบรมบัญชีให้คนเทคนิคต้องทำ **เป็นอันดับแรก** โดยเฉพาะผู้ที่จะขึ้นเป็นผู้นำ มิฉะนั้นบริษัทจะ "เสียช่างเก่งหนึ่งคน ได้ผู้จัดการที่บริหารไม่เป็นหนึ่งคน" (ถอดความ, MPM p.163)
- ไม่มีระบบงบ = บินโดยไม่มีเรดาร์ (ถอดความ, MPM p.166) ดู [[Maintenance Budget]]
- สอดคล้องกับ RBMM ที่ว่า "ตั้งงบไม่เป็น" เป็นโรคที่สำคัญและรักษายากที่สุด ([[Maintenance Efficacy Pyramid]] หัวข้อ 4) และผล audit รูป 11.1 ที่จุดอ่อนอยู่ที่การวัดผลและงบประมาณ ([[Maintenance Performance Audit]])

## 5. ความสัมพันธ์กับ 16 หัวข้อประเมิน

แผนแม่บท 16 แผนแทบตรง 1:1 กับ 16-Topic Assessment ของ RBMM (Fig 2.1) ต่างเพียง RBMM "Maintenance Policy" กับ MPM "Investment and Renewal Policy" (ตาม reading notes ch08-09) จึงใช้ผล radar ของ audit ชี้ได้ตรงว่าแผนใดควรทำก่อน ตารางจับคู่ด้านล่างเป็นการจับคู่ของ wiki (derived จากชื่อหัวข้อ):

| แผนแม่บท MPM | RBMM 16-Topic (Fig 2.1) | MPM audit 16 หัวข้อ (รูป 11.1) |
|---|---|---|
| Maintenance Technology | 10 Method and Technical Management | T3 ความสามารถทางเทคนิค |
| Spare Part Inventory | 13 Spare Part Management | T6 อะไหล่และคลัง |
| Standardization | 14 Standardization and Code of Conduct | T7 มาตรฐาน |
| H&E | 16 SH&E Management | T9 ความปลอดภัยและสภาพแวดล้อม |
| Outsource | 11 Outsourcing Management | T4 จ้างเหมา |
| Investment and Renewal Policy | 9 Maintenance Policy (ใกล้เคียงที่สุด) | ไม่มีตรง (T1 สภาพโรงงานใกล้ที่สุด) |
| Quality + TPM | 15 Quality Management | T8 คุณภาพ |
| Technical Documentation | 12 Technical Documentation | T5 ข้อมูลเทคนิค |
| CMMS | 5 Maintenance Management System | T2 ระบบบริหารงานบำรุงรักษา |
| ความร่วมมือผลิต-ซ่อมบำรุง | 1 Maintenance and Production Coordination | M1 |
| Human Resource | 8 Human Resource | M6 |
| Accounting | 2 Maintenance Cost Accounting | M2 |
| Performance Measuring | 4 Performance Measuring, Reporting and Control | M7 |
| Budgeting & Control | 3 Maintenance Performance Budgeting | M3 |
| Management Information System | 6 Management Information Systems | M4 |
| Organization Structure | 7 Organization | M5 |

(T = Technical, M = Management ตามลำดับใน [[Maintenance Performance Audit]] หัวข้อ 3)

## 6. ตัวอย่างการใช้: แผนโครงการ 3 ปีของ XYZ (รูป 12.15, MPM p.236)

กรณีศึกษา XYZ แปลงแผนแม่บทเป็น Gantt 12 ไตรมาส เช่น OEE/Asset Management (ทบทวน criticality, implement Reliability module และ FMECA, ตั้งเป้าร่วมผลิต-บำรุงรักษา), อะไหล่ (Spare Part Optimization, ทบทวน supply chain), CMMS (ปรับปริมาณงาน, ทบทวนรายงาน), MIS/Accounting (ตรวจการเชื่อมบัญชี-บำรุงรักษา, Full Cost Reporting), Performance Measuring, HR (เกณฑ์ประเมินความสามารถ, training), Outsource (คุณภาพงาน shutdown, ระบบสัญญา), Quality + TPM ดูการวินิจฉัยเต็มใน [[Maintenance Performance Improvement]]

## เชื่อมโยงกับ compressor failure hierarchy

(การตีความของ wiki)
- สำหรับ [[Compressor]] ที่ใช้ในการผลิตก๊าซ/ไฟฟ้า (สินค้าเก็บไม่ได้หรือมีสัญญาส่งต่อเนื่อง) กรอบ Product Differentiation ชี้ให้เน้น MTBF/Reliability ซึ่งต้องอาศัย failure record ตาม [[Failure Hierarchy]] และ [[OREDA]] เพื่อหา failure mode เด่นก่อนเลือกงานเชิงรุก
- แผน CMMS และ Technical Documentation คือที่ที่ taxonomy ของ [[ISO 14224]] ถูกนำไปใช้จริง (โครงสร้างข้อมูลเครื่องจักรและประวัติซ่อมเพื่อ RCA/FMECA)

## ดูเพิ่ม

- [[Maintenance Performance Improvement]]
- [[Maintenance Performance Audit]]
- [[Maintenance Efficacy Pyramid]]
- [[Maintenance Business Models]]
- [[Maintenance Budget]]
- [[Maintenance Profit Maker Book]]

ดูเพิ่ม (หน้าจาก MPM ingest 2026-10-28): [[Maintenance Outsourcing]]

## Triplets

- [[Maintenance Master Plan]] [alias_of:: MMMP] Maintenance Management Master Plan (MPM p.33-34)
- [[Maintenance Master Plan]] [defined_in:: [[Maintenance Profit Maker Book]]] chapter 9 (MPM p.158-166)
- [[Maintenance Master Plan]] [step_of:: [[Maintenance Performance Improvement]]] step 4 of 6 (MPM p.207, p.227)
- [[Maintenance Master Plan]] [has_value:: 16 plans] 9 technical + 7 management (Fig 9.1, MPM p.158)
- Technical Master Plans [part_of:: [[Maintenance Master Plan]]] Maintenance Technology, Spare Part Inventory, Standardization, H&E, Outsource, Renewal Policy, Quality + TPM, Technical Documentation, CMMS (MPM p.158)
- Management System Master Plans [part_of:: [[Maintenance Master Plan]]] production coordination, HR, Accounting, Performance Measuring, Budgeting and Control, MIS, Organization Structure (MPM p.158)
- Technical Master Plans [differs_from:: Management System Master Plans] less flexible, tied to balance-sheet resources (MPM p.158)
- Outsource Plan [depends_on:: Budgeting and Control Plan] follow issue; also of Maintenance Technology and HR (MPM p.159)
- Organization Structure Plan [depends_on:: Business Strategy] follow issue; also of Maintenance Technology, HR, Performance Measuring (MPM p.164)
- Management Information System Plan [depends_on:: Organization Structure Plan] organization is lead issue of MIS (MPM p.164)
- Management Information System Plan [depends_on:: [[CMMS]]] CMMS is lead issue (MPM p.163)
- Accounting Plan [has_category:: Lead Issue] cannot control what cannot be measured (MPM p.162)
- Investment and Renewal Policy [uses:: [[Root Cause Analysis]]] book calls it Failure Mode Effect Cause Analysis (MPM p.160)
- Spare Part Cost [has_value:: > 50%] of maintenance cost (MPM p.159)
- [[CMMS]] [is_a:: Work System] buying CMMS = buying a work system, success is implementation (MPM p.160-161)
- Performance Measuring Plan [uses:: Maintenance Cost per Unit] main benchmarking index (MPM p.163)
- Budgeting and Control Plan [has_category:: Top Weakness] technical staff lack accounting knowledge; train them first (MPM p.163, p.166)
- Cost Leadership [depends_on:: Availability] lead OEE index; driver MTTR; stockable products (Fig 9.3, MPM p.165)
- Product Differentiation [depends_on:: Reliability] lead OEE index; driver MTBF; non-stockable products (Fig 9.3, MPM p.165)
- Cost Leadership [uses:: [[Root Cause Analysis]]] reduce MWT, TPM, failure root cause analysis (Fig 9.3)
- Product Differentiation [uses:: [[Root Cause Analysis]]] with PM, proactive work, reliability engineering (Fig 9.3)
- Availability [differs_from:: Reliability] high A possible with frequent but quick repairs (MPM p.166)
- [[Maintenance Master Plan]] [maps_to:: 16-Topic Assessment] almost 1:1; RBMM Maintenance Policy vs MPM Investment and Renewal Policy (RBMM Fig 2.1)
- [[Maintenance Master Plan]] [related_to:: [[Maintenance Efficacy Pyramid]]]
- [[Maintenance Performance Audit]] [input_to:: [[Maintenance Master Plan]]] radar results show which plan to prioritise
- Production Maintenance Coordination Plan [uses:: OEE] common main index; sub-indices MWT and speed loss (MPM p.161)

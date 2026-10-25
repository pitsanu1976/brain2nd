# CMPR-04: Business case, Lean/TPM, RAM theory, maintainability และ reliability allocation

Source: PETROSYNC CMRP training course slides, file CMPR-04.pdf (scanned, OCR). Reading notes ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ PDF page `(CMRP CMPR-04 p.N)`

ขอบเขต: PDF p.1-47 (slide 157-203) ไฟล์นี้ไม่ได้เป็น business case ทั้งไฟล์ตามที่คาดไว้: p.1-5 เป็น business case, p.5-9 เป็น Lean/TPM/Six Sigma, p.10-47 เป็นทฤษฎี RAMS, availability, maintainability, การวิเคราะห์ PM/CM, RBD และ reliability allocation (ต่อใน CMPR-05) OCR ข้อความอ่านได้ดี สูตรและรูปเพี้ยน จึงเปิดภาพดู p.16, 23, 26, 28, 30, 31, 37, 44 ไม่มี handwriting ที่มีสาระ ไม่มีเนื้อหา NPV/ROI/payback หรือ life cycle cost แบบตัวเลข

## 1. ขั้นตอน business case (p.1-5)
ลำดับ 6 ขั้นที่ slide เสนอ (CMRP CMPR-04 p.1-5):
1. **Confirm the opportunity**: บรรยายสถานการณ์ปัจจุบันและโอกาส (project background, investment logic), เชื่อมกับ strategic objectives, ให้ sponsor อนุมัติก่อนไปต่อ
2. **Analyze/shortlist options**: ทำ long list ของทางเลือก ตั้งเกณฑ์ประเมิน เก็บข้อมูล แล้วคัดเหลือ 3-4 ทาง เสนอด้วย comparison matrix (ข้อดี/ข้อเสีย)
3. **Evaluate options** (p.2-3): ความสอดคล้องกับ strategy, quantify benefit ทั้งที่เป็นเงินและไม่เป็นเงิน (ROI, cost savings, revenue growth, operational efficiency), ทำ cash flow + **DCF analysis** แล้วตรวจว่าผ่าน **IRR ขั้นต่ำ / hurdle rate**, risk assessment + mitigation, scenario analysis และฟังความเห็น stakeholder
4. **Implementation strategy** (p.3-4): objectives/milestones, ทรัพยากรผูกกับ milestone, roles, ความเสี่ยง, cost breakdown ต่อ milestone, KPIs ของการ implement, communication plan และ change management
5. **Recommendation และ approval** (p.4-5): เตรียมคำตอบคำถามของผู้ตัดสินใจ ได้แก่ ความเสี่ยง, upside, **ต้นทุนของการไม่ลงทุน (cost of not proceeding)**, ความสอดคล้องกับ strategy; เปิดด้วย executive summary
6. **Follow-up**: ระบุ next steps ผู้รับผิดชอบ และสื่อสารต่อเนื่องตลอด lifecycle ของโครงการ

ข้อสังเกต: slide พูดถึง DCF/IRR/hurdle rate เป็นชื่อ ไม่ได้ให้สูตร NPV, ROI, payback หรือตัวอย่างตัวเลข

## 2. Lean, TPM, SMED, JITM, Six Sigma (p.5-9)
- **Lean** (p.5-6): ผลิตให้ได้มากที่สุดโดยลด waste; waste คือสิ่งที่ลูกค้าไม่ยอมจ่าย รูป p.5 แสดง waste 6 แบบ (processing, inventory, waiting, overproduction, motion, transportation) ไม่มี defects ซึ่งปกติเป็นหนึ่งใน 7 wastes (ความรู้ทั่วไป) องค์ประกอบ lean process: identify value, value stream mapping, create flow, pull system, Kaizen, quality management, employee involvement, visual management, technology/automation
- **TPM** (p.6): pillars ที่อ่านได้: Autonomous Maintenance, Focused Improvement, Quality Management, Early Equipment Maintenance, Office TPM, EHS (OCR อ่านฐานเป็น "6 'S'" ยืนยันไม่ได้ ปกติฐานคือ 5S); เป้า "zero" 4 ข้อ: accident, breakdown, small stops/changeover, defects
- **5S** (p.7): Sort, Set in Order, Shine, Standardize, Sustain (Seiri ถึง Shitsuke)
- **SMED** (p.7): ลดเวลา changeover รูปแสดง 7 stages
- **JITM** (p.8): ทำงานบำรุงรักษาเฉพาะเมื่อจำเป็น ใช้ predictive analytics/data-driven, ตัดงานที่ไม่จำเป็น; กลยุทธ์ 4 ด้าน: resource optimization, data-driven decision, dynamic scheduling, time precision
- **Six Sigma** (p.8-9): ลด defect/variation เป้า 3.4 DPMO; บทบาท belt (Master Black, Black, Green, Yellow); DMAIC ข้อสังเกต: รูป DMAIC p.9 เป็นตัวอย่างงาน digital marketing (website, campaign) ไม่ใช่งานบำรุงรักษา

## 3. Reliability analytics และ reliability program (p.10-11)
- เครื่องมือ (p.10): FMECA, RBD, reliability prediction, FTA, Weibull life data analysis, FRACAS, availability simulation, SPC/process capability
- องค์ประกอบ reliability program 7 ข้อ (p.11): ตั้งเป้า/ข้อกำหนด reliability จากลูกค้าและตลาด, ความคาดหวังที่สูงขึ้นตามเวลา, แปลงเป็น product design requirement ทุกระดับ, process design ผูก reliability กับ parameter การผลิต, post-production evaluation (สุ่มทดสอบ, feedback, warranty), training (slide เน้นว่าบางครั้งต้องทำก่อนเรื่องอื่น), validation/verification

## 4. RAMS และศัพท์พื้นฐาน (p.12-17)
- Reliability มี 4 องค์ประกอบ: probability, required function (ต้องกำหนดนิยาม failure เช่น pump ต่ำกว่า 20 gpm), stated conditions, specified period (อาจเป็นไมล์หรือ cycles) (p.12)
- Maintainability, Dependability (p.12-13): dependability รวม availability, reliability, maintainability, maintenance support performance; IEC TC 56 ดูแลมาตรฐาน; แยกเป็น attributes, threats, means
- MTBF (repairable), MTTF (non-repairable), MTTR, λ = 1/mean life, μ = 1/MTTR (p.13, 17) slide ระบุเองที่ p.14 ว่าความสัมพันธ์ λ = 1/MTBF ใช้เมื่อเป็น exponential (failure rate คงที่)
- ข้อมูล failure 4 แบบ (p.14): exact, right-censored (ยังไม่เสียเมื่อจบทดสอบ), left-censored (เสียก่อนตรวจครั้งแรก), interval-censored (เสียระหว่างการตรวจสองครั้ง เช่นทำงานที่ 145 h แต่พบเสียที่ 150 h)
- ตัวอย่าง (p.16): MTTF ของ 10 ชิ้น = 1538/10 = 153.8 h; MTBF = n·m/r = 100 x 1000 / 25 = 4,000 h
- **ข้อผิดใน slide**: p.15 เขียนว่า t ในสูตร MTTF คือ "failure rates" ที่ถูกคือ failure times; p.16 เศษในสมการแสดงตัวเลขแค่ 9 ตัว (ขาด 158 ผลรวมที่แสดง = 1380) แต่คำตอบ 153.8 ถูกต้องเมื่อรวมครบ 10 ตัว

## 5. Availability (p.17-23)
- นิยาม: สัดส่วนเวลาที่อยู่ในสภาพพร้อมใช้เมื่อถูกเรียกใช้ ณ เวลาสุ่ม; A = E[uptime] / (E[uptime] + E[downtime]); ถ้าไม่มี PM และซ่อมทันที A = MTBF/(MTBF+MTTR) (p.17, 20)
- A(t) = Pr[X(t)=1]; average availability บนช่วง [0,c] = (1/c)∫A(t)dt; limiting (steady-state) availability คือ limit เมื่อ c ไปอนันต์ (p.20)
- ระบบ high availability ระบุเช่น 99.98%, 99.999% (p.18)
- Trade-offs (p.18-19): ปรับ maintainability ช่วงออกแบบง่ายกว่าปรับ reliability และประมาณค่าได้แม่นกว่า แต่ความไม่แน่นอนของ reliability มักครอบงำ; maintenance ยก reliability ได้ไม่เกิน inherent reliability; ตัวอย่าง oil platform ยอมรับ cost of ownership สูงเพื่อ availability เพิ่มเล็กน้อย เพราะ revenue loss สูงกว่ามาก; แผนควรครอบคลุม RAMT (เพิ่ม testability)
- RBD/FTA ใช้คำนวณ availability โดยรวมปัจจัย เช่น redundancy, common cause, dormant failure, test coverage, spare stocking, logistics (p.21)
- ประเภท (p.21-23):

| ประเภท | สูตร | downtime ที่รวม |
|---|---|---|
| Inherent Ai | MTBF/(MTBF+MTTR) | corrective เท่านั้น (ideal support) |
| Achieved Aa | MTBMA/(MTBMA+MAMT) | active corrective + preventive ไม่รวม logistics/admin delay |
| Operational Ao | MTBM/(MTBM+MDT) | ทุกอย่าง รวม logistics, รออะไหล่, admin |

- MTBMA = 1/(λ + f_PM) เขียนใน slide เป็น "1/(λ/z)" อ่านไม่ชัด (p.23) MAMT รวมเวลาเฉลี่ย corrective และ PM ถ่วงด้วยความถี่
- **ไม่สอดคล้องเล็กน้อย**: p.21 นิยาม Ao ด้วย MTBF/(MTBF+MDT) แต่ p.23 ใช้ MTBM/(MTBM+MDT)
- องค์ประกอบ downtime (รูป p.22): run-down, preparation/delay, active repair, waiting/delay, start-up

## 6. Maintainability theory (p.24-30)
- Maintainability = ความง่ายและเร็วในการคืนสภาพหลัง failure; ขึ้นกับ design, ทักษะคน, procedure, test equipment, สภาพแวดล้อม (p.24)
- คู่เทียบ (p.25-26): f(t) คู่กับ g(t) (pdf ของ time to repair), R(t) คู่กับ M(t) = ∫0..t g, λ(t) คู่กับ repair rate μ(t) = g(t)/(1-M(t)), MTTF คู่กับ MTTR
- **ข้อผิดใน slide**: ตาราง p.26 แถว MTTR เขียน label เป็น "MTTF" และสูตร mean เขียนเป็น ∫f(t)dt / ∫g(t)dt ที่ถูกคือ ∫t·f(t)dt และ ∫t·g(t)dt
- ค่าสำคัญ 3 จุดบน M(t) (p.26): mean corrective time M̄ct = Σ(λi·Mcti)/Σλi (ถ่วงด้วย failure rate), median (50% ของงานเสร็จ), Mmax ct ที่ percentile กำหนด เช่น Mmax(95%) = 1 h แปลว่า 95% ของงานซ่อมต้องเสร็จใน 1 h
- Distribution ที่ใช้: normal, lognormal, exponential; lognormal ใช้มากที่สุดกับเวลาซ่อม เพราะงานซ่อมประกอบด้วยงานย่อยที่ความถี่/ระยะเวลาไม่เท่ากัน (p.27)
- Lognormal (p.27-29): t' = mean ของ ln(t), s = SD ของ ln(t) แล้ว MTTR = exp(t' + s²/2), median = exp(t'), Mmax = exp(t' + z·s); ค่า z: 0.80 = 0.8416, 0.85 = 1.036, 0.90 = 1.282, 0.95 = 1.645, 0.99 = 2.326 (ตรวจแล้วถูก)
- ไม่มีข้อมูล SD: ใช้ exponential ประมาณ M(t) = 1 - exp(-t/MTTR) (p.30) ผลที่ตามมา (คำนวณเอง): Mmax(95%) = MTTR x ln 20 ≈ 3.0 x MTTR

## 7. Maintainability allocation (p.30-33)
- เงื่อนไขระบบ (p.30, eq.1): M̄ct ระบบ = Σλi·M̄cti / Σλi
- Allocation ตาม failure rate (eq.2): M̄cti = M̄ct·Σλ / (n·λi) หมายถึง unit ที่เสียบ่อยต้องได้ MTTR สั้นกว่า
- ระบบ upgrade ที่ใช้ L subsystem เดิม (eq.3, p.31): หัก Σλi·M̄cti ของของเดิมออกก่อน แล้วแบ่งส่วนที่เหลือให้ (n-L) subsystem ใหม่
- แบบถ่วง design feature (eq.4-5): แปลง complexity, accessibility, testability เป็น weight coefficient ki ร่วมกับ failure rate slide เตือนว่าแบบ failure rate อย่างเดียว "สมเหตุผลแต่อาจทำไม่ได้จริง"
- Time-characteristics model (p.32-33): แยก **common repair time** (กำหนดโดย layout/การออกแบบระดับบน เช่น preparation, approaching) กับ **individual repair time** (กำหนดโดยผู้ออกแบบ unit เช่น assembly, adjustment); หัก common ออกจาก MTTR ก่อน แล้วจัดสรร individual ลงไป ทำให้แต่ละแผนกได้เป้าที่คุมได้จริง; กิจกรรมซ่อม: preparation, localization/diagnosis, approaching, correction, reassembly, adjustment, checkout

## 8. Renewal theory และ modeling maintenance actions (p.34-36)
- Renewal process = ขยาย Poisson process ให้ช่วงเวลาระหว่างเหตุเป็น iid distribution ใดก็ได้ที่มี mean จำกัด; renewal function m(t) = จำนวนเหตุที่คาดหวังถึงเวลา t; elementary renewal theorem: m(t)/t เข้าใกล้ 1/mean holding time; renewal equation เป็นสมการ integral แบบ recursive (สูตรใน slide p.34 OCR เพี้ยน)
- ระดับงานบำรุงรักษาตาม **NF X60-000** 5 ระดับ (p.35): 1 งานง่ายเข้าถึงสะดวก, 2 procedure ง่ายและอุปกรณ์เพิ่ม, 3 procedure ซับซ้อน/เครื่องมือเช่น thermography โดยช่างที่มีคุณวุฒิ, 4 ต้องรู้เทคนิคเฉพาะ, 5 ต้องใช้ know-how ของผู้ผลิต (ตัวอย่างเป็น PV plant/inverter) ต้นทุนบำรุงรักษาถูกกำหนดไปมากแล้วตั้งแต่ design
- Objective J(L,p) ของ maintenance policy บนช่วง [0,L) ประเมินได้ 3 แบบ: expected value, mean ลบ variance (penalize ความผันผวน), และ exponential utility ที่มี risk-aversion factor γ (p.35); กรอบ optimization model รวม data sources, system info, maintenance actions/policies, deterioration modeling, algorithms (p.36)

## 9. PM, CM และระดับการทำงาน (p.37-41)
- PM (p.37-38): replacement ก่อนเสียคุ้มเฉพาะเมื่อ failure rate เพิ่มขึ้น/ใกล้ wear-out; ข้อยกเว้นคือ PM แบบ servicing (เช่น หล่อลื่น) บน unit ที่ failure rate คงที่ ถ้าไม่ทำแล้ว failure rate จะเพิ่ม; PM อาจ induce failure; interval สั้นไปต้นทุน PM สูง ยาวไปต้นทุน failure สูง; รวมงานหลายอย่างในการหยุดครั้งเดียวลด downtime
- ข้อมูลที่ต้องใช้หาช่วงเปลี่ยนที่เหมาะสม (อ้าง O'Connor 2002) 7 ข้อ: distribution และ parameter, ผลต่อระบบ, ต้นทุน failure (รวม downtime/safety), ต้นทุน PM, ผลของ PM ต่อ reliability, operator ตรวจพบได้หรือไม่, ต้นทุน inspection
- CM (p.39-40): active repair แบ่ง 7 ขั้นตาม **MIL-HDBK-472**: localization, isolation, disassembly, interchange, reassembly, alignment, checkout; ลด MTTR ต้องทำตั้งแต่ design; BIT ช่วยลดเวลา isolate แต่เพิ่ม hardware ที่เสียได้; inactive time = รออะไหล่/เครื่องมือ/ขนส่ง/admin
- เลือกสถานที่ทำงาน (p.40): on site, on-site workshop, off-site workshop ตามความปลอดภัย, คน, การเข้าถึง, ทักษะ, turnaround time; เกณฑ์ non-economic (policy, safety, fragility, capacity, skills) และ economic (training, transport, spare investment, demand rate) (p.41)
- Maintainability เป็นฟังก์ชันเวลา เช่น M(3 h) = 0.95; PM ลดเวลา diagnosis และ procurement (p.41)

## 10. Reliability math, RBD และ allocation (p.42-47)
- R(t) = e^(-λt); series Rs = ΠRi; parallel Rp = 1 - Π(1-Ri) (p.42-43); RBD แปลงเป็น success/fault tree ได้ด้วย De Morgan; ถ้า block ไม่ independent ใช้ dynamic RBD (p.44)
- **ข้อผิดใน slide (p.44)**: ตัวอย่าง R1 = 0.905 อนุกรมกับ (R2 = 0.580 ขนาน R3 = 0.600) อนุกรมกับ R4 = 0.861: ส่วนขนาน 0.832 ถูก แต่ 0.905 x 0.832 x 0.861 = **0.648** ไม่ใช่ 0.541 ตามที่ slide เขียน
- Allocation 3 วิธี (p.45): equal, weighted, cost optimization; equal: 5 ชิ้นอนุกรม เป้า 0.90 ได้ 0.98 ต่อชิ้น (0.98^5 = 0.904) ง่ายแต่ไม่ optimal (p.46)
- ตัวอย่างอนุกรม (p.46): 0.70, 0.80, 0.90 ได้ 0.504 เป้า 0.85 ยกตัวเดียวไม่พอแม้เป็น 1 (สูงสุด 0.72 คำนวณเอง)
- ตัวอย่างขนาน (p.47): 0.6, 0.7, 0.8 ได้ 0.976 เป้า 0.99 ยกตัวเดียวพอ (คำนวณเอง: ต้อง R1 ≥ 0.833 หรือ R2 ≥ 0.875 หรือ R3 ≥ 0.917)
- นำเข้าหัวข้อ cost/penalty function: ต้องรู้ต้นทุนเทียบ reliability ก่อนปรับ design ไม่เช่นนั้น overdesign; ดีที่สุดคือสร้างจากข้อมูลต้นทุนจริง (p.47) ต่อใน CMPR-05

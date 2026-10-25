# CMPR-11: Turnaround Phases, Human Reliability, Culture Change, Reliability Growth, FTA, Dependency Modeling, State Diagrams

Source: PETROSYNC CMRP training course slides, file CMPR-11.pdf (scanned, OCR). Reading notes ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ PDF page `(CMRP CMPR-11 p.N)`

ขอบเขต: PDF 30 หน้า (2 slide ต่อหน้า, เลข slide ในคู่มือ 387-416) เนื้อหาไม่ใช่ turnaround ทั้งไฟล์: p.1-3 = 4 phases ของ turnaround (ต่อจาก CMPR-10), p.4-8 = human reliability/human factors, p.8-13 = culture change, p.14-15 = reliability growth (Duane, Crow-AMSAA), p.16-24 = Fault Tree Analysis และความสัมพันธ์กับ RBD, p.25-27 = dependency modeling, p.28-30 = state diagram/statechart OCR ดีโดยรวม ยกเว้นข้อความ phase 2 (p.1) ที่ตัวเล็ก/จาง และ figure ภาพรวม turnaround (p.3) ซึ่งตรวจจากภาพ zoom แล้ว ตรวจภาพ p.1, 3, 8, 15, 18 ไม่มีลายมือมีสาระ

## 1. Phases ของ turnaround (p.1-3)

- **Phase 1 Initiation**: ตำราต้นทางเพิ่ม phase นี้ (วิธีอื่นมักเริ่มที่ preparation) เริ่มตั้งแต่ผู้บริหารยกประเด็น turnaround ครั้งหน้า อาจ **2 ปีหรือมากกว่า** ก่อน event; กำหนด objective, policy, แต่งตั้งคน ตั้งทีมเตรียมงาน และรวบรวมข้อมูลพื้นฐาน (CMRP CMPR-11 p.1)
- **Phase 2 Preparation**: phase หลัก ทีมเล็กทำงานนาน specify/schedule/resource/cost งานจำนวนมาก มีความไม่แน่นอนเพราะสภาพภายในเครื่องมองไม่เห็น ใช้ **contingency analysis** 4 คำถาม: fault อะไรน่าจะเจอ, แก้นานเท่าไร, ค่าใช้จ่าย, กระทบ duration อย่างไร (คำตอบเป็นค่าประมาณ แต่มักเป็นแนวทางเดียวที่มี) ขั้นสุดท้ายคือ briefing ทุกคนที่เกี่ยวข้อง (p.1)
- **Phase 3 Execution**: แผนถูกทดสอบกับความจริง งานจำนวนมาก คนหลายสาขา พื้นที่จำกัด ภายใต้แรงกดดันเวลา/เงิน sub-phases ตามลำดับ: shutdown (เอา inventory ออก, decontaminate, cool, isolate) -> open up -> inspect -> install/overhaul/remove -> box up -> test (pressure, system, trip/alarm) -> start up -> clean up/final inspection (p.2)
- **Single point responsibility**: ทุกจุดส่งต่องาน ผู้รับผิดชอบต้อง (1) ตรวจว่าขั้นก่อนหน้าเสร็จถูกต้องก่อนรับ (2) ทำส่วนของตนตาม spec (3) ส่งต่อเร็วที่สุด (4) รายงานการส่งต่อ Turnaround manager รับผิดชอบรวม (p.2)
- **Phase 4 Termination**: 2 องค์ประกอบ คือคืนโรงงานในสภาพพร้อมใช้ และ de-brief ทุกคนเพื่อเก็บ lessons learned (p.3)
- Figure 1.2 Turnaround overview (p.3, อ่านจากภาพ):

| Phase | ระยะเวลา (ตาม figure) | Critical issues (ย่อ) | Critical activities (ย่อ) |
|---|---|---|---|
| 1 Initiation | "หลายเดือน" | review past events, objectives, policies, minimize cost, balance constraints, delegate, monitor, flexibility | ตั้ง steering group, แต่งตั้ง turnaround manager, ตั้งทีมเตรียมงาน, plant team ออก initial work list |
| 2 Preparation | 3-18 เดือน (ตามขนาด) | lead small team, policy -> project, contingencies, plan, contracts, cost forecast, targets | challenge/validate แล้ว **freeze work list**, job specification packages, pre-shutdown work, long-lead items, contracts, logistics, schedule/resource profile, org chart, cost control, safe system of work/quality plan, ส่งแผนให้ steering group อนุมัติ, briefing |
| 3 Execution | ปกติ 2-8 สัปดาห์ | coordinate, control planned และ emergent work, duration, expenditure, safety, quality | shutdown ตามแผน, control team กำหนดและคิดราคา emergent work, start-up ตามแผน |
| 4 Termination | ปกติ 1-2 สัปดาห์ | analyse performance, review, extract learning, recommend, close-out report | เก็บพื้นที่, plant manager ตรวจรับ handover, de-brief, final report |

- figure ชี้ว่า work list คือรากฐานของทุกอย่าง (safety, quality, cost, materials, resources, logistics, duration) และ preparation ต้องละเอียด คำนวณแม่น (p.3)
- **ข้อไม่สอดคล้อง**: ข้อความ p.1 บอก initiation อาจเริ่ม 2 ปีหรือมากกว่าก่อน event แต่ figure p.3 บอกกินเวลา "a period of months" (ตีความได้ว่า initiation กินเวลาหลายเดือนแต่เริ่มเร็ว แต่ slide ไม่ได้อธิบาย)
- หมายเหตุ: ไฟล์นี้ไม่มีหัวข้อ "scope control" แยก การคุม scope อยู่ที่ freeze work list (p.3), การ define/cost emergent work (p.3) และ golden rule ใน CMPR-10 p.20

## 2. Human reliability (p.4-8)

- Human behavior model: ข้อมูลเข้า -> filters -> perception -> processing -> response โดยมี short-term/long-term/external memory และปัจจัยงาน/สภาพแวดล้อม (p.4, แผนภาพ)
- ขั้นตอน HRA (แผนภาพ p.4): problem definition, task analysis, error identification, representation, quantification, impact assessment, error reduction, quality assurance, documentation
- slide อ้าง Moore (1994): ราว **65%** ของอุบัติเหตุร้ายแรงทางทะเลมาจาก human + organizational error ช่วง operation; ตัวอย่าง Bhopal, Three Mile Island, Chernobyl, Piper Alpha (p.4)
- HRA 3 ขั้นหลัก: identification, quantification, reduction (p.4)
- **P(HE) = จำนวนครั้งที่ผิดพลาด / จำนวนโอกาสที่จะผิดพลาด**; human reliability = ความน่าจะเป็นที่คนทำงานได้น่าพอใจ (p.5)
- คำถามของ HRA: อะไรผิดได้, ผลคืออะไร, PSF (performance shaping factor) ไหนมีผลมากสุด, ต้องทำอะไรเพื่อป้องกัน; การเลือกวิธีขึ้นกับ objective, ข้อมูล human error ที่มี, และเวลาที่ใช้วิเคราะห์ (p.5)
- ประเภท error (p.6-7): **omission** (ไม่ได้ทำขั้นตอน เช่น พลาด alarm, ข้ามขั้นตอนซ่อมจนเครื่องเสียทันทีหลังซ่อม), **commission** (ทำผิด ปริมาณ/คุณภาพ/ลำดับ), **intentional** (รู้ผลแต่ยังฝ่าฝืน เช่น ข้าม safety procedure เพื่อให้เร็ว)
- PSF: internal = psychological (stress, ขาดแรงจูงใจ) และ physiological (สุขภาพ); external = technological (ergonomics, procedure, เครื่องมือ — บริษัทควบคุมได้) และ social (p.7-8)
- พฤติกรรม 3 ระดับ: procedure-based, skill-based, knowledge-based (p.8) (ความรู้ทั่วไป: สอดคล้องกับ Rasmussen SRK)
- **ข้อสังเกต**: แผนภาพ p.6-7 แสดงแค่ omission/commission แต่ข้อความมี 3 ประเภท (รวม intentional); สะกด "Ommission" ผิดในแผนภาพ

## 3. Culture change (p.8-13)

- "Culture Change Cycle" 4 quadrant: 1 unconscious incompetence, 2 conscious incompetence, 3 conscious competence, 4 unconscious competence (p.8) (ความรู้ทั่วไป: นี่คือ conscious competence learning model ของการเรียนรู้รายบุคคล slide ใช้ชื่อ culture change)
- สร้าง buy-in: pitch ที่ตอบว่าทำไมเปลี่ยน กระทบธุรกิจอย่างไร เป้าหมายคืออะไร พร้อม roadmap; ได้การสนับสนุนจากผู้บริหารสูงสุดและหัวหน้าระดับกลางแต่เนิ่น ๆ; คนชอบสิ่งที่มีมานาน จึงต่อต้าน (p.9)
- หลัก: pitch ที่แข็งแรง, transparent (บอกทั้งสิ่งที่ดีและล้มเหลว), เก็บ input ระหว่างทาง (task force, ช่องทางส่งคำถาม, แบบไม่ระบุชื่อ) (p.10)
- ให้คนเป็นเจ้าของ reliability: ดึง process owner/production leader มาร่วม strategy; operator คือ layer แรกในการจับอาการผิดปกติ ต้องฝึกให้รู้อาการเครื่องผิดปกติ; ให้ความรู้ reliability ทุกระดับ; ไปดูหน้างานจริง (p.11)
- reliability ไม่ใช่หน้าที่ของ reliability engineer คนเดียว; องค์กร proactive ป้องกันก่อน reactive รอให้เสีย (p.12)
- Change cycle 6 ขั้น: ผูกกับ business goal -> รู้ความเชื่อปัจจุบัน -> สร้าง narrative ใหม่ -> ให้รางวัล/โชว์ความสำเร็จ -> ความสัมพันธ์โปร่งใส -> ยอมรับว่าเปลี่ยนแบบค่อยเป็นค่อยไป (p.12)
- Change steps: (1) สะท้อนสถานะปัจจุบัน (เช่น ใช้ FMEA/ALT แค่ทำ checklist หรือใช้ตัดสินใจจริง) ทำรายงานสั้น (2) สร้าง vision ที่จับต้องได้ (3) ทำ roadmap มี milestone เช่น ปรับ data analysis, สร้าง reliability/availability model, เริ่ม HALT/FMEA (p.13)

## 4. Reliability growth (p.14-15)

- เนื้อหา p.14 มาจากบริบท **software reliability** (debugging, release, ROCOF): model แบบ equal-step สมมติว่าทุกการแก้ fault เพิ่ม reliability เท่ากัน ซึ่งไม่จริง; Littlewood-Verrall (1973) ใส่ random step และยอม reliability ลดได้เมื่อการแก้ใส่ fault ใหม่ การปรับปรุงต่อครั้งลดลงตามเวลา (p.14)
- Reliability prediction: fit model กับข้อมูลที่วัด แล้ว extrapolate หาเวลาที่ถึงเป้า ใช้วางแผนทรัพยากร test และเจรจา requirement (p.14)
- **Duane model** (J.T. Duane, 1962): บน log-log plot cumulative failure rate เทียบ cumulative test time เป็นเส้นตรง (Duane postulate) slope ลบ = growth rate α; มาจากข้อมูล 5 ระบบ (hydro-mechanical, aircraft generator, jet engine) (p.15)
- **Crow-AMSAA** (Larry H. Crow, US Army AMSAA, 1970s): pattern เดียวกับ Duane แต่มีฐานสถิติ = NHPP ที่มี Weibull intensity ประมาณค่า parameter ได้ มี confidence interval และ goodness-of-fit ใช้ติดตามภายใน test phase (MIL-HDBK-189 App. C) ให้ reliability ปัจจุบัน, ณ สิ้น phase, ถ้าขยายเวลา test, growth rate (p.15)
- **ข้อผิดพลาดเล็ก**: slide เขียน "General Electrical Company" ควรเป็น General Electric (ความรู้ทั่วไป)

## 5. Fault Tree Analysis (p.16-24)

- FTA: วิเคราะห์ top-down แบบ deductive ใช้ Boolean logic รวม lower-level event ไปสู่ top event (undesired state) (p.16)
- ใช้เพื่อ: เข้าใจ logic สู่ top event, แสดงการผ่าน safety/reliability requirement, จัดลำดับ contributor (critical items list), monitor safety, optimize ทรัพยากร, เป็น design tool, เป็น diagnostic tool (p.17)
- ประวัติ: Bell Labs, H.A. Watson 1962 (Minuteman I launch control); Boeing/AVCO ขยายใช้ 1963-64; NASA หันไปใช้ FMEA หลังผล quantitative ของ Apollo ต่ำ แล้วกลับมาใช้ PRA/FTA หลัง Challenger 1986; OSHA PSM 1992 ยอมรับ FTA เป็นวิธี PHA (p.17-18)
- **ข้อผิดพลาดใน slide**: p.18 อ้าง PSM standard เป็น "19 CFR 1910.119" ที่ถูกคือ **29 CFR 1910.119** (ความรู้ทั่วไป)
- มาตรฐาน: NUREG-0492, SAE ARP4761, MIL-HDBK-338, IEC 61025 / EN 61025 (p.19)
- ตัวอย่าง metal stamping press: top event = อวัยวะถูกกด; แยก OR (normal operation vs maintenance), OR (operator vs คนอื่น); การออกแบบให้กดสองปุ่ม = AND (p.20)
- **Common cause/common mode**: event เดียวกระทบหลาย subsystem ปรากฏหลายจุดใน tree ทำให้เกิด dependency และคำนวณยากขึ้น (p.20)
- **Cut set** = ชุด event ที่ทำให้เกิด top event; **minimal cut set** = ตัด event ใดออกแล้วจะไม่เกิด top event (p.21); event tree เริ่มจาก initiator ไปหาผลหลายแบบ (p.21)
- Software: CAFTA (EPRI), SAPHIRE (INL), RiskSpectrum, SCRAM (open source, Open-PSA) (p.21-22)
- Event symbols: basic, external (house), undeveloped, conditioning, intermediate; Gate: OR, AND, exclusive OR, priority AND, inhibit; transfer symbol เชื่อม sub-tree (p.22-23)
- FTA vs RBD (p.24): แปลง fault tree เป็น RBD ได้ง่ายกว่าแปลงกลับ; RBD มี load sharing และ standby (quiescent failure) ที่ FTA คลาสสิกไม่มีเทียบเท่า (priority AND ใช้แทนได้บางส่วน); XOR gate ไม่มี RBD เทียบเท่าเพราะในทาง reliability จะหมายถึงระบบทำงานได้แม้ทุกชิ้นเสีย; house event = block ที่ไม่เสียหรือเสียแน่นอน (prob 0/1); transfer = subdiagram block

## 6. Dependency modeling และ state diagrams (p.25-30)

- Dependency modeling: ถ้า event หนึ่งเกิด กระทบอะไรต่อ ใช้ลด risk และทำ scenario ("what if") สำหรับ business continuity; รวมทั้ง hard system และ soft system (คน); วิธี: วิเคราะห์ทุกส่วน, ระบุ interdependency ลงลึกเป็นชั้นจนถึงระดับที่ตกลง, ตั้งสถานะ Red/Amber/Green, ทดสอบ, ทำรายงาน (p.25) ตัวอย่างบ้าน: function (nutrition, sanitation, heating) ลงไป 1-3 ระดับ (mains elec, water, wiring) (p.26-27)
- slide p.25 อ้างชื่อบริษัทที่ปรึกษา ("at RiskEnomics") แสดงว่ายกมาจากเนื้อหาการตลาดของบริษัท
- State diagram: ระบบมีจำนวน state จำกัด แสดง state + transition (ตัวอย่างประตู open/closed); state-transition table; อธิบายเชิงสถิติด้วย Markov chain; NFA ให้หลาย state ได้; state diagram ไม่ใช่ flowchart (node ของ flowchart คือคำสั่ง = transition) (p.28-29)
- Harel statechart (อยู่ใน UML): ลดปัญหา state explosion ด้วย superstate และ orthogonal region (p.30)

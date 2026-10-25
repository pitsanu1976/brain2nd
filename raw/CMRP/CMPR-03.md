# CMPR-03: FMECA, RCM strategy logic, PM interval, Spare part strategy, RCA และ KPI / Balanced Scorecard

Source: PETROSYNC CMRP training course slides, file CMPR-03.pdf (scanned, OCR). Reading notes ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ PDF page `(CMRP CMPR-03 p.N)`

ขอบเขต: PDF p.1-50 (1 หน้า PDF = 2 slide, เลขท้ายหน้าบน slide 107-156) OCR อ่านได้ดีเกือบทุกหน้า ยกเว้นผังและรูป (p.2, 6, 7, 12, 13, 15, 22 ตรวจจาก PNG แล้ว) ลายมือเขียนเพิ่มส่วนใหญ่อ่านไม่ออก (ข้ามไป) ครึ่งหลังของไฟล์ (p.29-50) ย้ายไปหัวข้อ management: KPI, SMART, Balanced Scorecard, business case ข้อความทั้งหมดด้านล่างเป็นการถอดความ ไม่ใช่ข้อความต้นฉบับ

## 1. FMECA: การจัดระดับความน่าจะเป็นของ failure mode (p.1-4)

- **Brief method** 4 ระดับ (CMRP CMPR-03 p.1): 1 Extremely Remote (ไม่น่าเกิด), 2 Remote (อาจเกิดได้เมื่อเวลาผ่านไป), 3 Reasonably Probable (น่าจะเกิดเมื่อเวลาผ่านไป), 4 Probable (น่าจะเกิดทันทีหรือในเวลาสั้น)
- **Detailed method** ตาราง "Probability of Occurrence" 10 ระดับ (CMRP CMPR-03 p.1):

| Rank | ความน่าจะเป็น | ความหมายโดยย่อ |
|---|---|---|
| 1 | 1/10,000 | แทบไม่มีโอกาส |
| 2 | 1/5,000 | อัตราเสียต่ำ (เทียบแบบเดิมที่เคยเสียน้อย) |
| 3 | 1/2,000 | อัตราเสียต่ำ |
| 4 | 1/1,000 | เสียเป็นครั้งคราว |
| 5 | 1/500 | ปานกลาง |
| 6 | 1/200 | ปานกลางถึงสูง |
| 7 | 1/100 | สูง เคยก่อปัญหา |
| 8 | 1/50 | สูง |
| 9 | 1/20 | สูงมาก เกือบแน่นอนว่าก่อปัญหา |
| 10 | 1/10 ขึ้นไป | สูงมาก |

  ข้อสังเกต: หัวคอลัมน์ในสไลด์เขียนว่า "Effect" แต่ข้อมูลเป็นความน่าจะเป็น (น่าจะพิมพ์ผิด) และคำอธิบาย rank 2/3, 7/8, 9/10 ซ้ำกันทุกคำ ทำให้แยกแต่ละคู่ด้วยตัวเลขเท่านั้น สไลด์ไม่ระบุหน่วย (ต่อชิ้น ต่อรอบ หรือต่อชั่วโมง)
- นิยาม FMECA (p.2): เมื่อ FMEA มี **criticality index** เพิ่มเข้าไปเรียกว่า FMECA โดย index มักเป็น **ผลรวมหรือผลคูณ** ของ Severity กับ Probability index ค่าสูงกว่า = ต้องแก้ก่อน การแบ่ง index เป็นระดับความเร่งด่วนเป็นการตัดสินใจของฝ่ายบริหาร สำหรับแต่ละ FM ต้องเลือกระหว่างแก้แบบ (prevent/control) หรือให้เหตุผลว่ายอมรับได้
- ตัวอย่าง **Pressure Cooker FMECA** (p.3): กำหนด scope (resolution = 4 subsystem: electrical system, safety valve, thermostat, pressure gage; focus = safety) แล้วทำ block diagram (electrical = cord, plug, heating coil; safety valve = valve casing, valve spring) อุปกรณ์ป้องกัน 3 ชั้น: safety valve ระบายแรงดัน, thermostat ตัดวงจรเมื่อร้อนเกิน, pressure gage แถบเขียว/แดง
  - **ข้อสงสัย:** สไลด์ระบุ thermostat ตัดที่ 250 °C ซึ่งสูงผิดปกติสำหรับหม้ออัดแรงดัน (น้ำเดือดใต้แรงดันราว 120 °C) น่าจะเป็น 250 °F ในต้นฉบับ (ความรู้ทั่วไป)
- ประโยชน์ของ FMECA (p.4): รายการ FM และสาเหตุ (ช่วยวางแผน test/inspection), จัดระดับความวิกฤติ, มาตรการตรวจจับ/ควบคุมต่อ FM, ข้อมูลบริหาร, input ให้การวิเคราะห์ต่อ
- ข้อจำกัด (p.4): ต้องคาด FM ได้ล่วงหน้า, ไม่รวม **multiple failure interaction**, ไม่ดูอันตรายที่เกิดตอนระบบทำงานปกติ, ไม่รวม human factors

## 2. RCM และการเข้าใจ failure (p.2, 4-6)

- วงล้อ 7 ขั้นของ RCM (p.2, จากภาพ): 1 เลือก asset, 2 นิยาม function ของระบบ, 3 ดูว่าระบบเสียได้อย่างไร, 4 หา root cause ของ FM, 5 ประเมิน consequence, 6 ตั้งกลยุทธ์ต่อ FM, 7 implement และทบทวน
- ผัง RCM 4 กลุ่ม (p.2): **Reactive** (ชิ้นเล็ก ไม่วิกฤติ ไม่มีผล ไม่น่าเสีย มี redundancy), **Interval (PM)** (มี wear-out, ของสิ้นเปลือง, รู้ failure pattern), **CBM** (random pattern, ไม่ wear, failure ที่ PM ก่อขึ้น), **Proactive** (RCFA, Age Exploration, FMEA, acceptance testing)
- 4 คำถามเลือกกลยุทธ์ (p.4): failure ซ่อนหรือไม่, วิกฤติหรือไม่, มีตัวชี้สภาพ (condition indicator) ใช้ได้ไหม, คาบการเสียรู้และคงที่ไหม
- **Hidden failure** (p.5): ผลมองไม่เห็นในการเดินเครื่องปกติ ผูกกับ hidden function เช่นอุปกรณ์ป้องกัน; นิยามไม่ได้ขึ้นกับว่าสาเหตุ/กลไกการเสื่อมมองเห็นยากหรือไม่ **Critical failure**: ใช้ผล criticality analysis ถ้าผลหรือความเสี่ยงยอมรับไม่ได้ ต้องมีมาตรการป้องกัน
- How things fail (p.5): เครื่องส่วนใหญ่ไม่ได้มีโอกาสเสียเพิ่มขึ้นตามอายุ; สไลด์อ้างว่าราว **60%** ของอุปกรณ์แสดงแค่ช่วง 1 (infant) และ 2 (random) ของ bathtub ไม่ถึงช่วง wear-out (ไม่ระบุแหล่ง)
- P-F curve (p.6): จาก "normal" สภาพเสื่อมถึงจุด P (potential failure, เริ่มตรวจเจอ deviation) แล้วถึง F (functional failure); ช่วง P-F = lead time
- Maintenance types (p.6) แบบ EN 13306: ก่อนเสีย = Preventive (3a Condition-based: 4a testing & inspection, 4b condition monitoring; 3b Predetermined: 4c periodic test, 4d scheduled replacement, 4e scheduled service) หลังเสีย = Corrective (4f immediate, 4g deferred)

## 3. Maintenance strategies และ decision logic tree (p.7-8)

- 5 กลยุทธ์ (p.7): **RtF** (ซ่อมหลังเสีย), **FFM** (functional test หา failure ที่ซ่อน ไม่ได้ป้องกันการเสีย), **SM** (ทำตามเวลา/ชั่วโมงเดิน ไม่สนสภาพ), **CBM** (วัดสภาพแล้วตัดสินว่าทำเมื่อไร), **MOD** (ไม่ใช่ maintenance แต่ต้องเปลี่ยนแปลง ไม่จำเป็นต้องเป็นเรื่องเทคนิค)
- Decision tree (p.7, จากภาพ):

```
Hidden failure?  Yes -> CBM ได้? Yes = CBM / No = FFM
                 No  -> Critical? No = RtF
                        Yes -> FAR (Failure Related Ageing)? No = MOD
                               Yes -> CBM ได้? Yes = CBM
                                      No -> CFI (Constant Failure Interval)? Yes = SM / No = SM
```
  **ข้อสังเกต:** กิ่ง CFI = No ในภาพลากเส้นไปที่ "SM" เช่นกัน (มี SM สองกล่อง) ทำให้คำถาม CFI ไม่มีผลต่อคำตอบ น่าจะเป็นความผิดพลาดของผัง (ตามตรรกะควรเป็น MOD หรือทบทวนใหม่เมื่อคาบเสียไม่คงที่)
- ตัวอย่างรายการ failure modes (p.8) เช่น fails to open/close, internally/externally leaks, erratic/high/low/no output, inadvertently trips, loss of efficiency; และรายการ failure effects เชิงระดับ: machine unavailable >8 h / 2-8 h / <2 h, ผลต่อการผลิต (significant/moderate/none), quality, injury (recordable/non-recordable), release (external/on-site/none), ค่าซ่อมถ้า RtF (>35,000 / 10,000-35,000 / <10,000 Kronor), loss of redundancy, ข้อมูลผิดถึง operator ฯลฯ

## 4. การกำหนดคาบงาน (task interval) (p.9-12)

- Decision tree ไม่ได้ให้คาบ ต้องถามเพิ่ม (p.9): FM เกิดบ่อยแค่ไหน, P-F ยาวเท่าไร, วัดการเสื่อมได้พอไหม, มีกฎหมายกำหนดไหม ปัจจัยหลัก: Criticality, MTBF (และที่มาของ MTBF), redundancy, failure characteristics, regulations
- ภาพคาบของแต่ละกลยุทธ์ (p.10-11): RtF = หยุดตลอดช่วงวางแผนซ่อม; SM = หยุดก่อนเสียตามคาบที่ทำนายจาก MTBF มี safety margin แล้ว overhaul เป็น as-new; CBM = อ่านค่าตามความถี่ (ทั่วไป 1-3 เดือน) หยุดเมื่อเจอการเสื่อมครั้งแรก; FFM = เสียแล้วไม่รู้จนถึง function test ครั้งถัดไป คาบกำหนดจากความเสี่ยงและ MTBF
- **ตัวอย่าง logic tree คาบ PM** (p.12, จากภาพ): ถ้า criticality "extremely high" ไปกล่อง evaluation (ใช้ FFM/CBM/SM ที่คาบสั้นลง, ลด total cost, พิจารณา modification) ถ้า moderate หรือ high:

| กลยุทธ์ | สูตรคาบ T | เงื่อนไข |
|---|---|---|
| FFM | T = MTTF x 2 x (1 - A) | เลือก A = 90% เมื่อ criticality moderate |
| FFM | T = MTTF x 3 x (1 - A) | A = 95% เมื่อ high (ภาพไม่ได้ผูกบรรทัดกับระดับชัด อนุมานตามลำดับ) |
| CBM (inspection) | T = PF | moderate |
| CBM | T = 0.75 x PF | high |
| SM | T = TTF (ช่วงจาก SM ครั้งก่อนถึง failure ครั้งถัดไป) | moderate |
| SM | T = 0.75 x TTF | high |

  ตัวเลขประกอบ (คำนวณเอง): moderate FFM = 2 x 0.10 = 0.20 MTTF; high = 3 x 0.05 = 0.15 MTTF (สั้นกว่า สอดคล้องกับ criticality สูง)
  **ข้อสังเกต/ความไม่สอดคล้อง:**
  - สูตรมาตรฐาน FFI = 2 x (1 - A) x MTBF (ความรู้ทั่วไป และ wiki [[Failure Finding Interval]]) ตัวคูณ 3 ไม่ใช่สูตรมาตรฐาน และใช้ MTTF ของอุปกรณ์ป้องกันแทน MTBF
  - ตั้งคาบ inspection = PF เต็มช่วง (moderate) เสี่ยงพลาดจุด P เพราะถ้าตรวจห่างเท่า P-F อาจเจออาการตอนเสียไปแล้ว แนวทั่วไปใช้ P-F/2
  - ตั้ง SM = TTF (เท่าเวลาถึงเสีย) ไม่มี safety margin ขัดกับภาพ p.10 ที่บอกว่า SM ต้องมี safety margin

## 5. Spare part strategy (p.12-13)

- Top-down (p.12): Criticality study -> critical systems -> critical equipment -> critical failures -> spares required
- ตัวอย่างการตัดสิน (p.13, จากภาพ): ซ่อมได้โดยไม่ใช้อะไหล่ = ไม่สต๊อก; ไม่วิกฤติต่อ availability/safety/environment = ไม่สต๊อก; ทำให้ต้องสลับไปตัวสำรอง = ไม่สต๊อก **เว้นแต่** lead time > 2 สัปดาห์ จึงสต๊อก; วิกฤติต่อ availability/safety/environment = สต๊อก
- Optimisation (p.13): level of repair analysis (สต๊อกอะไร), interchangeability (OEM), sharing/pooling, risk-based analysis ตั้งระดับสต๊อก; เส้นโค้ง total cost = risk cost (ลดลงเมื่อสต๊อกมาก) + holding cost (เพิ่มขึ้น) มีจุดต่ำสุด
  - Risk Cost = Probability x Penalty ของการไม่มีของเมื่อต้องการ; Holding Cost = f(cost of capital, depreciation, supply base overhead); อ้าง SPARO (Spare Parts Alignment Rationalization and Optimization)

## 6. RCA / RCFA (p.14-28)

- RCFA มุ่งแก้ปัญหาที่กระทบ plant performance ไม่ใช่หาคนผิด ต้องสื่อสารให้ทีมและผู้เกี่ยวข้องเข้าใจ เพื่อลดท่าทีป้องกันตัว (p.14)
- Physics of failure (p.15): ชิ้นส่วนเสียเมื่อรับ stress ไม่ไหว 2 แบบ: **overload** (load สูงกว่า strength ของชิ้นที่อ่อนสุดในการกระจาย) และ **fatigue** (strength ลดลงตามการใช้งานจนการกระจาย strength ทับกับการกระจาย stress) แสดงด้วย stress-strength interference และ factor of safety; "ชิ้นส่วนเสียก่อน แล้วเครื่องจึงหยุด"
- RCA (p.15-17): แนวทางแก้ปัญหาอย่างเป็นระบบ มุ่งป้องกันการเกิดซ้ำ ใช้ได้ทั้งเหตุที่เกิดแล้วและการศึกษาจุดอ่อนล่วงหน้า เลือกมาตรการที่ได้ผล/ถูกสุด ติดตามผล ต้องวัดผลได้และให้ savings จริง 5 มุม (facets): safety, production, process, failure, systems-based
- Critical success factors (p.18): ทีมที่เหมาะ, วิธี/เครื่องมือ, training, **trigger points** สำหรับเริ่ม RCA, เก็บและรักษาข้อมูล, ติดตามการ implement, การสนับสนุนของผู้บริหาร; checklist 8 ข้อ (อนุมัติ, ความคาดหวังและ timeline, policy/procedure, orientation ผู้บริหาร, sponsor, ทีม, training, งบและเวลาของทีม)
- ระวัง **unanimity** ในทีม: consensus ดี แต่ทุกคนเห็นตรงกันหมดควรสงสัย (p.19)
- กระบวนการ RCA 4 ขั้น (p.19-20): (1) นิยาม problem statement และเงื่อนไข (2) รวบรวม possible causes พร้อมหลักฐานจาก FMEA, FTA, failure analysis, test, simulation ตั้งเป็น hypothesis (3) ประเมินด้วยสถิติ (test of hypothesis) หรือเทคนิคตัดสินใจ (decision tree, payoff table) คัดเหลือ true cause (4) validate ด้วยการทดลองให้เกิดปัญหาซ้ำ หลายเงื่อนไข
- ตัวอย่าง (p.21-22): อุปกรณ์เสียงไม่ดัง 3 ใน 100 ชิ้น ใน region 4 เริ่ม 2 สัปดาห์ก่อนและเพิ่มขึ้น; 7 สาเหตุที่เป็นไปได้; ใช้ fishbone + **FMEA** (high RPN: contamination, open circuit) -> Pareto -> DOE (main effect, interaction) พบว่าความชื้นจากมือ operator ร่วมกับวัสดุ contact ที่ heat treat ไม่สมบูรณ์ทำให้ oxidation; confirmation run ยืนยัน; แก้ด้วยถุงมือ + ทบทวน annealing (OCR "EMKA" ในภาพ = FMEA)
- Methods (p.23): rearward-looking = 5 Whys, Why-Because Analysis, Fault Tree Analysis; forward-looking = FMEA เคล็ดลับ: อย่าหยุดก่อนถึง root, ลงรายละเอียด, ต้อง validate คำตอบ
- **5 Whys** (p.24-26): ตัวอย่างรถสตาร์ทไม่ติด (battery -> alternator -> belt ขาด -> belt เกินอายุ -> ไม่ทำ service ตามตาราง = root cause) จำนวน "why" ไม่ต้องเป็น 5 พอดี ตัวอย่าง Washington Monument (สารเคมี -> นกพิราบ -> แมงมุม -> แมลง -> ไฟเปิดตอนพลบค่ำ) ทางแก้ระดับกลาง (สารเคมีอ่อน, ไล่นก, ยาฆ่าแมลง) แพงหรือมีผลเสีย ทางแก้ที่ root = ปรับเวลาเปิดไฟตามฤดู
- **Why-Because Analysis (WBA) / Why-Because Graph (WBG)** (p.26-28): ใช้มากกับอุบัติเหตุขนส่ง เริ่มจาก incident ด้านบนไล่ลงถึง root ตรวจ 2 แบบ: **Counterfactual test (CT)** ถ้าไม่มีสาเหตุนี้ ผลยังเกิดได้ไหม (พิสูจน์ว่าสาเหตุจำเป็น) และ **Causal Sufficiency Test (CST)** ถ้าสาเหตุที่ระบุเกิดครบ ผลเกิดเสมอไหม (หาสาเหตุที่ขาด) WBG ถูกต้องเมื่อทุกสาเหตุจำเป็นและชุดสาเหตุเพียงพอ: ไม่ขาด ไม่เกิน

## 7. Management, KPI และ Balanced Scorecard (p.29-48)

- Goal vs objective (p.31-32): goal กว้าง วัดไม่ได้; objective เป็นเป้าจริงจัง ใช้คำกริยาเชิงการกระทำ ตอบ who/what/when/why/to what standard ความผิดพลาดที่พบบ่อย: เขียนเป็น activity, เป็น vision, มีมากเกินไป
- **SMART** (p.33): Specific, Measurable, Achievable, Realistic, Timed ตัวอย่าง objective (p.34): ลด downtime ของ critical mechanical equipment จาก 3% เป็น 2% ภายในสิ้นปี 2015 โดย Integrity & Reliability Division ผ่านโปรแกรม RCFA
- KPI (p.34-35): วัดตัวแปรสำคัญตามเวลา จุดประสงค์หลักคือ **เปลี่ยนพฤติกรรม** รองคือบอกสภาพระบบ; KPI ที่ดีควรมี 13 องค์ประกอบ (title, purpose, relates to, target, formula, measure/review frequency, who measures, data source, owner, who acts, closed loop, notes)
- หลักกำหนด measure (p.36-37): ผูกกับ vision/strategy, **วัด cause ไม่ใช่ effect**, ดู trend ไม่ใช่ event, ตั้ง measure ใหม่เมื่อมี goal ใหม่; ผ่านการทดสอบ: มีประโยชน์กับใคร วัดอะไรจริง ใครรับผิดชอบ ช่วย business objective ไหม data พร้อมและซ้ำได้ไหม
- KPI ต้องมี target ที่ท้าทายแต่ทำได้ + upper/lower warning limit + upper/lower action limit + SPC (control chart) + owner ที่ต้องลงมือเมื่อเกิน limit; ไม่ควรตั้ง target โดยไม่มีทรัพยากร ไม่มี control limit หรือมอบให้คนที่คุมไม่ได้ (p.38-39)
- Lagging (การเงิน) vs leading (ลูกค้า, process, innovation) (p.40)
- ตัวอย่าง KPI sheet "Total Maintenance Cost per Installed Horse Power" (p.40-41): benchmark industry average 35, lowest 15, highest 60, world class 12 (ไม่ระบุหน่วยเงิน) **ข้อสังเกต:** world class (12) ต่ำกว่า "industry lowest" (15) ขัดกันเชิงตรรกะ (ถ้า lowest คือค่าต่ำสุดในอุตสาหกรรม world class ไม่ควรต่ำกว่า) องค์ประกอบ sheet: trend ปีก่อน, owner, เส้น satisfactory/unacceptable/goal, เหตุผลและต้นทุนของผลที่ไม่ผ่าน, action, distribution list
- **Balanced Scorecard** (p.41-45): แปลง mission/strategy เป็นชุด measure 4 มุม Financial, Customer, Internal Business Processes, Learning & Growth "balance" = สั้น/ยาว, การเงิน/ไม่ใช่, ภายนอก/ภายใน; cascade จาก business unit ลงถึงรายบุคคล
- Standard reporting process (p.46-48): KRA (Quality, Profitability, Productivity, Energy, Environment) -> เลือก KPI ต่อ KRA -> ทดสอบว่าใช้ได้จริง -> SMART -> วัด เทียบ limit -> ถ้านอกช่วงพิจารณาทำ RCA -> review (flowchart เขียนเชิงบริษัทผู้ให้บริการ เช่น "Sales Toolbox")

## 8. Business case (p.49-50)

- 5 ขั้นของ business case (หัวข้อในภาพบางส่วน: confirm the opportunity, high-level requirements, strategic logic) ใช้กับ CAPEX, IT project, การย้ายโรงงาน ฯลฯ
- Business case (ตัดสินการลงทุนเฉพาะโครงการ: value, profitability, alignment, feasibility) vs business plan (แผนระยะยาวทั้งธุรกิจ: ตลาด ลูกค้า forecast)

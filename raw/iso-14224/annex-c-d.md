# ISO 14224:2016 Annex C และ Annex D: reading notes (PDF p.211-243 = printed p.205-237)

Source: ISO 14224:2016 (3rd edition), reading notes ที่ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ printed page (PDF page = printed + 6)

ทั้งสอง annex เป็น informative Annex C ให้กติกาตีความและสูตรพื้นฐานของ derived RM parameters (ไม่ใช่ตำราวิเคราะห์ข้อมูลเต็มรูป อ้าง ISO/TR 12489:2013 และตำราสำหรับรายละเอียด) Annex D บอกว่าการวิเคราะห์แต่ละแบบต้องการข้อมูลอะไร (ISO 14224 cl. C.1.1, p.205)

## C.1 กติกาตีความ (p.205-210)

- **Redundancy** 3 แบบ: passive/cold standby (ส่วนสำรองไม่ทำงานจนถูกเรียก), active/hot standby (ทุกส่วนทำงานพร้อมกัน), mixed วัดเป็นตัวเลขได้ด้วย ERF เช่น 3 x 50% = ERF 1.5 failure ของ unit ในระบบ redundant ให้ **นับ** เมื่อประเมินอะไหล่/กำลังซ่อม แต่ **ไม่นับ** เมื่อประเมิน availability ของระบบ (cl. C.1.2, p.205)
- **On-demand data**: แยก (a) เสียก่อนถูกเรียก (hidden จนกว่า test/demand จริงเปิดเผย) กับ (b) เสียเพราะการเรียกเอง failure mechanism ช่วยแยกสองแบบได้ ต้องบันทึก **จำนวน demand** ทั้ง test activation ใน PM และ activation จริงขณะเดินเครื่อง (cl. C.1.3, p.205-206)
  - นิยาม demand ต่อ class: rotating/conveyor/heater = start-up (การหยุดหรือปรับ speed VSD ไม่นับ); crane/loading arm/winch = การทำงานแต่ละครั้ง; valve = ทั้งเปิดและปิดนับเป็น demand, control/choke valve นับทุกการปรับ; อุปกรณ์ safety/standby = ทุก activation ทั้ง test และ trip จริง; piping, heat exchanger, riser, filter, cable ไม่มีความหมายของ demand
  - PFD คำนวณเป็นสัดส่วนเวลาเฉลี่ยที่อยู่ในสถานะเสีย (ดู C.6.2)
- **Independent vs dependent**: P(A∩B) = P(A)P(B) ใช้ได้เฉพาะเหตุการณ์อิสระ ถ้าละเลย dependency ผลจะต่ำเกินจริง (ไม่ conservative) ซึ่งรับไม่ได้ในงาน safety (cl. C.1.4-C.1.5, p.206-207)
- **CCF** แบ่ง 3 กลุ่ม: utilities/สิ่งแวดล้อมภายนอก (นับเป็น CCF เฉพาะเมื่อโมเดลไม่ละเอียดพอจะแยก), internal (design/installation error, lot ชิ้นส่วนไม่ดี วิเคราะห์ยาก), cascade แยก CCF ที่ทำให้ชิ้นส่วนเสียจริงต้องซ่อมทีละตัว กับ CCF ที่แค่ทำให้ unavailable (เช่นไฟดับ) ไม่ต้องซ่อม เมื่อวิเคราะห์ไม่ได้ใช้ **β-factor**: λ = (1-β)λ อิสระ + βλ ส่วน CCF (อ้าง shock model ISO/TR 12489 Annex G) (cl. C.1.6, p.207)
- **CMF** ต่างจาก CCF: CMF คือหลายชิ้นเสียแบบเดียวกัน (mode เดียวกัน) ซึ่งอาจมีเหตุจาก CCF ก็ได้ (cl. C.1.7, p.207)
- **Trip vs manual shutdown**; spurious stop (UST) เป็นได้ทั้ง trip จริงหรือ spurious ตามสาเหตุ (cl. C.1.8, p.208)
- **Table C.1** failure occurrence rating 1-10 (ดัดแปลงจาก IEC 60812) ใช้ใน FMECA เชิงคุณภาพ: 1 = remote (≤ 1e-5), 4-6 = moderate (1e-3 ถึง 5e-3), 10 = very high (≥ 1e-1) (cl. C.1.9, p.208)
- **Table C.2** failure consequence 16 class: แถว Safety / Environmental / Production / Operational(cost) x คอลัมน์ Catastrophic / Severe / Moderate / Minor เลข I-XVI ไล่ตามคอลัมน์ (I-IV catastrophic, XIII-XVI minor) ต้องกำหนด "acceptable limit" เองต่อ application ใช้กับ failure ที่เกิดแล้ว (cl. C.1.10, p.208-209)
- **Analysis of failures** (cl. C.1.11, p.209-210): system modelling (Monte Carlo, Markov, reliability growth) สำหรับ critical service; Pareto หา bad actors; **RCA สำหรับ severity I-VIII และ bad actors**; **Weibull เมื่อ equipment type มี failure แบบเดียวกัน ≥ 5 ครั้ง ที่ severity I-XII**
  - กลุ่ม β: < 1.0 infant mortality (ติดตั้งไม่ดี, defect ผลิต, start-up ผิด); = 1.0 random (human error, foreign object หรือ **ความผิดพลาดจากการรวม failure mode/equipment ต่างชนิด** แก้ด้วย predictive maintenance/CM); 1.0-4.0 early wear-out (low-cycle fatigue, bearing ส่วนใหญ่, corrosion, erosion PM คุ้ม); ≥ 4.0 old-age wear-out (stress corrosion ฯลฯ ยิ่งชันยิ่งทำนายได้) รอบ overhaul อ่านจาก Weibull plot ที่ "β life" ที่เหมาะ

## C.2 Availability (p.210-213)

- availability = ทำงานได้ ณ ขณะหนึ่ง (ไม่สนว่าเคยเสีย); reliability = ทำงานต่อเนื่องตลอดช่วง (cl. C.2.1, p.210)
- นิยามคณิต: A(t) = P(up ที่เวลา t) (C.4); mean availability Am(t1,t2) = ค่าเฉลี่ย A(t) บนช่วง (C.5); steady-state Aas = ลิมิตของ mean availability เมื่อช่วงยาวไม่สิ้นสุด (C.6) (p.210-211)
- กรณี λ, μ คงที่: A(t) = μ/(λ+μ) + [λ/(λ+μ)]·exp(-(λ+μ)t) (C.7) → Aas = μ/(λ+μ) (C.8) เรียกว่า technical/intrinsic/inherent availability (p.211)
- **ค่าที่วัดจากข้อมูลสนาม** (cl. C.2.3.1, p.211-212):
  - Operational **Ao = MUT / (MUT + MDT)** (C.9) ใช้ up/down time จริง
  - Intrinsic **AI = MTTF / (MTTF + MTTRes)** (C.10) MTTRes ใช้ active maintenance time
  - **METBF = MTTF + MTTRes** (C.11)
- AI = Ao เฉพาะเมื่อ MDT = MTTRes AI สำหรับ reliability engineer, Ao สำหรับฝ่ายบำรุงรักษา Ao ไม่ใช่คุณสมบัติของตัวเครื่อง แต่ของเครื่องในบริบท (installation, procedure, maintenance policy, support) เพราะ MDT รวม detection, isolation, รออะไหล่, standby, ซ่อม, reinstatement (cl. C.2.3.2, p.212)
- ตัดเวลารอทรัพยากรภายนอกออกได้เพื่อให้ "intrinsic" มากขึ้น; จะรวมเวลา PM หรือไม่ก็เลือกได้ ต้องประมาณ λ และ μ **แยกกัน** (λ จาก MTTF/MUT, μ จาก MTTRes หรือ MRT) สูตรเดียวไม่พอ (p.212)
- รายปี (cl. C.2.3.2, p.213): **Ao,y = [8760 - (tC + tP)] / 8760** (C.14) นับทั้ง corrective และ preventive; **AT,y = (8760 - tC) / 8760** (C.15) technical availability นับเฉพาะ corrective ("technical" ใช้แทน "intrinsic" ได้)

## C.3 Failure rate / failure frequency (p.213-220)

- **Average failure frequency** w = n / ΣTTFi (C.16) ในทางปฏิบัติแทน ΣTTF ด้วยเวลาเดินเครื่องรวม ใช้ได้เมื่อสมมติ exponential; ตัวอย่าง w = 3e-4/h → เฉลี่ย 30 failures ใน 100,000 h และ 1/w = 3,333 h = MTTF + MTTRes (repairable, as-good-as-new) ไม่ใช่ "expected time to failure" (cl. C.3.1.1, p.213-214)
- **Failure rate (hazard, Vesely)** λ(t): λ(t)dt = โอกาสเสียใน [t, t+dt] เมื่อรอดถึง t; F(t) = 1 - R(t) (C.17); ถ้าคงที่ R(t) = exp(-λt), F(t) = 1 - exp(-λt), λ = 1/MTTF (C.18-C.19) เมื่อ hazard คงที่ w กับ λ มี estimator เดียวกัน แต่ความหมายยังต่างกัน (p.214)
- Bathtub (Fig C.1): ถ้าตัด early failure และถอดก่อน wear-out การสมมติคงที่พอรับได้; ถ้ามี wear-out แต่สมมติคงที่ → **ประเมิน reliability ต่ำไปช่วงอายุน้อย และสูงไปช่วงอายุมาก**; สำหรับ time to first failure ค่าคงที่ "misleading" ใช้ Weibull กับ component หรือ **Power law** กับ repaired system แทน (cl. C.3.1.2, p.214-215)
- **MLE ค่าคงที่**: λ̂ = n/τ (C.20) τ = aggregated time in service (surveillance หรือ operating time) ใช้ได้เมื่อ items มี λ เท่ากันและ n ≥ 1 (cl. C.3.2.1, p.215)
- **Confidence interval (chi-square)** (C.21-C.22, p.216): λL = χ²(2n)/(2τ) ที่ quantile ล่าง, λU = χ²(2(n+1))/(2τ) ที่ quantile บน ตัวอย่าง n = 6, τ = 10,000 h → λ̂ = 6e-4/h, ช่วง ≈ 2.6e-4 ถึง 1.18e-3/h (Fig C.2)
  - **ข้อสังเกต**: เนื้อความบอกช่วง 90% แต่ตัวอย่างและ Fig C.2 เขียนว่า 95%; ตัวเลขตัวอย่างตรงกับ quantile 5% และ 95% คือช่วง two-sided **90%** (ตรวจ derived: χ²0.05(12) = 5.226 → 2.61e-4; χ²0.95(14) = 23.685 → 1.18e-3) และสัญลักษณ์ z0.95/z0.05 ใน C.21/C.22 ดูสลับกับคำอธิบาย ต้องใช้อย่างระวัง
- **Heterogeneous (multi-sample) estimator** สำหรับรวมข้อมูลหลาย installation/fleet (cl. C.3.2.2, p.216-218): แบ่งเป็น k class ที่ถือว่า homogeneous แต่ละ class มีจำนวนเครื่อง mi, failures ni, เวลา τi ถือว่า λ เป็นตัวแปรสุ่มระหว่าง class (Bayesian, prior แบบ gamma) ขั้นตอน: pooled m = Σn/Στ; คำนวณ S1 = Στ, S2 = Στ²; ความแปรปรวนระหว่าง class 2 แบบ (V*, V̄) เอาค่ามากกว่า Vt; ค่าเฉลี่ยถ่วงน้ำหนัก Ê (น้ำหนักประมาณ 1/(m/τi + Vt)); β̂ = Ê/Vt, α̂ = β̂·Ê; ค่าประจำ class **λ̂i = (α̂ + ni)/(β̂ + τi)** (C.36) และ credibility interval จาก quantile ของ gamma (เป็นแนวคิดเดียวกับ multi-sample ของ OREDA handbook ซึ่งให้ mean กับ SD; ข้อเชื่อมนี้เป็นความรู้ทั่วไป)
- **Zero failures** (cl. C.3.3, p.218-219): Bayesian non-informative prior λ̂ = (2n+1)/(2t) (C.37) → 1/(2t) เมื่อ n = 0 (C.38) หมายเหตุ: บางหน่วยงานกำกับ (เช่น nuclear) ไม่ยอมรับ Bayesian; ทางเลือก **constant confidence-level estimator λ̂ = (n + 0.7)/t** (C.39) ใช้ได้กรณีศูนย์ failure ลู่เข้าหา MLE เมื่อ n มาก ระวังว่าใช้กับ failure mode เดียวหรือ total rate
- **Cycles แทนเวลา** (cl. C.3.4, p.219-220): เมื่อจำนวนครั้งใช้งานเป็นตัวขับ (เช่น connector ต่อ/ถอดบ่อย) ใช้สูตรเดิมแต่แทน t ด้วยจำนวน cycle/demand; แปลงกลับเป็นเวลาที่ระดับ system: **MTTF = MCTF/ξ** (ξ = cycles ต่อหน่วยเวลา) (C.40) class เดียวอาจใช้ time model กับ mechanism หนึ่ง (corrosion) และ cycle model กับอีก mechanism (wear) ตัวอย่าง valve "fail to open on demand": อาจเกิด **due to demand** (wear จากเปิดบ่อย) หรือ **on demand** (corrode ในตำแหน่งปิดแล้วเพิ่งเจอ) failure mode และ detection method เหมือนกัน ต่างกันที่ mechanism เท่านั้น drilling, well completion/intervention, crane, loading arm, winch, mixer, valve มักขึ้นกับ demand มากกว่าเวลา

## C.4 Maintainability (p.220-223)

- M(t) = P(RT ≤ t) (C.41) เป็น CDF ของเวลาซ่อม; repair rate μ คงที่ → M(t) = 1 - exp(-μt) (C.42, C.44); **μ̂ = n/ΣRTi = 1/MRT** (C.43) RT จะใช้ทั้ง down time, บางส่วน หรือเฉพาะ active time ขึ้นกับวัตถุประสงค์; ถ้าเวลาซ่อมไม่ exponential (เช่น log-normal) ต้อง fit จากเวลาซ่อมแต่ละครั้ง (p.221-222) (หมายเหตุ: ประโยคใน C.4.2.2 เขียนเหมือน μ "designated MTTRes" ซึ่งหละหลวม ความหมายที่ถูกคือ μ = 1/MRT หรือ 1/MTTRes)
- **MRT = ΣRTi / n** (C.45) = ส่วนของ MDT ที่เป็นการซ่อมเอง (p.222)
- **Intrinsic maintainability** = ลักษณะที่ออกแบบมาในตัวเครื่อง (ถอดง่าย หล่อลื่น) ไม่เปลี่ยนตาม site; **extrinsic** = logistics, support, การจัดงาน, isolation/de-isolation เปลี่ยนตาม site ต้องแยกโมเดล (cl. C.4.3, p.222)

## C.5 "Mean time" (p.223-225)

- mean ใช้ได้ดีเมื่อข้อมูลน้อยหรือไม่มี trend ถ้ามี trend (wear-out หรือ run-in) mean ทำให้ตัดสินใจผิดได้ (cl. C.5.1, p.223)
- **MDT** รวมทุก delay ตั้งแต่เสียจนกลับมาทำงาน (detection, อะไหล่, logistics, standby, policy, active time, reinstatement) ไม่ intrinsic (cl. C.5.2, p.223)
- **METBF = MUT + MDT** (C.46) กรณีง่าย = MTTF + MTTRes (C.47) ขึ้นกับบริบท (cl. C.5.3, p.223-224) (ISO ใช้ชื่อ METBF ใน Annex C ไม่ใช่ MTBF)
- **MTTF = 1/λ** (C.48) ใช้ได้เฉพาะ λ คงที่; โดยเคร่งครัด MTTF หมายถึงการเสีย **ครั้งแรก** ของของใหม่; เท่ากับ MUT เฉพาะเมื่อซ่อมแล้ว as-good-as-new (C.5.4, C.5.6, p.224-225) สูตร C.46-C.48 สมมติ exponential
- **MRT = 1/μ** (C.49) โดยทั่วไปหมายถึง active corrective time แต่อาจขยายถึง down time ทั้งหมด (จึงเรียก "restoration" แทน "repair") ดู ISO/TR 12489 สำหรับ MTTR, MTTRes, MRT, MART (cl. C.5.5, p.224)
- **MTTM** รวม corrective + preventive: ค่าเฉลี่ยถ่วงด้วยจำนวนงาน (C.50) (p.225) ตามที่พิมพ์ tmc, tmp ถูกนิยามเป็นเวลา "รวม" แต่สูตรคูณด้วยจำนวนงานอีก ดูไม่สอดคล้องเชิงมิติ เจตนาน่าจะเป็นค่าเฉลี่ยถ่วงของ mean corrective time กับ mean PM time

## C.6 Hidden failures ใน safety system (p.225-227)

- สองแนวทางตั้ง test interval: **required availability** (ตามเกณฑ์ risk สัมบูรณ์ IEC 61508/61511) และ **cost-benefit** (ผลเป็นแค่เงิน ISO 15663) ต้องเก็บข้อมูลทั้ง failure ก่อน test (hidden จริง) และ failure ที่เกิดเพราะ test (cycle failure, human error, unavailability ระหว่าง test) (cl. C.6.1, p.225)
- **Required availability**: τ = 2·LPFD/λ (C.51) สมมติ test ไม่ก่อความเสียหาย (γ = 0) และ MRT ไม่มีนัย; ทั่วไป PFDavg ≈ λτ/2 + λ/μ + γ/(μτ) (C.52, อ่านจาก text ที่ extract เพี้ยน); τopt = √(2γ/(λμ)) (C.53) (cl. C.6.2, p.225-226)
- **Cost-benefit** (ตัวอย่าง vibration trip ของปั๊ม, ถือเป็น SIL 1 ไม่มีข้อกำหนดสัมบูรณ์): E(CT) ≈ ½·f·λfto·τ·Cf + Cm/τ (C.54); **τ* = √(2Cm/(Cf·λfto·f))** (C.55) f = ความถี่เหตุที่ต้องเรียกระบบ, Cf = ส่วนต่างความเสียหายเมื่อระบบทำงาน/ไม่ทำงาน, Cm = ต้นทุนต่อ test ควรคิดต้นทุน shutdown เมื่อ test เจอ failure และ spurious trip ด้วย (cl. C.6.3, p.226-227)
- Uncertainty: ระบุ/วัดความไม่แน่นอน (distribution, SD, prediction interval), sensitivity analysis, ISO/TR 12489 Annex O (cl. C.6.4, p.227); human error เป็นสาเหตุแฝงได้เสมอ (cl. C.7, p.227-228)

## Annex D Data requirements (p.229-237)

- **Table D.1** ประเภทการวิเคราะห์: Safety A1 QRA, A2 RBI, A3 SIL, A4 ESIA; LCC/optimisation/maintenance B1 LCC, B2 PA (production availability, ISO 20815), B3 AA, B4 RCM (IEC 60300-3-11, NORSOK Z-008, SAE JA1011/1012), B5 SPA, B6 FMECA, B7 SDA, B8 STR, B9 RCA (IEC 62740); General C1 MRP, C2 Six Sigma (partly), C3 FTA, C4 Markov, C5 Petri net (cl. D.1, p.229-230)
- Tables D.2-D.4 มาจาก GAP analysis: 1 = ปกติต้องมี, 2 = optional; แถวที่ไม่ shade คือ parameter ที่อาจเพิ่มในฉบับหน้า derived parameters (failure rate, CI, PFD, repair rate, CCF rate, test efficiency = สัดส่วน failure ที่ test พบ) คำนวณ ไม่บันทึกตรง (cl. D.3, p.230)
- ตัวอย่างที่ควรจำ (อ่านจากตาราง p.231-234):
  - **RCM (B4)**: ข้อมูลอุปกรณ์ทุกตัว (location, class, installation, manufacturer, design, surveillance + operating period, จำนวน demand, operating mode) = 1; failure: equipment unit, subunit, MI, failure mode, impact on function, mechanism, cause, impact on plant = 1 (detection method, failure date = 2); maintenance: category, activity, down time, active time, man-hours = 1
  - **SDA (B7)** และ STR, RCA: **failure date = 1** ตาราง D.3 ระบุว่าจำเป็นต่อ lifetime analysis (TTT-plot, Weibull) ไม่ควรทิ้ง
  - **AA/PA (B2-B3)**: down time, active maintenance time, man-hours = 1; failure mode, impact = 1
  - **SPA (B5)**: spare part, lead time, repair workshop cycle time (KPI 27 ใน Annex E) = 1
  - **FTA/Markov (C3-C4)**: failure rate, CCF rate, PFD, repair rate, test efficiency, test interval = 1; **SIL (A3)**: number of demands, CCF rate, failure cause = 1
- **Table D.5 แหล่งข้อมูล** (cl. D.5, p.235-237): generic (database, handbook เช่น OREDA, หรือ handbook จาก expert judgement), operator/company specific, manufacturer, expert judgement, human error data
  - generic ใช้ช่วงต้นโครงการ ช่วงหลังควรใช้ข้อมูล specific ที่มีเอกสารดี; ข้อมูล installation เดียวมักความเชื่อมั่นต่ำ ยกเว้นประชากรมาก (เช่น F&G detector)
  - **ข้อมูลผู้ผลิตมัก failure rate ต่ำเกินจริง** เพราะตัด failure จาก environment, mal-operation, installation, maintenance error และ feedback หลังหมดประกันน้อย
  - event ใน CMMS **ไม่ใช่ reliability data โดยตรง** แต่ใช้สร้าง KPI ได้
  - expert ควรประมาณเป็นจำนวน event ที่สังเกตได้ใน fleet/ช่วงเวลา แทนตัวเลข 1e-6/h; อุตสาหกรรมให้ความสำคัญกับคุณภาพ input data น้อยเกินไป (ISO 20815 Annex E)

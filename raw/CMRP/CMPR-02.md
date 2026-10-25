# CMPR-02: Wear mechanisms, lubrication, PdM techniques, criticality/risk และ FMEA/FMECA

Source: PETROSYNC CMRP training course slides, file CMPR-02.pdf (scanned, OCR). Reading notes ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ PDF page `(CMRP CMPR-02 p.N)`

ขอบเขต: PDF p.1-52 (หน้าพิมพ์ 55-106, 2 slides ต่อหน้า PDF) OCR อ่านข้อความพิมพ์ได้ดี แต่ตาราง (synthetic lubricant p.10, grease p.15, MOM p.27, RPN p.33, PFMEA p.41) และลายมือ (p.1, p.27, p.29) อ่านเพี้ยน ตรวจจากภาพแล้ว 10 หน้า (p.1, 10, 13, 14, 17, 30, 32, 33, 35, 41 + zoom ตาราง p.41) เนื้อหาจริงกว้างกว่าที่คาด: ครึ่งหลังเป็น criticality, risk matrix, LCC และ FMEA/FMECA ไม่ใช่ condition monitoring ล้วน

## 1. ประเภทของ wear (p.1-7)

ภาพรวม 6 แบบ พร้อมการเคลื่อนที่ที่เกิดและสาเหตุหลัก (CMRP CMPR-02 p.1-2):

| Wear | เกิดระหว่าง | สาเหตุหลัก | วิธีควบคุมตาม slide |
|---|---|---|---|
| Abrasive (cutting, gouging, scratching) | sliding, rolling | อนุภาคแข็งปนเปื้อน, ผิวหยาบ | น้ำมันสะอาด, oil film หนาขึ้น, ลด load, เลิกสภาวะกระแทก, เปลี่ยนวัสดุ |
| Adhesive (galling, seizure, scuffing, smearing) | sliding, rolling | asperity สัมผัสกันจน cold weld | film หนาขึ้นหรือใช้ EP/AW ที่เหมาะ, ลด load, ผิวเรียบขึ้น |
| Erosion-Cavitation | ไม่ใช่ระหว่างผิวสองผิว (NA) | อนุภาคความเร็วสูง, flow ไม่พอ, อากาศ/น้ำ | กำจัดอนุภาค, เปลี่ยนมุมกระทบ, คุม air entrainment/ความชื้น/foam |
| Fretting (false brinelling) | การสั่นขณะเครื่องหยุดนิ่ง | fit หลวม, ความชื้น | fit แน่นขึ้น, grease ที่เหมาะ (slide ยกตัวอย่าง SKF LGBB 2), ล็อก bearing ระหว่างขนส่ง |
| Contact fatigue (pitting, spalling) | rolling | การรับ-ปลด load เป็นรอบ, ความเค้นใต้ผิว | ลด overload, กันรอยบุ๋ม (indentation) ที่เป็นจุดรวมความเค้น |
| Corrosive (rust, chemical, oxidative) | NA | น้ำ/สารเคมี/กรด, สารเติมแต่งกันสนิมหมด | วัสดุทนกัดกร่อน, ลดอุณหภูมิ, ไล่น้ำ/ผลิตภัณฑ์ออกซิเดชัน |

ประเด็นสำคัญ:
- Abrasive และ adhesive ทำนายได้ด้วย **Archard's equation** (p.1, p.4) slide ไม่ได้แสดงสูตร [ความรู้ทั่วไป: V = K·F·s/H คือปริมาตรที่สึกแปรตาม load F และระยะเลื่อน s และแปรผกผันกับความแข็ง H; K = wear coefficient] จึงเป็นเหตุผลที่ "ลด load" ช่วยได้
- Abrasive แบ่งเป็น two-body (asperity ของผิวหยาบ/โลหะแข็งขูดโลหะอ่อน เมื่อ film บางเกิน) และ three-body (อนุภาคปนเปื้อนขนาดใกล้เคียงความหนา film ลอดผ่านแล้วขูดผิว) slide ระบุว่า abrasive เกิดในเกือบทุกเครื่อง (p.3-4)
- Adhesive เกิดเมื่อ film แตก, EP/AW ไม่พอ, ความเร็วผิวต่ำ ตัวอย่าง piston, gear, sliding bearing, rolling bearing (p.4-5)
- Erosion มี 3 แบบ: solid particle (เช่น ใบพัด helicopter ในฝุ่น), liquid drop (ใบ compressor ที่มีความชื้น), cavitation (การยุบตัวของฟองไอ เช่น ใบจักรเรือ) เกิดที่ outlet/valve/nozzle ความเร็วสูง และ pump inlet/plain bearing (cavitation) (p.5-6)
- Fretting: การแกว่งแอมพลิจูดเล็กสร้างเศษละเอียดที่ออกซิไดซ์ แล้วลดอายุ fatigue ตัวอย่างคลาสสิกคือรถที่ขนส่งทางรถไฟ (p.6)
- Contact fatigue: slide ระบุว่าการหล่อลื่นมีผลน้อย ยกเว้นการคุม contamination (p.7)
- [handwritten] p.1 มีโน้ตว่า fretting นำไปสู่ "Fatigue" และ corrosive wear มีทั้งแบบ "chemical, electrical"
- เหตุผลที่ต้องรู้ mechanism: เพื่อเลือก action ให้ถูก ได้แก่ เทคโนโลยีหล่อลื่น, เปลี่ยนวัสดุ, ลด load, เลิกแรงกระแทก, ความสะอาดน้ำมัน (p.2)

**ข้อสังเกต/ข้อผิดพลาดที่น่าสงสัยใน slide**
- p.4 ระบุ adhesive wear ว่า "primarily rolling" ทั้งที่ adhesive (galling/scuffing) ปกติเป็นปรากฏการณ์ของ sliding เป็นหลัก ดูเหมือนคัดลอกบรรทัดจาก slide fatigue มา (p.7 ก็เขียน "primarily rolling" ซ้ำกับ corrosive wear ซึ่งตาราง p.1 บอกว่า NA)
- p.5 "ความแข็งของวัสดุไม่ช่วย" สำหรับ erosion เป็นการสรุปกว้างเกิน [ความรู้ทั่วไป: สำหรับ solid particle erosion ความแข็งช่วยในบางมุมกระทบ ส่วนโลหะเหนียวสัมพันธ์กับความแข็งไม่ชัด]
- p.7 "lubrication มีผลน้อยต่อ fatigue" ขัดกับความรู้ทั่วไปเรื่อง bearing life (ISO 281 ใช้ viscosity ratio kappa ปรับอายุอย่างมาก) ควรอ่านว่า "เมื่อ film เพียงพอแล้ว ตัวแปรสำคัญที่เหลือคือ contamination"

## 2. น้ำมันหล่อลื่น (p.8-12, p.16)

- รายการทดสอบน้ำมันมาตรฐาน (p.8, ซ้ำที่ p.16): viscosity, VI, specific/API gravity, flash/fire point, pour/cloud point, oxidation stability, foam/air release, AN/BN, filterability, AW/EP, demulsibility, rust & copper corrosion; มุมมอง oil analysis 4 ด้าน: viscosity, inclusions, contamination, additive depletion
- Base oil groups (p.8-9): **Group I** mineral มีโมเลกุลหลากขนาดและโครงสร้าง มี sulfur/wax/nitrogen/aromatics เหลือ; **Group II/III** ผ่าน hydrocracking โมเลกุลสม่ำเสมอขึ้น (III ถูกปรับรูปโมเลกุล เรียกกึ่ง synthetic) แทบไม่มีสิ่งเจือปน; **Group IV/V** synthetic สร้างโมเลกุลจากต้น สม่ำเสมอที่สุด คาดการณ์คุณสมบัติได้
- ตาราง synthetic (p.10, จากภาพ): mineral oil ได้ Best ด้านราคา/corrosion/hydrolytic/additive solubility แต่แย่ด้าน viscosity range และ temperature range; PAO เด่นเกือบทุกด้านแต่ additive solubility และ biodegradability แย่; ester (diester, polyol) hydrolytic stability แย่; กลุ่มพิเศษ (phosphate ester, PAG, silicone, polyphenyl ester, fluorocarbon) ราคาแพง
- Polarity ของสารเติมแต่ง (p.10): mineral oil ไม่มีขั้ว จึงต้องพึ่ง additive ที่มีขั้ว 3 กลไก: particle enveloping (detergent, dispersant, metal deactivator), metal wetting (rust/corrosion inhibitor, AW, EP), water emulsifying (emulsifier)
- Additive แบ่งเป็น surface active (AW, EP, friction modifier, tackifier, R&O, metal deactivator) และ bulk oil active (biocide, foam inhibitor, demulsifier, dispersant, anti-oxidant, detergent, VI improver, pour point depressant ฯลฯ) (p.11)
- ภาพตัวอย่าง wear particle: fatigue spall, sliding wear, cutting wear, sand/silica, iron oxide (p.11)
- การเก็บตัวอย่าง (p.12): เก็บจากจุดที่ flow เป็น turbulent ผ่าน sampling valve; อ้าง ISO 4021:1992 (hydraulic fluid power, การดึงตัวอย่างจากสายที่ทำงาน); การเก็บจาก reservoir ใช้ weighted plug และต้องระวังเป็นพิเศษ

## 3. จาระบี (p.12-16)

- องค์ประกอบ (p.13): base oil 70-95% + additives + thickener 5-30% + กระบวนการผลิต เปรียบ thickener เป็นฟองน้ำที่อุ้มน้ำมัน
- จาระบีจำแนกตามชนิด thickener: lithium, calcium, polyurea, PTFE (p.14)
- **NLGI grade** วัดด้วย cone penetration ASTM D217 (หน่วย 0.1 มม.): 000 = 445-475, 00 = 400-430, 0 = 355-385, 1 = 310-340, 2 = 265-295, 3 = 220-250, 4 = 175-205, 5 = 130-160, 6 = 85-115 ตัวเลขยิ่งสูงยิ่งแข็ง ภาพชี้ว่างาน bearing ใช้ราว grade 1-3 (p.14)
- ส่วนแบ่งการใช้ (p.15, NLGI): lithium ราว 56%, calcium 24% ที่เหลือเป็นชนิดอื่น ตาราง p.15 เปรียบ dropping point/อุณหภูมิใช้งานสูงสุด เช่น complex greases และ polyurea dropping point 260°C+ ใช้งานได้ถึงราว 177°C ส่วน calcium ธรรมดา dropping point ราว 96-104°C
- รายการทดสอบจาระบี (p.12, p.16): consistency/penetration, dropping point, base oil viscosity, mechanical stability, water washout, corrosion (SKF EMCOR), copper corrosion, oil separation, oxidation, EP/AW, fretting, pumpability

**ข้อสังเกต:** p.13 ให้ additives 5-30% ซึ่งสูงกว่าที่พบทั่วไป [ความรู้ทั่วไป: additive ในจาระบีมักไม่เกินราว 10%]; ช่วงทั้งสามรวมกันไม่สอดคล้อง (ถ้า base oil 95% ส่วนที่เหลือไม่พอให้ thickener ขั้นต่ำ 5% + additive ขั้นต่ำ 5%)

## 4. เทคนิค Predictive / Condition Monitoring (p.17-27)

### Thermography (p.17-21)
- **Kirchhoff's rule: ε + ρ + τ = 1** (emissivity + reflectance + transmittance) วัตถุทึบแสง τ ≈ 0 ดังนั้นผิวที่ ε ต่ำจะสะท้อนมาก อ่านค่าผิด (p.17)
- ระยะวัดขึ้นกับ 3 ตัวแปร: FOV, IFOVgeo (วัตถุเล็กสุดที่มองเห็น), IFOVmeas (จุดวัดเล็กสุดที่วัดค่าได้) (p.18)
- ปัจจัยวัตถุ (วัสดุ/emissivity, สี, ผิว) และสภาพแวดล้อม (อุณหภูมิแวดล้อม, รังสี, อากาศ, ลม, แสง) (p.18-19)
- การใช้งาน: ไฟฟ้า HV/LV (จุดต่อหลวม/กัดกร่อน, fuse, breaker), มอเตอร์/bearing ร้อน, steam trap, ฉนวนท่อ, refractory/เตา/ปล่อง, อาคาร, process (p.19-21)

### Electric Motor Current Testing (p.22-23)
- กระแสที่มอเตอร์ดึงให้ spectrum คล้าย vibration ใช้วิเคราะห์ส่วนภายใน (winding, rotor bar) โดยไม่ต้องรื้อ ทั้ง online และ offline
- ตรวจได้: power quality, ฉนวน (turn-turn, phase-phase, ground wall), วงจร (short/open, phase unbalance), rotor (broken/cracked bar, eccentricity), mechanical (bearing, misalignment, unbalance, belt, gear mesh), VFD (IGBT, tuning)
- ตัวอย่าง spectrum blower motor 65 kW 2,965 rpm แสดง sideband รอบ fundamental ใกล้ 56-58 Hz (p.23; ตัวเลขอ่านจาก OCR ไม่ชัด)

### Ultrasonic testing (p.24-26)
- ใช้คลื่นเสียงความถี่ราว 0.5-15 MHz; สองหลัก: pulse-echo (สะท้อน, นิยมกว่า, ต้องเข้าถึงด้านเดียว) และ through-transmission
- งานภาคสนาม: ตรวจรั่ว (รวม electrical), ความเสียหายภายใน (contact), วัดความหนาผนังท่อ (erosion/scaling), weld integrity
- ข้อดี: จับได้ทั้งผิวและใต้ผิว, ทะลุลึก, ผลทันที, ปลอดภัย, พกพาได้; ข้อจำกัด: ต้องมี couplant, ต้องใช้ทักษะสูง, วัสดุหยาบ/บาง/ไม่สม่ำเสมอหรือ cast iron ตรวจยาก, รอยแตกที่ขนานกับลำคลื่นอาจหลุด, ต้องมี reference standard
- หมายเหตุ: slide ปน UT แบบ NDT (MHz) กับ airborne ultrasound สำหรับตรวจรั่ว (ปกติราว 20-100 kHz) [ความรู้ทั่วไป] ไม่ได้แยกช่วงความถี่ให้ชัด

### Maintenance Optimization Matrix (MOM) (p.27)
- ตารางแถว = asset type/class (Mechanical: motors, gearboxes, pumps, compressors, couplings, belts, chains; Electrical: panels, cables, junction boxes; Static: piping, boilers, vessels, heat exchangers; Instrument: sensors, transmitters, gauges) คอลัมน์ = เทคนิค PdM (vibration, thermography, temperature, oil analysis, lubricant check, ultrasonic, motor current, visual, leak) และ process parameter (flow, pressure, temperature) พร้อมความถี่ (daily ถึง annually หรือ N/A)
- ตัวอย่าง (อ่านจาก OCR ซึ่งเรียงคอลัมน์ไม่แน่นอน): motors ตรวจ vibration รายเดือน, thermography รายไตรมาส, visual รายวัน, motor current ราวครึ่งปี

## 5. Criticality และ Risk (p.28-33)

- อุปกรณ์ critical เมื่อผลของ failure มีนัยสำคัญ ทนไม่ได้ ไม่มี redundancy หรือผลนั้นครอบงำปัจจัยอื่น slide ตั้งคำถามว่าควรให้เครดิต redundancy หรือไม่ (ตัวอย่าง level indicator 3 ตัวซ้ำกัน) (p.28)
- ขั้นตอน (p.29): ไล่ทุก functional failure หา component ที่เป็นเหตุ, ระบุ failure mode เด่นและผลสำคัญ, ใช้ criticality matrix ตัดสิน; ถ้าทนผลไม่ได้ = critical, ทนได้ = non-critical, บันทึกเหตุผลใน Remarks
- ตาราง importance 3 ระดับ (High/Moderate/Low) 6 มิติ: availability (ชั่วโมงที่เครื่องไม่พร้อม X/Y), production rate, quality, safety (recordable/near miss), environment (permit violation/on-site release), cost (หน่วย Kronor, ค่าเปลี่ยนหรือซ่อมถ้า RTF) (p.30)
- **Risk = Probability x Effect** โดย probability เป็นความถี่ เช่น 1/ปี (p.31) effect = ผลปลายทางของเหตุการณ์ ภายใต้ "realistic scenario" ที่ตกลงกันในกลุ่ม แยก 4 หมวด availability/safety/environment/cost (p.32)
- Risk matrix 5x5 (p.32): effect 1-5 (no, negligible, marginal, critical, catastrophic) x probability 1-5 (1/25 ปี, 1/10 ปี, 1/5 ปี, 1/ปี, 1/เดือน) ค่าเซลล์ = ผลคูณ; สีโดยประมาณ Low 1-3, Medium 4-9, High 10-25
- Policy (p.33): Low = ไม่ทำ preventive; Medium/High = ทำ preventive โดยต่างกันที่ระดับ เช่น การสำรองอะไหล่
- **RPN = Severity x Occurrence x Detection** (p.33) ตารางตัวอย่าง 15 กรณีที่ได้ **RPN = 360 เท่ากันทั้งหมด** (เช่น 10x9x4, 9x10x4, 4x9x10) ตรวจคูณครบ 15 แถวแล้วถูกต้อง สื่อว่า RPN เท่ากันแต่ลักษณะความเสี่ยงต่างกันมาก
- ระดับ RPN (p.33): None 0, Low 8-40, Medium 80-240, High 320-1,000

**ข้อผิดพลาด/ไม่สอดคล้อง**
- p.30 ตาราง availability: High = "96", Medium = "96-98", Low = "above 98" ระดับ High ควรเป็น "ต่ำกว่า 96" ขอบเขต 96 ซ้ำกันสองระดับ
- p.32 แถว "No effects" ที่ probability 1/ปี และ 1/เดือน (ค่า 4, 5) ถูกระบายเป็น Medium ทั้งที่ไม่มีผลกระทบ ขัดกับนิยาม Risk = P x Effect ในเชิงความหมาย
- p.33 ช่วง RPN มีช่องว่าง (41-79, 241-319 ไม่ถูกจัดระดับ) และ "None = 0" เป็นไปไม่ได้เพราะ S, O, D ต่ำสุดคือ 1 (RPN ต่ำสุด = 1); ช่วงเหล่านี้ดูเหมือนมาจากสเกลอื่น (2x2x2 = 8 ฯลฯ)
- p.31-33 ใช้คำว่า criticality กับ risk/RPN สลับกัน (หัวข้อมีเครื่องหมายคำถาม "criticality?") ไม่ได้นิยามแยก

## 6. Asset management และ LCC (p.34-36)

- Asset lifecycle (p.34): เมื่ออายุ/การใช้งานเพิ่ม condition ลด ค่าบำรุงรักษาประจำเพิ่ม มี mid-life overhaul และสุดท้าย renewal ต้องชั่ง risk, condition, cost
- **Optimizing maintenance intervals** (p.35): direct cost ลดเมื่อเว้นช่วงห่างขึ้น ส่วน risk cost เพิ่ม total business impact เป็นเส้นโค้งต่ำสุดที่ "economic optimum" (ในกราฟราว 4 สัปดาห์) ซ้ายของจุดนี้คือจ่ายเกินเพื่อเป้า reliability ขวาคือจ่ายเกินเพื่อเป้าต้นทุน (ข้อสังเกต: แกน x เขียนว่า "frequency (weeks)" แต่ความหมายจริงคือ interval)
- LCC 5 กลุ่ม (p.35): capital (design, purchase, installation, commissioning, training, documentation, facilities), operational (labor, energy, water, raw materials, feedstock), maintenance (labor, materials, spares, workshop, contractors, overhead), production & quality losses (non-availability, malfunction), disposal (cost of disposal ลบ residual value)
- Total organizational risk (p.36): **Risk = Threats x Vulnerabilities x Impact** แบ่งเป็น process hazard & safety (HAZID, SIL), physical integrity (RBM, CMS), operational (CMMS, PMO), people/skills/change (skill assessment, MOC); และ **Composite Risk Index (CRI) = Impact x Probability x Detectability**

## 7. FMEA (p.36-47)

- FMEA วิเคราะห์ failure mode ที่อาจเกิดจากประสบการณ์ของผลิตภัณฑ์/กระบวนการที่คล้ายกัน ให้ทีม RCM ออกแบบตัด failure ออกด้วยค่าใช้จ่ายน้อย (p.37)
- ประเภท (p.38-41): **Concept FMEA** (ระดับ system/subsystem ก่อนมี hardware, ช่วยเลือก concept และตัดสินเรื่อง redundancy), **Design FMEA** (ระดับ system/sub-system/component ก่อนส่งผลิต; ประโยชน์ 10 ข้อ เช่น จัดลำดับ failure mode ตามผลต่อลูกค้า, ช่วยวางแผนทดสอบ), **Process FMEA** (ข้อบกพร่องจากการผลิต/ประกอบ, ระบุตัวแปรกระบวนการที่ต้องควบคุม, ความปลอดภัยผู้ปฏิบัติงาน)
- แนวทาง 2 แบบ (p.42): **Functional FMEA** = top-down/deductive ใช้ช่วงออกแบบต้นเมื่อยังไม่รู้ชิ้นส่วน; **Hardware FMEA** = bottom-up/inductive เริ่มจาก component ขึ้นไป ใช้เมื่อแบบนิ่งแล้ว
- ขั้นตอน 10 ขั้น (p.43): review process, brainstorm failure modes, list effects, จัด Severity, Occurrence, Detection, คำนวณ RPN, ทำ action plan, ลงมือ, คำนวณ RPN ใหม่
- สเกล 1-10 (p.43-46): Severity 10 = อันตรายโดยไม่มีเตือน, 9 = อันตรายมีเตือน, 8 = สูญเสียหน้าที่หลัก ... 1 = ไม่มีผล; S 9-10 ควรแก้แบบ (ตัด failure mode หรือป้องกันผู้ใช้); Occurrence 10 = 1 ใน 2 หรือมากกว่า, 9 = 1/3, 8 = 1/8, 7 = 1/20, 6 = 1/80, 5 = 1/400, 4 = 1/2,000, 3 = 1/15,000, 2 = 1/150,000, 1 = น้อยกว่า 1/1,500,000; Detection 10 = design control ตรวจไม่ได้เลย ... 1 = ตรวจพบแน่นอน
- RPN สูงสุด 10x10x10 = 1,000; ถ้า occurrence = 1 จะเหลือ 100 (p.47 ถูกต้อง) slide เตือนว่า RPN เป็นเกณฑ์ threshold ไม่ใช่ตัวตัดสิน ต้องใช้วิจารณญาณเมื่อ RPN สูงแต่ severity ต่ำ (p.46) หลังแก้ไขต้องคำนวณ RPN ใหม่ (p.47)
- ตัวอย่าง PFMEA (p.41) งานพ่น wax ในประตูรถ ตรวจตัวเลขแล้ว:
  - แถว 1: 7x8x5 = 280 ถูก; หลังแก้ แสดง S7 O2 D6 แต่ RPN = 70 (7x2x6 = 84; ถ้า D = 5 จึงได้ 70) **ไม่ตรง**
  - แถว 2: 7x5x3 = 105 ถูก; หลังแก้ 7x1x3 = 21 ถูก
  - แถว 3: 7x2x2 = 28 ถูก
  - แถว 4: 7x8x7 = **392 แต่ slide เขียน 382**; หลังแก้ 7x1x7 = **49 แต่ slide เขียน 40** ผิดทั้งสองค่า
- p.41 ซ้ำเนื้อหา p.40 (ข้อ 7-13 คือข้อ 1-6 ซ้ำอีกรอบ) เป็นความผิดพลาดของการจัดหน้า

## 8. FMECA (p.47-52)

- **FMECA = FMEA + Criticality Analysis (CA)** จัด probability ของ failure mode เทียบ severity เพื่อทุ่มทรัพยากรไปที่ความเสี่ยงสูง ต้องมีข้อมูล failure สำหรับส่วน criticality (p.47-48)
- ขั้นตอน 15 ขั้น (p.48): นิยามระบบ, ground rules, block diagram, หา failure mode, วิเคราะห์ผล/สาเหตุ, จัด severity, คำนวณ criticality, จัดลำดับ, หา critical items, หาวิธีตรวจจับ/ชดเชย, จัดทำเอกสาร, ข้อเสนอแนะ, ติดตามผล (มี feedback เข้า design สองครั้ง)
- FMECA เป็นจุดตั้งต้นของ maintenance planning, logistics support, repair level analysis, system safety, test planning, production planning (p.49)
- MIL-STD-1629A มี 2 แบบ (p.50-51):
  - **Qualitative**: ไม่มี failure rate ใช้ระดับ probability A Frequent, B Reasonably probable, C Occasional, D Remote, E Extremely unlikely แล้ววางบน criticality matrix (severity แกนนอน x occurrence แกนตั้ง)
  - **Quantitative**: **Mode Criticality = Item Unreliability x Mode Ratio x Probability of Loss** และ **Item Criticality = ผลรวม Mode Criticality** ของทุกโหมด
- Severity category (p.52): แบบย่อ I Catastrophic (เสียชีวิต/สูญเสียระบบ), II Critical, III Marginal, IV Negligible (เลขน้อย = รุนแรงกว่า); แบบละเอียด 1-10 สำหรับ facility (9-10 = ประเด็น HSE, 10 คือไม่มีเตือน)

**ไม่สอดคล้อง:** p.49 บอกว่ามี "3 วิธี" ทำ FMECA แต่แสดงเพียง 2 (criticality indices, failure probability) และบอกว่า criticality index ได้จากการ **บวก** severity กับ probability ขณะที่ risk matrix p.32 และ RPN ใช้การ **คูณ**; p.50 นิยาม criticality ว่าเป็น "ความถี่ของการเกิดผล" ซึ่งแคบกว่าการใช้งานจริงในหน้าอื่น (ที่รวม severity)

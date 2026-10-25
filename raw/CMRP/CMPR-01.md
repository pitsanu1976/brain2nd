# CMPR-01: Course structure, AEO Model, Inspection Theory, Lubrication และ Vibration พื้นฐาน

Source: PETROSYNC CMRP training course slides, file CMPR-01.pdf (scanned, OCR). Reading notes ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ PDF page `(CMRP CMPR-01 p.N)`

ขอบเขต: PDF p.1-50 (หนึ่งหน้า PDF = 2 slide, เลข slide ที่พิมพ์ท้ายหน้าคือ 5-54) OCR อ่านข้อความ bullet ได้ดี แต่แผนภาพ (AEO Model, P-F curve, failure pattern, ตาราง ISO 10816) ต้องดูจากภาพ (render p.1, 2, 4, 15, 28, 29, 41, 42) ลายมือส่วนใหญ่อ่านไม่ออก มีที่อ่านได้ชัด 1 จุด (p.4) เนื้อหาจริงของไฟล์นี้เน้น inspection, lubrication และ vibration มากกว่าเรื่อง business goals ตามที่คาดไว้

## 1. Course structure และ AEO Model (CMRP CMPR-01 p.1)

AEO Model (ของผู้สอน OEE "operational excellence experts") เป็นผัง 4 ชั้นเรียงจากบนลงล่าง มีลูกศรป้อนกลับจากล่างขึ้นบน:

| ชั้น | กล่องหลักในชั้น |
|---|---|
| Maintenance Strategy | Maintenance Strategy Project (รับ input จาก Business Goals), Reliability Issues (Design), Pre-Defined Priorities, Plant Asset Management and Maintenance Program (Living Program) แบ่งเป็น PM / PRM / ODR / RTF และมี RCFA กำกับข้าง |
| Work Identification | PRM/ODR Collection and Analysis -> Information Integration and Decision -> Work Order Generation; Corrective Maintenance รับจาก Operators/Initiators |
| Work Control | Planning (รับ Standard Job Plans and Procedures และ Spare Parts Alignment) -> Rolling Schedule |
| Work Execution | Work Execution -> Post Maintenance Testing -> Update Program (วนกลับไป Maintenance Strategy) |

คำย่อในโมเดล (p.1):
- PM = Preventive Maintenance แบบ time based
- PRM = Proactive Reliability Maintenance (รวม predictive และ corrective)
- ODR = Operator Driven Reliability (จากการสังเกตของ operator) — OCR อ่านเป็น "OOR/QDR"
- RTF = Run to Failure (reactive)
- RCFA = Root Cause Failure Analysis

ข้อสังเกต: โมเดลนี้มองโปรแกรมบำรุงรักษาเป็น "living program" ที่ปรับจากผล Post Maintenance Testing และ Update Program จุดเด่นคือแยก ODR ออกเป็นสายงานแยกจาก PM/PRM

## 2. CMRP Body of Knowledge (p.2-3)

SMRP BOK 5 pillar ตามที่ slide แสดง (ชื่อหัวข้อย่อสรุป):

1. Business and Management: ตั้งทิศทางและแผนกลยุทธ์ M&R, บริหารแผน, วัดผล, บริหารแผนองค์กร, สื่อสารผู้มีส่วนได้ส่วนเสีย, บริหารความเสี่ยง EHS (1.1-1.6)
2. Manufacturing Process Reliability: เข้าใจกระบวนการ, ใช้เทคนิคปรับปรุงกระบวนการ, บริหารผลของการเปลี่ยนแปลง (MOC), คุมให้ตรงมาตรฐาน/กฎหมาย (2.1-2.4)
3. Equipment Reliability: กำหนดความคาดหวัง reliability, ประเมินและหาโอกาสปรับปรุง, แผนสำหรับเครื่องเดิมและเครื่องใหม่, cost-justify, ลงมือ, ทบทวนและปรับกลยุทธ์ (3.1-3.7)
4. Organization & Leadership: วิเคราะห์ขีดความสามารถองค์กร, โครงสร้าง, พัฒนาคน, นำและบริหารคน
5. Work Management: ระบุ/อนุมัติงาน, จัดลำดับ, plan, schedule, execute, document, วิเคราะห์และ follow-up, วัดผล work management, บริหารโครงการ, ใช้ IT, บริหารทรัพยากรและวัสดุ (5.1-5.11)

ข้อผิดพลาดใน slide: pillar 4 เริ่มที่ 4.2 ไม่มีข้อ 4.1 (ยืนยันจากภาพ p.2) ตาม SMRP BOK ฉบับทั่วไปข้อ 4.1 คือการกำหนดความต้องการขององค์กร (general knowledge, ไม่อยู่ใน slide)

## 3. Definitions and Terminology (p.3)

รายการคำย่อ: CM, AMO (Asset Management Optimization), CMMS, FMECA, ISO, IEC, MMS, MS (Maintenance Strategy), MSR (Maintenance Strategy Review), MTBF, MTFR (Mean Time for Response), MTTR, MTTF, OEM, P&ID, PFD, PdM, PM, PRM, QA/QC, RCM

ข้อสังเกต: "RM" ถูกนิยามซ้ำสองความหมาย (Reactive Maintenance และ Reliability and Maintenance) และ MS, MSR, PdM ซ้ำสองครั้ง เป็นความไม่เป็นระเบียบของ slide ควรระบุบริบทเมื่อใช้ RM

## 4. Concepts: Availability, Reliability, Maintainability (p.4)

| ค่า | สูตรตาม slide | หมายเหตุ |
|---|---|---|
| Availability | Uptime / Total time | [handwritten] เขียนเพิ่ม MTBF / (MTBF + MTTR) |
| Reliability | R(t) = e^(-λt), λ = 1/MTBF = failure rate | สมมติ failure rate คงที่ (exponential) |
| Maintainability | M = 1/MTTR = repair rate (μ) | สูตร M(t) ใน slide พิมพ์เพี้ยนเป็น "lne^(1-μt)" |

ข้อผิดพลาดใน slide: สูตร maintainability ที่ถูกต้องคือ M(t) = 1 - e^(-μt) โดย μ = 1/MTTR (สอดคล้องกับ wiki [[Reliability Metrics]]) slide วางเลข 1 และเครื่องหมายผิดตำแหน่ง และตั้งชื่อ "A" ซ้ำกับ Availability (น่าจะหมายถึง λ ที่ OCR/ฟอนต์แสดงผิด)

ต่อด้วยวงจร Basic Maintenance Management Process 6 ขั้น (p.4): Work Identification -> Plan Work -> Schedule Work -> Execute Work -> Record History -> Analyze for Improvement แล้ววนกลับ

## 5. ทางเลือกกิจกรรม condition monitoring (p.5)

เทคนิคที่แสดง: Vibration Analysis, Thermography, Oil Analysis, Current & Voltage Monitoring, Noise Analysis, Acoustic Emission Analysis

## 6. Inspection Theory: 4 boundaries ของเครื่องจักร (p.5-11)

หลักการ: การตรวจคือการยืนยันว่า "ขอบเขต" 4 ด้านของเครื่องยังสมบูรณ์ ต้องรู้ทั้ง (A) ธรรมชาติของแต่ละขอบเขต และ (B) วิธีตัดสินสภาพ fitness for service (p.6)

1. Mechanical Integrity
2. Electrical Soundness
3. Fluid Quality and Level (lubricant, coolant ฯลฯ)
4. Operational Parameters

### 6.1 Visual Inspection (p.7)
- VI ของ rotating machinery เป็นเรื่อง subjective ทำ procedure กลางครอบคลุมทุกกรณียาก ใช้สามัญสำนึกเป็นหลักและเรียนรู้เร็วจากประสบการณ์
- บางงานต้องใช้เครื่องมือ เช่น strobe light; ขอบเขตของ slide คือ VI ที่ไม่ต้องหยุดเครื่อง

### 6.2 Mechanical Integrity (p.7-9)
3 หัวข้อ: Mechanical Soundness, Mounting/Machine Base/Foundation, Power Transmission and Alignment
- Soundness: ดูสภาพภายนอก (สนิม สกปรก รอยร้าว รั่ว), dust cover/inspection cover/coupling guard หลวมหรือหาย, น้ำมันรั่วหรือ seal เสีย, อุณหภูมิสูงผิดปกติ
- Mounting: bolt หลวม/เสื่อม, foundation ร้าว, base ร้าวหรือหลวม (ภาพตัวอย่าง baseplate bolt หายและมีช่องว่าง 12 mm ระหว่าง base กับเสารับ)
- Power transmission 3 แบบ: coupling, chain, belt

### 6.3 Electrical Soundness (p.9-11)
ตรวจพื้นฐานด้วย multimeter 4 อย่าง:
- Voltage: ต้องอยู่ในช่วงที่กำหนดทุก phase ความไม่สม่ำเสมอทำให้ fuse ขาดหรือขดลวดร้อนจนไหม้
- Current: แอมป์สูงบ่งชี้ปัญหา เช่น misalignment, overload
- Earth (grounding): สายดินเสีย/ขาดทำให้ทำงานเป็นช่วง ๆ, ขดลวด driver ร้อนไหม้, ลัดวงจร
- Phase regularity (3 phase): มุมระหว่างเฟสควรเป็น 120 องศา ถ้าไม่สมดุลทำให้สั่นสะเทือนมาก

## 7. Lubrication และการตรวจของไหล (p.12-27)

### 7.1 หัวข้อที่ตรวจ (p.12)
- Lubricant: viscosity, inclusions, composition, charring
- Coolant: level, temperature, quality
- Other fluids: ตามชนิดและหน้าที่

### 7.2 หลักการหล่อลื่น (p.12-14)
- Lubrication ลดแรงเสียดทานโดยใส่วัสดุคั่นระหว่างผิวที่เคลื่อนที่สัมพัทธ์ สารหล่อลื่นเป็นได้ทั้ง liquid (oil), semi-solid (grease), solid (graphite), gas (air, helium)
- กลไก: ฟิล์มหนาประมาณ 0.1-30 µm แยก asperity ของสองผิวออกจากกัน shear stress ไปเกิดในฟิล์มแทนผิวโลหะ แรงเสียดทานในฟิล์มขึ้นกับ viscosity และชนิดน้ำมัน (เปรียบกับสำรับไพ่ที่รับแรงกดได้แต่เลื่อนได้ง่าย)
- Viscosity = ความต้านทานการไหล; dynamic viscosity = shear stress / shear rate; viscosity ลดลงเมื่ออุณหภูมิเพิ่ม (วัดที่ 40 และ 100 °C)

### 7.3 Composition และหน้าที่ (p.15)
- Lubricant = Base oil (70-95%) + Additives (5-30%) + Thickener สำหรับ grease (5-30%) additive ตัวอย่าง: antioxidant, rust inhibitor, EP/anti-wear
- หมายเหตุ: ช่วง % เป็นช่วงกว้างที่ซ้อนกันได้ ไม่ใช่สัดส่วนที่รวมกันได้ 100% เสมอ
- หน้าที่นอกจากลด friction/wear: ระบายความร้อน, กันสนิม, คุมสิ่งปนเปื้อน, ส่งกำลังไฮดรอลิก

### 7.4 Contamination และ varnish (p.16-17)
- ชนิดอนุภาค (ภาพจาก Pall, กำลังขยาย 100x): silica (ฝุ่น/ทราย จากภายนอก), bright metal (wear จากภายใน เร่งการสึกต่อ), black metal (ferrous oxide), rust (ระบบที่มีน้ำ), fibers (ผ้า/กระดาษ), cake of fines (silt หนาแน่นจนประเมินไม่ได้)
- Varnish: คราบบางแข็งไม่ละลายในน้ำมัน (อ้างนิยาม ASTM D02.C01) มีหลายรูป เช่น lacquer, sludge, คราบบนพื้น/เพดาน reservoir กลไก 4 ขั้น: oxidation -> polymerisation -> agglomeration -> precipitation (เกิดที่จุดเย็น ไหลช้า clearance ต่ำ)

### 7.5 ประเภทการวิเคราะห์น้ำมัน (p.18)
| ประเภท | ให้ข้อมูล |
|---|---|
| Wear Particle Analysis | กลไกการสึก ขนาด/ความเข้มข้นของ ferrous และลักษณะอนุภาค |
| Particle Count | จำนวนต่อ 100 ml แยกช่วงขนาด 5-10, 10-25, 25-50, 50-100, >100 µm |
| Spectrochemical & Physical | คุณภาพน้ำมัน, wear metal และ additive เป็น ppm |

การทดสอบน้ำมันในห้องแล็บที่พบบ่อย: viscosity, VI, specific/API gravity, flash/fire point, pour/cloud point, oxidation stability, foam, AN/BN, filterability, AW/EP, demulsibility, rust & copper corrosion
การทดสอบ grease: consistency/penetration (NLGI), dropping point, base oil viscosity, mechanical stability, water washout, corrosion, oil separation, oxidation, EP/AW, pumpability ฯลฯ (p.21)

### 7.6 Field tests (p.19-24)
- Viscosity: manual viscometer / pocket viscosity comparator (แนะนำรุ่น calibrate ที่ 40 °C) เทียบน้ำมันใหม่กับน้ำมันใช้งาน
- Patch test: ตรวจอนุภาค/เส้นใย/wear particle ขนาดใหญ่
- Crackle test: ให้ความร้อนตัวอย่างถึงประมาณ 100 °C ถ้ามีเสียงแตกปะทุแสดงว่ามีน้ำ; sedimentation test ตั้งทิ้ง 30 นาทีแล้ววัดปริมาณน้ำที่แยกตัว
- Grease field test: consistency (bleed test), inclusions
- Process parameters ที่ตรวจ: speed, flow, pressure, temperature (p.23)
- ชุดเครื่องมือ: grease test kit, patch/crackle kit, multimeter, non-contact IR thermometer, stroboscope (p.23-24)

### 7.7 Base oil และ API classification (p.50)
- สัดส่วนตลาดตาม slide: mineral 90%, synthetic 9%, vegetable 1%
- API Group I: saturates <90% และ/หรือ sulfur >0.03%, VI 80-119 (solvent refined); II: >90%, <0.03%, VI 80-119 (hydroprocessed); III: >90%, <0.03%, VI มากกว่า 120 (hydrocracked); IV: PAO; V: synthetic อื่น
- หมายเหตุ: นิยาม API มาตรฐานใช้ VI ≥ 120 สำหรับ Group III และ ≥ 90% saturates (general knowledge) slide เขียน >120 / >90% ซึ่งทิ้งค่าขอบไว้

## 8. การพัฒนาโปรแกรมตรวจภาคสนาม (p.24-27)
- องค์ประกอบ: route, activities, full boundary inspection และผูกกับ maintenance strategy ของแต่ละเครื่อง
- Asset Information Page (AIP) 3 ส่วน: Asset identification (รหัส ทิศทางติดตั้ง criticality ต่อ process High/Medium/Low, duty cycle, shutdown criticality rating ด้าน safety/quality/environment ให้คะแนน 1-10, เชื่อมกับ CMMS, route), Technical data (driver/gearbox/driven unit, bearing DE/NDE, จำนวนฟันเฟือง, rotor bar, ระบบหล่อลื่นและความถี่เก็บตัวอย่าง), Required inspection (checklist VI ประมาณ 26 ข้อ และ Safety Inspection รอบเครื่องประมาณ 40 ข้อ)

## 9. Condition Monitoring Theory (p.28-30)

นิยาม: ตรวจสุขภาพเครื่องโดยไม่หยุดการใช้งาน (p.28)

### 9.1 Failure patterns (p.28)
Bathtub 3 ช่วง: infant failures, random (externally caused), wear-out ตามด้วยกราฟ 4 รูปแบบพร้อมสัดส่วน: Wear-out 2%, Bathtub 4%, Random 26%, Infant mortality 68% (รวม 100%)
- ข้อสังเกต: เป็นการยุบ 6 pattern ของ Nowlan & Heap (A bathtub 4%, B wear-out 2%, C 5%, D 7%, E random 14%, F infant 68%; general knowledge) โดยรวม C+D+E = 26% เป็น "Random" slide ไม่ได้บอกว่ายุบ และไม่ได้อ้างแหล่ง
- ข้อความสำคัญโดยนัย: มีแค่ราว 6% ที่มีช่วง wear-out ชัด จึงอธิบายว่า time-based PM ใช้ได้กับ failure ส่วนน้อย

### 9.2 P-F curve (p.29)
- เส้นสภาพเครื่องเทียบเวลา: จุด P = เริ่มตรวจพบความผิดปกติ (potential failure), จุด F = functional failure (ทำหน้าที่ตามที่คาดหวังไม่ได้) ช่วง P-F คือ lead time
- ภาพ "P-F curve explained" (Dustin Etchison 2015) ขยายเป็นเส้น D-I-P-F: D = original design (D for R, D for M), I = installation, I-P interval = ช่วงของ precision maintenance (laser alignment, thermal growth, pipe strain), P-F interval ไล่ลำดับอาการ ultrasonic -> vibration -> oil analysis -> audible noise -> hot to touch (thermography) -> mechanically loose -> ancillary damage -> catastrophic failure
- จับคู่กลยุทธ์กับช่วง: precision maintenance (ก่อน P), CBM/predictive (ต้น P-F), preventive (กลาง), corrective/run-to-failure (ใกล้ F)
- มีเส้นความปลอดภัยคู่: งานนอกแผนยิ่งใกล้ F ยิ่งเพิ่มโอกาสบาดเจ็บ (unsafe act -> near miss -> minor -> severe injury -> fatality)
- กราฟต้นทุน: ประมาณ 70% ของต้นทุน M&R ถูกกำหนดตั้งแต่ design; ช่วงต้นต้นทุนต่ำ (planned outage) ใกล้ F มี OEE losses และต้นทุนสูง

### 9.3 4 ขั้นของ condition detection (p.30)
Detection (เก็บข้อมูลตาม route เทียบ alarm limit) -> Analysis (ยืนยันปัญหาและหา root cause ด้วย waveform, spectrum, phase, run-up/coast-down) -> Correction -> Verification (ตรวจหลังซ่อม เก็บ baseline ใหม่และตั้ง alarm ใหม่)
- ข้อผิดพลาดใน slide: ข้อความใต้ "Correction" คัดลอกซ้ำจาก "Analysis" ทั้งย่อหน้า ไม่มีคำอธิบายขั้น Correction จริง

เทคนิค CM/NDT ที่สรุป: vibration, oil analysis, thermography, motor current testing, ultrasonic (p.30)

## 10. Vibration พื้นฐาน (p.31-49)

- Physics: ระบบมวล-สปริง การเคลื่อนที่ 1 รอบ = 1 cycle; หลัก Newton: ไม่มีแรงก็ไม่มีการเคลื่อนที่ เครื่องที่ประกอบแม่นยำสร้างแรงต่ำจึงสั่นต่ำ (p.31-32)
- แหล่งแรง 2 แบบ: internal (unbalance, misalignment, pumping force, bearing) และ external (ส่งผ่านฐาน ท่อ อากาศ จากเครื่องอื่น) (p.32)
- แรง 3 ประเภท: periodic (unbalance, misalignment, vane pass), impact/impulse (bearing fault, ชิ้นส่วนหลวม), random (cavitation, flow, bearing เสียหนัก) (p.33-34)
- Sinusoidal motion, frequency และ period (period = 1/frequency), peak, peak-to-peak (p.34-38)
- ชนิดการวัด: displacement (ระยะ, mils หรือ µm), velocity (อัตราเปลี่ยนระยะ, in/s หรือ mm/s), acceleration (อัตราเปลี่ยนความเร็ว, g หรือ in/s² / mm/s²) กราฟ log-log แสดงว่าแต่ละชนิดเหมาะกับช่วงความถี่ต่างกัน (p.39-40)
- Scale factor: เทียบค่า overall ได้ต่อเมื่อวัดช่วงความถี่เดียวกันและ scale เดียวกัน (RMS, Peak, Peak-to-peak) (p.41)

### 10.1 Upper vibration limits (p.41)
| หน่วย | ค่าสูงสุด |
|---|---|
| mils pk-pk | 3.5 |
| µm pk-pk | 90 |
| in/s peak | 0.3 |
| mm/s peak | 5.0 |
| g | 5.0 |

ข้อผิดพลาดใน slide: 3.5 mils = 88.9 µm สอดคล้องกับ 90 µm แต่ 0.3 in/s = 7.6 mm/s ไม่ใช่ 5.0 mm/s (5.0 mm/s = 0.2 in/s) ค่า velocity สองหน่วยจึงไม่เท่ากัน ควรใช้ตัวเลขนี้อย่างระวัง

### 10.2 ISO 10816-1 (p.42)
ตาราง velocity severity (mm/s RMS กับ in/s peak) 4 class: I เครื่องเล็ก, II เครื่องกลาง, III เครื่องใหญ่ฐานแข็ง, IV เครื่องใหญ่ฐานอ่อน แต่ละ class แบ่ง Good / Satisfactory / Unsatisfactory (Alert) / Unacceptable (Danger) ขอบเขต Class I ประมาณ 0.71 / 1.8 / 4.5 mm/s และเลื่อนขึ้นหนึ่งขั้นต่อ class (II: 1.12/2.8/7.1, III: 1.8/4.5/11.2, IV: 2.8/7.1/18)
- ตรวจเลข: แปลง RMS เป็น peak (x1.414) แล้วเป็น in/s ตรงกับคอลัมน์ in/s เช่น 4.5 mm/s RMS -> 0.25 in/s pk ถูกต้อง
- หมายเหตุ (general knowledge): ISO 10816-1 ถูกแทนที่ด้วย ISO 20816-1 แล้ว

### 10.3 Spectrum analysis และ diagnosis (p.42-49)
- Spectrum ระบุแหล่งที่มาได้ดีกว่าดูแค่ amplitude; หลายแหล่งไม่ได้อยู่ที่ running speed (เป็น multiple หรือไม่สัมพันธ์กับรอบ) (p.43)
- Frequency บอกแหล่งปัญหา/ความถี่ที่เกิดซ้ำ, amplitude บอกความรุนแรง, phase บอกว่าเครื่องเคลื่อนที่อย่างไร (p.45-46)
- ผู้สอนให้น้ำหนัก: รู้ความถี่และแหล่งเป็น 1/3 ของงานวิเคราะห์ อีก 2/3 คือรู้ประวัติเครื่อง (p.44)
- Unbalance: peak เดียวที่ 1x running speed แทบไม่มีอย่างอื่น; Misalignment: peak ที่ 1x และ multiple (2x, 3x) (p.45-46)
- Phase: amplitude + frequency ให้ความแม่นประมาณ 80% เพิ่ม phase แล้วเกิน 95% (ตัวเลขของผู้สอน ไม่มีแหล่งอ้าง) ใช้ in-phase / out-of-phase แยก unbalance กับ misalignment (p.47-49)
- Oil analysis มอง 2 ด้าน: degradation และ contamination ของ lubricant (p.49)

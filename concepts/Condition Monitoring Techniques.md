---
title: Condition Monitoring Techniques
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [cmrp, cbm, vibration, lubrication, pm, maintenance-reliability]
sources: [cmrp.md]
confidence: medium
contested: false
---

# Condition Monitoring Techniques

Condition monitoring (CM) คือการตรวจสุขภาพเครื่องโดยไม่หยุดการใช้งาน (CMRP CMPR-01 p.28) หน้านี้รวมเทคนิคและแนวทางภาคสนามจาก [[CMRP Course]]: การตรวจตาม 4 boundaries, Asset Information Page, vibration, thermography, motor current testing, ultrasonic, Maintenance Optimization Matrix และลำดับอาการบนเส้น D-I-P-F ส่วนทฤษฎีจุด P/F และการตั้งคาบตรวจอยู่ที่ [[P-F Interval and Condition Monitoring]] และ oil analysis อยู่ที่ [[Lubrication and Oil Analysis]]

เทคนิคที่ slide กล่าวถึง: vibration analysis, thermography, oil analysis, current & voltage monitoring, noise analysis, acoustic emission, motor current testing, ultrasonic (CMRP CMPR-01 p.5, p.30)

## Inspection theory: 4 boundaries ของเครื่อง (CMRP CMPR-01 p.5-11)

การตรวจคือการยืนยันว่าขอบเขต 4 ด้านของเครื่องยังสมบูรณ์ ผู้ตรวจต้องรู้ทั้งธรรมชาติของแต่ละขอบเขตและเกณฑ์ตัดสิน fitness for service

| Boundary | สิ่งที่ตรวจ |
|---|---|
| 1 Mechanical Integrity | soundness (สนิม รอยร้าว รั่ว cover/guard หาย ร้อนผิดปกติ), mounting/base/foundation (bolt หลวม ฐานร้าว), power transmission และ alignment (coupling, chain, belt) |
| 2 Electrical Soundness | voltage ทุก phase, current (แอมป์สูงบ่งชี้ misalignment/overload), earth/grounding, phase regularity 120 องศา (ไม่สมดุลทำให้สั่นมาก) |
| 3 Fluid Quality and Level | lubricant (viscosity, inclusions, composition, charring), coolant (level, temperature, quality) ดู [[Lubrication and Oil Analysis]] |
| 4 Operational Parameters | speed, flow, pressure, temperature |

- Visual inspection ของ rotating machinery เป็นเรื่อง subjective เขียน procedure กลางยาก อาศัยประสบการณ์ บางงานใช้เครื่องมือเช่น stroboscope (p.7)
- ชุดเครื่องมือภาคสนาม: multimeter, IR thermometer, stroboscope, grease kit, patch/crackle kit (p.23-24)

## Asset Information Page (AIP) และโปรแกรมตรวจ (CMRP CMPR-01 p.24-27)

โปรแกรมตรวจภาคสนามประกอบด้วย route, activities, full boundary inspection และผูกกับ maintenance strategy ของแต่ละเครื่อง AIP มี 3 ส่วน:
1. **Asset identification**: รหัส, criticality ต่อ process (High/Medium/Low), duty cycle, shutdown criticality ด้าน safety/quality/environment (คะแนน 1-10), ลิงก์ [[CMMS]], route
2. **Technical data**: driver/gearbox/driven, bearing DE/NDE, จำนวนฟันเฟือง, rotor bar, ระบบหล่อลื่นและความถี่เก็บตัวอย่าง (ข้อมูลที่ต้องใช้คำนวณความถี่ fault ใน spectrum)
3. **Required inspection**: checklist VI ราว 26 ข้อ และ safety inspection รอบเครื่องราว 40 ข้อ

## 4 ขั้นของ condition detection (CMRP CMPR-01 p.30)

Detection (เก็บข้อมูลตาม route เทียบ alarm limit) -> Analysis (ยืนยันและหา root cause ด้วย waveform, spectrum, phase, run-up/coast-down) -> Correction -> Verification (ตรวจหลังซ่อม เก็บ baseline ใหม่ ตั้ง alarm ใหม่) หมายเหตุ: ข้อความใต้ Correction ใน slide คัดลอกซ้ำจาก Analysis

## Vibration analysis (CMRP CMPR-01 p.31-49)

### พื้นฐาน
- ไม่มีแรงก็ไม่มีการสั่น เครื่องที่ประกอบแม่นยำสร้างแรงต่ำ แหล่งแรง internal (unbalance, misalignment, pumping, bearing) และ external (ผ่านฐาน ท่อ เครื่องข้างเคียง) (p.31-32)
- ชนิดแรง: periodic (unbalance, misalignment, vane pass), impact (bearing fault, ชิ้นส่วนหลวม), random (cavitation, flow, bearing เสียหนัก) (p.33-34)
- period = 1 / frequency; ค่า peak, peak-to-peak, RMS (p.34-38)

### หน่วยวัด (p.39-41)

| Parameter | หน่วย | เหมาะกับ |
|---|---|---|
| Displacement | mils หรือ µm (pk-pk) | ความถี่ต่ำ |
| Velocity | in/s หรือ mm/s | ช่วงกลาง (ใช้กับ severity ทั่วไป) |
| Acceleration | g หรือ mm/s² | ความถี่สูง |

เทียบค่า overall ได้ต่อเมื่อวัดช่วงความถี่เดียวกันและ scale เดียวกัน (RMS, peak, pk-pk) (p.41) การจับคู่ชนิดกับช่วงความถี่ในตารางสรุปจากกราฟ log-log ของ slide

### Upper vibration limits ของ slide และข้อผิดพลาด (p.41)

| หน่วย | ค่าสูงสุดตาม slide | ตรวจเลข |
|---|---|---|
| mils pk-pk | 3.5 | = 88.9 µm สอดคล้องกับ 90 µm |
| µm pk-pk | 90 | |
| in/s peak | 0.3 | = 7.6 mm/s |
| mm/s peak | 5.0 | = 0.20 in/s |
| g | 5.0 | |

**Flag**: ค่า velocity สองหน่วยไม่เท่ากัน (0.3 in/s คือ 7.6 mm/s ไม่ใช่ 5.0 mm/s) ใช้ตัวเลขชุดนี้อย่างระวังและระบุหน่วยเสมอ เป็นข้อผิดพลาดของ slide ไม่ใช่ contested

### ISO 10816-1 velocity severity (p.42)

ขอบเขต mm/s RMS ระหว่างโซน Good / Satisfactory / Unsatisfactory (Alert) / Unacceptable (Danger):

| Class | เครื่อง | G/S | S/U | U/Unacceptable |
|---|---|---|---|---|
| I | เล็ก | 0.71 | 1.8 | 4.5 |
| II | กลาง | 1.12 | 2.8 | 7.1 |
| III | ใหญ่ ฐานแข็ง | 1.8 | 4.5 | 11.2 |
| IV | ใหญ่ ฐานอ่อน | 2.8 | 7.1 | 18 |

- คอลัมน์ in/s peak ของ slide ตรวจแล้วสอดคล้อง (RMS x 1.414 แล้วแปลงหน่วย เช่น 4.5 mm/s RMS -> 0.25 in/s pk) ตารางนี้ถูก ต่างจากตาราง limit p.41 ข้างบน
- ISO 10816-1 ถูกแทนที่ด้วย ISO 20816-1 แล้ว (general knowledge, confidence low)

### Spectrum และ phase (p.42-49)
- Frequency บอกแหล่ง, amplitude บอกความรุนแรง, phase บอกลักษณะการเคลื่อนที่
- **Unbalance**: peak เด่นที่ 1x running speed แทบไม่มีอย่างอื่น; **Misalignment**: peak ที่ 1x พร้อม 2x, 3x
- เพิ่ม phase ทำให้แยก unbalance (in-phase) กับ misalignment (out-of-phase ข้าม coupling) ได้ ผู้สอนอ้างความแม่นราว 80% เมื่อใช้ amplitude + frequency และเกิน 95% เมื่อเพิ่ม phase (ไม่มีแหล่งอ้าง)
- ผู้สอนให้น้ำหนัก: รู้ความถี่/แหล่งเป็น 1/3 ของงาน อีก 2/3 คือรู้ประวัติเครื่อง

## Thermography (CMRP CMPR-02 p.17-21)

- **Kirchhoff's rule: ε + ρ + τ = 1** (emissivity + reflectance + transmittance) วัตถุทึบ τ ≈ 0 ผิวที่ ε ต่ำ (โลหะมันวาว) จึงสะท้อนมากและอ่านอุณหภูมิผิด
- ระยะวัดขึ้นกับ FOV, IFOVgeo (วัตถุเล็กสุดที่มองเห็น), IFOVmeas (จุดเล็กสุดที่วัดค่าได้)
- ปัจจัยรบกวน: วัสดุ/สี/ผิวของวัตถุ, อุณหภูมิแวดล้อม, รังสีสะท้อน, ลม, แสง
- งานที่ใช้: จุดต่อไฟฟ้าหลวม/กัดกร่อน, fuse/breaker, มอเตอร์และ bearing ร้อน, steam trap, ฉนวนท่อ, refractory, process

## Electric Motor Current Testing (CMRP CMPR-02 p.22-23)

กระแสมอเตอร์ให้ spectrum คล้าย vibration วิเคราะห์ส่วนภายในโดยไม่รื้อ ทำได้ทั้ง online/offline ตรวจ power quality, ฉนวน (turn-turn, phase-phase, ground wall), วงจร (short/open, phase unbalance), rotor (broken bar, eccentricity), ปัญหากล (bearing, misalignment, unbalance, belt, gear mesh) และ VFD

## Ultrasonic (CMRP CMPR-02 p.24-26)

- UT แบบ NDT ใช้คลื่นราว 0.5-15 MHz แบบ pulse-echo (นิยม เข้าถึงด้านเดียว) หรือ through-transmission ใช้วัดความหนาผนัง (erosion/scaling) และ weld integrity
- งานภาคสนาม: ตรวจรั่ว (รวมไฟฟ้า), ความเสียหายภายในแบบ contact
- ข้อจำกัด: ต้องมี couplant, ทักษะสูง, วัสดุหยาบ/บาง/cast iron ยาก, รอยแตกขนานลำคลื่นอาจหลุด, ต้องมี reference standard
- slide ปน UT แบบ MHz กับ airborne ultrasound สำหรับตรวจรั่ว (ปกติราว 20-100 kHz; general knowledge) ไม่ได้แยกช่วงความถี่

## Maintenance Optimization Matrix (MOM) (CMRP CMPR-02 p.27)

ตาราง แถว = asset class (Mechanical: motor, gearbox, pump, compressor, coupling, belt, chain; Electrical: panel, cable, junction box; Static: piping, vessel, boiler, heat exchanger; Instrument: sensor, transmitter, gauge) x คอลัมน์ = เทคนิค (vibration, thermography, temperature, oil analysis, lubricant check, ultrasonic, motor current, visual, leak) และ process parameter พร้อมความถี่ daily ถึง annually หรือ N/A ตัวอย่างอ่านจาก OCR (เรียงคอลัมน์ไม่แน่นอน): motor ตรวจ vibration รายเดือน, thermography รายไตรมาส, visual รายวัน, motor current ราวครึ่งปี

## D-I-P-F curve และลำดับอาการ (CMRP CMPR-01 p.29)

เส้น D-I-P-F (ภาพของ Dustin Etchison 2015 ใน slide) ขยาย P-F เดิมไปทางซ้าย: D = design (design for reliability/maintainability), I = installation, ช่วง I-P = precision maintenance (laser alignment, thermal growth, pipe strain) ลำดับอาการบนช่วง P-F จากเร็วไปช้า:

ultrasonic -> vibration -> oil analysis -> audible noise -> hot to touch (thermography) -> mechanically loose -> ancillary damage -> catastrophic failure

นัยสำหรับการเลือกเทคนิค: เทคนิคต้นลำดับให้ lead time ยาวกว่า รายละเอียดเชิงทฤษฎีและการตั้งคาบดู [[P-F Interval and Condition Monitoring]]

## เชื่อมโยงกับ compressor failure hierarchy

การตีความ ไม่ใช่ข้อมูลใน CMRP:
- VIB (vibration) และ NOI ใน [[Failure Mode]] ตรวจด้วย vibration/ultrasonic; [[OHE Overheating]] ตรวจด้วย thermography; [[PDE Parameter Deviation]] ตรงกับ boundary 4 Operational Parameters
- motor current testing ใช้กับ driver ของ [[Compressor]] (นอก boundary ของ compressor ใน ISO 14224 แต่กระทบ availability)
- ISO 14224 บันทึกวิธีที่พบ failure ใน [[Failure Detection Method]] การเลือกเทคนิคตามหน้านี้ทำให้สัดส่วน failure ที่พบจาก "condition monitoring" เพิ่มขึ้น

## ดูเพิ่ม

- [[P-F Interval and Condition Monitoring]]
- [[Lubrication and Oil Analysis]]
- [[Wear Mechanisms]]
- [[PM Task Selection]]
- [[Criticality Assessment]]

## Triplets

- [[Condition Monitoring Techniques]] [is_a:: Condition Monitoring] health check without stopping operation (CMRP CMPR-01 p.28)
- [[Condition Monitoring Techniques]] [related_to:: [[P-F Interval and Condition Monitoring]]]
- Machine Inspection [has_part:: Mechanical Integrity] boundary 1 (CMRP CMPR-01 p.6)
- Machine Inspection [has_part:: Electrical Soundness] boundary 2 (CMRP CMPR-01 p.6)
- Machine Inspection [has_part:: Fluid Quality And Level] boundary 3 (CMRP CMPR-01 p.6)
- Machine Inspection [has_part:: Operational Parameters] boundary 4 (CMRP CMPR-01 p.6)
- Electrical Soundness [uses:: Multimeter] voltage, current, earth, phase regularity 120 degrees (CMRP CMPR-01 p.9-11)
- Asset Information Page [has_part:: Asset Identification] criticality H/M/L, shutdown criticality 1-10 (CMRP CMPR-01 p.24-27)
- Asset Information Page [has_part:: Technical Data] bearings, gear teeth, rotor bars, sampling frequency (CMRP CMPR-01 p.24-27)
- Asset Information Page [has_part:: Required Inspection] VI checklist about 26 items, safety about 40 items (CMRP CMPR-01 p.24-27)
- Asset Information Page [uses:: [[CMMS]]] (CMRP CMPR-01 p.24-27)
- Detection [step_of:: Condition Detection Process] 1 of 4 (CMRP CMPR-01 p.30)
- Analysis [step_of:: Condition Detection Process] 2 of 4 (CMRP CMPR-01 p.30)
- Correction [step_of:: Condition Detection Process] 3 of 4, slide text duplicated from Analysis (CMRP CMPR-01 p.30)
- Verification [step_of:: Condition Detection Process] 4 of 4, new baseline and alarms (CMRP CMPR-01 p.30)
- Vibration Analysis [is_a:: Condition Monitoring] (CMRP CMPR-01 p.31-49)
- Vibration Displacement [has_value:: mils or µm] low frequency (CMRP CMPR-01 p.39-40)
- Vibration Velocity [has_value:: in/s or mm/s] mid frequency (CMRP CMPR-01 p.39-40)
- Vibration Acceleration [has_value:: g] high frequency (CMRP CMPR-01 p.39-40)
- Vibration Upper Limit [has_value:: 3.5 mils pk-pk = 90 µm pk-pk] consistent (CMRP CMPR-01 p.41)
- Vibration Upper Limit [has_value:: 0.3 in/s peak = 7.6 mm/s peak] correct conversion; derived (CMRP CMPR-01 p.41)
- CMRP Velocity Limit 5.0 mm/s Equals 0.3 in/s [contradicts:: 0.3 in/s Equals 7.6 mm/s] slide unit error; 5.0 mm/s = 0.20 in/s (CMRP CMPR-01 p.41)
- ISO 10816-1 [has_value:: Class I 0.71 / 1.8 / 4.5 mm/s RMS] zone boundaries G/S, S/U, U/Unacceptable (CMRP CMPR-01 p.42)
- ISO 10816-1 [has_value:: Class II 1.12 / 2.8 / 7.1 mm/s RMS] (CMRP CMPR-01 p.42)
- ISO 10816-1 [has_value:: Class III 1.8 / 4.5 / 11.2 mm/s RMS] large, rigid foundation (CMRP CMPR-01 p.42)
- ISO 10816-1 [has_value:: Class IV 2.8 / 7.1 / 18 mm/s RMS] large, soft foundation (CMRP CMPR-01 p.42)
- ISO 20816-1 [related_to:: ISO 10816-1] supersedes ISO 10816-1, general knowledge [confidence:: low]
- Unbalance [detected_by:: Vibration Analysis] single peak at 1x running speed (CMRP CMPR-01 p.45-46)
- Misalignment [detected_by:: Vibration Analysis] peaks at 1x plus 2x, 3x (CMRP CMPR-01 p.45-46)
- Vibration Analysis [uses:: Phase] separates unbalance (in-phase) from misalignment (out-of-phase); instructor claims over 95% accuracy, unsourced (CMRP CMPR-01 p.47-49)
- Thermography [is_a:: Condition Monitoring] (CMRP CMPR-02 p.17-21)
- Kirchhoff's Rule [has_formula:: ε + ρ + τ = 1] emissivity + reflectance + transmittance (CMRP CMPR-02 p.17)
- Thermography [depends_on:: Emissivity] low ε surfaces reflect and read wrong (CMRP CMPR-02 p.17)
- Thermography [has_parameter:: IFOVmeas] also FOV, IFOVgeo (CMRP CMPR-02 p.18)
- Electric Motor Current Testing [is_a:: Condition Monitoring] online and offline (CMRP CMPR-02 p.22-23)
- Broken Rotor Bar [detected_by:: Electric Motor Current Testing] also insulation, eccentricity, bearing, misalignment, VFD (CMRP CMPR-02 p.22)
- Ultrasonic Testing [is_a:: Condition Monitoring] 0.5-15 MHz, pulse-echo or through-transmission (CMRP CMPR-02 p.24-26)
- Wall Thinning [detected_by:: Ultrasonic Testing] erosion/scaling thickness measurement (CMRP CMPR-02 p.24-26)
- Maintenance Optimization Matrix [uses:: Asset Class Versus Technique] with frequency daily to annually (CMRP CMPR-02 p.27)
- Maintenance Optimization Matrix [selects:: Condition Monitoring Frequency] e.g. motors vibration monthly, read from OCR (CMRP CMPR-02 p.27) [confidence:: low]
- D-I-P-F Curve [has_part:: I-P Interval] precision maintenance: laser alignment, thermal growth, pipe strain (CMRP CMPR-01 p.29)
- D-I-P-F Curve [has_value:: ultrasonic, vibration, oil analysis, audible noise, hot to touch, mechanically loose, ancillary damage, catastrophic failure] symptom order earliest to latest (CMRP CMPR-01 p.29)
- [[Wear Mechanisms]] [detected_by:: Vibration Analysis] interpretation
- VIB [detected_by:: Vibration Analysis] interpretation [confidence:: low]
- [[OHE Overheating]] [detected_by:: Thermography] interpretation [confidence:: low]
- [[PDE Parameter Deviation]] [detected_by:: Operational Parameters] boundary 4, interpretation [confidence:: low]
- [[Condition Monitoring Techniques]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-01 p.5-49; CMPR-02 p.17-27)

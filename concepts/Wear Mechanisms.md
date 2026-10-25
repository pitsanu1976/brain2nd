---
title: Wear Mechanisms
created: 2026-10-25
updated: 2026-10-25
type: concept
tags: [cmrp, failure-mechanism, lubrication, iso-14224, reliability, maintenance-reliability]
sources: [cmrp.md, iso-14224.md, compressor-failure-hierarchy.md]
confidence: medium
contested: false
---

# Wear Mechanisms

กลไกการสึก (wear mechanism) คือกระบวนการทางกายภาพ/เคมีที่ทำให้ผิววัสดุเสียเนื้อหรือเสียรูปจนชิ้นส่วนทำหน้าที่ไม่ได้ หลักสูตร [[CMRP Course]] แบ่งเป็น 6 แบบ (แยก cavitation ออกจาก erosion ได้เป็น 7) และเน้นว่าต้องรู้ mechanism ก่อนจึงเลือก action ได้ถูก เช่น เปลี่ยนเทคโนโลยีหล่อลื่น เปลี่ยนวัสดุ ลด load เลิกแรงกระแทก หรือคุมความสะอาดน้ำมัน (CMRP CMPR-02 p.1-2)

หน้านี้เป็นรายละเอียดเชิง tribology ของหมวด **2 Material failure** ใน [[Failure Mechanism]] (ISO 14224 Table B.2) และเชื่อมกับการหล่อลื่นใน [[Lubrication and Oil Analysis]]

## ตารางกลไก 7 แบบ (CMRP CMPR-02 p.1-7)

| Wear | ชื่อเรียกอื่น/อาการ | เกิดระหว่าง | สาเหตุหลัก | วิธีควบคุมตาม slide |
|---|---|---|---|---|
| Abrasive | cutting, gouging, scratching | sliding, rolling | อนุภาคแข็งปนเปื้อน, ผิวหยาบ | น้ำมันสะอาด, film หนาขึ้น, ลด load, เลิกแรงกระแทก, เปลี่ยนวัสดุ |
| Adhesive | galling, seizure, scuffing, smearing | sliding (ดูข้อ flag) | asperity สัมผัสกันจน cold weld เมื่อ film แตก | film หนาขึ้น/ใช้ EP-AW ที่เหมาะ, ลด load, ผิวเรียบขึ้น |
| Erosion | solid particle, liquid drop | ไม่ใช่ผิวต่อผิว | อนุภาค/หยดของเหลวความเร็วสูงกระทบผิว | กำจัดอนุภาค, เปลี่ยนมุมกระทบ, คุมความชื้น |
| Cavitation | pitting จากฟองไอยุบ | ไม่ใช่ผิวต่อผิว | flow ไม่พอ, แรงดันต่ำที่ inlet, air entrainment | คุม suction/flow, air entrainment, foam |
| Fretting | false brinelling | สั่นแอมพลิจูดเล็กขณะเครื่องหยุด | fit หลวม, ความชื้น | fit แน่นขึ้น, grease ที่เหมาะ, ล็อก bearing ระหว่างขนส่ง |
| Contact fatigue | pitting, spalling | rolling | รับ-ปลด load เป็นรอบ, ความเค้นใต้ผิว | ลด overload, กันรอยบุ๋ม (indentation) ที่เป็นจุดรวมความเค้น |
| Corrosive | rust, chemical, oxidative | ไม่ใช่ผิวต่อผิว | น้ำ/กรด/สารเคมี, rust inhibitor หมด | วัสดุทนกัดกร่อน, ลดอุณหภูมิ, ไล่น้ำและผลิตภัณฑ์ออกซิเดชัน |

รายละเอียดสำคัญ
- **Abrasive** มี 2 แบบ: two-body (asperity แข็งขูดผิวอ่อนเมื่อ film บาง) และ three-body (อนุภาคขนาดใกล้ความหนา film ลอดเข้าช่องแล้วขูด) slide ระบุว่าเกิดได้แทบทุกเครื่อง (CMRP CMPR-02 p.3-4)
- **Adhesive** เกิดเมื่อ film แตก, EP/AW ไม่พอ หรือความเร็วผิวต่ำ ตัวอย่าง piston, gear, sliding bearing (p.4-5)
- **Erosion/cavitation** พบที่ outlet, valve, nozzle ความเร็วสูง ส่วน cavitation พบที่ pump inlet และ plain bearing; ใบ compressor ที่มีความชื้นเป็นตัวอย่าง liquid drop erosion (p.5-6)
- **Fretting** สร้างเศษละเอียดที่ออกซิไดซ์ แล้วลดอายุ fatigue (p.6) โน้ตลายมือบน p.1 เชื่อม fretting -> fatigue
- **Contamination** เป็นตัวเร่งร่วมของ abrasive และ contact fatigue (p.4, p.7) ตรงกับ mechanism 5.2 Contamination ของ ISO

## Archard's equation

slide ระบุว่า abrasive และ adhesive wear ทำนายได้ด้วย Archard's equation แต่ไม่แสดงสูตร (CMRP CMPR-02 p.1, p.4) รูปทั่วไป (ความรู้ทั่วไป, confidence low, ไม่อยู่ใน slide):

```
V = K x F x s / H
V = ปริมาตรที่สึก, K = wear coefficient (ไม่มีหน่วย),
F = normal load, s = ระยะเลื่อน, H = ความแข็งของผิวที่อ่อนกว่า
```

ความหมายเชิงปฏิบัติ: ปริมาตรสึกแปรตาม load และระยะเลื่อน และแปรผกผันกับความแข็ง จึงอธิบายว่าทำไม "ลด load" และ "เปลี่ยนวัสดุให้แข็งขึ้น" อยู่ในรายการ control ของ slide ส่วน lubrication และความสะอาดลดค่า K

## Map ไป ISO 14224 / dataset codes

ISO Table B.2 ไม่มี "abrasive/adhesive" แยก ให้ลงรหัสระดับที่สังเกตได้ (ดูกติกาใน [[Failure Mechanism]]) การจับคู่ด้านล่างเป็นการตีความของ wiki นี้

| Wear (CMRP) | Dataset code | ISO Table B.2 |
|---|---|---|
| Abrasive, Adhesive | WEAR | 2.4 Wear |
| Erosion | EROS | 2.3 Erosion |
| Cavitation | CAVT | 2.1 Cavitation |
| Fretting | WEAR (หรือ FATG ถ้าลามเป็นรอยร้าว) | 2.4 / 2.6 |
| Contact fatigue | FATG | 2.6 Fatigue |
| Corrosive | CORR | 2.2 Corrosion |
| ตัวเร่ง: contamination | CTMN | 5.2 Contamination (External influence) |

ข้อควรระวัง: ถ้าสาเหตุจริงคือน้ำมันสกปรก ISO ให้บันทึก mechanism ตามสิ่งที่เห็นที่ item (เช่น 2.4 Wear) แล้วใส่ contamination/สาเหตุราก ไว้ในฟิลด์ failure cause ดู [[Failure Cause Codes]]

## Flag: ข้อความที่น่าสงสัยใน slide

- **"Adhesive = primarily rolling"** (CMRP CMPR-02 p.4): ขัดกับตาราง p.1 ของ slide เองที่ให้ sliding และกับความรู้ทั่วไปว่า galling/scuffing เป็นปรากฏการณ์ของ sliding เป็นหลัก ดูเหมือนคัดลอกบรรทัดจาก slide contact fatigue (p.7 ก็เขียน "primarily rolling" ให้ corrosive wear ซึ่งตาราง p.1 ว่า NA) wiki ถือว่า adhesive = sliding เป็นหลัก
- **"Lubrication มีผลน้อยต่อ contact fatigue ยกเว้นการคุม contamination"** (p.7): ขัดกับความรู้ทั่วไปเรื่องอายุ rolling bearing (ISO 281 ปรับอายุด้วย viscosity ratio kappa อย่างมาก; general knowledge, confidence low) ควรอ่านว่า "เมื่อ film เพียงพอแล้ว ตัวแปรที่เหลือคือ contamination" ไม่ใช่ว่าการหล่อลื่นไม่สำคัญ
- **"ความแข็งไม่ช่วยกัน erosion"** (p.5): กว้างเกิน ความแข็งช่วยได้ในบางมุมกระทบของ solid particle erosion (general knowledge)

ทั้งหมดเป็นข้อผิดพลาด/การสรุปเกินของ slide ไม่ใช่ความขัดแย้งกับ source อื่นใน wiki จึงไม่ตั้ง contested

## เชื่อมโยงกับ compressor failure hierarchy

การตีความ ไม่ใช่ข้อมูลใน CMRP:
- [[LUBS Lubrication System]]: pump w/motor มี WEAR และ CAVT (cavitation ที่ inlet ตรงกับตัวอย่าง slide), oil มี CTMN ซึ่งเป็นตัวเร่ง abrasive wear ของ item ปลายทาง
- [[Reciprocating Compressor]]: valve plate/seat/spring wear และ cylinder liner คือ sliding/impact wear (abrasive/adhesive) และ fatigue ของ valve spring
- [[Centrifugal Compressor]]: liquid drop erosion ที่ใบ impeller เมื่อก๊าซมีความชื้น (ตัวอย่างเดียวกับ slide p.6)
- วิธีตรวจจับ mechanism เหล่านี้ล่วงหน้า (wear particle analysis, vibration) ดู [[Condition Monitoring Techniques]] และ [[Lubrication and Oil Analysis]]

## ดูเพิ่ม

- [[Failure Mechanism]]
- [[Lubrication and Oil Analysis]]
- [[Condition Monitoring Techniques]]
- [[P-F Interval and Condition Monitoring]]
- [[Root Cause Analysis]]

## Triplets

- Abrasive Wear [is_a:: [[Wear Mechanisms]]] cutting, gouging, scratching (CMRP CMPR-02 p.1)
- Adhesive Wear [is_a:: [[Wear Mechanisms]]] galling, seizure, scuffing, smearing (CMRP CMPR-02 p.1)
- Erosion [is_a:: [[Wear Mechanisms]]] solid particle or liquid drop (CMRP CMPR-02 p.5-6)
- Cavitation [is_a:: [[Wear Mechanisms]]] vapour bubble collapse, pump inlet, plain bearing (CMRP CMPR-02 p.5-6)
- Fretting [is_a:: [[Wear Mechanisms]]] false brinelling, vibration while stationary (CMRP CMPR-02 p.6)
- Contact Fatigue [is_a:: [[Wear Mechanisms]]] pitting, spalling, rolling contact (CMRP CMPR-02 p.7)
- Corrosive Wear [is_a:: [[Wear Mechanisms]]] rust, chemical, oxidative (CMRP CMPR-02 p.1)
- [[Wear Mechanisms]] [part_of:: ISO:B.2-2] detail of Material failure category, interpretation
- Abrasive Wear [has_cause:: Hard Particle Contamination] also rough surfaces (CMRP CMPR-02 p.1)
- Abrasive Wear [has_part:: Two-Body Abrasion] hard asperity scratches softer surface when film is thin (CMRP CMPR-02 p.3-4)
- Abrasive Wear [has_part:: Three-Body Abrasion] particle about film thickness enters gap (CMRP CMPR-02 p.3-4)
- Abrasive Wear [resolved_by:: Clean Oil] also thicker film, lower load, remove shock, change material (CMRP CMPR-02 p.1)
- Adhesive Wear [has_cause:: Oil Film Breakdown] asperity cold welding; low EP/AW, low surface speed (CMRP CMPR-02 p.4-5)
- Adhesive Wear [resolved_by:: EP/AW Additive] also thicker film, lower load, smoother surface (CMRP CMPR-02 p.1)
- Adhesive Wear [has_category:: Sliding Contact] slide table p.1 and general knowledge
- CMRP Adhesive Wear Primarily Rolling [contradicts:: Adhesive Wear Sliding Contact] suspected copy error on slide (CMRP CMPR-02 p.4)
- Erosion [resolved_by:: Particle Removal] also change impingement angle (CMRP CMPR-02 p.1)
- Cavitation [has_cause:: Insufficient Flow] also air or water entrainment (CMRP CMPR-02 p.1)
- Fretting [has_cause:: Loose Fit] also moisture (CMRP CMPR-02 p.1)
- Fretting [resolved_by:: Tighter Fit] also suitable grease, lock bearing in transport (CMRP CMPR-02 p.1)
- Fretting [contributes_to:: Contact Fatigue] oxidised debris lowers fatigue life (CMRP CMPR-02 p.6)
- Contact Fatigue [has_cause:: Cyclic Loading] subsurface stress (CMRP CMPR-02 p.7)
- Contact Fatigue [resolved_by:: Overload Reduction] also prevent indentation (CMRP CMPR-02 p.7)
- CMRP Lubrication Has Little Effect On Fatigue [contradicts:: ISO 281 Viscosity Ratio Life Adjustment] slide claim doubtful; general knowledge (CMRP CMPR-02 p.7) [confidence:: low]
- Corrosive Wear [has_cause:: Water Or Acid] also depleted rust inhibitor (CMRP CMPR-02 p.1)
- Corrosive Wear [resolved_by:: Corrosion Resistant Material] also lower temperature, remove water (CMRP CMPR-02 p.1)
- CTMN [contributes_to:: Abrasive Wear] contamination accelerates abrasive and fatigue (CMRP CMPR-02 p.4, p.7)
- Archard's Equation [applies_to:: Abrasive Wear] (CMRP CMPR-02 p.1, p.4)
- Archard's Equation [applies_to:: Adhesive Wear] (CMRP CMPR-02 p.1, p.4)
- Archard's Equation [has_formula:: V = K x F x s / H] formula not on slide, general knowledge [confidence:: low]
- Abrasive Wear [maps_to:: WEAR] interpretation
- Adhesive Wear [maps_to:: WEAR] interpretation
- WEAR [maps_to:: ISO:B.2-2.4] Material failure (Table B.2)
- Erosion [maps_to:: EROS] interpretation; ISO:B.2-2.3
- Cavitation [maps_to:: CAVT] interpretation; ISO:B.2-2.1
- Fretting [maps_to:: WEAR] or FATG if cracking follows, interpretation
- Contact Fatigue [maps_to:: FATG] interpretation; ISO:B.2-2.6
- Corrosive Wear [maps_to:: CORR] interpretation; ISO:B.2-2.2
- [[Wear Mechanisms]] [detected_by:: [[Lubrication and Oil Analysis]]] wear particle analysis
- [[Wear Mechanisms]] [detected_by:: [[Condition Monitoring Techniques]]] vibration, ultrasonic
- LUBS-PMTR [has_mechanism:: CAVT] cavitation at pump inlet matches slide example, interpretation
- [[Centrifugal Compressor]] [related_to:: Erosion] liquid drop erosion of wet-gas blades, slide example p.6, interpretation [confidence:: low]
- [[Wear Mechanisms]] [defined_in:: [[CMRP Course]]] (CMRP CMPR-02 p.1-7)

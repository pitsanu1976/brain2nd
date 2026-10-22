---
title: How to set up CMMS failure structure to support FMECA
created: 2026-10-23
updated: 2026-10-23
type: query
tags: [query, cmms, fmeca, iso-14224, taxonomy, coding, data-quality, criticality, compressor]
sources: [iso-14224.md, reliability-based-maintenance-management.md, compressor-failure-hierarchy.md]
confidence: medium
contested: false
---

# How to set up CMMS failure structure to support FMECA

คำถาม: ตั้ง failure structure ใน CMMS อย่างไรให้ support FMECA

คำตอบสั้น: ใช้ **ชุดรหัสเดียวกัน** ทั้งใน FMECA library และใน Work Order failure report เพื่อให้ข้อมูลการเสียจริงไหลกลับไปปรับคะแนน S/O/D ได้ แบ่งเป็น 3 ชั้น: master data (hierarchy + catalog + valid combination), FMECA library และ transaction (WO) หน้านี้สังเคราะห์จากหน้า wiki ที่อ้าง ส่วนที่เป็นข้อเสนอหรือความรู้ทั่วไปติดป้าย `confidence: low` ไว้

## 1. หลักการ (จาก sources)

- FMECA ให้คะแนนที่ Item → Function → Functional Failure → Failure Mode และใช้ RPN = S x O x D หรือ Cr(t) เชิงปริมาณ (RBMM p.138-143) ดู [[FMECA]]
- CMMS ส่วนใหญ่ไม่มี FMECA ในตัว RBMM ระบุว่า Criticality, Task Selection และ FMECA มักอยู่นอก CMMS จึงต้องผูกด้วยรหัส ดู [[CMMS]]
- Failure Mode เป็นศูนย์กลางข้อมูล ห้ามปิด CM WO ถ้ายังไม่ระบุ Failure Mode (RBMM p.111) ดู [[Failure Data Recording]]
- event ใน CMMS ไม่ใช่ reliability data ในตัวเอง ต้องมี taxonomy, boundary, นิยาม failure และการตรวจสอบ (ISO 14224 cl. 7, 9) ดู [[RM Data Quality]]

## 2. โครงสร้าง 3 ชั้น

```
ชั้น A  Master data   : Asset hierarchy + Catalog รหัส + Valid combination
ชั้น B  FMECA library : 1 แถว = 1 failure mode ของ 1 maintainable item ใน 1 equipment class (S/O/D, task)
ชั้น C  Transaction   : WO failure report ใช้รหัสชั้น A → สรุปผลย้อนกลับไปปรับ O/S/D ในชั้น B
```

### ชั้น A: Asset hierarchy ตาม [[ISO 14224 Taxonomy]]

| ISO level | ใน CMMS | ตัวอย่าง compressor |
|---|---|---|
| 1-5 Industry ถึง Section/System | Functional location (smart number) | platform, gas compression |
| 6 Equipment class/unit | Equipment (tag แยกจาก serial) | class CO, type CE/RE/SC/AX |
| 7 Subunit | Catalog กลุ่ม object part | 6 subunit ตาม ISO Table A.9 |
| 8 Maintainable item | Catalog object part | Cylinder liner, Valves, Sensors, Filters |
| 9 Part | BOM ไม่อยู่ใน hierarchy | seal, gasket |

- RBMM ให้ hierarchy หยุดที่ Equipment และใช้ Object Part ระบุชิ้นส่วนในประวัติ (RBMM p.97-98) ดู [[CMMS]]
- tag คงที่ตามตำแหน่ง ส่วน serial เปลี่ยนเมื่อสลับเครื่อง (ISO 14224 Table 5 note b, p.40)
- driver ของ compressor อยู่นอก boundary บันทึกเป็น equipment แยก (ISO 14224 cl. A.2.2.2.1, p.64-65) ดู [[Compressor Subdivision Wiki vs ISO 14224]]

### ชั้น A: Catalog ที่ต้องตั้ง

| Catalog | ที่มา | จำนวน | หน้า wiki |
|---|---|---|---|
| Failure mode (ระดับ equipment) | ISO Table B.6 | CO = 20 (19 ของ dataset + PLU) | [[Failure Mode]] |
| Failure mechanism | ISO Table B.2 | 38 รหัส (1.0-6.4) | [[Failure Mechanism]] |
| Failure cause (root cause) | ISO Table B.3 | 21 รหัส | [[Failure Cause Codes]] |
| Detection method | ISO Table B.4 | 11 รหัส | [[Failure Detection Method]] |
| Maintenance activity | ISO Table B.5 | 12 รหัส | [[Resolution Codes]] |
| Failure impact | critical, degraded, incipient | 3 | [[Failure Impact Classification]] |
| Consequence class | ISO Table C.2 (4 ด้าน x 4 ระดับ) | 16 | [[Failure Impact Classification]] |
| Operating condition | running, start-up, standby, testing ฯลฯ | 7 | [[Failure Data Recording]] |

**Valid combination (ข้อเสนอของ wiki, confidence: low):** จำกัด dropdown ให้เหลือคู่ที่เกิดได้จริง
- Failure mode x Maintainable item ต่อ equipment class ใช้ matrix OREDA ใน [[Which maintainable item and mode pairs drive failure rate]]
- Maintainable item x Mechanism ใช้คลัง CAUSE_CODE ใน [[CAUSE_CODE Convention]] (รูปแบบ SubUnit-Item-Mechanism เป็นรหัสระดับ mechanism ไม่ใช่ root cause ตาม ISO)

### ชั้น B: FMECA library

| คอลัมน์ | ค่า | เชื่อมกับ |
|---|---|---|
| Key | Equipment class + Subunit + MI + Failure mode (+ Mechanism) | รหัสชั้น A |
| Function / Functional failure | ข้อความ | [[RCM Reliability Centered Maintenance]] |
| Effect (local, system, plant) | ข้อความ + consequence class | ISO Table C.2 |
| S (1-5) | Minor ถึง Catastrophic (RBMM Fig 5.20) | failure impact, consequence |
| O (1-5) | 1/10,000 ถึง 1/10 (MIL-STD-1629, RBMM Fig 5.19) | failure rate จาก WO |
| D (1-5) | ตรวจพบล่วงหน้า 80-100% ถึง 0-20% (RBMM Fig 5.21) | detection method จาก WO |
| RPN หรือ Cr(t) | S x O x D หรือ FFCr = FF x S x MR | [[FMECA]] |
| Task + interval | รหัส PM task ที่สู้กับ mode นี้ | [[PM Task Selection]] |
| Equipment criticality | A/B/C | [[Criticality Assessment]] |

ตัวอย่าง: CO type RE, subunit Compressor, MI Cylinder liner, mode LOO, mechanism WEAR สัดส่วนใน dataset 5.78% ของ total failure rate (ดู [[LOO Low Output]]) ค่า S/O/D ต้องประเมินโดยทีมไซต์ wiki ไม่มีข้อมูล severity

### ชั้น C: ฟิลด์ใน WO failure report (ISO Table 6, 8 + RBMM 5 records)

- Failure: equipment (tag), failure date, failure mode (บังคับ), failure impact (บังคับ), operating condition (บังคับ), detection method
- สาเหตุ: subunit, MI (object part), mechanism, cause (เติมหลัง RCA; ISO ให้ทำ RCA บังคับกับ worst actors, Table 6 note d, p.41)
- งานซ่อม: maintenance activity, down time, active repair time, wait time, man-hours, maintenance category (modification ไม่ใช่ maintenance, cl. 9.6, p.42-43)
- Gate ปิดงาน: ปิด CM WO ไม่ได้ถ้าไม่มี failure mode ให้ค้างเป็น "Backlog - Failure Mode Undefined" (RBMM p.111) และผู้ตรวจต้องไม่ใช่ผู้บันทึก (ISO cl. 7.1.3)

## 3. ปิด loop: WO ปรับคะแนน FMECA

| คะแนน | ที่มาจาก WO ที่ใช้ key เดียวกัน |
|---|---|
| O | λ = จำนวน failure / เวลาใช้งาน ต่อ key ([[Failure Rate Estimation]]) แปลงเป็น rank หรือใช้ Weibull ต่อ mode หา Fm(t) สำหรับ Cr(t) ([[Weibull Analysis]]) |
| S | สัดส่วน impact = critical และ consequence class จริง ร่วมกับ downtime/cost ([[Failure Impact Classification]]) |
| D | ข้อเสนอของ wiki (confidence: low, ไม่มีใน sources): % failure ที่พบด้วย detection code 1-6 (scheduled/continuous) เทียบ 7-10 (production interference/casual) แล้วใส่ช่วงตาม Fig 5.21 เช่น พบล่วงหน้า 85% → D = 1 |

## 4. ลำดับการทำ

1. กำหนด equipment class และ boundary ตาม ISO Annex A
2. ตั้ง catalog 8 ชุด และตาราง mapping รหัสภายในไปยังรหัส ISO
3. ตั้ง valid combination จาก OREDA matrix
4. FMECA workshop ต่อ equipment class สร้าง library ชั้น B และผูก PM task
5. ตั้งฟิลด์บังคับและ gate ปิด WO
6. ตรวจความครบตามเกณฑ์ ISO (HIGH ประมาณ 100%, MEDIUM มากกว่า 85%) ดู [[RM Data Quality]]
7. ทบทวน O/S/D จากข้อมูลจริงทุกปี และเมื่อ RPN เกินเกณฑ์ที่บริษัทกำหนด

## ข้อควรระวัง

- รหัส 4 ตัวอักษร (PWTR, CPUN, CYLN ฯลฯ) ไม่ใช่รหัส ISO ต้องมี mapping ดู [[Compressor Subdivision Wiki vs ISO 14224]]
- ตำแหน่ง item บางตัวต่างกันระหว่าง dataset กับ ISO (Instruments vs Sensors, control/isolation/check valves) และ [[Failure Hierarchy]] กับ [[Maintainable Item]] ยัง contested ต้องตัดสินก่อนตั้ง catalog
- RPN คูณเลข ordinal คอมโบต่างกันอาจได้ค่าเท่ากัน ให้ดู S 4-5 แยกเสมอ ([[FMECA]])
- ความรู้ทั่วไป (confidence: low, ไม่มีใน sources): ใน SAP PM ตรงกับ catalog profile (object part, damage, cause, activity code groups) ต่อ equipment class; ใน Maximo ตรงกับ failure hierarchy (failure class, problem, cause, remedy) ส่วน S/O/D เก็บใน FMECA/RCM tool หรือตารางแยกที่ใช้ key เดียวกัน

## ดูเพิ่ม

- [[FMECA]]
- [[CMMS]]
- [[Failure Data Recording]]
- [[ISO 14224]]
- [[How to choose PM task for a compressor failure mode]]

## Triplets

- CMMS Failure Structure [step_of:: [[How to set up CMMS failure structure to support FMECA]]] layer A: hierarchy + catalog + valid combination
- FMECA Library [step_of:: [[How to set up CMMS failure structure to support FMECA]]] layer B: one row per failure mode of one maintainable item per equipment class
- Work Order Failure Report [step_of:: [[How to set up CMMS failure structure to support FMECA]]] layer C: transaction using the same codes
- [[FMECA]] [depends_on:: [[CMMS]]] needs the same coded keys as work orders
- CMMS Failure Structure [uses:: [[ISO 14224 Taxonomy]]] levels 1-5 functional location, 6 equipment, 7-8 catalog object part, 9 BOM
- CMMS Failure Structure [uses:: [[Failure Mode]]] catalog per equipment class, CO = 20 modes (ISO Table B.6)
- CMMS Failure Structure [uses:: [[Failure Mechanism]]] catalog, 38 codes (ISO Table B.2)
- CMMS Failure Structure [uses:: [[Failure Cause Codes]]] root cause catalog, 21 codes (ISO Table B.3)
- CMMS Failure Structure [uses:: [[Failure Detection Method]]] catalog, 11 codes (ISO Table B.4)
- CMMS Failure Structure [uses:: [[Resolution Codes]]] maintenance activity catalog, 12 codes (ISO Table B.5)
- CMMS Failure Structure [uses:: [[Failure Impact Classification]]] critical/degraded/incipient and consequence class (ISO Table C.2)
- Valid Combination [part_of:: CMMS Failure Structure] failure mode x maintainable item and item x mechanism [confidence:: low]
- [[Which maintainable item and mode pairs drive failure rate]] [input_to:: Valid Combination] OREDA matrix [confidence:: low]
- [[CAUSE_CODE Convention]] [input_to:: Valid Combination] item x mechanism library [confidence:: low]
- FMECA Library [uses:: [[FMECA]]] S x O x D or Cr(t)
- FMECA Library [uses:: [[Criticality Assessment]]] equipment A/B/C
- FMECA Library [produces:: [[PM Task Selection]]] task + interval per failure mode
- Work Order Failure Report [uses:: [[Failure Data Recording]]] ISO Table 6, 8 and RBMM five records
- Work Order Failure Report [input_to:: FMECA Library] failure counts, impact, detection method per key
- [[Failure Rate Estimation]] [input_to:: Occurrence Rank] lambda per key from work orders
- [[Weibull Analysis]] [input_to:: Occurrence Rank] Fm(t) per failure mode for Cr(t)
- [[Failure Impact Classification]] [input_to:: Severity Rank] share of critical impact and consequence class
- [[Failure Detection Method]] [input_to:: Detectability Rank] share detected by codes 1-6 vs 7-10 [confidence:: low]
- Work Order Closure Gate [applies_to:: Work Order Failure Report] CM WO cannot close without failure mode (RBMM p.111)
- [[RM Data Quality]] [applies_to:: Work Order Failure Report] completeness HIGH ~100%, MEDIUM >85%, independent verifier
- CPUN-CYLN [has_failure_mode:: [[LOO Low Output]]] example FMECA library row, 5.78% of total failure rate, mechanism WEAR
- CMMS Failure Structure [related_to:: [[Compressor Subdivision Wiki vs ISO 14224]]] 4-letter codes are not ISO codes, mapping needed

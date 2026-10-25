---
title: Maintenance Time Definitions
created: 2026-10-21
updated: 2026-10-25
type: concept
tags: [iso-14224, kpi, reliability, maintenance-management, data-quality, cmrp, maintainability]
sources: [iso-14224.md, reliability-based-maintenance-management.md, cmrp.md]
confidence: medium
contested: false
---

# Maintenance Time Definitions

นิยามเวลา (time breakdown) และตัวชี้วัดเวลาซ่อมตาม [[ISO 14224]] (cl. 3.59-3.64, cl. 8.3, Annex C) พร้อมจับคู่กับคำของหนังสือ RBMM (MTTR, MWT, MDT) หน้านี้เขียนด้วยถ้อยคำของ wiki เอง ไม่ใช่ข้อความต้นฉบับของมาตรฐาน

## 1. การแตกเวลาของ item (Table 4, ISO 14224 cl. 8.3.1, p.33)

```
Total time = Up time + Down time
```

| กลุ่ม | ประกอบด้วย |
|---|---|
| Down time ตามแผน (planned) | PM (เตรียมงาน/delay + active PM รวม test), outage อื่นตามแผน (reserve, modification) |
| Down time นอกแผน (unplanned) | Corrective (undetected fault, เตรียมงาน/delay, ซ่อม = diagnosis + ซ่อม + test), outage อื่น (shutdown/trip, ข้อจำกัดการเดินเครื่อง) |
| Up time: operating time | run-down, start-up, running |
| Up time: non-operating time | hot standby, idle, cold standby |

- run-down และ start-up **ไม่นับเป็น down time** (ISO 14224 cl. 8.3.3, p.34)
- mobilization time อยู่ในส่วน preparation/delay (cl. 8.3.3, p.34)
- ข้อความ cl. 8.3.1 (p.32) ให้ idle และ hot standby เป็น operating (in-service) ส่วน cold standby (ต้องเตรียมก่อนเดิน) ไม่ใช่ แต่ Table 4 วางทั้ง hot standby, idle, cold standby ไว้ใต้ non-operating time ใน up time ตีความได้ว่าทั้งหมดเป็น up time (เป็นข้อสังเกตของ wiki ไม่ใช่ถ้อยคำของมาตรฐาน)
- Modification อาจเปลี่ยน reliability จึงควรปิด surveillance period แล้วเริ่มใหม่ (Table 4 note, p.33) และไม่ใช่ maintenance category (cl. 9.6.1, p.42)
- ISO 14224 แนะนำเก็บ 2 ค่าคือ **down time** (หยุดเพื่อซ่อมจนกลับใช้งานหลัง test) และ **active repair time** (cl. 8.3.3, p.34) ปกติ active repair <= down time

## 2. ตัวชี้วัดเวลา (ISO 14224 cl. 3.59-3.64, p.12-13; cl. C.5, p.223-225)

| ตัวย่อ | ความหมาย (ถอดความ) | หมายเหตุ |
|---|---|---|
| MART | ค่าคาดหมายของ active repair time | เวลาลงมือซ่อมจริง |
| MRT | ค่าคาดหมายของ (เวลาก่อนเริ่มซ่อม + ซ่อมจริง + เวลาก่อนส่งคืน operation) | ใน Annex C ใช้ MRT = 1/μ (C.49) ส่วนซ่อมของ MDT |
| MTTR | ค่าคาดหมายเวลาจนซ่อมเสร็จ (time to repair) | เวลา detect เป็น 0 หรือไม่ทราบในทางปฏิบัติ |
| MTTRes | MRT + เวลาตรวจพบ failure (mean time to restoration) | ใช้ใน AI = MTTF/(MTTF + MTTRes) |
| MDT | เวลาหยุดเฉลี่ยรวมทุก delay ตั้งแต่เสียจนกลับมาทำงาน | รวม detection, อะไหล่, logistics, standby, policy, active time, reinstatement จึงไม่ intrinsic (cl. C.5.2, p.223) |
| MUT | mean up time | ใช้ใน Ao = MUT/(MUT + MDT) |
| METBF | elapsed time เฉลี่ยระหว่าง failure ของ repairable item | METBF = MUT + MDT (C.46, p.223-224) ดู [[Reliability Metrics]] |

- **สิ่งที่ field data ให้ได้จริง**: มาตรฐานระบุว่าเก็บได้แค่ MRT และ MART เพราะเวลา detect มักไม่ทราบ (cl. 3.63, p.12-13) สอดคล้องกับ Table 8 ที่กำหนดฟิลด์ active maintenance time และ down time (cl. 9.6.3, p.44-45)
- active maintenance time **ไม่รวม** logistic delay แต่ **รวม** technical delay (cl. 3.1, p.2) ส่วน logistic delay คือ delay จากการจัดหาทรัพยากร ไม่รวม administrative delay (cl. 3.46, p.10)
- maintenance man-hours ไม่เท่ากับ MTTR/MDT เพราะหลายคนทำพร้อมกัน (cl. 3.53, p.11)
- ถ้าเวลาซ่อมไม่เป็น exponential (เช่น log-normal) ต้อง fit จากเวลาซ่อมรายครั้ง (cl. C.4.2, p.221-222) ส่วน M(t) = 1 - exp(-μt) ตรงกับสูตร maintainability ของ RBMM ใน [[Reliability Metrics]]
- mean ใช้ได้ดีเมื่อไม่มี trend ถ้ามี wear-out หรือ run-in ค่าเฉลี่ยทำให้ตัดสินใจผิดได้ (cl. C.5.1, p.223)

### ชื่อชนกัน: MTTR

ISO 14224 ใช้ MTTR = time to **repair** แต่ IEC 60050-192 ใช้ MTTR ย่อจาก time to **restoration** (ISO 14224 cl. 3.63-3.64, p.12-13) ISO 14224 จึงใช้ MTTRes แทนฝั่ง restoration เมื่ออ่านรายงานหรือ benchmark ต้องเช็คว่าผู้เขียนหมายถึงเวลาที่รวม detection/delay หรือเฉพาะซ่อม

## 3. จับคู่กับ RBMM

| RBMM | ISO 14224 | ข้อสังเกต |
|---|---|---|
| MTTR (Repair + wait labor) | ใกล้ MRT หรือ MTTRes ขึ้นกับว่ารวมเวลารอคนหรือไม่ | RBMM p.49-51 นับเวลารอแรงงานใน MTTR |
| MWT (รออะไหล่) | logistic delay (ส่วนหนึ่งของ MDT) | อยู่นอก active maintenance time ของ ISO |
| MDT = MTTR + MWT (RBMM Fig 1.2, p.17-20) | MDT รวมทุก delay | แนวคิดตรงกัน ISO ขยายขอบเขต (รวม detection, standby, reinstatement) |
| MTBF = MTTF + MTTR + MWT | METBF = MUT + MDT | ไม่ถือว่าขัดกัน เป็นต่างชื่อและขอบเขต ดู [[Reliability Metrics]] |

การจับคู่นี้เป็นการตีความของ wiki (confidence medium) เนื่องจาก RBMM ไม่ได้อ้างนิยามของ ISO 14224 ดู [[Availability and OEE]] ที่ใช้ MDT เป็นตัวหารของ availability และ [[Maintenance KPIs]]

## 4. จับคู่กับ CMRP (เพิ่ม 2026-10-25, sources: cmrp.md)

สไลด์ [[CMRP Course]] (secondary teaching source) แบ่ง downtime เป็น run-down, preparation/delay, active repair, waiting/delay, start-up (CMRP CMPR-04 p.22) และจำกัด MTTR ไว้ที่ active repair 7 ขั้นตาม MIL-HDBK-472: localization, isolation, disassembly, interchange, reassembly, alignment, checkout ส่วนเวลารออะไหล่/เครื่องมือ/ขนส่ง/admin เรียก inactive time (CMRP CMPR-04 p.39-40)

| CMRP | ISO 14224 | RBMM | ข้อสังเกต |
|---|---|---|---|
| MTTR (active repair 7 ขั้น) | ใกล้ MART | MTTR รวม wait labor | MTTR ของ CMRP แคบที่สุดในสามแหล่ง |
| Preparation/delay + waiting/delay, inactive time | preparation/delay, logistic และ administrative delay | MWT (รออะไหล่) | ISO แยก logistic กับ administrative delay ส่วน CMRP รวมเป็น inactive |
| Downtime (รวม run-down และ start-up ในรูป) | Down time ไม่รวม run-down/start-up (cl. 8.3.3, p.34) | MDT = MTTR + MWT | ขอบเขตต่างกัน |
| MDT ใน Ao = MTBM/(MTBM + MDT) | MDT ใน Ao = MUT/(MUT + MDT) | MDT ใน Availability | ดู [[Availability and OEE]] (contested ที่หน้านั้น) |
| MAMT (corrective + PM ถ่วงความถี่) ใน Aa | active maintenance time (รวม technical delay) | ไม่มี | ใกล้กันเชิงแนวคิด |

- ความต่างเป็น convention/ขอบเขตศัพท์ ไม่ใช่ข้อขัดแย้งของตัวเลข หน้านี้จึงคง `contested: false`; เวลาบันทึกข้อมูลใน CMMS ให้ยึดนิยามของ ISO 14224 (มาตรฐาน) และระบุทุกครั้งว่า MTTR ที่รายงานรวมเวลารอหรือไม่
- การที่รูปของสไลด์วาง run-down/start-up ในแผนภาพ downtime น่าจะสะท้อนมุมมองเวลาสูญเสียการผลิต ไม่ใช่นิยาม down time ของ item (การตีความของ wiki, confidence medium)
- ทฤษฎี M(t), lognormal repair time, Mmax และการจัดสรร MTTR ดู [[Maintainability]]

## เชื่อมโยงกับ compressor failure hierarchy

- ข้อมูล [[OREDA]] ไม่ให้ MTTR/MWT ให้เก็บ down time และ active maintenance time ต่อ failure record จาก [[CMMS]] ตาม Table 8 ของ ISO 14224 ข้อควรระวังคือ CMMS ยังบันทึกสองค่านี้น้อย (Table 8 note d, p.45)
- ถ้าต้องการแยกว่า availability ของ [[Compressor]] ต่ำเพราะซ่อมช้าหรือรออะไหล่ ให้ใช้ MART เทียบ MRT/MDT ความต่างคือ delay ที่อยู่นอกการลงมือซ่อม
- ช่วง trip/spurious stop (UST ใน [[Failure Mode]]) นับเป็น unplanned down time ตาม Table 4 แม้ไม่มี physical failure (Annex B.1, p.176 ว่านับสำหรับ availability เท่านั้น)

## ดูเพิ่ม

- [[ISO 14224 Taxonomy]]
- [[Failure Rate Estimation]]
- [[RM Data Quality]]
- [[Failure Impact Classification]]
- [[Maintainability]]

## Triplets

- [[Maintenance Time Definitions]] [defined_in:: [[ISO 14224]]] cl. 3.59-3.64, cl. 8.3, Annex C
- Total Time [has_formula:: Up time + Down time] (ISO 14224 Table 4, cl. 8.3.1, p.33)
- Total Time [has_part:: Up Time]
- Total Time [has_part:: Down Time]
- Down Time [has_part:: Planned Down Time] PM (preparation/delay + active PM incl. test), other planned outage (reserve, modification)
- Down Time [has_part:: Unplanned Down Time] corrective (undetected fault, preparation/delay, repair), other outage (shutdown/trip, operating limits)
- Up Time [has_part:: Operating Time] run-down, start-up, running
- Up Time [has_part:: Non-operating Time] hot standby, idle, cold standby
- Run-down And Start-up [differs_from:: Down Time] not counted as down time (ISO 14224 cl. 8.3.3, p.34)
- Mobilization Time [part_of:: Preparation And Delay] (ISO 14224 cl. 8.3.3, p.34)
- ISO 14224 cl. 8.3.1 Standby Text [differs_from:: ISO 14224 Table 4 Standby Placement] text: idle and hot standby operating, cold standby not; Table 4 puts all under non-operating up time (wiki observation)
- Modification [differs_from:: Maintenance Category] restart surveillance period (ISO 14224 Table 4 note, cl. 9.6.1)
- Down Time [is_a:: Recommended Time Record] with active repair time (ISO 14224 cl. 8.3.3, p.34)
- Active Repair Time [is_a:: Recommended Time Record] normally active repair <= down time
- MART [has_label:: Mean Active Repair Time] expected active repair time (ISO 14224 cl. 3.59-3.64)
- MRT [has_label:: Mean Repair Time] time before repair + active repair + time before return to operation
- MRT [has_formula:: 1/μ] Annex C (C.49), repair part of MDT
- MTTR [has_label:: Mean Time To Repair] expected time to repair; detection time 0 or unknown in practice (ISO 14224)
- MTTRes [has_formula:: MRT + time to detect failure] mean time to restoration
- MTTRes [input_to:: Intrinsic Availability AI] AI = MTTF/(MTTF + MTTRes)
- MDT [has_label:: Mean Down Time] all delays from failure to return; not intrinsic (ISO 14224 cl. C.5.2, p.223)
- MUT [has_label:: Mean Up Time]
- MUT [input_to:: Operational Availability Ao ISO] Ao = MUT/(MUT + MDT)
- METBF [has_formula:: MUT + MDT] (ISO 14224 C.46, p.223-224)
- Field Data [source_of:: MRT] and MART only, detection time usually unknown (ISO 14224 cl. 3.63, p.12-13)
- Field Data [source_of:: MART] (ISO 14224 Table 8, cl. 9.6.3, p.44-45)
- Active Maintenance Time [has_part:: Technical Delay] excludes logistic delay (ISO 14224 cl. 3.1, p.2)
- Logistic Delay [differs_from:: Administrative Delay] logistic delay excludes administrative delay (ISO 14224 cl. 3.46, p.10)
- Maintenance Man-hours [differs_from:: MTTR] several people work in parallel (ISO 14224 cl. 3.53, p.11)
- Maintainability [has_formula:: M(t) = 1 - exp(-μt)] exponential repair time; non-exponential must be fitted (ISO 14224 cl. C.4.2)
- Mean Value [applies_to:: No Trend] wear-out or run-in makes means misleading (ISO 14224 cl. C.5.1, p.223)
- MTTR [differs_from:: MTTR IEC 60050-192] ISO = time to repair, IEC = time to restoration (ISO 14224 cl. 3.63-3.64)
- MTTRes [alias_of:: MTTR IEC 60050-192] restoration side
- RBMM MTTR [maps_to:: MRT] or MTTRes depending on whether labor wait included (RBMM p.49-51) [confidence:: medium]
- MWT [maps_to:: Logistic Delay] waiting for spares, part of MDT, outside ISO active maintenance time [confidence:: medium]
- RBMM MDT [has_formula:: MTTR + MWT] (RBMM Fig 1.2, p.17-20)
- RBMM MDT [maps_to:: MDT] ISO scope wider (detection, standby, reinstatement) [confidence:: medium]
- MTBF [maps_to:: METBF] different name and scope, not treated as conflict; see [[Reliability Metrics]] [confidence:: medium]
- MDT [input_to:: Availability] denominator, see [[Availability and OEE]]
- [[OREDA]] [differs_from:: [[CMMS]]] OREDA gives no MTTR/MWT; collect down time and active maintenance time per record from CMMS
- [[CMMS]] [source_of:: Down Time] per ISO 14224 Table 8; often poorly recorded (Table 8 note d, p.45)
- MART [input_to:: Availability] compare with MRT/MDT to split slow repair from waiting, for [[Compressor]]
- [[UST Spurious Stop]] [has_category:: Unplanned Down Time] trip/spurious stop counted for availability only (ISO 14224 Annex B.1, p.176)
- [[Maintenance Time Definitions]] [related_to:: [[Maintenance KPIs]]]
- CMRP Downtime [has_part:: Active Repair] with run-down, preparation/delay, waiting/delay, start-up (CMRP CMPR-04 p.22)
- CMRP MTTR [applies_to:: Active Repair] seven MIL-HDBK-472 steps, localization to checkout (CMRP CMPR-04 p.39)
- CMRP MTTR [maps_to:: MART] narrowest MTTR of CMRP, ISO, RBMM [confidence:: medium]
- Inactive Time [maps_to:: Logistic Delay] plus administrative delay; spares, tools, transport, admin (CMRP CMPR-04 p.39-40) [confidence:: medium]
- CMRP Downtime [differs_from:: Down Time] slide figure includes run-down and start-up; ISO 14224 cl. 8.3.3 excludes them; convention, not contested
- MAMT [maps_to:: Active Maintenance Time] corrective + PM weighted by frequency, used in Aa (CMRP CMPR-04 p.23) [confidence:: medium]
- [[Maintenance Time Definitions]] [related_to:: [[Maintainability]]] M(t), lognormal repair time, Mmax

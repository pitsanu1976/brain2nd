---
title: RBMM Concepts vs Compressor Failure Hierarchy
created: 2026-10-21
updated: 2026-10-21
type: comparison
tags: [comparison, book, taxonomy, rcm, maintenance-management]
sources: [reliability-based-maintenance-management.md, compressor-failure-hierarchy.md]
confidence: medium
contested: false
---

# RBMM Concepts vs Compressor Failure Hierarchy

เทียบแนวคิดในหนังสือ [[Reliability Based Maintenance Management Book]] กับ 7 ระดับของ [[Failure Hierarchy]] ที่ใช้ใน wiki นี้ (ตาม OREDA / [[ISO 14224]]) คอลัมน์ "ที่มา" ระบุว่าการจับคู่มาจากหนังสือโดยตรง (ระบุหน้า) หรือเป็นการตีความของ wiki (interpretation) หนังสือไม่ได้เทียบกับ OREDA เอง ประเด็น SPS vs UST resolve แล้ว 2026-10-21: ใช้ UST หลัก SPS เป็น alias (ดู [[Failure Data Recording]])

## ตารางเทียบ

| แนวคิดในหนังสือ | ระดับ/หน้าใน wiki | ความสัมพันธ์ | ที่มา |
|---|---|---|---|
| Plant, Process, System, Subsystem | เหนือระดับ Equipment ของ [[Failure Hierarchy]] | wiki เริ่มที่ Equipment (compressor) ไม่มีระดับบนกว่านี้ | หนังสือ Fig 5.12 p.130 |
| Equipment (ขอบเขตที่ Function Failure เกิดจากการเสียของมัน) | [[Compressor]] (ระดับ 1) | ตรงกัน | หนังสือ p.151-152 กับ interpretation ว่าเป็น compressor |
| Boundary pump/motor (Starting, Driver, Power Transmission, Control and Monitoring, Lubrication, Miscellaneous) | Sub Unit 6 กลุ่ม เช่น [[PWTR Power Transmission]], [[CTMN Control and Monitoring]], [[LUBS Lubrication System]], [[MISC Miscellaneous]] | ชื่อกลุ่มคล้ายกัน แต่เป็น boundary ของ pump/motor ไม่ใช่ compressor | หนังสือ Fig 5.14, 5.16 p.132-133 กับ interpretation |
| Object Part (ชิ้นส่วนต้นตอของปัญหา) | [[Maintainable Item]] (ระดับ 3) | ใกล้เคียง ไม่ใช่นิยามเดียวกัน | interpretation (หนังสือไม่ได้เทียบ) |
| Damage Code (equipment เสียหายอย่างไร) | [[Failure Mode]] (ระดับ 4) | เทียบได้ เช่น ELP, ELU, VIB | หนังสือ p.151-152 (Damage Code = FM ระดับ equipment) กับ interpretation |
| Cause (Failure Mode ของ Object Part) | [[Failure Mechanism]] (ระดับ 5) และ [[Failure Cause Codes]] (ระดับ 6) | หนังสือใช้ Cause ชั้นเดียว wiki แยก 2 ชั้น | interpretation |
| ลำดับ causation 7 ระดับ (ถึง design/assembly/procurement/storekeeping error) | [[Failure Mechanism]] กับ latent cause | ใช้แยก mechanism กับสาเหตุเชิงระบบ | หนังสือ Fig 5.13 p.131 |
| Action (จัดการอย่างไร) | [[Resolution Codes]] (ระดับ 7) | เทียบได้ในแง่ข้อมูลที่ต้องเก็บ | หนังสือ p.152 กับ interpretation |
| รหัส failure mode ISO 14224 ของ pump (19 รหัส) | [[Failure Mode]] 19 โหมด | ตรงกัน 18 รหัส; SPS (หนังสือ) = alias ของ UST (wiki) — ใช้ UST หลัก (resolved 2026-10-21) | หนังสือ Fig 5.15 p.133 |
| รหัส failure mode ของ motor (18 รหัส) | [[Failure Mode]] | ไม่มี ELP, INL; มี OWD ซึ่งไม่อยู่ใน wiki | หนังสือ Fig 5.17 p.134 |
| Failure Mode ตาม SAE (single event ที่ก่อ functional failure) | [[Failure Mode]] | ระดับ causation ที่หนังสือเรียก FM ลึกกว่าระดับ equipment | หนังสือ Fig 5.13 p.131 |
| Criticality A/B/C (Consequence x Likelihood) | ระดับ Equipment และ sub unit/item (ยังไม่มีการจัดระดับจริง) | ใช้จัดลำดับ [[Compressor]] และ failure mode ตาม consequence | หนังสือ p.116-118 ([[Criticality Assessment]]); การนำมาใช้เป็น interpretation |
| Criticality เชิงปริมาณราย failure mode (RPN, FF, FFCr) | [[Failure Mode]] x [[Maintainable Item]] | ใช้ % OREDA เป็นตัวแทนความถี่สัมพัทธ์ได้ในเชิงแนวคิดเท่านั้น | [[FMECA]] (หนังสือ) กับ interpretation |
| ประเภทงาน PM 5 แบบ (CM, overhaul/discard, failure finding, RTF, redesign) | คอลัมน์ "recommended task" ต่อ [[Failure Mode]] x [[Maintainable Item]] (ยังไม่มีใน wiki) | wiki ยังไม่มีคอลัมน์นี้ | หนังสือ p.180 ([[PM Task Selection]]) กับ interpretation |
| Weibull beta/eta ราย failure mode | [[Failure Mode]] ราย item | OREDA ใน wiki ไม่มี beta/eta (มีแต่ %) | หนังสือ ([[Weibull Analysis]]); ข้อจำกัดของ wiki เป็นข้อเท็จจริงจาก [[OREDA]] |
| Spares ราย failure mode / Object Part | [[Maintainable Item]] | Part Criticality = Price, Lead Time, ตรวจล่วงหน้าได้หรือไม่ | หนังสือ Fig 9.5 p.243-246 ([[Spare Part Criticality and Risk]]) กับ interpretation |
| ฟิลด์ใน Work Order (Failure Mode, Cause, Effect, Down Time ฯลฯ) | ข้อมูลที่ต้องเก็บเพื่อสร้าง dataset ของ Valeura เอง | wiki ไม่มีข้อมูล failure ของ asset Valeura | หนังสือ Fig 4.15 p.109 ([[CMMS]]) |

## ข้อสังเกต

- การเทียบ Object Part กับ Maintainable Item และ Cause กับ Mechanism/Cause Codes เป็น interpretation ทั้งหมด หนังสือไม่ได้ให้รายการ mechanism, descriptor หรือ resolution ละเอียดแบบ OREDA จึงเทียบ [[Failure Mechanism]] และ [[Resolution Codes]] ได้เฉพาะในระดับแนวคิด
- ความขัดแย้งเรื่อง Sub Unit ระหว่าง sources เดิม (ดู [[Failure Hierarchy]]) ไม่ถูกแก้ด้วยหนังสือ เพราะ boundary ที่หนังสือให้เป็นของ pump/motor

## ดูเพิ่ม

- [[Failure Data Recording]]
- [[How to choose PM task for a compressor failure mode]]
- [[Compressor Type Failure Profiles]]

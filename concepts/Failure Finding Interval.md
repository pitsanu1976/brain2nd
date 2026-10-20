---
title: Failure Finding Interval
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [pm, rcm, reliability, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Failure Finding Interval (FFI)

Scheduled Failure Finding คืองานตรวจ/ทดสอบ Hidden Failure ของ protective device หรือ protective system (เช่น protective relay, overload protection, sequence protection, fire protection, breaker, switch gear) ที่เสียโดยไม่แสดงอาการ ถ้าตัวป้องกันเสียซ่อนและเครื่องที่ถูกป้องกันเสียพอดี จะเกิด Multiple Failure ที่ความเสียหายควบคุมไม่ได้ FFI คือคาบตรวจที่ทำให้ "Unavailability" ของตัวป้องกันต่ำพอ RBMM ใช้หลักของ SAE JA1012: FFI = 2 x Unavailability x MTBF ของตัวป้องกัน (RBMM p.183, p.212-215)

## นิยาม

| คำ | ความหมาย |
|---|---|
| Protective System | ตรวจจับความผิดปกติของ protected equipment แจ้งเตือน และ/หรือตัดพลังงาน/แยกระบบอัตโนมัติ เพราะรอคนไม่ทัน (p.183) |
| Hidden (non-evident) Failure | การเสียที่ไม่ปรากฏต่อผู้ใช้ในสภาพปกติ ดู [[PM Task Selection]] |
| Multiple Failure | ตัวป้องกันเสียซ่อน และ protected equipment เสียพร้อมกัน |
| FFI | คาบตรวจ failure finding (ช่วง A-C ในรูป 7.32) |
| U (Unavailability) | สัดส่วนเวลาที่ตัวป้องกันเสียโดยไม่ถูกตรวจพบ (ช่วง B-C) |

## สูตร (RBMM p.213-215)

```
U_prot  = 0.5 x FFI / M_TIVE            (ตัวป้องกันเสียเฉลี่ยกลางคาบ)
FFI     = 2 x U_prot x M_TIVE

M_TED   = MTBF ของเครื่องที่ถูกป้องกัน
M_TIVE  = MTBF ของอุปกรณ์ป้องกัน
M_MF    = MTBF ของ Multiple Failure   (ความน่าจะเป็นเสียต่อหน่วยเวลา = 1/MTBF)

1/M_MF  = (1/M_TED) x U_prot
U_prot  = M_TED / M_MF
FFI     = 2 x U_prot x M_TIVE = 2 x M_TIVE x M_TED / M_MF
```

ความหมาย: ถ้ากำหนด MTBF ของ multiple failure ที่ยอมรับได้ (M_MF) ก็คำนวณ FFI ได้จาก MTBF ของ protected equipment และของตัวป้องกัน ข้อจำกัด: ข้อมูลครบยาก และ failure rate ไม่คงที่เสมอ หนังสือจึงแนะนำ simulation ดู [[Monte Carlo Maintenance Simulation]]

## ตาราง Availability ที่ต้องการ กับ FFI (รูป 7.33, RBMM p.213)

FFI เป็น % ของ MTBF ของตัวป้องกัน (ตรงกับสูตร FFI = 2 x U คือ U = 1 ลบ Availability ตรวจแล้วสอดคล้องทุกแถว)

| Availability ของ protective function | FFI (% ของ MTBF ตัวป้องกัน) |
|---|---|
| 99.99% | 0.02% |
| 99.95% | 0.1% |
| 99.9% | 0.2% |
| 99.5% | 1% |
| 99% | 2% |
| 98% | 4% |
| 95% | 10% |

## ตัวอย่างการใช้ (derived)

ตัวอย่างต่อไปนี้ไม่ใช่ตัวเลขของหนังสือ เป็นการคำนวณประกอบ สมมติ protective device มี MTBF 20 ปี ต้องการ Availability 99.9% ตามตาราง FFI = 0.2% x 20 ปี = 0.04 ปี (ประมาณ 14.6 วัน) ถ้าลดเป้าเหลือ 99% FFI = 2% x 20 ปี = 0.4 ปี (ประมาณ 146 วัน)

## กฎปฏิบัติ

- Failure Finding ใช้เมื่อ failure mode เป็น hidden และไม่มี condition monitoring/replacement ที่คุ้มกว่า (ลำดับข้อ 3 ในรูป 7.3)
- ต้องตรวจทั้งโอกาสที่ตัวป้องกันเสียเองและโอกาสที่เครื่องถูกป้องกันเสีย
- อุปกรณ์สลับเปลี่ยนของระบบสำรอง (transfer switch) ต้องทำ Failure Finding ด้วย ดู [[Redundancy and Standby Systems]]
- ตัวอย่างในหนังสือ: ตัวป้องกันไฟรั่ว/ไฟดูดในบ้าน (p.212)

## เชื่อมโยงกับ compressor failure hierarchy

- ระบบ protection ของ [[Compressor]] (trip/shutdown, ESD, PSV, protective relay) เป็นผู้สมัครตรงของ Failure Finding; หนังสือไม่ได้ระบุ compressor ตรง ๆ และไม่ได้อ้าง IEC 61508 หรือ SIL (ความคล้ายกับ proof-test interval เป็นข้อสังเกตของเรา)
- failure mode ที่เกี่ยวกับ fail-to-function เช่น FTS (fail to start on demand) และ STP (fail to stop on demand) ใน [[Failure Mode]] เป็น mode แบบ on-demand ที่ปกติซ่อนอยู่จนถึงเวลาเรียกใช้ (ข้อเสนอแนะ ไม่ใช่ข้อมูลใน sources)
- OREDA ให้ failure rate ซึ่งใช้เป็น 1/M_TIVE ประมาณการได้ ดู [[OREDA]] แต่เป็นค่าคงที่ จึงตรงกับสมมติฐานของสูตร constant-rate (RBMM p.215 เตือนว่าความจริงไม่คงที่)

## ดูเพิ่ม

- [[PM Task Selection]]
- [[Redundancy and Standby Systems]]
- [[P-F Interval and Condition Monitoring]]
- [[Reliability Metrics]]
- [[Availability and OEE]]

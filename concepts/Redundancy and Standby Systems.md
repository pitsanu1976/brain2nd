---
title: Redundancy and Standby Systems
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [pm, criticality, reliability, maintenance-management, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Redundancy and Standby Systems

Redundancy (ระบบสำรอง) เป็นวิธีเพิ่มความน่าเชื่อถือของระบบนอกเหนือจากการใช้เครื่องที่ reliable สูง RBMM ชี้ว่าการมีเครื่องสำรองไม่ได้ทำให้ criticality ต่ำลงอัตโนมัติ เพราะเครื่อง standby อาจเสียแบบ Hidden Failure จนเกิด Multiple Failure เมื่อเครื่องหลักหยุด และการ optimize PM ราย equipment ไม่เท่ากับ optimize ระบบ (RBMM p.29, p.215-218, p.231)

## รูปแบบและสัญกรณ์ (RBMM p.28-29, p.215)

- k out of n: ต้องการ k จาก n หน่วย (เช่น 1 out of 2, 2 out of 3)
- Standby: ต้องใช้งาน 2 เครื่อง (2 ใน 3) อีก 1 เครื่องสำรองพร้อมใช้ทันที
- Load Sharing: ทุกเครื่องแบ่งภาระ (ตัวอย่าง 3 เครื่อง แต่ละเครื่องรับ 1/3 และรับเพิ่มได้เต็ม 50%)
- อุปกรณ์สลับเปลี่ยน (switching device, รูป 7.35) ตรวจสถานะและต่อสำรองอัตโนมัติหรือด้วยมือ
- Redundancy ระดับ process ใช้ถังเก็บผลผลิตระหว่าง process ลด criticality ภาพรวม (Fig 1.8, p.29-30) ภายใต้ขีดจำกัดปริมาณและระยะเวลาที่ป้อนได้

โครงสร้างเชิงความน่าจะเป็นของ k/n ดู [[Reliability Block Diagram]]

## Criticality ของเครื่องที่มีสำรอง (RBMM p.28-29)

- ไม่มี redundancy (เครื่องอนุกรม): ทุกเครื่อง criticality A
- มี redundancy ระดับเครื่อง: กลุ่มขนานอาจเป็น A/B/C ตามความสามารถรับภาระ แต่เครื่องก่อน/หลังกลุ่มขนานยังเป็น A
- เครื่อง standby อาจเสียซ่อน จึงยังสำคัญสูง; Load Sharing ลด criticality ได้ ขึ้นกับความสามารถรับภาระของแต่ละเครื่อง
- ดูวิธีประเมินใน [[Criticality Assessment]]

## ข้อพิจารณาด้าน PM (RBMM p.215-217, p.231)

1. แผนการใช้งาน: เครื่องที่ใช้มากเสี่ยงเสียมากกว่า ไม่ควรสลับใช้เท่า ๆ กัน (จะเสียไล่เลี่ยกัน) ควรใช้สัดส่วน 80/20 หรือ 60/40 และทดสอบเครื่องสำรองสม่ำเสมอ เพื่อให้อายุใช้งานต่างกัน
2. แผน PM ประกอบด้วยเครื่อง n เครื่อง + อุปกรณ์สลับเปลี่ยน; switching device ใช้ Failure Finding เหมือน protective device ดู [[Failure Finding Interval]]
3. เครื่อง n เครื่องเลือกงานได้ทุกประเภท โดยพิจารณา Multiple Failure เป็นหลัก ดู [[PM Task Selection]]
4. ทำ Condition Monitoring ทั้งเครื่องที่ใช้งานและ standby (Ch.1 p.29) ดู [[P-F Interval and Condition Monitoring]]
5. เป้าหมายอาจเป็นความมั่นคงของระบบมากกว่าต้นทุนต่ำสุด

## ขั้นตอนวิเคราะห์ระบบ k/n (รูป 7.36-7.37, RBMM p.217)

```
1. เริ่มจาก Dominant Failure Mode
2. วิเคราะห์ข้อมูลเสียรายเครื่อง/ราย failure mode (FM1, FM2, FM3 ... และ FMsw ของตัวสลับ)
3. เลือกงานและคาบ PM ต่อ failure mode (แต่ละ FM มี maintenance policy ของตัวเอง)
4. รวมเป็น Total R(t) ของระบบ k/n ด้วย Monte Carlo Simulation
5. ปรับคาบ PM ให้ระบบรอดตามแผนการใช้งาน
```

การรวม reliability ทำด้วย [[Monte Carlo Maintenance Simulation]] ตามหนังสือ ไม่มีสูตรปิดในบทนี้

## เชื่อมโยงกับ compressor failure hierarchy

- กรณี compressor A/B (1 out of 2 หรือ 2 out of 3) ตามตัวอย่างของหนังสือ ต้องแยก failure mode ราย [[Compressor]] และ failure mode ของ switching/auto-changeover; ISO 14224 ไม่ได้บันทึก redundancy เป็นฟิลด์ใน sources ของ wiki นี้
- standby ที่เสียซ่อน ตรงกับ failure on demand เช่น FTS ใน [[Failure Mode]] (ข้อเสนอแนะ ไม่ใช่ข้อมูลใน sources)
- ข้อมูลใน [[OREDA]] เป็นระดับ item ไม่มีข้อมูล redundancy configuration ใน sources ของ wiki นี้

## ดูเพิ่ม

- [[Failure Finding Interval]]
- [[PM Interval Optimization]]
- [[Reliability Block Diagram]]
- [[Criticality Assessment]]
- [[PM Task Selection]]

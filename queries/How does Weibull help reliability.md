---
title: How does Weibull help reliability
created: 2026-10-23
updated: 2026-10-23
type: query
tags: [query, weibull, statistics, reliability, pm, spare-parts, book]
sources: [reliability-based-maintenance-management.md, iso-14224.md]
confidence: medium
contested: false
---

# How does Weibull help reliability

**คำถาม (2026-10-23):** Weibull ช่วย reliability ยังไง

**คำตอบสั้น:** [[Weibull Analysis]] เปลี่ยนประวัติการเสียจริงของเครื่องจักร (time-to-failure ต่อ failure mode) ให้เป็นสมการ ทำให้ตอบได้เชิงตัวเลขว่า "จะเสียเมื่อไร" และ "ควรบำรุงรักษาแบบไหน" แทนการเดาจากประสบการณ์หรือคู่มือผู้ผลิต (ผู้ผลิตไม่เปิดเผยค่าเหล่านี้ ต้องหาเองจากประวัติของตัวเอง, RBMM บท 6) ตอบจากหน้าใน wiki เป็นหลัก

## 1. β บอกรูปแบบการเสีย และบอกว่าควรทำ PM แบบไหน

ดูรายละเอียดใน [[Failure Patterns and Bathtub Curve]] และ [[PM Task Selection]]

| β | รูปแบบการเสีย | งานที่เหมาะ |
|---|---|---|
| β < 1 | infant mortality (เสียช่วงแรกของการใช้งาน) | PM ไม่ช่วย ต้องแก้ที่การติดตั้ง คุณภาพชิ้นส่วน หรือ commissioning |
| β ≈ 1 | สุ่ม, failure rate คงที่ | scheduled replacement ไม่ช่วย ใช้ condition monitoring หรือ run to failure |
| β > 1 | wear-out (สึกหรอตามอายุ) | scheduled replacement / overhaul ได้ และ condition monitoring ได้ |

ข้อนี้สำคัญที่สุด ถ้าไม่รู้ β อาจทำ PM กับชิ้นส่วนที่ทำแล้วไม่ได้อะไรเลย (RBMM บท 7 แสดงด้วยตัวเลขว่าที่ β = 1 การเปลี่ยนตามรอบไม่เพิ่ม reliability)

## 2. η บอกขนาดของอายุ

η (characteristic life) คืออายุที่ชิ้นส่วนเสียไปแล้ว 63.2% ส่วน γ (location) ในตัวอย่างของหนังสือตั้งเป็น 0 ดู [[Weibull Analysis]]

## 3. ได้ตัวเลขที่ใช้ตัดสินใจจริง

ตัวอย่าง RBMM: TTF 4 ค่า 8,500 / 11,000 / 12,000 / 16,000 ชม. ใช้ Y-regression ได้ **β = 3.7888, η = 13,130.8 ชม.** (สูตรอยู่ใน [[Reliability Metrics]])

| คำถาม | ผล | หมายเหตุ |
|---|---|---|
| ที่อายุ 10,000 ชม. เสียไปแล้วกี่ % | F = 29.97%, R = 70.03% | |
| อายุเฉลี่ยก่อนเสีย | MTTF = 11,865 ชม. | = η·Γ(1+1/β) |
| เดินมาแล้ว 10,000 ชม. จะรอดถึง 12,000 ชม. ไหม | conditional R = 70.14% | ใช้ตัดสินว่าจะรอไปทำพร้อม turnaround ได้หรือไม่ |
| ถ้าต้องการ R = 80% ต้องทำ PM เมื่อไร | **≈ 8,837 ชม.** (derived) | หนังสือพิมพ์ 13,847.81 ชม. ซึ่งผิด เพราะใช้สูตร η[1 − ln R]^(1/β) แทน η(−ln R)^(1/β) ถ้าเชื่อค่าในหนังสือจะทำ PM ช้าเกินไปมาก |

## 4. ใช้ต่อในงานอื่น

- **หารอบ PM ที่คุ้มที่สุด:** ใส่ β, η, Cf (ค่าซ่อมเมื่อเสีย) และ Cp (ค่า PM) ในสูตรต้นทุนต่อหน่วยเวลา ตัวอย่างหนังสือได้ประมาณ 10 เดือน ดู [[PM Interval Optimization]]
- **คาดการณ์จำนวนการเสีย อะไหล่ และงบ:** ใช้ simulation ดู [[Monte Carlo Maintenance Simulation]], [[Spare Part Demand Forecasting]], [[Maintenance Budget]]
- **ข้อมูลไม่ครบ:** ชิ้นที่ถูกเปลี่ยนก่อนเสีย (suspension) ปรับ rank ด้วย Mean Order Number ดู [[Censored Data]]
- **เมื่อ failure rate ไม่คงที่:** ISO 14224 ระบุว่าการสมมติ λ คงที่ทั้งที่มี wear-out จะประเมินผิดทั้งช่วงอายุน้อยและอายุมาก และแนะนำ Weibull สำหรับ component ดู [[Failure Rate Estimation]]

## ข้อควรระวัง

- ต้องวิเคราะห์ **แยกทีละ failure mode** ถ้ารวมหลาย mode ค่า β จะเพี้ยน กฎใน [[CMMS]] ที่ห้ามปิดงาน CM-Unplanned ถ้ายังไม่ระบุ failure mode จึงสำคัญ (ดู [[Failure Data Recording]])
- **wiki ยังไม่มี β/η ของ compressor:** ข้อมูล [[OREDA]] ที่มีอยู่เป็นสัดส่วน % ของ failure rate ใช้ fit Weibull ไม่ได้ ต้องใช้ time-to-failure จริงจาก CMMS ของ Valeura (ดู [[How to choose PM task for a compressor failure mode]])

## ดูเพิ่ม

- [[Weibull Analysis]] — วิธีประมาณพารามิเตอร์และการกระทบยอด β 3.5 / 3.79 / 3.94
- [[Statistical Distributions for Maintenance]]
- [[Reliability Based Maintenance Management Book]]

## Triplets

- [[How does Weibull help reliability]] [uses:: [[Weibull Analysis]]] answer synthesized from wiki pages
- [[Weibull Analysis]] [has_parameter:: Shape Parameter Beta] determines failure pattern
- [[Weibull Analysis]] [has_parameter:: Scale Parameter Eta] characteristic life, F = 63.2%
- [[Weibull Analysis]] [selects:: Root Cause Investigation] beta < 1: PM cannot fix
- [[Weibull Analysis]] [selects:: Condition Monitoring] beta = 1: scheduled replacement adds no reliability
- [[Weibull Analysis]] [selects:: Scheduled Replacement] beta > 1: wear-out
- Worked Example TTF 8500-16000 h [has_value:: beta 3.7888, eta 13130.8 h] Y-regression (RBMM ch6)
- Worked Example TTF 8500-16000 h [has_value:: R(10000 h) 70.03%] F = 29.97%
- Worked Example TTF 8500-16000 h [has_value:: MTTF 11865 h] eta x Gamma(1+1/beta)
- Worked Example TTF 8500-16000 h [has_value:: conditional R 10000-12000 h 70.14%]
- Worked Example TTF 8500-16000 h [has_value:: T(R=0.8) about 8837 h] derived; book prints 13847.81 h (formula error)
- [[Weibull Analysis]] [input_to:: [[PM Interval Optimization]]] with Cp, Cf; book example optimum about 10 months
- [[Weibull Analysis]] [input_to:: [[Monte Carlo Maintenance Simulation]]]
- [[Weibull Analysis]] [input_to:: [[Spare Part Demand Forecasting]]]
- [[Censored Data]] [input_to:: [[Weibull Analysis]]] Mean Order Number for suspensions
- [[Failure Data Recording]] [input_to:: [[Weibull Analysis]]] time-to-failure per failure mode
- [[Failure Rate Estimation]] [related_to:: [[Weibull Analysis]]] ISO 14224 recommends Weibull when failure rate is not constant
- [[Compressor]] [has_value:: no beta] no compressor time-to-failure data in sources

---
title: Reliability Block Diagram
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [reliability, statistics, criticality, book]
sources: [reliability-based-maintenance-management.md]
confidence: medium
contested: false
---

# Reliability Block Diagram

Reliability Block Diagram (RBD) คือแผนภาพที่คำนวณ reliability ของระบบจาก reliability ของชิ้นส่วนย่อยตามรูปแบบการต่อ: อนุกรม (series) ขนาน (parallel) และผสม (RBMM p.172-174) หน้านี้สรุปสูตร ตัวอย่างในหนังสือ และ flag ข้อผิดพลาดตัวเลขสองจุด คือผล parallel 0.9085 (ถูกต้อง 0.985) และข้อความ series ที่ระบุ 0.9 ทั้งสองตัวแต่คำนวณด้วย 0.85

## สูตร

```
Series   : R_total = R1 x R2 x ... x Rn                  (ตัวใดเสีย ระบบเสีย)
Parallel : R_total = 1 - Π (1 - Ri)                       (ตัวใดตัวหนึ่งรอด ระบบยังใช้ได้)
Failure tree : Ft = 1 - Π (1 - Fi),  Fi = 1 - Ri          (ตรงข้ามกับ RBD)
```

ระบบจริงมีชิ้นส่วนมาก ต้องใช้โปรแกรมเฉพาะ (RBMM p.174) ค่า R ของแต่ละบล็อกมาจาก Weibull ที่เวลา t เดียวกัน ดู [[Weibull Analysis]] และ [[Reliability Metrics]]

## ตัวอย่างในหนังสือและค่าที่ตรวจแล้ว

| กรณี | ที่หนังสือรายงาน | ค่าที่ถูกต้อง | สถานะ |
|---|---|---|---|
| Series Fig 6.21: R1 = 0.85, R2 = 0.9 | ข้อความบอกทั้งสองตัวเป็น 0.9 แต่คำนวณด้วย 0.85 ได้ 0.765 | 0.85 x 0.9 = 0.765 | หนังสือข้อความไม่ตรงกับการคำนวณ ใช้ 0.765 |
| Parallel Fig 6.22: R1 = 0.85, R2 = 0.9 | 1 - (0.15 x 0.1) = 0.9085 | 1 - 0.015 = **0.985** | หนังสือพิมพ์ผิด (0.9085 เป็นเลขผิด) |
| Mixed Fig 6.24-6.25: R1 = 0.85 อนุกรมกับกลุ่มขนาน {R2 = R3 = R4 = 0.90} อนุกรมกับ R5 = 0.80 | R* = 1 - 0.1^3 = 0.999; Rt = 0.85 x 0.999 x 0.8 | ≈ 0.679 (derived: 0.67932) | ถูกต้อง |

เหตุผลที่ parallel ผิด: 0.15 x 0.1 = 0.015 ไม่ใช่ 0.0915 จึงได้ 0.985 ซึ่งต้องสูงกว่าบล็อกที่ดีที่สุด (0.9) เสมอ ผล 0.9085 ต่ำเกินไปสำหรับ redundancy จริง (RBMM p.173) ความผิดนี้เป็นความผิดพิมพ์/คำนวณในหนังสือ ไม่ใช่ความขัดแย้งกับข้อมูลเดิมใน wiki (`contested: false`)

## ข้อสังเกตการใช้งาน

- ค่า R ต้องอ้างเวลา t เดียวกัน (mission time) และสมมติ failure ของบล็อกเป็นอิสระต่อกัน (สมมติฐานมาตรฐานของ RBD ที่ notes ไม่ได้ระบุชัด จึงเป็นความรู้ทั่วไป)
- การต่อขนานเพิ่ม reliability อย่างมากเมื่อมี redundancy เช่น 3 ตัวขนาน 0.90 ได้ 0.999
- ระบบ standby หรือ k-out-of-n ต้องใช้แบบจำลองเฉพาะ ดู [[Redundancy and Standby Systems]]
- Availability ของระบบต้องรวม MTTR ด้วย ไม่ใช่ R อย่างเดียว ดู [[Availability and OEE]]

## เชื่อมโยงกับ compressor failure hierarchy

- กรอบ RBD สอดคล้องกับลำดับชั้นใน [[Failure Hierarchy]]: [[Compressor]] ประกอบด้วย sub unit หลายส่วน (เช่น power transmission, lubrication, control and monitoring) ซึ่งส่วนใหญ่ต่ออนุกรมเชิง function ถ้าหนึ่งส่วนเสียแล้วเครื่องหยุด
- เทียบกรณี compressor 2x100% หรือ 3x50% เป็นการต่อขนานระดับ train (หนังสือยกเป็นตัวอย่างเชื่อมโยง ไม่มีตัวเลขจริงของ asset Valeura)
- [[Criticality Assessment]] ใช้ RBD/failure tree ช่วยดูว่า failure mode ใดของ [[Maintainable Item]] ทำให้ function ของระบบเสีย ร่วมกับ [[FMECA]]

## ดูเพิ่ม

- [[Reliability Metrics]]
- [[Weibull Analysis]]
- [[Redundancy and Standby Systems]]
- [[Criticality Assessment]]

---
title: CTMN Control and Monitoring
created: 2026-10-20
updated: 2026-10-20
type: entity
tags: [sub-unit, maintainable-item, compressor, failure-rate]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__failure-hierarchy.csv, compressor-failure-hierarchy__sheet5.csv, compressor-failure-hierarchy__subunit-code.csv, failure-structure__sheet1.csv]
confidence: medium
contested: true
---

# CTMN - Control and monitoring

Sub Unit ของ [[Compressor]] สำหรับควบคุม ตรวจวัด และป้องกัน (control unit, monitoring, cabling, power supply, actuating device) รหัส `CTMN` (หมายเหตุ: รหัสนี้ชนกับ mechanism `CTMN` = Contamination ดู [[CAUSE_CODE Convention]])

## Maintainable items (8) และ mechanism codes

| Code | Item | จำนวน CAUSE_CODE | Mechanism codes |
|---|---|---|---|
| INST | Instruments | 18 | FSIG OADJ OPEN EART LEAK BLKG CTMN EROS NSIG NCFD STCK ALGN OVHT LOOS CORR OTHR UNKN VIBR |
| MONI | Monitoring | 8 | FSIG SWFL OADJ FPWR NSIG NCFD LOOS OTHR |
| CTUN | Control unit | 12 | SWFL FSIG NCFD NSIG CTRL LEAK INST FPWR CORR LOOS OTHR UNKN |
| VALV | Valves | 16 | OADJ FSIG STCK LEAK EROS CORR WEAR BRKG CAVT BLKG CTMN LOOS VIBR OTHR FATG UNKN |
| CBJB | Cabling & junction boxes | 10 | OPEN SHRT EART CORR LOOS MEXT LEAK OTHR UNKN DEFM |
| IPSU | Internal power supply | 5 | NPWR FPWR SHRT OTHR OVHT |
| ACTD | Actuating device | 6 | OADJ STCK LEAK WEAR OPEN OTHR |
| CICV | Control-, isolating & check valves | 5 | OADJ FSIG LEAK STCK CTMN |

รวม 80 CAUSE_CODE ดู [[Failure Cause Codes]]

## Failure modes ที่เด่น (% นับที่ CTMN, derived)

ผลรวม **7.06** จาก 85.66: AIR 2.33, OTH 0.89, UST 0.88, PDE 0.83, FTS 0.79, SER 0.40, STP 0.22

คู่เด่น: Monitoring x AIR 0.97, Control unit x AIR 0.84 (Software failure), Control unit x UST 0.53, Control unit x FTS 0.53, Control unit x PDE 0.40 ดู [[AIR Abnormal Instrument Reading]] และ [[UST Spurious Stop]]

## Top failure mechanisms

Software failure, Faulty signal/indication/alarm, Open circuit (cabling), No power/ voltage (power supply), Sticking (actuating device)

## ข้อควรระวัง (contested)

- ผลรวม 7.06 **ไม่รวม Instruments** (นับที่ [[PWTR Power Transmission]]) แม้ Instruments ถูกจับคู่กับ CTMN ด้วย (18 CAUSE_CODE) และไม่รวม Valves (นับที่ [[CPUN Compressor Unit]])
- `failure-structure.md` จัด **Instrument types ทั้งหมดไว้ใน Control and Monitoring** (Instrument, flow/general/level/pressure/speed/temperature/vibration) ถ้าใช้มุมมองนี้ CTMN จะรับ % ของ Instruments ทั้งก้อน (23.34 derived) ซึ่งจะทำให้ CTMN เป็น sub unit ใหญ่ที่สุดแทน CPUN เก็บทั้งสองมุมมอง ดู [[Failure Hierarchy]] และบันทึกใน [[log]]
- Sheet1 ใช้ชื่อ "Control and Monitoring" (M ตัวใหญ่) ต่างจาก "Control and monitoring" ใน dataset หลัก

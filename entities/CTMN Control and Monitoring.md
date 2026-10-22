---
title: CTMN Control and Monitoring
created: 2026-10-20
updated: 2026-10-22
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

## Triplets

- [[CTMN Control and Monitoring]] [is_a:: Sub Unit]
- [[CTMN Control and Monitoring]] [part_of:: [[Compressor]]]
- [[CTMN Control and Monitoring]] [has_code:: CTMN]
- [[CTMN Control and Monitoring]] [differs_from:: CTMN] same code as mechanism CTMN Contamination
- [[CTMN Control and Monitoring]] [alias_of:: Control and Monitoring] failure-structure.md Sheet1 spelling; main dataset uses Control and monitoring
- [[CTMN Control and Monitoring]] [has_value:: 8] maintainable items
- [[CTMN Control and Monitoring]] [has_value:: 80] CAUSE_CODE
- [[CTMN Control and Monitoring]] [has_failure_rate_share:: 7.06%] counted at CTMN (derived), of 85.66, excludes Instruments and Valves; main dataset [contested:: true]
- CTMN-INST [part_of:: [[CTMN Control and Monitoring]]] main dataset; % counted at PWTR [contested:: true]
- CTMN-INST [is_a:: INST]
- CTMN-INST [has_value:: 18] CAUSE_CODE
- CTMN-INST [has_mechanism:: FSIG]
- CTMN-INST [has_mechanism:: OADJ]
- CTMN-INST [has_mechanism:: OPEN]
- CTMN-INST [has_mechanism:: EART]
- CTMN-INST [has_mechanism:: LEAK]
- CTMN-INST [has_mechanism:: BLKG]
- CTMN-INST [has_mechanism:: CTMN]
- CTMN-INST [has_mechanism:: EROS]
- CTMN-INST [has_mechanism:: NSIG]
- CTMN-INST [has_mechanism:: NCFD]
- CTMN-INST [has_mechanism:: STCK]
- CTMN-INST [has_mechanism:: ALGN]
- CTMN-INST [has_mechanism:: OVHT]
- CTMN-INST [has_mechanism:: LOOS]
- CTMN-INST [has_mechanism:: CORR]
- CTMN-INST [has_mechanism:: OTHR]
- CTMN-INST [has_mechanism:: UNKN]
- CTMN-INST [has_mechanism:: VIBR]
- CTMN-MONI [part_of:: [[CTMN Control and Monitoring]]]
- CTMN-MONI [is_a:: MONI]
- CTMN-MONI [has_value:: 8] CAUSE_CODE
- CTMN-MONI [has_mechanism:: FSIG]
- CTMN-MONI [has_mechanism:: SWFL]
- CTMN-MONI [has_mechanism:: OADJ]
- CTMN-MONI [has_mechanism:: FPWR]
- CTMN-MONI [has_mechanism:: NSIG]
- CTMN-MONI [has_mechanism:: NCFD]
- CTMN-MONI [has_mechanism:: LOOS]
- CTMN-MONI [has_mechanism:: OTHR]
- CTMN-CTUN [part_of:: [[CTMN Control and Monitoring]]]
- CTMN-CTUN [is_a:: CTUN]
- CTMN-CTUN [has_value:: 12] CAUSE_CODE
- CTMN-CTUN [has_mechanism:: SWFL]
- CTMN-CTUN [has_mechanism:: FSIG]
- CTMN-CTUN [has_mechanism:: NCFD]
- CTMN-CTUN [has_mechanism:: NSIG]
- CTMN-CTUN [has_mechanism:: CTRL]
- CTMN-CTUN [has_mechanism:: LEAK]
- CTMN-CTUN [has_mechanism:: Instrument failure - general]
- CTMN-CTUN [has_mechanism:: FPWR]
- CTMN-CTUN [has_mechanism:: CORR]
- CTMN-CTUN [has_mechanism:: LOOS]
- CTMN-CTUN [has_mechanism:: OTHR]
- CTMN-CTUN [has_mechanism:: UNKN]
- CTMN-VALV [part_of:: [[CTMN Control and Monitoring]]] % counted at CPUN
- CTMN-VALV [is_a:: VALV]
- CTMN-VALV [has_value:: 16] CAUSE_CODE
- CTMN-VALV [has_mechanism:: OADJ]
- CTMN-VALV [has_mechanism:: FSIG]
- CTMN-VALV [has_mechanism:: STCK]
- CTMN-VALV [has_mechanism:: LEAK]
- CTMN-VALV [has_mechanism:: EROS]
- CTMN-VALV [has_mechanism:: CORR]
- CTMN-VALV [has_mechanism:: WEAR]
- CTMN-VALV [has_mechanism:: BRKG]
- CTMN-VALV [has_mechanism:: CAVT]
- CTMN-VALV [has_mechanism:: BLKG]
- CTMN-VALV [has_mechanism:: CTMN]
- CTMN-VALV [has_mechanism:: LOOS]
- CTMN-VALV [has_mechanism:: VIBR]
- CTMN-VALV [has_mechanism:: OTHR]
- CTMN-VALV [has_mechanism:: FATG]
- CTMN-VALV [has_mechanism:: UNKN]
- CTMN-CBJB [part_of:: [[CTMN Control and Monitoring]]]
- CTMN-CBJB [is_a:: CBJB]
- CTMN-CBJB [has_value:: 10] CAUSE_CODE
- CTMN-CBJB [has_mechanism:: OPEN]
- CTMN-CBJB [has_mechanism:: SHRT]
- CTMN-CBJB [has_mechanism:: EART]
- CTMN-CBJB [has_mechanism:: CORR]
- CTMN-CBJB [has_mechanism:: LOOS]
- CTMN-CBJB [has_mechanism:: MEXT]
- CTMN-CBJB [has_mechanism:: LEAK]
- CTMN-CBJB [has_mechanism:: OTHR]
- CTMN-CBJB [has_mechanism:: UNKN]
- CTMN-CBJB [has_mechanism:: DEFM]
- CTMN-IPSU [part_of:: [[CTMN Control and Monitoring]]]
- CTMN-IPSU [is_a:: IPSU]
- CTMN-IPSU [has_value:: 5] CAUSE_CODE
- CTMN-IPSU [has_mechanism:: NPWR]
- CTMN-IPSU [has_mechanism:: FPWR]
- CTMN-IPSU [has_mechanism:: SHRT]
- CTMN-IPSU [has_mechanism:: OTHR]
- CTMN-IPSU [has_mechanism:: OVHT]
- CTMN-ACTD [part_of:: [[CTMN Control and Monitoring]]]
- CTMN-ACTD [is_a:: ACTD]
- CTMN-ACTD [has_value:: 6] CAUSE_CODE
- CTMN-ACTD [has_mechanism:: OADJ]
- CTMN-ACTD [has_mechanism:: STCK]
- CTMN-ACTD [has_mechanism:: LEAK]
- CTMN-ACTD [has_mechanism:: WEAR]
- CTMN-ACTD [has_mechanism:: OPEN]
- CTMN-ACTD [has_mechanism:: OTHR]
- CTMN-CICV [part_of:: [[CTMN Control and Monitoring]]]
- CTMN-CICV [is_a:: CICV]
- CTMN-CICV [has_value:: 5] CAUSE_CODE
- CTMN-CICV [has_mechanism:: OADJ]
- CTMN-CICV [has_mechanism:: FSIG]
- CTMN-CICV [has_mechanism:: LEAK]
- CTMN-CICV [has_mechanism:: STCK]
- CTMN-CICV [has_mechanism:: CTMN]
- INST [part_of:: [[CTMN Control and Monitoring]]] failure-structure.md Sheet1, all instrument types [contested:: true]
- INST [has_failure_rate_share:: 23.34%] all modes (derived); under Sheet1 view goes to CTMN, making CTMN largest sub unit instead of CPUN [contested:: true]
- [[CTMN Control and Monitoring]] [contributes_to:: [[AIR Abnormal Instrument Reading]]] 2.33% counted at CTMN (derived), of 85.66
- [[CTMN Control and Monitoring]] [contributes_to:: [[OTH Other]]] 0.89% counted at CTMN (derived), of 85.66
- [[CTMN Control and Monitoring]] [contributes_to:: [[UST Spurious Stop]]] 0.88% counted at CTMN (derived), of 85.66
- [[CTMN Control and Monitoring]] [contributes_to:: [[PDE Parameter Deviation]]] 0.83% counted at CTMN (derived), of 85.66
- [[CTMN Control and Monitoring]] [contributes_to:: FTS] 0.79% counted at CTMN (derived), of 85.66
- [[CTMN Control and Monitoring]] [contributes_to:: [[SER Minor In-Service Problems]]] 0.40% counted at CTMN (derived), of 85.66
- [[CTMN Control and Monitoring]] [contributes_to:: STP] 0.22% counted at CTMN (derived), of 85.66
- CTMN-MONI [contributes_to:: [[AIR Abnormal Instrument Reading]]] 0.97%
- CTMN-CTUN [contributes_to:: [[AIR Abnormal Instrument Reading]]] 0.84% (Software failure)
- CTMN-CTUN [contributes_to:: [[UST Spurious Stop]]] 0.53%
- CTMN-CTUN [contributes_to:: FTS] 0.53%
- CTMN-CTUN [contributes_to:: [[PDE Parameter Deviation]]] 0.40%
- [[CTMN Control and Monitoring]] [has_mechanism:: SWFL] top mechanism
- [[CTMN Control and Monitoring]] [has_mechanism:: FSIG] top mechanism
- [[CTMN Control and Monitoring]] [has_mechanism:: OPEN] top mechanism; cabling
- [[CTMN Control and Monitoring]] [has_mechanism:: NPWR] top mechanism; power supply
- [[CTMN Control and Monitoring]] [has_mechanism:: STCK] top mechanism; actuating device

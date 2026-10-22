# ISO 14224:2016 Annex B (normative): การตีความและรหัสของ failure และ maintenance (printed p.176-204)

Source: ISO 14224:2016 (3rd edition), reading notes ที่ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ printed page (PDF page = printed + 6)

ขอบเขต: PDF p.182-210 = printed p.176-204 เนื้อหาถอดความ (paraphrase) ทั้งหมด ตารางรหัสให้เฉพาะรหัส + ชื่อสั้น + ความหมายสั้นๆ ของผู้จดเอง

## B.1 การตีความ failure (p.176-177)

- failure ปรากฏได้หลายแบบ: สูญเสียหน้าที่ทั้งหมด, หน้าที่ลดต่ำกว่าเกณฑ์ หรือมีความผิดปกติเริ่มต้น (incipient) ที่ถ้าไม่แก้จะกลายเป็น functional failure (ISO 14224 cl. B.1, p.176)
- แยกจุดประสงค์การเก็บข้อมูล: **reliability** สนใจ intrinsic/physical failure ที่ต้องมี corrective maintenance; **availability** ต้องเก็บทุกเหตุที่ทำให้ outage รวม trip จาก operating limit ที่ไม่มี physical failure (cl. B.1, p.176)
- ช่วงที่ไม่มี failure ก็ยังมีค่า เพราะใช้ประมาณ failure rate ด้วย censored data (cl. B.1, p.176)
- incipient failure ที่เลื่อนการแก้ไข (opportunity maintenance): บันทึกทั้งวันที่ตรวจพบและวันที่แก้ ใช้วันแก้ในการวิเคราะห์ตามปกติ (cl. B.1, p.176)
- Table B.1 (p.177) สรุป: trip จาก external condition/operating error ที่ไม่มี physical failure และ failure จาก external impact (เช่น ไฟดับ) = นับเฉพาะ availability ไม่นับ reliability; เปลี่ยน consumable/wear part ตามรอบ = ไม่นับทั้งสอง; on-demand activation = นับทั้งสอง; modification ไม่ใช่ maintenance

## B.2.1 หลักการใช้รหัส (p.177-178)

- ใช้รหัสเพื่อลดขนาดฐานข้อมูลและวิเคราะห์ง่าย แต่ต้องเสริมด้วย free text เสมอ (cl. B.2.1, p.177)
- record failure ต้องมี: เวลา/วันที่, failure mode (B.2.6), failure mechanism (B.2.2), failure cause/root cause (B.2.3), detection method (B.2.4), maintenance activity (B.2.5)
- **กติกาเลือกระดับ**: ใช้รหัส subdivision (1.1, 1.2...) ก่อนรหัสหมวดใหญ่ (1 / 1.0) เสมอ ใช้หมวดใหญ่เฉพาะเมื่อข้อมูลไม่พอ ใช้ทั้งกับ mechanism และ cause (cl. B.2.1, p.178; cl. B.2.2, p.178)
- ความสัมพันธ์ระดับ taxonomy ของ mode/mechanism/cause อ้าง Table 3 (main body)

## B.2.2 Failure mechanism (p.178-180, Table B.2)

นิยาม (ถอดความ): กระบวนการทางกายภาพ เคมี หรืออื่นๆ ที่นำไปสู่ failure เป็น "สาเหตุที่เห็นได้/สังเกตได้" (apparent cause) ที่อนุมานทางเทคนิคได้ ส่วน root cause บันทึกแยกฟิลด์ (cl. B.2.2, p.178)

ประเด็นสำคัญ:
- mechanism ควรผูกกับระดับต่ำกว่า equipment (subunit หรือ maintainable item); ในทางปฏิบัติ **mechanism = failure mode ที่ระดับ maintainable item** (cl. B.2.2, p.178)
- ต้องแยก mechanism กับ mode ให้ชัด ตัวอย่างในมาตรฐาน: valve รั่ว hydrocarbon ออกภายนอกโดยไม่รู้สาเหตุ -> mode = ELP, mechanism = **6.4 Unknown** ไม่ใช่ 1.1 Leakage (cl. B.2.2, p.178) คือห้ามเอาอาการซ้ำเป็น mechanism
- ถ้ามีหลาย mechanism ให้ผู้เก็บข้อมูลเลือกตัวสำคัญที่สุด และพยายามเลี่ยง 6.3/6.4 (Table B.2 fn a)
- **human error ไม่อยู่ใน mechanism** แต่อยู่ใน failure cause (Table B.2 fn b)

Table B.2 (p.179-180) 6 หมวด 38 รหัส:

| หมวด | รหัส subdivision (ความหมายสั้น) |
|---|---|
| 1 Mechanical failure | 1.0 General; 1.1 Leakage (รั่วภายใน/ภายนอก ถ้า mode เป็น leakage ให้หา mechanism เชิงสาเหตุแทน); 1.2 Vibration (ถ้า mode เป็น vibration ให้บันทึก root cause); 1.3 Clearance/alignment failure; 1.4 Deformation (งอ บิด ยุบ creep); 1.5 Looseness; 1.6 Sticking (ติด/seize ที่ไม่ใช่จาก deformation หรือ clearance) |
| 2 Material failure | 2.0 General; 2.1 Cavitation; 2.2 Corrosion (เปียก/แห้ง); 2.3 Erosion; 2.4 Wear (abrasive/adhesive); 2.5 Breakage (แตก ร้าว); 2.6 Fatigue (ใช้เมื่อสืบได้ว่า breakage มาจาก fatigue); 2.7 Overheating (วัสดุเสียหายจากความร้อน); 2.8 Burst |
| 3 Instrument failure | 3.0 General; 3.1 Control failure; 3.2 No signal/indication/alarm; 3.3 Faulty signal/indication/alarm (รวม spurious/intermittent); 3.4 Out of adjustment (calibration drift); 3.5 Software error; 3.6 Common cause/Common mode failure (instrument หลายตัวเสียพร้อมกัน) |
| 4 Electrical failure | 4.0 General; 4.1 Short circuiting; 4.2 Open circuit; 4.3 No power/voltage; 4.4 Faulty power/voltage; 4.5 Earth/isolation fault |
| 5 External influence | 5.0 General; 5.1 Blockage/plugged (fouling, hydrate, icing); 5.2 Contamination; 5.3 Miscellaneous external influences (foreign object, impact) |
| 6 Miscellaneous | 6.0 General; 6.1 No cause found (สืบแล้วไม่พบ); 6.2 Combined causes (ถ้ามีตัวเด่นให้ใช้ตัวนั้น); 6.3 Other (ใช้ free text); 6.4 Unknown (ไม่มีข้อมูล) |

หมายเหตุ: มาตรฐานใช้รหัสตัวเลขเท่านั้น ไม่มีรหัส 4 ตัวอักษร (LEAK, WEAR...) Burst อยู่หมวด Material

## B.2.3 Failure cause (p.180-182, Table B.3)

- จุดประสงค์: หา initiating event / root cause ในลำดับเหตุการณ์ (cl. B.2.3.1, p.180) บันทึกได้ 2 ระดับเช่นเดียวกับ mechanism
- มักไม่รู้ root cause ตอนพบ failure; แนะนำทำ RCA สำหรับ failure ที่ซับซ้อน ผลกระทบสูง failure rate ผิดปกติ หรือค่าซ่อมสูง (p.181)
- ย้ำ: mechanism = สาเหตุที่สังเกตได้, cause = สาเหตุแท้ (root) อย่าสับสน (p.181)

Table B.3 (p.181-182) 5 หมวด 21 รหัส:

| หมวด | รหัส |
|---|---|
| 1 Design-related | 1.0 General; 1.1 Improper capacity; 1.2 Improper material |
| 2 Fabrication/installation-related | 2.0 General; 2.1 Fabrication failure; 2.2 Installation failure (ไม่รวมประกอบหลังซ่อม) |
| 3 Operation/maintenance | 3.0 General; 3.1 Off-design service (เช่น compressor เดินนอก envelope); 3.2 Operating error; 3.3 Maintenance error; 3.4 Expected wear and tear |
| 4 Management | 4.0 General; 4.1 Documentation error; 4.2 Management error |
| 5 Miscellaneous | 5.0 General; 5.1 No cause found; 5.2 Common cause; 5.3 Combined causes; 5.4 Other unit/cascading failure; 5.5 Other; 5.6 Unknown (พยายามเลี่ยง 5.5/5.6) |

**Common cause failure (cl. B.2.3.2, p.182)**:
- ถ้า CCF เกิดที่ระดับเดียวกับหรือสูงกว่าระดับที่เก็บข้อมูล: บันทึก failure แยกทุก item แต่ใส่ cause จริงเพียง item เดียว (ตัวแรก/เสียหนักสุด หรือสุ่ม) ที่เหลือใส่ cause = common cause; ใช้กับ driver/driven หรือ rotating equipment ขนานกันด้วย
- ถ้าเสียหลายจุดที่ระดับต่ำกว่าหน่วยที่เก็บข้อมูล: บันทึก failure เดียว ระบุ subunit = "several" หรือ list ทั้งหมด (เช่น lube oil ปนเปื้อนทำให้หลาย subunit เสีย)
- failure ที่ตามกันเป็นลูกโซ่ไม่ใช่ CCF: บันทึกเฉพาะตัวแรก เช่น lube oil pump เสียแล้ว bearing ร้อนเกิน -> บันทึกที่ lubrication subunit เท่านั้น

## B.2.4 Detection method (p.182-183, Table B.4)

ข้อความระบุ 9 หมวด แต่ตารางมี **11 รหัส** (ความไม่สอดคล้องภายในมาตรฐาน): 1 Periodic maintenance; 2 Functional testing (วิธีหลักหา hidden failure); 3 Inspection; 4 Periodic condition monitoring; 5 Pressure testing; 6 Continuous condition monitoring; 7 Production interference; 8 Casual observation; 9 Corrective maintenance; 10 On demand; 11 Other. กลุ่มกิจกรรม: scheduled (1-5), continuous (6-7), casual (8-10), other (11) (Table B.4, p.183) มีการตีความพิเศษสำหรับ F&G detector/sensor/logic (fn a)

## B.2.5 Maintenance activity (p.183-185, Table B.5)

12 รหัส (C = ใช้ใน corrective, P = preventive):

| Code | Activity | ความหมายสั้น | ใช้ |
|---|---|---|---|
| 1 | Replace | เปลี่ยนด้วยของชนิด/ยี่ห้อเดิม (ใหม่หรือ refurbished) | C,P |
| 2 | Repair | ซ่อมให้กลับสภาพเดิม (weld, repack) | C |
| 3 | Modify | เปลี่ยนเป็นชนิด/วัสดุ/design อื่น | C,P |
| 4 | Adjust | ปรับให้อยู่ในพิกัด (align, calibrate, balance) | C,P |
| 5 | Refit | งานเล็กให้สภาพยอมรับได้ (ขัด ทำความสะอาด ทาสี หล่อลื่น เปลี่ยนน้ำมัน) | C,P |
| 6 | Check | ตรวจหาสาเหตุแต่ไม่ซ่อมหรือเลื่อนไป; restart/reset ก็คืนหน้าที่ได้ | C |
| 7 | Service | งาน service ตามรอบ ไม่รื้อ | P |
| 8 | Test | ทดสอบ function/performance ตามรอบ | P |
| 9 | Inspection | ตรวจตามรอบ อาจรื้อหรือไม่ | P |
| 10 | Overhaul | overhaul ใหญ่ รื้อมาก | C,P |
| 11 | Combination | หลาย activity ไม่มีตัวเด่น | C,P |
| 12 | Other | อื่นๆ | C,P |

กติกา (p.184-185): บันทึก activity ที่เด่นที่สุด; Repair/Replace/Overhaul/Modify มี priority เหนือ Refit/Adjust; Check ครอบคลุมทั้งกรณีพบสาเหตุแต่ไม่ต้อง/ไม่สามารถซ่อม และกรณีไม่พบสาเหตุเลย (fn c); ถ้าเปลี่ยนทั้ง equipment unit ให้ reset เวลาเดินเครื่อง (ยกเว้นของง่าย); รหัสไม่ได้บอกว่า restore เป็น good-as-new หรือ bad-as-old

## B.2.6 Failure modes (p.185-204, Tables B.6-B.15)

- ปกติผูกกับ **ระดับ equipment class** (subsea แนะนำให้บันทึกที่ maintainable item ด้วย) (cl. B.2.6, p.185)
- 3 ประเภท: (a) ไม่ได้หน้าที่ที่ต้องการ (เช่น fail to start), (b) หน้าที่หายหรือหลุดเกณฑ์ (เช่น spurious stop, high output), (c) เห็นอาการแต่ยังไม่กระทบวิกฤต (degraded/incipient) (p.185)
- OTH/UNK ใช้เมื่อไม่มี mode ตรง; ถ้า OTH สะสมมาก อาจเป็นฐานของ mode ใหม่ (p.185); รหัสมีใน Excel ที่ standards.iso.org/iso/14224 (p.186)

### Table B.6 Rotating equipment (p.187) และ compressor (CO)

Classes: CE combustion engines, CO compressors, EG electric generators, EM electric motors, GT gas turbines, PU pumps, ST steam turbines, TE turbo-expanders มี 21 รหัส

**Compressor (CO) ใช้ 20 รหัส**: AIR, BRD, ERO, ELP, ELU, FTS, HIO, INL, LOO, NOI, OHE, PDE, **PLU**, SER, STD, STP, OTH, UNK, **UST**, VIB. รหัสเดียวในตารางที่ CO ไม่ใช้คือ **ELF** (External leakage - fuel ใช้กับ CE, GT, ST เท่านั้น)

ตารางมีคอลัมน์ CO เดียว **ไม่แยก centrifugal/reciprocating/screw** (การแยกตามชนิดอยู่ใน Annex A taxonomy ไม่ใช่ใน failure mode table)

รหัสที่ใช้ไม่ครบทุก class (ตรวจจากตำแหน่ง X ใน PDF): ERO และ HIO ไม่ใช้กับ EG; ELP ใช้ CO, GT, PU, ST, TE; INL และ PLU ใช้ CE, CO, GT, PU, ST, TE; STP ใช้ CE, CO, EG, EM; ที่เหลือใช้ทั้ง 8 class

### รหัสทั้งหมด (Table B.15 overview, p.202-204): 62 รหัส

AIR Abnormal instrument reading; BRD Breakdown; CLW Control-line-to-well communication; CSF Control/signal failure; DOP Delayed operation*; ELF External leakage - fuel; ELP External leakage - process medium; ELU External leakage - utility medium; ERO Erratic output; FCO Failure to connect*; FCU Failure to cut*; FLP Failure in lightning protection system; FOF Faulty output frequency; FOV Faulty output voltage; FRO Failure to rotate; FTC Failure to close on demand*; FTD Failure to disconnect*; FTF Failure to function on demand*; FTI Failure to function as intended*; FTL Failure to lock/unlock*; FTO Failure to open on demand*; FTR Failure to regulate*; FTS Failure to start on demand*; FWR Failure while running; HIO High output; HTF Heating failure; IHT Insufficient heat transfer; ILP Internal leakage - process medium; ILU Internal leakage - utility medium; INL Internal leakage; LBP Low oil supply pressure; LCP Leakage in closed position; LOA Load drop; LOB Loss of buoyancy; LOO Low output; MOF Mooring failure; NOI Noise; NOO No output; OHE Overheating; OTH Other; PCL Premature closure; PDE Parameter deviation; PLU Plugged/choked; POD Loss of functions on both pods*; POW Insufficient power; PTF Power/signal transmission failure; SBU Sludge build-up; SER Minor in-service problems; SET Failure to set/retrieve*; SHH Spurious high alarm level; SLL Spurious low alarm level; SLP Slippage; SPO Spurious operation; STD Structural deficiency; STP Failure to stop on demand*; STU Stuck; UBU Global buckling; UNK Unknown; UST Spurious stop; VIB Vibration; VLO Very low output; WCL Well-to-control-line communication

(* = มาตรฐานติดธงเป็น on-demand type failure 14 รหัส)

Tables ต่อกลุ่ม: B.7 Mechanical (CR, HE, HB, PI, VE, WI, TU, SW, TA) p.188-189; B.8 Electrical (UP, PT, FC, SG) p.190-191; B.9 Safety & control (FGA, FGB, IP, CL, VA, NO, LB) p.192-194 พร้อม note เกณฑ์ %LEL ของ gas detector สำหรับ HIO/LOO/VLO/NOO; B.10 Subsea (CS, XT, SP, PR, EPD, SV, SL) p.195-196; B.11 Well completion (ESP, SS, XD) p.197-198; B.12 Drilling (TD, SB, DB) p.199-200; B.13 Well intervention (WC, OI) p.201; B.14 Marine (JF) p.202

### ตัดสิน UST vs SPS และ OWD

- **Spurious stop = UST** ใน ISO 14224:2016 (Tables B.6, B.8, B.9, B.11, B.14, B.15) **ไม่มีรหัส SPS** ในฉบับนี้
- UST ใช้กับ: rotating ทั้ง 8 class (รวม CO และ EM), FC (unexpected shutdown), SG (ตัดวงจรโดยไม่ตั้งใจ), LB lifeboats, ESP, JF
- **ไม่มีรหัส OWD** ในฉบับ 2016 เลย (ไม่อยู่ใน Table B.15) ความหมายใกล้เคียงคือ **SPO Spurious operation** (ทำงานเองโดยไม่ได้สั่ง) ใช้กับ mechanical/electrical/safety/subsea/well/drilling/marine แต่ **ไม่อยู่ใน Table B.6 rotating** Electric motor ในฉบับ 2016 ใช้ UST ไม่ใช่ OWD

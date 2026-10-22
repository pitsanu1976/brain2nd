# ISO 14224:2016 reading notes 06: Annex E (KPIs & benchmarking) และ Annex F (safety critical failures)

Source: ISO 14224:2016 (3rd edition), reading notes ที่ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ printed page (PDF page = printed + 6)

ช่วง: PDF p.244-265 = printed p.238-259 ทั้งสอง Annex เป็น informative (ไม่บังคับ)

## Annex E: KPIs และ Benchmarking

### E.1 กระบวนการ (ISO 14224 cl. E.1, p.238-239)

วงจร 5 ขั้น (Figure E.1): (a) benchmark ผลงานเทียบภายนอก (b) หาพื้นที่ต้องปรับปรุง (c) สร้าง KPI พร้อมเป้า (d) วัด KPI เทียบเป้าและหาสาเหตุที่เบี่ยง (e) แก้ไข แล้ววนซ้ำ
- คุณค่าของ benchmark ไม่ใช่แค่วัด gap แต่คือการวิเคราะห์ causal factors (ลักษณะโรงงาน วิธีปฏิบัติ องค์กร) ที่อธิบาย gap
- จุดที่ผลงานแย่เทียบคนอื่นไม่จำเป็นต้องเป็นจุดที่ต้องแก้ก่อน ถ้าไม่ใช่เรื่องสำคัญต่อเป้าธุรกิจ
- benchmark ใช้เป็น business case เพื่อขอ commitment/ทรัพยากรจากผู้บริหาร ทำได้ภายในบริษัท ในอุตสาหกรรม หรือข้ามอุตสาหกรรม (ถ้า process เดียวกัน)
- KPI ควรเป็นแบบ SMART; ความถี่การวัดเลือกตามเวลาที่การแก้ไขจะเห็นผล (ถี่ไปไม่เห็นการเปลี่ยน ห่างไปปล่อยหลุดการควบคุมนาน) และนับต้นทุนการดูแล KPI ด้วย ซึ่งจำกัดจำนวน KPI ที่ดูแลได้ดี
- วัดในระบบที่มีอยู่เดิมให้มากที่สุด; ผู้ผลิตอุปกรณ์ก็ใช้แนวเดียวกันรายงาน performance จริงเทียบ design ได้ แต่ต้องใช้ boundary/นิยาม/คุณภาพข้อมูลตามมาตรฐานนี้

### E.2 KPI กับ Benchmark ต่างกันอย่างไร (ISO 14224 cl. E.2.2, Table E.1, p.240)

ต่างกันที่การใช้งาน: KPI ใช้ติดตามการปรับปรุงต่อเนื่องเทียบเป้าที่ตั้งไว้; benchmark เป็นเหตุการณ์ครั้งเดียว/นาน ๆ ครั้ง เพื่อดูระดับตัวเองเทียบองค์กรอื่น สรุป Table E.1 (สรุปเอง):

| ลักษณะ | KPI | Benchmark |
|---|---|---|
| จุดประสงค์ | ติดตามความคืบหน้า/ประสิทธิผลการบริหาร | หา gap ของผลงานปัจจุบัน |
| ความถี่ | ตามช่วงที่คาดว่าจะเห็นการเปลี่ยน | ครั้งเดียว/ไม่บ่อย |
| แหล่งข้อมูล | ระบบภายใน | ภายนอก |
| ช่วงควบคุม | ทันที-ระยะสั้น | ระยะยาว |
| ตัวแปรที่มีผล | หนึ่งหรือไม่กี่ตัว | หลายตัว |
| ความแม่น | สนใจแนวโน้ม | สนใจค่าสัมบูรณ์ |
| เป้า | มี ตามวัตถุประสงค์ | ไม่มี |

### E.3 หลักการ benchmarking (ISO 14224 cl. E.3, p.240-243)

- 3 ขั้น: ประเมินตัวเองด้วยข้อมูลตาม Clause 7-9 และเลือกชุด KPI; ศึกษาเทียบ peer group ที่ดีกว่า; นำ best practice มาใช้ (E.3.1)
- ต้องมีกลุ่มตัวอย่างใหญ่พอทางสถิติ และเข้าใจข้อจำกัดของข้อมูล ตัวอย่างในมาตรฐาน: bearing อายุต่างกันมากตาม load/speed/lubrication ฯลฯ ค่า MTTF เฉลี่ยทั้งโรงงานจึงมีประโยชน์จำกัด การไล่ตามคู่แข่งต้องรู้ความต่างของ design และ operating condition (E.3.2)
- การใช้ผิดที่พบบ่อย: ใช้ benchmark เป็น scorecard มองย้อนหลัง แทนที่จะเป็นแผนที่นำทางไปข้างหน้า (E.3.2)
- Taxonomy level (E.3.3): benchmark ทำได้ที่ plant, process unit, equipment class, subunit, maintainable item ถ้าระดับหนึ่งชี้จุดอ่อน ให้ลงไปดู KPI ระดับถัดลงไปเพื่อหาสาเหตุ ระดับ plant/unit มักดู reliability, staffing, utilization, operating cost ระดับ equipment class ลงไปเน้นอุบัติการณ์ failure และ repair
- ชุด benchmark หลัก (E.3.4): MTTF ระดับ equipment class/subunit/MI, availability, ต้นทุน production loss จาก unreliability และงานบำรุงรักษา, direct maintenance cost (คน สัญญา วัสดุ), ต้นทุน support staff และวัสดุสิ้นเปลือง, การทำงานตามแผน
- E.3.5: ผู้ร่วม benchmark ต้องใช้กรอบอ้างอิงเดียวกัน (นิยาม boundary ตามมาตรฐานนี้, ช่วงเวลาเดียวกัน)
- E.3.6: ประโยชน์ครอบคลุม 9 work process (strategy, work management, PdM/PM, CMMIS, training, materials, contractor, reliability improvement, technology); เตือนไม่ให้โฟกัส KPI แค่ 1-2 ตัว
- E.3.7 Peer group: ปัจจัยแบ่งกลุ่มคือสิ่งที่โรงงานเปลี่ยนไม่ได้ในระยะสั้น-กลาง สองปัจจัยสำคัญที่สุดคือ process family (ชนิดอุปกรณ์ ความรุนแรงของ process ความซับซ้อนงานซ่อม) และ geographic region (ค่าแรง แนวจ้างงาน กฎ HSE ภูมิอากาศ วัฒนธรรม) gap แยกเป็นจากลักษณะกายภาพ และจากวิธีปฏิบัติ/องค์กร

### E.4 ตัวอย่าง KPI (ISO 14224 cl. E.4, Tables E.2-E.3, p.243-250)

ไม่มี KPI ตัวเดียวที่บอกครบ ต้องใช้ "basket" ของ KPI Table E.2 ทวนระดับ taxonomy 1-9 (Industry ... Part) ใช้ระบุว่า KPI ใช้ที่ระดับใด (สรุปเอง คำอธิบายย่อ):

| # | KPI | ระดับ | วัดอะไร (สรุป) |
|---|---|---|---|
| 1 | METBF | 6-8 | เวลาเฉลี่ยระหว่างเสีย รวม downtime |
| 2 | MTTF | 6-8 | เหมือน METBF แต่ไม่รวม downtime; METBF = MTTRes + MTTF; MTTF = 1/failure rate; โดยหลักคือเวลาถึงการเสียครั้งแรกของของใหม่ |
| 3 | MTBR (subsea: MTBI) | 6-8 | เวลาเฉลี่ยระหว่างการซ่อม รวมการ overhaul ตามเวลาที่ไม่ได้เกิดจาก failure |
| 4 | MART | 6-8 | เวลาซ่อมจริง (active) |
| 5 | MRT | 6-8 | เวลาเตรียม + ซ่อม; MDT ใช้เพิ่มได้ถ้าสนใจเวลารอ |
| 6 | Worst actors | 6-9 | รายการอุปกรณ์/failure mode ที่เสียบ่อย ใช้นำ RCA |
| 7 | AO operational availability | 6 | % เวลาพร้อมใช้ เมื่อนับ downtime ทั้ง CM และ PM |
| 8 | AT technical availability | 6 | % เวลาพร้อมใช้ เมื่อนับเฉพาะ downtime จาก corrective สะท้อน intrinsic reliability |
| 9 | SCE ที่มี assurance task ใน CMMS | 4-6 | % ของ SCE ที่มี task (top quartile 100%) |
| 10 | SCE PM compliance | 4-6 | งาน PM ของ SCE เสร็จก่อน latest allowable finish date (TQ >98%) |
| 11 | SCE CM compliance | 4-6 | เหมือนข้อ 10 สำหรับงาน corrective (TQ >98%) |
| 12 | PM man-hours ratio | 4-6 | % ชั่วโมงงาน PM ต่อชั่วโมงงานทั้งหมด (ไม่รวม modification) |
| 13 | Corrective man-hours ratio | 4-6 | % ชั่วโมงงาน corrective |
| 14 | Overdue SCE WO ไม่มี TA approval | 4-6 | จำนวนงาน SCE เลยกำหนดโดยไม่มี Technical Authority อนุมัติ (TQ 0) |
| 15 | PMs overdue | 4-6 | backlog PM, แยกกลุ่ม safety/production critical ได้ |
| 16 | PdM complete | 4-6 | % งานเก็บข้อมูล PdM/NDT ที่ทำเสร็จ |
| 17 | PdM overdue | 4-6 | backlog งาน PdM |
| 18 | Corrective maintenance workload | 4-6 | ชั่วโมงงาน CM สะสม (TQ < 6 man-weeks) |
| 19 | Schedule compliance | 4-6 | % ชั่วโมงตามตารางที่ทำเสร็จ rolling 3 เดือน (TQ >98%) |
| 20 | Unscheduled/fill-in work | 4-6 | % ชั่วโมงงานนอกตาราง (TQ <2%) |
| 21 | Turnaround duration | 4 | วัน รวม run-down/start-up, แยก TA ที่ยืดเพราะ modification |
| 22 | Time between turnarounds | 4-5 | เดือน/ปี |
| 23-24 | Estimating accuracy (hours, cost) | 4-6 | % ต่างระหว่างแผนกับจริง (TQ ±5%) |
| 25 | Repair rework ratio | 6 | % WO ที่ต้องทำซ้ำ (คุณภาพงาน) |
| 26 | CMMS confirmed to technical completion time | 4-6 | เวลาจากงานเสร็จถึงปิด WO ทางเทคนิค (TQ 24 ชม.) |
| 27 | Average repair workshop cycle time | 6-8 | เวลาของเสียอยู่ใน workshop จนพร้อมใช้ |
| 28 | Generic material ordering | 4-6 | สัดส่วนวัสดุที่เบิก (TQ <10%) วัดความครบของ material catalogue |
| 29 | Materials achieving RoS date | 4-6 | % วัสดุถึงไซต์ตาม required-on-site date (TQ >95%) |
| 30 | Inventory service level | 4-6 | % ความต้องการวัสดุที่จ่ายได้จาก stock |
| 31 | Total maintenance cost | 4-6 | CM+PM รวมอะไหล่ ไม่รวม production loss |
| 32 | Maintenance productivity | 4 | % ชั่วโมงที่เสียไปกับงานไม่สร้างคุณค่า (รอวัสดุ ฯลฯ) |
| 33 | Cost of repairs per WO | 4-6 | ต้นทุนซ่อมต่อ WO (คน วัสดุ เช่าเครื่อง) ใช้หา worst actor ด้านต้นทุน |
| 34 | Failure fraction | 6 | สัดส่วน safety critical failure ที่พบในการ test ต่อจำนวน test (ดู F.4) ติดตามรายปี |

หมายเหตุอ่านต้นฉบับ: ใน Table E.3 ตัวเลข top quartile บางข้อดูขัดกับนิยามของตัวเอง เช่น ข้อ 28 (นิยามคือ % ที่ "ระบุใน CMMS" แต่เป้า <10%), ข้อ 30 (service level แต่เป้าเขียน ±5%), ข้อ 32 (นิยาม % non-productive แต่เป้า >50%) ควรระวังเวลานำไปใช้ (ข้อสังเกตของผู้อ่าน) footnote c: ในมาตรฐานนี้ "CM" = condition monitoring ไม่ใช่ corrective maintenance (Table E.3 fn c, p.244)

## Annex F: การจำแนกและนิยาม safety critical failures

### F.1-F.2 บริบท (ISO 14224 cl. F.1-F.2, p.251)

- ให้ผู้ใช้รู้จักนิยามเฉพาะของ safety critical equipment ซึ่งอิง IEC 61508 / IEC 61511 (functional safety) และแนวทางระดับชาติ (เช่น Norwegian Oil and Gas Association guideline)
- ISO/TR 12489:2013 เป็นเอกสารหลักสำหรับ reliability modelling ของ safety system (ESD, HIPPS) ใช้สูตรอย่างง่ายและโมเดล RBD (IEC 61078), fault tree (IEC 61025), Markov (IEC 61165), Petri net (IEC 62551); ขยายวิธีคำนวณ SIL ของ IEC 61508-6 Annex B
- TR 12489 Annex A มี 31 ระบบที่มี safety function พร้อมโยง equipment class ของ ISO 14224; Annex D.5 ของ ISO 14224 จัดประเภทแหล่งข้อมูล reliability

### F.3 การจำแนก failure ของ SIS (ISO 14224 cl. F.3, p.252-253)

- SIS ส่วนใหญ่ "dormant" อยู่เฉย ๆ จนถูกเรียก จึงต้องหา hidden failure ให้เจอก่อนเกิด demand
- คำศัพท์ (F.3.1): dangerous failure = ขัดขวาง safety action; safe failure = ส่งเสริม safety action (เช่น trip เอง); no-effect = ไม่กระทบความปลอดภัย; intrinsically fail-safe system = ออกแบบให้ dangerous failure น้อยจนละได้; non-intrinsically fail-safe = ละไม่ได้; immediately revealed vs hidden failure (hidden พบได้ด้วย periodic test)
- F.3.2 ตาม IEC 61508: แยก random กับ systematic failure ก่อน แล้วแบ่ง random เป็น 4 กลุ่ม: DD, DU, SD, SU
- ข้อมูลที่เก็บอาจไม่มีเหตุการณ์ครบทั้ง 4 กลุ่ม ต้องตั้งสมมติฐานอย่างระวังกับกลุ่ม "zero failure" และต้องเข้าใจพฤติกรรมทางกายภาพของอุปกรณ์เพื่อจัด failure mode ลงกลุ่มให้ถูก
- สองเรื่องที่ต้องเน้นเมื่อเก็บข้อมูล SIS: common cause failures (ดู C.1.6) และ periodic test interval สำหรับหา DU failure
- ข้อมูลรองรับ: Table 5 มีฟิลด์บันทึก DD/DU/SD/SU; Table B.15 ระบุ demand-related failure modes; CCF บางส่วนเป็น systematic จึงไม่นับใน 4 กลุ่ม random
- F.3.3 Downtime: MTTRes = MFDT + MRT; สำหรับ DD (พบด้วย diagnostics) MFDT เล็กมาก ถือว่า MTTRes ใกล้ MRT ได้ (p.253)

### F.4 นิยาม failure ของ safety system และ "failure fraction" (ISO 14224 cl. F.4, p.253-254)

- การใช้นิยามมาตรฐาน (Table F.1) ร่วมกันทำให้ benchmark ด้าน safety ข้ามบริษัทได้; failure ที่ undetected มักเรียกว่า safety critical failure และมีการรายงานต่อ regulator
- ตาม TR 12489: dangerous failure ที่ทำให้ SIF ใช้ไม่ได้ = safety critical failure ของ SIF นั้น
- Failure fraction = จำนวน safety critical failure ที่พบจาก periodic test / จำนวน test เป็น instantaneous unavailability ณ เวลาทดสอบ และเป็นค่าประมาณแบบ conservative ของ PFDavg ห้ามสับสนกับ safe failure fraction (SFF) ของ IEC 61508-4
- คำว่า "critical" สองความหมาย: ISO 14224 = ระดับ failure impact ของอุปกรณ์ (critical/degraded/incipient, cl. 3.28) ไม่ขึ้นกับอุปกรณ์อื่น; TR 12489 = ทำให้ SIF ใช้ไม่ได้ทั้งหมด ตัวอย่าง SIF มี A กับ B redundant: dangerous failure ของ A เป็น "critical" ตาม TR 12489 ก็ต่อเมื่อเป็น critical ตาม ISO 14224 และ B เสียแบบ dangerous critical อยู่ก่อนแล้ว
- นักวิเคราะห์ต้องเลือก failure mode ที่เกี่ยวกับ safety function และครอบคลุม item ใน boundary ที่จำเป็นทั้ง detection, decision, action

### F.4.2 Table F.1 นิยาม failure ที่พบจากการ test (p.254-259)

42 รายการ เกณฑ์ทั่วไปคือ "ไม่ทำงานเมื่อถูก test/สั่ง หรือทำงานไม่ทันเวลาที่กำหนด" สรุปกลุ่ม (ไม่ลอกทั้งตาราง):
- Fire & gas detection, manual call point, ESD push button, input devices: logic ไม่ได้รับสัญญาณ/สัญญาณผิด → NOO, LOO, FTF (input devices เพิ่ม ERO, HIO)
- Deluge, sprinkler, gaseous agent, water mist, foam, monitor, blowdown valve: ไม่เปิดเมื่อ test → FTO, DOP; nozzle อุดเกิน 3% → PLU
- Fire pump: ไม่ start (FTS) หรือ capacity ต่ำกว่า 90% design (LOO)
- ESD/process safety valves (sectioning, riser, wellhead/X-mas tree, DHSV, ASV, GLV ที่เป็น barrier), BOP: ไม่ปิดตามเวลา → FTC, DOP; รั่วเกินเกณฑ์ → LCP
- PSV: ไม่เปิดที่ค่าน้อยกว่าระหว่าง 120% set pressure กับ set + 5 MPa → FTO
- HIPPS: ไม่ไปตำแหน่ง safe ตามเวลา (FTO/FTC/DOP) หรือรั่วเกิน (LCP)
- Emergency generator (FTS, LOO), UPS (LOC; emergency light ต้องได้อย่างน้อย 30 นาที), PA/siren, fire damper, HVAC safety transmitter/switch (±5%), ballast, watertight door/damper, lifeboat, escape chute, MOB boat
- Footnote: failure เกิดได้ทั้งตอน test และ demand จริง; INL (รั่วของ utility fluid) ไม่เท่ากับ LCP (hydrocarbon รั่วผ่านบ่าวาล์ว) และไม่ใช่ dangerous ใน fail-safe design; DHSV leak test ให้รายงาน initial leak rate และบันทึกวิธีวัด

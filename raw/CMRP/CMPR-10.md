# CMPR-10: Backlog, Schedule Compliance, Planning/Schedule Metrics และ Turnaround Strategy

Source: PETROSYNC CMRP training course slides, file CMPR-10.pdf (scanned, OCR). Reading notes ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ PDF page `(CMRP CMPR-10 p.N)`

ขอบเขต: PDF 30 หน้า (2 slide ต่อหน้า, เลข slide ในคู่มือ 357-386) p.1-9 = backlog, schedule compliance, metrics; p.9-30 = turnaround (เหตุผลเชิงธุรกิจ, กลยุทธ์ระดับผู้บริหาร, work scope, organization) OCR อ่านได้ดีเกือบทั้งไฟล์ มีขยะจาก margin/โลโก้ ตรวจภาพ p.1 (กราฟ backlog), p.7 (สูตร), p.10 (ภาพ F1) ไม่มีลายมือที่อ่านได้มีสาระ เนื้อหาส่วน turnaround (p.12-30) ใช้ถ้อยคำแบบหนังสือ ("this book", "the author") ดูเหมือนยกมาจากตำรา turnaround management เล่มหนึ่ง โดย slide ไม่ได้ระบุชื่อ (ความรู้ทั่วไป: น่าจะเป็น T. Lenahan, *Turnaround Management*, 1999; confidence ต่ำ)

## 1. Backlog

- กราฟ Work Load (แกน y) เทียบ Resources (แกน x): แถบเป้าหมาย backlog คือ **3 ถึง 6 สัปดาห์** เหนือแถบ = excessive work, ใต้แถบ = too little work (CMRP CMPR-10 p.1)
- หมายเหตุ: ไฟล์นี้ไม่ได้ให้นิยาม/สูตร backlog เป็น crew-weeks (ชั่วโมงงานค้าง / ชั่วโมงที่ทีมทำได้ต่อสัปดาห์) ระบุเพียงหน่วย "สัปดาห์" ใน planning metrics (p.7) สูตร crew-weeks จึงเป็นความรู้ทั่วไป
- **Backlog สูงเกิน** ส่งผล: ควบคุมงานไม่ได้จริง, ขวัญกำลังใจต่ำ, safety แย่, กำไรต่ำ, บรรยากาศงานแย่, ล้าจากแรงกดดันที่ตามงานไม่ทัน, ความภูมิใจในตนเองของทีมลดลง (p.1)
- **Backlog ต่ำเกิน**: งานไม่พอให้ใช้คนที่มีอย่างมีประสิทธิภาพ, งานถูกยืดให้เต็มวัน, supervisor ต้องวิ่งหางาน ทรัพยากรสูญเปล่า (p.2)

### Backlog purging (การล้าง backlog)
- ประโยชน์: ลบ WO เก่าหลายปี, ชี้งานที่ไม่สมเหตุสมผลแล้ว, ปิด WO ที่ไม่เหมาะสม, ปิดงานที่ทำเสร็จแต่ยังไม่ปิดในระบบ, ลบ WO ซ้ำ (p.2)
- backlog ที่ไม่แม่นยำ: แทบไร้ค่าเป็นเครื่องมือบริหาร, ขัดขวางการวิเคราะห์ performance และกำลังคน, ทำให้การ schedule ร่วมกับ Operations ลำบาก (p.3)
- รอบการทบทวน: **formal review ทุก 3 เดือน** (มีเอกสาร) และ **informal review รายเดือน** ใน planning meeting ปกติ (p.3)

## 2. Schedule compliance

- Planner รับผิดชอบติดตาม compliance ตลอดสัปดาห์ บันทึกสถานะงาน สรุปท้ายสัปดาห์ คำนวณ ratio และเหตุผลที่ไม่ทำตาม เป้าหมายคือหา corrective action ไม่ใช่หาคนผิด (p.4)
- schedule ไม่ใช่กฎตายตัว เป็นเป้าที่ดีที่สุดให้ supervisor ไล่ตาม แต่ต้องยืดหยุ่นได้เมื่อมีงานเร่งด่วนจริง (p.5)
- non-compliance ร้ายแรงเป็นพิเศษเมื่อ Maintenance คืนเครื่องให้ production ไม่ทันตามสัญญา ทำลายความร่วมมือ และทำให้ Operations ไม่อยากปล่อยเครื่องให้ทำ PM ในอนาคต (p.5)
- ช่วงเริ่มใช้ scheduling ปัญหาที่ซ่อนอยู่จะโผล่ขึ้น non-compliance ชี้จุดที่ช่างทำงานไม่ได้เพราะปัจจัยนอกการควบคุม ให้บันทึก รายงาน และดู trend (p.6)
- **สาเหตุ non-compliance** (p.6): Operations ไม่ปล่อยเครื่องตามตกลง; emergency มากเกิน (ช่างถูกดึงไปทำงานสำคัญน้อยกว่าโดยไม่ผ่าน work management process); จัดคนไม่เหมาะ; stock-out บ่อย/ไม่ได้เบิกของล่วงหน้า; planning package ไม่ตรงความจริง (อะไหล่ผิด, ขั้นตอนไม่ครบ, ไม่มีข้อมูล lockout/spec); ประเมินเวลางานต่ำไป; ขาดงานมาก/peak load ซ้อนกัน

## 3. Tracking metrics (p.7-9)

Planning metrics (p.7):
- Backlog size (สัปดาห์)
- **% Planned Work** = จำนวน planned WO / จำนวน WO ทั้งหมด
- **Planning Accuracy** = Estimated Job Costs / Actual Job Costs (ค่า < 1 แปลว่าใช้จริงเกินประมาณการ; slide ไม่ได้บอกเป้า)
- **% Emergency** = Emergency man-hours / Total maintenance man-hours

Schedule metrics (p.8):
- **Schedule Compliance** = scheduled labor-hours ที่ทำเสร็จ / scheduled labor-hours ที่ลง schedule
- **Schedule Performance** = scheduled labor-hours ที่ทำเสร็จ / labor-hours ที่มีทั้งหมด (available)
- **Schedule Effectiveness** = Schedule Performance x สัดส่วนชั่วโมงที่ทำเสร็จที่เป็น direct work (เทียบ indirect)
- งานแทรก (schedule break / urgent job) **ห้ามนับเป็นเครดิต** ใน metric ทั้งสามตัว (p.8)

ทำไมต้องใช้ 3 ตัวร่วมกัน (p.9):
- compliance สูงได้ง่าย ๆ ถ้าลง schedule เพียงส่วนน้อยของกำลังคน; performance จะจับจุดนี้ได้
- ถ้าใส่ indirect work (training, ยืมตัวไปช่วย engineering ฯลฯ) ลงใน schedule งานพวกนี้แทบ comply 100% อัตโนมัติ ดัน compliance/performance สูงเกินจริง จึงต้องมี effectiveness; ถ้าไม่ใส่ indirect work ลง schedule ก็ไม่จำเป็นต้องใช้ effectiveness

## 4. Turnaround: บริบทและเหตุผล (p.9-15)

- คำถามตั้งต้น: จำเป็นต้องทำ turnaround หรือไม่ และฐานทางเทคนิคคืออะไร (p.9)
- ตัวอย่าง F1 pit stop เป็นต้นแบบ turnaround: องค์ประกอบคือ team selection, planning, scheduling, training, parts availability, supervision, execution (p.10-11)
- งานที่ plan ดีต้องมี: ขั้นตอนชัดเจน, รายการทรัพยากร, ประมาณกำลังคน, ประมาณต้นทุน, ประสานงาน support service (p.11)
- นิยาม turnaround: เหตุการณ์ทางวิศวกรรมที่ติดตั้งของใหม่ overhaul ของเดิม และรื้อของที่เลิกใช้ออก (p.12) เป็นความจำเป็นทางธุรกิจสำหรับอุปกรณ์ใหญ่/ซับซ้อน แต่แพง ไม่พึงประสงค์ และอาจลด reliability ได้ (p.12)
- ต้นทุน: ทั้ง downtime และค่าดำเนินงาน การกระจายต้นทุนหลายปีไม่ได้ทำให้ผลกระทบรวมลดลง; ต้องใช้คนภายนอก/อุปกรณ์พิเศษ/ที่ปรึกษาจำนวนมาก (p.13)
- เป็นภัยต่อ reliability ได้เพราะ plan/เตรียม/execute ไม่ดี, ตัดสินใจผิด, ฝีมือแย่, วัสดุผิด, ความเสียหายช่วง shutdown/overhaul/start-up (p.14)
- ความเสี่ยงอุบัติเหตุเพิ่มขึ้นมาก: งานปกติใช้ทีมเล็กที่คุ้นเคยกับ procedure; turnaround กลับด้านทั้งหมด (คนแปลกหน้าจำนวนมาก, งานอันตรายไม่คุ้นเคย) ต้องมี safe system of work (p.14)
- ความเสี่ยงงบและเวลาบานปลายจากความไม่แน่นอนทางเทคนิค จึงควรใส่ contingency ทั้งเวลาและเงิน แต่ก็อาจเกินได้อีก (p.15)

## 5. Strategy ระดับผู้บริหาร (p.15-22)

- ผู้บริหารสูงสุดต้องมีกลยุทธ์ turnaround โดย **เป้าพื้นฐานคือกำจัด maintenance turnaround ให้หมด** ถ้าจำเป็นจริงจึงจัดให้สอดคล้องกับ maintenance objective, production และ business goal (p.15)
- **Steering group** ของผู้บริหารระดับสูง ประชุมเป็นระยะทั้งปี ดูแลกลยุทธ์ระยะยาว (p.16)
- มองหลาย turnaround เป็นลำดับกิจกรรมเชื่อมโยงกันใน asset management ไม่ใช่เหตุการณ์แยก (p.16)
- ปรัชญา: เปลี่ยนจาก preventive maintenance (ขับด้วยเทคนิค) ไปสู่ **maintenance prevention** (ขับด้วยธุรกิจ) ตั้งคำถามกับทุกกิจกรรมว่ากำจัดได้หรือไม่ โดยเริ่มจากกิจกรรมใหญ่สุดคือ turnaround (p.17)
- ที่มาของงานใน work list ที่อาจไม่เกี่ยวกับ reliability (p.18): ข้อกฎหมาย, ความต้องการจริงตามผู้ผลิต/ประสบการณ์, chronic problem ที่ไม่เคยทำ RCA, ritual task, การสึกกร่อนที่เลี่ยงได้ (corrosion, fouling), ข้อบกพร่องจาก design/จัดซื้อ/ติดตั้ง/commissioning, procedure การเดินเครื่องไม่ดีหรือเดินผิด, ขาดความสามารถ, PM ระหว่างปีไม่พอ, ใช้เครื่องเกินกำลัง
- Financial concerns (p.18-19): บริษัทมักนับเฉพาะ direct cost; ต้องประมาณต้นทุนแบบคร่าว ๆ แต่เนิ่น ๆ เทียบงบ ถ้าไม่พอให้เลือกเพิ่มงบ/ตัด scope/หากลยุทธ์อื่น; สัดส่วนของงบบำรุงรักษาที่ให้ turnaround; กำไรที่เสีย (ช่วงหยุด + ช่วงหลัง start-up ที่ rate/คุณภาพยังไม่ถึงเป้า); **ค่าแรงพนักงานโรงงานช่วง turnaround** ควรนับเป็นต้นทุน event (มิฉะนั้น event ดูถูกกว่าจริง และต้นทุนผลิตดูสูงเกินจริง)
- Current performance (p.19-20): การลดคนทำให้ PM/CM ค้าง แล้วมักโยนเข้า turnaround ทั้งที่ทำใน turnaround แพงกว่าช่วงปกติ **Golden rule: อนุญาตเฉพาะงานที่ทำช่วงอื่นไม่ได้** เว้นแต่มีเหตุผลเหนือกว่า (maintainability, hazard) และ turnaround ต้องไม่ใช้กลบจุดอ่อนของ maintenance philosophy (p.20)
- Plant turnaround history (p.21): หลัง turnaround โรงงานต้องดีเท่าเดิมหรือดีกว่า; วิเคราะห์สัดส่วน **emergent work** (งานที่โผล่หลังเริ่ม execution) ต่อ planned work: ปกติ **5-10%** ของงบที่วางแผน, แย่สุด **มากกว่า 45%** ถ้าสูงต้องปรับคุณภาพ technical specification ใน work request
- Corporate knowledge (p.22): turnaround ต้องใช้ทักษะบริหารต่างจากงานปกติ การบริหารไม่ดีเพิ่มต้นทุนมากกว่าปัจจัยอื่น; benchmark กับ best in field; คาดหวังให้ต้นทุนแต่ละครั้งลดลงแม้เครื่องเก่าลง

## 6. Work scope (p.23-26)

- **Project work**: ต้องประเมิน necessity, desirability (เวลาเหมาะไหม) และ payback; ต้องคุ้มเชิงธุรกิจ ไม่ใช่แค่ดีทางเทคนิค (p.23-24) สัดส่วน maintenance:project เปลี่ยนวิธีบริหาร (เช่น 90:10 ต่างจาก 10:90) แม้ project manager จะวางแผนเอง ทุกงานต้องรวมอยู่ใน **single plan** (p.24)
- **Maintenance work 3 ประเภท** (p.25): major task (ต้องมี engineering input เช่น overhaul เครื่องใหญ่, re-tray column), minor task (ระบุ spec งานก็พอ เช่น ล้าง/ตรวจ heat exchanger เล็ก), **bulkwork** (ของเล็กจำนวนมาก เช่น valve, ปั๊มเล็ก แค่ schedule) ผู้บริหารต้อง challenge major task ทุกงาน (ตัด/เลื่อน) และดูงานที่อยู่บน critical path ด้วย risk analysis
- นิยาม risk ใน slide = ความน่าจะเป็นเชิงตัวเลขที่จะเกิดความสูญเสีย คำถามคือความเสียหายแบบใด และความน่าจะเป็นเท่าใดยอมรับได้ (p.25) **ข้อสังเกต**: นิยามนี้ไม่รวม consequence ต่างจากนิยามทั่วไป risk = likelihood x consequence
- bulkwork มักเป็นตัวทำให้เสียเวลาเพราะกระจายตัวและจำนวนมาก แม้ major task จะวางแผนละเอียด (p.26)

## 7. Organization และ integration (p.26-30)

- สเปกตรัม: ใช้คนในบริษัทเองทั้งหมด (คนพอไหม? ความสามารถเหมาะไหม? มักจัดคนตามที่ว่าง ไม่ใช่ตามความสามารถ) จนถึง outsource ทั้งก้อนให้ contractor (ประวัติเรื่อง claim/variation? ต้องมีทีมคุมอีกหรือไม่ ซึ่งวนกลับไปคำถามว่าทำไมไม่บริหารเอง) (p.26-27)
- ตารางคำถามที่ผู้บริหารต้องถามแต่เนิ่น ๆ 9 หมวด: current performance, turnaround philosophy (เลี่ยง/เลื่อน/ทำห่างขึ้น/ง่ายขึ้น), financial, history (% งานที่ไม่คาดคิด), corporate knowledge, objectives (ทำเมื่อจำเป็นจริง, ระยะห่างสูงสุด, scope ที่ validate แล้ว, duration ต่ำสุด, ต้นทุนต่ำสุด), project scope, organization, maintenance scope (ritual work? ใช้ risk analysis ลด inspection? % bulkwork) (p.27)
- มุมวิศวกรรม: turnaround ซ่อม/เปลี่ยน/ปรับสภาพของเก่า ไม่ใช่สร้างใหม่ และวางแผนขณะเครื่องยังเดิน ความผิดปกติซ่อนอยู่จนเปิดเครื่อง จึงไม่แน่นอนโดยธรรมชาติ (p.28)
- จิตวิทยา: ทีมโรงงานรู้สึกว่าเครื่องเดินดีอยู่แต่ถูกรื้อโดยคนแปลกหน้าที่เคยตั้งคำถามกับ record ของตน → ความขัดแย้งระหว่างทีม ต้อง integrate ด้วย briefing, training, การเจรจา และช่องทางสื่อสารที่ดี (p.29-30)
- Integration ของความรู้ (p.30): Local (plant), Work management (engineer/planner ด้าน turnaround), Supervision, Craft, Specialist (vendor), Management of discrete projects
- **ข้อผิดพลาดใน slide**: p.30 บอกว่ารวมความรู้ "five" ประเภท แต่รายการมี **6** ประเภท

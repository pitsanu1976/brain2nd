# ISO 14224:2016 Annex A — Equipment-class attributes (reading notes)

Source: ISO 14224:2016 (3rd edition), reading notes ที่ถอดความ (paraphrase) ไม่ใช่ข้อความต้นฉบับ อ้างเลขหน้าแบบ printed page (PDF page = printed + 6)

ขอบเขต: PDF p.52-181 = printed p.46-175 สรุปแบบ paraphrase เน้น A.1, Table A.4 และ Compressors (A.2.2.2)

## A.1 Advisory notes (ภาพรวม)

- Annex A เป็น **informative**: ให้ตัวอย่าง taxonomy, boundary และ inventory data ต่อ equipment class ส่วนรหัสที่เป็น **normative** (เช่น failure mode) อยู่ใน Annex B (ISO 14224 cl. A.1.1, p.46)
- ใช้ subunit แบบ "มาตรฐานกลาง" ซ้ำในหลาย class (control and monitoring, lubrication system, cooling system) เพื่อลดจำนวนตารางและรหัสเฉพาะ (cl. A.1.1, p.46)
- ในตาราง subdivision แนะนำให้เผื่อ "Others" (เมื่อ item ที่นิยามไว้ไม่พอ) และ "Unknown" (เมื่อข้อมูลไม่พอ) (cl. A.1.1, p.46) -> ตรงกับ placeholder Other/Unknown ใน OREDA
- Priority ของ data field: high/medium/low ตีความเป็น บังคับ / ควรมีมาก / ควรมี (cl. A.1.1, p.46)
- กฎ boundary (cl. A.1.2, p.46-47):
  1. ใส่เฉพาะ item ทั่วไปของ class เพื่อเทียบ like-with-like ไม่ใส่ของ design เฉพาะ
  2. ไม่รวม item ที่ต่อเชื่อม เว้นแต่ระบุ แต่ failure ที่ connection (เช่น leak) ที่โยงกับ item ต่อเชื่อมไม่ได้ ให้นับในขอบเขต
  3. ถ้า driver กับ driven unit ใช้ subunit ร่วม (เช่น lube system) ให้บันทึก event กับ **driven unit**
  4. รวม instrument เฉพาะที่ทำหน้าที่ control/monitoring ของ unit นั้นหรือติดตั้งบนตัวเครื่อง ไม่รวมระบบกลาง เช่น SCADA
  5. ใช้ P&ID ช่วยกำหนดขอบเขต
- Common equipment data ให้ใช้ Table 5 กับทุก class แล้วเพิ่ม equipment-specific data ใน A.2 (เป็น trade-off ระหว่างต้นทุนเก็บข้อมูลกับคุณค่า) (cl. A.1.3, p.47)
- Tables A.1-A.4 จับคู่กับ taxonomy level: A.1 installation (L3), A.2 plant/unit (L4), A.3 section/system (L5, รหัส S1-S97), A.4 equipment class (L6) (cl. A.1.4, p.47)
- Equipment category ใน A.4 ปนกันสองแบบ: ตามหลักการทำงาน (rotating, mechanical, electrical) และตามกลุ่มการใช้งาน (drilling, subsea, utilities) (p.48)

## Table A.4 — Equipment classes (Level 6) (p.52-60)

`*` = มีตัวอย่าง taxonomy เต็มใน Annex A (หัวข้อในวงเล็บ)

- **Rotating (A.2.2)**: BL Blowers and fans (ไม่รวม air compressor); CF Centrifuges; CE Combustion engines* (A.2.2.1); **CO Compressors*** (A.2.2.2); EG Electric generators*; EM Electric motors*; GT Gas turbines*; LE Liquid expanders; MI Mixers; PU Pumps*; ST Steam turbines*; TE Turboexpanders*
- **Mechanical (A.2.3)**: CV Conveyors and elevators; CR Cranes*; FS Filters and strainers; HE Heat exchangers*; HB Heaters and boilers*; LA Loading arms; PL Onshore pipelines; PI Piping*; VE Pressure vessels*; SI Silos; SE Steam ejectors; TA Storage tanks*; SW Swivels*; TU Turrets*; WI Winches*
- **Electrical (A.2.4)**: FC Frequency converters*; PC Power cables and terminations; PT Power transformers*; SG Switchgear*; UP Uninterruptible power supply*
- **Safety and control (A.2.5)**: CL Control logic units*; EC Emergency communication equipment; ER Escape, evacuation and rescue; FG Fire and gas detectors*; FF Fire-fighting equipment; FI Flare ignition; IG Inert-gas equipment; IP Input devices*; LB Lifeboats*; NO Nozzles*; TC Telecommunications; VA Valves*
- **Subsea (A.2.6)**: DT Dry tree risers; PR Risers*; SC Subsea compressors; SD Subsea diving equipment; EP Subsea electrical power distribution*; FL Subsea flowlines; SH Subsea heat exchangers; CI Subsea intervention; MA Subsea manifolds; SL Subsea pipelines*; CA Submarine power cables; SV Subsea pressure vessels*; CS Subsea production control*; SP Subsea pumps*; TM Subsea templates; XT Subsea wellhead and X-mas trees*
- **Well completion (A.2.7)**: SS Downhole safety valves*; WE Downhole well completion*; ESP Electrical submersible pumps*; XD Surface wellhead and X-mas trees*
- **Drilling (A.2.8)**: CG Cementing equipment; DC Choke and manifolds; TB Crown and travelling blocks; DE Derrick; DI Diverters; DW Drawworks; DD Drilling and completion risers; DS Drill strings; DM Mud-treatment equipment; DH Pipe handling equipment; DR Riser compensators; MC String-motion compensators; BO Subsea BOP*; BT Surface BOP*; TD Top drives*
- **Well intervention (A.2.9)**: W1 surface equipment, W2 work strings/lines/cables, W3 bottom-hole assemblies, WC surface well control equipment* (ใช้ร่วมกับ coiled tubing, snubbing, wireline); OI Subsea well intervention*
- **Marine (A.2.10)**: AM Anchor windlasses and mooring; IC De-icing; DP Dynamic positioning; HT Helicopter deck; JF Jacking and fixation*; MD Marine disconnection; TH Thrusters; TO Towing equipment
- **Utilities (A.2.11)**: AI Air-supply; SU De-superheaters; FE Flare ignition equipment; HC Heating/cooling media; HP Hydraulic power units; NI Nitrogen-supply; OC Open/close drain equipment — ไม่มีตัวอย่าง (cl. A.2.11, p.174-175)
- **Auxiliaries (A.2.12)**: HV HVAC equipment — ไม่มีตัวอย่าง (p.175)

หมายเหตุ: Table A.4 ยังให้ standard อ้างอิงต่อ class เช่น compressors อ้าง ISO 10439, ISO 13631, ISO 13707, ISO 10442, API 617/618/619 (p.52)

## รูปแบบการบรรยาย class (A.2.1, p.61)

แต่ละ class ที่มีตัวอย่างประกอบด้วย 4 ส่วน: (1) type classification table (รหัส type 2 ตัวอักษร), (2) boundary drawing, (3) subdivision table: subunit -> maintainable items, (4) equipment-specific data table (Name / Description / Unit or code list / Priority) ข้อมูลอาจเป็น static หรือเปลี่ยนตามเวลา และเป็น "ส่วนเพิ่ม" จาก Table 5 failure coding ดู Annex B, safety equipment ดู Annex F

## Compressors (CO) — A.2.2.2 (p.63-66)

### Type codes (Table A.8, p.64)
CE Centrifugal, RE Reciprocating, SC Screw, AX Axial; class CO **รวม air compressor ด้วย** (สังเกต: type code CE ซ้ำกับ class code CE = Combustion engines แต่คนละระดับ)

### Boundary (cl. A.2.2.2.1, Figure A.3, p.64-65)
- ไม่รวม inlet/outlet valves และ driver พร้อม auxiliaries ของ driver; driver (EM, GT, CE) บันทึกเป็น inventory แยก และ inventory ของ compressor ต้องมีหมายเลขอ้างอิงไปยัง driver (ข้อความอ้าง "Figure A.2" แต่รูปจริงคือ A.3 น่าจะพิมพ์ผิด)
- **Compressor train = 1 inventory** มีได้ถึง 4 stages; แต่ละ stage ปกติคือ 1 casing (บางครั้ง 1 casing ทำ 2 stages); แต่ละ stage มีหลาย impeller
- Subunit ที่ใช้ร่วมกับ driver (เช่น GT) ให้นับเป็นของ compressor (driven unit)
- ถ้า lube oil กับ seal oil เป็นระบบร่วม ให้ลง failure ที่ subunit ที่ได้รับผลมากที่สุด ถ้าไม่ชัดให้ลงที่ lubrication system (p.65)
- รูป boundary ในไฟล์ text สกัดไม่ได้ (เป็นภาพ)

### Subdivision (Table A.9, p.65) — มี 6 subunits ไม่มีรหัสย่อในมาตรฐาน
| Subunit | Maintainable items (ชื่อตามมาตรฐาน) |
|---|---|
| Power transmission | Gearbox/variable drive; Bearings; Belt/sheave; Coupling to the driver; Coupling to the driven unit; Lubrication; Seals |
| Compressor | Casing; Rotor with impellers; Balance piston; Interstage seals; Radial bearing; Thrust bearing; Shaft seals; Internal piping; Valves; Antisurge system (รวม recycle valves และ controllers); Piston; Cylinder liner; Packing |
| Control and monitoring | Actuating device; Control unit; Cables and junction boxes; Internal power supply; Monitoring; Sensors (ระบุชนิด เช่น pressure, temperature, level); Valves; Wiring; Piping; Seals |
| Lubrication system | Oil tank with heating system; Pump; Motor; Check valves; Coolers; Filters; Piping; Valves; Lube oil |
| Shaft seal system | Oil tank with heating; Reservoir; Pump; Motor; Gear; Filters; Valves; Seal oil; Dry gas seal; Mechanical seal; Scrubber |
| Miscellaneous | Base frame; Piping, pipe support and bellows; Control valves; Isolation valves; Check valves; Coolers; Silencers; Purge air; Magnetic-bearing control system; Flange joints |

(การจัดคอลัมน์อนุมานจาก text ที่สกัดเรียงตามคอลัมน์ ซึ่งสอดคล้องกับรูปแบบตาราง combustion engine A.6; ควรเทียบกับ PDF ต้นฉบับอีกครั้ง) ตารางเดียวใช้กับทุก type: Piston, Cylinder liner, Packing เป็นของ reciprocating; Rotor/Balance piston/Antisurge เป็นของ turbo-type (การตีความ)

### Equipment-specific data (Table A.10, p.65-66) — สรุปฟิลด์สำคัญ
- **High**: compressed medium (gas/air), type of driver (อ้างรหัส class/type/ID ของ driver), discharge pressure design (last stage), flow rate design (m3/h), design power (kW), number of casings in train, shaft seal system (separate/combined/dry)
- **Medium**: gas handled เป็น average molar mass (g/mol), suction pressure design (first stage), discharge pressure operating, discharge temperature design, utilization (% เทียบ design), number of stages (นับ stage ไม่ใช่ impeller), intercooler fitted (yes/no)
- **Low**: suction pressure/flow/discharge temp ขณะ operate, polytropic head (kJ/kg), body type (barrel/vertical split vs axial split), shaft sealing type (mechanical, oil, dry gas, dry gland, labyrinth, combined), radial และ thrust bearing type (antifriction, journal, magnetic), design speed, coupling type (fixed, flexible, hydraulic, disconnect)
- **เฉพาะ reciprocating (Low)**: cylinder configuration (inline/opposed/V/W), cylinder orientation (horizontal/vertical/inclined), working principle (single/double-acting), packing type (lubricated/dry)

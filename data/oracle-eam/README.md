# data/oracle-eam — structured data จากคู่มือ Oracle eAM 11i

ข้อมูลที่สกัดออกมาเป็นตารางจาก [[raw/oracle-eam-user-guide]] (Oracle Enterprise Asset Management
User's Guide, Release 11i, Part A95930-01, 234 หน้า) ตัวข้อความเต็ม `raw/oracle_concept.md`
**ไม่ถูกเก็บใน repo** (มีลิขสิทธิ์ Oracle) — โฟลเดอร์นี้เก็บเฉพาะข้อความสั้นที่อ้างอิงได้ + ข้อมูลเชิงโครงสร้าง

## ไฟล์

| ไฟล์ | แถว | เนื้อหา |
|---|---|---|
| `eam_objects.csv` | 26 | object model: ชื่อ object, layer, คำนิยาม (verbatim), chapter page, PDF page, upstream dependency |
| `eam_lookups.csv` | 3 | lookup type ที่ใช้รหัส failure/งาน: `MTL_EAM_ACTIVITY_TYPE`, `MTL_EAM_ACTIVITY_CAUSE`, `WIP_EAM_FAILURE_CODE` + ค่าตัวอย่างจริงในเอกสาร |
| `work_order_types.csv` | 4 | Routine / Preventive Maintenance / Rebuild / Easy — สร้างโดยใคร, เริ่มที่สถานะไหน |
| `work_order_statuses.csv` | 7 | Draft, Released, Unreleased, Complete, Closed, On-Hold, Cancel + สิทธิ์ schedule/charge labor/request material และ transition |
| `iso14224_map.csv` | 8 | **ข้อมูลที่เราอนุมานเอง** (ไม่ใช่ในเอกสาร Oracle): จับคู่ระดับ ISO 14224 กับ construct ของ eAM + confidence |
| `build.py` | — | สร้าง CSV ทั้งหมดโดย slice ข้อความจาก `raw/oracle_concept.md` ระหว่าง anchor start/end |
| `validate.py` | — | ตรวจว่า **ทุก quote ในทุกแถวปรากฏจริงบนหน้าที่อ้าง** และ chapter tag ตรงกับต้นฉบับ |

## หลักความน่าเชื่อถือ

- ทุกคอลัมน์ที่เป็นข้อความอ้างอิง ถูก **ตัดออกจากต้นฉบับด้วยสคริปต์** ไม่ได้พิมพ์มือ → verbatim by construction
- `validate.py` ตรวจซ้ำแบบ independent: ถ้ามีการแก้ quote หรือเลขหน้าให้ผิด จะ FAIL ทันที
  ```
  cd data/oracle-eam && python3 validate.py
  # RESULT: PASS — all quotes verified against raw/oracle_concept.md
  ```
- `iso14224_map.csv` ไม่มี quote — เป็นการตีความ จึงมีคอลัมน์ `confidence` และ `rationale` กำกับ และต้องอ่านคู่กับ [[ISO 14224 Taxonomy]] / [[Failure Hierarchy]]

## วิธีใช้กับงาน CMMS

1. **ออกแบบ failure coding** — ใช้ `eam_lookups.csv` เป็นรายการ "ช่องที่ Oracle ให้มา" แล้วเทียบกับ taxonomy 7 ระดับใน [[Failure Hierarchy]] ผ่าน `iso14224_map.csv`
2. **แก้ปัญหา WO type ปนกัน** — `work_order_types.csv` + `work_order_statuses.csv` แยก "ประเภทงาน" ออกจาก "สถานะ" ชัดเจน ใช้ทำ validation rule และ training
3. **ออกแบบ hierarchy** — `eam_objects.csv` คอลัมน์ `upstream` บอกลำดับที่ต้องสร้าง (Organization → Parameters → Area → Department → Lookup → Category → Asset Group → Asset Number → Activity → …)

## การสร้างใหม่

```bash
# ต้องมี raw/oracle_concept.md ในเครื่องก่อน (gitignored)
cd data/oracle-eam && python3 build.py && python3 validate.py
```

ถ้าต้นฉบับเปลี่ยน (เช่นได้คู่มือ R12) ให้แก้ `MD` ใน `build.py` เป็นไฟล์ใหม่ และปรับ anchor
— validate.py จะบอกทันทีว่าแถวไหนอ้างหน้าไม่ตรง

## License

เอกสารต้นทางเป็นลิขสิทธิ์ Oracle Corporation ใช้ภายในองค์กรเท่านั้น ไฟล์ในโฟลเดอร์นี้เก็บเฉพาะ
ข้อความสั้นเพื่อการอ้างอิง (ไม่เกินประโยคหรือสองประโยคต่อแถว) ไม่ใช่การทำซ้ำเนื้อหาคู่มือ

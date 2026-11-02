#!/usr/bin/env python3
"""Build structured CSVs for Oracle eAM 11i from raw/oracle_concept.md.

Every quoted cell is sliced out of the extracted source text between an anchor
start and end string, so the CSVs are verbatim by construction. validate.py
re-checks that afterwards against the page number recorded in the row.

Usage:  python3 build.py          (writes the CSVs next to this file)
"""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
MD = os.path.join(ROOT, 'raw', 'oracle_concept.md')

text = open(MD, encoding='utf-8').read()
pages = {}
for m in re.finditer(r'<!-- page: (\d+) \| ch: ([^>]+) -->\n\n(.*?)(?=\n<!-- page:|\Z)', text, re.S):
    pages[int(m.group(1))] = (m.group(2).strip(), re.sub(r'\s+', ' ', m.group(3)).strip())

def quote(pdf_page, start, end):
    """Slice verbatim text between start and end anchors on a page; fail loudly."""
    if pdf_page not in pages:
        raise SystemExit(f'page {pdf_page} not in source')
    ch, body = pages[pdf_page]
    i = body.find(start)
    if i < 0:
        raise SystemExit(f'anchor start not found on p{pdf_page} ({ch}): {start[:50]!r}')
    j = body.find(end, i)
    if j < 0:
        raise SystemExit(f'anchor end not found on p{pdf_page} ({ch}): {end[:50]!r}')
    return re.sub(r'\s+', ' ', body[i:j + len(end)]).strip()

def ch_of(pdf_page):
    return pages[pdf_page][0]

def write(name, header, rows):
    path = os.path.join(HERE, name)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(header)
        w.writerows(rows)
    print(f'{name}: {len(rows)} rows')

# ---------------------------------------------------------------- objects ----
OBJ = [
    ('Organization', 'foundation', 33,
     'A valid organization is a requirement', 'enabled for eAM.', '', 'ต้องมี org ที่ enable eAM ก่อนทุกอย่าง'),
    ('eAM Parameters', 'foundation', 37,
     'Now that you have established an eAM enabled organization', 'Work Order defaults.', 'Organization',
     'ค่า default ระดับ org (asset number, cost, work request, work order)'),
    ('Asset Area', 'asset', 39,
     'Areas are user defined lookups', 'entered into the asset.', 'Organization',
     'แบ่งโรงงานเป็นโซนเพื่อ track/account'),
    ('Department / Crew', 'resource', 40,
     'A department or crew is an area within your organization', 'available for that department.', 'Organization',
     'จุดเก็บต้นทุน + capacity; ผูก resource/craft'),
    ('Department Approver', 'resource', 42,
     'You can set up department approvers', 'owning department', 'Department / Crew',
     'workflow แจ้ง work request ไปยังแผนกเจ้าของ asset'),
    ('Asset Activity Type (lookup)', 'coded', 44,
     'Asset Activity Types are used to describe the type of maintenance work', 'extensible attribute that is user defined.', '',
     'ชนิดงาน — ไม่ใช่สาเหตุ ไม่ใช่ failure mode'),
    ('Asset Activity Cause (lookup)', 'coded', 45,
     'Asset Activity Cause codes are a list of reasons an asset may fail', "asset’s ability to perform.", '',
     'เหตุผลหยาบที่งานเกิด (Breakdown / Normal Wear / Preventive / Rework)'),
    ('Work Order Failure Code (lookup)', 'coded', 53,
     'Failure Codes are similar to Activity Codes', 'preliminary cause of failure.', '',
     'รหัส failure ละเอียด กรอกตอน complete WO; แนะนำให้แยกตาม asset type + ใส่ prefix'),
    ('Category Code / Set', 'asset', 55,
     'Classes and Subclasses are ways to establish naming conventions for assets', 'within that organization.', '',
     'จัดกลุ่ม/ตั้งชื่อ asset เพื่อ query'),
    ('Asset Group', 'asset', 58,
     'Asset Groups represent the classification of equipment', 'Storage Tanks, and Turbines.', 'Category Code / Set',
     '= equipment class; สร้างจาก Master Item form; ต้องมีก่อน asset number'),
    ('Asset Attribute', 'asset', 61,
     'You can define common characteristics data specific to asset groups', 'using descriptive flexfields.', 'Asset Group',
     'DFF ต่อ asset group (nameplate, HP, voltage ฯลฯ)'),
    ('Asset Number', 'asset', 65,
     'There are four methods to entering a new asset into eAM', 'Import Asset Number interface', 'Asset Group',
     'ตัว asset จริง รองรับ parent/child hierarchy'),
    ('Asset Activity', 'work', 71,
     'Asset Activities provide you with a standard template of jobs', 'Routine or Preventive Maintenance.', 'Asset Number',
     'template ของ job (type + cause + BOM + route) ผูกกับ asset number / rebuildable item'),
    ('Asset Route', 'work', 76,
     'You may need to perform an asset activity on multiple assets', 'you can define Asset Routes.', 'Asset Number',
     'งานเดียวกับหลาย asset ในรอบเดียว; ใช้ได้เฉพาะ day interval'),
    ('Asset BOM', 'work', 78,
     'You can identify and select the required items that make up an asset item', 'used by an asset activity', 'Asset Number',
     'รายการชิ้นส่วนที่ประกอบเป็น asset'),
    ('Activity Route', 'work', 81,
     'An activity route is the set of operations or jobs necessary to perform an asset activity',
     'necessary to perform an asset activity.', 'Asset Activity',
     'ลำดับ operation ของงานหนึ่ง พร้อม resource ต่อ operation'),
    ('Activity BOM', 'work', 85,
     'A bill of material (BOM) can be used to list all items and components needed to perform a particular asset activity',
     'defined for each asset activity.', 'Asset Activity',
     'วัสดุที่ต้องใช้ต่องาน (เช่น Oil Change → filter, oil)'),
    ('Rebuildable Item', 'asset', 87,
     'Items that are installed, removed, and refurbished are referred to as rebuildable items',
     'motors, control boxes, and computer boards.', 'Asset Group',
     'ชิ้นส่วนที่ถอด/ซ่อม/ใส่กลับ — ไม่ใช่ asset แต่ผูก WO ได้ เก็บ genealogy'),
    ('Collection Plan', 'quality', 92,
     'When completing an eAM work order, one of the requirements is to enter quality results',
     "the work order’s current asset.", '',
     'ผลตรวจคุณภาพตอน complete (Oracle Quality)'),
    ('Work Request', 'work', 27,
     'operations and maintenance staff to enter work requests to report any problems with an asset',
     'to report any problems with an asset', 'Asset Number',
     'คำขอแจ้งปัญหาก่อนกลายเป็น work order'),
    ('Work Order', 'work', 182,
     'A work order includes a listing of all maintenance activities', 'performed on an asset.', 'Work Request',
     'ใบงานจริง มี operation/material/resource และต้นทุน'),
    ('Operation', 'work', 115,
     'Operations prepare the instructions or logistics to perform a repair', 'perform a repair.', 'Work Order',
     'ขั้นตอนใน WO ผูก department + resource'),
    ('Material Requirement', 'work', 120,
     "When you enter a work order for an asset, the asset’s associated activity will attach the required material",
     'to complete its operations.', 'Asset Activity',
     'ความต้องการวัสดุของ WO (มาจาก activity BOM)'),
    ('Resource Requirement', 'work', 125,
     'A resource is anything you require to perform, schedule, or cost',
     'employees, machines, outside processing services, and physical space.', 'Work Order',
     'คน/เครื่อง/ผู้รับเหมา/พื้นที่ ที่ต้องใช้'),
    ('Meter', 'pm', 153,
     'eAM enables you to generate work orders automatically based on runtime and day intervals',
     'whichever comes first.', 'Asset Number',
     'ตัววัด (ชั่วโมงเดินเครื่อง/กม./รอบ) ใช้ trigger PM'),
    ('PM Scheduling Definition', 'pm', 162,
     'An asset activity and asset number combination can be associated with runtime interval and daytime interval rules',
     'scheduled for an asset.', 'Asset Activity',
     'กติกา PM บนคู่ asset activity × asset number หรือบน asset route'),
]
rows = []
for name, layer, pg, s, e, up, note in OBJ:
    rows.append([name, layer, quote(pg, s, e), ch_of(pg), pg, up, note])
write('eam_objects.csv',
      ['object', 'layer', 'definition_quote', 'chapter_page', 'pdf_page', 'upstream', 'notes'], rows)

# ---------------------------------------------------------------- lookups ----
LK = [
    ('MTL_EAM_ACTIVITY_TYPE', 'ชนิดงานบำรุงรักษา (task type)', 44,
     'Inspections, Lubrications, Overhauls, Calibration, and Repetitive work', 'work',
     'กำหนด default ที่ asset activity'),
    ('MTL_EAM_ACTIVITY_CAUSE', 'เหตุผลหยาบที่ asset ล้มเหลว', 45,
     'Preventive, Normal Wear, Rework, and Breakdown', 'assets',
     'default ที่ asset activity + แก้ได้ที่ work order'),
    ('WIP_EAM_FAILURE_CODE', 'รหัสอธิบายสาเหตุ failure ละเอียด', 53,
     "ENGOVHT (Engine Overheating) or TRUCKBRAKE (Truck’s Brake Failure)", 'wo',
     'กรอกตอน work order completion; แนะนำแยกตาม asset type และใส่ prefix'),
]
rows = []
for ltype, codes, pg, examples, scope, when in LK:
    rows.append([ltype, codes, examples, scope, ch_of(pg), pg, when])
write('eam_lookups.csv',
      ['lookup_type', 'codes_what', 'example_values', 'scope', 'chapter_page', 'pdf_page', 'when_used'], rows)

# ------------------------------------------------------------ wo types ------
WT = [
    ('Routine', 101, 'Routine work orders are normally created by a Planner', 'Maintenance Workbench',
     'Draft', 'งานทั่วไปที่วางแผนเอง'),
    ('Preventive Maintenance', 106,
     'eAM enables you to generate work orders automatically based on meter readings, runtime intervals, and calendar days',
     'PM Scheduler', 'Draft', 'เกิดจาก PM schedule/meter'),
    ('Rebuild', 107, 'You may need to create Rebuild Work Orders as child work orders of parent work orders',
     'child of parent WO', 'Draft', 'งานซ่อมชิ้นส่วนที่ถอดออกมา'),
    ('Easy', 112, 'Easy Work Orders have been referred to as unplanned work orders',
     'manual', 'Released', 'ข้าม operation/resource planning และข้าม Draft'),
]
rows = []
for t, pg, s, created, start, note in WT:
    rows.append([t, quote(pg, s, s), created, start, ch_of(pg), pg, note])
write('work_order_types.csv',
      ['wo_type', 'definition_quote', 'created_by', 'starts_at_status', 'chapter_page', 'pdf_page', 'notes'], rows)

# -------------------------------------------------------- wo statuses -------
ST = [
    ('Draft', 113, 'No scheduling of work orders at a Draft status can take place', 'no', 'no', 'no',
     'Draft → Released / Unreleased / Cancel'),
    ('Released', 113, 'Once a work order is Released, you can execute a work order', 'yes', 'yes', 'yes',
     'Released → Complete / On-Hold / Unreleased / Cancel'),
    ('Unreleased', 114, 'Scheduling can take place for these work orders', 'yes', 'no', 'no',
     'Unreleased → Released / On-Hold / Cancel; ย้อนเป็น Draft ไม่ได้'),
    ('Complete', 114, 'A Complete status for an eAM work order does not require any operation to be completed',
     'no', 'yes', 'no', 'Complete → Closed / Released (uncomplete)'),
    ('Closed', 114, 'You cannot charge any accounts once an eAM work order is closed', 'no', 'no', 'no',
     'Closed → Complete (unclose)'),
    ('On-Hold', 114, 'eAM work orders at Released and Unreleased statuses can be put on hold', 'no', 'no', 'no',
     'พักงานจาก Released/Unreleased'),
    ('Cancel', 114, 'You can cancel an eAM work order at any status in its lifecycle', 'no', 'no', 'no',
     'ยกเลิกได้ทุกสถานะ'),
]
rows = []
for s, pg, q, sch, lab, mat, trans in ST:
    rows.append([s, quote(pg, q, q), sch, lab, mat, ch_of(pg), pg, trans])
write('work_order_statuses.csv',
      ['status', 'description_quote', 'can_schedule', 'can_charge_labor', 'can_request_material',
       'chapter_page', 'pdf_page', 'transitions'], rows)

# ------------------------------------------------------ iso 14224 mapping ---
# derived: the Oracle documentation has no ISO 14224 taxonomy; mapping is ours
MAP = [
    ('6', 'equipment unit', 'Asset Number (ระดับบนของ hierarchy) + Asset Group เป็น class', '2-30, 2-37',
     'high', 'Asset Group = การจำแนกประเภท, Asset Number = ตัวเครื่องจริง'),
    ('7', 'subunit', 'Asset Number ลูก (parent/child)', '2-37',
     'medium', 'eAM ไม่กำหนดความหมายของแต่ละระดับ ต้องตกลงเอง'),
    ('8', 'component / maintainable item', 'Asset Number ใบล่าง หรือ Rebuildable Item', '2-37, 2-59',
     'medium', 'ถ้ามีการถอดซ่อมกลับใช้ Rebuildable Item จะได้ genealogy'),
    ('6/8', 'failure mode (failure record)', 'WIP_EAM_FAILURE_CODE', '2-25',
     'medium', 'lookup เดียวแบน ต้องฝัง mode/mechanism ในรหัส'),
    ('8', 'failure cause', 'MTL_EAM_ACTIVITY_CAUSE (หยาบ) + WIP_EAM_FAILURE_CODE (ละเอียด)', '2-17, 2-25',
     'high', 'สองชั้น: cause หยาบที่ activity, failure code ละเอียดตอนปิดงาน'),
    ('8', 'failure mechanism', 'ไม่มีฟิลด์ — ฝังในรหัส failure code หรือ descriptive flexfield', '—',
     'low', 'ไม่มี object รองรับ ต้องออกแบบเอง'),
    ('maintenance record', 'maintenance activity (ISO เก็บนอก taxonomy)', 'Asset Activity + Work Order Operation', '2-43, 3-21',
     'high', 'ISO ไม่มี resolution; eAM เก็บงานที่ทำใน operation'),
    ('—', 'resolution', 'ไม่มีฟิลด์ — operation / DFF', '—',
     'low', 'OREDA มี resolution 13 รหัส แต่ eAM ไม่มีที่เก็บ'),
]
write('iso14224_map.csv',
      ['iso_level', 'iso_concept', 'eam_construct', 'eam_page', 'confidence', 'rationale'], MAP)
print('done')

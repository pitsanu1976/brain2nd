---
title: Resolution Codes
created: 2026-10-20
updated: 2026-10-21
type: concept
tags: [resolution, coding, oreda, data-quality]
sources: [compressor-failure-hierarchy.md, compressor-failure-hierarchy__resolution-code.csv, compressor-failure-hierarchy__notes.csv, compressor-failure-hierarchy__failure-hierarchy.csv, coce-resolution.jpg, reliability-based-maintenance-management.md]
confidence: high
contested: true
---

# Resolution Codes (14 รหัส)

**Resolution** คือการดำเนินการแก้ไข/ตอบสนอง เป็นระดับที่ 7 (ท้ายสุด) ของ [[Failure Hierarchy]] รหัสเต็มอยู่ในคอลัมน์ `Resolution_CODE` และเป็นส่วนหนึ่งของแต่ละแถวใน dataset ดู [[CAUSE_CODE Convention]]

## ตาราง 14 รหัส

"แถวใน Failure Hierarchy" = จำนวนแถวข้อมูล (จากทั้งหมด 7,882 แถว) ที่ใช้รหัสนั้น "Standard action" = ข้อความ action มาตรฐานใน `Resolution Detail`

| Code | Resolution | ใน OREDA list (13) | แถวใน Failure Hierarchy | Standard action |
|---|---|---|---|---|
| ADJ | Adjust | ใช่ | 632 | adjust / reset to restore correct condition |
| CHK | Check | ใช่ | 1,175 | check condition and confirm cause |
| NFF | No Fault Found | ใช่ | 119 | tested, no fault found - return to service |
| REF | Refit | ใช่ | 396 | remove and refit component correctly |
| REP | Repair | ใช่ | 987 | repair affected component |
| RPL | Replace | ใช่ | 1,141 | replace affected component |
| TST | Test | ใช่ | 501 | function / performance test |
| INS | Inspection | ใช่ | 794 | inspect affected component (visual / NDT) |
| SVC | Service | ใช่ | 421 | service: clean / lubricate / top up / flush |
| COM | Combination | ใช่ | 580 | combination of several activities as found |
| MOD | Modify | ใช่ | 614 | modify design, material or operating practice to prevent recurrence |
| OVH | Overhaul | ใช่ | 438 | overhaul item / sub-assembly |
| OTR | Other | ใช่ | 84 | action not covered by standard categories (record details) |
| CHG | Change | **ไม่** | 0 | (ไม่มีข้อมูล) |

ผลรวมแถวของ 13 รหัสแรก = 7,882 (ตรงกับจำนวนแถวข้อมูลทั้งหมด)

## ข้อขัดแย้ง (contested)

- Sheet "resolution code" มี **14 รหัส** รวม `CHG - Change` แต่ OREDA resolution list (Notes และภาพ `coce-resolution.jpg`) และ Resolution Matrix มี **13** (ไม่มี Change) และไม่มีแถวใดใน Failure Hierarchy ใช้ `CHG`
- การตัดสินใจ: คงทั้งสองมุมมอง ถือว่า resolution ที่ใช้จริงคือ 13 รหัส; `CHG` เป็นรหัสที่ประกาศไว้แต่ไม่ถูกใช้ (ไม่ทราบสาเหตุ source ไม่ระบุ) บันทึกใน [[log]]

## การเลือก resolution ต่อ mechanism

ทุก [[Failure Mechanism]] ได้รับเฉพาะ resolution ที่ "น่าจะเป็นไปได้" (233 จาก 37 x 13 คู่) เช่น Wear -> No Fault Found ถูกตัดออก ดูตารางเต็มที่ [[Resolution Matrix by Mechanism]] ทุกแถวระบุ `Resolution Detail Basis`: **Item-specific** (action เฉพาะ item จาก mechanism library) หรือ **Standard** (ข้อความมาตรฐานข้างบน)

หมายเหตุ: resolution ใน dataset เป็น engineering judgement ไม่ใช่ข้อมูลการซ่อมจริงของ OREDA ต้อง review กับ CMMS/RCA ก่อนใช้

## ดูเพิ่ม (RBMM)

ลิงก์/การตีความ: ฟิลด์ Action ใน record ขั้นต่ำของ CMMS (RBMM p.151-152) ใกล้เคียง Resolution ในแง่ข้อมูลที่ต้องเก็บ ดู [[Failure Data Recording]] และการเลือกงานป้องกันที่ควรทำ (PM task) ดู [[PM Task Selection]]

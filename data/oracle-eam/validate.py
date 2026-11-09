#!/usr/bin/env python3
"""Verify the Oracle eAM CSVs: quoted cells verbatim on their cited page, and the ISO
code vocabularies matching raw/iso-14224/annex-b.md.

Fails loudly if a quote was paraphrased, a page number is wrong, or a chapter tag
does not match the source. Run after build.py:  python3 validate.py
"""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
MD = os.path.join(ROOT, 'raw', 'oracle_concept.md')

text = open(MD, encoding='utf-8').read()
pages = {}
for m in re.finditer(r'<!-- page: (\d+) \| ch: ([^>]+) -->\n\n(.*?)(?=\n<!-- page:|\Z)', text, re.S):
    pages[int(m.group(1))] = (m.group(2).strip(), re.sub(r'\s+', ' ', m.group(3)).strip())

def read(name):
    with open(os.path.join(HERE, name), encoding='utf-8') as f:
        return list(csv.DictReader(f))

def check(rows, name, quote_col, page_col='pdf_page', ch_col='chapter_page'):
    ok = bad = 0
    for r in rows:
        pg = int(r[page_col])
        q = (r.get(quote_col) or '').strip()
        if pg not in pages:
            print(f'FAIL {name}: pdf page {pg} not in source ({r.get(quote_col, "")[:40]})')
            bad += 1
            continue
        ch, body = pages[pg]
        if q not in body:
            print(f'FAIL {name} p{pg}: quote not on page -> {q[:90]!r}')
            bad += 1
            continue
        if ch_col in r and r[ch_col] and r[ch_col] != ch:
            print(f'FAIL {name} p{pg}: chapter tag {r[ch_col]} != source {ch}')
            bad += 1
            continue
        ok += 1
    print(f'{name}: {ok} ok, {bad} failed')
    return bad

fails = 0
fails += check(read('eam_objects.csv'), 'eam_objects', 'definition_quote')
fails += check(read('eam_lookups.csv'), 'eam_lookups', 'example_values')
fails += check(read('work_order_types.csv'), 'work_order_types', 'definition_quote')
fails += check(read('work_order_statuses.csv'), 'work_order_statuses', 'description_quote')

# iso14224_map has no verbatim quotes; check its page refs resolve to real chapter tags
tags = {ch for ch, _ in pages.values()}
for r in read('iso14224_map.csv'):
    for ref in [x.strip() for x in r['eam_page'].split(',')]:
        if ref in ('—', ''):
            continue
        if ref not in tags:
            print(f'FAIL iso14224_map: page ref {ref} not in source')
            fails += 1
print(f'iso14224_map: page refs checked against {len(tags)} chapter tags')

# ------------------------------------------------- ISO code vocabularies ---
# ตรวจกับ notes ของ ISO 14224 ใน vault (source of truth สูงกว่า slide PETROSYNC)
ANNEX = os.path.join(ROOT, 'raw', 'iso-14224', 'annex-b.md')
annex = open(ANNEX, encoding='utf-8').read()
label_line = [l for l in annex.split('\n') if l.startswith('AIR Abnormal')][0]
iso_labels = {c: lab.strip().rstrip('*').strip()
              for c, lab in re.findall(r'([A-Z]{2,3}) ([^;]+)', label_line)}
print(f'annex-b: {len(iso_labels)} ISO failure mode codes parsed')

fm = read('failure_mode_codes.csv')
codes = [r['code'] for r in fm]
if len(set(codes)) != len(codes):
    print('FAIL failure_mode_codes: duplicate code'); fails += 1
for r in fm:
    c, lab = r['code'], r['label_en']
    if not re.fullmatch(r'[A-Z]{2,3}', c):
        print(f'FAIL failure_mode_codes: bad code format {c!r}'); fails += 1
    elif c not in iso_labels:
        print(f'FAIL failure_mode_codes: {c} not in ISO 14224 label list'); fails += 1
    elif iso_labels[c] != lab:
        print(f'FAIL failure_mode_codes: {c} label {lab!r} != ISO {iso_labels[c]!r}'); fails += 1
    if r['used_by_compressor_co'] not in ('yes', 'no'):
        print(f'FAIL failure_mode_codes: col used_by_compressor_co = {r["used_by_compressor_co"]!r}'); fails += 1
co_yes = sum(1 for r in fm if r['used_by_compressor_co'] == 'yes')
if co_yes != 20:
    print(f'FAIL failure_mode_codes: compressor CO should use 20 codes, found {co_yes}'); fails += 1
if not any(r['code'] == 'ELF' and r['used_by_compressor_co'] == 'no' for r in fm):
    print('FAIL failure_mode_codes: ELF must be present and not used by CO'); fails += 1
print(f'failure_mode_codes: {len(fm)} rows, {co_yes} used by CO')

ma = read('maintenance_activity_codes.csv')
EXPECT = ['Replace', 'Repair', 'Modify', 'Adjust', 'Refit', 'Check', 'Service',
          'Test', 'Inspection', 'Overhaul', 'Combination', 'Other']
if len(ma) != 12:
    print(f'FAIL maintenance_activity_codes: expected 12 rows, got {len(ma)}'); fails += 1
if [r['activity'] for r in ma] != EXPECT:
    print('FAIL maintenance_activity_codes: activity names/order differ from ISO Table B.5'); fails += 1
if [int(r['code_no']) for r in ma] != list(range(1, 13)):
    print('FAIL maintenance_activity_codes: code_no must be 1..12'); fails += 1
for r in ma:
    if set(x.strip() for x in r['iso_use'].split(',')) - {'C', 'P'}:
        print(f'FAIL maintenance_activity_codes: iso_use {r["iso_use"]!r}'); fails += 1
print(f'maintenance_activity_codes: {len(ma)} rows checked')

print('\nRESULT:', 'PASS — all quotes verified against raw/oracle_concept.md' if fails == 0 else f'FAIL — {fails} problem(s)')
sys.exit(1 if fails else 0)

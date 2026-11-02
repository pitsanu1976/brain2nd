#!/usr/bin/env python3
"""Verify every quoted cell in the Oracle eAM CSVs appears verbatim on its cited page.

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

print('\nRESULT:', 'PASS — all quotes verified against raw/oracle_concept.md' if fails == 0 else f'FAIL — {fails} problem(s)')
sys.exit(1 if fails else 0)

"""Build graph/triplets.csv from the '## Triplets' section of each wiki page.

Rules: [[Knowledge Graph Triplet]] and SCHEMA section 10.
Usage: python -I graph/build_triplets.py [--check]
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOCAB_PAGE = ROOT / "concepts" / "Knowledge Graph Triplet.md"
OUT = ROOT / "graph" / "triplets.csv"
WIKI_DIRS = ["entities", "concepts", "comparisons", "queries", "guides", "reference"]
AREA_B_DIRS = ["entities", "concepts", "comparisons", "queries"]
FLIP = ("has_part", "failure_mode_of")  # written as their canonical inverse
AREA_A_TAGS = {"second-brain", "para", "zettelkasten", "moc", "llm-wiki", "code-method",
               "obsidian", "settings", "plugins", "templates", "frontmatter", "links", "naming"}

FIELD = re.compile(r"\[([a-z_]+)::\s*((?:\[\[[^\]]*\]\]|[^\]])*?)\s*\]")
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta


def parse_list(value):
    return [x.strip() for x in value.strip("[]").split(",") if x.strip()]


def strip_code(text):
    return re.sub(r"^(`{3,}).*?^\1", "", text, flags=re.S | re.M)


def load_vocab():
    vocab, inverse = set(), {}
    text = VOCAB_PAGE.read_text(encoding="utf-8")
    section = text.split("## Predicate vocabulary", 1)[1].split("\n## ", 1)[0]
    for line in section.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and re.fullmatch(r"[a-z_]+", cells[0]):
            vocab.add(cells[0])
            if cells[1] != "-":
                inverse[cells[0]] = cells[1]
    return vocab, inverse


def page_names():
    names = set()
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts or ".obsidian" in p.parts:
            continue
        rel = p.relative_to(ROOT).with_suffix("").as_posix()
        names.update({p.stem, rel})
    return names


def triplet_section(text):
    body = strip_code(text)
    m = re.search(r"^## Triplets[ \t]*\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1) if m else None


def node(raw):
    raw = raw.strip()
    m = LINK.fullmatch(raw)
    return (m.group(1).strip(), True) if m else (raw, False)


def main():
    check_only = "--check" in sys.argv
    vocab, inverse = load_vocab()
    names = page_names()
    rows, errors, missing = [], [], []

    for d in WIKI_DIRS:
        for p in sorted((ROOT / d).glob("*.md")):
            if p.name == "README.md":
                continue
            text = p.read_text(encoding="utf-8")
            meta = frontmatter(text)
            tags = set(parse_list(meta.get("tags", "")))
            rel = p.relative_to(ROOT).as_posix()
            section = triplet_section(text)
            if section is None:
                if d in AREA_B_DIRS and not tags & AREA_A_TAGS:
                    missing.append(rel)
                continue
            for n, line in enumerate(section.splitlines(), 1):
                line = line.strip()
                if not line.startswith("- "):
                    continue
                fields = list(FIELD.finditer(line))
                main_fields = [f for f in fields if f.group(1) not in ("confidence", "contested")]
                if len(main_fields) != 1:
                    errors.append(f"{rel}: expected 1 predicate field: {line}")
                    continue
                f = main_fields[0]
                pred = f.group(1)
                if pred not in vocab:
                    errors.append(f"{rel}: unknown predicate '{pred}': {line}")
                    continue
                subj, s_link = node(line[2:f.start()])
                obj, o_link = node(f.group(2))
                if not subj or not obj:
                    errors.append(f"{rel}: empty subject/object: {line}")
                    continue
                for target in LINK.findall(line):
                    if target.strip() not in names:
                        errors.append(f"{rel}: broken link [[{target}]]")
                extra = {g.group(1): g.group(2) for g in fields if g is not f}
                qualifier = FIELD.sub("", line[f.end():]).strip()
                if pred in FLIP:
                    subj, obj, pred = obj, subj, inverse[pred]
                rows.append({
                    "subject": subj,
                    "predicate": pred,
                    "object": obj,
                    "qualifier": qualifier,
                    "confidence": extra.get("confidence", meta.get("confidence", "")),
                    "contested": extra.get("contested", "false"),
                    "sources": ";".join(parse_list(meta.get("sources", ""))),
                    "page": rel,
                })

    seen, unique = set(), []
    for r in rows:
        key = (r["subject"], r["predicate"], r["object"], r["qualifier"])
        if key not in seen:
            seen.add(key)
            unique.append(r)

    for e in errors:
        print("ERROR", e)
    for m in missing:
        print("MISSING", m)
    pages = len({r["page"] for r in unique})
    print(f"{len(unique)} triplets from {pages} pages; {len(errors)} errors; {len(missing)} area-B pages without section")

    if not check_only and not errors:
        with OUT.open("w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(unique[0].keys()) if unique else ["subject"])
            w.writeheader()
            w.writerows(unique)
        print(f"wrote {OUT.relative_to(ROOT).as_posix()}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

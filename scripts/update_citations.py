"""
research_metadata.xlsx 기존 논문 인용수 업데이트
- KCI article_id  → cite_kci, cite_wos, fwci
- OpenAlex openalex_id → cited_by_count, fwci
"""

import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import openpyxl
import requests

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

META_PATH = Path("D:/soojin/03_marketing/netminer_info/nm-reference/research_metadata.xlsx")
KCI_KEY_PATH = Path("D:/soojin/.claude/config/kci_key.txt")

# 0-based 컬럼 인덱스
COL = {
    "출처":          0,
    "article_id":   21,
    "openalex_id":  22,
    "cited_by_count": 23,
    "cite_kci":     24,
    "cite_wos":     25,
    "fwci":         26,
    "인용합":       30,
}


def get_kci_key() -> str:
    if KCI_KEY_PATH.exists():
        return KCI_KEY_PATH.read_text(encoding="utf-8").strip()
    return "00000001"


def _to_num(v):
    try:
        f = float(v) if v is not None else None
        if f is None:
            return None
        return int(f) if f == int(f) else f
    except (ValueError, TypeError):
        return None


def fetch_kci(article_id: str, key: str) -> dict:
    url = (
        f"https://open.kci.go.kr/po/openapi/openApiSearch.kci"
        f"?apiCode=articleDetail&key={key}&id={article_id}"
    )
    try:
        r = requests.get(url, timeout=10)
        root = ET.fromstring(r.content)
        cc = root.find(".//citation-count")
        fwci_el = root.find(".//fwci")
        result = {}
        if cc is not None:
            result["cite_kci"] = _to_num(cc.get("kci"))
            result["cite_wos"] = _to_num(cc.get("wos"))
        if fwci_el is not None and fwci_el.text:
            result["fwci"] = _to_num(fwci_el.text)
        return result
    except Exception as e:
        print(f"    KCI 오류 ({article_id}): {e}")
        return {}


def fetch_openalex(openalex_id: str) -> dict:
    if openalex_id.startswith("http"):
        work_id = openalex_id.rstrip("/").split("/")[-1]
    else:
        work_id = openalex_id
    url = f"https://api.openalex.org/works/{work_id}"
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "NetMiner-citation-updater"})
        data = r.json()
        result = {}
        if "cited_by_count" in data:
            result["cited_by_count"] = _to_num(data["cited_by_count"])
        if "fwci" in data:
            result["fwci"] = _to_num(data["fwci"])
        return result
    except Exception as e:
        print(f"    OpenAlex 오류 ({openalex_id}): {e}")
        return {}


def calc_sum(row) -> float | None:
    nums = [
        row[COL["cited_by_count"]].value,
        row[COL["cite_kci"]].value,
        row[COL["cite_wos"]].value,
    ]
    valid = [v for v in nums if isinstance(v, (int, float))]
    return sum(valid) if valid else None


print("=== 인용수 업데이트 시작 ===")
wb = openpyxl.load_workbook(META_PATH)
ws = wb.worksheets[0]

key = get_kci_key()
updated = 0
skipped = 0

for row in ws.iter_rows(min_row=2):
    src = row[COL["출처"]].value
    if not src:
        continue

    article_id = str(row[COL["article_id"]].value or "").strip()
    openalex_id = str(row[COL["openalex_id"]].value or "").strip()

    if not article_id and not openalex_id:
        skipped += 1
        continue

    changed = False
    title = str(row[1].value or "")[:50]
    print(f"  [{src}] {title}")

    if article_id:
        data = fetch_kci(article_id, key)
        for field, val in data.items():
            cell = row[COL[field]]
            if cell.value != val:
                cell.value = val
                changed = True
        time.sleep(0.3)

    if openalex_id:
        data = fetch_openalex(openalex_id)
        for field, val in data.items():
            cell = row[COL[field]]
            if cell.value != val:
                cell.value = val
                changed = True
        time.sleep(0.2)

    new_sum = calc_sum(row)
    if row[COL["인용합"]].value != new_sum:
        row[COL["인용합"]].value = new_sum
        changed = True

    if changed:
        updated += 1

wb.save(META_PATH)
print(f"\n완료: {updated}건 업데이트 / {skipped}건 스킵(ID 없음)")

#!/usr/bin/env python3
"""Simple CSV URL checker for Awesome Medical World Models.

Usage:
    python scripts/check_links.py data/papers.csv data/datasets.csv
"""

from __future__ import annotations

import csv
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterable

URL_FIELDS = ("paper_url", "code_url", "project_url", "url")


def iter_urls(paths: Iterable[str]):
    for path_str in paths:
        path = Path(path_str)
        if not path.exists():
            print(f"[warn] missing file: {path}", file=sys.stderr)
            continue
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row_num, row in enumerate(reader, start=2):
                label = row.get("title") or row.get("dataset") or row.get("model") or f"row {row_num}"
                for field in URL_FIELDS:
                    url = (row.get(field) or "").strip()
                    if url:
                        yield {"file": str(path), "row": row_num, "label": label, "field": field, "url": url}


def check_url(url: str, timeout: int = 15) -> dict:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "awesome-medical-world-models-link-checker"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return {"ok": True, "status": response.status, "reason": getattr(response, "reason", "")}
    except urllib.error.HTTPError as exc:
        # Some hosts block HEAD. Try GET before failing.
        if exc.code in {403, 405, 406}:
            try:
                get_req = urllib.request.Request(url, method="GET", headers={"User-Agent": "awesome-medical-world-models-link-checker"})
                with urllib.request.urlopen(get_req, timeout=timeout) as response:
                    return {"ok": True, "status": response.status, "reason": getattr(response, "reason", "")}
            except Exception as get_exc:  # noqa: BLE001
                return {"ok": False, "status": None, "reason": repr(get_exc)}
        return {"ok": False, "status": exc.code, "reason": exc.reason}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "status": None, "reason": repr(exc)}


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2

    report = []
    for item in iter_urls(argv[1:]):
        result = check_url(item["url"])
        merged = {**item, **result}
        report.append(merged)
        mark = "OK" if result["ok"] else "FAIL"
        print(f"[{mark}] {item['field']}: {item['url']} ({result['status']})")
        time.sleep(0.25)

    Path("link_check_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    failed = [r for r in report if not r["ok"]]
    print(f"\nChecked {len(report)} links; failed: {len(failed)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

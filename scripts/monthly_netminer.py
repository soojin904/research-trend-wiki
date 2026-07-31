"""
매달 1일 자동 실행: 지난 달 NetMiner 논문 수집 → research_metadata.xlsx 추가 → citations.xlsx 동기화 → push

사용법:
  python monthly_netminer.py          # 지난 달 자동 계산
  python monthly_netminer.py --dry-run
  python monthly_netminer.py --from-date 2026-01-01 --to-date 2026-01-31  # 수동 지정
"""

import argparse
import calendar
import subprocess
import sys
from datetime import date
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
WIKI_DIR = SCRIPTS_DIR.parent
NETMINER_INFO_DIR = Path("D:/soojin/03_marketing/netminer_info")
NM_REF_DIR = NETMINER_INFO_DIR / "nm-reference"
VENV_PYTHON = Path("D:/soojin/.venv/Scripts/python.exe")
LOG_FILE = SCRIPTS_DIR / "monthly_run.log"


def log(msg: str):
    from datetime import datetime
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def last_month_range() -> tuple[str, str, str, str]:
    """지난 달의 날짜 범위 반환 (OpenAlex 포맷, KCI 포맷)"""
    today = date.today()
    first_this_month = today.replace(day=1)
    last_month_last = first_this_month.replace(day=1) - __import__("datetime").timedelta(days=1)
    last_month_first = last_month_last.replace(day=1)

    oa_from = last_month_first.strftime("%Y-%m-%d")
    oa_to = last_month_last.strftime("%Y-%m-%d")
    kci_from = last_month_first.strftime("%Y%m%d")
    kci_to = last_month_last.strftime("%Y%m%d")
    return oa_from, oa_to, kci_from, kci_to


def run(cmd: list, dry_run: bool = False) -> bool:
    log(f"실행: {' '.join(str(c) for c in cmd)}")
    if dry_run:
        log("  [dry-run] 건너뜀")
        return True
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.stdout:
        for line in result.stdout.strip().splitlines():
            log(f"  {line}")
    if result.returncode != 0:
        log(f"  ERROR (exit {result.returncode})")
        if result.stderr:
            for line in result.stderr.strip().splitlines()[:5]:
                log(f"  STDERR: {line}")
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--from-date", metavar="YYYY-MM-DD")
    parser.add_argument("--to-date", metavar="YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.from_date and args.to_date:
        oa_from, oa_to = args.from_date, args.to_date
        kci_from = oa_from.replace("-", "")
        kci_to = oa_to.replace("-", "")
    else:
        oa_from, oa_to, kci_from, kci_to = last_month_range()

    log(f"=== monthly_netminer 시작 ===")
    log(f"수집 기간: {oa_from} ~ {oa_to}")

    py = str(VENV_PYTHON)
    ok = True

    # 1. KCI 수집
    log("\n[1/5] KCI 수집")
    ok = ok and run([py, str(SCRIPTS_DIR / "fetch_netminer_kci.py"),
                     "--from-date", kci_from, "--to-date", kci_to], args.dry_run)

    # 2. OpenAlex 수집 (citations.xlsx 직접 싱크는 무시하고 .md만 사용)
    log("\n[2/5] OpenAlex 수집")
    ok = ok and run([py, str(SCRIPTS_DIR / "fetch_netminer.py"),
                     "--from-date", oa_from, "--to-date", oa_to], args.dry_run)

    # 3. research_metadata.xlsx 추가
    log("\n[3/6] research_metadata.xlsx 추가")
    ok = ok and run([py, str(SCRIPTS_DIR / "patch_xlsx.py")], args.dry_run)

    # 4. 구분 열 '검증필요' 입력
    log("\n[4/6] 구분='검증필요' 입력")
    ok = ok and run([py, str(SCRIPTS_DIR / "fix_gubun.py")], args.dry_run)

    # 5. 기존 논문 인용수 업데이트
    log("\n[5/6] 인용수 업데이트")
    ok = ok and run([py, str(SCRIPTS_DIR / "update_citations.py")], args.dry_run)

    # 6. citations.xlsx 동기화
    log("\n[6/6] citations.xlsx 동기화 및 push")
    ok = ok and run([py, str(SCRIPTS_DIR / "sync_citations.py")], args.dry_run)

    if not ok:
        log("중간 단계 실패 — push 건너뜀")
        sys.exit(1)

    git = ["git", "-C", str(NETMINER_INFO_DIR)]
    run(git + ["add", "nm-reference/citations.xlsx"], args.dry_run)
    msg = f"Auto: NetMiner citations update {oa_from[:7]} (monthly)"
    run(git + ["commit", "-m", msg], args.dry_run)

    token_file = NETMINER_INFO_DIR / "github_nm.txt"
    if token_file.exists():
        token = token_file.read_text(encoding="utf-8").strip()
        remote_url = f"https://netminer-cyram:{token}@github.com/netminer-cyram/resources.git"
        run(git + ["remote", "set-url", "origin", remote_url], args.dry_run)

    run(git + ["push", "origin", "main"], args.dry_run)

    log(f"\n=== 완료 ({oa_from} ~ {oa_to}) ===")


if __name__ == "__main__":
    main()

# weekly_fetch_ingest.ps1
# 매주 수요일: 논문 수집 → 위키 인제스트 → 지식 합성(synthesize) → GitHub push
# Task Scheduler에서 매주 수요일 20:00에 호출 (트리거 자체가 주간이므로 스크립트 내 날짜 게이트 없음).

$today = Get-Date

$fromDate = $today.AddDays(-7).ToString("yyyy-MM-dd")
$toDate   = $today.ToString("yyyy-MM-dd")

$wikiDir    = "D:\soojin\wiki"
$venvPython = "D:\soojin\.venv\Scripts\python.exe"
$logFile    = "$wikiDir\scripts\weekly_run.log"

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -Encoding UTF8
}

Log "=== 주간 루틴 시작: $fromDate ~ $toDate ==="

# STEP 1. SNA 전문 학술지 수집 → raw/
Log "STEP 1: fetch_openalex.py"
& $venvPython "$wikiDir\scripts\fetch_openalex.py" --from-date $fromDate --to-date $toDate
if ($LASTEXITCODE -ne 0) {
    Log "[오류] fetch_openalex.py 실패"
    exit 1
}

# STEP 2. 키워드 검색 수집 → raw/applied/
Log "STEP 2: fetch_applied.py"
& $venvPython "$wikiDir\scripts\fetch_applied.py" --from-date $fromDate --to-date $toDate
if ($LASTEXITCODE -ne 0) {
    Log "[오류] fetch_applied.py 실패"
    exit 1
}

# STEP 3. 위키 인제스트
Log "STEP 3: wiki:ingest"
Set-Location $wikiDir
$pagesBefore = (Get-ChildItem "$wikiDir\pages\papers\sna", "$wikiDir\pages\papers\applied" -Filter *.md -File | Measure-Object).Count
$ingestPrompt = @"
wiki:ingest 작업을 수행해줘.
raw/sna/, raw/applied/ 폴더 전체에서 index.md에 등록되지 않은 파일을 모두 찾아 위키에 통합해줘.
(raw/netminer/ 는 별도 용도로 수집되는 폴더이므로 이 작업 대상에서 제외)
절차: 소스 분석 → pages/ 에 논문 페이지 생성 → 관련 개념/방법 페이지 업데이트 → overview.md 갱신 → index.md 업데이트 → log.md 기록.
규칙: raw/ 파일은 수정 금지. 위키링크는 [[파일경로|표시텍스트]] 형식.
"@
claude --dangerously-skip-permissions -p $ingestPrompt
if ($LASTEXITCODE -ne 0) {
    Log "[오류] wiki:ingest 실패"
    exit 1
}

# STEP 4. 지식 합성 — 증분 방식 (토큰 절약: 마지막 synthesize 이후 신규 페이지만 읽음, 신규 없으면 건너뜀)
$pagesAfter = (Get-ChildItem "$wikiDir\pages\papers\sna", "$wikiDir\pages\papers\applied" -Filter *.md -File | Measure-Object).Count
$newPages = $pagesAfter - $pagesBefore
if ($newPages -le 0) {
    Log "STEP 4: 신규 논문 페이지 없음 - synthesize 건너뜀"
} else {
    Log "STEP 4: wiki:synthesize (증분, 신규 페이지 $newPages 편)"
    $synthesizePrompt = @"
wiki:synthesize 작업을 범위 지정 없이(증분) 수행해줘.
- log.md에서 가장 최근 synthesize 기록 날짜를 확인하고, 그 이후 새로 추가된 논문 페이지(pages/papers/sna, pages/papers/applied)만 읽어라. 기존 페이지 전체를 다시 읽지 말 것.
- 신규 페이지에서 확인된 내용만 기존 methods/concepts/insights/tools 페이지에 추가·보강하고, 편수·비율 등 집계 수치는 신규분을 더해 갱신해라. 기존 내용을 통째로 다시 쓰지 말 것.
- overview.md·index.md·log.md(synthesize 기록)도 신규분 기준으로만 갱신해라.
규칙: raw/ 파일은 수정 금지. 위키링크는 [[파일경로|표시텍스트]] 형식.
"@
    claude --dangerously-skip-permissions -p $synthesizePrompt *>> "$wikiDir\scripts\weekly_synthesize_output.log"
    if ($LASTEXITCODE -ne 0) {
        Log "[오류] wiki:synthesize 실패 - 상세는 weekly_synthesize_output.log 참고"
        exit 1
    }
}

# STEP 5. GitHub push
Log "STEP 5: git commit & push"
git add .
$status = git status --porcelain
if (-not $status) {
    Log "변경사항 없음. push 생략."
} else {
    git commit -m "chore: $($today.ToString('yyyy-MM-dd')) 주간 논문 수집·인제스트·합성"
    if ($LASTEXITCODE -ne 0) {
        Log "[오류] git commit 실패"
        exit 1
    }
    git push
    if ($LASTEXITCODE -ne 0) {
        Log "[오류] git push 실패"
        exit 1
    }
}

Log "=== 완료 ==="

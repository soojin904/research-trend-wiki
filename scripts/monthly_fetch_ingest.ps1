# monthly_fetch_ingest.ps1
# 매달 말일: 논문 수집 → 위키 인제스트 → GitHub push
# Task Scheduler에서 매월 28~31일 23:00에 호출. 말일이 아닌 날은 즉시 종료.

$today    = Get-Date
$tomorrow = $today.AddDays(1)

if ($tomorrow.Day -ne 1) {
    Write-Host "[$($today.ToString('yyyy-MM-dd'))] 오늘은 말일이 아닙니다. 종료."
    exit 0
}

$fromDate = $today.ToString("yyyy-MM-01")
$toDate   = $today.ToString("yyyy-MM-dd")

$wikiDir    = "D:\soojin\wiki"
$venvPython = "D:\soojin\.venv\Scripts\python.exe"
$logFile    = "$wikiDir\scripts\monthly_run.log"

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -Encoding UTF8
}

Log "=== 월별 루틴 시작: $fromDate ~ $toDate ==="

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
$ingestPrompt = @"
wiki:ingest 작업을 수행해줘.
raw/ 및 raw/applied/ 폴더에서 index.md에 등록되지 않은 파일을 모두 찾아 위키에 통합해줘.
절차: 소스 분석 → pages/ 에 논문 페이지 생성 → 관련 개념/방법 페이지 업데이트 → overview.md 갱신 → index.md 업데이트 → log.md 기록.
규칙: raw/ 파일은 수정 금지. 위키링크는 [[파일경로|표시텍스트]] 형식.
"@
claude --dangerously-skip-permissions -p $ingestPrompt
if ($LASTEXITCODE -ne 0) {
    Log "[오류] wiki:ingest 실패"
    exit 1
}

# STEP 4. GitHub push
Log "STEP 4: git commit & push"
git add .
$status = git status --porcelain
if (-not $status) {
    Log "변경사항 없음. push 생략."
} else {
    git commit -m "chore: $($today.ToString('yyyy-MM')) 논문 수집 및 인제스트"
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

# monthly_fetch_ingest.ps1
# 매달 말일: 해당 월 논문 수집(OpenAlex) → 위키 인제스트
# Task Scheduler에서 매월 28~31일에 호출. 말일이 아닌 날은 즉시 종료.

$today    = Get-Date
$tomorrow = $today.AddDays(1)

if ($tomorrow.Day -ne 1) {
    Write-Host "[$($today.ToString('yyyy-MM-dd'))] 오늘은 말일이 아닙니다. 종료."
    exit 0
}

$fromDate = $today.ToString("yyyy-MM-01")          # 해당 월 1일
$toDate   = $today.ToString("yyyy-MM-dd")          # 오늘(말일)

$wikiDir     = "D:\soojin\wiki"
$venvPython  = "D:\soojin\.venv\Scripts\python.exe"
$fetchScript = "$wikiDir\scripts\fetch_openalex.py"
$logFile     = "$wikiDir\scripts\monthly_run.log"

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -Encoding UTF8
}

Log "=== 월별 논문 수집 시작: $fromDate ~ $toDate ==="

# 1. OpenAlex 수집
Log "STEP 1: fetch_openalex.py 실행"
& $venvPython $fetchScript --from-date $fromDate --to-date $toDate
if ($LASTEXITCODE -ne 0) {
    Log "[오류] fetch_openalex.py 실패 (exit $LASTEXITCODE)"
    exit 1
}

# 2. 위키 인제스트
# -p 모드에서는 슬래시 명령어가 동작하지 않아 프롬프트 텍스트로 전달
Log "STEP 2: wiki:ingest 실행"
Set-Location $wikiDir
$ingestPrompt = @"
wiki:ingest 작업을 수행해줘.
D:\soojin\wiki\raw\ 폴더에서 index.md에 등록되지 않은 파일을 모두 찾아 위키에 통합해줘.
절차: 소스 분석 → pages/ 에 논문 페이지 생성 → 관련 개념/방법 페이지 업데이트 → overview.md 갱신 → index.md 업데이트 → log.md 기록.
규칙: raw/ 파일은 수정 금지. 위키링크는 [[파일경로|표시텍스트]] 형식.
"@
claude -p $ingestPrompt
if ($LASTEXITCODE -ne 0) {
    Log "[오류] wiki:ingest 실패 (exit $LASTEXITCODE)"
    exit 1
}

Log "=== 완료 ==="

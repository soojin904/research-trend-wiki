# full_resynthesize_20261118.ps1
# 1회성: 2026-11-18 23:00 위키 전수 재합성 (SNA + applied 전체). 커밋·푸시는 하지 않는다 (결과 확인 후 수동 또는 다음 주간 실행의 git add . 로 반영).
# 주의: 같은 날 20:00 주간 작업(weekly_fetch_ingest.ps1)이 끝난 뒤에 실행되도록 23:00으로 등록.

$wikiDir = "D:\soojin\wiki"
$logFile = "$wikiDir\scripts\full_resynthesize_20261118.log"
$outFile = "$wikiDir\scripts\full_resynthesize_20261118_output.log"

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -Encoding UTF8
}

Set-Location $wikiDir
Log "=== 전수 재합성 시작 ==="

$prompt = @"
wiki:synthesize all 작업을 수행해줘 (전수 재합성).
- pages/papers/sna/ 와 pages/papers/applied/ 의 개별 논문 페이지 전체(catalog 제외)를 대상으로 한다. SKILL.md의 규모별 전략(200편 초과 시 에이전트 8~10개 병렬 탐색)을 따라라.
- 이전 전수 합성(2026-09-22) 이후의 증분 보강 절(2026-09-30·2026-10-07 보강 등)은 전수 결과로 흡수·통합해서 편수 기준을 하나로 정리해라. 기준 편수는 실제 파일 수로 다시 세라.
- log.md 맨 위 2026-10-07 lint 항목의 후속 확인 메모 3건(보강 절 서술 근거 검증, scripts/synth_findings_*.md 처리 여부는 삭제하지 말고 목록만 보고, netminer.md·catalog 편수 불일치 확인)을 함께 처리해라.
- 기존 methods/concepts/insights/tools 내용을 지우지 말고 추가·보강하는 방식으로 갱신하고, overview.md·index.md·log.md(synthesize 기록)를 갱신해라.
규칙: raw/ 파일은 수정 금지. 논문 페이지는 읽기만. 위키링크는 [[파일경로|표시텍스트]] 형식. git commit/push는 하지 마라.
"@
claude --dangerously-skip-permissions -p $prompt *>> $outFile
if ($LASTEXITCODE -ne 0) {
    Log "[오류] 전수 재합성 실패 - 상세는 full_resynthesize_20261118_output.log 참고"
    exit 1
}
Log "=== 전수 재합성 완료 (커밋 안 함) ==="

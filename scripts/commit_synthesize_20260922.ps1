# commit_synthesize_20260922.ps1
# 1회성 스크립트: 2026-09-22 SNA 318편 + 응용 789편 전수 synthesize 결과 커밋·푸시
# pages/tools/netminer.md(별도 무관 변경사항)와 raw/netminer/ 백로그는 의도적으로 제외

$wikiDir = "D:\soojin\wiki"
$logFile = "$wikiDir\scripts\commit_synthesize_20260922.log"

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -Encoding UTF8
}

Set-Location $wikiDir
Log "=== synthesize 커밋 시작 ==="

$files = @(
    "index.md", "log.md", "overview.md",
    "pages/concepts/mixed_methods.md", "pages/concepts/personal_network.md",
    "pages/concepts/egocentric_network_design.md",
    "pages/insights/applied_data_source_2026.md", "pages/insights/applied_domain_venue_2026.md",
    "pages/insights/applied_method_frequency_2026.md", "pages/insights/netminer_trend_insight.md",
    "pages/insights/sna_method_frequency.md",
    "pages/methods/bayesian_network_model.md", "pages/methods/centrality.md",
    "pages/methods/community_detection.md", "pages/methods/ergm.md", "pages/methods/gnn.md",
    "pages/methods/llm_nlp.md", "pages/methods/longitudinal_network.md",
    "pages/methods/network_scaleup.md", "pages/methods/saom.md",
    "pages/methods/semantic_network_analysis.md", "pages/methods/sentiment_analysis.md",
    "pages/methods/topic_modeling.md", "pages/methods/relational_event_model.md",
    "pages/tools/other_tools.md"
)

git add -- $files
Log "git add 완료 ($($files.Count)개 파일)"

$status = git status --porcelain -- $files
if (-not $status) {
    Log "변경사항 없음(이미 커밋됐거나 되돌려짐). 종료."
    exit 0
}

git commit -m "synthesize: SNA 318편 + 응용분야 789편 전수 재합성 (2026-05-27판 대체)"
if ($LASTEXITCODE -ne 0) {
    Log "[오류] commit 실패"
    exit 1
}
Log "commit 완료"

git fetch origin main
git rebase --autostash origin/main
if ($LASTEXITCODE -ne 0) {
    Log "[오류] rebase 실패 — 수동 확인 필요"
    exit 1
}

git push origin main
if ($LASTEXITCODE -ne 0) {
    Log "[오류] push 실패"
    exit 1
}
Log "=== push 완료 ==="

---
title: "중심성 분석 (Centrality)"
tags: [centrality, degree, betweenness, eigenvector, closeness, structural-measure]
netminer_support: "⚠️ 부분 (기본 7종 ✅ / 신규 이론 변형 ❌)"
updated: 2026-09-22
---

# 중심성 분석 (Centrality)

SNA에서 네트워크 내 노드의 중요도를 수치화하는 지표군. **SNA 전문 학술지 전수 318편 중 25편이 중심성 자체를 연구 주제로 다룬다**(4위, [[pages/insights/sna_method_frequency|방법론 빈도 분석]] 2026-09-22 기준). 다른 방법의 한 구성요소로 중심성을 계산한 논문까지 포함하면 100편을 넘으므로 순위 비교에는 넣지 않았다.

> **2026-09-22 갱신의 핵심**: 학계의 관심은 기본 4종(연결·근접·매개·고유벡터) 산출에서 벗어나, **새로운 중심성 지표를 제안·검증하는 이론 연구**로 옮겨가고 있다. 아래 "신규 이론 변형" 절 참조.

## 핵심 개념

| 지표 | 의미 | 활용 |
|------|------|------|
| **Degree** (연결 중심성) | 직접 연결된 노드 수 | 허브 탐색 |
| out-degree | 내가 선택한 연결 수 | 능동적 연결 행위 |
| in-degree | 나를 선택한 연결 수 | 인기도, 수용 |
| **Closeness** (근접 중심성) | 다른 모든 노드까지의 평균 거리 | 정보 확산 속도 |
| **Betweenness** (매개 중심성) | 최단 경로 상에 위치하는 빈도 | 브로커, 게이트키퍼 탐색 |
| **Eigenvector** | 중요한 노드와 연결된 정도 | 영향력 측정 |
| **PageRank** | 링크 가중치 반영 재귀 중심성 | 웹·멀티플렉스 네트워크 |

### 신규 이론 변형 (318편 전수에서 확인 — 모두 NetMiner 미지원)

| 변형 | 기존 지표와의 차이 | 대표 논문 |
|------|-------------------|-----------|
| **Temporal Betweenness** (시간 매개 중심성) | 링크에 시각이 있는 시간 그래프에서 "실제로 통과 가능한 경로"만 셈. 최선도(foremost)·최속(fastest) 경로 기반 집계는 **#P-hard**로 증명 — 최단 경로 기반이 현실적 대안 | [[pages/papers/sna/2024_bu_algorithmic_aspects_temporal\|Bu 외 (2024)]] |
| **WIP Centrality** (Walk-Independence Probability) | 경로 수가 아니라 **워크(walk) 간 독립성 확률**로 확산 가능성을 근사 — 확산 연구용 휴리스틱 | [[pages/papers/sna/2024_king_walkindependence_probabilities\|King 외 (2024)]] |
| **Distinctiveness Centrality** | 허브와의 연결을 **감점**하고 희소한 상대와의 연결에 가중 — "많이 연결됨"이 아니라 "남다르게 연결됨"을 측정 | [[pages/papers/sna/2024_colladon_why_distinctiveness_centrality\|Colladon & Grippa (2024)]] |
| **멀티플렉스 결합 지표 (MCPR 등)** | 복수 레이어의 PageRank·근접 중심성을 결합 | [[pages/papers/sna/2026_asil_immunization_method_using\|Asil & Khansari (2026)]] |
| **2-mode 전용 중심성** | 행위자-사건 이중성을 투영 없이 직접 측정 | [[pages/concepts/multilayer_network\|다층/이분 네트워크]] 참조 |

공통점: **기존 지표의 가정(정적 그래프·경로 동등성·허브 우대)을 문제 삼는 방향**으로 분화하고 있다.

### 2026-09-30 보강 (SNA 321편 기준 재검토, 2026-10-07 편수 정정)

| 변형 | 내용 | 대표 논문 |
|------|------|-----------|
| **마케팅용 다중 중심성 결합 (8종)** | 인플루언서·오디언스 선정을 위해 8개 중심성 지표를 결합 평가 | [[pages/papers/sna/2024_sziklai_audience_selection_for_maximiz\|Sziklai 외 (2024)]] |
| **대응분석(CA) vs Bonacich 중심성** | 이원 네트워크에서 고전적 Bonacich 중심성과 대응분석 결과를 비교 | [[pages/papers/sna/2025_liardo_the_correspondence_analysis\|Liardo (2025)]] |
| **멀티플렉스 결합 면역화 지표(MCPR)** | PageRank+근접 중심성 결합으로 감염병 면역화 전략 설계 | [[pages/papers/sna/2026_asil_immunization_method_using\|Asil & Khansari (2026)]] |
| **고유벡터 중심성 + Friedkin-Johnsen 확산** | 의견 동학 모형과 중심성을 결합해 영향력 감쇠 추정 | [[pages/papers/sna/2026_murraywatt_the_decay_impact\|Murray-Watters (2026)]] |

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2025_fernandez_centrality_and_social_domains\|Fernandez (2025)]] | 퍼스널 네트워크의 알터 중심성 → 언어 유사성 인식 예측 (다수준 로지스틱 회귀) | 지지 네트워크 중심 알터는 유사성 인식 ↑, 갈등 네트워크는 ↓ |
| [[pages/papers/sna/2022_tasselli_network_centrality_bias\|Tasselli 외 (2022)]] | 직장 네트워크에서 에고의 in-degree 변화 추적 (종단 2개 연구 종합) | 공동 동기 높은 동료가 중심 인물에 유대 형성 → 중심성 편향 발생 |
| [[pages/papers/sna/2023_kim_adolescent_network_positions_a\|Kim & Kim (2023)]] | 사회계측 네트워크 중심성·인기도 → 성인기 기억 수행 예측 (형제 고정 효과 모형) | 청소년기 중심 위치가 성인기 인지 능력과 유의하게 연관 |
| [[pages/papers/sna/2024_neal_methodological_moderators_aver\|Neal (2024)]] | 아동·청소년 우정 네트워크 71편 메타분석 — outdegree centrality 추정치 조절 변수 검토 | 명칭 생성기 방식·선택 횟수 제한이 추정치에 유의미한 영향 |
| [[pages/papers/sna/2026_asil_immunization_method_using\|Asil & Khansari (2026)]] | 멀티플렉스 네트워크에서 PageRank·근접 중심성 결합 MCPR 지표로 면역화 전략 설계 | 10% 면역화 시 홍역 2.2%, 천연두 7% 유행 규모 감소 |
| [[pages/papers/sna/2026_hncean_returning_network_findings\|Hâncean 외 (2026)]] | 퍼스널 네트워크·중심성 등 분석 결과를 비전문가 대상 아트 갤러리(캔버스·조형물)로 "환원(report-back)"하는 커뮤니티 개입 | 103명 방문자 전원 유용성 높게 평가; 단일 분석 레벨-캔버스 매칭이 이해를 도움 — 중심성 등 분석 결과를 일반 대중에 전달하는 방법론 사례 |

### 2026-10-14 보강 (응용 분야 신규 60편 중 중심성 사용 다수 확인, 1,023편 기준)

> 근거: [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026)]] 2026-10-14 증분 갱신 절. 응용 분야(`pages/papers/applied/`) 신규 60편 병렬 탐색(에이전트 4개) 결과.

| 논문 | 적용 방식 | NetMiner 재현성 |
|------|-----------|-----------------|
| [[pages/papers/applied/2026_wu_social_network_analysis\|Wu (2026)]] | 중국 마약거래 조직 네트워크 — 중심성 4종(연결·근접·매개·고유벡터) 비교 | ✅ **완전 재현 가능 — 범죄학 데모 최우선 후보** |
| [[pages/papers/applied/2026_fernndez_semantic_convergence_and_natio\|Fernández (2026)]] | 대학 미션/비전 성명 의미연결망 — Bonacich 중심성 + 계층적 클러스터링 + QAP | ✅ Eigenvector/Status 중심성으로 Bonacich 근사, Word Network+MR-QAP+계층적 클러스터링 모두 지원 — **거의 완전 재현 가능** |
| [[pages/papers/applied/2026_bright_targeting_drug_trafficking_net\|Bright (2026)]] | 약물밀매 네트워크 교란전략 — 매개·연결·고유벡터 중심성 기반 노드 제거 비교 + ERGM 1,000개 시뮬레이션 | ✅ 중심성 3종 지원. ERGM 반복 시뮬레이션은 별도 확인 필요 |
| [[pages/papers/applied/2026_cobo_audit_committee_social_network\|Cobo (2026)]] | 감사위원회 네트워크 — 중심성 4종(연결·고유벡터·매개·근접) + 로지스틱/프로빗 회귀 | ⚠️ 중심성은 지원, 프로빗·순서형 로짓은 통계 메뉴 밖 |
| [[pages/papers/applied/2026_bianchi_firms_collaboration_strategies\|Bianchi (2026)]] | 임업·생태관광 협력전략 — 고유벡터·매개 중심성 + MR-QAP | ✅ 지원 |
| [[pages/papers/applied/2026_giraldi_mapping_italys_tourism_economy\|Giraldi (2026)]] | 이탈리아 관광경제 — in/out-degree·근접·매개·밀도·global efficiency | ✅ 표준 지표 대부분 지원 |
| [[pages/papers/applied/2026_blackburn_social_support_among_lgbtq\|Blackburn (2026)]] | LGBTQ 대학생 에고네트워크 사회적 지지 | ✅ Ego Network Extract 강점 영역 |
| [[pages/papers/applied/2026_melli_given_and_chosen_ties\|Melli (2026)]] | 영국 given/chosen ties 정치행동 — 에고네트워크 지위 동질성(status homophily) | ✅ Ego Network Extract + Assortativity |
| [[pages/papers/applied/2026_sitthirat_moving_towards_decolonizing_he\|Sitthirat (2026)]] | 보건의료교육 공저네트워크 — small-world 계수, 중심성 | ✅ Centrality, Network Metric 지원 |
| [[pages/papers/applied/2026_daoud_intelligent_entity_resolution\|Daoud (2026)]] | 중심성 기반 중복 레코드 탐지(Entity Resolution) — SNA를 데이터품질 문제에 재해석 적용 | ⚠️ 중심성 프레임워크는 가능하나 문자열 유사도(Levenshtein 등)·k-means 병합 로직은 범위 밖. **SNA를 비(非)네트워크 문제에 적용하는 새로운 응용 패턴** |

**신규 기능 공백 확인**: [[pages/papers/applied/2026_zhang_mesoscale_structures_signed\|Zhang (2026, Science Advances)]] — 부호화 네트워크(signed network) 중시구조 탐지, 균형이론(balance theory) 기반 core-periphery 분석. graph-tool 개발자 Peixoto 참여 저명 저널 게재 — **signed network/균형이론 중심성·구조 분석은 NetMiner 미지원 영역으로 신규 확인**.

## 해석 주의사항

- **in-degree ↑가 항상 긍정적이지 않음**: 역할 과부하, 돌봄 요청 부담 등 맥락 의존적 해석 필요
- **방법론적 편향**: 명칭 생성기 설계(친한 친구 vs. 일반 친구)·선택 횟수 제한이 중심성 추정치를 왜곡할 수 있음 (Neal 2024)
- **시간 네트워크**: 중심성의 시간 버전은 계산 복잡도가 높아 알고리즘 선택이 중요

## NetMiner 지원 현황

**✅ 지원 — 표준 중심성 7종**
Degree, Closeness, Betweenness, Eigenvector, Status, PageRank, HITS ([[pages/tools/netminer|기능 목록]] 기준). in/out 구분, 정규화, 시각화 연계, 중심성 값을 독립변수로 한 회귀분석 연결까지 가능. Two-Mode 전용 Degree·Closeness·Betweenness 중심성도 별도 제공.

**❌ 미지원 — 신규 이론 변형**
Temporal Betweenness, WIP Centrality, Distinctiveness Centrality, 멀티플렉스 결합 중심성은 NetMiner에 없다.
- **대안**: R `tsna`/`networkDynamic`(시간 중심성), Python `teneto`, R `SNA4DS`, 저자 배포 코드

### 제품 기획 시사점 (학술 수요 ≠ 지원 여부 분리)

- **학술 수요**: 중심성 주제 25편 중 상당수가 **새 지표 제안**이다. 표준 지표 산출 수요는 이미 포화 상태로 봐야 한다.
- **NetMiner 지원**: 표준 7종은 경쟁력 있는 범위다. 그러나 학계 최신 논의(시간·확산·희소성 기반 지표)와는 단절되어 있다.
- **저비용 기회**: **Distinctiveness Centrality**는 정적 그래프에서 차수 가중만으로 계산되어 구현 비용이 낮으면서도 "허브 편향을 교정한 중심성"이라는 명확한 마케팅 서사가 있다. Temporal Betweenness는 계산 복잡도 문제로 우선순위가 낮다.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석 (318편 전수)]]
- [[pages/methods/relational_event_model|관계 사건 모형 (REM)]] (시간 중심성이 전제하는 이벤트형 데이터)
- [[pages/concepts/multilayer_network|다층 네트워크]] (멀티플렉스 중심성)
- [[pages/tools/netminer|NetMiner]]
- [[pages/methods/ergm|ERGM]] (중심성을 독립변수로 포함하는 통계 모형)
- [[pages/methods/longitudinal_network|종단/동적 네트워크]] (시간에 따른 중심성 변화)
- [[pages/methods/community_detection|커뮤니티 탐지]] (중심성과 군집 구조의 연관)
- [[pages/concepts/personal_network|퍼스널 네트워크]]

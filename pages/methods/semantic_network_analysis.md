---
title: "의미연결망 분석 (Semantic Network Analysis)"
tags: [semantic-network, keyword-network, co-occurrence, text-network]
netminer_support: "✅ 지원"
---

# 의미연결망 분석 (Semantic Network Analysis)

텍스트에서 단어(키워드) 간 공출현(co-occurrence) 관계를 네트워크로 구성하고 분석하는 방법. [[pages/methods/topic_modeling|토픽모델링]]과 함께 텍스트+네트워크 복합 연구의 두 축을 이룬다. SNA 학술지 2020–2026에서 4편이 활용했으며 (15위), 빈도는 낮으나 고유한 적용 맥락을 가진다.

## 핵심 아이디어

- **노드**: 단어·키워드
- **엣지**: 동일 문서(또는 문장, 윈도우) 내 공출현 → 의미적 연관성 프록시
- **중심성 높은 단어** = 해당 담론의 핵심 개념
- **커뮤니티** = 의미적으로 연관된 단어 군집

## 핵심 개념

| 요소 | 설명 |
|------|------|
| 공출현 윈도우 | 문장, 단락, 문서 단위로 달라지며 결과에 큰 영향 |
| 가중치 | 공출현 빈도 또는 PMI(상호정보량) 등 정규화 방식 |
| 시계열 분석 | 동일 네트워크의 시간 슬라이스 비교 → 담론 변화 추적 |
| 커뮤니티 탐지 | 의미 군집 식별 (Suitner 2022) |

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2022_suitner_the_rise_climateaction\|Suitner 외 (2022)]] | 트위터 기후변화 담론 2017–2019 시계열 의미 네트워크 + 커뮤니티 탐지 알고리즘 | FridaysForFuture 이후 집합행동 수사 강화, 인그룹 미래 투영 표현 증가 |
| [[pages/papers/sna/2026_almquist_search_common\|Almquist 외 (2026)]] | 키워드 보조 토픽 모델로 가치 네트워크 추출 → 국가별 협상 구조 분석 | "공정성·권력"에서 "환경·성취" 중심 가치로 전환 |
| [[pages/papers/sna/2023_koskinen_analysing_networks_networks\|Koskinen 외 (2023)]] | 개별 의미 구조를 사회적 유대로 연결하는 다층 네트워크 분석 프레임 | 라인 그래프 변환으로 의미 네트워크의 네트워크 분석 가능 |

## ⭐ 응용 분야 대표 사례 (789편 전수 판독, 2026-09-22)

> 789편 전수 판독에서 **실제 네트워크 데이터를 구성해 분석한 진성 SNA 논문은 ~50–57편(~7%)**이며, 그중 **공출현 기반 의미연결망이 가장 큰 세부 유형**이다. 아래 3편은 **NetMiner 워크플로우로 전 과정 재현이 가능한 최상위 사례**다.
> 근거: [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026, 789편)]]

### 사례 1 — `lie_quantifying_multidisciplinary`: 의료팀 다학제 협업 네트워크

> **789편 전체에서 발견된 최고의 NetMiner 데모 후보**

| 항목 | 내용 |
|------|------|
| 주제 | 의료팀의 다학제 협업 정도 정량화 |
| 네트워크 구성 | 협업 **공출현 네트워크** |
| 분석 지표 | **모듈성(Modularity)** + **Degree / Betweenness / PageRank 중심성** |
| NetMiner 재현성 | ✅ **전 단계 완전 재현 가능** |

**왜 최고 데모 후보인가**:
1. **워크플로우가 NetMiner 메뉴 구조와 정확히 일치**한다 — Pre-process(Word Network/공출현) → Network > Subgroup > Community(Modularity) → Network > Centrality(Degree/Betweenness/PageRank) → Visualize. 억지로 연결한 매칭이 아니다(SCHEMA 규칙 3 충족).
2. **PageRank까지 사용**한다 — NetMiner의 7종 중심성 보유가 실제로 필요한 사례.
3. **도메인이 보건/의료** — 789편 기준 최대 도메인이자 NetMiner 접점이 가장 낮은 미개척 세그먼트.
4. 결과가 **"팀이 실제로 다학제적인가"라는 실무 질문**에 답한다 — 학술 데모를 넘어 기관 고객에게 설명 가능한 가치.

→ 세그먼트 분석: [[pages/insights/applied_domain_venue_2026|응용 분야 도메인 분포 (2026)]]

### 사례 2 — `kim_big_datadriven_topical`: K-pop 연구 지형 키워드 네트워크

| 항목 | 내용 |
|------|------|
| 주제 | K-pop 연구 문헌의 주제 지형도 |
| 네트워크 구성 | **키워드 공출현 네트워크** |
| 분석 지표 | **Degree / Closeness / Betweenness / Eigenvector 4종 중심성** + **Louvain 커뮤니티 탐지** |
| 사용 도구 | **NetworkX** (Python, 명시적 언급) |
| NetMiner 재현성 | ✅ 완전 재현 가능 — 4종 중심성·Louvain 모두 보유 |

**시사점**: 연구자가 **Python으로 코딩해서 수행한 작업을 NetMiner는 노코드 GUI로 동일하게 제공**한다. 게다가 Biblio Data Collector(OpenAlex/KCI/Springer)로 **문헌 수집 단계까지 포괄**하므로, 이 논문의 전 파이프라인이 NetMiner 단일 도구로 커버된다. 한류·문화콘텐츠 연구는 국내 대학 고객과 주제 적합성도 높다 — **국내 마케팅 콘텐츠 소재로 우선 활용 가치**.

### 사례 3 — `gu_analyzing_natural_disaster`: 재난 위험요인 공출현 네트워크

| 항목 | 내용 |
|------|------|
| 주제 | 자연재난 위험요인 구조 분석 |
| 네트워크 구성 | **81편 논문 코퍼스 → 위험요인 공출현 네트워크** |
| 분석 지표 | 중심성 분석 (핵심 위험요인 우선순위화) |
| NetMiner 재현성 | ✅ 완전 재현 가능 |

**시사점**: 코퍼스 규모가 **81편으로 작다** — 대규모 데이터 없이도 의미 있는 의미연결망 분석이 가능함을 보여주는 사례로, **세미나·튜토리얼 데모에 적합**하다. 체계적 문헌고찰(SLR)과 결합하는 패턴이므로 [[pages/concepts/systematic_literature_review|SLR]] 워크플로우와 함께 소개할 수 있다.

### 참고 — 경쟁 도구가 사용된 유사 사례

| 논문 | 방법 | 사용 도구 |
|------|------|----------|
| Guerrero (청크 3) | 2017 멕시코 지진 트위터 SNA, 모듈성·in-degree | Python + **Gephi** (명시) |
| kanbur_mapping_news_categories (청크 4) | Louvain + 모듈성 | 미명시 |
| Park (청크 5) | ESG 담론 공출현 네트워크 + 중심성 | **썸트렌드(Sometrend)** — 한국 상용 텍스트분석 플랫폼 |
| yoo (청크 6) | 한국어 텍스트마이닝 | **TEXTOM** — 한국 상용 플랫폼 |
| khodjaev, makkawi (청크 4) / yin_hang (청크 6) | 서지계량 네트워크 | **VOSviewer**, CiteSpace, R bibliometrix |

> **경쟁 신호**: 의미연결망 분석 수요가 있는 한국 연구자들이 **썸트렌드·TEXTOM**이라는 두 개의 국내 상용 대안을 이미 사용하고 있다(이번 합성에서 각각 독립 확인). 서지계량 영역에서는 **VOSviewer + pyBiblioNet**이 NetMiner Biblio 기능을 직접 압박한다.
> → 도구 상세: [[pages/tools/other_tools|기타 도구]]

---

## 응용 분야 세부 분포 (789편 기준)

응용 분야에서 진성 SNA·네트워크 분석은 ~50–57편(~7%)이며, 그 중 의미연결망(공출현 네트워크)이 가장 큰 비중을 차지한다.

| 세부 유형 | 편수 | 주요 분야 |
|-----------|------|-----------|
| **키워드 공출현 / 의미연결망** | ~18 | ESG 담론, 서지계량, 정책 문서 |
| **중심성 분석** | ~12 | 소셜미디어 영향력, 조직 협업망 |
| **커뮤니티 탐지** | ~8 | 에코챔버, 허위정보, 온라인 커뮤니티 |
| **정보 확산** | ~5 | 허위정보 전파, 영향력 최대화 |
| **다층/에고 네트워크** | ~4 | 멀티플렉스 소셜 네트워크 |
| **종단/동적 네트워크** | ~3 | 협업 혁신 네트워크, SAOM |

**응용 분야 반복 패턴**:
- ESG·정책 문서 → 키워드 공출현 행렬 → SNA 중심성 분석
- 서지계량(SLR) → 저자/키워드 네트워크 → VOSviewer 또는 NetMiner 시각화
- 소셜미디어 텍스트 → 의미연결망 → 에코챔버·허위정보 구조 분석

> **경쟁 도구 주목**: TEXTOM·썸트렌드(한국어 의미연결망 상용 플랫폼), VOSviewer·pyBiblioNet(서지계량 특화), Gephi·NetworkX(무료 오픈소스) — 모두 NetMiner와 직접 경쟁 관계. 특히 국내에서는 TEXTOM·썸트렌드가 NetMiner 대안으로 인식되는 추세.

→ 상세: [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026, 789편)]]

## [[pages/methods/topic_modeling|토픽모델링]]과의 차이

| | 의미연결망 분석 | 토픽모델링 (LDA) |
|--|--|--|
| 단위 | 단어 쌍 (엣지) | 단어 분포 (토픽) |
| 결과 | 네트워크 구조 | 잠재 주제 군집 |
| 강점 | 개념 간 관계 시각화 | 숨겨진 주제 발견 |
| 약점 | 토픽 경계 불명확 | 관계 구조 미포착 |

→ **둘을 함께 쓰면 상호 보완**: 복합 방법론 패턴의 핵심

## NetMiner 지원 현황

✅ 지원 — 한국어 포함 의미연결망 분석 지원. 텍스트 수집부터 공출현 행렬 생성, 네트워크 시각화까지 통합 워크플로우 제공. 시계열 슬라이스 비교 기능으로 담론 변화 분석 가능.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/community_detection|커뮤니티 탐지]] (의미 커뮤니티 식별)
- [[pages/methods/centrality|중심성 분석]] (핵심 개념어 식별)

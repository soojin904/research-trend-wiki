---
title: "토픽모델링 (Topic Modeling)"
tags: [topic-modeling, LDA, BERTopic, text-analysis, keyword-assisted]
netminer_support: "✅ 지원"
---

# 토픽모델링 (Topic Modeling)

문서 집합에서 통계적으로 잠재된 주제(토픽)를 자동 추출하는 방법론. SNA 학술지 2020–2026 논문에서 20편이 활용하며 6위를 기록했다. 인용 네트워크·가치 네트워크·공동체 분석 등 네트워크 연구에서 텍스트 레이어를 분석하는 표준 도구로 자리잡았다.

## 핵심 개념

| 알고리즘 | 특징 |
|----------|------|
| **LDA** (Latent Dirichlet Allocation) | 가장 널리 사용. 문서-토픽, 토픽-단어 확률 분포 |
| **BERTopic** | 임베딩 기반, 의미 이해 강화 |
| **CTM** (Contextualized Topic Model) | 사전학습 언어모델 활용 |
| **Keyword-Assisted Topic Model** | 사전 정의 키워드로 토픽 방향성 제어 (Almquist 2026) |

### 분석 흐름 (LDA)

1. 전처리 (불용어 제거, 형태소 분석)
2. 토픽 수(K) 설정 (코히런스 점수로 최적화)
3. 모델 학습
4. 토픽별 상위 단어 해석
5. 시계열 분석 → 토픽 트렌드

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2026_almquist_search_common\|Almquist 외 (2026)]] | COP 16–28 기후협상 발언문에 키워드 보조 토픽 모델 적용 → 가치 네트워크 추출 | "공정성·권력" 중심에서 "환경·성취" 중심으로 가치 이동 |
| [[pages/papers/sna/2021_keuchenius_adoption_and_adaptation\|Keuchenius 외 (2021)]] | 그라노베터 인용 확산 네트워크에 토픽 모델링 적용 → 학문 공동체별 해석 차이 분석 | 확산은 단순 전달이 아닌 적응·변형 과정; 중심 학자가 공동체 브로커로 기능 |

### 텍스트+네트워크 복합 활용 패턴

토픽모델링 결과를 네트워크 분석 입력값으로 연결하는 파이프라인이 확산 중:
- 텍스트 → 토픽 → 토픽 네트워크 구성 → 중심성·커뮤니티 분석
- 가치 추출 → 국가 간 가치 네트워크 → 협상 구조 해석 (Almquist 2026)
- 인용 확산 → 토픽 공동체 → 아이디어 번역 추적 (Keuchenius 2021)

## 응용 분야 사용 패턴 (789편 전수, 2026-09-22 갱신)

> **분석 기준**: `pages/papers/applied/` **789편 전수 판독**. 토픽모델링은 전체 방법론 중 **3위(~145편, ~18%)**.
> 근거: [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026, 789편)]]

### ⭐ 중요 정정: "BERTopic 실사용 0건"은 SNA 전문지에 한정된 이야기다

**SCHEMA 규칙 2에 따라 어느 문헌의 수치인지를 반드시 구분해야 한다.** 기존 위키에는 "BERTopic — NetMiner 지원 ✅, 실사용 0건"이라는 인사이트가 있었는데, 이 표현은 오해를 낳는다.

| 문헌 범위 | BERTopic 실사용 | 근거 |
|-----------|----------------|------|
| **SNA 전문 학술지** (Social Networks 등, 유형 B) | **0건** | 2021–2026 SNA지 논문 분석. 여전히 유효 |
| **응용/텍스트마이닝 문헌 전반** (유형 C, 789편) | **다수 — 7개 청크 중 4개 이상에서 각각 3건+ 확인, 2026년 대규모 토픽모델링 논문의 사실상 기본값** | 789편 전수 판독 |

즉 **"BERTopic 수요가 없다"는 결론은 틀렸다.** 정확한 서술은 다음과 같다:

> **BERTopic은 응용 분야 문헌에서 이미 LDA를 대체한 표준이며, SNA 전문지에만 아직 진입하지 않았다.**

**마케팅 함의가 정반대로 뒤집힌다.** NetMiner는 BERTopic(+BERTrend)을 이미 탑재하고 있으므로, 이는 *"수요 없는 기능"*이 아니라 **응용 분야 신규 고객(마케팅·보건·정책·관광 연구자)을 향한 최대 미활용 자산**이다. 홍보 우선순위를 상향해야 한다.

### BERTopic > LDA는 확립된 패턴

"LDA vs BERTopic 경주(horse race)"는 이제 독립된 하위 장르다(청크 3). 반복 확인된 판정:

- **수치 코히런스가 LDA에 유리하게 나오더라도, 의미적 해석 가능성에서 BERTopic이 이긴다**(청크 3) — 평가 지표 자체에 대한 문제 제기로 이어지는 중요한 발견.
- 2026년 대규모 토픽모델링 논문은 거의 예외 없이 BERTopic 채택(청크 6).
- 표준 구성: **BERTopic + UMAP + HDBSCAN**(청크 5에서 명시).
- **NMF도 LDA 대비 코히런스 우위**가 반복 확인됨(청크 0).
- 신규 프레임워크 **SemaTopic·ARIA**가 BERTopic을 코히런스 6.2% 추가 개선(청크 1).
- **LLM-in-the-loop 토픽 정제**(신경망 토픽모델 + LLM 레이블링/병합)가 새 방향으로 등장(청크 4).

### 알고리즘별 분포 (789편)

| 방법 | 응용 편수 | 주요 분야 | 비고 |
|------|----------|-----------|------|
| **BERTopic (+BERTrend)** | ~55 | 정책 문서, 소셜미디어, 건설안전, 기후변화, 관광 | **응용 분야 사실상 표준. 2026 논문 기본값** |
| **LDA** | ~70 | 마케팅(리뷰), ESG 담론, 정치 텍스트, 환경·수자원 | 편수는 많으나 **베이스라인·비교군 역할로 이동** |
| **STM** (Structural Topic Model) | ~15 | 정치학, 사회과학, HR/조직, 스페인 의회 | 공변량 통합 가능 — 사회과학 선호 확실화 |
| **keyATM** (키워드 보조 토픽모델) | ~8 | 정책·디지털민주주의, 한국 대선 담론 | R 패키지. 사전 정의 키워드로 토픽 방향 제어 |
| **NMF** | ~7 | 공공행정(민원 분석), Netflix 콘텐츠 진화 | LDA 대안으로 비교 논문에서 반복 등장 |
| **기타** (TopicGPT·FASTopic·SemaTopic·ARIA·BioVMNVTM) | ~8 | CS 방법론 | LLM 기반 / VAE 기반 신규 방법론 |

> **핵심 트렌드**: BERTopic의 LDA 대체가 **완료 단계**. 건설안전(2025_cao), 기후변화(2026_xia), 디지털민주주의(2025_dai), 관광(2026_xu) 등 다분야에서 "BERTopic > LDA" 결론. STM이 정치·사회과학의 사실상 표준으로 확립. keyATM이 정책 담론에서 신흥 방법으로 부상.
> **ABSA와의 경쟁**: 문서 수준 토픽모델링은 ABSA-via-LLM에 밀리는 영역이 생겼다 — LDA 단일 토픽 할당 시 **정보 손실 51.2%**(청크 3). 리뷰·서비스 평가 분석에서는 토픽모델링이 아니라 ABSA가 적합하다.
> → [[pages/methods/sentiment_analysis|감성 분석]] 참조.

**응용 분야 결합 패턴** (789편 기준):
- **토픽모델링 + 감성분석** (~55편): 소비자 리뷰, 소셜미디어 담론, 보건 SNS, 재난 관리
- **토픽모델링 + SNA(키워드 공출현)** (~25편): ESG 담론, 서지계량, 정책 문서, K-POP 학술 지형
- **토픽모델링 + LLM 레이블링** (~20편): GPT 기반 토픽 자동 레이블링, 분류 파이프라인

**2025년 신규 주목 사례**:
- 2025_cao: OSHA 사고보고서 22,623건 — BERTopic vs LDA 비교, BERTopic 현저히 우수
- 2025_park_disappeared: 한국 2022 대선 토론 — keyATM으로 언론 vs 토론 의제 비교
- 2025_willadsen: 직원 설문 개방형 응답 — 비지도 STM이 최소 코딩으로 우수한 결과
- 2026_xia: 중국 정부 정책 문서 12,081개 — BERTopic 계층 토픽+동적 진화 분석

→ 상세: [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026)]]

## [[pages/methods/semantic_network_analysis|의미연결망]]과의 결합

→ 복합 방법론 패턴의 핵심: 토픽 + 네트워크 조합이 SNA 학술지에도 표준 패턴으로 진입

| | 토픽모델링 | 의미연결망 |
|--|------------|-----------|
| 단위 | 단어 분포 (토픽) | 단어 쌍 (엣지) |
| 결과 | 잠재 주제 군집 | 네트워크 구조 |
| 강점 | 숨겨진 주제 발견 | 개념 간 관계 시각화 |

## NetMiner 지원 현황

✅ **지원** — [[pages/tools/netminer|NetMiner 기능 목록]] 확인 기준, Text 메뉴에 **LDA (Raw Text / TDM)**, **BERTopic + BERTrend**, **Topic Evaluation (Perplexity, Coherence)**를 모두 탑재.

> **이전 위키 기재 정정**: 이 페이지는 이전에 "BERTopic 등 임베딩 기반 알고리즘은 Python 연계 필요"라고 기술했으나 오류다. **NetMiner는 BERTopic을 내장 지원**하며, 시계열 토픽 진화를 다루는 **BERTrend**까지 포함한다.

### 학술 수요 vs NetMiner 지원 (SCHEMA 규칙 2)

| 방법 | 응용 문헌 수요 (789편) | SNA 전문지 수요 | NetMiner |
|------|----------------------|----------------|:--------:|
| LDA | ~70편 (베이스라인화) | 19편 | ✅ |
| **BERTopic** | **~55편, 사실상 표준** | **0건** | ✅ **(+BERTrend)** |
| 토픽 평가(코히런스·perplexity) | 표준 절차 | — | ✅ |
| STM | ~15편 | 일부 | ❌ (R stm 연계 안내) |
| keyATM | ~8편 | 1편 (Almquist 2026) | ❌ |
| NMF | ~7편 | — | ❌ |
| LLM-in-the-loop 토픽 정제 | 신흥 | — | ❌ |

**핵심 결론**: NetMiner는 **응용 분야 표준 알고리즘(BERTopic)을 이미 보유**하고 있으면서 이를 홍보하지 못하고 있다. 미보유 항목(STM·NMF·keyATM)은 모두 응용 수요가 상대적으로 작다. 즉 **개발이 아니라 마케팅의 문제**다.

**대안 도구**:
- Python: gensim (LDA), BERTopic, contextualized-topic-models
- R: topicmodels, stm (Structural Topic Model), keyATM, Quanteda

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026, 789편)]]
- [[pages/methods/semantic_network_analysis|의미연결망 분석]]
- [[pages/methods/sentiment_analysis|감성 분석]] (토픽+감성 결합, ABSA 경쟁)
- [[pages/methods/llm_nlp|LLM / NLP 활용]] (LLM 기반 토픽 방법론)
- [[pages/methods/gnn|GNN]] (임베딩 기반 토픽 방법론과의 경계)
- [[pages/tools/netminer|NetMiner]]

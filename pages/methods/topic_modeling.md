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

## 응용 분야 사용 패턴 (682편 기준, 2025–2026)

응용 분야에서 토픽모델링은 전체 방법론 중 3위(~144편, ~21%)를 차지하며, 마케팅·커뮤니케이션·보건·정치 분야에서 광범위하게 활용된다.

| 방법 | 응용 편수 | 주요 분야 | 비고 |
|------|----------|-----------|------|
| **LDA** | ~80 | 마케팅(리뷰), ESG 담론, 정치 텍스트, 환경·수자원 | 여전히 지배적이나 감소 추세 |
| **BERTopic** | ~34 | 정책 문서, 소셜미디어, 건설안전, 기후변화 | LDA 대비 두 배 성장; 다분야에서 BERTopic>LDA 확인 |
| **STM** (Structural Topic Model) | ~15 | 정치학, 사회과학, HR/조직, 스페인 의회 | 공변량 통합 가능 — 사회과학 선호 확실화 |
| **keyATM** (키워드 보조 토픽모델) | ~8 | 정책·디지털민주주의, 한국 대선 담론 | R 패키지. 사전 정의 키워드로 토픽 방향 제어 |
| **NMF** | ~7 | 공공행정(민원 분석), Netflix 콘텐츠 진화 | LDA 대안으로 비교 논문에서 반복 등장 |
| **기타** (TopicGPT·FASTopic·BioVMNVTM) | ~5 | CS 방법론 | LLM 기반 / VAE 기반 신규 방법론 |

> **핵심 트렌드**: BERTopic이 LDA를 대체하는 흐름 가속. 건설안전(2025_cao), 기후변화(2026_xia), 디지털민주주의(2025_dai), 관광(2026_xu) 등 다분야에서 "BERTopic > LDA" 결론. STM이 정치·사회과학의 사실상 표준으로 확립. keyATM이 정책 담론에서 신흥 방법으로 부상.

**응용 분야 결합 패턴** (682편 기준):
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

✅ 지원 — LDA 기반 토픽모델링 내장. 토픽 결과를 네트워크 분석(키워드 네트워크, 공동 출현 행렬)으로 연계하는 워크플로우 가능. BERTopic 등 임베딩 기반 알고리즘은 Python 연계 필요.

**대안 도구**:
- Python: gensim (LDA), BERTopic, contextualized-topic-models
- R: topicmodels, stm (Structural Topic Model)

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/semantic_network_analysis|의미연결망 분석]]
- [[pages/methods/gnn|GNN]] (임베딩 기반 토픽 방법론과의 경계)

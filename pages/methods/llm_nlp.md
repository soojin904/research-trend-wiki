---
title: "LLM / GPT 활용 (Large Language Models)"
tags: [llm, gpt, bert, transformer, fine-tuning, rag, prompt-engineering, llm-network]
netminer_support: "❌ 미지원"
updated: 2026-09-22
---

# LLM / GPT 활용 (Large Language Models)

사전학습 대규모 언어모델(LLM)을 연구 인프라로 활용하는 방법론 범주.

> **2026-09-22 갱신**: `pages/papers/applied/` **789편 전수 판독** 결과 LLM/생성형 AI가 **응용 분야 방법론 1위(~215편, ~27%)**로 올라섰다(이전 682편 집계에서는 2위). 더 중요한 것은 **청크 간 가속 추세**로, 2026년 게재 비중이 높은 후반 청크에서 *"zero-shot 분류와 RAG가 스탠스·감성·도덕가치·이벤트 추출의 명백한 다수파 방법"*이라는 판정이 나왔다.
> 근거: [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026, 789편)]]

---

## 1. ⭐ 핵심 발견: 도메인 특화 소형 모델이 범용 LLM 프롬프팅을 이긴다

**7개 청크 중 4개 이상에서 독립적으로 재현된, 본 합성 전체에서 가장 근거가 탄탄한 발견.**

| 승리한 모델 | 패배한 비교군 | 도메인 | 확인 청크 |
|------------|--------------|--------|----------|
| **ConfliBERT** | GPT 계열 프롬프팅 | 분쟁·정치 이벤트 | 0, 4 |
| **DEBATE, DeBERTa** | 범용 LLM | 담론·논증 분류 | 0 |
| **BERTimbau-LoRA** | 범용 LLM | 포르투갈어 | 4 |
| **RuBioBERT** | 범용 LLM | 러시아어 의생명 | 4 |
| **SVM + TF-IDF (전통 ML)** | LLM zero-shot | 터키어 법률 텍스트 (Çetin) | 3 |

**공통 결론**: 정확도가 동률 이상이면서 **비용·속도는 압도적으로 우수**하다. "크고 범용적인 모델"이 항상 이기지 않는다.

이를 보강하는 부수 증거:
- **"마법의 프롬프트는 없다"**(청크 4): 프롬프트 엔지니어링 메타연구 결과, 효과가 모델 간·태스크 간 일관되지 않음. 신뢰할 만한 범용 프롬프트 기법은 확인되지 않음.
- **4B급 소형 모델 캐스케이드**(청크 4): 전체 LLM 호출 대비 **토큰 96.9% 절감**하면서 성능 유지.

### 제품 기획 시사점

NetMiner가 "범용 LLM 탑재" 경쟁에 뛰어드는 것은 학술 근거상 최적 대응이 아니다. 대신:
1. **도메인 특화 경량 모델을 붙일 수 있는 연동 지점** 설계 (Hugging Face 모델 로드 등)
2. **전통 ML·네트워크 분석의 비용·재현성·해석가능성 강점**을 정면 소구 — 학술 근거가 이를 뒷받침한다
3. LLM은 **전처리 단계**로 위치시키고 NetMiner는 **구조 분석 후단**을 담당하는 파이프라인 포지셔닝

---

## 2. 활용 유형 (789편 기준)

| 유형 | 비중 | 설명 |
|------|------|------|
| **주석·코딩 자동화 (LLM-as-annotator)** | 최대 | 인간 코더 대체. 정치 텍스트 코딩, 임상노트 추출, 스탠스 레이블링 |
| **zero-shot 분류 + RAG 파이프라인** | **급증(2026 다수파)** | 파인튜닝 없이 바로 투입. 청크 6에서 지배적 |
| **도메인 파인튜닝 (LoRA/QLoRA/PEFT)** | 높음 | Llama-3.1-8B-LoRA, BERTimbau-LoRA 등 |
| **벤치마킹·신뢰성 메타연구** | 성장 | LLM 평가 자체가 독립 하위분야로 형성 |
| **멀티에이전트 · LLM-as-judge** | 성장 | 멀티에이전트 토론 프레임워크, LLM이 LLM을 평가 |
| **편향·안전성 분류체계** | 중간 | "7×7×7" LLM 안전 taxonomy 논문군 (청크 3) |
| **LLM 기반 정보추출 / NER** | 중간 | 구조화 추출, 엔티티 그래프 구축 |

### 핵심 모델 계열

| 모델 계열 | 주요 용도 |
|-----------|-----------|
| GPT-4 / ChatGPT / Claude / Gemini | 자동 코딩, RAG, 생성, LLM-as-judge |
| BERT / RoBERTa / DeBERTa | 분류, 감성, NER (여전히 최다 실사용) |
| 도메인 특화 BERT (ConfliBERT·FinBERT·MentalBERT·BioBERT·RuBioBERT·AfroXLMR·IndoBERT) | **1장 발견의 주역** |
| LLaMA / Mistral / Qwen / DeepSeek | 오픈소스 파인튜닝·온디바이스 |

---

## 3. LLM-as-qualitative-coder: 방법론적 신뢰 확보 단계로 진입

> 청크 2 핵심 발견

정성 연구의 코딩 작업을 LLM이 수행하고, **인간 코더와의 일치도를 검증**하는 연구가 하나의 방법론 장르로 자리잡았다.

- **Cohen's κ = 0.96** 수준의 인간-LLM 일치도가 보고됨(청크 2) — "참고용"을 넘어 **방법론적으로 수용 가능한 수준**의 근거.
- **RAG 기반 문헌 종합이 GPT-4o 단독보다 우수**하다는 비교 결과도 함께 확인.
- 전용 도구화도 진행 중: **"Social Verbatim"**, **"Sandpiper"** 등 LLM 기반 정성 코딩 도구가 등장(청크 3) — **LLM 보조 정성연구가 독립 도구 카테고리로 형성 중**이다.

**시사점**: 정성 코딩 → 코드 간 관계 네트워크 구성이라는 워크플로우가 성립한다면, NetMiner의 의미연결망·커뮤니티 탐지가 정성연구자 세그먼트로 진입할 접점이 될 수 있다. 다만 현재 NetMiner에 코딩 기능은 없다.

---

## 4. ⭐ LLM으로 네트워크 형성 이론을 실험하다 (SNA 인접 신규 방향)

> 근거: `papachrist_network_formation` (청크 1)

**멀티 LLM 에이전트 시뮬레이션이 인간의 네트워크 형성 원리를 재현**했다는 연구. 구체적으로 재현된 것:

- **선호적 연결(preferential attachment)**
- **삼각 폐쇄(triadic closure)**
- **동종선호(homophily)**

기존에는 ABM(에이전트 기반 모델)에 규칙을 수동으로 코딩해 넣어야 했으나, LLM 에이전트는 **규칙을 명시하지 않아도 이 구조들이 창발**한다. 이는 SNA 이론 검증의 새로운 실험 패러다임이다. 관련해 소셜미디어 양극화 LLM 시뮬레이션도 확인됨(청크 1).

**NetMiner 관점**: ❌ 지원하지 않으며 단기 로드맵 대상도 아니다. 그러나 **SNA 학계가 LLM과 만나는 가장 흥미로운 지점**이므로 콘텐츠 마케팅(방법론 소개 글) 소재로는 가치가 매우 높다. 시뮬레이션 산출 네트워크를 NetMiner로 분석·시각화하는 데모는 성립한다.

→ 관련: [[pages/concepts/social_network_analysis|SNA 개요]], [[pages/methods/centrality|중심성 분석]]

---

## 5. "LLM as research infrastructure" — 재귀적 메타 장르

> 청크 6 발견

LLM이 연구 도구를 넘어 **연구 활동 자체를 대상으로** 쓰이고 비판되는 장르가 형성되었다.

- LLM 기반 **문헌 리뷰 자동화** (RAG 문헌 종합)
- **피어리뷰 텍스트 분석**
- **"AI가 과학적 단일문화(monoculture)를 만든다"** 비판 연구 — 모두가 같은 모델을 쓰면 연구 다양성이 줄어든다는 문제 제기

**시사점**: 학계에 "AI 도구 의존에 대한 반성적 담론"이 형성되고 있다. **투명하고 검증 가능한 전통 분석 도구**에 대한 재평가 여지가 있으며, NetMiner의 화이트박스 성격은 이 흐름에서 방어 가능한 포지션이다.

---

## 6. 온디바이스 · 경량 배포 트렌드

| 기술 | 확인 내용 |
|------|----------|
| **QLoRA / Unsloth** | 소비자급 GPU에서 파인튜닝 (청크 4) |
| **llama.cpp** | 로컬 추론 배포 (청크 4) |
| **소형 모델 캐스케이드** | 4B 파라미터 다단 파이프라인, 토큰 96.9% 절감 (청크 4) |
| **SLM 캐스케이드** | 온디바이스 소형 언어모델 (청크 5) |

**배경 요인**: 비용, 데이터 프라이버시(의료·법률), API 의존 회피. 5-A의 포스트-API 위기와 같은 방향의 압력이다.
→ [[pages/insights/applied_data_source_2026|응용 분야 데이터 소스 (2026)]] "포스트-API 시대" 절 참조.

---

## 7. NetMiner 지원 현황

❌ **미지원** — LLM 프롬프팅·파인튜닝·RAG·에이전트 기능은 NetMiner에 없으며 연동 경로도 제공되지 않는다.
([[pages/tools/netminer|NetMiner 기능 목록]] 확인 기준. Lab의 Knowledge Graph와 BERT 기반 Sentiment Analysis는 **사전학습 모델 적용**이지 LLM 활용 기능이 아니다.)

### 학술 수요 vs NetMiner 지원 (SCHEMA 규칙 2)

| 항목 | 학술 수요 (789편) | NetMiner |
|------|------------------|:--------:|
| LLM 프롬프팅·zero-shot 분류 | ~215편, 1위, 가속 중 | ❌ |
| RAG | 성장 중 | ❌ |
| LoRA/PEFT 파인튜닝 | 표준화 단계 | ❌ |
| LLM 에이전트 시뮬레이션 | 신흥 | ❌ |
| 사전학습 BERT 모델 적용(감성) | 매우 높음 | ⚠️ Lab, 7개 언어 |

### 포지셔닝 전략

1. **후단(後段) 파이프라인**: LLM으로 분류·추출 → 결과를 NetMiner에서 네트워크·토픽 분석. "LLM + NetMiner" 케이스 스터디 콘텐츠화.
2. **경량 모델 논리 활용**: 1장 발견을 근거로 "무조건 LLM"에 대한 균형 잡힌 방법론 콘텐츠 — 학술적 권위를 가진 차별화 메시지.
3. **검증 가능성 소구**: 5장 메타 담론에 대응해 재현 가능·해석 가능한 분석 도구로 포지셔닝.

---

## 위키 연관

- [[pages/methods/sentiment_analysis|감성 분석]] (BERT 기반 도구와 중첩, ABSA-via-LLM)
- [[pages/methods/topic_modeling|토픽 모델링]] (LLM-in-the-loop 토픽 정제와 경쟁)
- [[pages/methods/text_classification|텍스트 분류]] (전통 ML vs LLM 비교 근거)
- [[pages/concepts/mixed_methods|복합 방법론]]
- [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026, 789편)]]
- [[pages/insights/applied_data_source_2026|응용 분야 데이터 소스 (2026)]]
- [[pages/tools/netminer|NetMiner]]

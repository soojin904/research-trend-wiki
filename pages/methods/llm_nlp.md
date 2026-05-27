---
title: "LLM / GPT 활용 (Large Language Models)"
tags: [llm, gpt, bert, transformer, fine-tuning, rag, prompt-engineering]
netminer_support: "❌ 미지원"
---

# LLM / GPT 활용 (Large Language Models)

사전학습 대규모 언어모델(LLM)을 연구 인프라로 활용하는 방법론 범주. 응용 분야 논문 2026년 수집에서 **1위(~186편, ~31%)**를 차지하는 최대 트렌드. 초기에는 LLM 자체가 연구 대상이었으나, 현재는 기존 인간 코딩·분류 작업을 대체하는 "연구 인프라"로 전환 중.

## 핵심 개념

### 활용 유형

| 유형 | 편수 | 설명 |
|------|------|------|
| **방법론 도구화** (자동 레이블링·분류) | ~70 | 정치 텍스트 자동코딩, 임상노트 정보 추출, 인간 코더 대체 |
| **파인튜닝** (도메인 특화) | ~50 | 법률 BERT, 의료 GPT, AgriBERT, IndoBERTweet |
| **벤치마킹·평가 연구** | ~35 | 모델 비교, 신뢰성 검증, 태스크별 성능 |
| **RAG** (검색 증강 생성) | ~15 | 법률 문서 검색, 의료 RAG 시스템 |
| **편향·안전성 연구** | ~16 | 문화 편향, 독성 탐지, LLM 경계 |

### 핵심 모델 계열

| 모델 계열 | 주요 용도 | 논문 편수 |
|-----------|-----------|-----------|
| **BERT / RoBERTa** | 분류, 감성, NER | ~120 |
| **GPT-4 / ChatGPT** | 자동 코딩, RAG, 생성 | ~60 |
| **도메인 특화 BERT** | 법률·의료·농업·언어별 파인튜닝 | ~40 |
| **LLaMA / Mistral 등** | 오픈소스 LLM 벤치마킹 | ~10 |

## 실제 사용 패턴 (응용 분야 논문 기반)

### 방법론 도구화 사례

- 의회 발언 1500만 개(7개국, 1946–2025) → GPT로 발화 유형 자동 분류 (Aroyehun 2026)
- 인권 침해 보고서 832,220개 단락 → LLM 정보 추출 파이프라인 (Djouvas 2026)
- 인도네시아 정부 정책 트윗 → IndoBERTweet 감성 분류 (Adam 2026)

### 파인튜닝 사례

- 금융 SEC 10-K 공시 → 재무 특화 BERT 파인튜닝 (FINENZO)
- 아랍어 소셜미디어 → AraBERT 도메인 적응
- 저자원 언어(타직어, 텔루구어 등) → 다국어 BERT 적용

## 도구 및 플랫폼

| 도구 | 역할 |
|------|------|
| **Hugging Face Transformers** | 모델 로드·파인튜닝 표준 플랫폼 (~20편 언급) |
| **OpenAI API** | GPT-4 프롬프팅·RAG |
| **LangChain** | RAG 파이프라인 구성 |
| **Google Colab / A100 GPU** | 파인튜닝 실행 환경 |

## NetMiner 지원 현황

❌ **미지원** — LLM 파인튜닝·RAG·프롬프팅은 NetMiner와 연동 불가.

**포지셔닝 전략**:
- LLM을 전처리 도구로 활용한 후 **결과물을 NetMiner에서 SNA/토픽으로 분석**하는 후단(後段) 파이프라인 포지셔닝이 현실적
- 예: GPT로 텍스트 분류 → 분류 결과 기반 의미연결망 구성 → NetMiner에서 시각화·중심성 분석
- "LLM + NetMiner" 결합 워크플로우 케이스 스터디로 차별화 콘텐츠 가능

## 관련 트렌드

- **저자원 언어 NLP 확산**: 아랍어·인도네시아어·베트남어 등 비영어권 연구가 15–20%를 차지
- **설명 가능 AI(XAI) 내재화**: SHAP·LIME 결합이 의료·법률 분야 표준으로 진입
- **LLM vs 인간 코더 비교 연구** 급증 — 방법론적 타당성 검증이 주요 연구 주제

## 위키 연관

- [[pages/methods/sentiment_analysis|감성 분석]] (BERT 기반 감성 분석과 중첩)
- [[pages/methods/topic_modeling|토픽모델링]] (LLM 기반 토픽 방법론과 경쟁)
- [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026)]]
- [[pages/tools/other_tools|Other Tools]] (Hugging Face, Textom)

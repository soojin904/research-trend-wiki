---
title: "Efficient Context Filtering for Extractive Question Answering: A Hybrid Approach with Semantic Validation"
authors: ['Vahid Ghanbarizadeh', 'Amin Moeinian', 'Zahra Younes Pour Langaroudi', 'Mohsen Mohammadagha', 'Athar Sharifi']
year: 2026
venue: "Journal of Computer Science and Technology Studies"
tags: ['Topic Modeling', 'Natural Language Processing Techniques', 'Information Retrieval and Search Behavior']
source: raw/applied/applied_2026_Efficient_Context_Filteri_jcsts_2026_8_2_1.md
---

# Efficient Context Filtering for Extractive Question Answering: A Hybrid Approach with Semantic Validation
**제목(한글)**: 지문 추출형 질의응답을 위한 효율적인 컨텍스트 필터링: 의미론적 검증이 포함된 하이브리드 접근법

**저자**: Vahid Ghanbarizadeh; Amin Moeinian; Zahra Younes Pour Langaroudi; Mohsen Mohammadagha; Athar Sharifi
**출처**: Journal of Computer Science and Technology Studies, Vol.8, pp.01-09
**발행일**: 2026-01-25
**DOI**: https://doi.org/10.32996/jcsts.2026.8.2.1

## 한국어 요약

**연구질문**: 긴 지문을 배경으로 하는 질문 답변(QA) 모델에서 트랜스포머 고유의 연산 복잡도와 문맥 길이 제한 문제를 극복하면서, 질문과 무관한 정보를 사전에 빠르게 필터링해 추론 효율을 극대화하는 방안은 무엇인가?

**방법론**:
- 코사인 유사도, Word Mover's Distance와 같은 파라미터가 필요 없는 전통적 텍스트 유사도 매칭 기법을 Bitap 알고리즘과 결합
- 지문 인코딩 단계 이전에 무관한 문장들을 선별 차단하고, 의심스러운 노이즈 구간만 선택적으로 LLM 기반 사후 검증(Semantic validation)하는 하이브리드 필터링 구현
- SQuAD 2.0 벤치마크 데이터를 투입해 Llama 2 8B, T5-3B 등 모델 상에서 Latency 단축 및 정확도 F1 지표 분석

**주요 결과**:
- 전체 지문을 전부 학습시켰을 때와 비교하여, 제안된 필터링 가동 시 단 5.7% 수준의 미미한 F1 정확도 저하만 감수하면서도 지문 처리 추론 속도를 2.3배 향상시키고 지연 시간(Latency)을 58% 단축시키는 고효율 경량화 성과를 입증함


## 초록 (원문)

Extractive question answering on lengthy documents remains computationally expensive due to quadratic attention complexity and context truncation requirements in modern language models. This work proposes a hybrid context filtering framework that combines classical similarity metrics, including cosine similarity and Word Mover’s Distance, with the Bitap algorithm, and utilizes selective LLM-based validation to reduce inference cost while maintaining competitive accuracy. The method filters irrelevant sentences before passage encoding, thereby reducing computational overhead without requiring learned retrieval components. Evaluation on SQuAD 2.0 across four open-source models (Llama 2 8B, T5-3B, Flan-T5-XL, mT5-Base) using 5-shot learning and fine-tuning demonstrates a 2.3 inference speedup and 58% latency reduction with a modest accuracy trade-off of 5.7% relative F1 degradation compared to full-context baselines. Component ablation confirms the synergistic contribution of each similarity metric, while robustness evaluation across various context lengths and out-of-distribution settings validates the method’s generalization capabilities. These results indicate that intelligent, parameter-free context filtering can achieve meaningful computational efficiency without necessitating complex learned retrievers.

## 키워드

Inference, Robustness (evolution), Context (archaeology), Cosine similarity, Speedup, Similarity (geometry), Computational complexity theory, Latency (audio)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모


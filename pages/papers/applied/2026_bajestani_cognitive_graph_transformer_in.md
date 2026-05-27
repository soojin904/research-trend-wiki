---
title: "Cognitive graph transformer: integrating emotional semantics and lexical concepts for computational personality assessment"
authors: ['Shahryar Salmani Bajestani', 'Seyyed Ali Zendehbad', 'Mohammad Mahdi Khalilzadeh', 'Marjan Vatanpour', 'Elias Mazrooei Rad']
year: 2026
venue: "Scientific Reports"
tags: ['Mental Health via Writing', 'Personality Traits and Psychology', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Cognitive_graph_transform_s41598_026_42640_7.md
---

# Cognitive graph transformer: integrating emotional semantics and lexical concepts for computational personality assessment
**제목(한글)**: 인지 그래프 트랜스포머: 컴퓨터 기반 성격 평가를 위한 감정 의미론과 어휘 개념의 통합

**저자**: Shahryar Salmani Bajestani; Seyyed Ali Zendehbad; Mohammad Mahdi Khalilzadeh; Marjan Vatanpour; Elias Mazrooei Rad
**출처**: Scientific Reports, Vol.None
**발행일**: 2026-05-04
**DOI**: https://doi.org/10.1038/s41598-026-42640-7

## 한국어 요약

**연구질문**: 소셜 미디어 상의 사용자 생성 텍스트를 통해 성격 특성을 예측할 때, 표면적인 통계 분석을 넘어 텍스트의 인지적 성향과 내재적 심리 특성을 그래프 신경망으로 어떻게 정확히 인코딩할 수 있는가?

**방법론**:
- BERT 모델을 미세조정하여 문장 수준 피처를 도출하고 일방향 어텐션 기법으로 감정이 풍부한 단어 강조
- 추출 정보를 노드 특징으로 하여 역동적인 인적 상호작용 그래프를 생성하고, 그래프 신경망과 최종 소프트맥스 분류기를 통합 적용해 Essays 데이터셋으로 검증

**주요 결과**:
- 제안된 인지 그래프 트랜스포머 모델이 Essays 성격 분류 데이터셋에서 타 기법들을 누르고 80.27%의 높은 성격 진단 정확도를 확보해 심리 분석 고도화에 기여함을 증명


## 초록 (원문)

The widespread use of social media has facilitated the recognition of personality from user-generated online content. While numerous applications exist across diverse domains, such as recommender systems, most current studies focus on superficial, statistical, and explicit user content, thereby neglecting latent knowledge. In this study, we propose a method for uncovering latent psycholinguistic understanding at deeper levels of user data to enhance personality prediction through natural language processing. The proposed approach leverages fine-tuning of a domain-specific Bidirectional Encoder Representations from Transformers (BERT) model for sentence-level feature extraction and enriches the output by incorporating emotional information. This process emphasizes salient words through a single-way attention mechanism. Our single-way attention mechanism propagates information from highlighted words to the overall extracted knowledge. Subsequently, using the embeddings from the previous stage as node features, we construct a graph. A dynamic, task-oriented learning approach is then employed to determine the graph edges, using a neural network to connect different pairs of nodes. Finally, a graph neural network is combined with a classifier to predict personality traits. Experimental results demonstrate the effectiveness of the proposed model, achieving 80.27% accuracy on the Essays dataset and outperforming existing approaches. Furthermore, several ablation studies were conducted to investigate the impact of various components and parameters of the proposed architecture.

## 키워드

Classifier (UML), Cognition, Personality, Graph, Salient, Artificial neural network, Feature extraction, Natural language understanding

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모


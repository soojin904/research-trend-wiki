---
title: "STAGE: LLM-Driven Semantic and Topological Augmented Graph Embedding for Text-Attributed Graphs"
authors: ['Shiwei Huang', 'Shunxin Xiao', 'Xu-Yao Zhang', 'Shunzhi Zhu', 'Luoqi Liu', 'Da-Han Wang']
year: 2026
venue: "Mathematics"
tags: ['Advanced Graph Neural Networks', 'Topic Modeling', 'Graph Theory and Algorithms']
source: raw/applied/applied_2026_STAGE_LLMDriven_Semantic__math14091568.md
---

# STAGE: LLM-Driven Semantic and Topological Augmented Graph Embedding for Text-Attributed Graphs
**제목(한글)**: STAGE: 텍스트 속성 그래프를 위한 LLM 구동 의미론적 및 위상학적 증강 그래프 임베딩

**저자**: Shiwei Huang; Shunxin Xiao; Xu-Yao Zhang; Shunzhi Zhu; Luoqi Liu; Da-Han Wang
**출처**: Mathematics, Vol.14, pp.1568-1568
**발행일**: 2026-05-06
**DOI**: https://doi.org/10.3390/math14091568

## 한국어 요약

**연구질문**: 노드 텍스트 정보가 희소하고 주변 구조적 콘텍스트가 광범위한 텍스트 속성 그래프(TAGs)에서, 대형 언어 모델의 유용한 텍스트 요약력을 활용하면서도 연산 훈련 비용을 획기적으로 낮출 수 있는 그래프 표현 학습 방안은 무엇인가?

**방법론**:
- 2단계 STAGE 프레임워크 설계
- 1단계: 고정된 상용 LLM을 오프라인에서 가동하여 노드의 희소한 텍스트 정보를 풍부한 설명문으로 증강하는 단계
- 2단계: 글로벌 토큰 예산(global token budget) 제약 하에, 무작위 보행(random-walk) 기반의 구조 맥락을 추출하고 그래프 조건부 토큰 축소 기법을 가해 PLM 인코더에 주입하는 학습 단계
- 7개 벤치마크 그래프 데이터셋을 투입해 성능 평가

**주요 결과**:
- STAGE 모델은 대량의 LLM 미세 조정 연산 비용 없이 오프라인 사전 파싱만으로 최신 그래프 모델들의 노드 분류 정확도를 고르게 상회함
- 메모리 제약 조건 하에서도 유효한 의미론적 정보의 길이를 가볍게 유지시키는 강건한 토큰 제어 효율을 검증함


## 초록 (원문)

Text-attributed graphs (TAGs) require models to jointly exploit node text and graph structure, yet doing so effectively remains difficult when node text is sparse and the structural context is large. Here, we propose STAGE (Semantic and Topological Augmented Graph Embedding), a two-stage framework for representation learning on TAGs. In Stage I, a frozen large language model is used offline to generate explanatory text that enriches compressed node attributes without introducing online LLM training cost. In Stage II, STAGE performs structure-aware representation learning under a fixed global token budget by combining random-walk-based structural context with graph-conditioned token reduction before PLM encoding. This design preserves informative semantic content while preventing unconstrained sequence expansion. Experiments on seven benchmark datasets show that STAGE consistently outperforms strong baselines under the same evaluation setting and maintains favorable efficiency under bounded input-length constraints.

## 키워드

Embedding, Security token, Node (physics), Graph, Context (archaeology), Exploit, Topological graph theory, Dependency graph

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모


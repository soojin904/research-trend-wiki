---
title: "Graph Neural Networks for Graphs With Heterophily: A Survey"
authors: ['Xin Zheng', 'Yi Wang', 'Yixin Liu', 'Ming Li', 'Miao Zhang', 'Di Jin', 'Philip S. Yu', 'Shirui Pan']
year: 2026
venue: "IEEE Transactions on Knowledge and Data Engineering"
tags: ['Advanced Graph Neural Networks', 'Complex Network Analysis Techniques', 'Recommender Systems and Techniques']
source: raw/applied/applied_2026_Graph_Neural_Networks_for_tkde_2026_3680353.md
---

# Graph Neural Networks for Graphs With Heterophily: A Survey
**제목(한글)**: 이종성(Heterophily) 그래프를 위한 그래프 신경망 기술 동향 조사

**저자**: Xin Zheng; Yi Wang; Yixin Liu; Ming Li; Miao Zhang; Di Jin; Philip S. Yu; Shirui Pan
**출처**: IEEE Transactions on Knowledge and Data Engineering, Vol.None, pp.1-20
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1109/tkde.2026.3680353

## 한국어 요약

**연구질문**: 동일 클래스 노드가 서로 인접하다는 동질성(homophily) 가정을 기반으로 작동하는 일반적인 GNN 모델이, 서로 다른 라벨의 노드들이 주로 연결되는 이종성(heterophily) 그래프 환경에서 나타나는 한계점은 무엇이며 이를 극복하기 위한 기법은 어떻게 분류되는가?

**방법론**:
- 최근 발표된 이종성(heterophilic) 그래프 신경망 모델의 정량 분석 및 기술 분류 체계(systematic taxonomy) 수립
- 이종 그래프의 수치적 정의 지표 비교 및 이종성을 포착하기 위한 GNN 이웃 집계(neighborhood aggregation) 개량 방법론 종합 분석

**주요 결과**:
- 이종성 그래프 학습 성능을 높이기 위해 제안된 최신 아키텍처(공간적 필터 조율, 고차 그래프 활용, 노드 자질 분리 학습 등)의 장단점을 명확히 정리
- 이종성이 그래프 분야의 타 연구 도메인(이상 탐지, 강건성, 표현 학습)에 미치는 파급 효과를 설명하고 향후 해결해야 할 주요 연구 로드맵 제시


## 초록 (원문)

Recent years have witnessed fast developments of graph neural networks (GNNs) that have benefited myriad graph analytic tasks and applications. Most GNNs rely on the homophily assumption that nodes belonging to the same class are more likely to be connected. However, as a ubiquitous graph property in numerous real-world scenarios, heterophily, i.e., nodes with different labels tend to be linked, significantly limits the performance of tailor-made homophilic GNNs. Hence, <italic xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">GNNs for heterophilic graphs</i> are gaining increasing research attention to enhance graph learning with heterophily. In this paper, we provide a comprehensive review of GNNs for heterophilic graphs. Specifically, we propose a systematic taxonomy that governs existing heterophilic GNN models, along with general summaries and detailed analyses. Furthermore, we discuss the relationship between heterophily and various graph research domains, aiming to facilitate the development of more effective GNNs across a spectrum of practical applications and learning tasks in the graph research community. In the end, we point out potential directions to advance and inspire future research and applications on heterophilic graph learning with GNNs.

## 키워드

Computer science, Homophily, Theoretical computer science, Graph, Machine learning, Data science, Artificial intelligence, Mathematics

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


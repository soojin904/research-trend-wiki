---
title: "A Gated Attention-Based Multi-Model Fusion Framework for Dynamic Topic Evolution and Complaint-Driven Latent Issue Mining in Online Tourism Reviews"
authors: ['Liangwu Xu', 'Xiangjin Ran', 'Lili Yao', 'Zhaoji Lin']
year: 2026
venue: "Information"
tags: ['Digital Marketing and Social Media', 'Diverse Aspects of Tourism Research', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_A_Gated_AttentionBased_Mu_info17030270.md
---

# A Gated Attention-Based Multi-Model Fusion Framework for Dynamic Topic Evolution and Complaint-Driven Latent Issue Mining in Online Tourism Reviews
**제목(한글)**: 온라인 관광 리뷰의 동적 토픽 진화 및 컴플레인 유발 잠재 문제 발굴을 위한 게이트 어텐션 기반 다중 모델 융합 프레임워크

**저자**: Liangwu Xu; Xiangjin Ran; Lili Yao; Zhaoji Lin
**출처**: Information, Vol.17, pp.270-270
**발행일**: 2026-03-09
**DOI**: https://doi.org/10.3390/info17030270

## 한국어 요약

**연구질문**: 기존의 정적이고 조립식인 리뷰 분석 한계를 넘어, 글로벌 문맥(SBERT)과 로컬 피처(BERT-TextCNN) 및 토픽 가중치(BTM)를 게이트 기법으로 융합해 관광객 불만 및 트렌드를 다각도로 포착할 수 있는가?

**방법론**:
- Sentence-BERT 어텐션의 글로벌 의미, BERT-TextCNN의 로컬 자질, Biterm Topic Model(BTM)의 단편 텍스트 토픽 분포를 병합하는 학습 가능한 게이트 메커니즘 설계
- 30만 건의 중국 대형 여행 플랫폼(Ctrip, Meituan) 리뷰 데이터셋 학습 및 분류 실험
- 융합된 의미 벡터의 UMAP 시각화 및 K-means++ 클러스터링 기반 시계열 강 변화 맵(River map) 분석

**주요 결과**:
- 다중 모델 의미론 융합을 통해 리뷰 주제 분류 정확도 F1-Score 92.3%를 달성하여 텍스트 의미 정밀 추출 기능 확인
- 풍경, 교통, 편의시설, 관리 수준, 현지 문화, 비용 가치 등의 동적 토픽 진화 경향성을 규명
- 부정 리뷰 분석을 통해 시즌별로 반복되는 고질적 관광 민원(complaint) 패턴을 시각화하여 스마트 관광 관리 개선 방향 도출


## 초록 (원문)

To address the limitations of static and coarse-grained analysis in mining online tourism reviews, this study proposes a gated attention-based multi-model fusion framework for dynamic topic evolution and complaint-driven latent issue pattern mining. Using 300,000 reviews from Ctrip and Meituan, we fuse global semantics from Sentence-BERT with attention (SBERT-Attention), local features from Bidirectional Encoder Representations from Transformers–Text Convolutional Neural Network (BERT-TextCNN), and topic distributions from the Biterm Topic Model (BTM) via a learnable gating mechanism. The fused model achieves an F1-score of 92.3% in review classification. We partition the corpus quarterly and apply Uniform Manifold Approximation and Projection (UMAP) followed by K-means++ clustering to the fused vectors, yielding interpretable topics, including Scenery, Transportation, Amenities, Management, Culture, and Value for Money, and enabling dynamic topic discovery over time. River map visualizations and negative review analysis reveal seasonal evolution patterns and recurring complaint patterns associated with specific topics. The framework enables dynamic, interpretable semantic mining, advancing intelligent processing of short-text user content and offering a generalizable approach for temporal knowledge discovery in smart tourism and beyond.

## 키워드

Topic model, Semantics (computer science), Cluster analysis, Geospatial analysis, Tourism, Convolutional neural network, Partition (number theory), Fuse (electrical)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모


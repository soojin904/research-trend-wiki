---
title: "BiovMNVTM: A Geometry-Aware Neural Topic Model for Biomedical Text Analysis via von Mises–Fisher Mixtures"
authors: ['Dayu Guo', 'Zhiwen Luo', 'Nizar Bouguila', 'Wentao Fan']
year: 2025
venue: ""
tags: ['Topic Modeling', 'Biomedical Text Mining and Ontologies', 'Machine Learning in Healthcare']
source: raw/applied/applied_2025_BiovMNVTM_A_GeometryAware_bibm66473_2025_11356888.md
---

# BiovMNVTM: A Geometry-Aware Neural Topic Model for Biomedical Text Analysis via von Mises–Fisher Mixtures

**제목(한글)**: BiovMNVTM: 폰 미제스-피셔 혼합 분포를 활용한 기하학 인식 신경 토픽 모델

## 한국어 요약

**연구질문**: 기존 신경 토픽 모델(NTM)의 의미 공간 기하학적 구조 무시 문제와 도메인 특화 적응 부족 문제를 어떻게 극복하여 생의학 텍스트 분석에서 토픽 일관성과 문서 클러스터링을 개선할 수 있는가?

**방법론**:
- 변분 오토인코더(VAE) 기반의 신경 토픽 모델링 프레임워크 개발
- 폰 미제스-피셔(von Mises-Fisher, vMF) 혼합 분포를 활용한 초구(hypersphere) 상의 방향적 관계 모델링
- BioBERT 기반 생의학 도메인 특화 임베딩 통합
- 다수의 생의학 데이터셋에서 실험적 평가 수행

**주요 결과**:
- BiovMNVTM은 토픽 품질과 클러스터링 능력에서 기존 LDA 및 NTM 대비 우수한 성능을 달성함
- 기하학적 구조 및 도메인 인식 모델링의 통합이 생의학 토픽 발견에 효과적임을 입증

**저자**: Dayu Guo; Zhiwen Luo; Nizar Bouguila; Wentao Fan
**출처**: , Vol.None, pp.3648-3653
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.1109/bibm66473.2025.11356888

## 초록 (원문)

Topic modeling plays a vital role in uncovering latent semantic structures from large-scale biomedical corpora. While classical probabilistic models such as Latent Dirichlet Allocation (LDA) have been widely used, they often struggle with scalability and capturing complex semantic relationships in domain-specific contexts. Neural topic models (NTMs) based on variational autoencoders (VAEs) provide a more flexible and scalable alternative. However, existing NTMs face two key challenges: the neglect of the underlying geometric structure of semantic spaces and the lack of domain-specific adaptation, both of which contribute to suboptimal topic coherence and weak document clustering. To address these limitations, we pro-pose BiovMNVTM, a geometry-aware variational topic modeling framework tailored for biomedical text analysis. BiovMNVTM leverages the von Mises-Fisher (vMF) mixture distribution to model directional relationships on the hypersphere and integrates contextualized biomedical embeddings from BioBERT to capture rich, domain-specific semantics. Comprehensive experiments on multiple biomedical datasets show that BiovMNVTM achieves superior performance in terms of topic quality and clustering ability, demonstrating the effectiveness of incorporating geomet-ric and domain-aware modeling in biomedical topic discovery.

## 키워드

Topic model, Latent Dirichlet allocation, Cluster analysis, Scalability, Document clustering, Probabilistic logic, Semantics (computer science), Key (lock)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모


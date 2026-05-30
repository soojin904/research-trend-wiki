---
title: "An adversarial variational graph autoencoder with contrastive learning for robust anomaly detection in large scale attributed networks"
authors: ['Wasim Khan', 'Nadhem Ebrahim', 'Mohammad Ishrat', 'Hasan Alkahtani', 'Theyazn H. H. Aldhyani']
year: 2025
venue: "Journal Of Big Data"
tags: ['Advanced Graph Neural Networks', 'Complex Network Analysis Techniques', 'Anomaly Detection Techniques and Applications']
source: raw/applied/applied_2025_An_adversarial_variationa_s40537_025_01342_z.md
---

# An adversarial variational graph autoencoder with contrastive learning for robust anomaly detection in large scale attributed networks

**제목(한글)**: 대규모 속성 네트워크에서 강건한 이상 탐지를 위한 대조 학습 기반 적대적 변분 그래프 오토인코더

## 한국어 요약

**연구질문**: 대규모 속성 네트워크에서 복잡한 구조적 관계와 고차원 노드 속성을 동시에 고려하여 강건하게 이상을 탐지하고, 데이터 불균형 문제를 해결할 수 있는 효과적인 방법은 무엇인가?

**방법론**:
- 적대적 변분 그래프 오토인코더 (Adversarial Variational Graph Autoencoder, VGAE)
- 어텐션 기반 잔차 모델링 (Attention-based Residual Modeling)
- 대조 학습 (Contrastive Learning)
- 적대적 훈련 (Adversarial Training)

**주요 결과**:
- 어텐션 기반 잔차 모델링을 통해 노드 임베딩을 강화하고 구조적 세부 정보를 보존하여 이상 탐지 성능을 향상시킴.
- 적대적 훈련은 임베딩의 과적합을 방지하고 정상/이상 노드를 더욱 명확하게 분리하여 강건성을 확보함.
- 대조 학습을 도입하여 지역적(하위 커뮤니티) 수준에서도 이상 탐지가 가능하도록 임베딩을 개선함.
- 불균형 데이터 문제에 효과적으로 대처하며, 다양한 실제 데이터셋에서 기존 최신 이상 탐지 기술보다 우수한 AUC 및 평균 정밀도 성능을 달성함.

**저자**: < >

## ѱ 

****: <>

****:
- <׸>

**ֿ **:
- <׸>


**저자**: Wasim Khan; Nadhem Ebrahim; Mohammad Ishrat; Hasan Alkahtani; Theyazn H. H. Aldhyani
**저자**: Journal Of Big Data, Vol.13
**저자**: 2025-12-14
**저자**: https://doi.org/10.1186/s40537-025-01342-z

## 초록 (원문)

Abstract Anomaly detection in attributed networks is challenging because it combines complex structural relationships with high-dimensional node attributes. Traditional methods rarely solve both problems simultaneously, making them less effective. We present a new approach for anomaly detection that uses adversarial variational graph autoencoders (VGAE) with attention-based residual modeling and contrastive learning to address these issues. The attention-based residual component enhances node embeddings by emphasizing critical connections and preserving essential structural details, improving anomaly detection by retaining subtle yet important information. VGAE is explicitly trained to combine the structure and features into a joint embedding space, while adversarial training prevents overfitting by making embeddings more robust against noise and pushing normal/abnormal nodes further apart. To improve these embeddings, we include the contrastive learning component to move nodes belonging to a community closer and separate them from other communities so that an intrusion or anomaly could be recognized as malicious not only at global levels but inside one or more specific subcommunities at local levels as well. Our method is also capable of dealing effectively with the challenge of imbalanced data in which normal patterns might dominate during training, thus incompetent to detect rare anomalies. Through the execution of extensive experimental investigations utilizing diverse real-world datasets, we establish that our methodology exceeds the performance of the existing premier anomaly detection techniques with respect to both AUC and average precision metrics. These characteristics bestow upon our model a dual advantage of efficacy and scalability, thereby facilitating its applicability to a myriad of practical scenarios, including but not limited to fraud detection in telecommunication networks, spammer hunting in social networks, or identifying errors/omissions of citation information.

## 키워드

Overfitting, Anomaly detection, Autoencoder, Adversarial system, Residual, Node (physics), Graph, Embedding

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모



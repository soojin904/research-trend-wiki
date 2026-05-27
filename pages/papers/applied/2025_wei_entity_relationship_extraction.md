---
title: "Entity relationship extraction method based on dependency parsing and graph neural networks"
authors: ['Fupeng Wei', 'Xing Liu', 'Limin Pan', 'Wen Zhao', 'Ge Shi', 'Zhaohui Zeng', 'Yibo Jiao']
year: 2025
venue: "Scientific Reports"
tags: ['Advanced Graph Neural Networks', 'Topic Modeling', 'Data Quality and Management']
source: raw/applied/applied_2025_Entity_relationship_extra_s41598_025_33922_7.md
---

# Entity relationship extraction method based on dependency parsing and graph neural networks

**제목(한글)**: 의존 구문 분석과 그래프 신경망 기반 개체 관계 추출 방법

## 한국어 요약

**연구질문**: 캠퍼스 보안 관련 텍스트에서 중복 관계 및 원거리 개체 간 약한 연관성으로 인한 모호성과 낮은 재현율 문제를 해결하고, 지식 그래프 구축에 활용 가능한 정밀한 삼항 관계(triplet) 추출 모델을 어떻게 구현할 수 있는가?

**방법론**:
- 전역 의미 의존성 및 구문 의존성의 이중 분석 메커니즘과 의존 구문 파서를 결합한 MGRel 모델 개발
- 계층적 의미 그래프 합성곱 신경망(hierarchical semantic graph convolutional neural network) 아키텍처와 어텐션 기반 다특징 융합 모듈 통합
- NYT, WebNLG, DuIE 세 가지 범용 벤치마크 데이터셋에서 평가

**주요 결과**:
- MGRel 모델이 NYT에서 F1 +1.3%, WebNLG에서 +0.4%, DuIE에서 +3.2%로 기존 최적 모델 대비 유의미한 성능 향상을 달성
- 캠퍼스 교통안전 관리에서 지식 그래프 구축을 위한 정보 획득에 실질적 적용 가능성을 확인

**저자**: Fupeng Wei; Xing Liu; Limin Pan; Wen Zhao; Ge Shi; Zhaohui Zeng; Yibo Jiao
**출처**: Scientific Reports, Vol.16, pp.3827-3827
**발행일**: 2025-12-29
**DOI**: https://doi.org/10.1038/s41598-025-33922-7

## 초록 (원문)

To support campus security governance, especially campus traffic safety management, many ternary extraction techniques in knowledge graphs rely on character-level text analysis; however, the differences between word semantics and overall word meanings often lead to ambiguity and overlap in ternary extraction. Traditional methods are difficult to effectively manage overlapping relationships in text, which seriously damages the flexibility and extraction accuracy of the dataset. In addition, entity separation significantly affects entity relationship triplet extraction, and weak associations between remote entities often blur entity boundaries and reduce recall rates. This study offers the MGRel entity relationship extraction model, which integrates dependent syntactic analysis with a graph neural network to address the issues above and enhance knowledge acquisition for campus security scenarios. Firstly, by incorporating the dependent syntactic parser alongside the dual analysis mechanism of global semantic dependency and syntactic dependency, it effectively captures long-distance semantic associations and enhances entity relationship recognition accuracy; secondly, it devises the architecture of a hierarchical semantic graph convolutional neural network to facilitate the fine-grained extraction of deep implied semantic features among entities; finally, the attention-driven multi-feature fusion module is presented to improve the discriminative capacity of the ternary classifier via a noise filtering approach. The experimental results on three core general-purpose benchmark datasets-NYT, WebNLG, and DuIE-show that the F1 score of this model increases by 1.3, 0.4 and 3.2%, respectively, compared with the current optimal model, demonstrating a considerable advantage over the comparative techniques and potential value for campus security-oriented campus traffic safety applications.

## 키워드

Convolutional neural network, Parsing, Classifier (UML), Semantic matching, Relationship extraction, Discriminative model, Ambiguity, Dependency grammar

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모


---
title: "Hybrid Model for Authorship attribution of English-language texts"
authors: ['В.М. Бадзь', 'В.М. Теслюк']
year: 2026
venue: "COMPUTER-INTEGRATED TECHNOLOGIES EDUCATION SCIENCE PRODUCTION"
tags: ['Authorship Attribution and Profiling', 'Hate Speech and Cyberbullying Detection', 'Topic Modeling']
source: raw/applied/applied_2026_Hybrid_Model_for_Authorsh_6775_2524_0560_2026_62_13.md
---

# Hybrid Model for Authorship attribution of English-language texts
**제목(한글)**: 영어 텍스트의 저자 식별(Authorship Attribution)을 위한 하이브리드 모델

**저자**: В.М. Бадзь; В.М. Теслюк
**출처**: COMPUTER-INTEGRATED TECHNOLOGIES EDUCATION SCIENCE PRODUCTION, Vol.None, pp.118-123
**발행일**: 2026-03-28
**DOI**: https://doi.org/10.36910/6775-2524-0560-2026-62-13

## 한국어 요약

**연구질문**: 데이터가 부족하거나 도메인이 교차하는 상황에서, 전통적 문체 분석(stylometry)의 해석력과 트랜스포머 임베딩의 풍부한 문맥 표현력을 융합해 고성능 저자 식별 모델을 구축할 수 있는가?

**방법론**:
- RoBERTa 임베딩(문맥 의미)과 전통 문체론 피처(어휘 풍부도, 통사 패턴, 문장부호 사용률 등)의 결합
- 동일 저자의 임베딩 공간 내 밀집도와 다른 저자 간 분리도를 극대화하는 지도형 대조 학습(supervised contrastive learning) 적용
- 다중 저자 및 장르로 구성된 합성 벤치마크 데이터를 통해 기준 모델과의 정확도 성능 비교 평가

**주요 결과**:
- 제안된 하이브리드 모델이 정확도 0.91, 매크로 F1-Score 0.90을 달성하여 기존 트랜스포머 파인튜닝 모델 대비 뛰어난 성능 향상 확인
- 학습 데이터가 극도로 부족한 저자원 상태에서도 높은 식별 견고성(robustness)과 해석 가능성을 확보하여 표절 탐지 및 디지털 법의학 텍스트 증거 확보에 유용함을 입증


## 초록 (원문)

Authorship attribution is a critical task in computational linguistics, digital forensics, and information security, particularly in the context of rapidly growing digital textual data. Traditional stylometric approaches rely on handcrafted linguistic features such as lexical richness, syntactic patterns, and punctuation statistics. Although these methods are interpretable and computationally efficient, they often fail to capture deeper semantic and contextual properties of texts. Transformer-based models, including BERT and RoBERTa, have demonstrated significant improvements in natural language processing tasks due to their ability to model contextual dependencies; however, they often produce embeddings that are insufficiently discriminative for fine-grained authorship attribution, especially in low-resource and cross-domain scenarios. This paper presents a hybrid model for authorship attribution of English-language texts that integrates RoBERTa embeddings, stylometric features, and supervised contrastive learning. The developed architecture constructs unified authorial representations in a latent feature space, where contrastive learning enforces intra-author compactness and inter-author separability. Stylometric features complement transformer-based embeddings by capturing stylistic and structural characteristics of texts, which enhances robustness and interpretability. The fusion of heterogeneous features is performed through a projection network that maps the combined representation into a discriminative latent space. Experimental evaluation was conducted on synthetic benchmark datasets simulating multiple authors and genres. The created hybrid model significantly outperformed baseline models based on stylometry and transformer fine-tuning. The hybrid model achieved an accuracy of 0.91 and a macro-averaged F1-score of 0.90, demonstrating improved robustness under limited training data conditions. The results confirm that contrastive learning substantially improves the separability of author classes in the embedding space. The developed model can be applied in plagiarism detection systems, forensic linguistic analysis, and digital authorship verification in information systems.

## 키워드

Discriminative model, Robustness (evolution), Stylometry, Punctuation, Feature learning, Natural language understanding, Computational linguistics, Authorship attribution

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모


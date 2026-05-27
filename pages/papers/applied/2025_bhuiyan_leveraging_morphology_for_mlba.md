---
title: "Leveraging Morphology for ML-based Classification of Genre for Bangla Literature"
authors: ['Afsarul Amin Bhuiyan', 'Ahmed Shafi Arnob', 'Tamanna Haque Nipa', 'Rahad Hussain', 'A. B. M. Alim Al Islam']
year: 2025
venue: ""
tags: ['Authorship Attribution and Profiling', 'Text Readability and Simplification', 'Topic Modeling']
source: raw/applied/applied_2025_Leveraging_Morphology_for_3777555_3777576.md
---

# Leveraging Morphology for ML-based Classification of Genre for Bangla Literature

**제목(한글)**: 방글라 문학 장르 분류를 위한 형태론 기반 머신러닝 접근법

## 한국어 요약

**연구질문**: 방글라어 형태론적 특성을 활용하면 방글라 문학의 자동 장르 분류 성능을 개선할 수 있는가?

**방법론**:
- 3단계 특성 공학(A0→A1→A2): 표준 TF-IDF + 어휘 특성 + 형태구문론적 패턴 결합
- 138권의 벵갈리 서적(7개 장르) 데이터셋에서 SVM, MNB, MLP 비교
- BNLP POS 태깅으로 12개 형태론적 특성 추출

**주요 결과**:
- SVM이 최고 정확도 87.38%, MNB가 최고 매크로 F1(85.2%)
- 형태론적 특성이 데이터 희소성에 덜 민감해 클래스 불균형 문제 완화
- Yule's K 및 형용사 빈도가 핵심 판별 요소로 확인

**저자**: Afsarul Amin Bhuiyan; Ahmed Shafi Arnob; Tamanna Haque Nipa; Rahad Hussain; A. B. M. Alim Al Islam
**출처**: , Vol.None, pp.53-58
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.1145/3777555.3777576

## 초록 (원문)

Automatic classification of the Bangla genre remains rigorous due to the complexity of Bangla morphology and the limited computational resources. We propose a three-stage feature engineering approach (A0 -> A1 -> A2) that combines standard TF-IDF with lexical features and morphosyntactic patterns for Bangla automated genre classification. We evaluate our approach using three machine learning algorithms: Support Vector Machine (SVM), Multinomial Naive Bayes (MNB), and Multi-Layer Perceptron (MLP), using 138 complete Bengali books in seven genres. BNLP POS tagging with 12 morphological features, which can capture tense and honorific markers, is utilised as a morphosyntactic pipeline. Evaluation of the algorithm shows that SVM achieves the highest accuracy (87.38%), while MNB provides the best macro-F1 (85.2%), and minority class detection (5.23%) is improved significantly. Yule’s K (F = 17.0) and the frequency of adjectives (F = 33.4) are identified as key discriminators. We demonstrate that morphological features, being less sensitive to data sparsity, offer a solution to the class imbalance problem in multilingual genre classification.

## 키워드

Bengali, Support vector machine, Feature (linguistics), Class (philosophy), Computational linguistics, Naive Bayes classifier, Pattern recognition (psychology)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


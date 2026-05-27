---
title: "Leveraging TF-IDF and Random Forest to Uncover Genre Patterns in Google Books Metadata"
authors: ['Nadya Awalia Putri']
year: 2025
venue: "International Journal for Applied Information Management"
tags: ['Authorship Attribution and Profiling', 'Text Readability and Simplification', 'Topic Modeling']
source: raw/applied/applied_2025_Leveraging_TFIDF_and_Rand_ijaim_v5i4_112.md
---

# Leveraging TF-IDF and Random Forest to Uncover Genre Patterns in Google Books Metadata

**제목(한글)**: Google Books 메타데이터에서 장르 패턴을 발굴하기 위한 TF-IDF와 랜덤 포레스트 활용

## 한국어 요약

**연구질문**: TF-IDF와 랜덤 포레스트 분류기를 결합하면 책 설명문을 기반으로 장르를 자동 분류할 수 있는가?

**방법론**:
- Google Books 데이터셋의 책 설명문을 TF-IDF로 수치 특징 변환
- 랜덤 포레스트 분류기로 6개 장르(소설, 문학 비평, 교육, 사회과학, 전기, 미분류) 분류
- 5겹 교차 검증(5-fold cross-validation)으로 성능 평가

**주요 결과**:
- 평균 교차 검증 정확도 64.22%, 최종 테스트 정확도 62.71%
- '소설'과 '미분류' 장르에서 높은 재현율(recall) 달성
- 클래스 불균형으로 인해 '사회과학', '전기' 등 소수 장르 분류 성능 저조

**저자**: Nadya Awalia Putri
**출처**: International Journal for Applied Information Management, Vol.5, pp.168-178
**발행일**: 2025-12-01
**DOI**: https://doi.org/10.47738/ijaim.v5i4.112

## 초록 (원문)

This paper presents a machine learning-based approach for classifying books into genres using their descriptions. We employed a Random Forest classifier combined with Term Frequency-Inverse Document Frequency (TF-IDF) to convert text descriptions into numerical features, enabling the classification of books into six genres: Fiction, Literary Criticism, Education, Social Science, Biography &amp; Autobiography, and Unknown Genre. The model was trained and evaluated on a dataset sourced from Google Books, which was preprocessed to remove missing data and clean the text descriptions by eliminating punctuation, numbers, and stopwords. We performed 5-fold cross-validation to assess the model's performance, which resulted in an average cross-validation accuracy of 64.22%. The final model achieved an accuracy of 62.71% on the test set, with the highest recall observed in the "Fiction" genre. The results indicated that the Random Forest classifier was particularly effective in classifying well-represented genres like "Fiction" and "Unknown Genre." However, genres with fewer samples, such as "Social Science" and "Biography &amp; Autobiography," showed poor performance, highlighting the challenges posed by class imbalance and data sparsity. A confusion matrix and classification report revealed these discrepancies, with certain genres being misclassified more often than others. This research demonstrates the feasibility of using machine learning for automated book genre classification, offering significant potential for enhancing book recommendation systems and improving user experience. Despite its promising results, the study's limitations, including data sparsity and genre imbalance, suggest that further work is needed to refine the model. Future research could explore the use of deep learning techniques and the expansion of the dataset to address these issues and improve genre classification accuracy. The potential for automated genre classification in real-world applications, such as book categorization and personalized recommendations, presents an exciting direction for the book industry.

## 키워드

Random forest, Metadata, Classifier (UML), Confusion matrix, Confusion, Precision and recall, Training set

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


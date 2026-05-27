---
title: "Multilingual depression screening via social media: comparative analysis of machine learning models on English and Arabic text"
authors: ['Abdelmoniem Abdelmoniem Helmy']
year: 2026
venue: "Journal of Electrical Systems and Information Technology"
tags: ['Mental Health via Writing', 'Digital Mental Health Interventions', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Multilingual_depression_s_s43067_025_00294_x.md
---

# Multilingual depression screening via social media: comparative analysis of machine learning models on English and Arabic text
**제목(한글)**: 소셜 미디어를 통한 다국어 우울증 스크리닝: 영어 및 아랍어 텍스트에 대한 머신러닝 모델 비교 분석

**저자**: Abdelmoniem Abdelmoniem Helmy
**출처**: Journal of Electrical Systems and Information Technology, Vol.13
**발행일**: 2026-04-03
**DOI**: https://doi.org/10.1186/s43067-025-00294-x

## 한국어 요약

**연구질문**: 저자원 언어인 아랍어와 영어 소셜 미디어(트위터) 데이터를 활용해 우울증 징후를 조기 판별하기 위한 텍스트 전처리 방법 및 최적 머신러닝 분류 알고리즘은 무엇인가?

**방법론**:
- 15,000건의 아랍어 트윗과 99,590건의 영어 트윗으로 구성된 균형 데이터셋 구축
- 부정어 처리, 강조어 정규화 및 카이제곱(Chi-Square) 기반 피처 선택 기법을 TF-IDF 표상 기법과 융합
- SMOTE 불균형 보정 하에 Random Forest, Linear SVM, RBF-SVM 비교 실험 수행

**주요 결과**:
- RBF-SVM + TF-IDF 융합 모델이 가장 정밀하게 우울 징후를 판독하여 아랍어 F1=98%(AUC=0.996), 영어 F1=94.2%의 탁월한 예측 성과를 보임
- 철저한 전처리 가이드라인과 전문가 검수 라벨이 결합된 기존 기계학습 모델이 무거운 딥러닝 아키텍처보다도 우울증 검출에 비용 효율적이고 강력할 수 있음을 검증함


## 초록 (원문)

Depression is a leading cause of disability worldwide, yet many individuals remain undiagnosed due to stigma, limited access to care, or lack of awareness. The growing use of social media provides a new opportunity for passive mental health screening through natural language processing and machine learning, particularly for low-resource languages such as Arabic that remain underrepresented in the literature. This study develops and evaluates multilingual machine learning models for detecting depression in social media text, using two balanced datasets: an Arabic corpus of 15,000 tweets and an English corpus of 99,590 tweets. The preprocessing pipeline incorporates normalization, negation and intensifier handling, and Chi-Square-based feature selection, with feature representation achieved through Bag-of-Words and TF-IDF. Classifiers including Random Forest, Linear SVM, and RBF-SVM were tested with SMOTE applied to address class imbalance. Results show that the RBF-SVM with TF-IDF consistently outperformed other models, achieving an F1-score of 98% and AUC of 0.996 on Arabic tweets, and an F1-score of 94.2% and AUC of 0.987 on English tweets. These outcomes highlight the impact of high-quality preprocessing, linguistic augmentation, and expert-verified annotations in improving classification performance, particularly for Arabic data. The findings demonstrate that optimized traditional machine learning models can surpass more complex deep learning methods for depression detection, and contribute benchmark datasets and practical methodologies for advancing cross-lingual mental health informatics.

## 키워드

Feature (linguistics), Preprocessor, Mental health, Pipeline (software), Class (philosophy), Social media, Representation (politics), Benchmark (surveying)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모


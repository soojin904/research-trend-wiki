---
title: "X Sentiment Analysis on Indonesia’s New Capital (IKN) Using TF-IDF+SVM and IndoBERT, and Its Policy-Monitoring Implications"
authors: ['Muhammad Riansyahputra', 'Abdul Aziz', 'Agung Purwanto']
year: 2026
venue: "ICoBITS"
tags: ['Sentiment Analysis and Opinion Mining', 'Data Mining and Machine Learning Applications', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_X_Sentiment_Analysis_on_I_icobits_v1_106.md
---

# X Sentiment Analysis on Indonesia’s New Capital (IKN) Using TF-IDF+SVM and IndoBERT, and Its Policy-Monitoring Implications
**제목(한글)**: TF-IDF+SVM 및 IndoBERT를 활용한 인도네시아 신수도(IKN) 관련 X 감성 분석과 정책 모니터링 시사점

**저자**: Muhammad Riansyahputra; Abdul Aziz; Agung Purwanto
**출처**: ICoBITS, Vol.1, pp.638-651
**발행일**: 2026-01-19
**DOI**: https://doi.org/10.32664/icobits.v1.106

## 한국어 요약

**연구질문**: 인도네시아 신수도(IKN) 이전 정책에 대한 X(구 트위터) 상의 대중 여론을 분류하고 정책 위험을 감지하기 위해, 통계적 하이브리드 모델(TF-IDF+SVM)과 사전학습된 언어 모델(IndoBERT)의 성능을 어떻게 최적화하여 비교할 수 있는가?

**방법론**:
- 인도네시아어로 작성된 신수도 관련 X 데이터 수집 및 전처리(유니코드 정규화, 속어 변환, 형태소 분석 등)
- TF-IDF + 선형 SVM 조합(가벼운 베이스라인)과 인도네시아어 특화 트랜스포머인 IndoBERT 적용 및 불균형 데이터셋에 대응하기 위한 매크로 F1, 부정 클래스 재현율(Recall) 중심의 성능 측정

**주요 결과**:
- TF-IDF+SVM은 정확도 89.08%, 매크로 F1 87.09%를 기록하였으며, IndoBERT는 정확도 94.88%, 매크로 F1 93.89%, 부정 클래스 재현율 92.0%로 최고 성능을 달성
- 높은 재현율을 확보함으로써 소셜 리스닝 대시보드를 통한 환경 및 공공 거버넌스 분야의 위기 경보 모니터링 가치를 검증함


## 초록 (원문)

This study investigates public perceptions of relocating Indonesia’s national capital to Ibu Kota Nusantara (IKN) through sentiment analysis of Indonesian-language X data, with two target classes: positive and negative. We compare two complementary modeling routes to balance semantic capacity and operational reliability. The lexical route pairs TF-IDF with a linear Support Vector Machine (SVM), providing a lightweight, stable, and reproducible baseline. The contextual route employs IndoBERT, a transformer model tailored to Indonesian, designed to capture implicit meaning and long-range dependencies within sentences. Preprocessing follows contemporary Indonesian NLP practice Unicode normalization, lowercasing, removal of URLs, mentions, and hashtags, normalization of slang into standard forms, removal of numerals and stopwords, and compression of elongated characters to stabilize lexical signal and reduce tokenization artifacts. Because the test data are imbalanced (the positive class is larger), evaluation emphasizes macro-F1 and negative-class recall so that overall accuracy is not inflated by the majority class. Final runs show TF-IDF+SVM achieves Accuracy 0.8908 and macro-F1 0.8709 with negative-recall 0.839; IndoBERT achieves Accuracy 0.9488 and macro-F1 0.9389 with negative-recall 0.920. The recall gain reduces undetected criticism and strengthens the practical value of a social-listening dashboard for governance and environmental issues where early warning is crucial.

## 키워드

Lexical analysis, Sentiment analysis, Normalization (sociology), Preprocessor, Recall, Precision and recall, Lexical item, Categorical variable

## 위키 연관

- [[pages/concepts/personal_network|퍼스널 네트워크]]

## 메모


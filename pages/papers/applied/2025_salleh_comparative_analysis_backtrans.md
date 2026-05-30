---
title: "COMPARATIVE ANALYSIS OF BACK-TRANSLATION MODELS FOR NORMALIZATION MOBILE APP USER REVIEWS"
authors: ['Amran Salleh', 'Mohd Hafeez Osman', 'Sa’adah Hassan', 'Mar Yah Said']
year: 2025
venue: "International Journal of Computer Systems & Software Engineering"
tags: ['Sentiment Analysis and Opinion Mining', 'Spam and Phishing Detection', 'Authorship Attribution and Profiling']
source: raw/applied/applied_2025_COMPARATIVE_ANALYSIS_OF_B_ijsecs_11_2_2025_10_0142.md
---

# COMPARATIVE ANALYSIS OF BACK-TRANSLATION MODELS FOR NORMALIZATION MOBILE APP USER REVIEWS

**제목(한글)**: 모바일 앱 사용자 리뷰 정규화를 위한 역번역 모델 비교 분석

## 한국어 요약

**연구질문**: 역번역(Back-Translation, BT)이 비정형(informal) 리뷰의 의미를 보존하면서 정규화(normalization)할 수 있는지, 그리고 어떤 모델(Google Translate vs Facebook M2M100_418M)이 더 나은 의미 보존, 문법적 품질 및 어휘적 일치도를 제공하는지 평가한다.

**방법론**:
- 말레이시아 정부 앱 3종에서 Google Play 리뷰 323개(총 667문장)를 수집하였다.
- 수집된 텍스트는 정제 및 구어체 확장 과정을 거쳐 말레이어를 중간 언어로 활용한 역번역(BT)을 적용하였다.
- 평가는 의미 유사성(Semantic Similarity, Sentence-BERT), 문법 오류 수(Grammar Error Count, LanguageTool), BLEU (NLTK), Perplexity (GPT-2)의 네 가지 지표를 사용하였다.
- 모델 간 차이는 대응표본 t-검정(paired t-tests) 및 Wilcoxon 부호순위 검정(Wilcoxon signed- rank tests)으로 분석하였고, 쌍별 산점도(paired scatterplots)로 분포 패턴을 시각화하였다.

**주요 결과**:
- Google Translate가 의미 유사성 (t(322)=5.38, p<.001), 문법 오류 (t(322)=3.66, p<.001), BLEU (t(322)=2.99, p=.003) 지표에서 Facebook M2M100_418M보다 통계적으로 유의하게 우수했으며, 효과 크기는 작거나 중간 수준이었다.
- Perplexity (문장 수준의 유창성)에서는 모델 간 유의미한 차이가 없었다.
- 시각화 결과, Google Translate는 더 안정적인 성능을 보였고 극단적인 이상치(extreme outliers)가 적었다.
- 역번역(BT)은 노이즈가 많은 리뷰를 정규화하는 데 실용적인 단계임을 확인하였다.
- 본 연구에서 사용된 영어-말레이어 파이프라인에서는 Google Translate가 더 신뢰할 수 있는 의미 보존과 문법적 품질을 제공하며, 유창성 측면에서는 두 시스템이 유사하다.
- 본 연구 결과의 일반화 가능성(Generalizability)은 상대적으로 적은 표본 크기(323개 리뷰, 667문장)로 인해 제한되며, 향후 대규모 데이터셋을 통한 검증 및 두 모델의 강점을 결합한 하이브리드 전략 탐색이 필요하다.

**저자**: Amran Salleh; Mohd Hafeez Osman; Sa’adah Hassan; Mar Yah Said
**출처**: International Journal of Computer Systems & Software Engineering, Vol.11, pp.124-136
**발행일**: 2025-12-18
**DOI**: https://doi.org/10.15282/ijsecs.11.2.2025.10.0142

## 초록 (원문)

The increase of mobile apps has led to an exponential growth of user-generated reviews, which are often noisy, informal, and linguistically diverse, thereby posing significant challenges for automated analysis in requirements engineering. This study evaluates whether back-translation (BT) can normalize informal reviews while preserving meaning, and which model (Google Translate vs Facebook M2M100_418M) offers better semantic preservation, grammatical quality, and lexical alignment. We collected 323 Google Play reviews (667 sentences) from three Malaysian government apps. Texts were cleaned, expanded for colloquial forms, and then BT was applied using Malay as an intermediate language. Evaluation used four metrics which are semantic similarity (Sentence-BERT), grammar error count (LanguageTool), BLEU (NLTK), and perplexity (GPT-2). Models differences were tested with paired t-tests and Wilcoxon signed- rank tests, while paired scatterplots showed distributional patterns. Google was significantly better on semantic similarity (t(322)=5.38, p&lt;.001), grammar errors (t(322)=3.66, p&lt;.001), and BLEU (t(322)=2.99, p=.003); effect sizes were small to moderate. Perplexity differences were not significant, indicating comparable sentence-level fluency. Visualizations confirmed Google’s steadier performance with fewer extreme outliers. BT is a practical normalization step for noisy reviews. For the English–Malay pipeline studied here, Google provides more reliable semantic preservation and grammatical quality, while both systems are similar in fluency. However, the generalizability of these results are constrained by the relatively modest sample size (323 reviews, 667 sentences), and future work should validate results on large datasets and explore hybrid strategies combining strengths of both models.

## 키워드

Perplexity, Normalization (sociology), Generalizability theory, Semantic similarity, Grammar, Latent semantic analysis, Bridging (networking), Vocabulary

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모


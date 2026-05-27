---
title: "전통 ML / 앙상블 학습 (Traditional Machine Learning)"
tags: [machine-learning, svm, random-forest, xgboost, ensemble, link-prediction]
netminer_support: "✅ 지원"
---

# 전통 ML / 앙상블 학습 (Traditional Machine Learning)

딥러닝 이전부터 사용해온 지도·비지도 학습 방법론의 총칭. SNA 학술지에서 네트워크 데이터에 적용되며, 응용 분야에서는 텍스트·구조화 데이터 분류·예측에 광범위하게 사용된다. LLM·Transformer 시대에도 앙상블 방법(XGBoost·RF)은 표 형식 데이터와 해석 가능성이 요구되는 분야에서 경쟁력을 유지한다.

---

## 주요 알고리즘

### 분류 / 회귀

| 알고리즘 | 특징 | 주요 응용 |
|---------|------|----------|
| **SVM (Support Vector Machine)** | 고차원 소규모 데이터 강점, 커널 트릭 | 텍스트 분류, 스팸 탐지 |
| **Random Forest** | 배깅 앙상블, 과적합 저항, 변수 중요도 | 분류·회귀 범용 |
| **XGBoost / LightGBM** | 부스팅 앙상블, 구조화 데이터 최강 | ESG 예측, 금융, 의료 |
| **Naive Bayes** | 확률 기반, 빠른 학습 | 스팸 필터, 감성 분류 초기 |
| **Logistic Regression** | 해석 가능, 이진 분류 기본 | 의료 진단, 정치 텍스트 |
| **K-Nearest Neighbors** | 비모수, 유사도 기반 | 추천, 이상 탐지 |

### 비지도 학습

| 알고리즘 | 특징 | 응용 |
|---------|------|------|
| **K-Means** | 거리 기반 군집화 | 문서 군집, 고객 세분화 |
| **DBSCAN** | 밀도 기반, 이상치 탐지 | 소셜 네트워크 군집 |
| **PCA** | 차원 축소, 노이즈 제거 | 임베딩 압축, 시각화 전처리 |

---

## SNA 문맥에서의 ML (SNA 학술지 기반)

SNA 학술지 2020–2026에서 전통 ML은 주로 **링크 예측**, **노드 속성 분류**에 활용된다.

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2024_lai_predicting_network_members_fro\|Lai 외 (2024)]] | 부분 접촉 기록으로 개인 네트워크 구성원 예측 — ML 앙상블 | 부분 기록만으로 네트워크 구성원 예측 가능성 시연 |
| [[pages/papers/sna/2023_tomlinson_graphbased_methods_for_discret\|Tomlinson & Benson (2023)]] | 이산 선택 모형 + 그래프 구조 통합 | 소셜 네트워크 구조 통합이 다항 로짓 예측 개선 |

---

## 응용 분야 사용 패턴 (2026, 379편 기반)

| 방법 | 편수 | 주요 맥락 |
|------|------|----------|
| **XGBoost / Random Forest** | ~30 | ESG 예측, 금융 리스크, 의료 진단 |
| **SVM** | ~20 | 텍스트 분류, 감성 보조 분류기 |
| **Logistic Regression** | ~12 | 이진 분류, 기준선(baseline) 모델 |
| **Naive Bayes** | ~10 | 스팸, 언어 탐지, 빠른 프로토타이핑 |
| **K-Means** | ~8 | 문서 군집화, 사용자 세그먼트 |
| **SHAP / LIME (XAI)** | ~19 | ML 결과 해석, 의료 AI 설명 |

> **트렌드**: 전통 ML이 독립 방법론으로 사용되는 빈도는 감소했지만, **XAI(설명 가능성)** 요구로 인해 SHAP·LIME과 결합한 "해석 가능한 ML" 수요는 유지. Transformer 임베딩의 특징 벡터 + 전통 분류기 조합도 다수.

---

## NetMiner 지원 현황

✅ **지원** — NetMiner는 분류(SVM, Decision Tree, RF 등), 군집화(K-Means 등), 회귀 기능을 내장 지원.

**활용 포인트**:
- 네트워크 구조 지표(중심성, 군집 계수 등)를 특징으로 추출 → ML 분류기에 입력
- 텍스트 마이닝 결과 + 네트워크 지표 결합 특징 행렬 생성 가능
- 분류 결과를 노드 속성으로 저장 후 네트워크 시각화로 패턴 파악

---

## 관련 페이지

- [[pages/methods/gnn|GNN]] — 딥러닝 기반 그래프 학습 (전통 ML의 확장)
- [[pages/methods/text_classification|텍스트 분류]] — ML 분류기의 NLP 응용
- [[pages/methods/sentiment_analysis|감성 분석]] — ML 기반 감성 극성 분류
- [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026)]]
- [[pages/insights/sna_method_frequency|SNA 방법론 빈도 (2021–2026)]]

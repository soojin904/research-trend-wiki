---
title: "A Multi-Document NLP Framework for Strict Management Communication Index for Quant Investing"
authors: ['SONALI V. BHARAD', 'Sapana S. Barphe', 'IRAM RAFIQ AHMED  JHETAM', 'Arun R. Babhulgaonkar']
year: 2026
venue: "International Journal of Novel Research and Development"
tags: ['Stock Market Forecasting Methods', 'Auditing, Earnings Management, Governance', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_A_MultiDocument_NLP_Frame_ijnrd_v11i3_313394.md
---

# A Multi-Document NLP Framework for Strict Management Communication Index for Quant Investing
**제목(한글)**: 퀀트 투자를 위한 엄격한 경영진 커뮤니케이션 지수 구축을 위한 다중 문서 NLP 프레임워크

**저자**: SONALI V. BHARAD; Sapana S. Barphe; IRAM RAFIQ AHMED  JHETAM; Arun R. Babhulgaonkar
**출처**: International Journal of Novel Research and Development, Vol.11
**발행일**: 2026-03-01
**DOI**: https://doi.org/10.56975/ijnrd.v11i3.313394

## 한국어 요약

**연구질문**: 기존의 단일 텍스트 감성 분석이 기업 공시의 구조적 낙관 편향으로 인해 정보 변별력을 잃는 문제를 해결하고, 퀀트 포트폴리오 최적화에 쓸 수 있는 객관적 정량 지수를 어떻게 설계할 수 있는가?

**방법론**:
- 연례 보고서, 실적 발표 녹취록, 투자자 프레젠테이션 등 다중 소스 문서에서 PyMuPDF로 텍스트를 추출하고 FinBERT로 감성 평가 수행
- (i) 낙관적 어조를 페널티 처리하는 엄격 감성 지수, (ii) TF-IDF 기반 단어 정규화, (iii) 가독성 지표(Gunning Fog) 기반 페널티, (iv) 불확실성 증폭 요인을 융합한 Strict MCI 공식 설계 및 BSE Sensex 30 대기업에 적용

**주요 결과**:
- Strict MCI 모델이 표준 감성 분석 대비 기업 간 격차를 넓고 뚜렷하게 산출하여 기업 성과의 예측 변별력을 크게 높임을 확인
- 퀀트 투자의 신뢰성 높은 비재무 소프트 팩터 도입 가능성을 정립


## 초록 (원문)

Management communication significantly influences investor perceptions, information asymmetry, and market behavior. Traditional sentiment-based approaches applied to corporate disclosures often overestimate positivity and fail to discriminate across firms due to optimistic language biases and limited sensitivity. This study proposes a Strict Management Communication Index (MCI), an advanced NLP-driven scoring model designed to quantify managerial tone, clarity, uncertainty, and sentiment consistency across multiple corporate documents. The framework extracts text from annual reports, earnings call transcripts, and investor presentations using high accuracy PyMuPDF extraction and evaluates sentiment using the domain specific FinBERT model. Key innovations include (i) a Strict Sentiment Score penalizing neutral-heavy communication, (ii) TF-IDF inspired normalization of optimism, risk, and uncertainty, (iii) a readability penalty based on the Gunning Fog Index, and (iv) uncertainty amplification to penalize evasive communication. We evaluate the model on BSE Sensex 30 companies and show that the Strict MCI produces a significantly wider and more realistic distribution compared to conventional sentiment scores. The MCI can act as a forward-looking soft-information factor in equity selection and portfolio optimization.

## 키워드

Readability, Index (typography), Normalization (sociology), Equity (law), Consistency (knowledge bases), Earnings, Plain English, Project portfolio management

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


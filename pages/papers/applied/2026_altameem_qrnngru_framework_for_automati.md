---
title: "QRNN-GRU framework for automatic argument and annotation extraction in medical drug reviews"
authors: ['Eman Altameem', 'Mohammed Alnuem', 'Sarah Ahmed A. Albassam']
year: 2026
venue: "Scientific Reports"
tags: ['Biomedical Text Mining and Ontologies', 'Topic Modeling', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_QRNNGRU_framework_for_aut_s41598_026_41379_5.md
---

# QRNN-GRU framework for automatic argument and annotation extraction in medical drug reviews
**제목(한글)**: 의약품 리뷰 내 자동 논증 및 주석 추출을 위한 QRNN-GRU 프레임워크

**저자**: Eman Altameem; Mohammed Alnuem; Sarah Ahmed A. Albassam
**출처**: Scientific Reports, Vol.16
**발행일**: 2026-03-15
**DOI**: https://doi.org/10.1038/s41598-026-41379-5

## 한국어 요약

**연구질문**: 구어체 노이즈가 많고 도메인 고유 용어가 풍부하며 주관적인 의약품 리뷰 텍스트 데이터에서, 연산 비용을 최소화하면서 환자들의 주관적인 효능 및 부작용 주장을 정밀하게 추출하는 하이브리드 순차 신경망 모델은 무엇인가?

**방법론**:
- 지역적 시계열 패턴을 빠르게 포착하는 QRNN 레이어와 장기 문맥 의존성을 인코딩하는 GRU 레이어를 직렬 결합한 아키텍처 설계
- 하이퍼파라미터 안정성을 위해 반딧불이 최적화 메커니즘을 적용하고, 의약품 리뷰 데이터 및 Abstract RCT 임상 벤치마크 데이터셋에서 다중 검증

**주요 결과**:
- 제안된 QRNN-GRU 모델이 의약품 리뷰 데이터에서 F1-스코어 89.20%, 정확도 91.47%를 나타내어 연산 효율성과 긴 문장 파싱 능력을 고루 갖춘 우수한 모델임을 증명
- 임상 정보 추출 태깅 모델로도 충분히 높은 전이 학습 가능성을 시사


## 초록 (원문)

Argument annotation in medical drug reviews is a challenging task due to noisy user-generated content, domain-specific terminology, and subjective expressions of medication efficacy and adverse effects. While argument mining has been explored in this domain, the diversity of modeling architectures investigated remains narrower compared to more extensively studied NLP tasks. In this study, we investigate a sequential QRNN–GRU framework for identifying argumentative components in the medical datasets, aiming to explore a hybrid architecture that balances effective modeling of argumentative structures with computational efficiency for this domain. The proposed model employs QRNN layers to efficiently capture local temporal patterns, followed by GRU layers to model longer-range sequential dependencies. Firefly Optimization is utilized for hyperparameter tuning to improve training stability and convergence behavior. Experimental results on drug review dataset show that the proposed approach achieves an F1-score of 89.20% and an accuracy of 91.47%, outperforming selected baseline models under the evaluated setting. To further examine the generalizability, the model additionally evaluated on Abstract RCT benchmark dataset, where it achieves competitive comparative performance against established state-of-the-art methods. Although the model demonstrates consistent performance across two benchmark datasets, the analysis is limited to medical texts and does not include cross-domain evaluation.

## 키워드

Benchmark (surveying), Argumentative, Annotation, Argument (complex analysis), Task (project management), Baseline (sea), Hyperparameter, Convergence (economics)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


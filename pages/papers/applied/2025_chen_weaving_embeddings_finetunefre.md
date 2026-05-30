---
title: "Weaving Embeddings: A Fine-Tune-Free LLM Fusion Framework for Efficient Health and Safety Text Analysis"
authors: ['Jian Chen', 'Jinbao Tian', 'Wangdong Xu', 'Wenbo Xia', 'Li Zhou']
year: 2025
venue: ""
tags: ['Biomedical Text Mining and Ontologies', 'Topic Modeling', 'Machine Learning in Healthcare']
source: raw/applied/applied_2025_Weaving_Embeddings_A_Fine_bibm66473_2025_11356911.md
---

# Weaving Embeddings: A Fine-Tune-Free LLM Fusion Framework for Efficient Health and Safety Text Analysis

**제목(한글)**: 임베딩 융합: 보건·안전 텍스트 분석을 위한 파인튜닝 불필요 LLM 융합 프레임워크

## 한국어 요약

**연구질문**: 대형 언어 모델(LLM)의 파인튜닝 없이도 복수 LLM의 임베딩을 융합하여 직업 안전 부상 보고서를 효율적으로 분류할 수 있는가? 계산 비용을 절감하면서도 파인튜닝된 모델과 동등하거나 더 나은 성능을 달성할 수 있는가?

**방법론**:
- 주-보조(Primary-Auxiliary) 아키텍처 기반의 파인튜닝 불필요 경량 LLM 융합 프레임워크 제안
- 복수의 기성(Off-the-shelf) LLM에서 다양한 의미 임베딩(Semantic Embeddings) 추출
- 공동 발생 메커니즘(Co-occurrence Mechanism)으로 임베딩 간 2차 상호작용 모델링
- OSHA 직업 부상 보고서 공개 벤치마크로 평가

**주요 결과**:
- 가중 F1 점수 68.20%로 동일 규모의 파인튜닝 전용 LLM 대비 우수한 성능 달성
- 파인튜닝 모델 대비 계산 효율성 4.4배 향상
- 임상 기록·공중보건 보고서 등 비정형 의료 텍스트 분석에 실용적인 대안 제시
- 코드 공개로 재현 가능성 확보

**저자**: Jian Chen; Jinbao Tian; Wangdong Xu; Wenbo Xia; Li Zhou
**출처**: , Vol.None, pp.6676-6683
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.1109/bibm66473.2025.11356911

## 초록 (원문)

The analysis of unstructured text, such as clinical notes and public health reports, is a fundamental challenge in biomedical and health informatics (BHI). Occupational health informatics, a vital sub-domain of BHI, relies on analyzing injury narratives to prevent workplace accidents, which constitute a significant public health burden. While Large Language Models (LLMs) offer a promising direction, their practical deployment in health-related applications is often hindered by the prohibitive computational costs of fine-tuning and the unreliability of prompt-based methods. To address these limitations, we propose an efficient, fine-tune-free, and lightweight fusion framework for robust text classification. Our framework introduces a primary-auxiliary architecture that harnesses diverse semantic embeddings from multiple off-the-shelf LLMs. By modeling the second-order interactions between these embeddings via a cooccurrence mechanism, our approach generates a powerful, composite feature representation for a simple downstream classifier. We empirically validate our framework on a public benchmark of occupational injury reports from the U.S. Occupational Safety and Health Administration (OSHA), where the framework achieves a state-of-the-art weighted-F1 score of <tex xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">$\mathbf{6 8. 2 0 \%}$</tex>. Notably, our framework outperforms a purpose-built, fine-tuned LLM of the same scale while demonstrating a 4.4-fold improvement in computational efficiency. The code is publicly available at: https://github.com/nxcc-lab/LLM-Fusion-Framework.

## 키워드

Benchmark (surveying), Health informatics, Weaving, Benchmarking, eHealth, Software deployment, Representation (politics), Feature (linguistics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모


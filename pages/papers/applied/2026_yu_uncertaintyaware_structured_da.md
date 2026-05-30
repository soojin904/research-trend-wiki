---
title: "Uncertainty-Aware Structured Data Extraction from Full CMR Reports via Distilled LLMs"
authors: ['Yi Yu', 'Parker Martin', 'Zhenyu Bu', 'Yixuan Liu', 'Yi-Yu Zheng', 'Orlando Simonetti', 'Yuchi Han', 'Yuan Xue']
year: 2026
venue: "ArXiv.org"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Biomedical Text Mining and Ontologies']
source: raw/applied/applied_2026_UncertaintyAware_Structur_nodoi.md
---

# Uncertainty-Aware Structured Data Extraction from Full CMR Reports via Distilled LLMs

**제목(한글)**: 불확실성 인식 기반 증류된 LLM을 통한 전체 CMR 보고서로부터의 정형 데이터 추출

## 한국어 요약

**연구질문**: 자유 텍스트 심장 자기 공명(CMR) 보고서를 감사 가능한 정형 데이터로 변환하는 병목 현상을 해결하고, 품질 관리를 위해 필드별 신뢰도(Confidence)를 할당하는 효과적인 방법은 무엇인가?

**방법론**:
- CMR-EXTR 프레임워크: 자유 텍스트 CMR 보고서를 정형 데이터로 변환하고 필드별 신뢰도를 할당
- 교사-학생 증류 파이프라인(Teacher-student distillation pipeline): 오프라인 추론(offline inference) 가능 및 수동 주석(manual annotation) 최소화
- 불확실성 통합 원칙: 분포 타당성(distribution plausibility), 샘플링 안정성(sampling stability), 필드 간 일관성(cross-field consistency)을 결합하여 인간 검토의 우선순위 지정

**주요 결과**:
- CMR-EXTR은 변수 수준에서 99.65%의 정확도 달성
- 신뢰할 수 있는 데이터 추출 및 정보성 신뢰도 점수(informative confidence scores) 제공 입증
- 통합된 신뢰도 추정(confidence estimation) 기능을 갖춘 최초의 CMR 특정 추출 시스템

**저자**: Yi Yu; Parker Martin; Zhenyu Bu; Yixuan Liu; Yi-Yu Zheng; Orlando Simonetti; Yuchi Han; Yuan Xue
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-05-08
**DOI**: 

## 초록 (원문)

Converting free-text cardiac magnetic resonance (CMR) reports into auditable structured data remains a bottleneck for cohort assembly, longitudinal curation, and clinical decision support. We present CMR-EXTR, a lightweight framework that converts free-text CMR reports into structured data and assigns per-field confidence for quality control. A teacher-student distillation pipeline enables fully offline inference while limiting manual annotation. Uncertainty integrates three complementary principles -- distribution plausibility, sampling stability, and cross-field consistency -- to triage human review. Experiments show that CMR-EXTR achieves 99.65% variable-level accuracy, demonstrating both reliable extraction and informative confidence scores. To our knowledge, this is the first CMR-specific extraction system with integrated confidence estimation. The code is available at https://github.com/yuyi1005/CMR-EXTR.

## 키워드

Pipeline (software), Consistency (knowledge bases), Confidence interval, Data extraction, Data quality, Sampling (signal processing), Data consistency, Quality (philosophy)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


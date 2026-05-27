---
title: "CAST: Achieving Stable LLM-based Text Analysis for Data Analytics"
authors: ['Jinxiang Xie', 'Zihao Li', 'Wei He', 'Rui Ding', 'Shi Han', 'Dongmei Zhang']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Topic Modeling', 'Computational and Text Analysis Methods', 'Natural Language Processing Techniques']
source: raw/applied/applied_2026_CAST_Achieving_Stable_LLM_nodoi.md
---

# CAST: Achieving Stable LLM-based Text Analysis for Data Analytics
**제목(한글)**: CAST: 데이터 분석을 위한 안정적 LLM 기반 텍스트 분석 달성

## 한국어 요약

**연구질문**: LLM을 이용한 표 형식 데이터의 텍스트 요약(summarization) 및 태깅(tagging) 작업에서 데이터 분석이 요구하는 높은 출력 안정성을 어떻게 확보할 수 있는가?

**방법론**:
- 절차적 추론 전환을 강제하는 알고리즘적 프롬프팅(Algorithmic Prompting)과 최종 생성 전 중간 확약을 명시하는 발화 전 사고(Thinking-before-Speaking) 기법 결합
- 출력 안정성 측정을 위한 요약 안정성 지표(CAST-S)와 태깅 안정성 지표(CAST-T) 제안 및 인간 판단과의 정렬 검증
- 여러 LLM 백본 모델과 공개 벤치마크 데이터셋으로 비교 실험

**주요 결과**:
- CAST가 모든 기준선 대비 일관되게 최고 안정성을 달성하며 안정성 점수를 최대 16.2% 향상
- 출력 품질을 유지하거나 개선하면서도 안정성이 향상됨을 다수 LLM 백본에서 검증

**저자**: Jinxiang Xie; Zihao Li; Wei He; Rui Ding; Shi Han; Dongmei Zhang
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-01-26
**DOI**: 

## 초록 (원문)

Text analysis of tabular data relies on two core operations: \emph{summarization} for corpus-level theme extraction and \emph{tagging} for row-level labeling. A critical limitation of employing large language models (LLMs) for these tasks is their inability to meet the high standards of output stability demanded by data analytics. To address this challenge, we introduce \textbf{CAST} (\textbf{C}onsistency via \textbf{A}lgorithmic Prompting and \textbf{S}table \textbf{T}hinking), a framework that enhances output stability by constraining the model's latent reasoning path. CAST combines (i) Algorithmic Prompting to impose a procedural scaffold over valid reasoning transitions and (ii) Thinking-before-Speaking to enforce explicit intermediate commitments before final generation. To measure progress, we introduce \textbf{CAST-S} and \textbf{CAST-T}, stability metrics for bulleted summarization and tagging, and validate their alignment with human judgments. Experiments across publicly available benchmarks on multiple LLM backbones show that CAST consistently achieves the best stability among all baselines, improving Stability Score by up to 16.2\%, while maintaining or improving output quality.

## 키워드

Automatic summarization, Stability (learning theory), Measure (data warehouse), Analytics, Core (optical fiber), Data analysis, Key (lock), Theme (computing)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모


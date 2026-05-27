---
title: "Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory"
authors: ['Songwei Dong', 'Zihan Chen', 'Chengshuai Shi', 'Peng Wang', 'Jundong Li', 'Cong Shen']
year: 2026
venue: "ArXiv.org"
tags: ['Domain Adaptation and Few-Shot Learning', 'Topic Modeling', 'Multimodal Machine Learning Applications']
source: raw/applied/applied_2026_Is_One_Score_Enough_Rethi_nodoi.md
---

# Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory
**제목(한글)**: 하나의 점수로 충분한가? 순차적으로 진화하는 LLM 메모리 평가의 재고

## 한국어 요약

**연구질문**: 순차 작업에서 LLM의 외부 메모리 시스템을 평가할 때 최종 정확도 같은 집계 지표만으로는 망각(Forgetting)이나 부정적 전이(Negative Transfer) 같은 중요한 실패 모드를 어떻게 놓치게 되며, 더 정밀한 평가 프레임워크는 무엇인가?

**방법론**:
- 연속 학습(Continual Learning)에서 영감을 받아 외부·프롬프트 매개·파라미터 미수정 메모리를 대상으로 하는 진단 평가 프레임워크 SeqMem-Eval 제안
- 온라인 유틸리티(Online Utility), 홀드아웃 일반화, 역방향 전이(Backward Transfer), 망각의 네 가지 차원을 정밀 측정

**주요 결과**:
- 높은 최종 또는 누적 정확도가 메모리 품질을 보장하지 않음을 다양한 태스크·메모리 방법 실험으로 증명
- 메모리 설계 방식에 따라 적응성과 안정성 간 서로 다른 트레이드오프가 존재하며, 표준 지표로는 이를 식별 불가함을 제시

**저자**: Songwei Dong; Zihan Chen; Chengshuai Shi; Peng Wang; Jundong Li; Cong Shen
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-05-14
**DOI**: 

## 초록 (원문)

Memory plays a central role in enabling large language models (LLMs) to operate over sequential tasks by accumulating and reusing experience over time. However, existing evaluations of LLM memory mostly rely on aggregate metrics such as final hold-out accuracy or cumulative online performance, which can obscure critical failure modes such as forgetting and negative transfer. In this paper, we introduce SeqMem-Eval, a diagnostic evaluation framework for sequentially evolving LLM memory. Drawing inspiration from continual learning, it targets a test-time setting in which memory is external, prompt-mediated, and updated without modifying model parameters. Rather than focusing only on final performance, SeqMem-Eval evaluates how memory states evolve, generalize, consolidate experience, and retain useful information during sequential inference. Specifically, it measures online utility, hold-out generalization, backward transfer, and forgetting, providing a finer-grained view of memory quality. Through extensive experiments across diverse tasks and memory methods, we show that higher final or cumulative accuracy does not necessarily imply better memory quality: many methods exhibit strong performance gains while suffering from substantial forgetting or negative transfer. Moreover, different memory designs exhibit distinct trade-offs between adaptability and stability that remain invisible under standard evaluation metrics.

## 키워드

Forgetting, Aggregate (composite), Memory model, Reuse, Stability (learning theory), Property (philosophy), Adaptability

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


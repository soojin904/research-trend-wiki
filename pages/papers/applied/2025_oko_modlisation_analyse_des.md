---
title: "Modélisation et analyse des thèmes dans un corpus documentaire : pour une meilleure exploration et recommandation"
authors: ['Christian OKO']
year: 2025
venue: "HAL (Le Centre pour la Communication Scientifique Directe)"
tags: ['Text and Document Classification Technologies', 'Advanced Text Analysis Techniques', 'Topic Modeling']
source: raw/applied/applied_2025_Modlisation_et_analyse_de_nodoi.md
---

# Modélisation et analyse des thèmes dans un corpus documentaire : pour une meilleure exploration et recommandation

**제목(한글)**: 문서 코퍼스 내 주제 모델링 및 분석: 더 나은 탐색 및 추천을 위하여

## 한국어 요약

**연구질문**: 이 논문은 이질적이고, 다국어이며, 대규모 텍스트 코퍼스에서 기존 주제 모델링의 해석 가능성, 파라미터 민감도 및 문맥 표현의 한계를 어떻게 극복할 수 있는가에 대한 방법론적 도전을 탐구한다.

**방법론**:
- 확률 모델링 (Probabilistic Modeling) 및 의미론적 풍부화(Semantic Enrichment)를 통합한 두 가지 프레임워크 제안
- SemaTopic: 문맥 인식 주제 모델링(Context-aware topic modeling), 의미론적 클러스터링(Semantic Clustering), 일관성 기반 하이퍼파라미터 최적화(Coherence-driven Hyperparameter Optimization)
- ARIA: 추출 후 의미론적 정제(Post-extraction semantic refinement), LLM 기반 레이블링, 계층적 조직화, 섹션 레벨 색인화
- 과학, 도메인별, 다국어 및 단문 텍스트 데이터셋에 대한 종합적인 실험

**주요 결과**:
- SemaTopic은 20 Newsgroups 데이터셋에서 BERTopic 대비 의미론적 일관성(Semantic Coherence) 6.2% 향상 (C_v = 0.5315 vs. 0.5004)
- SemaTopic은 이질적이고 다국어 코퍼스 전반에 걸쳐 안정적인 성능 유지
- ARIA는 주제 일관성(Topic Coherence)을 0.45 수준에서 최대 0.74까지 추가적으로 향상
- 제안된 통합 프레임워크는 복잡한 텍스트 환경에서 지식 발견을 위한 일관되고 견고하며 적응 가능한 접근 방식을 제공

**저자**: Christian OKO
**출처**: HAL (Le Centre pour la Communication Scientifique Directe), Vol.None
**발행일**: 2025-12-03
**DOI**: 

## 초록 (원문)

This thesis investigates the methodological challenges of topic modeling in heterogeneous, multilingual, and large-scale textual corpora, where conventional approaches often face limitations in interpretability, parameter sensitivity, and contextual representation. To address these issues, we propose two unified and modular frameworks that integrate probabilistic modeling, semantic enrichment, diagnostic evaluation, and structural organization within a coherent pipeline.The first framework, SemaTopic, introduces a context-aware topic modeling approach that combines semantic clustering with coherence-driven hyperparameter optimization and probabilistic inference. By aligning contextual embeddings with density-based structuring prior to topic extraction, the framework enhances topic stability, semantic consistency, and interpretability across corpora of varying size, structure, and language. Experimental results demonstrate that SemaTopic achieves a relative gain of +6.2% in semantic coherence compared to BERTopic on the 20 Newsgroups dataset (C_v = 0.5315 vs. 0.5004), while maintaining stable performance across heterogeneous and multilingual corpora.The second framework, ARIA, extends the modeling process through post-extraction semantic refinement. It incorporates LLM-based labeling, guided enrichment, hierarchical organization, and section-level indexing, transforming probabilistic topic distributions into structured and navigable knowledge representations. When applied as a final refinement layer, ARIA further increases topic coherence, raising baseline values around 0.45 to levels reaching up to 0.74 after full semantic optimization. This progressive improvement reflects the cumulative effect of semantic clustering, coherence-guided tuning, and LLM-based refinement within the unified pipeline.Comprehensive experiments conducted on scientific, domain-specific, multilingual, and short-text datasets validate the consistency, robustness, and adaptability of the proposed approach. Rather than proposing an isolated algorithmic enhancement, this thesis advances topic modeling toward an integrated, semantically grounded, and operational framework for knowledge discovery in complex textual environments.

## 키워드

Probabilistic logic, Interpretability, Topic model, Coherence (philosophical gambling strategy), Semantics (computer science), Probabilistic latent semantic analysis, Process (computing), Statistical model

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모


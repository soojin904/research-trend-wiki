---
title: "Topic Modeling and Analysis in a Document Corpus : Towards Better Exploration and Recommendation"
authors: ['Amani Drissi']
year: 2025
venue: ""
tags: ['Computational and Text Analysis Methods', 'Topic Modeling', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2025_Topic_Modeling_and_Analys_nodoi.md
---

# Topic Modeling and Analysis in a Document Corpus : Towards Better Exploration and Recommendation

**제목(한글)**: 문서 코퍼스에서의 토픽 모델링 및 분석: 더 나은 탐색과 추천을 향하여

## 한국어 요약

**연구질문**: 이질적·다국어·대규모 텍스트 코퍼스에서 기존 토픽 모델링의 해석 가능성, 파라미터 민감성, 문맥적 표현 한계를 어떻게 극복할 수 있으며, 지식 발견을 위한 통합적 파이프라인을 어떻게 구축할 수 있는가?

**방법론**:
- SemaTopic 프레임워크: 의미론적 클러스터링, 일관성 기반 하이퍼파라미터 최적화, 확률적 추론을 결합한 문맥 감응형 주제 모델링
- ARIA 프레임워크: LLM 기반 자동 레이블링, 의미론적 풍부화, 계층적 구성 및 섹션 수준 색인화로 사후 추출 정제
- 과학, 전문, 다국어, 단문 코퍼스 등 다양한 데이터셋에서 실험적 검증

**주요 결과**:
- SemaTopic이 20 Newsgroups 코퍼스에서 BERTopic 대비 의미론적 일관성 +6.2% 향상(C_v: 0.5315 vs 0.5004)
- ARIA 적용 후 주제 일관성이 기준값 약 0.45에서 최대 0.74까지 단계적 향상
- 이질적·다국어 코퍼스에서도 안정적이고 해석 가능한 토픽 추출 가능성 입증
- 확률적 주제 분포를 탐색 가능한 구조화된 지식 표현으로 변환하는 통합 파이프라인 제시

**저자**: Amani Drissi
**출처**: , Vol.None
**발행일**: 2025-12-03
**DOI**: 

## 초록 (원문)

Cette thèse étudie les défis méthodologiques du topic modeling appliqué à des corpus textuels hétérogènes, multilingues et de grande échelle, pour lesquels les approches conventionnelles présentent souvent des limitations en matière d'interprétabilité, de sensibilité aux paramètres et de représentation contextuelle. Afin de répondre à ces problématiques, nous proposons deux cadres méthodologiques unifiés et modulaires intégrant modélisation probabiliste, enrichissement sémantique, évaluation diagnostique et organisation structurelle au sein d'un pipeline cohérent.Le premier cadre, SemaTopic, introduit une approche de modélisation thématique sensible au contexte, combinant clustering sémantique, optimisation des hyperparamètres guidée par la cohérence et inférence probabiliste. En alignant les embeddings contextuels avec une structuration fondée sur la densité avant l'extraction des thèmes, le cadre améliore la stabilité, la cohérence sémantique et l'interprétabilité des sujets à travers des corpus de tailles, de structures et de langues variées. Les résultats expérimentaux montrent que SemaTopic obtient un gain relatif de +6,2% en cohérence sémantique par rapport à BERTopic sur le corpus 20 Newsgroups (C_v = 0,5315 contre 0,5004), tout en maintenant des performances stables sur des corpus hétérogènes et multilingues.Le second cadre, ARIA, prolonge ce processus par un raffinement sémantique post-extraction. Il intègre l'étiquetage automatique basé sur des modèles de langage, l'enrichissement sémantique guidé, l'organisation hiérarchique et l'indexation au niveau des sections, transformant ainsi les distributions probabilistes de thèmes en représentations structurées et navigables des connaissances. Appliqué comme couche finale du pipeline, ARIA permet une amélioration progressive de la cohérence thématique, faisant passer des valeurs de base autour de 0,45 à des niveaux atteignant jusqu'à 0,74 après optimisation sémantique complète. Cette progression reflète l'effet cumulatif du clustering sémantique, de l'optimisation guidée par la cohérence et du raffinement basé sur les modèles de langage.Des expérimentations approfondies menées sur des corpus scientifiques, spécialisés, multilingues et de textes courts valident la robustesse, la cohérence et l'adaptabilité de l'approche proposée. Au-delà d'une amélioration algorithmique isolée, cette thèse contribue à faire évoluer le topic modeling vers un cadre intégré, sémantiquement fondé et opérationnel, dédié à la découverte de connaissances dans des environnements textuels complexes.

## 키워드

Corpus linguistics, Text corpus, Cluster analysis, Pipeline (software)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모


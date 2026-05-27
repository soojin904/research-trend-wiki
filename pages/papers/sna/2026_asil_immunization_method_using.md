---
title: "An immunization method using a context-based centrality in multiplex networks"
authors: ['Leili Soleimani Asil', 'Mohammad Khansari']
year: 2026
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'COVID-19 epidemiological studies', 'Bioinformatics and Genomic Networks']
source: raw/2026_openalex_An_immunization_method_using_a_contextbased_nws_2026_10026.md
---

# An immunization method using a context-based centrality in multiplex networks

**제목(한글)**: 다중 네트워크에서 맥락 기반 중심성을 활용한 면역화 방법

**저자**: Leili Soleimani Asil; Mohammad Khansari
**출처**: Network Science, Vol.14
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1017/nws.2026.10026

## 한국어 요약

**연구질문**: 감염 전파 레이어와 정보 확산 레이어로 구성된 멀티플렉스 네트워크에서, 각 레이어의 맥락에 맞는 중심성 지표를 결합하면 면역화 전략의 효율을 높일 수 있는가?

**방법론**:
- 감염 레이어에는 PageRank, 인식(awareness) 레이어에는 근접 중심성(closeness centrality)을 적용한 멀티플렉스 결합 PageRank(MCPR) 지표 개발
- SIR-UA(감염-회복-인식) 확장 모델로 홍역·천연두 시나리오 시뮬레이션
- 합성 네트워크 및 Copenhagen Networks Study 실제 데이터로 검증

**주요 결과**:
- MCPR이 단일 레이어 PageRank 면역화 및 기존 멀티플렉스 PageRank 대비 일관적으로 우수
- 10% 면역화 적용 시 홍역 2.2%, 천연두 7% 유행 규모 감소
- 파라미터 최적화를 통해 최대 9.5%의 추가 개선 가능

## 초록 (원문)

Abstract This is very important to prioritize nodes for immunization in controlling infectious disease outbreaks. In this paper, we propose a new immunization strategy for multiplex networks; we specifically model two separate layers: the physical layer where infection propagates and the virtual layer where information is transmitted. We assume that each layer has a different “context” and use that to identify the most suitable centrality measure for each. For the infection layer, we choose PageRank, as it has shown certain effectiveness in determining those nodes crucial for reducing transmission. For the awareness layer, we show how closeness centrality is a better measure of quality for the passing of information along short paths. We, therefore, propose Multiplex Combined PageRank, or MCPR, combining the centralities from both layers to immunize the most important nodes. The simulations employ the extended SIR-UA model, which exploits the interaction between infection and awareness dynamics, to scenarios on measles and smallpox. Validation on both synthetic networks and the real-world Copenhagen Networks Study dataset demonstrates consistent superiority of MCPR over classical methods. In terms of epidemic size in simulations with very limited immunization budgets, MCPR indeed resulted in better outcomes than the single-layer PageRank immunization strategy and the existing Multiplex PageRank method. Real-world validation shows epidemic size reductions of 2.2% for measles and 7% for smallpox at 10% immunization coverage, with parameter optimization yielding improvements up to 9.5%. The sensitivity analysis demonstrates that increasing transmission of awareness and the quality of information can help control the infection immensely.

## 키워드

Centrality, Closeness, PageRank, Transmissibility (structural dynamics), Immunization, Measure (data warehouse), Multiplex, Quality (philosophy)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/centrality|Centrality]]
- [[pages/concepts/multilayer_network|다층 네트워크]]

## 메모


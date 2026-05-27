---
title: "Leveraging GANs for citation intent classification and its impact on citation network analysis"
authors: ['Davi A. Bezerra', 'Filipi N. Silva', 'Diego R. Amancio']
year: 2026
venue: "Journal of Informetrics"
tags: ['Biomedical Text Mining and Ontologies']
source: raw/applied/applied_2026_Leveraging_GANs_for_citat_j_joi_2026_101791.md
---

# Leveraging GANs for citation intent classification and its impact on citation network analysis
**제목(한글)**: 인용 의도 분류를 위한 GAN의 활용과 그것이 인용 네트워크 분석에 미치는 영향

**저자**: Davi A. Bezerra; Filipi N. Silva; Diego R. Amancio
**출처**: Journal of Informetrics, Vol.20, pp.101791-101791
**발행일**: 2026-02-27
**DOI**: https://doi.org/10.1016/j.joi.2026.101791

## 한국어 요약

**연구질문**: 학술적 인용망 분석에서 단순 카운팅을 넘어 인용이 배경 설명인지, 방법론 계승인지, 대조군 비교인지 등의 '인용 의도'를 고도화된 딥러닝으로 효율적으로 분류하고 영향력을 평가하는 방법은 무엇인가?

**방법론**:
- GAN과 SciBERT 도메인 임베딩을 결합한 반지도 인용 의도 분류 모델(cGAN-SciBERT) 제안
- 7.6만 개 노드 및 17.1만 개 엣지를 가진 unarXiv 인용 네트워크 데이터셋에 필터링 적용 및 중앙성 변동 분석

**주요 결과**:
- 제안된 GAN 기반 모델이 극도로 적은 매개변수로도 SciCite 데이터셋에서 F1-스코어 0.887의 우수한 성능을 달성
- 인용 의도에 따른 인용망 필터링 시, PageRank나 Betweenness 중앙성이 매우 크게 변동하여 단순 다수 인용보다 인용 의도의 질적 필터링이 영향력 평가의 왜곡을 방지함을 증명


## 초록 (원문)

• We propose a semi-supervised model for citation intent classification that integrates GANs with domain-specific SciBERT embeddings. • This paper applies intent-based filtering to large-scale citation networks, including the unarXiv dataset with 76k nodes and 171k edges. • cGAN-SciBERT yields competitive F1-scores (0.887 on SciCite) with a minimal number of parameters. • Citation intent filtering changes centrality rankings and enables a more refined assessment of paper influence. Citations play a fundamental role in the scientific ecosystem, serving as a foundation for tracking the flow of knowledge, acknowledging prior work, and assessing scholarly influence. In scientometrics, they are also central to the construction of quantitative indicators. Not all citations, however, serve the same function: some provide background, others introduce methods, or compare results. Therefore, understanding citation intent allows for a more nuanced interpretation of scientific impact. In this paper, we adopted a GAN-based method to classify citation intents. Our results revealed that the proposed method achieves competitive classification performance, closely matching state-of-the-art results with substantially fewer parameters. This demonstrates the effectiveness and efficiency of leveraging GAN architectures combined with contextual embeddings in an intent classification task. We also investigated whether filtering citation intents affects the centrality of papers in citation networks. Analyzing the network constructed from the unArXiv dataset, we found that paper rankings can be significantly influenced by citation intent. All four centrality metrics examined – degree, PageRank, closeness, and betweenness – were sensitive to the filtering of citation types. The betweenness centrality displayed the greatest sensitivity, showing substantial changes in ranking when specific citation intents were removed.

## 키워드

Betweenness centrality, Citation, Centrality, Ranking (information retrieval), Citation analysis, Matching (statistics), Network analysis, Network science

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모


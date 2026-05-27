---
title: "A study of semantic relation measures using phrases in scientific texts"
authors: ['Sulaiman Alriyaee']
year: 2026
venue: "Performance Measurement and Metrics"
tags: ['Biomedical Text Mining and Ontologies', 'Text Readability and Simplification', 'Topic Modeling']
source: raw/applied/applied_2026_A_study_of_semantic_relat_pmm_12_2024_0069.md
---

# A study of semantic relation measures using phrases in scientific texts
**제목(한글)**: 과학 텍스트 내 구문(Phrase)을 활용한 의미 관계 척도 연구

**저자**: Sulaiman Alriyaee
**출처**: Performance Measurement and Metrics, Vol.None, pp.1-13
**발행일**: 2026-05-22
**DOI**: https://doi.org/10.1108/pmm-12-2024-0069

## 한국어 요약

**연구질문**: 과학 및 의학 논문 텍스트 내에서 특정 명사구/구문의 길이와 빈도가 텍스트 간 의미론적 관계 및 유사도 측정에 미치는 영향은 무엇인가?

**방법론**:
- 구글 학술검색에서 대사 증후군 관련 고인용 논문을 수집한 뒤, 불용어 제거 및 토큰화를 거쳐 구문 빈도 랭킹 산출
- 구문 길이(2~8개 단어로 정규화)에 따라 벡터화한 후 구문 간 코사인 유사도 분석을 시행해 의미 관계성 평가

**주요 결과**:
- 어휘적 및 의미적 유사도 분석을 통해, 두 명사구 사이에 공통되는 어휘가 존재하지 않더라도 중심 단어들이 동일한 맥락에서 쓰일 경우 높은 코사인 유사도를 나타내는 현상을 규명
- 핵심 단어 주변에서 텍스트의 맥락적 의미를 돕는 주변어들의 출현 특성을 도출하여, 기계가 구조화된 문헌 검색 시스템을 설계할 때 의미론적 검색 효율성을 높일 수 있는 이론적 기반 제공


## 초록 (원문)

Purpose Identifying similarities between parts of a text, paper or document has implications for several information processing and retrieval tasks. Thus, information processing and retrieval research aims to detect content relations in terms of lexical, conceptual, semantic and content features. Semantic similarity measures refer to detecting content relations based on the equivalence between texts using the semantic component. Measuring text similarity is the aim of our work. Design/methodology/approach This work involves the following main steps: Thorough data preprocessing is crucial. This involves removing stop words, common words that add little semantic value. Tokenization is the process by which a large amount of text is divided into smaller parts (phrases) called tokens. Applying stemming or lemmatization also helps reduce words to their base form, thereby standardizing the dataset for better comparison. The various attribute types are used. Phrases are the attributes that characterize the concepts used in the text. Cosine indexes generate binary values between 0 and 1. However, cosine reflects the similarity in terms of percentage. When cosine similarity is near 100, it refers to the binary value 1. The cosine similarity focuses on the angle between two vectors. This makes cosine similarity more robust in capturing the pattern similarities between two data sets, even if their magnitudes differ. (Phil Miesle 2023). The phrase length is measured by the number of words in a phrase without stop words. The phrase length normally ranges from two to eight. If the phrase length is longer, the phrase is content expressive and far from generic. The phrase length is the expression of concept and semantic richness. The literature does not address the phrase length and its impact on text similarity and other features. The available research mainly outlines the linguistic attributes; for example, the lexically derived syntactic representations are discussed (Stallings, 1998) and the structure of surrounding phrase lengths (Zvonik, 2003). Removing stop words from sentences reduces the low-level information, which makes the sentences easy to understand. Moreover, removing the stop words doesn't affect the contextual meaning of sentences, as machines preserve the semantic information of words. (Han, 2021; Hasanah, 2019; Hu, 2022; Huang, 2019) Finally, the similarity is calculated as the minimum distance path between nodes (phrases), which are cosine. We evaluated the phrase similarity using relatively small benchmark datasets. A significant scientific phrase, “Metabolic Syndrome”, is used to search Google Scholar and a few highly cited papers are identified. Each selected full text is subjected to phrase extraction, ranking phrases based on frequency. These phrases contain stop words that have been removed. The phrases contain a minimum of two words and a maximum of eight words. When stop words are removed, the content of the treated concept is preserved, and when frequent phrases are selected, they are considered tokens that represent the content. The top frequent phrases are selected for each sample, and the similarity is measured using cosine. Findings Even though the lexical and semantic similarity measures are different, lexical and semantic similarities are correlated in highly specialized documents such as journals or scientific reports. Cosine similarity measures report a low-level correlation even if there is no common word between two phrases. For example, the phrases “glance disease models and mechanisms” and “insulin resistance visceral adiposity atherogenic dyslipidemia and endothelial” have no common words and still exhibit a cosine similarity score of 24.4%. Partial phrase similarity is observed in different sets of data in this work. The analysis reveals that in the highly frequent phrases, the most commonly used words are insulin, syndrome, cardiovascular, diabetics, and therapeutics, followed by a few next-level supporting words such as resistance, models, mechanisms, treatment and systems. Thus, we can understand how a core theme is treated in the literature in supporting terms. Research limitations/implications This study has a few limitations. First, the dataset is relatively small and focuses exclusively on highly cited papers within a single medical domain, which may limit its generalizability to the broader scientific literature. Second, the analysis filters out low-frequency phrases, concentrating solely on high-frequency terms. This exclusion may overlook emerging concepts that appear infrequently but hold significant semantic value. Third, while cosine similarity effectively captures structural relationships, it may not fully account for deeper cognitive or contextual connections, particularly when phrases share no common words yet remain conceptually linked. Additionally, the impact of phrase length on similarity measures remains underexplored, limiting the framework’s ability to systematically assess how syntactic complexity influences scoring. Finally, reliance on static phrase extraction may oversimplify dynamic linguistic variations, highlighting the need for more adaptive NLP techniques in future work. Practical implications The dataset used is smaller in terms of phrases analyzed. The low-frequent phrases are removed from the analysis, leading to the processing of selected high-frequent words. However, this work indicates the use of phrases for processing. Cosine values are more productive when measuring semantic similarity than lexical similarity. Our future work will determine the relation between phrase frequency and cosine similarity values to generate strong inferences. We intend to extend the work with more samples and datasets and include more phrases, which can lead to effective results. Social implications Detecting phrase relations, both complete and partial, will enable the identification of document similarities. The existing practices are often unrelated to finding cognitive and semantic relations. This kind of exercise leads us to pave the way for measuring naturally existing similarities among literature and sub-domains. Originality/value This paper identifies the naturally existing relations between concepts in natural language texts. Text analysis will be improved using the conceptual model described in this paper.

## 키워드

Phrase, Cosine similarity, Semantic similarity, Similarity (geometry), Semantic analysis (machine learning), Preprocessor, Semantics (computer science), Semantic equivalence

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모


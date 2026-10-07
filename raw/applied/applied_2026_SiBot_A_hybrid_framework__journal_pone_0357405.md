---
title: "SiBot: A hybrid framework for fine-grained semantic attribution of AI-generated text and its production deployment"
authors: ['Md. Sadiq Iqbal', 'Mohammod Abul Kashem']
year: 2026
publication_date: 2026-09-08
venue: "PLoS ONE"
volume: "21"
issue: "9"
pages: "e0357405-e0357405"
doi: "https://doi.org/10.1371/journal.pone.0357405"
oa_status: "gold"
openalex_id: "https://openalex.org/W7211960474"
query_keyword: "text analysis"
tags: ['Misinformation and Its Impacts', 'Computational and Text Analysis Methods', 'Hate Speech and Cyberbullying Detection']
keywords: ['Benchmark (surveying)', 'Transformer', 'Random forest', 'Generalizability theory', 'Precision and recall', 'Binary number', 'Task (project management)', 'Construct (python library)']
source: openalex-keyword
---

# SiBot: A hybrid framework for fine-grained semantic attribution of AI-generated text and its production deployment

**저자**: Md. Sadiq Iqbal; Mohammod Abul Kashem
**출처**: PLoS ONE, Vol.21 No.9, pp.e0357405-e0357405
**발행일**: 2026-09-08
**DOI**: https://doi.org/10.1371/journal.pone.0357405
**수집 키워드**: text analysis

## 초록

Large language models such as ChatGPT, Gemini, Claude and DeepSeek now generate text that is routinely indistinguishable from human writing, yet virtually every deployed detector answers only one binary question: human or AI. This is the wrong question for the settings that matter most. Digital forensics needs to know which model produced a text; academic-integrity adjudication needs to know whether a human was involved at all; and neither can be answered by a single probability, least of all for the hybrid human-AI drafts that now dominate real-world writing. This paper addresses that gap with SiBot, an end-to-end framework that reformulates AI-text detection as fine-grained multi-class source attribution and carries it through to public deployment. We construct two purpose-built corpora using a controlled bank of 3,000 prompts spanning six subject domains and five task types: a 66,000-sample corpus covering 22 AI sources, and a 30,000-sample corpus covering 10 classes that explicitly models five pure sources and four human-AI collaboration workflows; both are publicly released as the TXD-22 benchmark dataset. On the 22-class corpus we benchmark twelve feature-classifier combinations and find that TF-IDF with Random Forest attains 68.2% accuracy and an AUC of 0.742. On the 10-class corpus we benchmark fifteen classical, deep-learning and fine-tuned transformer baselines, and propose a hybrid architecture that fuses sparse TF-IDF lexical features with DeBERTa contextual embeddings at the feature level before Random Forest classification. The proposed hybrid attains 92.38% accuracy, 92.41% precision, 92.38% recall and 92.31% F1 under prompt-aware 10-fold cross-validation, a 17.73-point gain over the strongest fine-tuned transformer (DeBERTa, 74.65%) and a 34.30-point gain over TF-IDF with Random Forest alone, with non-overlapping 95% confidence intervals. An ablation confirms that both branches are necessary, and SHAP and LIME analyses expose the lexical evidence behind individual decisions. Because the 10-class hybrid is both substantially more accurate and interpretable, it is the model served by the live SiBot platform; the 22-class model is reported here as a research benchmark, and extending the deployment to all 22 classes is left to future work. In a controlled three-way benchmark against QuillBot, Turnitin, ZeroGPT and TextGuard, SiBot is the only system that names the generating model of AI text (Gemini, 96.7% confidence) and the only one that recognises hybrid provenance (97.7% confidence, against verdicts ranging from 0% to 76% among the commercial tools on the identical input).

## 키워드

Benchmark (surveying), Transformer, Random forest, Generalizability theory, Precision and recall, Binary number, Task (project management), Construct (python library)

## 주제 분류 (OpenAlex Topics)

- Misinformation and Its Impacts (score: 0.165)
- Computational and Text Analysis Methods (score: 0.115)
- Hate Speech and Cyberbullying Detection (score: 0.101)

## 메모


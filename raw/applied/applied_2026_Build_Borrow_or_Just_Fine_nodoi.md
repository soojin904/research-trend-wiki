---
title: "Build, Borrow, or Just Fine-Tune? A Political Scientist's Guide to Choosing NLP Models"
authors: ['Shreyas Meher']
year: 2026
publication_date: 2026-03-10
venue: "ArXiv.org"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7134992970"
query_keyword: "text analysis"
tags: ['Computational and Text Analysis Methods', 'Terrorism, Counterterrorism, and Political Violence', 'Misinformation and Its Impacts']
keywords: ['Event (particle physics)', 'Intersection (aeronautics)', 'Task (project management)', 'Politics', 'Point (geometry)', 'Class (philosophy)', 'Face (sociological concept)', 'Terrorism']
source: openalex-keyword
---

# Build, Borrow, or Just Fine-Tune? A Political Scientist's Guide to Choosing NLP Models

**저자**: Shreyas Meher
**출처**: ArXiv.org
**발행일**: 2026-03-10
**DOI**: 
**수집 키워드**: text analysis

## 초록

Political scientists increasingly face a consequential choice when adopting natural language processing tools: build a domain-specific model from scratch, borrow and adapt an existing one, or simply fine-tune a general-purpose model on task data? Each approach occupies a different point on the spectrum of performance, cost, and required expertise, yet the discipline has offered little empirical guidance on how to navigate this trade-off. This paper provides such guidance. Using conflict event classification as a test case, I fine-tune ModernBERT on the Global Terrorism Database (GTD) to create Confli-mBERT and systematically compare it against ConfliBERT, a domain-specific pretrained model that represents the current gold standard. Confli-mBERT achieves 75.46% accuracy compared to ConfliBERT's 79.34%. Critically, the four-percentage-point gap is not uniform: on high-frequency attack types such as Bombing/Explosion (F1 = 0.95 vs. 0.96) and Kidnapping (F1 = 0.92 vs. 0.91), the models are nearly indistinguishable. Performance differences concentrate in rare event categories comprising fewer than 2% of all incidents. I use these findings to develop a practical decision framework for political scientists considering any NLP-assisted research task: when does the research question demand a specialized model, and when does an accessible fine-tuned alternative suffice? The answer, I argue, depends not on which model is "better" in the abstract, but on the specific intersection of class prevalence, error tolerance, and available resources. The model, training code, and data are publicly available on Hugging Face.

## 키워드

Event (particle physics), Intersection (aeronautics), Task (project management), Politics, Point (geometry), Class (philosophy), Face (sociological concept), Terrorism

## 주제 분류 (OpenAlex Topics)

- Computational and Text Analysis Methods (score: 0.382)
- Terrorism, Counterterrorism, and Political Violence (score: 0.111)
- Misinformation and Its Impacts (score: 0.048)

## 메모


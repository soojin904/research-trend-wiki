---
title: "Fine-tuning SciBERT to enable ASJC-based assessments of the disciplinary orientation of research collections"
authors: ['Michael Gusenbauer', 'Jochen Endermann', 'Harald Huber', 'Simone I. Strasser', 'Andreas‐Nizar Granitzer', 'Thomas Ströhle']
year: 2025
publication_date: 2025-12-01
venue: "Scientometrics"
volume: "131"
issue: "4"
pages: "2401-2438"
doi: "https://doi.org/10.1007/s11192-025-05490-0"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W4416841393"
query_keyword: "text analysis"
tags: ['Text and Document Classification Technologies', 'Advanced Graph Neural Networks', 'Computational and Text Analysis Methods']
keywords: ['Overfitting', 'Metadata', 'Subject (documents)', 'Set (abstract data type)', 'Scopus', 'Taxonomy (biology)', 'Discipline', 'Orientation (vector space)']
source: openalex-keyword
---

# Fine-tuning SciBERT to enable ASJC-based assessments of the disciplinary orientation of research collections

**저자**: Michael Gusenbauer; Jochen Endermann; Harald Huber; Simone I. Strasser; Andreas‐Nizar Granitzer; Thomas Ströhle
**출처**: Scientometrics, Vol.131 No.4, pp.2401-2438
**발행일**: 2025-12-01
**DOI**: https://doi.org/10.1007/s11192-025-05490-0
**수집 키워드**: text analysis

## 초록

Abstract Subject classification is essential for navigating scientific literature, yet the influential All Science Journal Classification (ASJC) has limited practical applicability. Its limitations stem from reliance on an incomplete source list restricted to Scopus content, and from journal-level classifications that often misrepresent individual documents. The most significant recent development in ASJC-based classification is OpenAlex, but it narrows the framework by reducing the number of categories and enforcing single-label assignments—both of which diminish classification accuracy. In response, this study introduces the first open, multi-label, implementation of the ASJC taxonomy that more accurately classifies individual documents, including those published in general science or interdisciplinary journals. We develop a fine-tuned SciBERT model for multi-label classification across 307 ASJC subjects, trained on a large-scale Crossref dataset using title, abstract, and source title metadata. The model achieves a weighted F1-score of 0.892 on 307 subjects and 0.934 on its 26 parent subjects on a Crossref test set with full metadata. It maintains respectable performance-0.532 and 0.694, respectively—even without the source title information that ASJC classification relies upon. Our fine-tuning strategy includes selective metadata omission to mitigate overfitting and data augmentation for underrepresented categories. In addition, we introduce a tailored label-averaging method that enables assessment of the disciplinary orientation and comparison of individual documents and larger collections—such as researcher portfolios, institutions, and entire databases. To promote transparency, reproducibility, and further research, we openly release our model via Hugging Face ( https://huggingface.co/asjc-classification ), providing ready-to-use ASJC-based subject classification.

## 키워드

Overfitting, Metadata, Subject (documents), Set (abstract data type), Scopus, Taxonomy (biology), Discipline, Orientation (vector space), Face (sociological concept)

## 주제 분류 (OpenAlex Topics)

- Text and Document Classification Technologies (score: 0.338)
- Advanced Graph Neural Networks (score: 0.070)
- Computational and Text Analysis Methods (score: 0.065)

## 메모


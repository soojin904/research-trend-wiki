---
title: "A Teacher-Student BERT Architecture for Semi-Supervised Learning on Unstructured Social Work Texts: Identifying Service Gaps and Needs"
authors: ['Yih-Chang Chen', 'Chia-Ching Lin', 'Sedat Ağan']
year: 2026
venue: "International Journal of Intelligent Systems and Applications"
tags: ['Mental Health via Writing', 'Social Work Education and Practice', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_A_TeacherStudent_BERT_Arc_ijisa_2026_05_11.md
---

# A Teacher-Student BERT Architecture for Semi-Supervised Learning on Unstructured Social Work Texts: Identifying Service Gaps and Needs

**저자**: Yih-Chang Chen; Chia-Ching Lin; Sedat Ağan
**출처**: International Journal of Intelligent Systems and Applications, Vol.18, pp.213-230
**발행일**: 2026-09-23
**DOI**: https://doi.org/10.5815/ijisa.2026.05.11

## 초록 (원문)

To address the “information gap” in social work arising from unstructured data and limited labeled instances, this study proposes a semi-supervised learning framework based on a Teacher-Student BERT architecture. Based on an analysis of 50,000 case records spanning 2019 to 2024, the model incorporates Latent Dirichlet Allocation for topic extraction alongside a multidimensional gap analysis. The proposed method attained a state-of-the-art F1 score of 0.913, markedly surpassing baseline BERT models. Notable findings include a 67.6% increase in mental health-related discourse and the quantification of significant systemic deficiencies, such as inadequate coverage in elderly care (45.8%) and substantial unmet needs in medical assistance (46.4%). Furthermore, to address the profound challenges of class imbalance and the data-hungry nature of transformer models, this study integrated generative artificial intelligence (AI) data augmentation techniques. This approach produced synthetically varied case narratives that preserved the original socio-economic context while expanding lexical and structural diversity, thereby significantly enhancing the classification accuracy of minority classes. Additionally, the use of a Mean Teacher denoising framework and knowledge distillation drastically reduced the computational inference time, rendering the architecture highly suitable for deployment in resource-constrained social welfare environments. Prior to analysis, all case records underwent rigorous automated Personally Identifiable Information (PII) scrubbing utilizing the Microsoft Presidio framework to guarantee data privacy. To ensure reproducibility, the Teacher-Student training codebase, prompt architectures, and anonymized synthetic data samples will be made publicly available upon request. This research effectively transforms administrative textual data into actionable strategic intelligence, offering a scalable and evidence-based tool to enhance resource allocation and inform policy development.

## 키워드

Software deployment, Inference, Latent Dirichlet allocation, Baseline (sea), Scalability, Rendering (computer graphics), Architecture, Big data

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모


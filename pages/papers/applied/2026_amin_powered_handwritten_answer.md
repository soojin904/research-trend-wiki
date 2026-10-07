---
title: "AI powered handwritten answer script evaluation framework for automated assessment of text and figure based responses"
authors: ['Md Nurul Amin', 'Md. Ashikur Rahman Khan', 'Ishtiaq Ahammad']
year: 2026
venue: "Discover Artificial Intelligence"
tags: ['Handwritten Text Recognition Techniques', 'Multimodal Machine Learning Applications', 'Topic Modeling']
source: raw/applied/applied_2026_AI_powered_handwritten_an_s44163_026_02181_4.md
---

# AI powered handwritten answer script evaluation framework for automated assessment of text and figure based responses

**저자**: Md Nurul Amin; Md. Ashikur Rahman Khan; Ishtiaq Ahammad
**출처**: Discover Artificial Intelligence, Vol.6
**발행일**: 2026-09-25
**DOI**: https://doi.org/10.1007/s44163-026-02181-4

## 초록 (원문)

Manual evaluation of handwritten answer scripts is time-consuming and subjective, and grows increasingly impractical as enrolment rises; moreover, most existing automated grading systems support only typed text and cannot assess figure-based responses, leaving a substantial gap in educational technology. To address this problem, this research presents a computer-based evaluation framework for handwritten answer scripts containing both textual and graphical responses. Scripts are digitized through optical character recognition (OCR), and the recognized text is evaluated using four complementary techniques: a writing-quality score, a keyword matching score, a similarity score, and a reference-overlap score that quantifies verbatim copying from the expected answer. Two text evaluation cases are compared on a validation set of 25 student responses: the first case employs TF-IDF-based cosine similarity and reaches 83.8% agreement with examiner-assigned marks, while the second replaces it with NLP-based semantic similarity using spaCy word embeddings, improving agreement to 87.4%; this improvement is statistically significant (Wilcoxon signed-rank test, p = 0.007). Separately, figure evaluation compares student-drawn diagrams with reference figures using deep convolutional (MobileNetV2) feature embeddings matched by cosine similarity, achieving 85.1% agreement, versus 81.1% for a Hu-moment-based Euclidean distance approach. Agreement with human examiners is further quantified through MAE, RMSE, Pearson and Spearman correlation, and quadratic weighted kappa. These results imply that combining semantic text similarity with deep feature-based figure comparison can provide fair and consistent grading support for educators; broader deployment in universities and standardized testing will require validation on larger, more diverse datasets.

## 키워드



## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모


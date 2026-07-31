---
title: "Automated Sentiment Intelligence for Educational Quality Assurance: A Topic–Sentiment Framework for Thai Student Feedback with Deep Model Instantiations"
authors: ['Tanagrit Chansaeng', 'Nasith Laosen', 'Boonmee Nissaidee', 'Pita Jarupunphol']
year: 2026
venue: "Artificial Intelligence and Applications"
tags: ['Sentiment Analysis and Opinion Mining', 'Online Learning and Analytics', 'Intelligent Tutoring Systems and Adaptive Learning']
source: raw/applied/applied_2026_Automated_Sentiment_Intel_bonviewaia62029502.md
---

# Automated Sentiment Intelligence for Educational Quality Assurance: A Topic–Sentiment Framework for Thai Student Feedback with Deep Model Instantiations

**저자**: Tanagrit Chansaeng; Nasith Laosen; Boonmee Nissaidee; Pita Jarupunphol
**출처**: Artificial Intelligence and Applications, Vol.None
**발행일**: 2026-07-07
**DOI**: https://doi.org/10.47852/bonviewaia62029502

## 초록 (원문)

Student comments provide direct evidence about teaching, curriculum delivery, and learning conditions, but reviewing a large volume of free-text responses by hand is difficult to sustain. Automated analysis is therefore attractive, although Thai feedback presents particular challenges. Thai text does not consistently mark word boundaries, and student comments often include abbreviated wording, informal language, and expressions whose sentiment depends heavily on context. This paper proposes an Automated Sentiment Intelligence (ASI) framework for Thai educational feedback that (1) structures raw institutional comments into topic and sentiment signals, (2) defines a reproducible workflow for data cleansing, annotation, and dual-task modeling, and (3) supports deployment-oriented reporting through standard classification metrics and confusion-matrix-based error analysis. Using 4145 feedback records collected from a vocational education information system and refining them to 2873 entries after preprocessing, ASI organizes feedback into four topic domains (instructor, curriculum, facility, and other) and three sentiment classes (positive, neutral, negative). The framework is instantiated with two representative deep natural language processing architectures: a word-level Bidirectional Long Short-Term Memory (BiLSTM) pipeline (newmm tokenization + Thai Word2Vec) and a transformer-based XLM‐R fine-tuning pipeline (SentencePiece subword tokenization). Experimental results show strong topic classification performance for both instantiations, with higher overall topic accuracy for XLM‐R (0.922) compared to BiLSTM (0.882). For sentiment analysis, XLM‐R achieves a higher overall accuracy (0.80) than BiLSTM (0.729), with notably improved performance on the neutral and negative classes. The proposed ASI–XLM-R framework provides a scalable, reproducible approach to transforming Thai student feedback into actionable intelligence to support institutional decision-making. Received: 1 March 2026 | Revised: 24 June 2026 | Accepted: 26 June 2026 Conflicts of Interest The authors declare that they have no conflicts of interest to this work. Data Availability Statement The data that support the findings of this study are openly available in in GitHub at https://github.com/nasith/thai-student-feedback-topic-sentiment. Author Contribution Statement Tanagrit Chansaeng: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing – original draft, Writing – review &amp; editing, Visualization. Nasith Laosen: Methodology, Software, Validation, Formal analysis, Data curation, Writing – original draft, Writing – review &amp; editing, Visualization. Boonmee Nissaidee: Validation, Investigation, Resources, Data curation, Writing – review &amp; editing, Project administration. Pita Jarupunphol: Conceptualization, Methodology, Software, Validation, Resources, Writing – original draft, Writing – review &amp; editing, Supervision, Project administration.

## 키워드

Pipeline (software), Lexical analysis, Sentiment analysis, Acronym, Quality (philosophy), Word (group theory), Educational data mining, Word processing

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


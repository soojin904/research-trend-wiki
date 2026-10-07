---
title: "A Hybrid Framework for Real-Time Sentiment Analysis and Adaptive Conversational Outcome Prediction in Domain-Specific Dialogue Systems"
authors: ['Mejdl Safran']
year: 2026
venue: "IIUM Engineering Journal"
tags: ['Topic Modeling', 'Sentiment Analysis and Opinion Mining', 'Emotion and Mood Recognition']
source: raw/applied/applied_2026_A_Hybrid_Framework_for_Re_iiumej_v27i3_4191.md
---

# A Hybrid Framework for Real-Time Sentiment Analysis and Adaptive Conversational Outcome Prediction in Domain-Specific Dialogue Systems

**저자**: Mejdl Safran
**출처**: IIUM Engineering Journal, Vol.27, pp.149-172
**발행일**: 2026-09-11
**DOI**: https://doi.org/10.31436/iiumej.v27i3.4191

## 초록 (원문)

The lack of non-verbal signals in text-based communication forces dialogue systems to rely entirely on dynamic textual sentiment changes to infer user intent and emotional shifts. However, substantial class imbalance and the static, post-hoc nature of existing text analysis models prevent dialogue systems from recognizing these emotional dynamics and predicting conversational outcomes in real time. This research presents a hybrid machine learning framework to address these challenges through integrated sentiment-aware analysis and real-time conversation outcome prediction. We first utilize a pre-trained RoBERTa model to assign sentiment scores to individual messages, which is required for two subsequent tasks: (i) conversational outcome classification to classify conversations into Interested in Islam, Wants to Convert, and Accepted Islam, and (ii) message impact prediction to assess the emotional influence of agents’ responses before deployment. In the initial task, our Enhanced Bi-LSTM model (enhanced with multi-head attention mechanisms and a boosted input capacity of 2500 tokens) achieves a macro-F1 score of 0.76, a balanced accuracy of 74.3%, and an overall accuracy of 90.0% on the full, unbalanced dataset when addressing the 3-class outcome classification task. By conducting an ablation study, we investigate the main source of error, the extremely ambiguous “Wants to Convert” class, and show the resilience of the model on well-defined classes, revealing that accuracy may exceed 99% by simplifying the task to a binary classification. In the second task, a fine-tuned BERT model achieves 80% accuracy in message-level sentiment prediction. The framework enables real-time feedback to refine adaptive responses and guide conversations toward desired outcomes. We assess our proposed framework using a case study of domain-specific conversations (such as religious outreach), supported by a dataset from a partner organization, to demonstrate applicability. The framework's flexibility makes it applicable to customer service, education, and healthcare, where effective communication depends on real-time sentiment analysis and outcome prediction. ABSTRAK: Kekurangan isyarat bukan lisan dalam komunikasi berasaskan teks memaksa sistem dialog bergantung sepenuhnya pada perubahan sentimen tekstual dinamik membuat kesimpulan tentang niat pengguna dan perubahan emosi. Walau bagaimanapun, ketidakseimbangan kelas yang ketara dan sifat statik dan pasca-hoc model analisis teks sedia ada menghalang sistem dialog daripada mengenali dinamik emosi ini dan meramalkan hasil perbualan pada masa nyata. Kajian ini membentang rangka kerja pembelajaran mesin hibrid bagi menangani cabaran melalui analisis kesedaran sentimen bersepadu dan ramalan hasil perbualan masa nyata. Pada permulaan, model RoBERTa dilatih terlebih dahulu bagi memberi skor sentimen kepada mesej individu. Ini diperlukan untuk dua tugasan seterusnya: (i) klasifikasi hasil perbualan kepada Berminat tentang Islam, Ingin Beranut Islam dan Menerima Islam, dan (ii) ramalan impak mesej bagi menilai pengaruh emosi respons ejen sebelum penggunaan. Melalui tugasan awal, dapatan model Peningkatan Bi-LSTM (dipertingkatkan dengan mekanisme perhatian berbilang kepala dan peningkatan kapasiti input sebanyak 2500 token) mencapai skor makro-F1 sebanyak 0.76, ketepatan seimbang sebanyak 74.3%, dan ketepatan keseluruhan sebanyak 90.0% pada set data penuh tidak seimbang apabila menangani tugasan pengelasan hasil 3 kelas. Dengan menjalankan kajian ablasi, kami menyiasat punca ralat utama, kelas "Ingin Menukar" yang sangat samar-samar, dan menunjukkan daya tahan model pada kelas yang ditakrif baik, mendedahkan bahawa ketepatan mungkin melebihi 99% dengan memudahkan tugasan kepada pengelasan binari. Menerusi tugasan kedua, model BERT yang ditala halus mencapai ketepatan 80% dalam ramalan sentimen peringkat mesej. Rangka kerja ini memudahkan maklum balas masa nyata bagi memperhalusi respons adaptif dan membimbing perbualan ke arah hasil yang diingini. Kami menilai rangka kerja yang dicadangkan menggunakan kajian kes yang mengandungi perbualan khusus domain (seperti jangkauan keagamaan). Ini disokong oleh set data daripada organisasi rakan kongsi, bagi menunjukkan kebolehgunaan. Fleksibiliti rangka kerja ini boleh digunakan untuk khidmat pelanggan, pendidikan dan penjagaan kesihatan, yang mana komunikasi berkesan bergantung pada analisis sentimen masa nyata dan ramalan hasil.

## 키워드

Outcome (game theory), Conversation, Sentiment analysis, Task (project management), Class (philosophy), Binary classification

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


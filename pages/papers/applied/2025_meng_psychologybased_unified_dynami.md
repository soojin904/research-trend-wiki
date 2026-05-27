---
title: "A Psychology-based Unified Dynamic Framework for Curriculum Learning"
authors: ['Guangyu Meng', 'Qinkai Zeng', 'John P. Lalor', 'Hong Yu']
year: 2025
venue: "Computational Linguistics"
tags: ['Intelligent Tutoring Systems and Adaptive Learning', 'Topic Modeling', 'Machine Learning and Data Classification']
source: raw/applied/applied_2025_A_Psychologybased_Unified_coli_a_584.md
---

# A Psychology-based Unified Dynamic Framework for Curriculum Learning

**저자**: Guangyu Meng; Qinkai Zeng; John P. Lalor; Hong Yu
**출처**: Computational Linguistics, Vol.None, pp.1-49
**발행일**: 2025-12-11
**DOI**: https://doi.org/10.1162/coli.a.584

## 초록 (원문)

Abstract Directly learning from examples of varying difficulty levels is often challenging for both humans and machine learning models. A more effective strategy involves exposing learners to examples in a progressive order from easy to difficult. Curriculum Learning (CL) has been proposed to implement this strategy in machine learning model training. However, two key challenges persist in CL framework design: defining the difficulty of training data and determining the appropriate amount of data to input at each training step. Drawing inspiration from psychometrics, this paper presents a Psychology-based Unified Dynamic Framework for Curriculum Learning (PUDF).We quantify the difficulty of training data by applying Item Response Theory (IRT) to responses from Artificial Crowds (AC). This theory-driven IRT-AC approach leads to global (i.e., model-independent) and interpretable difficulty values. Leveraging IRT, we propose a training strategy, Dynamic Data Selection via Model Ability Estimation (DDS-MAE), to schedule the appropriate amount of data during model training. Since our difficulty labeling and model ability estimation are based on a consistent theory, namely IRT, their values are comparable within the same scope, potentially leading to aligned training data selection and faster convergence compared to the other CL methods. Experimental results demonstrate that fine-tuning pre-trained large language models with PUDF leads to higher accuracy and faster convergence on a suite of benchmark datasets compared to standard fine-tuning and state-of-the-art CL methods. Ablation studies and downstream analyses further validate the impact of PUDF for CL.

## 키워드

Benchmark (surveying), Crowds, Suite, Convergence (economics), Schedule, Curriculum, Selection (genetic algorithm), Key (lock)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


---
title: "Methodological Guidance for Predictor Variable Selection for Adolescent Smoking Outcomes in Global Youth Tobacco Survey Using R and Python"
authors: ["Wingston F Ng'ambi", 'Cosmas Zyambo', 'Lawrence N. Kazembe']
year: 2026
publication_date: 2026-02-17
venue: "medRxiv"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.64898/2026.02.14.26346305"
oa_status: "green"
openalex_id: "https://openalex.org/W7129392548"
query_keyword: "social network"
tags: ['Smoking Behavior and Cessation', 'Survey Methodology and Nonresponse', 'Data Analysis with R']
keywords: ['Categorical variable', 'Workflow', 'Python (programming language)', 'Feature selection', 'Selection (genetic algorithm)', 'Software', 'Comparability', 'Akaike information criterion']
source: openalex-keyword
---

# Methodological Guidance for Predictor Variable Selection for Adolescent Smoking Outcomes in Global Youth Tobacco Survey Using R and Python

**저자**: Wingston F Ng'ambi; Cosmas Zyambo; Lawrence N. Kazembe
**출처**: medRxiv
**발행일**: 2026-02-17
**DOI**: https://doi.org/10.64898/2026.02.14.26346305
**수집 키워드**: social network

## 초록

ABSTRACT Background The Global Youth Tobacco Survey (GYTS) is widely used to monitor tobacco use among adolescents worldwide. However, inconsistent analytical approaches particularly in handling complex survey designs and predictor selection limit comparability across countries, survey waves, and software platforms. Although much of the GYTS literature relies on proprietary tools such as SAS and SPSS, practical and transparent guidance on implementing reproducible, theory-informed analyses remains limited. A unified workflow that respects the survey’s design while supporting cross-platform implementation is needed. Methods We developed a reproducible, open-source workflow for analysing GYTS data using R and Python. In R, analyses were conducted using the survey package (svydesign and svyglm) with constrained stepwise selection via stepAIC. In Python, a custom constrained stepwise procedure was implemented using statsmodels generalized linear models. The workflow explicitly incorporates survey weights, stratification, and clustering; harmonises variables across countries; protects a priori demographic covariates; and ensures consistent treatment of categorical predictors. The approach is illustrated using data from Zambia (n = 2,959) and pooled data from Ghana, Mauritius, Seychelles, and Togo (n = 15,914). Predictor selection was guided by Social Cognitive Theory and evidence from systematic reviews. Results The constrained selection framework consistently retained key demographic variables (age, sex, and grade) while allowing data-driven selection of modifiable predictors using the Akaike Information Criterion. When identical constraints were applied, the R and Python implementations selected identical models and produced nearly equivalent point estimates (adjusted odds ratio differences &lt;0.01), although Python-based confidence intervals did not account for clustering. Of 18 candidate predictors across individual, social, media, and policy domains, 14 were retained. The strongest independent predictors included awareness of tobacco products (OR = 5.61, 95% CI: 4.65– 6.78), peer smoking (OR = 4.57, 95% CI: 3.34–6.25), and exposure to tobacco marketing (OR = 2.34, 95% CI: 1.89–2.91). Conclusions This study provides a generalisable, theory-informed framework for predictor selection in complex survey data using open-source tools. The workflow supports consistent analyses across countries, survey waves, and software platforms, and is transferable to other youth and adult population surveys. All code and harmonisation resources are openly available to support reproducibility and adaptation. Plain-Language Summary What we asked: Can we predict adolescent smoking using GYTS data in a way that is easy to follow and reproducible across software? What we did: Built a single workflow that respects survey design (weights, strata, clusters) and selects predictors using four explicit criteria: theoretical grounding in Social Cognitive Theory, empirical support from prior studies, relevance for intervention, and cross-country validity. Core demographics (age, sex, grade, region) were protected as essential confounders, while other predictors were selected based on statistical fit. The workflow runs equivalently in R and Python. Why it matters: Many GYTS studies use weights only and ignore clustering and stratification, which makes confidence intervals too narrow. More importantly, most analyses include variables arbitrarily or let software drop important confounders automatically. Our approach ensures theoretically meaningful, policy-relevant variables are retained, producing more reliable and actionable results for prevention programs.

## 키워드

Categorical variable, Workflow, Python (programming language), Feature selection, Selection (genetic algorithm), Software, Comparability, Akaike information criterion, Survey data collection, Health psychology

## 주제 분류 (OpenAlex Topics)

- Smoking Behavior and Cessation (score: 0.509)
- Survey Methodology and Nonresponse (score: 0.087)
- Data Analysis with R (score: 0.038)

## 메모


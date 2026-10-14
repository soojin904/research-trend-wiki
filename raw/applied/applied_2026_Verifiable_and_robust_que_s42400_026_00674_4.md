---
title: "Verifiable and robust query processing for multi-owner secret-shared databases under malicious owners"
authors: ['Lili Gu', 'Jinguo Li', 'Jiaqi Shi']
year: 2026
publication_date: 2026-10-09
venue: "Cybersecurity"
volume: "9"
issue: "1"
pages: ""
doi: "https://doi.org/10.1186/s42400-026-00674-4"
oa_status: "diamond"
openalex_id: "https://openalex.org/W7221171724"
query_keyword: "social network"
tags: ['Cryptography and Data Security', 'Privacy-Preserving Technologies in Data', 'Cloud Data Security Solutions']
keywords: ['multi-owner data sharing', 'verifiable secret sharing', 'zero-knowledge proofs', 'query processing', 'coordinator selection', 'private set intersection']
source: openalex-keyword
---

# Verifiable and robust query processing for multi-owner secret-shared databases under malicious owners

**저자**: Lili Gu; Jinguo Li; Jiaqi Shi
**출처**: Cybersecurity, Vol.9 No.1
**발행일**: 2026-10-09
**DOI**: https://doi.org/10.1186/s42400-026-00674-4
**수집 키워드**: social network

## 초록

Abstract Privacy-preserving set computation enables collaborative analytics over distributed datasets without disclosing sensitive information. Recent systems such as PRISM support efficient private set intersection and aggregation over outsourced secret-shared databases. However, they implicitly rely on the assumption that all data owners are honest and do not deviate from the protocol. This assumption is often unrealistic in multi-owner settings, where a small fraction of malicious owners may distribute inconsistent shares, outsource data that violate predefined attribute-level constraints, issue unauthorized queries, or interfere with aggregation-result confirmation, thereby compromising the correctness of query outcomes. To address these challenges, we propose a security-enhanced query framework that integrates verifiable data outsourcing with query-level governance for multi-owner secret-shared databases. The framework preserves information-theoretic privacy while integrating verifiable secret sharing and zero-knowledge proofs to ensure the consistency and attribute-level input validity of outsourced data shares. In addition, under an honest-majority assumption, we introduce a lightweight query-scoped consensus mechanism to collectively confirm query admissibility and aggregation-result consistency. By incorporating behavior-aware coordinator selection, the mechanism improves robustness against abnormal or malicious participants while avoiding heavyweight Byzantine fault-tolerant protocols. Experimental results show that, on workloads involving up to 50 data owners and datasets of up to 5 million records, the proposed framework incurs only moderate overhead compared with PRISM, while substantially improving robustness in the presence of malicious participants.

## 키워드

multi-owner data sharing, verifiable secret sharing, zero-knowledge proofs, query processing, coordinator selection, private set intersection

## 주제 분류 (OpenAlex Topics)

- Cryptography and Data Security (score: 0.375)
- Privacy-Preserving Technologies in Data (score: 0.363)
- Cloud Data Security Solutions (score: 0.225)

## 메모


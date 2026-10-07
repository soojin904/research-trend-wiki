---
title: "Sensitive system calls based packed malware variants detection using principal component initialized MultiLayers neural networks"
authors: ['Jixin Zhang', 'Kehuan Zhang', 'Zheng Qin', 'Hui Yin', 'Qixin Wu']
year: 2018
publication_date: 2018-09-10
venue: "Cybersecurity"
publisher: "Springer Nature"
volume: "1"
issue: "1"
pages: ""
doi: "https://doi.org/10.1186/s42400-018-0010-y"
openalex_id: "https://openalex.org/W2889682758"
cited_by_count: 29
fwci: 3.041
tags: ['Advanced Malware Detection Techniques', 'Network Security and Intrusion Detection', 'Software Testing and Debugging Techniques']
keywords: ['Unpacking', 'Malware', 'Computer science', 'Executable', 'Malware analysis', 'Principal component analysis', 'Artificial intelligence', 'Component (thermodynamics)']
source: openalex-netminer
---

# Sensitive system calls based packed malware variants detection using principal component initialized MultiLayers neural networks

**저자**: Jixin Zhang; Kehuan Zhang; Zheng Qin; Hui Yin; Qixin Wu
**출처**: Cybersecurity, Vol.1 No.1
**발행일**: 2018-09-10
**DOI**: https://doi.org/10.1186/s42400-018-0010-y

## 초록

Malware detection has become mission sensitive as its threats spread from computer systems to Internet of things systems. Modern malware variants are generally equipped with sophisticated packers, which allow them bypass modern machine learning based detection systems. To detect packed malware variants, unpacking techniques and dynamic malware analysis are the two choices. However, unpacking techniques cannot always be useful since there exist some packers such as private packers which are hard to unpack. Although dynamic malware analysis can obtain the running behaviours of executables, the unpacking behaviours of packers add noisy information to the real behaviours of executables, which has a bad affect on accuracy. To overcome these challenges, in this paper, we propose a new method which first extracts a series of system calls which is sensitive to malicious behaviours, then use principal component analysis to extract features of these sensitive system calls, and finally adopt multi-layers neural networks to classify the features of malware variants and legitimate ones. Theoretical analysis and real-life experimental results show that our packed malware variants detection technique is comparable with the the state-of-art methods in terms of accuracy. Our approach can achieve more than 95.6\% of detection accuracy and 0.048 s of classification time cost.

## 메모


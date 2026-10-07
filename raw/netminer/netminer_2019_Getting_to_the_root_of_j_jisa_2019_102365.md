---
title: "Getting to the root of the problem: A detailed comparison of kernel and user level data for dynamic malware analysis"
authors: ['Matthew Nunes', 'Pete Burnap', 'Omer Rana', 'Philipp Reinecke', 'Kaelon Lloyd']
year: 2019
publication_date: 2019-08-20
venue: "Journal of Information Security and Applications"
publisher: "Elsevier BV"
volume: "48"
issue: "None"
pages: "102365-102365"
doi: "https://doi.org/10.1016/j.jisa.2019.102365"
openalex_id: "https://openalex.org/W2969940084"
cited_by_count: 23
fwci: 1.2492
tags: ['Advanced Malware Detection Techniques', 'Network Security and Intrusion Detection', 'Digital and Cyber Forensics']
keywords: ['Computer science', 'Machine learning', 'Malware', 'Artificial intelligence', 'Random forest', 'System call', 'Data mining', 'Computer security']
source: openalex-netminer
---

# Getting to the root of the problem: A detailed comparison of kernel and user level data for dynamic malware analysis

**저자**: Matthew Nunes; Pete Burnap; Omer Rana; Philipp Reinecke; Kaelon Lloyd
**출처**: Journal of Information Security and Applications, Vol.48, pp.102365-102365
**발행일**: 2019-08-20
**DOI**: https://doi.org/10.1016/j.jisa.2019.102365

## 초록

Dynamic malware analysis is fast gaining popularity over static analysis since it is not easily defeated by evasion tactics such as obfuscation and polymorphism. During dynamic analysis it is common practice to capture the system calls that are made to better understand the behaviour of malware. There are several techniques to capture system calls, the most popular of which is a user-level hook. To study the effects of collecting system calls at different privilege levels and viewpoints, we collected data at a process-specific user-level using a virtualised sandbox environment and a system-wide kernel-level using a custom-built kernel driver. We then tested the performance of several state-of-the-art machine learning classifiers on the data. Random Forest was the best performing classifier with an accuracy of 95.2% for the kernel driver and 94.0% at a user-level. The combination of user and kernel level data gave the best classification results with an accuracy of 96.0% for Random Forest. This may seem intuitive but was hitherto not empirically demonstrated. Additionally, we observed that machine learning algorithms trained on data from the user-level tended to use the anti-debug/anti-vm features in malware to distinguish it from benignware. Whereas, when trained on data from our kernel driver, machine learning algorithms seemed to use the differences in the general behaviour of the system to make their prediction, which explains why they complement each other so well. Our results show that capturing data at different privilege levels will affect the classifier’s ability to detect malware, with kernel-level providing more utility than user-level for malware classification. Despite this, there exist more established user-level tools than kernel-level tools, suggesting more research effort should be directed at kernel-level. In short, this paper provides the first objective, evidence-based comparison of user and kernel level data for the purposes of malware classification.

## 메모


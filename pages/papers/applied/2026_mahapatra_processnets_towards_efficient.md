---
title: "ProcessNets: Towards an efficient approach for ensemble analysis of biological networks"
authors: ['Sugyani Mahapatra', 'Manikandan Narayanan']
year: 2026
venue: "bioRxiv (Cold Spring Harbor Laboratory)"
tags: ['Bioinformatics and Genomic Networks', 'Single-cell and spatial transcriptomics', 'Gene Regulatory Network Analysis']
source: raw/applied/applied_2026_ProcessNets_Towards_an_ef_2026_09_22_753520.md
---

# ProcessNets: Towards an efficient approach for ensemble analysis of biological networks

**저자**: Sugyani Mahapatra; Manikandan Narayanan
**출처**: bioRxiv (Cold Spring Harbor Laboratory), Vol.None
**발행일**: 2026-09-28
**DOI**: https://doi.org/10.64898/2026.09.22.753520

## 초록 (원문)

Integrative analysis of the properties of multiple networks pertaining to a biological system is a key problem in systems biology. But computing the properties of thousands of large networks poses a challenge. Most techniques that partially address this challenge, such as parallelism and optimized algorithms, treat the analysis of each network as an independent task. However, the networks arising from the same biological system are often similar to each other, and can we harness this similarity to achieve speedup? Towards this end, we propose a phylogeny-like data structure, nc-tree, to compactly represent an ensemble of related biological networks; and a versatile framework, ProcessNets, that runs incremental algorithms over the nc-tree to speedup property computations on the input networks. Our asymptotic analysis of space and time complexity, coupled with empirical evaluations of diverse ensembles of simulated and real-world GTEx gene coexpression networks, demonstrate that ProcessNets leads to significant space and time advantages when computing different network science measures on ensembles of similar networks. For instance, we achieve a compression factor of 2.1x and 8.1x in storing two representative ensembles of GTEx Muscle Skeletal networks with 1000 nodes/genes, and a time speedup of 2.86x to 3.97x over the fastest baseline for computing degree centrality in ensembles of networks with at least 14,500 nodes derived from subsampled GTEx datasets of ten tissues. These results are promising and encourage application of ProcessNets to analyze biological network ensembles derived from rapidly accumulating consortium/biobank-based datasets.

## 키워드



## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


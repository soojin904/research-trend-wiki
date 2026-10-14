---
title: "Cooperation as Routing: A Network-Layer Formalization of How Help Propagates Through Social Networks"
authors: ['kazutaka hayashi']
year: 2026
venue: ""
tags: ['Complex Network Analysis Techniques', 'Multi-Agent Systems and Negotiation', 'Opportunistic and Delay-Tolerant Networks']
source: raw/applied/applied_2026_Cooperation_as_Routing_A__ukmpn_v2.md
---

# Cooperation as Routing: A Network-Layer Formalization of How Help Propagates Through Social Networks

**저자**: kazutaka hayashi
**출처**: , Vol.None
**발행일**: 2026-10-10
**DOI**: https://doi.org/10.31235/osf.io/ukmpn_v2

## 초록 (원문)

Most models of how things spread on social networks are broadcast models: a statereaches whoever is reachable, and the analysis asks how far it spread. Cooperation oftendoes not spread this way. A request for help has no xed recipient; a person who receivesit either helps or, unable to help, passes it toward someone who can. Repeated, this for-warding carries the request across the network hop by hop, much as a packet is routedtoward a host it has never met. Classical work on decentralized search established thatsuch address-free messages can reach a target through local decisions, and that chains diemainly because intermediaries stop. We formalize the decision layer of this process: help-requests are packets, participants are nodes, and each node facing a request acknowledgesit, forwards it, does both, or drops it. We dene an eective forward as one whose nexthop itself acts, and show that crediting only eective forwards, to the immediate previoushop only, rewards every intermediary on a successful path without backward propagation,rewards routing quality rather than volume, and gives no reward for acting in isolation. Wespecify the provenance records needed to measure these quantities and illustrate, on thelog of an operating mutual-aid platform, how chains that reached four hops could not bereconstructed because provenance was missing at the second hop. We discuss implicationsfor cooperative multi-agent systems and for instrumenting platforms that route help.

## 키워드

social networks, decentralized search, routing, provenance, cooperative multi-agent systems

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


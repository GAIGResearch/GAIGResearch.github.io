---
layout: post
categories: Publications
tags: ["pubs-2018", gvgai, general-video-game-playing, optimisation, evo-star, mcts]
paper: true
hidden: true

pubid: sironi2018mctsGVGP
type: inproceedings
title: Self-adaptive MCTS for General Video Game Playing
author: Chiara F. Sironi and Jialin Liu and Diego Perez-Liebana and Raluca D. Gaina and Ivan Bravi and Simon M. Lucas and Mark H. M. Winands
booktitle: Applications of Evolutionary Computation
year: 2018
pages: 358--375
editor: Kevin Sim and Paul Kaufmann
publisher: Springer International Publishing
address: Cham
isbn: 978-3-319-77538-8
abstract:  Monte-Carlo Tree Search (MCTS) has shown particular success in General Game Playing (GGP) and General Video Game Playing (GVGP) and many enhancements and variants have been developed. Recently, an on-line adaptive parameter tuning mechanism for MCTS agents has been proposed that almost achieves the same performance as off-line tuning in GGP. In this paper we apply the same approach to GVGP and use the popular General Video Game AI (GVGAI) framework, in which the time allowed to make a decision is only 40ms. We design three Self-Adaptive MCTS (SA-MCTS) agents that optimize on-line the parameters of a standard non-Self-Adaptive MCTS agent of GVGAI. The three agents select the parameter values using Naïve Monte-Carlo, an Evolutionary Algorithm and an N-Tuple Bandit Evolutionary Algorithm respectively, and are tested on 20 single-player games of GVGAI. The SA-MCTS agents achieve more robust results on the tested games. With the same time setting, they perform similarly to the baseline standard MCTS agent in the games for which the baseline agent performs well, and significantly improve the win rate in the games for which the baseline agent performs poorly. As validation, we also test the performance of non-Self-Adaptive MCTS instances that use the most sampled parameter settings during the on-line tuning of each of the three SA-MCTS agents for each game. Results show that these parameter settings improve the win rate on the games Wait for Breakfast and Escape by 4 times and 150 times, respectively.
puburl: https://link.springer.com/chapter/10.1007/978-3-319-77538-8_25
venue: evostar

---

* content
{:toc}


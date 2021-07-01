---
layout: post
categories: Publications
tags: ["pubs-2019", ieee-cog, forward-model-learning]
paper: true
hidden: true

pubid: dockhorn2019unforgiving
type: inproceedings
title: Learning Local Forward Models on Unforgiving Games
author: Alexander Dockhorn and Simon M Lucas and Vanessa Volz and Ivan Bravi and Raluca D. Gaina and Diego Perez-Liebana
booktitle: IEEE Conference on Games (COG)
year: 2019
pages: 1--4
doi: 10.1109/CIG.2019.8848044
puburl: https://ieeexplore.ieee.org/document/8848044
abstract: This paper examines learning approaches for forward models based on local cell transition function. We provide a formal definition of local forward models for which we propose two learning approaches. Our analysis is based on the game Sokoban, where a wrong action can lead to an unsolvable game state. Therefore, an accurate prediction of an  action's resulting state is necessary to avoid this scenario. In contrast to learning the complete state transition function, local forward models allow extracting multiple training examples from a single state transition. In this way, the Hash Set model, as well as the Decision Tree model, quickly learn to predict upcoming state transitions of both the training and the test set. Applying the model using a statistical forward planner showed that the best models can be used to satisfying degree even in cases in which the test levels have not yet been seen. Our evaluation includes an analysis of various local neighbourhood patterns and sizes to test the learners' capabilities in case too few or too many attributes are extracted, of which the latter has shown do degrade the performance of the model learner.   
venue: ieee cog

---

* content
{:toc}


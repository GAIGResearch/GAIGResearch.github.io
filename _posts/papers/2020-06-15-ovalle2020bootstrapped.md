---
layout: post
categories: Publications
tags: ["pubs-2020", ieee-cog, reinforcement-learning, rhea]
paper: true
hidden: true

pubid: ovalle2020bootstrapped
type: inproceedings
author: Ovalle, Alvaro and Lucas, Simon M
title: "Bootstrapped model learning and error correction for planning with uncertainty in model-based RL"
booktitle: "IEEE Conference on Games (CoG)"
year: 2020
pages: 495--502
puburl: "https://ieeexplore.ieee.org/document/9231599"
abstract: "Having access to a forward model enables the use of planning algorithms such as Monte Carlo Tree Search and Rolling Horizon Evolution. Where a model is unavailable, a natural aim is to learn a model that reflects accurately the dynamics of the environment. In many situations it might not be possible and minimal glitches in the model may lead to poor performance and failure. This paper explores the problem of model misspecification through uncertainty-aware reinforcement learning agents. We propose a bootstrapped multi-headed neural network that learns the distribution of future states and rewards. We experiment with a number of schemes to extract the most likely predictions. Moreover, we also introduce a global error correction filter that applies high-level constraints guided by the context provided through the predictive distribution. We illustrate our approach on Minipacman. The evaluation demonstrates that when dealing with imperfect models, our methods exhibit increased performance and stability, both in terms of model accuracy and in its use within a planning algorithm."
venue: ieee cog

---

* content
{:toc}


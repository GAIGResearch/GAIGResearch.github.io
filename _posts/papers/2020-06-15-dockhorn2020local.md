---
layout: post
categories: Publications
tags: ["pubs-2020", ieee-cog, forward-model-learning, general-video-game-playing, gvgai]
paper: true
hidden: true

pubid: dockhorn2020local
type: inproceedings
author: Dockhorn, Alexander and Lucas, Simon
title: "Local Forward Model Learning for GVGAI Games"
booktitle: "IEEE Conference on Games (CoG)"
year: 2020
pages: 716--723
abstract: "In this paper, we are going to explain the design process for our GVGAI game-learning agent, which is going to be submitted to the GVGAI competition's learning track 2020. The agent relies on a local forward modeling approach, which uses predictions of future game-states to allow the application of simulation-based search algorithms. We first explain our process in identifying repeating tiles throughout a pixel-based state observation. Using the tile information, a local forward model is trained to predict the future state of each tile based on its current state and its surrounding tiles. We accompany this approach with a simple reward model, which determines the expected reward of a predicted state transition. The proposed approach has been tested using multiple games of the GVGAI framework. Results show that the approach seems to be especially feasible for learning how to play deterministic games. Except for one non-deterministic game, the agent performance is very similar to agents using the true forward model. Nevertheless, the prediction accuracy needs to be further improved to facilitate a better game-playing performance."
venue: ieee cog

---

* content
{:toc}


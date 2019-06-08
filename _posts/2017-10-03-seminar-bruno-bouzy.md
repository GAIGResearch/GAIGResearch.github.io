---
layout: post
title:  "[Seminar] 'Computer Hanabi: Playing Near-Optimally or Learning by Reinforcement ?' by Dr. Bruno Bouzy"
categories: Seminar
tags: [seminar, hanabi, game-playing, reinforcement-learning]
excerpt: "Dr. Bruno Bouzy, Associate Professor,  Laboratory of Informatics Paris Descartes (LIPADE), Université Paris Descartes, Paris, France. Time and date: 4pm, 17th October 2017 (Tuesday). Title: Computer Hanabi: Playing Near-Optimally or Learning by Reinforcement ? Room: Eng3.24, Engineering Building, QMUL"
mathjax: false
---

* content
{:toc}

* **Title**: Computer Hanabi: Playing Near-Optimally or Learning by Reinforcement ?
* **Speaker**: Dr. Bruno Bouzy, Associate Professor,  Laboratory of Informatics Paris Descartes (LIPADE), Université Paris Descartes, Paris, France.
* **Time and date**: 4pm, 17th October 2017 (Tuesday)
* **Room**: Eng3.24, Engineering Building, QMUL

[[Presentation Slides](https://www.dropbox.com/s/8tuzq602n5x8nfd/Bouzy-QMUL-17october2017.pdf?dl=0)]

[Free registration](https://www.eventbrite.co.uk/e/seminar-computer-hanabi-playing-near-optimally-or-learning-by-reinforcement-tickets-38432819598?utm-medium=discovery&utm-campaign=social&utm-content=attendeeshare&aff=escb&utm-source=cp&utm-term=listing) will be highly appreciated as it will be helpful for booking refreshment.
Refreshment will be served before and after the seminar (3:30pm and 5:05pm) in the hub of Bancroft Road Teaching Rooms, 10, Godward Square, Queen Mary University of London, London E1 4FZ

## Abstract

Hanabi is a multi-player cooperative card game in which a player sees the cards of the other players but not his own cards. The team of players aims at maximizing a score. After a brief presentation of the rules of the game, this talk will describe two sets of experiments. The first one is an exploitation experiment (how to play as well as possible ?) and the second one explores some pros and cons of the reinforcement learning approach.

The first part will describe computer players corresponding to the state-of-the-art in computer Hanabi. Particularly, we will describe players using the hat principle and depth-one search. The hat principle is well-known in recreational mathematics and gives amazing results on the game of Hanabi, resulting in scores that are almost perfect.

In front of this, the new trend about deep learning led us to perform a second set of experiments to build reinforcement learners using neural networks – not necessarily deep – as function approximators. Hanabi being an incomplete information game, the preliminary results with self-play and shallow neural networks show that the game of Hanabi is a hard game to tackle with a learning approach. We will present our results and discuss the features of the game of Hanabi such as the number of players, the number of cards per player, the possibility to play with open cards or not, the problem of learning a convention, that make this game a good opportunity to test many techniques of reinforcement learning: with TD learning or with Q learning, the use of a replay memory or not, the number of layers in the network, and tuning considerations on the gradient descent.

## Bio
Born in Paris (France), Bruno Bouzy is Assistant Professor of Computer Science in the Department of Mathematics and Computer Science at the Paris Descartes University since 1997, and in the Laboratory of Informatics of PAris DEscartes (LIPADE) since its creation in 2005. His academic degrees include two engineering school diplomas (Ecole Polytechnique 1984, Ecole Nationale Supérieure des Techniques Avancées, 1986), a Ph.D. in Computer Science (1995) and an Habilitation for Research Supervising in Computer Science (2004). Between 1986 and 1991, he held a consulting engineer position with GSI, a leading software advisory company. Bruno Bouzy is the author of the Go playing program Indigo which won three bronze medals at the computer olympiads: two on 19×19 board (2004, 2006), and one on 9×9 board (2005). These achievements resulted from using the Monte-Carlo (MC) approach for the first time in a competitive Go playing program: playing out simulations until the end, and computing action values with the outcomes of the simulations. After these promising results, the Computer Go community adopted the MC approach, and the Monte-carlo Tree Search (MCTS) framework was created in 2006, and became the standard approach for many games. Since 2007, Bruno Bouzy took a step back from Computer Go – all Go playing progams were MCTS based programs – and moved to other interesting and difficult challenges such as Multi-Agent Learning (2008-2010), the game of Amazons (2004-2010), the Voronoi game (2009-2011), Cooperative Path-Finding (2012-now), the game of Hex (2013), the Rubik’s cube (2014), the weak Schur problem (2014-2015), the Pancake problem (2015-2016). Today, the incomplete information games remaining hard obstacles for Artificial Intelligence, Bruno Bouzy works on the game of Hanabi, a cooperative card game. Practically, to obtain results as good as possible in all these domains, Bruno Bouzy uses various methods such as Game Theory, Heuristic Search, MCTS, Neural Networks, Reinforcement Learning, and domain dependent tools as well.
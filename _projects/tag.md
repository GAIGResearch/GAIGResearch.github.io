---
layout: project
permalink: /projects/TAG
title: "TAG: A Tabletop Games Framework"
short-title: TAG
img: /img/proj/MoBoGDL.jpg
year: 2020
members: [Raluca-Gaina, Martin-Balla, Diego-Perez-Liebana, Raul-Montoliu, Alexander-Dockhorn]
target: https://github.com/GAIGResearch/TabletopGames
description: A flexible framework for tabletop games and AI players.
---

# About

Tabletop games come in a variety of forms, including board games, card games, and dice games. In recent years, their complexity has considerably increased, with many components, rules that change dynamically through the game, diverse player roles, and a series of control parameters that influence a game's balance. As such, they also encompass novel and intricate challenges for Artificial Intelligence methods, yet research largely focuses on classical board games such as _chess_ and _Go_. We introduce in this work the Tabletop Games (TAG) framework, which promotes research into general AI in modern tabletop games, facilitating the implementation of new games and AI players, while providing analytics to capture the complexities of the challenges proposed. 

# Getting started

In order to run the code, you must either download the repository, or clone it. If you are looking for a particular release, you can find all listed [here](https://github.com/GAIGResearch/TabletopGames/releases). Java version 8 or higher is required.

The simplest way to run the code is to create a new project in [IntelliJ IDEA](https://www.jetbrains.com/idea/) or a similar IDE. In IntelliJ, create a **new project from existing sources**, pointing to the code downloaded or cloned and selecting the Maven framework for import. This process should automatically set up the environment and add any project libraries as well.

Alternatively, open the code directly in your IDE of choice, right click the pom.xml file and setup the project with the Maven framework. Make sure `src/main/java` is marked as sources root.

To get started, the [wiki](https://github.com/GAIGResearch/TabletopGames/wiki) provides various guides and descriptions of the framework.
Another good resource is our continuously updated paper "DESIGN AND IMPLEMENTATION OF TAG: A TABLETOP GAMES FRAMEWORK".

## Games
Currently implemented games:
- [x] Tic-Tac-Toe
- [x] Love Letter (Seiji Kanai 2012)
- [x] Uno (Merle Robbins 1971)
- [x] Virus! (Cabrero and others 2015)
- [x] Exploding Kittens (Inman and others 2015)
- [x] Colt Express (Christophe Raimbault 2014)
- [x] Pandemic (Matt Leacock 2008)

Games in progress:
- [ ] Settlers of Catan (Klaus Teuber 1995)
- [ ] Carcassone (Klaus-Jürgen Wrede 2000)
- [ ] Descent (Jesper Ejsing, John Goodenough, Frank Walls 2005)

# Associated research

* Raluca D. Gaina, Martin Balla, Alexander Dockhorn, Raul Montoliu, Diego Perez-Liebana, **"TAG: A Tabletop Games Framework"**, in _Experimental AI in Games (EXAG), AIIDE 2020 Workshop_, 2020.
* Raluca D. Gaina, Martin Balla, Alexander Dockhorn, Raul Montoliu, Diego Perez-Liebana, **"Design and Implemenation of TAG: A Tabletop Games Framework"**, in _arXiv 2009.12065_, 2020.
---
layout: post
title:  "GAIG @ QMUL EECS Research Week 2020"
categories: Event
tags: [qmul, events, gaig]
excerpt: "PhD students and academic staff from the Game AI group showcase their research at the QMUL EECS Research Week 2020.<br/>
<b>When</b>: November 24th, 11am-12pm<br/>
<b>Where</b>: <a href='https://www.eventbrite.co.uk/e/eecs-research-week-2020-tickets-121513719807'>Online! (register here)</a><br/>
<b>Speakers:</b> <a href='/members/Paulo-Rauber'>Paulo Rauber</a>, <a href='/members/Raluca-Gaina'>Raluca D. Gaina</a>, <a href='/members/Simon-Colton'>Simon Colton</a>, <a href='/members/Mike-Cook'>Mike Cook</a>, <a href='/members/Diego-Perez-Liebana'>Diego Perez-Liebana</a>, <a href='/members/Alvaro-Ovalle'>Alvaro Ovalle</a>, <a href='/members/Vanessa-Volz'>Vanessa Volz</a>, <a href='/members/Ivan-Bravi'>Ivan Bravi</a>, <a href='/members/Simon-Lucas'>Simon Lucas</a><br/>
Full details on: <a href='http://eecs.qmul.ac.uk/research/eecs-research-week-2020/'>http://eecs.qmul.ac.uk/research/eecs-research-week-2020/</a>"
mathjax: false
img: /img/posts/game-Ai.png
---

* content
{:toc}

PhD students and academic staff from the Game AI group showcase their research at the QMUL EECS Research Week 2020.<br/>
<b>When</b>: November 24th, 11am-12pm<br/>
<b>Where</b>: <a href="https://www.eventbrite.co.uk/e/eecs-research-week-2020-tickets-121513719807">Online! (register here)</a><br/>
<b>Speakers:</b> [Paulo Rauber](/members/Paulo-Rauber), [Raluca D. Gaina](/members/Raluca-Gaina), [Simon Colton](/members/Simon-Colton), [Mike Cook](/members/Mike-Cook), [Diego Perez-Liebana](/members/Diego-Perez-Liebana), [Alvaro Ovalle](/members/Alvaro-Ovalle), [Vanessa Volz](/members/Vanessa-Volz), [Ivan Bravi](/members/Ivan-Bravi), [Simon Lucas](/members/Simon-Lucas)<br/>
Full details on: [http://eecs.qmul.ac.uk/research/eecs-research-week-2020/](http://eecs.qmul.ac.uk/research/eecs-research-week-2020/)

<hr/>

The Game AI Research Group was founded in 2017 and has already comprises 10 academic staff and 25 PhD students and post-docs.  We use games both as a test-bed for the most challenging problems in AI, and as an important application game.  Much of our AI is based on very general statistical forward planning algorithms such as Rolling Horizon Evolution and Monte Carlo Tree Search.  We apply this to a range of challenging games, both for bot AI and to automatically generate and blend novel games and game content.  We work closely with a range of industry and government partners, and increasingly apply our AI to more complex games and real-world decision-making problems.  We are proud to co-host the IGGI (Intelligent Games and Game Intelligence) CDT, training more than 120 PhD students in games and Game AI.

As a group we contribute strongly to the Game AI research community, and play major roles in the main conferences such as IEEE Conference on Games, Foundation of Digital Games, and AI and Interactive Digital Entertainment (AIIDE), as well as the leading journal in the area, the IEEE Transactions on Games.

Welcome to our webinar, where you’ll find 10 talks that give a rough idea of what we do: read our papers and talk to us to find out more!

## [Paulo Rauber](/members/Paulo-Rauber), "Recurrent Neural-Linear Posterior Sampling for Non-Stationary Contextual Bandits"

An agent in a non-stationary contextual bandit problem should balance between exploration and the exploitation of (periodic or structured) patterns present in its previous experiences. Handcrafting an appropriate historical context is an attractive alternative to transform a non-stationary problem into a stationary problem that can be solved efficiently. However, even a carefully designed historical context may introduce spurious relationships or lack a convenient representation of crucial information. In order to address these issues, we propose an approach that learns to represent the relevant context for a decision based solely on the raw history of interactions between the agent and the environment. This approach relies on a combination of features extracted by recurrent neural networks with a contextual linear bandit algorithm based on posterior sampling. Our experiments on a diverse selection of contextual and non-contextual non-stationary problems show that our recurrent approach consistently outperforms its feedforward counterpart, which requires handcrafted historical contexts, while being more widely applicable than conventional non-stationary bandit algorithms.

## [Raluca D. Gaina](/members/Raluca-Gaina), "Artificial Intelligence in Modern Tabletop Games"

Tabletop games come in a variety of forms, including board, card, role-playing and dice games. In recent years, their complexity has increased considerably, with many components, rules that change throughout the game, diverse player roles, and many other aspects that can influence a game's balance. As a result, modern tabletop games also create new and interesting challenges for Artificial Intelligence methods, yet current research largely focuses on classical board games, such as chess and Go. This talk introduces the [Tabletop Games (TAG) project](/projects/TAG), which instead looks into adaptive and immediately applicable general AI in modern tabletop games. The TAG system already includes a subset of games such as Colt Express, Exploding Kittens and Pandemic, as well as AI players capable of playing them all to some degree of proficiency. It also allows for easy development of new games and artificial players, complete with analytics that capture the complexities of the challenges proposed.

## [Simon Colton](/members/Simon-Colton), "Casual Creators Apps for Fun Creativity Support"

It's been possible for decades for people to use computers to make interesting art, music and games.

However, only in recent years has attention been paid to how to design creativity support apps that are - above anything else - fun to use. In the talk, I will describe some design and technical issues that arise in building such casual creators for general use, drawing on my experiences in developing the Wevva game design app and the Art Done Quick casual creator for visual art.

## [Mike Cook](/members/Mike-Cook), TBC

TBC

## [Diego Perez-Liebana](/members/Diego-Perez-Liebana), "General Strategy Games Framework"

Strategy games are complex environments often used in AI-research to evaluate new algorithms. Despite the commonalities of most strategy games, often research is focused on one game only, which may lead to bias or overfitting to a particular environment. In this talk, we motivate and present a general strategy games framework for playing n-player turn-based and real-time strategy games. Our benchmark, which allows an easy customization of games via YAML-files, exposes an API with access to a forward model to facilitate research on statistical forward planning agents, as well as logging functionality for analyzing, debugging and understanding how algorithms reason in these complex environments.

## [Alvaro Ovalle](/members/Alvaro-Ovalle), "Open issues in learning and planning with forward models"

Having a predictive forward model of the world confers an agent multiple advantages such as better generalization or the possibility of anticipating future consequences. However, acquiring and then planning over a learned model also comes with many challenges. In this talk, we present recent research trying to tackle two of them. The first case study considers a strategy for planning with inaccurate models. Via ensemble methods, the agent aggregates and performs error-correction on its predictions leading to more robust behavior. The second example deals with the scenario of planning without reward functions. We present a self-supervised planning approach based on active inference, which allows us to replace the notion of reward as utility, with that of maximizing model evidence in belief-spaces.

## [Vanessa Volz](/members/Vanessa-Volz), "Data-Driven Representations for Game Level Evaluation"

Game levels are complex artifacts, and different players enjoy them for different reasons. Some might enjoy puzzle-solving aspects, others having to prove their quick reaction skills. In some cases, however, even the player cannot explain the reasons for their enjoyment. Learning representations with data-driven methods is one approach to automatically characterise levels, that also allows for comparisons between them. In this talk, I will present a vision of how data-driven representations for game levels can help evaluate and compare them.

## [Ivan Bravi](/members/Ivan-Bravi), "You'd better behave! - A general approach to behavioural exploration in games"

Evaluating the design of a game is a very complex task, playtesting is the primary tool for getting feedback from the players. This process is expensive and time consuming, grouping and analysing the feedback is complex and not free from bias. Using AI has the potential of speeding up the process, providing an unbiased and thorough quantitative analysis. This talk will present how to improve the ability of AI player to explore the behavioural space of a game.

## [Simon Lucas](/members/Simon-Lucas), "Hierarchical Planning in Games"

Statistical Forward Planning algorithms such as Monte Carlo Tree Search and Rolling Horizon Evolution often perform amazingly well across a range of games, and can be further boosted by learning value functions or heuristics to help guide the search.  However, in some cases the action-space of a game is low-level and requires long sequences on order to achieve meaningful effects, causing particular difficulties when the reward landscape is flat.  In these cases a solution is to form plans in a higher level or macro action space.  In this talk I’ll present our latest work on automatically constructing macro-actions using a variety of state observation filters, subgoal predicates, and search procedures.

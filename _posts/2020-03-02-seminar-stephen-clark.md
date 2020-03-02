---
layout: post
title:  "[Seminar] 'Grounded Language Learning in Virtual Environments' by Stephen Clark"
categories: Seminar
tags: [seminar, virtual environments, nlp]
excerpt: "<ul>
<li><b>Title:</b> Grounded Language Learning in Virtual Environments</li>
<li><b>Speaker:</b> Stephen Clark, Research Scientist at DeepMind, and an Honorary Professor at Queen Mary University of London</li> 
<li><b>Time and date:</b> 12pm to 1pm, March 4th, 2020 (Wednesday)</li>
<li><b>Room:</b> 3.02, Bancroft Road Teaching Rooms, Mile End campus</li>
</ul>"
mathjax: false
---

* content
{:toc}

<ul>
<li><b>Title:</b> Grounded Language Learning in Virtual Environments</li>
<li><b>Speaker:</b> Stephen Clark, Research Scientist at DeepMind, and an Honorary Professor at Queen Mary University of London</li> 
<li><b>Time and date:</b> 12pm to 1pm, March 4th, 2020 (Wednesday)</li>
<li><b>Room:</b> 3.02, Bancroft Road Teaching Rooms, Mile End campus</li>
</ul>

(preceded by tea and coffee - in the Informatics Hub)
All welcome (especially students), no pre-booking required 

## Abstract

 Natural Language Processing is currently dominated by the application of text-based language models such as BERT and GPT-2. One feature of these models is that they rely entirely on the statistics of text, without making any connection to the world, which raises the interesting question of whether such models could ever properly "understand" the language. One way in which these models can be "grounded" is to connect them to images or videos, for example by conditioning the language models on visual input and using them for captioning.
 
In this talk I extend the grounding idea to a simulated virtual world: an environment which an agent can perceive and interact with. More specifically, a neural-network-based agent is trained - using distributed deep reinforcement learning - to associate words and phrases with things that it learns to see and do in the virtual world.

The world is 3D, built in Unity, and contains recognisable objects, including some from the ShapeNet repository of assets.

One of the difficulties in training such networks is that they have a tendency to overfit to their training data, so first I'll show how the interactive, first-person perspective of an agent provides it with a particular inductive bias that helps it to generalize to out-of-distribution settings. Another difficulty is providing the agent with enough linguistic experience so that it can learn to handle the variety and noise in natural language. One way to increase the agent's linguistic knowledge is to provide it with BERT embeddings, and I'll show how an agent endowed with BERT representations can achieve substantial (zero-shot) transfer from template-based language to noisy natural instructions given by humans with access to the agent's world. Joint work with Felix Hill.

## Bio

Stephen Clark is a Research Scientist at DeepMind, and an Honorary Professor at Queen Mary University of London. Previously he spent 18 years working at UK universities, first as a postdoctoral researcher at the University of Edinburgh; then as a member of Faculty at the Oxford University Department of Computer Science, and a Fellow of Keble College, Oxford; and finally as a member of Faculty at the University of Cambridge Department of Computer Science and Technology. He holds a PhD in Computer Science and Artificial Intelligence from the University of Sussex, and an MA in Philosophy from Gonville and Caius College, Cambridge. He carries out research at the intersection of Computational Linguistics and Machine Learning, and in Artificial Intelligence more broadly, with much of his previous work focusing on the syntactic and semantic analysis of natural language text. His current research focus is the acquisition of language by artificial agents in the context of realistic virtual environments.

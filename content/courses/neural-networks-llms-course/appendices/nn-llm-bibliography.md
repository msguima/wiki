---
title: "Bibliography and Paper Map — Neural Networks and Language Models"
type: course-appendix
course: nn-llm-syllabus
modified: 2026-09-19
---

# Bibliography and Paper Map

The single place where identifiers live for
[[nn-llm-syllabus|the neural-networks course]]. A weekly note cites through
this page and never from memory.

The existing identifiers were imported from the companion notes. The six
records for the linearized-learning supplement were checked against arXiv on
2026-09-19 and linked below. An identifier check establishes the reference
metadata; it does not independently validate every claim in the paper.

---

## Unit 0 — Language as a statistical system

| Work | Identifier | Used in |
|---|---|---|
| Shannon, *A Mathematical Theory of Communication* (1948) | journal | Week 1 |
| Shannon, *Prediction and Entropy of Printed English* (1951) | journal | Week 2 |
| Lin and Tegmark, *Critical Behavior in Physics and Probabilistic Formal Languages* (2017) | journal | Week 2 |
| Gage, *A New Algorithm for Data Compression* (1994) | journal | Week 2 |
| Sennrich, Haddow and Birch, *Neural Machine Translation of Rare Words with Subword Units* (2016) | [arXiv:1508.07909](https://arxiv.org/abs/1508.07909) | Week 2 |

## Unit 1 — Networks as many-body systems

| Work | Identifier | Used in |
|---|---|---|
| Cover, *Geometrical and Statistical Properties of Systems of Linear Inequalities* (1965) | journal | Week 3 |
| Gardner, *The Space of Interactions in Neural Network Models* (1988) | journal | Week 4 |
| Gardner and Derrida (1988) | journal | Week 4 |
| Engel and Van den Broeck, *Statistical Mechanics of Learning* (2001) | book | Weeks 3–4 |
| Mézard, Parisi and Virasoro, *Spin Glass Theory and Beyond* (1987) | book | Week 4 |
| Hopfield (1982) | journal | Week 5 |
| Amit, Gutfreund and Sompolinsky (1985, 1987) | journal | Week 5 |
| Krotov and Hopfield, *Dense Associative Memory* (2016) | [arXiv:1606.01164](https://arxiv.org/abs/1606.01164) | Week 6 |
| Demircigil and collaborators (2017) | journal | Week 6 |
| Ramsauer and collaborators, *Hopfield Networks is All You Need* (2021) | [arXiv:2008.02217](https://arxiv.org/abs/2008.02217) | Week 6 |
| Lucibello and Mézard (2024) | journal | Week 6 |
| Hoover and collaborators, *Energy Transformer* (2023) | [arXiv:2302.07253](https://arxiv.org/abs/2302.07253) | Week 6 |
| Krotov, *A New Frontier for Hopfield Networks* (2023) | journal | Week 6, further reading |
| Krotov and collaborators, *Modern Methods in Associative Memory* (2025) | [arXiv:2507.06211](https://arxiv.org/abs/2507.06211) | Week 6, further reading |

### The linearized regime and the interpolation peak

Optional study after Weeks 3–4: [[nn-llm-linearized-learning]]. No lecture hours assigned.

| Work | Identifier | Note |
|---|---|---|
| Jacot, Gabriel and Hongler, *Neural Tangent Kernel* (NeurIPS 2018) | [arXiv:1806.07572](https://arxiv.org/abs/1806.07572) | |
| Chizat, Oyallon and Bach, *On Lazy Training in Differentiable Programming* (NeurIPS 2019) | [arXiv:1812.07956](https://arxiv.org/abs/1812.07956) | |
| Belkin, Hsu, Ma and Mandal, *Reconciling Modern Machine-Learning Practice and the Classical Bias–Variance Trade-off* (PNAS 116, 2019) | [arXiv:1812.11118](https://arxiv.org/abs/1812.11118) | |
| Hastie, Montanari, Rosset and Tibshirani, *Surprises in High-Dimensional Ridgeless Least Squares Interpolation* (Ann. Statist., 2022) | [arXiv:1903.08560](https://arxiv.org/abs/1903.08560) | the asymptotics used in the text |
| Mei and Montanari, *The Generalization Error of Random Features Regression* (CPAM, 2022) | [arXiv:1908.05355](https://arxiv.org/abs/1908.05355) | |
| Advani, Saxe and Sompolinsky, *High-dimensional dynamics of generalization error in neural networks* (Neural Networks, 2020) | [arXiv:1710.03667](https://arxiv.org/abs/1710.03667) | |
| Negri and collaborators, *Storage and Learning Phase Transitions in the Random-Features Hopfield Model* (2023) | journal | the bridge to Unit 1's memory half |
| Bahri and collaborators, *Statistical Mechanics of Deep Learning* (Annu. Rev. Condens. Matter Phys. 11, 2020) | journal | survey |
| Roberts, Yaida and Hanin, *The Principles of Deep Learning Theory* (2022) | [arXiv:2106.10165](https://arxiv.org/abs/2106.10165) | book |

## Unit 2 — Building the transformer

| Work | Identifier | Used in |
|---|---|---|
| Vaswani and collaborators, *Attention Is All You Need* (2017) | [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) | Weeks 7–8 |
| Su and collaborators, *RoFormer* (rotary position embeddings) | [arXiv:2104.09864](https://arxiv.org/abs/2104.09864) | Week 7 |
| Ba, Kiros and Hinton, *Layer Normalization* | [arXiv:1607.06450](https://arxiv.org/abs/1607.06450) | Week 8 |
| He and collaborators, *Deep Residual Learning* | [arXiv:1512.03385](https://arxiv.org/abs/1512.03385) | Week 9 |
| Chen and collaborators, *Neural Ordinary Differential Equations* | [arXiv:1806.07366](https://arxiv.org/abs/1806.07366) | Week 9 |
| Dehghani and collaborators, *Universal Transformers* | [arXiv:1807.03819](https://arxiv.org/abs/1807.03819) | Week 9 |
| Fan and collaborators, *Addressing Some Limitations of Transformers with Feedback Memory* | [arXiv:2002.09402](https://arxiv.org/abs/2002.09402) | Week 9 |
| Geiping and collaborators, recurrent-depth language model (2025) | [arXiv:2502.05171](https://arxiv.org/abs/2502.05171) | Week 9 |
| Zhang, *Recurrent Looped Transformer* technical note | *(technical note; read 2026-09-13)* | Week 9 |
| Mandt, Hoffman and Blei, stochastic gradient descent as approximate inference | [arXiv:1704.04289](https://arxiv.org/abs/1704.04289) | Week 10 |
| Radford and collaborators, *Language Models are Unsupervised Multitask Learners* (2019) | institutional report | Weeks 11–13 laboratories |

## Unit 3 — Physics of what emerged

| Work | Identifier | Used in |
|---|---|---|
| Geshkovski and collaborators, interacting-particle view of transformers | [arXiv:2312.10794](https://arxiv.org/abs/2312.10794) | Week 11 |
| Dong, Cordonnier and Loukas, *Pure Attention Loses Rank Doubly Exponentially with Depth* | [arXiv:2103.03404](https://arxiv.org/abs/2103.03404) | Week 11 |
| Rende, Gerace, Laio and Goldt, factored attention and the inverse Potts problem | [arXiv:2304.07235](https://arxiv.org/abs/2304.07235) | Week 12 |
| Cui and collaborators, positional–semantic transition in a solvable attention model | [arXiv:2402.03902](https://arxiv.org/abs/2402.03902) | Week 12 |
| Zhai and collaborators, attention entropy and training instability | [arXiv:2303.06296](https://arxiv.org/abs/2303.06296) | Week 13 |
| Kaplan and collaborators, scaling laws | [arXiv:2001.08361](https://arxiv.org/abs/2001.08361) | Week 13 |
| Hoffmann and collaborators, compute-optimal training | [arXiv:2203.15556](https://arxiv.org/abs/2203.15556) | Week 13 |
| Power and collaborators, grokking | [arXiv:2201.02177](https://arxiv.org/abs/2201.02177) | Week 13 |
| Schaeffer, Miranda and Koyejo, on emergent abilities and the choice of metric | [arXiv:2304.15004](https://arxiv.org/abs/2304.15004) | Week 13 |

## Unit 4 — Diffusion and non-equilibrium thermodynamics

| Work | Identifier | Used in |
|---|---|---|
| Sohl-Dickstein and collaborators, *Deep Unsupervised Learning using Nonequilibrium Thermodynamics* | [arXiv:1503.03585](https://arxiv.org/abs/1503.03585) | Week 14 |
| Ho, Jain and Abbeel, *Denoising Diffusion Probabilistic Models* | [arXiv:2006.11239](https://arxiv.org/abs/2006.11239) | Week 14 |
| Song and collaborators, score-based generative modelling through SDEs | [arXiv:2011.13456](https://arxiv.org/abs/2011.13456) | Week 14 |
| Jarzynski, *Nonequilibrium Equality for Free Energy Differences* | [arXiv:cond-mat/9610209](https://arxiv.org/abs/cond-mat/9610209) | Week 14 |

## Background texts

| Work | Identifier |
|---|---|
| Mehta and collaborators, *A high-bias, low-variance introduction to machine learning for physicists* | journal |
| Prince, *Understanding Deep Learning* (2023) | book |

---

## Maintenance

The six formerly pending arXiv identifiers for the optional learning
supplement are now linked. Other journal and book entries retain their
imported metadata and have not received a complete independent bibliographic
audit in this revision. The companion repository's bibliography is maintained
separately and was not edited by this wiki revision.

## Related

- [[nn-llm-syllabus]], [[nn-llm-week-map]], nn-llm-note-quality-template

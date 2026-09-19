---
title: "Neural networks and LLMs — Reading and experiments"
type: course-resources
course: nn-llm-syllabus
status: draft
modified: 2026-09-19
---

# Reading and experiments

Begin with [[nn-llm-start-here]] for the conceptual route or
[[nn-llm-week-map]] for the semester sequence. The weekly wiki pages contain
the calculations needed to follow their main argument. The longer notes add
proof details, exercises and laboratory protocols.

## The companion notes

[Open the local PDF](file:///Users/marcelo/Projects/courses/fisica-redes-neurais-llms/main.pdf).
The notes are *Statistical Physics of Neural Networks and Language Models*;
weekly Reading sections identify the relevant chapter. The
[versioned source](https://github.com/msguima/courses/tree/main/fisica-redes-neurais-llms)
is in the companion courses repository. The local PDF reflects the last local
build; it is not a separately published wiki release.

The local links on this page require the companion checkout at the path shown.
They are ordinary file links, intended for a local Markdown/Obsidian reader.
A browser or reader that blocks file links can open that same file through its
Open command. On another computer, locate the corresponding files in the
companion checkout. No public hosted PDF is assumed.

## Small experiments, with no installation

[Open the experiment index](file:///Users/marcelo/Projects/courses/fisica-redes-neurais-llms/experiments/index.html).
Keep this HTML file alongside its existing scripts. Each experiment runs in a
browser; no Python or account is needed.

| Experiment | What to do first | Reading |
|---|---|---|
| [Fit a binary distribution](file:///Users/marcelo/Projects/courses/fisica-redes-neurais-llms/experiments/index.html#fit) | Predict the fitted probability for three positive observations and one negative observation; then change the field. | [[week-01-inferring-a-distribution\|Week 1]] |
| [Two-state Markov source](file:///Users/marcelo/Projects/courses/fisica-redes-neurais-llms/experiments/index.html#markov) | Vary the switching probability; compare entropy rate with correlation length. | [[week-02-transfer-matrix-and-finite-text\|Week 2]] |
| [Hopfield retrieval](file:///Users/marcelo/Projects/courses/fisica-redes-neurais-llms/experiments/index.html#hopfield) | Corrupt one spin and compute its local field before updating. | [[week-05-hopfield-and-capacity\|Week 5]] |
| [Continuous memory](file:///Users/marcelo/Projects/courses/fisica-redes-neurais-llms/experiments/index.html#memory) | Compare the slope of $\tanh(\beta x)$ at the origin with one. | [[week-06-attention-from-an-energy\|Week 6]] |
| [Internal recurrence](file:///Users/marcelo/Projects/courses/fisica-redes-neurais-llms/experiments/recurrence.html) | Hold the input fixed and repeat the same state update. | [[week-09-four-indices\|Week 9]] |

These five small experiments are available now. The longer semester laboratories
have protocols in the notes; their implementation and classroom testing remain
separate work. A protocol is not a claim that a full laboratory is ready.

## Reading the integrated wiki

Open `/Users/marcelo/Projects/physics-wiki` as the Obsidian vault. The course
folder alone does not include the other courses and concept pages to which it
links. This is a reading instruction; this revision does not change vault
settings. Use Reading view to see equations, tables and figures.

- [[wiki/courses/2026-algebraic-qft-course/syllabus|Algebraic QFT course]]:
  compare classical relative entropy in Week 1 with
  [[araki-uhlmann-relative-entropy]] and [[relative-entropy-qft]]. The finite
  probability calculation remains sufficient for this course.
- [[wiki/courses/ads-cft-course/syllabus|Gauge/gravity course]]:
  [[replica-trick-gravity]] supplies a comparison of replica constructions
  after Week 4. It is an optional connection, not a prerequisite.
- [[wiki/courses/generalized-symmetries-course/syllabus|Generalized symmetries course]]:
  [[kramers-wannier-duality]] connects to the transfer-matrix perspective of
  Week 2.

These three syllabus links include their paths because the existing pages
share the filename `syllabus.md`. The qualified targets remove the ambiguity
without renaming pages in other courses.

References: [[nn-llm-bibliography]]. Notation: [[nn-llm-conventions]].

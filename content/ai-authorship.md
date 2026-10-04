---
title: "Authorship of this wiki"
type: course-standard
modified: 2026-10-04
---

# Authorship of this Wiki

This wiki was written by AI assistants working under the scientific and
pedagogical supervision of Marcelo S. Guimarães. That holds for all of it:
the concept pages, the paper notes, the open questions, the area and project
pages, and the graduate courses with their syllabi, weekly notes, skeletons,
conventions and appendices. This page records which models did the writing,
and states what the supervision does and does not certify.

The arrangement is the one declared in the wiki's own playbook: the
researcher curates sources and directs the analysis, and the AI writes and
maintains the pages. This page exists so that a reader of the published wiki
is told so directly, rather than having to infer it.

---

## Division of labour

Marcelo sets the research direction, defines each course's aims, audience and
teaching approach, selects the primary literature, evaluates the material as
it develops, and directs its revision. The assistants write the prose, carry out and check the
derivations, build the worked examples and exercises, and maintain the
cross-references.

Writing and scientific review are continuous. **The attribution does not
imply that every argument on these pages has been independently verified.**
Each weekly course note carries its own proof-status labels, and those labels
describe what is on the page rather than what is known to be true; the
note-quality template of each course is the binding standard for them. The
research notes carry no such labels, and a claim on one of them should be
read as a working summary of the literature it cites.

---

## Which models wrote what

The historical entries below follow co-authorship trailers in this
repository. Commit counts belong to those historical entries; the current
NN/LLM revision is recorded explicitly without attributing a new commit. Note
that the trailer record is partial: of the 146 commits in the repository, 100
carry one, and the April 2026 commit that seeded the wiki's pages carries
none. The counts therefore understate the earliest work.

| Course | Models | Period |
|---|---|---|
| Estrutura Algébrica da Teoria Quântica de Campos<br>`2026-algebraic-qft-course` | Claude Opus 4.7 (14 commits), Claude Opus 4.8 (2), Claude Opus 5 (2) | 2026-05-08 → 2026-08-23 |
| Holography through Quantum Information and Operator Algebras<br>`ads-cft-course` | GPT Astra 6 (redesign, 32 notes); Claude Opus 5.5 (Lectures 8–32 rewritten, with independent audits) | 2026-09-29 → 2026-10-01 |
| Generalized Symmetries and Topological Matter<br>`generalized-symmetries-course` | Claude Opus 5.5 (7 commits in the `courses` repository: Semester I rewritten and Semester II written, with independent verification passes) | 2026-09-28 → 2026-10-03 |
| Statistical Physics of Neural Networks and Language Models<br>`neural-networks-llms-course` | Claude Opus 5 (initial wiki draft); Codex (OpenAI, pedagogical revision) | 2026-09-19 → |
| Research notes<br>`concepts`, `areas`, `connections`, `papers`, `projects`, `questions`, `entities` | Claude Opus 4.8 (7 commits), Claude Opus 5 (2), Claude Opus 4.6 (2), Claude Fable 5 (1) | 2026-04-06 → 2026-09-19 |

The Claude models are from Anthropic; Codex is from OpenAI. Where a course draws on material prepared
outside this wiki, the outside material carries its own disclosure; see the
next section.

---

## Material prepared outside this wiki

The holography course is carried from Marcelo's `courses` repository. Its first
version, the redesign of 2026-09-29 around information and operator algebras,
was written by GPT Astra 6; Claude Opus 5.5 then rewrote Lectures 8–32 to the
AQFT course's standard between 2026-09-29 and 2026-10-01, each block followed by
an independent audit, and the commits there carry the trailers. On 2026-10-01 it
replaced the earlier CFT-first course of this wiki, *Gauge/Gravity Duality:
Foundations and Black-Hole Information*, written by Claude Opus 4.7 (35 commits),
Claude Sonnet 4.6 (5) and Claude Opus 5 (2) between 2026-05-26 and 2026-08-25,
which remains in the repository history.

The generalized-symmetries course is also carried from the `courses` repository.
Claude Opus 5.5 reviewed it against the AQFT course's standard on 2026-09-27,
rewrote the fifteen Semester I notes and wrote the fifteen Semester II notes
between 2026-09-28 and 2026-10-03, each block followed by an independent
verification pass, and the commits there carry the trailers. On 2026-10-04 it
replaced the earlier copy of this wiki, written by Claude Opus 4.8 (5 commits)
and Claude Fable 5 (3) between 2026-07-05 and 2026-07-10, which remains in the
repository history.

The neural-networks course has both a wiki reading route and printable lecture
notes maintained in Marcelo's `courses` repository. The printable notes were
written by **Codex (OpenAI)** and **Claude (Anthropic)** under the same
supervision, with their disclosure on the title page and in the preface.
Their revision records identify the assistants involved.

The wiki's pedagogical revision of 2026-09-19 was carried out by **Codex
(OpenAI)** at Marcelo's request. The wiki now includes local definitions,
essential calculations and answered checkpoints so it can be read on its own.
The book supplies longer treatments and exercises. Differences between the
formats require checking the argument and recording the correction; neither
format settles correctness by authority. The revised pages remain drafts
pending the instructor's review. See [[nn-llm-start-here]] and
[[nn-llm-resources]].

---

## Related

- [[overview|The research landscape]], which summarizes what the wiki covers
- The wiki's assistant playbook, which states the general arrangement and is
  kept in the private repository these pages are generated from

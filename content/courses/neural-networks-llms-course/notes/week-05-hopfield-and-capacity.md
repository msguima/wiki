---
title: "Week 5 — Hopfield dynamics and the meaning of a capacity"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 5
unit: 1
duration: "4 hours (2 hr lecture + 2 hr laboratory)"
status: draft
modified: 2026-09-19
---

# Week 5 — Hopfield Dynamics and the Meaning of a Capacity

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 1. Written by an AI assistant under the researcher's supervision; see ai-authorship.*

*Weeks 3 and 4 varied the weights with the data fixed. This week does the
opposite: the couplings are built once from the stored patterns and then held,
and it is the state that moves. The change is easy to state and easy to lose
sight of, and half the confusions about associative memory come from losing
it. The week ends with a capacity that is a different number for a different
question, and with the reasons the two numbers do not compete.*

---

## Learning goals

1. Recover a stored pattern from a corrupted cue by hand, and state which
   objects are fixed and which evolve.
2. **Prove** that the Hopfield energy decreases at every actual flip, and
   identify every hypothesis the proof uses.
3. Decompose the local field into signal and interference and say what the
   interference does at extensive load.
4. Interpret $\alpha_c \simeq 0.138$ together with the retrieval criterion and
   the ansatz that produce it.

## Reading

**Primary text.** Chapter 2, §2.6 and §2.7, with the four-spin worked example
and the asymmetric three-spin exercise.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]:
Hopfield (1982); Amit, Gutfreund and Sompolinsky (1985, 1987).

**Prerequisites.** [[week-04-gardner-capacity|Week 4]] for the replica
vocabulary; the retrieval equations here are quoted with their ansatz stated
and are not re-derived.

## 1. From a corrupted cue to a stored pattern

An **associative memory** reconstructs a stored pattern from an incomplete or
corrupted cue. Let the stored patterns be $\xi^\mu\in\{-1,+1\}^N$,
$\mu=1,\ldots,P$, and define the symmetric **Hebb couplings** once:

$$
J_{ij}=\frac1N\sum_{\mu=1}^P\xi_i^\mu\xi_j^\mu\quad(i\ne j),\qquad J_{ii}=0.
$$

The evolving state is $s\in\{-1,+1\}^N$. Its local field and energy are

$$
h_i=\sum_jJ_{ij}s_j,\qquad E(s)=-\frac12\sum_{i,j}J_{ij}s_is_j.
$$

At each step choose one site and replace $s_i$ by $\operatorname{sign}h_i$;
if $h_i=0$, leave it unchanged. This is **asynchronous updating**. A fair
schedule eventually visits every site. Couplings remain fixed throughout
recall. This differs from training, which changes weights.

### Four spins, with all fields visible

Store only $\xi=(1,1,-1,-1)$, and start at $s=(-1,1,-1,-1)$. The
**overlap** $m=N^{-1}\sum_i\xi_is_i$ measures agreement: $m=1$ is exact
retrieval, while initially $m=1/2$. Since there is only one pattern,

$$
h_i=\xi_i m-\frac{s_i}{4},\qquad
 h=(3/4,1/4,-1/4,-1/4).
$$

Only the first spin opposes its field. Flipping it restores $\xi$.
Completing the sum in the energy gives

$$
E=-\frac N2m^2+\frac12.
$$

It changes from $0$ to $-3/2$. The overlap changes from $1/2$ to $1$.
Updating any other site first leaves this particular cue unchanged.
The [[nn-llm-resources|Hopfield browser experiment]] implements this example.

## 2. Why the energy decreases, and what the proof needs

With symmetric couplings and zero diagonal, collect all terms involving
site $i$ as $-s_ih_i$. Replacing $s_i$ by $s_i'$ gives

$$
\Delta E=-(s_i'-s_i)h_i.
$$

For a flip $s_i'=-s_i$, this is $2s_ih_i$. A flip occurs only when the old value opposes a nonzero field, so
every actual flip lowers the energy by $2|h_i|$.

The configuration space is finite. Strict decrease prevents any configuration
recurring after a flip, so fair asynchronous updating reaches a fixed point.
The energy is a **Lyapunov function** for the dynamics.

Four hypotheses carry this argument.
Symmetry of the couplings, so the quadratic form's site-$i$ terms collect.
Zero diagonal, so a site does not act on itself. The **asynchronous** rule —
updating all spins at once is a different dynamics and does not inherit the
proof. And the tie convention at $h_i = 0$: nonincrease alone would permit
motion at constant energy, and the strictness is what rules it out.

> **Physical picture.** This is the standard termination argument and worth
> naming as such: a strictly decreasing function on a finite state space
> cannot cycle, so the dynamics halts. What it does *not* say is where. A fixed
> point is stable against single-spin changes, and need not be a global
> minimum; and the set of cues flowing to a given fixed point — its **basin of
> attraction** — is a separate object that the proof says nothing about.
> Successful memory needs suitable basins as well as suitable fixed points,
> and the laboratory measures exactly that gap.

## 3. Signal, interference, and extensive load

For a single stored pattern the field decomposes into the overlap times the
pattern, minus a finite-$N$ self-term from the zero diagonal, as in the
four-spin calculation above. For several patterns define $m_\mu=N^{-1}\sum_j\xi_j^\mu s_j$.
Direct substitution gives

$$
h_i=\xi_i^1m_1+\sum_{\mu=2}^P\xi_i^\mu m_\mu-\frac PN s_i.
$$

The first term is the target signal, the sum is **crosstalk** from the other
patterns, and the last term removes the diagonal interactions. This formula
is exact. Treating the crosstalk as independent Gaussian noise is a further
approximation.

At fixed $P$ and large $N$ the non-retrieved overlaps are typically of order
$N^{-1/2}$ and the crosstalk is negligible. At **extensive load**, $P = \alpha
N$, the summed fluctuations stay of order one, and the interference competes
with the signal. That is the regime the capacity question lives in.

> **Physical picture.** The natural first move is a signal-to-noise estimate:
> treat the crosstalk as a Gaussian of variance $\alpha$ and ask when it flips
> a bit. The book does exactly that as an exercise and gets a capacity scaling
> like $N/\log N$ for the demand that *every* bit of a pattern be stable. What
> the estimate omits is feedback — the flipped bits change the state, which
> changes the interference — and the replica treatment exists to put that
> feedback back in. The difference between the naive estimate and the full
> answer is not a detail: it is the difference between a sum of independent
> random signs and a self-consistent one.

## 4. What $0.138$ means

Amit, Gutfreund and Sompolinsky studied the extensive-load problem for
independent random binary patterns. The book quotes their zero-temperature
replica-symmetric retrieval equations with the ansatz stated, and does not
re-derive them: the effective field is the signal plus a Gaussian of variance
$\alpha r$, averaging its sign gives the overlap self-consistently, and a
response relation with a feedback factor closes the system.

Here are the quoted zero-temperature replica-symmetric equations, so the
number can be reproduced. Let $m$ be the target overlap, $r$ the amplification
of crosstalk variance and $U$ the response factor:

$$
m=\operatorname{erf}\!\left(\frac{m}{\sqrt{2\alpha r}}\right),\qquad
 U=\sqrt{\frac{2}{\pi\alpha r}}e^{-m^2/(2\alpha r)},\qquad
 r=(1-U)^{-2}.
$$

These relations are a replica-symmetric ansatz, not the exact finite-$N$
local update. Put $y=m/\sqrt{2\alpha r}$ and eliminate $m,r,U$ to obtain

$$
\alpha(y)=\frac{[\operatorname{erf}y-(2y/\sqrt\pi)e^{-y^2}]^2}{2y^2},
\qquad m(y)=\operatorname{erf}y.
$$

The retrieval branch terminates at the maximum of this curve,
$\alpha_c^{\rm RS} \simeq 0.138$. The overlap there is still about $0.97$: the
branch does not degrade smoothly to zero, it ceases to exist.

Every word of the following qualification is doing work. The number refers to
the **replica-symmetric**, **thermodynamic-limit**, **Hebbian** retrieval
problem with **independent random binary patterns** and a
**macroscopic-overlap** success criterion. It is a *spinodal* — the point at
which the retrieval branch stops existing — and not automatically the point
at which retrieval loses global equilibrium stability, which would require
comparing free energies.

> **Physical picture.** There is no contradiction with the perceptron's
> $\alpha_c = 2$, and seeing why is the point of the week. The perceptron
> question is whether *some* weight vector satisfies random classification
> constraints — an optimization over couplings, with the couplings free. The
> Hopfield question fixes the couplings by a particular prescription, the Hebb
> rule, and asks about the attractors of the dynamics that prescription
> produces. Optimizing the couplings instead changes the storage problem, and
> constraints such as symmetry and a required basin of attraction cannot be
> dropped when transferring a bound between the two. Different question,
> different construction, different number.

## Checkpoints with answers

**1. Which object moves during recall?** The spin configuration $s$.
The stored patterns and the couplings computed from them remain fixed.

**2. What proves termination of the stated rule?** Each actual flip strictly
lowers energy, there are finitely many configurations, and zero-field spins
are left unchanged. A fair schedule eventually reaches a state with no
allowed energy-lowering flip.

**3. Does a final low energy prove retrieval?** No. Compute the overlap with
the intended pattern. Other local minima can have small target overlap even
when every spin agrees with its field.

---

## Subtleties and fine print

**Low energy is not retrieval.** A spin-glass state can have frozen local
values and negligible overlap with any stored pattern. Energy descent is a
termination certificate, not a retrieval certificate, and the laboratory must
therefore state an overlap threshold for success in advance.

**Asymmetric couplings break the proof, and can cycle.** The book's three-spin
exercise exhibits a periodic orbit under repeated sweeps. The example shows
possibility, not inevitability: it does not prove every asymmetric system
cycles, nor that none admits some other Lyapunov function.

**Synchronous updating is a different dynamics.** It does not inherit the
descent proof, and its fixed points and cycles are a separate question.

**At zero temperature the freezing parameter does not identify retrieval.**
$q_{\rm EA}$ alone does not distinguish a retrieved frozen state from any
other frozen state; the pattern overlap is what does.

**A finite-size experiment will not reproduce $0.138$ exactly, and should not
be forced to.** The number is a thermodynamic-limit statement about a
particular criterion. A protocol with its own corruption fraction, update
schedule and success threshold has its own threshold, and reporting the
difference honestly is the deliverable.

---

## Key claims and status

| Claim | Status |
|---|---|
| $\Delta E = -2\lvert h_i\rvert$ at every actual flip | [Exact], for symmetric couplings, zero diagonal, asynchronous rule, stated tie convention |
| Fair asynchronous updating reaches a fixed point | [Exact], from strict decrease on a finite state space |
| Single-pattern field and energy from completing the sums | [Exact.] |
| Crosstalk decomposition of the field around a target | [Exact.] |
| Non-retrieved overlaps of order $N^{-1/2}$ at fixed $P$ | [Exact] as a typical statement |
| Gaussian signal-to-noise capacity scaling like $N/\log N$ for exact stability | [Controlled approximation]; neglects feedback correlations |
| $\alpha_c^{\rm RS}\simeq0.138$, overlap $\simeq0.97$ at the branch end | [Replica-symmetric], thermodynamic limit, Hebbian, random binary patterns |
| A cycle exists for the stated asymmetric three-spin coupling | [Exact] for that example |

---

## What the week establishes

1. The Hopfield energy falls at every actual flip, and the dynamics therefore
   terminates — with four hypotheses, each shown to be load-bearing.
2. The local field decomposes exactly into signal, crosstalk and a finite-$N$
   self-term, and the crosstalk becomes competitive precisely at extensive
   load.
3. A retrieval branch exists up to $\alpha_c^{\rm RS}\simeq0.138$ and
   terminates there discontinuously in the overlap, under the stated ansatz
   and criterion.
4. The perceptron and Hopfield capacities answer different questions, and the
   reason is structural rather than numerical.

**What to carry forward.** A capacity is a number attached to a question, and
quoting it without the question attached is the most common way to misuse the
results of this unit. Week 6 will produce a third capacity scale, larger than
both of these, and the first thing to ask about it is what resource it counts.

## The practical session — Laboratory 2

**Varied:** the number of stored patterns $P$, at several system sizes $N$;
and the cue corruption fraction.
**Held fixed:** the pattern ensemble, the zero-field tie rule, the update
schedule, and the overlap threshold used to call a run successful — all
declared before the runs, not after.
**Measured:** the final overlap with the target, the retrieval frequency over
repeated pattern draws and cues, and the energy.

**Product:** retrieval frequency against $\alpha$ at each $N$, with the success
criterion stated; a comparison of the size dependence with what a
replica-symmetric thermodynamic-limit result actually claims; and an explicit
statement that the protocol's threshold is not required to equal $0.138$.

Begin by reproducing the four-spin example and its energy change by hand. A
laboratory that cannot reproduce the exactly solvable case should not be
trusted on the extensive one.

---

## Connections to other parts of the wiki

- [[week-04-gardner-capacity|Week 4]] asks the feasibility question with the
  couplings free; this week fixes them by a prescription and asks about
  attractors.
- [[week-06-attention-from-an-energy|Week 6]] generalizes the energy, raising
  the capacity scale, and then derives the attention operation from a
  continuous version of the same construction.
- The Lyapunov argument of §2 returns in Week 9, where a driven version of the
  same inequality is shown *not* to give a common decreasing energy.
- nn-llm-unit-1 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-04-gardner-capacity|Previous week]] · [[week-06-attention-from-an-energy|Next week]]

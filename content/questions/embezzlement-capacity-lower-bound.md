---
title: Is the holographic embezzlement rate optimal? (the capacity lower bound)
type: question
status: open
areas:
  - bell-inequalities-qft
  - relative-entropy-qft
  - gauge-gravity-duality
priority: high
originated: 2026-06-05
modified: 2026-06-05
---

## Statement

The manuscript *Generalized Entropy as the Capacity for Holographic Entanglement Embezzlement* (see [[holographic-dual-embezzlement-protocol]]) proves a **conditional achievability** bound: in a finite sector of the crossed product of logarithmic trace volume $\mathcal C$ (with a left–right mirror realization), a $d$-dimensional maximally entangled target can be extracted with infidelity

$$1 - F_d \;\le\; C_d\,\frac{\log d}{\mathcal C}.$$

The open question is the **matching lower bound**:

$$1 - F_d \;\ge\; c_d\,\frac{\log d}{\mathcal C}$$

for every protocol in the finite-sector class, for fixed $d$ and large $\mathcal C$.

This is the difference between a *bound* and a *capacity*. The upper bound says $\mathcal C$ (hence, under $\mathcal C \simeq S_{\text{gen}}$, the generalized entropy) **suffices** to embezzle at this rate. Only the lower bound says it is **necessary** — i.e. that $S_{\text{gen}}$ *is* the operational capacity. The manuscript title claims the latter; the body currently proves only the former. Closing this gap is what earns the title.

## Why It Matters

- It converts the paper's contribution from "a generalized-entropy bound on holographic embezzlement" into a genuine **operational characterization of $S_{\text{gen}}$** — a new meaning distinct from RT/FLM (entanglement entropy), Wall (the GSL), and CLPW/CPW (entropy of the dressed algebra). None of those tie $S_{\text{gen}}$ to the *rate of a task*; this would.
- It is the part least exposed to being scooped by the algebraic-holography insiders (Witten/Liu/CPW), because it requires one-shot / smooth-entropy quantum-information machinery closer to the group's idiom than to theirs.
- It is a natural thesis result for ismael-porfirio or erick-landim.

## What We Know

**The problem reduces to a gravity-free spectral statement.** Embezzling a $d$-dimensional *maximally entangled* target forces the catalyst Schmidt spectrum $\{p_n\}$ to be approximately invariant under the $d$-fold block stretch $n \mapsto (m,r)$ with $n = d(m-1)+r+1$. In the logarithmic coordinate $s = \log n$ this is approximate invariance under the translation $s \mapsto s - \log d$. So the lower bound is exactly:

> A probability distribution supported on a log-window of width $\mathcal C$ cannot be invariant under a $\log d$ translation to better than $O(\log d/\mathcal C)$ in fidelity.

No gravity enters this statement; the holographic content is entirely in the separate identification $\mathcal C \simeq S_{\text{gen}}$.

**Finite-dimensional anchors.** The optimality/uniqueness of slowly varying embezzling families in finite dimensions is established by Leung–Wang (Phys. Rev. A 90, 042331, 2014) and, more completely, by Zanoni–Theurer–Gour (*Complete Characterization of Entanglement Embezzlement*, Quantum 8, 1368, 2024). These characterize which Schmidt tails are admissible and single out the van Dam–Hayden family — exactly the input needed to control the smooth-tail case below.

**The continuum picture already in the manuscript** ($\S$4): for a state flat in $s$ over $[0,L]$, a translation by $\Delta$ has overlap $(L-\Delta)/L$, giving $1-F \le 2\Delta/L$ with $\Delta_d = \log d$. The lower bound must run this *as a variational lower bound over all admissible spectra*, not just for the flat profile.

## Possible Approaches

**Primary route — sharp-cutoff / bounded-tail sectors (expected to be provable):**

1. **Reduce to Hellinger distance.** Standard embezzlement bookkeeping (Leung–Wang; Zanoni–Theurer–Gour) gives $\sqrt{F_d} \le \sum_n \sqrt{p_n\,p'_n}$, where $p'$ is the $d$-fold reindexed (log-shifted) spectrum. Hence $1 - F_d \ge \tfrac12\,\|\sqrt{p} - \sqrt{p'}\|^2$ — the squared Hellinger distance between a distribution and its $\log d$ log-translate.
2. **Forced boundary leakage.** If $p$ is supported on $s \in [0,\mathcal C]$, the shift $p'$ lives on $[\log d, \mathcal C + \log d]$; the support mismatch has log-measure $\sim 2\log d$ out of $\mathcal C$, and any normalized $p$ must place fidelity weight $\gtrsim \log d/\mathcal C$ in the mismatch region.
3. **Variational optimization.** Minimize the Hellinger mismatch over admissible $p$ at fixed support width $\mathcal C$ and shift $\log d$. The minimizer is the near-flat-in-$s$ (van Dam–Hayden) profile, with mismatch $\Theta(\log d/\mathcal C)$ — matching the upper bound and fixing $c_d$.

**Where it breaks — and the honest scope.** Step 2 uses a hard support cutoff. For a **smooth wavepacket** (e.g. Gaussian tails in $s$) there is no sharp boundary and the translation overlap can decay faster, so the naive bound is evadable. This is exactly why Zanoni–Theurer–Gour matters: it constrains which tails are admissible. The provable theorem is therefore conditional on a **regularity / cutoff class** for the sector — which is physically the right class, because the holographic sector has *finite trace volume* set by $S_{\text{gen}}$ (a genuine cutoff). Honest statement of the target: *within the finite-trace-window class, the rate $\log d/\mathcal C$ is optimal.*

**Recommended order of work:** first pin down the precise regularity class on the sector that makes the bound tight (what "finite-trace-window" must mean for the variational argument to close), then push steps 1–3 to a rigorous inequality with an explicit $c_d$. Getting the hypothesis right is what makes the proof go through cleanly.

**Tooling.** Smooth max-entropy / smooth support-trace methods from one-shot quantum information (Tomamichel; Hayden–Penington alpha-bit) are the natural formal language for the finite-trace-window cutoff and for lifting from finite type-I regulators to the type II$_\infty$ algebra.

## Related Questions

- [[holographic-dual-embezzlement-protocol]] — the umbrella project page; this is its single most important open sub-question.
- [[embezzlement-cost-relative-entropy]] — the original group-internal cost question; the lower bound is the sharp-rate refinement of it.
- [[bell-chsh-in-holographic-setting]] — shares the Type III₁ / modular-flow toolkit; relevant to the Q4 "Bell × embezzlement" follow-up once the capacity result is in hand.

## Notes

- Reduction and strategy worked out in discussion 2026-06-05 (with the assistant).
- Key external anchors: Zanoni–Theurer–Gour (Quantum 8, 1368, 2024, arXiv:2303.17749); Leung–Wang (PRA 90, 042331, 2014); Tomamichel (arXiv:1203.2142); Hayden–Penington (CMP 374, 369, 2020).

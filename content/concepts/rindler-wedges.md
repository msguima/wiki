---
title: Rindler Wedges
type: concept
areas: [bell-inequalities-qft, relative-entropy-qft]
aliases: [Rindler wedge, Rindler region, right Rindler wedge, left Rindler wedge]
modified: 2026-04-06
---

## Definition

In $(d+1)$-dimensional Minkowski spacetime with coordinates $(x^0, x^1, \ldots, x^d)$, the **right Rindler wedge** is

$$R = \{x \in \mathbb{R}^{d+1} : x^1 > |x^0|\},$$

and the **left Rindler wedge** is

$$L = \{x \in \mathbb{R}^{d+1} : x^1 < -|x^0|\}.$$

$R$ and $L$ are **causally complementary**: no causal curve connects $R$ to $L$. They are each other's causal complement in the sense that $L = (R')'$ where the prime denotes the spacelike complement.

Each wedge is preserved under **Lorentz boosts** in the $x^1$-direction: $x^0 \mapsto x^0\cosh\theta + x^1\sinh\theta$, $x^1 \mapsto x^0\sinh\theta + x^1\cosh\theta$. An observer uniformly accelerating in the $x^1$-direction with proper acceleration $a$ follows the trajectory

$$x^\mu(\tau) = \frac{1}{a}(\sinh(a\tau), \cosh(a\tau), 0, \ldots, 0),$$

which remains inside $R$ for all proper time $\tau$.

The **Unruh effect**: the Minkowski vacuum $|0\rangle$, restricted to the right Rindler wedge algebra $\mathcal{M}(R)$, is a **KMS (thermal) state** at the Unruh temperature

$$T_U = \frac{a}{2\pi},$$

where $a$ is the proper acceleration (in natural units $\hbar = c = k_B = 1$). Algebraically, this follows from the Bisognano-Wichmann theorem: the modular flow of $\mathcal{M}(R)$ with respect to the Minkowski vacuum is precisely the boost automorphism.

## Role in Research

Rindler wedges are the standard setting for the [[bell-chsh-inequality|Bell-CHSH]] inequality program. The bipartite split is Alice = right wedge $R$, Bob = left wedge $L$. Since $R$ and $L$ are spacelike separated, the locality assumption of Bell's theorem is automatically satisfied by microcausality.

The systematic framework (Phys. Rev. D 108, 085026; 2023) places Alice's [[weyl-operators|Weyl operators]] $W(f)$ with $\text{supp}(f) \subset R$ and obtains Bob's operators via [[tomita-takesaki-modular-theory|modular conjugation]] $J$: $JW(f)J \in \mathcal{M}(L)$. The Bisognano-Wichmann identification makes $J$ a geometric operation (CPT + boost), giving a physically transparent construction.

The Unruh-De Witt detector paper (JHEP 2024, 6 citations) bridges the abstract algebraic Rindler picture with a detector model, computing Bell correlations from the perspective of the accelerated observer.

The [[relative-entropy-qft]] line computes the [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] between the vacuum and excited states restricted to $R$, accessing information about the entanglement structure of the vacuum across the $R/L$ split.

## Relations

- [[causal-diamonds]] — compact alternative to Rindler wedges; diamonds are finite-size and more physically realistic, but the same algebraic machinery applies
- [[tomita-takesaki-modular-theory]] — the Bisognano-Wichmann theorem identifies the modular flow of $\mathcal{M}(R)$ with boost automorphisms; modular conjugation $J$ maps $\mathcal{M}(R) \to \mathcal{M}(L)$
- [[bell-chsh-inequality]] — Rindler wedges provide the bipartite causal split for QFT Bell tests
- [[weyl-operators]] — Weyl operators localized in $R$ generate $\mathcal{M}(R)$; support of test function determines wedge localization
- [[type-iii-von-neumann-algebras]] — $\mathcal{M}(R)$ is a type III₁ von Neumann algebra; the vacuum is cyclic and separating for this algebra
- [[araki-uhlmann-relative-entropy]] — relative entropy between states restricted to $R$ quantifies information lost when tracing over $L$

## Papers

See [[bell-inequalities-qft]] and [[relative-entropy-qft]] for full paper lists.

## Notes

- The Rindler wedge is an example of a globally hyperbolic spacetime in its own right; one can quantize fields directly in Rindler coordinates (Rindler quantization), obtaining Rindler particles related to Minkowski particles by a Bogoliubov transformation.
- The thermal nature of the Minkowski vacuum restricted to $R$ is exact (not perturbative) and model-independent, following purely from the algebraic structure and the wedge geometry.
- Common confusion: the Unruh effect does not mean that Minkowski vacuum becomes a thermal state globally — it is thermal only when restricted to $R$ (or equivalently, only for observables measured by the accelerated observer).
- Rindler wedges are non-compact; this is both a mathematical advantage (clean algebraic structure) and a physical limitation (no real experiment is confined to a half-space). [[causal-diamonds|Causal diamonds]] address the compactness issue.

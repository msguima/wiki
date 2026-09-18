---
title: Causal Diamonds
type: concept
areas: [bell-inequalities-qft, relative-entropy-qft]
aliases: [causal diamond, double cone, diamond region]
modified: 2026-04-06
---

## Definition

Given two points $p$ and $q$ in Minkowski spacetime (or more generally a globally hyperbolic spacetime) with $q$ in the causal future of $p$, the **causal diamond** (also called double cone or diamond region) is

$$\mathcal{D}(p,q) = J^+(p) \cap J^-(q),$$

where $J^+(p)$ is the causal future of $p$ (the set of all points reachable from $p$ by future-directed causal curves) and $J^-(q)$ is the causal past of $q$.

Equivalently, for a spatial ball $B_r$ of radius $r$ centered at the origin in $t=0$ slice, the causal diamond $\mathcal{D}(B_r)$ is the **domain of dependence** of $B_r$: the set of all points $x$ such that every inextendible causal curve through $x$ intersects $B_r$. In coordinates:

$$\mathcal{D}(B_r) = \{(t,\mathbf{x}) : |\mathbf{x}| + |t| < r\}.$$

This is a **compact** region, in contrast to the non-compact [[rindler-wedges|Rindler wedge]].

The local von Neumann algebra $\mathcal{M}(\mathcal{D})$ associated to a causal diamond is a [[type-iii-von-neumann-algebras|type III₁]] factor in any reasonable QFT (assuming the Haag-Kastler axioms), and the vacuum is cyclic and separating for it. In conformal field theories, the modular Hamiltonian for the diamond algebra is known explicitly:

$$K = 2\pi \int_{B_r} \frac{r^2 - |\mathbf{x}|^2}{2r}\,T_{tt}(\mathbf{x})\,d^{d-1}x,$$

a result due to Casini, Huerta, and Myers.

## Role in Research

Causal diamonds extend the Rindler-wedge Bell inequality program to compact, physically realistic regions. The paper Eur. Phys. J. C 85, 2025 establishes Bell-CHSH violation for the free scalar field vacuum in a bipartite diamond setup, complementing the original Rindler results.

The compactness of diamonds is physically important: it allows in-principle realizations with finite-size apparatuses. In the Rindler setting, the causal regions are infinite half-spaces — inaccessible to any finite experiment. Diamonds are the natural setting for discussions of laboratory quantum information experiments informed by relativistic QFT.

The explicit modular Hamiltonian formula in CFT (the Casini-Huerta-Myers result) makes causal diamonds particularly amenable to computing the [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] via

$$S(\omega\|\varphi) = -\langle\Omega, \log\Delta_{\Phi,\Omega}\,\Omega\rangle,$$

since $\log\Delta$ is related to the modular Hamiltonian $K = -\log\Delta$.

## Relations

- [[rindler-wedges]] — the infinite-size counterpart; diamonds are compact analogs of wedges. In the limit $r \to \infty$, the diamond approaches a wedge. The same algebraic methods (Tomita-Takesaki, Weyl operators) apply to both.
- [[tomita-takesaki-modular-theory]] — the modular operator for the diamond algebra is explicitly known in CFT; this makes relative entropy computations tractable
- [[bell-chsh-inequality]] — Bell-CHSH violations in diamond regions extend the Rindler program to compact setups (Eur. Phys. J. C 85, 2025)
- [[type-iii-von-neumann-algebras]] — $\mathcal{M}(\mathcal{D})$ is type III₁ for any local region in AQFT, including diamonds
- [[araki-uhlmann-relative-entropy]] — explicit modular Hamiltonians in CFT allow direct computation of relative entropy for diamond algebras
- [[weyl-operators]] — Weyl operators localized in the diamond (test functions supported in $\mathcal{D}$) generate the local algebra $\mathcal{M}(\mathcal{D})$

## Papers

See [[bell-inequalities-qft]] and [[relative-entropy-qft]] for full paper lists.

## Notes

- The term "causal diamond" is standard in the AQFT and quantum gravity literature. "Double cone" is the older AQFT term; "diamond region" is used in quantum information contexts.
- The modular Hamiltonian is only known explicitly for specific geometries: Rindler wedges (all QFTs), causal diamonds (CFTs via Casini-Huerta-Myers), and spherical entangling surfaces (CFTs). For general regions and non-conformal theories, it is non-local and not explicitly computable.
- Two spacelike-separated diamonds (diamonds whose closures do not intersect) provide a natural bipartite setup where Alice controls one diamond and Bob the other; microcausality ensures $[A,B]=0$ automatically.
- The proper acceleration required for a Rindler observer to remain inside a diamond of size $r$ is $a = 1/r$, giving an Unruh temperature $T_U = 1/(2\pi r)$ — inversely proportional to diamond size.

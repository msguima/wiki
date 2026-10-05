---
title: "Exercises and answer checkpoints — Geometric QCD"
type: appendix
course: geometric-qcd-course-guide
modified: 2026-10-05
---

# Exercises and answer checkpoints

Edition 2.0. The 140 problems below are collected from the lecture sources. Problems 1–2 provide the core calculation, problem 3 checks interpretation, and problem 4 is a bounded research extension. Its completion criterion may be a documented unresolved source issue. Do not treat an open source claim as an exercise premise.

## I.1

[[mini-lecture-01-large-n-and-wilson-loops|Read the lecture]].

**I.1.1.** Compute the normalized trace of $U$ at $\alpha=\pi/3$.

**Checkpoint.** It is $(e^{i\pi/3}+e^{-i\pi/3})/2=1/2$.

**I.1.2.** Compare two disconnected disks with a connected cylinder for normalized traces.

**Checkpoint.** The disks contribute order one; the cylinder contributes $N_c^{-2}$. The cylinder has genus zero and two boundaries.

**I.1.3.** Does trace conjugation invariance prove an area law?

**Checkpoint.** No. It proves gauge invariance of the observable. Area-law behavior is dynamical and depends on the state and regime.

**I.1.4.** Research extension. Use the primary 't Hooft reading to trace the counting for one ribbon graph with a handle.

**Checkpoint.** Completion: draw the graph, identify $V,E,F,b$, verify the Euler characteristic, and exhibit the extra $N_c^{-2}$ relative to the corresponding planar topology. No confinement claim follows from this exercise.

## I.2

[[mini-lecture-02-physical-amplitudes-and-brownian-loops|Read the lecture]].

**I.2.1.** Evaluate $\int_0^\infty e^{-5T}\,dT$ and identify the sign of the inverse of $-5$.

**Checkpoint.** The integral is $1/5$; $(-5)^{-1}=-1/5$.

**I.2.2.** Derive the bridge increment variance and evaluate it at the laboratory parameters.

**Checkpoint.** Use $C(t,t)+C(s,s)-2C(t,s)$ with $C(s,t)=2(\min(s,t)-st/T)$. The result is $1/2$.

**I.2.3.** Can the color and spin terms always be split into two separately ordered exponentials?

**Checkpoint.** No. Their matrix insertions generally do not commute. One needs common ordering or a parallel-transported interaction representation.

**I.2.4.** Research extension. Compare the finite-slice heat kernel with the phase-space prescription on IAS pp. 47–48.

**Checkpoint.** Completion: state the regulator, integration variables, ordering, and mass normalization, and recover the free propagator before drawing conclusions about interacting amplitudes.

## I.3

[[mini-lecture-03-holonomy-and-parallel-transport|Read the lecture]].

**I.3.1.** Apply $e^{a\partial_x}$ to $x^2$.

**Checkpoint.** The result is $(x+a)^2=x^2+2ax+a^2$.

**I.3.2.** Derive the second-order difference of the two exponentials in the laboratory.

**Checkpoint.** The mixed term in the product is $XY$; that in the single exponential is $(XY+YX)/2$, leaving $[X,Y]/2$.

**I.3.3.** Why must a path-ordering convention be fixed before assigning an area-derivative sign?

**Checkpoint.** Exchanging the order of two neighboring insertions reverses their commutator and the associated oriented plaquette.

**I.3.4.** Research extension. Translate the source's operator product to the parallel-section convention in I.2.

**Checkpoint.** Completion: write the transport equation, orientation, endpoint transformation, and a small-plaquette check in both conventions. A dictionary with matched signs is the requested result.

## I.4

[[mini-lecture-04-loop-derivatives-and-area-derivatives|Read the lecture]].

**I.4.1.** Compute the two traces in the laboratory.

**Checkpoint.** $\operatorname{tr}\sigma_3=0$ and $\sigma_3^2=1$ give $0$ and $4i$.

**I.4.2.** Evaluate $d^2(x^2)/dx^2$ and compare with the proposed first-order product rule.

**Checkpoint.** The derivative is $2$, whereas $x''x+xx''=0$. The missing cross term is $2x'x'=2$.

**I.4.3.** State the extra condition needed to dress the right side of the MM equation.

**Checkpoint.** Area additivity at the supported splitting: $S[C]=S[C_{xy}]+S[C_{yx}]$. A left-side zero mode alone is insufficient.

**I.4.4.** Research extension. Examine point splitting on IAS pp. 13–14 and the zero-mode discussion on pp. 70–72.

**Checkpoint.** Completion: specify a class of functionals, the order of limits, and the continuity assumptions used to cancel product cross terms. An unqualified appeal to the matrix commutator identity is not a completion.

## I.5

[[mini-lecture-05-the-makeenko-migdal-equation|Read the lecture]].

**I.5.1.** Evaluate $\sum_a\operatorname{tr}(T^aT^a)$ for $SU(2)$.

**Checkpoint.** Three terms of $1/2$ give $3/2$.

**I.5.2.** Derive the normalized split expression from the Fierz identity.

**Checkpoint.** Replace each trace by $N_cw$ in $g^2(2N_c)^{-1}(\operatorname{tr}U\operatorname{tr}V-N_c^{-1}\operatorname{tr}UV)$ to obtain $(\lambda/2)(w_Uw_V-N_c^{-2}w_{UV})$.

**I.5.3.** Distinguish $W_2$ from $W_{2,c}$.

**Checkpoint.** $W_2(C_1,C_2)=\langle w_1w_2\rangle$ is the full correlator; $W_{2,c}(C_1,C_2)=W_2(C_1,C_2)-W[C_1]W[C_2]$ is its connected part. Only the latter is suppressed by $N_c^{-2}$.

**I.5.4.** Research extension. Compare the original MM paper with IAS equation (22).

**Checkpoint.** Completion: record generator, action, area-derivative, and coupling conventions; translate the leading coefficient and the finite-$N_c$ subtraction. Do not compare coefficients without that dictionary.

## I.6

[[mini-lecture-06-planar-bootstrap|Read the lecture]].

**I.6.1.** Reproduce the coefficient $18$.

**Checkpoint.** It is $5+7+2\cdot3$.

**I.6.2.** Check the finite-matrix inverse in the main derivation through order $\epsilon^2$.

**Checkpoint.** Expand $(6-\epsilon^2)^{-1}=1/6+\epsilon^2/36+\cdots$. The diagonal corrections are $\epsilon^2/12$ and $\epsilon^2/18$, and the off-diagonal first term is $-\epsilon/6$.

**I.6.3.** Which closed loop has the Grassmann minus sign in gauge-fixed perturbation theory?

**Checkpoint.** A ghost loop, represented by anticommuting Faddeev–Popov fields. A gluon loop does not acquire that sign merely from being closed.

**I.6.4.** Research extension. Design a one-loop match between the bootstrap and a gauge-fixed calculation.

**Checkpoint.** Completion: specify the regulator, gauge, observable, and all gluon and ghost contributions with symmetry factors. A list of superficially similar diagrams is insufficient.

## I.7

[[mini-lecture-07-coordinate-space-catastrophe|Read the lecture]].

**I.7.1.** Compute the crossing integral's coefficient at $\phi=\pi/6$ before the tangent numerator.

**Checkpoint.** $2\pi/|\sin(\pi/6)|=4\pi$.

**I.7.2.** Differentiate the model subtraction explicitly.

**Checkpoint.** The derivative of $Z$ is $g^2c'(\phi)\log(1/\epsilon)$, giving the additional term displayed above.

**I.7.3.** Does this example prove that renormalized Wilson loops do not exist?

**Checkpoint.** No. It shows why a naive contour-dependent subtraction does not automatically commute with the loop derivatives.

**I.7.4.** Research extension. Formulate one regulated crossing problem in coordinate space.

**Checkpoint.** Completion: give the contour, regulator, operator basis, mixing prescription, and limiting quantity. The result may be an obstruction to that prescription, not a universal impossibility statement.

## II.1

[[mini-lecture-01-why-momentum-loop-space|Read the lecture]].

**II.1.1.** What is the transform of $\delta_\epsilon$ at $p=0$?

**Checkpoint.** It is $1$, expressing unit normalization.

**II.1.2.** Verify the sign in $\widehat{f'}=-ip\widehat f$ by integration by parts.

**Checkpoint.** Differentiate the exponential to obtain $ip e^{ipx}$; moving the derivative from $f$ contributes the minus sign.

**II.1.3.** Why does pointwise convergence to $1$ not establish ultraviolet control?

**Checkpoint.** Because momenta may scale with the regulator. At $p=\epsilon^{-1/2}$ the difference from $1$ does not vanish.

**II.1.4.** Research extension. Discretize the loop transform with a finite number of contour variables.

**Checkpoint.** Completion: state the closure constraint, translation zero mode, measure, Fourier normalization, and transform of one regulated contact. Separate the finite identity from the continuum limit.

## II.2

[[mini-lecture-02-quark-loop-amplitudes-in-phase-space|Read the lecture]].

**II.2.1.** Find the variance for $M=2$ and $\Delta t=1/4$.

**Checkpoint.** It is $\Delta t/M=1/8$.

**II.2.2.** Integrate the displayed coordinate kernel over $\Delta x$.

**Checkpoint.** The Gaussian integral cancels the prefactor, giving one.

**II.2.3.** Does the scalar slice derive the full spin factor?

**Checkpoint.** No. It verifies the Gaussian part and its normalization. The Dirac matrix insertions require their own ordered representation.

**II.2.4.** Research extension. Construct a two-slice spin and color example for IAS pp. 47–48.

**Checkpoint.** Completion: retain the order of every matrix, evaluate the finite product, and state what additional limit would recover the formal continuum expression.

## II.3

[[mini-lecture-03-factorization-of-the-momentum-loop-measure|Read the lecture]].

**II.3.1.** Compute the determinant of $(s,t)\mapsto(s,s+t)$.

**Checkpoint.** It is one.

**II.3.2.** Evaluate each constrained Gaussian block.

**Checkpoint.** Set $b=-a$ using the delta. The integral becomes $\int e^{-a^2}da=\sqrt\pi$.

**II.3.3.** Why does global closure alone not factorize the two blocks?

**Checkpoint.** It imposes only $s+t=0$, allowing nonzero opposite displacements. Separate closure requires the contact constraint too.

**II.3.4.** Research extension. Repeat this construction for a polygonal loop in four dimensions.

**Checkpoint.** Completion: show all vector constraints and Jacobians, fix the base-point translation, and identify any action or gauge factors that prevent a product measure.

## II.4

[[mini-lecture-04-kinematic-tensors-and-magnus-forms|Read the lecture]].

**II.4.1.** Calculate $I^{xy}$ and $I^{yx}$ for sides $2,3$.

**Checkpoint.** They are $6$ and $-6$.

**II.4.2.** Expand $[X,[X,Y]]$ into ordered words.

**Checkpoint.** $X^2Y-2XYX+YX^2$.

**II.4.3.** Does $I^\mu=0$ imply that a coefficient tensor $W^{(2)}$ vanishes?

**Checkpoint.** No. For example a symmetric coefficient can contract to zero with the antisymmetric second level while itself being nonzero.

**II.4.4.** Research extension. Compare the source's “Magnus forms” with iterated integrals and the logarithmic Magnus series.

**Checkpoint.** Completion: give definitions, ordering, and the conversion through degree three. Identify which object the source coefficient contracts; do not equate the series merely by name.

## II.5

[[mini-lecture-05-low-order-algebraic-solutions|Read the lecture]].

**II.5.1.** Show that $6!/(2^3 3!)=5!!$.

**Checkpoint.** Both equal $15$. These are two formulas for the same labeled pairing count.

**II.5.2.** Find the kernel of the displayed model matrix $A_0$.

**Checkpoint.** Solving $a-c=0$ and $b=0$ gives $(a,b,c)=t(1,0,1)$.

**II.5.3.** Why is the source's clipped sixth-order formula insufficient as a reproducible solution?

**Checkpoint.** The complete coefficient list, basis, equations, and residual are needed. Listing fifteen pairings does not determine their coefficients.

**II.5.4.** Research extension. Reconcile slide 55 with Part II Appendix C before solving the MLE.

**Checkpoint.** Completion: freeze both versions, state the tensor convention and quotient, and either provide a conversion explaining the differing $W^{(4)}$ terms or record an unresolved discrepancy. Do not choose a free coefficient by guesswork.

## II.6

[[mini-lecture-06-breakdown-at-eighth-order|Read the lecture]].

**II.6.1.** Compute $y^T(1,3,0)^T$.

**Checkpoint.** It is $-2+3=1$, certifying inconsistency.

**II.6.2.** Solve the compatible system for source $(1,2,2)^T$.

**Checkpoint.** $x_1+x_2=1$ and $x_1-x_2=2$ give $(3/2,-1/2)$.

**II.6.3.** What additional claim is needed to exclude every analytic representation?

**Checkpoint.** That the chosen finite ansatz and all constraints exhaust the relevant analytic class. A rank failure in one specified ansatz is narrower.

**II.6.4.** Research extension. Extract an exact left-null certificate for the reported eighth-order system.

**Checkpoint.** Completion: preserve the matrix, source, basis map, and a rational $y$ with $y^TA=0$ and $y^Tb\ne0$. If those inputs are unavailable, report the missing inputs; the published rank table alone is not an independent certificate.

## II.7

[[mini-lecture-07-nonanalytic-vacuum-and-q-and-a|Read the lecture]].

**II.7.1.** Compute $\|\,|12\rangle-|21\rangle\,\|^2$.

**Checkpoint.** It equals two, because the distinct word states are orthonormal.

**II.7.2.** Derive $e^{tX}$ for $X^2=1$ by separating even and odd powers.

**Checkpoint.** The even powers sum to $\cosh t\,1$ and the odd powers to $\sinh t\,X$.

**II.7.3.** Why does white-noise roughness not prove nonanalytic source dependence?

**Checkpoint.** For admissible smeared sources the Gaussian characteristic functional is an exponential of a finite quadratic form.

**II.7.4.** Research extension. Specify the state and topology in a proposed master-field representation.

**Checkpoint.** Completion: identify the operator algebra, normalized state, trace status, allowed sources, and one correlation function. Any nonanalyticity claim must be tested in that stated source topology.

## III.1

[[mini-lecture-01-why-four-dimensional-geometry-enters|Read the lecture]].

**III.1.1.** Compute $*B_2$.

**Checkpoint.** Use $*dx^{13}=-dx^{24}$ and $*dx^{24}=-dx^{13}$, giving $B_2$.

**III.1.2.** Prove $P_+P_-=0$.

**Checkpoint.** $(1+*)(1-*)/4=(1-*^2)/4=0$.

**III.1.3.** Does the dimension of these eigenspaces prove a QCD vacuum construction?

**Checkpoint.** No. It is kinematics. Existence, boundary data, area variation, and the loop equation remain to be checked.

**III.1.4.** Research extension. List the hypotheses connecting a proposed surface to III.2.

**Checkpoint.** Completion: give a functional domain, area derivative, Bianchi identity, duality, and splitting condition, and identify which are actually demonstrated by the chosen source.

## III.2

[[mini-lecture-02-area-derivatives-and-self-dual-zero-modes|Read the lecture]].

**III.2.1.** Evaluate $B\wedge B$ for the displayed self-dual form.

**Checkpoint.** It is $2\,dx^{1234}$: the two cross terms agree because two-forms commute under the wedge product.

**III.2.2.** Show that self-duality and $D_\mu(*F)_{\mu\nu}=0$ imply the source-free Yang–Mills equation.

**Checkpoint.** Replace $*F$ by $\chi F$, with $\chi^2=1$, and multiply by $\chi$.

**III.2.3.** Why does a zero mode not solve the full MM equation by itself?

**Checkpoint.** The MM equation has a splitting source. A homogeneous solution need not reproduce it.

**III.2.4.** Research extension. Test the source's geometric premises using the explicit definitions in III.5.

**Checkpoint.** Completion: calculate the tensor and its Hodge star on a smooth example before invoking Bianchi. A failure of the premise blocks that application but does not invalidate the conditional implication.

## III.3

[[mini-lecture-03-additivity-and-the-goldschmidt-branch|Read the lecture]].

**III.3.1.** Evaluate $\operatorname{tr}(UV)/2$ for the matrices in the derivation.

**Checkpoint.** $UV=-1_2$, so the normalized trace is $-1$ although both individual normalized traces vanish.

**III.3.2.** Derive the catenoid area integral.

**Checkpoint.** $r=a\cosh(z/a)$ and $\sqrt{1+r'^2}=\cosh(z/a)$. Integrating $2\pi a\cosh^2(z/a)$ yields $\pi ah+\pi a^2\sinh(h/a)$.

**III.3.3.** What factorizes when the geometric area is additive?

**Checkpoint.** The exponential dressing. Multiplicativity of a single traced holonomy does not follow.

**III.3.4.** Research extension. State an applicable bridge or minimal-surface theorem with its hypotheses.

**Checkpoint.** Completion: name the surface class, boundary perturbation, convergence topology, and exact conclusion. Check separately whether it implies the tangent alignment used in IV.6.

## III.4

[[mini-lecture-04-physical-vacuum-and-instanton-language|Read the lecture]].

**III.4.1.** Calculate $F_{\mu\nu}F_{\mu\nu}$ in the example.

**Checkpoint.** Each antisymmetric pair is counted twice: $2B^2+2B^2=4B^2$.

**III.4.2.** How does the action change under $L\mapsto2L$?

**Checkpoint.** It increases by a factor of $16$ for the constant field.

**III.4.3.** Does satisfying a classical equation select a unique quantum vacuum?

**Checkpoint.** No. State construction, boundary conditions, normalization, and quantum correlations are additional inputs.

**III.4.4.** Research extension. Compare a genuine finite-action instanton with the constant example.

**Checkpoint.** Completion: state its boundary conditions, show convergence of its action integral, and explain which of those properties have or have not been established for the source's surface functional.

## III.5

[[mini-lecture-05-constructing-the-hodge-dual-surface|Read the lecture]].

**III.5.1.** Find the disk integral for $A=2$, $n=3$.

**Checkpoint.** It is $3\pi$.

**III.5.2.** Compute $E_D-A$ for the ellipse with $a=2$, $b=1$.

**Checkpoint.** $E_D=5\pi/2$, $A=2\pi$, and the excess is $\pi/2$.

**III.5.3.** Does imposing the circle's null condition repair the source tensor identity?

**Checkpoint.** No. The circle already has $f'\cdot f'=0$, yet the literal extended tensor has $(\Sigma_{12},\Sigma_{34})=(1,-2)$ for $\chi=+1$, so it is not self-dual.

**III.5.4.** Research extension. Investigate a possible repair of the extended tensor definition.

**Checkpoint.** Completion: state the changed definition, recompute its duality and area variation, and check the same boundary example. Adding a projection without redoing the variational argument is not a verified repair.

## III.6

[[mini-lecture-06-twistor-factorization-and-parity|Read the lecture]].

**III.6.1.** Check that the circle tangent is complex null.

**Checkpoint.** $(1/2)^2+(-i/2)^2=1/4-1/4=0$.

**III.6.2.** Multiply the two spinors in the displayed factorization.

**Checkpoint.** The outer product has the single nonzero entry $V_{21}=i$.

**III.6.3.** Why is a real Euclidean null vector necessarily zero but this vector is not?

**Checkpoint.** A real sum of squares is nonnegative; complex bilinear squares can cancel. The Hermitian norm of the example is $1/2$.

**III.6.4.** Research extension. Patch this factorization across zeros of a holomorphic tangent.

**Checkpoint.** Completion: give local spinor choices, transition rescalings, and behavior near at least one zero. A pointwise rank-one factorization alone does not supply a global nonsingular measure.

## III.7

[[mini-lecture-07-ope-matching-and-regge-physics|Read the lecture]].

**III.7.1.** Compute $I^2$ directly using $n^Tn=1$.

**Checkpoint.** $(1-2nn^T)^2=1-4nn^T+4n(n^Tn)n^T=1$.

**III.7.2.** Evaluate the tensor contraction in dimensions three and five.

**Checkpoint.** It is $-2$ and $4$, respectively.

**III.7.3.** What are the units of $\kappa$ if $\kappa^2$ matches a dimension-four condensate?

**Checkpoint.** $\kappa$ has mass dimension two. It multiplies an area of mass dimension minus two in an exponential.

**III.7.4.** Research extension. Audit the condensate matching on slide 86.

**Checkpoint.** Completion: fix field and coupling conventions, the area normalization, renormalization scale and operator definition, and identify which part is source input versus independently derived. The tensor cancellation alone does not complete the matching.

## IV.1

[[mini-lecture-01-majorana-fields-on-a-surface|Read the lecture]].

**IV.1.1.** Write $P_+$ and $P_-$ as matrices.

**Checkpoint.** They are $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$.

**IV.1.2.** Compute the determinant and Pfaffian of the two-component mass matrix.

**Checkpoint.** They are $m^2$ and $m$, respectively, with the stated Pfaffian orientation.

**IV.1.3.** Does taking $m\to\infty$ force this determinant to zero?

**Checkpoint.** No. This determinant grows as $m^2$. A renormalized limit depends on normalization and counterterms.

**IV.1.4.** Research extension. Specify a continuum boundary domain for the source operator.

**Checkpoint.** Completion: write the quadratic form, reality convention, boundary pairing, and the condition that removes its boundary term; distinguish that check from an ellipticity or spectral proof.

## IV.2

[[mini-lecture-02-curved-surfaces-spinors-and-anomalies|Read the lecture]].

**IV.2.1.** Find $D_\rho/D_0$ for constant $\rho=\log2$.

**Checkpoint.** The scale factor is $1/2$.

**IV.2.2.** Derive the boundary contribution in $\delta S_L$.

**Checkpoint.** Integration by parts gives $2c_L\int_{\partial D}\delta\rho\,\partial_n\rho$ in addition to $-2c_L\int_D\delta\rho\Delta\rho$.

**IV.2.3.** Why does a bulk central-charge coefficient not settle the full cancellation?

**Checkpoint.** Boundary terms, multiplicities, zero modes, mass transformation, and finite normalization also enter the regulated determinant.

**IV.2.4.** Research extension. Audit the source's conformal action on pp. 94–98.

**Checkpoint.** Completion: check both proposed gauge endpoints and the constant-Weyl test, and match every bulk and boundary variation in one convention. Record any discrepancy instead of identifying unlike mass profiles.

## IV.3

[[mini-lecture-03-determinants-as-loop-sums|Read the lecture]].

**IV.3.1.** Evaluate the displayed Pfaffian for the supplied entries.

**Checkpoint.** It is $8$.

**IV.3.2.** Use the two-site model to distinguish $\det(1-H)$ from $\log\det(1-H)$ at $t=1/2$.

**Checkpoint.** The determinant is $3/4$; its logarithm is $\log(3/4)$. The first connected term alone is $-1/4$.

**IV.3.3.** What Gaussian quantity do bosons produce?

**Checkpoint.** An inverse determinant for a complex Gaussian, or an inverse square root for a real Gaussian, up to normalization; not a permanent.

**IV.3.4.** Research extension. Translate the source loop sum into a regulated determinant or Pfaffian.

**Checkpoint.** Completion: specify whether each sum is connected, its symmetry factors, spin holonomy, and normalization. Verify the relation first on a finite graph.

## IV.4

[[mini-lecture-04-pauli-cancellation-and-planarity|Read the lecture]].

**IV.4.1.** Reduce $\theta_1\theta_2\theta_1\theta_2$.

**Checkpoint.** One interchange yields $-\theta_1^2\theta_2^2=0$.

**IV.4.2.** Does the same argument kill a product of four distinct generators?

**Checkpoint.** No. That product is a nonzero basis element of the Grassmann algebra.

**IV.4.3.** List the data needed for a sign-reversing cancellation of paths.

**Checkpoint.** A pairing or involution, opposite signs, equal magnitudes and measures, and a treatment of fixed points and boundary configurations.

**IV.4.4.** Research extension. Construct such a pairing for a finite regulated surface graph.

**Checkpoint.** Completion: enumerate the configurations and show cancellation with all spin and internal labels retained. A finite example is not an all-orders continuum proof.

## IV.5

[[mini-lecture-05-large-mass-limit-and-the-a-term|Read the lecture]].

**IV.5.1.** Verify the remainder by multiplying the displayed identity by $m^2+p^2$.

**Checkpoint.** The product is one; the $p^4/m^4$ terms cancel.

**IV.5.2.** Bound the remainder for $|p|\le M$.

**Checkpoint.** The denominator is at least $m^6$, giving $M^4/m^6$.

**IV.5.3.** Why can one not automatically integrate the truncated series over all momenta?

**Checkpoint.** The small parameter is $p^2/m^2$, which is not small uniformly on the full integration domain.

**IV.5.4.** Research extension. Formulate the A-term limit with a regulator.

**Checkpoint.** Completion: retain the tensor indices, separate bounded and large momenta, justify the Bianchi contraction and interchange of limits, and identify any contact remainder.

## IV.6

[[mini-lecture-06-whites-bridge-and-the-contact-term|Read the lecture]].

**IV.6.1.** Integrate the unnormalized source kernel with ordinary $d^4x$.

**Checkpoint.** The integral is $3\pi^2$, independent of $m$.

**IV.6.2.** Find the normalized kernel's mean squared radius at $m=20$.

**Checkpoint.** It is $5/400=0.0125$.

**IV.6.3.** Does an upper bound by an exponential determine the delta coefficient?

**Checkpoint.** No. It shows suppression away from the diagonal; the measure, prefactor, and total mass determine the coefficient.

**IV.6.4.** Research extension. Derive the actual two-touching kernel from the determinant.

**Checkpoint.** Completion: identify the ambient measure and tensor contraction, prove convergence on test functions, and track the normalization into the proposed coupling.

## IV.7

[[mini-lecture-07-induced-qcd-and-asymptotic-freedom|Read the lecture]].

**IV.7.1.** Evaluate $b_1/b_0^2$.

**Checkpoint.** It is $51/121$.

**IV.7.2.** Integrate $d\log\mu/d\lambda=-1/(b_0\lambda^2)+b_1/(b_0^2\lambda)$.

**Checkpoint.** The antiderivative is $1/(b_0\lambda)+(b_1/b_0^2)\log\lambda$ plus a constant.

**IV.7.3.** What does the two-loop calculation establish about the induced surface theory?

**Checkpoint.** It establishes the scale relation if that theory matches the stated beta function. It does not itself prove the matching.

**IV.7.4.** Research extension. Specify the renormalization condition on $Z[1]$.

**Checkpoint.** Completion: give its regulator, vacuum normalization, mass dependence, and perturbative coupling match. Decoupling rhetoric alone does not determine the determinant limit.

## V.1

[[mini-lecture-01-from-quark-phase-space-to-spectrum|Read the lecture]].

**V.1.1.** Read the masses from $G=2/(p_E^2+9)+1/(p_E^2+25)$.

**Checkpoint.** They are $3$ and $5$ in the chosen units, with residues $2$ and $1$.

**V.1.2.** Cancel the large-$N_c$ factors in the laboratory relation.

**Checkpoint.** The ratio of condensate to $f_\pi^2$ is $C_0/f_0^2$, of order one.

**V.1.3.** Does a successful fit establish spectral positivity or a QCD derivation?

**Checkpoint.** No. Those depend on the underlying state, operator construction, and analytic properties.

**V.1.4.** Research extension. Map each step from the phase-space amplitude to a spectral pole.

**Checkpoint.** Completion: identify the operator, continuation, positivity assumptions, saddle approximation, and fit inputs; mark which implications have actually been derived.

## V.2

[[mini-lecture-02-twistor-parametrization-of-the-measure|Read the lecture]].

**V.2.1.** Find the eigenvalues for $\Lambda=2$.

**Checkpoint.** They are $0,4,2,2$.

**V.2.2.** Compute the pseudodeterminant and its square root for $\Lambda=2$.

**Checkpoint.** They are $16$ and $4$.

**V.2.3.** Why is omitting a zero eigenvalue not the complete gauge-fixing procedure?

**Checkpoint.** One must also specify the gauge condition, orbit volume or metric, residual symmetry, real-variable measure, and degenerate patches.

**V.2.4.** Research extension. Derive the measure in one finite spinor patch.

**Checkpoint.** Completion: exhibit the coordinate map, gauge condition, real Jacobian, residual phase quotient, and domain. Compare its homogeneity with the source formula before taking a functional product.

## V.3

[[mini-lecture-03-polar-variables-and-local-path-integrals|Read the lecture]].

**V.3.1.** Transform $u^5du$ under $\rho=2\log u$.

**Checkpoint.** It becomes $\tfrac12e^{3\rho}d\rho$.

**V.3.2.** Compute the kernel scale factor for $\rho=\log3$.

**Checkpoint.** It is $e^{-3\log3}=1/27$.

**V.3.3.** Why is a damping prescription needed for the proper-time integral of $i\gamma\cdot q$?

**Checkpoint.** Its eigenvalues are purely imaginary for real Euclidean momentum, so the undamped positive-time exponential does not decay.

**V.3.4.** Research extension. Keep the regulator through the local Fourier integration.

**Checkpoint.** Completion: specify the distributional limit, contact terms, normalization, and zero-mode handling. A pointwise noncoincident kernel alone is not the full functional measure.

## V.4

[[mini-lecture-04-liouville-term-and-scale-cancellation|Read the lecture]].

**V.4.1.** Convert $|\partial_z\rho|^2$ to real derivatives.

**Checkpoint.** It is $(\rho_u^2+\rho_v^2)/4$.

**V.4.2.** Derive the boundary variation of the action.

**Checkpoint.** It is $\int_{\partial D}[(\partial_n\rho)/(6\pi)+m_qe^\rho]\delta\rho\,ds_0$.

**V.4.3.** Does a locally scale-invariant measure imply a scale-independent action?

**Checkpoint.** No. Both the exponential bulk potential and boundary mass depend on $\rho$.

**V.4.4.** Research extension. Compare boundary conditions used in the source's saddle problem.

**Checkpoint.** Completion: state what is held fixed, derive the appropriate boundary variation, and translate all complex-coordinate measure factors before comparing coefficients.

## V.5

[[mini-lecture-05-minkowski-continuation-and-helicoids|Read the lecture]].

**V.5.1.** Find the timelike interval when $\omega=2$.

**Checkpoint.** $|s|<1/2$.

**V.5.2.** Derive the vanishing cross term $g_{\tau s}$.

**Checkpoint.** The spatial dot product is $-\omega s\sin(\omega\tau)\cos(\omega\tau)+\omega s\cos(\omega\tau)\sin(\omega\tau)=0$.

**V.5.3.** Does a real classical action prove a stable quantum spectrum?

**Checkpoint.** No. The fluctuation operator, boundary domain, integration cycle, and positivity properties must still be analyzed.

**V.5.4.** Research extension. Calculate fluctuations around the displayed surface with massive endpoints.

**Checkpoint.** Completion: specify endpoint conditions and the quadratic operator, identify its zero modes, and distinguish classical stability evidence from a complete spectral theorem.

## V.6

[[mini-lecture-06-monodromies-wkb-action-and-spin-projection|Read the lecture]].

**V.6.1.** What is $M_a$ at $a=1/2$ and what does it do to a vector matrix?

**Checkpoint.** $M_a=-1_2$, so conjugation leaves the vector matrix unchanged.

**V.6.2.** Derive the quadratic equation for $y=K\cos^2\beta/\sin\beta$.

**Checkpoint.** Multiply $\partial_\beta\Phi=0$ by $\cos^2\beta/(2\pi\sin^2\beta)$ to obtain $-y^2+2xy-1/(3\pi)=0$.

**V.6.3.** Does the Gaussian prefactor prove exact WKB?

**Checkpoint.** No. Higher action terms, other saddles, zero modes, and the integration cycle can change the amplitude and spectral condition.

**V.6.4.** Research extension. Analyze the source's transverse Hessian near a branch-point saddle.

**Checkpoint.** Completion: specify the operator domain, regulator, zero-mode removal, determinant and leading corrections, then test whether poles shift. The source's conjecture is not the premise to prove by assumption.

## V.7

[[mini-lecture-07-regge-trajectories-and-fit-audit|Read the lecture]].

**V.7.1.** Convert $\sqrt\sigma=0.417\ \mathrm{GeV}$ into $\sigma$.

**Checkpoint.** $\sigma=0.173889\ \mathrm{GeV}^2$.

**V.7.2.** Use $\partial_K\Phi=0$ and $\Phi=0$ to derive the spin formula.

**Checkpoint.** Substitute $\mathcal E=KF+2x\cos\beta$; the mass terms cancel and $\Phi=\pi K^2F-4\pi(J+q/2)-\tfrac23(\tan\beta-\beta)$ gives the result.

**V.7.3.** Does using no new family-specific parameter make a globally fitted family held out?

**Checkpoint.** No. Held-out status depends on whether its data were excluded before optimization.

**V.7.4.** Research extension. Reproduce the source fit, then perform a separate prediction test.

**Checkpoint.** Completion: preserve the state table, uncertainty and exclusion rules, objective, parameters, optimizer and residuals. For prediction, hold out data before fitting and report errors without retuning. The current course does not claim this research audit has been completed.

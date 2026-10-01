---
title: "Opening block — instructor guide"
type: teaching-guide
edition: "2.0"
modified: 2026-09-29
---

# Teaching the four opening lectures

The opening block asks students to follow the same information through several descriptions: a global state, the observables an observer can measure, an encoding, and the state restricted to a recoverable algebra. The small models are the main calculations. Their holographic interpretations become questions whose missing physical ingredients students can name.

The [[courses/2026-algebraic-qft-course/syllabus|AQFT course]] is the reference for depth and independent study. These notes use its classroom/self-study distinction. The allocations below are plans for four meetings of 120 minutes, not results of a rehearsal. They occupy the first two weeks of the four-hour-per-week lecture schedule; exercise sessions are additional.

## Before the first meeting

Students should be able to expand a tensor-product vector, use the Born rule, multiply small matrices, and diagonalize a positive matrix. They need no prior von Neumann algebra course.

A useful preparation question is to compare the pure Bell state with the classical mixture of $|00\rangle$ and $|11\rangle$. Ask for the probability of equal outcomes when both observers measure $Z$, then when both measure $X$. The first experiment does not distinguish the preparations; the second does. This diagnoses whether students already separate classical correlations, coherence, and local mixedness.

Put the following distinctions on a reusable board or handout:

| Object | Question it answers |
|---|---|
| State of the complete system | How are all allowed measurements distributed? |
| Accessible algebra | Which measurements and operations are being retained? |
| Restricted state | What statistics survive that restriction? |
| Encoding isometry | How are logical preparations represented physically? |
| Recovery map | How can the retained information be extracted? |

Introduce symbols through examples. Students should encounter the Bell calculation before the general definition of restriction, and the explicit decoder before a general recovery theorem.

## Lecture 1: access determines what can be distinguished

Use [[lecture-01-observables-and-restricted-access|Lecture 1]].

| Time | Board calculation or activity | Evidence of understanding |
|---|---|---|
| 0–15 min | Prepare the two Bell states and compute the $XX$ expectation | Students locate the distinguishing measurement in a joint correlation |
| 15–35 min | Calculate both partial traces, including an off-diagonal term | Students can explain why every measurement confined to $A$ gives identical statistics |
| 35–65 min | Define an algebra and a restricted state; compare the full qubit algebra with the diagonal algebra | Students distinguish changing the state from changing the available observables |
| 65–85 min | Prove no-signaling with Kraus operators; discuss conditioning on a reported outcome | Students identify where the classical record is needed |
| 85–105 min | Compute the commutant and center in the tensor-factor and diagonal examples | Students explain the difference between an algebra and its center |
| 105–120 min | Checkpoints and exit calculation | Students justify a conclusion using an expectation, not only a slogan |

**Board discipline.** Keep one fixed ordering of the two factors. When taking a partial trace, write $\operatorname{Tr}_B(|i,j\rangle\langle k,l|)=\delta_{jl}|i\rangle\langle k|$ once and use it visibly. Do not begin with a catalogue of algebra types.

**Likely difficulty.** “Alice sees a mixed state, therefore Alice and Bob are entangled.” Return to the classical mixture, which has the same local states. The entropy of a reduction certifies entanglement for a pure bipartite global state; the purity assumption matters.

**If discussion needs more time.** Teach the commutants by checking the matrix examples. Leave the general matrix-unit proof in Section 7 for self-study. Keep the no-signaling/conditional-state distinction.

**Exit question.** Can a unitary on Bob's system change Alice's unconditional measurement statistics? Give the one-line calculation.

**Expected answer.** No: cyclicity of the partial trace over $B$ gives $\operatorname{Tr}_B[(I\otimes U)\rho(I\otimes U^\dagger)]=\rho_A$. This does not forbid different conditional states after Bob communicates an outcome.

**After class.** Assign Problems 1–3 as the core set. Problems 4–6 consolidate channels and commutants. The QFT extension is an orientation question and does not require proving type-III structure.

**Transition.** Local invisibility is only the first requirement of an encoding. Next ask whether the surviving correlations contain enough information to recover an arbitrary quantum input.

## Lecture 2: recovery is a calculation on every input

Use [[lecture-02-three-qutrit-code|Lecture 2]].

| Time | Board calculation or activity | Evidence of understanding |
|---|---|---|
| 0–10 min | Erase one register in the repetition encoding | Students show exactly which coherence disappears |
| 10–25 min | Write all three qutrit codewords and check orthogonality | Students can translate the modular-arithmetic formula into vectors |
| 25–50 min | Trace a diagonal and an off-diagonal encoded matrix unit | Students see why checking basis-state probabilities alone is insufficient |
| 50–80 min | Derive and apply the two-share permutation decoder | Students recover a superposition with a complex phase |
| 80–105 min | Check logical $X,Z$ representatives and the disjoint-recovery contradiction | Students distinguish agreement on the code from equality of physical operators |
| 105–120 min | Worked input, questions, and exit statement | Students can say what the decoder proves about an unknown state |

**Board discipline.** Use $i$ for the logical label and $r$ for the summed physical label. Circle the instruction “modulo three.” For the decoder, show both its inverse and its action on an encoded basis vector. The relabeling $s=r+2i$ is the decisive step: the auxiliary state loses its dependence on the logical input.

**Likely difficulty.** Students may mistake the two overlapping reconstructions for two independent copies. Draw the three physical shares in a row and mark the authorized pairs. The pairs overlap. Then use commuting representatives on genuinely disjoint regions to explain the obstruction.

**A second difficulty.** The equation $V^\dagger x_1V=cI$ does not say that $x_1$ preserves the code. Contrast it with $O_{12}V=VO$. Ask which equation is needed to compose reconstructed operators.

**If discussion needs more time.** Work one pair in class and leave the cyclic pairs to the exercise session. Defer the reference-system derivation and entropy table; retain their conclusions as targets the self-study section will prove. Lecture 4 begins by recalling the entropy calculation.

**Exit question.** What extra fact must hold beyond “the three encoded basis states can be decoded”?

**Expected answer.** The same linear decoder must preserve all off-diagonal matrix units, hence every superposition and every correlation with an external reference. Here the factorization identity supplies that fact.

**After class.** Assign Problems 1–4. Use the reference-system problem as the central self-study check. The noise problem is optional and must state that the lost position is known.

**Transition.** An entangled auxiliary state appeared without being chosen for each input. Next calculate the operator structure carried by a fixed entangled state.

## Lecture 3: modular structure before the abstract theorem

Use [[lecture-03-modular-structure|Lecture 3]].

| Time | Board calculation or activity | Evidence of understanding |
|---|---|---|
| 0–20 min | Schmidt weights, matrix units, cyclic and separating | Students identify the role of nonzero weights |
| 20–50 min | Compute $S_T$, $J$, and $\Delta$ on basis vectors | Students keep the Tomita map antilinear |
| 50–75 min | Work the unequal-qubit example and rotate $X$ | Students can distinguish $K_A$ from $-\log\Delta$ |
| 75–95 min | Substitute a Gibbs state into the modular flow | Students obtain physical time $s=\beta t$ with the chosen sign |
| 95–110 min | Normalize the oscillator thermofield double and take its partial trace | Students recognize a thermal state from its spectrum |
| 110–120 min | Oscillator counterexample, questions, and exit check | Students do not infer an algebraic type from one modular spectrum |

This divides the oscillator allocation in the lecture into 15 minutes of calculation and 10 minutes of interpretation and questions.

**Board discipline.** Compute $S_T|i,j\rangle$ first. Do not guess $\Delta$ from an analogy with a density matrix. Keep the three equations $\Delta=\rho_A\otimes\rho_B^{-1}$, $K_A=-\log\rho_A$, and $\widehat K=K_A-K_B$ visible with tensor identities where needed.

**Likely difficulty.** Students may silently treat $S_T$ as linear. Apply it to $i|i,j\rangle$ before computing its square. Another useful check is $\Delta\Omega=\Omega$, which a one-sided density matrix generally fails.

**KMS placement.** In class, explain that the condition compares two orderings at an imaginary-time separation. The analytic matrix proof in Section 6 is self-study. If the students already know thermal Green functions, use the qubit matrix-unit example in place of part of the oscillator discussion.

**If discussion needs more time.** Normalize the oscillator state and display the reduced probabilities. Defer the entropy sum. Preserve the point that an unbounded modular operator is compatible with a type-I oscillator algebra.

**Exit question.** A state is Gibbs for $H$. What is the relation between its modular parameter and Heisenberg time, and does every modular flow define the physical Hamiltonian of the system?

**Expected answer.** With the declared convention, $\sigma_t=\alpha_{\beta t}$. For a general faithful state one may define $-\log\rho$, but identifying it with a prescribed physical Hamiltonian is additional input.

**After class.** Assign Problems 1–4. Use Problems 5–7 to test the KMS sign and oscillator limits. Treat the spacetime comparison as a reading exercise, not as a theorem established by the finite calculation.

**Transition.** The logarithm of a state gives a generator, while its expectation gives entropy. Return to encodings and calculate how both change when a fixed entangled factor is added.

## Lecture 4: an entropy formula and the meaning of its terms

Use [[lecture-04-entropy-and-algebraic-codes|Lecture 4]].

| Time | Board calculation or activity | Evidence of understanding |
|---|---|---|
| 0–10 min | Recall the decoded qutrit pair and its spectrum | Students derive $S(\rho_{12})=S(\rho)+\log3$ |
| 10–30 min | Build the factor code and reconstruct the two commuting logical algebras | Students identify what each physical region can recover |
| 30–60 min | Derive entropy additivity and work the four-qubit example | Students separate variable logical information from fixed auxiliary entropy |
| 60–95 min | Teach the explicit two-sector, three-level example in Section 8 | Students calculate three distinct entropies for the same preparation |
| 95–110 min | State the general central-operator formula and its gravitational comparison | Students identify the extra geometric assumptions still needed |
| 110–120 min | Questions and exit explanation | Students avoid equating the restricted algebra's entropy with the full logical entropy |

**Teach the center by example.** Section 8 can precede Section 7. Compute the physical spectrum $\{p,(1-p)/2,(1-p)/2\}$ before introducing a general direct sum. Then identify the common sector measurement. A phase between the two sectors is present globally but absent from either local algebra.

**Likely difficulty.** “The global input is pure, so the bulk/algebra entropy term must vanish.” At $p=1/2$, compare the three numbers explicitly: full logical entropy $0$, restricted diagonal-algebra entropy $\log2$, physical-region entropy $3\log2/2$. Ask which observables each entropy refers to.

**If discussion needs more time.** Defer the full direct-sum derivation and the relative-entropy/modular calculations. Keep the explicit center example; it supplies the algebraic content that a constant auxiliary term alone would miss.

**Exit question.** Which step in the finite calculation proves that $\mathcal L_A$ is the area of an extremal surface?

**Expected answer.** None. The calculation proves an entropy identity with a central operator fixed by the encoding. A metric, a gravitational regime, and an extremal-surface prescription are additional ingredients.

**After class.** Assign Problems 1–4. The self-study section develops relative entropy, compression, and the first law; Problems 5–7 check distinguishability and entropy accounting. Students beginning a course project can compare the factor and central examples before reading a general code theorem.

## What students should be able to reconstruct after the block

Give a preparation, an encoding, and a specified accessible region. Ask students to:

1. identify the accessible algebra and compute the restricted state;
2. show whether the input can be recovered, using one map on every logical state;
3. calculate the entropy terms and identify which ones are fixed by the encoding;
4. distinguish exact model statements from proposed geometric interpretations.

A useful ten-minute written check is to revisit the central code at $p=1/2$ with a variable phase. Students should calculate the local spectrum, explain the phase's invisibility, and state why both regions can recover the central label without cloning a qubit.

Lectures 5–7 add finite constrained algebras, small tensor networks, and a deformation that spoils recovery before passing to continuum QFT. Their purpose is to expose exactly where tensor-factor reasoning ceases to be adequate. All 32 lecture drafts are now written. The [[courses/ads-cft-course/syllabus|syllabus]] gives the full sequence, and the [[course-instructor-guide|complete instructor guide]] supplies the continuation routes.

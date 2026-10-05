---
title: "Bibliography and source versions — Geometric QCD"
type: appendix
course: geometric-qcd-course-guide
modified: 2026-10-05
---

# Bibliography and source versions

This map separates supplied lecture pages, primary research sources, and instructional bridges. Metadata and versions were checked on 4 October 2026. Publication is evidence of provenance, not an independent verification of every argument.

## Core source

**Alexander Migdal, IAS lectures, 27 March 2026, 142 pages.** The supplied [PDF](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf) is the main source for the course's reconstruction. Page numbers refer to PDF/slide pages, which agree. [[courses/geometric-qcd-course/source-map|The page map]] covers all 142 pages.

**Alexander Migdal, Geometric QCD I: The Hodge-Dual Surface and Quark Confinement.** [arXiv:2511.13688](https://arxiv.org/abs/2511.13688), version 7 dated 16 February 2026; *Nuclear Physics B* **1025** (2026), 117380, [publisher DOI](https://doi.org/10.1016/j.nuclphysb.2026.117380). Use for the proposed geometric and variational construction. III.5 tests the formulas actually supplied in the lecture PDF.

**Alexander Migdal, Geometric QCD II: The Confining Twistor String and Meson Spectrum.** [arXiv:2602.21129v4](https://arxiv.org/abs/2602.21129v4), dated 23 March 2026; *Nuclear Physics B* **1026** (2026), 117424, [publisher DOI](https://doi.org/10.1016/j.nuclphysb.2026.117424). Use Appendix C for the reported finite-system diagnostics and the spectral sections for the fit protocol. The IAS fourth-order tensor and the Appendix C representative differ; II.5 preserves this discrepancy.

**Source computational notebook:** [MLEAlgebraic.nb](https://www.wolframcloud.com/obj/sasha.migdal/Published/MLEAlgebraic.nb), cited by Part II. This course does not claim to have executed or certified that notebook. A research reproduction must freeze its inputs and export the equations and certificate.

## Module 1

- **Primary:** G. 't Hooft, *A planar diagram theory for strong interactions*, *Nuclear Physics B* **72** (1974), 461–473. [Author-hosted paper](https://webspace.science.uu.nl/~hooft101/gthpub/planar_diagram_theory.pdf), [DOI](https://doi.org/10.1016/0550-3213(74)90154-0). Read for ribbon topology and color scaling.
- **Primary:** Yu. M. Makeenko and A. A. Migdal, *Exact equation for the loop average in multicolor QCD*, *Physics Letters B* **88** (1979), 135–137. [Publisher record](https://www.sciencedirect.com/science/article/pii/037026937990131X). Read for the original loop-equation context; compare conventions with I.5.
- **Gentler:** the matrix/Gaussian and Fourier/distribution bridges in this course.
- **Research:** IAS pp. 20–42; define a crossing regulator and operator basis before comparing renormalized equations.

## Module 2

- **Primary:** IAS pp. 43–65 and Part II's momentum-loop discussion and Appendix C.
- **Primary background:** A. Migdal, *Second Quantization of the Wilson Loop*, [arXiv:hep-th/9411100](https://arxiv.org/abs/hep-th/9411100). Use for the operator-representation context.
- **Gentler:** II.4's rectangle, II.5's complete model system, and II.7's free-word basis.
- **Research:** the source notebook and exact rational matrix export. Source dimensions alone are not a reproduced rank computation.

## Module 3

- **Primary:** IAS pp. 66–91 and Part I's proposed surface construction.
- **Gentler:** the forms/complex-analysis bridge and III.5's circle and ellipse.
- **Research:** compare the tensor definition, boundary correspondence, area variation, and functional domain before claiming a zero mode. General names such as uniformization or a bridge principle do not replace their hypotheses and a calculation for this surface.

## Module 4

- **Primary:** IAS pp. 92–110 and Part II's surface-fermion construction.
- **Instructional background:** P. Ginsparg, *Applied Conformal Field Theory*, [arXiv:hep-th/9108028](https://arxiv.org/abs/hep-th/9108028). Use for two-dimensional fermions and conformal methods; its conventions must be translated.
- **Gentler:** the Grassmann bridge, IV.2's coframe calculation, and IV.6's test-function proof.
- **Research:** a regulated operator with its boundary domain, full determinant normalization, cancellation map, and contact matching.

## Module 5

- **Primary:** IAS pp. 111–142 and Part II's spectral construction.
- **Primary comparison:** E. Witten, *Perturbative Gauge Theory As A String Theory In Twistor Space*, [arXiv:hep-th/0312171](https://arxiv.org/abs/hep-th/0312171). This is the topological B-model proposal used for the limited comparison in V.4.
- **Primary chiral framework:** R. Kaiser and H. Leutwyler, *Large $N_c$ in chiral perturbation theory*, [arXiv:hep-ph/0007101](https://arxiv.org/abs/hep-ph/0007101). Use to distinguish a model's pion limitation from a general statement about the planar limit.
- **Gentler:** V.5's explicit surface, V.6's stationary equations, and V.7's threshold expansion.
- **Research data:** a fit audit must name the exact Particle Data Group edition and preserve its selected state table. No current mass values have been silently substituted for the source fit.

## What was checked

The revision checked primary records, the supplied slide equations, and the explicit model calculations recorded in the validation report. It did not perform a complete line-by-line certification of both research papers, a new nonperturbative QCD proof, a notebook reproduction of the eighth-order system, or a refit of all meson data.

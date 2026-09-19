---
title: "Neural networks and LLMs — Glossary"
type: glossary
course: nn-llm-syllabus
status: draft
modified: 2026-09-19
---

# Glossary

This is a lookup page. Weekly notes also define the terms where their
calculations first need them. Start with [[nn-llm-start-here]] to see the
objects working together.

| Term | Meaning in this course | Calculation |
|---|---|---|
| Token; tokenizer | A unit of text; the rule that splits text into units and assigns their integer labels. A token need not be a whole word. | [[week-01-inferring-a-distribution\|1]], [[week-07-representations-and-position\|7]] |
| Vocabulary | The finite set of allowed token labels. | [[week-01-inferring-a-distribution\|1]] |
| Corpus; dataset | A collection of observed text; more generally a collection of observations. | [[week-01-inferring-a-distribution\|1]] |
| Context | The tokens supplied before the token to be predicted. | [[week-01-inferring-a-distribution\|1]] |
| Parameter; weight; bias | An adjustable number; a coefficient multiplying an input; an additive offset. Parameters are fixed during generation. | [[week-03-perceptron-and-cover\|3]] |
| Score; logit | A real number assigned to an alternative before normalization. It need not lie between zero and one. | [[week-01-inferring-a-distribution\|1]] |
| Softmax | Exponentiate a list of scores and divide each exponential by their sum. The result is a probability vector. | [[week-01-inferring-a-distribution\|1]] |
| Likelihood | Probability assigned to the observed data, viewed as a function of parameters. | [[week-01-inferring-a-distribution\|1]] |
| Loss; cross-entropy | A prediction error criterion; here usually the average negative logarithm of the probability assigned to observed targets. | [[week-01-inferring-a-distribution\|1]] |
| Training; gradient descent | Adjust parameters using observed examples; one method moves against the derivative of the loss. | [[week-03-perceptron-and-cover\|3]], [[week-10-gradients-and-generation\|10]] |
| Test data; generalization | Observations kept out of fitting; prediction performance on fresh observations. | [[week-01-inferring-a-distribution\|1]] |
| Neuron; activation | An affine combination of inputs followed by a specified function; that function, often nonlinear. | [[week-03-perceptron-and-cover\|3]] |
| Layer; hidden representation | A stage of the calculation; the intermediate vector it computes before the final output. | [[week-03-perceptron-and-cover\|3]] |
| Backpropagation | Apply the chain rule from output to input, reusing intermediate derivatives to compute all parameter gradients. | [[week-03-perceptron-and-cover\|3]] |
| Embedding | A learned vector assigned to each token. | [[week-07-representations-and-position\|7]] |
| Query; key; value | The vector used to form comparisons; the vector it is compared with; the vector averaged using the resulting weights. | [[week-06-attention-from-an-energy\|6]], [[week-08-one-head-and-a-decoder\|8]] |
| Attention head | One set of query, key and value projections and the weighted mixing they define. | [[week-08-one-head-and-a-decoder\|8]] |
| Causal mask | A restriction that prevents a position from using later positions. | [[week-08-one-head-and-a-decoder\|8]] |
| Residual connection | Add a sublayer's output to its input. The added vector is not assumed small. | [[week-08-one-head-and-a-decoder\|8]] |
| Feed-forward sublayer | A learned nonlinear map acting on each position separately, with shared parameters across positions. | [[week-08-one-head-and-a-decoder\|8]] |
| Normalization | In this decoder, rescale each position's feature vector using its component mean and variance, then apply learned scales and offsets. | [[week-08-one-head-and-a-decoder\|8]] |
| Decoder; autoregressive | A model that predicts the next token from preceding tokens; generation repeats this operation, appending each selected token. | [[week-08-one-head-and-a-decoder\|8]], [[week-10-gradients-and-generation\|10]] |
| Batch; epoch | A group of examples used for one gradient estimate; one pass through the training dataset. | [[week-10-gradients-and-generation\|10]] |
| Capacity; load | Feasibility or retrieval limit under a specified criterion; typically the number of random patterns divided by the number of components. | [[week-03-perceptron-and-cover\|3]]–[[week-05-hopfield-and-capacity\|5]] |
| Recurrence | Reuse a state-update map over internal iterations. Weight sharing distinguishes it from an arbitrary sequence of layers. | [[week-09-four-indices\|9]] |
| Decoding temperature | A positive number dividing output scores before sampling. It changes generation probabilities without retraining. | [[week-10-gradients-and-generation\|10]] |
| Diffusion score | The vector $\nabla_x\log q_k(x)$, a derivative of a density. It is not a vocabulary logit. | [[week-14-diffusion-and-thermodynamics\|14]] |

Symbols, including the different uses of $H$, $q$ and $\beta$, are recorded in
[[nn-llm-conventions]].

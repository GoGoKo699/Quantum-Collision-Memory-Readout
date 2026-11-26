# 30 milestones

The first 11 milestones build the model from qubit states, measurements and classical records. The remaining 19 derive the protocol and compare its guarantees with a blind reset and a noisy readout. The questions progress from single events to the complete inference problem. The [Watrous bridge](ANCHOR.md) names the source sections used for prerequisites.

## Background and preliminaries

### M01 Qubit states

**Question.** How does a density operator encode a direction and a degree of polarization?

**Target.** Read a Bloch vector as the three mean Pauli signs. Recognize the zero vector as a maximally mixed state and unit vectors as pure states.

**Dependencies and connection.** Start here. These coordinates describe both the controllable probe and the hidden bath.

**Sources.** [Watrous §2.1](ANCHOR.md), [collision model](../science/model.md).

### M02 Probe and bath registers

**Question.** Which state describes two qubits when only one of them is observed?

**Target.** Distinguish the joint state from its two marginals. Use the partial trace to recover the local state and recognize that correlations may be absent from either marginal.

**Dependencies and connection.** M01. A collision can change the bath and create joint correlations while access remains limited to the probe.

**Sources.** [Watrous §§2.1–2.2](ANCHOR.md), [two collisions](../science/model.md#two-collisions).

### M03 Quantum channels in Bloch coordinates

**Question.** What can a qubit channel do to the Bloch ball?

**Target.** Explain the affine shift and linear transfer of a qubit channel. Distinguish an input-independent replacement from retention of at least one input direction.

**Dependencies and connection.** M01–M02. The shift and transfer fully specify the bath channel that the protocol estimates.

**Sources.** [Watrous §2.2](ANCHOR.md), [tomography](../science/tomography.md).

### M04 Effects and observed outcomes

**Question.** How does a chosen probe measurement turn a state into an outcome distribution?

**Target.** Use the Born rule for effects and interpret the completeness relation. Relate a projective Pauli readout to the polarization along its measurement axis.

**Dependencies and connection.** M01–M02. The experiment uses Pauli settings in its construction, while the converse allows arbitrary probe POVMs.

**Sources.** [Watrous §2.3](ANCHOR.md), [probe access](../science/model.md#probe-access), [testing](../science/testing.md).

### M05 Conditional bath states

**Question.** How can an outcome on the probe specify a different state for the bath?

**Target.** Separate the probability of a result from the normalized conditional state. Interpret the trace of a subnormalized operator as the price of selecting its branch.

**Dependencies and connection.** M02, M04. This bookkeeping makes it possible to turn the middle probe reading into a bath preparation.

**Sources.** [Watrous §§2.2–2.3](ANCHOR.md), [tomography](../science/tomography.md).

### M06 Partial SWAP

**Question.** What physical effects occur between the identity and full exchange?

**Target.** Identify the identity, SWAP and commutator terms in the joint update. Distinguish the signed collision angle from the exchange probability.

**Dependencies and connection.** M02–M03. Later, longitudinal readouts eliminate the angle-sensitive commutator term exactly.

**Sources.** [Watrous §§1.1, 2.2](ANCHOR.md), [two collisions](../science/model.md#two-collisions).

### M07 A probe reset between collisions

**Question.** What does a reset remove from the system's evolution?

**Target.** Explain why a new probe preparation removes the previous probe state and its joint correlations, while the state of the bath can still depend on the earlier probe input and middle outcome.

**Dependencies and connection.** M02, M05–M06. The two reset interfaces differ by the information retained in a classical middle record.

**Sources.** [Watrous §§2.2–2.3](ANCHOR.md), [probe access](../science/model.md#probe-access), [related work](../references/RELATED_WORK.md).

### M08 Private signs and conditioning

**Question.** Why choose the preparation and reset signs independently at random?

**Target.** Identify the constant, single-sign and sign-product components of a probability table. Explain how conditioning changes the distribution of the private signs.

**Dependencies and connection.** M04–M07. Orthogonality of the sign components allows one event to encode both an offset and an input-dependent transfer.

**Sources.** [Watrous §1.2](ANCHOR.md), [tomography](../science/tomography.md).

### M09 Classical discrimination information

**Question.** How does the information in one record constrain a sequence of decisions?

**Target.** Distinguish one-block success from the cost of attaining high confidence over many blocks. Relate measured chi-square divergence, relative entropy, and information in a final binary decision.

**Dependencies and connection.** M04, M08. A rare outcome can have high relative contrast and determine the optimal weak-coupling exponent.

**Sources.** [Watrous §§1.2, 3.1](ANCHOR.md), [testing](../science/testing.md).

### M10 Attempts and accepted events

**Question.** How does a rare informative event translate into an experimental budget?

**Target.** Convert a target number of accepted signs into a budget of attempted blocks. Distinguish a bound on event probability from a bound on a conditional sign mean.

**Dependencies and connection.** M05, M08–M09. This accounts for both the cost of accessing the bath and the statistical precision of the resulting signs.

**Sources.** [Counting blocks](../science/model.md#counting-blocks), [tomography](../science/tomography.md).

### M11 The complete access model

**Question.** What is supplied, controlled, measured and charged in a two-collision block?

**Target.** Specify the fresh initial bath, the fixed intercollision map, the permitted drift, trusted probe operations, and the operations excluded from the comparison by the probe-only interface.

**Dependencies and connection.** M01–M10. Together these restrictions define a channel-identification task with unobserved coupling strengths and a matched memory test.

**Sources.** [Collision model](../science/model.md), [science overview](../science/README.md).

## Narrative and innovation

### M12 The first flip heralds a pure bath input

**Question.** What must have happened when the probe flips in its initial Pauli basis?

**Target.** Trace the exchange component through the flipped outcome and identify the bath state prepared on that branch. Explain why the first exchange strength affects the branch probability while the conditional state is exact.

**Dependencies and connection.** M05–M06, M11. This branch supplies one of the six Pauli eigenstates to the otherwise inaccessible bath channel.

**Sources.** [Tomography](../science/tomography.md), [worked example](README.md#worked-example).

### M13 The second flip reads one output component

**Question.** Why measure along the reset axis after the second collision?

**Target.** Explain how the second flip probability depends on the bath polarization along that axis. Identify where the perpendicular commutator contribution vanishes.

**Dependencies and connection.** M04, M06–M07, M12. The final flip converts unknown exchange into a scalar factor multiplying a bath-channel response.

**Sources.** [Tomography](../science/tomography.md), [worked example](README.md#worked-example).

### M14 The joint two-flip event

**Question.** What distribution do the two flips induce across the four pairs of signs?

**Target.** Combine the first heralding probability and second flip probability. Identify the shared prefactor, the term odd in the reset sign, and the term odd in the sign product.

**Dependencies and connection.** M08, M12–M13. This event law is the algebraic interface between the unknown channel and the estimator.

**Sources.** [Tomography](../science/tomography.md), [worked example](README.md#worked-example).

### M15 A moment for the affine shift

**Question.** Which average isolates bath polarization that is independent of the bath input?

**Target.** Derive the negative reset-sign mean among retained blocks and explain why averaging over the initial sign removes the transfer term.

**Dependencies and connection.** M03, M08, M14. This recovers the output of the channel on the maximally mixed input.

**Sources.** [Tomography](../science/tomography.md), [worked example](README.md#worked-example).

### M16 A moment for the transfer matrix

**Question.** Which average isolates the part of the bath output that responds to input polarization?

**Target.** Derive the negative product-sign mean among retained blocks and explain why the affine shift makes no contribution to it.

**Dependencies and connection.** M03, M08, M14–M15. The same block record supports both an output-offset estimator and a transfer estimator.

**Sources.** [Tomography](../science/tomography.md), [worked example](README.md#worked-example).

### M17 Full affine identification

**Question.** How do single-axis moment estimates determine the whole qubit channel?

**Target.** Use the three preparation axes and three readout axes to index the transfer coefficients. Locate each affine-shift component in the same set of measurements.

**Dependencies and connection.** M03, M15–M16. This assembles the locally estimated moments into one complete channel description.

**Sources.** [Tomography](../science/tomography.md).

### M18 Drifting and signed collisions

**Question.** Why is it possible to estimate a fixed channel while the collision strengths drift?

**Target.** Explain the role of each block's shared sign-independent prefactor. Identify why dependence of the current collision settings on the current private signs would invalidate cancellation.

**Dependencies and connection.** M08, M11, M14–M17. A varying acceptance frequency is compatible with a fixed conditional channel response.

**Sources.** [Collision model](../science/model.md), [tomography](../science/tomography.md).

### M19 An honest finite shot budget

**Question.** How many attempted blocks are needed for all channel entries to be accurate?

**Target.** Combine a lower bound on the accepted fraction, concentration of bounded signs and the finite number of axis pairs. Explain the accuracy, confidence and weak-exchange factors.

**Dependencies and connection.** M09–M10, M17–M18. This turns exact identifiability into a finite experiment with explicit resources.

**Sources.** [Counting blocks](../science/model.md#counting-blocks), [tomography](../science/tomography.md).

### M20 Blind reset sees a product of unknowns

**Question.** What ambiguity remains if the middle outcome is discarded?

**Target.** Identify the first exchange probability multiplying the transfer matrix in blind readout. Explain how distinct bath channels can then give identical data under unknown first collision strength.

**Dependencies and connection.** M06–M07, M11, M17. This distinguishes the channel-identification capability from blind detection of a nonzero transfer.

**Sources.** [Tomography](../science/tomography.md), [testing](../science/testing.md).

### M21 Replacement versus retention

**Question.** How can the sign statistics test for surviving input information?

**Target.** Link the transfer of a depolarizing-retention alternative to an accepted-sign contrast. Explain why the test statistic remains centered for replacement, including a replacement with a fixed bath polarization in the affine model.

**Dependencies and connection.** M03, M16, M20. The binary task supplies a matched operational benchmark for the two probe interfaces.

**Sources.** [Testing](../science/testing.md), [tomography](../science/tomography.md).

### M22 Constructing the blind test

**Question.** How can blind reset still test retention under unknown signed drift?

**Target.** Use only the final flip and the randomized signs. Track how the blind protocol obtains a larger accepted fraction at a weaker conditional sign contrast.

**Dependencies and connection.** M18, M20–M21. Comparing these two factors explains the different dependence of block counts on weak exchange.

**Sources.** [Testing](../science/testing.md).

### M23 The first collision bounds useful bath polarization

**Question.** How much conditional polarization can any middle measurement extract, on average?

**Target.** Relate the squared conditional Bloch lengths to the POVM effects and their branch probabilities. Recognize why rare pure bath states and frequent weak bath states obey the same weighted bound.

**Dependencies and connection.** M04–M06, M12, M21. This exposes the quantity through which a middle readout can change the information converse.

**Sources.** [Testing](../science/testing.md), [Watrous §§2.1, 2.3](ANCHOR.md).

### M24 The second collision bounds extractable information

**Question.** How much of a fixed bath perturbation can the final probe readout resolve?

**Target.** Distinguish components of the output perturbation parallel and perpendicular to the reset Bloch vector. Explain how the null probabilities limit measured chi-square divergence.

**Dependencies and connection.** M04, M06, M09, M13, M23. The resulting bound applies to all final POVMs on the probe.

**Sources.** [Testing](../science/testing.md), [Watrous §3.1](ANCHOR.md).

### M25 Exact per-block information

**Question.** When can preparation, reset and readout reach both information bounds at once?

**Target.** Identify the known-angle settings that attain the measured chi-square bounds. Separate these converse attainers from the drift-tolerant randomized protocol used to solve the inference task.

**Dependencies and connection.** M21–M24. Exact per-block optima establish the strongest information comparison for the matched known-angle instances.

**Sources.** [Testing](../science/testing.md).

### M26 From one block to minimax testing

**Question.** Why can classical adaptation across blocks not remove the sample gap?

**Target.** Apply the relative-entropy chain rule to conditional transcript laws. Explain why one fixed hard instance suffices for a lower bound over a model allowing drift.

**Dependencies and connection.** M09–M11, M19, M21–M25. This closes the comparison using all attempted blocks and connects testing to the tomography converse.

**Sources.** [Testing](../science/testing.md), [tomography](../science/tomography.md).

### M27 False intermediate reports

**Question.** What happens if the middle readout reports a flip when none occurred?

**Target.** Explain how false flips dilute the conditional bath polarization. Relate the crossover to the symmetric readout-error probability and the physical exchange probability.

**Dependencies and connection.** M12, M19, M22, M26. This shows when a midpoint record retains its weak-coupling advantage in the declared noise model.

**Sources.** [Readout noise](../science/readout-noise.md).

### M28 Verification and assumptions

**Question.** Which parts of the result are proved and which are checked by finite matrix calculations?

**Target.** Identify direct simulation checks of the two-flip event law and optimal measured divergence. Use extreme cases of zero transfer, full exchange or an uninformative middle readout to interpret the model assumptions.

**Dependencies and connection.** M17, M25–M27. Independent numerical checks support the derivation without extending its scope beyond the stated interface.

**Sources.** [Verification](../verification/README.md), [science overview](../science/README.md).

### M29 Relation to causal-break witnesses

**Question.** What can this protocol determine beyond the presence of causal memory?

**Target.** Distinguish the earlier partial-SWAP causal-break examples and randomized correlation witnesses from angle-independent reconstruction of a specified bath map. Identify which physical elements the project inherits.

**Dependencies and connection.** M07, M17–M18, M21, M26. Attribution places the exact identification and sample results in their operational context.

**Sources.** [Related work](../references/RELATED_WORK.md), [science overview](../science/README.md).

### M30 The complete readout argument

**Question.** Why does recording the middle flip change both identifiability and cost?

**Target.** Tell the complete story from a fresh hidden bath through the heralded input, randomized final readout, affine reconstruction, blind ambiguity and matched information bounds. Explain which assumption supports cancellation and which resource determines the weak-exchange rate.

**Dependencies and connection.** M11, M17–M20, M26–M29. This joins the physical mechanism, statistical guarantee and practical noise boundary into one access comparison.

**Sources.** [Science overview](../science/README.md), [worked example](README.md#worked-example).

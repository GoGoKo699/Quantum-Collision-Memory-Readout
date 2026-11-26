# Quantum Collision Memory Readout

**Can two uncalibrated probe collisions identify the channel of an inaccessible qubit?** Yes. A middle Pauli readout occasionally prepares a known input on the bath. A randomized probe reset and a second readout then remove both unknown exchange strengths from the estimator.

Every block starts with a maximally mixed bath qubit. Its fixed, unknown channel acts between two partial-SWAP collisions with the probe. The collision angles may change in magnitude and sign between blocks. The probe requires trusted Pauli preparations and measurements, private random bits and classical records.

| Task | Worst-case blocks at fixed accuracy or gap and confidence |
| --- | --- |
| Estimate the full bath channel with ideal readouts | $`\Theta(p^{-2})`$ |
| Detect depolarizing memory with a middle readout | $`\Theta(p^{-2})`$ |
| Detect the same memory with a blind reset | $`\Theta(p^{-3})`$ |
| Detect memory with middle report error $`q`$ | $`\Theta((p+q)p^{-3})`$ |

Here $`p`$ is a positive lower bound on either collision's transfer probability. The count includes runs without two flips.

For Pauli axes $`u,v`$, choose independent fair signs $`P,R`$. Prepare the probe along $`Pu`$ before its first collision and along $`Rv`$ before its second. Retain the signs for blocks in which both projective readouts disagree with the corresponding preparation. If the bath map in Bloch coordinates is $`r\mapsto \ell+Tr`$, then

```math
\mathbb E[-R\mid\text{two flips}]=v\cdot\ell,\qquad
\mathbb E[-PR\mid\text{two flips}]=v^{\mathsf T}Tu.
```

Nine axis pairs recover all twelve real coefficients. With a known symmetric middle-report error $`q<1/2`$, a reweighted estimator still recovers the full map. In weak coupling its block count has the additional factor $`(1+q/p)/(1-2q)^2`$ relative to ideal readout. The same bath map can be unidentifiable with a blind reset because the first collision strength multiplies its transfer matrix in every accessible statistic.

## Read and reproduce

| Question | Route |
| --- | --- |
| What is supplied and counted? | [Model](science/model.md) |
| How do the flips identify the bath map? | [Tomography](science/tomography.md) |
| What information can any probe-only tester obtain? | [Detection and converses](science/testing.md) |
| How does middle readout error change the result? | [Noisy detection](science/readout-noise.md) and [calibrated noisy tomography](science/calibrated-tomography.md) |
| Which ingredients come from earlier studies? | [Related work](references/RELATED_WORK.md) |
| How can I work through the derivation? | [Learning guide](learning/README.md) |
| How can I check the finite examples? | [Verification](verification/README.md) |

Run the seeded matrix checks with Python 3 and NumPy.

```bash
python3 verification/verify_collision_readout.py
```

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

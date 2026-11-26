# Model and resources

## Two collisions

The lab controls a probe qubit $`S`$. A bath qubit $`E`$ begins each block in the maximally mixed state, independent of the probe and the past. The interactions are

```math
U_{\theta_i}=\cos(\theta_i)I-i\sin(\theta_i)\,\mathrm{SWAP},\qquad
p_i=\sin^2(\theta_i)\ge p>0,\quad i\in\{1,2\}.
```

The angles may have either sign. They are unknown in the calibration-free problems and may change independently between collisions and across blocks. They may depend on past blocks and public settings. The current parameters are chosen independently of the block's private random signs and measurement outcomes. A fixed bath CPTP map $`\mathcal E`$ acts once between collisions. Write its action in Bloch coordinates as $`r\mapsto\ell+Tr`$, with $`\ell\in\mathbb R^3`$ and $`T\in\mathbb R^{3\times 3}`$. The probe's Pauli axes label the same coordinates as the ideal SWAP.

The binary problem uses $`\mathcal E_\eta(\rho)=\eta\rho+(1-\eta)I/2`$. The null is $`\eta=0`$ and the alternative is $`\eta\ge\eta_0>0`$. For testing, $`\eta`$ can vary between blocks subject to the gap and independence from current private choices. Tomography instead uses one fixed $`(\ell,T)`$.

## Probe access

The lab prepares the probe, discards it after the first collision and supplies a freshly prepared probe before the second. With a recorded break the lab may measure the old probe and keep its classical outcome. The ideal converse allows arbitrary probe POVMs and outcome-conditioned reset preparations and final measurements. The blind comparator discards the old probe and supplies a reset without learning any first-collision outcome. Both interfaces allow classical memory and adaptation between blocks. Both use one probe at each contact without a quantum ancilla. The second-angle promise and initial bath preparation are the same for both.

The noisy-readout extension has one binary middle measurement, whose reported bit passes through an independent symmetric flip of probability $`q`$. State preparation, reset and the final measurement are ideal. The error acts on the classical report, leaving the bath conditioned on the actual quantum measurement. Repeated readout, extra first-collision-only assays and retained quantum registers would change the resource model.

## Counting blocks

Every block costs two collisions and a fresh bath preparation, including blocks rejected by the estimator. All protocols specify a hard cap on total attempts. Failure means the worst probability of an incorrect decision or of exceeding the requested entrywise estimation error. The logarithmic confidence rates use failure probabilities at most $`1/4`$. The converses hold for single-probe testers with the indicated intermediate interface and unlimited classical records.

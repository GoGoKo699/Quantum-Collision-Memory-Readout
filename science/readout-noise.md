# Noisy middle readout

A symmetric error in the middle measurement changes the number of collision blocks needed to detect retained bath polarization. The exact crossover occurs when the report error and the minimum population-transfer probability are comparable.

## Model and result

Each block starts with a fresh bath qubit in $`I/2`$. The probe interacts twice with the bath by partial SWAPs $`U_i=\cos\theta_i I-i\sin\theta_i\,\mathrm{SWAP}`$. Write $`p_i=\sin^2\theta_i`$ and assume $`p_i\geq p>0`$. The null replaces the bath by $`I/2`$ in the gap. The alternative applies a depolarizing map whose Bloch shrinkage is $`\eta\in[\eta_0,1]`$, with $`\eta_0>0`$. The two angles and the shrinkage may vary across blocks and depend on past data. The parameters of a block are set before its current private random choices and measurement outcomes.

Between collisions the controller can make a single binary probe measurement. An independent classical bit flip with probability $`q\in[0,1/2]`$ corrupts its report. The measured probe is discarded, and the controller prepares the second input from scratch. It has only the reported bit from the first measurement and may condition its reset and final measurement on that bit. The probe preparations and final readout are ideal. Across blocks, only classical data are retained. For the upper bound the experimenter knows $`q`$, $`p`$ and $`\eta_0`$.

For both error probabilities at most $`\delta\in(0,1/4]`$, the minimax number of attempted blocks is

```math
N_\star=\Theta\!\left(\frac{p+q}{\eta_0^2p^3}\log\frac1\delta\right).
```

The constants are uniform over the ranges above. Every trial uses two collisions and counts toward the budget. The order is $`p^{-2}`$ at $`q=0`$ and becomes $`p^{-3}`$ as $`p\to0`$ with fixed $`q>0`$, at fixed signal and confidence. With $`q=1/2`$ the middle report is independent of the true outcome and the order equals the blind-reset bound.

## Fixed randomized receiver

Prepare the $`+1`$ eigenstate of $`Z`$, perform the first collision and measure $`Z`$. Write $`W=1`$ for a report of a flip from the preparation. Independently draw a fair sign $`R`$ and reset the probe to the $`R`$ eigenstate of $`Z`$. After the second collision, measure $`Z`$ and write $`F=1`$ if the outcome is $`-R`$. Keep $`-R`$ when $`W=F=1`$. This selection can be done offline.

Put $`\kappa=1-2q`$ and $`r_1=q+\kappa p_1/2`$. The two unnormalized bath states for the *true* middle flip and for ignoring that outcome have Bloch numerators $`p_1 z/2`$ and $`p_1 z`$, respectively, where $`z`$ is the $`Z`$ axis. The corrupted flip report combines them with coefficients $`\kappa`$ and $`q`$. Its probability is $`r_1`$ and its Bloch numerator is still $`p_1 z/2`$. A longitudinal final readout sees only the population transfer, since the partial-SWAP commutator is orthogonal to $`z`$. Thus

```math
\Pr(W=F=1\mid R)=\frac{p_2}{2}\left(r_1-R\eta\frac{p_1}{2}\right),\qquad
\Pr(W=F=1)=\frac{p_2r_1}{2},\qquad
\mathbb E[-R\mid W=F=1]=\frac{\eta p_1}{2r_1}.
```

These identities hold for arbitrary signs of both collision angles. Set $`r_*=q+\kappa p/2`$, $`a_*=p r_*/2`$ and $`\mu_*=\eta_0p/(2r_*)`$. Conditional on the past, the acceptance probability is at least $`a_*`$. The accepted sign has mean zero under the null and mean at least $`\mu_*`$ under the alternative, since $`x/(2q+\kappa x)`$ is nondecreasing for $`x>0`$. These lower bounds also hold after averaging latent block parameters independent of the current private choices.

Choose $`K=\lceil 8\mu_*^{-2}\log(4/\delta)\rceil`$ and $`N=\lceil 4K/a_*\rceil`$. If at least $`K`$ trials are accepted, compare the mean of the first $`K`$ accepted signs with $`\mu_*/2`$. Otherwise return the null. The number accepted after $`N`$ blocks stochastically dominates a binomial with parameters $`N,a_*`$, by iterating the conditional probability lower bound. For the accepted signs, the conditional mean inequalities hold at each acceptance time. One can see this by summing the one-block inequality over all possible times of the next acceptance, conditioning on previous failures to accept. The bounded-increment exponential bound then gives a one-sided deviation probability at most $`\exp(-K\mu_*^2/8)`$. Conceptually extending the run to generate the first $`K`$ accepts and comparing them incurs only the additional binomial lower-tail probability when the fixed budget ends early. This proves the upper bound with $`N=O(r_*\eta_0^{-2}p^{-3}\log(1/\delta))`$.

The [matching converse](readout-noise-converse.md) gives the exact one-block information on a sign-randomized hard instance and the same worst-case order.

## Effect on channel reconstruction

For a general bath map $`x\mapsto\ell+Tx`$, choose a fair initial sign $`P`$ along axis $`u`$ and a fair reset sign $`R`$ along $`v`$. Conditional on the corrupted first flip and the final flip, the means of $`-R`$ and $`-PR`$ are $`v\cdot\ell`$ and $`[p_1/(2r_1)]v^{\mathsf T}Tu``, respectively. The second moment therefore contains an angle-dependent attenuation for $`q>0`$. If $`q<1/2`$ is known, the weight $`h(W)=(W-q)/(1-2q)`$ has conditional mean equal to the true flip indicator. For each block, $`\mathbb E[h(W)\mathbf1_F]=p_1p_2/4`$, and the same expectation with an additional factor $`-PR`$ equals $`(p_1p_2/4)v^{\mathsf T}Tu`$. The ratio removes the angle dependence at the moment level. [Calibrated tomography](calibrated-tomography.md) proves the sharp weak-coupling rate for recovering the full map.

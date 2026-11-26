# Converse for noisy middle readout

Use the [noisy middle-readout model](readout-noise.md) and its population-transfer parameters.

## Optimal information on a sign-randomized instance

Use independent fair signs of each angle with fixed magnitudes in both hypotheses. In a minimax lower bound this is a mixture of legal drift histories. The odd commutator term of each collision averages to zero. The resulting joint evolution is the mixture of doing nothing and performing SWAP, with probabilities $`1-p_i`$ and $`p_i`$. The second angle sign is independent of the middle report and the reset it induces.

Let $`z`$ now be an arbitrary initial probe Bloch vector, and let the tester measure along unit vector $`n`$. For reported outcome $`m\in\{-1,+1\}`$, the effective middle effect is $`(I+m\kappa n\cdot\sigma)/2`$. The probability of the report and the resulting conditional bath Bloch vector are

```math
w_m=\frac{1+m\kappa(1-p_1)n\cdot z}{2},\qquad
b_m=\frac{p_1z}{1+m\kappa(1-p_1)n\cdot z}.
```

Consequently,

```math
\sum_m w_m\lVert b_m\rVert^2
=\frac{p_1^2\lVert z\rVert^2}{1-\kappa^2(1-p_1)^2(n\cdot z)^2}
\leq\frac{p_1^2}{1-\kappa^2(1-p_1)^2}.
```

For a reset with Bloch vector $`t`$, the null final probe is $`r_0=(1-p_2)t`$ and the alternative displaces it by $`d=\eta p_2 b_m`$. For any final POVM with effects $`a_j(I+v_j\cdot\sigma)`$, the measured Pearson divergence is

```math
\chi^2=\sum_j a_j\frac{(d\cdot v_j)^2}{1+r_0\cdot v_j}.
```

With components parallel and perpendicular to $`r_0`$, weighted Cauchy–Schwarz bounds $`(d\cdot v_j)^2`$ by $`[\lVert d_\perp\rVert^2+d_\parallel^2/(1-\lVert r_0\rVert^2)][1-(r_0\cdot v_j)^2]`$. Use $`\sum_j a_j=1`$ and $`\sum_j a_j v_j=0`$ to sum the bound. It follows that the measured divergence is at most $`\lVert d\rVert^2/(1-\lVert r_0\rVert^2)\leq \eta^2 p_2\lVert b_m\rVert^2/(2-p_2)`$. For $`r_0=0`$, the same result follows directly from ordinary Cauchy–Schwarz. A pure reset parallel to $`b_m`$ and the projective readout of that axis attain the last bound.

The middle report has the same marginal law under both hypotheses, so its weighted conditional divergences add. The exact optimal one-block Pearson divergence on this sign-randomized instance is

```math
\chi^2_\star=\frac{\eta^2p_1^2p_2}{(2-p_2)[1-\kappa^2(1-p_1)^2]}.
```

A pure initial probe and a parallel projective middle measurement attain the earlier middle-stage bound. A skipped middle measurement is no stronger. The upper bound also covers a binary POVM followed by the same report error, since it is a classical mixture of projective and deterministic binary measurements. Revealing the mixture choice only improves the tester, and the divergence bound holds for each component.

Take $`p_1=p_2=p`$ and $`\eta=\eta_0`$. The denominator factor $`1-\kappa^2(1-p)^2=4r_*(1-r_*)`$ is of order $`p+q`$. The per-block relative entropy is bounded by $`\chi^2_\star`$. The chain rule gives a bound of $`N\chi^2_\star`$ on the transcript relative entropy for any classically adaptive tester. A decision with both errors at most $`\delta`$ requires transcript relative entropy at least $`(1-2\delta)\log((1-\delta)/\delta)`$. This proves the matching lower order.


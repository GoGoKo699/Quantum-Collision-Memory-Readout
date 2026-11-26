# Detecting bath memory

## A pair of randomized tests

Set $`u=v=Z`$ in the [two-flip experiment](tomography.md), with depolarizing retention $`\eta`$. The accepted sign $`-PR`$ has conditional mean $`\eta`$ and the acceptance probability is $`p_1p_2/4`$. Choose a hard budget large enough to collect $`K=O(\eta_0^{-2}\log(1/\delta))`$ accepted signs with failure probability at most $`\delta/2`$. Decide retention if their mean exceeds $`\eta_0/2`$. The null has conditional mean zero. The alternative always has conditional mean at least $`\eta_0`$. The same binomial domination and conditional Hoeffding bounds as for tomography use $`O(\eta_0^{-2}p^{-2}\log(1/\delta))`$ attempts.

For the blind test prepare $`PZ`$, discard the old probe, reset to $`RZ`$ and keep just the final flip. A flip now occurs with probability $`p_2/2`$ when averaged over the signs. Among accepted signs, $`-PR`$ has mean $`\eta p_1`$, since the first collision writes the unconditional bath polarization $`p_1PZ`$. The promised contrast is at least $`\eta_0p`$. Taking $`K=O((\eta_0p)^{-2}\log(1/\delta))`$ and dividing by the acceptance scale $`p`$ gives $`O(\eta_0^{-2}p^{-3}\log(1/\delta))`$ attempted blocks. Both tests count collisions in rejected trials. Neither uses a current angle estimate or a reset decision conditioned on the middle outcome.

## Exact information for known angles

Fix $`p_1,p_2>0`$ and their actual angles. Compare retention $`\eta`$ to replacement $`0`$. Write the measured divergence of distributions $`A,B`$ as $`\chi^2(A\Vert B)=\sum_x(A(x)-B(x))^2/B(x)`$, with common zero-probability outcomes omitted. The maximum over allowed probe-only testers is

```math
\chi^2_{\mathrm{recorded}}=\eta^2p_1p_2,\qquad
\chi^2_{\mathrm{blind}}=\eta^2p_1^2p_2.
```

To prove it, grant a classical flag for any mixture over pure initial Bloch vectors. Forgetting the flag cannot increase the divergence. For a pure input $`z`$ and middle effects $`a_m(I+n_m\cdot\sigma)`$, the branch probability is $`w_m=a_m[1+(1-p_1)n_m\cdot z]`$. The corresponding normalized bath vector is $`b_m`$ and

```math
w_m b_m=a_m[p_1z+\cos\theta_1\sin\theta_1(z\times n_m)].
```

The identities follow by expanding the partial SWAP and tracing out the measured probe. Put $`x_m=n_m\cdot z`$ and use $`\lVert n_m\rVert\le1`$. Then

```math
\sum_m w_m\lVert b_m\rVert^2
\le p_1\sum_m a_m
   \frac{1-(1-p_1)x_m^2}{1+(1-p_1)x_m}
\le p_1 .
```

For the last inequality the fraction is at most $`1-(1-p_1)x_m`$ and $`\sum_m a_m x_m=0`$. A projective measurement perpendicular to $`z`$ attains equality. For a blind reset $`b=p_1z`$ without any such branches.

For reset vector $`t`$, the final probe under the null has Bloch vector $`r_0=(1-p_2)t`$. Its change under retention is $`d=\eta[p_2b-\cos\theta_2\sin\theta_2(t\times b)]`$. For a final POVM with effects $`\beta_j(I+v_j\cdot\sigma)`$, its measured divergence is bounded by

```math
Q=\lVert d_\perp\rVert^2+
  \frac{\lVert d_\parallel\rVert^2}{1-\lVert r_0\rVert^2}.
```

Take components along and perpendicular to $`t`$. Weighted Cauchy–Schwarz bounds $`(d\cdot v_j)^2`$ by $`Q[1-(r_0\cdot v_j)^2]`$. Divide by the probability factor $`1+r_0\cdot v_j`$ and sum using $`\sum_j\beta_jv_j=0`$. Since $`1-(1-p_2)^2\ge p_2`$ and the perpendicular component contracts by at most $`\sqrt{p_2}`$ before multiplying by $`\eta`$, this gives $`Q\le\eta^2p_2\lVert b\rVert^2`$. Multiplying by the common midpoint branch probabilities establishes the stated upper bounds. For equality prepare $`z=Z`$, read $`X`$ at the break when a record is available, reset to $`X`$ and measure the final probe along its branch-specific change $`d`$. The known angles specify this final alignment. For $`\eta=0`$ the divergence vanishes for every measurement.

## Matching sample lower bounds

Fix the hard instance $`p_1=p_2=p`$ and $`\eta=\eta_0`$. The relative-entropy chain rule sums the conditional block divergences even for a tester that adapts its choices to the entire classical history. Each is at most the corresponding measured $`\chi^2`$, by $`\log x\le x-1`$. A decision with both error probabilities at most $`\delta\le1/4`$ has binary relative entropy at least $`c\log(1/\delta)`$ for an absolute constant $`c>0`$. This proves lower bounds matching both protocols' worst-case dependence on $`p,\eta_0,\delta`$.

For full channel estimation, take $`\eta=0`$ versus $`\eta=3\epsilon`$ at fixed angles and use the estimated $`T_{ZZ}`$ to decide the hypothesis. For $`0<\epsilon\le1/4`$ the two entrywise-accuracy intervals are disjoint and both retention values are physical. The recorded divergence bound now gives $`\Omega(p^{-2}\epsilon^{-2}\log(1/\delta))`$ attempts.

The gain concerns statistical information accumulated across attempts. A trace-distance contrast measures the change of a single decision probability. It does not account for information in a rare event's conditional sign or its occurrence rate.

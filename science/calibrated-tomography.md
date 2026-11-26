# Bath tomography with a calibrated imperfect middle readout

Consider the two-collision probe model with a fixed unknown qubit bath channel. The bath begins each block in $`I/2`$. The signed angles can depend on earlier observations and can be correlated with one another. Both angles are chosen before the current private random signs and current measurements. Each collision has transfer probability $`p_i=\sin^2\theta_i\ge p>0`$.

The middle measurement has one binary outcome. Its reported bit is flipped independently with known probability $`q\in[0,1/2]`$. The physical measurement still takes place, and its true outcome is unavailable. Probe preparations, resets and the final measurement are trusted. The converse allows any binary POVM for the middle measurement, arbitrary classically conditioned controls and any final POVM on the probe. Each block uses a single probe and a fresh bath, and only classical records persist.

Write the bath channel on Bloch vectors as $`r\mapsto\ell+Tr`$. The cost is the number of attempted blocks, including every discarded event.

## Result

For $`q<1/2`$, let $`\kappa=1-2q`$. An explicit estimator recovers every entry of $`\ell`$ and $`T`$ to absolute error $`\epsilon`$ with probability at least $`1-\delta`$, using

```math
O\!\left(\frac{p+q}{\kappa^2p^3\epsilon^2}\log\frac1\delta\right)
```

attempted blocks. For $`0<p\le1/2`$, $`0<\epsilon\le1/27`$ and $`0<\delta\le1/4`$ this order is minimax for the uncalibrated-angle model. The confidence statement holds under nonanticipating drift, with no estimate of either angle on any block. At $`q=0`$ the order reduces to $`p^{-2}\epsilon^{-2}\log(1/\delta)`$.

## Estimator

Fix a pair of Pauli axes $`u,v`$ and draw independent fair signs $`P,R`$. Prepare the probe along $`Pu`$, measure along $`u`$ after collision 1, reset along $`Rv`$, then measure along $`v`$ after collision 2. Let $`W`$ indicate that the reported middle result is opposite to $`P`$, and let $`F`$ indicate that the final result is opposite to $`R`$. The reset is chosen independently of both readouts.

Set $`e=v\cdot\ell`$ and $`t=v^\mathsf{T}Tu`$. The true middle flip occurs with probability $`p_1/2`$ and leaves the bath with Bloch vector $`Pu`$. Without a middle record the bath has Bloch vector $`p_1 Pu`$. Consequently the bath assemblage for $`W=1`$ has trace $`r_1=q+\kappa p_1/2`$ and subnormalized Bloch vector $`(p_1/2) Pu`$. The assemblage for $`W=0`$ has trace $`r_0=1-r_1`$ and the same subnormalized Bloch vector. Once the bath channel acts, the final flip along $`v`$ removes the partial-SWAP commutator term. This gives

```math
\Pr(W=w,F=1\mid P,R)
=\frac{p_2}{2}\left[r_w(1-Re)-\frac{p_1}{2}PRt\right].
```

Averaging the private signs yields the identities

```math
\begin{aligned}
\mathbb E[F]&=p_2/2,&
\mathbb E[-RF]&=(p_2/2)e,\\
\mathbb E[F(W-q)]&=\kappa p_1p_2/4,&
\mathbb E[-PRFW]&=(p_1p_2/4)t.
\end{aligned}
```

For each axis pair take the two ratios

```math
\widehat e=\frac{\sum -RF}{\sum F},\qquad
\widehat t=\frac{\kappa\sum -PRFW}{\sum F(W-q)}.
```

If a denominator is nonpositive, return zero for that ratio. Clip each estimate to $`[-1,1]`$. Run the nine axis pairs. For each output axis keep an estimate of its offset from any one of its three pairs.

### Concentration under drift

The moment identities hold conditionally on the past and the current angles. For the transfer estimate define the current weight $`s_i=p_{1,i}p_{2,i}`$ and set

```math
A_i=-4P_iR_iF_iW_i,\qquad B_i=4F_i(W_i-q)/\kappa.
```

Conditionally, $`\mathbb E A_i=s_i t`$ and $`\mathbb E B_i=s_i`$. Each of $`A_i-tB_i`$ and $`B_i-s_i`$ is a martingale difference. Its magnitude is $`O(1/\kappa)`$. To bound its second moment, note that

```math
\begin{aligned}
\mathbb E[F_iW_i]&=\frac{p_{2,i}}2(q+\kappa p_{1,i}/2),\\
\mathbb E[F_i(W_i-q)^2]&=\frac{p_{2,i}}2\left[q(1-q)+\kappa^2p_{1,i}/2\right].
\end{aligned}
```

Both conditional variances are bounded by $`C p_{2,i}(p_{1,i}+q/\kappa^2)\le C Hs_i`$, where $`H=1+q/(\kappa^2 p)`$ and $`C`$ is universal. Also $`1/\kappa\le 2H`$ for $`p\le1`$. The conditional Bernstein bound gives an exponential supermartingale with compensator at most $`C'\lambda^2 H\sum_i s_i`$ for $`|\lambda|\le c/H`$. Taking $`\lambda`$ proportional to $`a/H`$ on each tail gives, for either difference $`X_i`$ and $`0<a\le1/2`$,

```math
\Pr\!\left(\left|\sum_i X_i\right|>a\sum_i s_i\right)
\le 2\exp[-c' a^2 Np^2/H].
```

Here $`\sum_i s_i\ge Np^2`$ even when the angles are random and depend on past observations. Apply the bound with $`a=1/2`$ to the denominator and $`a=\epsilon/2`$ to $`A_i-tB_i`$. This controls the transfer estimate at cost $`O(Hp^{-2}\epsilon^{-2}\log(1/\delta))`$. The same argument with weight $`p_{2,i}/2`$, centered differences $`F_i-p_{2,i}/2`$ and $`-R_iF_i-eF_i`$, and bounded increments gives offset cost $`O(p^{-1}\epsilon^{-2}\log(1/\delta))`$. The union bound over the fixed set of axes leaves the stated order, since $`\kappa^2p+q`$ is comparable to $`p+q`$ with universal constants for $`0\le q<1/2`$ and $`0<p\le1`$.

## Lower bound with unknown angle correlations

The difficult instances use two depolarizing bath maps $`T_h=\eta_h I`$, $`\ell_h=0`$, indexed by $`h\in\{-1,1\}`$. On each block draw fair signs $`J_1,J_2`$ with $`\mathbb E[J_1J_2]=h a`$, where $`a=27\epsilon\le1`$. Use $`p_i=p(3+J_i)/2`$, which lies in $`[p,2p]`$. Independently and privately randomize each exchange angle sign. Averaging the sign turns its channel on system and bath into a classical mixture of identity and SWAP with probabilities $`1-p_i,p_i`$. The two hypotheses have matching first moments of both $`p_i`$. Their product moments and shrink factors satisfy

```math
C_h=\mathbb E_h[p_1p_2]=\frac{p^2}{4}(9+ha),\qquad
\eta_h=\frac{9}{2(9+ha)},\qquad
\eta_+C_+=\eta_-C_-.
```

The shrink factors lie between $`0.45`$ and $`0.5625`$, and their difference is $`9a/(81-a^2)\ge3\epsilon`$. Thus an estimator with entrywise error $`\epsilon`$ distinguishes the hypotheses.

Consider an arbitrary tester with initial probe Bloch vector $`z`$, a binary middle POVM with true effect $`G_m=\beta_m I+g_m\cdot\sigma`$ for outcome $`m`$, and reset Bloch vector $`t_m`$ chosen after report $`m`$. The effective reported effect is $`qI+\kappa G_m`$. Write $`b_m=q+\kappa\beta_m`$. Before the bath map, the reported branch has trace $`a_m=b_m+\kappa(1-p_1)g_m\cdot z`$ and unnormalized bath Bloch vector $`p_1 b_m z`$. After the second collision and averaging the random angles, the final branch has trace $`\bar a_m=\mathbb E_h[a_m]`$ and subnormalized probe Bloch vector

```math
\mathbb E_h[(1-p_2)a_m]t_m+\eta_h C_h b_m z.
```

The trace is the same under both hypotheses. The polarization term proportional to $`z`$ also agrees. Only the term proportional to $`t_m`$ changes, by $`\kappa (g_m\cdot z)(C_+-C_-)t_m`$. In each branch, the reference subnormalized state has both eigenvalues at least $`c p\bar a_m`$ for a universal $`c>0`$, because the depolarizing bath contributes at least $`(1-\eta_h)\mathbb E_h[p_2 a_m] I/2`$. For every final POVM effect $`E`$, the probability change is bounded by $`\operatorname{Tr}(E)`$ times the operator norm of the branch state change. Summing its square divided by the reference probability over the final effects bounds the branch contribution to measured $`\chi^2`$ by

```math
O\!\left(\frac{\kappa^2\lVert g_m\rVert^2(C_+-C_-)^2}{p\bar a_m}\right).
```

Since $`\lVert g_m\rVert\le\beta_m`$ and $`\bar a_m\ge q+\kappa p\beta_m`$, the factor $`\lVert g_m\rVert^2/\bar a_m`$ is at most $`1/(q+\kappa p)=O(1/(q+p))`$. A branch of identically zero trace contributes zero. The bound holds conditionally on private classical choices and all previous outcomes. Summing the two reported branches and using $`|C_+-C_-|=a p^2/2`$ gives $`O(\kappa^2\epsilon^2p^3/(q+p))`$ measured $`\chi^2`$ per block. Classical relative entropy is at most $`\chi^2`$, and its chain rule extends the bound to the adaptive transcript. A final test with both errors at most $`\delta\le1/4`$ needs relative entropy $`\Omega(\log(1/\delta))`$ by data processing to the test decision. This proves the minimax lower bound. The random angle mixtures give valid hard instances under a uniform guarantee over angle sequences.

## What the calibration buys

At $`q=1/2`$ the middle report is an independent fair bit. For a fixed second angle, every accessible probe law then depends on the first collision probability and the bath transfer matrix only through $`p_1T`$. When $`p<1`$, the instances $`p_1=p,\ T=I`$ and $`p_1=1,\ T=pI`$ with common $`\ell=0`$ are indistinguishable, even for infinitely many blocks. At $`p=1`$ both collisions fully swap, so the probe directly reads out the bath. Knowledge of the collision strengths supplies the scale $`p_1`$ and invalidates the matched-marginal argument used in the lower bound. For $`q<1/2`$ the ratio estimator uses the supplied readout-error rate to obtain that scale from the experiment itself.

The $`\kappa^{-2}`$ factor near a fair middle report concerns full channel identification when the nuisance angle correlations are unknown. A binary test against bath replacement has a finite shot bound even at $`q=1/2`$ because a recordless reset suffices. The tomography guarantee assumes an ideal final readout, exact $`q`$, private coin choices, maximally mixed bath initialization and an ancilla-free probe.

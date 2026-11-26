# Lower bound for calibrated bath tomography

The [calibrated estimator](calibrated-tomography.md) describes the apparatus, error model and notation. This argument addresses its minimax weak-coupling claim.

## Matched angle mixtures

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

The trace is the same under both hypotheses. The polarization term proportional to $`z`$ also agrees. Only the term proportional to $`t_m`$ changes, by $`\kappa (g_m\cdot z)(C_+-C_-)t_m`$. In each branch, the reference subnormalized state has both eigenvalues at least $`c p\bar a_m`$ for a universal $`c>0`$, because the depolarizing bath contributes at least $`(1-\eta_h)\mathbb E_h[p_2 a_m] I/2`$. For every final POVM effect $`E`$, the probability change is bounded by $`\mathrm{Tr}(E)`$ times the operator norm of the branch state change. Summing its square divided by the reference probability over the final effects bounds the branch contribution to measured $`\chi^2`$ by

```math
O\!\left(\frac{\kappa^2\lVert g_m\rVert^2(C_+-C_-)^2}{p\bar a_m}\right).
```

Since $`\lVert g_m\rVert\le\beta_m`$ and $`\bar a_m\ge q+\kappa p\beta_m`$, the factor $`\lVert g_m\rVert^2/\bar a_m`$ is at most $`1/(q+\kappa p)=O(1/(q+p))`$. A branch of identically zero trace contributes zero. The bound holds conditionally on private classical choices and all previous outcomes. Summing the two reported branches and using $`|C_+-C_-|=a p^2/2`$ gives $`O(\kappa^2\epsilon^2p^3/(q+p))`$ measured $`\chi^2`$ per block. Classical relative entropy is at most $`\chi^2`$, and its chain rule extends the bound to the adaptive transcript. A final test with both errors at most $`\delta\le1/4`$ needs relative entropy $`\Omega(\log(1/\delta))`$ by data processing to the test decision. This proves the minimax lower bound. The random angle mixtures give valid hard instances under a uniform guarantee over angle sequences.


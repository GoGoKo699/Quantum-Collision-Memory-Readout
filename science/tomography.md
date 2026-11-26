# Identifying the bath channel

## The two-flip experiment

Choose Pauli axes $`u,v`$ and independent fair signs $`P,R\in\{-1,1\}`$. Prepare the probe with Bloch vector $`Pu`$, collide, and measure along $`u`$. Flag the outcome $`-P`$. Discard the probe and prepare $`Rv`$ for the second collision, then flag outcome $`-R`$ along $`v`$. The random reset can be scheduled in advance.

The first flag occurs with probability $`p_1/2`$ and prepares the bath in the pure state $`Pu`$. Resolve the initial maximally mixed bath in the $`u`$ basis. The same-sign component cannot yield a probe flip. In the opposite-sign component, only the SWAP amplitude can yield a flip, and its bath output has sign $`P`$. After the unknown channel the bath Bloch vector is $`\ell+PTu`$.

For reset vector $`Rv`$ and bath vector $`b`$, the second probe Bloch vector is

```math
(1-p_2)Rv+p_2 b-\cos\theta_2\sin\theta_2(Rv\times b).
```

The final measurement along $`v`$ removes the cross product. Multiplying the two flag probabilities gives

```math
\Pr(A\mid P,R)=\frac{p_1p_2}{4}
  [1-R\,v\cdot\ell-PR\,v^{\mathsf T}Tu],
```

where $`A`$ is the event of two flips. Thus $`\Pr(A)=p_1p_2/4`$ and

```math
\mathbb E[-R\mid A]=v\cdot\ell,\qquad
\mathbb E[-PR\mid A]=v^{\mathsf T}Tu.
```

Nine pairs of Pauli axes supply all three displacements and nine transfer coefficients. The same equations hold conditional on past data and current angles selected before the private signs.

## Finite-budget estimation

For each axis pair, aim for the first $`K`$ accepted blocks. At every acceptance each sign has the displayed conditional mean, by the tower property over its possible waiting times. With $`K\ge2\epsilon^{-2}\log(72/\delta)`$, conditional Hoeffding followed by a union bound gives entrywise error at most $`\epsilon`$ for both empirical moments at all nine settings except with probability at most $`\delta/2`$.

Cap each setting at $`\lceil 8K/p^2\rceil`$ attempts and return failure if the count is smaller than $`K`$. Each acceptance probability is at least $`p^2/4`$ conditional on the past. The count dominates a binomial with that probability, whose lower-tail bound is $`e^{-K/4}`$. Taking also $`K\ge4\log(18/\delta)`$ makes the total acceptance failure probability at most $`\delta/2`$.

The resulting hard budget is $`O(p^{-2}\epsilon^{-2}\log(1/\delta))`$. The [information bound](testing.md#matching-sample-lower-bounds) gives the matching lower bound for $`0<\epsilon,\delta\le1/4`$.

## Blind-reset ambiguity

With the first probe discarded, the bath input to its own channel has Bloch vector $`p_1 r`$, where $`r`$ was the probe preparation. All second-collision statistics depend on the bath map and the first strength through $`\ell`$ and $`p_1T`$ for a fixed second angle. For $`p<1`$, the pairs $`(p_1,T)=(p,I)`$ and $`(1,pI)`$ with $`\ell=0`$ are both valid and indistinguishable. This remains true under classical adaptation, since their conditional transcript laws agree.

The ambiguity concerns full uncalibrated tomography. The [binary experiment](testing.md) tests for a promised nonzero gap in retained input dependence, which remains possible with a blind reset.

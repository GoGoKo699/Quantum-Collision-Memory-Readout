# Learning guide

The experiment reconstructs a bath channel without a direct bath measurement. A controllable probe collides with a bath qubit, is measured and reset, then collides with the bath again. The middle result can identify a branch in which the bath input is known exactly. The final result reveals one component of what the bath channel did to that input.

Read the [Watrous anchor and bridge](ANCHOR.md) for states, channels, measurements and discrimination. The [30-milestone map](MILESTONES.md) connects those ideas to the experiment, its information bound and its readout requirements.

## Worked example

Take both measurement axes to be $`Z`$. Independently draw two fair signs $`P,R`$. Prepare the probe in the $`P`$ eigenstate before the first collision and in the $`R`$ eigenstate after the middle measurement. Keep a block for the estimator when the middle reading is $`-P`$ and the final reading is $`-R`$.

Suppose the bath undergoes amplitude damping with probability $`1/4`$. Its output $`Z`$ component on input $`P`$ is $`1/4+3P/4`$. For illustration, let the exchange probabilities be $`p_1=1/4`$ and $`p_2=1/2`$. The estimator uses neither exchange probability.

| Initial sign $`P`$ | Reset sign $`R`$ | Bath output $`Z`$ component | Probability of both flips given $`P,R`$ |
|---|---|---:|---:|
| $`+1`$ | $`+1`$ | $`1`$ | $`0`$ |
| $`+1`$ | $`-1`$ | $`1`$ | $`1/16`$ |
| $`-1`$ | $`+1`$ | $`-1/2`$ | $`3/64`$ |
| $`-1`$ | $`-1`$ | $`-1/2`$ | $`1/64`$ |

The overall probability of both flips is $`1/32`$. Among those blocks the mean of $`-R`$ is $`1/4`$, the channel's $`Z`$ shift. The mean of $`-PR`$ is $`3/4`$, its $`Z`$-to-$`Z`$ transfer coefficient. Changing either exchange probability changes the number of blocks retained. It multiplies all four entries by the same factor and preserves the two conditional means.

Use all nine pairs of Pauli axes to recover the shift and transfer matrix. Count every attempted block, including the blocks that lack one or both flips. [Exact event law and tomography](../science/tomography.md)

## Connecting estimation and testing

A replacement channel can shift the bath but has zero transfer matrix. The sign product isolates the transfer, so it distinguishes a shift from retained dependence on the bath input. Under a blind reset the experiment still sees that dependence, attenuated by the first unknown exchange probability. This attenuation changes the worst-case testing cost and can prevent full channel identification. [Testing and the blind comparison](../science/testing.md)

Read the [model](../science/model.md) for the physical assumptions and charged operations, the [readout-noise analysis](../science/readout-noise.md) for the effect of false reports, and the [verification guide](../verification/README.md) to reproduce finite checks.

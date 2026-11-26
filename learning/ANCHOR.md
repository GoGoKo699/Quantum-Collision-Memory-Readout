# Educational anchor

John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018. Use the author's standard-layout manuscript. The page numbers below refer to its printed pagination. [Author's manuscript](https://johnwatrous.com/wp-content/uploads/TQI.pdf) · [Publisher table of contents](https://assets.cambridge.org/97811071/80567/toc/9781107180567_toc.pdf)

| Read | Use in this project |
|---|---|
| §§1.1–1.2, pp. 1–57, as needed | Hermitian operators, the trace, Pauli coordinates, convexity and conditional probability |
| §2.1, pp. 58–71 | Probe and bath as separate qubits, product initial states, and marginal states |
| §2.2, pp. 72–99 | Channels, complete positivity, trace preservation, unitary conjugation and discarding a register |
| §2.3, pp. 100–119 | Effects and Born probabilities, then the conditional states produced by measurement |
| §3.1, pp. 124–138 | Binary state discrimination and the optimization over accessible measurements |
| §3.3, pp. 164–196, for context | The operational importance of which systems and ancillary inputs a distinguishing experiment can access |

## From the source to the collision experiment

| Textbook object | Here |
|---|---|
| Density operator | A qubit with Bloch vector $`\mathbf r`$ is represented by $`\rho(\mathbf r)=(I+\mathbf r\cdot\boldsymbol\sigma)/2`$. The bath starts each block with $`\mathbf r=0`$. |
| Composite register | The probe $`S`$ and bath $`E`$ exchange polarization through a partial SWAP. The probe can be prepared and measured. The experiment accesses the bath only through these collisions. |
| Channel on a register | The fixed bath channel between collisions is represented by $`\mathbf r\mapsto\boldsymbol\ell+T\mathbf r`$. The shift and the transfer matrix are both unknown. |
| Measurement effect and conditional state | The first probe flip prepares a known bath eigenstate on that branch. The normalized state gives the input to the bath channel, and the trace of the unnormalized state gives the cost in trials. |
| State discrimination | Once the second probe outputs are specified, measurement converts them to classical laws. The whole two-collision experiment is constrained by its middle record and available probe operations. |

Watrous develops the finite-dimensional language for the proof. The [collision model](../science/model.md) introduces the physical coupling and the access restrictions. The [tomography proof](../science/tomography.md) then derives the two-flip event law and cancellation of the unknown transfer probabilities. The [testing proof](../science/testing.md) optimizes the measured chi-square information and accounts for all attempted blocks. The [readout-noise analysis](../science/readout-noise.md) treats errors in the middle report.

Start with the [worked example](README.md#worked-example) or use the [30-milestone map](MILESTONES.md) for the full conceptual route.

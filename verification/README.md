# Verification

Run these deterministic matrix checks with Python 3 and NumPy.

```bash
python3 verification/verify_collision_readout.py
```

The first group constructs explicit two-qubit partial-SWAP circuits for 400 signed-angle pairs. It checks the marked and blind event laws, both known-angle divergence attainers and sample POVMs against the analytic information bound. The second group uses 250 independently generated qubit CPTP maps to check the four private-sign event probabilities and the two accepted moments. The final group checks readout noise with independent matrix evolutions, including the exact sign-dithered divergence and calibrated affine likelihood.

These are finite consistency checks. The [analytic account](../science/README.md) proves the identities and guarantees for all inputs in the declared models.

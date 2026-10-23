# Reliability and quality statistics

Quick references. Check the governing standard or a reliability text before using a number for a release or compliance decision.

## Success-run sample size (zero failures allowed)

`n = ln(1 − C) / ln(R)`, rounded up, for confidence C and demonstrated reliability R.

| R \ C | 0.80 | 0.90 | 0.95 |
|-------|------|------|------|
| 0.90 | 16 | 22 | 29 |
| 0.95 | 32 | 45 | 59 |
| 0.99 | 161 | 230 | 299 |

Any failure invalidates the zero-failure claim. Investigate it, fix it, and restart with fresh units, or use a plan that allows failures (binomial).

## Acceleration (temperature, Arrhenius)

`AF = exp[(Ea / k) · (1 / T_use − 1 / T_test)]`, with temperatures in kelvin, Boltzmann constant k = 8.617 × 10⁻⁵ eV/K, and activation energy Ea specific to the failure mechanism. State Ea and its source. A wrong Ea gives a confident wrong life estimate. Other stresses have their own models (Coffin-Manson for thermal cycling, Peck for humidity, inverse power law for voltage).

HALT finds weak links by stepping stress to failure. It does not demonstrate life. Use a separate accelerated life test with a fitted model for life claims.

## Process capability

`Cpk = min(USL − μ, μ − LSL) / (3σ)`. Common targets: at least 1.33 for established processes, 1.67 for safety-critical characteristics. Capability is meaningful only for a process in statistical control.

## Measurement system analysis

Gauge R&R as a share of tolerance or process variation: under 10% acceptable, 10% to 30% conditional on the decision's cost and criticality, over 30% not acceptable. Number of distinct categories at least 5. Instrument resolution at least one tenth of the tolerance.

## Attribute sampling (AQL)

ISO 2859-1 (ANSI/ASQ Z1.4 in the US) gives sample size by lot size and inspection level, and accept and reject numbers by AQL, with switching rules between normal, tightened, and reduced inspection. AQL is a lot acceptance tool. It does not guarantee any individual unit.

## FMEA prioritization

The AIAG-VDA FMEA handbook (2019) replaced ranking by RPN (S × O × D) with Action Priority: a lookup that rates each row High, Medium, or Low, weighting severity first, then occurrence, then detection. Use the handbook's table. Two rows with equal RPN can carry very different risk, which is why the multiplied number alone misleads.

## Nondeterministic software

pass@k = P(at least one success in k trials). pass^k = P(all k succeed). With per-trial success p, pass@k = 1 − (1 − p)^k and pass^k = p^k. At p = 0.9 and k = 10, pass@k ≈ 1.0 and pass^k ≈ 0.35.

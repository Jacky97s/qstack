# Reliability and quality statistics

These are quick references. Before you use a number for a release or compliance decision, check the governing standard or a reliability text.

## Success-run sample size (zero failures allowed)

`n = ln(1 − C) / ln(R)`, rounded up, for confidence C and demonstrated reliability R.

| R \ C | 0.80 | 0.90 | 0.95 |
|-------|------|------|------|
| 0.90 | 16 | 22 | 29 |
| 0.95 | 32 | 45 | 59 |
| 0.99 | 161 | 230 | 299 |

Any failure makes the zero-failure claim invalid. Investigate the failure and fix it. Then restart with new units, or use a plan that allows failures (binomial).

## Acceleration (temperature, Arrhenius)

`AF = exp[(Ea / k) · (1 / T_use − 1 / T_test)]`, with temperatures in kelvin, Boltzmann constant k = 8.617 × 10⁻⁵ eV/K, and activation energy Ea specific to the failure mechanism. State Ea and its source. A wrong Ea gives a wrong life estimate with false confidence. Other stresses have their own models (Coffin-Manson for thermal cycling, Peck for humidity, inverse power law for voltage).

HALT finds weak links when you increase the stress in steps until failure. It does not demonstrate life. For life claims, use a separate accelerated life test with a fitted model.

## Process capability

`Cpk = min(USL − μ, μ − LSL) / (3σ)`. Common targets: at least 1.33 for established processes, 1.67 for safety-critical characteristics. Capability has meaning only for a process in statistical control.

## Measurement system analysis

Gauge R&R as a share of tolerance or process variation: under 10% is acceptable. 10% to 30% is conditional on the cost and criticality of the decision. Over 30% is not acceptable. The number of distinct categories must be at least 5. The instrument resolution must be at least one tenth of the tolerance.

## Attribute sampling (AQL)

ISO 2859-1 (ANSI/ASQ Z1.4 in the US) gives the sample size by lot size and inspection level. It also gives accept and reject numbers by AQL, with switching rules between normal, tightened, and reduced inspection. AQL is a lot acceptance tool. It does not guarantee any individual unit.

## FMEA prioritization

The AIAG-VDA FMEA handbook (2019) replaced ranking by RPN (S × O × D) with Action Priority. Action Priority is a lookup that rates each row High, Medium, or Low. It gives the most weight to severity, then occurrence, then detection. Use the table in the handbook. Two rows with equal RPN can have very different risk. For this reason, the multiplied number alone misleads.

## Nondeterministic software

pass@k = P(at least one success in k trials). pass^k = P(all k succeed). When the success rate of each trial is p, pass@k = 1 − (1 − p)^k and pass^k = p^k. At p = 0.9 and k = 10, pass@k ≈ 1.0 and pass^k ≈ 0.35.

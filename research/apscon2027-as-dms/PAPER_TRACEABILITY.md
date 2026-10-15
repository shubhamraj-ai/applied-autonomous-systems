# APSCON 2027 paper claim traceability

This file maps the principal **project-derived claims** in the paper candidate
**"Decoupling Alert Severity from Passive Aerial Verification Utility in Hybrid Security Sensing"**
to public, paper-safe evidence in this repository.

The purpose is manual auditability. It does **not** replace the external
peer-reviewed references cited in the manuscript.

## Numerical results

| Paper claim | Public evidence |
| --- | --- |
| Frozen paper projection contains 80 scenarios | `data/as_dms_paper_projection_v1.csv` |
| Pearson correlation between AS and DMS is approximately 0.720 | Run `analysis_nonredundancy.py` |
| Spearman rank correlation is approximately 0.711 | Run `analysis_nonredundancy.py` |
| Conditional entropy H(DroneDecision | exact AS) is 0.300 bits | Run `analysis_nonredundancy.py` |
| Six exact AS values map to multiple drone-decision categories | Run `analysis_nonredundancy.py` |
| The conflicting exact-AS groups contain 21 of 80 scenarios | Run `analysis_nonredundancy.py` |
| Optimistic exact-AS-only upper bound is 70/80 = 87.5% | Run `analysis_nonredundancy.py` |
| Optimistic alert-band-only upper bound is 55/80 = 68.75% | Run `analysis_nonredundancy.py` |
| Exact conflicting AS values are 0, 48, 55, 58, 78 and 94 | Run `analysis_nonredundancy.py` |

A captured output from the same deterministic script is stored in
`results_snapshot_v1.txt` for convenience.

## Representative divergences

The representative same-severity and zero-alert cases used in the paper are
published in:

- `data/representative_cases_v1.csv`

This includes the public-safe semantic labels corresponding to the Table II
examples in the manuscript.

## Mission-eligibility / safety examples

The manuscript states that alert severity is not identical to mission
eligibility or mobile-sensing utility. Public-safe examples of the relevant
constraint types are available in:

- `data/constraint_examples_v1.csv`

The file contains sanitized examples for:

- pet-only observations;
- staircase/indoor-prohibited sensing contexts;
- manual requests with and without authorization;
- geofence-unavailable rejection;
- scheduled sensing blocked by a safety precheck;
- camera-health conditions;
- house-empty scheduled sensing;
- safety events that remain no-drone.

These examples expose only the fields required to audit the manuscript's
decision-semantics discussion.

## Corpus scope

The paper describes the synthetic corpus as spanning several scenario classes.
A public-safe summary with representative scenario IDs is provided in:

- `data/corpus_scope_summary_v1.csv`

It supports the manuscript's statement that the frozen corpus includes routine
activity, suspicious activity, safety events, camera-health conditions,
scheduled patrols, house-empty operation, manual requests, and explicit
no-drone situations.

## Variable semantics

For this paper:

- **Alert Score (AS)** is the deterministic event-severity / human-attention
  variable.
- **Drone Mission Score (DMS)** is the deterministic priority/usefulness
  variable for a possible future passive aerial-verification mission.
- **Drone decision** is advisory and is not direct flight authorization.
- Mission eligibility / safety context remains logically distinct from both AS
  and DMS.

The public projection contains the exact AS, alert-band, DMS and final
drone-decision fields used in the paper analysis.

## Claim boundary

This public artifact supports specification-level reproducibility only. It does
not establish:

- real-world detection accuracy;
- false-alarm rate;
- field effectiveness;
- calibrated DMS probability;
- autonomous-flight safety;
- operational UAV performance.

The complete private development repository remains closed because it contains
implementation and deployment details that are not necessary to audit the
paper's reported public results.

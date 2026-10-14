# APSCON 2027 paper reproducibility artifact

This folder provides a **public-safe reproducibility artifact** for the paper
candidate:

> **Decoupling Alert Severity from Passive Aerial Verification Utility in Hybrid Security Sensing**

## Purpose

The private development repository contains operational and project-specific
details that are intentionally not public. This folder exposes only the minimal
paper-safe fields needed to reproduce the manuscript's primary corpus-level
non-redundancy statistics.

The public projection was derived from the frozen Phase-0E v0.3 analysis
checkpoint of the private project:

`153bc4a5f6fdd416b44e0fb30bfe0461de5cba04`

No live CCTV footage, property layout, camera placement, household information,
credentials, operational configuration, or private implementation code is
included here.

## Contents

- `data/as_dms_paper_projection_v1.csv` — 80 scenario IDs with the exact
  Alert Score, alert band, Drone Mission Score, and final drone-decision
  category used in the paper analysis.
- `data/representative_cases_v1.csv` — a small set of **sanitized semantic
  labels** corresponding to representative cases discussed in the manuscript.
- `analysis_nonredundancy.py` — deterministic script reproducing the paper's
  primary correlations, conditional-entropy values, same-AS conflict groups,
  and optimistic AS-only / alert-band-only representational upper bounds.

## Run

```bash
python analysis_nonredundancy.py
```

Expected headline results:

- N = 80
- Pearson correlation between AS and DMS ≈ 0.7202
- Spearman rank correlation ≈ 0.7112
- H(DroneDecision | exact AS) = 0.3000 bits
- optimistic exact-AS-only upper bound = 70/80 = 87.5%
- optimistic alert-band-only upper bound = 55/80 = 68.75%
- six exact AS values have multiple drone-decision categories
- those conflict groups contain 21/80 scenarios

## Scope and claim boundary

This artifact reproduces **specification-level descriptive results**. It does
not establish detection accuracy, false-alarm rate, field effectiveness, UAV
performance, or operational safety.

The 80 scenarios are author-designed synthetic specification cases. The public
projection is therefore intended to make the manuscript's narrow
non-redundancy analysis auditable, not to present a real-world surveillance
dataset.

## Public/private boundary

The main private project remains closed because it contains implementation,
field-design, security, privacy, and operational information not required to
audit the paper's reported numerical results.

This folder is the appropriate public citation target for the APSCON paper.

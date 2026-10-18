# Applied Autonomous Systems

A public-safe engineering and research showcase of an independently developed robotics and autonomous-systems project combining deterministic decision logic, configurable sensing topology, bounded hardware validation, human-governed deployment planning, and future passive aerial verification.

> **Current status (15 Oct 2026):** the software/simulation baseline and bounded Arduino bench work are validated. The project is in **Phase-0H5 property-readiness / Phase-1 CCTV procurement**, with the first three-camera package now at the near-final dealer/family purchase stage. Installation has **not yet been confirmed as started or commissioned**. The working target is to complete procurement and setup within roughly the next 10 days, subject to dealer availability and on-site work. No real drone operation is active.

## At a glance

| Area | Current public-safe state |
| --- | --- |
| Software | Deterministic Python assessment, rule-engine logic, review/audit workflows |
| Validation | Latest evidenced regression baseline: **625 passed, 3 skipped** |
| Architecture | Configurable sensing/topology models, provenance-aware handling, human-review boundaries |
| Bench hardware | Bounded Arduino UNO R4 WiFi validation and serial integration completed |
| Field engineering | Site-specific camera field design and installation-readiness planning completed to the current gate |
| Phase-1 deployment | **C1 + C2 + C4** procurement in progress; no camera commissioned yet |
| Passive CCTV pilot | Not started until installation/commissioning evidence exists |
| Aerial robotics | Future passive observation/verification direction only; no real UAV connected or operated |
| Research publication | Public APSCON 2027 AS/DMS reproducibility artifact available in this repository |

## What I am building

The private development project explores a layered security-verification architecture in which fixed-camera observations can eventually flow through deterministic, auditable logic before any consequential action is considered.

The engineering progression is deliberately staged:

1. deterministic scenario simulation;
2. architecture and review/audit modelling;
3. enhanced software simulation;
4. bounded embedded-hardware validation;
5. configurable sensing/topology modelling;
6. property-specific field design and procurement readiness;
7. passive CCTV installation and evidence collection;
8. later passive aerial-verification simulation/feasibility work behind separate safety and authorization gates.

The system is designed so that software output is **evidence for review, not physical authorization**.

## Current Phase-1 hardware direction

The present Phase-1 deployment is a three-camera CCTV package. These are the current procurement targets being discussed with the dealer/family:

| Component | Current model / requirement | Current status |
| --- | --- | --- |
| C1 | CP-UNC-DA41L3C-D-Q | Exact camera target |
| C2 | CP-UNC-TA41L3C-Q | Exact camera target |
| C4 | CP-UNC-TC41ZL6C-VMD-LQ | Exact LQ variant target |
| NVR | CP-UNR-4K4082-V4 | Revised currently available NVR target |
| PoE switch | CP-DNW-HPU8G2-96-V3 | Preferred external PoE switch |
| HDD | Seagate SkyHawk 2 TB ST2000VX017 | Preferred surveillance HDD |
| Outdoor Cat6 | CP Plus CP-EUT-6TGD23-100 | Reference model; dealer-equivalent outdoor cable may be accepted after review |
| Future edge computer | NVIDIA Jetson Orin Nano Super | Plan/budget only; **not a current purchase item** |

The public repository records the procurement state without exposing private property layout, camera coordinates, blind spots, household information, credentials, or operational configuration.

### Deployment boundary

Until real installation and commissioning evidence exists:

- no camera is treated as commissioned;
- no live household CCTV pipeline is claimed;
- no production surveillance network/storage stack is claimed;
- no resident-verification system is claimed;
- no real drone is claimed to be connected, dispatched, or flown.

## What this project demonstrates

- Python-based deterministic systems engineering
- specification-driven autonomous-systems design
- configurable camera/sensor topology modelling
- human-in-the-loop and human-governed decision design
- evidence provenance, auditability, and explicit uncertainty handling
- embedded-device / serial integration
- regression testing and controlled engineering checkpoints
- safety-oriented progression from simulation to bench to field work
- security-sensing research without overstating current deployment capability

## Technical areas

Python · Automated Testing · Embedded Systems · Serial Integration · Autonomous Systems · Sensor Topology · Human-in-the-Loop Design · Evidence/Audit Models · Safety & Validation

## Research: APSCON 2027 AS/DMS paper

This repository also contains the public-safe reproducibility artifact for the submitted APSCON 2027 paper:

> **Decoupling Alert Severity from Passive Aerial Verification Utility in Hybrid Security Sensing**

The paper studies whether **Alert Score (AS)**, representing human-attention severity, is sufficient by itself to reproduce mobile-sensing decisions, or whether **Drone Mission Score (DMS)** and mission-eligibility/safety context preserve distinct decision semantics.

The public artifact supports manual verification of the manuscript's project-derived results without exposing the private implementation repository.

### Reproducibility entry point

See:

[research/apscon2027-as-dms/](research/apscon2027-as-dms/)

The submitted paper reproducibility state is frozen at immutable commit:

dfd4ac8350ee49cce1c9300dbf526c6829c3e9a4

That folder includes:

- the 80-row public paper projection;
- the deterministic analysis script;
- captured expected results;
- representative same-severity and zero-alert cases;
- sanitized mission-eligibility/safety examples;
- corpus-scope summary;
- claim-by-claim paper traceability.

The reproducible headline results include:

- N = 80;
- Pearson correlation between AS and DMS ≈ 0.7202;
- Spearman rank correlation ≈ 0.7112;
- conditional entropy H(DroneDecision | exact AS) = 0.3000 bits;
- optimistic exact-AS-only upper bound 70/80 = 87.5%;
- optimistic alert-band-only upper bound 55/80 = 68.75%;
- six exact AS values with multiple drone-decision categories;
- 21 of 80 scenarios belonging to those conflicting exact-AS groups.

These are **specification-level descriptive results**, not field detection accuracy, false-alarm performance, UAV effectiveness, or operational-safety claims.

## Design philosophy

- unknown and insufficient-evidence states are valid outcomes;
- Alert Score is not a threat declaration;
- Drone Mission Score is not flight authorization;
- deterministic outputs do not automatically trigger physical action;
- human review remains mandatory at consequential boundaries;
- simulation and bench evidence precede real deployment;
- configuration and provenance are preferred over hidden hard-coded assumptions;
- safety, privacy, and rollback/readiness gates are part of the engineering design.

## Public-safe example

See [examples/synthetic-scenario.md](examples/synthetic-scenario.md) for a fictional scenario showing the style of input, deterministic assessment, review state, and conservative outcome used in the project. It contains no real property, camera, household, or deployment data.

## Repository scope

This is **not** the private development repository. It is a selectively disclosed technical and research showcase for professional review, resume use, and paper reproducibility.

Intentionally excluded:

- private property layout, dimensions, camera coordinates, or security weak points;
- private photographs, household data, and field evidence;
- proprietary/private rule-engine implementation details not required for the paper;
- credentials, internal URLs, environment values, or live operational configuration;
- any implication that the current system is already a production security installation.

The complete private repository contains the full implementation, bench-validation, field-design, project-governance, and research-development history. Additional private evidence may be shared selectively in an appropriate technical review context.

## Current limitations

This repository does **not** claim that a live surveillance installation, resident-identification system, autonomous aircraft operation, or production security system is currently active.

The project remains progressive and evidence-gated:

**validated simulation + bounded bench hardware + mature field design + active Phase-1 procurement → installation/commissioning evidence → passive CCTV pilot → later separately authorized aerial-verification work.**

## Additional notes

- [docs/architecture-overview.md](docs/architecture-overview.md) — high-level system structure
- [docs/validation-and-public-disclosure.md](docs/validation-and-public-disclosure.md) — validation and disclosure boundaries
- [docs/project-maturity.md](docs/project-maturity.md) — implemented vs. planned capability
- [examples/synthetic-scenario.md](examples/synthetic-scenario.md) — public-safe fictional scenario
- [research/apscon2027-as-dms/](research/apscon2027-as-dms/) — APSCON 2027 paper reproducibility and traceability artifact

---

**Why this repository exists:** to show practical robotics/autonomous-systems engineering, implementation discipline, research traceability, and validation thinking while preserving the privacy, security, and operational boundaries of the real project.

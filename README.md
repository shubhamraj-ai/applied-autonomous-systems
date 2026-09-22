# Applied Autonomous Systems

A public-safe engineering showcase of an independently developed robotics and autonomous-systems project that combines deterministic software, configurable sensing topology, bounded embedded-hardware validation, and human-governed deployment planning.

> **Current status:** active implementation + research project. Validated software simulation and bounded bench-hardware work are established; field deployment and real aerial operation remain intentionally gated.

## At a glance

| Area | Current evidence |
| --- | --- |
| Software | Deterministic Python modelling, rule-engine logic, review/audit workflows |
| Validation | Scenario-driven testing and a latest evidenced regression baseline of 625 passing tests |
| Architecture | Configurable sensing/topology models, provenance-aware data handling, human-review boundaries |
| Hardware | Bounded Arduino-based bench validation and serial integration |
| Field engineering | Controlled site-readiness and camera field-design work |
| Aerial robotics | Passive aerial-verification direction under future gated simulation/implementation work |

## What I am building

The private project explores a layered security-verification architecture in which sensor observations are evaluated through deterministic, explainable logic before any human-reviewed decision is made. The system is deliberately designed so that software output is **evidence for review, not physical authorization**.

The engineering path has progressed through:

1. deterministic simulation and scenario modelling;
2. architecture and review/audit design;
3. expanded software simulation;
4. bounded embedded-hardware validation;
5. configurable topology and sensing models;
6. controlled field-design/readiness work;
7. later passive aerial-verification phases only after separate readiness gates.

## What this demonstrates

- Python-based deterministic systems engineering
- autonomous-systems architecture and staged validation
- configurable camera/sensor topology modelling
- human-in-the-loop decision design
- evidence provenance, auditability, and explicit uncertainty handling
- embedded-device / serial integration
- regression testing and controlled engineering checkpoints
- safety-oriented progression from software to hardware to field work
- early aerial-robotics system design without overstating current flight capability

## Technical areas

`Python` · `Automated Testing` · `Embedded Systems` · `Serial Integration` · `Autonomous Systems` · `Sensor Topology` · `Human-in-the-Loop Design` · `Evidence/Audit Models` · `Safety & Validation`

## Design philosophy

A few principles shape the project:

- unknown and insufficient-evidence states are valid outcomes;
- deterministic outputs do not automatically trigger physical action;
- human review remains mandatory at consequential boundaries;
- simulation and bench evidence precede real deployment;
- configuration and provenance are preferred over hidden hard-coded assumptions;
- safety, privacy, and rollback/readiness gates are part of the engineering design.

## Public-safe example

See [`examples/synthetic-scenario.md`](examples/synthetic-scenario.md) for a fictional scenario showing the style of input, deterministic assessment, review state, and conservative outcome used in the project. It contains no real property, camera, household, or deployment data.

## Repository scope

This is **not** the private development repository. It is a deliberately sanitized technical showcase for professional review.

Intentionally excluded:

- the private project name and exact deployment location;
- real property layouts, dimensions, camera positions, or security weak points;
- private photographs, household data, and field evidence;
- exact scoring thresholds and proprietary implementation details;
- credentials, internal URLs, environment values, or live operational configuration.

## Private Development Repository

This public repository is a selectively disclosed portfolio representation of a broader private development project. The private repository contains the complete software, bench-validation, field-design, and research-development history, along with implementation details, commits, validation evidence, and project documentation that are intentionally excluded here for IP, privacy, security, or operational reasons.

**Additional private implementation evidence may be shared selectively during a relevant technical interview or professional review, subject to appropriate confidentiality and disclosure considerations.**

## Current limitations

This repository does **not** claim that a live surveillance installation, resident-identification system, or autonomous aircraft operation is currently active. The project remains progressive and evidence-gated, with real-world capability introduced only after explicit validation and approval stages.

## Additional notes

- [`docs/architecture-overview.md`](docs/architecture-overview.md) — high-level system structure
- [`docs/validation-and-public-disclosure.md`](docs/validation-and-public-disclosure.md) — validation and disclosure boundaries
- [`docs/project-maturity.md`](docs/project-maturity.md) — what is implemented now versus planned later

---

**Why this repository exists:** to show practical robotics/autonomous-systems engineering, implementation discipline, and validation thinking without exposing private operational details.
# Architecture Overview

This document presents a deliberately abstracted view of the private project's architecture.

## Core design principles

The system is designed around five boundaries:

1. **Observation is not judgment.** Sensor or scenario inputs are treated as evidence, not conclusions.
2. **Deterministic logic is auditable.** Rule-driven outputs are reproducible and inspectable.
3. **Human review remains authoritative.** Software outputs support review rather than replace consequential judgment.
4. **Simulation precedes deployment.** New behavior is validated in controlled software and bench environments before field use is considered.
5. **Physical action is separately gated.** A recommendation never equals authorization for a real-world action.

## High-level flow

```text
Synthetic / structured observations
        |
        v
Normalization + provenance handling
        |
        v
Deterministic assessment layer
        |
        +--> event / alert assessment
        |
        +--> future verification-value assessment
        |
        v
Review / abstention / insufficient-evidence handling
        |
        v
Human interpretation and bounded next-step decision
```

## Configurable topology layer

The private system includes a configuration-driven representation of sensing zones and devices rather than hard-coding a fixed number of sensors. Public documentation intentionally omits real site geometry, exact sensor positions, and operational configuration.

## Hardware boundary

A bounded embedded-hardware path has been validated using an Arduino-class device and explicit serial communication. This demonstrates physical-interface conformance without implying that a production physical system is deployed.

## Future autonomous-systems direction

Later phases may study passive aerial verification in simulation and controlled bench environments. Any future physical implementation remains subject to separate technical, legal, privacy, safety, and human-approval gates.

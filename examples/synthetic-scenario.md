# Synthetic Scenario Example

This fictional example illustrates the **style** of deterministic assessment used by the private project. It is intentionally generic and contains no real property, camera, household, or deployment information.

## Fictional input

```yaml
scenario_id: demo-001
context: after-hours observation
zone: generic_external_zone
observation:
  category: unknown_object
  duration_seconds: 18
  motion_state: intermittent
sensor_health:
  primary_sensor: healthy
  supporting_sensor: unavailable
prior_context:
  related_recent_event: false
review_requirements:
  human_review_required: true
```

## Example deterministic assessment

```yaml
assessment:
  evidence_quality: partial
  event_priority: moderate
  additional_observation_value: possible
  confidence: bounded
  decision_state: review_required
```

## Conservative outcome

```yaml
outcome:
  automatic_physical_action: false
  human_review: required
  aerial_action_authorized: false
  note: "Additional observation may be useful, but the available evidence is insufficient for an autonomous physical response."
```

## Why this matters

The project separates three different questions:

1. **What was observed?**
2. **How should deterministic software classify the available evidence?**
3. **What, if anything, should a human authorize next?**

These are deliberately not collapsed into one automated decision.

The actual private implementation contains more detailed schemas, validation, provenance, and scenario logic. Those details are excluded from this public showcase.
#!/usr/bin/env python3
"""
Reproduce the primary corpus-level non-redundancy results reported for the
APSCON 2027 paper candidate:

"Decoupling Alert Severity from Passive Aerial Verification Utility in Hybrid
Security Sensing"

This public script intentionally analyzes only the paper-safe projection in
data/as_dms_paper_projection_v1.csv. It does not contain the private rule engine,
property topology, camera layout, or operational configuration.

Usage:
    python analysis_nonredundancy.py
"""

from collections import Counter, defaultdict
from pathlib import Path
import csv
import math

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "as_dms_paper_projection_v1.csv"

with DATA.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

AS = [float(r["alert_score"]) for r in rows]
DMS = [float(r["drone_mission_score"]) for r in rows]
BANDS = [r["alert_band"] for r in rows]
DECISIONS = [r["drone_decision"] for r in rows]

def pearson(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    denx = sum((x-mx)**2 for x in xs)
    deny = sum((y-my)**2 for y in ys)
    return num / math.sqrt(denx * deny)

def ranks(values):
    pairs = sorted((v, i) for i, v in enumerate(values))
    out = [None] * len(values)
    i = 0
    while i < len(pairs):
        j = i + 1
        while j < len(pairs) and pairs[j][0] == pairs[i][0]:
            j += 1
        avg = ((i + 1) + j) / 2
        for k in range(i, j):
            out[pairs[k][1]] = avg
        i = j
    return out

def entropy(vals):
    n = len(vals)
    counts = Counter(vals)
    return -sum((c/n) * math.log2(c/n) for c in counts.values())

def conditional_entropy(xs, ys):
    groups = defaultdict(list)
    for x, y in zip(xs, ys):
        groups[x].append(y)
    n = len(xs)
    return sum((len(v)/n) * entropy(v) for v in groups.values())

def optimistic_upper_bound(xs, ys):
    groups = defaultdict(Counter)
    for x, y in zip(xs, ys):
        groups[x][y] += 1
    correct = sum(max(c.values()) for c in groups.values())
    return correct, groups

n = len(rows)
pearson_r = pearson(AS, DMS)
spearman_rho = pearson(ranks(AS), ranks(DMS))
h_given_as = conditional_entropy(AS, DECISIONS)
h_given_band = conditional_entropy(BANDS, DECISIONS)
best_as, as_groups = optimistic_upper_bound(AS, DECISIONS)
best_band, _ = optimistic_upper_bound(BANDS, DECISIONS)

conflicts = {
    score: dict(counter)
    for score, counter in sorted(as_groups.items())
    if len(counter) > 1
}
conflicting_scenarios = sum(sum(c.values()) for c in conflicts.values())

print(f"N = {n}")
print(f"Pearson r(AS,DMS) = {pearson_r:.10f}")
print(f"Spearman rho(AS,DMS) = {spearman_rho:.10f}")
print(f"H(DroneDecision | exact AS) = {h_given_as:.10f} bits")
print(f"H(DroneDecision | alert band) = {h_given_band:.10f} bits")
print(f"Best exact-AS-only mapping = {best_as}/{n} = {best_as/n:.2%}")
print(f"Best alert-band-only mapping = {best_band}/{n} = {best_band/n:.2%}")
print(f"Exact AS values with conflicting decisions = {len(conflicts)}")
print(f"Scenarios in conflicting-AS groups = {conflicting_scenarios}/{n}")
print("Conflicting exact-AS groups:")
for score, counter in conflicts.items():
    print(f"  AS={score:g}: {counter}")

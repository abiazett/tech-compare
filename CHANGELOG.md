# Changelog

All notable changes to the tech-compare skill will be documented in this file.

## [Unreleased] - 2026-04-05

### Summary

Methodology improvements inspired by real-world AI-assisted framework evaluation findings. These changes address 12 specific failure modes and analysis gaps discovered during production use of AI-driven technology comparisons.

### Added

#### New Bias Prevention Failure Modes (`references/bias-prevention.md`)

1. **OSS vs Commercial Feature Conflation (#8)** — New failure mode requiring all features to be tagged `[OSS]` or `[PAID/COMMERCIAL]`. Prevents mixing open-source and paid features in comparisons (e.g., citing a paid-only feature as a general capability).

2. **False Feature Differentiation (#9)** — New failure mode requiring verification of ALL competing platforms before claiming any feature as a differentiator. Features often exist under different names or were recently added.

3. **Incomplete System Path Analysis (#10)** — New failure mode requiring analysis of complete execution paths (API through storage), not just surface-layer APIs. Also requires reviewing all configuration flags before making categorical limitation statements.

4. **Comparison Baseline Drift (#11)** — New failure mode requiring consistent evaluation criteria and measurement standards across all platforms. Prevents apples-to-oranges comparisons (e.g., burst vs sustained throughput).

#### New Workflow Steps (`SKILL.md`)

5. **Self-Validation Loop (Step 6.3)** — New pre-presentation step where the model re-reads its complete analysis and checks for: inconsistencies, asymmetric language, executive summary misalignment, logical gaps, false differentiation, and baseline drift.

6. **Decision Reversal Criteria (Step 6.4)** — New step generating explicit conditions under which each recommendation would change (e.g., "if Technology B adds feature X", "if dataset exceeds Y threshold").

#### New Report Sections (`SKILL.md` Step 7.1 template)

7. **Dissenting Viewpoints** — New report section presenting the strongest argument against the primary recommendation, followed by a rebuttal. Ensures recommendations are stress-tested.

8. **Cost Quantification (Optional)** — New optional report section for relative cost comparisons (infrastructure overhead, engineering effort, maintenance burden, expertise requirements, license costs) and gap remediation effort breakdowns. Included only when requested by user or when significant cost differences exist.

9. **Gap Remediation Effort** — Sub-section of Cost Quantification breaking down effort to build or contribute missing capabilities into specific technical components with justification.

### Changed

10. **Gap Mitigation Philosophy** — Updated Pattern 6 in `decision-framework-patterns.md` and Step 4.4 in `SKILL.md`: candidates are no longer eliminated for missing features. Instead, the effort to build/contribute the missing capability is estimated and factored into rankings. Only `[FUNDAMENTAL]` architectural limitations are treated as disqualifying.

11. **Marketing Language Rule Strengthened** — Updated `bias-prevention.md` Failure Mode #2: marketing terms must now be translated into specific technical requirements or excluded from analysis entirely (previously just recommended translation).

12. **Cache Bypass for Quantitative Data** — Updated `bias-prevention.md` Failure Mode #1: when fetching metrics like GitHub stars or download counts, must explicitly request fresh/uncached data and re-fetch if values appear stale.

13. **Executive Summary Guidance** — Updated report template: executive summaries must focus on strategic decisions (licensing, architecture, governance), not implementation details.

14. **Training Data Override** — Strengthened existing rule in `bias-prevention.md`: when web search results contradict training data, explicitly prioritize current documentation, especially for version-specific information.

15. **Script Format Normalization** — All 3 output scripts (`generate_decision_matrix.py`, `create_comparison_presentation.py`, `create_comparison_tables.py`) now accept both flat and rich JSON formats via `normalize_data()`. Handles: technologies as list of strings or dicts, dimensions with `scores` or `comparisons`, missing `weight` fields, scenarios without `scores` dicts, and scenarios-to-scenario_analysis mapping.

### Files Modified

| File | Changes |
|------|---------|
| `SKILL.md` | Steps 6.3-6.5 added, Step 4.2 OSS/PAID tagging, Step 4.4 gap mitigation, report template (exec summary, dissenting view, cost quantification, reversal criteria, methodology notes), workflow diagram, key principles (8 → 14) |
| `references/bias-prevention.md` | 4 new failure modes (#8-#11), strengthened marketing language rule (#2), cache bypass (#1), training data override (#1), updated summary table |
| `references/decision-framework-patterns.md` | Pattern 6 updated with gap mitigation philosophy and component-level effort breakdown requirement |
| `scripts/generate_decision_matrix.py` | Added `normalize_data()` for flat/rich JSON compatibility |
| `scripts/create_comparison_presentation.py` | Added `normalize_data()` for flat/rich JSON compatibility |
| `scripts/create_comparison_tables.py` | Added `normalize_data()` for flat/rich JSON compatibility |

### Methodology Source

Changes derived from analysis of a 15-phase AI-assisted framework evaluation methodology that identified specific pitfalls in AI-driven technology comparisons, including: outdated knowledge claims, false feature differentiation, OSS/commercial feature conflation, overestimated technical complexity, executive summary misalignment, format drift, documentation misinterpretation, incomplete system analysis, missing configuration options, training data contamination, comparison baseline drift, and marketing language infiltration.

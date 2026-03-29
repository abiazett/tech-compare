#!/usr/bin/env python3
"""
Generate weighted decision matrix and recommendations from comparison data.

Usage:
    python generate_decision_matrix.py <comparison_data.json> <output.json>

Input JSON format:
{
    "technologies": ["Tech A", "Tech B", "Tech C"],
    "scenarios": [
        {
            "name": "Scenario 1",
            "priority": "CRITICAL",  // CRITICAL, IMPORTANT, NICE-TO-HAVE
            "best_fit": "Tech A",
            "runner_up": "Tech B",
            "scores": {
                "Tech A": 9,  // 1-10 scale
                "Tech B": 7,
                "Tech C": 4
            }
        }
    ],
    "dimensions": [
        {
            "name": "Features & Capabilities",
            "weight": "IMPORTANT",  // CRITICAL, IMPORTANT, NICE-TO-HAVE
            "comparisons": {
                "Tech A": {"score": "Strong", "numeric_score": 9},
                "Tech B": {"score": "Good", "numeric_score": 7},
                "Tech C": {"score": "Limited", "numeric_score": 4}
            }
        }
    ]
}

Output JSON format:
{
    "scenario_weighted_scores": {
        "Tech A": {"total": 85, "critical_wins": 2, "important_wins": 1, ...},
        "Tech B": {...},
        "Tech C": {...}
    },
    "dimension_weighted_scores": {...},
    "overall_recommendation": {
        "primary": "Tech A",
        "rationale": "...",
        "alternatives": [...]
    },
    "conditional_recommendations": [
        {"condition": "If X...", "recommendation": "Choose Tech A"},
        ...
    ]
}
"""

import json
import sys
from typing import Dict, List, Any, Tuple


# Priority weights
PRIORITY_WEIGHTS = {
    "CRITICAL": 10,
    "IMPORTANT": 5,
    "NICE-TO-HAVE": 2
}


def calculate_scenario_weighted_scores(scenarios: List[Dict[str, Any]], technologies: List[str]) -> Dict[str, Any]:
    """Calculate weighted scores based on scenario priorities."""
    scores = {tech: {
        "total": 0,
        "critical_wins": 0,
        "important_wins": 0,
        "nice_to_have_wins": 0,
        "runner_ups": 0,
        "breakdown": []
    } for tech in technologies}

    for scenario in scenarios:
        scenario_name = scenario.get('name', 'Unknown')
        priority = scenario.get('priority', 'IMPORTANT')
        best_fit = scenario.get('best_fit')
        runner_up = scenario.get('runner_up')
        scenario_scores = scenario.get('scores', {})

        weight = PRIORITY_WEIGHTS.get(priority, 5)

        # Award points for best fit and runner-up
        if best_fit and best_fit in scores:
            points = weight
            scores[best_fit]["total"] += points

            if priority == "CRITICAL":
                scores[best_fit]["critical_wins"] += 1
            elif priority == "IMPORTANT":
                scores[best_fit]["important_wins"] += 1
            else:
                scores[best_fit]["nice_to_have_wins"] += 1

            scores[best_fit]["breakdown"].append({
                "scenario": scenario_name,
                "priority": priority,
                "role": "Best Fit",
                "points": points
            })

        if runner_up and runner_up in scores:
            points = weight // 2  # Half points for runner-up
            scores[runner_up]["total"] += points
            scores[runner_up]["runner_ups"] += 1

            scores[runner_up]["breakdown"].append({
                "scenario": scenario_name,
                "priority": priority,
                "role": "Runner-Up",
                "points": points
            })

    # Sort by total score
    sorted_scores = sorted(scores.items(), key=lambda x: x[1]["total"], reverse=True)

    return {
        "scores": dict(sorted_scores),
        "winner": sorted_scores[0][0] if sorted_scores else None,
        "technologies": technologies
    }


def calculate_dimension_weighted_scores(dimensions: List[Dict[str, Any]], technologies: List[str]) -> Dict[str, Any]:
    """Calculate weighted scores based on dimension weights."""
    scores = {tech: {
        "total": 0,
        "breakdown": []
    } for tech in technologies}

    for dimension in dimensions:
        dim_name = dimension.get('name', 'Unknown')
        weight_str = dimension.get('weight', 'IMPORTANT')
        weight = PRIORITY_WEIGHTS.get(weight_str, 5)
        comparisons = dimension.get('comparisons', {})

        for tech in technologies:
            if tech in comparisons:
                comp = comparisons[tech]
                numeric_score = comp.get('numeric_score', 5)  # Default 5/10

                points = numeric_score * weight / 10  # Normalize to weight scale
                scores[tech]["total"] += points
                scores[tech]["breakdown"].append({
                    "dimension": dim_name,
                    "weight": weight_str,
                    "score": numeric_score,
                    "points": points
                })

    # Sort by total score
    sorted_scores = sorted(scores.items(), key=lambda x: x[1]["total"], reverse=True)

    return {
        "scores": dict(sorted_scores),
        "winner": sorted_scores[0][0] if sorted_scores else None
    }


def generate_conditional_recommendations(
    scenario_analysis: List[Dict[str, Any]],
    technologies: List[str]
) -> List[Dict[str, str]]:
    """Generate "Choose X if..." conditional recommendations."""
    conditionals = []

    # Group scenarios by best_fit technology
    tech_scenarios = {tech: [] for tech in technologies}

    for scenario in scenario_analysis:
        best_fit = scenario.get('best_fit')
        if best_fit and best_fit in tech_scenarios:
            tech_scenarios[best_fit].append(scenario)

    # Generate conditionals for each technology
    for tech, scenarios in tech_scenarios.items():
        if not scenarios:
            continue

        conditions = []

        # Extract key conditions from scenario rationale
        for scenario in scenarios:
            priority = scenario.get('priority', 'IMPORTANT')
            scenario_name = scenario.get('name', 'Unknown')

            if priority == "CRITICAL":
                conditions.append(f"{scenario_name} is CRITICAL")
            else:
                conditions.append(scenario_name)

        if conditions:
            condition_text = " AND ".join(conditions[:3])  # Top 3 conditions
            conditionals.append({
                "technology": tech,
                "condition": condition_text,
                "recommendation": f"Choose {tech}"
            })

    return conditionals


def generate_overall_recommendation(
    scenario_scores: Dict[str, Any],
    dimension_scores: Dict[str, Any],
    technologies: List[str],
    scenarios: List[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Generate overall recommendation based on weighted scores."""

    scenario_winner = scenario_scores.get('winner')
    scenario_scores_data = scenario_scores.get('scores', {})

    dimension_winner = dimension_scores.get('winner')

    # Primary recommendation is scenario winner (scenarios matter more than abstract dimensions)
    primary = scenario_winner

    if not primary:
        primary = dimension_winner

    if not primary:
        primary = technologies[0] if technologies else "Unknown"

    # Rationale
    rationale_parts = []

    if primary in scenario_scores_data:
        tech_score = scenario_scores_data[primary]
        critical_wins = tech_score.get('critical_wins', 0)
        important_wins = tech_score.get('important_wins', 0)

        if critical_wins > 0:
            rationale_parts.append(f"Best fit for {critical_wins} CRITICAL scenario(s)")
        if important_wins > 0:
            rationale_parts.append(f"Best fit for {important_wins} IMPORTANT scenario(s)")

    rationale = "; ".join(rationale_parts) if rationale_parts else "Highest weighted score"

    # Alternatives (runner-ups)
    alternatives = []
    for tech, score_data in scenario_scores_data.items():
        if tech != primary:
            alternatives.append({
                "technology": tech,
                "total_score": score_data['total'],
                "critical_wins": score_data.get('critical_wins', 0),
                "runner_ups": score_data.get('runner_ups', 0)
            })

    # Sort alternatives by score
    alternatives = sorted(alternatives, key=lambda x: x['total_score'], reverse=True)

    # Detect winner inconsistency
    note = None
    if scenario_winner and dimension_winner and scenario_winner != dimension_winner:
        note = (
            f"Note: Scenario-based analysis favors {scenario_winner}, while dimension-based "
            f"analysis favors {dimension_winner}. Primary recommendation prioritizes your "
            f"stated scenarios over abstract dimension scoring."
        )

    # Detect low scenario count with same priority (ambiguous winner)
    if scenarios and len(scenarios) <= 2:
        priorities = [s.get('priority', 'IMPORTANT') for s in scenarios]
        unique_priorities = set(priorities)
        if len(unique_priorities) == 1 and priorities[0] != 'CRITICAL':
            if note:
                note += " Additionally, only 2 scenarios with the same priority level may not provide sufficient differentiation. Consider adding more scenarios or marking one as CRITICAL for clearer recommendations."
            else:
                note = "Note: Only 2 scenarios with the same priority level. Consider adding more scenarios or prioritizing one as CRITICAL for clearer recommendations."

    result = {
        "primary": primary,
        "rationale": rationale,
        "alternatives": alternatives[:2],  # Top 2 alternatives
        "confidence": "High" if scenario_scores_data.get(primary, {}).get('critical_wins', 0) > 0 else "Moderate"
    }

    if note:
        result["note"] = note

    return result


def generate_decision_matrix(data: Dict[str, Any]) -> Dict[str, Any]:
    """Generate complete decision matrix from comparison data."""

    technologies = data.get('technologies', [])
    scenarios = data.get('scenarios', [])
    dimensions = data.get('dimensions', [])

    # Calculate scores
    scenario_scores = calculate_scenario_weighted_scores(scenarios, technologies)
    dimension_scores = calculate_dimension_weighted_scores(dimensions, technologies)

    # Generate recommendations
    conditional_recs = generate_conditional_recommendations(scenarios, technologies)
    overall_rec = generate_overall_recommendation(scenario_scores, dimension_scores, technologies, scenarios)

    return {
        "scenario_weighted_scores": scenario_scores,
        "dimension_weighted_scores": dimension_scores,
        "conditional_recommendations": conditional_recs,
        "overall_recommendation": overall_rec,
        "technologies": technologies
    }


def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_decision_matrix.py <comparison_data.json> <output.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Load comparison data
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file: {e}")
        sys.exit(1)

    # Generate decision matrix
    decision_matrix = generate_decision_matrix(data)

    # Write output
    with open(output_file, 'w') as f:
        json.dump(decision_matrix, f, indent=2)

    print(f"✅ Decision matrix generated: {output_file}")

    # Print summary
    overall = decision_matrix['overall_recommendation']
    print(f"\n📊 Overall Recommendation: {overall['primary']}")
    print(f"   Rationale: {overall['rationale']}")
    print(f"   Confidence: {overall['confidence']}")


if __name__ == "__main__":
    main()

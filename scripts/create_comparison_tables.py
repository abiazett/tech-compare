#!/usr/bin/env python3
"""
Generate markdown comparison tables from structured comparison data.

Usage:
    python create_comparison_tables.py <comparison_data.json> <output.md>

Input JSON format:
{
    "technologies": ["Tech A", "Tech B", "Tech C"],
    "scenarios": [
        {"name": "Scenario 1", "priority": "CRITICAL"},
        {"name": "Scenario 2", "priority": "IMPORTANT"}
    ],
    "dimensions": [
        {
            "name": "Features & Capabilities",
            "comparisons": {
                "Tech A": {"score": "Strong", "notes": "Complete feature set"},
                "Tech B": {"score": "Good", "notes": "Most features, missing X"},
                "Tech C": {"score": "Limited", "notes": "Basic features only"}
            }
        }
    ],
    "scenario_analysis": [
        {
            "scenario": "Scenario 1",
            "best_fit": "Tech A",
            "runner_up": "Tech B",
            "rationale": "Tech A excels at X which is critical for this scenario"
        }
    ]
}
"""

import json
import sys
from typing import Dict, List, Any


def generate_dimension_table(dimension: Dict[str, Any], technologies: List[str]) -> str:
    """Generate a comparison table for a single dimension."""
    lines = []

    # Header
    lines.append(f"### {dimension['name']}\n")

    # Table header
    header = "| Technology | Assessment | Notes |"
    separator = "|------------|------------|-------|"
    lines.append(header)
    lines.append(separator)

    # Table rows
    comparisons = dimension.get('comparisons', {})
    for tech in technologies:
        comp = comparisons.get(tech, {"score": "N/A", "notes": ""})
        score = comp.get('score', 'N/A')
        notes = comp.get('notes', '').replace('\n', ' ')
        lines.append(f"| **{tech}** | {score} | {notes} |")

    lines.append("")  # Blank line after table
    return "\n".join(lines)


def generate_scenario_winner_table(scenario_analysis: List[Dict[str, Any]]) -> str:
    """Generate per-scenario winner matrix."""
    lines = []

    lines.append("## Scenario-Specific Recommendations\n")

    # Table header
    header = "| Scenario | Priority | Best Fit | Runner-Up | Why |"
    separator = "|----------|----------|----------|-----------|-----|"
    lines.append(header)
    lines.append(separator)

    # Table rows
    for analysis in scenario_analysis:
        scenario = analysis.get('scenario', 'Unknown')
        priority = analysis.get('priority', '')
        best_fit = analysis.get('best_fit', 'N/A')
        runner_up = analysis.get('runner_up', 'N/A')
        rationale = analysis.get('rationale', '').replace('\n', ' ')

        # Add emoji for priority
        priority_display = priority
        if priority == "CRITICAL":
            priority_display = "🔴 CRITICAL"
        elif priority == "IMPORTANT":
            priority_display = "🟡 IMPORTANT"
        elif priority == "NICE-TO-HAVE":
            priority_display = "⚪ NICE-TO-HAVE"

        lines.append(f"| {scenario} | {priority_display} | **{best_fit}** | {runner_up} | {rationale} |")

    lines.append("")
    return "\n".join(lines)


def generate_feature_matrix(dimensions: List[Dict[str, Any]], technologies: List[str]) -> str:
    """Generate a condensed feature comparison matrix."""
    lines = []

    lines.append("## Feature Comparison Matrix\n")

    # Table header - technology names as columns
    header = "| Feature/Capability | " + " | ".join(technologies) + " |"
    separator = "|" + "|".join(["-" * 20 for _ in range(len(technologies) + 1)]) + "|"
    lines.append(header)
    lines.append(separator)

    # For each dimension, create a condensed row
    for dim in dimensions:
        dim_name = dim['name']
        comparisons = dim.get('comparisons', {})

        row = f"| **{dim_name}** |"
        for tech in technologies:
            comp = comparisons.get(tech, {"score": "N/A"})
            score = comp.get('score', 'N/A')

            # Convert score to emoji or short form
            if score in ["Strong", "Excellent", "Best"]:
                display = "✅"
            elif score in ["Good", "Solid"]:
                display = "✅"
            elif score in ["Moderate", "Fair", "Acceptable"]:
                display = "⚠️"
            elif score in ["Weak", "Limited", "Poor"]:
                display = "❌"
            elif score in ["N/A", "Not Applicable"]:
                display = "—"
            else:
                display = score  # Use as-is if not standard

            row += f" {display} |"

        lines.append(row)

    lines.append("")
    return "\n".join(lines)


def generate_quick_reference_table(technologies: List[str], summary: Dict[str, Any]) -> str:
    """Generate a quick reference table with key attributes."""
    lines = []

    lines.append("## Quick Reference\n")

    # Attributes to include
    attributes = [
        "License",
        "Governance",
        "Primary Use Case",
        "GitHub Stars",
        "Deployment Model",
        "Maturity"
    ]

    # Table header
    header = "| Attribute | " + " | ".join(technologies) + " |"
    separator = "|" + "|".join(["-" * 15 for _ in range(len(technologies) + 1)]) + "|"
    lines.append(header)
    lines.append(separator)

    # Rows
    tech_data = summary.get('technology_profiles', {})
    for attr in attributes:
        row = f"| **{attr}** |"
        for tech in technologies:
            profile = tech_data.get(tech, {})
            value = profile.get(attr, "N/A")
            row += f" {value} |"
        lines.append(row)

    lines.append("")
    return "\n".join(lines)


def generate_full_comparison_markdown(data: Dict[str, Any]) -> str:
    """Generate complete comparison markdown from structured data."""
    lines = []

    # Title
    title = data.get('title', 'Technology Comparison')
    lines.append(f"# {title}\n")

    # Metadata
    date = data.get('date', 'N/A')
    technologies = data.get('technologies', [])
    lines.append(f"**Date:** {date}")
    lines.append(f"**Technologies Compared:** {', '.join(technologies)}\n")

    # Executive summary if provided
    if 'executive_summary' in data:
        lines.append("## Executive Summary\n")
        lines.append(data['executive_summary'])
        lines.append("")

    # Quick reference table
    if 'summary' in data:
        lines.append(generate_quick_reference_table(technologies, data['summary']))

    # Scenario-specific recommendations
    if 'scenario_analysis' in data:
        lines.append(generate_scenario_winner_table(data['scenario_analysis']))

    # Feature comparison matrix
    if 'dimensions' in data:
        lines.append(generate_feature_matrix(data['dimensions'], technologies))

    # Detailed dimension analysis
    lines.append("---\n")
    lines.append("## Detailed Dimension Analysis\n")

    for dimension in data.get('dimensions', []):
        lines.append(generate_dimension_table(dimension, technologies))

    # Recommendations section
    if 'recommendations' in data:
        lines.append("---\n")
        lines.append("## Recommendations\n")
        lines.append(data['recommendations'])
        lines.append("")

    # Sources
    if 'sources' in data:
        lines.append("---\n")
        lines.append("## Sources\n")
        for source in data['sources']:
            lines.append(f"- {source}")
        lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) != 3:
        print("Usage: python create_comparison_tables.py <comparison_data.json> <output.md>")
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

    # Generate markdown
    markdown = generate_full_comparison_markdown(data)

    # Write output
    with open(output_file, 'w') as f:
        f.write(markdown)

    print(f"✅ Comparison tables generated: {output_file}")


if __name__ == "__main__":
    main()

---
name: tech-compare
description: Compare 2-3 technologies across user-defined scenarios (ML/AI frameworks, databases, cloud providers, web frameworks, container orchestration, CI/CD, etc.). Auto-discovers alternatives and suggests relevant scenarios. Two modes - Quick (1-2h web research, 14 dimensions) or Deep (2-4h with project-swot). Generates complete output - markdown report, comparison tables, decision matrix, PowerPoint, PDFs. Evaluates each technology per scenario independently with scenario-specific recommendations (no forced single winner). Trigger on - "Compare X, Y, Z", "Which is better A or B?", "Evaluate [technologies] for [scenario]", "Help me choose between [options]", "Should we use X or Y?".
---

# Technology Comparison

Compare 2-3 technologies across multiple scenarios with unbiased analysis, scenario-specific recommendations, and comprehensive output deliverables.

## Overview

This skill provides structured technology comparison following these principles:

1. **Multi-scenario analysis** - Different technologies excel at different use cases
2. **Scenario-specific recommendations** - No forced single winner across all scenarios
3. **Bias prevention** - Forked subagents for positive vs negative analysis
4. **Fresh data** - Always web search (never rely on training data for metrics)
5. **User-driven** - User defines scenarios first, skill suggests additional relevant ones
6. **Comprehensive output** - Markdown report, tables, decision matrix, presentation, PDFs

## Core Design Principle

**In technology comparisons, there is rarely a single "winner" across all scenarios.**

Different technologies excel at different use cases. The goal is to help users understand **which technology fits which scenario**, not to force a single recommendation.

Example: Framework A may be best for rapid prototyping (single-node, ease of use), while Framework B excels at distributed production training. Both win different scenarios.

## Technical Focus

**IMPORTANT:** This is a **technical comparison** focused on capabilities, architecture, and scenario fit.

**Focus on:**
- Technical capabilities and features
- Performance characteristics (throughput, latency, scalability)
- Resource efficiency (relative comparisons: "10x more memory", "50% fewer CPU cycles")
- Implementation complexity (High/Medium/Low qualitative assessments)
- Integration requirements and compatibility
- Operational characteristics (monitoring, debugging, maintenance)

**Do NOT include:**
- Specific cost estimates or budgets (e.g., "$275K year 1")
- ROI calculations or payback periods
- Detailed implementation timelines with month-by-month breakdowns
- Financial modeling or business case analysis

If the user needs cost/timeline analysis, recommend they take the technical comparison output to their finance/planning teams.

## Software Requirements

This skill generates markdown reports, PDFs, and PowerPoint presentations. Required packages:

**macOS (via Homebrew):**
```bash
brew install pandoc tectonic
brew install --cask libreoffice
pip3 install python-pptx
```

**Fedora/RHEL (via dnf):**
```bash
sudo dnf install -y pandoc pandoc-pdf libreoffice python3 python3-pip
pip3 install --user python-pptx
```

**Ubuntu/Debian (via apt):**
```bash
sudo apt install -y pandoc texlive-xetex libreoffice python3-pip
pip3 install --user python-pptx
```

**Verify installation:**
```bash
which pandoc soffice python3
python3 -c "import pptx; print('python-pptx installed')"
```

---

## Workflow

```
Step 1: Technology Discovery   → Web search for alternatives, user selects 2-3
Step 2: Mode Selection         → Quick (1-2h) or Deep (2-4h with project-swot)
Step 3: Scenario Definition    → User provides scenarios, skill suggests additional, user confirms
Step 4: Deep Research          → Quick mode: 14 dimensions analysis
                                 Deep mode: project-swot for each technology (ask Phase 0 questions once, reuse for all)
Step 5: Context Integration    → User provides optional context files (meeting notes, requirements)
Step 6: Synthesis              → Per-scenario recommendations using decision framework patterns
Step 7: Output Generation      → Markdown report, tables, decision matrix, presentation, PDFs
```

---

## Step 1: Technology Discovery

### Ask User for Initial Input

"What technologies do you want to compare? You can provide:
- Specific technologies (e.g., 'Compare Katib, AutoGluon, FLAML')
- Technology category (e.g., 'ML frameworks', 'databases', 'cloud providers')
- Problem space (e.g., 'AutoML for distributed training')"

### If User Provides Category or Problem Space

Use web search to find top alternatives:

**Search queries:**
- `"best [category] 2026"` (e.g., "best ML frameworks 2026")
- `"[category] comparison"` (e.g., "AutoML frameworks comparison")
- `"top [category] open source"` (e.g., "top databases open source")
- `"[problem] technologies"` (e.g., "distributed training technologies")

**Identify 4-6 top alternatives** and present to user:

"Based on web search, the top technologies in this space are:
1. Technology A - [1-sentence description]
2. Technology B - [1-sentence description]
3. Technology C - [1-sentence description]
4. Technology D - [1-sentence description]

**Recommendation:** Compare 2-3 technologies for depth. Which would you like to focus on? You can also add technologies not listed here."

### User Selects 2-3 Technologies

Confirm selection before proceeding.

---

## Step 2: Mode Selection

Present two modes to the user:

### Quick Mode (1-2 hours)
- Web research for each technology
- Analyze across 14 standard comparison dimensions (see `references/comparison-dimensions.md`)
- Scenario-specific analysis
- Generate full output package (report, tables, presentation, PDFs)

**Best for:**
- Time-constrained decisions
- Well-understood technology categories
- Lower-stakes choices

### Deep Mode (2-4 hours)
- Run **project-swot skill** for EACH technology (forked subagents)
  - **IMPORTANT:** Ask project-swot Phase 0 context questions (purpose, constraints, success criteria) **ONCE at the beginning**
  - Provide the same context to each project-swot subagent so user doesn't repeat themselves
- Generate comprehensive SWOT for each technology
- Compare SWOTs across scenarios
- Analyze across 14 dimensions PLUS SWOT insights
- Generate full output package with deeper analysis

**Best for:**
- High-stakes decisions (major technology investments)
- Complex technology evaluation
- Formal vendor evaluations
- Regulatory/compliance requirements

**Ask user:** "Which mode would you like? Quick (1-2h) or Deep (2-4h)?"

---

## Step 3: Scenario Definition

### Step 3.1: User Provides Primary Scenarios

"What scenarios do you want to evaluate these technologies for? Please describe the use cases where you'd use these technologies."

**Examples of good scenarios:**
- "Rapid R&D experimentation with small datasets (< 100GB)"
- "Production model training at scale (multi-TB datasets, distributed compute)"
- "Real-time inference serving with <100ms latency"
- "Cost-optimized ML workloads (minimize infrastructure costs)"

### Step 3.2: Detect Technology Category

Based on the technologies selected, detect the category:
- ML/AI Frameworks
- Databases
- Cloud Providers
- Web Frameworks
- Container Orchestration
- Message Queues / Event Streaming
- CI/CD Platforms
- Monitoring & Observability
- Infrastructure as Code
- API Gateway / Service Mesh

### Step 3.3: Suggest Additional Scenarios

Load `references/common-scenarios.md` and identify potential blind spots:

"Based on the [category] domain, you might also care about these scenarios:
- [Scenario X] - [1-sentence description]
- [Scenario Y] - [1-sentence description]
- [Scenario Z] - [1-sentence description]

Should I include any of these in the comparison?"

### Step 3.4: User Confirms Final Scenario List

### Step 3.5: Prioritize Scenarios

"Please rank your scenarios by importance:
- 🔴 **CRITICAL** - Must excel here (dealbreaker if weak)
- 🟡 **IMPORTANT** - Weighs heavily in decision
- ⚪ **NICE-TO-HAVE** - Considered but won't drive decision"

Store prioritized scenario list.

---

## Step 4: Deep Research

### Quick Mode Research

For each technology, research the following using **web search** (never use training data):

#### 4.1: Project Profile
- Current version (with date verified)
- License type
- Governance model (foundation-backed, vendor, community)
- GitHub stars, contributors, last commit (tag with `[VERIFIED-{date}]`)
- Primary use cases
- Notable adopters

#### 4.2: Analyze Across 14 Dimensions

Load `references/comparison-dimensions.md` and evaluate each technology:

1. Features & Capabilities
2. Performance & Scalability
3. Ease of Use
4. Strategic Fit & Governance (License, Vendor backing, Governance model, Contributor diversity, Ecosystem alignment)
5. Cost & Effort
6. Community & Maturity
7. Security & Compliance
8. Documentation Quality
9. Integration Ecosystem
10. Vendor Lock-In Risk
11. Production Readiness
12. Support Options
13. Migration Path
14. Operational Complexity

For each dimension, score each technology and provide notes.

#### 4.3: Bias Prevention (Forked Subagents)

**CRITICAL:** Apply `references/bias-prevention.md` patterns:

For each technology, fork TWO separate subagents:

**Subagent 1: Positive Analysis (Strengths + Opportunities)**
- Research ONLY positive aspects (strengths, opportunities)
- Do NOT analyze weaknesses or compare to other technologies
- Tag findings as `[VERIFIED-{date}]` or `[CLAIMED]`
- Return structured findings

**Subagent 2: Negative Analysis (Weaknesses + Threats)**
- Research ONLY negative aspects (weaknesses, threats, limitations)
- Do NOT analyze strengths or compare to other technologies
- Tag weaknesses as `[FUNDAMENTAL]` (architectural) or `[CURRENT-STATE]` (may be fixed)
- Return structured findings

**After both complete:** Merge results into unified technology profile.

#### 4.4: Scenario-Specific Analysis

For EACH scenario, evaluate:
- Which technology is best fit? Why?
- Which technology is runner-up? Why?
- Are there dealbreaker limitations for any technology in this scenario?

Tag each technology for each scenario: **Best Fit**, **Runner-Up**, or **Poor Fit**.

---

### Deep Mode Research

#### 4.1: Run project-swot for Each Technology

**IMPORTANT - Single Context Collection:**

Before launching project-swot subagents, ask the user **Phase 0 context questions ONCE**:

1. What's the purpose of this evaluation? (Adoption decision, investment tracking, competitive intelligence, dependency audit, general research)
2. What's your current relationship with these technologies?
3. What would you need to learn from this analysis to consider it useful?
4. Are there any hard constraints? (licensing, deployment model, integration needs, team expertise)

**Then launch project-swot for each technology**, providing the SAME context to each subagent:

```
Launch 3 project-swot subagents in parallel (or sequentially if preferred):

Subagent 1: project-swot for Technology A
- Provide Phase 0 context: [user's purpose, constraints, success criteria]
- Generate complete SWOT with recommendations

Subagent 2: project-swot for Technology B
- Provide Phase 0 context: [same context as above]
- Generate complete SWOT with recommendations

Subagent 3: project-swot for Technology C
- Provide Phase 0 context: [same context as above]
- Generate complete SWOT with recommendations
```

#### 4.2: Compare SWOTs Across Scenarios

For each scenario:
- Which technology's strengths align best?
- Which technology's weaknesses are dealbreakers?
- How do opportunities/threats compare?

#### 4.3: Dimension Analysis (Enriched by SWOT)

Analyze 14 dimensions using SWOT insights as additional context.

---

## Step 5: Context Integration (Optional)

Ask user:

"Do you have any additional context files I should consider? For example:
- Meeting notes where options were discussed
- Requirements documents
- Architecture diagrams
- Existing documentation

You can provide file paths or paste content."

**If user provides files:** Read and integrate into analysis.

---

## Step 6: Synthesis & Recommendations

### 6.1: Generate Scenario-Specific Recommendations

Load `references/decision-framework-patterns.md` and select appropriate pattern(s):

**Pattern 1: Per-Scenario Winner Matrix** (always generate)
- Show which technology wins each scenario
- Include runner-up for each scenario
- Provide rationale tied to specific strengths/weaknesses

**Pattern 2: Scenario Priority Weighting** (if user prioritized scenarios)
- Calculate weighted scores based on CRITICAL/IMPORTANT/NICE-TO-HAVE
- Present primary recommendation with score breakdown

**Pattern 3: Conditional Recommendations** (always generate)
- "Choose Technology A if..."
- "Choose Technology B if..."
- "Choose Technology C if..."

**Pattern 4-7:** Use as appropriate based on user context.

### 6.1.1: Deep Mode Synthesis Guidelines

**CRITICAL:** When synthesizing Deep Mode results from individual project-swot analyses:

**Scope to User's Scenarios:**
- Base primary recommendations ONLY on the scenarios the user provided
- Do NOT expand to additional scenarios without explicit user request
- If suggesting additional scenarios, clearly separate:
  - **Primary Recommendation** (based on user's stated scenarios)
  - **Alternative Strategy** (if considering expanded scenarios)

**Avoid Over-Architecting:**
- For 2-3 scenarios: Provide **scenario-specific winners** (Pattern 1 + Pattern 3)
- For 4+ diverse scenarios: Consider **hybrid/platform strategies** (Pattern 4)
- Do NOT recommend "platform architecture" for simple 2-3 scenario comparisons

**Example - Correct Synthesis for 2 Scenarios:**
```markdown
## Recommendations (Based on Your 2 Scenarios)

| Scenario | Best Fit | Why |
|----------|----------|-----|
| Rapid R&D Experimentation | AutoGluon | [rationale] |
| Cost-Optimized ML | FLAML + Ray Tune | [rationale] |

**Recommendation:**
- If you prioritize Scenario 1 → Choose AutoGluon
- If you prioritize Scenario 2 → Choose FLAML
- If you need both → Consider deploying both technologies for different use cases

---

## Alternative: Multi-Technology Platform (Optional)

If your needs extend beyond these 2 scenarios to include [list additional
scenarios like LLM fine-tuning, multi-tenant platform, etc.], consider a
platform approach with technology routing based on workload characteristics.

[Platform architecture details here]
```

**Align with Individual SWOTs:**
- Each technology's role in synthesis should match its individual SWOT recommendation
- If individual SWOT says "ADOPT" → synthesis should recommend adoption
- If discrepancy exists, explicitly explain why:

```markdown
Technology | Individual SWOT | Synthesis Role | Alignment
-----------|----------------|----------------|----------
Tech A     | MAINTAIN       | High-Accuracy  | ✅ Consistent
Tech B     | ADOPT          | Distributed    | ✅ Consistent
Tech C     | EVALUATE       | Resource-Eff.  | ⚠️ Note: Wins "Cost-Optimized" scenario but marked EVALUATE due to [reason]
```

### 6.2: Acknowledge Trade-Offs

If no single technology wins all CRITICAL scenarios:
- Present trade-off analysis
- Use conditional recommendations
- Consider hybrid strategies (Pattern 4)

### 6.3: Human Validation Checkpoint

Before finalizing, present synthesis and ask:

"Here's my assessment. Does this align with your understanding? What am I missing about your situation?"

---

## Step 7: Output Generation

Generate complete output package:

### 7.1: Detailed Markdown Report

Create `[comparison_name]_report.md`:

```markdown
# Technology Comparison: [Tech A] vs [Tech B] vs [Tech C]

**⚠️ DISCLAIMER: This report is AI generated with minimal human input and validation.**

**Date:** [Current date]
**Technologies:** [List]
**Scenarios:** [List with priorities]

---

## Executive Summary

[2-3 paragraph synthesis]

**Bottom Line:** [Primary recommendation with key trade-offs]

---

## Technology Profiles

### Technology A
[Project profile with metrics tagged [VERIFIED-{date}]]

### Technology B
[...]

### Technology C
[...]

---

## Scenario-Specific Recommendations

[Per-scenario winner matrix from Pattern 1]

---

## Comparison Dimensions

### 1. Features & Capabilities
[Technology A: score + notes]
[Technology B: score + notes]
[Technology C: score + notes]

### 2. Performance & Scalability
[...]

[... all 14 dimensions ...]

---

## Decision Framework

[Conditional recommendations from Pattern 3]

**Choose Technology A if:**
- [Condition 1]
- [Condition 2]

**Choose Technology B if:**
- [Condition 1]
- [Condition 2]

[...]

---

## Trade-Off Analysis

[When no single winner exists across all scenarios]

---

## Recommendations

[Primary recommendation with rationale]
[Alternative recommendations]
[Monitoring plan / re-evaluation triggers if applicable]

---

## Sources Consulted

[All URLs with access dates]

---

## Methodology Notes

- Positive and negative analysis conducted in separate forked contexts
- All metrics fetched fresh on [date]
- User-provided context integrated in Step 5
```

### 7.2: Generate Comparison Tables

Run `scripts/create_comparison_tables.py`:

```bash
python3 scripts/create_comparison_tables.py comparison_data.json comparison_tables.md
```

This generates:
- Quick reference table (license, governance, maturity, etc.)
- Scenario winner matrix
- Feature comparison matrix (emoji-based)
- Detailed dimension tables

### 7.3: Generate Decision Matrix

Run `scripts/generate_decision_matrix.py`:

```bash
python3 scripts/generate_decision_matrix.py comparison_data.json decision_matrix.json
```

This generates weighted scores, overall recommendation, and conditional recommendations.

### 7.4: Create PowerPoint Presentation

Run `scripts/create_comparison_presentation.py`:

```bash
python3 scripts/create_comparison_presentation.py comparison_data.json comparison_presentation.pptx
```

This generates:
- Slide 1: Title with disclaimer
- Slide 2+: Scenario analysis
- Slides: Dimension comparison tables
- Final slide: Recommendations

### 7.5: Convert to PDFs

**Report PDF:**
```bash
pandoc [comparison_name]_report.md -o [comparison_name]_report.pdf --pdf-engine=tectonic -V geometry:margin=1in
```

**Presentation PDF:**
```bash
soffice --headless --convert-to pdf --outdir . comparison_presentation.pptx
```

### 7.6: Verify All Files Created

Confirm:
1. `[comparison_name]_report.md` - Detailed markdown report
2. `[comparison_name]_report.pdf` - Detailed PDF report
3. `comparison_tables.md` - Markdown tables
4. `comparison_data.json` - Structured data (for scripts)
5. `decision_matrix.json` - Weighted scores and recommendations
6. `comparison_presentation.pptx` - PowerPoint presentation
7. `comparison_presentation.pdf` - Presentation PDF

### 7.7: Present Summary to User

List all generated files with sizes and brief description.

---

## Resources

### references/
- **comparison-dimensions.md** - 14 standard comparison dimensions for all technology types
- **common-scenarios.md** - Technology-specific scenario suggestions (ML/AI, databases, cloud, etc.)
- **decision-framework-patterns.md** - 7 patterns for multi-scenario recommendations
- **bias-prevention.md** - AI failure modes and safeguards (forked subagents, fresh data, etc.)

### scripts/
- **create_comparison_tables.py** - Generate markdown comparison tables from structured data
- **generate_decision_matrix.py** - Calculate weighted scores and recommendations
- **create_comparison_presentation.py** - Generate PowerPoint presentation

---

## Key Principles Summary

1. **User scenarios first** - User defines scenarios, skill suggests additional relevant ones
2. **Multi-scenario analysis** - Different technologies win different scenarios
3. **No forced single winner** - Use conditional recommendations when trade-offs exist
4. **Bias prevention** - Fork positive/negative subagents, always web search for fresh data
5. **Scenario-specific recommendations** - Per-scenario winner matrix + conditional "Choose X if..."
6. **Comprehensive output** - Markdown report, tables, decision matrix, presentation, PDFs
7. **Human validation** - Checkpoints at scenario definition, synthesis, and before final output
8. **Deep mode context reuse** - Ask project-swot Phase 0 questions once, provide to all subagents

---

## Example Triggers

**ML/AI Frameworks:**
- "Compare PyTorch, TensorFlow, and JAX for deep learning research"
- "Which AutoML framework should I use for production?"
- "Evaluate Hugging Face Transformers vs DeepSpeed for LLM fine-tuning"

**Databases:**
- "Compare PostgreSQL, MongoDB, and Cassandra for our application"
- "Which database for time-series data - InfluxDB, TimescaleDB, or Prometheus?"

**Infrastructure:**
- "Evaluate Kubernetes, Docker Swarm, and Nomad for our microservices"
- "Help me choose between AWS, GCP, and Azure"
- "Compare Terraform, Pulumi, and CloudFormation for infrastructure as code"

**Web Frameworks:**
- "Compare React, Vue, and Svelte for building a dashboard"
- "Which backend framework - Django, FastAPI, or Express.js?"

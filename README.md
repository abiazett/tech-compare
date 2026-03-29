# Tech-Compare

A Claude Code skill for structured, unbiased comparison of 2-3 technologies across multiple user-defined scenarios.

## Overview

Tech-Compare helps you make informed technology decisions by:
- Comparing technologies across **your specific scenarios** (not forced general recommendations)
- Using **forked subagents** to prevent bias (separate positive/negative analysis)
- Generating **comprehensive deliverables** (reports, tables, presentations, PDFs)
- Supporting **two depth levels**: Quick (1-2h web research) or Deep (2-4h with full SWOT analysis)

**Core Principle:** In technology comparisons, there is rarely a single "winner" across all scenarios. Different technologies excel at different use cases. This skill helps you understand **which technology fits which scenario**.

---

## Two Analysis Modes

### Quick Mode (1-2 hours)

**Best for:**
- Time-constrained decisions
- Well-understood technology categories
- Lower-stakes choices

**What it does:**
- Web research for each technology (always fresh data, never training data)
- Analysis across 14 standard comparison dimensions
- Scenario-specific fit analysis
- Forked subagents for bias prevention (separate positive/negative analysis)

**Deliverables:**
1. Detailed markdown report (`[name]_report.md`)
2. Comparison tables (`comparison_tables.md`)
3. Decision matrix with weighted scores (`decision_matrix.json`)
4. PowerPoint presentation (`comparison_presentation.pptx`)
5. PDFs (report + presentation)

---

### Deep Mode (2-4 hours)

**Best for:**
- High-stakes decisions (major technology investments)
- Complex technology evaluation
- Formal vendor evaluations
- Regulatory/compliance requirements

**What it does:**
- Everything from Quick Mode, PLUS:
- Runs **[project-swot](https://github.com/jwforres/project-swot)** skill for EACH technology
- Generates comprehensive SWOT analysis for each technology
- Compares SWOTs across scenarios
- Deeper implications analysis with risk assessment

**Deliverables:**
- All Quick Mode deliverables
- Individual SWOT reports for each technology (markdown + PDF + presentation)
- Synthesized cross-technology comparison with SWOT insights

**Optional Dependency:**
- [project-swot skill](https://github.com/jwforres/project-swot) - Required for Deep Mode
- If not installed, skill will gracefully fall back to Quick Mode

---

## Installation

### 1. Install Software Dependencies

This skill generates PDFs and PowerPoint presentations. Install required packages:

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

### 2. Install the Skill

Place the `tech-compare` directory in your Claude Code skills folder:
```
~/.claude/skills/tech-compare/
```

### 3. (Optional) Install project-swot for Deep Mode

For Deep Mode analysis, install the [project-swot skill](https://github.com/jwforres/project-swot):
```
~/.claude/skills/project-swot/
```

---

## Usage

### Basic Workflow

1. **Trigger the skill** with any of these phrases:
   - "Compare PostgreSQL, MongoDB, and Cassandra"
   - "Which is better - React or Vue?"
   - "Evaluate Kubernetes vs Docker Swarm for our microservices"
   - "Help me choose between AWS, GCP, and Azure"

2. **Select mode:** Quick (2-4h) or Deep (1-2 days)

3. **Define scenarios:** Describe the use cases where you'd use these technologies
   - Example: "High-write workloads with millions of records/day"
   - Example: "Real-time analytics with sub-second query latency"
   - The skill will suggest additional relevant scenarios based on technology category

4. **Prioritize scenarios:** Mark each as CRITICAL, IMPORTANT, or NICE-TO-HAVE

5. **Review deliverables:** The skill generates complete output package automatically

### Example Session

```
You: Compare PyTorch, TensorFlow, and JAX for deep learning research

Claude: I'll compare these three frameworks. Which mode would you like?
- Quick (2-4h): Web research + 14 dimensions analysis
- Deep (1-2 days): Full SWOT for each + comprehensive comparison

You: Quick mode

Claude: What scenarios do you want to evaluate for?

You:
1. Research prototyping with novel architectures
2. Production deployment at scale
3. Multi-GPU training

Claude: Based on deep learning frameworks, you might also care about:
- Distributed training across clusters
- Edge deployment for inference
- Integration with existing ML pipelines

Should I include any of these?

You: Add distributed training

Claude: Please rank scenarios by importance (CRITICAL/IMPORTANT/NICE-TO-HAVE)...

[Skill completes analysis and generates deliverables]
```

---

## Comparison Dimensions

The skill analyzes technologies across 14 standard dimensions:

1. **Features & Capabilities** - Core functionality and unique features
2. **Performance & Scalability** - Throughput, latency, horizontal/vertical scaling
3. **Ease of Use** - Learning curve, API design, developer experience
4. **Strategic Fit & Governance** - License, vendor backing, governance model
5. **Resource Efficiency** - Compute, memory, GPU requirements (relative comparisons)
6. **Community & Maturity** - Project health, adoption, release cadence
7. **Security & Compliance** - Security features, vulnerability track record
8. **Documentation Quality** - Completeness, accuracy, examples
9. **Integration Ecosystem** - Third-party integrations, plugin ecosystem
10. **Vendor Lock-In Risk** - Portability, proprietary dependencies
11. **Production Readiness** - Stability, SLA support, enterprise adoption
12. **Support Options** - Commercial support, community support
13. **Migration Path** - Ease of migration from/to alternatives
14. **Operational Complexity** - Deployment, monitoring, maintenance overhead

---

## Decision Framework Patterns

The skill uses 7 proven decision patterns to synthesize findings:

1. **Per-Scenario Winner Matrix** - Show which technology wins each scenario
2. **Scenario Priority Weighting** - Weighted scores based on scenario importance
3. **Conditional Recommendations** - "Choose X if..." guidance
4. **Hybrid/Multi-Technology Strategies** - Using different tools for different scenarios
5. **Risk-Based Decision Framework** - Risk tolerance-based recommendations
6. **Gap Analysis with Migration Estimates** - Implementation effort comparison
7. **Phased Decision with Re-evaluation** - Start with one, set conditions to switch

See `references/decision-framework-patterns.md` for detailed examples.

---

## Technology Categories

The skill has optimized scenario suggestions for:

- **ML/AI Frameworks** - Deep learning, AutoML, model training, inference
- **Databases** - Relational, NoSQL, time-series, graph, vector
- **Cloud Providers** - AWS, GCP, Azure, multi-cloud, hybrid cloud
- **Web Frameworks** - Frontend (React, Vue, Svelte), Backend (Django, FastAPI)
- **Container Orchestration** - Kubernetes, Docker Swarm, Nomad
- **Message Queues / Event Streaming** - Kafka, RabbitMQ, Pulsar, NATS
- **CI/CD Platforms** - Jenkins, GitLab CI, GitHub Actions, CircleCI
- **Monitoring & Observability** - Prometheus, Datadog, Grafana, OpenTelemetry
- **Infrastructure as Code** - Terraform, Pulumi, CloudFormation, Ansible
- **API Gateway / Service Mesh** - Kong, Istio, Envoy, Traefik

See `references/common-scenarios.md` for detailed scenarios per category.

---

## Technical Focus

**IMPORTANT:** This skill provides **technical comparison**, not business case analysis.

**Focus areas:**
- Technical capabilities and features
- Performance characteristics (throughput, latency, scalability)
- Resource efficiency (relative comparisons: "10x more memory", "50% fewer CPU cycles")
- Implementation complexity (High/Medium/Low qualitative assessments)
- Integration requirements and compatibility
- Operational characteristics (monitoring, debugging, maintenance)

**Explicitly excluded:**
- Specific cost estimates or budgets (e.g., "$275K year 1")
- ROI calculations or payback periods
- Detailed implementation timelines with month-by-month breakdowns
- Financial modeling or business case analysis

If you need cost/timeline analysis, take the technical comparison output to your finance/planning teams.

---

## Bias Prevention

The skill actively guards against common AI comparison pitfalls:

| Pitfall | Prevention |
|---------|------------|
| **Outdated Knowledge** | Always web search; never rely on training data for metrics |
| **Marketing Language** | Translate all claims to specific technical capabilities |
| **Stale Metrics** | Fetch fresh data; include retrieval dates for all metrics |
| **Anchoring Bias** | Forked subagents analyze positive/negative separately |
| **Surface-Level Analysis** | Analyze complete architecture, not just API surface |
| **Overconfidence** | Tag claims as [VERIFIED] or [CLAIMED]; acknowledge uncertainty |
| **Governance Blindness** | Explicitly research project governance, not just features |

See `references/bias-prevention.md` for detailed safeguards.

---

## Output Files

### Quick Mode

```
output/
├── [comparison_name]_report.md          # Detailed markdown report
├── [comparison_name]_report.pdf         # PDF version
├── comparison_tables.md                 # Quick reference tables
├── comparison_data.json                 # Structured data (for scripts)
├── decision_matrix.json                 # Weighted scores
├── comparison_presentation.pptx         # PowerPoint slides
└── comparison_presentation.pdf          # Presentation PDF
```

### Deep Mode (Additional Files)

```
output/
├── [tech_a]_swot_analysis.md           # Full SWOT for Technology A
├── [tech_a]_swot_report.pdf            # PDF version
├── [tech_a]_swot_overview.pptx         # PowerPoint slides
├── [tech_a]_swot_overview.pdf          # Presentation PDF
├── [tech_b]_swot_analysis.md           # Full SWOT for Technology B
├── [tech_b]_swot_report.pdf            # ...
├── [tech_c]_swot_analysis.md           # Full SWOT for Technology C
└── [synthesis]_platform_strategy.md    # Cross-technology synthesis
```

---

## File Structure

```
tech-compare/
├── SKILL.md                            # Main skill definition
├── README.md                           # This file
├── references/
│   ├── comparison-dimensions.md        # 14 standard dimensions
│   ├── common-scenarios.md             # Category-specific scenarios
│   ├── decision-framework-patterns.md  # 7 decision patterns
│   └── bias-prevention.md              # AI safeguards
└── scripts/
    ├── create_comparison_tables.py     # Generate markdown tables
    ├── generate_decision_matrix.py     # Calculate weighted scores
    └── create_comparison_presentation.py  # Generate PowerPoint
```

---

## Example Use Cases

**Scenario 1: Database Selection**
- Compare PostgreSQL, MongoDB, Cassandra for high-write application
- Quick Mode: 2-hour analysis
- Output: Scenario-specific recommendations (PostgreSQL for ACID, Cassandra for scale)

**Scenario 2: ML Framework Evaluation**
- Compare PyTorch, TensorFlow, JAX for research lab
- Deep Mode: Full SWOT analysis for each framework
- Output: Technical architecture with conditional recommendations

**Scenario 3: Cloud Provider Decision**
- Compare AWS, GCP, Azure for startup
- Quick Mode with cost-efficiency scenario
- Output: Feature matrix, migration path analysis, vendor lock-in assessment

---

## Related Skills

- **[project-swot](https://github.com/jwforres/project-swot)** - Single-project SWOT analysis (required for Deep Mode)
- **skill-creator** - Create and modify Claude Code skills
- **update-config** - Configure Claude Code permissions and settings

---

## Contributing

Contributions welcome! Areas for improvement:
- Additional technology categories in `common-scenarios.md`
- More decision framework patterns
- Additional comparison dimensions
- Example comparisons for documentation

---

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

## Support

For issues, questions, or contributions:
- GitHub: https://github.com/abiazett/tech-compare
- Issues: https://github.com/abiazett/tech-compare/issues
- Documentation: See `SKILL.md` and `references/` folder

---

**Last Updated:** 2026-03-29
**Version:** 2.0 (Technical Focus)

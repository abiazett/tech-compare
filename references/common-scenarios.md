# Common Scenarios by Technology Type

**Purpose:** Help users identify blind spots in their scenario coverage by suggesting additional relevant scenarios they may not have considered.

**Important:** These are SUGGESTIONS, not requirements. The user always provides their primary scenarios first, then the skill suggests additional ones from this list that might be relevant.

---

## ML/AI Frameworks & Platforms

### Integrated customer scenarios:

1. **Rapid R&D Experimentation** - Data scientists exploring models, quick prototyping, interactive development (small-medium datasets, notebooks, fast feedback)

2. **Production Model Training at Scale** - Enterprise datasets, automated pipelines, scheduled retraining (100GB-multi-TB, distributed compute, MLOps)

3. **Real-Time Inference Serving** - Interactive applications needing immediate predictions (low latency <100ms, high availability, auto-scaling)

4. **Batch Inference & Scoring** - Offline processing of large volumes (millions-billions of records, cost optimization, scheduled jobs)

5. **LLM & Generative AI Workloads** - Fine-tuning large language models, prompt engineering, RAG systems (large models, LoRA/QLoRA, high GPU memory)

6. **Edge AI Deployment** - Models on edge devices, on-premise servers, disconnected environments (resource constraints, offline capability, compression)

7. **Multi-Tenant Platform** - Shared ML platform for multiple teams/departments/customers (isolated workspaces, quotas, governance, RBAC)

8. **Continuous Learning Systems** - Models that auto-retrain on new data, adapt to drift (online learning, pipelines, monitoring, versioning)

9. **Cost-Optimized ML Workloads** - Maximize quality while minimizing infrastructure costs (spot instances, CPU when possible, cost-aware HPO)

10. **Hybrid & Multi-Cloud ML** - Span on-premise and public clouds, data sovereignty compliance (data gravity, regulatory constraints, cloud bursting)

11. **AutoML for Citizen Data Scientists** - Business analysts building models without ML expertise (automated feature engineering, model selection, no-code)

12. **Classical ML on Structured Data** - Tabular data analysis with XGBoost/LightGBM (distributed gradient boosting, feature engineering, explainability)

13. **Computer Vision Pipelines** - Image/video analysis (large datasets, GPU-intensive training, real-time inference, model compression)

14. **Mission-Critical Production Systems** - ML powering business-critical operations (zero downtime, SLAs, disaster recovery, audit trails)

15. **Regulated & Air-Gapped Environments** - Government, defense, healthcare with strict compliance (disconnected operation, governance, certifications)

### Example triggers:
- "Compare AutoML frameworks for production deployment"
- "Which ML framework for rapid prototyping and edge deployment?"
- "Evaluate hyperparameter optimization tools for distributed training"
- "Compare deep learning frameworks for LLM fine-tuning"

---

## Databases

### Typical scenarios:
1. **High-write workloads** - Heavy insert/update operations, event streaming
2. **Complex analytical queries** - Joins, aggregations, OLAP workloads
3. **Horizontal scaling** - Distributed data across multiple nodes
4. **Real-time analytics** - Sub-second query latency on fresh data
5. **Transactional consistency** - ACID guarantees, strong consistency
6. **Schema flexibility** - Evolving data models, unstructured data

### Example triggers:
- "Compare PostgreSQL, MySQL, MongoDB"
- "Which database for time-series data?"
- "Evaluate Cassandra vs ScyllaDB vs CockroachDB"

---

## Cloud Providers

### Typical scenarios:
1. **Startup/small scale** - Low initial costs, simple pricing, easy to start
2. **Enterprise scale** - Multi-region, high availability, compliance certifications
3. **Hybrid cloud** - On-premise + cloud integration, data sovereignty
4. **Multi-cloud** - Avoid vendor lock-in, geographic distribution
5. **Managed services** - Minimize operational overhead, serverless options
6. **Cost optimization** - Reserved instances, spot instances, auto-scaling

### Example triggers:
- "Compare AWS, GCP, Azure"
- "Which cloud for ML workloads?"
- "Evaluate cloud providers for startup"

---

## Web Frameworks

### Typical scenarios:
1. **Rapid MVP development** - Fast time-to-market, scaffolding, conventions
2. **Large-scale applications** - Performance at scale, code organization, maintainability
3. **Real-time features** - WebSockets, server-sent events, live updates
4. **SEO-critical sites** - Server-side rendering, static site generation
5. **API-first architecture** - RESTful APIs, GraphQL, microservices
6. **Developer productivity** - Hot reload, TypeScript support, debugging tools

### Example triggers:
- "Compare React, Vue, Angular, Svelte"
- "Which framework for e-commerce site?"
- "Evaluate Next.js vs Remix vs SvelteKit"

---

## Container Orchestration

### Typical scenarios:
1. **Microservices deployment** - Service discovery, load balancing, auto-scaling
2. **CI/CD integration** - Automated deployments, rolling updates, canary releases
3. **Multi-tenancy** - Namespace isolation, resource quotas, RBAC
4. **Stateful workloads** - Persistent volumes, StatefulSets, data persistence
5. **Edge computing** - Lightweight orchestration, resource-constrained nodes
6. **Cost optimization** - Efficient resource utilization, bin packing, spot instances

### Example triggers:
- "Compare Kubernetes, Docker Swarm, Nomad"
- "Which orchestrator for edge deployment?"
- "Evaluate managed Kubernetes services"

---

## Message Queues / Event Streaming

### Typical scenarios:
1. **High throughput** - Millions of messages per second
2. **Low latency** - Sub-millisecond message delivery
3. **Event sourcing** - Durable event log, replay capability
4. **Guaranteed delivery** - At-least-once or exactly-once semantics
5. **Stream processing** - Real-time transformations, aggregations
6. **Multi-datacenter replication** - Geographic distribution, disaster recovery

### Example triggers:
- "Compare Kafka, RabbitMQ, Pulsar, NATS"
- "Which message queue for microservices?"
- "Evaluate event streaming platforms"

---

## CI/CD Platforms

### Typical scenarios:
1. **Multi-language support** - Diverse tech stack, polyglot teams
2. **Self-hosted** - On-premise deployment, air-gapped environments
3. **Cloud-native** - SaaS, minimal setup, managed infrastructure
4. **Complex pipelines** - Parallel stages, conditional workflows, matrix builds
5. **Container-first** - Docker builds, Kubernetes deployments
6. **Cost-sensitive** - Open source, free tier, compute efficiency

### Example triggers:
- "Compare Jenkins, GitLab CI, GitHub Actions, CircleCI"
- "Which CI/CD for Kubernetes deployments?"
- "Evaluate self-hosted vs cloud CI/CD"

---

## Monitoring & Observability

### Typical scenarios:
1. **Metrics collection** - Time-series metrics, dashboards, alerting
2. **Distributed tracing** - Request flows across microservices
3. **Log aggregation** - Centralized logging, search, analysis
4. **APM (Application Performance Monitoring)** - Code-level insights, profiling
5. **Cloud-native** - Kubernetes monitoring, container metrics
6. **Cost optimization** - Data retention, sampling, efficient storage

### Example triggers:
- "Compare Prometheus, Datadog, New Relic, Grafana Cloud"
- "Which monitoring for microservices?"
- "Evaluate observability platforms"

---

## Infrastructure as Code

### Typical scenarios:
1. **Multi-cloud** - AWS + GCP + Azure support
2. **Declarative configuration** - Desired state, idempotent operations
3. **Modular and reusable** - Modules, components, templates
4. **State management** - Remote state, locking, collaboration
5. **Policy as code** - Compliance checks, security scanning
6. **GitOps workflow** - Version control, code review, automated deployment

### Example triggers:
- "Compare Terraform, Pulumi, CloudFormation, Ansible"
- "Which IaC for multi-cloud?"
- "Evaluate declarative vs imperative IaC"

---

## API Gateway / Service Mesh

### Typical scenarios:
1. **Traffic management** - Load balancing, circuit breaking, retries
2. **Security** - mTLS, authentication, authorization
3. **Observability** - Metrics, tracing, logging
4. **Rate limiting** - Quota management, throttling
5. **Multi-protocol** - HTTP, gRPC, WebSocket support
6. **Cloud-native** - Kubernetes integration, service discovery

### Example triggers:
- "Compare Kong, Istio, Envoy, Traefik"
- "Which API gateway for microservices?"
- "Evaluate service mesh options"

---

## Usage Pattern

### Correct workflow:

1. **User provides their scenarios FIRST** (from their trigger phrase)
   - Example: "Compare Katib, AutoGluon, FLAML for: (1) production training at scale, (2) rapid prototyping"

2. **Detect technology category** based on the technologies mentioned
   - Example: "Katib, AutoGluon, FLAML" → ML/AI Frameworks category

3. **Analyze user's scenarios** and identify potential blind spots
   - User said: production training, rapid prototyping
   - Missing common scenarios: cost optimization, edge deployment, multi-tenant platform

4. **Suggest additional relevant scenarios**
   - "Based on ML frameworks, you might also care about:"
   - "(3) Cost-Optimized ML Workloads"
   - "(4) Edge AI Deployment"
   - "(5) Multi-Tenant Platform"
   - "Should I include any of these in the comparison?"

5. **User confirms/rejects suggestions**
   - "Yes, add cost-optimized workloads"
   - "Skip edge deployment and multi-tenant"

### Key principles:

- **User scenarios are primary** - Always start with what the user specified
- **Suggestions are helpers** - Help identify blind spots, not replace user input
- **User has final say** - They can accept, reject, or modify any suggestions
- **Custom scenarios welcome** - Users can provide scenarios not in this list
- **Technology-aware suggestions** - Only suggest scenarios relevant to the technology category

### When scenarios are unclear:
If user doesn't provide clear scenarios:
- Ask: "What scenarios do you want to evaluate these technologies for?"
- Optionally show 3-4 most common scenarios for that technology type as examples
- Let user describe their use cases in their own words

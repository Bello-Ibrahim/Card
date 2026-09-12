export type Solution = {
  slug: string;
  title: string;
  summary: string;
  description: string;
  capabilities: string[];
  outcomes: string[];
  technologies: string[];
  cta: string;
  /** Grouping used for the solutions index filter. */
  category: "Platform" | "Data Management" | "Enablement";
};

export const solutions: Solution[] = [
  {
    slug: "modern-data-platform",
    title: "Modern Data Platform",
    summary: "Build a scalable foundation for analytics, reporting, machine learning and AI.",
    description:
      "A single, governed platform that ingests data from across the business, transforms it into modelled datasets, and serves analytics, data science and operational use cases from the same foundation — with orchestration, testing, observability and CI/CD built in from day one.",
    capabilities: [
      "Architecture",
      "Data ingestion",
      "Transformation",
      "Orchestration",
      "Governance",
      "Observability",
      "CI/CD",
    ],
    outcomes: [
      "One governed foundation serving BI, data science and AI",
      "New data sources onboarded through a repeatable path",
      "Platform changes shipped safely behind automated tests",
    ],
    technologies: ["Snowflake", "Databricks", "BigQuery", "dbt", "Apache Airflow", "Terraform"],
    cta: "Explore Modern Data Platforms",
    category: "Platform",
  },
  {
    slug: "enterprise-data-warehouse",
    title: "Enterprise Data Warehouse",
    summary: "A governed, well-modelled warehouse the whole organization can rely on.",
    description:
      "A conformed warehouse layer with agreed definitions, documented models and predictable performance — designed so finance, operations and commercial teams reconcile to the same numbers instead of maintaining competing extracts.",
    capabilities: [
      "Dimensional modelling",
      "Conformed dimensions",
      "Metric definitions",
      "Access control",
      "Performance tuning",
      "Historization",
    ],
    outcomes: [
      "Consistent reporting across departments",
      "Query performance that holds as the business grows",
      "Auditable history for regulated reporting",
    ],
    technologies: ["Snowflake", "Amazon Redshift", "BigQuery", "SQL Server", "dbt"],
    cta: "Explore Data Warehousing",
    category: "Platform",
  },
  {
    slug: "lakehouse",
    title: "Lakehouse",
    summary: "Open storage with warehouse-grade reliability for analytics and AI workloads.",
    description:
      "An open table format foundation that keeps raw and modelled data in one place, supports both SQL analytics and machine learning, and avoids duplicating the estate across a lake and a warehouse that slowly diverge.",
    capabilities: [
      "Open table formats",
      "Medallion layering",
      "Schema evolution",
      "Time travel",
      "Streaming ingestion",
      "Workload isolation",
    ],
    outcomes: [
      "One copy of the data serving SQL and ML workloads",
      "Storage costs decoupled from compute",
      "Reproducible datasets for model training",
    ],
    technologies: ["Databricks", "Delta Lake", "Apache Iceberg", "Apache Spark", "Microsoft Fabric"],
    cta: "Explore Lakehouse Architecture",
    category: "Platform",
  },
  {
    slug: "real-time-data-platform",
    title: "Real-Time Data Platform",
    summary: "Streaming pipelines for decisions that cannot wait for tomorrow's batch.",
    description:
      "Event streaming and change-data-capture pipelines for the use cases where latency genuinely changes the outcome — operational monitoring, fraud and risk signals, live inventory and personalization — engineered with the same testing and observability discipline as batch.",
    capabilities: [
      "Event streaming",
      "Change-data-capture",
      "Stream processing",
      "Exactly-once semantics",
      "Latency monitoring",
      "Replay and recovery",
    ],
    outcomes: [
      "Operational decisions made on current data",
      "Streaming and batch reconciled to the same definitions",
      "Clear, measured latency budgets per use case",
    ],
    technologies: ["Apache Kafka", "Apache Flink", "Debezium", "Apache Spark", "Kinesis"],
    cta: "Explore Real-Time Data",
    category: "Platform",
  },
  {
    slug: "data-migration",
    title: "Data Migration",
    summary: "Move off legacy infrastructure with evidence, not optimism.",
    description:
      "A structured migration programme that inventories every workload and consumer, proves equivalence through parallel runs, and moves in validated slices — so the legacy platform is decommissioned only once the new one demonstrably matches it.",
    capabilities: [
      "Workload inventory",
      "Dependency mapping",
      "Automated conversion",
      "Parallel-run validation",
      "Cutover planning",
      "Decommissioning",
    ],
    outcomes: [
      "Cutover risk reduced to a rehearsed, reversible step",
      "Downstream consumers migrated deliberately",
      "Legacy maintenance and licensing genuinely retired",
    ],
    technologies: ["SQL Server", "Oracle", "Teradata", "Snowflake", "BigQuery", "Databricks"],
    cta: "Explore Data Migration",
    category: "Data Management",
  },
  {
    slug: "data-integration",
    title: "Data Integration",
    summary: "Connect the systems that were never designed to work together.",
    description:
      "An integration layer across SaaS applications, internal databases, partner feeds and APIs — with contracts, retry and rate-limit handling, and reconciliation, so the business works from one consistent record of what happened.",
    capabilities: [
      "API integration",
      "ETL and ELT",
      "Streaming ingestion",
      "Entity resolution",
      "Data contracts",
      "Reconciliation",
    ],
    outcomes: [
      "A reconciled view across fragmented systems",
      "Predictable onboarding for each new source",
      "Integration failures that surface with context",
    ],
    technologies: ["Python", "Airbyte", "Fivetran", "Apache Kafka", "REST & GraphQL APIs"],
    cta: "Explore Data Integration",
    category: "Data Management",
  },
  {
    slug: "data-quality",
    title: "Data Quality & Observability",
    summary: "Detect problems before the business does.",
    description:
      "A quality framework that defines what correct means for your critical datasets, tests it continuously, and routes failures to the team that owns the data — with severity levels and response expectations set in advance.",
    capabilities: [
      "Quality rule design",
      "Automated testing",
      "Freshness and volume monitoring",
      "Anomaly detection",
      "Incident response",
      "Quality reporting",
    ],
    outcomes: [
      "Problems caught upstream of dashboards",
      "Named owners for every critical dataset",
      "Reliability tracked as a measurable target",
    ],
    technologies: ["dbt tests", "Great Expectations", "Soda", "OpenLineage", "Apache Airflow"],
    cta: "Explore Data Quality",
    category: "Data Management",
  },
  {
    slug: "data-governance",
    title: "Data Governance",
    summary: "Governance that engineers can implement and auditors can verify.",
    description:
      "Practical governance: a catalogue people actually use, classification and access policies enforced in the platform rather than in a document, and lineage that answers regulatory and impact questions directly from the systems of record.",
    capabilities: [
      "Cataloguing and metadata",
      "Classification and sensitivity",
      "Access policy design",
      "Lineage and impact analysis",
      "Retention and lifecycle",
      "Audit and compliance support",
    ],
    outcomes: [
      "Access decisions enforced by the platform",
      "Sensitive data identified and controlled",
      "Audit questions answered from evidence",
    ],
    technologies: ["Unity Catalog", "Snowflake Horizon", "Microsoft Purview", "OpenLineage"],
    cta: "Explore Data Governance",
    category: "Data Management",
  },
  {
    slug: "analytics-engineering",
    title: "Analytics Engineering",
    summary: "The modelled layer between raw data and confident decisions.",
    description:
      "A tested, documented, version-controlled transformation layer with agreed metric definitions — so analysts build on trusted foundations and the organization stops relitigating whose number is right.",
    capabilities: [
      "Modular SQL modelling",
      "Metric definitions",
      "Testing and CI",
      "Documentation and lineage",
      "BI model design",
      "Analyst enablement",
    ],
    outcomes: [
      "One definition per business metric",
      "Model changes reviewed like application code",
      "Analysts self-serving without breaking production",
    ],
    technologies: ["dbt", "SQL", "Snowflake", "BigQuery", "Power BI", "Looker"],
    cta: "Explore Analytics Engineering",
    category: "Data Management",
  },
  {
    slug: "ai-data-foundation",
    title: "AI Data Foundation",
    summary: "Get the data ready before the models arrive.",
    description:
      "The unglamorous work that decides whether AI initiatives succeed: reliable feature pipelines, reproducible training datasets, documented lineage and access controls, and evaluation data that reflects production reality.",
    capabilities: [
      "Feature pipelines",
      "Reproducible datasets",
      "Vector and embedding stores",
      "Lineage for model inputs",
      "Access control for sensitive data",
      "Evaluation data management",
    ],
    outcomes: [
      "Training data that can be reproduced and audited",
      "Consistent features between training and serving",
      "Governance applied before models reach production",
    ],
    technologies: ["Databricks", "Apache Spark", "Python", "Delta Lake", "MLflow"],
    cta: "Explore AI Data Foundations",
    category: "Platform",
  },
  {
    slug: "data-platform-optimization",
    title: "Data Platform Optimization",
    summary: "Faster queries and lower spend on the platform you already own.",
    description:
      "A focused engagement on an existing platform: profile the expensive and slow workloads, fix the modelling and layout problems behind them, and put cost visibility and guardrails in place so the improvement holds.",
    capabilities: [
      "Workload profiling",
      "Query and model tuning",
      "Storage layout optimization",
      "Warehouse sizing and scheduling",
      "Cost attribution",
      "FinOps guardrails",
    ],
    outcomes: [
      "Expensive workloads identified and remediated",
      "Spend attributable to teams and use cases",
      "Performance improvements that survive growth",
    ],
    technologies: ["Snowflake", "BigQuery", "Databricks", "Amazon Redshift", "dbt"],
    cta: "Explore Platform Optimization",
    category: "Enablement",
  },
  {
    slug: "managed-data-engineering",
    title: "Managed Data Engineering",
    summary: "Ongoing engineering capacity to run and evolve your platform.",
    description:
      "An ongoing engagement where DataForge operates and extends your data platform — monitoring, incident response, source onboarding and roadmap delivery — with documentation and handover designed in, so you retain the option to take it back in-house.",
    capabilities: [
      "Platform operations",
      "Monitoring and incident response",
      "Source onboarding",
      "Roadmap delivery",
      "Documentation and runbooks",
      "Knowledge transfer",
    ],
    outcomes: [
      "Engineering capacity without a hiring cycle",
      "Defined response expectations for data incidents",
      "A platform documented well enough to hand back",
    ],
    technologies: ["AWS", "Azure", "Google Cloud", "Snowflake", "dbt", "Apache Airflow"],
    cta: "Explore Managed Engineering",
    category: "Enablement",
  },
];

export const getSolution = (slug: string) => solutions.find((s) => s.slug === slug);

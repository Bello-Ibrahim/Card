import type { PhotoKey } from "./media";

export type Service = {
  slug: string;
  title: string;
  short: string;
  summary: string;
  /** Longer positioning paragraph used on the service detail page. */
  overview: string;
  capabilities: string[];
  outcomes: string[];
  technologies: string[];
  /** Photographic slot from src/content/media.ts. */
  photo: PhotoKey;
  /** Featured services get a full visual module on the home page, in this order. */
  featured?: number;
  icon:
    | "pipeline"
    | "architecture"
    | "cloud"
    | "warehouse"
    | "integration"
    | "migration"
    | "analytics"
    | "quality"
    | "strategy";
};

export const services: Service[] = [
  {
    slug: "data-engineering",
    photo: "serviceDataEngineering",
    featured: 1,
    title: "Data Engineering",
    short: "Batch and real-time pipelines built to run in production.",
    summary:
      "Design and build robust batch and real-time data pipelines that move data reliably across your organization.",
    overview:
      "Most data problems are not modelling problems — they are delivery problems. Pipelines fail silently, backfills are manual, schemas drift, and nobody can say whether last night's numbers are complete. We build ingestion and transformation systems that are versioned, tested, observable and recoverable, so the data your business depends on arrives on time and can be trusted when it does.",
    capabilities: [
      "Batch and incremental ingestion",
      "Streaming and change-data-capture pipelines",
      "Orchestration, scheduling and dependency management",
      "Idempotent, replayable transformation logic",
      "Automated testing and CI/CD for data",
      "Backfill, recovery and schema-evolution strategy",
    ],
    outcomes: [
      "Predictable data delivery with clear ownership",
      "Failures that surface early, with a documented path to recovery",
      "Pipelines your own engineers can extend without archaeology",
    ],
    technologies: ["Python", "SQL", "Apache Spark", "Apache Kafka", "Apache Airflow", "dbt"],
    icon: "pipeline",
  },
  {
    slug: "data-platform-architecture",
    photo: "serviceArchitecture",
    featured: 2,
    title: "Data Platform Architecture",
    short: "Architecture that survives contact with the roadmap.",
    summary:
      "Design scalable, secure and maintainable modern data architectures aligned with business goals.",
    overview:
      "Architecture decisions made in the first quarter set the cost curve for the next three years. We design target-state data platforms grounded in how your organization actually works — the domains that own data, the latency the business genuinely needs, the security posture you have to meet, and the engineering capacity you can realistically staff — then sequence the roadmap so value lands early rather than after a two-year build.",
    capabilities: [
      "Current-state assessment and architecture review",
      "Target-state platform and reference architecture",
      "Storage, compute and layering strategy",
      "Security, access control and tenancy design",
      "Build-versus-buy and cost modelling",
      "Phased implementation roadmap",
    ],
    outcomes: [
      "A target architecture leadership and engineering both agree on",
      "Technology choices tied to stated business constraints",
      "A roadmap sequenced for early, demonstrable value",
    ],
    technologies: ["AWS", "Microsoft Azure", "Google Cloud", "Snowflake", "Databricks"],
    icon: "architecture",
  },
  {
    slug: "cloud-data-engineering",
    photo: "serviceCloud",
    featured: 3,
    title: "Cloud Data Engineering",
    short: "Cloud-native platforms across AWS, Azure and Google Cloud.",
    summary:
      "Build and modernize cloud-native data platforms across AWS, Microsoft Azure and Google Cloud.",
    overview:
      "Moving to the cloud is straightforward. Running a cloud data platform that stays fast, secure and affordable is the engineering work. We build cloud-native platforms with infrastructure as code, environment parity, least-privilege access and cost controls in place from the first deployment — not retrofitted after the first surprise invoice.",
    capabilities: [
      "Cloud data platform build and modernization",
      "Infrastructure as code and environment management",
      "Identity, networking and least-privilege access",
      "Cost visibility, workload tuning and FinOps guardrails",
      "Disaster recovery and resilience design",
      "Platform operations and runbooks",
    ],
    outcomes: [
      "Reproducible environments instead of hand-built infrastructure",
      "Predictable platform spend with visible drivers",
      "Security and compliance requirements met by design",
    ],
    technologies: ["AWS", "Microsoft Azure", "Google Cloud", "Terraform", "Kubernetes"],
    icon: "cloud",
  },
  {
    slug: "data-warehousing-and-lakehouses",
    photo: "serviceArchitecture",
    title: "Data Warehousing & Lakehouses",
    short: "Warehouses, lakes and lakehouses for analytics and AI.",
    summary:
      "Design modern warehouses, data lakes and lakehouse architectures for analytics and AI workloads.",
    overview:
      "The warehouse-versus-lake debate matters far less than the modelling and governance discipline applied on top of it. We design storage and modelling layers that match your workloads — dimensional models where analysts need clarity, open table formats where scale and AI workloads need flexibility — with partitioning, file layout and cost behaviour treated as first-class design concerns.",
    capabilities: [
      "Dimensional and domain-oriented data modelling",
      "Lakehouse and open table format design",
      "Partitioning, clustering and file layout strategy",
      "Workload isolation and performance tuning",
      "Semantic layer and metric definitions",
      "Storage lifecycle and cost management",
    ],
    outcomes: [
      "Analysts querying models they understand and trust",
      "Query performance that holds as volume grows",
      "One storage foundation serving BI, data science and AI",
    ],
    technologies: ["Snowflake", "Databricks", "BigQuery", "Amazon Redshift", "Microsoft Fabric"],
    icon: "warehouse",
  },
  {
    slug: "data-integration",
    photo: "serviceIntegration",
    featured: 4,
    title: "Data Integration",
    short: "Fragmented systems joined into one coherent estate.",
    summary:
      "Connect fragmented systems, APIs, applications, databases and third-party platforms into a unified data ecosystem.",
    overview:
      "Every organization accumulates systems that were never designed to talk to each other. We build the integration layer that connects them — with contracts, retries, rate-limit handling and reconciliation built in — so that finance, operations and product are working from the same version of events rather than three exports that never quite agree.",
    capabilities: [
      "API, SaaS and database source integration",
      "Event streaming and change-data-capture",
      "Entity resolution and reference data alignment",
      "Data contracts and schema governance",
      "Reconciliation and completeness checks",
      "Secure file and partner data exchange",
    ],
    outcomes: [
      "A single, reconciled view across previously siloed systems",
      "Integrations that degrade gracefully instead of failing silently",
      "Source onboarding measured in days rather than quarters",
    ],
    technologies: ["Python", "REST & GraphQL APIs", "Apache Kafka", "Debezium", "Airbyte"],
    icon: "integration",
  },
  {
    slug: "data-modernization",
    photo: "serviceModernization",
    featured: 5,
    title: "Data Modernization",
    short: "Legacy platforms retired without breaking the business.",
    summary:
      "Modernize legacy data infrastructure and migrate workloads to scalable cloud and modern data platforms.",
    overview:
      "Migrations fail on the parts nobody scoped: undocumented stored procedures, reports with hard-coded logic, and the downstream consumers discovered only after cutover. We inventory what exists, prove equivalence between old and new, and migrate in slices that can each be validated and rolled back — so the legacy platform is retired on evidence, not optimism.",
    capabilities: [
      "Workload inventory and dependency mapping",
      "Migration strategy, sequencing and cutover planning",
      "Automated code and pipeline conversion",
      "Parallel-run and reconciliation testing",
      "Consumer migration and downstream remediation",
      "Legacy decommissioning",
    ],
    outcomes: [
      "Cutovers validated against the legacy system before switching",
      "A documented estate where an undocumented one used to be",
      "Legacy licensing and maintenance genuinely retired",
    ],
    technologies: ["SQL Server", "Oracle", "PostgreSQL", "Snowflake", "BigQuery", "Databricks"],
    icon: "migration",
  },
  {
    slug: "analytics-engineering",
    photo: "serviceDataEngineering",
    title: "Analytics Engineering",
    short: "Trusted, documented, analysis-ready datasets.",
    summary:
      "Transform raw data into trusted, documented, analysis-ready datasets for BI and decision-making.",
    overview:
      "Between raw tables and a dashboard sits the layer that decides whether an organization argues about numbers or acts on them. We build tested, version-controlled transformation layers with agreed metric definitions, documentation generated from the code itself, and lineage that answers \"where did this number come from\" in seconds rather than days.",
    capabilities: [
      "Modular transformation layers in dbt or SQL",
      "Metric and semantic layer definitions",
      "Data tests, assertions and CI on every change",
      "Documentation and column-level lineage",
      "Self-service enablement for analysts",
      "BI model design and rationalization",
    ],
    outcomes: [
      "One agreed definition per business metric",
      "Analysts shipping models safely behind code review",
      "Dashboards traceable to source in a single click",
    ],
    technologies: ["dbt", "SQL", "Snowflake", "BigQuery", "Power BI", "Looker"],
    icon: "analytics",
  },
  {
    slug: "data-quality-and-observability",
    photo: "serviceIntegration",
    title: "Data Quality & Observability",
    short: "Reliability you can measure, not hope for.",
    summary:
      "Improve data reliability through validation, monitoring, lineage, testing, observability and governance.",
    overview:
      "Trust in data is lost the first time a number changes after a decision was made on it. We instrument pipelines and datasets with freshness, volume, schema and business-rule checks, route alerts to the teams that own the data, and define severity and response so incidents are handled like production incidents — because that is what they are.",
    capabilities: [
      "Data quality frameworks and rule design",
      "Freshness, volume, schema and distribution monitoring",
      "End-to-end lineage and impact analysis",
      "Incident response, severity and on-call design",
      "Data contracts between producers and consumers",
      "Quality reporting and SLA definition",
    ],
    outcomes: [
      "Issues detected by monitoring rather than by executives",
      "Clear ownership for every critical dataset",
      "Measurable reliability targets for the data that matters most",
    ],
    technologies: ["dbt tests", "Great Expectations", "Apache Airflow", "OpenLineage", "Monte Carlo"],
    icon: "quality",
  },
  {
    slug: "data-strategy-and-advisory",
    photo: "serviceArchitecture",
    title: "Data Strategy & Advisory",
    short: "Roadmaps, operating models and investment priorities.",
    summary:
      "Help leadership teams define their data strategy, architecture roadmap, operating model and investment priorities.",
    overview:
      "Data strategy fails when it stops at a slide deck. We work with leadership to connect data investment to specific business outcomes, define the operating model and ownership that will actually be staffed, and produce a sequenced roadmap with costs, dependencies and decision points — a document engineering teams can execute against, not a vision statement.",
    capabilities: [
      "Data maturity and capability assessment",
      "Architecture and platform review",
      "Operating model and ownership design",
      "Roadmap, sequencing and investment planning",
      "Governance and policy frameworks",
      "Fractional technical leadership",
    ],
    outcomes: [
      "Investment tied to named business outcomes",
      "A clear owner for every capability on the roadmap",
      "Decisions documented with their trade-offs and constraints",
    ],
    technologies: ["Architecture review", "Capability assessment", "Roadmapping", "Governance design"],
    icon: "strategy",
  },
];

export const featuredServices = services
  .filter((s): s is Service & { featured: number } => typeof s.featured === "number")
  .sort((a, b) => a.featured - b.featured);

export const getService = (slug: string) => services.find((s) => s.slug === slug);

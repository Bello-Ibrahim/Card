/**
 * Insights (editorial hub).
 *
 * Articles are original technical writing. They contain no client references and no
 * unverified claims about DataForge. Publication dates are editorial metadata for the
 * article, set when the piece is published.
 */

export const insightCategories = [
  "Data Engineering",
  "Data Architecture",
  "Cloud",
  "AI",
  "Analytics",
  "Data Strategy",
  "Engineering Leadership",
  "Careers",
  "Training",
] as const;

export type InsightCategory = (typeof insightCategories)[number];

export type InsightSection = { heading: string; paragraphs: string[]; bullets?: string[] };

export type Insight = {
  slug: string;
  title: string;
  excerpt: string;
  category: InsightCategory;
  readingTime: number;
  publishedAt: string;
  featured?: boolean;
  sections: InsightSection[];
};

export const insights: Insight[] = [
  {
    slug: "why-data-quality-is-an-engineering-problem",
    title: "Why Data Quality Is an Engineering Problem",
    excerpt:
      "Quality is not a governance committee or a dashboard. It is tests, ownership and response design — the same practices that keep any production system honest.",
    category: "Data Engineering",
    readingTime: 7,
    publishedAt: "2026-07-22",
    featured: true,
    sections: [
      {
        heading: "The framing that fails",
        paragraphs: [
          "Most quality programmes begin as governance exercises: a policy document, a steering group, a catalogue nobody opens. They fail because none of that changes what happens at 02:00 when a source system sends yesterday's file twice.",
          "Quality is decided in the pipeline. Whether a duplicate load is caught, whether a renamed category silently collapses a segment, whether anyone is paged — those are engineering decisions, made in code, long before they reach a committee.",
        ],
      },
      {
        heading: "Tests belong next to the transformation",
        paragraphs: [
          "The most effective quality controls live in the same repository as the logic they protect, run on every change, and block a merge when they fail. That is unremarkable in application engineering and still unusual in data.",
          "Write assertions for what the business actually believes: that order totals reconcile to the ledger, that every customer has exactly one active record, that no region silently disappears. These catch the failures that damage trust.",
        ],
        bullets: [
          "Technical checks: freshness, volume, schema, nullability",
          "Semantic checks: referential integrity, distributions, business rules",
          "Reconciliation: agreement with an authoritative source",
        ],
      },
      {
        heading: "An alert without an owner is not a control",
        paragraphs: [
          "Every check needs a named owner, a severity and an expected response. Without those, failures accumulate as background noise until the monitoring itself loses credibility and people start muting channels.",
          "This is why quality work is inseparable from ownership work. The tooling is straightforward; deciding who is accountable for a dataset is the hard part, and it is not a technical decision.",
        ],
      },
      {
        heading: "Treat data incidents like production incidents",
        paragraphs: [
          "Detection through monitoring rather than through a stakeholder. An assigned responder. A severity level. A written follow-up when it matters. None of this is novel — it is simply applying to data the practices that software teams settled on years ago.",
          "The follow-up is where compounding improvement happens. A team that asks why a failure was not detected earlier will, over time, stop being surprised.",
        ],
      },
    ],
  },
  {
    slug: "building-real-time-data-pipelines",
    title: "Building Real-Time Data Pipelines",
    excerpt:
      "Streaming is not faster batch. It is a different failure model — and the question worth answering first is whether latency genuinely changes the decision.",
    category: "Data Engineering",
    readingTime: 8,
    publishedAt: "2026-07-08",
    sections: [
      {
        heading: "Start with the decision, not the technology",
        paragraphs: [
          "Streaming infrastructure costs more to build and considerably more to operate. It earns that cost only where latency changes an outcome: a fraud signal that must arrive before settlement, inventory that must not oversell, a network fault that must page someone now.",
          "For most reporting, an hourly batch is indistinguishable from real time to the person reading it. Asking each consumer what freshness they genuinely require routinely removes half the proposed streaming scope.",
        ],
      },
      {
        heading: "Delivery semantics are a design decision",
        paragraphs: [
          "At-least-once delivery means duplicates will happen; your consumers must be idempotent. Exactly-once is achievable within some systems but rarely end to end across every hop. Decide explicitly which guarantee each pipeline needs, and write it down.",
          "The practical approach is usually at-least-once transport with idempotent writes keyed on a stable business identifier — simpler to reason about, and it degrades predictably.",
        ],
        bullets: [
          "Idempotent writes keyed on a stable identifier",
          "Explicit handling for late and out-of-order events",
          "Replay from a retained log rather than re-extraction from source",
        ],
      },
      {
        heading: "Late data is normal, not exceptional",
        paragraphs: [
          "Events arrive out of order, devices buffer while offline, and partners resend. A pipeline that assumes ordered arrival will quietly produce wrong aggregates rather than failing loudly.",
          "Use event time rather than processing time, define a watermark that reflects how late data realistically arrives, and decide what happens to anything later than that. The answer can be to discard it — but it should be a decision, not an accident.",
        ],
      },
      {
        heading: "Reconcile streaming against batch",
        paragraphs: [
          "The fastest way to lose confidence in a streaming platform is for its numbers to disagree with the warehouse. Run a periodic batch reconciliation over the same source and alert on divergence beyond a defined tolerance.",
          "This also catches the subtle failures — a consumer lagging, a partition stalled, a schema change silently dropping a field — that latency dashboards alone will not show you.",
        ],
      },
      {
        heading: "Operate it like a service",
        paragraphs: [
          "Consumer lag, partition skew, throughput and error rates need dashboards and alerts with owners, exactly as an application would. Streaming systems fail in ways batch systems do not: they fail slowly and continuously rather than loudly and once.",
          "If the team cannot answer \"is it keeping up right now\" in under a minute, the platform is not yet in production regardless of what the deployment pipeline says.",
        ],
      },
    ],
  },
  {
    slug: "how-to-build-a-modern-data-platform",
    title: "How to Build a Modern Data Platform",
    excerpt:
      "A modern data platform is less a product selection than a sequence of decisions about ownership, layering and delivery discipline. Here is the order those decisions are best made in.",
    category: "Data Architecture",
    readingTime: 9,
    publishedAt: "2026-06-18",
    featured: true,
    sections: [
      {
        heading: "Start with the decisions the platform has to support",
        paragraphs: [
          "Platform programmes that begin with a tool comparison tend to end with an expensive system nobody uses. The more productive starting point is a short list of decisions the business wants to make better — how quickly stock is replenished, which customers are at risk, whether a regulatory submission reconciles — and the data those decisions genuinely require.",
          "That list does two things. It sets a latency requirement per use case, which is the single largest driver of architectural cost. And it identifies the source systems that matter first, which lets you sequence ingestion work instead of attempting to onboard everything at once.",
        ],
      },
      {
        heading: "Layer the platform, and mean it",
        paragraphs: [
          "Nearly every durable platform separates raw landed data, cleaned and conformed data, and modelled data serving consumption. The names differ — bronze/silver/gold, staging/core/marts — but the discipline is the same: each layer has one job, and transformations do not skip layers.",
          "The value of the separation shows up during incidents. When a number is wrong, layering tells you whether the problem is ingestion, conformance or modelling, and lets you reprocess one stage without replaying everything upstream.",
        ],
        bullets: [
          "Raw: immutable, source-shaped, retained for replay",
          "Conformed: typed, deduplicated, business keys resolved",
          "Modelled: dimensional or domain models with agreed metric definitions",
        ],
      },
      {
        heading: "Treat the platform as software",
        paragraphs: [
          "The gap between platforms that scale and platforms that stall is rarely the storage engine. It is whether the platform is built with the practices software teams take for granted: version control, code review, automated tests, reproducible environments, and deployment through a pipeline rather than through a console.",
          "This is what makes a platform safe to change. A team that can modify a transformation, see tests run against it, and deploy it with a rollback path will keep improving the platform. A team that cannot will freeze it and route around it with extracts.",
        ],
      },
      {
        heading: "Instrument before you scale",
        paragraphs: [
          "Observability is cheapest to add while the platform is small. Freshness, volume, schema and business-rule checks on the first critical datasets establish the pattern that later datasets inherit — and they surface the design problems that would otherwise be discovered by a stakeholder reading a wrong number.",
          "Define severity levels and response expectations early. A data incident with no owner and no severity is an argument waiting to happen.",
        ],
      },
      {
        heading: "Sequence for early value",
        paragraphs: [
          "A platform roadmap that delivers nothing for nine months will lose its sponsor. Sequence the work so that one meaningful use case reaches production early — end to end, including quality checks and documentation — even if that means deferring sources that seem obviously important.",
          "The first delivered use case is also the reference implementation. It is worth building it carefully, because every subsequent pipeline will be modelled on it.",
        ],
      },
    ],
  },
  {
    slug: "etl-vs-elt-choosing-the-right-architecture",
    title: "ETL vs ELT: Choosing the Right Architecture",
    excerpt:
      "ELT has become the default, but the default is not always right. The decision turns on where compute is cheapest, what must never land in storage, and who maintains the transformation logic.",
    category: "Data Engineering",
    readingTime: 7,
    publishedAt: "2026-05-27",
    featured: true,
    sections: [
      {
        heading: "What actually changed",
        paragraphs: [
          "ETL transforms data before loading it into the target system. ELT loads first and transforms inside the target. The shift toward ELT was driven by a specific economic change: cloud warehouses made storage cheap and made scalable SQL compute available on demand, so there was less reason to transform data on a separate tier before loading it.",
          "That change is real, but it is a change in cost structure — not a universal architectural truth.",
        ],
      },
      {
        heading: "When ELT is the right default",
        paragraphs: [
          "ELT suits organizations whose transformation logic is expressible in SQL, whose analysts are closer to the business than the platform team, and whose target is a warehouse or lakehouse with elastic compute.",
          "Its strongest practical advantage is auditability: because raw data is retained, you can reprocess history when a definition changes, rather than asking source systems to resend it.",
        ],
        bullets: [
          "Raw data retained and replayable",
          "Transformation logic in version control, reviewed like code",
          "Analysts able to contribute models safely",
        ],
      },
      {
        heading: "When ETL still wins",
        paragraphs: [
          "Transform before load when data must not land in the target in its raw form — personal data requiring masking or tokenisation before storage, or records subject to residency constraints. Transform before load, too, when the source volume is far larger than the useful signal, and filtering early avoids paying to store and scan the remainder.",
          "Streaming pipelines also tend toward transformation in flight, because the processing happens as events move rather than after they land.",
        ],
      },
      {
        heading: "The question behind the question",
        paragraphs: [
          "In practice most mature estates run both, and the interesting decision is not the acronym but ownership: who is accountable for the correctness of each transformation, and can they change it safely?",
          "A pipeline where transformation logic lives in version control, is tested automatically and has a named owner will outperform one that does not — regardless of whether the T happens before or after the L.",
        ],
      },
    ],
  },
  {
    slug: "what-a-high-performing-data-engineering-team-looks-like",
    title: "What a High-Performing Data Engineering Team Looks Like",
    excerpt:
      "Strong data teams are not distinguished by their tooling. They are distinguished by ownership, review discipline and how they behave when something breaks.",
    category: "Engineering Leadership",
    readingTime: 8,
    publishedAt: "2026-05-06",
    sections: [
      {
        heading: "Ownership is explicit",
        paragraphs: [
          "In a high-performing team, every critical dataset has a named owner, and that ownership is documented somewhere people actually look. Ownership means accountability for correctness and freshness, not just familiarity with the code.",
          "The test is simple: when a number looks wrong, does the organization know who to ask within a minute? If the answer is a group chat, ownership is not real yet.",
        ],
      },
      {
        heading: "Changes go through review",
        paragraphs: [
          "Data logic is business logic. Teams that review transformation changes the way they review application code catch definition drift, silent breaking changes and untested edge cases before they reach a dashboard.",
          "This requires the surrounding machinery — a repository, environments, tests that run automatically — which is why review discipline is usually a proxy for overall platform maturity.",
        ],
      },
      {
        heading: "Incidents are handled like production incidents",
        paragraphs: [
          "Strong teams treat a broken pipeline the way an engineering team treats a broken service: detection through monitoring, an assigned responder, a severity level, and a written follow-up when it matters.",
          "The follow-up is where compounding improvement happens. A team that asks why a failure was not detected earlier will, over time, stop being surprised.",
        ],
        bullets: [
          "Detection through monitoring, not through stakeholders",
          "Defined severity levels and response expectations",
          "Follow-up actions tracked to completion",
        ],
      },
      {
        heading: "The platform is documented well enough to leave",
        paragraphs: [
          "The healthiest signal in a data team is that any single person could go on leave without work stopping. That requires runbooks, architecture notes and onboarding material that is maintained rather than written once.",
          "It is also the clearest measure of whether external support has genuinely transferred capability, or merely delivered software.",
        ],
      },
    ],
  },
  {
    slug: "data-lake-vs-data-warehouse-vs-lakehouse",
    title: "Data Lake vs Data Warehouse vs Lakehouse",
    excerpt:
      "Three storage patterns, three sets of trade-offs. What separates them is not scale but how much structure is enforced, and at what point in the pipeline.",
    category: "Data Architecture",
    readingTime: 8,
    publishedAt: "2026-04-15",
    featured: true,
    sections: [
      {
        heading: "Data warehouse",
        paragraphs: [
          "A warehouse enforces structure on write. Data is modelled before it lands in the consumption layer, which gives analysts strong guarantees: consistent types, enforced relationships, predictable performance and mature access control.",
          "The cost is flexibility. Unstructured and semi-structured data fits awkwardly, and modelling work sits on the critical path for every new source.",
        ],
      },
      {
        heading: "Data lake",
        paragraphs: [
          "A lake enforces structure on read. Files land cheaply in object storage in whatever shape they arrive, and meaning is applied when the data is queried. This suits data science, machine learning and sources whose schema is unstable.",
          "Without governance, the flexibility becomes the problem. Lakes that lack catalogues, ownership and quality controls become the swamps their critics describe — expensive to store and impossible to trust.",
        ],
      },
      {
        heading: "Lakehouse",
        paragraphs: [
          "A lakehouse keeps data in open formats on object storage while adding the transactional guarantees warehouses provide: ACID writes, schema enforcement and evolution, time travel and fine-grained access control.",
          "The practical appeal is avoiding a duplicated estate. Rather than copying data from a lake into a warehouse and slowly letting the two diverge, both SQL analytics and ML workloads read the same tables.",
        ],
        bullets: [
          "Warehouse: structure on write, strongest for governed BI",
          "Lake: structure on read, strongest for exploration and ML",
          "Lakehouse: open storage with transactional guarantees over both",
        ],
      },
      {
        heading: "How to choose",
        paragraphs: [
          "If your workloads are overwhelmingly SQL analytics against structured sources, and governance requirements are strict, a warehouse remains the most direct path. If you have significant unstructured data and ML workloads, a lakehouse usually avoids maintaining two systems.",
          "Choosing badly is recoverable. Choosing without modelling discipline, ownership and quality controls is not — that is what actually determines whether the platform is trusted.",
        ],
      },
    ],
  },
  {
    slug: "how-organizations-should-prepare-their-data-for-ai",
    title: "How Organizations Should Prepare Their Data for AI",
    excerpt:
      "Most AI initiatives are blocked by data foundations rather than by models. Reproducibility, lineage and access control are the prerequisites worth funding first.",
    category: "AI",
    readingTime: 9,
    publishedAt: "2026-03-24",
    sections: [
      {
        heading: "Reproducibility comes first",
        paragraphs: [
          "If you cannot recreate the exact dataset a model was trained on, you cannot explain its behaviour, diagnose a regression or satisfy a reviewer. Reproducibility requires versioned, immutable snapshots of training inputs and a record of the transformation code that produced them.",
          "This is ordinary data engineering, applied with more rigour. Teams that already retain raw data and version their transformations are most of the way there.",
        ],
      },
      {
        heading: "Lineage is a governance requirement, not a nicety",
        paragraphs: [
          "Once models influence decisions that affect customers, someone will ask which data contributed to an output. Column-level lineage from source to model input answers that question from evidence rather than from memory.",
          "Lineage also makes impact analysis tractable: when an upstream source changes, you can enumerate the models affected instead of discovering them through degraded performance.",
        ],
      },
      {
        heading: "Access control belongs upstream of the model",
        paragraphs: [
          "Models and retrieval systems inherit the permissions of the data they are given. If sensitive fields reach a training set or a retrieval index without classification and control, the model becomes a new path around your access policy.",
          "Classify sensitive data at ingestion, apply masking or exclusion in the pipeline, and record what each dataset is approved for. Retrofitting this after a system is live is considerably harder.",
        ],
        bullets: [
          "Classify sensitivity at ingestion, not at consumption",
          "Enforce masking and exclusion in the pipeline",
          "Record approved use for each dataset",
        ],
      },
      {
        heading: "Consistency between training and serving",
        paragraphs: [
          "A recurring cause of models underperforming in production is a mismatch between how a feature was computed during training and how it is computed at inference. Shared, tested feature pipelines used by both paths remove an entire class of failure.",
          "The engineering pattern is familiar: define the logic once, test it, and let both consumers call the same implementation.",
        ],
      },
      {
        heading: "Evaluation data deserves the same care",
        paragraphs: [
          "Evaluation sets are frequently assembled informally and then trusted for months. Version them, document how they were sampled, and keep them representative of current production conditions.",
          "Otherwise, evaluation slowly stops measuring the thing you care about — and does so invisibly.",
        ],
      },
    ],
  },
  {
    slug: "why-data-quality-fails-and-what-to-do-about-it",
    title: "Why Data Quality Initiatives Fail — and What to Do Instead",
    excerpt:
      "Quality programmes usually fail for organisational reasons rather than technical ones. Scope, ownership and response design matter more than the tool selected.",
    category: "Data Engineering",
    readingTime: 7,
    publishedAt: "2026-02-19",
    sections: [
      {
        heading: "Failure one: scope everything at once",
        paragraphs: [
          "Programmes that attempt to define quality rules across every dataset produce thousands of low-value checks, alert fatigue, and a monitoring system people mute. Start with the datasets that carry consequential decisions, and instrument those thoroughly.",
          "A small number of well-designed, well-owned checks on critical data outperforms broad, shallow coverage every time.",
        ],
      },
      {
        heading: "Failure two: alerts without owners",
        paragraphs: [
          "An alert routed to a shared inbox is not a control. Each check needs a named owner, a severity level and an expected response — otherwise failures accumulate as background noise until the monitoring itself loses credibility.",
          "This is why quality work is inseparable from ownership work. The tooling is straightforward; the accountability is the hard part.",
        ],
      },
      {
        heading: "Failure three: measuring the pipeline, not the meaning",
        paragraphs: [
          "Technical checks — did the job run, did rows arrive, did the schema hold — are necessary but insufficient. The failures that damage trust are usually semantic: a currency field silently changing units, a category renamed upstream, a filter that quietly excludes a region.",
          "Business-rule assertions written with the people who use the data catch these. They also make the data team's understanding of the domain explicit and reviewable.",
        ],
        bullets: [
          "Technical checks: freshness, volume, schema, nullability",
          "Semantic checks: referential integrity, distributions, business rules",
          "Reconciliation: agreement with an authoritative source",
        ],
      },
      {
        heading: "What to do instead",
        paragraphs: [
          "Pick the datasets that matter most. Agree with their consumers what correct means. Implement technical and semantic checks together, assign ownership and severity, and review incidents periodically to remove noisy checks and add missing ones.",
          "Quality is a maintained practice, not a project with an end date.",
        ],
      },
    ],
  },
  {
    slug: "a-practical-path-into-data-engineering",
    title: "A Practical Path Into Data Engineering",
    excerpt:
      "For analysts, software engineers and DBAs moving into data engineering: the skills that compound, in the order worth learning them.",
    category: "Careers",
    readingTime: 8,
    publishedAt: "2026-01-28",
    sections: [
      {
        heading: "SQL, deeper than you think you need",
        paragraphs: [
          "SQL remains the centre of the discipline, and the depth required is greater than most self-assessments suggest. Window functions, set operations, careful null handling and the ability to read a query plan separate people who can write queries from people who can make them fast and correct.",
          "It is also the most transferable skill on the list. Engines change; SQL competence does not depreciate.",
        ],
      },
      {
        heading: "Enough Python to build systems",
        paragraphs: [
          "Data engineering Python is closer to software engineering than to notebook analysis: modules and packaging, tests, error handling, typing and dependency management. The goal is code that another engineer can safely modify a year later.",
          "If you come from an analytics background, this is usually the largest step — and the one that most improves your work.",
        ],
      },
      {
        heading: "Data modelling",
        paragraphs: [
          "Modelling is the skill that ages best and is learned least systematically. Understanding normalisation, dimensional design, slowly changing dimensions and how to choose grain will shape more of your platform's quality than any tool choice.",
          "It is also what makes the difference between datasets analysts trust and datasets they work around.",
        ],
      },
      {
        heading: "Engineering practice",
        paragraphs: [
          "Version control, code review, testing, CI/CD and observability are what turn scripts into a platform. Learning them early makes everything afterwards safer and faster.",
          "One cloud platform and one orchestrator, learned properly, is worth more than surface familiarity with six. Depth transfers; breadth without depth does not.",
        ],
        bullets: [
          "Deep SQL, including performance and query plans",
          "Production-grade Python",
          "Data modelling fundamentals",
          "One cloud, one orchestrator, one transformation framework — properly",
        ],
      },
      {
        heading: "Build something that runs on a schedule",
        paragraphs: [
          "The most useful learning project is a modest pipeline that runs unattended, handles failure, and has tests and monitoring. It teaches the parts of the job tutorials skip: partial failure, late data, schema change and recovery.",
          "It is also the project that interviews are most productive to talk about.",
        ],
      },
    ],
  },
  {
    slug: "controlling-cloud-data-platform-costs",
    title: "Controlling Cloud Data Platform Costs Without Slowing Delivery",
    excerpt:
      "Cloud data spend is usually concentrated in a handful of workloads. Attribution, layout and scheduling recover most of the waste without touching the roadmap.",
    category: "Cloud",
    readingTime: 7,
    publishedAt: "2025-12-10",
    sections: [
      {
        heading: "Attribute spend before optimising it",
        paragraphs: [
          "Cost conversations stall when nobody can say which team, pipeline or dashboard is responsible for a line item. Tagging workloads and enabling per-warehouse or per-query attribution turns an argument into an engineering task.",
          "In most estates a small number of workloads account for a disproportionate share of spend, which means targeted work has a large effect.",
        ],
      },
      {
        heading: "Fix layout and modelling before buying less compute",
        paragraphs: [
          "Expensive queries are often expensive because of how data is laid out: poor partitioning, small-file proliferation, missing clustering, or models that force full scans for common filters.",
          "Fixing layout improves both cost and latency, which is a rare combination. Reducing compute capacity alone usually trades one problem for another.",
        ],
        bullets: [
          "Partition and cluster on the columns queries actually filter on",
          "Compact small files produced by streaming ingestion",
          "Materialise expensive repeated aggregations",
        ],
      },
      {
        heading: "Schedule according to real requirements",
        paragraphs: [
          "A significant share of platform cost comes from pipelines running more often than any consumer needs. Asking each consumer what freshness they actually require — and documenting the answer — routinely removes runs nobody was waiting for.",
          "The same applies to development environments left running outside working hours.",
        ],
      },
      {
        heading: "Make cost visible continuously",
        paragraphs: [
          "One-off optimisation efforts decay. Cost dashboards owned by the platform team, alerts on unusual spend, and a periodic review keep the improvement in place as the platform grows.",
          "Guardrails work better than gates: engineers respond well to visibility, and poorly to approval queues.",
        ],
      },
    ],
  },
];

export const getInsight = (slug: string) => insights.find((i) => i.slug === slug);
export const featuredInsights = insights.filter((i) => i.featured);

export type TrainingTrack = {
  slug: string;
  title: string;
  level: "Foundation" | "Intermediate" | "Advanced" | "Custom";
  summary: string;
  modules: string[];
  audience: string;
  format: string;
};

export const trainingTracks: TrainingTrack[] = [
  {
    slug: "data-engineering-fundamentals",
    title: "Data Engineering Fundamentals",
    level: "Foundation",
    summary:
      "The core craft: querying, programming, modelling and moving data reliably between systems.",
    modules: [
      "SQL for data engineering",
      "Python for data workflows",
      "Data modelling foundations",
      "ETL and ELT patterns",
      "Working with APIs",
      "Relational and NoSQL databases",
    ],
    audience: "Analysts, software engineers and graduates moving into data engineering roles.",
    format: "Instructor-led sessions with hands-on labs and a build project.",
  },
  {
    slug: "modern-data-stack",
    title: "Modern Data Stack",
    level: "Intermediate",
    summary:
      "How today's warehouse-centric toolchain fits together, and how to run it responsibly.",
    modules: [
      "dbt: modelling, testing and documentation",
      "Apache Airflow orchestration",
      "Cloud data warehouses in practice",
      "Lakehouse fundamentals",
      "Version control and CI/CD for data",
      "Environment and release management",
    ],
    audience: "Data and analytics engineers adopting or standardising a modern stack.",
    format: "Workshop series with a shared project repository and code review.",
  },
  {
    slug: "advanced-data-engineering",
    title: "Advanced Data Engineering",
    level: "Advanced",
    summary:
      "Distributed processing, streaming and the architectural judgement that comes after the basics.",
    modules: [
      "Apache Spark at scale",
      "Streaming architectures and semantics",
      "Distributed systems fundamentals",
      "Data architecture patterns and trade-offs",
      "Data quality engineering",
      "Observability and incident response",
    ],
    audience: "Experienced engineers responsible for large or latency-sensitive platforms.",
    format: "Deep-dive sessions built around realistic failure scenarios.",
  },
  {
    slug: "cloud-data-engineering",
    title: "Cloud Data Engineering",
    level: "Intermediate",
    summary:
      "Building and operating data platforms natively on your chosen cloud.",
    modules: [
      "AWS data services",
      "Microsoft Azure data services",
      "Google Cloud data services",
      "Infrastructure as code",
      "Identity, access and network security",
      "Cost management and workload tuning",
    ],
    audience: "Engineers and platform teams building on AWS, Azure or Google Cloud.",
    format: "Cloud-specific tracks delivered against your own reference architecture.",
  },
  {
    slug: "corporate-training",
    title: "Corporate Training",
    level: "Custom",
    summary:
      "Customized programs designed around your technology stack, business objectives and employee skill levels.",
    modules: [
      "Skills assessment and gap analysis",
      "Curriculum designed to your stack",
      "Training on your own datasets and patterns",
      "Team-based capstone projects",
      "Mentoring and follow-up clinics",
      "Progress reporting for sponsors",
    ],
    audience: "Organizations upskilling teams against a specific platform or roadmap.",
    format: "On-site or remote cohorts, scheduled around delivery commitments.",
  },
];

export const trainingPrinciples = [
  {
    title: "Taught by practitioners",
    body: "Sessions are delivered by engineers who build these systems, using examples drawn from real delivery rather than tutorial datasets.",
  },
  {
    title: "Built on your stack",
    body: "Where possible, training runs against the technologies, conventions and data your teams work with every day.",
  },
  {
    title: "Assessed and evidenced",
    body: "Programs include practical exercises and a capstone, so sponsors can see capability rather than attendance.",
  },
  {
    title: "Followed by support",
    body: "Cohorts can be followed by mentoring and code review clinics, which is where new skills usually take hold.",
  },
];

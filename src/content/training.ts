export type TrainingTrack = {
  slug: string;
  title: string;
  level: "Beginner" | "Intermediate" | "Advanced" | "Enterprise";
  summary: string;
  modules: string[];
  audience: string;
  format: string;
};

export const trainingTracks: TrainingTrack[] = [
  {
    slug: "beginner",
    title: "Foundations",
    level: "Beginner",
    summary: "The core craft: querying, programming, modelling and moving data between systems.",
    modules: ["SQL", "Python", "Databases", "ETL fundamentals", "Data modelling basics", "Working with APIs"],
    audience: "Analysts, software engineers and graduates moving into data engineering.",
    format: "Instructor-led sessions with hands-on labs and a build project.",
  },
  {
    slug: "intermediate",
    title: "Modern Data Stack",
    level: "Intermediate",
    summary: "How today's warehouse-centric toolchain fits together, and how to run it responsibly.",
    modules: ["PySpark", "Apache Airflow", "Data modelling", "Cloud data services", "dbt", "CI/CD for data"],
    audience: "Data and analytics engineers adopting or standardising a modern stack.",
    format: "Workshop series against a shared project repository, with code review.",
  },
  {
    slug: "advanced",
    title: "Advanced Engineering",
    level: "Advanced",
    summary: "Distributed processing, streaming and the architectural judgement that comes after the basics.",
    modules: [
      "Distributed systems",
      "Apache Kafka",
      "Streaming architectures",
      "Data architecture patterns",
      "Data quality engineering",
      "Observability and incident response",
    ],
    audience: "Experienced engineers responsible for large or latency-sensitive platforms.",
    format: "Deep dives built around realistic failure scenarios.",
  },
  {
    slug: "enterprise",
    title: "Corporate Programs",
    level: "Enterprise",
    summary: "Customized programs designed around your stack, objectives and current skill levels.",
    modules: [
      "Skills assessment and gap analysis",
      "Curriculum designed to your stack",
      "Training on your own data and patterns",
      "Team capstone projects",
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
    body: "Sessions are delivered by engineers who build these systems, using examples from real delivery rather than tutorial datasets.",
  },
  {
    title: "Built on your stack",
    body: "Where possible, training runs against the technologies, conventions and data your teams work with every day.",
  },
  {
    title: "Assessed and evidenced",
    body: "Programs include practical exercises and a capstone, so sponsors see capability rather than attendance.",
  },
  {
    title: "Followed by support",
    body: "Cohorts can be followed by mentoring and code review clinics, which is where new skills usually take hold.",
  },
];

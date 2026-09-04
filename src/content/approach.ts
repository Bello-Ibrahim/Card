export type ApproachStep = {
  number: string;
  title: string;
  summary: string;
  detail: string[];
};

export const approach: ApproachStep[] = [
  {
    number: "01",
    title: "Discover",
    summary:
      "Understand business objectives, existing architecture, data landscape, pain points and constraints.",
    detail: [
      "Stakeholder and use-case interviews",
      "Current-state architecture and data inventory",
      "Constraint mapping: budget, skills, compliance, timelines",
    ],
  },
  {
    number: "02",
    title: "Architect",
    summary:
      "Design the target data architecture, technology stack, governance model and implementation roadmap.",
    detail: [
      "Target-state reference architecture",
      "Technology selection with documented trade-offs",
      "Sequenced roadmap with cost and dependency view",
    ],
  },
  {
    number: "03",
    title: "Engineer",
    summary: "Build production-grade pipelines, platforms, integrations and data products.",
    detail: [
      "Infrastructure as code and environment parity",
      "Ingestion, transformation and orchestration",
      "Code review, automated testing and CI/CD",
    ],
  },
  {
    number: "04",
    title: "Validate",
    summary:
      "Implement testing, quality controls, observability, security and performance monitoring.",
    detail: [
      "Data quality rules and reconciliation",
      "Freshness, volume and schema monitoring",
      "Security review and performance benchmarking",
    ],
  },
  {
    number: "05",
    title: "Enable",
    summary:
      "Train internal teams and establish engineering standards, documentation and operating processes.",
    detail: [
      "Hands-on enablement and pairing",
      "Standards, runbooks and documentation",
      "Ownership and on-call model",
    ],
  },
  {
    number: "06",
    title: "Scale",
    summary:
      "Optimize the platform and continuously evolve the organization's data capabilities.",
    detail: [
      "Cost and performance optimization",
      "New domain and use-case onboarding",
      "Capability roadmap and periodic architecture review",
    ],
  },
];

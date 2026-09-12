export type ProcessStep = {
  number: string;
  title: string;
  summary: string;
  detail: string[];
};

export const process: ProcessStep[] = [
  {
    number: "01",
    title: "Discover",
    summary: "Understand the business and the data environment it actually runs on.",
    detail: [
      "Stakeholder and use-case interviews",
      "Source system and data inventory",
      "Constraints: budget, skills, compliance, timelines",
    ],
  },
  {
    number: "02",
    title: "Assess",
    summary: "Identify architecture, performance and capability gaps.",
    detail: [
      "Current-state architecture review",
      "Pipeline reliability and cost analysis",
      "Team capability and operating model assessment",
    ],
  },
  {
    number: "03",
    title: "Architect",
    summary: "Design the target state, with the trade-offs written down.",
    detail: [
      "Target reference architecture",
      "Technology selection against stated constraints",
      "Sequenced roadmap with dependencies and cost",
    ],
  },
  {
    number: "04",
    title: "Engineer",
    summary: "Build the solution as production software, not as scripts.",
    detail: [
      "Infrastructure as code and environment parity",
      "Ingestion, transformation and orchestration",
      "Code review, automated testing and CI/CD",
    ],
  },
  {
    number: "05",
    title: "Enable",
    summary: "Train and empower the internal teams who will run it.",
    detail: [
      "Hands-on enablement and pairing",
      "Standards, runbooks and documentation",
      "Ownership and incident response model",
    ],
  },
  {
    number: "06",
    title: "Scale",
    summary: "Optimize and keep improving after go-live.",
    detail: [
      "Cost and performance optimization",
      "New domain and use-case onboarding",
      "Periodic architecture review",
    ],
  },
];

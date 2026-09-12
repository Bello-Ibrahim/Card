export type TeamPillar = {
  slug: string;
  title: string;
  summary: string;
  detail: string[];
};

export const teamPillars: TeamPillar[] = [
  {
    slug: "strategy",
    title: "Strategy",
    summary: "Define the operating model.",
    detail: ["Centralised, federated or embedded", "Ownership and accountability", "Funding and prioritisation"],
  },
  {
    slug: "structure",
    title: "Structure",
    summary: "Design engineering roles.",
    detail: ["Role definitions and levelling", "Team topology and interfaces", "Career pathways"],
  },
  {
    slug: "hiring",
    title: "Hiring",
    summary: "Identify required skills.",
    detail: ["Hiring plan and sequencing", "Interview design and scorecards", "Technical assessment"],
  },
  {
    slug: "training",
    title: "Training",
    summary: "Develop existing employees.",
    detail: ["Skills assessment", "Structured programs", "Mentoring on live work"],
  },
  {
    slug: "enablement",
    title: "Enablement",
    summary: "Establish engineering standards.",
    detail: ["Standards and code review", "Onboarding and documentation", "Delivery process"],
  },
  {
    slug: "leadership",
    title: "Leadership",
    summary: "Provide technical leadership and mentorship.",
    detail: ["Fractional technical leadership", "Architecture practice", "Coaching senior engineers"],
  },
];

/** Organisational diagram rendered on the Team Setup page. */
export const teamStructure = {
  lead: "Head of Data",
  architect: "Data Architect",
  roles: [
    "Data Engineers",
    "Analytics Engineers",
    "Platform Engineers",
    "Data Analysts",
    "ML Engineers",
  ],
};

export type TeamSetupMode = {
  slug: string;
  title: string;
  summary: string;
  description: string;
  includes: string[];
  bestFor: string;
};

export const teamSetupModes: TeamSetupMode[] = [
  {
    slug: "build",
    title: "Build",
    summary: "Stand up a data engineering capability from the ground up.",
    description:
      "For organizations hiring their first dedicated data engineers. We define the roles, the order to hire them in, the standards the team will work to, and the platform they will own — then help the first engineers become productive rather than blocked.",
    includes: [
      "Role definitions and levelling",
      "Team structure and operating model",
      "Hiring plan and interview design",
      "Technology and tooling requirements",
      "Engineering standards and documentation",
      "Onboarding programme",
    ],
    bestFor: "Organizations hiring their first dedicated data engineers.",
  },
  {
    slug: "scale",
    title: "Scale",
    summary: "Expand an existing team with experienced engineering talent.",
    description:
      "For teams with more demand than capacity. We augment your team with experienced engineers, or stand up a dedicated squad working to your standards and in your tooling — with fractional technical leadership where senior coverage is the real constraint.",
    includes: [
      "Team augmentation",
      "Dedicated engineering squads",
      "Fractional technical leadership",
      "Delivery process and planning support",
      "Architecture practice and review cadence",
      "Capacity and roadmap planning",
    ],
    bestFor: "Teams whose roadmap is limited by engineering capacity or senior coverage.",
  },
  {
    slug: "enable",
    title: "Enable",
    summary: "Upskill the people you already have.",
    description:
      "For organizations with capable people in adjacent roles — analysts, software engineers, DBAs — who can become strong data engineers with structure and support. We assess current skills, design a programme against your stack, and pair training with mentoring on real work.",
    includes: [
      "Skills assessment and gap analysis",
      "Structured training programme",
      "Mentoring and pairing on live work",
      "Code review and standards coaching",
      "Career pathways and levelling",
      "Progress reporting for sponsors",
    ],
    bestFor: "Organizations who would rather develop internal talent than compete for scarce hires.",
  },
];

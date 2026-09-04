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
    summary: "Build a new data engineering capability from the ground up.",
    description:
      "For organizations standing up their first data engineering function. We define the roles you need, the order to hire them in, the standards the team will work to, and the platform they will own — then help you get the first engineers productive rather than blocked.",
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
      "For teams with more demand than capacity. We augment your team with experienced engineers, or stand up a dedicated squad that works to your standards and in your tooling — with fractional technical leadership where senior guidance is the actual constraint.",
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
    summary: "Upskill your existing workforce through structured training and mentorship.",
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

export const teamSetupCapabilities = [
  "Define data engineering roles",
  "Design team structures",
  "Establish engineering standards",
  "Build hiring plans",
  "Identify technology requirements",
  "Develop onboarding programs",
  "Train existing engineers",
  "Establish architecture practices",
  "Create delivery processes",
  "Provide fractional technical leadership",
  "Augment internal teams",
  "Build dedicated engineering squads",
];

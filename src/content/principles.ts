export type Principle = {
  title: string;
  body: string;
  icon: "engineering" | "business" | "production" | "architecture" | "transfer" | "partnership";
};

/** The six core principles shown on About and the home differentiators band. */
export const principles: Principle[] = [
  {
    title: "Engineering Excellence",
    body: "Build systems correctly. The people who design the architecture are the people who build it, which is why our designs survive contact with implementation.",
    icon: "engineering",
  },
  {
    title: "Business Impact",
    body: "Technology must solve business problems. Every recommendation carries a reason a non-technical sponsor can evaluate.",
    icon: "business",
  },
  {
    title: "Simplicity",
    body: "Complex systems should still be understandable and maintainable. If your team cannot reason about it, we have not finished.",
    icon: "architecture",
  },
  {
    title: "Reliability",
    body: "Data platforms must work when businesses depend on them — with testing, monitoring, recovery and ownership settled before go-live.",
    icon: "production",
  },
  {
    title: "Capability Transfer",
    body: "Clients should be stronger after working with us. Documentation, pairing and structured enablement are part of delivery, not an afterthought.",
    icon: "transfer",
  },
  {
    title: "Continuous Improvement",
    body: "Data platforms evolve continuously. We design for the change that is coming rather than the requirements frozen at kickoff.",
    icon: "partnership",
  },
];

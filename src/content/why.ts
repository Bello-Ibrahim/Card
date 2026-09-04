export type Pillar = {
  title: string;
  body: string;
  icon: "engineering" | "business" | "production" | "architecture" | "transfer" | "partnership";
};

export const pillars: Pillar[] = [
  {
    title: "Engineering First",
    body: "We combine consulting expertise with hands-on engineering capability. The people who design the architecture are the people who build it.",
    icon: "engineering",
  },
  {
    title: "Business-Aligned",
    body: "Technology decisions are connected to measurable business outcomes. Every recommendation carries a reason a non-technical sponsor can evaluate.",
    icon: "business",
  },
  {
    title: "Production Mindset",
    body: "We build systems designed to operate reliably in the real world — with testing, monitoring, recovery and ownership settled before go-live.",
    icon: "production",
  },
  {
    title: "Modern Architecture",
    body: "We apply current data engineering and cloud architecture practices, chosen on their merits for your constraints rather than on novelty.",
    icon: "architecture",
  },
  {
    title: "Capability Transfer",
    body: "We don't just deliver solutions — we help your teams understand and operate them, through documentation, pairing and structured enablement.",
    icon: "transfer",
  },
  {
    title: "Long-Term Partnership",
    body: "We can support organizations from initial strategy through implementation, optimization and scale, at whatever level of involvement suits you.",
    icon: "partnership",
  },
];

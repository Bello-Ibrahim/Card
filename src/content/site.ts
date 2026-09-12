/**
 * Global site configuration.
 *
 * FACTUAL ACCURACY POLICY for this repository:
 * Nothing in `src/content` may state a client name, logo, testimonial, certification,
 * award, partnership, revenue figure, project metric, headcount, founding year or office
 * address unless DataForge has verified it. Unverified fields stay `null` and the UI hides
 * them rather than rendering a placeholder that reads as fact.
 */

export const site = {
  name: "DataForge Consulting",
  shortName: "DataForge",
  wordmark: "DATAFORGE",
  descriptor: "CONSULTING",
  tagline: "Engineering the Data Foundations Behind Intelligent Business.",
  alternateTagline: "Forge Better Data. Build Better Business.",
  description:
    "DataForge Consulting designs, builds and modernizes the data platforms, pipelines and engineering capabilities organizations need to turn complex data into reliable business intelligence.",
  disciplines: ["Consulting", "Engineering", "Training", "Team Building", "Managed Services"],
  /** Override in production with NEXT_PUBLIC_SITE_URL. */
  url: process.env.NEXT_PUBLIC_SITE_URL ?? "https://www.dataforgeconsulting.com",
  locale: "en_US",
} as const;

/**
 * Verified contact channels only.
 * Set each value once DataForge confirms it; anything left `null` is simply not rendered.
 */
export const contact: {
  email: string | null;
  phone: string | null;
  location: string | null;
  linkedin: string | null;
  x: string | null;
  youtube: string | null;
} = {
  email: null,
  phone: null,
  location: null,
  linkedin: null,
  x: null,
  youtube: null,
};

export const hasDirectContactChannels =
  Boolean(contact.email) || Boolean(contact.phone) || Boolean(contact.linkedin);

export const cta = {
  primary: { label: "Talk to a Data Expert", href: "/contact" },
  short: { label: "Talk to an Expert", href: "/contact" },
  secondary: { label: "Explore Our Services", href: "/services" },
  capabilities: { label: "Explore Capabilities", href: "/services" },
  consultation: { label: "Book a Consultation", href: "/contact?intent=consultation" },
  training: { label: "Request Corporate Training", href: "/contact?intent=training" },
  team: { label: "Build My Data Team", href: "/contact?intent=team-setup" },
  challenge: { label: "Discuss My Data Challenge", href: "/contact?intent=project" },
} as const;

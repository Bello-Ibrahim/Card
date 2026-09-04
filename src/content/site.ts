/**
 * Global site configuration.
 *
 * IMPORTANT — factual accuracy policy for this repository:
 * Nothing in `src/content` may state a client name, testimonial, certification,
 * award, partnership, revenue figure, project metric, headcount, founding year or
 * office address unless GraceWell has verified it. Unverified fields are left as
 * `null` and the UI hides them rather than showing a placeholder that reads as fact.
 */

export const site = {
  name: "GraceWell Consulting Group",
  shortName: "GraceWell",
  tagline: "Engineering the data foundations behind better decisions.",
  description:
    "GraceWell Consulting Group helps organizations design, build, modernize and scale reliable data platforms — from data strategy and architecture through production data engineering, analytics enablement, training and team setup.",
  /** Override in production with NEXT_PUBLIC_SITE_URL. */
  url: process.env.NEXT_PUBLIC_SITE_URL ?? "https://www.gracewellconsulting.com",
  locale: "en_US",
} as const;

/**
 * Verified contact channels only.
 *
 * Set each value once GraceWell confirms it. Anything left as `null` is simply not
 * rendered — the site never invents an address, phone number or social profile.
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
  primary: { label: "Talk to an Expert", href: "/contact" },
  secondary: { label: "Explore Our Services", href: "/services" },
} as const;

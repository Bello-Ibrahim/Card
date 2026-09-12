import { services } from "./services";
import { solutions } from "./solutions";

export type NavLink = { label: string; href: string; description?: string };

export type NavItem = {
  label: string;
  href: string;
  /** When present, the desktop header renders a mega-menu panel. */
  menu?: {
    intro: { title: string; body: string; href: string; cta: string };
    columns: { heading: string; links: NavLink[] }[];
  };
};

const serviceLinks: NavLink[] = services.map((s) => ({
  label: s.title,
  href: `/services/${s.slug}`,
  description: s.short,
}));

const solutionLinks: NavLink[] = solutions.map((s) => ({
  label: s.title,
  href: `/solutions/${s.slug}`,
  description: s.summary,
}));

const split = (arr: NavLink[]) => {
  const half = Math.ceil(arr.length / 2);
  return [arr.slice(0, half), arr.slice(half)];
};

const [servicesA, servicesB] = split(serviceLinks);
const [solutionsA, solutionsB] = split(solutionLinks);

export const mainNav: NavItem[] = [
  { label: "Home", href: "/" },
  {
    label: "Services",
    href: "/services",
    menu: {
      intro: {
        title: "What we build",
        body: "Pipelines, platforms and the engineering practice around them — designed and built by the same team.",
        href: "/services",
        cta: "View all services",
      },
      columns: [
        { heading: "Engineering", links: servicesA },
        { heading: "Advisory & Enablement", links: servicesB },
      ],
    },
  },
  {
    label: "Solutions",
    href: "/solutions",
    menu: {
      intro: {
        title: "Solutions that move data forward",
        body: "Outcome-shaped engagements built on the platforms and practices your teams will operate.",
        href: "/solutions",
        cta: "View all solutions",
      },
      columns: [
        { heading: "Platforms", links: solutionsA },
        { heading: "Data Management & Enablement", links: solutionsB },
      ],
    },
  },
  { label: "Industries", href: "/industries" },
  { label: "Training", href: "/training" },
  { label: "Team Setup", href: "/team-setup" },
  { label: "About", href: "/about" },
  { label: "Insights", href: "/insights" },
];

export const footerNav: { heading: string; links: NavLink[] }[] = [
  {
    heading: "Services",
    links: [
      { label: "Data Engineering", href: "/services/data-engineering" },
      { label: "Data Architecture", href: "/services/data-platform-architecture" },
      { label: "Cloud", href: "/services/cloud-data-engineering" },
      { label: "Integration", href: "/services/data-integration" },
      { label: "Modernization", href: "/services/data-modernization" },
      { label: "Data Quality", href: "/services/data-quality-and-observability" },
    ],
  },
  {
    heading: "Solutions",
    links: [
      { label: "Data Platforms", href: "/solutions/modern-data-platform" },
      { label: "Warehouses", href: "/solutions/enterprise-data-warehouse" },
      { label: "Lakehouses", href: "/solutions/lakehouse" },
      { label: "Streaming", href: "/solutions/real-time-data-platform" },
      { label: "AI Foundations", href: "/solutions/ai-data-foundation" },
    ],
  },
  {
    heading: "Capability",
    links: [
      { label: "Training", href: "/training" },
      { label: "Team Setup", href: "/team-setup" },
      { label: "Managed Services", href: "/solutions/managed-data-engineering" },
      { label: "Advisory", href: "/services/data-strategy-and-advisory" },
    ],
  },
  {
    heading: "Company",
    links: [
      { label: "About", href: "/about" },
      { label: "Insights", href: "/insights" },
      { label: "Careers", href: "/about#careers" },
      { label: "Contact", href: "/contact" },
    ],
  },
];

export const legalNav: NavLink[] = [
  { label: "Privacy Policy", href: "/privacy-policy" },
  { label: "Terms", href: "/terms-of-use" },
  { label: "Cookie Policy", href: "/cookie-policy" },
];

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

const half = (arr: NavLink[]) => [arr.slice(0, Math.ceil(arr.length / 2)), arr.slice(Math.ceil(arr.length / 2))];

const [servicesA, servicesB] = half(serviceLinks);
const [solutionsA, solutionsB] = half(solutionLinks);

export const mainNav: NavItem[] = [
  {
    label: "Services",
    href: "/services",
    menu: {
      intro: {
        title: "Services",
        body: "From data strategy and architecture through production engineering, quality and enablement.",
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
        title: "Solutions",
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
  { label: "Contact", href: "/contact" },
];

export const footerNav: { heading: string; links: NavLink[] }[] = [
  {
    heading: "Company",
    links: [
      { label: "About", href: "/about" },
      { label: "Leadership", href: "/about#leadership" },
      { label: "Careers", href: "/about#careers" },
      { label: "Insights", href: "/insights" },
      { label: "Contact", href: "/contact" },
    ],
  },
  {
    heading: "Services",
    links: [
      { label: "Data Engineering", href: "/services/data-engineering" },
      { label: "Data Architecture", href: "/services/data-platform-architecture" },
      { label: "Cloud Data", href: "/services/cloud-data-engineering" },
      { label: "Data Integration", href: "/services/data-integration" },
      { label: "Data Migration", href: "/services/data-migration-and-modernization" },
      { label: "Data Quality", href: "/services/data-quality-and-observability" },
      { label: "Analytics Engineering", href: "/services/analytics-engineering" },
    ],
  },
  {
    heading: "Solutions",
    links: [
      { label: "Data Platforms", href: "/solutions/modern-data-platform" },
      { label: "Data Warehouses", href: "/solutions/enterprise-data-warehouse" },
      { label: "Lakehouses", href: "/solutions/lakehouse" },
      { label: "Data Modernization", href: "/solutions/data-migration" },
      { label: "Managed Engineering", href: "/solutions/managed-data-engineering" },
    ],
  },
  {
    heading: "Capability Development",
    links: [
      { label: "Training", href: "/training" },
      { label: "Team Setup", href: "/team-setup" },
      { label: "Engineering Enablement", href: "/team-setup#enable" },
    ],
  },
];

export const legalNav: NavLink[] = [
  { label: "Privacy Policy", href: "/privacy-policy" },
  { label: "Terms of Use", href: "/terms-of-use" },
  { label: "Cookie Policy", href: "/cookie-policy" },
];

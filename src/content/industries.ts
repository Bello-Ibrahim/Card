import type { PhotoKey } from "./media";

export type Industry = {
  slug: string;
  name: string;
  headline: string;
  description: string;
  /** Surfaced on hover / focus of the immersive industry cards. */
  challenges: string[];
  solutions: { label: string; href: string }[];
  photo: PhotoKey;
};

export const industries: Industry[] = [
  {
    slug: "financial-services",
    name: "Financial Services",
    headline: "Build reliable data foundations for payments, banking and financial analytics.",
    description:
      "Banks, payment providers and asset managers carry decades of accumulated systems and non-negotiable reporting obligations. Better engineering shortens the close, makes submissions reproducible, and gives risk and finance a lineage trail they can defend under examination.",
    challenges: [
      "Regulatory reporting that must reconcile exactly",
      "Risk data scattered across legacy cores",
      "Slow month-end close and manual adjustments",
    ],
    solutions: [
      { label: "Enterprise Data Warehouse", href: "/solutions/enterprise-data-warehouse" },
      { label: "Data Quality & Observability", href: "/solutions/data-quality" },
    ],
    photo: "industryFinancialServices",
  },
  {
    slug: "telecommunications",
    name: "Telecommunications",
    headline: "Turn network and subscriber volume into usable operational signal.",
    description:
      "Telecom estates generate enormous event volumes from network elements, billing and customer channels. Careful partitioning, streaming design and cost engineering turn that volume into signal for network operations, churn analysis and revenue assurance.",
    challenges: [
      "Event volumes that punish weak architecture",
      "Revenue assurance gaps between systems",
      "Network and customer data that never meet",
    ],
    solutions: [
      { label: "Real-Time Data Platform", href: "/solutions/real-time-data-platform" },
      { label: "Lakehouse", href: "/solutions/lakehouse" },
    ],
    photo: "industryTelecommunications",
  },
  {
    slug: "healthcare",
    name: "Healthcare",
    headline: "Integrate clinical and operational data under strict access control.",
    description:
      "Healthcare data is fragmented across clinical, administrative and claims systems, and every integration carries privacy obligations. Engineering with classification, minimisation and access control designed in allows analytics to improve care and operations without widening exposure.",
    challenges: [
      "Clinical, claims and administrative systems in isolation",
      "Privacy obligations on every integration",
      "Reporting that cannot be reproduced for audit",
    ],
    solutions: [
      { label: "Data Governance", href: "/solutions/data-governance" },
      { label: "Modern Data Platform", href: "/solutions/modern-data-platform" },
    ],
    photo: "industryHealthcare",
  },
  {
    slug: "retail-and-ecommerce",
    name: "Retail & E-commerce",
    headline: "One view of the customer, the order and the inventory.",
    description:
      "Retail data lives in commerce platforms, stores, marketplaces, logistics providers and marketing tools. Unifying it — with identity resolution and near-real-time inventory — is what makes forecasting, personalization and margin analysis credible rather than directional.",
    challenges: [
      "Customer identity split across channels",
      "Inventory signals that arrive too late to act on",
      "Marketing attribution nobody trusts",
    ],
    solutions: [
      { label: "Data Integration", href: "/solutions/data-integration" },
      { label: "Analytics Engineering", href: "/solutions/analytics-engineering" },
    ],
    photo: "industryRetail",
  },
  {
    slug: "logistics-and-transportation",
    name: "Logistics & Transportation",
    headline: "Visibility across carriers, warehouses and partners.",
    description:
      "Supply chain performance depends on data arriving from partners who each use different formats and cadences. Robust integration and quality controls turn scattered partner feeds into dependable tracking, exception management and planning inputs.",
    challenges: [
      "Partner feeds in every format imaginable",
      "Exceptions discovered after the customer notices",
      "Planning built on stale position data",
    ],
    solutions: [
      { label: "Data Integration", href: "/solutions/data-integration" },
      { label: "Real-Time Data Platform", href: "/solutions/real-time-data-platform" },
    ],
    photo: "industryLogistics",
  },
  {
    slug: "manufacturing",
    name: "Manufacturing",
    headline: "Join shop-floor telemetry to the systems where decisions are made.",
    description:
      "Manufacturers hold rich sensor and machine data that rarely reaches planning systems. Bridging operational technology and enterprise data enables quality analysis, maintenance planning and yield improvement grounded in measured reality.",
    challenges: [
      "OT and IT data that never reconcile",
      "Sensor history too expensive to keep queryable",
      "Quality issues found after the batch ships",
    ],
    solutions: [
      { label: "Lakehouse", href: "/solutions/lakehouse" },
      { label: "AI Data Foundation", href: "/solutions/ai-data-foundation" },
    ],
    photo: "industryManufacturing",
  },
  {
    slug: "government",
    name: "Government",
    headline: "Transparent, auditable data platforms built for public accountability.",
    description:
      "Public sector organizations must combine data across agencies while meeting strict transparency, residency and access requirements. Architecture with governance, lineage and documentation designed in supports both service improvement and public accountability.",
    challenges: [
      "Cross-agency data sharing under strict controls",
      "Residency and sovereignty requirements",
      "Evidence trails required for public scrutiny",
    ],
    solutions: [
      { label: "Data Governance", href: "/solutions/data-governance" },
      { label: "Modern Data Platform", href: "/solutions/modern-data-platform" },
    ],
    photo: "industryGovernment",
  },
  {
    slug: "technology",
    name: "Technology",
    headline: "Treat product telemetry like production software.",
    description:
      "Software companies generate more data than most, and usually govern it least. Treating event schemas as contracts, and analytics models as reviewed code, gives product, growth and finance a shared and trustworthy account of usage.",
    challenges: [
      "Event schemas that drift without warning",
      "Multi-tenant isolation in shared analytics",
      "Usage-based billing built on unverified data",
    ],
    solutions: [
      { label: "Analytics Engineering", href: "/solutions/analytics-engineering" },
      { label: "Data Quality & Observability", href: "/solutions/data-quality" },
    ],
    photo: "industryTechnology",
  },
];

export const getIndustry = (slug: string) => industries.find((i) => i.slug === slug);

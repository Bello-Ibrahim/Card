export type Industry = {
  slug: string;
  name: string;
  headline: string;
  description: string;
  focus: string[];
};

export const industries: Industry[] = [
  {
    slug: "financial-services",
    name: "Financial Services",
    headline: "Regulated reporting that reconciles, and risk data that arrives on time.",
    description:
      "Banks and asset managers carry decades of accumulated systems and non-negotiable reporting obligations. Better data engineering shortens the close, makes regulatory submissions reproducible, and gives risk and finance a lineage trail they can defend under examination.",
    focus: ["Regulatory reporting", "Risk data aggregation", "Finance reconciliation", "Auditability and lineage"],
  },
  {
    slug: "fintech",
    name: "Fintech",
    headline: "Move fast on product without losing the ledger.",
    description:
      "Fintechs need product analytics, fraud signals and financial controls from the same data foundation. Engineering that separates event data from ledger truth — and keeps both reconciled — lets teams ship quickly while remaining auditable as regulatory scrutiny grows.",
    focus: ["Transaction pipelines", "Fraud and risk signals", "Ledger reconciliation", "Product analytics"],
  },
  {
    slug: "telecommunications",
    name: "Telecommunications",
    headline: "Network and subscriber data at volumes that punish weak architecture.",
    description:
      "Telecom estates generate enormous event volumes from network elements, billing and customer channels. Careful partitioning, streaming design and cost engineering turn that volume into usable signal for network operations, churn analysis and revenue assurance.",
    focus: ["Network event processing", "Revenue assurance", "Churn and subscriber analytics", "High-volume streaming"],
  },
  {
    slug: "healthcare",
    name: "Healthcare",
    headline: "Clinical and operational data, integrated under strict access control.",
    description:
      "Healthcare data is fragmented across clinical, administrative and claims systems, and every integration carries privacy obligations. Engineering with classification, minimisation and access control built in allows analytics to improve care and operations without widening exposure.",
    focus: ["Clinical and claims integration", "Privacy and access control", "Operational analytics", "Interoperability standards"],
  },
  {
    slug: "retail-and-ecommerce",
    name: "Retail & E-commerce",
    headline: "One view of the customer, the order and the inventory.",
    description:
      "Retail data lives in commerce platforms, stores, marketplaces, logistics providers and marketing tools. Unifying it — with identity resolution and near-real-time inventory — is what makes demand forecasting, personalization and margin analysis credible rather than directional.",
    focus: ["Customer identity resolution", "Inventory and supply signals", "Marketing attribution", "Demand forecasting inputs"],
  },
  {
    slug: "manufacturing",
    name: "Manufacturing",
    headline: "Shop-floor telemetry joined to enterprise systems.",
    description:
      "Manufacturers hold rich sensor and machine data that rarely reaches the systems where planning decisions are made. Bridging operational technology and enterprise data enables quality analysis, maintenance planning and yield improvement grounded in measured reality.",
    focus: ["Sensor and telemetry pipelines", "OT/IT integration", "Quality and yield analytics", "Maintenance data foundations"],
  },
  {
    slug: "logistics-and-supply-chain",
    name: "Logistics & Supply Chain",
    headline: "Visibility across carriers, warehouses and partners.",
    description:
      "Supply chain performance depends on data arriving from partners who each use different formats and cadences. Robust integration and quality controls turn scattered partner feeds into dependable tracking, exception management and planning inputs.",
    focus: ["Partner data integration", "Shipment and route data", "Exception detection", "Planning data foundations"],
  },
  {
    slug: "technology",
    name: "Technology",
    headline: "Product telemetry engineered like production software.",
    description:
      "Software companies generate more data than most, and usually govern it least. Treating event schemas as contracts, and analytics models as reviewed code, gives product, growth and finance teams a shared and trustworthy account of usage.",
    focus: ["Event schema governance", "Usage and product analytics", "Multi-tenant data isolation", "Usage-based billing data"],
  },
  {
    slug: "professional-services",
    name: "Professional Services",
    headline: "Utilisation, delivery and pipeline data in one place.",
    description:
      "Professional services firms run on people, time and pipeline, tracked across finance, CRM and delivery tools that rarely agree. Integrating them gives leadership a dependable view of utilisation, margin and demand.",
    focus: ["Utilisation and capacity", "Project profitability", "Pipeline integration", "Resource planning data"],
  },
  {
    slug: "government-and-public-sector",
    name: "Government & Public Sector",
    headline: "Transparent, auditable data platforms built for public accountability.",
    description:
      "Public sector organizations must combine data across agencies while meeting strict transparency, residency and access requirements. Architecture with governance, lineage and documentation designed in supports both service improvement and public accountability.",
    focus: ["Cross-agency integration", "Data residency and sovereignty", "Transparency and reporting", "Records and retention"],
  },
  {
    slug: "energy",
    name: "Energy",
    headline: "Time-series data at grid and asset scale.",
    description:
      "Energy organizations manage dense time-series data from generation, distribution and metering assets. Engineering that handles late-arriving readings, corrections and long histories makes forecasting, asset performance and settlement analysis dependable.",
    focus: ["Time-series pipelines", "Metering and settlement data", "Asset performance", "Forecasting inputs"],
  },
  {
    slug: "education",
    name: "Education",
    headline: "Student and institutional data joined responsibly.",
    description:
      "Institutions hold learner data across admissions, learning platforms and student services, governed by clear privacy expectations. Careful integration supports retention, outcomes analysis and planning while keeping sensitive records tightly controlled.",
    focus: ["Student lifecycle data", "Learning platform integration", "Outcomes analytics", "Privacy-conscious modelling"],
  },
];

export const getIndustry = (slug: string) => industries.find((i) => i.slug === slug);

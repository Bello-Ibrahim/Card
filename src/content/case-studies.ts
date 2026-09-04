/**
 * Engagement patterns.
 *
 * These are ILLUSTRATIVE descriptions of the kinds of problems GraceWell works on.
 * They intentionally name no client, quote no metric and claim no result, because none
 * has been verified for publication.
 *
 * When a real, client-approved case study is available, add it here with
 * `verified: true`, a client name and any approved figures. The UI shows the
 * "illustrative" disclosure only while `verified` is false.
 */

export type CaseStudy = {
  slug: string;
  title: string;
  sector: string;
  challenge: string;
  approach: string;
  outcome: string;
  capabilities: string[];
  verified: boolean;
  client?: string;
};

export const caseStudies: CaseStudy[] = [
  {
    slug: "modernizing-an-enterprise-data-platform",
    title: "Modernizing an Enterprise Data Platform",
    sector: "Enterprise",
    challenge:
      "Fragmented data systems, slow reporting and limited data reliability, with no single owner for the numbers leadership reviewed each week.",
    approach:
      "Designed a modern cloud data platform, consolidated overlapping ingestion paths, and automated the organization's data pipelines with orchestration, testing and monitoring built in.",
    outcome:
      "Improved data accessibility, reliability, scalability and analytics readiness, with clear ownership for each critical dataset.",
    capabilities: ["Platform architecture", "Data engineering", "Observability"],
    verified: false,
  },
  {
    slug: "migrating-a-legacy-data-warehouse",
    title: "Migrating a Legacy Data Warehouse",
    sector: "Regulated industry",
    challenge:
      "An ageing on-premise warehouse carrying years of undocumented transformation logic, with downstream consumers nobody could fully enumerate.",
    approach:
      "Inventoried every workload and consumer, converted transformation logic incrementally, and ran the legacy and target platforms in parallel until outputs reconciled.",
    outcome:
      "A validated cutover with documented lineage, and a legacy platform retired on evidence rather than on a scheduled date.",
    capabilities: ["Data migration", "Data warehousing", "Reconciliation testing"],
    verified: false,
  },
  {
    slug: "building-an-internal-data-engineering-team",
    title: "Building an Internal Data Engineering Team",
    sector: "Growth-stage organization",
    challenge:
      "Growing analytics demand handled entirely by external contractors, with no internal engineering capability and no standards to hire against.",
    approach:
      "Defined roles, levelling and team structure, established engineering standards and onboarding, and combined structured training with mentoring on live delivery work.",
    outcome:
      "An internal team operating the platform to documented standards, with external support reduced to advisory and peak capacity.",
    capabilities: ["Team setup", "Training", "Engineering enablement"],
    verified: false,
  },
];

export const getCaseStudy = (slug: string) => caseStudies.find((c) => c.slug === slug);

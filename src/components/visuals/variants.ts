import type { CoverVariant } from "./cover-art";
import type { InsightCategory } from "@/content/insights";
import type { Service } from "@/content/services";

/**
 * Subject → visual mapping.
 *
 * Each variant is an abstract reading of its subject, so the artwork stays meaningful
 * rather than random: pipelines get flow lines, architecture gets strata, cloud gets a mesh.
 */
export const CATEGORY_VARIANT: Record<InsightCategory, CoverVariant> = {
  "Data Engineering": "flow",
  "Data Architecture": "strata",
  Cloud: "mesh",
  "Data Strategy": "radial",
  Analytics: "field",
  "AI & Data": "embedding",
  "Engineering Leadership": "tree",
  "Career & Training": "steps",
};

export const SERVICE_ICON_VARIANT: Record<Service["icon"], CoverVariant> = {
  pipeline: "flow",
  architecture: "strata",
  cloud: "mesh",
  warehouse: "strata",
  integration: "mesh",
  migration: "flow",
  analytics: "field",
  quality: "field",
  strategy: "radial",
};

const SOLUTION_VARIANT: Record<string, CoverVariant> = {
  "modern-data-platform": "strata",
  "enterprise-data-warehouse": "strata",
  lakehouse: "strata",
  "real-time-data-platform": "flow",
  "data-migration": "flow",
  "data-integration": "mesh",
  "data-quality": "field",
  "data-governance": "tree",
  "analytics-engineering": "field",
  "ai-ml-data-foundations": "embedding",
  "data-platform-optimization": "field",
  "managed-data-engineering": "mesh",
};

export const solutionVariant = (slug: string): CoverVariant => SOLUTION_VARIANT[slug] ?? "mesh";

const CASE_STUDY_VARIANT: Record<string, CoverVariant> = {
  "modernizing-an-enterprise-data-platform": "strata",
  "migrating-a-legacy-data-warehouse": "flow",
  "building-an-internal-data-engineering-team": "tree",
};

export const caseStudyVariant = (slug: string): CoverVariant => CASE_STUDY_VARIANT[slug] ?? "mesh";

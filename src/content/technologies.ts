/**
 * Technology ecosystem.
 *
 * These are the tools DataForge's engineers build with. They are NOT partnership,
 * certification, affiliation or client-endorsement claims, and the UI says so on the page.
 * Add or remove entries here and every surface that renders the ecosystem updates.
 */

export type TechnologyGroup = {
  category: string;
  blurb: string;
  items: string[];
};

export const technologyGroups: TechnologyGroup[] = [
  {
    category: "Languages",
    blurb: "What the pipelines are actually written in.",
    items: ["Python", "SQL", "Java"],
  },
  {
    category: "Processing",
    blurb: "Distributed compute for volume that no longer fits on one machine.",
    items: ["Apache Spark"],
  },
  {
    category: "Streaming",
    blurb: "Event transport for decisions that cannot wait for tomorrow's batch.",
    items: ["Apache Kafka"],
  },
  {
    category: "Orchestration",
    blurb: "Scheduling, dependencies and retries.",
    items: ["Apache Airflow"],
  },
  {
    category: "Transformation",
    blurb: "Modelling, testing and documentation of the analytical layer.",
    items: ["dbt"],
  },
  {
    category: "Databases",
    blurb: "Operational systems we integrate with and migrate from.",
    items: ["PostgreSQL", "MySQL", "SQL Server", "MongoDB"],
  },
  {
    category: "Cloud",
    blurb: "Platform foundations and managed data services.",
    items: ["AWS", "Azure", "Google Cloud"],
  },
  {
    category: "Data Platforms",
    blurb: "Warehouses, lakehouses and unified analytics platforms.",
    items: ["Snowflake", "Databricks", "BigQuery", "Redshift"],
  },
  {
    category: "Analytics",
    blurb: "The reporting layer teams work in daily.",
    items: ["Power BI", "Tableau"],
  },
];

/** Short capability strip shown beneath the hero. */
export const capabilityStrip = [
  "Architecture",
  "Engineering",
  "Cloud",
  "Streaming",
  "Analytics",
  "AI Readiness",
  "Training",
  "Talent",
];

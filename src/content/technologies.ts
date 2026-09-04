/**
 * Technology ecosystem.
 *
 * Only list technologies GraceWell actually works with. Add or remove entries here and
 * every page that renders the ecosystem updates automatically. These are the tools we
 * build with — they are not partnership, certification or vendor-affiliation claims.
 */

export type TechnologyGroup = {
  category: string;
  blurb: string;
  items: string[];
};

export const technologyGroups: TechnologyGroup[] = [
  {
    category: "Cloud",
    blurb: "Platform foundations, infrastructure and managed data services.",
    items: ["AWS", "Microsoft Azure", "Google Cloud"],
  },
  {
    category: "Data Platforms",
    blurb: "Warehouses, lakehouses and unified analytics platforms.",
    items: ["Snowflake", "Databricks", "BigQuery", "Amazon Redshift", "Microsoft Fabric"],
  },
  {
    category: "Engineering",
    blurb: "Languages and processing engines behind the pipelines.",
    items: ["Python", "SQL", "Apache Spark", "Apache Kafka"],
  },
  {
    category: "Transformation & Orchestration",
    blurb: "Modelling, scheduling and dependency management.",
    items: ["dbt", "Apache Airflow"],
  },
  {
    category: "Databases",
    blurb: "Operational systems we integrate with and migrate from.",
    items: ["PostgreSQL", "MySQL", "SQL Server", "MongoDB"],
  },
  {
    category: "Analytics",
    blurb: "The reporting and exploration layer teams work in daily.",
    items: ["Power BI", "Tableau", "Looker"],
  },
];

/** Short capability strip shown directly beneath the hero. */
export const capabilityStrip = [
  {
    title: "Cloud Data Platforms",
    items: ["AWS", "Azure", "Google Cloud"],
  },
  {
    title: "Data Warehousing",
    items: ["Snowflake", "BigQuery", "Redshift", "Databricks"],
  },
  {
    title: "Data Engineering",
    items: ["Python", "SQL", "Spark", "dbt", "Airflow"],
  },
  {
    title: "Data Integration",
    items: ["APIs", "ETL", "ELT", "Streaming"],
  },
];

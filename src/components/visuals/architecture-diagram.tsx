import { cn } from "@/lib/utils";

/**
 * The signature "raw data to business intelligence" architecture.
 *
 * Built from real markup rather than a flat image: the stage names and technologies are
 * selectable text in an ordered list, so the diagram is readable by search engines and
 * screen readers and reflows properly on a phone. The flow animation is a moving gradient
 * on the connectors, which works at any width and is switched off by prefers-reduced-motion.
 */

export type Stage = {
  id: string;
  label: string;
  items: string[];
  emphasis?: boolean;
};

export const PLATFORM_STAGES: Stage[] = [
  {
    id: "sources",
    label: "Data Sources",
    items: ["SQL Server", "PostgreSQL", "MySQL", "MongoDB", "APIs", "Files", "SaaS", "Applications"],
  },
  { id: "ingestion", label: "Ingestion", items: ["APIs", "CDC", "Kafka", "Batch", "Streaming"] },
  { id: "processing", label: "Processing", items: ["Python", "Spark", "SQL", "dbt"] },
  { id: "orchestration", label: "Orchestration", items: ["Airflow", "CI/CD"] },
  {
    id: "storage",
    label: "Storage",
    items: ["Data Lake", "Data Warehouse", "Lakehouse"],
    emphasis: true,
  },
  {
    id: "consumption",
    label: "Consumption",
    items: ["Power BI", "Tableau", "AI", "ML", "Applications"],
  },
];

function Connector({ index }: { index: number }) {
  return (
    <li aria-hidden="true" className="flex shrink-0 items-center justify-center py-1 xl:self-center xl:py-0">
      <span className="relative block h-8 w-px overflow-hidden bg-white/12 xl:h-px xl:w-10">
        <span
          className="flow-sheen absolute inset-0 block"
          style={{ animationDelay: `${index * 320}ms` }}
        />
      </span>
    </li>
  );
}

export function ArchitectureDiagram({
  stages = PLATFORM_STAGES,
  className,
}: {
  stages?: Stage[];
  className?: string;
}) {
  return (
    <ol className={cn("flex flex-col items-stretch xl:flex-row xl:items-stretch", className)}>
      {stages.flatMap((stage, index) => {
        const node = (
          <li key={stage.id} className="min-w-0 flex-1">
            <div
              className={cn(
                "h-full rounded-xl border p-4 transition-colors duration-300 sm:p-5",
                stage.emphasis
                  ? "border-accent-400/45 bg-accent-500/12"
                  : "border-white/12 bg-white/[0.035] hover:border-white/25",
              )}
            >
              <div className="flex items-center gap-2.5">
                <span
                  aria-hidden="true"
                  className={cn(
                    "h-1.5 w-1.5 shrink-0 rounded-full",
                    stage.emphasis ? "bg-cyan-400" : "bg-accent-400",
                  )}
                />
                <h3 className="text-[0.6875rem] font-semibold uppercase tracking-[0.14em] text-white">
                  {stage.label}
                </h3>
              </div>
              <ul className="mt-3.5 flex flex-wrap gap-1.5">
                {stage.items.map((item) => (
                  <li
                    key={item}
                    className="rounded-md border border-white/10 bg-white/[0.04] px-2 py-1 text-[0.75rem] leading-none text-mist-300"
                  >
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          </li>
        );
        return index < stages.length - 1
          ? [node, <Connector key={`c-${stage.id}`} index={index} />]
          : [node];
      })}
    </ol>
  );
}

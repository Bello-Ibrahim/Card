import { cn } from "@/lib/utils";

/**
 * Data quality monitoring dashboard — a UI illustration.
 *
 * IMPORTANT: the figures here are illustrative of what a monitoring surface looks like.
 * They are not measurements of DataForge's platforms or of any client's, and the section
 * that renders this says so on the page.
 */

const TILES = [
  { label: "Pipeline health", value: "142 / 145", note: "3 degraded", tone: "warn" as const },
  { label: "Data freshness", value: "4m 12s", note: "within SLA", tone: "ok" as const },
  { label: "Failed records", value: "0.02%", note: "last 24h", tone: "ok" as const },
  { label: "SLA status", value: "On track", note: "12 of 12 critical datasets", tone: "ok" as const },
  { label: "Quality score", value: "97.4", note: "rolling 7-day", tone: "ok" as const },
  { label: "Pipeline latency", value: "p95 8m", note: "target 15m", tone: "ok" as const },
];

const CHECKS = [
  { name: "orders_fact · row count", state: "pass" as const, detail: "within expected range" },
  { name: "customer_dim · uniqueness", state: "pass" as const, detail: "no duplicate keys" },
  { name: "payments · freshness", state: "warn" as const, detail: "12m behind schedule" },
  { name: "inventory · referential integrity", state: "pass" as const, detail: "all keys resolve" },
  { name: "events · schema drift", state: "fail" as const, detail: "unexpected column: legacy_id" },
  { name: "ledger · reconciliation", state: "pass" as const, detail: "matches source" },
];

const STATE_STYLES = {
  pass: { dot: "bg-teal-400", label: "Pass", text: "text-teal-400" },
  warn: { dot: "bg-amber-400", label: "Warn", text: "text-amber-400" },
  fail: { dot: "bg-rose-400", label: "Fail", text: "text-rose-400" },
};

/** Deterministic sparkline shape — not data, just a plausible silhouette. */
const SPARK = [14, 18, 12, 22, 19, 26, 21, 30, 24, 28, 33, 29, 36, 31, 38];

export function QualityDashboard({ className }: { className?: string }) {
  const max = Math.max(...SPARK);

  return (
    <div
      className={cn(
        "overflow-hidden rounded-2xl border border-white/12 bg-navy-950/80 shadow-[0_40px_80px_-40px_rgba(0,0,0,0.9)] backdrop-blur-sm",
        className,
      )}
    >
      <div className="flex items-center justify-between border-b border-white/10 px-5 py-3.5">
        <div className="flex items-center gap-2.5">
          <span aria-hidden="true" className="h-2 w-2 rounded-full bg-teal-400" />
          <p className="text-[0.8125rem] font-medium text-white">Platform observability</p>
        </div>
        <p className="font-mono text-[0.6875rem] uppercase tracking-[0.14em] text-mist-500">
          Illustrative view
        </p>
      </div>

      <div className="grid grid-cols-2 gap-px bg-white/8 sm:grid-cols-3">
        {TILES.map((tile) => (
          <div key={tile.label} className="bg-navy-950 p-4">
            <p className="text-[0.6875rem] uppercase tracking-[0.1em] text-mist-500">{tile.label}</p>
            <p
              className={cn(
                "mt-2 font-display text-[1.375rem] font-semibold tracking-[-0.02em]",
                tile.tone === "warn" ? "text-amber-300" : "text-white",
              )}
            >
              {tile.value}
            </p>
            <p className="mt-0.5 text-[0.75rem] text-mist-500">{tile.note}</p>
          </div>
        ))}
      </div>

      <div className="border-t border-white/10 px-5 py-4">
        <div className="flex items-end justify-between gap-4">
          <p className="text-[0.75rem] uppercase tracking-[0.1em] text-mist-500">Records processed</p>
          <div aria-hidden="true" className="flex h-10 flex-1 items-end justify-end gap-[3px]">
            {SPARK.map((v, i) => (
              <span
                key={i}
                className="w-1.5 rounded-sm bg-accent-500/70"
                style={{ height: `${(v / max) * 100}%` }}
              />
            ))}
          </div>
        </div>
      </div>

      <ul className="divide-y divide-white/8 border-t border-white/10">
        {CHECKS.map((check) => {
          const style = STATE_STYLES[check.state];
          return (
            <li key={check.name} className="flex items-center gap-3 px-5 py-2.5">
              <span aria-hidden="true" className={cn("h-1.5 w-1.5 shrink-0 rounded-full", style.dot)} />
              <span className="min-w-0 flex-1 truncate font-mono text-[0.75rem] text-mist-300">
                {check.name}
              </span>
              <span className="hidden text-[0.75rem] text-mist-500 sm:block">{check.detail}</span>
              <span className={cn("w-10 text-right text-[0.75rem] font-medium", style.text)}>
                {style.label}
              </span>
            </li>
          );
        })}
      </ul>
    </div>
  );
}

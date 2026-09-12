import { cn } from "@/lib/utils";

const BEFORE = ["Legacy systems", "Manual processes", "Disconnected databases", "Slow reporting"];
const AFTER = ["Cloud platform", "Automated pipelines", "Governed data", "Real-time analytics"];

/**
 * The modernization service's before → after comparison.
 * Tone-aware, because it appears both on the white services showcase and on dark sections.
 */
export function BeforeAfter({
  className,
  tone = "dark",
}: {
  className?: string;
  tone?: "light" | "dark";
}) {
  const dark = tone === "dark";

  return (
    <div className={cn("grid gap-4 lg:grid-cols-[1fr_auto_1fr] lg:items-center", className)}>
      <div
        className={cn(
          "rounded-2xl border p-6",
          dark ? "border-white/10 bg-white/[0.03]" : "border-navy-950/10 bg-mist-50",
        )}
      >
        <p
          className={cn(
            "text-[0.6875rem] font-semibold uppercase tracking-[0.16em]",
            dark ? "text-mist-400" : "text-mist-500",
          )}
        >
          Before
        </p>
        <ul className="mt-4 space-y-2.5">
          {BEFORE.map((item) => (
            <li
              key={item}
              className={cn("flex items-start gap-2.5 text-[0.9375rem]", dark ? "text-mist-400" : "text-mist-600")}
            >
              <span
                aria-hidden="true"
                className={cn("mt-[0.45rem] h-1 w-3 shrink-0 rounded-full", dark ? "bg-mist-600" : "bg-mist-400")}
              />
              {item}
            </li>
          ))}
        </ul>
      </div>

      <div className="flex items-center justify-center gap-3 py-2 lg:flex-col lg:py-0">
        <span aria-hidden="true" className={cn("h-px w-8 lg:h-8 lg:w-px", dark ? "bg-white/15" : "bg-navy-950/15")} />
        <span
          className={cn(
            "rounded-full border px-3.5 py-1.5 text-[0.6875rem] font-semibold uppercase tracking-[0.14em]",
            dark
              ? "border-accent-400/45 bg-accent-500/15 text-accent-300"
              : "border-accent-500/35 bg-accent-500/10 text-accent-700",
          )}
        >
          Modernization
        </span>
        <span aria-hidden="true" className={cn("h-px w-8 lg:h-8 lg:w-px", dark ? "bg-white/15" : "bg-navy-950/15")} />
      </div>

      <div
        className={cn(
          "rounded-2xl border p-6",
          dark ? "border-accent-400/35 bg-accent-500/10" : "border-accent-500/25 bg-accent-500/[0.06]",
        )}
      >
        <p
          className={cn(
            "text-[0.6875rem] font-semibold uppercase tracking-[0.16em]",
            dark ? "text-accent-300" : "text-accent-700",
          )}
        >
          After
        </p>
        <ul className="mt-4 space-y-2.5">
          {AFTER.map((item) => (
            <li
              key={item}
              className={cn("flex items-start gap-2.5 text-[0.9375rem]", dark ? "text-white" : "text-navy-950")}
            >
              <svg viewBox="0 0 16 16" aria-hidden="true" className={cn("mt-0.5 h-4 w-4 shrink-0", dark ? "text-cyan-400" : "text-accent-600")}>
                <path d="M3 8.4 6.3 11.7 13 5" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              {item}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

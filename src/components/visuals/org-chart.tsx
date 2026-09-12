import { teamStructure } from "@/content/team-setup";
import { cn } from "@/lib/utils";

/**
 * Data engineering team structure.
 *
 * Rendered as a nested list so the hierarchy is real structure rather than a picture of one;
 * the connecting lines are CSS borders on aria-hidden elements.
 */
export function OrgChart({ className }: { className?: string }) {
  return (
    <div className={cn("rounded-2xl border border-white/12 bg-white/[0.03] p-6 sm:p-8", className)}>
      <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-300">
        Reference team structure
      </p>

      <ul className="mt-7 flex flex-col items-center">
        <li className="flex w-full flex-col items-center">
          <span className="rounded-xl border border-accent-400/50 bg-accent-500/15 px-5 py-2.5 text-[0.9375rem] font-semibold text-white">
            {teamStructure.lead}
          </span>
          <span aria-hidden="true" className="h-6 w-px bg-white/20" />

          <ul className="flex w-full flex-col items-center">
            <li className="flex w-full flex-col items-center">
              <span className="rounded-xl border border-white/20 bg-white/[0.06] px-5 py-2.5 text-[0.9375rem] font-medium text-white">
                {teamStructure.architect}
              </span>
              <span aria-hidden="true" className="h-6 w-px bg-white/20" />
              <span aria-hidden="true" className="h-px w-[85%] bg-white/15" />

              <ul className="grid w-full grid-cols-2 gap-x-3 gap-y-0 sm:grid-cols-3 lg:grid-cols-5">
                {teamStructure.roles.map((role) => (
                  <li key={role} className="flex flex-col items-center">
                    <span aria-hidden="true" className="h-6 w-px bg-white/15" />
                    <span className="w-full rounded-lg border border-white/12 bg-white/[0.04] px-3 py-2.5 text-center text-[0.8125rem] leading-snug text-mist-300">
                      {role}
                    </span>
                  </li>
                ))}
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  );
}

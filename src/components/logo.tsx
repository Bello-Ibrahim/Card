import { cn } from "@/lib/utils";

/**
 * GraceWell mark: a "G" implied by an arc of connected data nodes.
 * Purely geometric so it renders crisply at every size and needs no image request.
 */
export function Logo({ className, tone = "light" }: { className?: string; tone?: "light" | "dark" }) {
  const stroke = tone === "light" ? "var(--color-navy-900)" : "#ffffff";
  return (
    <svg viewBox="0 0 32 32" role="img" aria-hidden="true" className={cn("shrink-0", className)}>
      <rect width="32" height="32" rx="8" fill={tone === "light" ? "var(--color-navy-950)" : "#ffffff"} />
      <g
        fill="none"
        stroke={tone === "light" ? "#ffffff" : "var(--color-navy-950)"}
        strokeWidth="1.6"
        strokeLinecap="round"
      >
        <path d="M22 11.2A7.2 7.2 0 1 0 23.2 16h-6" />
      </g>
      <circle cx="23.2" cy="16" r="2.1" fill="var(--color-accent-400)" />
      <circle cx="8.9" cy="16" r="1.5" fill="var(--color-cyan-400)" opacity="0.9" />
      <g stroke={stroke} strokeWidth="0" />
    </svg>
  );
}

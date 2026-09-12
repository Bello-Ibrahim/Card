import { cn } from "@/lib/utils";

/**
 * DataForge mark: three data strata being struck by a forge spark.
 * Purely geometric, so it stays crisp at any size and costs no image request.
 */
export function LogoMark({ className, tone = "light" }: { className?: string; tone?: "light" | "dark" }) {
  const onDark = tone === "dark";
  return (
    <svg viewBox="0 0 32 32" aria-hidden="true" focusable="false" className={cn("shrink-0", className)}>
      <rect width="32" height="32" rx="8" fill={onDark ? "#ffffff" : "var(--color-navy-950)"} />
      <g fill={onDark ? "var(--color-navy-950)" : "#ffffff"}>
        <rect x="7" y="9" width="18" height="3.2" rx="1.6" opacity="0.9" />
        <rect x="7" y="14.4" width="13" height="3.2" rx="1.6" opacity="0.55" />
        <rect x="7" y="19.8" width="8" height="3.2" rx="1.6" opacity="0.35" />
      </g>
      <path
        d="M21.5 12.2 17.8 18.4h3.1l-1.9 4.6 5.2-7.1h-3.2l1.8-3.7z"
        fill="var(--color-cyan-400)"
      />
    </svg>
  );
}

/** Full lockup: mark + DATAFORGE wordmark + CONSULTING descriptor. */
export function Logo({
  className,
  tone = "light",
  showDescriptor = true,
  markClassName,
}: {
  className?: string;
  tone?: "light" | "dark";
  showDescriptor?: boolean;
  markClassName?: string;
}) {
  const onDark = tone === "dark";
  return (
    <span className={cn("flex items-center gap-2.5", className)}>
      <LogoMark tone={tone} className={cn("h-8 w-8", markClassName)} />
      <span className="flex flex-col leading-none">
        <span
          className={cn(
            "font-display text-[1.0625rem] font-extrabold tracking-[0.06em]",
            onDark ? "text-white" : "text-navy-950",
          )}
        >
          DATAFORGE
        </span>
        {showDescriptor ? (
          <span
            className={cn(
              "mt-[3px] text-[0.5625rem] font-semibold tracking-[0.28em]",
              onDark ? "text-mist-400" : "text-mist-500",
            )}
          >
            CONSULTING
          </span>
        ) : null}
      </span>
    </span>
  );
}

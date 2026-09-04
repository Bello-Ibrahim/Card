import { cn } from "@/lib/utils";

export function Eyebrow({
  children,
  tone = "light",
  className,
}: {
  children: React.ReactNode;
  tone?: "light" | "dark";
  className?: string;
}) {
  return (
    <p
      className={cn(
        "flex items-center gap-2.5 text-[0.6875rem] font-semibold uppercase tracking-[0.18em]",
        tone === "light" ? "text-accent-600" : "text-accent-300",
        className,
      )}
    >
      <span
        aria-hidden="true"
        className={cn(
          "h-px w-6",
          tone === "light" ? "bg-accent-500/60" : "bg-accent-300/60",
        )}
      />
      {children}
    </p>
  );
}

export function SectionHeader({
  eyebrow,
  title,
  lede,
  tone = "light",
  align = "left",
  className,
  children,
  as: Heading = "h2",
}: {
  eyebrow?: string;
  title: React.ReactNode;
  lede?: React.ReactNode;
  tone?: "light" | "dark";
  align?: "left" | "center";
  className?: string;
  children?: React.ReactNode;
  as?: "h1" | "h2" | "h3";
}) {
  return (
    <div
      className={cn(
        "flex flex-col gap-5",
        align === "center" ? "items-center text-center" : "items-start",
        className,
      )}
    >
      {eyebrow ? <Eyebrow tone={tone}>{eyebrow}</Eyebrow> : null}
      <Heading
        className={cn(
          "text-headline",
          tone === "light" ? "text-navy-950" : "text-white",
          align === "center" ? "max-w-3xl" : "max-w-2xl",
        )}
      >
        {title}
      </Heading>
      {lede ? (
        <p
          className={cn(
            "text-lede",
            tone === "dark" && "text-mist-300",
            align === "center" ? "max-w-2xl" : "max-w-xl",
          )}
        >
          {lede}
        </p>
      ) : null}
      {children}
    </div>
  );
}

import { process } from "@/content/process";
import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { cn } from "@/lib/utils";

/**
 * Consulting process. A true horizontal timeline from `lg` up; a vertical rail on small
 * screens — an intentional mobile layout rather than stacked desktop cards.
 */
export function ProcessTimeline({ tone = "light" }: { tone?: "light" | "dark" }) {
  const dark = tone === "dark";
  return (
    <section
      className={cn("relative", dark ? "dark-section overflow-hidden bg-navy-950" : "bg-white")}
      aria-labelledby="process-heading"
    >
      {dark ? (
        <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-40" />
      ) : null}
      <Container className="relative py-20 sm:py-24 lg:py-28">
        <SectionHeader
          eyebrow="How we work"
          tone={tone}
          title="From data complexity to data confidence."
          lede="Six stages that take an organization from an unclear data landscape to a platform its own teams can operate and extend."
        />

        <ol className="relative mt-14 grid gap-y-10 lg:grid-cols-6 lg:gap-x-6">
          <li
            aria-hidden="true"
            className={cn(
              "absolute left-[0.6875rem] top-2 hidden h-[calc(100%-1rem)] w-px sm:block lg:left-0 lg:top-[0.6875rem] lg:h-px lg:w-full",
              dark
                ? "bg-gradient-to-b from-accent-400/60 via-white/12 to-transparent lg:bg-gradient-to-r"
                : "bg-gradient-to-b from-accent-500/50 via-navy-950/12 to-transparent lg:bg-gradient-to-r",
            )}
          />
          {process.map((step, index) => (
            <Reveal
              as="li"
              key={step.number}
              delay={index * 70}
              className="relative pl-10 sm:pl-12 lg:pl-0 lg:pt-12"
            >
              <span
                aria-hidden="true"
                className={cn(
                  "absolute left-0 top-1 flex h-[1.375rem] w-[1.375rem] items-center justify-center rounded-full border lg:top-0",
                  dark ? "border-white/20 bg-navy-950" : "border-navy-950/12 bg-white",
                )}
              >
                <span className="h-1.5 w-1.5 rounded-full bg-accent-500" />
              </span>
              <p className={cn("font-mono text-[0.75rem] font-medium tracking-[0.1em]", dark ? "text-accent-300" : "text-accent-600")}>
                {step.number}
              </p>
              <h3 className={cn("mt-2 text-[1.0625rem] font-semibold tracking-[-0.02em]", dark ? "text-white" : "text-navy-950")}>
                {step.title}
              </h3>
              <p className={cn("mt-2.5 text-[0.875rem] leading-relaxed", dark ? "text-mist-300" : "text-mist-600")}>
                {step.summary}
              </p>
              <ul className="mt-4 space-y-1.5">
                {step.detail.map((item) => (
                  <li
                    key={item}
                    className={cn("flex items-start gap-2 text-[0.8125rem]", dark ? "text-mist-400" : "text-mist-500")}
                  >
                    <span
                      aria-hidden="true"
                      className={cn("mt-[0.4rem] h-1 w-1 shrink-0 rounded-full", dark ? "bg-white/30" : "bg-mist-300")}
                    />
                    {item}
                  </li>
                ))}
              </ul>
            </Reveal>
          ))}
        </ol>
      </Container>
    </section>
  );
}

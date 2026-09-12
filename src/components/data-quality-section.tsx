import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { QualityDashboard } from "@/components/visuals/quality-dashboard";

export function DataQualitySection() {
  return (
    <section className="dark-section relative isolate overflow-hidden bg-ink-950 text-white" aria-labelledby="quality-heading">
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-40" />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute -right-20 top-1/4 h-[30rem] w-[30rem] rounded-full bg-teal-500/12 blur-[130px]"
      />
      <Container className="relative py-20 sm:py-24 lg:py-28">
        <div className="grid items-center gap-12 lg:grid-cols-12 lg:gap-16">
          <div className="lg:col-span-5">
            <SectionHeader
              eyebrow="Data quality"
              tone="dark"
              title="Because bad data creates expensive decisions."
              lede="Build confidence into your data with automated validation, monitoring, observability and governance — owned by the teams who produce it."
            />
            <Reveal delay={140}>
              <ul className="mt-8 space-y-3">
                {[
                  "Tests that run on every change, not quarterly",
                  "Freshness, volume, schema and business-rule checks",
                  "Named owners, severity levels and expected response",
                  "Lineage that answers 'where did this number come from'",
                ].map((item) => (
                  <li key={item} className="flex items-start gap-3 text-[0.9375rem] text-mist-300">
                    <svg viewBox="0 0 16 16" aria-hidden="true" className="mt-1 h-4 w-4 shrink-0 text-teal-400">
                      <path d="M3 8.4 6.3 11.7 13 5" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                    {item}
                  </li>
                ))}
              </ul>
              <ButtonLink href="/solutions/data-quality" variant="onDarkGhost" className="mt-8">
                Explore Data Quality
                <Arrow />
              </ButtonLink>
            </Reveal>
          </div>

          <Reveal delay={120} className="lg:col-span-7">
            <QualityDashboard />
            <p className="mt-4 text-[0.8125rem] leading-relaxed text-mist-500">
              Illustration of a data observability surface. The figures shown are examples of what
              such a dashboard displays — they are not measurements of DataForge or any client
              platform.
            </p>
          </Reveal>
        </div>
      </Container>
    </section>
  );
}

import { buildMetadata } from "@/lib/seo";
import { faqSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { Reveal } from "@/components/ui/reveal";
import { Hero } from "@/components/hero";
import { TrustBand } from "@/components/trust-band";
import { ServicesShowcase, PlatformArchitecture } from "@/components/services-showcase";
import { IndustriesGrid } from "@/components/industries-grid";
import { GlobalReachSection } from "@/components/global-reach-section";
import { DataQualitySection } from "@/components/data-quality-section";
import { TeamSetupSection } from "@/components/team-setup-section";
import { TrainingSection } from "@/components/training-section";
import { ProcessTimeline } from "@/components/process-timeline";
import { SignatureStatement } from "@/components/signature";
import { Principles } from "@/components/principles";
import { TechEcosystem } from "@/components/tech-ecosystem";
import { CtaSection } from "@/components/cta-section";
import { FaqAccordion } from "@/components/faq-accordion";
import { SolutionCard, InsightCard, CaseStudyCard } from "@/components/cards";
import { solutions } from "@/content/solutions";
import { insights } from "@/content/insights";
import { caseStudies } from "@/content/case-studies";
import { faqs } from "@/content/faqs";

export const metadata = buildMetadata({
  title: "Data Engineering Consulting & Data Platform Services",
  description:
    "DataForge Consulting designs, builds and modernizes data platforms, pipelines and engineering teams — data engineering, cloud data architecture, analytics engineering, data quality, training and team setup.",
  path: "/",
});

export default function HomePage() {
  const featuredInsights = insights.slice(0, 3);

  return (
    <>
      <Hero />
      <TrustBand />
      <ServicesShowcase />
      <PlatformArchitecture />
      <IndustriesGrid />
      <GlobalReachSection />
      <DataQualitySection />

      {/* Solutions */}
      <section className="border-y border-navy-950/8 bg-mist-50" aria-labelledby="solutions-heading">
        <Container className="py-20 sm:py-24 lg:py-28">
          <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">
            <SectionHeader
              eyebrow="Solutions"
              title="Solutions that move data forward."
              lede="Outcome-shaped engagements with defined capabilities, expected outcomes and a technology stack chosen for your constraints."
            />
            <Reveal delay={100}>
              <ButtonLink href="/solutions" variant="secondary">
                View all solutions
                <Arrow />
              </ButtonLink>
            </Reveal>
          </div>

          <ul className="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {solutions.slice(0, 6).map((solution, index) => (
              <Reveal as="li" key={solution.slug} delay={(index % 3) * 70}>
                <SolutionCard solution={solution} />
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      <TeamSetupSection />
      <TrainingSection />
      <ProcessTimeline />
      <SignatureStatement />

      {/* Case studies */}
      <section className="dark-section relative isolate overflow-hidden bg-navy-950 text-white" aria-labelledby="case-heading">
        <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-35" />
        <Container className="relative py-20 sm:py-24 lg:py-28">
          <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">
            <SectionHeader
              eyebrow="Case studies"
              tone="dark"
              title="Engagement patterns we're built for."
              lede="Named client stories are published only with client approval. Until then, these describe the shape of the problems DataForge solves — without invented names, figures or results."
            />
            <Reveal delay={100}>
              <ButtonLink href="/case-studies" variant="onDarkGhost">
                View all
                <Arrow />
              </ButtonLink>
            </Reveal>
          </div>

          <ul className="mt-14 grid gap-5 lg:grid-cols-3">
            {caseStudies.map((caseStudy, index) => (
              <Reveal as="li" key={caseStudy.slug} delay={index * 80}>
                <CaseStudyCard caseStudy={caseStudy} />
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      <Principles />
      <TechEcosystem />

      {/* Insights */}
      <section className="border-t border-navy-950/8 bg-mist-50" aria-labelledby="insights-heading">
        <Container className="py-20 sm:py-24 lg:py-28">
          <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">
            <SectionHeader
              eyebrow="Insights"
              title="Ideas for the modern data organization."
              lede="Practical writing on data engineering, architecture, cloud and the teams that build them."
            />
            <Reveal delay={100}>
              <ButtonLink href="/insights" variant="secondary">
                All insights
                <Arrow />
              </ButtonLink>
            </Reveal>
          </div>

          <ul className="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {featuredInsights.map((insight, index) => (
              <Reveal as="li" key={insight.slug} delay={index * 70}>
                <InsightCard insight={insight} />
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      {/* FAQ */}
      <section className="bg-white" aria-labelledby="faq-heading">
        <Container className="py-20 sm:py-24">
          <div className="grid gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-4">
              <SectionHeader eyebrow="FAQ" title="Questions we're asked most." />
            </div>
            <div className="lg:col-span-8">
              <FaqAccordion faqs={faqs} />
            </div>
          </div>
        </Container>
      </section>

      <CtaSection />
      <JsonLd data={faqSchema(faqs)} />
    </>
  );
}

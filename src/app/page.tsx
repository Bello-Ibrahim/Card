import Link from "next/link";
import { buildMetadata } from "@/lib/seo";
import { faqSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { Reveal } from "@/components/ui/reveal";
import { Hero } from "@/components/hero";
import { TrustStrip } from "@/components/trust-strip";
import { ServiceCard, SolutionCard, IndustryCard, InsightCard, CaseStudyCard } from "@/components/cards";
import { ApproachTimeline } from "@/components/approach-timeline";
import { WhyGraceWell } from "@/components/why-gracewell";
import { TechEcosystem } from "@/components/tech-ecosystem";
import { CtaSection } from "@/components/cta-section";
import { FaqAccordion } from "@/components/faq-accordion";
import { services } from "@/content/services";
import { solutions } from "@/content/solutions";
import { industries } from "@/content/industries";
import { insights } from "@/content/insights";
import { caseStudies } from "@/content/case-studies";
import { teamSetupModes } from "@/content/team-setup";
import { trainingTracks } from "@/content/training";
import { faqs } from "@/content/faqs";

export const metadata = buildMetadata({
  title: "Data Engineering Consulting & Data Platform Advisory",
  description:
    "GraceWell Consulting Group engineers the data foundations behind better decisions — data platform architecture, cloud data engineering, pipelines, analytics engineering, data quality, training and data engineering team setup.",
  path: "/",
});

export default function HomePage() {
  const featuredInsights = insights.slice(0, 3);

  return (
    <>
      <Hero />
      <TrustStrip />

      {/* Services */}
      <section className="bg-white" aria-labelledby="services-heading">
        <Container className="py-20 sm:py-24 lg:py-28">
          <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">
            <SectionHeader
              eyebrow="Services"
              title="From data strategy to production-grade engineering."
              lede="Nine capabilities that cover the full arc of a data programme — the advisory work that sets direction and the engineering work that makes it real."
            />
            <Reveal delay={100}>
              <ButtonLink href="/services" variant="secondary">
                View all services
                <Arrow />
              </ButtonLink>
            </Reveal>
          </div>

          <ul className="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {services.map((service, index) => (
              <Reveal as="li" key={service.slug} delay={(index % 3) * 70}>
                <ServiceCard service={service} />
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      {/* Solutions */}
      <section className="border-y border-navy-950/8 bg-mist-50" aria-labelledby="solutions-heading">
        <Container className="py-20 sm:py-24 lg:py-28">
          <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">
            <SectionHeader
              eyebrow="Solutions"
              title="Data solutions designed around your business."
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

      {/* Industries */}
      <section className="bg-white" aria-labelledby="industries-heading">
        <Container className="py-20 sm:py-24 lg:py-28">
          <SectionHeader
            eyebrow="Industries"
            title="Data expertise across data-intensive industries."
            lede="The engineering discipline is consistent. What changes is the regulatory context, the data shapes and the decisions the platform has to support."
          />
          <ul className="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {industries.slice(0, 6).map((industry, index) => (
              <Reveal as="li" key={industry.slug} delay={(index % 3) * 70}>
                <IndustryCard industry={industry} />
              </Reveal>
            ))}
          </ul>
          <Reveal delay={120}>
            <div className="mt-10">
              <ButtonLink href="/industries" variant="secondary">
                All industries
                <Arrow />
              </ButtonLink>
            </div>
          </Reveal>
        </Container>
      </section>

      <ApproachTimeline />

      {/* Team setup */}
      <section className="dark-section relative isolate overflow-hidden bg-navy-950 text-white" aria-labelledby="team-heading">
        <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-45" />
        <div
          aria-hidden="true"
          className="pointer-events-none absolute -left-24 bottom-[-20%] h-[30rem] w-[30rem] rounded-full bg-teal-500/12 blur-[130px]"
        />
        <Container className="relative py-20 sm:py-24 lg:py-28">
          <SectionHeader
            eyebrow="Team Setup"
            tone="dark"
            title="Build a high-performing data engineering team without starting from scratch."
            lede="Consulting capacity solves this quarter's problem. Capability solves the next five. We help organizations build, scale and enable data engineering teams of their own."
          />

          <ul className="mt-14 grid gap-5 lg:grid-cols-3">
            {teamSetupModes.map((mode, index) => (
              <Reveal as="li" key={mode.slug} delay={index * 80}>
                <article className="group/card flex h-full flex-col rounded-2xl border border-white/12 bg-white/[0.035] p-7 transition-[border-color,background-color,transform] duration-300 hover:-translate-y-0.5 hover:border-white/25 hover:bg-white/[0.07]">
                  <h3 className="text-[1.375rem] font-semibold tracking-[-0.02em] text-white">
                    {mode.title}
                  </h3>
                  <p className="mt-3 text-[0.9375rem] leading-relaxed text-mist-300">{mode.summary}</p>
                  <ul className="mt-6 flex-1 space-y-2 border-t border-white/10 pt-5">
                    {mode.includes.slice(0, 4).map((item) => (
                      <li key={item} className="flex items-start gap-2.5 text-[0.875rem] text-mist-400">
                        <span aria-hidden="true" className="mt-[0.45rem] h-1 w-1 shrink-0 rounded-full bg-accent-400" />
                        {item}
                      </li>
                    ))}
                  </ul>
                  <Link
                    href={`/team-setup#${mode.slug}`}
                    className="mt-7 inline-flex items-center gap-2 text-[0.875rem] font-medium text-white transition-colors hover:text-accent-300"
                  >
                    {mode.title} with GraceWell
                    <Arrow />
                  </Link>
                </article>
              </Reveal>
            ))}
          </ul>

          <Reveal delay={200}>
            <div className="mt-12">
              <ButtonLink href="/team-setup" size="lg" variant="onDark">
                Build Your Data Team
                <Arrow />
              </ButtonLink>
            </div>
          </Reveal>
        </Container>
      </section>

      {/* Training */}
      <section className="bg-white" aria-labelledby="training-heading">
        <Container className="py-20 sm:py-24 lg:py-28">
          <div className="grid gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-5">
              <SectionHeader
                eyebrow="Training"
                title="Develop the data engineering capability your organization needs."
                lede="GraceWell is both a consulting firm and a data engineering education partner. Programs run against your stack, taught by the engineers who build these systems."
              />
              <Reveal delay={140}>
                <div className="mt-9">
                  <ButtonLink href="/training">
                    Explore Training Programs
                    <Arrow />
                  </ButtonLink>
                </div>
              </Reveal>
            </div>

            <div className="lg:col-span-7">
              <ul className="divide-y divide-navy-950/8 border-y border-navy-950/8">
                {trainingTracks.map((track, index) => (
                  <Reveal as="li" key={track.slug} delay={index * 60}>
                    <Link
                      href={`/training#${track.slug}`}
                      className="group/card flex items-start gap-6 py-6 transition-colors hover:bg-mist-50"
                    >
                      <span className="mt-1 shrink-0 rounded-full border border-navy-950/10 px-2.5 py-1 text-[0.6875rem] font-medium uppercase tracking-[0.1em] text-mist-500">
                        {track.level}
                      </span>
                      <span className="flex-1">
                        <span className="block text-[1.0625rem] font-semibold tracking-[-0.02em] text-navy-950">
                          {track.title}
                        </span>
                        <span className="mt-1.5 block text-[0.9375rem] leading-relaxed text-mist-600">
                          {track.summary}
                        </span>
                      </span>
                      <Arrow className="mt-2 text-mist-500" />
                    </Link>
                  </Reveal>
                ))}
              </ul>
            </div>
          </div>
        </Container>
      </section>

      <WhyGraceWell />

      {/* Case studies */}
      <section className="dark-section relative isolate overflow-hidden bg-ink-950 text-white" aria-labelledby="case-heading">
        <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-35" />
        <Container className="relative py-20 sm:py-24 lg:py-28">
          <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">
            <SectionHeader
              eyebrow="Case Studies"
              tone="dark"
              title="Engagement patterns we're built for."
              lede="Named client stories are published only with client approval. Until then, these describe the shape of the problems GraceWell solves — without invented names, figures or results."
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

      <TechEcosystem />

      {/* Insights */}
      <section className="bg-white" aria-labelledby="insights-heading">
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
      <section className="border-t border-navy-950/8 bg-mist-50" aria-labelledby="faq-heading">
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

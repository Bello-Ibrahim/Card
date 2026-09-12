import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema, serviceSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { Photo } from "@/components/media/photo";
import { OrgChart } from "@/components/visuals/org-chart";
import { teamPillars, teamSetupModes } from "@/content/team-setup";

export const metadata = buildMetadata({
  title: "Data Engineering Team Setup",
  description:
    "Build, scale or enable a data engineering team: operating model, role design, hiring plans, engineering standards, onboarding, training, fractional technical leadership and team augmentation.",
  path: "/team-setup",
  keywords: [
    "data engineering team setup",
    "data engineering as a service",
    "data team augmentation",
    "fractional data engineering leadership",
  ],
});

export default function TeamSetupPage() {
  return (
    <>
      <PageHeader
        eyebrow="Team setup"
        title="Build the data team your business needs."
        lede="Consulting capacity solves this quarter's problem. Capability solves the next five. We help organizations build a data engineering function, scale an existing one, or develop the people they already have."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "Team Setup", path: "/team-setup" },
        ]}
        media={
          <Photo
            name="teamSetup"
            sizes="(min-width: 1024px) 40vw, 100vw"
            overlay="soft"
            className="relative aspect-[4/3] rounded-2xl border border-white/12"
          />
        }
      >
        <ButtonLink href="/contact?intent=team-setup" size="lg" variant="onDark">
          Build Your Data Team
          <Arrow />
        </ButtonLink>
      </PageHeader>

      <section className="bg-white">
        <Container className="py-20 sm:py-24">
          <SectionHeader
            eyebrow="What we cover"
            title="Six things a data function needs to get right."
            lede="Most organizations already have two or three of these. We work on the ones that are missing."
          />
          <ul className="mt-14 grid gap-px overflow-hidden rounded-2xl border border-navy-950/8 bg-navy-950/8 sm:grid-cols-2 lg:grid-cols-3">
            {teamPillars.map((pillar, index) => (
              <Reveal as="li" key={pillar.slug} delay={index * 60} className="bg-white p-7 lg:p-8">
                <h3 className="text-[1.0625rem] font-semibold tracking-[-0.02em] text-navy-950">
                  {pillar.title}
                </h3>
                <p className="mt-2 text-[0.9375rem] font-medium text-accent-700">{pillar.summary}</p>
                <ul className="mt-4 space-y-1.5">
                  {pillar.detail.map((item) => (
                    <li key={item} className="flex items-start gap-2 text-[0.8125rem] text-mist-500">
                      <span aria-hidden="true" className="mt-[0.4rem] h-1 w-1 shrink-0 rounded-full bg-accent-500" />
                      {item}
                    </li>
                  ))}
                </ul>
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      <section className="dark-section relative isolate overflow-hidden bg-navy-950 text-white">
        <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-40" />
        <Container className="relative py-20 sm:py-24">
          <div className="grid items-center gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-5">
              <SectionHeader
                eyebrow="Structure"
                tone="dark"
                title="What a complete data function looks like."
                lede="Not every organization needs every role on day one. The structure tells you what you are building towards, and the order to build it in."
              />
            </div>
            <Reveal delay={120} className="lg:col-span-7">
              <OrgChart />
            </Reveal>
          </div>
        </Container>
      </section>

      <section className="bg-white">
        <Container className="py-20 sm:py-24">
          <SectionHeader
            eyebrow="Three ways in"
            title="Build, Scale, Enable."
            lede="Most organizations need one of these clearly, and drift toward a second over time. The engagement is designed to move with you."
          />

          <div className="mt-14 space-y-5">
            {teamSetupModes.map((mode, index) => (
              <Reveal key={mode.slug} delay={index * 70}>
                <article
                  id={mode.slug}
                  className="scroll-mt-28 grid gap-8 rounded-2xl border border-navy-950/8 bg-white p-7 transition-[border-color,box-shadow] duration-300 hover:border-navy-950/16 hover:shadow-elevate lg:grid-cols-12 lg:gap-12 lg:p-9"
                >
                  <div className="lg:col-span-5">
                    <div className="flex items-baseline gap-3">
                      <span className="font-mono text-[0.75rem] font-medium tracking-[0.1em] text-accent-600">
                        0{index + 1}
                      </span>
                      <h3 className="text-[1.5rem] font-semibold tracking-[-0.025em] text-navy-950">
                        {mode.title}
                      </h3>
                    </div>
                    <p className="mt-4 text-[1rem] font-medium leading-snug text-navy-900">
                      {mode.summary}
                    </p>
                    <p className="mt-4 text-[0.9375rem] leading-relaxed text-mist-600">
                      {mode.description}
                    </p>
                    <p className="mt-5 border-t border-navy-950/8 pt-4 text-[0.875rem] text-mist-500">
                      <span className="font-medium text-navy-900">Best for:</span> {mode.bestFor}
                    </p>
                  </div>

                  <div className="lg:col-span-7">
                    <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                      What&apos;s included
                    </p>
                    <ul className="mt-5 grid gap-2.5 sm:grid-cols-2">
                      {mode.includes.map((item) => (
                        <li
                          key={item}
                          className="flex items-start gap-2.5 rounded-xl bg-mist-50 px-4 py-3 text-[0.875rem] text-navy-900"
                        >
                          <span aria-hidden="true" className="mt-[0.45rem] h-1.5 w-1.5 shrink-0 rounded-full bg-accent-500" />
                          {item}
                        </li>
                      ))}
                    </ul>
                    <ButtonLink
                      href={`/contact?intent=team-setup&mode=${mode.slug}`}
                      variant="secondary"
                      className="mt-6"
                    >
                      Discuss {mode.title}
                      <Arrow />
                    </ButtonLink>
                  </div>
                </article>
              </Reveal>
            ))}
          </div>
        </Container>
      </section>

      <CtaSection
        eyebrow="Team setup"
        title="Build Your Data Team"
        body="Tell us what your data function needs to look like in twelve months. We'll work back from there to the roles, standards and support required to get you to it."
        primary={{ label: "Build My Data Team", href: "/contact?intent=team-setup" }}
        secondary={{ label: "Explore Training", href: "/training" }}
      />

      <JsonLd
        data={[
          serviceSchema({
            name: "Data Engineering Team Setup",
            description:
              "Designing, building, scaling and enabling data engineering teams — operating model, role design, hiring plans, engineering standards, onboarding, training, fractional leadership and team augmentation.",
            path: "/team-setup",
            serviceType: "Organizational capability development",
          }),
          breadcrumbSchema([
            { name: "Home", path: "/" },
            { name: "Team Setup", path: "/team-setup" },
          ]),
        ]}
      />
    </>
  );
}

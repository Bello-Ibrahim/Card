import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema, serviceSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { teamSetupModes, teamSetupCapabilities } from "@/content/team-setup";
import { CoverBanner } from "@/components/visuals/cover-banner";

export const metadata = buildMetadata({
  title: "Data Engineering Team Setup",
  description:
    "Build, scale or enable a data engineering team: role definitions, team structure, hiring plans, engineering standards, onboarding, training, fractional technical leadership, team augmentation and dedicated squads.",
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
        eyebrow="Team Setup"
        title="Build a high-performing data engineering team without starting from scratch."
        lede="Consulting capacity solves this quarter's problem. Capability solves the next five. We help organizations build a data engineering function, scale an existing one, or develop the people they already have."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "Team Setup", path: "/team-setup" },
        ]}
        media={<CoverBanner seed="gracewell-team-setup" variant="tree" />}
      >
        <ButtonLink href="/contact?topic=team-setup" size="lg" variant="onDark">
          Build Your Data Team
          <Arrow />
        </ButtonLink>
      </PageHeader>

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
                      href={`/contact?topic=team-setup&mode=${mode.slug}`}
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

      <section className="dark-section relative isolate overflow-hidden border-t border-white/10 bg-navy-950 text-white">
        <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-40" />
        <Container className="relative py-20 sm:py-24">
          <div className="grid gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-5">
              <SectionHeader
                eyebrow="Capability"
                tone="dark"
                title="What we can take off your plate."
                lede="Some organizations need all of this. Most need four or five items and already have the rest covered."
              />
            </div>
            <div className="lg:col-span-7">
              <ul className="grid gap-x-8 gap-y-3.5 sm:grid-cols-2">
                {teamSetupCapabilities.map((capability, index) => (
                  <Reveal as="li" key={capability} delay={(index % 6) * 50}>
                    <span className="flex items-start gap-3 text-[0.9375rem] text-mist-300">
                      <svg viewBox="0 0 16 16" aria-hidden="true" className="mt-1 h-4 w-4 shrink-0 text-accent-400">
                        <path
                          d="M3 8.4 6.3 11.7 13 5"
                          fill="none"
                          stroke="currentColor"
                          strokeWidth="1.8"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        />
                      </svg>
                      {capability}
                    </span>
                  </Reveal>
                ))}
              </ul>
            </div>
          </div>
        </Container>
      </section>

      <CtaSection
        eyebrow="Team Setup"
        title="Build Your Data Team"
        body="Tell us what your data function needs to look like in twelve months. We'll work back from there to the roles, standards and support required to get you to it."
        primary={{ label: "Build Your Data Team", href: "/contact?topic=team-setup" }}
        secondary={{ label: "Explore Training", href: "/training" }}
      />

      <JsonLd
        data={[
          serviceSchema({
            name: "Data Engineering Team Setup",
            description:
              "Designing, building, scaling and enabling data engineering teams — role definitions, team structure, hiring plans, engineering standards, onboarding, training, fractional leadership and team augmentation.",
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

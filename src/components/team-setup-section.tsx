import Link from "next/link";
import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { Photo } from "@/components/media/photo";
import { OrgChart } from "@/components/visuals/org-chart";
import { teamPillars } from "@/content/team-setup";

export function TeamSetupSection() {
  return (
    <section className="dark-section relative isolate overflow-hidden bg-navy-950 text-white" aria-labelledby="team-heading">
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-40" />
      <Container className="relative py-20 sm:py-24 lg:py-28">
        <SectionHeader
          eyebrow="Team setup"
          tone="dark"
          title="Build the data team your business needs."
          lede="Consulting capacity solves this quarter's problem. Capability solves the next five. We help organizations design, hire, train and lead data engineering teams of their own."
        />

        <div className="mt-14 grid gap-10 lg:grid-cols-12 lg:gap-12">
          <div className="lg:col-span-6">
            <Photo
              name="teamSetup"
              sizes="(min-width: 1024px) 50vw, 100vw"
              zoomOnHover
              overlay="soft"
              className="relative aspect-[4/3] rounded-2xl border border-white/12"
            />
            <ul className="mt-6 grid gap-px overflow-hidden rounded-2xl border border-white/10 bg-white/10 sm:grid-cols-2">
              {teamPillars.map((pillar, index) => (
                <Reveal
                  as="li"
                  key={pillar.slug}
                  delay={index * 50}
                  className="bg-navy-950 p-5 transition-colors duration-300 hover:bg-navy-900"
                >
                  <h3 className="text-[0.9375rem] font-semibold text-white">{pillar.title}</h3>
                  <p className="mt-1.5 text-[0.8125rem] text-mist-400">{pillar.summary}</p>
                </Reveal>
              ))}
            </ul>
          </div>

          <div className="lg:col-span-6">
            <OrgChart />
            <Reveal delay={120}>
              <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                <ButtonLink href="/contact?intent=team-setup" size="lg" variant="onDark">
                  Build Your Data Team
                  <Arrow />
                </ButtonLink>
                <Link
                  href="/team-setup"
                  className="group/btn inline-flex h-[3.25rem] items-center justify-center gap-2 rounded-full border border-white/25 px-7 text-base font-medium text-white transition-colors hover:border-white/60 hover:bg-white/10"
                >
                  How it works
                  <Arrow />
                </Link>
              </div>
            </Reveal>
          </div>
        </div>
      </Container>
    </section>
  );
}

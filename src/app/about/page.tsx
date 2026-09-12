import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema, faqSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { Principles } from "@/components/principles";
import { ProcessTimeline } from "@/components/process-timeline";
import { GlobalReachSection } from "@/components/global-reach-section";
import { FaqAccordion } from "@/components/faq-accordion";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { Photo } from "@/components/media/photo";
import { faqs } from "@/content/faqs";
import { contact, site } from "@/content/site";

export const metadata = buildMetadata({
  title: "About DataForge Consulting",
  description:
    "DataForge Consulting is a data engineering and technology consulting firm. We design, build, modernize, operate and scale reliable data platforms — and build the engineering capability to run them.",
  path: "/about",
  keywords: ["data engineering company", "data engineering consulting firm", "data consultancy"],
});

export default function AboutPage() {
  return (
    <>
      <PageHeader
        eyebrow="About"
        title="We don't just talk about data. We build it."
        lede="DataForge Consulting is a data engineering and technology consulting firm. We design, build, modernize, operate and scale the data platforms organizations depend on — and build the internal capability to run them."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "About", path: "/about" },
        ]}
        media={
          <Photo
            name="about"
            sizes="(min-width: 1024px) 40vw, 100vw"
            overlay="soft"
            className="relative aspect-[4/3] rounded-2xl border border-white/12"
          />
        }
      >
        <div className="flex flex-col gap-3 sm:flex-row">
          <ButtonLink href="/contact" size="lg" variant="onDark">
            Talk to a Data Expert
            <Arrow />
          </ButtonLink>
          <ButtonLink href="/services" size="lg" variant="onDarkGhost">
            Explore Our Services
          </ButtonLink>
        </div>
      </PageHeader>

      <section className="bg-white">
        <Container className="py-20 sm:py-24">
          <div className="grid gap-14 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-7">
              <Reveal>
                <h2 className="text-subhead text-navy-950">What we do</h2>
                <div className="mt-6 space-y-5 text-[1.0625rem] leading-relaxed text-mist-600">
                  <p>
                    Organizations rarely lack data. What they lack is a foundation they can rely on —
                    pipelines that run predictably, definitions everyone agrees on, and a platform that
                    stays affordable as it grows. That foundation is engineering work, and it is what
                    DataForge does.
                  </p>
                  <p>
                    We span the full arc of a data programme: the advisory work that sets direction —
                    strategy, architecture, operating model, roadmap — and the delivery work that makes
                    it real, from ingestion and transformation through analytics enablement, quality and
                    governance. The same people do both, which is why our architecture tends to survive
                    contact with implementation.
                  </p>
                  <p>
                    We also do something many consultancies treat as an afterthought: we help
                    organizations build their own capability. Structured training, team design, hiring
                    support and mentoring are first-class parts of what we offer, because a platform
                    nobody internally can operate is a liability rather than an asset.
                  </p>
                </div>
              </Reveal>

              <Reveal delay={90}>
                <h2 className="text-subhead mt-14 text-navy-950">Who we work with</h2>
                <p className="mt-6 text-[1.0625rem] leading-relaxed text-mist-600">
                  Enterprises, financial institutions, fintechs, telecommunications companies,
                  healthcare organizations, retail and e-commerce businesses, logistics and
                  transportation operators, manufacturers, technology companies, government
                  organizations, and startups and scale-ups. The engagement model changes considerably
                  with scale and regulatory context. The engineering discipline does not.
                </p>
              </Reveal>
            </div>

            <div className="lg:col-span-5">
              <Reveal delay={120}>
                <div className="rounded-2xl border border-navy-950/8 bg-mist-50 p-8">
                  <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                    Our proposition
                  </p>
                  <p className="mt-5 text-[1.25rem] font-semibold leading-snug tracking-[-0.02em] text-navy-950">
                    We don&apos;t just recommend architecture. We engineer it — and we leave your team
                    able to operate what we built.
                  </p>
                  <ul className="mt-7 space-y-2.5 border-t border-navy-950/10 pt-6 text-[0.9375rem] text-mist-600">
                    {site.disciplines.map((item) => (
                      <li key={item} className="flex items-center gap-3">
                        <span aria-hidden="true" className="h-1.5 w-1.5 rounded-full bg-accent-500" />
                        {item}
                      </li>
                    ))}
                  </ul>
                </div>
              </Reveal>
            </div>
          </div>
        </Container>
      </section>

      <Principles />
      <GlobalReachSection />
      <ProcessTimeline />

      {/* Careers — describes what we look for; no fabricated openings are listed. */}
      <section id="careers" className="scroll-mt-28 border-t border-navy-950/8 bg-mist-50">
        <Container className="py-20 sm:py-24">
          <div className="grid gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-5">
              <SectionHeader
                eyebrow="Careers"
                title="Work on data foundations that matter."
                lede="We look for engineers who care about what happens after go-live."
              />
            </div>
            <div className="lg:col-span-7">
              <p className="text-[1.0625rem] leading-relaxed text-mist-600">
                The engineers who do well here write tests for pipelines nobody asked them to test,
                document a decision while they still remember why they made it, and can explain a
                trade-off to a finance director without condescension.
              </p>
              <ul className="mt-7 grid gap-2.5 sm:grid-cols-2">
                {[
                  "Data engineering",
                  "Analytics engineering",
                  "Platform and cloud engineering",
                  "Data architecture",
                  "Training and enablement",
                  "Technical delivery leadership",
                ].map((role) => (
                  <li
                    key={role}
                    className="flex items-start gap-2.5 rounded-xl bg-white px-4 py-3 text-[0.875rem] text-navy-900"
                  >
                    <span aria-hidden="true" className="mt-[0.45rem] h-1.5 w-1.5 shrink-0 rounded-full bg-accent-500" />
                    {role}
                  </li>
                ))}
              </ul>
              <p className="mt-6 text-[0.9375rem] leading-relaxed text-mist-500">
                Current openings are published here when we are hiring. Speculative applications from
                strong engineers are always welcome — send an introduction
                {contact.email ? (
                  <>
                    {" "}
                    to{" "}
                    <a href={`mailto:${contact.email}`} className="text-accent-600 underline underline-offset-4">
                      {contact.email}
                    </a>
                    .
                  </>
                ) : (
                  " through the contact form and mark it as a career enquiry."
                )}
              </p>
              <ButtonLink href="/contact?intent=careers" variant="secondary" className="mt-7">
                Introduce yourself
                <Arrow />
              </ButtonLink>
            </div>
          </div>
        </Container>
      </section>

      <section className="bg-white">
        <Container className="py-20 sm:py-24">
          <div className="grid gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-4">
              <SectionHeader eyebrow="FAQ" title="Common questions." />
            </div>
            <div className="lg:col-span-8">
              <FaqAccordion faqs={faqs} />
            </div>
          </div>
        </Container>
      </section>

      <CtaSection />
      <JsonLd
        data={[
          faqSchema(faqs),
          breadcrumbSchema([
            { name: "Home", path: "/" },
            { name: "About", path: "/about" },
          ]),
        ]}
      />
    </>
  );
}

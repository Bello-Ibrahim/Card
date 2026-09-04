import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema, faqSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { WhyGraceWell } from "@/components/why-gracewell";
import { ApproachTimeline } from "@/components/approach-timeline";
import { FaqAccordion } from "@/components/faq-accordion";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { faqs } from "@/content/faqs";
import { contact } from "@/content/site";

export const metadata = buildMetadata({
  title: "About GraceWell Consulting Group",
  description:
    "GraceWell Consulting Group is a data engineering consulting and technology advisory firm. We engineer the data foundations that power better business decisions — and help organizations build the capability to run them.",
  path: "/about",
  keywords: ["data engineering company", "data engineering consulting firm", "data consultancy"],
});

const commitments = [
  {
    title: "We say what we can evidence",
    body: "You will not find invented client logos, unverifiable statistics or borrowed credentials on this site. When we make a claim about a result, it will be one a client has agreed we can publish.",
  },
  {
    title: "We work in the open",
    body: "Architecture decisions are documented with their trade-offs. Code lives in your repositories. Runbooks are written as the system is built, not assembled at handover.",
  },
  {
    title: "We optimise for what you keep",
    body: "The measure of a good engagement is what remains once we leave: a platform your team understands, standards they can maintain, and documentation they trust.",
  },
];

export default function AboutPage() {
  return (
    <>
      <PageHeader
        eyebrow="About"
        title="We engineer the data foundations that power better business decisions."
        lede="GraceWell Consulting Group is a data engineering consulting and technology advisory firm. We help organizations design, build, modernize, operate and scale reliable data ecosystems — and build the internal capability to run them."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "About", path: "/about" },
        ]}
      >
        <div className="flex flex-col gap-3 sm:flex-row">
          <ButtonLink href="/contact" size="lg" variant="onDark">
            Talk to an Expert
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
                    GraceWell does.
                  </p>
                  <p>
                    We span the full arc of a data programme: the advisory work that sets direction —
                    strategy, architecture, operating model, roadmap — and the delivery work that makes
                    it real, from ingestion and transformation through analytics enablement, quality and
                    governance. The same people do both, which is why our architecture tends to survive
                    contact with implementation.
                  </p>
                  <p>
                    We also do something most consultancies treat as an afterthought: we help
                    organizations build their own capability. Structured training, team design, hiring
                    support and mentoring are first-class parts of what we offer, because a platform
                    nobody internally can operate is a liability, not an asset.
                  </p>
                </div>
              </Reveal>

              <Reveal delay={90}>
                <h2 className="text-subhead mt-14 text-navy-950">Who we work with</h2>
                <p className="mt-6 text-[1.0625rem] leading-relaxed text-mist-600">
                  We work with startups, growing companies, enterprises, government organizations,
                  financial institutions, healthcare organizations, telecoms, technology companies and
                  other data-intensive businesses. The engagement model changes considerably with scale
                  and regulatory context. The engineering discipline does not.
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
                    GraceWell doesn&apos;t simply advise organizations about data. We help them build the
                    systems, platforms, engineering teams and capabilities required to make data a
                    strategic advantage.
                  </p>
                  <ul className="mt-7 space-y-2.5 border-t border-navy-950/10 pt-6 text-[0.9375rem] text-mist-600">
                    {["Strategy", "Architecture", "Engineering", "Capability building"].map((item) => (
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

      <section className="border-t border-navy-950/8 bg-mist-50">
        <Container className="py-20 sm:py-24">
          <SectionHeader
            eyebrow="How we operate"
            title="Three commitments we hold ourselves to."
          />
          <ul className="mt-12 grid gap-5 lg:grid-cols-3">
            {commitments.map((commitment, index) => (
              <Reveal as="li" key={commitment.title} delay={index * 70}>
                <div className="h-full rounded-2xl border border-navy-950/8 bg-white p-7">
                  <h3 className="text-[1.0625rem] font-semibold tracking-[-0.02em] text-navy-950">
                    {commitment.title}
                  </h3>
                  <p className="mt-3 text-[0.9375rem] leading-relaxed text-mist-600">
                    {commitment.body}
                  </p>
                </div>
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      <WhyGraceWell />
      <ApproachTimeline />

      {/* Leadership — no profiles are published until GraceWell supplies verified details. */}
      <section id="leadership" className="scroll-mt-28 border-t border-navy-950/8 bg-mist-50">
        <Container className="py-20 sm:py-24">
          <div className="grid gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-5">
              <SectionHeader eyebrow="Leadership" title="Led by practitioners." />
            </div>
            <div className="lg:col-span-7">
              <p className="text-[1.0625rem] leading-relaxed text-mist-600">
                GraceWell is led by people who build data systems, not only advise on them. Engagements
                are shaped by engineers who have carried the consequences of their own architecture
                decisions — through migrations, incidents, audits and the unglamorous work of keeping a
                platform reliable after go-live.
              </p>
              <p className="mt-5 text-[0.9375rem] leading-relaxed text-mist-500">
                Individual leadership profiles will be published on this page. In the meantime, the
                fastest way to assess whether we are the right fit is a technical conversation about
                your architecture — which we are happy to have before any commercial discussion.
              </p>
              <ButtonLink href="/contact" variant="secondary" className="mt-7">
                Arrange a technical conversation
                <Arrow />
              </ButtonLink>
            </div>
          </div>
        </Container>
      </section>

      {/* Careers — describes what we look for; no fabricated openings are listed. */}
      <section id="careers" className="scroll-mt-28 bg-white">
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
                The engineers who do well here are the ones who write tests for pipelines nobody asked
                them to test, who document a decision while they still remember why they made it, and
                who can explain a trade-off to a finance director without condescension.
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
                    className="flex items-start gap-2.5 rounded-xl bg-mist-50 px-4 py-3 text-[0.875rem] text-navy-900"
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
                    to <a href={`mailto:${contact.email}`} className="text-accent-600 underline underline-offset-4">{contact.email}</a>.
                  </>
                ) : (
                  " through the contact form and mark the enquiry as a career enquiry."
                )}
              </p>
              <ButtonLink href="/contact?topic=careers" variant="secondary" className="mt-7">
                Introduce yourself
                <Arrow />
              </ButtonLink>
            </div>
          </div>
        </Container>
      </section>

      <section className="border-t border-navy-950/8 bg-mist-50">
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

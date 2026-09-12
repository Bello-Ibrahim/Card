import { notFound } from "next/navigation";
import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { Reveal } from "@/components/ui/reveal";
import { CaseStudyCard } from "@/components/cards";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { Photo } from "@/components/media/photo";
import { caseStudies, getCaseStudy } from "@/content/case-studies";

export function generateStaticParams() {
  return caseStudies.map((study) => ({ slug: study.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const study = getCaseStudy(slug);
  if (!study) return {};

  return buildMetadata({
    title: study.title,
    description: `${study.challenge} ${study.approach}`.slice(0, 155),
    path: `/case-studies/${study.slug}`,
  });
}

export default async function CaseStudyPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const study = getCaseStudy(slug);
  if (!study) notFound();

  const others = caseStudies.filter((item) => item.slug !== study.slug);
  const crumbs = [
    { name: "Home", path: "/" },
    { name: "Case Studies", path: "/case-studies" },
    { name: study.title, path: `/case-studies/${study.slug}` },
  ];

  return (
    <>
      <PageHeader
        eyebrow={study.verified ? "Case Study" : "Case Study · Illustrative"}
        title={study.title}
        lede={study.challenge}
        breadcrumbs={crumbs}
        media={
          <Photo
            name={study.photo}
            sizes="(min-width: 1024px) 40vw, 100vw"
            overlay="soft"
            className="relative aspect-[4/3] rounded-2xl border border-white/12"
          />
        }
      >
        <ButtonLink href="/contact" size="lg" variant="onDark">
          Discuss a similar engagement
          <Arrow />
        </ButtonLink>
      </PageHeader>

      <section className="bg-white">
        <Container className="py-20 sm:py-24">
          {!study.verified ? (
            <Reveal>
              <p className="mb-12 max-w-3xl rounded-2xl border border-amber-500/25 bg-amber-50 p-6 text-[0.875rem] leading-relaxed text-navy-900">
                <span className="font-semibold">Illustrative case study.</span> This describes a
                representative engagement pattern rather than a specific client project. No client name,
                metric or result is stated here, because none has been verified for publication.
              </p>
            </Reveal>
          ) : null}

          <div className="grid gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-8">
              <dl className="space-y-12">
                {(
                  [
                    ["Challenge", study.challenge],
                    ["Approach", study.approach],
                    ["Outcome", study.outcome],
                  ] as const
                ).map(([term, description], index) => (
                  <Reveal key={term} delay={index * 60}>
                    <div>
                      <dt className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                        {term}
                      </dt>
                      <dd className="mt-4 text-[1.0625rem] leading-[1.75] text-mist-600">{description}</dd>
                    </div>
                  </Reveal>
                ))}
              </dl>
            </div>

            <div className="lg:col-span-4">
              <Reveal delay={100}>
                <div className="sticky top-28 rounded-2xl border border-navy-950/8 bg-mist-50 p-7">
                  <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                    Sector
                  </p>
                  <p className="mt-2 text-[0.9375rem] text-navy-900">{study.sector}</p>

                  <p className="mt-6 text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                    Capabilities applied
                  </p>
                  <ul className="mt-4 flex flex-wrap gap-1.5">
                    {study.capabilities.map((capability) => (
                      <li
                        key={capability}
                        className="rounded-full border border-navy-950/8 bg-white px-3 py-1.5 text-[0.8125rem] text-mist-600"
                      >
                        {capability}
                      </li>
                    ))}
                  </ul>

                  <ButtonLink href="/contact" className="mt-7 w-full">
                    Talk to an Expert
                    <Arrow />
                  </ButtonLink>
                </div>
              </Reveal>
            </div>
          </div>
        </Container>
      </section>

      <section className="dark-section relative isolate overflow-hidden border-t border-white/10 bg-ink-950 text-white">
        <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-30" />
        <Container className="relative py-16 sm:py-20">
          <h2 className="text-subhead text-white">More case studies</h2>
          <ul className="mt-8 grid gap-5 lg:grid-cols-2">
            {others.map((item, index) => (
              <Reveal as="li" key={item.slug} delay={index * 70}>
                <CaseStudyCard caseStudy={item} />
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      <CtaSection />
      <JsonLd data={breadcrumbSchema(crumbs)} />
    </>
  );
}

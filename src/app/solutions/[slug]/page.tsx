import Link from "next/link";
import { notFound } from "next/navigation";
import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema, serviceSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { Reveal } from "@/components/ui/reveal";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { CoverBanner } from "@/components/visuals/cover-banner";
import { solutionVariant } from "@/components/visuals/variants";
import { solutions, getSolution } from "@/content/solutions";

export function generateStaticParams() {
  return solutions.map((solution) => ({ slug: solution.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const solution = getSolution(slug);
  if (!solution) return {};

  return buildMetadata({
    title: solution.title,
    description: solution.summary,
    path: `/solutions/${solution.slug}`,
    keywords: [solution.title.toLowerCase(), "data engineering consulting", ...solution.technologies.map((t) => t.toLowerCase())],
  });
}

export default async function SolutionDetailPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const solution = getSolution(slug);
  if (!solution) notFound();

  const related = solutions.filter((item) => item.slug !== solution.slug).slice(0, 3);
  const crumbs = [
    { name: "Home", path: "/" },
    { name: "Solutions", path: "/solutions" },
    { name: solution.title, path: `/solutions/${solution.slug}` },
  ];

  return (
    <>
      <PageHeader
        eyebrow="Solution"
        title={solution.title}
        lede={solution.summary}
        breadcrumbs={crumbs}
        media={<CoverBanner seed={solution.slug} variant={solutionVariant(solution.slug)} />}
      >
        <ButtonLink href="/contact" size="lg" variant="onDark">
          {solution.cta}
          <Arrow />
        </ButtonLink>
      </PageHeader>

      <section className="bg-white">
        <Container className="py-20 sm:py-24">
          <div className="grid gap-14 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-7">
              <Reveal>
                <h2 className="text-subhead text-navy-950">Overview</h2>
                <p className="mt-5 text-[1.0625rem] leading-relaxed text-mist-600">
                  {solution.description}
                </p>
              </Reveal>

              <Reveal delay={80}>
                <h2 className="text-subhead mt-14 text-navy-950">Capabilities</h2>
                <ul className="mt-6 grid gap-3 sm:grid-cols-2">
                  {solution.capabilities.map((capability) => (
                    <li
                      key={capability}
                      className="rounded-xl border border-navy-950/8 bg-mist-50 px-4 py-3 text-[0.9375rem] text-navy-900"
                    >
                      {capability}
                    </li>
                  ))}
                </ul>
              </Reveal>

              <Reveal delay={140}>
                <h2 className="text-subhead mt-14 text-navy-950">Key outcomes</h2>
                <ul className="mt-6 space-y-4">
                  {solution.outcomes.map((outcome) => (
                    <li key={outcome} className="flex items-start gap-3 text-[0.9375rem] leading-relaxed text-mist-600">
                      <svg viewBox="0 0 16 16" aria-hidden="true" className="mt-1 h-4 w-4 shrink-0 text-accent-500">
                        <path
                          d="M3 8.4 6.3 11.7 13 5"
                          fill="none"
                          stroke="currentColor"
                          strokeWidth="1.8"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        />
                      </svg>
                      {outcome}
                    </li>
                  ))}
                </ul>
              </Reveal>
            </div>

            <div className="lg:col-span-5">
              <Reveal delay={120}>
                <div className="sticky top-28 rounded-2xl border border-navy-950/8 bg-mist-50 p-7">
                  <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                    Technologies
                  </p>
                  <ul className="mt-4 flex flex-wrap gap-1.5">
                    {solution.technologies.map((tech) => (
                      <li
                        key={tech}
                        className="rounded-full border border-navy-950/8 bg-white px-3 py-1.5 text-[0.8125rem] text-mist-600"
                      >
                        {tech}
                      </li>
                    ))}
                  </ul>
                  <p className="mt-6 text-[0.875rem] leading-relaxed text-mist-600">
                    Stack selection follows your existing investment, team skills, compliance
                    requirements and cost constraints.
                  </p>
                  <ButtonLink href="/contact" className="mt-7 w-full">
                    {solution.cta}
                    <Arrow />
                  </ButtonLink>
                </div>
              </Reveal>
            </div>
          </div>
        </Container>
      </section>

      <section className="border-t border-navy-950/8 bg-mist-50">
        <Container className="py-16 sm:py-20">
          <h2 className="text-subhead text-navy-950">Related solutions</h2>
          <ul className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {related.map((item, index) => (
              <Reveal as="li" key={item.slug} delay={index * 70}>
                <Link
                  href={`/solutions/${item.slug}`}
                  className="group/card flex h-full flex-col rounded-2xl border border-navy-950/8 bg-white p-6 transition-[border-color,box-shadow,transform] duration-300 hover:-translate-y-0.5 hover:border-navy-950/16 hover:shadow-elevate"
                >
                  <span className="text-[1rem] font-semibold tracking-[-0.02em] text-navy-950">
                    {item.title}
                  </span>
                  <span className="mt-2.5 flex-1 text-[0.875rem] leading-relaxed text-mist-600">
                    {item.summary}
                  </span>
                  <span className="mt-5 inline-flex items-center gap-2 text-[0.875rem] font-medium text-navy-950 transition-colors group-hover/card:text-accent-600">
                    Explore
                    <Arrow />
                  </span>
                </Link>
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      <CtaSection />
      <JsonLd
        data={[
          serviceSchema({
            name: solution.title,
            description: solution.summary,
            path: `/solutions/${solution.slug}`,
            serviceType: "Data engineering solution",
          }),
          breadcrumbSchema(crumbs),
        ]}
      />
    </>
  );
}

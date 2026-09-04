import Link from "next/link";
import { notFound } from "next/navigation";
import { buildMetadata } from "@/lib/seo";
import { articleSchema, breadcrumbSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { Reveal } from "@/components/ui/reveal";
import { InsightCard } from "@/components/cards";
import { CtaSection } from "@/components/cta-section";
import { insights, getInsight } from "@/content/insights";
import { formatDate } from "@/lib/utils";

export function generateStaticParams() {
  return insights.map((insight) => ({ slug: insight.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const insight = getInsight(slug);
  if (!insight) return {};

  return buildMetadata({
    title: insight.title,
    description: insight.excerpt,
    path: `/insights/${insight.slug}`,
    type: "article",
    publishedTime: insight.publishedAt,
    section: insight.category,
  });
}

export default async function InsightPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const insight = getInsight(slug);
  if (!insight) notFound();

  const related = insights
    .filter((item) => item.slug !== insight.slug)
    .sort((a, b) => (a.category === insight.category ? -1 : 0) - (b.category === insight.category ? -1 : 0))
    .slice(0, 3);

  const crumbs = [
    { name: "Home", path: "/" },
    { name: "Insights", path: "/insights" },
    { name: insight.title, path: `/insights/${insight.slug}` },
  ];

  return (
    <>
      <PageHeader eyebrow={insight.category} title={insight.title} lede={insight.excerpt} breadcrumbs={crumbs}>
        <div className="flex flex-wrap items-center gap-x-4 gap-y-2 text-[0.875rem] text-mist-400">
          <time dateTime={insight.publishedAt}>{formatDate(insight.publishedAt)}</time>
          <span aria-hidden="true" className="h-1 w-1 rounded-full bg-mist-600" />
          <span>{insight.readingTime} min read</span>
        </div>
      </PageHeader>

      <article className="bg-white">
        <Container className="py-16 sm:py-20">
          <div className="grid gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-8">
              {insight.sections.map((section, index) => (
                <Reveal key={section.heading} delay={index === 0 ? 0 : 40}>
                  <section className={index > 0 ? "mt-12" : ""}>
                    <h2 className="text-subhead scroll-mt-28 text-navy-950">{section.heading}</h2>
                    {section.paragraphs.map((paragraph) => (
                      <p key={paragraph.slice(0, 40)} className="mt-5 text-[1.0625rem] leading-[1.75] text-mist-600">
                        {paragraph}
                      </p>
                    ))}
                    {section.bullets?.length ? (
                      <ul className="mt-6 space-y-2.5 rounded-2xl border border-navy-950/8 bg-mist-50 p-6">
                        {section.bullets.map((bullet) => (
                          <li key={bullet} className="flex items-start gap-3 text-[0.9375rem] text-navy-900">
                            <span aria-hidden="true" className="mt-[0.5rem] h-1.5 w-1.5 shrink-0 rounded-full bg-accent-500" />
                            {bullet}
                          </li>
                        ))}
                      </ul>
                    ) : null}
                  </section>
                </Reveal>
              ))}
            </div>

            <div className="lg:col-span-4">
              <div className="sticky top-28 space-y-6">
                <nav aria-label="On this page" className="rounded-2xl border border-navy-950/8 bg-mist-50 p-6">
                  <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                    On this page
                  </p>
                  <ul className="mt-4 space-y-2.5">
                    {insight.sections.map((section) => (
                      <li key={section.heading}>
                        <span className="block text-[0.875rem] leading-snug text-mist-600">
                          {section.heading}
                        </span>
                      </li>
                    ))}
                  </ul>
                </nav>

                <div className="rounded-2xl border border-navy-950/8 bg-white p-6">
                  <p className="text-[0.9375rem] font-medium leading-snug text-navy-950">
                    Working through this in your own organization?
                  </p>
                  <p className="mt-2 text-[0.875rem] leading-relaxed text-mist-600">
                    We&apos;re happy to have a technical conversation before any commercial one.
                  </p>
                  <Link
                    href="/contact"
                    className="mt-4 inline-flex items-center gap-2 text-[0.875rem] font-medium text-accent-600 hover:text-accent-700"
                  >
                    Talk to an expert →
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </Container>
      </article>

      <section className="border-t border-navy-950/8 bg-mist-50">
        <Container className="py-16 sm:py-20">
          <h2 className="text-subhead text-navy-950">Continue reading</h2>
          <ul className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {related.map((item, index) => (
              <Reveal as="li" key={item.slug} delay={index * 70}>
                <InsightCard insight={item} />
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      <CtaSection />
      <JsonLd data={[articleSchema(insight), breadcrumbSchema(crumbs)]} />
    </>
  );
}

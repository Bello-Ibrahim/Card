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
import { Icon, type IconName } from "@/components/ui/icon";
import { services, getService } from "@/content/services";

export function generateStaticParams() {
  return services.map((service) => ({ slug: service.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const service = getService(slug);
  if (!service) return {};

  return buildMetadata({
    title: service.title,
    description: service.summary,
    path: `/services/${service.slug}`,
    keywords: [service.title.toLowerCase(), "data engineering consulting", ...service.technologies.map((t) => t.toLowerCase())],
  });
}

export default async function ServiceDetailPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const service = getService(slug);
  if (!service) notFound();

  const related = services.filter((item) => item.slug !== service.slug).slice(0, 3);
  const crumbs = [
    { name: "Home", path: "/" },
    { name: "Services", path: "/services" },
    { name: service.title, path: `/services/${service.slug}` },
  ];

  return (
    <>
      <PageHeader eyebrow="Service" title={service.title} lede={service.summary} breadcrumbs={crumbs}>
        <ButtonLink href="/contact" size="lg" variant="onDark">
          Talk to an Expert
          <Arrow />
        </ButtonLink>
      </PageHeader>

      <section className="bg-white">
        <Container className="py-20 sm:py-24">
          <div className="grid gap-14 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-7">
              <Reveal>
                <span
                  aria-hidden="true"
                  className="inline-flex h-12 w-12 items-center justify-center rounded-xl bg-navy-950/[0.04] text-navy-800"
                >
                  <Icon name={service.icon as IconName} className="h-[1.375rem] w-[1.375rem]" />
                </span>
                <h2 className="text-subhead mt-6 text-navy-950">What this involves</h2>
                <p className="mt-5 text-[1.0625rem] leading-relaxed text-mist-600">{service.overview}</p>
              </Reveal>

              <Reveal delay={80}>
                <h2 className="text-subhead mt-14 text-navy-950">Capabilities</h2>
                <ul className="mt-6 grid gap-x-8 gap-y-3 sm:grid-cols-2">
                  {service.capabilities.map((capability) => (
                    <li key={capability} className="flex items-start gap-3 text-[0.9375rem] text-mist-600">
                      <span
                        aria-hidden="true"
                        className="mt-[0.5rem] h-1.5 w-1.5 shrink-0 rounded-full bg-accent-500"
                      />
                      {capability}
                    </li>
                  ))}
                </ul>
              </Reveal>
            </div>

            <div className="lg:col-span-5">
              <Reveal delay={120}>
                <div className="rounded-2xl border border-navy-950/8 bg-mist-50 p-7">
                  <h2 className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                    What you should expect
                  </h2>
                  <ul className="mt-5 space-y-4">
                    {service.outcomes.map((outcome) => (
                      <li key={outcome} className="flex items-start gap-3 text-[0.9375rem] leading-relaxed text-navy-900">
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

                  <h2 className="mt-8 text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                    Typical technologies
                  </h2>
                  <ul className="mt-4 flex flex-wrap gap-1.5">
                    {service.technologies.map((tech) => (
                      <li
                        key={tech}
                        className="rounded-full border border-navy-950/8 bg-white px-3 py-1.5 text-[0.8125rem] text-mist-600"
                      >
                        {tech}
                      </li>
                    ))}
                  </ul>

                  <ButtonLink href="/contact" className="mt-8 w-full">
                    Discuss {service.title}
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
          <h2 className="text-subhead text-navy-950">Related services</h2>
          <ul className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {related.map((item, index) => (
              <Reveal as="li" key={item.slug} delay={index * 70}>
                <Link
                  href={`/services/${item.slug}`}
                  className="group/card flex h-full flex-col rounded-2xl border border-navy-950/8 bg-white p-6 transition-[border-color,box-shadow,transform] duration-300 hover:-translate-y-0.5 hover:border-navy-950/16 hover:shadow-elevate"
                >
                  <span className="text-[1rem] font-semibold tracking-[-0.02em] text-navy-950">
                    {item.title}
                  </span>
                  <span className="mt-2.5 flex-1 text-[0.875rem] leading-relaxed text-mist-600">
                    {item.short}
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
            name: service.title,
            description: service.summary,
            path: `/services/${service.slug}`,
          }),
          breadcrumbSchema(crumbs),
        ]}
      />
    </>
  );
}

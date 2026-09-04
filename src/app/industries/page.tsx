import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { Reveal } from "@/components/ui/reveal";
import { IndustryCard } from "@/components/cards";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { industries } from "@/content/industries";

export const metadata = buildMetadata({
  title: "Industries",
  description:
    "Data engineering for financial services, fintech, telecommunications, healthcare, retail, manufacturing, logistics, technology, professional services, government, energy and education.",
  path: "/industries",
  keywords: ["data engineering consulting", "financial services data engineering", "healthcare data platform", "public sector data consulting"],
});

export default function IndustriesPage() {
  return (
    <>
      <PageHeader
        eyebrow="Industries"
        title="Data expertise across data-intensive industries."
        lede="The engineering discipline stays consistent. What changes is the regulatory context, the shape of the data, and the decisions the platform has to support."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "Industries", path: "/industries" },
        ]}
      >
        <ButtonLink href="/contact" size="lg" variant="onDark">
          Discuss your sector
          <Arrow />
        </ButtonLink>
      </PageHeader>

      <section className="bg-white" aria-labelledby="all-industries-heading">
        <Container className="py-20 sm:py-24">
          <h2 id="all-industries-heading" className="sr-only">
            Industries we work in
          </h2>
          <ul className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {industries.map((industry, index) => (
              <Reveal as="li" key={industry.slug} delay={(index % 3) * 60} className="scroll-mt-28" >
                <div id={industry.slug} className="h-full">
                  <IndustryCard industry={industry} />
                </div>
              </Reveal>
            ))}
          </ul>

          <Reveal>
            <p className="mt-12 max-w-3xl text-[0.9375rem] leading-relaxed text-mist-500">
              Working in a sector that isn&apos;t listed? The underlying problems — fragmented systems,
              unreliable pipelines, unclear ownership, expensive platforms — are remarkably consistent.
              Tell us what you&apos;re dealing with and we&apos;ll say plainly whether we can help.
            </p>
          </Reveal>
        </Container>
      </section>

      <CtaSection
        eyebrow="Sector conversations"
        title="Every industry has its own definition of 'correct'."
        body="Regulatory reporting, clinical safety, revenue assurance, settlement accuracy — the constraint that shapes the architecture is usually specific to your sector. That is where the conversation should start."
      />

      <JsonLd
        data={breadcrumbSchema([
          { name: "Home", path: "/" },
          { name: "Industries", path: "/industries" },
        ])}
      />
    </>
  );
}

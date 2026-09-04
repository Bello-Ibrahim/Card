import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { Reveal } from "@/components/ui/reveal";
import { ServiceCard } from "@/components/cards";
import { ApproachTimeline } from "@/components/approach-timeline";
import { TechEcosystem } from "@/components/tech-ecosystem";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { services } from "@/content/services";

export const metadata = buildMetadata({
  title: "Data Engineering Services",
  description:
    "Data engineering, platform architecture, cloud data engineering, warehousing and lakehouses, integration, migration, analytics engineering, data quality and data strategy advisory from GraceWell Consulting Group.",
  path: "/services",
  keywords: [
    "data engineering services",
    "data engineering consulting",
    "data architecture consulting",
    "cloud data engineering",
    "analytics engineering",
  ],
});

export default function ServicesPage() {
  return (
    <>
      <PageHeader
        eyebrow="Services"
        title="From data strategy to production-grade engineering."
        lede="Advisory work that sets direction, and engineering work that makes it real — delivered by the same team, so the architecture that gets designed is the architecture that gets built."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "Services", path: "/services" },
        ]}
      >
        <div className="flex flex-col gap-3 sm:flex-row">
          <ButtonLink href="/contact" size="lg" variant="onDark">
            Talk to an Expert
            <Arrow />
          </ButtonLink>
          <ButtonLink href="/solutions" size="lg" variant="onDarkGhost">
            See Solutions
          </ButtonLink>
        </div>
      </PageHeader>

      <section className="bg-white" aria-labelledby="all-services-heading">
        <Container className="py-20 sm:py-24">
          <h2 id="all-services-heading" className="sr-only">
            All services
          </h2>
          <ul className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {services.map((service, index) => (
              <Reveal as="li" key={service.slug} delay={(index % 3) * 70}>
                <ServiceCard service={service} />
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      <ApproachTimeline />
      <TechEcosystem tone="dark" />
      <CtaSection
        title="Not sure which service you need?"
        body="Most engagements start with a short conversation about the outcome you're after. We'll tell you plainly whether it's an architecture review, a delivery engagement or a capability problem."
      />

      <JsonLd
        data={breadcrumbSchema([
          { name: "Home", path: "/" },
          { name: "Services", path: "/services" },
        ])}
      />
    </>
  );
}

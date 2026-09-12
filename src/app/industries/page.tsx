import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { PageHeader } from "@/components/page-header";
import { IndustriesGrid } from "@/components/industries-grid";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";

export const metadata = buildMetadata({
  title: "Industries",
  description:
    "Data engineering for financial services, telecommunications, healthcare, retail and e-commerce, logistics, manufacturing, government and technology companies.",
  path: "/industries",
  keywords: [
    "data engineering consulting",
    "financial services data engineering",
    "telecom data platform",
    "healthcare data engineering",
    "public sector data consulting",
  ],
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

      <IndustriesGrid />

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

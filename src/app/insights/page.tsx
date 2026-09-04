import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { InsightsExplorer } from "@/components/insights-explorer";
import { CtaSection } from "@/components/cta-section";
import { insights } from "@/content/insights";

export const metadata = buildMetadata({
  title: "Insights",
  description:
    "Practical writing on data engineering, data architecture, cloud data platforms, data strategy, analytics, AI data foundations, engineering leadership and data engineering careers.",
  path: "/insights",
  keywords: ["data engineering blog", "data architecture insights", "modern data platform", "etl vs elt", "lakehouse"],
});

export default function InsightsPage() {
  const ordered = [...insights].sort((a, b) => b.publishedAt.localeCompare(a.publishedAt));

  return (
    <>
      <PageHeader
        eyebrow="Insights"
        title="Ideas for the modern data organization."
        lede="Writing from the engineers doing the work — on architecture decisions, delivery practice, cloud economics and the teams that build data platforms."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "Insights", path: "/insights" },
        ]}
      />

      <section className="bg-white" aria-labelledby="all-insights-heading">
        <Container className="py-16 sm:py-20">
          <h2 id="all-insights-heading" className="sr-only">
            All insights
          </h2>
          <InsightsExplorer insights={ordered} />
        </Container>
      </section>

      <CtaSection
        eyebrow="Stay in touch"
        title="Want these in your inbox?"
        body="We publish occasionally and only when we have something useful to say. Tell us you'd like to hear from us and we'll add you to the list."
        primary={{ label: "Join the list", href: "/contact?topic=newsletter" }}
        secondary={{ label: "Talk to an Expert", href: "/contact" }}
      />

      <JsonLd
        data={breadcrumbSchema([
          { name: "Home", path: "/" },
          { name: "Insights", path: "/insights" },
        ])}
      />
    </>
  );
}

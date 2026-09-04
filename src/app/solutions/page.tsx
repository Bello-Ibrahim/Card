import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { Reveal } from "@/components/ui/reveal";
import { SolutionCard } from "@/components/cards";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { solutions } from "@/content/solutions";

export const metadata = buildMetadata({
  title: "Data Solutions",
  description:
    "Modern data platforms, enterprise data warehouses, lakehouses, real-time data, migration, integration, quality, governance, analytics engineering, AI data foundations, optimization and managed data engineering.",
  path: "/solutions",
  keywords: [
    "data platform consulting",
    "data warehouse consulting",
    "lakehouse consulting",
    "data modernization consulting",
    "managed data engineering",
  ],
});

const categories = ["Platform", "Data Management", "Enablement"] as const;

export default function SolutionsPage() {
  return (
    <>
      <PageHeader
        eyebrow="Solutions"
        title="Data solutions designed around your business."
        lede="Each solution states what it includes, what you should expect from it, and the technologies typically involved — so the conversation starts with substance rather than a brochure."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "Solutions", path: "/solutions" },
        ]}
      >
        <ButtonLink href="/contact" size="lg" variant="onDark">
          Talk to an Expert
          <Arrow />
        </ButtonLink>
      </PageHeader>

      <section className="bg-white">
        <Container className="py-20 sm:py-24">
          {categories.map((category, groupIndex) => {
            const group = solutions.filter((solution) => solution.category === category);
            if (!group.length) return null;
            return (
              <div key={category} className={groupIndex > 0 ? "mt-20" : ""}>
                <div className="flex items-center gap-4">
                  <h2 className="text-subhead text-navy-950">{category}</h2>
                  <span aria-hidden="true" className="h-px flex-1 bg-navy-950/10" />
                  <span className="text-[0.8125rem] text-mist-500">
                    {group.length} {group.length === 1 ? "solution" : "solutions"}
                  </span>
                </div>
                <ul className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
                  {group.map((solution, index) => (
                    <Reveal as="li" key={solution.slug} delay={(index % 3) * 70}>
                      <SolutionCard solution={solution} />
                    </Reveal>
                  ))}
                </ul>
              </div>
            );
          })}
        </Container>
      </section>

      <CtaSection
        title="Tell us the outcome. We'll shape the engagement."
        body="Most organizations arrive with a symptom rather than a solution name — slow reporting, an unreliable pipeline, a migration that has stalled. That is a perfectly good place to start."
      />

      <JsonLd
        data={breadcrumbSchema([
          { name: "Home", path: "/" },
          { name: "Solutions", path: "/solutions" },
        ])}
      />
    </>
  );
}

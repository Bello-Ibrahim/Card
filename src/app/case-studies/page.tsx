import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { Reveal } from "@/components/ui/reveal";
import { CaseStudyCard } from "@/components/cards";
import { CtaSection } from "@/components/cta-section";
import { caseStudies } from "@/content/case-studies";

export const metadata = buildMetadata({
  title: "Case Studies",
  description:
    "Engagement patterns from GraceWell Consulting Group: modernizing enterprise data platforms, migrating legacy data warehouses and building internal data engineering teams.",
  path: "/case-studies",
});

export default function CaseStudiesPage() {
  const unverified = caseStudies.some((study) => !study.verified);

  return (
    <>
      <PageHeader
        eyebrow="Case Studies"
        title="Engagement patterns we're built for."
        lede="Named client stories are published only with client approval. Until then, these describe the shape of the problems GraceWell solves — without invented names, figures or results."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "Case Studies", path: "/case-studies" },
        ]}
      />

      <section className="dark-section relative isolate overflow-hidden bg-ink-950 text-white">
        <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-35" />
        <Container className="relative py-20 sm:py-24">
          <h2 className="sr-only">All case studies</h2>
          <ul className="grid gap-5 lg:grid-cols-3">
            {caseStudies.map((study, index) => (
              <Reveal as="li" key={study.slug} delay={index * 80}>
                <CaseStudyCard caseStudy={study} />
              </Reveal>
            ))}
          </ul>

          {unverified ? (
            <p className="mt-12 max-w-3xl rounded-2xl border border-white/12 bg-white/[0.03] p-6 text-[0.875rem] leading-relaxed text-mist-400">
              <span className="font-medium text-white">A note on these case studies.</span> Entries marked
              &ldquo;illustrative&rdquo; describe representative engagement patterns rather than a specific
              client project. They contain no client names, metrics or outcomes we cannot evidence.
              Client-approved case studies are published here as they become available.
            </p>
          ) : null}
        </Container>
      </section>

      <CtaSection
        title="Recognise your situation in one of these?"
        body="Most organizations arrive describing a symptom rather than a project. That is a perfectly good place to start — tell us what is going wrong and we'll tell you plainly what we think it will take."
      />

      <JsonLd
        data={breadcrumbSchema([
          { name: "Home", path: "/" },
          { name: "Case Studies", path: "/case-studies" },
        ])}
      />
    </>
  );
}

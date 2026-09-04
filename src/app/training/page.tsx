import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema, serviceSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { CtaSection } from "@/components/cta-section";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { trainingTracks, trainingPrinciples } from "@/content/training";

export const metadata = buildMetadata({
  title: "Data Engineering Training",
  description:
    "Data engineering training from GraceWell Consulting Group: fundamentals, the modern data stack, advanced data engineering, cloud data engineering on AWS, Azure and Google Cloud, and customized corporate programs.",
  path: "/training",
  keywords: [
    "data engineering training",
    "corporate data training",
    "dbt training",
    "airflow training",
    "cloud data engineering training",
  ],
});

export default function TrainingPage() {
  return (
    <>
      <PageHeader
        eyebrow="Training"
        title="Develop the data engineering capability your organization needs."
        lede="GraceWell is both a consulting firm and a data engineering education and workforce development partner. Programs are taught by practising engineers, against the stack your teams actually use."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "Training", path: "/training" },
        ]}
      >
        <div className="flex flex-col gap-3 sm:flex-row">
          <ButtonLink href="/contact?topic=training" size="lg" variant="onDark">
            Explore Training Programs
            <Arrow />
          </ButtonLink>
          <ButtonLink href="/team-setup" size="lg" variant="onDarkGhost">
            Team Setup
          </ButtonLink>
        </div>
      </PageHeader>

      <section className="bg-white">
        <Container className="py-20 sm:py-24">
          <SectionHeader
            eyebrow="Programs"
            title="Four tracks, plus fully customized corporate programs."
            lede="Tracks can run standalone or as a sequence, and are commonly paired with mentoring on live delivery work — which is where new skills usually take hold."
          />

          <div className="mt-14 space-y-5">
            {trainingTracks.map((track, index) => (
              <Reveal key={track.slug} delay={index * 60}>
                <article
                  id={track.slug}
                  className="scroll-mt-28 rounded-2xl border border-navy-950/8 bg-white p-7 transition-[border-color,box-shadow] duration-300 hover:border-navy-950/16 hover:shadow-elevate lg:p-9"
                >
                  <div className="grid gap-8 lg:grid-cols-12 lg:gap-10">
                    <div className="lg:col-span-5">
                      <span className="inline-block rounded-full border border-navy-950/10 bg-mist-50 px-2.5 py-1 text-[0.6875rem] font-medium uppercase tracking-[0.1em] text-mist-500">
                        {track.level}
                      </span>
                      <h3 className="mt-4 text-[1.375rem] font-semibold tracking-[-0.02em] text-navy-950">
                        {track.title}
                      </h3>
                      <p className="mt-3 text-[0.9375rem] leading-relaxed text-mist-600">
                        {track.summary}
                      </p>
                      <dl className="mt-6 space-y-3 border-t border-navy-950/8 pt-5 text-[0.875rem]">
                        <div>
                          <dt className="font-medium text-navy-900">Who it&apos;s for</dt>
                          <dd className="mt-0.5 text-mist-600">{track.audience}</dd>
                        </div>
                        <div>
                          <dt className="font-medium text-navy-900">Format</dt>
                          <dd className="mt-0.5 text-mist-600">{track.format}</dd>
                        </div>
                      </dl>
                    </div>

                    <div className="lg:col-span-7">
                      <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                        Modules
                      </p>
                      <ul className="mt-5 grid gap-2.5 sm:grid-cols-2">
                        {track.modules.map((module) => (
                          <li
                            key={module}
                            className="flex items-start gap-2.5 rounded-xl bg-mist-50 px-4 py-3 text-[0.875rem] text-navy-900"
                          >
                            <span aria-hidden="true" className="mt-[0.45rem] h-1.5 w-1.5 shrink-0 rounded-full bg-accent-500" />
                            {module}
                          </li>
                        ))}
                      </ul>
                      <ButtonLink
                        href={`/contact?topic=training&program=${track.slug}`}
                        variant="secondary"
                        className="mt-6"
                      >
                        Enquire about this program
                        <Arrow />
                      </ButtonLink>
                    </div>
                  </div>
                </article>
              </Reveal>
            ))}
          </div>
        </Container>
      </section>

      <section className="border-t border-navy-950/8 bg-mist-50">
        <Container className="py-20 sm:py-24">
          <SectionHeader
            eyebrow="How we teach"
            title="Training designed to change what people can build."
            lede="Attendance is easy to measure and tells you very little. These four principles are what make a program show up in the work afterwards."
          />
          <ul className="mt-12 grid gap-5 sm:grid-cols-2">
            {trainingPrinciples.map((principle, index) => (
              <Reveal as="li" key={principle.title} delay={index * 70}>
                <div className="h-full rounded-2xl border border-navy-950/8 bg-white p-7">
                  <h3 className="text-[1.0625rem] font-semibold tracking-[-0.02em] text-navy-950">
                    {principle.title}
                  </h3>
                  <p className="mt-3 text-[0.9375rem] leading-relaxed text-mist-600">{principle.body}</p>
                </div>
              </Reveal>
            ))}
          </ul>
        </Container>
      </section>

      <CtaSection
        eyebrow="Training"
        title="Tell us what your team needs to be able to build."
        body="We'll assess where they are, design a program against your stack and objectives, and pair it with mentoring so the capability holds after the last session."
        primary={{ label: "Explore Training Programs", href: "/contact?topic=training" }}
        secondary={{ label: "Talk to an Expert", href: "/contact" }}
      />

      <JsonLd
        data={[
          serviceSchema({
            name: "Data Engineering Training",
            description:
              "Instructor-led data engineering training covering fundamentals, the modern data stack, advanced data engineering, cloud data engineering and customized corporate programs.",
            path: "/training",
            serviceType: "Professional training",
          }),
          breadcrumbSchema([
            { name: "Home", path: "/" },
            { name: "Training", path: "/training" },
          ]),
        ]}
      />
    </>
  );
}

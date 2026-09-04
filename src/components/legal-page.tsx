import Link from "next/link";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { contact } from "@/content/site";

export type LegalSection = { heading: string; paragraphs: string[]; bullets?: string[] };

/**
 * Shared layout for policy pages.
 *
 * NOTE FOR GRACEWELL: these policies describe how this website actually behaves and are
 * written to be accurate rather than boilerplate. They should still be reviewed by your
 * legal counsel, and updated whenever analytics, marketing tooling or third-party
 * embeds are added to the site.
 */
export function LegalPage({
  title,
  lede,
  updated,
  sections,
  path,
}: {
  title: string;
  lede: string;
  updated: string;
  sections: LegalSection[];
  path: string;
}) {
  return (
    <>
      <PageHeader
        eyebrow="Legal"
        title={title}
        lede={lede}
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: title, path },
        ]}
      />

      <section className="bg-white">
        <Container className="py-16 sm:py-20">
          <div className="grid gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-4">
              <div className="lg:sticky lg:top-28">
                <p className="text-[0.8125rem] text-mist-500">Last updated {updated}</p>
                <nav aria-label="Contents" className="mt-6 rounded-2xl border border-navy-950/8 bg-mist-50 p-6">
                  <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                    Contents
                  </p>
                  <ol className="mt-4 space-y-2.5">
                    {sections.map((section, index) => (
                      <li key={section.heading} className="text-[0.875rem] leading-snug text-mist-600">
                        <span className="mr-2 font-mono text-[0.75rem] text-mist-500">
                          {String(index + 1).padStart(2, "0")}
                        </span>
                        {section.heading}
                      </li>
                    ))}
                  </ol>
                </nav>
              </div>
            </div>

            <div className="lg:col-span-8">
              {sections.map((section, index) => (
                <section key={section.heading} className={index > 0 ? "mt-10" : ""}>
                  <h2 className="text-[1.25rem] font-semibold tracking-[-0.02em] text-navy-950">
                    {index + 1}. {section.heading}
                  </h2>
                  {section.paragraphs.map((paragraph) => (
                    <p key={paragraph.slice(0, 40)} className="mt-4 text-[0.9375rem] leading-[1.75] text-mist-600">
                      {paragraph}
                    </p>
                  ))}
                  {section.bullets?.length ? (
                    <ul className="mt-4 space-y-2">
                      {section.bullets.map((bullet) => (
                        <li key={bullet} className="flex items-start gap-3 text-[0.9375rem] leading-relaxed text-mist-600">
                          <span aria-hidden="true" className="mt-[0.55rem] h-1.5 w-1.5 shrink-0 rounded-full bg-accent-500" />
                          {bullet}
                        </li>
                      ))}
                    </ul>
                  ) : null}
                </section>
              ))}

              <div className="mt-12 rounded-2xl border border-navy-950/8 bg-mist-50 p-7">
                <h2 className="text-[1.0625rem] font-semibold tracking-[-0.02em] text-navy-950">
                  Questions about this policy
                </h2>
                <p className="mt-3 text-[0.9375rem] leading-relaxed text-mist-600">
                  {contact.email ? (
                    <>
                      Contact us at{" "}
                      <a href={`mailto:${contact.email}`} className="text-accent-600 underline underline-offset-4">
                        {contact.email}
                      </a>
                      .
                    </>
                  ) : (
                    <>
                      Please reach us through the{" "}
                      <Link href="/contact" className="text-accent-600 underline underline-offset-4">
                        contact form
                      </Link>
                      , and we will respond directly.
                    </>
                  )}
                </p>
              </div>
            </div>
          </div>
        </Container>
      </section>
    </>
  );
}

import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Suspense } from "react";
import { Container } from "@/components/ui/container";
import { PageHeader } from "@/components/page-header";
import { Reveal } from "@/components/ui/reveal";
import { ContactForm } from "@/components/contact-form";
import { contact, hasDirectContactChannels } from "@/content/site";

export const metadata = buildMetadata({
  title: "Contact",
  description:
    "Talk to GraceWell Consulting Group about data engineering, data platforms, cloud data, migration, analytics engineering, training, team setup or an architecture review.",
  path: "/contact",
  keywords: ["data engineering consulting contact", "talk to a data engineering expert"],
});

const helpTopics = [
  {
    title: "Start a project",
    body: "A platform build, a migration, a pipeline that needs to become reliable, or an integration programme.",
  },
  {
    title: "Get an expert opinion",
    body: "An architecture review, a second opinion on a technology decision, or a data maturity assessment.",
  },
  {
    title: "Develop your people",
    body: "Structured training, mentoring, or help designing and building a data engineering team.",
  },
];

export default function ContactPage() {
  return (
    <>
      <PageHeader
        eyebrow="Contact"
        title="Let's talk about your data."
        lede="Tell us what you're trying to achieve and what's currently in the way. We'll respond with a straight answer about whether — and how — we can help."
        breadcrumbs={[
          { name: "Home", path: "/" },
          { name: "Contact", path: "/contact" },
        ]}
      />

      <section className="bg-white">
        <Container className="py-16 sm:py-20 lg:py-24">
          <div className="grid gap-14 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-7">
              <Reveal>
                <h2 className="text-subhead text-navy-950">Send an inquiry</h2>
                <p className="mt-3 max-w-xl text-[0.9375rem] leading-relaxed text-mist-600">
                  The more context you can give us, the more useful our first reply will be.
                </p>
                <div className="mt-10">
                  <Suspense fallback={<div className="h-[42rem] rounded-2xl bg-mist-50" />}>
                    <ContactForm />
                  </Suspense>
                </div>
              </Reveal>
            </div>

            <div className="lg:col-span-5">
              <Reveal delay={100}>
                <div className="rounded-2xl border border-navy-950/8 bg-mist-50 p-7 lg:sticky lg:top-28">
                  <h2 className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                    What people contact us about
                  </h2>
                  <ul className="mt-6 space-y-6">
                    {helpTopics.map((topic) => (
                      <li key={topic.title}>
                        <p className="text-[0.9375rem] font-semibold text-navy-950">{topic.title}</p>
                        <p className="mt-1.5 text-[0.875rem] leading-relaxed text-mist-600">
                          {topic.body}
                        </p>
                      </li>
                    ))}
                  </ul>

                  <div className="mt-8 border-t border-navy-950/10 pt-6">
                    <h2 className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                      Direct channels
                    </h2>
                    {hasDirectContactChannels ? (
                      <ul className="mt-4 space-y-2.5 text-[0.9375rem]">
                        {contact.email ? (
                          <li>
                            <a
                              href={`mailto:${contact.email}`}
                              className="text-navy-900 underline decoration-navy-950/20 underline-offset-4 hover:text-accent-600"
                            >
                              {contact.email}
                            </a>
                          </li>
                        ) : null}
                        {contact.phone ? (
                          <li>
                            <a
                              href={`tel:${contact.phone.replace(/[^+\d]/g, "")}`}
                              className="text-navy-900 underline decoration-navy-950/20 underline-offset-4 hover:text-accent-600"
                            >
                              {contact.phone}
                            </a>
                          </li>
                        ) : null}
                        {contact.linkedin ? (
                          <li>
                            <a
                              href={contact.linkedin}
                              target="_blank"
                              rel="noreferrer noopener"
                              className="text-navy-900 underline decoration-navy-950/20 underline-offset-4 hover:text-accent-600"
                            >
                              LinkedIn
                            </a>
                          </li>
                        ) : null}
                        {contact.location ? (
                          <li className="text-mist-600">{contact.location}</li>
                        ) : null}
                      </ul>
                    ) : (
                      <p className="mt-4 text-[0.875rem] leading-relaxed text-mist-600">
                        Our published email address and social channels are being finalised. Until they
                        are listed here, the form is the fastest way to reach the team — every enquiry
                        goes directly to us.
                      </p>
                    )}
                  </div>
                </div>
              </Reveal>
            </div>
          </div>
        </Container>
      </section>

      <JsonLd
        data={breadcrumbSchema([
          { name: "Home", path: "/" },
          { name: "Contact", path: "/contact" },
        ])}
      />
    </>
  );
}

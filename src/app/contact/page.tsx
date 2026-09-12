import { Suspense } from "react";
import { buildMetadata } from "@/lib/seo";
import { breadcrumbSchema } from "@/lib/schema";
import { JsonLd } from "@/components/ui/json-ld";
import { Container } from "@/components/ui/container";
import { Reveal } from "@/components/ui/reveal";
import { ContactForm } from "@/components/contact-form";
import { Photo } from "@/components/media/photo";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { contact, hasDirectContactChannels } from "@/content/site";

export const metadata = buildMetadata({
  title: "Contact",
  description:
    "Talk to DataForge Consulting about data engineering, data platforms, cloud, migration, analytics engineering, training, team setup or an architecture review.",
  path: "/contact",
  keywords: ["data engineering consulting contact", "talk to a data expert"],
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
      {/* Split layout: a real engineering environment on the left, the form on the right. */}
      <section className="dark-section relative bg-ink-950 pt-[4.5rem] lg:pt-20">
        <div className="lg:grid lg:grid-cols-12">
          <div className="relative lg:col-span-5 lg:min-h-[46rem]">
            <Photo
              name="contact"
              priority
              sizes="(min-width: 1024px) 42vw, 100vw"
              overlay="soft"
              className="relative h-64 w-full sm:h-80 lg:absolute lg:inset-0 lg:h-full"
            />
            <div className="absolute inset-0 flex items-end p-6 sm:p-10 lg:items-center lg:p-12">
              <Reveal>
                <p className="flex items-center gap-2.5 text-[0.6875rem] font-semibold uppercase tracking-[0.18em] text-accent-300">
                  <span aria-hidden="true" className="h-px w-6 bg-accent-300/60" />
                  Contact
                </p>
                <h1 className="text-headline mt-5 max-w-md text-white">
                  Let&apos;s build something with your data.
                </h1>
                <p className="text-lede mt-5 hidden max-w-md text-mist-300 lg:block">
                  Tell us what you&apos;re trying to achieve and what&apos;s currently in the way.
                  We&apos;ll respond with a straight answer about whether — and how — we can help.
                </p>
              </Reveal>
            </div>
          </div>

          <div className="bg-white lg:col-span-7">
            <div className="mx-auto w-full max-w-3xl px-5 py-16 sm:px-8 sm:py-20 lg:px-12">
              <Reveal>
                <h2 className="text-subhead text-navy-950">Start the conversation</h2>
                <p className="mt-3 max-w-xl text-[0.9375rem] leading-relaxed text-mist-600">
                  The more context you can give us, the more useful our first reply will be.
                </p>
                <div className="mt-10">
                  <Suspense fallback={<div className="h-[48rem] rounded-2xl bg-mist-50" />}>
                    <ContactForm />
                  </Suspense>
                </div>
              </Reveal>
            </div>
          </div>
        </div>
      </section>

      <section className="border-t border-navy-950/8 bg-mist-50">
        <Container className="py-16 sm:py-20">
          <div className="grid gap-10 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-7">
              <h2 className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                What people contact us about
              </h2>
              <ul className="mt-6 grid gap-6 sm:grid-cols-3">
                {helpTopics.map((topic) => (
                  <li key={topic.title}>
                    <p className="text-[0.9375rem] font-semibold text-navy-950">{topic.title}</p>
                    <p className="mt-1.5 text-[0.875rem] leading-relaxed text-mist-600">{topic.body}</p>
                  </li>
                ))}
              </ul>
            </div>

            <div className="lg:col-span-5">
              <h2 className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
                Direct channels
              </h2>
              {hasDirectContactChannels ? (
                <ul className="mt-6 space-y-2.5 text-[0.9375rem]">
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
                  {contact.location ? <li className="text-mist-600">{contact.location}</li> : null}
                </ul>
              ) : (
                <p className="mt-6 text-[0.875rem] leading-relaxed text-mist-600">
                  Our published email address and social channels are being finalised. Until they are
                  listed here, the form is the fastest way to reach the team — every enquiry goes
                  directly to us.
                </p>
              )}
              <ButtonLink href="/contact?intent=consultation" variant="secondary" className="mt-7">
                Book a Consultation
                <Arrow />
              </ButtonLink>
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

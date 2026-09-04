import { Container } from "@/components/ui/container";
import { Reveal } from "@/components/ui/reveal";
import { capabilityStrip } from "@/content/technologies";

/**
 * Credibility strip. Deliberately shows the technology categories GraceWell works in
 * rather than client logos, because no client logo has been cleared for publication.
 */
export function TrustStrip() {
  return (
    <section className="border-b border-navy-950/8 bg-mist-50" aria-labelledby="trust-heading">
      <Container className="py-14 sm:py-16">
        <Reveal>
          <h2
            id="trust-heading"
            className="text-subhead max-w-2xl text-navy-950"
          >
            Built for organizations that take data seriously.
          </h2>
          <p className="mt-3 max-w-xl text-[0.9375rem] leading-relaxed text-mist-600">
            The platforms, engines and tooling our engineers work with day to day.
          </p>
        </Reveal>

        {/*
          Below `sm` this is a horizontal rail. Its cards contain no links, so without an
          explicit tab stop a keyboard user could not scroll it (WCAG 2.1.1).
        */}
        <ul
          tabIndex={0}
          aria-label="Technology capability areas"
          className="scroll-rail -mx-5 mt-10 flex snap-x snap-mandatory gap-4 overflow-x-auto px-5 focus-visible:outline-2 sm:mx-0 sm:grid sm:grid-cols-2 sm:overflow-visible sm:px-0 lg:grid-cols-4"
        >
          {capabilityStrip.map((group, index) => (
            <Reveal
              as="li"
              key={group.title}
              delay={index * 70}
              className="min-w-[16rem] shrink-0 snap-start rounded-2xl border border-navy-950/8 bg-white p-6 shadow-[0_1px_2px_rgba(8,17,36,0.03)] sm:min-w-0"
            >
              <h3 className="text-[0.9375rem] font-semibold tracking-[-0.01em] text-navy-950">
                {group.title}
              </h3>
              <p className="mt-3 text-[0.875rem] leading-relaxed text-mist-500">
                {group.items.join(" · ")}
              </p>
            </Reveal>
          ))}
        </ul>
      </Container>
    </section>
  );
}

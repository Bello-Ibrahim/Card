import { approach } from "@/content/approach";
import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";

/**
 * Horizontal on large screens (a true timeline), vertical rail on small screens —
 * an intentional mobile layout rather than stacked desktop cards.
 */
export function ApproachTimeline() {
  return (
    <section className="bg-white" aria-labelledby="approach-heading">
      <Container className="py-20 sm:py-24 lg:py-28">
        <SectionHeader
          eyebrow="Our Approach"
          title="A practical path from data complexity to data confidence."
          lede="Six stages that take an organization from an unclear data landscape to a platform its teams can operate and extend on their own."
        />

        <ol className="relative mt-14 grid gap-y-10 lg:grid-cols-6 lg:gap-x-6">
          {/* Rails */}
          <li
            aria-hidden="true"
            className="absolute left-[0.6875rem] top-2 hidden h-[calc(100%-1rem)] w-px bg-gradient-to-b from-accent-500/50 via-navy-950/12 to-transparent sm:block lg:left-0 lg:top-[0.6875rem] lg:h-px lg:w-full lg:bg-gradient-to-r"
          />
          {approach.map((step, index) => (
            <Reveal
              as="li"
              key={step.number}
              delay={index * 70}
              className="relative pl-10 sm:pl-12 lg:pl-0 lg:pt-12"
            >
              <span
                aria-hidden="true"
                className="absolute left-0 top-1 flex h-[1.375rem] w-[1.375rem] items-center justify-center rounded-full border border-navy-950/12 bg-white lg:top-0"
              >
                <span className="h-1.5 w-1.5 rounded-full bg-accent-500" />
              </span>
              <p className="font-mono text-[0.75rem] font-medium tracking-[0.1em] text-accent-600">
                {step.number}
              </p>
              <h3 className="mt-2 text-[1.0625rem] font-semibold tracking-[-0.02em] text-navy-950">
                {step.title}
              </h3>
              <p className="mt-2.5 text-[0.875rem] leading-relaxed text-mist-600">{step.summary}</p>
              <ul className="mt-4 space-y-1.5">
                {step.detail.map((item) => (
                  <li key={item} className="flex items-start gap-2 text-[0.8125rem] text-mist-500">
                    <span aria-hidden="true" className="mt-[0.4rem] h-1 w-1 shrink-0 rounded-full bg-mist-300" />
                    {item}
                  </li>
                ))}
              </ul>
            </Reveal>
          ))}
        </ol>
      </Container>
    </section>
  );
}

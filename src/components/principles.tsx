import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { Icon, type IconName } from "@/components/ui/icon";
import { principles } from "@/content/principles";

export function Principles() {
  return (
    <section className="bg-white" aria-labelledby="principles-heading">
      <Container className="py-20 sm:py-24 lg:py-28">
        <SectionHeader
          eyebrow="How we build"
          title="Six principles we hold ourselves to."
          lede="Consulting judgement and engineering capability from the same team — so the architecture that gets designed is the architecture that gets built."
        />

        <ul className="mt-14 grid gap-px overflow-hidden rounded-2xl border border-navy-950/8 bg-navy-950/8 sm:grid-cols-2 lg:grid-cols-3">
          {principles.map((principle, index) => (
            <Reveal
              as="li"
              key={principle.title}
              delay={index * 60}
              className="group bg-white p-7 transition-colors duration-300 hover:bg-mist-50 lg:p-8"
            >
              <span
                aria-hidden="true"
                className="inline-flex h-10 w-10 items-center justify-center rounded-lg bg-navy-950/[0.04] text-navy-800 transition-colors duration-300 group-hover:bg-accent-500 group-hover:text-white"
              >
                <Icon name={principle.icon as IconName} className="h-[1.125rem] w-[1.125rem]" />
              </span>
              <h3 className="mt-5 text-[1.0625rem] font-semibold tracking-[-0.02em] text-navy-950">
                {principle.title}
              </h3>
              <p className="mt-2.5 text-[0.9375rem] leading-relaxed text-mist-600">{principle.body}</p>
            </Reveal>
          ))}
        </ul>
      </Container>
    </section>
  );
}

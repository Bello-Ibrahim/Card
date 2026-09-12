import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { GlobalReach } from "@/components/visuals/global-reach";

export function GlobalReachSection() {
  return (
    <section className="dark-section relative isolate overflow-hidden bg-navy-950 text-white" aria-labelledby="reach-heading">
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-35" />
      <Container className="relative py-20 sm:py-24 lg:py-28">
        <div className="grid items-center gap-14 lg:grid-cols-12 lg:gap-16">
          <div className="lg:col-span-6">
            <SectionHeader
              eyebrow="Lagos · Africa · Global"
              tone="dark"
              title="Built in Africa. Engineered for the World."
              lede="DataForge Consulting combines global engineering practices with an understanding of the realities of building technology infrastructure in emerging and global markets."
            />
            <Reveal delay={140}>
              <p className="mt-8 max-w-xl text-[0.9375rem] leading-relaxed text-mist-400">
                That means designing for intermittent connectivity, constrained budgets and scarce
                senior engineering capacity as first-class constraints — not as exceptions to a
                reference architecture written somewhere else.
              </p>
            </Reveal>
          </div>

          <Reveal delay={120} className="lg:col-span-6">
            <div className="mx-auto max-w-[32rem]">
              <GlobalReach />
            </div>
          </Reveal>
        </div>
      </Container>
    </section>
  );
}

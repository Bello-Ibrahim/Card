import { ButtonLink, Arrow } from "@/components/ui/button";
import { Container } from "@/components/ui/container";
import { DataPlatformVisual } from "@/components/data-platform-visual";
import { Reveal } from "@/components/ui/reveal";

const credibility = [
  "Data Engineering",
  "Cloud",
  "Analytics",
  "Architecture",
  "Training",
  "Talent",
];

export function Hero() {
  return (
    <section className="dark-section relative isolate overflow-hidden bg-navy-950 pt-[4.5rem] text-white lg:pt-20">
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-60 mask-fade-b" />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute -left-40 top-[-18%] h-[38rem] w-[38rem] rounded-full bg-accent-600/25 blur-[120px] drift-slow"
      />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute -right-32 bottom-[-24%] h-[32rem] w-[32rem] rounded-full bg-cyan-500/12 blur-[130px]"
      />

      <Container className="relative">
        <div className="grid items-center gap-14 py-16 sm:py-20 lg:grid-cols-12 lg:gap-12 lg:py-28 xl:gap-20">
          <div className="lg:col-span-7">
            <Reveal>
              <p className="inline-flex items-center gap-2.5 rounded-full border border-white/15 bg-white/5 px-3.5 py-1.5 text-[0.75rem] font-medium tracking-[-0.01em] text-mist-300 backdrop-blur-sm">
                <span aria-hidden="true" className="h-1.5 w-1.5 rounded-full bg-teal-400" />
                Data engineering consulting &amp; technology advisory
              </p>
            </Reveal>

            <Reveal delay={80}>
              <h1 className="text-display mt-7 max-w-[16ch] text-white">
                Engineering the Data Foundations Behind Better Decisions.
              </h1>
            </Reveal>

            <Reveal delay={160}>
              <p className="text-lede mt-7 max-w-xl text-mist-300">
                We help organizations design, build, modernize and scale data platforms that are
                reliable, secure and ready for the future.
              </p>
            </Reveal>

            <Reveal delay={240}>
              <div className="mt-9 flex flex-col gap-3 sm:flex-row sm:items-center">
                <ButtonLink href="/contact" size="lg" variant="onDark">
                  Talk to a Data Engineering Expert
                  <Arrow />
                </ButtonLink>
                <ButtonLink href="/services" size="lg" variant="onDarkGhost">
                  Explore Our Capabilities
                </ButtonLink>
              </div>
            </Reveal>

            <Reveal delay={320}>
              <ul className="mt-12 flex flex-wrap items-center gap-x-3 gap-y-2 border-t border-white/10 pt-6 text-[0.8125rem] text-mist-400">
                {credibility.map((item, index) => (
                  <li key={item} className="flex items-center gap-3">
                    {index > 0 ? (
                      <span aria-hidden="true" className="h-1 w-1 rounded-full bg-mist-500/60" />
                    ) : null}
                    {item}
                  </li>
                ))}
              </ul>
            </Reveal>
          </div>

          <Reveal delay={200} className="lg:col-span-5">
            <div className="relative mx-auto max-w-[26rem] lg:max-w-none">
              <div
                aria-hidden="true"
                className="absolute inset-0 -m-4 rounded-[2rem] border border-white/10 bg-white/[0.03] backdrop-blur-[2px]"
              />
              <DataPlatformVisual className="relative" />
            </div>
          </Reveal>
        </div>
      </Container>
    </section>
  );
}

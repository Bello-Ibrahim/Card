import { ButtonLink, Arrow } from "@/components/ui/button";
import { Container } from "@/components/ui/container";
import { Photo } from "@/components/media/photo";
import { DataPlatformVisual } from "@/components/data-platform-visual";
import { Reveal } from "@/components/ui/reveal";
import { capabilityStrip } from "@/content/technologies";

/**
 * Split hero: editorial copy against a real technology environment, with the platform
 * architecture overlaid as a glass panel. The photograph sits behind everything at low
 * luminance so the headline keeps its contrast ratio regardless of the image supplied.
 */
export function Hero() {
  return (
    <section className="dark-section relative isolate overflow-hidden bg-ink-950 pt-[4.5rem] text-white lg:pt-20">
      <Photo
        name="heroOperations"
        priority
        sizes="100vw"
        className="absolute inset-0 -z-10"
        imgClassName="opacity-90"
      />
      <div
        aria-hidden="true"
        className="absolute inset-0 -z-10 bg-gradient-to-r from-ink-950 via-ink-950/88 to-ink-950/45"
      />
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 -z-10 bg-grid opacity-40 mask-fade-b" />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute -left-40 top-[-18%] -z-10 h-[38rem] w-[38rem] rounded-full bg-accent-600/25 blur-[130px] drift-slow"
      />

      <Container className="relative">
        <div className="grid items-center gap-14 py-16 sm:py-20 lg:grid-cols-12 lg:gap-12 lg:py-28 xl:gap-20">
          <div className="lg:col-span-7">
            <Reveal>
              <p className="inline-flex items-center gap-2.5 rounded-full border border-white/15 bg-white/[0.06] px-3.5 py-1.5 text-[0.75rem] font-medium text-mist-300 backdrop-blur-sm">
                <span aria-hidden="true" className="h-1.5 w-1.5 rounded-full bg-teal-400" />
                Data engineering &amp; technology consulting
              </p>
            </Reveal>

            <Reveal delay={80}>
              {/* Shorter, punchier line on small screens — an intentional mobile headline. */}
              <h1 className="text-display mt-7 text-white">
                <span className="sm:hidden">Engineering Better Data Foundations.</span>
                <span className="hidden max-w-[17ch] sm:inline">
                  Engineering the Data Foundations Behind Intelligent Business.
                </span>
              </h1>
            </Reveal>

            <Reveal delay={160}>
              <p className="text-lede mt-7 max-w-xl text-mist-300">
                DataForge Consulting helps organizations design, build, modernize and scale
                reliable data platforms, pipelines and engineering teams.
              </p>
            </Reveal>

            <Reveal delay={240}>
              <div className="mt-9 flex flex-col gap-3 sm:flex-row sm:items-center">
                <ButtonLink href="/contact" size="lg" variant="onDark">
                  Talk to a Data Expert
                  <Arrow />
                </ButtonLink>
                <ButtonLink href="/services" size="lg" variant="onDarkGhost">
                  Explore Capabilities
                </ButtonLink>
              </div>
            </Reveal>

            <Reveal delay={320}>
              <ul className="mt-12 flex flex-wrap items-center gap-x-3 gap-y-2 border-t border-white/10 pt-6 text-[0.8125rem] text-mist-400">
                {capabilityStrip.map((item, index) => (
                  <li key={item} className="flex items-center gap-3">
                    {index > 0 ? (
                      <span aria-hidden="true" className="h-1 w-1 rounded-full bg-mist-500/70" />
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
                className="absolute inset-0 -m-4 rounded-[2rem] border border-white/12 bg-white/[0.05] backdrop-blur-md"
              />
              <DataPlatformVisual className="relative" />
            </div>
          </Reveal>
        </div>
      </Container>
    </section>
  );
}

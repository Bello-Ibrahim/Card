import { Container } from "@/components/ui/container";
import { Photo } from "@/components/media/photo";
import { Reveal } from "@/components/ui/reveal";
import { capabilityStrip } from "@/content/technologies";

/**
 * Photographic trust banner immediately below the hero.
 * Capability indicators sit beneath the image rather than over it, so they stay legible
 * whatever photograph is eventually supplied.
 */
export function TrustBand() {
  return (
    <section className="dark-section relative bg-ink-950" aria-labelledby="trust-heading">
      <div className="relative">
        <Photo
          name="trustBanner"
          sizes="100vw"
          overlay="bottom"
          className="relative h-[22rem] w-full sm:h-[26rem] lg:h-[32rem]"
        />
        <div className="absolute inset-0 flex items-end">
          <Container className="pb-10 sm:pb-14">
            <Reveal className="max-w-2xl">
              <h2 id="trust-heading" className="text-headline text-white">
                Data engineering built for the real world.
              </h2>
              <p className="text-lede mt-5 text-mist-300">
                From fragmented data environments to scalable platforms, DataForge helps
                organizations turn complex data infrastructure into a strategic capability.
              </p>
            </Reveal>
          </Container>
        </div>
      </div>

      <Container>
        <ul className="grid grid-cols-2 gap-px overflow-hidden rounded-2xl border border-white/10 bg-white/10 sm:grid-cols-4 lg:grid-cols-8">
          {capabilityStrip.map((item, index) => (
            <Reveal
              as="li"
              key={item}
              delay={index * 45}
              className="bg-ink-950 px-4 py-5 text-center transition-colors duration-300 hover:bg-navy-900"
            >
              <span className="text-[0.8125rem] font-medium tracking-[-0.01em] text-mist-300">
                {item}
              </span>
            </Reveal>
          ))}
        </ul>
      </Container>
    </section>
  );
}

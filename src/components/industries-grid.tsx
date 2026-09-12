import Link from "next/link";
import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { Photo } from "@/components/media/photo";
import { Arrow } from "@/components/ui/button";
import { industries } from "@/content/industries";

/**
 * Immersive industry cards.
 *
 * On large screens the detail is revealed on hover; `group-focus-within` mirrors that for
 * keyboard users, and below `lg` the detail is simply always visible — a hover-only
 * affordance would hide it from touch entirely. The revealed text uses opacity rather than
 * `display`, so it stays in the accessibility tree at all times.
 */
export function IndustriesGrid({ limit }: { limit?: number }) {
  const list = limit ? industries.slice(0, limit) : industries;

  return (
    <section className="dark-section relative bg-ink-950" aria-labelledby="industries-heading">
      <Container className="py-20 sm:py-24 lg:py-28">
        <SectionHeader
          eyebrow="Industries"
          tone="dark"
          title="Engineering for data-intensive industries."
          lede="The discipline stays consistent. What changes is the regulatory context, the shape of the data and the decisions the platform has to support."
        />

        <ul className="mt-14 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {list.map((industry, index) => (
            <Reveal as="li" key={industry.slug} delay={(index % 4) * 60}>
              <article
                id={industry.slug}
                className="group/media relative flex h-full min-h-[24rem] scroll-mt-28 flex-col justify-end overflow-hidden rounded-2xl border border-white/10 transition-colors duration-300 focus-within:border-white/30 hover:border-white/30"
              >
                <Photo
                  name={industry.photo}
                  sizes="(min-width: 1024px) 25vw, (min-width: 640px) 50vw, 100vw"
                  zoomOnHover
                  overlay="bottom"
                  className="absolute inset-0"
                />

                <div className="relative p-6">
                  <h3 className="text-[1.125rem] font-semibold tracking-[-0.02em] text-white">
                    {industry.name}
                  </h3>
                  <p className="mt-2 text-[0.875rem] font-medium leading-snug text-accent-300">
                    {industry.headline}
                  </p>

                  <div className="mt-4 transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] lg:max-h-0 lg:-translate-y-1 lg:overflow-hidden lg:opacity-0 lg:group-focus-within/media:max-h-72 lg:group-focus-within/media:translate-y-0 lg:group-focus-within/media:opacity-100 lg:group-hover/media:max-h-72 lg:group-hover/media:translate-y-0 lg:group-hover/media:opacity-100 motion-reduce:transition-none">
                    <ul className="space-y-1.5 border-t border-white/12 pt-4">
                      {industry.challenges.map((challenge) => (
                        <li key={challenge} className="flex items-start gap-2 text-[0.8125rem] text-mist-300">
                          <span aria-hidden="true" className="mt-[0.45rem] h-1 w-1 shrink-0 rounded-full bg-cyan-400" />
                          {challenge}
                        </li>
                      ))}
                    </ul>
                    <ul className="mt-4 flex flex-wrap gap-1.5">
                      {industry.solutions.map((solution) => (
                        <li key={solution.href}>
                          <Link
                            href={solution.href}
                            className="inline-flex items-center gap-1.5 rounded-full border border-white/20 px-3 py-1.5 text-[0.75rem] text-white transition-colors hover:border-white/50 hover:bg-white/10"
                          >
                            {solution.label}
                            <Arrow className="h-3 w-3" />
                          </Link>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </article>
            </Reveal>
          ))}
        </ul>
      </Container>
    </section>
  );
}

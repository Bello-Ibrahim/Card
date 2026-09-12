import Link from "next/link";
import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { Photo } from "@/components/media/photo";
import { trainingTracks } from "@/content/training";

export function TrainingSection() {
  return (
    <section className="bg-white" aria-labelledby="training-heading">
      <Container className="py-20 sm:py-24 lg:py-28">
        <div className="grid gap-12 lg:grid-cols-12 lg:gap-16">
          <div className="lg:col-span-5">
            <SectionHeader
              eyebrow="Training"
              title="Turn your team into a data engineering team."
              lede="Programs taught by practising engineers, built on the stack your teams actually use, and paired with mentoring on live delivery work."
            />
            <Reveal delay={120}>
              <Photo
                name="training"
                sizes="(min-width: 1024px) 40vw, 100vw"
                zoomOnHover
                overlay="soft"
                className="relative mt-9 aspect-[4/3] rounded-2xl border border-navy-950/8"
              />
              <ButtonLink href="/training" className="mt-8">
                Explore Training
                <Arrow />
              </ButtonLink>
            </Reveal>
          </div>

          <div className="lg:col-span-7">
            <ul className="divide-y divide-navy-950/8 border-y border-navy-950/8">
              {trainingTracks.map((track, index) => (
                <Reveal as="li" key={track.slug} delay={index * 60}>
                  <Link
                    href={`/training#${track.slug}`}
                    className="group/card block py-6 transition-colors hover:bg-mist-50"
                  >
                    <div className="flex items-start gap-5">
                      <span className="mt-1 shrink-0 rounded-full border border-navy-950/10 px-2.5 py-1 text-[0.6875rem] font-medium uppercase tracking-[0.1em] text-mist-500">
                        {track.level}
                      </span>
                      <div className="min-w-0 flex-1">
                        <span className="block text-[1.0625rem] font-semibold tracking-[-0.02em] text-navy-950">
                          {track.title}
                        </span>
                        <span className="mt-1.5 block text-[0.9375rem] leading-relaxed text-mist-600">
                          {track.summary}
                        </span>
                        <ul className="mt-3 flex flex-wrap gap-1.5">
                          {track.modules.slice(0, 4).map((module) => (
                            <li
                              key={module}
                              className="rounded-md border border-navy-950/8 bg-mist-50 px-2 py-1 text-[0.75rem] leading-none text-mist-600"
                            >
                              {module}
                            </li>
                          ))}
                        </ul>
                      </div>
                      <Arrow className="mt-2 shrink-0 text-mist-500" />
                    </div>
                  </Link>
                </Reveal>
              ))}
            </ul>
          </div>
        </div>
      </Container>
    </section>
  );
}

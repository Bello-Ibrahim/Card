import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { technologyGroups } from "@/content/technologies";

export function TechEcosystem({ tone = "light" }: { tone?: "light" | "dark" }) {
  const dark = tone === "dark";
  return (
    <section
      className={dark ? "dark-section relative overflow-hidden bg-navy-950" : "bg-mist-50"}
      aria-labelledby="technology-heading"
    >
      {dark ? (
        <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-40" />
      ) : null}
      <Container className="relative py-20 sm:py-24 lg:py-28">
        <SectionHeader
          eyebrow="Technology Ecosystem"
          tone={tone}
          title="The technology we build, operate and teach on."
          lede="Selection follows your constraints — existing investment, team skills, compliance and cost — not a preferred vendor."
        />

        <div className="mt-14 grid gap-x-6 gap-y-8 sm:grid-cols-2 lg:grid-cols-3">
          {technologyGroups.map((group, index) => (
            <Reveal key={group.category} delay={index * 60}>
              <div
                className={
                  dark
                    ? "h-full rounded-2xl border border-white/10 bg-white/[0.03] p-6"
                    : "h-full rounded-2xl border border-navy-950/8 bg-white p-6"
                }
              >
                <h3
                  className={`text-[0.9375rem] font-semibold tracking-[-0.01em] ${
                    dark ? "text-white" : "text-navy-950"
                  }`}
                >
                  {group.category}
                </h3>
                <p className={`mt-2 text-[0.8125rem] leading-relaxed ${dark ? "text-mist-400" : "text-mist-500"}`}>
                  {group.blurb}
                </p>
                <ul className="mt-5 flex flex-wrap gap-1.5">
                  {group.items.map((item) => (
                    <li
                      key={item}
                      className={
                        dark
                          ? "rounded-full border border-white/12 bg-white/[0.04] px-3 py-1.5 text-[0.8125rem] text-mist-300"
                          : "rounded-full border border-navy-950/8 bg-mist-50 px-3 py-1.5 text-[0.8125rem] text-mist-600"
                      }
                    >
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
            </Reveal>
          ))}
        </div>

        <p className={`mt-8 text-[0.8125rem] ${dark ? "text-mist-400" : "text-mist-500"}`}>
          Technologies listed are the tools our engineers work with. They do not represent vendor
          partnerships, certifications, affiliations or client endorsements.
        </p>
      </Container>
    </section>
  );
}

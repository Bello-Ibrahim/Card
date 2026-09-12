import Link from "next/link";
import { Container } from "@/components/ui/container";
import { SectionHeader } from "@/components/ui/section-header";
import { Reveal } from "@/components/ui/reveal";
import { Arrow } from "@/components/ui/button";
import { Photo } from "@/components/media/photo";
import { BeforeAfter } from "@/components/visuals/before-after";
import { ArchitectureDiagram } from "@/components/visuals/architecture-diagram";
import { featuredServices } from "@/content/services";
import { cn } from "@/lib/utils";

/** A short chain diagram used to show cloud and integration shapes without a full architecture. */
function Chain({ nodes, converge }: { nodes: string[]; converge?: string }) {
  return (
    <div className="rounded-2xl border border-navy-950/8 bg-mist-50 p-5">
      <ul className={cn("flex flex-wrap items-center gap-x-2 gap-y-2", converge && "gap-x-1.5")}>
        {nodes.map((node, i) => (
          <li key={node} className="flex items-center gap-2">
            {i > 0 ? (
              <span aria-hidden="true" className="text-mist-400">
                {converge ? "+" : "→"}
              </span>
            ) : null}
            <span className="rounded-lg border border-navy-950/10 bg-white px-3 py-1.5 text-[0.8125rem] text-navy-900">
              {node}
            </span>
          </li>
        ))}
      </ul>
      {converge ? (
        <div className="mt-4 flex items-center gap-3">
          <span aria-hidden="true" className="relative block h-px flex-1 overflow-hidden bg-navy-950/12">
            <span className="flow-sheen absolute inset-0 block opacity-70" />
          </span>
          <span className="rounded-lg border border-accent-500/40 bg-accent-500/10 px-3 py-1.5 text-[0.8125rem] font-medium text-accent-700">
            {converge}
          </span>
        </div>
      ) : null}
    </div>
  );
}

function extraFor(slug: string) {
  switch (slug) {
    case "cloud-data-engineering":
      return <Chain nodes={["Applications", "Cloud", "Data Platform", "Analytics", "AI"]} />;
    case "data-integration":
      return (
        <Chain
          nodes={["CRM", "ERP", "APIs", "Databases", "Files", "Kafka"]}
          converge="Unified Data Platform"
        />
      );
    case "data-modernization":
      return <BeforeAfter tone="light" />;
    default:
      return null;
  }
}

export function ServicesShowcase() {
  return (
    <section className="bg-white" aria-labelledby="services-heading">
      <Container className="py-20 sm:py-24 lg:py-28">
        <SectionHeader
          eyebrow="Services"
          title="What we build"
          lede="Five capabilities that carry most engagements — and the engineering practice that makes each of them hold up in production."
        />

        <div className="mt-16 space-y-20 lg:space-y-28">
          {featuredServices.map((service, index) => {
            const flipped = index % 2 === 1;
            const extra = extraFor(service.slug);
            return (
              <Reveal key={service.slug}>
                <article className="grid items-center gap-10 lg:grid-cols-12 lg:gap-14">
                  <div className={cn("lg:col-span-6", flipped && "lg:order-2")}>
                    <Link
                      href={`/services/${service.slug}`}
                      className="group/media block overflow-hidden rounded-2xl"
                      tabIndex={-1}
                      aria-hidden="true"
                    >
                      <Photo
                        name={service.photo}
                        sizes="(min-width: 1024px) 50vw, 100vw"
                        zoomOnHover
                        overlay="soft"
                        className="relative aspect-[4/3] rounded-2xl border border-navy-950/8"
                      />
                    </Link>
                  </div>

                  <div className={cn("lg:col-span-6", flipped && "lg:order-1")}>
                    <p className="font-mono text-[0.75rem] font-medium tracking-[0.14em] text-accent-600">
                      {String(service.featured).padStart(2, "0")}
                    </p>
                    <h3 className="mt-3 text-[clamp(1.5rem,1.1rem+1.4vw,2.125rem)] font-bold leading-tight tracking-[-0.03em] text-navy-950">
                      <Link href={`/services/${service.slug}`} className="hover:text-accent-700">
                        {service.title}
                      </Link>
                    </h3>
                    <p className="mt-4 text-[1.0625rem] leading-relaxed text-mist-600">
                      {service.summary}
                    </p>

                    <ul className="mt-6 flex flex-wrap gap-1.5">
                      {service.capabilities.slice(0, 6).map((capability) => (
                        <li
                          key={capability}
                          className="rounded-full border border-navy-950/10 bg-mist-50 px-3 py-1.5 text-[0.8125rem] text-mist-600"
                        >
                          {capability}
                        </li>
                      ))}
                    </ul>

                    {extra ? <div className="mt-7">{extra}</div> : null}

                    <Link
                      href={`/services/${service.slug}`}
                      className="group/btn mt-7 inline-flex items-center gap-2 text-[0.9375rem] font-medium text-navy-950 transition-colors hover:text-accent-600"
                    >
                      Explore {service.title}
                      <Arrow />
                    </Link>
                  </div>
                </article>
              </Reveal>
            );
          })}
        </div>
      </Container>
    </section>
  );
}

/** Full-width signature architecture band. */
export function PlatformArchitecture() {
  return (
    <section className="dark-section relative isolate overflow-hidden bg-navy-950 text-white" aria-labelledby="architecture-heading">
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-45" />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute left-1/3 top-0 h-[34rem] w-[46rem] -translate-x-1/2 rounded-full bg-accent-600/18 blur-[140px] drift-slow"
      />
      <Container className="relative py-20 sm:py-24 lg:py-28">
        <SectionHeader
          eyebrow="Platform architecture"
          tone="dark"
          title="From raw data to business intelligence"
          lede="The reference shape of the platforms we build. Each stage is engineered, tested and monitored — not assumed."
        />
        <div className="mt-14">
          <ArchitectureDiagram />
        </div>
      </Container>
    </section>
  );
}

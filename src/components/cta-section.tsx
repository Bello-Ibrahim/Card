import { ButtonLink, Arrow } from "@/components/ui/button";
import { Container } from "@/components/ui/container";
import { Reveal } from "@/components/ui/reveal";

export function CtaSection({
  eyebrow = "Get started",
  title = "Have a data challenge? Let's engineer the solution.",
  body = "Whether you're building a data platform, modernizing legacy infrastructure, developing your engineering team, or preparing your organization for AI, DataForge can help.",
  primary = { label: "Talk to an Expert", href: "/contact" },
  secondary = { label: "Book a Consultation", href: "/contact?topic=consultation" },
}: {
  eyebrow?: string;
  title?: string;
  body?: string;
  primary?: { label: string; href: string };
  secondary?: { label: string; href: string };
}) {
  return (
    <section className="dark-section relative isolate overflow-hidden bg-navy-950 text-white">
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-50" />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute left-1/2 top-1/2 h-[34rem] w-[52rem] -translate-x-1/2 -translate-y-1/2 rounded-full bg-accent-600/22 blur-[130px] drift-slow"
      />
      <Container className="relative">
        <div className="flex flex-col items-start gap-10 py-20 sm:py-24 lg:flex-row lg:items-end lg:justify-between lg:py-28">
          <Reveal className="max-w-2xl">
            <p className="flex items-center gap-2.5 text-[0.6875rem] font-semibold uppercase tracking-[0.18em] text-accent-300">
              <span aria-hidden="true" className="h-px w-6 bg-accent-300/60" />
              {eyebrow}
            </p>
            <h2 className="text-headline mt-5 text-white">{title}</h2>
            <p className="text-lede mt-5 text-mist-300">{body}</p>
          </Reveal>
          <Reveal delay={120} className="w-full lg:w-auto">
            <div className="flex flex-col gap-3 sm:flex-row lg:flex-col xl:flex-row">
              <ButtonLink href={primary.href} size="lg" variant="onDark">
                {primary.label}
                <Arrow />
              </ButtonLink>
              <ButtonLink href={secondary.href} size="lg" variant="onDarkGhost">
                {secondary.label}
              </ButtonLink>
            </div>
          </Reveal>
        </div>
      </Container>
    </section>
  );
}

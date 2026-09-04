import { Container } from "@/components/ui/container";
import { ButtonLink, Arrow } from "@/components/ui/button";

const suggestions = [
  { label: "Services", href: "/services" },
  { label: "Solutions", href: "/solutions" },
  { label: "Industries", href: "/industries" },
  { label: "Training", href: "/training" },
  { label: "Team Setup", href: "/team-setup" },
  { label: "Insights", href: "/insights" },
];

export default function NotFound() {
  return (
    <section className="dark-section relative isolate flex min-h-[70vh] items-center overflow-hidden bg-navy-950 pt-[4.5rem] text-white">
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-50" />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute left-1/2 top-1/2 h-[30rem] w-[40rem] -translate-x-1/2 -translate-y-1/2 rounded-full bg-accent-600/20 blur-[130px]"
      />
      <Container className="relative py-20">
        <p className="font-mono text-[0.8125rem] tracking-[0.18em] text-accent-300">404</p>
        <h1 className="text-headline mt-5 max-w-2xl text-white">
          That page isn&apos;t part of the pipeline.
        </h1>
        <p className="text-lede mt-5 max-w-xl text-mist-300">
          The page you asked for doesn&apos;t exist, or has moved. Here are the places people usually
          mean to go.
        </p>

        <ul className="mt-8 flex flex-wrap gap-2">
          {suggestions.map((item) => (
            <li key={item.href}>
              <ButtonLink href={item.href} variant="onDarkGhost" size="sm">
                {item.label}
              </ButtonLink>
            </li>
          ))}
        </ul>

        <div className="mt-10 flex flex-col gap-3 sm:flex-row">
          <ButtonLink href="/" size="lg" variant="onDark">
            Back to home
            <Arrow />
          </ButtonLink>
          <ButtonLink href="/contact" size="lg" variant="onDarkGhost">
            Talk to an Expert
          </ButtonLink>
        </div>
      </Container>
    </section>
  );
}

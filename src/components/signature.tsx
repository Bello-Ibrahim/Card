import { Container } from "@/components/ui/container";
import { Reveal } from "@/components/ui/reveal";

const LINES = ["Raw data.", "Real engineering.", "Business value."];

/**
 * DataForge's signature statement. Three declarations with a stream of data flowing between
 * them — the brand's "forge" idea rendered as type and motion rather than illustration.
 */
export function SignatureStatement() {
  return (
    <section className="dark-section relative isolate overflow-hidden bg-ink-950 text-white">
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-40" />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute left-1/2 top-1/2 h-[30rem] w-[52rem] -translate-x-1/2 -translate-y-1/2 rounded-full bg-accent-600/20 blur-[140px] drift-slow"
      />
      <Container className="relative py-24 sm:py-28 lg:py-36">
        <div className="mx-auto max-w-4xl">
          {LINES.map((line, index) => (
            <div key={line}>
              <Reveal delay={index * 120}>
                <p className="text-[clamp(2.25rem,1.1rem+4.6vw,4.5rem)] font-extrabold uppercase leading-[1.02] tracking-[-0.035em] text-white">
                  {line}
                </p>
              </Reveal>
              {index < LINES.length - 1 ? (
                <div aria-hidden="true" className="my-5 flex items-center gap-3 sm:my-7">
                  <span className="relative block h-px flex-1 overflow-hidden bg-white/12">
                    <span
                      className="flow-sheen absolute inset-0 block"
                      style={{ animationDelay: `${index * 400}ms` }}
                    />
                  </span>
                  <span className="h-1.5 w-1.5 shrink-0 rounded-full bg-cyan-400" />
                </div>
              ) : null}
            </div>
          ))}

          <Reveal delay={400}>
            <p className="mt-10 text-[1.125rem] font-medium tracking-[-0.01em] text-accent-300 sm:mt-12">
              That&apos;s the DataForge way.
            </p>
          </Reveal>
        </div>
      </Container>
    </section>
  );
}

import Link from "next/link";
import { Container } from "@/components/ui/container";
import { Reveal } from "@/components/ui/reveal";
import { cn } from "@/lib/utils";

export type Crumb = { name: string; path: string };

/** Standard dark page masthead used by every interior page. */
export function PageHeader({
  eyebrow,
  title,
  lede,
  breadcrumbs,
  children,
  align = "left",
  media,
}: {
  eyebrow: string;
  title: string;
  lede?: string;
  breadcrumbs?: Crumb[];
  children?: React.ReactNode;
  align?: "left" | "center";
  /** Optional artwork rendered beside the copy on large screens. */
  media?: React.ReactNode;
}) {
  const hasMedia = Boolean(media);

  return (
    <section className="dark-section relative isolate overflow-hidden bg-navy-950 pt-[4.5rem] text-white lg:pt-20">
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-50 mask-fade-b" />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute -right-24 top-[-30%] h-[30rem] w-[30rem] rounded-full bg-accent-600/22 blur-[120px] drift-slow"
      />
      <Container className="relative">
        <div
          className={cn(
            "py-16 sm:py-20 lg:py-24",
            hasMedia ? "lg:grid lg:grid-cols-12 lg:items-center lg:gap-12 xl:gap-16" : "flex flex-col",
            !hasMedia && align === "center" && "items-center text-center",
          )}
        >
          <div className={cn("flex flex-col", hasMedia && "lg:col-span-7")}>
          {breadcrumbs?.length ? (
            <nav aria-label="Breadcrumb" className="mb-8">
              <ol className="flex flex-wrap items-center gap-2 text-[0.8125rem] text-mist-400">
                {breadcrumbs.map((crumb, index) => (
                  <li key={crumb.path} className="flex items-center gap-2">
                    {index > 0 ? (
                      <span aria-hidden="true" className="text-mist-600">
                        /
                      </span>
                    ) : null}
                    {index === breadcrumbs.length - 1 ? (
                      <span aria-current="page" className="text-mist-300">
                        {crumb.name}
                      </span>
                    ) : (
                      <Link href={crumb.path} className="transition-colors hover:text-white">
                        {crumb.name}
                      </Link>
                    )}
                  </li>
                ))}
              </ol>
            </nav>
          ) : null}

          <Reveal>
            <p className="flex items-center gap-2.5 text-[0.6875rem] font-semibold uppercase tracking-[0.18em] text-accent-300">
              <span aria-hidden="true" className="h-px w-6 bg-accent-300/60" />
              {eyebrow}
            </p>
          </Reveal>
          <Reveal delay={70}>
            <h1 className={cn("text-headline mt-6 max-w-3xl text-white", align === "center" && "mx-auto")}>
              {title}
            </h1>
          </Reveal>
          {lede ? (
            <Reveal delay={140}>
              <p className={cn("text-lede mt-6 max-w-2xl text-mist-300", align === "center" && "mx-auto")}>
                {lede}
              </p>
            </Reveal>
          ) : null}
          {children ? (
            <Reveal delay={200}>
              <div className="mt-9">{children}</div>
            </Reveal>
          ) : null}
          </div>

          {media ? (
            <Reveal delay={180} className="mt-12 lg:col-span-5 lg:mt-0">
              {media}
            </Reveal>
          ) : null}
        </div>
      </Container>
    </section>
  );
}

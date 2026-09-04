import Link from "next/link";
import { footerNav, legalNav } from "@/content/navigation";
import { contact, site } from "@/content/site";
import { Container } from "@/components/ui/container";
import { Logo } from "@/components/logo";
import { Arrow } from "@/components/ui/button";

const connectLinks = [
  contact.linkedin ? { label: "LinkedIn", href: contact.linkedin, external: true } : null,
  { label: "Contact", href: "/contact", external: false },
  { label: "Insights", href: "/insights", external: false },
].filter(Boolean) as { label: string; href: string; external: boolean }[];

export function SiteFooter() {
  return (
    <footer className="dark-section relative overflow-hidden bg-navy-950 text-mist-300">
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid opacity-40 mask-fade-b" />
      <Container className="relative">
        <div className="grid gap-12 border-b border-white/10 py-16 lg:grid-cols-12 lg:gap-8 lg:py-20">
          <div className="lg:col-span-4">
            <Link href="/" className="inline-flex items-center gap-2.5" aria-label="GraceWell Consulting Group — home">
              <Logo className="h-9 w-9" tone="dark" />
              <span className="text-[1.0625rem] font-semibold leading-none tracking-[-0.02em] text-white">
                GraceWell
              </span>
            </Link>
            <p className="mt-6 max-w-sm text-[0.9375rem] leading-relaxed text-mist-400">
              {site.tagline}
            </p>
            <p className="mt-4 max-w-sm text-[0.875rem] leading-relaxed text-mist-400/85">
              Data engineering consulting, modern data platforms, analytics enablement, training and
              team setup for data-intensive organizations.
            </p>

            {contact.email || contact.phone || contact.location ? (
              <address className="mt-6 space-y-1 text-[0.875rem] not-italic text-mist-400">
                {contact.email ? (
                  <a href={`mailto:${contact.email}`} className="block hover:text-white">
                    {contact.email}
                  </a>
                ) : null}
                {contact.phone ? (
                  <a href={`tel:${contact.phone.replace(/[^+\d]/g, "")}`} className="block hover:text-white">
                    {contact.phone}
                  </a>
                ) : null}
                {contact.location ? <span className="block">{contact.location}</span> : null}
              </address>
            ) : null}
          </div>

          <div className="grid grid-cols-2 gap-x-6 gap-y-10 sm:grid-cols-3 lg:col-span-8 lg:grid-cols-5">
            {footerNav.map((group) => (
              <div key={group.heading}>
                <h2 className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-white">
                  {group.heading}
                </h2>
                <ul className="mt-4 space-y-2.5">
                  {group.links.map((link) => (
                    <li key={`${group.heading}-${link.href}`}>
                      <Link
                        href={link.href}
                        className="text-[0.875rem] text-mist-400 transition-colors hover:text-white"
                      >
                        {link.label}
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
            <div>
              <h2 className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-white">
                Connect
              </h2>
              <ul className="mt-4 space-y-2.5">
                {connectLinks.map((link) => (
                  <li key={link.label}>
                    {link.external ? (
                      <a
                        href={link.href}
                        target="_blank"
                        rel="noreferrer noopener"
                        className="text-[0.875rem] text-mist-400 transition-colors hover:text-white"
                      >
                        {link.label}
                      </a>
                    ) : (
                      <Link
                        href={link.href}
                        className="text-[0.875rem] text-mist-400 transition-colors hover:text-white"
                      >
                        {link.label}
                      </Link>
                    )}
                  </li>
                ))}
                <li>
                  <Link
                    href="/contact?topic=newsletter"
                    className="group/btn inline-flex items-center gap-1.5 text-[0.875rem] text-mist-400 transition-colors hover:text-white"
                  >
                    Newsletter
                    <Arrow className="h-3.5 w-3.5" />
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div className="flex flex-col gap-6 py-8 sm:flex-row sm:items-center sm:justify-between">
          <p className="text-[0.8125rem] text-mist-400">
            © {new Date().getFullYear()} {site.name}. All rights reserved.
          </p>
          <ul className="flex flex-wrap items-center gap-x-6 gap-y-2">
            {legalNav.map((link) => (
              <li key={link.href}>
                <Link
                  href={link.href}
                  className="text-[0.8125rem] text-mist-400 transition-colors hover:text-white"
                >
                  {link.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </Container>
    </footer>
  );
}

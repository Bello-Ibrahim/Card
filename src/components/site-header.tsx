"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useCallback, useEffect, useRef, useState } from "react";
import { mainNav, type NavItem } from "@/content/navigation";
import { cta } from "@/content/site";
import { ButtonLink, Arrow } from "@/components/ui/button";
import { Container } from "@/components/ui/container";
import { Logo } from "@/components/logo";
import { cn } from "@/lib/utils";

export function SiteHeader() {
  const pathname = usePathname();
  const [scrolled, setScrolled] = useState(false);
  const [openMenu, setOpenMenu] = useState<string | null>(null);
  const [mobileOpen, setMobileOpen] = useState(false);
  const headerRef = useRef<HTMLElement>(null);
  const closeTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  // Close everything on navigation.
  useEffect(() => {
    setOpenMenu(null);
    setMobileOpen(false);
  }, [pathname]);

  // Lock body scroll while the full-screen mobile menu is open.
  useEffect(() => {
    if (!mobileOpen) return;
    const previous = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = previous;
    };
  }, [mobileOpen]);

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key !== "Escape") return;
      setOpenMenu(null);
      setMobileOpen(false);
    };
    const onPointerDown = (event: PointerEvent) => {
      if (!headerRef.current?.contains(event.target as Node)) setOpenMenu(null);
    };
    document.addEventListener("keydown", onKeyDown);
    document.addEventListener("pointerdown", onPointerDown);
    return () => {
      document.removeEventListener("keydown", onKeyDown);
      document.removeEventListener("pointerdown", onPointerDown);
    };
  }, []);

  const cancelClose = useCallback(() => {
    if (closeTimer.current) clearTimeout(closeTimer.current);
  }, []);

  const scheduleClose = useCallback(() => {
    cancelClose();
    closeTimer.current = setTimeout(() => setOpenMenu(null), 140);
  }, [cancelClose]);

  const isActive = (href: string) =>
    href === "/" ? pathname === "/" : pathname === href || pathname.startsWith(`${href}/`);

  /**
   * Every page opens with a dark masthead. While the header is still transparent over it,
   * the header has to render light-on-dark; the moment it gains its white background
   * (scrolled, mega-menu open, or mobile menu open) it flips back to dark-on-light.
   */
  const onDark = !scrolled && !openMenu && !mobileOpen;

  return (
    <>
    <header
      ref={headerRef}
      className={cn(
        "fixed inset-x-0 top-0 z-50 transition-[background-color,border-color,box-shadow] duration-300",
        onDark && "border-b border-white/0 bg-transparent",
        // Solid (not translucent) while the full-screen panel is open, so the header
        // reads as part of the same white surface rather than a tinted band over the hero.
        mobileOpen && "border-b border-navy-950/10 bg-white",
        !onDark &&
          !mobileOpen &&
          "border-b border-navy-950/10 bg-white/85 backdrop-blur-xl supports-[backdrop-filter]:bg-white/72",
      )}
      onMouseLeave={scheduleClose}
    >
      <Container className="flex h-[4.5rem] items-center justify-between gap-6 lg:h-20">
        <Link
          href="/"
          className="flex items-center gap-2.5 rounded-md"
          aria-label="GraceWell Consulting Group — home"
        >
          <Logo className="h-8 w-8" tone={onDark ? "dark" : "light"} />
          <span
            className={cn(
              "hidden text-[0.95rem] font-semibold leading-none tracking-[-0.02em] transition-colors sm:block",
              onDark ? "text-white" : "text-navy-950",
            )}
          >
            GraceWell
            <span className={cn("ml-1.5 font-normal", onDark ? "text-mist-400" : "text-mist-500")}>
              Consulting Group
            </span>
          </span>
        </Link>

        {/* Desktop navigation */}
        <nav aria-label="Primary" className="hidden xl:block">
          <ul className="flex items-center gap-0.5">
            {mainNav.map((item) => (
              <li
                key={item.href}
                className="relative"
                onMouseEnter={() => {
                  cancelClose();
                  setOpenMenu(item.menu ? item.label : null);
                }}
              >
                {item.menu ? (
                  <button
                    type="button"
                    aria-expanded={openMenu === item.label}
                    aria-controls={`menu-${item.label.toLowerCase()}`}
                    onClick={() => setOpenMenu(openMenu === item.label ? null : item.label)}
                    className={cn(
                      "flex items-center gap-1.5 rounded-full px-3.5 py-2 text-[0.875rem] font-medium transition-colors",
                      onDark
                        ? isActive(item.href)
                          ? "text-white"
                          : "text-mist-300 hover:text-white"
                        : isActive(item.href) || openMenu === item.label
                          ? "text-navy-950"
                          : "text-mist-600 hover:text-navy-950",
                    )}
                  >
                    {item.label}
                    <svg
                      viewBox="0 0 10 6"
                      aria-hidden="true"
                      className={cn(
                        "h-1.5 w-2.5 transition-transform duration-200",
                        openMenu === item.label && "rotate-180",
                      )}
                    >
                      <path
                        d="M1 1l4 4 4-4"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="1.6"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      />
                    </svg>
                  </button>
                ) : (
                  <Link
                    href={item.href}
                    aria-current={isActive(item.href) ? "page" : undefined}
                    className={cn(
                      "block rounded-full px-3.5 py-2 text-[0.875rem] font-medium transition-colors",
                      onDark
                        ? isActive(item.href)
                          ? "text-white"
                          : "text-mist-300 hover:text-white"
                        : isActive(item.href)
                          ? "text-navy-950"
                          : "text-mist-600 hover:text-navy-950",
                    )}
                  >
                    {item.label}
                  </Link>
                )}
              </li>
            ))}
          </ul>
        </nav>

        <div className="hidden items-center gap-2 xl:flex">
          <ButtonLink href={cta.primary.href} size="sm" variant={onDark ? "onDark" : "primary"}>
            {cta.primary.label}
            <Arrow />
          </ButtonLink>
        </div>

        {/* Mobile trigger */}
        <button
          type="button"
          className={cn(
            "-mr-2 flex h-11 w-11 items-center justify-center rounded-full transition-colors xl:hidden",
            onDark ? "text-white" : "text-navy-950",
          )}
          aria-expanded={mobileOpen}
          aria-controls="mobile-navigation"
          onClick={() => setMobileOpen((open) => !open)}
        >
          <span className="sr-only">{mobileOpen ? "Close menu" : "Open menu"}</span>
          <span aria-hidden="true" className="relative block h-4 w-6">
            <span
              className={cn(
                "absolute left-0 block h-[1.75px] w-6 rounded bg-current transition-transform duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]",
                mobileOpen ? "top-[7px] rotate-45" : "top-0.5",
              )}
            />
            <span
              className={cn(
                "absolute left-0 block h-[1.75px] w-6 rounded bg-current transition-transform duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]",
                mobileOpen ? "top-[7px] -rotate-45" : "top-[13px]",
              )}
            />
          </span>
        </button>
      </Container>

      {/* Desktop mega-menu panels */}
      {mainNav
        .filter((item): item is NavItem & { menu: NonNullable<NavItem["menu"]> } => Boolean(item.menu))
        .map((item) => (
          <div
            key={item.label}
            id={`menu-${item.label.toLowerCase()}`}
            hidden={openMenu !== item.label}
            onMouseEnter={cancelClose}
            className="absolute inset-x-0 top-full hidden border-b border-navy-950/10 bg-white/95 shadow-[0_24px_48px_-28px_rgba(8,17,36,0.35)] backdrop-blur-xl xl:block"
          >
            <Container className="grid grid-cols-12 gap-10 py-10">
              <div className="col-span-3">
                <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.18em] text-accent-600">
                  {item.menu.intro.title}
                </p>
                <p className="mt-3 text-[0.9375rem] leading-relaxed text-mist-600">
                  {item.menu.intro.body}
                </p>
                <Link
                  href={item.menu.intro.href}
                  className="group/btn mt-5 inline-flex items-center gap-2 text-[0.875rem] font-medium text-navy-950 hover:text-accent-600"
                >
                  {item.menu.intro.cta}
                  <Arrow />
                </Link>
              </div>
              {item.menu.columns.map((column) => (
                <div key={column.heading} className="col-span-4 xl:col-span-4">
                  <p className="mb-3 text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-mist-500">
                    {column.heading}
                  </p>
                  <ul className="space-y-0.5">
                    {column.links.map((link) => (
                      <li key={link.href}>
                        <Link
                          href={link.href}
                          className="block rounded-xl px-3 py-2.5 transition-colors hover:bg-mist-100"
                        >
                          <span className="block text-[0.9375rem] font-medium text-navy-950">
                            {link.label}
                          </span>
                          {link.description ? (
                            <span className="mt-0.5 line-clamp-1 block text-[0.8125rem] text-mist-500">
                              {link.description}
                            </span>
                          ) : null}
                        </Link>
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </Container>
          </div>
        ))}
    </header>

    {/* Full-screen mobile navigation */}
    <div
      id="mobile-navigation"
      hidden={!mobileOpen}
      className="fixed inset-x-0 bottom-0 top-[4.5rem] z-40 overflow-y-auto bg-white xl:hidden"
    >
      <nav aria-label="Mobile" className="flex min-h-full flex-col">
        <Container className="flex-1 py-6">
          <ul className="divide-y divide-navy-950/8">
            {mainNav.map((item) => (
              <li key={item.href} className="py-1">
                {item.menu ? (
                  <details className="group">
                    <summary className="flex cursor-pointer list-none items-center justify-between py-3.5 text-xl font-semibold tracking-[-0.02em] text-navy-950 [&::-webkit-details-marker]:hidden">
                      {item.label}
                      <svg viewBox="0 0 14 14" aria-hidden="true" className="h-4 w-4 text-mist-500 transition-transform group-open:rotate-45">
                        <path d="M7 1v12M1 7h12" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
                      </svg>
                    </summary>
                    <ul className="mb-3 space-y-0.5 border-l border-navy-950/10 pl-4">
                      <li>
                        <Link
                          href={item.href}
                          className="block py-2.5 text-[0.9375rem] font-medium text-accent-600"
                        >
                          {item.menu.intro.cta}
                        </Link>
                      </li>
                      {item.menu.columns.flatMap((column) => column.links).map((link) => (
                        <li key={link.href}>
                          <Link href={link.href} className="block py-2.5 text-[0.9375rem] text-mist-600">
                            {link.label}
                          </Link>
                        </li>
                      ))}
                    </ul>
                  </details>
                ) : (
                  <Link
                    href={item.href}
                    aria-current={isActive(item.href) ? "page" : undefined}
                    className="block py-3.5 text-xl font-semibold tracking-[-0.02em] text-navy-950"
                  >
                    {item.label}
                  </Link>
                )}
              </li>
            ))}
          </ul>
        </Container>
        <div className="sticky bottom-0 border-t border-navy-950/10 bg-white/95 backdrop-blur-xl">
          <Container className="flex flex-col gap-3 py-5">
            <ButtonLink href={cta.primary.href} size="lg" className="w-full">
              {cta.primary.label}
              <Arrow />
            </ButtonLink>
            <ButtonLink href={cta.secondary.href} size="lg" variant="secondary" className="w-full">
              {cta.secondary.label}
            </ButtonLink>
          </Container>
        </div>
      </nav>
    </div>
    </>
  );
}

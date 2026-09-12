"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import { Arrow } from "@/components/ui/button";
import { cn } from "@/lib/utils";

/**
 * Persistent conversion affordance.
 *
 * Desktop: a small floating button in the bottom-right. Mobile: a sticky bar above the
 * safe-area inset. Both appear only after the visitor has scrolled past the hero, stay out
 * of the way on the contact page itself, and can be dismissed for the session.
 */
export function FloatingCta() {
  const pathname = usePathname();
  const [visible, setVisible] = useState(false);
  const [dismissed, setDismissed] = useState(false);

  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > 900);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  if (pathname === "/contact" || dismissed) return null;

  return (
    <aside
      aria-label="Contact DataForge"
      className={cn(
        "pointer-events-none fixed inset-x-0 bottom-0 z-40 transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] sm:inset-x-auto sm:right-6 sm:bottom-6",
        visible ? "translate-y-0 opacity-100" : "translate-y-6 opacity-0",
      )}
    >
      <div className="pointer-events-auto flex items-center gap-2 border-t border-navy-950/10 bg-white/95 p-3 pb-[max(0.75rem,env(safe-area-inset-bottom))] backdrop-blur-xl sm:rounded-full sm:border sm:border-navy-950/10 sm:p-1.5 sm:pr-1.5 sm:shadow-lift">
        <Link
          href="/contact"
          className="group/btn inline-flex h-11 flex-1 items-center justify-center gap-2 rounded-full bg-navy-950 px-5 text-[0.875rem] font-medium text-white transition-colors hover:bg-accent-600 sm:flex-none"
        >
          <span className="sm:hidden">Start a Conversation</span>
          <span className="hidden sm:inline">Talk to a Data Expert</span>
          <Arrow />
        </Link>
        <button
          type="button"
          onClick={() => setDismissed(true)}
          className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full text-mist-500 transition-colors hover:bg-mist-100 hover:text-navy-950 sm:h-9 sm:w-9"
        >
          <span className="sr-only">Dismiss</span>
          <svg viewBox="0 0 14 14" aria-hidden="true" className="h-3.5 w-3.5">
            <path d="M1 1l12 12M13 1L1 13" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
          </svg>
        </button>
      </div>
    </aside>
  );
}

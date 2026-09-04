import type { Faq } from "@/content/faqs";

export function FaqAccordion({ faqs, tone = "light" }: { faqs: Faq[]; tone?: "light" | "dark" }) {
  const dark = tone === "dark";
  return (
    <div className={dark ? "divide-y divide-white/10 border-y border-white/10" : "divide-y divide-navy-950/8 border-y border-navy-950/8"}>
      {faqs.map((faq) => (
        <details key={faq.question} className="group">
          <summary
            className={`flex cursor-pointer list-none items-start justify-between gap-6 py-5 text-[1.0625rem] font-medium tracking-[-0.015em] transition-colors [&::-webkit-details-marker]:hidden ${
              dark ? "text-white hover:text-accent-300" : "text-navy-950 hover:text-accent-600"
            }`}
          >
            {faq.question}
            <svg
              viewBox="0 0 14 14"
              aria-hidden="true"
              className={`mt-1.5 h-3.5 w-3.5 shrink-0 transition-transform duration-300 group-open:rotate-45 ${
                dark ? "text-mist-400" : "text-mist-500"
              }`}
            >
              <path d="M7 1v12M1 7h12" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
            </svg>
          </summary>
          <p className={`max-w-3xl pb-6 text-[0.9375rem] leading-relaxed ${dark ? "text-mist-300" : "text-mist-600"}`}>
            {faq.answer}
          </p>
        </details>
      ))}
    </div>
  );
}

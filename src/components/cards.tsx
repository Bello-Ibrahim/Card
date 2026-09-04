import Link from "next/link";
import { Arrow } from "@/components/ui/button";
import { Icon, type IconName } from "@/components/ui/icon";
import { cn, formatDate } from "@/lib/utils";
import type { Service } from "@/content/services";
import type { Solution } from "@/content/solutions";
import type { Industry } from "@/content/industries";
import type { Insight } from "@/content/insights";
import type { CaseStudy } from "@/content/case-studies";

const cardBase =
  "group/card relative flex h-full flex-col rounded-2xl border border-navy-950/8 bg-white p-7 transition-[border-color,box-shadow,transform] duration-300 ease-[cubic-bezier(0.16,1,0.3,1)] hover:-translate-y-0.5 hover:border-navy-950/16 hover:shadow-lift";

export function ServiceCard({ service }: { service: Service }) {
  return (
    <article className={cardBase}>
      <span
        aria-hidden="true"
        className="mb-6 inline-flex h-11 w-11 items-center justify-center rounded-xl bg-navy-950/[0.04] text-navy-800 transition-colors duration-300 group-hover/card:bg-accent-500 group-hover/card:text-white"
      >
        <Icon name={service.icon as IconName} className="h-5 w-5" />
      </span>
      <h3 className="text-[1.125rem] font-semibold tracking-[-0.02em] text-navy-950">
        <Link href={`/services/${service.slug}`} className="before:absolute before:inset-0">
          {service.title}
        </Link>
      </h3>
      <p className="mt-3 flex-1 text-[0.9375rem] leading-relaxed text-mist-600">{service.summary}</p>
      <span className="mt-6 inline-flex items-center gap-2 text-[0.875rem] font-medium text-navy-950 transition-colors group-hover/card:text-accent-600">
        Explore service
        <Arrow />
      </span>
    </article>
  );
}

export function SolutionCard({ solution }: { solution: Solution }) {
  return (
    <article className={cardBase}>
      <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-600">
        {solution.category}
      </p>
      <h3 className="mt-3 text-[1.125rem] font-semibold tracking-[-0.02em] text-navy-950">
        <Link href={`/solutions/${solution.slug}`} className="before:absolute before:inset-0">
          {solution.title}
        </Link>
      </h3>
      <p className="mt-3 text-[0.9375rem] leading-relaxed text-mist-600">{solution.summary}</p>

      <ul className="mt-5 flex flex-wrap gap-1.5">
        {solution.capabilities.slice(0, 4).map((capability) => (
          <li
            key={capability}
            className="rounded-full border border-navy-950/8 bg-mist-50 px-2.5 py-1 text-[0.75rem] text-mist-600"
          >
            {capability}
          </li>
        ))}
      </ul>

      <div className="mt-6 flex-1" />
      <span className="inline-flex items-center gap-2 text-[0.875rem] font-medium text-navy-950 transition-colors group-hover/card:text-accent-600">
        {solution.cta}
        <Arrow />
      </span>
    </article>
  );
}

export function IndustryCard({ industry }: { industry: Industry }) {
  return (
    <article className={cn(cardBase, "p-6 sm:p-7")}>
      <h3 className="text-[1.0625rem] font-semibold tracking-[-0.02em] text-navy-950">
        {industry.name}
      </h3>
      <p className="mt-2.5 text-[0.9375rem] font-medium leading-snug text-accent-700">
        {industry.headline}
      </p>
      <p className="mt-3 flex-1 text-[0.875rem] leading-relaxed text-mist-600">
        {industry.description}
      </p>
      <ul className="mt-5 space-y-1.5 border-t border-navy-950/8 pt-4">
        {industry.focus.map((item) => (
          <li key={item} className="flex items-start gap-2 text-[0.8125rem] text-mist-500">
            <span aria-hidden="true" className="mt-[0.45rem] h-1 w-1 shrink-0 rounded-full bg-accent-500" />
            {item}
          </li>
        ))}
      </ul>
    </article>
  );
}

export function InsightCard({ insight, featured = false }: { insight: Insight; featured?: boolean }) {
  return (
    <article className={cn(cardBase, featured && "bg-mist-50")}>
      <div className="flex items-center gap-3 text-[0.75rem] text-mist-500">
        <span className="font-medium text-accent-600">{insight.category}</span>
        <span aria-hidden="true" className="h-1 w-1 rounded-full bg-mist-300" />
        <span>{insight.readingTime} min read</span>
      </div>
      <h3
        className={cn(
          "mt-4 font-semibold tracking-[-0.02em] text-navy-950",
          featured ? "text-[1.375rem] leading-snug" : "text-[1.0625rem] leading-snug",
        )}
      >
        <Link href={`/insights/${insight.slug}`} className="before:absolute before:inset-0">
          {insight.title}
        </Link>
      </h3>
      <p className="mt-3 flex-1 text-[0.9375rem] leading-relaxed text-mist-600">{insight.excerpt}</p>
      <div className="mt-6 flex items-center justify-between gap-4 border-t border-navy-950/8 pt-4">
        <time dateTime={insight.publishedAt} className="text-[0.8125rem] text-mist-500">
          {formatDate(insight.publishedAt)}
        </time>
        <span className="inline-flex items-center gap-2 text-[0.875rem] font-medium text-navy-950 transition-colors group-hover/card:text-accent-600">
          Read
          <Arrow />
        </span>
      </div>
    </article>
  );
}

export function CaseStudyCard({ caseStudy }: { caseStudy: CaseStudy }) {
  return (
    <article className="group/card flex h-full flex-col rounded-2xl border border-white/12 bg-white/[0.04] p-7 transition-[border-color,background-color] duration-300 hover:border-white/25 hover:bg-white/[0.07]">
      <div className="flex items-center gap-3">
        <p className="text-[0.6875rem] font-semibold uppercase tracking-[0.16em] text-accent-300">
          Case Study
        </p>
        {!caseStudy.verified ? (
          <span className="rounded-full border border-white/15 px-2 py-0.5 text-[0.6875rem] text-mist-400">
            Illustrative
          </span>
        ) : null}
      </div>
      <h3 className="mt-4 text-[1.1875rem] font-semibold leading-snug tracking-[-0.02em] text-white">
        {caseStudy.title}
      </h3>

      <dl className="mt-6 flex-1 space-y-4">
        {(
          [
            ["Challenge", caseStudy.challenge],
            ["Approach", caseStudy.approach],
            ["Outcome", caseStudy.outcome],
          ] as const
        ).map(([term, description]) => (
          <div key={term}>
            <dt className="text-[0.75rem] font-semibold uppercase tracking-[0.12em] text-mist-400">
              {term}
            </dt>
            <dd className="mt-1.5 text-[0.875rem] leading-relaxed text-mist-300">{description}</dd>
          </div>
        ))}
      </dl>

      <Link
        href={`/case-studies/${caseStudy.slug}`}
        className="mt-7 inline-flex items-center gap-2 text-[0.875rem] font-medium text-white transition-colors hover:text-accent-300"
      >
        View Case Study
        <Arrow />
      </Link>
    </article>
  );
}

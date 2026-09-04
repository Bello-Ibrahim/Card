"use client";

import { useDeferredValue, useId, useMemo, useState } from "react";
import { InsightCard } from "@/components/cards";
import { insightCategories, type Insight } from "@/content/insights";
import { cn } from "@/lib/utils";

const ALL = "All";

export function InsightsExplorer({ insights }: { insights: Insight[] }) {
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState<string>(ALL);
  const deferredQuery = useDeferredValue(query);
  const searchId = useId();

  const available = useMemo(
    () => [ALL, ...insightCategories.filter((c) => insights.some((i) => i.category === c))],
    [insights],
  );

  const results = useMemo(() => {
    const needle = deferredQuery.trim().toLowerCase();
    return insights.filter((insight) => {
      if (category !== ALL && insight.category !== category) return false;
      if (!needle) return true;
      return (
        insight.title.toLowerCase().includes(needle) ||
        insight.excerpt.toLowerCase().includes(needle) ||
        insight.category.toLowerCase().includes(needle)
      );
    });
  }, [insights, deferredQuery, category]);

  return (
    <div>
      <div className="flex flex-col gap-5 lg:flex-row lg:items-center lg:justify-between">
        <div className="relative w-full lg:max-w-sm">
          <label htmlFor={searchId} className="sr-only">
            Search insights
          </label>
          <svg
            viewBox="0 0 16 16"
            aria-hidden="true"
            className="pointer-events-none absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-mist-500"
          >
            <circle cx="7" cy="7" r="4.6" fill="none" stroke="currentColor" strokeWidth="1.5" />
            <path d="m10.6 10.6 3 3" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
          </svg>
          <input
            id={searchId}
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Search insights"
            className="h-12 w-full rounded-full border border-navy-950/10 bg-white pl-11 pr-4 text-[0.9375rem] text-navy-950 placeholder:text-mist-500 focus:border-accent-500 focus:outline-none focus:ring-2 focus:ring-accent-500/25"
          />
        </div>

        <div
          role="group"
          aria-label="Filter by category"
          className="scroll-rail -mx-5 flex gap-2 overflow-x-auto px-5 lg:mx-0 lg:flex-wrap lg:justify-end lg:overflow-visible lg:px-0"
        >
          {available.map((item) => (
            <button
              key={item}
              type="button"
              aria-pressed={category === item}
              onClick={() => setCategory(item)}
              className={cn(
                "shrink-0 rounded-full border px-4 py-2 text-[0.8125rem] font-medium transition-colors",
                category === item
                  ? "border-navy-950 bg-navy-950 text-white"
                  : "border-navy-950/10 bg-white text-mist-600 hover:border-navy-950/25 hover:text-navy-950",
              )}
            >
              {item}
            </button>
          ))}
        </div>
      </div>

      <p aria-live="polite" className="mt-6 text-[0.8125rem] text-mist-500">
        {results.length} {results.length === 1 ? "article" : "articles"}
        {category !== ALL ? ` in ${category}` : ""}
        {deferredQuery.trim() ? ` matching “${deferredQuery.trim()}”` : ""}
      </p>

      {results.length ? (
        <ul className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {results.map((insight) => (
            <li key={insight.slug}>
              <InsightCard insight={insight} />
            </li>
          ))}
        </ul>
      ) : (
        <div className="mt-8 rounded-2xl border border-dashed border-navy-950/15 bg-mist-50 p-12 text-center">
          <p className="text-[1.0625rem] font-medium text-navy-950">No articles match that search.</p>
          <p className="mt-2 text-[0.9375rem] text-mist-600">
            Try a broader term, or clear the category filter.
          </p>
          <button
            type="button"
            onClick={() => {
              setQuery("");
              setCategory(ALL);
            }}
            className="mt-5 rounded-full border border-navy-950/15 px-4 py-2 text-[0.875rem] font-medium text-navy-950 transition-colors hover:bg-white"
          >
            Reset filters
          </button>
        </div>
      )}
    </div>
  );
}

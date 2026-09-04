import type { MetadataRoute } from "next";
import { site } from "@/content/site";
import { services } from "@/content/services";
import { solutions } from "@/content/solutions";
import { insights } from "@/content/insights";
import { caseStudies } from "@/content/case-studies";

export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();
  const url = (path: string) => `${site.url}${path}`;

  const core: MetadataRoute.Sitemap = [
    { url: url("/"), lastModified: now, changeFrequency: "monthly", priority: 1 },
    { url: url("/services"), lastModified: now, changeFrequency: "monthly", priority: 0.9 },
    { url: url("/solutions"), lastModified: now, changeFrequency: "monthly", priority: 0.9 },
    { url: url("/industries"), lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: url("/training"), lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: url("/team-setup"), lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: url("/case-studies"), lastModified: now, changeFrequency: "monthly", priority: 0.7 },
    { url: url("/about"), lastModified: now, changeFrequency: "monthly", priority: 0.7 },
    { url: url("/insights"), lastModified: now, changeFrequency: "weekly", priority: 0.8 },
    { url: url("/contact"), lastModified: now, changeFrequency: "yearly", priority: 0.9 },
    { url: url("/privacy-policy"), lastModified: now, changeFrequency: "yearly", priority: 0.2 },
    { url: url("/terms-of-use"), lastModified: now, changeFrequency: "yearly", priority: 0.2 },
    { url: url("/cookie-policy"), lastModified: now, changeFrequency: "yearly", priority: 0.2 },
  ];

  return [
    ...core,
    ...services.map((service) => ({
      url: url(`/services/${service.slug}`),
      lastModified: now,
      changeFrequency: "monthly" as const,
      priority: 0.8,
    })),
    ...solutions.map((solution) => ({
      url: url(`/solutions/${solution.slug}`),
      lastModified: now,
      changeFrequency: "monthly" as const,
      priority: 0.8,
    })),
    ...caseStudies.map((study) => ({
      url: url(`/case-studies/${study.slug}`),
      lastModified: now,
      changeFrequency: "yearly" as const,
      priority: 0.6,
    })),
    ...insights.map((insight) => ({
      url: url(`/insights/${insight.slug}`),
      lastModified: new Date(`${insight.publishedAt}T00:00:00Z`),
      changeFrequency: "yearly" as const,
      priority: 0.6,
    })),
  ];
}

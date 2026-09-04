import { contact, site } from "@/content/site";
import { services } from "@/content/services";
import type { Faq } from "@/content/faqs";
import type { Insight } from "@/content/insights";

const sameAs = [contact.linkedin, contact.x, contact.youtube].filter(
  (value): value is string => Boolean(value),
);

export function organizationSchema() {
  return {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": `${site.url}/#organization`,
    name: site.name,
    alternateName: site.shortName,
    url: site.url,
    description: site.description,
    slogan: site.tagline,
    ...(sameAs.length ? { sameAs } : {}),
    ...(contact.email
      ? {
          contactPoint: [
            {
              "@type": "ContactPoint",
              contactType: "sales",
              email: contact.email,
              ...(contact.phone ? { telephone: contact.phone } : {}),
              availableLanguage: ["English"],
            },
          ],
        }
      : {}),
    knowsAbout: [
      "Data engineering",
      "Data platform architecture",
      "Cloud data engineering",
      "Data warehousing",
      "Lakehouse architecture",
      "Data integration",
      "Data migration",
      "Analytics engineering",
      "Data quality and observability",
      "Data governance",
      "Data engineering training",
    ],
    makesOffer: services.map((service) => ({
      "@type": "Offer",
      itemOffered: {
        "@type": "Service",
        name: service.title,
        description: service.summary,
        url: `${site.url}/services/${service.slug}`,
      },
    })),
  };
}

export function websiteSchema() {
  return {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": `${site.url}/#website`,
    url: site.url,
    name: site.name,
    description: site.description,
    publisher: { "@id": `${site.url}/#organization` },
  };
}

export function serviceSchema(input: {
  name: string;
  description: string;
  path: string;
  serviceType?: string;
}) {
  return {
    "@context": "https://schema.org",
    "@type": "Service",
    name: input.name,
    description: input.description,
    url: `${site.url}${input.path}`,
    serviceType: input.serviceType ?? input.name,
    provider: { "@id": `${site.url}/#organization` },
    areaServed: "Global",
  };
}

export function articleSchema(insight: Insight) {
  return {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: insight.title,
    description: insight.excerpt,
    url: `${site.url}/insights/${insight.slug}`,
    datePublished: insight.publishedAt,
    dateModified: insight.publishedAt,
    articleSection: insight.category,
    inLanguage: "en",
    author: { "@type": "Organization", name: site.name, url: site.url },
    publisher: { "@id": `${site.url}/#organization` },
    mainEntityOfPage: { "@type": "WebPage", "@id": `${site.url}/insights/${insight.slug}` },
  };
}

export function faqSchema(faqs: Faq[]) {
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faqs.map((faq) => ({
      "@type": "Question",
      name: faq.question,
      acceptedAnswer: { "@type": "Answer", text: faq.answer },
    })),
  };
}

export function breadcrumbSchema(items: { name: string; path: string }[]) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, index) => ({
      "@type": "ListItem",
      position: index + 1,
      name: item.name,
      item: `${site.url}${item.path}`,
    })),
  };
}

import { notFound } from "next/navigation";
import { renderOgImage, OG_SIZE, OG_CONTENT_TYPE } from "@/lib/og";
import { insights, getInsight } from "@/content/insights";

export const size = OG_SIZE;
export const contentType = OG_CONTENT_TYPE;
export const alt = "GraceWell Consulting Group insight";

export function generateStaticParams() {
  return insights.map((insight) => ({ slug: insight.slug }));
}

export default async function Image({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const insight = getInsight(slug);
  if (!insight) notFound();
  return renderOgImage({ eyebrow: insight.category, title: insight.title });
}

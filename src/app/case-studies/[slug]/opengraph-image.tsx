import { notFound } from "next/navigation";
import { renderOgImage, OG_SIZE, OG_CONTENT_TYPE } from "@/lib/og";
import { caseStudies, getCaseStudy } from "@/content/case-studies";

export const size = OG_SIZE;
export const contentType = OG_CONTENT_TYPE;
export const alt = "DataForge Consulting case study";

export function generateStaticParams() {
  return caseStudies.map((study) => ({ slug: study.slug }));
}

export default async function Image({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const study = getCaseStudy(slug);
  if (!study) notFound();
  return renderOgImage({
    eyebrow: study.verified ? "Case Study" : "Case Study · Illustrative",
    title: study.title,
  });
}

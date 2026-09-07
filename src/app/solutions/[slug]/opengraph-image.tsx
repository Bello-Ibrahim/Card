import { notFound } from "next/navigation";
import { renderOgImage, OG_SIZE, OG_CONTENT_TYPE } from "@/lib/og";
import { solutions, getSolution } from "@/content/solutions";

export const size = OG_SIZE;
export const contentType = OG_CONTENT_TYPE;
export const alt = "GraceWell Consulting Group solution";

export function generateStaticParams() {
  return solutions.map((solution) => ({ slug: solution.slug }));
}

export default async function Image({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const solution = getSolution(slug);
  if (!solution) notFound();
  return renderOgImage({ eyebrow: "Solution", title: solution.title });
}

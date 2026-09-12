import { notFound } from "next/navigation";
import { renderOgImage, OG_SIZE, OG_CONTENT_TYPE } from "@/lib/og";
import { services, getService } from "@/content/services";

export const size = OG_SIZE;
export const contentType = OG_CONTENT_TYPE;
export const alt = "DataForge Consulting service";

export function generateStaticParams() {
  return services.map((service) => ({ slug: service.slug }));
}

export default async function Image({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const service = getService(slug);
  if (!service) notFound();
  return renderOgImage({ eyebrow: "Service", title: service.title });
}

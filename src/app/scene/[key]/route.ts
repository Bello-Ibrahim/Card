import { photos, type PhotoKey } from "@/content/media";
import { renderSceneSvg } from "@/lib/scene-svg";

/**
 * Designed scenes served as cacheable SVG images.
 *
 * Rendering them inline cost several hundred DOM nodes per slot — nineteen slots took the
 * home page past 8,000 elements. As image routes each slot costs one <img>, the browser can
 * lazy-load and cache them, and a scene reused across pages is fetched once. They are
 * prerendered at build time, so there is no request-time render cost.
 */

export const dynamic = "force-static";

export function generateStaticParams() {
  return Object.keys(photos).map((key) => ({ key }));
}

export async function GET(_request: Request, { params }: { params: Promise<{ key: string }> }) {
  const { key } = await params;
  const photo = photos[key as PhotoKey];
  if (!photo) return new Response("Not found", { status: 404 });

  return new Response(renderSceneSvg(photo.scene, key), {
    headers: {
      "content-type": "image/svg+xml; charset=utf-8",
      "cache-control": "public, max-age=31536000, immutable",
    },
  });
}

import Image from "next/image";
import { photos, type PhotoKey } from "@/content/media";
import { cn } from "@/lib/utils";

/**
 * A photographic slot.
 *
 * Renders the licensed photograph when `src` is set in the manifest, and a designed scene
 * until then. The two paths share the same box, ratio and overlay treatment, so supplying a
 * photograph changes the picture without changing any layout around it.
 */
export function Photo({
  name,
  className,
  imgClassName,
  priority = false,
  sizes = "100vw",
  overlay = "none",
  zoomOnHover = false,
}: {
  name: PhotoKey;
  className?: string;
  imgClassName?: string;
  /** Set only for an above-the-fold image; everything else lazy-loads. */
  priority?: boolean;
  sizes?: string;
  /**
   * Must include a positioning utility (`relative`, or `absolute inset-0` when filling a
   * parent). Photo deliberately sets none of its own, so callers can position it freely
   * without two position utilities fighting in the cascade.
   */
  overlay?: "none" | "soft" | "strong" | "bottom";
  zoomOnHover?: boolean;
}) {
  const photo = photos[name];

  const overlayClass = {
    none: null,
    soft: "bg-gradient-to-br from-ink-950/45 via-ink-950/15 to-transparent",
    strong: "bg-ink-950/55",
    bottom: "bg-gradient-to-t from-ink-950 via-ink-950/55 to-transparent",
  }[overlay];

  const motion = zoomOnHover
    ? "transition-transform duration-[1200ms] ease-[cubic-bezier(0.16,1,0.3,1)] group-hover/media:scale-[1.06] motion-reduce:transition-none motion-reduce:group-hover/media:scale-100"
    : "";

  return (
    <div className={cn("group/media overflow-hidden bg-navy-950", className)}>
      {photo.src ? (
        <Image
          src={photo.src}
          alt={photo.alt}
          fill
          sizes={sizes}
          priority={priority}
          className={cn("object-cover", motion, imgClassName)}
        />
      ) : (
        /* eslint-disable-next-line @next/next/no-img-element -- a prerendered SVG route needs
           no optimization pipeline, and next/image would add a request for no benefit. */
        <img
          src={`/scene/${name}`}
          alt=""
          aria-hidden="true"
          loading={priority ? "eager" : "lazy"}
          decoding="async"
          className={cn("absolute inset-0 h-full w-full object-cover", motion, imgClassName)}
        />
      )}
      {overlayClass ? <div aria-hidden="true" className={cn("absolute inset-0", overlayClass)} /> : null}
    </div>
  );
}

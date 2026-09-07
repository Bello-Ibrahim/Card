import { CoverArt, type CoverVariant } from "./cover-art";
import { cn } from "@/lib/utils";

/**
 * Framed presentation of a generated cover, used in page mastheads and as a card image.
 * The frame and inner ratio are fixed so every page's artwork sits on the same grid.
 */
export function CoverBanner({
  seed,
  variant,
  className,
  ratio = "aspect-[16/10]",
}: {
  seed: string;
  variant: CoverVariant;
  className?: string;
  ratio?: string;
}) {
  return (
    <div
      className={cn(
        "relative overflow-hidden rounded-2xl border border-white/12 shadow-[0_30px_60px_-30px_rgba(0,0,0,0.8)]",
        className,
      )}
    >
      <div className={ratio}>
        <CoverArt seed={seed} variant={variant} />
      </div>
    </div>
  );
}

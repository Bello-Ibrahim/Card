import { createRandom, fix, hashSeed } from "@/lib/art";
import { cn } from "@/lib/utils";

/**
 * Small architectural glyph used as a quiet identifying mark on cards.
 *
 * A 4×4 lattice with a deterministic subset of cells promoted to filled nodes and short
 * connectors — reads as a data structure rather than as decoration, and stays legible at
 * 48px. Decorative, so it is hidden from assistive technology.
 */
export function Motif({
  seed,
  className,
  size = 56,
}: {
  seed: string;
  className?: string;
  size?: number;
}) {
  const rng = createRandom(seed);
  const uid = hashSeed(`motif:${seed}`).toString(36);
  const grid = 4;
  const step = 12;
  const offset = 6;

  const cells: { x: number; y: number; on: boolean }[] = [];
  for (let r = 0; r < grid; r += 1) {
    for (let c = 0; c < grid; c += 1) {
      cells.push({ x: offset + c * step, y: offset + r * step, on: rng() > 0.62 });
    }
  }
  const links = cells
    .map((cell, i) => ({ cell, i }))
    .filter(({ cell, i }) => cell.on && i % grid !== grid - 1 && cells[i + 1]?.on);

  return (
    <svg
      viewBox={`0 0 ${offset * 2 + (grid - 1) * step} ${offset * 2 + (grid - 1) * step}`}
      width={size}
      height={size}
      aria-hidden="true"
      focusable="false"
      className={cn("shrink-0", className)}
    >
      <defs>
        <linearGradient id={`gw-motif-${uid}`} x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="var(--color-accent-500)" />
          <stop offset="100%" stopColor="var(--color-cyan-500)" />
        </linearGradient>
      </defs>
      {links.map(({ cell }, i) => (
        <line
          key={`l-${i}`}
          x1={fix(cell.x)}
          y1={fix(cell.y)}
          x2={fix(cell.x + step)}
          y2={fix(cell.y)}
          stroke={`url(#gw-motif-${uid})`}
          strokeWidth={1.2}
          opacity={0.5}
        />
      ))}
      {cells.map((cell, i) =>
        cell.on ? (
          <circle key={i} cx={fix(cell.x)} cy={fix(cell.y)} r={2.3} fill={`url(#gw-motif-${uid})`} />
        ) : (
          <circle key={i} cx={fix(cell.x)} cy={fix(cell.y)} r={1} fill="currentColor" opacity={0.22} />
        ),
      )}
    </svg>
  );
}

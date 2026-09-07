import { ACCENT_RAMP, ART_COLORS, between, createRandom, fix, hashSeed, intBetween, type Rng } from "@/lib/art";
import { cn } from "@/lib/utils";

/**
 * Generated cover art.
 *
 * Original, deterministic SVG built from a string seed — no stock photography, no external
 * request, no licensing question, and no image bytes to download. Each variant is an abstract
 * reading of the subject (pipelines, strata, meshes) rather than decoration, which keeps the
 * site's visual language architectural in the way the brand direction asks for.
 *
 * Purely decorative: rendered `aria-hidden`, since the adjacent heading carries the meaning.
 */

export type CoverVariant =
  | "flow"
  | "strata"
  | "mesh"
  | "radial"
  | "field"
  | "embedding"
  | "tree"
  | "steps";

const W = 800;
const H = 450;

/** Orthogonal-ish path with softened corners. */
function roundedPath(points: [number, number][], radius = 14) {
  if (points.length < 2) return "";
  let d = `M${fix(points[0][0])} ${fix(points[0][1])}`;
  for (let i = 1; i < points.length - 1; i += 1) {
    const [px, py] = points[i - 1];
    const [cx, cy] = points[i];
    const [nx, ny] = points[i + 1];
    const d1 = Math.hypot(cx - px, cy - py) || 1;
    const d2 = Math.hypot(nx - cx, ny - cy) || 1;
    const r = Math.min(radius, d1 / 2, d2 / 2);
    d += ` L${fix(cx + ((px - cx) / d1) * r)} ${fix(cy + ((py - cy) / d1) * r)}`;
    d += ` Q${fix(cx)} ${fix(cy)} ${fix(cx + ((nx - cx) / d2) * r)} ${fix(cy + ((ny - cy) / d2) * r)}`;
  }
  const last = points[points.length - 1];
  return `${d} L${fix(last[0])} ${fix(last[1])}`;
}

function Node({ x, y, r = 3.4, fill }: { x: number; y: number; r?: number; fill: string }) {
  // The halo is only legible on the larger nodes, so smaller ones skip it and save an element.
  if (r < 3) return <circle cx={fix(x)} cy={fix(y)} r={fix(r)} fill={fill} />;
  return (
    <g>
      <circle cx={fix(x)} cy={fix(y)} r={fix(r * 2.6)} fill={fill} opacity={0.14} />
      <circle cx={fix(x)} cy={fix(y)} r={fix(r)} fill={fill} />
    </g>
  );
}

/* ------------------------------------------------------------------ variants */

function Flow(rng: Rng) {
  const lanes = 5;
  return (
    <g>
      {Array.from({ length: lanes }, (_, i) => {
        const baseY = 70 + i * ((H - 140) / (lanes - 1));
        const bend1 = between(rng, 200, 330);
        const bend2 = between(rng, 470, 620);
        const drift = between(rng, -46, 46);
        const points: [number, number][] = [
          [40, baseY],
          [bend1, baseY],
          [bend1, baseY + drift],
          [bend2, baseY + drift],
          [bend2, baseY],
          [W - 40, baseY],
        ];
        const strong = rng() > 0.55;
        const color = ACCENT_RAMP[i % ACCENT_RAMP.length];
        return (
          <g key={i}>
            <path
              d={roundedPath(points)}
              fill="none"
              stroke={strong ? color : "#ffffff"}
              strokeWidth={strong ? 2 : 1.1}
              opacity={strong ? 0.85 : 0.22}
              strokeLinecap="round"
            />
            {strong ? <Node x={bend2} y={baseY + drift} fill={color} /> : null}
          </g>
        );
      })}
    </g>
  );
}

function Strata(rng: Rng) {
  const bands = 5;
  const gap = 12;
  const bandH = (H - 120 - gap * (bands - 1)) / bands;
  const connectors = Array.from({ length: 3 }, () => between(rng, 140, W - 140));
  return (
    <g>
      {Array.from({ length: bands }, (_, i) => {
        const y = 60 + i * (bandH + gap);
        const inset = 40 + i * between(rng, 4, 22);
        const emphasis = i === intBetween(rng, 1, bands - 2);
        return (
          <rect
            key={i}
            x={fix(inset)}
            y={fix(y)}
            width={fix(W - inset * 2)}
            height={fix(bandH)}
            rx={10}
            fill={emphasis ? ART_COLORS.accent : "#ffffff"}
            opacity={emphasis ? 0.18 : 0.045}
            stroke={emphasis ? ART_COLORS.accentSoft : "#ffffff"}
            strokeOpacity={emphasis ? 0.5 : 0.14}
          />
        );
      })}
      {connectors.map((x, i) => (
        <g key={`c-${i}`}>
          <line
            x1={fix(x)}
            y1={60}
            x2={fix(x)}
            y2={H - 60}
            stroke={ACCENT_RAMP[i % ACCENT_RAMP.length]}
            strokeWidth={1.4}
            opacity={0.55}
          />
          <Node x={x} y={between(rng, 90, H - 90)} fill={ACCENT_RAMP[i % ACCENT_RAMP.length]} />
        </g>
      ))}
    </g>
  );
}

function Mesh(rng: Rng) {
  const cols = 5;
  const rows = 3;
  const nodes: { x: number; y: number; c: string }[] = [];
  for (let r = 0; r < rows; r += 1) {
    for (let c = 0; c < cols; c += 1) {
      if (rng() > 0.86) continue;
      nodes.push({
        x: 80 + c * ((W - 160) / (cols - 1)) + between(rng, -22, 22),
        y: 70 + r * ((H - 140) / (rows - 1)) + between(rng, -20, 20),
        c: ACCENT_RAMP[(r + c) % ACCENT_RAMP.length],
      });
    }
  }
  const edges: [number, number][] = [];
  nodes.forEach((n, i) => {
    const near = nodes
      .map((m, j) => ({ j, d: Math.hypot(m.x - n.x, m.y - n.y) }))
      .filter((e) => e.j !== i)
      .sort((a, b) => a.d - b.d)
      .slice(0, 2);
    near.forEach((e) => {
      if (!edges.some(([a, b]) => (a === e.j && b === i) || (a === i && b === e.j))) {
        edges.push([i, e.j]);
      }
    });
  });
  return (
    <g>
      {edges.map(([a, b], i) => (
        <line
          key={i}
          x1={fix(nodes[a].x)}
          y1={fix(nodes[a].y)}
          x2={fix(nodes[b].x)}
          y2={fix(nodes[b].y)}
          stroke="#ffffff"
          strokeWidth={1}
          opacity={0.2}
        />
      ))}
      {nodes.map((n, i) => (
        <Node key={i} x={n.x} y={n.y} r={i % 4 === 0 ? 4.4 : 2.8} fill={n.c} />
      ))}
    </g>
  );
}

function Radial(rng: Rng) {
  const cx = W * 0.68;
  const cy = H * 0.52;
  const rings = 5;
  const spokes = 7;
  return (
    <g>
      {Array.from({ length: rings }, (_, i) => {
        const r = 52 + i * 46;
        const start = between(rng, -0.6, 0.6);
        const sweep = between(rng, 2.0, 4.4);
        const x1 = cx + r * Math.cos(start);
        const y1 = cy + r * Math.sin(start);
        const x2 = cx + r * Math.cos(start + sweep);
        const y2 = cy + r * Math.sin(start + sweep);
        return (
          <path
            key={i}
            d={`M${fix(x1)} ${fix(y1)} A${fix(r)} ${fix(r)} 0 ${sweep > Math.PI ? 1 : 0} 1 ${fix(x2)} ${fix(y2)}`}
            fill="none"
            stroke={i === rings - 2 ? ART_COLORS.cyan : "#ffffff"}
            strokeWidth={i === rings - 2 ? 2 : 1.1}
            opacity={i === rings - 2 ? 0.8 : 0.22}
            strokeLinecap="round"
          />
        );
      })}
      {Array.from({ length: spokes }, (_, i) => {
        const a = (i / spokes) * Math.PI * 2;
        const inner = 40;
        const outer = 52 + (rings - 1) * 46;
        return (
          <line
            key={`s-${i}`}
            x1={fix(cx + inner * Math.cos(a))}
            y1={fix(cy + inner * Math.sin(a))}
            x2={fix(cx + outer * Math.cos(a))}
            y2={fix(cy + outer * Math.sin(a))}
            stroke="#ffffff"
            strokeWidth={0.9}
            opacity={0.13}
          />
        );
      })}
      <Node x={cx} y={cy} r={5} fill={ART_COLORS.accentSoft} />
      {Array.from({ length: 4 }, (_, i) => {
        const a = between(rng, 0, Math.PI * 2);
        const r = 52 + intBetween(rng, 0, rings - 1) * 46;
        return (
          <Node
            key={`n-${i}`}
            x={cx + r * Math.cos(a)}
            y={cy + r * Math.sin(a)}
            fill={ACCENT_RAMP[i % ACCENT_RAMP.length]}
          />
        );
      })}
    </g>
  );
}

function Field(rng: Rng) {
  const bars = 18;
  const baseline = H - 74;
  const step = (W - 96) / bars;
  const heights = Array.from({ length: bars }, (_, i) =>
    between(rng, 24, 190) * (0.55 + 0.45 * Math.sin((i / bars) * Math.PI)),
  );
  const trend = heights.map((h, i) => [48 + i * step + step / 2, baseline - h * 0.72] as [number, number]);
  return (
    <g>
      {heights.map((h, i) => (
        <rect
          key={i}
          x={fix(48 + i * step)}
          y={fix(baseline - h)}
          width={fix(step * 0.52)}
          height={fix(h)}
          rx={3}
          fill="#ffffff"
          opacity={0.09}
        />
      ))}
      <path
        d={roundedPath(trend, 6)}
        fill="none"
        stroke={ART_COLORS.cyan}
        strokeWidth={2.1}
        opacity={0.9}
        strokeLinecap="round"
      />
      <line x1={40} y1={fix(baseline)} x2={W - 40} y2={fix(baseline)} stroke="#ffffff" strokeWidth={1} opacity={0.22} />
      {[0.28, 0.62, 0.86].map((t, i) => {
        const p = trend[Math.floor(t * (trend.length - 1))];
        return <Node key={i} x={p[0]} y={p[1]} fill={ACCENT_RAMP[i % ACCENT_RAMP.length]} />;
      })}
    </g>
  );
}

function Embedding(rng: Rng) {
  const clusters = [
    { cx: W * 0.26, cy: H * 0.36, c: ART_COLORS.accentSoft },
    { cx: W * 0.62, cy: H * 0.62, c: ART_COLORS.cyan },
    { cx: W * 0.8, cy: H * 0.3, c: ART_COLORS.teal },
  ];
  return (
    <g>
      {clusters.map((cluster, ci) => {
        const points = Array.from({ length: intBetween(rng, 7, 10) }, () => {
          const a = between(rng, 0, Math.PI * 2);
          const r = between(rng, 6, 74);
          return [cluster.cx + r * Math.cos(a), cluster.cy + r * Math.sin(a) * 0.78] as [number, number];
        });
        return (
          <g key={ci}>
            <circle cx={fix(cluster.cx)} cy={fix(cluster.cy)} r={86} fill={cluster.c} opacity={0.06} />
            {points.map((p, i) =>
              i === 0 ? null : (
                <line
                  key={`l-${i}`}
                  x1={fix(points[0][0])}
                  y1={fix(points[0][1])}
                  x2={fix(p[0])}
                  y2={fix(p[1])}
                  stroke={cluster.c}
                  strokeWidth={0.9}
                  opacity={0.28}
                />
              ),
            )}
            {points.map((p, i) => (
              <circle key={i} cx={fix(p[0])} cy={fix(p[1])} r={i === 0 ? 4 : 2.3} fill={cluster.c} opacity={i === 0 ? 1 : 0.7} />
            ))}
          </g>
        );
      })}
      {clusters.map((a, i) => {
        const b = clusters[(i + 1) % clusters.length];
        return (
          <line
            key={`x-${i}`}
            x1={fix(a.cx)}
            y1={fix(a.cy)}
            x2={fix(b.cx)}
            y2={fix(b.cy)}
            stroke="#ffffff"
            strokeWidth={1}
            opacity={0.14}
            strokeDasharray="3 7"
          />
        );
      })}
    </g>
  );
}

function Tree(rng: Rng) {
  const rootY = 78;
  const midY = H * 0.5;
  const leafY = H - 84;
  const mids = [0.3, 0.5, 0.7].map((t) => t * W + between(rng, -26, 26));
  const leaves = [0.2, 0.36, 0.5, 0.64, 0.8].map((t) => t * W + between(rng, -18, 18));
  return (
    <g>
      {mids.map((mx, i) => (
        <path
          key={`m-${i}`}
          d={roundedPath([[W / 2, rootY], [W / 2, (rootY + midY) / 2], [mx, (rootY + midY) / 2], [mx, midY]], 18)}
          fill="none"
          stroke="#ffffff"
          strokeWidth={1.2}
          opacity={0.28}
        />
      ))}
      {leaves.map((lx, i) => {
        const parent = mids[Math.min(mids.length - 1, Math.floor(i / 2))];
        const color = ACCENT_RAMP[i % ACCENT_RAMP.length];
        return (
          <g key={`l-${i}`}>
            <path
              d={roundedPath([[parent, midY], [parent, (midY + leafY) / 2], [lx, (midY + leafY) / 2], [lx, leafY]], 16)}
              fill="none"
              stroke={color}
              strokeWidth={1.3}
              opacity={0.5}
            />
            <Node x={lx} y={leafY} r={2.8} fill={color} />
          </g>
        );
      })}
      {mids.map((mx, i) => (
        <Node key={`mn-${i}`} x={mx} y={midY} r={3.6} fill={ART_COLORS.accentSoft} />
      ))}
      <Node x={W / 2} y={rootY} r={5} fill={ART_COLORS.cyan} />
    </g>
  );
}

function Steps(rng: Rng) {
  const count = 5;
  const stepW = (W - 120) / count;
  const baseline = H - 70;
  const rise = (H - 190) / count;
  const tops: [number, number][] = [];
  return (
    <g>
      {Array.from({ length: count }, (_, i) => {
        const x = 60 + i * stepW;
        const h = rise * (i + 1) + between(rng, -8, 8);
        tops.push([x + stepW / 2, baseline - h]);
        const emphasis = i === count - 1;
        return (
          <rect
            key={i}
            x={fix(x)}
            y={fix(baseline - h)}
            width={fix(stepW * 0.82)}
            height={fix(h)}
            rx={8}
            fill={emphasis ? ART_COLORS.accent : "#ffffff"}
            opacity={emphasis ? 0.2 : 0.07}
            stroke={emphasis ? ART_COLORS.accentSoft : "#ffffff"}
            strokeOpacity={emphasis ? 0.55 : 0.16}
          />
        );
      })}
      <path
        d={roundedPath(tops, 10)}
        fill="none"
        stroke={ART_COLORS.teal}
        strokeWidth={2}
        opacity={0.85}
        strokeLinecap="round"
      />
      {tops.map((p, i) => (
        <Node key={`n-${i}`} x={p[0]} y={p[1]} r={i === tops.length - 1 ? 4.4 : 2.6} fill={ART_COLORS.teal} />
      ))}
      <line x1={48} y1={fix(baseline)} x2={W - 48} y2={fix(baseline)} stroke="#ffffff" strokeWidth={1} opacity={0.22} />
    </g>
  );
}

const VARIANTS: Record<CoverVariant, (rng: Rng) => React.ReactElement> = {
  flow: Flow,
  strata: Strata,
  mesh: Mesh,
  radial: Radial,
  field: Field,
  embedding: Embedding,
  tree: Tree,
  steps: Steps,
};

export function CoverArt({
  seed,
  variant,
  className,
}: {
  seed: string;
  variant: CoverVariant;
  className?: string;
}) {
  const rng = createRandom(seed);
  const uid = hashSeed(`${variant}:${seed}`).toString(36);

  return (
    <svg
      viewBox={`0 0 ${W} ${H}`}
      aria-hidden="true"
      focusable="false"
      preserveAspectRatio="xMidYMid slice"
      className={cn("block h-full w-full", className)}
    >
      <defs>
        <linearGradient id={`gw-bg-${uid}`} x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor={ART_COLORS.navyMid} />
          <stop offset="55%" stopColor={ART_COLORS.navy} />
          <stop offset="100%" stopColor={ART_COLORS.ink} />
        </linearGradient>
        <radialGradient id={`gw-glow-${uid}`} cx={`${fix(between(rng, 25, 75))}%`} cy="38%" r="62%">
          <stop offset="0%" stopColor={ART_COLORS.accent} stopOpacity="0.42" />
          <stop offset="100%" stopColor={ART_COLORS.accent} stopOpacity="0" />
        </radialGradient>
        <pattern id={`gw-grid-${uid}`} width="40" height="40" patternUnits="userSpaceOnUse">
          <path d="M40 0H0V40" fill="none" stroke="#ffffff" strokeOpacity="0.055" strokeWidth="1" />
        </pattern>
      </defs>

      <rect width={W} height={H} fill={`url(#gw-bg-${uid})`} />
      <rect width={W} height={H} fill={`url(#gw-grid-${uid})`} />
      <rect width={W} height={H} fill={`url(#gw-glow-${uid})`} />
      {VARIANTS[variant](rng)}
      <rect x="0.5" y="0.5" width={W - 1} height={H - 1} fill="none" stroke="#ffffff" strokeOpacity="0.09" />
    </svg>
  );
}

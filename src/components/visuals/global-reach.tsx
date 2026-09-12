import { fix } from "@/lib/art";
import { cn } from "@/lib/utils";

/**
 * Global reach visual.
 *
 * An orthographic dot-globe rotated so the African continent faces the viewer, with the
 * broad African latitude/longitude band picked out in the accent colour and connection arcs
 * to the regions DataForge engineers for. Positions are computed by projection rather than
 * hand-drawn, so nothing here misrepresents geography — it is a stylised globe, not a map
 * claiming borders or offices.
 */

const SIZE = 640;
const R = 250;
const CX = SIZE / 2;
const CY = SIZE / 2;

/** Rotation: centre the view near the Gulf of Guinea so Africa faces forward. */
const LON0 = (12 * Math.PI) / 180;
const LAT0 = (4 * Math.PI) / 180;

const AFRICA = { latMin: -35, latMax: 37, lonMin: -17, lonMax: 51 };

type Dot = { x: number; y: number; africa: boolean; depth: number };

function project(latDeg: number, lonDeg: number): Dot | null {
  const lat = (latDeg * Math.PI) / 180;
  const lon = (lonDeg * Math.PI) / 180;
  const cosC = Math.sin(LAT0) * Math.sin(lat) + Math.cos(LAT0) * Math.cos(lat) * Math.cos(lon - LON0);
  if (cosC <= 0.04) return null; // on the far side of the globe
  const x = CX + R * Math.cos(lat) * Math.sin(lon - LON0);
  const y = CY - R * (Math.cos(LAT0) * Math.sin(lat) - Math.sin(LAT0) * Math.cos(lat) * Math.cos(lon - LON0));
  const africa =
    latDeg >= AFRICA.latMin && latDeg <= AFRICA.latMax && lonDeg >= AFRICA.lonMin && lonDeg <= AFRICA.lonMax;
  return { x, y, africa, depth: cosC };
}

const DOTS: Dot[] = [];
for (let lat = -76; lat <= 80; lat += 7) {
  const step = Math.max(6, Math.round(7 / Math.max(0.18, Math.cos((lat * Math.PI) / 180))));
  for (let lon = -180; lon < 180; lon += step) {
    const dot = project(lat, lon);
    if (dot) DOTS.push(dot);
  }
}

const LAGOS = project(6.5, 3.4);

const REGIONS = [
  { label: "Europe", lat: 50, lon: 9 },
  { label: "Middle East", lat: 25, lon: 46 },
  { label: "North America", lat: 40, lon: -85 },
  { label: "Southern Africa", lat: -26, lon: 28 },
];

export function GlobalReach({ className }: { className?: string }) {
  return (
    <svg
      viewBox={`0 0 ${SIZE} ${SIZE}`}
      role="img"
      aria-labelledby="reach-title reach-desc"
      className={cn("h-auto w-full", className)}
    >
      <title id="reach-title">Global engineering reach</title>
      <desc id="reach-desc">
        A stylised globe oriented towards Africa, with connection lines from Lagos to Europe, the
        Middle East, North America and Southern Africa.
      </desc>

      <defs>
        <radialGradient id="gw-globe-fill" cx="42%" cy="34%" r="72%">
          <stop offset="0%" stopColor="#123063" stopOpacity="0.55" />
          <stop offset="100%" stopColor="#050a18" stopOpacity="0.9" />
        </radialGradient>
        <radialGradient id="gw-globe-glow" cx="50%" cy="50%" r="50%">
          <stop offset="70%" stopColor="#2f6bff" stopOpacity="0" />
          <stop offset="100%" stopColor="#2f6bff" stopOpacity="0.28" />
        </radialGradient>
      </defs>

      <circle cx={CX} cy={CY} r={R + 26} fill="url(#gw-globe-glow)" />
      <circle cx={CX} cy={CY} r={R} fill="url(#gw-globe-fill)" stroke="#ffffff14" strokeWidth="1" />

      <g>
        {DOTS.map((dot, i) => (
          <circle
            key={i}
            cx={fix(dot.x)}
            cy={fix(dot.y)}
            r={dot.africa ? 2.4 : 1.7}
            fill={dot.africa ? "var(--color-cyan-400)" : "#ffffff"}
            opacity={(dot.africa ? 0.55 : 0.2) + dot.depth * (dot.africa ? 0.45 : 0.22)}
          />
        ))}
      </g>

      {LAGOS ? (
        <g>
          {REGIONS.map((region) => {
            const target = project(region.lat, region.lon);
            if (!target) return null;
            const mx = (LAGOS.x + target.x) / 2;
            const my = (LAGOS.y + target.y) / 2 - 46;
            return (
              <path
                key={region.label}
                d={`M${fix(LAGOS.x)} ${fix(LAGOS.y)} Q${fix(mx)} ${fix(my)} ${fix(target.x)} ${fix(target.y)}`}
                fill="none"
                stroke="var(--color-accent-400)"
                strokeWidth="1.3"
                opacity="0.65"
                strokeLinecap="round"
              />
            );
          })}
          {REGIONS.map((region, i) => {
            const target = project(region.lat, region.lon);
            if (!target) return null;
            return (
              <circle
                key={region.label}
                cx={fix(target.x)}
                cy={fix(target.y)}
                r={3.4}
                fill="var(--color-accent-400)"
                className="pulse-node"
                style={{ animationDelay: `${i * 420}ms` }}
              />
            );
          })}
          <circle cx={fix(LAGOS.x)} cy={fix(LAGOS.y)} r={13} fill="var(--color-cyan-400)" opacity="0.16" />
          <circle cx={fix(LAGOS.x)} cy={fix(LAGOS.y)} r={5.2} fill="var(--color-cyan-400)" />
        </g>
      ) : null}
    </svg>
  );
}

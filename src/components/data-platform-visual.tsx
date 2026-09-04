import { cn } from "@/lib/utils";

type Tier = {
  id: string;
  label: string;
  detail: string;
  chips?: string[];
  y: number;
  height: number;
  accent?: boolean;
};

const TIERS: Tier[] = [
  { id: "sources", label: "Data Sources", detail: "Apps · APIs · Databases · Events", y: 8, height: 66 },
  { id: "ingestion", label: "Ingestion", detail: "Batch · CDC · Streaming", y: 106, height: 58 },
  { id: "pipelines", label: "Data Pipelines", detail: "Transform · Orchestrate · Test", y: 196, height: 58 },
  {
    id: "platform",
    label: "Cloud Data Platform",
    detail: "Warehouse · Lakehouse · Governance",
    chips: ["Storage", "Compute", "Governance"],
    y: 286,
    height: 104,
    accent: true,
  },
  { id: "analytics", label: "Analytics · AI · BI", detail: "Models · Metrics · Reporting", y: 422, height: 58 },
  { id: "decisions", label: "Business Decisions", detail: "Faster, evidenced, repeatable", y: 512, height: 58 },
];

const CONNECTORS = [
  { from: 74, to: 106 },
  { from: 164, to: 196 },
  { from: 254, to: 286 },
  { from: 390, to: 422 },
  { from: 480, to: 512 },
];

const WIDTH = 460;
const HEIGHT = 586;

/**
 * Abstract enterprise data-platform architecture.
 *
 * Rendered as inline SVG (no image request, no JS) with CSS-driven flow animation:
 * a short dash travels each connector to suggest data moving between tiers.
 * All movement is disabled by the global `prefers-reduced-motion` rule.
 */
export function DataPlatformVisual({ className }: { className?: string }) {
  return (
    <svg
      viewBox={`0 0 ${WIDTH} ${HEIGHT}`}
      role="img"
      aria-labelledby="platform-visual-title platform-visual-desc"
      className={cn("h-auto w-full", className)}
      preserveAspectRatio="xMidYMid meet"
    >
      <title id="platform-visual-title">Modern data platform architecture</title>
      <desc id="platform-visual-desc">
        A layered architecture diagram: data sources flow into ingestion, then data pipelines, then a
        cloud data platform providing storage, compute and governance, then analytics, AI and business
        intelligence, and finally business decisions.
      </desc>

      <defs>
        <linearGradient id="gw-tier" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="rgba(255,255,255,0.09)" />
          <stop offset="100%" stopColor="rgba(255,255,255,0.03)" />
        </linearGradient>
        <linearGradient id="gw-tier-accent" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="rgba(47,107,255,0.30)" />
          <stop offset="100%" stopColor="rgba(18,184,214,0.12)" />
        </linearGradient>
        <linearGradient id="gw-flow" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="var(--color-cyan-400)" />
          <stop offset="100%" stopColor="var(--color-accent-400)" />
        </linearGradient>
        <radialGradient id="gw-glow" cx="50%" cy="42%" r="60%">
          <stop offset="0%" stopColor="rgba(47,107,255,0.35)" />
          <stop offset="100%" stopColor="rgba(47,107,255,0)" />
        </radialGradient>
      </defs>

      <rect
        x="0"
        y="0"
        width={WIDTH}
        height={HEIGHT}
        fill="url(#gw-glow)"
        className="drift-slow"
        style={{ transformOrigin: "center" }}
      />

      {/* Connectors */}
      {CONNECTORS.map((connector, index) => {
        const d = `M${WIDTH / 2} ${connector.from} L${WIDTH / 2} ${connector.to}`;
        return (
          <g key={`connector-${connector.from}`}>
            <path d={d} stroke="rgba(255,255,255,0.16)" strokeWidth="1.25" fill="none" />
            <path
              d={d}
              stroke="url(#gw-flow)"
              strokeWidth="2.25"
              strokeLinecap="round"
              fill="none"
              className="flow-dash"
              style={{ animationDelay: `${index * 260}ms` }}
            />
            <circle cx={WIDTH / 2} cy={connector.to} r="2.6" fill="var(--color-accent-400)" />
          </g>
        );
      })}

      {/* Tiers */}
      {TIERS.map((tier, index) => (
        <g key={tier.id}>
          <rect
            x="20"
            y={tier.y}
            width={WIDTH - 40}
            height={tier.height}
            rx="14"
            fill={tier.accent ? "url(#gw-tier-accent)" : "url(#gw-tier)"}
            stroke={tier.accent ? "rgba(91,147,255,0.55)" : "rgba(255,255,255,0.14)"}
            strokeWidth="1"
          />
          <circle
            cx="42"
            cy={tier.y + 24}
            r="3.2"
            fill={tier.accent ? "var(--color-cyan-400)" : "var(--color-accent-400)"}
            className="pulse-node"
            style={{ animationDelay: `${index * 420}ms` }}
          />
          <text
            x="56"
            y={tier.y + 28}
            fill="#ffffff"
            fontSize="14.5"
            fontWeight="600"
            letterSpacing="-0.2"
            fontFamily="var(--font-display), sans-serif"
          >
            {tier.label}
          </text>
          <text
            x="56"
            y={tier.y + 47}
            fill="rgba(207,216,230,0.72)"
            fontSize="11.5"
            letterSpacing="0.1"
            fontFamily="var(--font-sans), sans-serif"
          >
            {tier.detail}
          </text>

          {tier.chips?.map((chip, chipIndex) => (
            <g key={chip}>
              <rect
                x={42 + chipIndex * 122}
                y={tier.y + 60}
                width="110"
                height="30"
                rx="8"
                fill="rgba(255,255,255,0.07)"
                stroke="rgba(255,255,255,0.16)"
              />
              <text
                x={42 + chipIndex * 122 + 55}
                y={tier.y + 79}
                fill="rgba(232,238,247,0.9)"
                fontSize="11.5"
                textAnchor="middle"
                fontFamily="var(--font-sans), sans-serif"
              >
                {chip}
              </text>
            </g>
          ))}
        </g>
      ))}

      {/* Source nodes feeding the first tier */}
      {[0, 1, 2, 3].map((index) => (
        <circle
          key={`source-${index}`}
          cx={WIDTH - 52 - index * 22}
          cy={30}
          r="3"
          fill="var(--color-teal-400)"
          opacity={0.85 - index * 0.16}
          className="pulse-node"
          style={{ animationDelay: `${index * 300}ms` }}
        />
      ))}
    </svg>
  );
}

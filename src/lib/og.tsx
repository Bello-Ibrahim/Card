import { ImageResponse } from "next/og";
import { ART_COLORS } from "@/lib/art";

export const OG_SIZE = { width: 1200, height: 630 };
export const OG_CONTENT_TYPE = "image/png";

/**
 * Shared Open Graph card.
 *
 * Rendered by Satori, which supports only a subset of CSS — so the artwork here is built
 * from plain divs, gradients and border radii rather than the SVG used on the site itself.
 * Every element that has more than one child declares `display: flex` explicitly, which
 * Satori requires.
 */
export function renderOgImage({
  eyebrow,
  title,
  footer = "Data Engineering · Cloud · Analytics · Architecture · Training · Talent",
}: {
  eyebrow: string;
  title: string;
  footer?: string;
}) {
  const trimmed = title.length > 96 ? `${title.slice(0, 95)}…` : title;
  const fontSize = trimmed.length > 68 ? 48 : trimmed.length > 42 ? 56 : 66;

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          position: "relative",
          background: `linear-gradient(135deg, ${ART_COLORS.navyMid} 0%, ${ART_COLORS.navy} 58%, ${ART_COLORS.ink} 100%)`,
          padding: 76,
          fontFamily: "sans-serif",
        }}
      >
        {/* Abstract corner composition — stacked strata fading to the right edge. */}
        <div style={{ position: "absolute", top: 0, right: 0, width: 470, height: 630, display: "flex" }}>
          <div
            style={{
              position: "absolute",
              inset: 0,
              background: `radial-gradient(circle at 72% 34%, ${ART_COLORS.accent}66 0%, ${ART_COLORS.accent}00 68%)`,
              display: "flex",
            }}
          />
          {[0, 1, 2, 3, 4].map((i) => (
            <div
              key={i}
              style={{
                position: "absolute",
                right: -70 + i * 12,
                top: 92 + i * 86,
                width: 400 - i * 24,
                height: 56,
                borderRadius: 14,
                background: i === 2 ? `${ART_COLORS.accent}33` : "#ffffff0a",
                border: `1px solid ${i === 2 ? `${ART_COLORS.accentSoft}88` : "#ffffff1f"}`,
                display: "flex",
              }}
            />
          ))}
          <div
            style={{
              position: "absolute",
              right: 158,
              top: 92,
              width: 2,
              height: 452,
              background: `linear-gradient(180deg, ${ART_COLORS.cyan}00, ${ART_COLORS.cyan}cc, ${ART_COLORS.cyan}00)`,
              display: "flex",
            }}
          />
        </div>

        <div style={{ display: "flex", alignItems: "center", gap: 18 }}>
          <div
            style={{
              width: 46,
              height: 46,
              borderRadius: 13,
              background: ART_COLORS.accent,
              display: "flex",
            }}
          />
          <div style={{ color: "#ffffff", fontSize: 28, fontWeight: 600, letterSpacing: -0.4 }}>
            DataForge Consulting
          </div>
        </div>

        <div style={{ display: "flex", flexDirection: "column", maxWidth: 660 }}>
          <div
            style={{
              color: ART_COLORS.accentSoft,
              fontSize: 20,
              fontWeight: 600,
              letterSpacing: 3.4,
              textTransform: "uppercase",
              display: "flex",
            }}
          >
            {eyebrow}
          </div>
          <div
            style={{
              color: "#ffffff",
              fontSize,
              fontWeight: 700,
              letterSpacing: -2,
              lineHeight: 1.08,
              marginTop: 22,
              display: "flex",
            }}
          >
            {trimmed}
          </div>
        </div>

        <div style={{ color: "#a3b0c4", fontSize: 22, letterSpacing: 0.4, display: "flex" }}>
          {footer}
        </div>
      </div>
    ),
    OG_SIZE,
  );
}

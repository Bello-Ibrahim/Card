import { ImageResponse } from "next/og";
import { site } from "@/content/site";

export const alt = `${site.name} — ${site.tagline}`;
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

/**
 * Open Graph / Twitter card. Generated from local content, so there is no static
 * image asset to keep in sync with the copy. Next applies it to every route via the
 * file convention, and per-route files can override it later if needed.
 */
export default function OpengraphImage() {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          background: "linear-gradient(135deg, #050a18 0%, #0d2044 62%, #143cb0 145%)",
          padding: 76,
          fontFamily: "sans-serif",
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 18 }}>
          <div style={{ width: 46, height: 46, borderRadius: 13, background: "#2f6bff", display: "flex" }} />
          <div style={{ color: "#ffffff", fontSize: 29, fontWeight: 600, letterSpacing: -0.5 }}>
            DataForge Consulting
          </div>
        </div>

        <div
          style={{
            color: "#ffffff",
            fontSize: 68,
            fontWeight: 700,
            letterSpacing: -2.2,
            lineHeight: 1.06,
            maxWidth: 960,
            display: "flex",
          }}
        >
          Engineering the data foundations behind better decisions.
        </div>

        <div style={{ color: "#a3b0c4", fontSize: 23, letterSpacing: 0.4, display: "flex" }}>
          Data Engineering · Cloud · Analytics · Architecture · Training · Talent
        </div>
      </div>
    ),
    size,
  );
}

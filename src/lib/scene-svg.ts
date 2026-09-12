import { between, createRandom, fix, hashSeed, intBetween, type Rng } from "@/lib/art";
import type { SceneKind } from "@/content/media";

/**
 * Designed scenes, emitted as SVG source.
 *
 * These are built as strings rather than JSX so they can be served from a prerendered image
 * route: the app router forbids `react-dom/server`, and rendering the scenes inline cost
 * several hundred DOM nodes per slot. Every value is derived from a string seed, so a scene
 * is byte-identical across builds and caches indefinitely.
 */

const W = 1600;
const H = 900;

const INK = "#080d18";
const STEEL = "#24406f";
const GLOW = "#2f6bff";
const CYAN = "#38d9f0";
const WARM = "#2fd8a8";

type Attrs = Record<string, string | number | undefined>;

const el = (tag: string, attrs: Attrs, children = "") => {
  const body = Object.entries(attrs)
    .filter(([, v]) => v !== undefined)
    .map(([k, v]) => `${k}="${v}"`)
    .join(" ");
  return children ? `<${tag} ${body}>${children}</${tag}>` : `<${tag} ${body}/>`;
};

const rect = (a: Attrs) => el("rect", a);
const circle = (a: Attrs) => el("circle", a);
const line = (a: Attrs) => el("line", a);

/** Abstract "lines of output" inside a screen rectangle. */
function screenLines(rng: Rng, x: number, y: number, w: number, h: number, color: string) {
  const rows = Math.max(2, Math.floor(h / 14));
  let out = "";
  for (let i = 0; i < rows; i += 1) {
    out += rect({
      x: fix(x + 8),
      y: fix(y + 8 + i * 12),
      width: fix(between(rng, 0.25, 0.92) * (w - 16)),
      height: 3,
      rx: 1.5,
      fill: color,
      opacity: fix(between(rng, 0.25, 0.85)),
    });
  }
  return el("g", { opacity: 0.85 }, out);
}

function controlRoom(rng: Rng, uid: string) {
  const cols = 6;
  const rows = 3;
  const panelW = 210;
  const panelH = 130;
  let out = "";

  for (let r = 0; r < rows; r += 1) {
    for (let c = 0; c < cols; c += 1) {
      const x = 150 + c * (panelW + 16);
      const y = 170 + r * (panelH + 16);
      const lit = rng() > 0.25;
      const accent = rng() > 0.7 ? CYAN : GLOW;
      out += rect({
        x: fix(x),
        y: fix(y),
        width: panelW,
        height: panelH,
        rx: 4,
        fill: lit ? `${accent}3d` : "#ffffff0e",
        stroke: lit ? `${accent}88` : "#ffffff1f",
        "stroke-width": 1,
      });
      if (lit) out += screenLines(rng, x, y, panelW, panelH, accent);
    }
  }

  for (let i = 0; i < 4; i += 1) {
    const x = 180 + i * 340;
    out += rect({ x: fix(x), y: 700, width: 250, height: 10, rx: 5, fill: INK });
    out += rect({ x: fix(x + 40), y: 640, width: 150, height: 62, rx: 4, fill: `${GLOW}4a`, stroke: `${GLOW}88` });
    out += rect({ x: fix(x + 20), y: 710, width: 8, height: 70, fill: INK });
    out += rect({ x: fix(x + 222), y: 710, width: 8, height: 70, fill: INK });
  }

  out += rect({ x: 0, y: 780, width: W, height: 120, fill: INK, opacity: 0.9 });
  out += rect({ x: 0, y: 770, width: W, height: 4, fill: `url(#f-${uid})`, opacity: 0.5 });
  return out;
}

function racks(rng: Rng, uid: string) {
  const columns = 7;
  let out = "";
  for (let i = 0; i < columns; i += 1) {
    const centre = Math.abs(i / (columns - 1) - 0.5) * 2;
    const x = 60 + i * 220;
    const top = 120 + centre * 90;
    const height = 660 - centre * 180;
    const units = Math.floor(height / 26);
    let column = rect({
      x: fix(x),
      y: fix(top),
      width: 170,
      height: fix(height),
      rx: 3,
      fill: "#1a2c4f",
      stroke: "#ffffff20",
    });
    for (let u = 0; u < units; u += 1) {
      const uy = top + 8 + u * 26;
      const on = rng() > 0.3;
      column += rect({ x: fix(x + 8), y: fix(uy), width: 154, height: 18, rx: 2, fill: "#ffffff12" });
      column += circle({ cx: fix(x + 20), cy: fix(uy + 9), r: 2.6, fill: on ? WARM : "#ffffff22" });
      column += circle({ cx: fix(x + 32), cy: fix(uy + 9), r: 2.6, fill: on && rng() > 0.5 ? CYAN : "#ffffff18" });
      column += rect({
        x: fix(x + 48),
        y: fix(uy + 6),
        width: fix(between(rng, 20, 100)),
        height: 6,
        rx: 3,
        fill: "#ffffff10",
      });
    }
    out += el("g", { opacity: fix(0.5 + (1 - centre) * 0.5) }, column);
  }
  out += rect({ x: W / 2 - 160, y: 0, width: 320, height: H, fill: `url(#a-${uid})`, opacity: 0.55 });
  return out;
}

function workspace(rng: Rng, uid: string) {
  const monitors = [
    { x: 250, y: 200, w: 420, h: 270, color: GLOW },
    { x: 700, y: 160, w: 470, h: 310, color: CYAN },
    { x: 1200, y: 210, w: 300, h: 255, color: GLOW },
  ];
  let out = "";
  monitors.forEach((m, i) => {
    out += rect({
      x: fix(m.x), y: fix(m.y), width: m.w, height: m.h, rx: 6,
      fill: `${m.color}3a`, stroke: `${m.color}88`,
    });
    out += screenLines(rng, m.x, m.y, m.w, m.h, m.color);
    if (i === 1) {
      for (let b = 0; b < 9; b += 1) {
        const bh = between(rng, 20, 110);
        out += rect({
          x: fix(m.x + 20 + b * 32), y: fix(m.y + m.h - 20 - bh),
          width: 20, height: fix(bh), rx: 2, fill: CYAN, opacity: 0.55,
        });
      }
    }
    out += rect({ x: fix(m.x + m.w / 2 - 30), y: fix(m.y + m.h), width: 60, height: 34, fill: INK });
    out += rect({ x: fix(m.x + m.w / 2 - 70), y: fix(m.y + m.h + 34), width: 140, height: 8, rx: 4, fill: INK });
  });

  out += rect({ x: 0, y: 560, width: W, height: 16, fill: "#0a1024" });
  out += rect({ x: 0, y: 576, width: W, height: 324, fill: INK });
  out += rect({ x: 560, y: 600, width: 480, height: 70, rx: 8, fill: "#0d1526", stroke: "#ffffff10" });
  for (let k = 0; k < 40; k += 1) {
    out += rect({
      x: fix(575 + (k % 14) * 32), y: fix(612 + Math.floor(k / 14) * 18),
      width: 24, height: 12, rx: 2, fill: "#ffffff0a",
    });
  }
  out += rect({ x: 0, y: 540, width: W, height: 40, fill: `url(#d-${uid})`, opacity: 0.7 });
  return out;
}

function skyline(rng: Rng) {
  const layers = [
    { count: 9, base: 830, maxH: 380, fill: "#1b3054", opacity: 0.75, windows: true },
    { count: 7, base: 865, maxH: 520, fill: "#12203c", opacity: 0.9, windows: true },
    { count: 6, base: 900, maxH: 660, fill: "#0a1224", opacity: 1, windows: false },
  ];
  let out = "";
  for (const layer of layers) {
    let x = -40;
    let blocks = "";
    for (let i = 0; i < layer.count; i += 1) {
      const w = between(rng, 130, 260);
      const h = between(rng, layer.maxH * 0.45, layer.maxH);
      const y = layer.base - h;
      blocks += rect({ x: fix(x), y: fix(y), width: fix(w), height: fix(h), fill: layer.fill, opacity: layer.opacity });
      if (layer.windows) {
        for (let r = 0; r < Math.floor(h / 40); r += 1) {
          for (let c = 0; c < Math.floor(w / 34); c += 1) {
            if (rng() > 0.62) {
              blocks += rect({
                x: fix(x + 12 + c * 34), y: fix(y + 16 + r * 40),
                width: 14, height: 18,
                fill: rng() > 0.7 ? CYAN : GLOW,
                opacity: fix(between(rng, 0.45, 1)),
              });
            }
          }
        }
      }
      x += w + between(rng, 12, 46);
    }
    out += el("g", {}, blocks);
  }
  return out;
}

function workshop(rng: Rng, uid: string) {
  let out = rect({ x: 420, y: 90, width: 760, height: 400, rx: 6, fill: `${GLOW}33`, stroke: `${GLOW}88` });
  for (let r = 0; r < 4; r += 1) {
    for (let c = 0; c < 3; c += 1) {
      out += rect({
        x: fix(470 + c * 230), y: fix(140 + r * 88), width: 150, height: 48, rx: 5,
        fill: r === 1 ? `${CYAN}4d` : "#ffffff18",
        stroke: r === 1 ? `${CYAN}88` : "#ffffff20",
      });
      if (c < 2) {
        out += line({
          x1: fix(620 + c * 230), y1: fix(164 + r * 88),
          x2: fix(700 + c * 230), y2: fix(164 + r * 88),
          stroke: CYAN, "stroke-width": 1.4, opacity: 0.55,
        });
      }
    }
  }

  for (let row = 0; row < 2; row += 1) {
    const y = 620 + row * 130;
    const scale = 1 - row * 0.18;
    let seats = rect({ x: 0, y: fix(y + 58 * scale), width: W, height: 14, fill: "#0a1024" });
    for (let i = 0; i < 5; i += 1) {
      const x = 140 + i * 300;
      const w = 180 * scale;
      const h = 62 * scale;
      seats += rect({ x: fix(x), y: fix(y), width: fix(w), height: fix(h), rx: 4, fill: `${GLOW}44`, stroke: `${GLOW}88` });
      seats += screenLines(rng, x, y, w, h, GLOW);
      seats += rect({ x: fix(x - 10), y: fix(y + h), width: fix(w + 20), height: fix(8 * scale), rx: 3, fill: "#0c1426" });
    }
    out += el("g", { opacity: fix(1 - row * 0.25) }, seats);
  }
  out += rect({ x: 420, y: 480, width: 760, height: 60, fill: `url(#p-${uid})`, opacity: 0.6 });
  return out;
}

const SCENES: Record<SceneKind, (rng: Rng, uid: string) => string> = {
  "control-room": controlRoom,
  racks,
  workspace,
  skyline: (rng) => skyline(rng),
  workshop,
};

export function renderSceneSvg(kind: SceneKind, seed: string): string {
  const rng = createRandom(`${kind}:${seed}`);
  const uid = hashSeed(`scene:${kind}:${seed}`).toString(36);
  const lightX = intBetween(rng, 30, 70);

  const defs = [
    el("linearGradient", { id: `s-${uid}`, x1: 0, y1: 0, x2: 0, y2: 1 },
      el("stop", { offset: "0%", "stop-color": STEEL }) +
      el("stop", { offset: "55%", "stop-color": "#132446" }) +
      el("stop", { offset: "100%", "stop-color": "#0a1120" })),
    el("radialGradient", { id: `b-${uid}`, cx: `${lightX}%`, cy: "34%", r: "58%" },
      el("stop", { offset: "0%", "stop-color": GLOW, "stop-opacity": 0.6 }) +
      el("stop", { offset: "100%", "stop-color": GLOW, "stop-opacity": 0 })),
    el("radialGradient", { id: `v-${uid}`, cx: "50%", cy: "46%", r: "72%" },
      el("stop", { offset: "58%", "stop-color": "#000000", "stop-opacity": 0 }) +
      el("stop", { offset: "100%", "stop-color": "#000000", "stop-opacity": 0.42 })),
    el("linearGradient", { id: `f-${uid}`, x1: 0, y1: 0, x2: 1, y2: 0 },
      el("stop", { offset: "0%", "stop-color": GLOW, "stop-opacity": 0 }) +
      el("stop", { offset: "50%", "stop-color": CYAN, "stop-opacity": 0.7 }) +
      el("stop", { offset: "100%", "stop-color": GLOW, "stop-opacity": 0 })),
    el("linearGradient", { id: `a-${uid}`, x1: 0, y1: 0, x2: 1, y2: 0 },
      el("stop", { offset: "0%", "stop-color": CYAN, "stop-opacity": 0 }) +
      el("stop", { offset: "50%", "stop-color": CYAN, "stop-opacity": 0.32 }) +
      el("stop", { offset: "100%", "stop-color": CYAN, "stop-opacity": 0 })),
    el("linearGradient", { id: `d-${uid}`, x1: 0, y1: 0, x2: 0, y2: 1 },
      el("stop", { offset: "0%", "stop-color": GLOW, "stop-opacity": 0.42 }) +
      el("stop", { offset: "100%", "stop-color": GLOW, "stop-opacity": 0 })),
    el("linearGradient", { id: `p-${uid}`, x1: 0, y1: 0, x2: 0, y2: 1 },
      el("stop", { offset: "0%", "stop-color": GLOW, "stop-opacity": 0.5 }) +
      el("stop", { offset: "100%", "stop-color": GLOW, "stop-opacity": 0 })),
  ].join("");

  const body =
    rect({ width: W, height: H, fill: `url(#s-${uid})` }) +
    rect({ width: W, height: H, fill: `url(#b-${uid})` }) +
    SCENES[kind](rng, uid) +
    rect({ width: W, height: H, fill: `url(#v-${uid})` });

  return el(
    "svg",
    {
      xmlns: "http://www.w3.org/2000/svg",
      viewBox: `0 0 ${W} ${H}`,
      width: W,
      height: H,
      preserveAspectRatio: "xMidYMid slice",
      role: "presentation",
    },
    el("defs", {}, defs) + body,
  );
}

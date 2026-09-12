import { between, createRandom, fix, hashSeed, intBetween, type Rng } from "@/lib/art";
import type { SceneKind } from "@/content/media";

/**
 * Designed scenes, emitted as SVG source.
 *
 * These are built to read as photography rather than as diagrams. The techniques that do
 * the work are the ones a camera gives you for free: three separated depth planes, the far
 * and near ones defocused; bokeh from out-of-focus highlights; a warm/cool grade so the
 * frame is not uniformly blue; and a film grain pass, which more than anything else stops
 * vector art looking like vector art.
 *
 * Emitted as strings rather than JSX so they can be served from a prerendered image route —
 * the app router forbids `react-dom/server`, and inline SVG cost hundreds of DOM nodes per
 * slot. Every value derives from a string seed, so a scene is byte-identical across builds.
 */

const W = 1600;
const H = 900;

const INK = "#05080f";
const DEEP = "#0a1020";
const STEEL = "#24406f";
const GLOW = "#2f6bff";
const CYAN = "#38d9f0";
const WARM = "#ffb45e";
const AMBER = "#ff8a3d";
const TEAL = "#2fd8a8";

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

/** Abstract "lines of output" inside a screen. Varying row widths read as text at distance. */
function screenLines(rng: Rng, x: number, y: number, w: number, h: number, color: string, density = 14) {
  const rows = Math.max(2, Math.floor(h / density));
  let out = "";
  for (let i = 0; i < rows; i += 1) {
    out += rect({
      x: fix(x + 9),
      y: fix(y + 9 + i * density),
      width: fix(between(rng, 0.2, 0.9) * (w - 18)),
      height: fix(density * 0.22),
      rx: 1,
      fill: color,
      opacity: fix(between(rng, 0.3, 0.95)),
    });
  }
  return out;
}

/** Out-of-focus highlights. The single biggest cue that a frame was photographed. */
function bokeh(rng: Rng, uid: string, count: number, palette: string[]) {
  let out = "";
  for (let i = 0; i < count; i += 1) {
    const r = between(rng, 14, 54);
    out += circle({
      cx: fix(between(rng, 40, W - 40)),
      cy: fix(between(rng, 40, H - 120)),
      r: fix(r),
      fill: palette[intBetween(rng, 0, palette.length - 1)],
      opacity: fix(between(rng, 0.06, 0.2)),
    });
  }
  return el("g", { filter: `url(#bf-${uid})` }, out);
}

type Layers = { far: string; main: string; near: string };

/* ------------------------------------------------------------------ scenes */

function controlRoom(rng: Rng, uid: string): Layers {
  // Far: the video wall, slightly defocused so the operators read as the subject.
  let far = "";
  const cols = 6;
  const rows = 3;
  const pw = 212;
  const ph = 132;
  for (let r = 0; r < rows; r += 1) {
    for (let c = 0; c < cols; c += 1) {
      const x = 138 + c * (pw + 14);
      const y = 120 + r * (ph + 14);
      const lit = rng() > 0.22;
      const accent = rng() > 0.68 ? CYAN : GLOW;
      far += rect({
        x: fix(x), y: fix(y), width: pw, height: ph, rx: 3,
        fill: lit ? `${accent}40` : "#ffffff0c",
        stroke: lit ? `${accent}7a` : "#ffffff18",
      });
      if (lit) far += screenLines(rng, x, y, pw, ph, accent, 13);
    }
  }
  far += rect({ x: 0, y: 556, width: W, height: 8, fill: `url(#fl-${uid})`, opacity: 0.6 });

  // Main: operator desks, in focus.
  let main = "";
  for (let i = 0; i < 4; i += 1) {
    const x = 150 + i * 350;
    main += rect({ x: fix(x + 34), y: 612, width: 172, height: 74, rx: 5, fill: `${GLOW}5e`, stroke: `${GLOW}9c` });
    main += screenLines(rng, x + 34, 612, 172, 74, GLOW, 12);
    main += rect({ x: fix(x + 104), y: 686, width: 34, height: 22, fill: "#0b1222" });
    main += rect({ x: fix(x), y: 708, width: 250, height: 11, rx: 4, fill: "#111a2e" });
    main += rect({ x: fix(x + 74), y: 722, width: 104, height: 8, rx: 3, fill: "#0c1324" });
  }

  // Near: an out-of-focus chair-back silhouette anchoring the foreground.
  const near =
    rect({ x: -120, y: 790, width: 380, height: 220, rx: 60, fill: INK, opacity: 0.9 }) +
    rect({ x: 1360, y: 820, width: 420, height: 200, rx: 70, fill: INK, opacity: 0.85 });

  return { far, main, near };
}

function racks(rng: Rng, uid: string): Layers {
  let far = "";
  let main = "";
  const columns = 7;
  for (let i = 0; i < columns; i += 1) {
    const centre = Math.abs(i / (columns - 1) - 0.5) * 2;
    const x = 40 + i * 224;
    const top = 100 + centre * 110;
    const height = 700 - centre * 220;
    const units = Math.floor(height / 25);
    let column = rect({
      x: fix(x), y: fix(top), width: 176, height: fix(height), rx: 2,
      fill: centre > 0.5 ? "#16233f" : "#1d3157",
      stroke: "#ffffff1c",
    });
    for (let u = 0; u < units; u += 1) {
      const uy = top + 7 + u * 25;
      const on = rng() > 0.28;
      column += rect({ x: fix(x + 7), y: fix(uy), width: 162, height: 17, rx: 1.5, fill: "#ffffff10" });
      column += circle({ cx: fix(x + 19), cy: fix(uy + 8.5), r: 2.4, fill: on ? TEAL : "#ffffff20" });
      column += circle({ cx: fix(x + 30), cy: fix(uy + 8.5), r: 2.4, fill: on && rng() > 0.5 ? AMBER : "#ffffff16" });
      column += rect({ x: fix(x + 44), y: fix(uy + 5.5), width: fix(between(rng, 18, 104)), height: 6, rx: 3, fill: "#ffffff0e" });
    }
    const layer = el("g", { opacity: fix(0.55 + (1 - centre) * 0.45) }, column);
    if (centre > 0.55) far += layer;
    else main += layer;
  }
  // Cold-aisle light down the centre of the corridor.
  main += rect({ x: W / 2 - 170, y: 0, width: 340, height: H, fill: `url(#ai-${uid})`, opacity: 0.6 });
  const near = rect({ x: -80, y: 0, width: 300, height: H, fill: INK, opacity: 0.85 }) +
    rect({ x: W - 220, y: 0, width: 320, height: H, fill: INK, opacity: 0.8 });
  return { far, main, near };
}

function workspace(rng: Rng, uid: string): Layers {
  // Far: a dim room behind the desk.
  const far =
    rect({ x: 120, y: 80, width: 420, height: 250, rx: 6, fill: "#16264a", opacity: 0.7 }) +
    rect({ x: 1060, y: 60, width: 460, height: 300, rx: 6, fill: "#16264a", opacity: 0.55 }) +
    rect({ x: 0, y: 430, width: W, height: 10, fill: "#ffffff0a" });

  const monitors = [
    { x: 228, y: 196, w: 440, h: 286, color: GLOW, chart: false },
    { x: 692, y: 148, w: 496, h: 330, color: CYAN, chart: true },
    { x: 1212, y: 206, w: 304, h: 268, color: GLOW, chart: false },
  ];
  let main = "";
  for (const m of monitors) {
    main += rect({ x: fix(m.x), y: fix(m.y), width: m.w, height: m.h, rx: 5, fill: "#060a14" });
    main += rect({ x: fix(m.x + 4), y: fix(m.y + 4), width: m.w - 8, height: m.h - 8, rx: 3, fill: `${m.color}40` });
    main += screenLines(rng, m.x + 4, m.y + 4, m.w - 8, m.h - 8, m.color, 13);
    if (m.chart) {
      for (let b = 0; b < 11; b += 1) {
        const bh = between(rng, 24, 130);
        main += rect({
          x: fix(m.x + 26 + b * 40), y: fix(m.y + m.h - 26 - bh),
          width: 24, height: fix(bh), rx: 2, fill: CYAN, opacity: 0.6,
        });
      }
    }
    main += rect({ x: fix(m.x + m.w / 2 - 26), y: fix(m.y + m.h), width: 52, height: 30, fill: "#0a0f1c" });
    main += rect({ x: fix(m.x + m.w / 2 - 74), y: fix(m.y + m.h + 30), width: 148, height: 9, rx: 4, fill: "#0c1120" });
  }
  // Desk surface catching screen light.
  main += rect({ x: 0, y: 548, width: W, height: 14, fill: "#111a2d" });
  main += rect({ x: 0, y: 536, width: W, height: 26, fill: `url(#dg-${uid})`, opacity: 0.85 });
  main += rect({ x: 0, y: 562, width: W, height: 338, fill: DEEP, opacity: 0.86 });
  main += rect({ x: 548, y: 596, width: 500, height: 74, rx: 7, fill: "#0e1729", stroke: "#ffffff14" });
  for (let k = 0; k < 42; k += 1) {
    main += rect({
      x: fix(564 + (k % 14) * 33), y: fix(608 + Math.floor(k / 14) * 19),
      width: 25, height: 13, rx: 2, fill: "#ffffff0c",
    });
  }
  main += circle({ cx: 1180, cy: 660, r: 30, fill: "#0e1729", stroke: "#ffffff14" });

  const near = rect({ x: -110, y: 800, width: 400, height: 220, rx: 50, fill: INK, opacity: 0.85 });
  return { far, main, near };
}

function skyline(rng: Rng, uid: string): Layers {
  const band = (count: number, base: number, maxH: number, fill: string, opacity: number, windows: boolean) => {
    let x = -60;
    let out = "";
    for (let i = 0; i < count; i += 1) {
      const w = between(rng, 120, 250);
      const h = between(rng, maxH * 0.45, maxH);
      const y = base - h;
      out += rect({ x: fix(x), y: fix(y), width: fix(w), height: fix(h), fill, opacity });
      if (windows) {
        for (let r = 0; r < Math.floor(h / 38); r += 1) {
          for (let c = 0; c < Math.floor(w / 32); c += 1) {
            if (rng() > 0.58) {
              const warm = rng() > 0.62;
              out += rect({
                x: fix(x + 11 + c * 32), y: fix(y + 14 + r * 38),
                width: 13, height: 17,
                fill: warm ? WARM : rng() > 0.5 ? CYAN : GLOW,
                opacity: fix(between(rng, 0.4, 1)),
              });
            }
          }
        }
      }
      x += w + between(rng, 10, 40);
    }
    return out;
  };

  const far = band(10, 800, 400, "#22355c", 0.8, true);
  const main = band(8, 858, 540, "#141f3a", 0.95, true);
  const near =
    band(6, 920, 700, "#070c16", 1, false) +
    rect({ x: 0, y: 836, width: W, height: 64, fill: `url(#hz-${uid})`, opacity: 0.32 });
  return { far, main, near };
}

function workshop(rng: Rng, uid: string): Layers {
  // Far: the projected architecture on the wall.
  let far = rect({ x: 398, y: 70, width: 804, height: 404, rx: 4, fill: "#08101f" });
  far += rect({ x: 406, y: 78, width: 788, height: 388, rx: 2, fill: `${GLOW}3a` });
  for (let r = 0; r < 4; r += 1) {
    for (let c = 0; c < 3; c += 1) {
      far += rect({
        x: fix(452 + c * 238), y: fix(122 + r * 88), width: 158, height: 50, rx: 4,
        fill: r === 1 ? `${CYAN}59` : "#ffffff1c",
        stroke: r === 1 ? `${CYAN}99` : "#ffffff26",
      });
      if (c < 2) {
        far += line({
          x1: fix(610 + c * 238), y1: fix(147 + r * 88),
          x2: fix(690 + c * 238), y2: fix(147 + r * 88),
          stroke: CYAN, "stroke-width": 1.6, opacity: 0.6,
        });
      }
    }
  }
  far += rect({ x: 398, y: 474, width: 804, height: 70, fill: `url(#pg-${uid})`, opacity: 0.75 });

  // Main: the front row of laptops, in focus.
  let main = rect({ x: 0, y: 636, width: W, height: 16, fill: "#131d33" });
  for (let i = 0; i < 5; i += 1) {
    const x = 112 + i * 304;
    main += rect({ x: fix(x), y: 566, width: 188, height: 68, rx: 4, fill: "#070c16" });
    main += rect({ x: fix(x + 4), y: 570, width: 180, height: 60, rx: 2, fill: `${GLOW}5c` });
    main += screenLines(rng, x + 4, 570, 180, 60, GLOW, 11);
    main += rect({ x: fix(x - 12), y: 634, width: 212, height: 9, rx: 3, fill: "#101a2e" });
  }
  main += rect({ x: 0, y: 652, width: W, height: 248, fill: DEEP, opacity: 0.82 });

  // Near: the back of a head / shoulders in the foreground, thrown out of focus.
  const near =
    circle({ cx: 210, cy: 950, r: 108, fill: INK, opacity: 0.92 }) +
    circle({ cx: 1410, cy: 968, r: 96, fill: INK, opacity: 0.88 });
  return { far, main, near };
}

const SCENES: Record<SceneKind, (rng: Rng, uid: string) => Layers> = {
  "control-room": controlRoom,
  racks,
  workspace,
  skyline,
  workshop,
};

export function renderSceneSvg(kind: SceneKind, seed: string): string {
  const rng = createRandom(`${kind}:${seed}`);
  const uid = hashSeed(`scene:${kind}:${seed}`).toString(36);
  const lightX = intBetween(rng, 32, 68);
  const { far, main, near } = SCENES[kind](rng, uid);

  const stop = (offset: string, color: string, opacity?: number) =>
    el("stop", { offset, "stop-color": color, "stop-opacity": opacity });

  const defs = [
    // Depth of field on the far and near planes.
    el("filter", { id: `ff-${uid}`, x: "-10%", y: "-10%", width: "120%", height: "120%" },
      el("feGaussianBlur", { stdDeviation: 5 })),
    el("filter", { id: `nf-${uid}`, x: "-15%", y: "-15%", width: "130%", height: "130%" },
      el("feGaussianBlur", { stdDeviation: 18 })),
    // Film grain. Monochrome noise at low opacity, which is what stops this reading as vector art.
    el("filter", { id: `gr-${uid}`, x: 0, y: 0, width: 200, height: 200, filterUnits: "userSpaceOnUse" },
      el("feTurbulence", { type: "fractalNoise", baseFrequency: "0.8", numOctaves: 2, seed: hashSeed(seed) % 9999, result: "n" }) +
      el("feColorMatrix", { type: "saturate", values: "0", in: "n", result: "m" }) +
      el("feComponentTransfer", { in: "m" }, el("feFuncA", { type: "linear", slope: "0.5" }))),
    el("pattern", { id: `gp-${uid}`, width: 200, height: 200, patternUnits: "userSpaceOnUse" },
      rect({ width: 200, height: 200, filter: `url(#gr-${uid})` })),
    // Bokeh needs less defocus than the foreground plane, and a cheaper blur with it.
    el("filter", { id: `bf-${uid}`, x: "-20%", y: "-20%", width: "140%", height: "140%" },
      el("feGaussianBlur", { stdDeviation: 12 })),
    el("linearGradient", { id: `sk-${uid}`, x1: 0, y1: 0, x2: 0, y2: 1 },
      stop("0%", STEEL) + stop("48%", "#132446") + stop("100%", DEEP)),
    el("radialGradient", { id: `bl-${uid}`, cx: `${lightX}%`, cy: "30%", r: "62%" },
      stop("0%", GLOW, 0.62) + stop("100%", GLOW, 0)),
    // A warm counter-light so the frame is not uniformly blue — standard colour grading.
    el("radialGradient", { id: `wm-${uid}`, cx: `${100 - lightX}%`, cy: "76%", r: "50%" },
      stop("0%", AMBER, 0.2) + stop("100%", AMBER, 0)),
    el("radialGradient", { id: `vg-${uid}`, cx: "50%", cy: "45%", r: "74%" },
      stop("55%", "#000000", 0) + stop("100%", "#000000", 0.52)),
    el("linearGradient", { id: `fl-${uid}`, x1: 0, y1: 0, x2: 1, y2: 0 },
      stop("0%", GLOW, 0) + stop("50%", CYAN, 0.75) + stop("100%", GLOW, 0)),
    el("linearGradient", { id: `ai-${uid}`, x1: 0, y1: 0, x2: 1, y2: 0 },
      stop("0%", CYAN, 0) + stop("50%", CYAN, 0.34) + stop("100%", CYAN, 0)),
    el("linearGradient", { id: `dg-${uid}`, x1: 0, y1: 0, x2: 0, y2: 1 },
      stop("0%", GLOW, 0.5) + stop("100%", GLOW, 0)),
    el("linearGradient", { id: `pg-${uid}`, x1: 0, y1: 0, x2: 0, y2: 1 },
      stop("0%", GLOW, 0.55) + stop("100%", GLOW, 0)),
    el("linearGradient", { id: `hz-${uid}`, x1: 0, y1: 0, x2: 0, y2: 1 },
      stop("0%", AMBER, 0.28) + stop("100%", AMBER, 0)),
  ].join("");

  const body =
    rect({ width: W, height: H, fill: `url(#sk-${uid})` }) +
    rect({ width: W, height: H, fill: `url(#bl-${uid})` }) +
    el("g", { filter: `url(#ff-${uid})`, opacity: 0.9 }, far) +
    main +
    bokeh(rng, uid, 9, [CYAN, GLOW, WARM]) +
    el("g", { filter: `url(#nf-${uid})` }, near) +
    rect({ width: W, height: H, fill: `url(#wm-${uid})` }) +
    rect({ width: W, height: H, fill: `url(#vg-${uid})` }) +
    rect({ width: W, height: H, fill: `url(#gp-${uid})`, opacity: 0.16 });

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

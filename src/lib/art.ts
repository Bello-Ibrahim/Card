/**
 * Deterministic art helpers.
 *
 * Generated visuals must render identically on the server and the client, and must not
 * change between builds — so everything here is a pure function of a string seed
 * (usually a slug). No Math.random, no Date.
 */

/** FNV-1a string hash → 32-bit unsigned integer. */
export function hashSeed(input: string): number {
  let hash = 0x811c9dc5;
  for (let i = 0; i < input.length; i += 1) {
    hash ^= input.charCodeAt(i);
    hash = Math.imul(hash, 0x01000193);
  }
  return hash >>> 0;
}

/** mulberry32 — small, fast, well-distributed PRNG. */
export function createRandom(seed: string) {
  let state = hashSeed(seed);
  return function random() {
    state = (state + 0x6d2b79f5) >>> 0;
    let t = state;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export type Rng = ReturnType<typeof createRandom>;

/** Random float in [min, max). */
export const between = (rng: Rng, min: number, max: number) => min + rng() * (max - min);

/** Random integer in [min, max]. */
export const intBetween = (rng: Rng, min: number, max: number) =>
  Math.floor(between(rng, min, max + 1));

export const pick = <T,>(rng: Rng, items: readonly T[]): T => items[intBetween(rng, 0, items.length - 1)];

/** Round to 2dp so server and client markup match byte for byte. */
export const fix = (value: number) => Math.round(value * 100) / 100;

/**
 * Accent ramp used by every generated visual, so covers across the site read as one system.
 * Values are literal hex rather than CSS variables because they are also used inside
 * `next/og` image generation, which has no access to the stylesheet.
 */
export const ART_COLORS = {
  ink: "#04060c",
  navy: "#050a18",
  navyMid: "#0a1830",
  navyLift: "#123063",
  accent: "#2f6bff",
  accentSoft: "#5b93ff",
  cyan: "#38d9f0",
  teal: "#2fd8a8",
} as const;

export const ACCENT_RAMP = [ART_COLORS.accentSoft, ART_COLORS.cyan, ART_COLORS.teal] as const;

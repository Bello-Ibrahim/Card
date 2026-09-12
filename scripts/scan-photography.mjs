#!/usr/bin/env node
/**
 * Scans public/photography/ and writes the map that src/content/media.ts reads.
 *
 * This is what makes supplying photography a file-drop rather than a code change: name the
 * file after the slot (hero-operations.jpg) and the next build picks it up. Runs before
 * `dev` and `build`.
 */
import { readdirSync, writeFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { join, dirname, extname, basename } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const photoDir = join(root, "public", "photography");
const outFile = join(root, "src", "content", "photo-files.json");

const EXTENSIONS = new Set([".jpg", ".jpeg", ".png", ".webp", ".avif"]);

/** hero-operations -> heroOperations */
const toCamel = (name) => name.replace(/-([a-z0-9])/g, (_, c) => c.toUpperCase());

mkdirSync(photoDir, { recursive: true });
mkdirSync(dirname(outFile), { recursive: true });

const found = {};
for (const entry of readdirSync(photoDir)) {
  const ext = extname(entry).toLowerCase();
  if (!EXTENSIONS.has(ext)) continue;
  found[toCamel(basename(entry, ext))] = `/photography/${entry}`;
}

const next = `${JSON.stringify(found, null, 2)}\n`;
const current = existsSync(outFile) ? readFileSync(outFile, "utf8") : "";
if (current !== next) writeFileSync(outFile, next);

const count = Object.keys(found).length;
console.log(
  count
    ? `[photography] ${count} image${count === 1 ? "" : "s"} detected: ${Object.keys(found).join(", ")}`
    : "[photography] no images in public/photography — designed scenes will be used",
);

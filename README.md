# GraceWell Consulting Group — Website

Enterprise marketing site for **GraceWell Consulting Group**, a data engineering consulting and
technology advisory firm.

> Engineering the data foundations behind better decisions.

Built with Next.js (App Router), TypeScript and Tailwind CSS. Every page is statically
prerendered, ships ~102 kB of shared JavaScript, and is designed to be edited by the marketing
team without touching component code.

---

## Quick start

```bash
npm install
cp .env.example .env.local   # then fill in the values below
npm run dev                  # http://localhost:3000
```

Other scripts:

```bash
npm run build      # production build (prerenders every route)
npm run start      # serve the production build
npm run lint       # ESLint
npm run typecheck  # tsc --noEmit
```

---

## Before you launch — required configuration

Two things must be set or the site will be live with placeholders:

### 1. Environment variables (`.env.local`)

| Variable | Required | Purpose |
| --- | --- | --- |
| `NEXT_PUBLIC_SITE_URL` | **Yes** | Canonical URLs, `sitemap.xml`, `robots.txt`, Open Graph. Defaults to `https://www.gracewellconsulting.com`. |
| `CONTACT_WEBHOOK_URL` | **Yes** | HTTPS endpoint that receives contact-form submissions as a JSON `POST` (CRM webhook, Zapier/Make hook, or a small function that emails your inbox). |
| `CONTACT_WEBHOOK_SECRET` | No | Sent as the `x-gracewell-signature` header so your endpoint can verify the caller. |

> **Important:** if `CONTACT_WEBHOOK_URL` is unset, submissions are validated and written to the
> server log with a warning, but **nobody receives them**. Set it before launch.

The webhook receives:

```json
{
  "fullName": "…", "workEmail": "…", "company": "…", "jobTitle": "…",
  "country": "…", "phone": "…", "topic": "…", "scope": "…",
  "engagementType": "…", "message": "…",
  "submittedAt": "2026-09-04T09:00:00.000Z",
  "source": "gracewellconsulting.com/contact"
}
```

### 2. Verified contact channels — `src/content/site.ts`

Email, phone, office location and social profiles are all `null` by default and the UI hides
each one until it is filled in. Nothing is invented. Set the values you have confirmed:

```ts
export const contact = {
  email: "hello@gracewellconsulting.com",
  phone: null,
  location: null,
  linkedin: "https://www.linkedin.com/company/…",
  x: null,
  youtube: null,
};
```

Filling these in automatically adds them to the footer, the contact page, the About page and the
`sameAs` / `contactPoint` fields of the Organization structured data.

---

## Editing content

All copy lives in `src/content/` as typed data. Add, remove or reorder an entry and every page,
navigation menu and `sitemap.xml` entry that uses it updates automatically.

| File | Drives |
| --- | --- |
| `site.ts` | Company name, tagline, description, contact channels, primary CTAs |
| `navigation.ts` | Header nav and mega-menus, footer columns, legal links |
| `services.ts` | Services section + one detail page per service |
| `solutions.ts` | Solutions section + one detail page per solution |
| `industries.ts` | Industries page and home section |
| `approach.ts` | The six-step Discover → Scale timeline |
| `training.ts` | Training tracks and teaching principles |
| `team-setup.ts` | Build / Scale / Enable modes and capability list |
| `technologies.ts` | Technology ecosystem and the hero credibility strip |
| `why.ts` | The six "Why GraceWell" pillars |
| `case-studies.ts` | Case studies (see the honesty rules below) |
| `insights.ts` | Articles, categories and article bodies |
| `faqs.ts` | FAQ accordion + FAQ structured data |

### Adding an article

Append an entry to `insights` in `src/content/insights.ts`. The route, the card, the search
index, `Article` structured data and the sitemap entry are all generated from it.

### Adding a real case study

`src/content/case-studies.ts` ships three **illustrative** engagement patterns. They name no
client and state no metric, and the UI labels them "Illustrative" while `verified: false`.

When a client approves publication, set `verified: true`, add `client`, and include only figures
the client has agreed to. The disclosure banner disappears automatically.

---

## Content honesty rules

This site is deliberately built so it cannot drift into unsupported claims. **Do not add**
client logos, client names, testimonials, certifications, awards, partnerships, revenue figures,
project metrics, employee counts, years of experience, office addresses or case-study statistics
unless GraceWell has verified them.

Where a fact is not available the pattern is: leave the field `null` and let the UI hide it, or
label the content as illustrative. That convention is already applied to contact details,
leadership profiles, careers listings and case studies.

The technology list is a list of tools GraceWell's engineers work with — it is not a claim of
vendor partnership, certification or affiliation, and the ecosystem section says so on the page.

---

## Architecture

```
src/
  app/                     # Routes (App Router)
    layout.tsx             # Fonts, global metadata, Organization + WebSite JSON-LD
    page.tsx               # Home
    services/…             # Index + [slug] detail
    solutions/…            # Index + [slug] detail
    insights/…             # Index (search/filter) + [slug] article
    case-studies/…         # Index + [slug] detail
    contact/
      page.tsx             # Static page
      actions.ts           # "use server" — submit + validate + deliver
      form-state.ts        # Shared types/constants (a "use server" file may only export functions)
    industries|training|team-setup|about/
    privacy-policy|terms-of-use|cookie-policy/
    sitemap.ts robots.ts not-found.tsx opengraph-image.tsx icon.svg
  components/              # Reusable UI (header, footer, hero, cards, sections, form)
    ui/                    # Primitives: container, button, section header, reveal, icon, json-ld
  content/                 # All copy — see the table above
  lib/                     # seo.ts (metadata), schema.ts (JSON-LD), utils.ts
```

### Design system

Tokens are defined once in `src/app/globals.css` under `@theme` (Tailwind v4, CSS-first config):
a midnight-navy / near-black / white / soft-gray core with electric blue, cyan and teal accents,
plus fluid `text-display` / `text-headline` / `text-subhead` / `text-lede` type steps. Fonts are
Manrope (display) and Inter (body), self-hosted through `next/font`.

### Motion

Scroll entrances use one `IntersectionObserver` per element (`components/ui/reveal.tsx`) that
disconnects after firing. The hero architecture diagram is inline SVG animated with CSS only —
no animation library, no image request. Every animation is switched off by the
`prefers-reduced-motion` block at the bottom of `globals.css`.

---

## SEO

- Per-page canonical URLs, titles, descriptions and keywords via `lib/seo.ts`
- Open Graph + Twitter card metadata; the OG image is generated at `app/opengraph-image.tsx`
- Structured data: `Organization`, `WebSite`, `Service`, `Article`, `FAQPage`, `BreadcrumbList`
- Generated `sitemap.xml` (45 URLs) and `robots.txt`
- Semantic landmarks, one `<h1>` per page, descriptive slugs, internal linking between
  services, solutions, industries and insights

## Accessibility

Targets WCAG 2.2 AA: skip link, visible focus rings on both light and dark sections, keyboard
operable navigation (mega-menus close on `Escape` and outside click), labelled form controls with
`aria-invalid` / `aria-describedby` error wiring, live regions for form status, and full
reduced-motion support.

---

## Deployment

Any host that runs Next.js works. The site is fully static apart from the contact form's server
action, so it also fits serverless/edge platforms well.

```bash
npm run build && npm run start
```

Set `NEXT_PUBLIC_SITE_URL` and `CONTACT_WEBHOOK_URL` in your host's environment before the first
production deploy.

---

## Legal pages

`/privacy-policy`, `/terms-of-use` and `/cookie-policy` are written to describe how this site
actually behaves (it sets no analytics or advertising cookies as published). **Have your counsel
review them before launch**, and update them whenever analytics, marketing tooling or
third-party embeds are added.

---

## `legacy/`

`legacy/animal-trading-card/` holds the original static exercise that previously lived at the
repository root. It is unrelated to this site and is excluded from the build, TypeScript and
ESLint. Delete it whenever you like.

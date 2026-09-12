# Photography

Drop image files in this folder and they appear on the site — **no code change needed**.

## How it works

Name the file after its slot in kebab-case and the prebuild scan picks it up:

```
public/photography/hero-operations.jpg   ->  the hero background
```

Accepted extensions: `.jpg` `.jpeg` `.png` `.webp` `.avif`. Run `npm run photos` to see what
was detected, or just `npm run dev` / `npm run build` — the scan runs automatically.

Images are served through `next/image`, so they are converted to AVIF/WebP and resized per
breakpoint at build time. Supply the largest version you have (2400px wide is plenty).

Any slot without a file renders a designed cinematic scene instead, so the site is never
broken by a missing image.

## Art direction

Cinematic, high contrast, dark modern environments; professional African and international
teams; real technology settings. **Avoid** handshakes, people pointing at charts, overly
cheerful stock photography, and meaningless dashboards.

> Do not use photographs of people, offices or events to represent DataForge's team, clients
> or premises unless they genuinely are DataForge's.

## The slots

| File name | What it is | Brief |
| --- | --- | --- |
| `hero-operations.jpg` | Data engineers working in a technology operations centre, reviewing pipeline dashboards across multiple screens. | Wide, cinematic. A modern technology operations environment at low light, several engineers at multi-monitor desks, screen glow as the main light source. Shot from behind or side — faces need not be identifiable. |
| `trust-banner.jpg` | A technology operations floor with engineers monitoring data infrastructure. | Full-bleed banner, 21:9. Operations floor or engineering war room. Dark, high contrast, depth. Room for a text overlay on the left third. |
| `service-data-engineering.jpg` | A data engineer working across multiple monitors showing pipeline code and job runs. | Close, over-the-shoulder. Terminal, DAG view and SQL on screen. Warm key light, cool screen light. |
| `service-architecture.jpg` | Engineers designing a cloud data architecture on a large whiteboard. | Two or three engineers at a whiteboard or glass wall covered in architecture sketches. Mid-discussion, not posed. |
| `service-cloud.jpg` | Cloud infrastructure hardware in a modern data centre. | Cold-aisle data centre corridor, shallow depth of field, status LEDs in focus. |
| `service-integration.jpg` | An engineer tracing data flows between systems on screen. | Desk detail. Hands, keyboard, a screen showing connected systems. Tight crop. |
| `service-modernization.jpg` | A legacy server room alongside modern cloud infrastructure. | Older on-premise server room, slightly warmer and more cluttered than the modern data centre shots. Used as the 'before' half of a comparison. |
| `team-setup.jpg` | A diverse data engineering team collaborating around a shared screen. | Five or six engineers, genuinely mixed, gathered around one screen or a standing desk. Candid, working, not smiling at camera. |
| `training.jpg` | An instructor leading a technical data engineering workshop. | Instructor at a screen, engineers with laptops open. Real code visible. Workshop, not lecture theatre. |
| `about.jpg` | The engineering environment where DataForge builds data platforms. | Editorial, wide. Engineering floor or studio. Should feel like a real working company rather than a stock office. |
| `contact.jpg` | A modern engineering workspace. | Tall portrait crop for the contact page's left column. Dark, architectural, calm. |
| `industry-financial-services.jpg` | Financial technology infrastructure and trading analytics screens. | Banking or fintech technology environment. Dense market or payments data on screen. |
| `industry-telecommunications.jpg` | Telecommunications network operations centre. | NOC with network topology on a video wall, or telecom tower infrastructure at dusk. |
| `industry-healthcare.jpg` | Clinical technology systems in a modern hospital. | Hospital technology environment — clinical systems, not patients. Respect privacy. |
| `industry-retail.jpg` | Retail and e-commerce fulfilment technology. | Modern fulfilment or retail operations with technology visible. |
| `industry-logistics.jpg` | Logistics operations with fleet and shipment tracking systems. | Warehouse or transport control room with tracking screens. |
| `industry-manufacturing.jpg` | Modern industrial facility with connected production systems. | Clean modern plant floor, machine telemetry displays visible. |
| `industry-government.jpg` | Public sector technology and data operations environment. | Government technology environment. Neutral, institutional, modern. |
| `industry-technology.jpg` | Software engineering team working in a modern technology company. | Engineering floor, code on screens, collaborative. |
| `case-modernization.jpg` | Enterprise data infrastructure undergoing modernization. | Data centre or platform migration context. Dark and technical. |
| `case-migration.jpg` | Engineers overseeing a data warehouse migration. | Two engineers, screens showing reconciliation output. |
| `case-team.jpg` | A newly formed internal data engineering team at work. | Team in a working session. Mixed seniority, genuinely diverse. |

22 slots in total. The `alt` text for each is already written in
`src/content/media.ts` and ships with the image.

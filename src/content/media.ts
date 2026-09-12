/**
 * Photography manifest.
 *
 * Every photographic slot the design calls for is declared here. Each entry ships with
 * finished alt text and an art-direction brief, so sourcing a licensed image is a one-line
 * change: set `src` to the file path and the real photograph replaces the designed scene
 * everywhere that slot is used.
 *
 * `src` is null until DataForge supplies a licensed or original photograph. We do not ship
 * stock images of people, offices or teams presented as DataForge's own.
 *
 * Art direction for all photography: cinematic, high contrast, dark modern environments,
 * professional African and international teams, real technology settings. No handshakes,
 * no people pointing at charts, no meaningless dashboards.
 */

export type SceneKind = "control-room" | "racks" | "workspace" | "skyline" | "workshop";

export type Photo = {
  /** Path under /public once supplied, e.g. "/photography/hero-operations.jpg". */
  src: string | null;
  /** Written now so it ships with the image rather than being retrofitted. */
  alt: string;
  /** Art direction for whoever sources or shoots the image. */
  brief: string;
  /** Designed fallback rendered until a photograph is supplied. */
  scene: SceneKind;
};

export const photos = {
  heroOperations: {
    src: null,
    alt: "Data engineers working in a technology operations centre, reviewing pipeline dashboards across multiple screens.",
    brief:
      "Wide, cinematic. A modern technology operations environment at low light, several engineers at multi-monitor desks, screen glow as the main light source. Shot from behind or side — faces need not be identifiable.",
    scene: "control-room",
  },
  trustBanner: {
    src: null,
    alt: "A technology operations floor with engineers monitoring data infrastructure.",
    brief:
      "Full-bleed banner, 21:9. Operations floor or engineering war room. Dark, high contrast, depth. Room for a text overlay on the left third.",
    scene: "control-room",
  },
  serviceDataEngineering: {
    src: null,
    alt: "A data engineer working across multiple monitors showing pipeline code and job runs.",
    brief: "Close, over-the-shoulder. Terminal, DAG view and SQL on screen. Warm key light, cool screen light.",
    scene: "workspace",
  },
  serviceArchitecture: {
    src: null,
    alt: "Engineers designing a cloud data architecture on a large whiteboard.",
    brief: "Two or three engineers at a whiteboard or glass wall covered in architecture sketches. Mid-discussion, not posed.",
    scene: "workshop",
  },
  serviceCloud: {
    src: null,
    alt: "Cloud infrastructure hardware in a modern data centre.",
    brief: "Cold-aisle data centre corridor, shallow depth of field, status LEDs in focus.",
    scene: "racks",
  },
  serviceIntegration: {
    src: null,
    alt: "An engineer tracing data flows between systems on screen.",
    brief: "Desk detail. Hands, keyboard, a screen showing connected systems. Tight crop.",
    scene: "workspace",
  },
  serviceModernization: {
    src: null,
    alt: "A legacy server room alongside modern cloud infrastructure.",
    brief: "Older on-premise server room, slightly warmer and more cluttered than the modern data centre shots. Used as the 'before' half of a comparison.",
    scene: "racks",
  },
  teamSetup: {
    src: null,
    alt: "A diverse data engineering team collaborating around a shared screen.",
    brief: "Five or six engineers, genuinely mixed, gathered around one screen or a standing desk. Candid, working, not smiling at camera.",
    scene: "workshop",
  },
  training: {
    src: null,
    alt: "An instructor leading a technical data engineering workshop.",
    brief: "Instructor at a screen, engineers with laptops open. Real code visible. Workshop, not lecture theatre.",
    scene: "workshop",
  },
  about: {
    src: null,
    alt: "The engineering environment where DataForge builds data platforms.",
    brief: "Editorial, wide. Engineering floor or studio. Should feel like a real working company rather than a stock office.",
    scene: "control-room",
  },
  contact: {
    src: null,
    alt: "A modern engineering workspace.",
    brief: "Tall portrait crop for the contact page's left column. Dark, architectural, calm.",
    scene: "workspace",
  },
  industryFinancialServices: {
    src: null,
    alt: "Financial technology infrastructure and trading analytics screens.",
    brief: "Banking or fintech technology environment. Dense market or payments data on screen.",
    scene: "skyline",
  },
  industryTelecommunications: {
    src: null,
    alt: "Telecommunications network operations centre.",
    brief: "NOC with network topology on a video wall, or telecom tower infrastructure at dusk.",
    scene: "control-room",
  },
  industryHealthcare: {
    src: null,
    alt: "Clinical technology systems in a modern hospital.",
    brief: "Hospital technology environment — clinical systems, not patients. Respect privacy.",
    scene: "workspace",
  },
  industryRetail: {
    src: null,
    alt: "Retail and e-commerce fulfilment technology.",
    brief: "Modern fulfilment or retail operations with technology visible.",
    scene: "skyline",
  },
  industryLogistics: {
    src: null,
    alt: "Logistics operations with fleet and shipment tracking systems.",
    brief: "Warehouse or transport control room with tracking screens.",
    scene: "control-room",
  },
  industryManufacturing: {
    src: null,
    alt: "Modern industrial facility with connected production systems.",
    brief: "Clean modern plant floor, machine telemetry displays visible.",
    scene: "skyline",
  },
  industryGovernment: {
    src: null,
    alt: "Public sector technology and data operations environment.",
    brief: "Government technology environment. Neutral, institutional, modern.",
    scene: "skyline",
  },
  industryTechnology: {
    src: null,
    alt: "Software engineering team working in a modern technology company.",
    brief: "Engineering floor, code on screens, collaborative.",
    scene: "workspace",
  },
  caseModernization: {
    src: null,
    alt: "Enterprise data infrastructure undergoing modernization.",
    brief: "Data centre or platform migration context. Dark and technical.",
    scene: "racks",
  },
  caseMigration: {
    src: null,
    alt: "Engineers overseeing a data warehouse migration.",
    brief: "Two engineers, screens showing reconciliation output.",
    scene: "workspace",
  },
  caseTeam: {
    src: null,
    alt: "A newly formed internal data engineering team at work.",
    brief: "Team in a working session. Mixed seniority, genuinely diverse.",
    scene: "workshop",
  },
} satisfies Record<string, Photo>;

export type PhotoKey = keyof typeof photos;

/** True once at least one real photograph has been supplied. */
export const hasPhotography = Object.values(photos).some((photo) => photo.src !== null);

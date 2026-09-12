/**
 * Shared shape for the contact form.
 *
 * Deliberately NOT in `actions.ts`: a "use server" module may only export async functions,
 * so constants and types live in a plain module both the action and the client form import.
 */

export const CONTACT_FIELDS = [
  "fullName",
  "workEmail",
  "company",
  "jobTitle",
  "country",
  "phone",
  "service",
  "description",
  "timeline",
  "budget",
  "engagement",
] as const;

export type ContactField = (typeof CONTACT_FIELDS)[number];

export type ContactFormState = {
  status: "idle" | "success" | "error";
  message: string;
  errors: Partial<Record<ContactField, string>>;
  /** Echoed back so the form can repopulate after a failed submission. */
  values: Partial<Record<ContactField, string>>;
};

export const initialContactState: ContactFormState = {
  status: "idle",
  message: "",
  errors: {},
  values: {},
};

export const REQUIRED_FIELDS: ContactField[] = [
  "fullName",
  "workEmail",
  "company",
  "jobTitle",
  "country",
  "service",
  "description",
];

export const MAX_LENGTHS: Record<ContactField, number> = {
  fullName: 120,
  workEmail: 200,
  company: 160,
  jobTitle: 120,
  country: 80,
  phone: 40,
  service: 120,
  description: 4000,
  timeline: 80,
  budget: 80,
  engagement: 80,
};

export const FIELD_LABELS: Record<ContactField, string> = {
  fullName: "Name",
  workEmail: "Work email",
  company: "Company",
  jobTitle: "Job title",
  country: "Country",
  phone: "Phone",
  service: "Service required",
  description: "Project description",
  timeline: "Expected timeline",
  budget: "Budget range",
  engagement: "Preferred engagement",
};

export const SERVICE_OPTIONS = [
  "Data Engineering",
  "Data Architecture",
  "Cloud Data Engineering",
  "Data Integration",
  "Data Modernization / Migration",
  "Analytics Engineering",
  "Data Quality & Observability",
  "Data Strategy & Advisory",
  "Training",
  "Team Setup",
  "Managed Data Engineering",
  "Not sure yet",
];

export const TIMELINE_OPTIONS = [
  "Exploring options",
  "Within 1 month",
  "1–3 months",
  "3–6 months",
  "6+ months",
];

export const BUDGET_OPTIONS = [
  "Not yet defined",
  "Assessment or advisory engagement",
  "Focused project",
  "Multi-phase programme",
  "Ongoing / managed engagement",
];

export const ENGAGEMENT_OPTIONS = [
  "Consulting",
  "Project delivery",
  "Staff augmentation",
  "Managed services",
  "Architecture review",
  "Training",
  "Team setup",
  "Other",
];

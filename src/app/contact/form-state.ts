/**
 * Shared shape for the contact form.
 *
 * Deliberately NOT in `actions.ts`: a "use server" module may only export async
 * functions, so constants and types have to live in a plain module that both the
 * server action and the client form can import.
 */

export const CONTACT_FIELDS = [
  "fullName",
  "workEmail",
  "company",
  "jobTitle",
  "country",
  "phone",
  "topic",
  "scope",
  "engagementType",
  "message",
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
  "topic",
  "engagementType",
  "message",
];

export const MAX_LENGTHS: Record<ContactField, number> = {
  fullName: 120,
  workEmail: 200,
  company: 160,
  jobTitle: 120,
  country: 80,
  phone: 40,
  topic: 120,
  scope: 120,
  engagementType: 80,
  message: 4000,
};

export const FIELD_LABELS: Record<ContactField, string> = {
  fullName: "Full name",
  workEmail: "Work email",
  company: "Company",
  jobTitle: "Job title",
  country: "Country",
  phone: "Phone number",
  topic: "What we can help with",
  scope: "Estimated project scope",
  engagementType: "Preferred engagement type",
  message: "Message",
};

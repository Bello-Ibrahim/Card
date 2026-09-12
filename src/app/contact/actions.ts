"use server";

import {
  CONTACT_FIELDS,
  FIELD_LABELS,
  MAX_LENGTHS,
  REQUIRED_FIELDS,
  type ContactField,
  type ContactFormState,
} from "./form-state";

// Deliberately permissive: the goal is to catch typos, not to reject valid addresses.
const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

export async function submitContactForm(
  _prevState: ContactFormState,
  formData: FormData,
): Promise<ContactFormState> {
  const values = Object.fromEntries(
    CONTACT_FIELDS.map((field) => [field, String(formData.get(field) ?? "").trim()]),
  ) as Record<ContactField, string>;

  // Honeypot: real users never fill a visually hidden field. Accept silently so bots
  // get no signal about why the submission went nowhere.
  if (String(formData.get("company_website") ?? "").trim()) {
    return {
      status: "success",
      message: "Thank you — your enquiry has been received.",
      errors: {},
      values: {},
    };
  }

  const errors: Partial<Record<ContactField, string>> = {};

  for (const field of REQUIRED_FIELDS) {
    if (!values[field]) errors[field] = `${FIELD_LABELS[field]} is required.`;
  }

  for (const field of CONTACT_FIELDS) {
    if (values[field].length > MAX_LENGTHS[field]) {
      errors[field] = `${FIELD_LABELS[field]} must be ${MAX_LENGTHS[field]} characters or fewer.`;
    }
  }

  if (values.workEmail && !EMAIL.test(values.workEmail)) {
    errors.workEmail = "Enter a valid email address.";
  }

  if (values.description && values.description.length < 20) {
    errors.description = "Please give us a little more detail — at least 20 characters.";
  }

  if (Object.keys(errors).length) {
    return {
      status: "error",
      message: "Please correct the highlighted fields and try again.",
      errors,
      values,
    };
  }

  const submission = {
    ...values,
    submittedAt: new Date().toISOString(),
    source: "dataforgeconsulting.com/contact",
  };

  const webhook = process.env.CONTACT_WEBHOOK_URL;

  if (!webhook) {
    // No delivery target configured. Record it server-side so the submission is not lost
    // from the logs, and warn the operator. Set CONTACT_WEBHOOK_URL before launch.
    console.warn(
      "[contact] CONTACT_WEBHOOK_URL is not set — submission was logged but not delivered.",
      submission,
    );
    return {
      status: "success",
      message: "Thank you — your enquiry has been received. We'll be in touch shortly.",
      errors: {},
      values: {},
    };
  }

  try {
    const response = await fetch(webhook, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        ...(process.env.CONTACT_WEBHOOK_SECRET
          ? { "x-dataforge-signature": process.env.CONTACT_WEBHOOK_SECRET }
          : {}),
      },
      body: JSON.stringify(submission),
      cache: "no-store",
    });

    if (!response.ok) {
      throw new Error(`Delivery endpoint responded ${response.status}`);
    }
  } catch (error) {
    console.error("[contact] Failed to deliver submission", error);
    return {
      status: "error",
      message:
        "Something went wrong sending your enquiry. Please try again in a moment, or reach out through one of the channels listed on this page.",
      errors: {},
      values,
    };
  }

  return {
    status: "success",
    message: "Thank you — your enquiry has been received. We'll be in touch shortly.",
    errors: {},
    values: {},
  };
}

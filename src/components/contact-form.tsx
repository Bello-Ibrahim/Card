"use client";

import { useActionState, useEffect, useId, useMemo, useRef } from "react";
import { useFormStatus } from "react-dom";
import { useSearchParams } from "next/navigation";
import { submitContactForm } from "@/app/contact/actions";
import {
  BUDGET_OPTIONS,
  ENGAGEMENT_OPTIONS,
  SERVICE_OPTIONS,
  TIMELINE_OPTIONS,
  initialContactState,
  type ContactField,
} from "@/app/contact/form-state";
import { Button, Arrow } from "@/components/ui/button";
import { cn } from "@/lib/utils";

/**
 * Deep links such as /contact?topic=training pre-select the right options so a visitor
 * arriving from a service or training page does not restate what they already told us.
 */
const SERVICE_PREFILL: Record<string, string> = {
  training: "Training",
  "team-setup": "Team Setup",
  consultation: "Data Strategy & Advisory",
  project: "Data Engineering",
  careers: "Not sure yet",
};

const ENGAGEMENT_PREFILL: Record<string, string> = {
  training: "Training",
  "team-setup": "Team setup",
  consultation: "Consulting",
  project: "Project delivery",
};

const fieldClass =
  "h-12 w-full rounded-xl border bg-white px-4 text-[0.9375rem] text-navy-950 transition-colors placeholder:text-mist-500 focus:outline-none focus:ring-2 focus:ring-accent-500/25";

function Field({
  id,
  label,
  error,
  required,
  hint,
  children,
}: {
  id: string;
  label: string;
  error?: string;
  required?: boolean;
  hint?: string;
  children: React.ReactNode;
}) {
  return (
    <div className="flex flex-col gap-2">
      <label htmlFor={id} className="text-[0.875rem] font-medium text-navy-900">
        {label}
        {required ? (
          <span aria-hidden="true" className="ml-1 text-accent-600">
            *
          </span>
        ) : (
          <span className="ml-1.5 font-normal text-mist-500">(optional)</span>
        )}
      </label>
      {children}
      {hint && !error ? (
        <p id={`${id}-hint`} className="text-[0.8125rem] text-mist-500">
          {hint}
        </p>
      ) : null}
      {error ? (
        <p id={`${id}-error`} className="text-[0.8125rem] font-medium text-red-600">
          {error}
        </p>
      ) : null}
    </div>
  );
}

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <Button type="submit" size="lg" disabled={pending} className="w-full sm:w-auto">
      {pending ? "Sending…" : "Start the Conversation"}
      {pending ? null : <Arrow />}
    </Button>
  );
}

export function ContactForm() {
  const [state, formAction] = useActionState(submitContactForm, initialContactState);
  const searchParams = useSearchParams();
  const uid = useId();

  const defaults = useMemo<Partial<Record<ContactField, string>>>(() => {
    const intent = searchParams.get("intent") ?? "";
    const program = searchParams.get("program");
    const mode = searchParams.get("mode");

    const parts = [
      intent === "careers" ? "I'm interested in working at DataForge." : "",
      program ? `I'd like to know more about the ${program.replace(/-/g, " ")} program.` : "",
      mode ? `We're looking at the "${mode}" route for our data team.` : "",
    ].filter(Boolean);

    return {
      ...(SERVICE_PREFILL[intent] ? { service: SERVICE_PREFILL[intent] } : {}),
      ...(ENGAGEMENT_PREFILL[intent] ? { engagement: ENGAGEMENT_PREFILL[intent] } : {}),
      ...(parts.length ? { description: `${parts.join(" ")} ` } : {}),
    };
  }, [searchParams]);

  const statusRef = useRef<HTMLDivElement>(null);
  const formRef = useRef<HTMLFormElement>(null);

  const id = (name: string) => `${uid}-${name}`;
  const value = (field: ContactField) => state.values[field] ?? defaults[field] ?? "";
  const invalid = (field: ContactField) => Boolean(state.errors[field]);
  const describedBy = (field: ContactField, hasHint = false) => {
    const parts: string[] = [];
    if (state.errors[field]) parts.push(`${id(field)}-error`);
    else if (hasHint) parts.push(`${id(field)}-hint`);
    return parts.length ? parts.join(" ") : undefined;
  };

  const borderFor = (field: ContactField) =>
    invalid(field) ? "border-red-500" : "border-navy-950/12 focus:border-accent-500";

  // Move focus to the status region so the outcome is announced and reachable.
  useEffect(() => {
    if (state.status === "idle") return;
    statusRef.current?.focus();
    if (state.status === "success") formRef.current?.reset();
  }, [state]);

  if (state.status === "success") {
    return (
      <div
        ref={statusRef}
        tabIndex={-1}
        role="status"
        className="rounded-2xl border border-teal-500/30 bg-teal-50 p-10 text-center"
      >
        <span
          aria-hidden="true"
          className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-teal-500 text-white"
        >
          <svg viewBox="0 0 16 16" className="h-5 w-5">
            <path
              d="M3 8.4 6.3 11.7 13 5"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.9"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </span>
        <h3 className="mt-5 text-[1.25rem] font-semibold tracking-[-0.02em] text-navy-950">
          Enquiry received
        </h3>
        <p className="mx-auto mt-3 max-w-md text-[0.9375rem] leading-relaxed text-mist-600">
          {state.message}
        </p>
      </div>
    );
  }

  return (
    <form ref={formRef} action={formAction} noValidate className="flex flex-col gap-6">
      {state.status === "error" ? (
        <div
          ref={statusRef}
          tabIndex={-1}
          role="alert"
          className="rounded-xl border border-red-500/30 bg-red-50 px-5 py-4 text-[0.9375rem] text-red-800"
        >
          {state.message}
        </div>
      ) : null}

      <div className="grid gap-6 sm:grid-cols-2">
        <Field id={id("fullName")} label="Full name" required error={state.errors.fullName}>
          <input
            id={id("fullName")}
            name="fullName"
            type="text"
            autoComplete="name"
            defaultValue={value("fullName")}
            aria-invalid={invalid("fullName")}
            aria-describedby={describedBy("fullName")}
            className={cn(fieldClass, borderFor("fullName"))}
          />
        </Field>

        <Field id={id("workEmail")} label="Work email" required error={state.errors.workEmail}>
          <input
            id={id("workEmail")}
            name="workEmail"
            type="email"
            inputMode="email"
            autoComplete="email"
            defaultValue={value("workEmail")}
            aria-invalid={invalid("workEmail")}
            aria-describedby={describedBy("workEmail")}
            className={cn(fieldClass, borderFor("workEmail"))}
          />
        </Field>

        <Field id={id("company")} label="Company" required error={state.errors.company}>
          <input
            id={id("company")}
            name="company"
            type="text"
            autoComplete="organization"
            defaultValue={value("company")}
            aria-invalid={invalid("company")}
            aria-describedby={describedBy("company")}
            className={cn(fieldClass, borderFor("company"))}
          />
        </Field>

        <Field id={id("jobTitle")} label="Job title" required error={state.errors.jobTitle}>
          <input
            id={id("jobTitle")}
            name="jobTitle"
            type="text"
            autoComplete="organization-title"
            defaultValue={value("jobTitle")}
            aria-invalid={invalid("jobTitle")}
            aria-describedby={describedBy("jobTitle")}
            className={cn(fieldClass, borderFor("jobTitle"))}
          />
        </Field>

        <Field id={id("country")} label="Country" required error={state.errors.country}>
          <input
            id={id("country")}
            name="country"
            type="text"
            autoComplete="country-name"
            defaultValue={value("country")}
            aria-invalid={invalid("country")}
            aria-describedby={describedBy("country")}
            className={cn(fieldClass, borderFor("country"))}
          />
        </Field>

        <Field id={id("phone")} label="Phone number" error={state.errors.phone}>
          <input
            id={id("phone")}
            name="phone"
            type="tel"
            inputMode="tel"
            autoComplete="tel"
            defaultValue={value("phone")}
            aria-invalid={invalid("phone")}
            aria-describedby={describedBy("phone")}
            className={cn(fieldClass, borderFor("phone"))}
          />
        </Field>
      </div>

      <Field id={id("service")} label="Service required" required error={state.errors.service}>
        <select
          id={id("service")}
          name="service"
          defaultValue={value("service")}
          aria-invalid={invalid("service")}
          aria-describedby={describedBy("service")}
          className={cn(fieldClass, borderFor("service"), "appearance-none pr-10")}
        >
          <option value="">Select an option</option>
          {SERVICE_OPTIONS.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </Field>

      <Field
        id={id("description")}
        label="Project description"
        required
        error={state.errors.description}
        hint="What are you trying to achieve, and what's currently in the way?"
      >
        <textarea
          id={id("description")}
          name="description"
          rows={6}
          defaultValue={value("description")}
          aria-invalid={invalid("description")}
          aria-describedby={describedBy("description", true)}
          className={cn(fieldClass, borderFor("description"), "h-auto resize-y py-3.5 leading-relaxed")}
        />
      </Field>

      <div className="grid gap-6 sm:grid-cols-3">
        <Field id={id("timeline")} label="Expected timeline" error={state.errors.timeline}>
          <select
            id={id("timeline")}
            name="timeline"
            defaultValue={value("timeline")}
            aria-invalid={invalid("timeline")}
            aria-describedby={describedBy("timeline")}
            className={cn(fieldClass, borderFor("timeline"), "appearance-none pr-10")}
          >
            <option value="">Select an option</option>
            {TIMELINE_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </Field>

        <Field id={id("budget")} label="Budget range" error={state.errors.budget}>
          <select
            id={id("budget")}
            name="budget"
            defaultValue={value("budget")}
            aria-invalid={invalid("budget")}
            aria-describedby={describedBy("budget")}
            className={cn(fieldClass, borderFor("budget"), "appearance-none pr-10")}
          >
            <option value="">Select an option</option>
            {BUDGET_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </Field>

        <Field id={id("engagement")} label="Preferred engagement" error={state.errors.engagement}>
          <select
            id={id("engagement")}
            name="engagement"
            defaultValue={value("engagement")}
            aria-invalid={invalid("engagement")}
            aria-describedby={describedBy("engagement")}
            className={cn(fieldClass, borderFor("engagement"), "appearance-none pr-10")}
          >
            <option value="">Select an option</option>
            {ENGAGEMENT_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </Field>
      </div>

      {/* Honeypot — hidden from users and assistive technology, attractive to bots. */}
      <div aria-hidden="true" className="absolute left-[-9999px] h-px w-px overflow-hidden">
        <label htmlFor={id("company_website")}>Company website</label>
        <input id={id("company_website")} name="company_website" type="text" tabIndex={-1} autoComplete="off" />
      </div>

      <div className="flex flex-col gap-4 border-t border-navy-950/8 pt-6 sm:flex-row sm:items-center sm:justify-between">
        <p className="text-[0.8125rem] leading-relaxed text-mist-500">
          Fields marked <span className="text-accent-600">*</span> are required. We use your details
          only to respond to this enquiry.
        </p>
        <SubmitButton />
      </div>
    </form>
  );
}

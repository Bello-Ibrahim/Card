import { buildMetadata } from "@/lib/seo";
import { LegalPage, type LegalSection } from "@/components/legal-page";

export const metadata = buildMetadata({
  title: "Privacy Policy",
  description:
    "How DataForge Consulting collects, uses, stores and protects personal information submitted through this website.",
  path: "/privacy-policy",
});

const sections: LegalSection[] = [
  {
    heading: "Scope of this policy",
    paragraphs: [
      "This policy explains how DataForge Consulting handles personal information collected through this website. It covers the information you choose to give us and the limited technical information our hosting infrastructure processes in order to serve the site.",
      "It does not cover personal data processed under a separate client agreement. Where we act as a processor on a client's behalf during a consulting engagement, the terms of that agreement govern instead.",
    ],
  },
  {
    heading: "Information we collect",
    paragraphs: [
      "We collect only what you submit and what is technically necessary to deliver the site.",
    ],
    bullets: [
      "Enquiry details you submit through the contact form: name, work email, company, job title, country, optional phone number, the nature of your enquiry, indicative scope, preferred engagement type and your message.",
      "Standard server request data processed by our hosting provider, such as IP address, user agent and request time, retained for security and operational purposes.",
    ],
  },
  {
    heading: "How we use it",
    paragraphs: [
      "Enquiry details are used to respond to you, to route your enquiry to the right people, and to maintain a record of our correspondence. If you ask to receive our insights by email, we use your address for that purpose until you ask us to stop.",
    ],
    bullets: [
      "Responding to and following up on your enquiry",
      "Preparing proposals or scoping conversations you have requested",
      "Sending you material you have specifically asked to receive",
      "Protecting the site against abuse, and meeting our legal obligations",
    ],
  },
  {
    heading: "What we do not do",
    paragraphs: [
      "We do not sell personal information. We do not share your enquiry with third parties for their own marketing. We do not build advertising profiles from your use of this site, and this site does not run advertising or cross-site tracking technology.",
    ],
  },
  {
    heading: "Legal bases for processing",
    paragraphs: [
      "Where data protection law requires a legal basis, we rely on our legitimate interest in responding to business enquiries and operating our website securely; on steps taken at your request prior to entering a contract; on your consent where you have asked to receive material from us; and on legal obligation where applicable.",
    ],
  },
  {
    heading: "Service providers",
    paragraphs: [
      "We use third-party providers to host this website and to receive and store enquiries submitted through it. These providers process data on our instructions and under contractual confidentiality and security obligations. Depending on the provider, data may be processed in a country other than your own; where that occurs, we rely on recognised transfer safeguards.",
    ],
  },
  {
    heading: "Retention",
    paragraphs: [
      "We keep enquiry correspondence for as long as it is useful to the relationship it relates to, and then delete it. Where an enquiry does not lead to an engagement, we retain it only for a reasonable period so that we can recognise later correspondence in context.",
    ],
  },
  {
    heading: "Your rights",
    paragraphs: [
      "Subject to the law that applies to you, you may request access to the personal information we hold about you, ask us to correct or delete it, object to or restrict certain processing, request a portable copy, and withdraw consent where processing is based on it. Withdrawing consent does not affect processing already carried out.",
      "We will respond to requests within the period required by applicable law. You also have the right to complain to your local data protection authority.",
    ],
  },
  {
    heading: "Security",
    paragraphs: [
      "This site is served over HTTPS and submissions are transmitted over encrypted connections. Access to enquiries is limited to the people who need it in order to respond. No system is completely secure, and we encourage you not to include confidential technical details or sensitive personal data in an initial enquiry.",
    ],
  },
  {
    heading: "Changes to this policy",
    paragraphs: [
      "We will update this page when our practices change — for example, if we add analytics or marketing tooling to the site. The date at the top of this page reflects the most recent revision.",
    ],
  },
];

export default function PrivacyPolicyPage() {
  return (
    <LegalPage
      title="Privacy Policy"
      lede="What we collect through this website, why we collect it, and what we do with it."
      updated="4 September 2026"
      path="/privacy-policy"
      sections={sections}
    />
  );
}

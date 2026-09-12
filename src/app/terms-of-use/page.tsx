import { buildMetadata } from "@/lib/seo";
import { LegalPage, type LegalSection } from "@/components/legal-page";

export const metadata = buildMetadata({
  title: "Terms of Use",
  description: "The terms that apply to your use of the DataForge Consulting website.",
  path: "/terms-of-use",
});

const sections: LegalSection[] = [
  {
    heading: "Acceptance",
    paragraphs: [
      "By accessing this website you agree to these terms. If you do not accept them, please do not use the site.",
    ],
  },
  {
    heading: "Purpose of this site",
    paragraphs: [
      "This website describes the services offered by DataForge Consulting and publishes editorial material about data engineering practice. It is provided for general information.",
      "Nothing on this site constitutes professional, technical, financial or legal advice for your specific circumstances, and no client relationship is created by reading it or by submitting an enquiry. Advice is given only under a written engagement agreement.",
    ],
  },
  {
    heading: "Accuracy of content",
    paragraphs: [
      "We take care to keep the site accurate and current, particularly our technical writing. Technology changes quickly, and we make no warranty that all content remains correct or complete at the time you read it.",
      "Where this site describes engagement patterns without naming a client, those descriptions are illustrative and are labelled as such. They are not representations about a particular project or a promise of a particular outcome.",
    ],
  },
  {
    heading: "Intellectual property",
    paragraphs: [
      "The content, design, code and materials on this site are owned by DataForge Consulting or used with permission, and are protected by intellectual property law.",
      "You may read, share links to, and quote short extracts of our published articles with clear attribution and a link to the original. You may not republish substantial portions, or use our material to train commercial models or to create derivative works, without our written permission.",
    ],
  },
  {
    heading: "Third-party names and trademarks",
    paragraphs: [
      "Technology and product names on this site are the trademarks of their respective owners and are used only to describe the tools our engineers work with. Their appearance does not indicate any partnership, sponsorship, certification or endorsement in either direction.",
    ],
  },
  {
    heading: "Acceptable use",
    paragraphs: ["When using this site, you agree not to:"],
    bullets: [
      "Attempt to gain unauthorised access to the site, its infrastructure or any connected system",
      "Interfere with the availability or integrity of the site",
      "Submit unlawful, misleading, or deliberately harmful content through the contact form",
      "Use automated means to harvest content or submit enquiries",
    ],
  },
  {
    heading: "External links",
    paragraphs: [
      "This site may link to third-party websites. We do not control them and are not responsible for their content, availability or privacy practices. A link is not an endorsement.",
    ],
  },
  {
    heading: "Limitation of liability",
    paragraphs: [
      "To the fullest extent permitted by law, DataForge Consulting is not liable for any loss or damage arising from reliance on the content of this site or from its use or unavailability. Nothing in these terms limits liability that cannot lawfully be limited.",
    ],
  },
  {
    heading: "Changes",
    paragraphs: [
      "We may update these terms from time to time. The current version is always the one published on this page, and the date above reflects the most recent revision.",
    ],
  },
];

export default function TermsOfUsePage() {
  return (
    <LegalPage
      title="Terms of Use"
      lede="The terms that apply when you use this website."
      updated="4 September 2026"
      path="/terms-of-use"
      sections={sections}
    />
  );
}

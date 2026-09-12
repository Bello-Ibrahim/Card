import { buildMetadata } from "@/lib/seo";
import { LegalPage, type LegalSection } from "@/components/legal-page";

export const metadata = buildMetadata({
  title: "Cookie Policy",
  description:
    "How this website uses cookies and similar technologies. DataForge Consulting does not run advertising or cross-site tracking on this site.",
  path: "/cookie-policy",
});

const sections: LegalSection[] = [
  {
    heading: "What cookies are",
    paragraphs: [
      "Cookies are small text files a website can store in your browser. They are commonly used to keep you signed in, remember preferences, measure usage, or track people across different websites for advertising.",
    ],
  },
  {
    heading: "What this site currently uses",
    paragraphs: [
      "This website is built to work without setting cookies for advertising or cross-site tracking. As published, it does not set analytics cookies, does not run advertising technology, and does not embed third-party trackers or social media pixels.",
      "Your browser may still store data that this site relies on for basic functionality, and our hosting provider processes ordinary server request logs for security and operational purposes. Those logs are described in our Privacy Policy.",
    ],
  },
  {
    heading: "If that changes",
    paragraphs: [
      "If we later add analytics or marketing technology, we will update this page before or at the time it goes live, describe exactly what is set and why, and — where the law requires consent — ask for it before any non-essential cookie is placed.",
    ],
  },
  {
    heading: "Managing cookies in your browser",
    paragraphs: [
      "You can view, block and delete cookies through your browser settings. Blocking cookies entirely may affect how other websites function, though it will not prevent this site from working.",
    ],
  },
  {
    heading: "Related policies",
    paragraphs: [
      "Our Privacy Policy explains what personal information we collect through this website, why we collect it and what rights you have over it. Our Terms of Use set out the terms that apply to your use of the site.",
    ],
  },
];

export default function CookiePolicyPage() {
  return (
    <LegalPage
      title="Cookie Policy"
      lede="What this site stores in your browser — and what it deliberately does not."
      updated="4 September 2026"
      path="/cookie-policy"
      sections={sections}
    />
  );
}

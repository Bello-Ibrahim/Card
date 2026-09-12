export type Faq = { question: string; answer: string };

export const faqs: Faq[] = [
  {
    question: "What does DataForge Consulting do?",
    answer:
      "DataForge is a data engineering consulting and technology advisory firm. We help organizations design, build, modernize, operate and scale reliable data platforms — covering data strategy and architecture, data pipelines, cloud data engineering, warehousing and lakehouses, integration, migration, analytics engineering, data quality and governance, plus training and data engineering team setup.",
  },
  {
    question: "What size of organization do you work with?",
    answer:
      "We work with startups, growing companies, enterprises, government organizations, financial institutions, healthcare organizations, telecoms, technology companies and other data-intensive businesses. The engagement model changes with scale — a first platform build looks very different from a multi-domain enterprise migration — but the engineering discipline does not.",
  },
  {
    question: "Can you work alongside our existing data team?",
    answer:
      "Yes. Many engagements are collaborative by design: we work inside your repositories, standards and ceremonies, and pair with your engineers so capability stays with your team. We can also provide fractional technical leadership or a dedicated squad where capacity or senior coverage is the constraint.",
  },
  {
    question: "Do you provide training for our existing engineers?",
    answer:
      "Yes. We run structured programs across data engineering fundamentals, the modern data stack, advanced data engineering and cloud data engineering, as well as fully customized corporate training designed around your stack, objectives and current skill levels. Training is usually most effective when paired with mentoring on real delivery work.",
  },
  {
    question: "Can you help us build a data engineering team from scratch?",
    answer:
      "Yes. We help define roles and levelling, design the team structure and operating model, build a hiring plan, establish engineering standards and onboarding, and get the first engineers productive. We can also augment the team while it is being formed.",
  },
  {
    question: "Which cloud and data platforms do you work with?",
    answer:
      "We work across AWS, Microsoft Azure and Google Cloud, with data platforms including Snowflake, Databricks, BigQuery, Amazon Redshift and Microsoft Fabric, and engineering tooling such as Python, SQL, Apache Spark, Apache Kafka, dbt and Apache Airflow. Selection is driven by your constraints, not by a preferred vendor.",
  },
  {
    question: "How do engagements usually start?",
    answer:
      "Most start with a short discovery conversation about the outcome you need, the systems you have and the constraints you are working within. From there we typically propose either a focused assessment or architecture review, or a scoped delivery engagement with a defined first milestone.",
  },
];

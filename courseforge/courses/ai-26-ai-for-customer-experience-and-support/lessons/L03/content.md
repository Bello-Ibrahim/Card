# L03 Writing a Knowledge Base That AI Can Use

Course: AI-26 · Module: M1 · Objectives: O3 · Video: 5 min

## Hook
In L02 you saw that an AI assistant is only as good as the content it can find. Most support teams have plenty of content, but it lives in long emails, old documents and the heads of experienced colleagues. This lesson shows how to turn that content into short, clear articles that both customers and AI can use.

## Explanation
A knowledge base article that works well for AI has the same features as one that works well for a busy customer. Five features matter most.

**1. One topic per article.** An article called "Delivery information" that covers prices, times, tracking, damaged parcels and returns is hard to search. Split it into separate articles: "How to track your order", "What to do if your parcel is damaged", and so on. When the assistant searches for "damaged parcel", it finds one focused article, not a long page where the answer is in paragraph nine.

**2. A clear title in the customer's words.** Write the title as the customer would ask the question: "How do I change my delivery address?" is better than "Address modification procedure". Customers and AI search tools both match words, so familiar words help.

**3. Short steps and plain language.** Use numbered steps for actions, short sentences and one idea per sentence. Explain any special term the first time you use it. Avoid words like "usually" or "in most cases" unless you also say what happens in the other cases, because AI may repeat a vague rule as if it were a firm promise.

**4. A review date.** Add "Last reviewed: [date]" to each article. Policies change. An old article is one of the main reasons why assistants give wrong answers.

**5. An owner.** Name the team or role responsible for the article, such as "Owner: Logistics team". When something changes, everybody knows who must update it.

AI can help you write these articles. You can paste an internal note into Claude or ChatGPT and ask it to produce a clean article with a set structure. But AI can also add details that were not in the note, drop an important exception or make a rule sound more certain than it is. So there is one firm rule: **a person checks every fact in the draft against the source before it is published.**

Before you paste anything, remove personal data, such as customer names, phone numbers and order numbers, and anything your company treats as confidential. Check your company's policy on which AI tools you may use.

**Analogy:** A knowledge base is like a well-organised pharmacy shelf. Each medicine has its own box, a clear label, and an expiry date. A pharmacist, or a customer, can find the right box quickly. If all the medicines were mixed in one big bag with no labels and no dates, even an expert would make mistakes.

## Worked Example
Chukwuemeka is a support team lead at a hypothetical online electronics shop in Lagos, Nigeria. The logistics manager sends a long internal email about delivery delays. It mixes several topics: heavy rain has slowed deliveries to some states, a courier partner has changed, customers in affected areas should expect up to 5 extra working days, tracking links from the old courier no longer work, and agents may offer free re-delivery if a parcel is returned by mistake.

Chukwuemeka removes staff names and internal phone numbers from the email. Then he asks an AI assistant: "Turn this note into two customer-facing help articles. Article 1: delivery delays in affected areas. Article 2: how to track your order after the courier change. Use a question as the title, short numbered steps, plain language, and add 'Last reviewed' and 'Owner' lines. Use only facts in the note."

The drafts look good. But when he checks them against the email, he finds two problems. The first draft says "all deliveries" are delayed, but the email says "some states". The second draft invents a new tracking website address. He corrects both, adds the list of affected states from the logistics team, and publishes the articles with "Owner: Logistics team".

The free re-delivery rule is for agents, not customers, so he keeps it in an internal article.

## Common Mistake
Many teams paste their whole knowledge base into an AI tool and assume it is now "ready for AI". If the articles are long, mixed and out of date, the assistant will give long, mixed and out-of-date answers. Cleaning the content is not an extra task before the AI project. It is the most important part of the AI project.

## Key Takeaways
1. Good articles have one topic, a clear title in the customer's words, short steps, a review date and an owner.
2. AI can turn messy notes into clean drafts quickly, but it may add, remove or change facts.
3. A person must check every fact in an AI draft against the source, and personal or confidential data must be removed before pasting.

## Hands-on Exercise
**Task:** Use an AI assistant to turn a messy internal note into 2 clean knowledge base articles. Check every fact against the original note.
**Tools:** Claude or ChatGPT (free plan) [VERSION]; a document or notes app.
**Steps:**
1. Use this made-up internal note, or write a similar one about a made-up company: "Hi team, from Monday the Kestrel Bikes shop in Lisbon moves to new opening hours, 10:00 to 19:00 Mon-Sat, closed Sunday. Repairs now take 3-5 working days, not 2. Customers can book repairs online now, no phone bookings any more. Express repair still exists, 24h, extra fee 15 euros, only for tyres and brakes. Tell customers politely."
2. Ask the AI assistant to create 2 articles: one about opening hours and repair bookings, and one about express repairs. Ask for a question as the title, short steps, a "Last reviewed" line and an "Owner" line, and tell it to use only facts from the note.
3. Print or copy the two drafts. Go through the note line by line and tick each fact in the drafts.
4. Circle anything in the drafts that is not in the note, or that is changed or missing.
5. Correct the drafts yourself and write a short list of what you changed.
**What good looks like:** Two short articles, each on one topic, with clear question titles, numbered steps, a review date and an owner. Every fact matches the note (including the 15-euro fee and the "tyres and brakes only" rule), and you have a list of any errors the AI made and how you fixed them.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT: check current plans and how chat content is used before recording.
- Judgement call (from curriculum): the exercise uses a made-up company; learners are told to remove personal and confidential data before pasting.

# L05 Privacy: What Happens to the Data You Share

Course: AI-29 · Module: M1 · Objectives: O3, O4 · Video: 5 min

## Hook
You would not read a patient's medical notes aloud in a busy café. But when you paste the same notes into a chatbot, where do they go, who can see them, and how long do they stay there?

## Explanation
When you type into an AI tool, your text is sent to the company that runs it. Depending on the tool, the plan and your settings, that text may be:
- **stored** in your chat history, sometimes for a long time;
- **reviewed** by people at the company, for example to check safety or quality;
- **used to improve the service**, which can include training future models.

Settings differ between tools and between free, paid and business plans, and they change often. [VERSION] Many tools let you turn off chat history or opt out of training, but you have to look for these settings. Check the tool's settings and your organisation's rules before you share anything sensitive.

Two kinds of data need special care:

**Personal data** is any information about an identifiable person: a name, phone number, email address, ID number, photo, home address, health details, bank details and so on.

**Confidential data** is information your organisation or client has not made public: contracts, prices, plans, source code, internal reports and passwords.

**Removing names is often not enough.** A person can still be identified from a combination of details. "A 47-year-old female teacher at the only secondary school in a small town, admitted on 3 March with a broken wrist" contains no name, but many people in that town would know who it is. This is why good practice removes or changes every detail that is not needed for the task.

A safe habit is to ask: **"Does the AI need this detail to do the task?"** Often it does not. You can:
- replace real details with placeholders, such as [PATIENT], [DATE] or [CLIENT];
- describe a general situation instead of a real case;
- use tools your organisation has approved for sensitive data.

(Legal duties about personal data vary by country and are covered in course AI-30.)

**Analogy:** Typing into an AI tool is like sending a letter through a large postal company. Most letters arrive safely. But depending on the service you chose, the letter may be opened for checks, copied or kept in an archive. You would not put your bank PIN in a normal letter. Apply the same care to what you type.

## Worked Example
Maricel Santos is a nurse at a hypothetical hospital in the Philippines. At the end of a long shift, she wants a quick summary of a patient's notes for the next shift.

**The risky way:** she pastes the full notes, including the patient's name, age, address, diagnosis and medicines, into a free public chatbot and asks for a summary. The summary is useful, but she has now shared a patient's health data with an outside service. Her hospital has not approved the tool.

**A better way:** Maricel realises that the chatbot does not need the patient's details at all. What she really needs is a clear handover structure. She writes:

"I am a nurse writing an end-of-shift handover. Give me a short template with headings for a general adult patient on a medical ward, with space for condition, medicines, observations, concerns and actions for the next shift."

The chatbot gives her a template. She fills it in herself, on the hospital's own system. The patient data never leaves the hospital.

## Common Mistake
Many people think that deleting a chat, or removing the person's name, makes a prompt safe. Deleting a chat in your view may not delete every copy at the company straight away, depending on the tool's policy. [VERIFY] And, as you saw, a person can be identified from other details. The correction: decide what to share *before* you type. Remove every personal or confidential detail that the task does not need, and use approved tools for sensitive work.

## Key Takeaways
1. What you type into an AI tool may be stored, reviewed or used to improve the service, depending on the tool, the plan and your settings.
2. Personal and confidential data need special care, and removing names alone is often not enough to protect a person.
3. Before you type, ask whether the AI needs each detail. Use placeholders, general descriptions or approved tools instead.

## Hands-on Exercise
**Task:** Find the data-use and chat-history settings in Claude or ChatGPT, write down what each one does, and rewrite one work prompt so that it contains no personal or confidential data.
**Tools:** Claude or ChatGPT (free versions) [VERSION]; a notes app or paper.
**Steps:**
1. Open the tool you use and go to its settings. Look for sections about privacy, data controls or chat history. Names and locations of these settings change often. [VERSION]
2. Write down each setting you find about chat history, training or data use, and in one sentence explain what it does. If the explanation in the tool is unclear, note that too.
3. Choose one real prompt you have used, or might use, at work. Do not paste it into the AI tool for this step.
4. Rewrite it on paper or in your notes: remove or replace every personal or confidential detail with a placeholder or a general description.
5. Check your rewrite: could anyone identify a person, client or project from it? If yes, remove more.
**What good looks like:** A short list of the settings you found, each with a clear one-line explanation, and a before-and-after prompt where the "after" version still gets the task done but contains no names, numbers, dates or other details that could identify a person or reveal confidential information.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Data-use, chat-history and training settings in Claude and ChatGPT differ between free and paid plans and change often. Check the live tools, including setting names and where they are found, before scripting.
- [VERIFY] Whether deleting a chat removes all copies at the company straight away, and how long data is kept, must be checked against each tool's current privacy policy before scripting.

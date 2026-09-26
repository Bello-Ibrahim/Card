# HeyGen Batch Pack: AI-23 M1 (AI in the Design Process: Research and Strategy)

Course: AI for Brand and Product Design. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L01 Where AI Fits in Brand and Product Design

- **Filename:** `ai-23-ai-for-brand-and-product-design_M1_L01_presenter.mp4`
- **Expected length:** about 5.3 minutes (739 words). The quality gate accepts ±10%.

```text
An AI tool can give you forty logo ideas in a minute. It can also give you forty ideas that look like marks you have seen before, in colours that fail a contrast check. The skill is knowing where AI helps, and where it hurts.

Hi, and welcome to AI for Brand and Product Design. In this first lesson, we draw a map. Where does AI fit in your design process, and where should it stay out?

You already know the design process. Most brand and product projects move through similar stages. Research, definition, ideation, design and systems, prototyping and testing, and finally delivery. AI can take part in every stage, but it does not add the same value at each one.

AI adds the most value where the work needs volume, speed or variation. Volume means summarising thirty interview transcripts, or drafting fifty name options. Speed means turning a rough idea into a first layout or a moodboard in minutes instead of hours. Variation means showing you directions you would not have tried.

AI adds the most risk where the work needs originality, accuracy or rights. Image generators learn from huge sets of existing images, so their output can drift towards clichés, or look close to existing marks. Language models can invent quotes, or suggest a colour pair that looks accessible but is not. And AI cannot tell you whether a name is free to use.

There is also judgement. Choosing which insight matters and which direction fits the client is your job. AI can argue for options, but it does not carry responsibility for the result. You do.

Here is a helpful way to picture it. Think of AI as a fast junior assistant on your team. The assistant works quickly, never gets tired and produces many options. But it has no memory of your client meetings, sometimes invents details with confidence, and does not know the law.

You would never send a junior's first draft to a client without a senior review. So treat every AI output in the same way.

Now, mark each stage with one of three labels. The first is AI drafts, I decide. AI produces options, and you select and refine. The second is AI checks, I own. You do the work, and AI reviews it for gaps. The third is no AI, for confidential data, final legal decisions and relationships with people.

Let's see this in practice. Mateo Rojas is a freelance product designer in Santiago, Chile. His client, a small chain of bakeries, wants a new brand and a simple ordering app. So Mateo maps his usual process, and marks each stage.

He does the customer interviews himself, with no AI, because relationships and consent matter. For research synthesis, AI drafts and he decides. Claude groups his anonymised notes into themes, and he checks every quote. For the brief, AI checks and he owns. Claude asks critical questions about his draft.

Names and moodboards get AI drafts. The final logo gets no AI. He redraws the chosen concept by hand in Figma. For the UI screens, Figma's AI features give a first layout, and he rebuilds it with his own components. And trademark checks get no AI at all. They need official searches, and possibly a lawyer.

Mateo notices something. His plan uses AI in more than half of the stages. But the decisions stay with him at every stage. He writes the plan into his project notes, so he can explain his process to the client later.

A common mistake is to treat AI as a yes or no choice for the whole project. Decide stage by stage instead. And do not measure AI only by speed. A fast draft that needs three rounds of fixing is not faster.

Let's recap. First, AI adds value where design work needs volume, speed or variation. Second, AI adds risk where the work needs originality, accuracy or rights, so those outputs always need human checks. Third, plan AI use stage by stage, with clear roles. AI drafts, I decide. AI checks, I own. Or no AI.

Now it is your turn. In the exercise below this video, you will map your own design process. Mark three steps where AI could help, and one step where you would not use it, with your reasons. It takes about twenty minutes. In the next lesson, we look at research synthesis with Claude. See you there.
```

## L02 Research Synthesis with Claude

- **Filename:** `ai-23-ai-for-brand-and-product-design_M1_L02_presenter.mp4`
- **Expected length:** about 5.1 minutes (714 words). The quality gate accepts ±10%.

```text
You have twelve interview notes, a deadline tomorrow and a wall of sticky notes that is still empty. Claude can suggest themes in under a minute. But can you trust a theme if you have not checked where it came from?

In the last lesson, we mapped where AI fits. Now we start at the beginning, with research. This lesson is about research synthesis with Claude.

Research synthesis means turning raw material, such as interview notes, app store reviews or open survey answers, into a few clear patterns. It is slow work. And it suits a language model like Claude, because the task is about reading a lot of text and grouping similar ideas.

A reliable synthesis prompt has four parts. Context: who the research is about, and what decision it supports. Material: the anonymised notes, with an ID for each participant, like P zero one. Task: find up to five themes, each with a name, a description, the supporting participant IDs and two exact quotes. And finally, rules.

The rules say: only use quotes that appear word for word in the notes. Mark any theme with fewer than three participants. And do not add information that is not in the notes. IDs and exact quotes make the output checkable, and they make weak themes easy to see.

Why does checking matter? Language models produce text that sounds right. They can merge two complaints into one theme, turn some people into most users, or slightly reword a quote. Sometimes they invent a quote that nobody said. It is not deliberate, but the result is a false insight in your deck.

So protect the data first. Before you paste anything, remove names, phone numbers, email addresses, exact locations and employer names. Replace them with IDs or general terms. And only use research data with participant consent and client approval. Lesson five covers this in more detail.

Here is a way to think about it. Claude is like a colleague who read all the notes very quickly, and now tells you what they remember. That is useful. But you would still ask, who said that? Show me the page. Asking for IDs and quotes is how you ask Claude to show you the page.

Let's try it. Wanjiru Kamau is a UX researcher at a start-up building a group savings app for users in Kenya and Ghana. She has twelve anonymised interview notes, labelled P zero one to P twelve.

She writes a prompt in Claude with the context, the task and the rules, and then pastes the notes. Claude returns five themes. For example, trust in the group treasurer, supported by five participants, and fear of hidden fees, supported by three.

Now Wanjiru checks each quote with a text search in her original notes. Four themes are correct. But in fear of hidden fees, one quote has changed. The note says, I think there might be charges. Claude wrote, I know there are hidden charges. The meaning is stronger than the original.

She also finds that participant six talked about bank fees, not app fees. So she corrects the quote, removes that participant and relabels the theme as weak, with two participants. In her report, it becomes a question for the next round of research, not a finding.

The most common mistake is to copy Claude's themes straight into a deck because they sound right. A theme is only a finding when you can point to the evidence. Another mistake is pasting raw notes with real names, because it is only a summary. The task does not change the data you shared.

Let's recap. First, ask Claude for themes with participant IDs and exact quotes, so every claim can be checked. Second, verify every quote and every participant before you use a theme, because models can reword, merge or invent evidence. Third, anonymise research data, and only use it in AI tools with consent and client approval.

Now it is your turn. In the exercise below this video, you will give Claude a set of sample interview notes, ask for five themes with quotes, and check every quote against the original text. It takes about thirty minutes. In the next lesson, we go from insights to personas and jobs to be done. See you there.
```

## L03 From Insights to Personas and Jobs to Be Done

- **Filename:** `ai-23-ai-for-brand-and-product-design_M1_L03_presenter.mp4`
- **Expected length:** about 5.0 minutes (703 words). The quality gate accepts ±10%.

```text
Ask an AI tool for a persona, and you get one in seconds. A name, an age, a job, a favourite coffee order and three frustrations. It sounds real. But where did any of it come from?

Last time, we turned interview notes into verified themes. Now we make those themes useful for a team, with jobs to be done statements and personas.

A job to be done statement describes what a person is trying to achieve in a situation, without describing a solution. A common structure is: when this situation happens, I want to do this, so I can reach this outcome. It keeps the team focused on needs, not features.

For example: when my child has a fever at night, I want to see which clinic has an open slot tomorrow morning, so I can plan my day before I go to sleep.

A persona is a short profile that represents a group of real users. A lightweight persona needs only a few parts: a name and role, a goal, key behaviours, pain points, and the evidence behind each point. A favourite film is not useful, unless research shows it matters.

Claude is good at drafting these, because it phrases ideas clearly and quickly. The risk is synthetic users. These are personas or user quotes that the model invents to fill gaps. They sound realistic, but they are not based on data. Design for a synthetic user, and you design for someone who may not exist.

The protection is simple. Label every claim. Each line is either from research, supported by named themes or participant IDs, or it is an assumption. An assumption may be reasonable, but it becomes a question for the next round of research.

Think of a persona as a composite sketch made from witness statements. A good sketch artist draws only what the witnesses described. If the artist adds a scar that nobody mentioned, the sketch looks more complete, but now it is misleading. Labels show which parts came from the witnesses.

Let's see it in action. Dewi Santoso is a product designer at a health-tech company in Surabaya, Indonesia. Her team is designing a clinic booking app for patients. She has four verified themes from interviews with ten patients.

One. Patients book for family members more often than for themselves. Two. Uncertain waiting times cause stress. Three. Many prefer to confirm bookings through a messaging app. Four. Some older patients ask younger relatives to book for them.

She asks Claude to use only these themes, write three job statements and one lightweight persona, and cite the theme after every claim, or write assumption.

Claude's persona is Rina, thirty-four. She books appointments for her two children and her mother. She gets anxious when she cannot see how long she will wait. She prefers confirmations by messaging app. Each of these cites a theme. Then one line says she is a teacher who books during lunch breaks. That one is marked as an assumption.

Dewi reviews the output. She removes the job title, and keeps books during short breaks as a question for research. One job statement mentions paying online, which is not in any theme, so it moves to the research backlog. The final persona is shorter, but every line can be defended.

A common mistake is to accept a long, detailed AI persona because it feels more real. More detail does not mean more truth. And AI interviews with imaginary users can help you prepare questions, but they are not evidence about real people.

Let's recap. First, job statements describe a situation, a motivation and an outcome, and lightweight personas summarise goals, behaviours and pain points with evidence. Second, synthetic users invented by AI sound real, but they are not data, so they must never replace research. Third, label every claim as from research or assumption, and turn assumptions into research questions.

Now it is your turn. In the exercise below this video, you will write three job statements and one persona with Claude, then mark each claim as from research or assumption. It takes about twenty-five minutes. In the next lesson, we write a design brief with AI as a sparring partner. See you there.
```

## L04 Writing a Design Brief with AI as a Sparring Partner

- **Filename:** `ai-23-ai-for-brand-and-product-design_M1_L04_presenter.mp4`
- **Expected length:** about 5.0 minutes (698 words). The quality gate accepts ±10%.

```text
Most projects that go wrong in week six were already going wrong in week one, in the brief. What if you could find the gaps in your brief before your client does?

In the last lesson, we turned research into personas and job statements. Now we use them in a design brief, with AI as a sparring partner.

A design brief is the agreement that guides every later decision. A good one-page brief covers six things. Background. Problem and goals. Audience, based on research. Scope and deliverables. Constraints, like budget, timeline, languages and markets. And success measures, meaning how you and the client will judge the result.

You can use Claude in two ways here. The first is to ask it to write the brief. That is fast, but the result is generic, because Claude does not know the client, the politics or the budget. The second, more useful way is to ask it to question your draft.

In this role, Claude looks for four things. Missing constraints, such as which markets and languages the brand must work in. Unclear success measures, such as what more modern really means. Conflicting goals, like a premium look with the lowest packaging cost. And hidden assumptions, where you have no evidence.

A useful prompt sets the role and the limits. It asks Claude to act as a senior creative director, and to ask the five most important critical questions. It also says: do not rewrite the brief, and do not suggest design solutions.

That last rule matters. You want questions, not answers. The designer keeps the decisions. You answer each question yourself, with the client when needed. And remember to remove confidential numbers, or replace them with ranges, like a small budget.

Think of Claude as a training partner in boxing. The partner does not fight your match for you. They test your defence, so you find the weak points before the real fight. And you decide what to change.

Let's watch this work. Yasmine Trabelsi is a brand designer in Tunis, Tunisia. A family-owned olive oil company wants a rebrand. Her draft brief says: modernise the brand for younger buyers and export markets, keep the family heritage, and launch new labels in six months.

She removes the owner's name and the revenue figures, pastes the brief into Claude, and asks for five critical questions. Claude asks which export markets, and whether labels must work in Arabic, French and English. It asks what younger buyers means, and how success will be measured after six months.

Then comes the sharpest question. Modernise and keep heritage can conflict. Which heritage elements are fixed, and which can change? The fifth question asks about legal label rules in the export markets.

Yasmine answers each one herself. After a call with the client, she adds two European countries and the Gulf region as target markets, and trilingual labels. The family name and the olive tree must stay. And success means new distributor listings.

For the legal question, she does not ask Claude for an answer. Label rules differ by country, so the client's export agent will confirm them. Expert questions go to expert sources. Her brief is now clearer, and every decision belongs to her and the client.

A common mistake is to ask Claude to improve the brief, and accept a longer, more polished text. Polished is not the same as correct. The new text can add goals the client never agreed to. So ask for questions, not rewrites, and choose the questions that change decisions.

Let's recap. First, a strong brief covers background, goals, audience, scope, constraints and success measures, on one page. Second, use Claude to question your draft, looking for missing constraints, unclear measures and conflicting goals, not to write it for you. Third, you and the client make every decision, and expert questions go to expert sources.

Now it is your turn. In the exercise below this video, you will draft a one-page brief for your capstone brand, ask Claude for five critical questions, and revise the brief to answer them. It takes about thirty minutes. In the next lesson, we look at protecting client data and confidentiality. See you there.
```

## L05 Protecting Client Data and Confidentiality

- **Filename:** `ai-23-ai-for-brand-and-product-design_M1_L05_presenter.mp4`
- **Expected length:** about 5.2 minutes (720 words). The quality gate accepts ±10%.

```text
You paste an unreleased product name into an AI tool to get tagline ideas. Two weeks later, the client asks: which tools have seen our launch plans? Can you answer?

So far in this module, we have used Claude with research and briefs. Before we go further, let's make sure that client data stays safe. This lesson is about protecting client data and confidentiality.

Designers see sensitive material every day. Research recordings, customer lists, unreleased products, pricing and strategy. When you use an AI tool, you share some of this with a third-party service. That is not always wrong. But it must be a deliberate choice, and a permitted one.

So, what should you not paste without permission? First, personal data: names, contact details, photos, voice recordings, and anything that identifies a research participant. Second, unreleased work: product names, launch dates, prototypes and campaign ideas. Third, client secrets: strategy, prices, contracts and sales figures.

Next, check each tool's settings. Before you use a tool for client work, read its current privacy and data-use information, and check your own account settings. Do this for every tool, including Claude, Figma's AI features and image generators. And do not forget plugins. A plugin may send your content to its own service, with its own terms.

Then anonymise research, as we did in lesson two. Replace names with IDs before any AI step, and keep the key that links IDs to people outside AI tools.

Data-protection law also differs by country and region. This course teaches principles, not legal advice. If you work with personal data, ask your client or a data-protection specialist which rules apply.

Think of an AI tool as a print shop outside your studio. You would not send a client's secret launch poster to any print shop without checking who can see it, how long they keep the files, and whether the client agreed. AI tools need the same checks.

The simplest protection is to agree AI use in writing. Put a short statement in your proposal or contract. Which tools you use, and for what. What data you will not share. And how the client can say no.

Let's see a real plan. Katarzyna Nowak runs a small design studio in Kraków, Poland. A physiotherapy clinic network asks her to redesign its patient app, and the work includes patient interviews.

First, she lists her tools. Claude for synthesis and microcopy, Figma with its AI features, and a free image generator for moodboards. For each one, she reads the current data-use information and checks her account settings. Health data is especially sensitive, so she asks the clinic's data-protection contact which rules apply.

Then she makes three decisions. Interview recordings and names never go into AI tools, and notes are anonymised first. The new service name stays out of prompts until the client approves it, so she uses a placeholder. And moodboard prompts describe mood and materials, not the client's plans.

Finally, she adds a statement to her proposal. It names the tools and what they are used for. It says that patient names, recordings, health details and unreleased names never go into these tools. It says designers finish all final work, and the client can say no to AI. The client asks one question, and signs.

A common mistake is to assume that a paid plan always protects client data, or that a free plan always uses it for training. Do not assume either. Settings depend on the tool, the plan and the account, and they change. Check the current terms, and share less data by default. And put your agreement in writing.

Let's recap. First, do not paste personal data, unreleased work or client secrets into AI tools without permission, and anonymise research first. Second, check each tool's current data-use and training settings for your plan, including plugins. Third, rules differ by country, so agree AI use with clients in writing, and ask a specialist when personal data is involved.

Now it is your turn. In the exercise below this video, you will write a short AI-use statement for a client proposal, covering which tools you use and how you protect their data. It takes about twenty-five minutes. That completes module one. In the next lesson, we start on brand identity, with naming and verbal identity. See you there.
```

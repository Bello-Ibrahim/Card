# HeyGen Batch Pack: AI-03 M1 (Prompt Foundations)

Course: Prompt Engineering Masterclass. Make one HeyGen video per lesson below, using these settings for every video.

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

## L01 How AI Chat Tools Respond to You

- **Filename:** `ai-03-prompt-engineering-masterclass_M1_L01_presenter.mp4`
- **Expected length:** about 4.9 minutes (691 words). The quality gate accepts ±10%.

```text
You type write an email to a client into an AI chat tool. In a few seconds, you get a polite, well-written email. But it could be sent by anyone, to anyone, about anything. Why did a clever tool give you such a general answer?

Hi, and welcome to the Prompt Engineering Masterclass. In this first lesson, we look at how AI chat tools respond to you, and why your words matter so much.

An AI chat tool, such as Claude, ChatGPT or Gemini, is a program that reads the text you type and writes a reply. You do not need any technical knowledge. You type a request in normal language, which is called a prompt, and the tool responds.

The tool learned from a very large amount of text during its training. When you send a prompt, it predicts a likely, useful answer, word by word, based on your words and the patterns it learned. It does not look into your inbox or your files unless you give it that material. And it does not know your client, your team or your goal.

This explains two surprises. First, a vague prompt gives a generic answer. The tool fills the gaps with safe, common choices. Second, the same prompt can give different answers, because the tool is predicting, not looking up one fixed answer. Clear context and instructions leave fewer gaps, so the answers vary less.

Here is a simple way to picture it. Imagine a capable new colleague on their first day. They have read a lot and write well. But they know nothing about your team, your client or your goal.

If you say write to the client, they produce something polite and general. If you say write to Mr Diallo, whose delivery was three days late, apologise, and offer Friday, they can do excellent work. The AI tool is that new colleague, every time you start a new chat.

Let's see this at work. Mariana is an account manager at an engineering firm in São Paulo. A client's inspection visit has to move, because a key engineer is ill.

Her first prompt is just five words: write an email to a client. The tool returns a friendly email about their continued partnership. Nothing in it is wrong, but she cannot send it. It does not mention the visit, the new date or the reason.

Her second prompt is a few lines. It says who the reader is, that the Tuesday inspection must move because the lead engineer is ill, and that she can offer Thursday or Friday morning. It asks for one apology, a warm, professional tone, and a reply by Monday.

This time, the email names the visit, gives the reason in one sentence, offers both dates and asks for a reply by Monday. Mariana changes one phrase and sends it.

Notice that she used no special tricks. She gave the information a new colleague would need. She also used a placeholder instead of the client's real name. You will learn more about that in lesson three.

A common mistake is to think a generic answer means the tool is not very smart, and to keep pressing regenerate. Usually, the problem is missing information. Before you judge the output, ask yourself: did I tell it who, what and why? Adding two or three lines of context often helps more than asking again with the same words.

Let's recap. First, an AI chat tool predicts a likely answer from your prompt and its training. It does not know your situation unless you tell it. Second, vague prompts get generic answers, and the same prompt can give different answers. Third, clear context and instructions leave fewer gaps, so the output is often more useful and more consistent.

Now it is your turn. In the exercise below this video, you will ask Claude for an email to a client, first with five words, then with who, what and why. Then you compare the two answers in three short points. It takes about fifteen minutes. In the next lesson, we look at the anatomy of a strong prompt. See you there.
```

## L02 The Anatomy of a Strong Prompt

- **Filename:** `ai-03-prompt-engineering-masterclass_M1_L02_presenter.mp4`
- **Expected length:** about 5.0 minutes (697 words). The quality gate accepts ±10%.

```text
Most strong prompts are built from the same six parts. Once you know them, you can look at any weak prompt and quickly see what is missing. Today, you will learn all six.

In the last lesson, you saw that an AI tool fills the gaps you leave. Now let's look at a structure that helps you close those gaps. A structured prompt can contain six parts. Think of them as a checklist, not a form.

Part one is the role, the point of view the AI should take. For example, you are an experienced HR officer. A role often helps with tone and vocabulary. Part two is the task, the action you want, with a clear verb such as write, summarise, compare or list. The task is the only part you always need.

Part three is context, the background the AI cannot know, such as the audience and the situation. Part four is format, the shape of the output, like an email, a table or five bullet points. Part five is constraints, the limits and rules, such as a word limit or words to avoid. Part six is examples, a sample of what good output looks like.

When is each part worth adding? A quick question needs only a task. A document that other people will read usually needs task, context, format and constraints. A role helps when tone or expertise matters. Examples help most when you want a specific style or a repeated pattern.

The order is flexible. Many people write role and task first, then context, then format and constraints. What matters is that each part is clear, and that the parts do not contradict each other.

Think of a good order form at a print shop. The shop needs to know what to print, for which event, what size and paper, and by which date and budget. A sample helps too. Leave out a field, and the shop has to guess.

Let's see the six parts at work. Amara is an HR officer at a logistics company in Lagos. She needs a job advert for a logistics coordinator.

Her first prompt is just four words: write a job advert. The result is a general advert with invented benefits and no details about the real job. It looks finished, but Amara cannot use it.

Her new prompt is about eight lines. In short, it gives the AI an HR role, the job title and city, what the person will do each day, the experience needed, a clear layout, a limit of two hundred and fifty words, and a rule not to invent salary figures or benefits.

Amara labels each part for her team. Role, the HR officer. Task, write the advert. Context, the trucks, the warehouse staff and the experience needed. Format, an introduction, two bullet lists and how to apply. Constraints, the word limit, inclusive language and no invented pay. She uses no examples this time, because the format is already clear.

The constraint about salary is important. AI tools often fill gaps with details that sound real, so it helps to say what the tool must not add. The new advert is specific and ready for her manager to review.

A common mistake is to think a longer prompt is always better. They add every part, repeat themselves, and include background that does not matter. Long prompts can hide the task and create conflicting instructions. Add a part only when it changes the result.

Let's recap. First, the six parts of a structured prompt are role, task, context, format, constraints and examples. Second, only the task is always needed. Add the other parts when they change the result, especially for documents other people will read. Third, constraints such as do not invent figures help reduce made-up details.

Now it is your turn. In the exercise below this video, you will rewrite three weak prompts using the six parts, run one of them in Claude or ChatGPT, and label every part. Try to use at least four of the six parts in each one. It takes about twenty minutes. In the next lesson, we look at giving context that matters. See you there.
```

## L03 Giving Context That Matters

- **Filename:** `ai-03-prompt-engineering-masterclass_M1_L03_presenter.mp4`
- **Expected length:** about 4.9 minutes (683 words). The quality gate accepts ±10%.

```text
Context is the part of a prompt that turns a general answer into your answer. But some context should never go into an AI tool. So how do you give enough, without giving too much?

In lesson one, you saw that an AI tool fills gaps with safe, average choices. Context closes those gaps. Useful context answers four questions.

First, audience. Who will read the output? A board member, a new employee, or an angry customer? Second, purpose. Should it inform, persuade, apologise, or get a reply by a date? Third, background. What happened, and what was agreed before? Fourth, material. What do you already have? Pasting your own rough notes is often better than describing them.

Four short lines, one for each question, are often enough. You do not need to write a story.

Now, the other side: what not to share. Many AI tools may store your conversations, and your employer may have rules about which tools you can use. Before you paste anything, remove personal data, such as names, phone numbers and salaries of real people. Remove confidential client data, like client names and contract values. And remove internal secrets, such as unreleased products, prices and passwords.

Replace them with neutral placeholders in square brackets, such as client, product or amount, in capital letters. The AI can still write a good output, and you add the real details afterwards, outside the tool. Always follow your organisation's policy on AI tools. A simple habit helps. Before you press send, read your prompt once more and look for any name, number or address. If you find one, replace it.

Think of briefing a taxi driver. The airport is not enough if there are two terminals and your flight is in forty minutes. You tell them the terminal and the time. But you do not hand them your passport.

Let's see this in practice. Lan is a marketing coordinator at a cosmetics company in Hanoi. A large retail client has complained that a product launch campaign started late in their stores. She needs to reply quickly, and she wants an AI tool to help.

Her first prompt has useful facts. But it also contains a real person's name, her email address, the client's company name and an unreleased product name. None of that should go into the tool.

Her second prompt uses the four questions. The audience is the marketing lead at a retail chain, who is unhappy and busy. The purpose is to apologise and keep the relationship strong. The background is a five-day delay in forty stores, caused by late displays from a supplier. The material is her own short notes. Then comes the task, a polite, direct email under one hundred and fifty words.

Notice that the facts are still there. Only the identities are gone.

The reply is clear and specific. Lan copies it into her email program and puts in the real names there. The AI tool never saw them.

A common mistake is to remove so much detail that the prompt becomes vague again. Write to a client about a problem is safe, but not useful. The goal is to remove identities and secrets, not the situation. A retail client, a five-day delay in forty stores, caused by a supplier. That sentence contains no personal or confidential data, but it still gives the AI what it needs.

Let's recap. First, useful context answers four questions: audience, purpose, background and material. Second, never paste personal data, confidential client data or internal secrets into an AI tool. Use placeholders instead, and add the real details yourself, outside the tool. Third, keep the situation and remove the identities, so the output stays specific and safe.

Now it is your turn. In the exercise below this video, you will take a real work task, write its context in four short lines, and replace every name or sensitive detail with a placeholder. If you like, test it in Claude, ChatGPT or Gemini. It takes about fifteen minutes. In the next lesson, we look at controlling format, length and tone. See you there.
```

## L04 Controlling Format, Length and Tone

- **Filename:** `ai-03-prompt-engineering-masterclass_M1_L04_presenter.mp4`
- **Expected length:** about 5.0 minutes (697 words). The quality gate accepts ±10%.

```text
The same information can be a one-line message, a table or a polite email. If you do not say which one you want, the AI chooses for you. And it often chooses something longer than you need.

In the last lesson, you learned what context to give. Now we look at how the output looks and sounds. Three parts of the structured prompt control this: format, constraints and tone.

Format is the shape of the output, and it pays to be specific. For example, a table with the columns task, owner and status. Or five bullet points, one sentence each. Or an email with a subject line. Or a slide outline, with a title and three bullet points per slide. The more exact the shape, the less the tool has to guess.

Length is a constraint. Numbers work better than words like short. Under one hundred words, three sentences, or one line are easier for the tool to follow than brief. Word limits are not always exact, so check the result.

Reading level is also a constraint. For example, use simple words for readers who speak English as a second language. Tone is the voice, such as formal, friendly, firm or warm. Two words together often work well, like polite but firm, or warm and professional. If you have a sample of the tone you want, you can paste it in. You will practise that in the next lesson.

A useful habit is to put format and length at the end of your prompt, on their own lines. This keeps them easy to see and easy to change.

Asking for content without a format is like asking a caterer for food for a meeting. You might get a three-course lunch, when you wanted coffee and biscuits for ten people. Say the shape and the quantity, and you get what the meeting needs.

Let's see this in action. Kenji is a project manager at an equipment manufacturer in Osaka. His project to install a new packaging line is one week late, because a part is delayed. He needs to tell three different people.

First, he pastes his project notes into the prompt. A motor part is late at the supplier. Testing moves from week three to week four. The budget is not affected. And the supplier must confirm the delivery time by Friday.

For his director, he asks for one line, under twenty-five words, in a formal tone, with the delay, the new week and the budget. For his team, he asks for a table with three named columns, a neutral tone, and no extra text. For the supplier, he asks for a polite but firm email under one hundred words, with a subject line.

The results are three very different outputs from the same facts. But Kenji notices one thing. The tool added a sentence before the table, even though he asked for no extra text. He deletes it.

Small failures like this are normal. Noticing them is part of the skill. Always count the words, check the columns and check the tone before you send anything.

A common mistake is to write keep it short, or make it professional, and then be surprised when the result is still long or too stiff. These words mean different things to different readers. Use a number, a named format and two tone words instead. If the tool still ignores an instruction, ask for a fix in a follow-up, such as shorten this to fifty words.

Let's recap. First, name the format exactly, such as a table with named columns, a number of bullet points, or an email with a subject line. Second, use numbers for length, and plain descriptions for reading level. Third, describe tone with one or two clear words, and check the output, because tools do not always follow every instruction.

Now it is your turn. In the exercise below this video, you will ask for the same content in three formats, each with a length limit, and note which instruction the tool followed least well. It takes about twenty minutes. In the next lesson, we look at showing examples, also called few-shot prompting. See you there.
```

## L05 Showing Examples: Few-Shot Prompting

- **Filename:** `ai-03-prompt-engineering-masterclass_M1_L05_presenter.mp4`
- **Expected length:** about 5.0 minutes (689 words). The quality gate accepts ±10%.

```text
Sometimes you know exactly what you want, but you find it hard to describe. In those cases, showing is often easier than explaining. Today, you will learn how to show the AI what you mean.

In the last lesson, you controlled format and tone with clear instructions. Now we add the sixth part of the structured prompt: examples. This is called few-shot prompting.

Few-shot prompting means you include a few examples of the output you want inside your prompt. Few usually means two or three. A prompt with no examples is sometimes called zero-shot. Most of the prompts you have written so far in this course were zero-shot.

Examples help because they show several things at once: the format, the length, the tone and the way you make decisions. A description like label each comment by type leaves questions open. What are the types? And what about a comment that is both praise and a question? Two or three examples answer this without long explanations.

Few-shot prompting often helps with sorting and labelling, like customer comments or survey answers. It helps with repeated writing patterns, like short posts in your brand voice. And it helps with extracting information in a fixed shape, like a name, a date and an amount from each line.

A few rules make examples work well. Show the input and the output for each example, in the same layout every time. Cover the different cases, so if there are three labels, show at least one of each. Keep examples realistic, but invented. And check the results, because the tool may copy your examples too closely.

Think of a tailor. You could describe the collar, the fit and the sleeves in words. But the tailor understands much faster when you bring a shirt you already like. Examples work the same way for an AI tool.

Let's try it. Youssef is the guest relations manager at a hotel in Marrakesh. Every week, he receives many short guest comments. He wants to sort each one into praise, complaint or question.

His first prompt simply asks the tool to sort the comments into categories. The tool invents its own categories, such as food, staff and other, and some comments get two labels. This is not what he needs.

His new prompt names the three labels and says each comment gets exactly one. It adds a rule: if a comment contains a complaint, label it complaint. Then it shows three short example comments, one for each label, each followed by its label. Finally, it asks the tool to label new comments in the same format.

Youssef tests it with ten invented comments. Nine labels are correct. But one comment, lovely staff, but is the pool heated, is labelled praise. His rule covers complaints, not questions. So he adds one more line: if a comment contains a question and praise, label it question. He runs it again, and the label is now correct.

Notice what Youssef did. The examples set the pattern, and the extra rule handled the difficult case. He still checked every label himself, because examples improve results, but do not make them perfect.

A common mistake is to give examples that are all the same type, such as three positive comments. The tool then learns a narrow pattern, and may label too many new items as positive. Cover every category, and include a mixed case if you can.

Let's recap. First, few-shot prompting means including two or three examples of input and output in your prompt. Second, good examples use the same layout, cover every category, and are invented rather than copied from real, personal data. Third, examples often improve consistency, but you must still check each result, and add a rule for difficult cases.

Now it is your turn. In the exercise below this video, you will write a prompt with three labelled example comments, use it to sort ten new invented comments, and check every label yourself. It takes about twenty minutes. That completes week one. In the next lesson, we start on everyday work with writing and rewriting emails, reports and messages. See you there.
```

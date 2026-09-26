# HeyGen Batch Pack: AI-03 M3 (Reliable Prompts and Your Prompt Library)

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

## L11 Checking Outputs: Accuracy, Bias and Confidentiality

- **Filename:** `ai-03-prompt-engineering-masterclass_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (680 words). The quality gate accepts ±10%.

```text
When you send a document written with AI help, your name is on it, not the tool's. A two-minute check before you use an output protects you, your colleagues and your organisation. Today, you will learn a simple checklist.

Welcome to week three. This week is about reliable prompts, and about your own prompt library. We start with a four-part checklist to use before any AI output goes into your work.

Part one is facts and figures. Check every number, date, name and quotation. AI tools can produce figures that look exact but are invented, and they may not know recent events. Part two is sources. If the output mentions a study, a law or a report, check that it exists and says what the output claims. If you cannot find it, remove it.

Part three is bias and one-sided wording. Read the output as the people it describes would read it. Look for one side presented as the only view, assumptions about gender, age or background, and strong words like obviously or failed, where a neutral word would be fairer.

Part four is confidentiality. Confirm that you did not paste personal data, client details or internal secrets, and that the output contains none. Rules on personal data and workplace AI use differ between countries and employers. So always check your own organisation's policy.

You can also write prompts that make checking easier. For example, ask the tool to mark any figure that did not come from your notes, to include no sources unless you gave them, and to say when it is not sure. These lines often help, but they do not replace your own check.

Checking an AI output is like checking a restaurant bill before you pay. Most of the time, it is correct. But it is your payment, so you look at each line, and you do not pay for a dish you never ordered.

Let's use the checklist. Kwame is a policy analyst at a farmers' cooperative in Kumasi. He asked an AI tool for a short briefing on drip irrigation for the cooperative's board. He is busy, and the draft looks ready to send.

Here is part of the output. It reads well. But look closely. It gives one exact water saving for every farm, cites a named report, says every modern farmer has already switched, and names two cooperative members with their plot numbers.

Kwame works through the four checks. Facts: the exact saving has no basis in his notes, because real savings depend on crop, soil and climate. He marks it to check. Sources: he cannot find the report anywhere, so he removes it.

Bias: all modern farmers and clearly falling behind are one-sided, and unfair to members who cannot afford new equipment. He rewrites them in neutral words. Confidentiality: two members' names appear, because he pasted them in his notes. He removes them, and will use placeholders next time.

His improved prompt adds four short lines. Use only the figures in my notes. Mark anything else to check. Present benefits and costs in a balanced way. And do not name members.

A common mistake is to check only the parts that look wrong. The most dangerous errors look correct: a realistic figure, a believable report title, a confident sentence. So go through the whole checklist every time.

Let's recap. First, before using any AI output, check facts and figures, check sources, look for bias, and confirm confidentiality. Second, prompts can make checking easier, but they do not replace your own check. Third, rules on data and AI use differ between countries and employers, so always follow your own organisation's policy. Soon, you will use this checklist on every prompt in your capstone library.

Now it is your turn. In the exercise below this video, you will check a short AI-written briefing with the checklist, mark every issue you find, and rewrite the prompt so the next output is easier to check. It takes about twenty minutes. In the next lesson, we look at testing a prompt across tools. See you there.
```

## L12 Testing a Prompt Across Tools

- **Filename:** `ai-03-prompt-engineering-masterclass_M3_L12_presenter.mp4`
- **Expected length:** about 4.9 minutes (681 words). The quality gate accepts ±10%.

```text
You have a prompt that works well in one tool. Will it work as well in another tool, or next month in the same tool? The only way to know is to test it. Today, I will show you how.

In the last lesson, you learned to check one output. Now we compare outputs from different tools, in a fair and simple way.

Claude, ChatGPT and Gemini are built by different companies and trained in different ways. The same prompt can give a different length, structure and tone in each one, and sometimes different facts. Tools are also updated, so a result can change over time.

A fair test keeps everything the same except the tool. Use the same prompt, copied exactly, without improving it between tools. Use the same input. And start a new chat in each tool, so earlier messages do not affect the result. If you use saved instructions, note that too.

Then score each output from one, poor, to five, excellent, on three criteria. Accuracy: the facts are correct, and nothing is invented or missing. Format: it follows the requested format and length. Tone: it suits the audience. Finally, record the tool, the model if it is shown, and the date.

Your scores are your judgement, not a scientific measurement. That is fine. The aim is a practical choice for one task, not finding the best AI. Free plans may also limit how many messages you can send in a day, so plan your tests.

Think of testing one recipe in three different ovens. Same ingredients, same steps, same time. If one cake is dry, you know it is the oven, not the recipe. And you write a note on the recipe card.

Let's run a test. Chloé is a communications officer at an environmental charity in Montréal. She wants to test her prompt for turning event notes into a short social media post.

I have three browser tabs open: Claude, ChatGPT and Gemini, each on its free plan. Here is the prompt in a notes app. It asks for a post under sixty words, in a friendly and hopeful tone, ending with one question, and with no figures that are not in the notes. The notes are below it.

I start a new chat in Claude, paste the prompt exactly, and send it. Then I do the same in ChatGPT, and then in Gemini. A new chat each time, and no changes to the prompt.

Now I place the three outputs side by side, and open a simple spreadsheet. The columns are tool, date, accuracy, format, tone, total and notes.

Let's score them. For example, one output might count sixty-four words, so it loses a point on format. Another might add a phrase like our biggest event ever, which is not in the notes, so it scores low on accuracy. Another might follow every instruction.

Finally, I fill in the notes column, and write the choice: use the highest-scoring tool for this task, and retest in three months. Chloé now has evidence for her choice, not only a feeling.

A common mistake is to change the prompt a little in each tool, or to test in a chat that already has earlier messages. Then the test is not fair. Another is to test once and decide forever. Tools change, so record the date and retest important prompts.

Let's recap. First, a fair test uses the same prompt, the same input, and a new chat in each tool. Second, score each output from one to five on accuracy, format and tone, and record the tool and the date. Third, the best tool depends on the task, and results can change when tools are updated, so retest important prompts.

Now it is your turn. In the exercise below this video, you will run one of your own prompts in Claude, ChatGPT and Gemini, score each output on three criteria, and choose a tool for that task. It takes about twenty-five minutes. In the next lesson, we turn prompts into reusable templates, and start your capstone. See you there.
```

## L13 Turning Prompts into Reusable Templates

- **Filename:** `ai-03-prompt-engineering-masterclass_M3_L13_presenter.mp4`
- **Expected length:** about 4.9 minutes (686 words). The quality gate accepts ±10%.

```text
If you write a good prompt once and never use it again, you lose most of its value. A template lets you, and your colleagues, get the same quality every time, in a few seconds. Today, you will learn how to build one.

In the last lesson, you tested one prompt across three tools. Now we make good prompts reusable. This lesson also starts your capstone project. It is the first of three steps.

A prompt template is a prompt where the parts that change are replaced with clear placeholders. You used placeholders in lesson three to protect confidential data. In a template, they also show what the user must fill in. So a placeholder does two jobs: it keeps data safe, and it makes the prompt easy to reuse.

Here is how to make one. Start from a prompt that worked, one you have tested and improved. Find the parts that change each time, such as the audience, the document or the date. Replace them with placeholders in capital letters and square brackets. Keep the parts that make it work: the role, the format, the constraints and the checking instructions.

Most work tasks fit one of six patterns from this course. Draft from notes. Rewrite. Summarise or extract. Classify with examples. Analyse or compare step by step. And interview first, when the context is unclear. Choose the pattern first, and each template is faster to write.

A template is like a form letter with blank lines. The structure, the tone and the important sentences are already written. Each time, you only fill in the name, the date and the details, and the quality stays the same.

Let's make one. Ana is a pharmacy manager at a chain of pharmacies in Lisbon. Every week, she writes a short update for her staff, and she has a prompt that she has tested and improved.

Her prompt gives a manager role, names the audience and the two topics, asks for a friendly tone, five bullet points under one hundred and twenty words, and says do not add facts that are not in my notes. In the template, the role, the audience, the topics, the tone, the number of points and the word limit all become placeholders.

Look at the last line. The notes placeholder includes a reminder: no personal or patient data. Because it is part of the template, every future user will see it. Ana tests the template with a different topic, stock changes, and the result has the same quality.

A common mistake is to replace too much. A template like write output for audience in format is too empty to help anyone. Keep fixed everything that made the original prompt work, and use placeholders only for what really changes. The quality comes from the fixed parts.

Now, your capstone. Over the next three lessons, you will build a personal prompt library: fifteen tested, documented templates for your own job role. To choose the fifteen tasks, look for tasks that are frequent, time-consuming, and safe to do with AI, which means they need no personal or confidential data. Those tasks usually save the most time.

Ana does this too. She lists her fifteen recurring tasks, such as a reply to a supplier delay, a rota change message, or sorting customer feedback, and she writes the pattern next to each one. This list becomes the plan for her whole library.

Let's recap. First, a template replaces the changing parts of a tested prompt with clear placeholders, such as audience or document. Second, keep the role, format, constraints and checking instructions fixed, because they make the template reliable. Third, for the capstone, choose fifteen tasks that are frequent, time-consuming and safe to do with AI.

Now it is your turn. This exercise is capstone step one. You will list fifteen recurring tasks from your job, choose a pattern for each, and turn your first three prompts into templates on a prompt card. Use only invented or non-confidential material. It takes about forty minutes. In the next lesson, we look at building and testing your library. See you there.
```

## L14 Building and Testing Your Library

- **Filename:** `ai-03-prompt-engineering-masterclass_M3_L14_presenter.mp4`
- **Expected length:** about 4.9 minutes (684 words). The quality gate accepts ±10%.

```text
A template that worked once might have worked by luck. Before you trust it, and before a colleague uses it, test it with different inputs. Today, you will learn how to test your templates, and what to do when a test fails.

In the last lesson, you turned your first prompts into templates and chose fifteen tasks for your capstone. Now you build and test the whole library.

Test each template at least twice, with inputs that are really different. One typical case, such as a normal weekly update. And one harder case, such as a sensitive topic, very short notes, or an unusual request. One test shows that a template can work. Two or more show whether it works reliably.

For each test, use the method you already know. Fill the placeholders with realistic, non-confidential input. Run the template in a new chat. Check the output for facts, sources, bias and confidentiality. Score it from one to five on accuracy, format and tone. Then record the input, the scores and any problems on the prompt card.

When a test shows a weakness, use the diagnosis from lesson ten. Make one targeted change, raise the version number, for example from version one to version two, and test again. Free plans may limit how many messages you can send each day, so plan your tests across several days.

Testing a template is like testing a new bridge. One light car crossing safely does not prove much. Engineers test with a typical load, and a heavy load, before the bridge opens to the public. Your harder case is the heavy load.

Let's watch a test. Leila is a school administrator at a private school in Amman. Her template writes letters to parents. It names the year group, the situation and a deadline, asks for a warm and clear tone under one hundred and eighty words, in simple English, and says do not add facts that are not in my notes.

Test one is a typical case: a school trip to a museum, with a consent form due on a date. The letter is clear, one hundred and sixty words, and includes the deadline. She scores it five, five and five.

Test two is a harder case. Several students had a stomach illness after a school lunch, and the school has changed its catering company. The letter is the right length. But it says there is no risk to any student. That is not in her notes, and she cannot promise it. The tone is also too cheerful for a health topic. She scores it two, five and two.

Leila names the cause: missing context, and a gap in the constraints. She adds two lines. Match the tone to the situation, serious and calm for health or safety. And do not make promises or reassurances that are not in my notes.

She saves it as version two and repeats both tests. The trip letter is still good. The illness letter is now calm and factual, and makes no new promises. Her prompt card records both versions, the inputs, the scores and the change.

A common mistake is to test with two very similar inputs. Both pass, and the weakness stays hidden until a difficult situation arrives. So always make one test a harder case: a sensitive topic, missing information, or an unusual audience.

Let's recap. First, test every template at least twice with different inputs: one typical case and one harder case. Second, check each output with the four-part checklist, score it, and record the input, the scores and the changes on the prompt card. Third, when a test fails, make one targeted change, raise the version number, and test again.

Now it is your turn. This exercise is capstone step two. You will write all fifteen templates, test each one at least twice, including a harder case, and record the results and any changes. It takes about an hour, so split it over more than one session if you need to. In the final lesson, we look at documenting and sharing your library. See you there.
```

## L15 Documenting and Sharing Your Library

- **Filename:** `ai-03-prompt-engineering-masterclass_M3_L15_presenter.mp4`
- **Expected length:** about 5.0 minutes (695 words). The quality gate accepts ±10%.

```text
Six months from now, will you remember why a template says do not make promises? Will a new colleague know which placeholder to fill? Good documentation turns your prompts into a tool other people can trust.

In the last lesson, you tested all fifteen templates. In this final lesson, you document them, so that you and your colleagues can use them with confidence. You will also see how your capstone will be assessed.

Each prompt gets one prompt card, with the same fields. A short, clear name, such as supplier delay reply. A version number, which you raise every time you change the template. A one-line purpose. The pattern. And the full template, with placeholders.

Then, the inputs: what goes in each placeholder, and what must never go in. A short, non-confidential example input and output. Your test notes. And the tool and the date of the last test. Keep all the cards in one shared place your team already uses, such as a shared document or a spreadsheet.

AI tools change their features, limits and behaviour, so a template that works this month may give different results later. Three habits help. Retest important prompts regularly, for example every three months. Update the date and version after every test or change. And remove prompts that nobody uses, or that no longer work well.

At the top of the library, write a short introduction for colleagues. Say what the library is for, how to use a card, and give three safety rules. Never paste personal or confidential data. Check every output with the four-part checklist. And follow your organisation's AI policy.

A documented library is like a well-kept recipe book in a restaurant kitchen. Each recipe has the method, a photo of the dish and the chef's notes. A new cook can make the same dish. And the chef updates the recipe when a supplier changes.

Let's look at a finished card. Min-jun is a finance analyst at a manufacturing company in Seoul. His card is called monthly variance summary, and it is on version three. Its purpose is to explain the main budget differences to department heads.

The template asks for the three largest differences between budget and actual, in a table, followed by three plain sentences for a non-finance reader. It marks any figure the tool calculated, so he can check it. And the figures placeholder says no salaries or personal data.

Now look at his test notes. Version one used too many finance words. Version two added a non-finance reader. Version three added the check mark, after one wrong subtraction. Anyone who reads the card knows why each line is there. His scores in the last test were five, five and four.

His introduction for colleagues is only five sentences long, and it ends with the three safety rules. Short is fine, as long as it is clear.

A common mistake is to keep only the final prompt, and delete the test notes. Without test notes, nobody knows why the prompt looks the way it does. Then a colleague might remove an important line. Keep the test notes short, but keep them.

Your library will be assessed on the quality of your prompts, how you improved them, how you tested and checked them, how safely you handled data, and how well they are documented. Read the full rubric on the course page before you submit.

Let's recap. First, every prompt card has the same fields, from name and version to test notes and the date of the last test. Second, retest important prompts regularly, and update the version and date, because tools change. Third, a short introduction with clear safety rules helps colleagues use the library correctly. Your library is a real tool you can use at work every week.

Congratulations. You have completed the Prompt Engineering Masterclass. Your last exercise is capstone step three. Document all fifteen prompts in one shared place, write a short introduction, and ask a colleague to try one card. Then submit your Personal Prompt Library for assessment. Before you submit, go through the checklist on the course page. Thank you for learning with us, and good luck.
```

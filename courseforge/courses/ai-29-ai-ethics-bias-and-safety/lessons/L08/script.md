# L08 Testing an AI Tool for Bias | Presenter Script

Course: AI-29 · Video: 5 min · Words: 693

## Hook
Two people have the same CV, word for word. The only difference is the name at the top. If you ask a chatbot to write a job reference for each of them, will it describe them in the same way?

## Explain
In the last lesson, you built a responsible-use checklist. Now we start your capstone. You cannot see inside a chatbot, but you can test what it writes. The simplest structured test is a paired prompt. You send the same request twice, and change only one detail, such as a name, age, gender, country or disability. Then you compare the answers.

Good testing follows five rules. Change one detail only. Start a new chat for every prompt. Repeat each pair at least three times, because answers vary. Record the exact prompts and answers. And describe your findings carefully, because a few prompts are a limited test, not proof of bias.

Always follow the tool's terms of use, and never use real personal data. Invented names and CVs only. And remember that chatbots change between versions, so your results show one version at one time.

Think of a fair taste test. You give people the same drink in the same kind of cup, and change only the label. If they rate the drinks differently, the label is the likely reason. If you also change the cup, you learn nothing.

## Demonstrate
Let's run a test on screen. Tomás Herrera is an HR officer in Chile. Before his team drafts references with a chatbot, he wants to test it. We will follow his steps in a free chatbot and a spreadsheet.

First, open a spreadsheet with these columns. Pair number, detail changed, prompt A, prompt B, run, answer A, answer B, and differences noticed. Next, write an invented CV. A project coordinator with five years' experience, who managed a team of six and delivered twelve projects on time.

Now write prompt A. Write a short job reference for Amina, a project coordinator with this CV. Then copy it and change only the name to Lucas. That is prompt B. Check carefully that nothing else has changed.

Open a new chat, paste prompt A, and copy the full answer into the spreadsheet. Open another new chat, paste prompt B, and copy that answer too. Then repeat both, two more times, so each prompt has three runs.

Now compare. Highlight describing words, such as caring, supportive, confident or decisive. Note the length, the skills and any leadership words. Here is what you might see. Perhaps leadership words appear in one of three Amina answers, and in three of three Lucas answers. Your results may be different.

Finally, write one careful sentence. For example, in this limited test of three runs, the Lucas references used more leadership words, and more tests are needed. Notice what it does not say. It does not say the tool is biased.

A common mistake is to run one pair, see a difference, and say the tool is biased. One difference may be random. The opposite mistake is also common. One pair looks the same, so people say the tool is fair. Repeat each pair, test several details, and record everything.

For your notes, here is a short case with the same structure. A bank tested its chatbot with twenty pairs, changing only the customer's age. It saw a pattern, called it a limited test, asked its vendor to investigate, and repeated the test each month.

## Recap
Let's recap. First, a paired prompt sends the same request twice and changes only one detail. Second, use a new chat for each prompt, repeat each pair several times, and record the exact prompts and answers. Third, follow the tool's terms, never use real personal data, and describe findings as a limited test, not proof of bias.

## CTA
Now it is your turn. This exercise is step one of your capstone. Choose a real AI tool, run at least five pairs of prompts that each change one detail, and record the differences in a table. It takes about forty minutes. Keep your table, because in the next lesson, we will rate and prioritise the risks you find. See you there.

## Thumbnail
Headline: Same CV, Different Words?
Image: Navy background, two identical CV cards side by side, one headed 'Amina' and one 'Lucas', with a magnifying glass between them, headline in teal Inter Bold.

## Production Notes
- [VERSION] Chatbot outputs change between model versions. Every answer shown in the screen demo must be recorded from the live tool on the day of recording, never written in advance. The voiceover describes results only as 'what you might see' and 'a limited test, not proof of bias'.
- [VERSION] Demo tool: Claude or ChatGPT (free version) in a browser, plus any spreadsheet app. Check free access and the 'new chat' button location before recording. Record the tool name, plan and date on screen in the spreadsheet header.
- Screen steps are copied from the content.md worked example (steps 1 to 10). Use only the invented CV from content.md: no real names, CVs or personal data anywhere on screen. Hide the account name, email and chat history sidebar before recording.
- If the live runs show no difference, keep that result on screen: the voiceover already allows for any outcome ('you might see'). Do not re-run until a difference appears.
- Tomás Herrera (HR officer, Chile) and the regional bank case study are hypothetical, written by CertifAI (DECISIONS.md: CertifAI's own hypothetical case); no named incident or statistic is used.
- Follow the chatbot's terms of use during recording, as the lesson tells learners to do.

# L04 Controlling Format, Length and Tone | Presenter Script

Course: AI-03 · Video: 5 min · Words: 702

## Hook
The same information can be a one-line message, a table or a polite email. If you do not say which one you want, the AI chooses for you. And it often chooses something longer than you need.

## Explain
In the last lesson, you learned what context to give. Now we look at how the output looks and sounds. Three parts of the structured prompt control this: format, constraints and tone.

Format is the shape of the output, and it pays to be specific. For example, a table with the columns task, owner and status. Or five bullet points, one sentence each. Or an email with a subject line. Or a slide outline, with a title and three bullet points per slide. The more exact the shape, the less the tool has to guess.

Length is a constraint. Numbers work better than words like short. Under one hundred words, three sentences, or one line are easier for the tool to follow than brief. Word limits are not always exact, so check the result.

Reading level is also a constraint. For example, use simple words for readers who speak English as a second language. Tone is the voice, such as formal, friendly, firm or warm. Two words together often work well, like polite but firm, or warm and professional. If you have a sample of the tone you want, you can paste it in. You will practise that in the next lesson.

A useful habit is to put format and length at the end of your prompt, on their own lines. This keeps them easy to see and easy to change.

Asking for content without a format is like asking a caterer for food for a meeting. You might get a three-course lunch, when you wanted coffee and biscuits for ten people. Say the shape and the quantity, and you get what the meeting needs.

## Demonstrate
Let's see this in action. Kenji is a project manager at an equipment manufacturer in Osaka. His project to install a new packaging line is one week late, because a part is delayed. He needs to tell three different people.

First, he pastes his project notes into the prompt. A motor part is late at the supplier. Testing moves from week three to week four. The budget is not affected. And the supplier must confirm the delivery time by Friday.

For his director, he asks for one line, under twenty-five words, in a formal tone, with the delay, the new week and the budget. For his team, he asks for a table with three named columns, a neutral tone, and no extra text. For the supplier, he asks for a polite but firm email under one hundred words, with a subject line.

The results are three very different outputs from the same facts. But Kenji notices one thing. The tool added a sentence before the table, even though he asked for no extra text. He deletes it.

Small failures like this are normal. Noticing them is part of the skill. Always count the words, check the columns and check the tone before you send anything.

A common mistake is to write keep it short, or make it professional, and then be surprised when the result is still long or too stiff. These words mean different things to different readers. Use a number, a named format and two tone words instead. If the tool still ignores an instruction, ask for a fix in a follow-up, such as shorten this to fifty words.

## Recap
Let's recap. First, name the format exactly, such as a table with named columns, a number of bullet points, or an email with a subject line. Second, use numbers for length, and plain descriptions for reading level. Third, describe tone with one or two clear words, and check the output, because tools do not always follow every instruction.

## CTA
Now it is your turn. In the exercise below this video, you will ask for the same content in three formats, each with a length limit, and note which instruction the tool followed least well. It takes about twenty minutes. In the next lesson, we look at showing examples, also called few-shot prompting. See you there.

## Thumbnail
Headline: One Update, Three Shapes
Image: Navy background, one note card branching into three outputs: a one-line message, a small table and an email, headline in teal Inter Bold.

## Production Notes
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini must be checked before recording (content.md Review Flags).
- Kenji, his equipment manufacturer in Osaka, and team members Aiko, Ben and Chen are hypothetical. Do not show real company names or logos in stock footage.
- All four prompts from the worked example (notes, director, team, supplier) appear on code slides using the exact text in content.md, including the [MONTH] placeholder. The voiceover summarises them.
- Word limits are described as not always exact; do not suggest tools always follow format instructions.

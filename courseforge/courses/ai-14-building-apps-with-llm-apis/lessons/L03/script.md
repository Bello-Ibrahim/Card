# L03 Prompt Design for Applications | Presenter Script

Course: AI-14 · Video: 5 min · Words: 686

## Hook
In a chat window, you can fix a bad answer by asking again. In an app, the same prompt runs thousands of times for people you never see. So it must work well every time, without you there to correct it.

## Explain
In the last lesson, you made your first call. Now let's make the prompt good. In an application, a prompt has two parts. A system prompt that you write once, and user data that changes on every request, such as a customer message or a form field.

Good application prompts do four things. First, set the role, the task and the audience. Say who the model is acting as, what it must do, and for whom. Second, give clear rules. Tone, length, language, and what to do when it does not know.

Positive instructions, like reply in the customer's language, work better than a long list of things not to do. And give the reason for a rule when it is not obvious. The model then applies the rule more sensibly.

Third, separate instructions from data. Put user data inside clear tags, and tell the model what the tags contain. This helps it tell your instructions apart from the user's text, and it prepares you for lesson eleven, on prompt injection.

Fourth, show one to three short, varied examples of good input and output. They teach style faster than paragraphs of description. Vary them, so the model does not copy one word for word.

A system prompt is like the briefing for a new employee. Help customers is a weak briefing. A strong one says who the customers are, what the employee may promise, how to write, what to do when unsure, and shows two good past replies.

One more rule. Prompts are code. Keep them in files under version control, give each version a name, and test a new version before you use it. In this course, we also leave sampling settings such as temperature alone, because some current models do not accept them. Improve the prompt instead.

## Demonstrate
Efua Mensah builds a reply assistant for a mobile network provider in Accra, Ghana. Support agents paste a customer message, and the app drafts a reply.

Her first version just says reply to this customer, followed by the message. The replies are long, and sometimes promise refunds the company does not offer. Once, it even followed an instruction written inside the customer's message.

Now look at version three, stored in its own file. It sets the role and the readers, and limits replies to eighty words. It never promises refunds, and says an agent will review the request. It asks one short question when unsure. It explains the tags, and gives one example.

Her code reads the prompt from the file, sends it as the system prompt, and wraps each customer message in the tags. Max tokens stays at three hundred. Because the prompt lives in a file, every change shows up in Git, with a clear version name.

She runs both versions on the same five test messages. You'll see something like this. Version three replies are shorter, never promise refunds, and ignore the instruction hidden in the customer's message.

Watch out for a common mistake. Many developers edit a prompt in production after one bad answer. The fix helps that case, but breaks three others that nobody checks. Keep the old version, and compare both on the same inputs before you switch.

## Recap
Let's recap. First, a strong system prompt sets the role, task and audience, gives clear rules with reasons, and includes a few varied examples. Second, put user data inside clear tags, and tell the model to treat it as data. Third, prompts are code. Store them in version control, name each version, and compare versions on the same inputs.

## CTA
Now it is your turn. In the exercise, you will improve a weak support prompt in three versions, run each one on the same five customer messages, and score the replies in a table. In the next lesson, Tokens, Context and Cost, you will see exactly what each call costs. See you there.

## Thumbnail
Headline: Prompts That Work Every Time
Image: Navy background, three stacked prompt files labelled v1, v2, v3 with a teal tick on v3, headline in teal Inter Bold.

## Production Notes
- [VERSION] The voiceover says some current models do not accept sampling settings such as temperature. Check this against the current docs on the recording day; if it is no longer true, cut that sentence from scene 7 and re-time.
- The comparison results for versions 1 and 3 are hypothetical example results from Efua's notes; show 'example results' on screen.
- Record the demo with a small development model and max_tokens 300 (from L02). Do not show a model ID in the voiceover.
- The status page link inside the v3 prompt should be a placeholder, not a real provider's URL. Efua Mensah and the Accra provider are fictional: no real network brand or logo on screen.

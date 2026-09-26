# HeyGen Batch Pack: AI-14 M1 (LLM API Foundations)

Course: Building Apps with LLM APIs. Make one HeyGen video per lesson below, using these settings for every video.

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

## L01 How LLM APIs Work

- **Filename:** `ai-14-building-apps-with-llm-apis_M1_L01_presenter.mp4`
- **Expected length:** about 5.3 minutes (734 words). The quality gate accepts ±10%.

```text
You chat with an AI assistant for ten minutes, and it remembers everything you said. Then you call the same model through its API, ask a follow-up question, and it has no idea what you mean. Nothing is broken. Let's see why.

Hi, and welcome to Building Apps with LLM APIs. Over four weeks, you will build real features on a large language model API, using the Claude API as our main example. We start with the basics of a request and a response.

An LLM API works like other web APIs. Your code sends an HTTP request and gets a response back. What is new is the shape of that request. Its main part is a list of messages. Each message has a role and some content.

The user role is text from the person using your app. The assistant role holds earlier replies from the model. The list starts with a user message, and the roles take turns. The system prompt is a separate field, not a message. It sets the model's role, rules and style.

You also send settings. The two you will use in every call are the model, which chooses the model to run, and max tokens, the longest reply you allow. And what is a token? Models do not read words. They read tokens, small pieces of text, often a short word or part of a longer one.

Everything is measured in tokens. Input length, reply length, price and limits. Each model can read only a limited number of tokens in one request. This limit is the context window. It includes the system prompt, every message and the reply. The size depends on the model, so check the current models page.

The response gives you three things. First, content, a list of blocks. For now, you only need the text block. Second, the stop reason. End turn means the model finished normally. Max tokens means it hit your limit, and the reply is cut off. Third, usage, the input and output tokens you pay for.

Now the most important idea. The API is stateless. It does not remember earlier requests. Picture a very knowledgeable assistant who answers the phone, but forgets every call as soon as it ends.

To continue yesterday's discussion, you must read your notes aloud first. Yesterday I asked this, you said that, and now my question is this. The notes are your messages list. And longer notes mean longer, more expensive calls.

Let's see this in practice. Tomás builds a help chat for a chain of bakeries in Montevideo, Uruguay. A customer writes, do you have gluten-free bread?

His app sends a short system prompt that says be brief and friendly, and one user message with the question. You'll see something like this. Yes, we bake gluten-free loaves every morning. The stop reason is end turn, and usage shows a few input and output tokens.

Then the customer asks, which shops have it? Tomás's first version sent only this new question. The model replied, which product do you mean? It had no idea what it referred to, because nobody sent the history.

In the fixed version, his app adds the model's earlier reply and the new question to the list, and sends the full list. Now the model understands what it means. Tomás also notices something. Input tokens grow with every turn, because the whole history is sent again each time.

A common mistake is to think the API remembers the user because you send the same API key each time. The key only identifies your account for billing. Your app must keep the history, in memory, a session or a database, and send it every time.

Let's recap. First, a request has a list of messages with user and assistant roles, a system prompt in its own field, a model and a max tokens limit. Second, a response has content blocks, a stop reason and token usage. Third, the API is stateless. Your app sends the full history every time, so cost grows as the conversation grows.

Now it is your turn. In the exercise, you will turn a four-turn chat into a messages list on paper, and mark every part that is sent again. No API account is needed yet. In the next lesson, Setup: API Keys, SDKs and a Low-Cost Budget, you will make your first real call. See you there.
```

## L02 Setup: API Keys, SDKs and a Low-Cost Budget

- **Filename:** `ai-14-building-apps-with-llm-apis_M1_L02_presenter.mp4`
- **Expected length:** about 4.9 minutes (687 words). The quality gate accepts ±10%.

```text
An API key is like a credit card number for your code. If it leaks into a public repository, someone else can spend your money. Today you will make your first call, and you will set it up safely and cheaply from the first minute.

In the last lesson, you saw what a request and a response look like. Now let's make a real one. First, one important fact. The Claude API is a paid service. You pay for every input and output token. Your costs can stay small, but only if you set limits before you start.

Setup has five steps. Create an account in the Claude Console and add a payment method. Set a monthly spend limit. Create an API key and copy it once. Store it in an environment variable, never in your code. Then install the official SDK. Before you sign up, check the current list of supported countries.

Keep keys out of Git. If you use a dot env file, add it to your git ignore file before your first commit. And if a key is ever committed, even for one minute, delete it in the Console and create a new one. Removing the file is not enough, because the key stays in the history.

Three habits keep costs low while you develop. Use a smaller, cheaper model for building and testing. Keep max tokens low, for example three hundred. And keep the model name in one constant, so you can change it in one place. Model names and prices change, so check the current models and pricing pages.

Think of a prepaid travel card that you give a teenager instead of your main bank card. It has a fixed limit, you can cancel it at any time, and a mistake cannot empty your account. The spend limit is that fixed limit. A new key is the replacement card.

Let's follow Mei Lin. She is a developer at a small travel start-up in Penang, Malaysia, and she is setting up her laptop.

In the Console, she opens the billing settings and sets a low monthly limit. Then she creates a key and gives it a clear name, so she always knows where it is used. She copies it once, because the Console will not show it again.

In her terminal, she saves the key in an environment variable. On Windows, the command looks a little different. Then she creates a virtual environment and installs the SDK.

Now she writes a short file for her first call. It sets the model in one constant, creates a client that reads the key automatically, asks for one day trip from Penang, and allows three hundred tokens. Then it prints the reply, the stop reason and the token counts.

She runs it. You'll see something like a suggestion for a day trip to Langkawi, then a stop reason of end turn, and a small number of input and output tokens. Then she lowers max tokens to twenty and runs it again. This time the reply is cut off, and the stop reason says max tokens.

Finally, she runs git status to check that no file with her key will be committed. A common mistake is to paste the key straight into the code just to test, and then commit it. Always use the environment variable, and replace any key that has been exposed.

Let's recap. First, the Claude API is paid, so set a monthly spend limit before your first call. Second, keep your key in an environment variable, never in code or Git, and replace any key that leaks. Third, while developing, use a smaller model, a low max tokens value and one model constant, and look up model names and prices on the live pages.

Now it is your turn. In the exercise, you will make your first API call and print the reply, the stop reason and the token counts. Then run it again with a tiny max tokens value and compare. In the next lesson, Prompt Design for Applications, you will learn to write prompts that work every time. See you there.
```

## L03 Prompt Design for Applications

- **Filename:** `ai-14-building-apps-with-llm-apis_M1_L03_presenter.mp4`
- **Expected length:** about 4.9 minutes (686 words). The quality gate accepts ±10%.

```text
In a chat window, you can fix a bad answer by asking again. In an app, the same prompt runs thousands of times for people you never see. So it must work well every time, without you there to correct it.

In the last lesson, you made your first call. Now let's make the prompt good. In an application, a prompt has two parts. A system prompt that you write once, and user data that changes on every request, such as a customer message or a form field.

Good application prompts do four things. First, set the role, the task and the audience. Say who the model is acting as, what it must do, and for whom. Second, give clear rules. Tone, length, language, and what to do when it does not know.

Positive instructions, like reply in the customer's language, work better than a long list of things not to do. And give the reason for a rule when it is not obvious. The model then applies the rule more sensibly.

Third, separate instructions from data. Put user data inside clear tags, and tell the model what the tags contain. This helps it tell your instructions apart from the user's text, and it prepares you for lesson eleven, on prompt injection.

Fourth, show one to three short, varied examples of good input and output. They teach style faster than paragraphs of description. Vary them, so the model does not copy one word for word.

A system prompt is like the briefing for a new employee. Help customers is a weak briefing. A strong one says who the customers are, what the employee may promise, how to write, what to do when unsure, and shows two good past replies.

One more rule. Prompts are code. Keep them in files under version control, give each version a name, and test a new version before you use it. In this course, we also leave sampling settings such as temperature alone, because some current models do not accept them. Improve the prompt instead.

Efua Mensah builds a reply assistant for a mobile network provider in Accra, Ghana. Support agents paste a customer message, and the app drafts a reply.

Her first version just says reply to this customer, followed by the message. The replies are long, and sometimes promise refunds the company does not offer. Once, it even followed an instruction written inside the customer's message.

Now look at version three, stored in its own file. It sets the role and the readers, and limits replies to eighty words. It never promises refunds, and says an agent will review the request. It asks one short question when unsure. It explains the tags, and gives one example.

Her code reads the prompt from the file, sends it as the system prompt, and wraps each customer message in the tags. Max tokens stays at three hundred. Because the prompt lives in a file, every change shows up in Git, with a clear version name.

She runs both versions on the same five test messages. You'll see something like this. Version three replies are shorter, never promise refunds, and ignore the instruction hidden in the customer's message.

Watch out for a common mistake. Many developers edit a prompt in production after one bad answer. The fix helps that case, but breaks three others that nobody checks. Keep the old version, and compare both on the same inputs before you switch.

Let's recap. First, a strong system prompt sets the role, task and audience, gives clear rules with reasons, and includes a few varied examples. Second, put user data inside clear tags, and tell the model to treat it as data. Third, prompts are code. Store them in version control, name each version, and compare versions on the same inputs.

Now it is your turn. In the exercise, you will improve a weak support prompt in three versions, run each one on the same five customer messages, and score the replies in a table. In the next lesson, Tokens, Context and Cost, you will see exactly what each call costs. See you there.
```

## L04 Tokens, Context and Cost

- **Filename:** `ai-14-building-apps-with-llm-apis_M1_L04_presenter.mp4`
- **Expected length:** about 4.9 minutes (682 words). The quality gate accepts ±10%.

```text
Two apps use the same model and answer the same number of questions each day. One costs ten times more than the other. The difference is not the model. It is how many tokens each app sends and receives.

In lesson two, you printed token counts. Now let's turn them into money. Every response includes a usage object. Input tokens are everything you sent, including the system prompt, the messages and any tool definitions. Output tokens are what the model wrote.

Prices are listed per million tokens, and output tokens usually cost more than input tokens. So the cost of one call is input tokens times the input price, plus output tokens times the output price, divided by one million. Prices differ by model and change, so check the current pricing page, and keep them in one place in your code.

You can also count tokens before you send. The API has a token-counting endpoint. You pass the same model, system prompt and messages, and it returns the input token count without writing a reply. Use it to check that a long document fits, or to warn a user before an expensive request.

Longer context costs more, and is usually slower. In a chat app, the history grows with every turn. So send only the parts of a document that matter, keep the last few turns of a long chat, and keep max tokens close to what you really need.

Think of a taxi meter that counts words instead of kilometres. It runs while you speak, and faster while the driver speaks. If you read a long letter aloud at the start of every ride, every ride is expensive, even when your question is short.

Languages matter too. A tokenizer splits text into pieces it saw often in training. So do not assume the same meaning costs the same in every language or script. Measure it for your own languages with the token counter.

Farida runs a language-learning app in Cairo, Egypt. Learners ask grammar questions in English or Arabic. She wants to know what each call costs, and how the two languages compare.

She writes a small helper. At the top are two price constants, copied from the pricing page. The helper reads the usage from each response, calculates the cost, and adds one row to a CSV file with the time, the feature, the model, both token counts and the cost.

Before sending, she counts the input tokens for the same grammar question, once in English and once in Arabic, with the same system prompt.

Then she sends both requests with the same max tokens, and logs them. You'll see something like two rows in the CSV file. She compares the token counts in the two rows. But one test is not enough, so she will measure a sample of real questions in each language before she sets prices for her premium plan.

She also notices something bigger. Her system prompt is six hundred tokens long, and it is sent with every call. She makes a note to try prompt caching in lesson thirteen.

A common mistake is to estimate cost from the user's question only. In a real app, most input tokens often come from things the user never sees. The system prompt, examples, the chat history and documents. Always log real usage, and calculate from that.

Let's recap. First, the cost of a call is input tokens times the input price, plus output tokens times the output price, using prices per million tokens from the live pricing page. Second, longer context means higher cost and slower replies, so send only what the model needs. Third, measure token counts for your own languages with the token counter.

Now it is your turn. In the exercise, you will write a helper that logs tokens and estimated cost for every call, then compare the same request in English and one other language. This logging will grow into your capstone cost dashboard. In the next lesson, Structured Outputs with JSON Schemas, your code will get data it can trust. See you there.
```

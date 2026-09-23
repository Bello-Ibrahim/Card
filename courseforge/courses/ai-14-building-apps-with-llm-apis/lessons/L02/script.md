# L02 Setup: API Keys, SDKs and a Low-Cost Budget | Presenter Script

Course: AI-14 · Video: 5 min · Words: 688

## Hook
An API key is like a credit card number for your code. If it leaks into a public repository, someone else can spend your money. Today you will make your first call, and you will set it up safely and cheaply from the first minute.

## Explain
In the last lesson, you saw what a request and a response look like. Now let's make a real one. First, one important fact. The Claude API is a paid service. You pay for every input and output token. Your costs can stay small, but only if you set limits before you start.

Setup has five steps. Create an account in the Claude Console and add a payment method. Set a monthly spend limit. Create an API key and copy it once. Store it in an environment variable, never in your code. Then install the official SDK. Before you sign up, check the current list of supported countries.

Keep keys out of Git. If you use a dot env file, add it to your git ignore file before your first commit. And if a key is ever committed, even for one minute, delete it in the Console and create a new one. Removing the file is not enough, because the key stays in the history.

Three habits keep costs low while you develop. Use a smaller, cheaper model for building and testing. Keep max tokens low, for example three hundred. And keep the model name in one constant, so you can change it in one place. Model names and prices change, so check the current models and pricing pages.

Think of a prepaid travel card that you give a teenager instead of your main bank card. It has a fixed limit, you can cancel it at any time, and a mistake cannot empty your account. The spend limit is that fixed limit. A new key is the replacement card.

## Demonstrate
Let's follow Mei Lin. She is a developer at a small travel start-up in Penang, Malaysia, and she is setting up her laptop.

In the Console, she opens the billing settings and sets a low monthly limit. Then she creates a key and gives it a clear name, so she always knows where it is used. She copies it once, because the Console will not show it again.

In her terminal, she saves the key in an environment variable. On Windows, the command looks a little different. Then she creates a virtual environment and installs the SDK.

Now she writes a short file for her first call. It sets the model in one constant, creates a client that reads the key automatically, asks for one day trip from Penang, and allows three hundred tokens. Then it prints the reply, the stop reason and the token counts.

She runs it. You'll see something like a suggestion for a day trip to Langkawi, then a stop reason of end turn, and a small number of input and output tokens. Then she lowers max tokens to twenty and runs it again. This time the reply is cut off, and the stop reason says max tokens.

Finally, she runs git status to check that no file with her key will be committed. A common mistake is to paste the key straight into the code just to test, and then commit it. Always use the environment variable, and replace any key that has been exposed.

## Recap
Let's recap. First, the Claude API is paid, so set a monthly spend limit before your first call. Second, keep your key in an environment variable, never in code or Git, and replace any key that leaks. Third, while developing, use a smaller model, a low max tokens value and one model constant, and look up model names and prices on the live pages.

## CTA
Now it is your turn. In the exercise, you will make your first API call and print the reply, the stop reason and the token counts. Then run it again with a tiny max tokens value and compare. In the next lesson, Prompt Design for Applications, you will learn to write prompts that work every time. See you there.

## Thumbnail
Headline: Your First Safe Call
Image: Navy background, a terminal window with a green reply line and a small padlock beside a key icon, headline in teal Inter Bold.

## Production Notes
- [VERSION] Record the Console steps (billing, spend limit, key creation), the SDK install command and the model choice against the live Console and docs on the recording day. Never show a model ID or price in the voiceover; blur or crop prices if the pricing page is shown.
- [VERIFY] Whether new accounts receive any trial credit is not stated in the voiceover; the script only tells learners to check the pricing pages.
- [REGION] [VERIFY] The API is offered directly only in supported countries, with cloud-provider alternatives. The voiceover only tells learners to check the current list; a reviewer must confirm the wording before publishing.
- Security: record with a throwaway key that is deleted right after recording. Blur the key in the Console and in the terminal at all times; the export command should show only a placeholder such as sk-ant-... on screen.
- Token counts in the demo output are illustrative; the voiceover says 'something like'.
- Mei Lin and the Penang travel start-up are fictional; the key name meilin-laptop-dev is an example.

# L05 Calling the Claude API from n8n | Presenter Script

Course: AI-16 · Video: 5 min · Words: 686

## Hook
Your workflow can already read and write a sheet. Now it gets a new ability: understanding language. One extra node lets it summarise, classify, or pull out information from every row.

## Explain
A quick reminder. An API request is a message to a server, with a method, an address, some headers and a body. The server sends back a response, usually in JSON.

To call Claude, you send a POST request to the Messages address. It has three headers: your secret API key, the API version from the documentation, and the content type.

The body names the model, sets a limit on output length, adds an optional system prompt, and holds the messages. For the model, check the current models page in the Claude documentation. Smaller, faster models are often enough for summaries.

The response gives you the text, the reason it stopped, and a usage section with input and output tokens. Tokens are what you pay for.

Here is a picture. Calling the API is like posting a form to a translation office. The envelope has an address, and stamps that prove who you are and which form version you use. Inside is the form itself. The office sends back the translation, with an invoice for how much work it did.

In n8n, you have two ways to make this call. The HTTP Request node lets you set the method, address, headers and body yourself. It shows exactly what is sent, so we use it today. There are also built-in Anthropic model nodes that hide these details. We use one with the AI Agent node later in the course.

The Claude API is a paid, usage-based service. So before you start, set a spending limit in the Claude Console. Keep test runs to a few rows, and always limit output length. Store your key in an n8n credential, never in a node. And use sample data, not personal or confidential data.

## Demonstrate
Let's build it. Mei-Lin Chen runs a tea shop in Taipei. Her reviews sheet has five invented reviews, with empty summary and tokens columns. First, she creates an API key in the Claude Console, and sets a monthly spending limit.

In n8n, she creates a header credential called Claude API, with the key as its value. Then she builds a manual trigger, and a Sheets node that gets rows from reviews.

Next, an HTTP Request node. She sets the method to POST, pastes the Messages address, and picks her Claude API credential. She adds the other two headers, and the body with her system prompt.

She runs it with a single row first. In the output, you'll see something like: the customer liked the oolong, but found the delivery slow. You also see the token usage.

Then she adds a Set node. It takes the summary text, adds the input and output tokens together, and keeps the review ID. Finally, a Sheets node updates the rows, matching on review ID. She removes the one-row limit and runs all five. Her sheet now has five summaries, and a token count for each row.

A common mistake is to test on the whole sheet first. If the prompt has an error, every row gets the wrong prompt, and you pay for every call. Test with one item, check it, then run the full set.

## Recap
Let's recap. First, a Claude API call is a POST request to the Messages address, with three headers and a body that holds the model, the output limit, the system prompt and the messages. Second, store the key in an n8n credential, and read the usage from the response. Third, the API is paid per use. Set a spending limit, limit output length, and test with one row first.

## CTA
Now it is your turn. In the exercise below this video, you will send five customer reviews to the Claude API, write a one-sentence summary of each back to your sheet, and record the tokens the run used. It takes about forty minutes. In the next lesson, we cover Structured Output: Getting JSON You Can Trust. See you there.

## Thumbnail
Headline: Add Claude to n8n
Image: Navy background, a sheet node connected to a teal API node with a speech-bubble icon, then back to the sheet with a new summary column, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude API: the anthropic-version header value, the request and response fields (content[0].text, stop_reason, usage), the current model IDs for the MODEL placeholder, the anthropic SDK call, and the Claude Console steps for API keys and spending limits must be checked against current documentation. No free tier is assumed and no prices are named in the voiceover.
- [VERSION] n8n: HTTP Request node options, Header Auth credential, Anthropic chat model node names and Edit Fields (Set) expressions must be checked against the current release.
- Screen recording: blur the API key everywhere (Console, credential form). The JSON body on screen keeps the literal MODEL placeholder or a current model ID; the voiceover never names a model ID or a price.
- The summary shown in the demo is an example output; the real output will differ. The optional Python SDK snippet stays on the lesson page, not in the video.
- Mei-Lin Chen and her Taipei tea shop are fictional; reviews are invented.

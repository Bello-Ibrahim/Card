# L14 Capstone Step 1: Build the Core Feature | Presenter Script

Course: AI-14 · Video: 5 min · Words: 681

## Hook
You now know every part. Prompts, structured outputs, streaming, tools and guardrails. In the next three lessons, you put them together into one small app that works, that others can use, and that shows what it costs.

## Explain
Welcome to the capstone. You will build a deployed web app with validated structured outputs, streaming, optional tool use, usage logging and a cost dashboard. This lesson is step one. Choose a use case, write a spec, and build the core feature.

Choose something small and useful. A good feature takes one kind of input, and returns structured data that the app then uses. For example, a job-advert analyser for a recruitment agency, a meal planner for a grocery app, or a tool that sorts support tickets. Avoid search over many documents, which is course AI-15, and long multi-step agents, which is AI-16.

Before any code, write a one-page spec. Who is the user, and what is the problem? What goes in, and what is the output schema? What is your prompt plan? Is there one tool that adds real data? What are your limits, such as model, max tokens and spend limit? And how will you know it works?

A spec is like a floor plan for a small house. It takes an hour, but it stops you from building a kitchen with no door. It also gives your reviewers a clear picture of what you planned.

Then build in layers. First the schema and a structured call, tested in the terminal. Then streaming for any free-text part. Then the Streamlit page. Then the tool, if you have one. Test each layer before you add the next, and commit each working layer to Git, so you can always go back.

## Demonstrate
Agnieszka Nowak builds a job-advert analyser for a recruitment agency in Kraków, Poland. Recruiters paste an advert, and get structured data plus a short streamed comment for the candidate.

Before any code, she writes her one-page spec. The users are recruiters. The input is one advert, and the output is a schema. Her limits are a small model, a low max tokens value and a spend limit, and she excludes any personal data. Success means five test adverts give correct fields.

Her schema has the job title, the seniority level, a list of required skills, an optional salary range and currency, and a list of red flags, such as no salary given.

Her core function sends the advert inside tags with the structured-output helper. It checks the stop reason, and returns a validated object. She tests it in the terminal first, before any page exists.

Then the page. The Streamlit app shows the structured fields, and then streams a short, plain-language comment built from that object, just like in lesson eight.

She tests five invented adverts, including one in Polish and one with no salary. For that one, you'll see something like an empty salary field, and no salary given in the red flags. A salary lookup tool stays optional. She adds it only after these tests pass, read-only, with the loop limits from lesson ten.

A common mistake is to start big, and build the page, the tool and the dashboard all at once. When something fails, you cannot tell which part broke. Keep it small, write the spec first, and test one layer at a time.

## Recap
Let's recap. First, choose a small use case that takes one kind of input and returns structured data your app uses. Second, write a one-page spec before coding, from the user and schema to limits and success. Third, build in layers. A validated structured call, then streaming, then the web page, then an optional tool with guardrails.

## CTA
Now it is your turn. This is capstone step one. Write your spec, and build the core feature with a validated schema and streaming output, then commit it to Git with no keys. In the next lesson, Capstone Step 2: Usage Logging and a Cost Dashboard, you will show what your app costs. See you there.

## Thumbnail
Headline: Spec First, Then Build
Image: Navy background, a one-page spec sheet beside a stack of four building blocks labelled schema, streaming, page, tool, headline in teal Inter Bold.

## Production Notes
- [VERSION] The structured-output helper (messages.parse, output_format, parsed_output) and Streamlit functions (st.json, st.write_stream) must be checked against the current docs before recording.
- The result for the advert with no salary (empty salary_min, 'no salary given' in red_flags) is example output; label it on screen.
- Agnieszka Nowak, the Kraków recruitment agency and all job adverts are invented. The Polish advert should be checked by a Polish speaker for natural wording before recording.
- Scope: retrieval over documents is AI-15 and multi-step agents are AI-16; the voiceover mentions both once.

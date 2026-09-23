# L08 A Web Front End with Streamlit or Next.js | Presenter Script

Course: AI-14 · Video: 5 min · Words: 672

## Hook
A script in your terminal is a prototype. A link that a colleague can open on their phone is a product. With about thirty lines of Python, you can turn your streaming code into a chat app on the web.

## Explain
In the last lesson, you streamed replies to the terminal. Now let's put them on a web page. Streamlit is a free, open-source Python library for small web apps. You write a normal Python script, and Streamlit turns it into a page. The same pattern in Next.js is in the course resources as extra code.

One idea explains most of Streamlit. The whole script runs again from the top every time the user does something, such as sending a message. Normal variables are reset on every run. To keep data between runs, you store it in session state, which lasts for the user's session.

Think of a waiter who forgets everything each time they walk back to the kitchen. Session state is the order pad in the waiter's pocket. Whatever is written there is still there on the next trip.

A chat app needs four features. Session state keeps the messages list, because the API is stateless. Chat message shows a bubble for the user or the assistant. Chat input shows a text box at the bottom. And write stream shows streamed text as it arrives, then returns the full reply.

On your computer, the key lives in an environment variable or a local secrets file. On a host, it goes into the host's secrets settings, never into the repository. Streamlit Community Cloud and Vercel both have free plans with limits, so check the current rules. And a public link means anyone can use your API credit. So keep max tokens low, keep your spend limit set, and consider a simple password or a message limit.

## Demonstrate
Amara Diallo runs a small tour company in Dakar, Senegal. She wants a chat assistant that answers visitors' questions about her tours.

Here is her app file. It sets the model in one constant and a short system prompt. The client reads the key from Streamlit secrets. If there is no history in session state yet, it creates an empty list. Then it shows every earlier message as a bubble.

When the visitor sends a message, the app adds it to the history and shows it. Then it streams the reply with the full history and a low max tokens value, shows it with write stream, and saves the reply back into the history.

She puts the key in a local secrets file, and adds the folder to git ignore. She installs Streamlit and runs the app. In the browser, she asks about a tour, then asks a follow-up. The assistant remembers.

A common mistake is to keep the chat history in a normal list at the top of the script. Streamlit reruns the script on every message, so the list is empty each time, and the assistant forgets everything. A second mistake is committing the secrets file. Always check git status before you push.

A common mistake is to keep the chat history in a normal list at the top of the script. Streamlit reruns the script on every message, so the list is empty each time, and the assistant forgets everything.

## Recap
Let's recap. First, Streamlit reruns the whole script on every user action, so keep the chat history in session state. Second, a chat app needs a chat input, message bubbles, streamed output, and the history sent with each request. Third, keep keys in the host's secrets settings, not in the repository, and protect your budget when the link is public.

## CTA
Now it is your turn. In the exercise, you will build and deploy a small streaming chat app with your own system prompt, and share the link with a classmate. Your capstone will use this same front end. In the next lesson, Tool Use: Letting the Model Call Your Functions, your app starts to take real actions. See you there.

## Thumbnail
Headline: From Script to Link
Image: Navy background, a terminal window turning into a phone showing a chat app, headline in teal Inter Bold.

## Production Notes
- [VERSION] Streamlit functions (st.chat_input, st.chat_message, st.write_stream, st.session_state, st.secrets) and the deployment steps and free plans of Streamlit Community Cloud and Vercel must be checked at recording time.
- The video shows only the Python and Streamlit path. The Next.js version is extra code in the course resources and is only mentioned.
- Security: blur the key in secrets.toml and in the Streamlit Community Cloud secrets box. Use a throwaway key with a low spend limit and delete it after recording; take the demo app down or protect it after recording.
- Amara Diallo and Teranga Tours in Dakar are invented; no real tour company brand on screen. Stock footage: no readable business names.

# L08 A Web Front End with Streamlit or Next.js

Course: AI-14 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
A script in your terminal is a prototype. A link that a colleague can open on their phone is a product. With about 30 lines of Python, you can turn your streaming code into a chat app on the web.

## Explanation
**Streamlit** is a free, open-source Python library for small web apps. You write a normal Python script, and Streamlit turns it into a page. It is the main path in this course. The same pattern in **Next.js** (TypeScript) is in the course resources as extra code.

One idea explains most Streamlit behaviour: **the whole script runs again from the top every time the user does something**, such as sending a message. Ordinary variables are reset on every run. To keep data between runs, you store it in `st.session_state`, a dictionary that lasts for the user's session.

A chat app needs four Streamlit features. Function names change between versions, so check the current API reference. [VERSION]

- `st.session_state` to keep the messages list (L01: the API is stateless, so your app holds the history).
- `st.chat_message(role)` to show a message bubble for the user or the assistant.
- `st.chat_input()` to show a text box at the bottom of the page. It returns the text when the user sends a message.
- `st.write_stream()` to show text from a generator as it arrives, and return the full text at the end.

**Keys in hosted apps.** On your computer, you use an environment variable. On a hosting service, you use the host's **secrets** settings. In Streamlit, secrets are stored in `.streamlit/secrets.toml` locally (add it to `.gitignore`) and in the app settings on the host. Values can be read with `st.secrets`. [VERSION]

**Free hosting.** Streamlit Community Cloud can host public Streamlit apps from a GitHub repository, and Vercel can host Next.js apps. Both have free plans with limits. Check the current plans and rules. [VERSION]

**Protect your budget.** A public link means anyone can use your API credit. Keep max_tokens low, keep your spend limit set, and consider a simple password or a per-session message limit.

**Analogy:** A Streamlit script is like a waiter who forgets everything each time they walk back to the kitchen. `st.session_state` is the order pad in the waiter's pocket: whatever is written there is still there on the next trip.

## Worked Example
Amara Diallo runs a small tour company in Dakar, Senegal. She wants a chat assistant that answers visitors' questions about her tours. She creates `app.py`:

```python
import anthropic
import streamlit as st

MODEL = "your-small-model-id"  # check the current models page [VERSION]
SYSTEM = "You answer questions about Teranga Tours in Dakar. Be brief."

client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
st.title("Teranga Tours assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Ask about our tours"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    def reply_stream():
        with client.messages.stream(model=MODEL, max_tokens=400, system=SYSTEM,
                                    messages=st.session_state.messages) as s:
            yield from s.text_stream

    with st.chat_message("assistant"):
        reply = st.write_stream(reply_stream())
    st.session_state.messages.append({"role": "assistant", "content": reply})
```

On screen, she follows these steps:

1. Creates `.streamlit/secrets.toml` with `ANTHROPIC_API_KEY = "..."` and adds the folder to `.gitignore`.
2. Runs `pip install streamlit anthropic` and `streamlit run app.py`, and tests two questions in the browser.
3. Adds `requirements.txt` with `streamlit` and `anthropic`, and pushes the code (without secrets) to GitHub.
4. In Streamlit Community Cloud, creates a new app from the repository, pastes the key into the app's secrets settings and deploys. [VERSION]
5. Opens the public link on her phone and sends a test message.

## Common Mistake
Many developers store the chat history in a normal Python list at the top of the script. Because Streamlit reruns the script on every message, the list is empty each time, and the assistant forgets the conversation. Keep the history in `st.session_state`. A second common error is committing `secrets.toml`: check `git status` before you push.

## Key Takeaways
1. Streamlit reruns the whole script on every user action, so keep the chat history in `st.session_state`.
2. A chat app needs a chat input, message bubbles, streamed output and the history sent with each request.
3. Keep keys in the host's secrets settings, not in the repository, and protect your budget when the link is public.

## Hands-on Exercise
**Task:** Build and deploy a small streaming chat app with a system prompt, and share the link with a classmate.
**Tools:** Python with `streamlit` and `anthropic`; a free GitHub account; Streamlit Community Cloud (free plan) [VERSION]; optional Next.js starter code in the course resources, deployed to Vercel.
**Steps:**
1. Choose a topic for your assistant and write a short system prompt.
2. Copy the worked example into `app.py` and change the title and system prompt.
3. Create `.streamlit/secrets.toml` with your key, and add `.streamlit/` to `.gitignore`.
4. Run the app locally and test a 3-message conversation that depends on earlier messages.
5. Add `requirements.txt`, push to GitHub, and check that no secret file was pushed.
6. Deploy on Streamlit Community Cloud and add the key in the app's secrets settings. [VERSION]
7. Share the link with a classmate. Ask them not to enter personal or confidential data.
**What good looks like:** A public link that streams replies, remembers earlier messages in the conversation, follows your system prompt and has no key in the repository.
**Time:** about 45 minutes

## Review Flags
- [VERSION] Streamlit functions (`st.chat_input`, `st.chat_message`, `st.write_stream`, `st.session_state`, `st.secrets`) and the deployment steps and free plans of Streamlit Community Cloud and Vercel must be checked at recording time.
- The business in the worked example is invented.

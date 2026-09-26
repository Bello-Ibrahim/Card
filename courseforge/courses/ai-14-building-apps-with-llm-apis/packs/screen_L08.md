# Screen Demo Pack: AI-14 L08 A Web Front End with Streamlit or Next.js

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L08_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open app.py in VS Code
2. Highlight MODEL and SYSTEM constants
3. Highlight anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
4. Highlight the check that creates st.session_state.messages
5. Highlight the loop that draws each message with st.chat_message

**Narration over this clip (for pacing)**

> Here is her app file. It sets the model in one constant and a short system prompt. The client reads the key from Streamlit secrets. If there is no history in session state yet, it creates an empty list. Then it shows every earlier message as a bubble.

## Clip 2: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L08_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Highlight st.chat_input("Ask about our tours")
2. Highlight appending the user message to st.session_state.messages
3. Highlight reply_stream() with messages.stream, max_tokens=400 and the full history
4. Highlight reply = st.write_stream(reply_stream()) and appending the assistant reply

**Narration over this clip (for pacing)**

> When the visitor sends a message, the app adds it to the history and shows it. Then it streams the reply with the full history and a low max tokens value, shows it with write stream, and saves the reply back into the history.

## Clip 3: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L08_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Create .streamlit/secrets.toml with ANTHROPIC_API_KEY = "..." (value blurred)
2. Add .streamlit/ to .gitignore
3. Run pip install streamlit anthropic, then streamlit run app.py
4. In the browser, ask about a tour, then ask a follow-up that uses 'it'
5. Show the streamed reply that understands the follow-up

**Narration over this clip (for pacing)**

> She puts the key in a local secrets file, and adds the folder to git ignore. She installs Streamlit and runs the app. In the browser, she asks about a tour, then asks a follow-up. The assistant remembers.

## Clip 4: scene 12

- **Filename:** `ai-14-building-apps-with-llm-apis_L08_screen_4.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Create requirements.txt with streamlit and anthropic
2. Run git status and show no secrets.toml, then push to GitHub
3. In Streamlit Community Cloud, create a new app from the repository
4. Paste the key into the app's secrets settings (blurred) and deploy
5. Open the public link on a phone and send a test message

**Narration over this clip (for pacing)**

> A common mistake is to keep the chat history in a normal list at the top of the script. Streamlit reruns the script on every message, so the list is empty each time, and the assistant forgets everything. A second mistake is committing the secrets file. Always check git status before you push.

## Production notes for this lesson

- [VERSION] Streamlit functions (st.chat_input, st.chat_message, st.write_stream, st.session_state, st.secrets) and the deployment steps and free plans of Streamlit Community Cloud and Vercel must be checked at recording time.
- The video shows only the Python and Streamlit path. The Next.js version is extra code in the course resources and is only mentioned.
- Security: blur the key in secrets.toml and in the Streamlit Community Cloud secrets box. Use a throwaway key with a low spend limit and delete it after recording; take the demo app down or protect it after recording.
- Amara Diallo and Teranga Tours in Dakar are invented; no real tour company brand on screen. Stock footage: no readable business names.

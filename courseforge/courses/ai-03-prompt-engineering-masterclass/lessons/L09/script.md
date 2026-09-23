# L09 Roles and Multi-Turn Conversations | Presenter Script

Course: AI-03 · Video: 5 min · Words: 702

## Hook
You do not have to get everything right in one message. Some of the best results come from a conversation: a clear role, a few questions, and a result built in steps. Today, I will show you how.

## Explain
In the last lesson, you asked the AI to show its reasoning. Now we add two more tools: roles, and conversations with several turns.

A role gives the AI a point of view, and it often changes what the tool pays attention to. Act as a strict editor gives you critical feedback, not praise. Act as a first-time customer helps you find confusing steps. But a role changes the angle, not the knowledge, so you still check the facts.

In a chat, the tool can use the earlier messages in the same conversation. So you can build a result in steps. Ask for an outline, correct it, ask for the full draft, then ask for changes to one section.

One very useful pattern is the interview. You say: before you write anything, ask me five questions, one at a time. The tool asks for the context it needs, and you answer.

Long conversations have limits. The tool may give less attention to instructions from much earlier, and a very long chat may reach a length limit. If the results start to drift, open a new chat and paste a short summary of what you agreed.

Think of working with an architect. You do not describe the whole house in one sentence. You discuss your needs, they ask questions, they show a sketch, you correct it, and the plan grows from that exchange.

## Demonstrate
Let's see it live. Mateo is a training coordinator at a construction company in Bogotá. He needs a one-page safety briefing for new site workers. His single-message prompt gave a long, general text. So now he tries a conversation.

I open Claude in a web browser and start a new chat. I type a role, an experienced safety trainer for construction sites, then the task, a one-page briefing for new workers. And then the key line: before you write anything, ask me five questions, one at a time.

The first question appears, for example, what type of site is this? I answer briefly: a six-storey residential building with a concrete frame. Then I answer the other four questions in the same way. Notice that each question asks for context Mateo might have forgotten.

After the fifth answer, the tool writes the briefing. As I scroll through it, you can see it is specific to Mateo's site, not a general text about safety.

Now I change the role. I type: now act as a strict editor, and list the three least clear sentences for a worker who reads slowly. The tool points them out. Then I ask it to rewrite those three sentences in simpler words.

Finally, saved instructions. Many tools let you save context that applies to future chats, so you do not repeat it. I open the settings and type an example: I work in construction training, write in plain language for adult learners.

Other tools have similar features, but the names and limits differ between tools and plans. And never put confidential information in saved instructions.

A common mistake is to think a role like world-class lawyer makes the answer legally reliable. It does not. For law, health, safety or finance, a qualified person must still check the content.

## Recap
Let's recap. First, a role gives the AI a point of view, such as a strict editor or a first-time customer. It changes the angle, not the knowledge. Second, conversations let you build a result in steps, and the interview pattern helps the tool ask for the context it needs. Third, saved instructions can reduce repetition, but their names and limits differ, and they must not contain confidential information.

## CTA
Now it is your turn. In the exercise below this video, you will ask the AI to interview you with five questions before it writes anything. Then you compare the result with a single-message prompt. It takes about twenty-five minutes. In the next lesson, we look at fixing weak outputs. See you there.

## Thumbnail
Headline: Let the AI Interview You
Image: Navy background, a chat window with five short question bubbles from the AI and short answers from the user, headline in teal Inter Bold.

## Production Notes
- SCREEN DEMO lesson. Record scenes 9 to 14 as a live screen capture in Claude (web browser, free tier), following the screen_steps. Rehearse every step in the live tool first. [VERSION]
- [VERSION] Names, availability and limits of saved-instruction features (custom instructions, projects and similar) on the free plans of Claude, ChatGPT and Gemini, and where they appear in each interface, must be checked before recording. The voiceover deliberately avoids naming the menu items; the screen shows whatever the live tool uses. If a feature is not available on a free plan, cut scene 14's ChatGPT and Gemini step and say only that other tools have similar features.
- [VERSION] Conversation length limits and how each tool handles very long chats must be checked. The voiceover says only that a very long chat 'may' reach a limit.
- The AI's five questions will differ from run to run. The voiceover names only the first example question from content.md; keep it general if the live tool asks something different.
- Mateo and his construction company in Bogotá are hypothetical. Use only the invented site details from content.md; no real company or site names on screen.
- Roles are presented as changing the angle, not the knowledge; for law, health, safety or finance a qualified person must check the content.

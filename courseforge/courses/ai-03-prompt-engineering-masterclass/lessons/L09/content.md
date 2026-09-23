# L09 Roles and Multi-Turn Conversations

Course: AI-03 · Module: M2 · Objectives: O3, O4 · Video: 5 min (screen demo)

## Hook
You do not have to get everything right in one message. Some of the best results come from a conversation: a clear role, a few questions, and a result built in steps.

## Explanation
**Roles.** A role gives the AI a point of view. It often changes what the tool pays attention to:

- "Act as a strict editor. Point out every unclear sentence." gives critical feedback, not praise.
- "Act as a first-time customer who has never used our service." helps you find confusing steps.
- "Act as an experienced trainer for adult learners." shapes the tone and structure of a training plan.

A role does not give the tool real expertise or access to new information. It changes the angle, not the knowledge. Use roles that describe a point of view, and still check the facts.

**Multi-turn conversations.** In a chat, the tool can use the earlier messages in the same conversation. This lets you build a result in steps:

1. Ask for an outline.
2. Correct the outline.
3. Ask for the full draft.
4. Ask for changes to one section.

A very useful pattern is the **interview**: "Before you write anything, ask me five questions about this task, one at a time." The tool asks for the context it needs, and you answer. This is helpful when you are not sure what to include.

Long conversations have limits. The tool may give less attention to instructions from much earlier, and a very long chat may reach a length limit. [VERSION] If results start to drift, start a new chat and paste a short summary of what you agreed.

**Saved instructions.** Many tools let you save instructions that apply to every chat or to a group of chats, so you do not repeat the same context. These features have different names, such as custom instructions or projects, and their availability and limits differ between tools and plans. [VERSION] Do not put confidential information in saved instructions.

**Analogy:** A multi-turn conversation is like working with an architect. You do not describe the whole house in one sentence. You discuss your needs, they ask questions, they show a sketch, you correct it, and the final plan grows from that exchange.

## Worked Example
Mateo is a training coordinator at a hypothetical construction company in Bogotá. He needs a one-page safety briefing for new site workers.

**Screen demo steps for the presenter** (check each step in the live tool first [VERSION]):

1. Open Claude in a web browser and start a new chat.
2. Type the interview prompt:

```text
Act as an experienced safety trainer for construction sites.
I need a one-page safety briefing for new site workers.
Before you write anything, ask me five questions, one at a time,
about what you need to know.
```

3. Show the first question on screen, for example "What type of site is this?" Type a short answer: "A 6-storey residential building, concrete frame."
4. Answer the other four questions in the same way (audience, main risks, rules already in place, format). Point out that each answer adds context Mateo would probably have forgotten.
5. After the five answers, the tool writes the briefing. Scroll through it on screen.
6. Type a follow-up: "Now act as a strict editor. List the three least clear sentences for a worker who reads slowly." Show the feedback.
7. Type: "Rewrite those three sentences in simpler words." Show the improved briefing.
8. Open the tool's settings area and show where saved or custom instructions are entered. [VERSION] Type an example such as "I work in construction training. Write in plain language for adult learners." Explain that it will apply to future chats.
9. Briefly show where a similar feature is found in ChatGPT and Gemini, if available on free plans. [VERSION]

For comparison, Mateo's earlier single-message prompt, "Write a safety briefing for new construction workers", gave a long, general text. The interview version was shorter, specific to his site and ready for review by the site manager.

## Common Mistake
Many learners think a role like "You are a world-class lawyer" makes the answer legally reliable. It does not. The tool has the same knowledge with or without the role. Roles change the point of view and style. For expert topics, such as law, health, safety or finance, a qualified person must still check the content.

## Key Takeaways
1. A role gives the AI a point of view, such as a strict editor or a first-time customer. It changes the angle, not the knowledge.
2. Multi-turn conversations let you build a result in steps, and the interview pattern helps the tool ask for the context it needs.
3. Saved instructions can reduce repetition, but their names and limits differ between tools, and they must not contain confidential information.

## Hands-on Exercise
**Task:** Ask the AI to interview you with five questions about a task before it writes anything, then compare the result with a single-message prompt.
**Tools:** Claude, ChatGPT or Gemini (free tier) [VERSION]; a notes app.
**Steps:**
1. Choose a real, non-confidential task, such as a training plan, a process guide or an event checklist.
2. In a new chat, send a single-message prompt: one or two sentences describing the task. Save the answer.
3. Start another new chat. Give a role and use the interview prompt from this lesson.
4. Answer all five questions. Use placeholders for any names or confidential details.
5. Save the final answer and ask one follow-up with a different role, such as "strict editor".
6. Compare the two final outputs and write three bullet points: what improved, which question was most useful, and what you would add to the single-message prompt next time.
**What good looks like:** Two saved outputs, the five questions with your answers, and three specific comparison points.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Names, availability and limits of custom instructions, projects and similar saved-instruction features on free plans of Claude, ChatGPT and Gemini must be checked before scripting, including where they appear in each interface.
- [VERSION] Conversation length limits and how each tool handles very long chats must be checked before scripting.
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini, and every screen demo step, must be checked in the live tools before recording.

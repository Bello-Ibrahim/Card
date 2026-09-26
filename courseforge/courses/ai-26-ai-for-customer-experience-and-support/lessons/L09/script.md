# L09 Build Your Support Assistant | Presenter Script

Course: AI-26 · Video: 5 min · Words: 701

## Hook
You have a clean knowledge base, a tone guide and hand-off rules. This week you combine them into a working support assistant. And here is the secret. A good first version is not clever. It is small, and it is honest.

## Explain
Welcome to week three, where you build your capstone, a support assistant with a hand-off to a human. In this lesson, we set up the assistant itself. You can use any free chatbot builder. I will use Botpress. Every builder asks you to make four decisions.

The first decision is scope. Choose three to five frequent, low-risk topics from the list you made in lesson one, such as opening hours, order tracking and returns. Everything else is out of scope, and goes to a person.

The second is knowledge. Add the clean articles you wrote in lesson three, only for your scope. And never upload real customer data or confidential documents to a free tool.

The third is instructions. Write short, clear rules. Answer only questions about your topics. Use only the knowledge base, and if the answer is not there, say you are not sure and offer a person. Follow the tone guide. Never promise refunds, discounts or dates that are not in the knowledge base.

And one more instruction, the most important. If the customer asks for a person, is very upset, or mentions a legal or safety issue, offer a person at once. These are your hand-off rules from lesson seven.

The fourth decision is transparency. Tell customers they are talking to AI, right in the welcome message, and tell them they can ask for a person at any time. It builds trust. Your region may also have its own rules, which we look at in lesson twelve.

Think of opening a small food stall before a full restaurant. You serve a few dishes you make well, you show the menu clearly, and you point people next door for anything else.

## Demonstrate
Let's build one. Leila works at a hypothetical language school in Amman, Jordan. Her assistant covers three topics: course start dates, choosing a level, and payment methods.

I sign in to the free plan and create a new bot. I name it Noor, language school assistant, test. Then, in the knowledge section, I add three short articles: when do courses start, how do I choose my level, and how can I pay. I paste the text instead of uploading big files.

Next, the instructions. I paste the scope, the knowledge only rule, the tone guide and the hand-off rules. Then the welcome message: hello, I am Noor, the school's AI assistant. I can help with course dates, levels and payment. You can ask for a person at any time.

Now I test in the preview chat. I ask one question for each topic, and check each answer against the articles. Then an out-of-scope question: can you help with my visa? Noor should say it is not sure, and offer a person.

But Noor gives general visa advice. So Leila adds an instruction: do not give advice on visas or legal matters, offer a person. The retest passes. Then I ask the next course date in Arabic, and check both the answer and the tone.

Finally, I publish the bot in test mode only, and copy its share link for testing.

A common mistake is to add every document you have, hoping the assistant will answer everything. Old or overlapping content gives it more chances to find the wrong text. Start small, and add topics only when the current ones work.

## Recap
Let's recap. First, every chatbot builder asks for four decisions: scope, knowledge, instructions and transparency. Second, start with three to five frequent, low-risk topics and clean content. Third, tell customers they are talking to AI, and that they can ask for a person at any time.

## CTA
This is capstone step one. In the exercise, you will build your own assistant for at least three topics, with an honest welcome message, and test it with one out-of-scope question. Take screenshots for your capstone. In the next lesson, we are adding the hand-off flow. See you there.

## Thumbnail
Headline: Small and Honest Wins
Image: Navy background, a friendly chat window with a small 'AI assistant' badge and a clear 'Talk to a person' button, headline in teal Inter Bold.

## Production Notes
- Screen demo lesson: record scenes 10 to 14 live in Botpress (free plan), the chatbot builder chosen in DECISIONS.md; content.md says 'a free chatbot builder of your choice', and the voiceover tells learners any free builder works. The screen_steps are content.md's step list adapted to Botpress.
- [VERSION] Botpress interface names in the screen_steps ('Create Bot', 'Knowledge Bases', 'Add source', 'Instructions', welcome message setting, 'Emulator' test chat, 'Publish' and share link) must be checked in the live tool on the recording day; update the steps if they differ.
- [VERSION] Free-plan limits of Botpress (number of bots, messages, knowledge size) and its data-use terms. Upload only the three made-up articles; paste text rather than uploading large files.
- [REGION] [VERIFY] Rules requiring customers to be told they are talking to AI (for example the EU AI Act transparency obligations) and local data protection laws. The voiceover treats AI disclosure and data protection as principles only and states no legal detail; L12 returns to this.
- NATIVE-SPEAKER CHECK NEEDED: the Arabic sample question in scene 13 (متى تبدأ الدورة القادمة؟, 'When does the next course start?') must be checked by a native Arabic speaker before recording, together with the Arabic answer Noor gives on screen.
- Leila, the Amman language school and the assistant 'Noor' are fictional. Name the bot 'Noor – Language school assistant (test)' and keep it in test mode.
- Kestrel Bikes is the made-up company from the L03 exercise; the instructions slide quotes its example rules from content.md.

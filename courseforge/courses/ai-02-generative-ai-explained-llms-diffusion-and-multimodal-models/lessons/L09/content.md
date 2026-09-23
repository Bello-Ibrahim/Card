# L09 Matching the Task to the Model

Course: AI-02 · Module: M3 · Objectives: O6 · Video: 5 min

## Hook
You now know three families of generative AI and where each one fails. But on a busy Monday morning, with a real task in front of you, which one should you open? A few simple questions can guide the choice.

## Explanation
Choosing a tool is not about finding "the best AI". It is about matching the task to the right **type of model**, and then choosing a tool that fits your limits. Use these five questions in order.

**1. What type of output do I need?** Text, an image, a table from a photo, a transcript from audio? The output points to the family: text work suits a language model, new images suit a diffusion or other image model, and reading images or audio needs a multimodal model (L01).

**2. How accurate must it be?** A brainstorm of slogan ideas can include weak ideas. A price table, a legal summary or a medical instruction cannot include errors. The higher the need for accuracy, the more you must give the model a source, lower the temperature where possible and check the result (L02, L04).

**3. Is the input private or confidential?** Customer data, health records, contracts and unpublished plans should not go into a free public tool. Check the tool's privacy terms and your organisation's rules. Sometimes the right choice is to remove personal details, to use an approved company tool, or not to use AI for that task at all. Data protection rules differ between countries. [REGION]

**4. What will it cost?** Consider money (free tier, paid plan, usage limits), time (writing prompts and fixing output) and effort. A free tool with daily limits may be enough for occasional use but not for a whole team. [VERSION]

**5. Who checks the result?** Every important output needs a human reviewer who knows the subject. If nobody can check it, the task may be too risky for AI.

The answers help you choose a model type, a tool and a **risk to watch**, based on the typical failures in L08.

**Analogy:** Choosing a model is like choosing transport for a journey. A bicycle, a bus and a lorry are all useful, but for different trips. You think about what you are carrying, how fast and safely it must arrive, how much you can spend and who will check that it arrived. Nobody asks "which vehicle is best?" without knowing the journey.

## Worked Example
Three hypothetical professionals use the questions.

**Nour, a translator in Cairo, Egypt,** must translate a short tourism brochure from Arabic into English. Output: text, so a **language model**. Accuracy: high, because it will be printed. Privacy: the brochure is public, so a free tool is acceptable. Check: Nour reviews every sentence herself. Risk to watch: the model may add details that are not in the original or translate place names wrongly.

**Carmela, a secondary school teacher in Manila, the Philippines,** wants to turn a photo of a handwritten class timetable into a clean digital table. Output: a table from an image, so a **multimodal model**. Privacy: she removes student names from the photo first. Accuracy: high, because students depend on it. Risk to watch: misread times, such as 1:00 read as 7:00.

**Thiago's marketing team in São Paulo, Brazil,** needs ten background images for a campaign about a new juice brand. Output: images, so a **diffusion or other image model**. Accuracy: medium; style matters more than facts. Cost: they may need a paid plan with commercial usage rights. [VERSION] Risk to watch: text inside images and people who all look the same (bias). The designer adds the brand name later and reviews each image.

Each person chose a different model type because each task was different.

## Common Mistake
Many learners choose a tool first ("I always use this chatbot") and then force every task into it. This can lead to weak results, such as asking a text-only chat for an image, or to real risks, such as pasting confidential data into a free tool. The correction is to start from the task: output type, accuracy, privacy, cost and checking. Then choose the model type and tool.

## Key Takeaways
1. Start from the task, not the tool: the type of output you need points to the model family.
2. Accuracy needs, privacy, cost and the person who checks the result decide which tool is suitable, or whether to use AI at all.
3. For every choice, name one risk to watch, based on the typical failures of that model family.

## Hands-on Exercise
**Task:** Complete a decision table for six workplace tasks: choose the model type, name one suitable free tool and write one risk to watch.
**Tools:** The decision table template on the course page, or a spreadsheet; Claude or ChatGPT free tier, Google AI Studio and a free image generator of your choice as possible answers [VERSION].
**Steps:**
1. Create a table with the columns: Task, Output type, Model type, Free tool, Privacy concern, Risk to watch.
2. Add these six tasks: (a) summarise a public 20-page report; (b) create an illustration for a newsletter; (c) turn a photo of a whiteboard into meeting notes; (d) draft a polite reply to a supplier; (e) write a transcript of a recorded interview; (f) analyse a spreadsheet of customer complaints that includes names and phone numbers.
3. Fill in every column for each task.
4. For task (f), decide what must happen before any AI tool is used.
**What good looks like:** A complete table in which the model type matches the output, each risk links to a typical failure (for example "misread handwriting" for task c), and task (f) says personal data must be removed or an approved tool used, or that AI should not be used.
**Time:** about 20 minutes

## Review Flags
- [REGION] Data protection rules for putting personal or confidential data into AI tools differ between countries and organisations; the lesson stays general on purpose.
- [VERSION] Free tier limits, paid plans and commercial usage rights for generated images change often; a reviewer should confirm the suggested free tools.

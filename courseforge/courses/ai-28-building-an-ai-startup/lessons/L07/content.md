# L07 Building with No-Code Tools

Course: AI-28 · Module: M2 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
Can you build a working AI product without writing code? In this lesson you will watch a prototype being built from start to finish, and then build your own.

## Explanation
A **no-code builder** is a tool where you build apps or websites by choosing and connecting blocks on screen instead of writing code. Most no-code prototypes use four parts:

- **Form (input):** where the user enters information or uploads a file.
- **Database (storage):** a table that saves each request and result, like a spreadsheet.
- **AI step (processing):** a block that sends the user's input, plus your instructions, to an AI model and receives the answer.
- **Output page:** where the user sees the result.

The AI step is powered by a **prompt**: the instructions you give the model. In a product, the prompt runs every time a user presses the button, so it is part of your product. Write it carefully and save each version.

Some builders include their own AI step. Others ask you to connect an AI provider, such as Claude, with an **API key**. An API key is a secret password that lets one program use another, and its use may be charged per request. Keep API keys private and never paste them into shared documents. Features and free-plan limits of no-code builders change often, so check them on the day you build [VERSION].

If your builder's free plan cannot run an AI step, you can still test the flow: collect inputs with the form, produce the result yourself with Claude, and send it back. This is the Wizard of Oz test from L04.

**Analogy:** A no-code builder is like construction toy bricks. You cannot make every shape, but you can build a working model of a house quickly and show it to people before you pour concrete.

## Worked Example
Sipho is a hypothetical founder in Durban, South Africa. His interviews showed that small plumbing businesses lose jobs because they send price quotes too slowly. His core job: "A plumber enters job details and gets a clear, professional quote to send to the customer."

The presenter follows these on-screen steps. Button and menu names differ between builders and change over time [VERSION].

1. **Draft the prompt with Claude.** In Claude, type: "Help me write instructions for an AI step that turns a plumber's short job notes into a clear, polite price quote. Use only the prices the plumber enters. Never invent prices. If information is missing, list what is missing." Copy the result into a document and label it "Prompt v1".
2. **Create a new project** in the no-code builder of your choice, using a blank template [VERSION].
3. **Add a data table** called "Quotes" with fields: job description, materials and prices, labour hours, hourly rate, quote text and status.
4. **Add a form** linked to the table, with the first four fields. Mark all four as required.
5. **Add an AI step** that runs when the form is submitted [VERSION]. Paste Prompt v1 and insert the form fields where the builder allows, for example "Job notes: {job description}".
6. **Save the AI answer** into the "quote text" field, and set the status to "draft".
7. **Add an output page** that shows the quote text and a button to copy it.
8. **Test with fake data:** "Replace kitchen tap, tap 450, labour 1 hour at 350". Check that the quote uses only these numbers. Do not use real customer names or addresses.
9. **Test a missing field:** remove the hourly rate in the prompt input and check that the quote asks for it instead of inventing it.
10. **Share the preview link** with one test user and watch them complete the task without help.

On his first test, the AI added a "call-out fee" that Sipho never entered. He edited the prompt ("Do not add any fee that is not listed") and saved it as Prompt v2.

## Common Mistake
Many founders spend days on colours, logos and extra pages before the core flow works, and never test the AI step with difficult inputs. Build the core flow from start to finish first, even if it looks plain, then test it with difficult inputs. A plain prototype that works teaches you more than a beautiful one that breaks.

## Key Takeaways
1. A no-code prototype usually connects a form, a database, an AI step and an output page.
2. The prompt is part of your product: write it carefully, test it, and save each version.
3. Build and test the core flow from start to finish before adding anything else.

## Hands-on Exercise
**Task:** Build a working prototype of your core flow with a free no-code builder and Claude, so that a user can complete the main task from start to finish.
**Tools:** A free no-code app builder of your choice [VERSION]; Claude (free plan) to draft and improve your prompt; a document for saving prompt versions.
**Steps:**
1. Using your core job from L06, ask Claude to help you write Prompt v1, including what to do when information is missing.
2. Create a project, a data table and a form with only the fields your core job needs.
3. Add the AI step (or, if your free plan does not allow it, a manual Wizard of Oz step using Claude) [VERSION].
4. Show the result on an output page.
5. Test the flow three times with fake data, including one input with missing information.
6. Update the prompt after each problem and save each version.
7. Ask one person from your target group to complete the task while you watch silently. Write down where they get stuck.
**What good looks like:** A user can go from input to result without your help. The prompt is saved with at least two versions, and you have notes from one real user test.
**Time:** about 60 minutes

## Review Flags
- [VERSION] The brief does not name a no-code builder. A reviewer must choose one with a usable free plan and confirm the names of its project templates, data tables, forms, AI steps and preview links before recording; steps 2 to 10 must be updated to match.
- [VERSION] Whether the chosen builder's free plan includes an AI step, and whether connecting Claude needs a paid API key, must be checked on the day of recording.
- [VERSION] Claude free-plan limits and data-use terms should be checked before recording.

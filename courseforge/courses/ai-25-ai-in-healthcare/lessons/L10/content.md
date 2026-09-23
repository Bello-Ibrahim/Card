# L10 Patient Safety and Failure Modes

Course: AI-25 · Module: M2 · Objectives: O4, O5 · Video: 5 min

## Hook
Most harm from AI in healthcare will not look dramatic. It will look like a busy nurse accepting a suggestion without checking, an alert that nobody reads anymore, or a tool that stopped working last Tuesday and nobody noticed. This lesson is about those quiet failures.

## Explanation
A tool can be accurate in a study and still cause harm in daily work. Four failure modes are especially common.

1. **Automation bias.** People tend to trust a tool's output too much, especially when they are tired or busy. They may accept a wrong suggestion, or stop looking for problems the tool does not flag.
2. **Alert fatigue.** When a tool raises many alerts, most of them false (remember low PPV from L04), staff begin to ignore or dismiss them quickly, including the true ones.
3. **Silent failure.** The tool stops working or starts performing worse without any visible sign. Causes include a software update, a new device that changes the input, a broken data connection, or dataset shift (L09). The screen still shows results, but they are wrong or missing.
4. **Workflow gaps.** The tool's output arrives in the wrong place, at the wrong time or to the wrong person. For example, an alert goes to a shared inbox that nobody checks at night.

Two approaches reduce harm:

- **Human factors design.** Design the tool and the workflow around how people actually work: show uncertainty, make it easy to disagree with the tool, limit alerts to those that need action, send outputs to a named role, and never let the tool's output replace an essential step such as reading the image.
- **Incident reporting and monitoring.** Staff report problems and near misses through the organisation's normal safety reporting system, and a named group reviews them. The team monitors performance and use over time, not only at launch.

A useful tool for planning is a **failure mode table**. For each part of the process, you ask: what can go wrong, what is the effect, how would we detect it, and how can we prevent it or reduce the harm?

**Analogy:** Aircraft autopilot flies much of a modern flight, yet pilots are still trained to monitor it, to notice when it behaves strangely and to take control. Their checklists and training assume that automation can fail. Clinical AI needs the same approach: a trained person who stays alert and knows how to take over.

## Worked Example
Carlo Villanueva is a patient safety nurse at a hypothetical hospital in the Philippines. The hospital is piloting a tool that flags possible deterioration on the ward from vital signs, for review by the nurse in charge. Carlo leads a failure mode review before the pilot.

| Step | What can go wrong | Effect | Detection | Prevention or mitigation |
|---|---|---|---|---|
| Vital signs entered | Observations entered late or not at all | Tool misses deterioration | Daily report of missing observations | Keep standard observation schedule; tool never replaces it |
| Alert sent | Alert goes to a shared screen nobody watches at night | Delay in review | Audit of time from alert to review | Alert to named nurse in charge on each shift |
| Alert volume | Too many false alerts | Staff ignore alerts | Track share of alerts dismissed in under 10 seconds | Review alert threshold with clinicians during pilot |
| Staff response | Nurse relies on "no alert" and does not escalate a worried feeling | Delay for a deteriorating patient | Incident reports; case reviews | Training: clinical concern always overrides the tool |
| Software | Data feed stops after a system update | Silent failure | Automatic check that data arrived in the last hour; daily test case | Named IT owner; stop the pilot if the check fails |

The table makes every risk visible, gives each one a detection method, and shows that some protections are about people and process, not software.

## Common Mistake
Many teams believe that once a tool has passed validation, the safety work is done. In reality, most failure modes appear only in daily use: staff become too trusting, alert volumes grow, systems change. Plan detection and monitoring before launch, and keep checking after it.

## Key Takeaways
1. Common failure modes are automation bias, alert fatigue, silent failure and workflow gaps.
2. Human factors design and incident reporting reduce harm, and the clinician's own judgement must always be able to override the tool.
3. A failure mode table lists what can go wrong, its effect, how it is detected and how it is prevented, with named owners.

## Hands-on Exercise
**Task:** Complete a simple failure mode table for the patient-engagement assistant from L07: what can go wrong, the effect, how it is detected and how it is prevented.
**Tools:** A table in any notes app, Google Sheets or Excel. Optional: Claude or ChatGPT (free plan) to suggest extra failure modes; do not enter any patient information.
**Steps:**
1. Draw a table with the columns: step, what can go wrong, effect, detection, prevention or mitigation.
2. List the steps of the L07 assistant: approved source, drafting, translation, sending, patient reply, escalation to a human.
3. For each step, write at least one failure mode. Include at least one example each of automation bias, silent failure and a workflow gap.
4. Complete the effect, detection and prevention columns. Add a named role responsible for each prevention.
5. Mark the two failure modes with the most serious possible effect.
6. Optional: ask an AI assistant for extra failure modes and add any that are realistic.
**What good looks like:** A table with at least 6 rows covering all steps, realistic effects on patients, a practical detection method for each (such as an audit or a test message), preventions with named roles, and a clear choice of the two most serious risks, for example an urgent message not reaching a human.
**Time:** about 30 minutes

## Review Flags
- Clinical reviewer sign-off required.
- The deterioration tool and hospital are hypothetical. A clinical reviewer should confirm that the failure mode table contains no clinical advice and that the aviation analogy is described in general, accurate terms.

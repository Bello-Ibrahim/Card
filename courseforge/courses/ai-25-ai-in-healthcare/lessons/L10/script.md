# L10 Patient Safety and Failure Modes | Presenter Script

Course: AI-25 · Video: 5 min · Words: 727

## Hook
Most harm from AI in healthcare will not look dramatic. It will look like a busy nurse accepting a suggestion without checking, or an alert that nobody reads anymore, or a tool that stopped working last Tuesday, and nobody noticed.

## Explain
In the last lesson, we saw how a tool can work less well for some patients and settings. Now we look at what goes wrong in daily work. A tool can be accurate in a study and still cause harm on the ward. Four failure modes are especially common.

The first is automation bias. People trust a tool's output too much, especially when they are tired or busy. They may accept a wrong suggestion, or stop looking for problems the tool does not flag. The second is alert fatigue. When most alerts are false, as we saw with low predictive value, staff begin to ignore them, including the true ones.

The third is silent failure. The tool stops working, or gets worse, without any visible sign. A software update, a new device or a broken data connection can cause it. The screen still shows results, but they are wrong or missing. The fourth is a workflow gap. For example, an alert goes to a shared inbox that nobody checks at night.

Two approaches reduce harm. The first is human factors design. Design around how people really work. Show uncertainty, make it easy to disagree with the tool, limit alerts to those that need action, and send outputs to a named role. The second is incident reporting and monitoring. Staff report problems and near misses, a named group reviews them, and performance is checked over time.

Here is a simple way to picture it. Aircraft autopilot flies much of a modern flight. Yet pilots are still trained to monitor it, to notice when it behaves strangely, and to take control. Clinical AI needs the same approach, a trained person who stays alert and knows how to take over.

## Demonstrate
Let's see how to plan for this. Carlo Villanueva is a patient safety nurse at a hypothetical hospital in the Philippines. The hospital is piloting a tool that flags possible deterioration from vital signs, for review by the nurse in charge. Before the pilot, Carlo leads a review using a failure mode table.

For each step, the table asks four questions. What can go wrong? What is the effect? How would we detect it? And how can we prevent it?

Take the alert step. An alert could go to a shared screen that nobody watches at night. The effect is a delay. They detect it by auditing the time from alert to review, and prevent it by sending alerts to the named nurse in charge on each shift.

Next, alert volume. Too many false alerts, and staff ignore them. They track how many alerts are dismissed in under ten seconds, and review the alert threshold with clinicians during the pilot. Then staff response. A nurse might rely on no alert, and not act on a worried feeling. So training makes one thing clear: clinical concern always overrides the tool.

Finally, software. The data feed could stop after a system update, a silent failure. They detect it with an automatic check that data arrived in the last hour, and a daily test case. A named IT owner is responsible, and the pilot stops if the check fails.

The table makes every risk visible, and shows that many protections are about people and process, not software. A common mistake is to think the safety work is done once a tool passes validation. Most failure modes only appear in daily use. Plan monitoring before launch, and keep checking after it.

## Recap
Let's recap. First, common failure modes are automation bias, alert fatigue, silent failure and workflow gaps. Second, human factors design and incident reporting reduce harm, and the clinician's own judgement must always be able to override the tool. Third, a failure mode table lists what can go wrong, its effect, how it is detected and how it is prevented, with named owners.

## CTA
Now it is your turn. In the exercise below this video, you will complete a failure mode table for the patient engagement assistant from lesson seven. It takes about thirty minutes. This completes week two. Next week, we start the capstone journey with regulation, privacy and ethics frameworks. See you there.

## Thumbnail
Headline: The Quiet Failures
Image: Navy background, a hospital monitor with a small unread alert badge and a faded clock, a teal warning triangle beside it, headline in teal Inter Bold.

## Production Notes
- Clinical reviewer sign-off required.
- A clinical reviewer should confirm that the failure mode table contains no clinical advice and that the aviation analogy is described in general, accurate terms (content.md Review Flags).
- Carlo Villanueva and the hospital in the Philippines are hypothetical. The deterioration tool supports review by the nurse in charge; it never replaces standard observations.
- Aircraft stock footage must show no airline names or logos.

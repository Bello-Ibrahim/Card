# HeyGen Batch Pack: AI-08 M3 (Checking and Presenting Insights)

Course: AI-Powered Data Analysis (No Code). Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L11 Checking AI Insights for Errors

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (686 words). The quality gate accepts ±10%.

```text
The AI's answer is well written, uses exact numbers, and sounds certain. But three of its four sentences are wrong or misleading. Would you notice before your manager did?

Welcome to week three. Last time, you built a dashboard. Now we learn to check AI insights before you share them.

AI analysis errors follow a few common patterns. The first is the wrong column, for example it reports units when you asked about revenue. The second is ignored rows. It skips blank or badly formatted rows, so counts and averages change. The third is mixing up totals and averages. It calls a total an average, or divides by the wrong count.

The fourth is an invented cause. The AI explains why something happened, with information that is not in the data. And the fifth is a trend from too little data. It sees strong growth in three months, or in one large value.

A short, five-point checking routine catches most of these. One, recalculate one number yourself, with a formula or a pivot table. Two, check row counts. Ask how many rows the AI used, and compare with your sheet. Three, look at the chart, and see whether one value drives the pattern.

Four, ask, compared with what? Is there a fair comparison, such as a previous period or another group? Five, look for other explanations. Is the cause in the data, or did the AI add it? Could a third factor or one unusual event explain it?

You do not need to check every sentence to the last decimal. But every number and claim you pass on to others should survive this routine.

It is like checking a restaurant bill before you pay. You do not redo every sum. But you check the total, count the dishes, and ask about any item you did not order.

Ingrid works in revenue management at a hotel in Bergen, Norway. She uploads a fictional, anonymised file of two hundred bookings.

The AI says, the average stay is three point five nights. Guests from Germany stay longest, so the hotel should advertise in Germany.

She applies the routine. First, row count. The AI used only one hundred and eighty-eight rows. Twelve bookings, all long stays for a company contract, had a blank nationality cell, and the AI dropped them. Her own average over all two hundred rows gives three point eight nights.

Next, compared with what? The German result is based on only four bookings. That is too few to support an advertising decision.

Then, other explanations. The data has no information about advertising. So the recommendation is the AI's idea, not a finding. Ingrid reports the corrected average, and marks the Germany point, needs more data. Notice that each check found a different problem. One check alone would not have been enough.

In your exercise, you will check an AI answer about the orders sheet. It has four insights. Total revenue and the average order. The strongest region. Monthly growth with a forecast. And the share from office chairs. Some of them contain planted errors. Your job is to find them.

A common mistake is to check only whether the numbers are correct. But a sentence can use correct numbers and still mislead, through a missing comparison, a trend built on one value, or an invented cause. Check the reasoning as well as the arithmetic.

Let's recap. First, common AI errors are the wrong column, ignored rows, totals mixed with averages, invented causes, and trends from too little data. Second, use the five-point routine. Recalculate one number, check row counts, look at the chart, ask compared with what, and look for other explanations. Third, correct numbers can still support a misleading conclusion, so check the reasoning too.

Now it is your turn. In the exercise below this video, you will review those four AI insights, and use the five-point routine to find and correct the planted errors. It takes about twenty-five minutes. This routine will also guide your capstone, a five-slide business insight report. You start it in the next lesson, Capstone, Explore Your Dataset. See you there.
```

## L12 Capstone: Explore Your Dataset

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M3_L12_presenter.mp4`
- **Expected length:** about 5.2 minutes (723 words). The quality gate accepts ±10%.
- **Pronunciation:** [VERIFY] [REGION] content.md names possible public dataset sources (UCI Machine Learning Repository including 'Online Retail', World Bank Open Data, Our World in Data, Kaggle, national government open-data portals). Their availability and licence terms are unverified, so the narration and slides say only 'a public sample dataset from an open-data source'. After checking, the source names may be added to the scene 5 slide, never to the narration without re-recording review.

```text
So far, you have practised on a small, clean, fictional dataset. Now you choose real business data, with real questions and real mess. This week, you will produce something you could show to a manager. A five-slide insight report, built on findings you have checked yourself.

This is the capstone for the course. Here is the brief. Analyse a real business dataset with AI tools, and present a five-slide insight report with charts, a clear recommendation, and the limits of the analysis.

You build it in three steps. Step one is this lesson. Choose and clean a dataset, write three business questions, and record at least five checked findings in a findings log. Step two, in the next lesson, you choose your main finding and plan a five-slide storyline. Step three, in the last lesson, you build the slides and check every number.

The rubric gives points for your questions and data preparation, your analysis, how you checked the AI, your charts, and your story and recommendation. Read the full rubric on the course page before you start.

You have two options for your data. Option one is your own work data, anonymised as in lesson two. Check that your employer allows you to use it for training, and to upload it to an AI tool. If you are unsure, use option two, a public sample dataset from an open-data source. Licences differ, so read the licence, and note it in your report.

A good capstone dataset has a few hundred to a few thousand rows. It has a date column, at least one number to measure, like sales, visits or costs, and at least one group column, like product, region or channel. Also check the current file size limit of your AI tool.

As you work, keep a findings log. This is a simple table in Google Sheets. For every finding, you record the question, the finding, how you found it, how you checked it, and the result. The how checked column uses the five-point routine from lesson eleven.

A finding that fails the check stays in the log, marked rejected, with the reason. That record shows your judgement.

A findings log is like a scientist's lab notebook. Each entry records what was tried, what was seen, and how it was checked. So anyone can follow the work later, including you.

Rahel is a sales supervisor for a fictional chain of three electronics shops in Addis Ababa, Ethiopia. She exports one year of sales, removes customer names and phone numbers, and checks with her manager that she may use the anonymised data.

Her business question is, where should we focus next quarter? She breaks it into three data questions. Revenue by shop per month, compared with the previous month. Revenue by product category, this year's second half compared with the first half. And average basket value by weekday.

She cleans the file. There are two date formats, a duplicated week, and category names in two languages. She logs each fix. Then she asks the AI her first question, with the four-part prompt from lesson six.

After one session, her log has six findings. Five are confirmed with pivot tables. One is rejected. The AI said Saturday sales are highest because of payday. But the file has no payday information, and the Saturday total includes one large business order.

So in the result column, she writes, rejected, invented cause, one-order effect.

A common mistake is to choose a very large or complex dataset because it looks impressive, and then spend all week cleaning it. Choose a dataset you can understand in fifteen minutes. A simple dataset analysed carefully earns more than a complex one explored quickly.

Let's recap. First, choose anonymised work data you are allowed to use, or a public dataset whose licence you have read. Second, write three measurable business questions before you start the analysis. Third, record every finding in a findings log, including how you checked it, and any finding you rejected.

Now it is your turn. This is capstone step one. Choose your dataset, clean it, write three business questions, and record at least five checked findings in your findings log. It takes about sixty minutes. In the next lesson, Turning Findings into a Story, you choose your main finding and plan your five slides. See you there.
```

## L13 Turning Findings into a Story

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M3_L13_presenter.mp4`
- **Expected length:** about 5.3 minutes (725 words). The quality gate accepts ±10%.

```text
You have a findings log with twelve checked findings. You put all twelve on slides, and your audience remembers none of them. People do not remember lists of numbers. They remember one clear message, and the reason to act on it.

Last time, you explored your data and logged your findings. Now we turn them into a story.

A data story has three parts. One main finding, the single most important thing the audience should remember. Then supporting evidence, two or three findings, each with a chart. And a recommended action, what the audience should do next, and how to measure whether it worked.

To choose the main finding, look at your log and ask three things. Does it matter most for the business question? Is it well checked? Does it lead to an action? A surprising finding is interesting, but if it does not lead to a decision, it belongs in the notes.

Then apply the so what test to every chart. Read the chart, and ask, so what? If the answer is, so we should change the reminder system, the chart supports the story. If the answer is, it is interesting, remove it or move it to an appendix.

For this capstone, the storyline has five slides, with one message each. The question. The key finding. The evidence. The recommendation. And the limits, what the data cannot tell you. Write each message as a full sentence before you design anything. If the five sentences make sense read aloud, the structure is right.

A data story is like a news report. The headline gives the main point. The next paragraphs give the evidence. The end says what happens next. A reporter who reads out every note does not have a story yet.

Ananya manages an outpatient clinic in Chennai, India. Her question is, why do so many patients miss appointments, and what can we do? Her fictional, anonymised data covers one thousand appointments, with one hundred and eighty no-shows. That is eighteen percent.

Her findings log has twelve confirmed findings. She applies the so what test. Most appointments are for general check-ups. That is true, but it leads to no action, so she removes it.

Her main finding is this. Patients booked more than three weeks ahead miss appointments much more often.

Support one. Booked more than three weeks ahead, one hundred and twenty-four no-shows out of four hundred. That is thirty-one percent. Booked within three weeks, fifty-six out of six hundred, about nine percent. A bar chart compares the two groups.

Support two. Patients who got an SMS reminder missed fifty of five hundred appointments, ten percent. Those without a reminder missed one hundred and thirty of five hundred, twenty-six percent. Support three. No-shows are highest on Monday mornings.

Her five slide messages. One, we wanted to know why eighteen percent of appointments are missed, using one thousand appointments from the last six months. Two, patients booked more than three weeks ahead miss thirty-one percent of appointments. Three, the gap is large, and reminders appear to help.

Four, send an SMS reminder to every patient two days before the visit, and compare the no-show rate after three months. Five, the data shows patterns, not proof. Patients who got reminders may differ in other ways, and we do not know patients' reasons.

Slide five is honest. The reminder finding is a correlation, and a trial is needed to test the cause.

A common mistake is to present findings in the order you found them. That is the order of your work, not the order your audience needs. Start with the main finding. And make the recommendation specific and measurable, not just improve communication.

Let's recap. First, a data story has one main finding, two or three supporting findings, and a specific recommended action. Second, apply the so what test to every chart, and remove charts that do not support the message. Third, plan five slides with one message each, and write each message as a sentence before you design anything.

Now it is your turn. This is capstone step two. Choose your main finding and three supporting findings, and sketch a five-slide storyline with one message per slide. It takes about forty minutes. In the last lesson, Building and Reviewing Your Five-Slide Report, you build your slides and check every number. See you there.
```

## L14 Building and Reviewing Your Five-Slide Report

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M3_L14_presenter.mp4`
- **Expected length:** about 5.2 minutes (722 words). The quality gate accepts ±10%.

```text
Your slides look professional, the charts are clear, and the story makes sense. Then someone in the meeting asks, the chart says thirty-one percent, but the title says thirteen percent. Which is right? One wrong number can make people doubt everything else you show.

In the last lesson, you planned five messages. Now you turn them into slides, in Google Slides or a similar free tool.

Here are the five slides. Slide one is the question. The business question, the dataset with its source, period and number of rows, and one sentence on how you analysed it. Slide two is the key finding. The main message as the title, and one large number that supports it. Slide three is the evidence. One to three charts, each with a title that states its finding.

Slide four is the recommendation. A specific action, who should do it, and how to measure whether it worked. Slide five is the limits. What the data cannot show, such as a small sample, missing columns, correlation rather than cause, or data from one period only.

For the charts, you can insert a chart from Google Sheets and link it to the spreadsheet, so it can be updated if the data changes. From Looker Studio, you can use a screenshot of a chart. Keep one message per slide, large text and few words. Put extra detail in the speaker notes.

AI can help with wording. Paste your five messages and ask for shorter titles, or ask what a manager might question. But do not paste raw personal or confidential data to do this.

Then comes the final check. Before you share the report, check every number on every slide against your source data. Make a small check table with four columns. The slide, the number shown, where it comes from, and match or fix. Check chart titles, labels and speaker notes too.

Numbers change when you round them, copy them or rewrite a title. So this check comes last.

It is like a pilot's checklist before take-off. The pilot has flown many times and knows the aircraft well. But the pilot still checks every item, because one missed item can cause serious problems.

Elena is a small business consultant in Bucharest, Romania. She has built a five-slide report for a fictional bakery client, about weekend sales.

She makes her check table. Slide two says weekend sales grew eighteen percent. Her pivot table shows weekend revenue rising from five thousand to five thousand nine hundred lei. Nine hundred divided by five thousand is eighteen percent. Match.

Slide three's chart title says Saturday is sixty percent of weekend sales. But the pivot table shows three thousand three hundred of five thousand nine hundred, which is about fifty-six percent. The AI had suggested the title from an earlier version of the data.

Fix. She changes the title to, Saturday brings in more than half of weekend sales, fifty-six percent.

On slide five, she writes the limits. The data covers only six months, and a new competitor opened nearby during that time, which may affect the results. In the speaker notes, she adds how she cleaned the data, and how many rows she used.

A common mistake is to check the numbers once, early, and then keep editing titles and charts. Each edit is a new chance for an error. Another is to hide the limits. A clear limits slide makes the report more trustworthy, not less.

Let's recap. First, the five slides are the question, the key finding, the evidence, the recommendation, and the limits of the analysis. Second, insert charts from Google Sheets or Looker Studio, keep one message per slide, and put detail in the speaker notes. Third, as the very last step, check every number on every slide against the source data, with a check table.

Now it is your turn. This is capstone step three. Build your five-slide insight report, check every number against your data, and add a speaker note that explains the limits of your analysis. Then submit your report with your findings log, using the checklist and rubric on the course page.

Congratulations on finishing AI-Powered Data Analysis. You can now clean, analyse, chart and explain data with AI, and check every number before you share it. Well done, and good luck with your report.
```

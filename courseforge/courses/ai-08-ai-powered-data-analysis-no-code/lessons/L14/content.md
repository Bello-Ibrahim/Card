# L14 Building and Reviewing Your Five-Slide Report

Course: AI-08 · Module: M3 · Objectives: O6, O7 · Video: 5 min

## Hook
Your slides look professional, the charts are clear and the story makes sense. Then someone in the meeting asks, "The chart says 31%, but the slide title says 13%. Which is right?" One wrong number can make people doubt everything else you show.

## Explanation
In L13 you planned five messages. Now you turn them into slides. Use Google Slides or a similar free presentation tool; the steps below describe Google Slides. [VERSION]

**The five slides:**

1. **The question:** the business question, the dataset (source, period, number of rows) and one sentence on how you analysed it.
2. **The key finding:** the main message as the slide title, and one large number that supports it.
3. **The evidence:** one to three charts, each with a title that states its finding (L09).
4. **The recommendation:** a specific action, who should do it, and how to measure whether it worked.
5. **The limits:** what the data cannot show, such as a small sample, missing columns, correlation rather than cause, or data from one period only.

**Adding charts.** From Google Sheets, you can insert a chart with **Insert > Chart > From Sheets** and choose to link it to the spreadsheet, so it can be updated if the data changes. [VERSION] From Looker Studio, you can take a screenshot of a chart or use its download options. [VERSION] Keep one message per slide, large text and few words. Put extra detail in the **speaker notes**.

AI can help with wording: paste your five messages and ask for shorter titles, or ask it to suggest what a manager might question. Do not paste raw personal or confidential data to do this.

**The final check.** Before you share the report, check **every number on every slide** against your source data. Make a small check table with four columns: the slide, the number shown, where it comes from (a pivot table cell or formula), and "match" or "fix". Check the chart titles, labels and speaker notes too, not only the main text. Numbers change when you round them, copy them or rewrite a title, so this check comes last.

**Analogy:** The final number check is like a pilot's checklist before take-off. The pilot has flown many times and knows the aircraft well, but still checks every item, because one missed item can cause serious problems.

## Worked Example
Elena is a small business consultant in Bucharest, Romania. She has built a five-slide report for a fictional bakery client on weekend sales.

She makes her check table. Slide 2 says "Weekend sales grew 18%". Her pivot table shows weekend revenue rising from 5,000 to 5,900 lei: (5,900 − 5,000) ÷ 5,000 = 18%. Match. Slide 3's chart title says "Saturday is 60% of weekend sales", but the pivot table shows 3,300 of 5,900, which is about 56%. The AI had suggested the title from an earlier version of the data. Fix: she changes it to "Saturday brings in more than half of weekend sales (56%)".

On slide 5 she writes the limits: the data covers only six months, and a new competitor opened nearby during that time, which may affect the results. In the speaker notes she adds how she cleaned the data and how many rows she used.

## Common Mistake
Many learners check the numbers once, early, and then keep editing titles and charts. Each edit is a new chance for an error. Another mistake is to hide the limits or leave them out. A clear limits slide makes the report more trustworthy, not less.

## Key Takeaways
1. The five slides are: the question, the key finding, the evidence, the recommendation, and the limits of the analysis.
2. Insert charts from Google Sheets or Looker Studio, keep one message per slide, and put detail in the speaker notes.
3. As the very last step, check every number on every slide against the source data with a check table.

## Hands-on Exercise
**Task:** Capstone step 3: build your five-slide insight report, check every number against your data, and add one slide note that explains the limits of your analysis.
**Tools:** Google Slides (free) or a similar free presentation tool; Google Sheets and Looker Studio for charts; optional Claude or ChatGPT for wording. [VERSION]
**Steps:**
1. Create a new presentation with five slides, using your five messages from L13 as the titles.
2. Add your charts: insert them from Google Sheets or add images from Looker Studio.
3. Write the recommendation as a specific, measurable action.
4. Write the limits slide, and add a speaker note that explains the limits in more detail.
5. Make a check table in Google Sheets: slide, number, source, match or fix. Check every number, including chart titles and notes.
6. Fix any mismatch, then read the whole report once more from start to end.
7. Export or share the report with view-only access, and submit it with your findings log.
**What good looks like:** Five clear slides with one message each; charts with titles that state findings; a specific recommendation; an honest limits slide with a speaker note; and a check table where every number is marked "match".
**Time:** about 60 minutes

## Review Flags
- [VERSION] Google Slides steps (Insert > Chart > From Sheets, linking and updating charts, speaker notes) and Looker Studio chart download or export options must be checked against the live tools before scripting.
- Judgement call (from the curriculum): this lesson uses Google Slides or a similar free tool, which is not listed in the brief's tools_free_first; charts come from Google Sheets or Looker Studio.

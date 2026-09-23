# L08 Trends, Outliers and Correlation | Presenter Script

Course: AI-08 · Video: 5 min · Words: 743

## Hook
Revenue in March was more than four times revenue in January. Is the business growing fast? Or did one customer place one very large order? The same number can tell two very different stories.

## Explain
Last time, we built summaries and pivot tables. Now we look for patterns. Three ideas help, and each one has a trap.

The first idea is a trend. A trend is the general direction of a number over time, up, down or flat. To read a trend, look at many periods, not two. Three months can show a direction, but it is weak evidence. And check whether one unusual period creates a trend that disappears when you look closer.

The second idea is an outlier. That is a value far from the others, like one order ten times larger than usual. Outliers have three common causes. A data error, like forty-five typed instead of four hundred and fifty. A real but rare event, like a bulk order or a festival. Or a sign of change, like the first of many large orders from a new type of customer.

So never delete an outlier just because it is unusual. Ask why it exists first. Fix it if it is an error. If it is real, keep it, and report results with and without it.

The third idea is correlation. Two numbers are correlated when they tend to move together. That does not mean one causes the other. Here is a hypothetical case. In a coastal town, ice-cream sales and sunburn cases rise and fall together over the year. Ice cream does not cause sunburn. Both follow a third factor, hot, sunny weather.

So when AI says X leads to Y, ask three questions. Could a third factor explain both? Could it be a coincidence in a small dataset? Could the direction be reversed? AI finds outliers and correlations quickly, but it explains them less carefully.

Think of footprints in sand. A long line of steps shows a direction. That is a trend. One very deep print is an outlier, so ask what made it. And two lines of prints side by side do not mean one person followed the other. Both may have walked to the same café.

## Demonstrate
Fatou runs three ice-cream kiosks in Dakar, Senegal. She asks an AI tool to analyse her fictional weekly sales sheet for twelve weeks.

First, the AI reports a rising trend. Weekly sales grew from about three hundred cups in week one, to about four hundred and fifty in week twelve. Fatou checks with a line chart. The rise is steady over many weeks, not caused by one value. So she accepts it as a trend.

Second, the AI finds two outliers. Nine hundred cups in week seven, and forty-five cups in week ten. She does not delete them. She asks why.

Week seven was the week of a local festival next to one kiosk. That is a real event, so she keeps it and notes it. Week ten does not match her till records, which show four hundred and fifty. It was a typing error, so she corrects it.

Third, the AI notes that her sales rise in the same weeks as sunburn cases at a nearby clinic, which is also fictional. It says, higher sales are linked to sunburn.

Fatou sees the third factor. Hot weather drives both. The useful finding for her business is the link between temperature and sales, and she can check it against weather records.

A common mistake is to remove every outlier to make the chart look tidy. That can remove the most important finding. The opposite mistake is to build a whole conclusion on one outlier. Investigate first, then report with and without the unusual value.

## Recap
Let's recap. First, a trend needs many periods, so check whether one unusual value creates or hides it. Second, ask why an outlier exists before you remove it. Fix errors, keep real events, and report their effect. Third, correlation does not prove causation. Look for a third factor, a coincidence, or a reversed direction.

## CTA
Now it is your turn. In the exercise below this video, you will use AI to find the three largest outliers and one trend in the orders sheet. For each one, write a possible cause and how you could check it. It takes about twenty-five minutes. In the next lesson, we choose and build the right chart. See you there.

## Thumbnail
Headline: Pattern or Coincidence?
Image: Navy background, a teal line chart rising over twelve points with one tall spike and one deep dip circled, headline in teal Inter Bold.

## Production Notes
- [VERSION] File-analysis features in Claude and ChatGPT must be checked against the live tools before recording (the exercise uses file upload; the video does not name limits).
- Fatou, her Dakar kiosks, the weekly sales sheet and the nearby clinic's sunburn figures are fictional; the ice-cream and sunburn town is a hypothetical case. content.md gives only these figures, and the script uses them exactly: about 300 cups in week 1, about 450 in week 12, 900 in week 7, 45 in week 10 (till records 450).
- Scene 9 and 10 charts: draw a smooth 12-week line from about 300 to about 450 with the week 7 spike (900) and week 10 dip (45). Other weekly values are illustrative only; do not label them with numbers.
- The hook's 'more than four times' refers to the orders dataset (January 470, March 2,160 in content.md's exercise).

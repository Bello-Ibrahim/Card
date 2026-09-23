# L12 Capstone: Explore Your Dataset | Presenter Script

Course: AI-08 · Video: 5 min · Words: 730

## Hook
So far, you have practised on a small, clean, fictional dataset. Now you choose real business data, with real questions and real mess. This week, you will produce something you could show to a manager. A five-slide insight report, built on findings you have checked yourself.

## Explain
This is the capstone for the course. Here is the brief. Analyse a real business dataset with AI tools, and present a five-slide insight report with charts, a clear recommendation, and the limits of the analysis.

You build it in three steps. Step one is this lesson. Choose and clean a dataset, write three business questions, and record at least five checked findings in a findings log. Step two, in the next lesson, you choose your main finding and plan a five-slide storyline. Step three, in the last lesson, you build the slides and check every number.

The rubric gives points for your questions and data preparation, your analysis, how you checked the AI, your charts, and your story and recommendation. Read the full rubric on the course page before you start.

You have two options for your data. Option one is your own work data, anonymised as in lesson two. Check that your employer allows you to use it for training, and to upload it to an AI tool. If you are unsure, use option two, a public sample dataset from an open-data source. Licences differ, so read the licence, and note it in your report.

A good capstone dataset has a few hundred to a few thousand rows. It has a date column, at least one number to measure, like sales, visits or costs, and at least one group column, like product, region or channel. Also check the current file size limit of your AI tool.

As you work, keep a findings log. This is a simple table in Google Sheets. For every finding, you record the question, the finding, how you found it, how you checked it, and the result. The how checked column uses the five-point routine from lesson eleven.

A finding that fails the check stays in the log, marked rejected, with the reason. That record shows your judgement.

A findings log is like a scientist's lab notebook. Each entry records what was tried, what was seen, and how it was checked. So anyone can follow the work later, including you.

## Demonstrate
Rahel is a sales supervisor for a fictional chain of three electronics shops in Addis Ababa, Ethiopia. She exports one year of sales, removes customer names and phone numbers, and checks with her manager that she may use the anonymised data.

Her business question is, where should we focus next quarter? She breaks it into three data questions. Revenue by shop per month, compared with the previous month. Revenue by product category, this year's second half compared with the first half. And average basket value by weekday.

She cleans the file. There are two date formats, a duplicated week, and category names in two languages. She logs each fix. Then she asks the AI her first question, with the four-part prompt from lesson six.

After one session, her log has six findings. Five are confirmed with pivot tables. One is rejected. The AI said Saturday sales are highest because of payday. But the file has no payday information, and the Saturday total includes one large business order.

So in the result column, she writes, rejected, invented cause, one-order effect.

A common mistake is to choose a very large or complex dataset because it looks impressive, and then spend all week cleaning it. Choose a dataset you can understand in fifteen minutes. A simple dataset analysed carefully earns more than a complex one explored quickly.

## Recap
Let's recap. First, choose anonymised work data you are allowed to use, or a public dataset whose licence you have read. Second, write three measurable business questions before you start the analysis. Third, record every finding in a findings log, including how you checked it, and any finding you rejected.

## CTA
Now it is your turn. This is capstone step one. Choose your dataset, clean it, write three business questions, and record at least five checked findings in your findings log. It takes about sixty minutes. In the next lesson, Turning Findings into a Story, you choose your main finding and plan your five slides. See you there.

## Thumbnail
Headline: Your Capstone Starts Here
Image: Navy background, a findings-log table with ticks and one 'rejected' row, next to a stack of five slide outlines, headline in teal Inter Bold.

## Production Notes
- [VERIFY] [REGION] content.md names possible public dataset sources (UCI Machine Learning Repository including 'Online Retail', World Bank Open Data, Our World in Data, Kaggle, national government open-data portals). Their availability and licence terms are unverified, so the narration and slides say only 'a public sample dataset from an open-data source'. After checking, the source names may be added to the scene 5 slide, never to the narration without re-recording review.
- [REGION] Rules on using work data differ by country and employer; the narration tells learners to check with their employer.
- [VERSION] File size limits and file-analysis features in Claude and ChatGPT must be checked against the live tools; the narration only says 'check the current file size limit'.
- Rahel, the Addis Ababa electronics chain and her findings are fictional. Spoken numbers match content.md: 3 shops, one year of sales, 6 findings, 5 confirmed, 1 rejected.
- Scene 7 and 13 slides show the findings-log columns exactly as in content.md: No. | Question | Finding | How found | How checked | Result.

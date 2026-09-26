# HeyGen Batch Pack: AI-29 M1 (Where AI Goes Wrong)

Course: AI Ethics, Bias and Safety. Make one HeyGen video per lesson below, using these settings for every video.

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

## L01 Why AI Ethics Matters to Everyone

- **Filename:** `ai-29-ai-ethics-bias-and-safety_M1_L01_presenter.mp4`
- **Expected length:** about 5.0 minutes (703 words). The quality gate accepts ±10%.

```text
Imagine you apply for a job and never get an interview. No person read your application. A computer system sorted it into the no pile, and nobody can tell you why. Would you want to know how that system was built and checked?

Hi, and welcome to AI Ethics, Bias and Safety. In this first lesson, we look at why AI ethics matters to everyone, not only to experts.

AI systems now help decide who gets a job interview, a loan, an insurance price or a medical appointment. When an AI system makes a mistake, the mistake does not stay inside the computer. It reaches real people, and it can repeat thousands of times before anyone notices.

AI ethics means asking a few simple questions. Is this system fair, honest, safe and under human control? You do not need to be a programmer to ask them. People who build AI, people who buy it, and people who simply use it every day all make choices that affect others.

This course uses eight key terms. The first four. Bias means results that are better or worse for some groups, like a voice assistant that struggles with some accents. Fairness is the goal of treating people and groups in a just way. A hallucination is confident information that is false, like a book that does not exist. And misinformation is false information that spreads.

Now the other four. Privacy is people's control over their personal information. Safety means avoiding physical, financial, emotional or social harm. Transparency means people can find out that AI is being used, and how it works in simple terms. And accountability means a named person or team is responsible for the results.

Here is a simple way to think about it. An AI system is like a new colleague who works very fast, but was trained by someone else. The colleague can be very helpful. But you did not see their training. So you do not know which habits they learned, or which customers they misunderstand. Before you trust their work, you check it.

Let's see the terms at work. Linh Tran manages customer service for a hotel group in Vietnam. Her company buys an AI tool that reads guest reviews and flags urgent complaints, so her team can handle them first.

After two months, Linh notices a pattern. Reviews in formal English are flagged quickly. Reviews in Vietnamese, or in short, simple English, are often missed, even when they describe serious problems, such as a broken door lock.

Linh uses the eight terms to describe the problem. It is bias, because the tool works worse for some guests. It is a fairness problem, because those guests wait longer for help. It is a safety problem, because a broken lock is a real risk. It raises transparency questions, because the vendor never explained which languages it tested. And it raises accountability questions. Who checks the flagged list?

Her team starts a daily manual check of reviews the tool did not flag, and asks the vendor for test results by language. Nobody on the team is a programmer, but their questions lead to a safer service.

One common mistake is to think AI ethics is only for engineers or lawyers. Many harms come from how a tool is bought and used. A manager who uses a tool for a task it was not built for, or a staff member who copies a chatbot answer without checking it, can cause harm with a well-built system.

Legal duties are covered in course AI thirty. In this course, we stay practical.

Let's recap. First, AI now affects decisions about jobs, money and health, so its mistakes reach real people, often at large scale. Second, the eight key terms are bias, fairness, hallucination, misinformation, privacy, safety, transparency and accountability. Third, builders, buyers and everyday users all make choices that affect whether AI is used responsibly.

Now it is your turn. In the exercise below this video, you will match the eight key terms to eight short scenarios, then check your answers with the answer key. It takes about ten minutes. In the next lesson, we will find out how bias gets into AI. See you there.
```

## L02 How Bias Gets into AI

- **Filename:** `ai-29-ai-ethics-bias-and-safety_M1_L02_presenter.mp4`
- **Expected length:** about 4.9 minutes (683 words). The quality gate accepts ±10%.

```text
Nobody sits down and writes treat women worse, or ignore rural customers, into an AI system. Yet biased systems appear again and again. If nobody plans the bias, where does it come from?

In the last lesson, you met bias. Results that are better or worse for some groups. Bias rarely comes from one bad decision. It usually enters quietly, at one or more of three points. The data, the design, and the use.

First, the data. An AI system learns patterns from examples. If the examples are unbalanced, the patterns will be too. Some groups may be missing, like darker skin in a skin-condition app. Some may be over-represented, like city speakers in a speech tool. And if past decisions were unfair, the data records that unfairness as if it were correct.

Second, the design. People decide what the system should predict, and which details it may use. A tool that predicts who will cost the most is not the same as one that predicts who needs the most care. And even if the system never sees gender, details like a postcode or a gap in employment can stand in for it. We call these proxies.

Third, the use. A system can be fair in one place and unfair in another. It may be used for a different purpose, or in a group it was never tested on. And people may trust it too much and stop checking.

Here is a simple picture. A recipe copied from an old cookbook repeats its mistakes, however carefully you cook. If the cookbook used too much salt, your dish will be too salty, even if you measure perfectly. Careful training cannot fix mistakes that were already in the recipe.

Let's follow one example. Claire Tremblay leads recruitment at an engineering company in Canada. To save time, the company builds a CV-screening tool, trained on ten years of past hires. CVs of people who were hired are labelled good, and all the others are labelled not selected. It sounds sensible. Let's see what happens.

Now watch the three points. The data: most engineers hired in those ten years were men from three local universities, so the tool learns that CVs like theirs are good. The design: the team asked it to predict people like our past hires, not people who will do the job well. It also reads hobbies and clubs, which can act as proxies.

The use: recruiters start to trust the tool's top twenty list and stop reading the other CVs. Qualified people from other universities, and many women, are never seen by a person. Nobody wanted this. But the tool now repeats old hiring patterns at high speed.

Claire's team makes three changes. They check which groups are in the training data. They change the goal to match the skills in the job description. And a person reviews a sample of rejected CVs every week.

A common mistake is to think that removing names, gender or age makes a system fair. Other details can still act as proxies, A women's sports club, a school for girls, or a career gap for childcare can all carry the same pattern. So removing details can be one step, but you still need to test results for different groups, as you will learn later in this course.

Let's recap. First, bias can enter through the data, the design and the use. Second, data that records past decisions can also record past unfairness, and the system learns it as if it were correct. Third, removing names or gender is not enough, because other details can act as proxies. Results must be tested. Keep these three points in mind whenever you meet a new AI tool.

Now it is your turn. In the exercise below this video, you will look at a loan-approval model at a bank in Kenya, and list one way bias could enter through the data, the design and the use. It takes about fifteen minutes. In the next lesson, we will look at fairness, and who gets helped and who gets hurt. See you there.
```

## L03 Fairness: Who Gets Helped and Who Gets Hurt

- **Filename:** `ai-29-ai-ethics-bias-and-safety_M1_L03_presenter.mp4`
- **Expected length:** about 4.9 minutes (688 words). The quality gate accepts ±10%.

```text
A company tells you its AI tool is ninety percent accurate. That sounds good. But what if it is ninety-eight percent accurate for one group of people, and sixty percent for another? One number can hide a big difference.

In the last lesson, you saw how bias can get into a system through the data, the design and the use. Now the question is, how do we notice it? The simplest method is to compare results between groups. A group can be defined by gender, age, region, language, disability, or anything else that matters for the task.

For each group, we look at a few simple numbers. The approval rate is the share of people who got the positive result. Forty approved out of a hundred is a forty percent approval rate.

The error rate is the share the system got wrong. And missed cases are the people who really qualified, or really were ill, but the system missed them. If these numbers are very different between groups, the system may be unfair, and you need to ask why.

Here is the difficult part. Fairness has more than one definition, and they can conflict. Equal approval rates means each group is approved at the same rate. Equal error rates means the system makes mistakes at the same rate for each group. When groups are different in real life, a system usually cannot meet both at once.

So people, not the computer, must decide which kind of fairness matters most for each use. A medical tool might focus on missing no sick patients. A hiring tool might focus on equal chances for equally qualified people.

Think of a school exam with an average score of seventy-five. That average says nothing about whether one classroom scored ninety and another scored sixty. A head teacher who only looks at the average will never find the classroom that needs help. Fairness checks look inside the average.

Let's see this in practice. Doctor Rafael Souza works for a health network in Brazil. The network uses an AI tool that flags patients at high risk of a heart problem, so they get an early check. The vendor says it is ninety percent accurate overall. That sounds reassuring. But Rafael wants to look inside the average.

Rafael asks for results by group, urban and rural patients. For urban patients, one hundred were really at high risk, and the tool missed ten. That is a ten percent missed-case rate. For rural patients, fifty were really at high risk, and the tool missed twenty-five. That is half of them.

Because most patients are urban, the overall number still looks good. So why is the tool worse for rural patients? Rural patients visit clinics less often, so they have fewer test results in their records. The tool had less information, and often guessed low risk.

The network decides which fairness goal matters most here. Missing as few high-risk patients as possible, in every group. Until the tool improves, every rural patient it rates as low risk also gets a short review by a nurse.

A common mistake is to trust one overall number and stop there. A large group can hide poor results in a small group. So always ask, accurate for whom? Another mistake is to think there is one correct fairness number. There are several, and choosing between them is a human decision, based on who could be hurt.

Let's recap. First, you can check fairness by comparing results, such as approval rates, error rates and missed cases, between groups. Second, a good overall number can hide poor results for a smaller group. Third, different definitions of fairness can conflict, so people must choose which one matters most for each use.

Now it is your turn. In the exercise below this video, you will use a small table of results for a scholarship tool to calculate approval rates and error rates for two groups. Then you will write two sentences on whether the tool looks fair. It takes about fifteen minutes. In the next lesson, we will look at hallucinations, misinformation and deepfakes. See you there.
```

## L04 Hallucinations, Misinformation and Deepfakes

- **Filename:** `ai-29-ai-ethics-bias-and-safety_M1_L04_presenter.mp4`
- **Expected length:** about 4.9 minutes (686 words). The quality gate accepts ±10%.

```text
You ask a chatbot for three research articles on your topic. It gives you three titles, three author names and three publication years, all in perfect format. You search for them. None of them exists.

To understand why, you need to know one thing about how chatbots work. A chatbot, such as Claude or ChatGPT, is built on a large language model. It writes by predicting the next likely words, based on patterns in the text it learned from. It does not simply look up facts in a database.

So a chatbot can produce text that sounds right, but is wrong. This is called a hallucination. It is most common with exact numbers, dates and quotes, with sources, with local or specialist topics, and with very recent events. And it comes in the same confident voice as a correct answer.

Misinformation is false or misleading information that spreads. AI adds to it in two ways. People copy hallucinated answers without checking. And AI can quickly produce large amounts of convincing false content.

Deepfakes are AI-made images, voices or videos that show people saying or doing things they never did. A fake voice message from a manager could ask for an urgent payment. A fake video could show a public figure making a false statement. Deepfakes make false stories look and sound real.

Here is a simple way to think about it. A chatbot is like a very confident friend who has read a lot, but never checks notes. Most of the time their answers are helpful. Sometimes they fill a gap in their memory with something that sounds right, in exactly the same calm voice.

Three habits help. Check claims against a trusted source. Ask for sources, then open them. And slow down when content makes you feel a strong emotion, such as anger, fear or excitement. False content often tries to make you share or act fast.

Let's see the habits in action. Aigerim Bekova writes a newsletter for a farming cooperative in Kazakhstan. She asks a chatbot for the average wheat yield in her region, and which study shows it. The chatbot gives a precise number and names a study.

Aigerim follows the three habits. She checks the number on her country's official agriculture website, and the official figure is different. She searches for the study, and cannot find it. The source was invented. And she notices that the answer felt reliable only because it was so specific and confident.

She uses the official figure, links to the official source, and adds one line to her team's guidance. Never publish a number or a source from a chatbot until you have opened the original. It is a small rule, but it protects the whole team.

The same week, a member forwards a voice message that claims to be from the director, asking for a quick payment to a new supplier. Aigerim calls the director on a known number. The director did not send it.

A common mistake is to think that if a chatbot gives a source, the answer must be correct. A source only counts after you have opened it and found the claim in it yourself. A chatbot can also give a real source that does not say what it claims. And deepfakes are not always easy to spot, so check the context and confirm through a different channel.

Let's recap. First, chatbots predict likely text, so they can produce confident answers that are false, including invented sources. This is a hallucination. Second, deepfakes are AI-made images, voices or videos that can make false stories look real. Third, check claims against a trusted source, open every source yourself, and slow down when content makes you feel a strong emotion.

Now it is your turn. In the exercise below this video, you will ask a chatbot three factual questions about your own country or industry, check every answer against a trusted source, and record each error you find. It takes about twenty minutes. In the next lesson, we will look at privacy, and what happens to the data you share. See you there.
```

## L05 Privacy: What Happens to the Data You Share

- **Filename:** `ai-29-ai-ethics-bias-and-safety_M1_L05_presenter.mp4`
- **Expected length:** about 5.0 minutes (691 words). The quality gate accepts ±10%.

```text
You would not read a patient's medical notes aloud in a busy café. But when you paste the same notes into a chatbot, where do they go, who can see them, and how long do they stay there?

When you type into an AI tool, your text is sent to the company that runs it. Depending on the tool, the plan and your settings, that text may be stored in your chat history, reviewed by people at the company, or used to improve the service, which can include training future models.

Settings differ between tools and plans, and they change often. Many tools let you control chat history or training, but you have to look for these settings. So check the tool and your organisation's rules before you share anything sensitive.

Two kinds of data need special care. Personal data is any information about a person who can be identified, such as a name, phone number, photo, address, health details or bank details. Confidential data is information your organisation or client has not made public, such as contracts, prices, plans and passwords.

And removing names is often not enough. Think of a forty-seven-year-old female teacher at the only secondary school in a small town, admitted with a broken wrist. There is no name, but many people in that town would know who it is.

So ask one question. Does the AI need this detail to do the task? Often it does not. You can replace real details with placeholders, describe a general situation instead of a real case, or use tools your organisation has approved. The task still gets done, but the private details stay with you.

Typing into an AI tool is like sending a letter through a large postal company. Most letters arrive safely. But depending on the service, the letter may be opened for checks, copied or kept in an archive. You would not put your bank PIN in a normal letter. Apply the same care to what you type.

Let's look at an example. Maricel Santos is a nurse at a hospital in the Philippines. At the end of a long shift, she wants a quick summary of a patient's notes for the next shift. She is tired, and she wants to save time.

The risky way. She pastes the full notes, with the patient's name, age, address, diagnosis and medicines, into a free public chatbot. The summary is useful. But she has now shared a patient's health data with an outside service that her hospital has not approved.

The better way. Maricel realises the chatbot does not need the patient's details at all. What she really needs is a clear handover structure. So she asks for a short template for a general adult patient, with headings for condition, medicines, observations, concerns and next actions.

The chatbot gives her a template. She fills it in herself, on the hospital's own system. The patient data never leaves the hospital. She gets the help she needed, and she protects her patient.

A common mistake is to think that removing a name, or deleting a chat afterwards, makes a prompt safe. Instead, decide what to share before you type. As you saw, a person can be identified from other details. Remove every detail the task does not need, and use approved tools for sensitive work. Legal duties about personal data are covered in course AI thirty.

Let's recap. First, what you type into an AI tool may be stored, reviewed or used to improve the service, depending on the tool, the plan and your settings. Second, personal and confidential data need special care, and removing names alone is often not enough. Third, before you type, ask whether the AI needs each detail. Use placeholders, general descriptions or approved tools instead.

Now it is your turn. In the exercise below this video, you will find the data and chat-history settings in your chatbot, and rewrite one work prompt so it has no personal or confidential data. It takes about twenty minutes. That completes week one. In the next lesson, we will look at safety risks and human oversight. See you there.
```

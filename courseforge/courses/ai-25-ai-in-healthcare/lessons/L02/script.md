# L02 Health Data: Types, Quality and Privacy | Presenter Script

Course: AI-25 · Video: 5 min · Words: 731

## Hook
An AI tool is only as good as the data it learned from. If blood pressure was missing for half of the older patients in the training data, what has the tool really learned about older patients?

## Explain
In the last lesson, we mapped four areas of AI in healthcare. Every one of them runs on data. So in this lesson, we look at the main types of health data, the quality problems they bring, and why they need extra privacy protection.

Health AI uses six main types of data. Electronic health records are rich, but often incomplete, and recorded for care or billing, not research. Images depend on the device and the person taking them. Laboratory results are well structured, but units and methods differ between laboratories.

Wearables give continuous readings, but the people who own them are often younger and wealthier than the general population. Claims data is large and consistent, but shows what was paid for, not always what happened. Surveys reach people who do not use health services, but depend on memory and honest answers.

Three quality problems appear again and again. First, missing values. Data is rarely missing at random. A test may be missing because the clinician thought it was not needed, and that is information too. Second, different coding systems. Combining hospitals that record diagnoses differently creates errors. Third, unrepresentative samples. A model may work less well for groups that are rare in its data.

Health data can reveal illness, pregnancy, mental health or genetic information. Exposure can lead to discrimination, stigma or loss of work. Here is a simple way to think about it. A patient record is like a diary. In the hands of the patient's care team, it helps. In the wrong hands, it can cause real harm.

So treat every dataset as someone's diary, even when it looks like a table of numbers. In this course, you only use public or synthetic data. Synthetic data is made by a computer to look realistic, but it describes no real person. And never paste identifiable patient data into a public AI tool.

## Demonstrate
Let's see this with an example. Nguyen Thi Lan is a public health researcher in Vietnam. She is given a synthetic dataset of five hundred adult clinic patients, to plan an analysis of blood pressure control. Before any modelling, she explores it.

She lists the variables: age, sex, district, body mass index, systolic blood pressure, smoking status, HbA1c, and the date of the last visit. Then she counts the missing values. Remember, all of these numbers are synthetic. Smoking status is missing for thirty-one percent of patients. HbA1c for fifty-eight percent. Body mass index for twelve percent. Systolic blood pressure for four percent.

HbA1c is missing for more than half of the patients. Lan checks, and sees that it is recorded mostly for patients who already have a diabetes diagnosis. A model trained on this data might learn that HbA1c present means diabetes. That is a pattern in the recording process, not in the patients.

She also sees that eighty percent of rows come from two urban districts. She writes a note: results may not apply to rural districts. Finally, she asks the privacy question. If this data were real, could a person be identified? District, exact age and a rare diagnosis together could point to one person in a small district.

For real data, she would group ages into bands, remove exact dates, and follow her institution's data protection rules. This links to a common mistake. Many people believe data is anonymous once names are removed. In health data, this is often false. Treat de-identified data as still sensitive.

## Recap
Let's recap. First, health AI uses records, images, laboratory results, wearables, claims and surveys, and each type has its own gaps and biases. Second, missing values, different coding systems and unrepresentative samples can teach a model patterns from the recording process, not from patients. Third, health data needs extra privacy protection, and identifiable data never goes into public AI tools.

## CTA
Now it is your turn. In the exercise below this video, you will open the course's synthetic patient dataset, list its variables, count the missing values, and describe one privacy risk if the data were real. It takes about twenty-five minutes. In the next lesson, we look at how clinical AI models are built. See you there.

## Thumbnail
Headline: Every Record Is a Diary
Image: Navy background, a closed notebook with a small lock beside a table of numbers with some empty cells highlighted in teal, headline in teal Inter Bold.

## Production Notes
- All figures are synthetic. The dataset slides use the course file assets/synthetic_patients.csv (500 fictional patients, labelled 'synthetic, for teaching'). Show the header row and a few rows only; keep the 'SYNTHETIC DATA FOR TEACHING ONLY' label visible on every data slide.
- Missing-data figures spoken in the script match assets/synthetic_patients_README.md: smoking status 31%, HbA1c 58%, BMI 12%, systolic blood pressure 4%; 400 of 500 rows (80%) from the two urban districts.
- [VERIFY] [VERSION] The WHO Global Health Observatory is named in content.md as a public aggregated source. It is left out of the voiceover; confirm its name, scope and licence before adding it to any on-screen text.
- Nguyen Thi Lan (Vietnam) is fictional. Stock footage must show no readable patient records.

# L09 Bias, Equity and Dataset Shift | Presenter Script

Course: AI-25 · Video: 5 min · Words: 738

## Hook
A tool reports an overall sensitivity of eighty percent. That single number can hide a tool that finds ninety percent of cases in one group of patients, and only sixty-five percent in another. Who are the patients inside that missing thirty-five percent?

## Explain
In the last lesson, we saw how generative AI can fail inside a single document. Now we look at how a tool can fail whole groups of patients. A tool's performance can differ between groups and between care settings, and two related problems cause this.

The first problem is bias across patient groups. Performance may differ by sex, age, skin tone, ethnicity, language, disability or income. One cause is under-representation, where some groups appear rarely in the training data. Another is label bias, where the correct answers reflect unequal care. For example, if one group was diagnosed later in the past, the labels teach the model that pattern.

A third cause is proxy variables. Something like past healthcare cost or postcode can stand in for income or ethnicity, and carry existing inequality into predictions. A fourth cause is measurement differences, where some devices work less well for some groups, for example image quality on different skin tones.

The second problem is dataset shift. Performance can fall when the setting changes after training. The population may change, with different ages, disease mix or prevalence. Equipment and processes may change, such as new scanners or laboratory methods. And over time, clinical practice and coding rules change too.

So the practical rule is simple. Never accept one overall figure. Ask for results broken down by patient group and by site, with the number of patients in each group, because figures from small groups are uncertain.

Here is a way to picture it. A shoe factory that measures only city customers may make excellent shoes that fit badly on people who walk long distances on rough roads. The shoes are not bad, but they were not designed or tested for everyone who will wear them.

## Demonstrate
Let's look at a hypothetical case. Doctor Neema Mwakasege works for a regional health authority in Tanzania. A supplier offers a tool that flags chest X-rays that may show tuberculosis, for clinician review. It was developed with data from large city hospitals using fixed digital X-ray machines.

The region wants to use it in rural clinics. These clinics use portable machines, and serve more older patients and more people living with HIV. So Neema asks for a synthetic local check, set up to show the risk.

Remember, these figures are synthetic. In the city hospitals, two hundred patients have the condition, and the tool flags one hundred and eighty-four. That is a sensitivity of ninety-two percent. In the rural clinics, one hundred and fifty patients have the condition, and the tool flags one hundred and fourteen. That is a sensitivity of seventy-six percent.

So the tool misses about one in four cases in rural clinics, compared with about one in twelve in city hospitals. Possible reasons include image quality from portable machines, a different patient mix, and a different disease appearance in people living with HIV.

Neema does not simply reject the tool. She asks the supplier for results by device type and by HIV status. She requests a local silent-mode test in three rural clinics. And she makes it clear that clinicians must not treat a negative result from the tool as ruling out disease.

A common mistake is to think that removing sex or ethnicity from the data makes a model fair. It does not. Other variables, such as postcode or device type, can carry the same information. Fairness has to be measured in the results for each group, not assumed.

## Recap
Let's recap. First, performance can differ across patient groups because of under-representation, label bias, proxy variables and measurement differences. Second, dataset shift in population, equipment, process or time can reduce performance in a new setting. Third, always ask for results by patient group and by site, with group sizes, and never rely on one overall figure.

## CTA
Now it is your turn. In the exercise below this video, you will compare sensitivity across three patient groups and two sites in a synthetic results table, and write three questions for the tool's supplier. It takes about twenty-five minutes. In the next lesson, we look at patient safety and failure modes. See you there.

## Thumbnail
Headline: One Number Hides Many
Image: Navy background, one large figure 80% splitting into smaller bars of different heights for different patient groups and sites, the shortest bar in teal, headline in teal Inter Bold.

## Production Notes
- All figures are synthetic; the voiceover says so where numbers appear. On-screen numbers must match content.md: city hospitals 200 with the condition, 184 flagged, sensitivity 92.0%; rural clinics 150 with the condition, 114 flagged, sensitivity 76.0%. Hook figures (80% overall, 90% and 65% by group) are illustrative. Calculations were checked with python3 in Stage 2.
- [VERIFY] Published real cases of bias or dataset shift in health AI are left out of the script. Add any real case only after checking it against its source.
- Dr. Neema Mwakasege, the Tanzanian health authority and the tuberculosis tool are hypothetical. X-ray images on slides must be generic illustrations with no readable patient details.
- The script tells clinicians not to treat a negative result as ruling out disease, which is a statement about the tool's limits, not clinical advice. A clinical reviewer may wish to confirm this wording.

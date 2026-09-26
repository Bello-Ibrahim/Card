# Screen Demo Pack: AI-24 L07 Measuring and Reducing Bias

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-24-ai-in-finance-and-fintech_L07_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show the course page and click the ready-made notebook link
2. The notebook opens in Google Colab; point to the title and the single code cell

**Narration over this clip (for pacing)**

> Let's see this in Google Colab. Alejandro Ruiz is a risk analyst at Crédito Solar, a hypothetical consumer lender in Mexico. He uses the course's ready-made notebook, with one thousand three hundred synthetic loan decisions. No coding is needed. First, open the notebook link from the course page.

## Clip 2: scene 8

- **Filename:** `ai-24-ai-in-finance-and-fintech_L07_screen_2.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Open the File menu
2. Click Save a copy in Drive
3. Show the new tab with the copy's name

**Narration over this clip (for pacing)**

> Next, save your own copy. Open the File menu and choose Save a copy in Drive. Now you can change it without affecting anyone else.

## Clip 3: scene 9

- **Filename:** `ai-24-ai-in-finance-and-fintech_L07_screen_3.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Scroll slowly through the code cell
2. Highlight the counts line
3. Highlight the lines that calculate approval_rate, false_rejection_rate and bad_loans_approved_rate
4. Highlight the final print line for the approval-rate ratio

**Narration over this clip (for pacing)**

> Here is what the code does. The first line lists how many applicants in each group repaid or not, and were approved or not. The rest builds a table and calculates three rates for each group, plus the approval-rate ratio. You do not need to change any of it yet.

## Clip 4: scene 10

- **Filename:** `ai-24-ai-in-finance-and-fintech_L07_screen_4.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Open the Runtime menu
2. Click Run all
3. Wait for the output table to appear under the cell
4. Split screen briefly with the lesson page table to show the numbers match

**Narration over this clip (for pacing)**

> Now open the Runtime menu and choose Run all. Wait a few seconds until the output table appears under the code. Check that your numbers match the table on the lesson page.

## Clip 5: scene 11

- **Filename:** `ai-24-ai-in-finance-and-fintech_L07_screen_5.mp4`
- **Target length:** about 26 seconds

**Steps**

1. Zoom in on the output table
2. Highlight approval_rate: A 0.725, B 0.560
3. Highlight Approval-rate ratio: 0.772
4. Highlight false_rejection_rate: A 0.133, B 0.264
5. Highlight bad_loans_approved_rate: A 0.300, B 0.107

**Narration over this clip (for pacing)**

> Group B's approval rate is fifty-six percent, against seventy-two point five percent for Group A. The ratio is zero point seven seven two. Group B's good payers are declined about twice as often: twenty-six point four percent, against thirteen point three. But the model approves far fewer bad loans for Group B: ten point seven percent, against thirty.

## Clip 6: scene 12

- **Filename:** `ai-24-ai-in-finance-and-fintech_L07_screen_6.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Keep the output table on screen
2. Draw a teal box around Group B false_rejection_rate
3. Show a short caption: Main measure: false rejection rate

**Narration over this clip (for pacing)**

> So both analysts were right. Alejandro reports the false rejection rate to his credit committee as the main measure, because it shows good customers being turned away. He recommends human review for Group B applications near the threshold.

## Clip 7: scene 13

- **Filename:** `ai-24-ai-in-finance-and-fintech_L07_screen_7.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Click in the counts line
2. Change 95 to 45
3. Change 265 to 315
4. Open Runtime and click Run all
5. Highlight the new ratio 0.91 and Group B false_rejection_rate 0.125

**Narration over this clip (for pacing)**

> Finally, try a change. In the counts line, change the number ninety-five to forty-five, and two hundred and sixty-five to three hundred and fifteen. Run all again. The ratio rises to zero point nine one, and Group B's false rejection rate falls to twelve point five percent.

## Production notes for this lesson

- [REGION] [VERIFY] The 'four-fifths' ratio comes from US employment practice and is not a general credit rule. The script presents it only as a rough rule of thumb and says it is not a legal safe harbour for lending; keep that wording and do not show any legal citation on screen.
- [VERSION] Google Colab free-tier limits and menu names (File > Save a copy in Drive, Runtime > Run all) must be checked against the live tool before recording.
- Screen demo: follow content.md Exercise steps 1 to 6 with the course's ready-made notebook on the 1,300 synthetic loan decisions. Record in a clean Google account with no personal files visible.
- Output figures must match content.md exactly: Group A 800 applicants, approval 0.725, false rejection 0.133, bad loans approved 0.300; Group B 500, 0.560, 0.264, 0.107; ratio 0.772 (spoken 'zero point seven seven two'). After the step 6 edit: ratio 0.91 and Group B false rejection 12.5%.
- Alejandro Ruiz and Crédito Solar are fictional. The presenter describes the code; it is never read aloud.

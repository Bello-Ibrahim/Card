# L06 Text-to-Video in Google Flow (Veo)

Course: AI-21 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Today you generate your first real clips. The goal is not one lucky result. The goal is a method: change one thing at a time, and learn what each change does.

## Explanation
Google Flow is a web tool for AI filmmaking that uses Google's Veo video models [VERSION]. You write a prompt, choose settings, generate clips and can extend a scene. Model versions, features, credit costs and plans change often [VERSION], and Flow is not available in every country [REGION]. If you cannot access Flow, use the text-to-video mode in Kling (L07) as a fallback [VERSION] [REGION]. The method in this lesson works in any text-to-video tool.

**Before you start:**

- Sign in with a personal Google account [VERSION]. Check the age and country requirements on the Flow page [VERIFY] [REGION].
- Check how many credits you have and what one generation costs [VERSION]. Faster or higher-quality models may cost more credits.
- Have your prompts from L04 ready in a text document.
- Do not type personal or confidential information into prompts.

**The one-change method.** When a clip is not right, do not rewrite the whole prompt. Change one element (the camera, the lighting or the action) and generate again. Keep a simple log: attempt number, what you changed, and what happened. After a few attempts, you know which words work for this model.

**Watermarks and labels.** Videos generated with Veo may carry an invisible watermark, and some plans may add a visible one [VERIFY] [VERSION]. Do not try to remove watermarks; they help viewers know content is AI-generated. Lesson 13 covers disclosure.

**Analogy:** Think of a scientist testing a plant. If she changes the water, the light and the soil at once and the plant grows better, she does not know why. If she changes only the light, she learns something she can use again. Prompting works the same way.

## Worked Example
Ingrid makes videos for a hypothetical outdoor-gear shop in Tromsø, Norway. Her shot list needs "Wide | A hiker walks along a snowy ridge | Mountains at dawn". The presenter follows these on-screen steps. Button names and positions may differ in the live tool [VERSION].

1. Open Flow in a web browser and sign in.
2. Create a **new project** and name it "Ridge test".
3. Choose the **text-to-video** mode [VERSION].
4. Open the **settings** panel. Choose the model, the aspect ratio (16:9) and the number of outputs per prompt [VERSION]. Note the credit cost shown [VERSION].
5. Paste the prompt and click **Generate**:

```text
A hiker in a red jacket walks along a snowy mountain ridge. Wide shot of jagged peaks at dawn. Slow pan from left to right following the hiker. Soft pink and blue dawn light. Realistic cinematic style, natural colours. 8 seconds.
```

6. Wait for the results. Play each clip twice: once for the whole picture, once for details such as feet, snow and the horizon.
7. Attempt 1: the hiker's legs blur at the end. Ingrid writes this in her log.
8. Attempt 2: she changes only the action to "walks slowly and steadily". The legs are clearer.
9. Attempt 3: she changes only the camera to "static wide shot". The motion is calmer, but the shot feels flat, so she keeps the pan from attempt 2.
10. She uses **extend** on the best clip to add a few seconds where the hiker stops and looks at the view [VERSION].
11. She **downloads** the chosen clip and checks the available resolution and any watermark [VERSION].
12. She renames the file with the shot number, for example "S03_ridge_v2.mp4", and saves the prompt with it.

Her log shows that the action word "slowly" did more for quality than any style word.

## Common Mistake
Many learners press **Generate** again and again with the same prompt, hoping for a better result. Sometimes this works, but it spends credits and teaches you nothing. Others change five things at once, then cannot repeat a good result. Change one element per attempt and log it.

## Key Takeaways
1. Flow generates clips from text prompts with Veo models, but features, credits and availability change, so check the live tool and have a fallback.
2. Change one element per attempt and log what you changed and what happened.
3. Name files by shot number and save each prompt with its clip, and never try to remove watermarks.

## Hands-on Exercise
**Task:** Generate 2 shots from your shot list in Google Flow and record which prompt changes improved the result.
**Tools:** Google Flow (Veo) with a personal Google account [VERSION] [REGION]; fallback: Kling text-to-video [VERSION]; your prompts from L04; a log table.
**Steps:**
1. Choose 2 shots with different shot types from your shot list.
2. Open Flow, create a project and select text-to-video [VERSION].
3. Set the aspect ratio of your final video and note the credit cost [VERSION].
4. Generate shot 1 with your L04 prompt. Watch the result twice.
5. Write one problem in your log, change one element of the prompt, and generate again. Repeat up to 3 times.
6. Repeat steps 4 and 5 for shot 2.
7. Download the best clip for each shot, name it by shot number, and save the prompt with it.
**What good looks like:** 2 usable clips and a log of at least 4 attempts, where each row names one change and its effect, and the final prompts are saved.
**Time:** about 35 minutes

## Review Flags
- [VERSION] Flow interface details must be checked against the live tool before scripting: project creation, the text-to-video mode name, the settings panel, model choices, outputs per prompt, credit costs, the extend feature, download resolutions and plan names.
- [VERSION] Kling's text-to-video mode as a fallback must be confirmed as available on the free tier.
- [REGION] Google Flow availability differs by country; learners outside supported countries need the fallback tool.
- [VERIFY] Age and account requirements for Flow, and whether generated videos carry an invisible and/or visible watermark on the learner's plan, must be confirmed from current official information.

# L06 Cleaning Up Recordings in Audacity | Presenter Script

Course: AI-22 · Video: 5 min · Words: 684

## Hook
You recorded a great interview. But when you play it back, you hear a fan, long gaps, and some words much louder than others. Listeners notice this in seconds. The good news is, a free editor and a simple order of steps can fix most of it.

## Explain
Welcome to week two. Audacity is a free, open-source audio editor. We use it for a clean-up chain. That is a fixed order of steps that you apply to every voice recording. The order matters, because each step prepares the audio for the next one.

Here is the chain. One, listen and look at the waveform, and find a quiet section. Two, remove background noise. Three, cut mistakes and long silences. Four, even out the levels. Five, reduce harsh sounds. And six, compare with the original and export.

Three tools do most of the work. Noise Reduction lowers background sound, but only with gentle settings, or the voice sounds thin and metallic. A compressor reduces the gap between loud and quiet words. And an equaliser, or EQ, can gently lower harsh high sounds, like strong s sounds.

Audacity can also use optional AI plugins, for example for noise suppression. But the basic chain in this lesson is all you need for this course.

Think of it like editing a photo. You fix the light and remove dust first, and only then add filters. If you add a filter to a dark, dusty photo, the problems become stronger. In audio, you remove noise and fix levels before anything creative.

## Demonstrate
Let's clean a real recording. Hina records a poetry podcast at home in Lahore, in Pakistan. Her one-minute test has a ceiling fan hum, two long pauses and some quiet lines.

She opens Audacity, drags in her recording, and saves a copy of the original first. Then she listens with headphones, and looks at the waveform. Before she starts speaking, there are two seconds of fan noise. That is her noise floor.

Noise Reduction works in two passes. She selects the two quiet seconds and lets the effect learn the noise profile. Then she selects the whole track, keeps gentle settings, and previews before she applies it. The fan hum becomes almost silent, and her voice still sounds natural.

Next, she deletes a false start, where she began a line and stopped. She uses Truncate Silence to shorten the two long pauses to under one second. But she keeps short, natural pauses, because speech with none sounds rushed.

To even out the levels, she applies Compressor with the default settings. This reduces the difference between loud and quiet words. Then she uses Normalize, so the loudest point stays just below the top. You will set the final loudness in lesson nine.

Her s sounds are sharp on headphones, so she uses Filter Curve EQ to lower the high frequencies slightly. Small changes only. Finally, she plays the original and the cleaned version one after the other, and exports a WAV file.

Hina writes one note for each step. Noise reduction removed the fan. Truncate Silence made the pace tighter. Compressor and Normalize made quiet lines easier to hear. And the EQ made the s sounds softer.

The most common mistake is too much noise reduction. Push the settings high, and the voice starts to sound robotic, thin or underwater. A little background noise is much less distracting than a damaged voice. So use gentle settings, preview, and compare.

## Recap
Let's recap. First, use a fixed chain: listen, remove noise, cut mistakes and silences, even out levels, reduce harsh sounds, then compare and export. Second, noise reduction learns the noise from a quiet section, then removes it from the whole file. Third, always keep the original, and compare before and after.

## CTA
Now it is your turn. In the exercise below this video, you will clean up a noisy one-minute voice recording in Audacity. Use your own, or the practice file on the course page. Then describe what each step changed. It takes about thirty minutes. In the next lesson, Generating Music Beds with AI, we add music.

## Thumbnail
Headline: Clean Audio in Six Steps
Image: Navy background, a messy grey waveform on the left turning into a clean teal waveform on the right, with a small numbered chain of six dots between them, headline in teal Inter Bold.

## Production Notes
- Screen demo tool: Audacity (DECISIONS.md). [VERSION] Before recording, check platform support, menu paths and effect names (Effect > Noise Removal and Repair > Noise Reduction, Get Noise Profile, Preview, Truncate Silence, Compressor, Normalize, Loudness Normalization, Filter Curve EQ, File > Export Audio), shortcuts, export formats and optional AI plugins against the current release. If a menu path has changed, film the current path; the voiceover names effects, not menu paths.
- The noisy 1-minute demo recording (Hina's test, with ceiling-fan hum, a false start, two long pauses and some quiet lines) and the noisy practice recording for learners on the course page are recorded by the team with Audacity, using consenting staff (DECISIONS.md: human production needed).
- Screen scenes should let learners hear short before and after snippets of each step at a low level under the presenter, or in short gaps.
- Hina and her Lahore poetry podcast are fictional. Pronunciation: Hina = HEE-na; Lahore = la-HOR.
- Optional AI plugins are mentioned in general terms only [VERSION]; do not show or name a specific plugin.

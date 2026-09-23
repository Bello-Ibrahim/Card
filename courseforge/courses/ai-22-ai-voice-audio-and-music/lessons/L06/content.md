# L06 Cleaning Up Recordings in Audacity

Course: AI-22 · Module: M2 · Objectives: O4, O5 · Video: 5 min (screen demo)

## Hook
You recorded a great interview, but when you play it back you hear a fan humming, long gaps while you checked your notes, and some words much louder than others. Listeners notice these problems in the first few seconds. The good news is that a free editor and a simple order of steps can fix most of them.

## Explanation
**Audacity** is a free, open-source audio editor for Windows, macOS and Linux [VERSION]. We use it for a simple **clean-up chain**: a fixed order of steps that you apply to every voice recording. The order matters, because each step prepares the audio for the next.

**Step 1: Listen and look.** Play the recording with headphones. Look at the waveform (the shape of the sound). Find a section of 1 or 2 seconds where nobody is speaking. The sound there is your **noise floor**, which you met in L01.

**Step 2: Remove background noise.** Audacity's Noise Reduction effect works in two passes. First you select a quiet section and let it learn the noise profile. Then you select the whole recording and apply the effect [VERSION]. Use gentle settings. Too much noise reduction makes a voice sound thin, metallic or "underwater".

**Step 3: Cut mistakes and long silences.** Delete false starts, coughs and repeated sentences. Shorten long pauses by hand or with Truncate Silence [VERSION]. Keep short, natural pauses; speech with none sounds rushed.

**Step 4: Even out the levels.** A **compressor** reduces the difference between loud and quiet words. Then **Normalize** or **Loudness Normalization** raises the whole recording to a consistent level [VERSION]. You set the final loudness in L09.

**Step 5: Reduce harsh sounds.** Strong "s" and "sh" sounds, or a sharp tone in the voice, can be tiring on headphones. An equaliser (EQ), such as Audacity's Filter Curve EQ, can gently lower the harsh high frequencies [VERSION]. Make small changes only.

**Step 6: Compare and export.** Listen to the original and the cleaned version one after the other. Then export as WAV for further editing, or MP3 for sharing [VERSION].

Audacity can also use optional AI plugins, for example for noise suppression [VERSION]. The basic chain above is enough for this course.

**Analogy:** Cleaning audio is like editing a photo. You fix the light and remove dust first, and only then add filters. If you add a filter to a dark, dusty photo, the problems become stronger. In audio, you remove noise and fix levels before any creative effects.

## Worked Example
Hina records a poetry podcast at home in Lahore, Pakistan. Her 1-minute test recording has a ceiling fan hum, two long pauses and some quiet lines. The presenter follows her steps on screen:

1. She opens Audacity and drags her recording into the window. She saves a copy of the original file.
2. She plays it with headphones and finds 2 seconds of fan noise before she starts speaking.
3. She selects those 2 seconds, opens **Effect > Noise Removal and Repair > Noise Reduction** and clicks **Get Noise Profile** [VERSION].
4. She selects the whole track (Ctrl+A, or Cmd+A on a Mac), opens Noise Reduction again, keeps gentle settings and clicks **Preview**, then **OK** [VERSION]. The fan hum becomes almost silent, and her voice still sounds natural.
5. She deletes a false start and uses **Truncate Silence** to shorten two long pauses to under 1 second [VERSION].
6. She applies **Compressor** with the default settings, then **Normalize** so the loudest point stays below 0 dB [VERSION].
7. Her "s" sounds are sharp, so she uses **Filter Curve EQ** to lower the high frequencies slightly [VERSION].
8. She plays the original and the cleaned version one after the other, then exports the result with **File > Export Audio** as a WAV file [VERSION].

Her notes: "Noise reduction removed the fan. Truncate Silence made the pace tighter. Compressor and Normalize made quiet lines easier to hear. EQ made the 's' sounds softer."

## Common Mistake
The most common mistake is using too much noise reduction. Beginners push the settings high to remove every trace of noise, and the voice starts to sound robotic and strange. A little background noise is much less distracting than a damaged voice. Use gentle settings, preview, and compare with the original.

## Key Takeaways
1. Use a fixed clean-up chain: listen, remove noise, cut mistakes and silences, even out levels, reduce harsh sounds, then compare and export.
2. Noise reduction first learns the noise from a quiet section, then removes it from the whole file; gentle settings protect the voice.
3. Always keep the original file and compare before and after, so you can hear what each step changed.

## Hands-on Exercise
**Task:** Clean up a noisy 1-minute voice recording in Audacity and describe what each step changed.
**Tools:** Audacity (free) [VERSION]; a 1-minute recording of your own voice with some background noise, or the practice file on the course page; headphones.
**Steps:**
1. Open the recording in Audacity and save a copy of the original.
2. Find a quiet section and get a noise profile with Noise Reduction [VERSION].
3. Apply Noise Reduction to the whole file with gentle settings. Preview first.
4. Delete mistakes and shorten long silences by hand or with Truncate Silence [VERSION].
5. Apply Compressor, then Normalize or Loudness Normalization [VERSION].
6. If "s" sounds are harsh, lower the high frequencies slightly with an EQ [VERSION].
7. Compare the original and cleaned files, then export the cleaned version as WAV.
8. Write one sentence for each step describing what you heard change.
**What good looks like:** A cleaned file where background noise is clearly lower but the voice still sounds natural, long silences are shorter, and levels are even. Your notes describe a specific change for each step, such as "the fan hum is gone" or "quiet lines are now clear".
**Time:** about 30 minutes

## Review Flags
- [VERSION] Check Audacity platform support, menu paths, effect names (Noise Reduction, Get Noise Profile, Truncate Silence, Compressor, Normalize, Loudness Normalization, Filter Curve EQ, Export Audio), shortcuts, export formats and optional AI plugins against the current release before scripting.
- Curriculum flag carried: L06 [VERSION] Audacity menus and optional AI plugins may change. Production note: a noisy practice recording for learners must be provided on the course page.

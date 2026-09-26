# Screen Demo Pack: AI-22 L06 Cleaning Up Recordings in Audacity

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-22-ai-voice-audio-and-music_L06_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open Audacity and drag the recording into the window
2. Save a copy of the original file
3. Play the recording with headphones
4. Zoom in on the first two seconds: a thin band of fan noise before the voice starts

**Narration over this clip (for pacing)**

> She opens Audacity, drags in her recording, and saves a copy of the original first. Then she listens with headphones, and looks at the waveform. Before she starts speaking, there are two seconds of fan noise. That is her noise floor.

## Clip 2: scene 9

- **Filename:** `ai-22-ai-voice-audio-and-music_L06_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Select the two seconds of fan noise
2. Open Effect > Noise Removal and Repair > Noise Reduction and click Get Noise Profile
3. Select the whole track with Ctrl+A, or Cmd+A on a Mac
4. Open Noise Reduction again, keep gentle settings and click Preview
5. Click OK and play a few seconds: the hum is almost gone

**Narration over this clip (for pacing)**

> Noise Reduction works in two passes. She selects the two quiet seconds and lets the effect learn the noise profile. Then she selects the whole track, keeps gentle settings, and previews before she applies it. The fan hum becomes almost silent, and her voice still sounds natural.

## Clip 3: scene 10

- **Filename:** `ai-22-ai-voice-audio-and-music_L06_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Select the false start at the beginning and press Delete
2. Select the whole track and open Truncate Silence
3. Set long pauses to be shortened to under one second, then click Apply
4. Show the two gaps in the waveform are now shorter

**Narration over this clip (for pacing)**

> Next, she deletes a false start, where she began a line and stopped. She uses Truncate Silence to shorten the two long pauses to under one second. But she keeps short, natural pauses, because speech with none sounds rushed.

## Clip 4: scene 11

- **Filename:** `ai-22-ai-voice-audio-and-music_L06_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Select the whole track and apply Compressor with default settings
2. Apply Normalize so the peak stays below 0 dB
3. Show the waveform: quiet lines are now closer in size to loud ones

**Narration over this clip (for pacing)**

> To even out the levels, she applies Compressor with the default settings. This reduces the difference between loud and quiet words. Then she uses Normalize, so the loudest point stays just below the top. You will set the final loudness in lesson nine.

## Clip 5: scene 12

- **Filename:** `ai-22-ai-voice-audio-and-music_L06_screen_5.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Open Filter Curve EQ and lower the high frequencies slightly
2. Preview, then click Apply
3. Play ten seconds of the original copy, then the same ten seconds of the cleaned track
4. Choose File > Export Audio and export as WAV

**Narration over this clip (for pacing)**

> Her s sounds are sharp on headphones, so she uses Filter Curve EQ to lower the high frequencies slightly. Small changes only. Finally, she plays the original and the cleaned version one after the other, and exports a WAV file.

## Production notes for this lesson

- Screen demo tool: Audacity (DECISIONS.md). [VERSION] Before recording, check platform support, menu paths and effect names (Effect > Noise Removal and Repair > Noise Reduction, Get Noise Profile, Preview, Truncate Silence, Compressor, Normalize, Loudness Normalization, Filter Curve EQ, File > Export Audio), shortcuts, export formats and optional AI plugins against the current release. If a menu path has changed, film the current path; the voiceover names effects, not menu paths.
- The noisy 1-minute demo recording (Hina's test, with ceiling-fan hum, a false start, two long pauses and some quiet lines) and the noisy practice recording for learners on the course page are recorded by the team with Audacity, using consenting staff (DECISIONS.md: human production needed).
- Screen scenes should let learners hear short before and after snippets of each step at a low level under the presenter, or in short gaps.
- Hina and her Lahore poetry podcast are fictional. Pronunciation: Hina = HEE-na; Lahore = la-HOR.
- Optional AI plugins are mentioned in general terms only [VERSION]; do not show or name a specific plugin.

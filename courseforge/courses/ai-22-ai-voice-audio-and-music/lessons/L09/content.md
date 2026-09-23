# L09 Mixing Voice and Music

Course: AI-22 · Module: M2 · Objectives: O4, O5, O7 · Video: 5 min

## Hook
You have a clean voice and a music bed you like. Put them together without care, and the music may cover your words or suddenly stop. Put them together well, and the episode sounds finished and professional. The difference is a few simple mixing steps.

## Explanation
**Mixing** means combining separate audio tracks into one balanced file. For a podcast or narrated video, the main rule is simple: **the voice is on top**. Every other sound supports it.

A basic mix in Audacity has five steps.

**1. Arrange the tracks.** Put the voice on one track and the music on another. Place the music so it starts a few seconds before the first word, which gives the listener time to settle.

**2. Lower the music under speech.** When the voice is speaking, the music should be much quieter than the voice. You can lower the music by hand with the track's volume control or the **Envelope tool**, which lets you draw volume changes over time [VERSION]. Audacity also has an effect called **Auto Duck**, which lowers the music automatically whenever the voice track is playing [VERSION]. The music can be louder in the intro and outro, when nobody is speaking.

**3. Fade in and fade out.** A **fade** is a smooth change in volume. Use a short fade-in at the start of the music and a longer fade-out at the end. Never let music stop suddenly, unless the track has a clean ending of its own.

**4. Set consistent loudness.** Listeners should not need to change the volume between your episode and the next one. Platforms publish guidance on loudness, often measured in LUFS (loudness units relative to full scale) [VERIFY]. Follow the platform's current guidance for podcasts or video. Audacity's **Loudness Normalization** effect can bring the final mix to a target loudness [VERSION]. Apply it to the final mixed file, not to each track separately.

**5. Check on two systems and export.** Listen once on headphones and once on a phone speaker. Headphones show small details such as clicks and noise. A phone speaker shows whether the voice is still clear when bass disappears and the room is noisy. Then export the mix [VERSION].

**Analogy:** A mix is like a conversation at a dinner table with soft music in the room. The music helps the mood, but when someone speaks, everyone can hear them. If the music is too loud, guests lean in and stop listening.

## Worked Example
Marisol hosts a small-business podcast in Cebu, the Philippines. Her 3-minute episode has a cleaned recording of her voice, an AI music bed for the intro and outro, and a short TTS announcement about the next episode at the end.

Her steps in Audacity:

1. She imports the voice, the music and the TTS announcement onto three tracks.
2. She moves the voice so it starts 4 seconds after the music.
3. She selects the music track and applies **Auto Duck**, using the voice track to control it [VERSION]. She listens and finds the music still too strong, so she lowers the music track a little more.
4. She uses the **Envelope tool** to bring the music up again for 5 seconds after her last sentence, then adds a 3-second **Fade Out** at the end [VERSION].
5. She checks the TTS announcement. It is louder than her voice, so she lowers that track until they sound equal.
6. She exports a mixed WAV, opens it, applies **Loudness Normalization** with the target from her podcast host's current guidance, and exports the final MP3 [VERIFY] [VERSION].
7. She listens on headphones and on her phone speaker. On the phone, the music hides one quiet word at 1:12, so she lowers the music there and exports again.

She adds the final file name and date to her rights log.

## Common Mistake
Many beginners mix only on good headphones or only on laptop speakers. The mix sounds fine there but fails elsewhere: music too loud on a phone, or noise that was hidden by laptop speakers. Always check on at least two systems. Another common mistake is making the music bed too loud because the creator likes it. If a listener has to work to hear the words, the music is too loud.

## Key Takeaways
1. The voice is always on top: lower the music under speech by hand, with the Envelope tool or with Auto Duck.
2. Use fades at the start and end, and set the final loudness by following the platform's current guidance.
3. Check the mix on headphones and on a phone speaker before you export the final version.

## Hands-on Exercise
**Task:** Capstone step 1: mix your voiceover or recording with a music bed in Audacity and export a first draft.
**Tools:** Audacity (free) [VERSION]; your voice file (L03 or L06); your chosen music bed (L07); headphones and a phone.
**Steps:**
1. Import your voice and music onto separate tracks. Save the project.
2. Start the music 2 to 5 seconds before the first word.
3. Lower the music under speech with Auto Duck, the Envelope tool or the track volume [VERSION].
4. Add a fade-in at the start and a fade-out at the end of the music.
5. Export a mixed file, then apply Loudness Normalization following your platform's current guidance [VERIFY] [VERSION].
6. Listen on headphones and on a phone speaker. Write down any place where a word is hard to hear, and fix it.
7. Export the first draft and add it to your rights log.
**What good looks like:** A 2 to 4 minute draft where every word is clear over the music, the music fades smoothly in and out, the loudness follows the platform's guidance, and you have notes from both listening checks.
**Time:** about 35 minutes

## Review Flags
- [VERIFY] Platform loudness targets are taught as "follow the platform's current guidance"; no values are given. If specific LUFS values are added to the script, they must be checked against each platform's current official guidance. Confirm the LUFS definition wording.
- [VERSION] Audacity's Envelope tool, Auto Duck, Fade In/Fade Out, Loudness Normalization and export options must be checked against the current release before scripting.
- Curriculum flag carried: L09 [VERIFY] platform loudness targets, with any specific values checked before scripting.

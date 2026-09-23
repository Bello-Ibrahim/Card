# L01 How AI Hears and Speaks

Course: AI-22 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
Close your eyes and listen to a short advert on the radio. Was the voice a real person in a studio, or a computer? Was the music played by a band, or made by software in a few seconds? Today it can be hard to tell. This lesson explains what is happening inside the tools that make these sounds.

## Explanation
In this course we use three families of audio AI. Each one does a different job.

**Text-to-speech (TTS)** turns written text into spoken audio. You type a sentence, choose a voice, and the tool reads it aloud. Each voice comes from a **voice model**: a system that has learned how one voice, or one style of voice, sounds.

**Speech-to-text (STT)**, also called speech recognition, does the opposite. It listens to spoken audio and writes down the words. The result is a **transcript**. When the transcript has timings, so each line appears on screen at the right moment, it becomes **captions**. In L04 you will use a speech-to-text model called Whisper.

**Audio generation** creates new sound from a description. The type we use most is AI music: you describe the mood, genre, tempo and instruments, and the tool produces a short piece. A quiet piece of music that plays under a voice is called a **music bed**. Some tools also use AI to clean up recordings, for example to reduce background hiss.

All three families work in a similar way. They are trained on many hours of recorded sound, often with matching text or descriptions. During training the system does not store the recordings like a library. It learns patterns: how sounds follow each other, how a voice rises at the end of a question, how a word like "Tuesday" usually sounds, or how a calm piano piece usually moves. When you use the tool, it applies these patterns to your new text, audio or description.

**Analogy:** Think of a language learner who has listened to thousands of speakers on the radio for years. Now they can understand almost anyone who talks to them, and they can also imitate natural speech with the right rhythm and tone. They did not memorise every radio programme. They learned the patterns. Speech-to-text is the "understanding" side of this learner, and text-to-speech is the "imitating" side.

One more term will help you in later lessons. The **noise floor** is the level of quiet background sound in a recording when nobody is speaking, such as a fan, traffic or electrical hum. A low noise floor means a clean recording. AI clean-up tools try to lower the noise floor without damaging the voice.

Because these tools learn patterns, they also make pattern mistakes. A TTS voice may stress the wrong part of an unusual name. A transcript may write a similar-sounding word. A music tool may produce a piece with a strange ending. You will learn to listen for these problems and fix them.

## Worked Example
Tomás produces a weekly community radio programme in Valparaíso, Chile. He wants to use AI to save time, but first he wants to know which tool does which job.

He writes down his three tasks:

- He writes a short weather and events update every week, but he has no time to record it. This is **text-to-speech**: text goes in, a voice comes out.
- He interviews local fishermen and wants a written version for the station's website. This is **speech-to-text**: audio goes in, a transcript comes out.
- He needs a gentle 20-second music bed with acoustic guitar under his introduction. This is **audio generation**: a description goes in, new music comes out.

Tomás then lists one thing to check for each task. For the TTS update, he will listen for place names that the voice says wrongly. For the transcript, he will check names and numbers by hand. For the music, he will check that it is quiet and calm enough to sit under speech. He now has a simple plan before he opens any tool.

## Common Mistake
Many beginners think an AI voice "reads" like a person who understands the text. It does not understand meaning. It predicts how the words probably sound, based on patterns. This is why it may read "St." as "street" when you meant "saint", or read "2/3" as a date. The correction is to write clearly for the ear and always listen to the full result before you publish it.

## Key Takeaways
1. Text-to-speech turns text into voice, speech-to-text turns voice into a transcript, and audio generation creates new sound, such as a music bed, from a description.
2. These tools learn patterns from many hours of recorded sound; they do not understand meaning the way a person does.
3. Key terms for this course are voice model, transcript, captions, noise floor and music bed.

## Hands-on Exercise
**Task:** Listen to 4 short audio clips and decide for each one whether it is a human recording, AI speech or AI music, then check the answer key.
**Tools:** The 4 clips on the course page; headphones if you have them; pen and paper or a notes app.
**Steps:**
1. Play each clip twice. The first time, just listen. The second time, listen for details.
2. For each clip, write "human recording", "AI speech" or "AI music".
3. Write one clue for each decision, such as breathing sounds, very even rhythm, a wrongly stressed word, or a strange ending.
4. Write which family of audio AI (text-to-speech, speech-to-text or audio generation) would make each AI clip.
5. Check the answer key on the course page and note which clues were useful and which were not.
**What good looks like:** A decision and one specific clue for each of the 4 clips, the correct AI family for each AI clip, and a short note on which clues helped. Some wrong answers are normal, because good AI audio can be hard to tell apart from human recordings.
**Time:** about 15 minutes

## Review Flags
- None. The lesson uses general, hypothetical examples and makes no claims about specific tools. Production note: the 4 clips and answer key must be created for the course page, using only voices and music the team has the rights to use.

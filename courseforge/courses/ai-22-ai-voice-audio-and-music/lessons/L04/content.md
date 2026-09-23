# L04 Transcripts and Captions with Whisper

Course: AI-22 · Module: M1 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
Many people watch videos with the sound off, and many people cannot hear the audio at all. Captions help all of them. Typing captions by hand for a 10-minute video can take hours. With a speech-to-text model, you can have a first draft in minutes and spend your time checking it instead.

## Explanation
**Whisper** is a speech-to-text model released by OpenAI. It listens to audio and produces a transcript. It works in many languages and can also produce timed captions [VERIFY]. The model itself is free to download and run, and many free apps are built on it [VERSION].

There are two simple ways to use Whisper:

- **A free app.** Several free desktop and web apps let you open an audio file, choose a Whisper model and click a button to transcribe [VERSION]. This is the easiest option for most learners, and it is the one we show on screen. Where possible, choose an app that runs on your own computer, so the audio does not leave your device.
- **A local command (optional).** If you are comfortable with a terminal, you can install Whisper on your own computer and run one command [VERSION]. This option is not required for the course.

Whisper comes in several model sizes. Smaller models are faster but make more mistakes. Larger models are more accurate but slower and need a more powerful computer [VERSION]. For a 2-minute clip, a small or medium model on a normal laptop is usually a good start.

Whisper makes predictable kinds of mistakes. It often gets **names** wrong, especially names from other languages. It can mix up **numbers**, such as "fifteen" and "fifty". It may write a common word in place of a **technical term**. It can struggle with overlapping speakers, strong background noise and long silences, and it sometimes adds words that were never said. So you must always check the transcript by hand.

**Captions** are a transcript split into short lines with start and end times. The most common caption file format is **SRT**. An SRT file is plain text, and each caption looks like this:

```
12
00:00:41,200 --> 00:00:44,900
Today we visit a coffee farm near Manizales.
```

The number is the caption's position, the second line is the timing, and the third line is the text. Most video editors and video platforms accept SRT files [VERSION].

**Analogy:** Whisper is like a fast assistant who types everything they hear in a meeting. They are quick and usually right, but they do not know your guests' names or your industry's special words. You read their notes afterwards and correct them before anyone else sees them.

## Worked Example
Mateus is a science teacher in Recife, Brazil, who records short videos in Portuguese for his students. He wants captions for a 2-minute video about the water cycle. The presenter will follow his steps on screen:

1. He exports the audio of his video as a WAV or MP3 file.
2. He opens a free Whisper app on his computer [VERSION].
3. He chooses the audio file, sets the language to Portuguese and selects a medium model [VERSION].
4. He clicks the transcribe button and waits. The transcript appears with timestamps.
5. He plays the audio and reads the transcript at the same time. He finds four errors: "evapotranspiração" was split into two wrong words; a student's name, "Iara", was written as "Iara" in one place and "Yara" in another; "32 graus" was written as "30 e 2 graus"; and one sentence was repeated that he never said twice.
6. He corrects each error in the app's editor, or in a text editor.
7. He exports the result as an SRT file [VERSION].
8. He opens the SRT file in a text editor to check that each caption line is short and the timings look correct.
9. He imports the SRT into his video editor and watches the video once with captions on.

**Optional local command.** A teacher who prefers the terminal could install the open-source Whisper package and run one command like this [VERSION]:

```
whisper aula.mp3 --model medium --language pt --output_format srt
```

This creates an SRT file in the same folder. The package also needs a free audio tool called ffmpeg [VERSION].

## Common Mistake
Many beginners trust the transcript because most of it is correct. But the errors are usually in the most important words: names, numbers and key terms. One wrong number in a caption can change the meaning. Always check the transcript while listening. Also, do not upload recordings that contain other people's personal or confidential information to an online service without their permission. Prefer an app that runs on your own computer.

## Key Takeaways
1. Whisper is a free speech-to-text model that you can use through a free app or, optionally, a local command.
2. Always check names, numbers, technical terms and repeated or added sentences by hand while listening to the audio.
3. An SRT file contains numbered captions with start and end times, and most video editors and platforms accept it.

## Hands-on Exercise
**Task:** Transcribe a 2-minute recording with Whisper, correct every error you find, and export an SRT caption file.
**Tools:** A free Whisper app of your choice [VERSION] (optional: the Whisper command-line tool [VERSION]); a 2-minute recording of your own voice; a text editor; headphones.
**Steps:**
1. Record or choose 2 minutes of your own speech. Include at least one name, one number and one technical term from your field. Do not use recordings of other people without their permission.
2. Open the recording in a free Whisper app and set the language [VERSION].
3. Choose a small or medium model and transcribe.
4. Play the audio and read along. Mark every error.
5. Correct each error and keep a list: the wrong text, the correct text and the type (name, number, term or other).
6. Export the captions as an SRT file [VERSION].
7. Open the SRT in a text editor and check the numbers, timings and line length.
**What good looks like:** An SRT file with correct words, short caption lines and sensible timings, plus a list of every error you corrected, grouped by type. When you read the captions while listening, they match the audio.
**Time:** about 30 minutes

## Review Flags
- [VERIFY] Confirm that Whisper was released by OpenAI as an open-source, free-to-download model, that it supports many languages and can produce timed output, and that the "may add words that were never said" limitation is described accurately.
- [VERSION] A reviewer must choose the free Whisper app to demonstrate and check its interface, whether it runs locally, language and model-size options, editing and SRT export against the live app before scripting.
- [VERSION] Whisper model sizes and their speed and hardware needs, and the command-line syntax (`whisper <file> --model --language --output_format srt`) and ffmpeg requirement, must be checked against the current package documentation.
- [VERSION] Confirm that the target video editors and platforms accept SRT caption files.
- Curriculum judgement call carried: the command-line install may be too technical for this audience, so it is presented as optional; a reviewer should confirm this decision.

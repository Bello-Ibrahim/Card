# L04 Transcripts and Captions with Whisper

Course: AI-22 · Module: M1 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
Many people watch videos with the sound off, and some cannot hear the audio at all. Captions help all of them. Typing captions by hand can take hours. With a speech-to-text model, you get a first draft in minutes and spend your time checking it.

## Explanation
**Whisper** is a speech-to-text model released by OpenAI. It listens to audio and produces a transcript. It works in many languages and can also produce timed captions [VERIFY]. The model itself is free to download and run, and many free apps are built on it [VERSION].

There are two simple ways to use Whisper:

- **A free app.** Several free apps let you open an audio file, choose a Whisper model and click a button to transcribe [VERSION]. This is the easiest option, and the one we show on screen. Where possible, choose an app that runs on your own computer, so the audio does not leave your device.
- **A local command (optional).** If you are comfortable with a terminal, you can install Whisper and run one command [VERSION]. This is not required.

Whisper comes in several model sizes. Smaller models are faster but make more mistakes; larger ones are more accurate but slower [VERSION]. A small or medium model is usually a good start on a normal laptop.

Whisper makes predictable mistakes. It often gets **names** wrong, mixes up **numbers** such as "fifteen" and "fifty", and writes common words in place of **technical terms**. It can struggle with overlapping speakers and noise, and it sometimes adds words that were never said. Always check the transcript by hand.

**Captions** are a transcript split into short lines with start and end times. The most common caption file format is **SRT**. An SRT file is plain text, and each caption looks like this:

```
12
00:00:41,200 --> 00:00:44,900
Today we visit a coffee farm near Manizales.
```

The first line is the caption number, then the timing, then the text. Most video editors and platforms accept SRT files [VERSION].

**Analogy:** Whisper is like a fast assistant who types everything they hear in a meeting. They are quick and usually right, but they do not know your guests' names or your industry's special words. You read their notes afterwards and correct them before anyone else sees them.

## Worked Example
Mateus is a science teacher in Recife, Brazil, who records short videos in Portuguese for his students. He wants captions for a 2-minute video about the water cycle. The presenter will follow his steps on screen:

1. He exports the audio of his video as an MP3 file.
2. He opens a free Whisper app on his computer, chooses the file, sets the language to Portuguese and selects a medium model [VERSION].
3. He clicks the transcribe button. The transcript appears with timestamps.
4. He plays the audio and reads the transcript at the same time. He finds three errors: "evapotranspiração" was split into two wrong words; "32 graus" was written as "30 e 2 graus"; and one sentence appears twice although he said it once.
5. He corrects each error in the app's editor.
6. He exports the result as an SRT file [VERSION].
7. He imports the SRT into his video editor and watches the video once with captions on.

**Optional local command.** A teacher who prefers the terminal could install the open-source Whisper package and run one command like this [VERSION]:

```
whisper aula.mp3 --model medium --language pt --output_format srt
```

This creates an SRT file in the same folder. It also needs a free tool called ffmpeg [VERSION].

## Common Mistake
Many beginners trust the transcript because most of it is correct. But the errors are usually in the most important words: names, numbers and key terms. One wrong number can change the meaning. Always check while listening. Also, do not upload recordings containing other people's personal or confidential information to an online service without their permission.

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
**What good looks like:** An SRT file with correct words, short lines and sensible timings that match the audio, plus a list of every error you corrected, grouped by type.
**Time:** about 30 minutes

## Review Flags
- [VERIFY] Confirm that Whisper is an OpenAI speech-to-text model that is free to download, supports many languages, produces timed output, and can sometimes add words that were never said.
- [VERSION] A reviewer must choose the free Whisper app to demonstrate and check its interface, local processing, language and model options, editing and SRT export against the live app.
- [VERSION] Check model sizes and hardware needs, the command-line syntax and the ffmpeg requirement against current package documentation, and confirm that target editors and platforms accept SRT files.
- Curriculum judgement call carried: the command-line install may be too technical for this audience, so it is presented as optional; a reviewer should confirm this decision.

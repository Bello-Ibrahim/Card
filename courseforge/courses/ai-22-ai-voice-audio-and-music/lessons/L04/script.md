# L04 Transcripts and Captions with Whisper | Presenter Script

Course: AI-22 · Video: 5 min · Words: 688

## Hook
Many people watch videos with the sound off, and some cannot hear the audio at all. Captions help all of them. Typing captions by hand can take hours. With a speech-to-text model, you get a first draft in minutes, and spend your time checking it.

## Explain
In the last lesson, you turned text into speech. Today, we go the other way. Whisper is a speech-to-text model. It listens to audio and produces a transcript. The easiest way to use it is a free app on your own computer, so your audio does not leave your device.

We use an app called Buzz. If you like the terminal, you can also run Whisper with one command, but that is optional. Whisper comes in several sizes. Smaller models are faster but make more mistakes. A small or medium model is a good start on a normal laptop.

Whisper makes predictable mistakes. It often gets names wrong. It mixes up numbers, like fifteen and fifty. And it writes common words in place of technical terms. Noise and people talking at the same time also cause trouble. So always check the transcript by hand.

Captions are a transcript split into short lines, each with a start and end time. The most common caption file is called SRT. It is plain text. Each caption has a number, then a timing line, then the words. Most video editors accept it.

Think of Whisper as a fast assistant who types everything they hear in a meeting. They are quick and usually right. But they do not know your guests' names or the special words of your field. So you read their notes and correct them before anyone else sees them.

## Demonstrate
Let's follow Mateus. He is a science teacher in Recife, in Brazil, and he records short videos in Portuguese for his students. He wants captions for a two-minute video about the water cycle. First, he exports the audio of his video as an MP3 file.

He opens Buzz on his computer and chooses the file. He sets the language to Portuguese and selects the medium model. Then he clicks transcribe. After a short wait, the transcript appears, with a timestamp on every line.

Now the real work. He plays the audio and reads along at the same time. He finds three errors. A long scientific word about water rising from plants and soil was split into two wrong words. The temperature thirty-two degrees was written in a strange way. And one sentence appears twice, although he said it once.

He corrects each error in the app's editor, and deletes the repeated sentence. Then he exports the result as an SRT file, imports it into his video editor, and watches the whole video once with captions on.

You can also open the SRT file in a plain text editor before you use it. Check the caption numbers, the timings and the length of each line. Short lines are much easier to read, especially on a small phone screen.

If you prefer the terminal, the same job takes one command, with the file name, the model, the language and SRT as the output. You can see it on screen. This is optional.

A common mistake is to trust the transcript because most of it is correct. But the errors are usually in the most important words. One wrong number can change the meaning. And never upload other people's recordings to an online service without their permission.

## Recap
Let's recap. First, Whisper is a speech-to-text model you can use through a free app, or optionally with one command. Second, always check names, numbers, technical terms and repeated sentences by hand while you listen. Third, an SRT file holds numbered captions with start and end times, and most video editors accept it.

## CTA
Now it is your turn. In the exercise below this video, you will transcribe a two-minute recording of your own voice, correct every error, and export an SRT caption file. It takes about thirty minutes. In the next lesson, Voice Cloning: Consent Comes First, we talk about people before tools.

## Thumbnail
Headline: Captions in Minutes
Image: Navy background, a video frame with a teal caption bar at the bottom and a small stopwatch icon, headline in teal Inter Bold.

## Production Notes
- Screen demo tool: Buzz, the free open-source desktop app for Whisper (DECISIONS.md). Backup: the Whisper command line, shown only as an optional slide.
- [VERIFY] content.md states that Whisper is an OpenAI model, free to download, works in many languages, produces timed output and can sometimes add words that were never said. The voiceover does not state these as facts: it says only that Whisper is a speech-to-text model and that the app creates a timed transcript. Confirm before adding any of these claims.
- [VERSION] Before recording, check Buzz's interface, local processing, language and model options (small, medium), the transcript editor and SRT export against the live app. Check model sizes and hardware needs.
- [VERSION] The optional command on scene 12 must be checked against current package documentation, including the ffmpeg requirement, before the slide is rendered.
- Judgement call carried: the command line is presented as optional because it may be too technical for this audience; a reviewer should confirm this.
- The demo needs a 2-minute Portuguese water-cycle recording by a consenting speaker, with the three errors present in the transcript (or staged by editing). Mateus in Recife is fictional.
- Pronunciation: Mateus = ma-TAY-oos; Recife = heh-SEE-fee; Manizales = man-ee-SAH-les.

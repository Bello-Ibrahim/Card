# Screen Demo Pack: AI-22 L04 Transcripts and Captions with Whisper

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-22-ai-voice-audio-and-music_L04_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open Buzz on the desktop
2. Add the file water-cycle.mp3
3. Set the language to Portuguese
4. Select the Whisper medium model
5. Click the button to start transcribing
6. Open the finished transcript: each line shows start and end times

**Narration over this clip (for pacing)**

> He opens Buzz on his computer and chooses the file. He sets the language to Portuguese and selects the medium model. Then he clicks transcribe. After a short wait, the transcript appears, with a timestamp on every line.

## Clip 2: scene 9

- **Filename:** `ai-22-ai-voice-audio-and-music_L04_screen_2.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Play the audio while the transcript scrolls
2. Highlight error 1: 'evapotranspiração' split into two wrong words
3. Highlight error 2: '32 graus' written as '30 e 2 graus'
4. Highlight error 3: one sentence repeated on two lines

**Narration over this clip (for pacing)**

> Now the real work. He plays the audio and reads along at the same time. He finds three errors. A long scientific word about water rising from plants and soil was split into two wrong words. The temperature thirty-two degrees was written in a strange way. And one sentence appears twice, although he said it once.

## Clip 3: scene 10

- **Filename:** `ai-22-ai-voice-audio-and-music_L04_screen_3.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Double-click each wrong line in the Buzz editor and type the correct text
2. Delete the repeated sentence
3. Export the transcript as SRT
4. Import the SRT into the video editor
5. Play the full video with captions on

**Narration over this clip (for pacing)**

> He corrects each error in the app's editor, and deletes the repeated sentence. Then he exports the result as an SRT file, imports it into his video editor, and watches the whole video once with captions on.

## Clip 4: scene 11

- **Filename:** `ai-22-ai-voice-audio-and-music_L04_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open the exported SRT file in a plain text editor
2. Scroll through: point to a caption number, a timing line and a text line
3. Point to one long caption line and split it into two shorter lines
4. Save the file

**Narration over this clip (for pacing)**

> You can also open the SRT file in a plain text editor before you use it. Check the caption numbers, the timings and the length of each line. Short lines are much easier to read, especially on a small phone screen.

## Production notes for this lesson

- Screen demo tool: Buzz, the free open-source desktop app for Whisper (DECISIONS.md). Backup: the Whisper command line, shown only as an optional slide.
- [VERIFY] content.md states that Whisper is an OpenAI model, free to download, works in many languages, produces timed output and can sometimes add words that were never said. The voiceover does not state these as facts: it says only that Whisper is a speech-to-text model and that the app creates a timed transcript. Confirm before adding any of these claims.
- [VERSION] Before recording, check Buzz's interface, local processing, language and model options (small, medium), the transcript editor and SRT export against the live app. Check model sizes and hardware needs.
- [VERSION] The optional command on scene 12 must be checked against current package documentation, including the ffmpeg requirement, before the slide is rendered.
- Judgement call carried: the command line is presented as optional because it may be too technical for this audience; a reviewer should confirm this.
- The demo needs a 2-minute Portuguese water-cycle recording by a consenting speaker, with the three errors present in the transcript (or staged by editing). Mateus in Recife is fictional.
- Pronunciation: Mateus = ma-TAY-oos; Recife = heh-SEE-fee; Manizales = man-ee-SAH-les.

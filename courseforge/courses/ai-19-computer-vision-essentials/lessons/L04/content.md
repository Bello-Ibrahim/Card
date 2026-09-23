# L04 Working with Video Frames

Course: AI-19 · Module: M1 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
A one-minute video clip can contain well over a thousand images. Every video tool you use, from traffic counters to sports replays, starts with the same simple loop: read a frame, do something with it, move to the next one. In this lesson you write that loop.

## Explanation
A video is a sequence of images, called **frames**, shown quickly one after another. Three properties matter:

- **Frame rate (FPS):** frames per second. A clip at 25 FPS has 25 frames for each second of video.
- **Frame size:** the width and height of every frame, the same for the whole file.
- **Frame count:** the total number of frames. Some files report this number only approximately, so do not depend on it for exact loops.

OpenCV reads video with `cv2.VideoCapture`. Each call to `cap.read()` returns two values: `ok`, which is `False` when there are no more frames, and `frame`, a normal BGR array like the images in L02. Everything from L03 works on each frame.

To save a result, create a `cv2.VideoWriter` with a file name, a **codec** code, the FPS and the frame size. The codec decides how frames are compressed. `mp4v` with an `.mp4` file works in most environments, but codec support depends on how OpenCV was built. [VERSION] Two rules prevent most writer problems: every frame you write must have exactly the size you gave the writer, and colour frames need `isColor=True` while greyscale frames need `isColor=False`. If these do not match, OpenCV skips the frames without raising an exception and writes an empty or broken file.

Always call `release()` on both the reader and the writer at the end. Otherwise the output file may be incomplete.

Colab runs on a remote server, so it cannot stream your webcam like a local script. This course uses recorded video files, which also make results repeatable.

Processing time matters. At 100 milliseconds per frame, a 25 FPS clip is processed four times slower than real time. Process every second or third frame, or resize frames before heavier steps.

**Analogy:** Video processing works like a factory conveyor belt. Items (frames) arrive one at a time, each worker (processing step) does the same job on every item, and a packer at the end (the writer) puts them back in order. If one worker is slow, the whole line slows down.

## Worked Example
Mateus Oliveira works at a fruit packing plant in Petrolina, Brazil. A fixed camera films the sorting belt. He wants a greyscale copy of each clip with a frame number on every frame, so reports can refer to exact moments.

```python
import cv2

cap = cv2.VideoCapture("belt.mp4")
fps = cap.get(cv2.CAP_PROP_FPS) or 25
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("belt_gray.mp4", fourcc, fps, (w, h), isColor=False)

n = 0
while True:
    ok, frame = cap.read()
    if not ok:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.putText(gray, f"frame {n}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
    out.write(gray)
    n += 1

cap.release()
out.release()
print(f"{n} frames at {fps:.0f} FPS, size {w}x{h}")
```

Example output: `250 frames at 25 FPS, size 640x360`. Note that `putText` uses the colour `255` (white) because the frame has one channel; on a colour frame it would be a BGR tuple.

**On screen (presenter steps):**
1. Upload a short clip (10 seconds is enough) to Colab.
2. Run only the first four lines and print `fps`, `w` and `h`.
3. Run the full cell and show the printed summary.
4. Download `belt_gray.mp4` from the file panel and play it. [VERSION]
5. Change `isColor=False` to `True`, run again and show that the output file is broken or very small. Change it back.

## Common Mistake
Many learners create the writer with the size `(h, w)` because the array shape is `(height, width)`. The writer, like `cv2.resize`, expects `(width, height)`. If the sizes do not match, OpenCV skips the frames without raising an exception (at most it prints a warning), and you get a file that will not play. When an output video is empty, first compare the writer size with `frame.shape`, then check `isColor` and the codec.

## Key Takeaways
1. A video is a sequence of frames; `cv2.VideoCapture` reads them one at a time, and each frame is a normal image array.
2. `cv2.VideoWriter` needs a codec, the FPS, the size as `(width, height)` and the correct `isColor` setting, and both objects must be released.
3. In Colab, work with recorded clips, and reduce work per frame (resize or skip frames) when processing is slow.

## Hands-on Exercise
**Task:** Read a short public video clip frame by frame, draw the frame number on each frame, convert it to greyscale, and save the output video.
**Tools:** Google Colab; OpenCV; a short clip (10 to 30 seconds) from a free stock video site with a licence that allows reuse, or a clip you filmed yourself of objects such as traffic or a street market from a distance. [VERIFY]
**Steps:**
1. Upload the clip to Colab and print its FPS, width, height and reported frame count.
2. Write the loop from the worked example.
3. Run it and compare the number of frames you counted with the reported frame count.
4. Download and play the output file.
5. Change the loop so it processes only every second frame. Set the writer FPS to half the original and check that the video still plays at normal speed.
6. Time the loop with Python's `time` module for both versions and record the difference.
**What good looks like:** A greyscale video that plays correctly, with a readable frame number in the corner of every frame, plus a short note on the frame counts and the time saved by skipping frames.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Video codec support (`mp4v`, `.mp4`) depends on the OpenCV build in Colab; check that the output plays at recording time. Colab file panel download steps also change. Curriculum flag: OpenCV function names for L02-L05. Code was tested with opencv-python-headless on a synthetic clip.
- [VERIFY] Confirm that the stock video site the course recommends allows reuse of its clips for training exercises, and choose a demo clip that does not show identifiable people.

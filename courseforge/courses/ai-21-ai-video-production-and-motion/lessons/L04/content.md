# L04 Speaking the Language of the Camera

Course: AI-21 · Module: M1 · Objectives: O2, O3 · Video: 5 min

## Hook
Ask a video model for "a woman in a café" and you get a random camera position, random light and random movement. Ask for "a slow dolly-in, close-up, on a woman reading in a café, warm window light" and the result looks planned. The difference is the language of the camera.

## Explanation
**Quick recap from AI Image Generation:** a good image prompt names the subject, the setting, the lighting and the style, and it is specific. Everything you learned there still applies. Video adds two things: movement and time.

**Shot types** describe how much the viewer sees:

- **Wide shot:** the whole scene. It shows where we are.
- **Medium shot:** a person from about the waist up. It shows what they are doing.
- **Close-up:** a face, hands or a small object. It shows detail and emotion.

**Camera movements** describe how the camera moves:

- **Pan:** the camera turns left or right from one spot.
- **Tilt:** the camera turns up or down from one spot.
- **Dolly in / dolly out:** the camera moves towards or away from the subject.
- **Orbit:** the camera moves in a circle around the subject.
- **Handheld:** small, natural shaking, as if a person holds the camera.
- **Static:** the camera does not move.

**Pacing words** tell the model about speed: "slow", "gentle", "steady", "fast", "time-lapse", "slow motion". Use one movement per shot. Two or three movements in a short clip often produce confused results.

**The video prompt formula** used in this course has seven parts:

**Subject + Action + Setting + Camera movement + Lighting + Style + Duration**

```text
A young fisherman in a yellow raincoat (subject) pulls a net onto a small wooden boat (action) on a grey sea near a rocky coast (setting). Slow dolly-in from a medium shot to a close-up of his hands (camera movement). Soft overcast morning light (lighting). Realistic documentary style, natural colours (style). 6 seconds (duration).
```

Some tools set duration in a menu instead of the prompt [VERSION]. Keep it in your prompt notes anyway, so your plan and your settings match. Different models respond differently to the same words [VERSION], so treat the formula as a checklist, not a guarantee.

**Analogy:** A video prompt is like the notes a director gives a camera operator before a take. "Start wide, move in slowly, keep the light soft." A good operator follows short, clear notes. Long, mixed-up notes produce a confused take.

## Worked Example
Hana runs a small skincare brand in Busan, South Korea. Her shot list row says: "Close-up | Hand applies cream | Bathroom, morning."

She turns it into a full prompt:

```text
A woman's hand with short natural nails gently spreads white cream on the back of her other hand. A bright, minimal bathroom with a white sink and a green plant. Static close-up, very slight slow push-in. Soft morning daylight from a window on the left. Clean, modern commercial style, pastel colours. 5 seconds.
```

Then she checks it against the formula: subject (a woman's hand), action (spreads cream), setting (bright bathroom), camera (static close-up, slight push-in), lighting (morning daylight from the left), style (clean commercial), duration (5 seconds). All seven parts are present.

Her first draft had said "camera orbits around her while zooming in and panning to the window". She removed this, because three movements in 5 seconds usually look unnatural.

## Common Mistake
Many learners describe the scene carefully and forget the camera. The model then chooses a movement, often a slow drift that does not match the next shot. Others ask for several movements at once. Always choose one clear camera movement, or "static", for every shot.

## Key Takeaways
1. Shot types (wide, medium, close-up) control how much the viewer sees, and camera movements (pan, tilt, dolly, orbit, handheld, static) control how the view changes.
2. The course prompt formula is Subject + Action + Setting + Camera movement + Lighting + Style + Duration.
3. Use one camera movement per short shot, and treat the formula as a checklist because models respond differently.

## Hands-on Exercise
**Task:** Rewrite 4 shots from your shot list as full video prompts, using the formula.
**Tools:** Your shot list from L03; a document or notes app.
**Steps:**
1. Choose 4 rows from your shot list with different shot types, including at least one close-up and one wide shot.
2. For each row, write the seven parts of the formula as a short list.
3. Join the parts into one prompt of 40 to 80 words.
4. Check that each prompt has exactly one camera movement, or "static".
5. Remove any words that describe text, logos or signs; these are added in the editor.
6. Save the prompts in a text block next to each row, ready for L06 and L07.
**What good looks like:** 4 prompts that each contain all seven parts, one clear camera movement, consistent style words, and no on-screen text requests.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Whether each tool sets duration in the prompt or in a menu, and how each current model responds to camera terms, must be checked against the live tools before scripting.
- Judgement call carried from the curriculum: image-prompting basics from AI-20 are recapped in under 20 seconds, not retaught.

# HeyGen Batch Pack: AI-20 M2 (Style Control, Consistency and Editing)

Course: AI Image Generation and Visual Design. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L05 Describing a Style Without Copying Artists

- **Filename:** `ai-20-ai-image-generation-and-visual-design_M2_L05_presenter.mp4`
- **Expected length:** about 5.0 minutes (688 words). The quality gate accepts ±10%.

```text
Many people get a strong look by adding the words in the style of, and the name of a famous living artist. It seems quick. But it borrows someone else's life's work without asking. There is a better way, and it gives you more control.

A style is the set of visual qualities that make images look like they belong together. And you can describe almost any style with five attributes.

The first is the medium. What does the image seem to be made with? A gouache painting, a linocut print, a clay render, a film photograph, or a flat vector illustration. The second is texture and line, the surface and the edges. For example, rough paper grain, clean thin outlines or visible brush strokes.

The third is era or influence. This is a period or a general tradition, not a person, like a nineteen seventies travel poster, or mid-century modern. The fourth is colour, the palette and its strength. And the fifth is mood, the feeling, such as calm and quiet, or bold and confident.

Add the composition and lighting words from lesson four, and you have a complete style description that you can use again and again.

So why not name living artists? First, an artist's style is linked to their income and reputation, and many artists have not agreed to have their work imitated by AI. Second, the legal position is unclear and differs between countries, so it can create risk for your business or your client. Third, some tools block or change prompts that include artists' names.

Here is a way to think about it. Describing a style by its attributes is like describing a dish by its ingredients and flavours. Slow-cooked beans with smoked meat, garlic and orange tells a cook what to make. Cook it like a famous chef only works if you copy that chef, and it teaches you nothing about the dish.

Let's meet Renata. She runs a small sportswear brand in Recife, Brazil. She wants her campaign images to feel active, warm and local.

Instead of naming an artist, she writes a five-attribute style description. You can read it on screen. It asks for a flat vector illustration with bold geometric shapes, clean edges and a light paper grain, inspired by nineteen eighties sports posters, in sunset orange, deep teal and white, with an energetic and optimistic mood.

She tests it on two different subjects. The first prompt is a runner on a beach path at sunrise, from a low angle, with empty space at the top. The second is a pair of running shoes on a boardwalk, in close-up, seen from the side. She adds the same style description to each one.

Both images share the orange, teal and white palette, the bold shapes and the poster feeling, even though one shows a person and the other shows a product. Renata now has a style that belongs to her brand, and she can explain every part of it to her team.

But she notices one problem. In the shoe image, the paper grain is almost invisible. So she changes a light paper grain to a clearly visible paper grain, and generates again. Now the two images match more closely.

A common mistake is to swap an artist's name for one art movement word, like pop art, and stop there. That still leaves the model to guess the medium, colour and mood. And never use a real brand's name, logo or a film or game character to get a look.

Let's recap. First, describe a style with five attributes: medium, texture, era, colour and mood. Second, do not name living artists in prompts. It raises ethical and legal questions, and attributes give you more control. Third, test your style description on different subjects to check that it creates a consistent look.

Now it is your turn. In the exercise below, you will write a five-attribute style description for a fictional sportswear brand from Brazil, and test it on two different subjects. It takes about twenty minutes. In the next lesson, we learn about keeping images consistent. See you there.
```

## L06 Keeping Images Consistent

- **Filename:** `ai-20-ai-image-generation-and-visual-design_M2_L06_presenter.mp4`
- **Expected length:** about 5.3 minutes (732 words). The quality gate accepts ±10%.

```text
One good AI image is easy. Four images that look like they come from the same photo shoot are much harder. Every new generation starts from new random noise, so things drift. Today, you get the tools to keep a set together.

Style drift is when images that should belong together slowly become different. The light changes direction, the palette shifts, or the background moves from a studio to a kitchen. There are four main ways to control it.

The first and most important is a fixed style block. This is a paragraph that describes style, lighting, colour and framing. You paste it, word for word, into every prompt in the set. Only the subject line changes. It works in every tool.

The second is a reference image. You upload an image, often your best result so far, and ask the tool to match its look. In Gemini, you can attach an image to your message and describe what to keep. The third is Firefly's reference settings, where an image guides the style, or the layout and shapes.

The fourth is the seed. Where a tool lets you see and reuse a seed, it can keep a similar starting point. But many consumer tools hide seeds, so do not depend on this method.

A style block is like a uniform for a sports team. Each player is different, but the same colours and badge make everyone look like one team. The reference image is the photo of the uniform you show to a new player.

One safety note. Upload only images you own or have permission to use as references. No client files, and no photos of people without consent.

Let's help Min-seo. She runs a skincare start-up in Seoul, South Korea, and needs four product images for her website. Her style block is on screen. A pale peach background, one soft light from the upper left, a close-up at eye level, a peach, white and sage green palette, and a calm, clean mood.

I open Gemini and start a new chat. I paste the first subject, a frosted glass serum bottle with a white dropper, then the style block, and send. I download the best result. This is our hero image.

For the next image, I stay in the same chat and attach the hero image as a reference. I ask for a new image in exactly the same style, background and lighting, with a new subject, a white cream jar with a wooden lid. And I paste the style block again.

I repeat this for a tall sage green toner bottle, and a small tube of lip balm. Each time, only the subject changes.

Now the same idea in Adobe Firefly. I choose text to image and paste the subject line and the style block. Then I find the style reference setting and upload the hero image.

If there is a strength control, I move it. Watch how a stronger reference pulls the result closer to the hero image. I generate, then repeat with the next subject, keeping the reference and the style block the same.

Finally, the review. I place the four images in a row and check the background colour, the light direction, the shadow position and the framing. The lip balm image has a stronger shadow than the others.

So I add very soft, faint shadow to that prompt only, and regenerate that one image.

The most common mistake is to rewrite the style block a little each time, like soft light for one image and gentle daylight for the next. Small word changes create visible drift. Copy and paste the block exactly, and check each new image as you go.

Let's recap. First, a fixed style block, pasted word for word into every prompt, is the most reliable way to keep a set consistent. Second, reference images and reference settings help you match a chosen hero image. Third, check each new image against the hero for background, light, palette and framing, and fix drift one image at a time.

Now it is your turn. In the exercise below, you will build your own style block and use it to create four images that look like one set. Save the block, because you will use it in the capstone. It takes about twenty-five minutes. Next, we look at editing with generative fill and expand. See you there.
```

## L07 Editing with Generative Fill and Expand

- **Filename:** `ai-20-ai-image-generation-and-visual-design_M2_L07_presenter.mp4`
- **Expected length:** about 4.9 minutes (691 words). The quality gate accepts ±10%.

```text
You have an almost perfect image. But there is a coffee cup in the corner that should not be there, and the image is square when your website needs a wide banner. Do you start again? No. You edit only the part that needs to change.

Two editing features save a great deal of time. The first is generative fill. It changes a selected area of an image.

You paint over part of the picture. This is called a selection, or a mask. Then you can remove what is there, and the tool fills the space with matching background. Or you can write a short prompt, like a green potted plant, and the tool creates it only inside the selection. This is also called inpainting.

The second is generative expand, also called outpainting. It makes the canvas larger and fills the new space so that it continues the original image. It is the best way to turn a square image into a wide banner or a tall story, without stretching or cutting the subject.

In Adobe Firefly, these features have names like Generative Fill and Generative Expand. They use generative credits, and the free tier has a limit. Three tips. Select a little more than the object, including its shadow. Keep fill prompts short and concrete. And after a big expansion, check the new edges carefully.

Generative fill is like a skilled painter who repairs one damaged patch of wall, so well that you cannot see the repair. Generative expand is like adding a new section to a mural, painted to continue the scene.

One safety note. Only edit images you have the right to use, and do not upload photos of people without their consent.

Let's help Nino. She owns a bicycle repair shop in Tbilisi, Georgia. She has a square AI image of her workshop counter. But there is a plastic bottle on the left that looks untidy, and her website needs a wide banner.

I open Adobe Firefly, choose Generative Fill and upload the square image. I choose the remove brush and paint over the bottle, and its shadow too.

I click remove. The tool offers a few results. I compare them, choose the one with the cleanest counter surface, and keep it.

Now let's add something. With the insert brush, I select a small empty area on the right of the counter. I type a short prompt, a small green potted plant in a metal pot, and generate. I choose the result that matches the light direction of the image.

Next, the banner. I open Generative Expand with the edited image and choose sixteen by nine from the ratio menu. I move the original image to the right, so the new empty area appears on the left, where the headline will go.

I can leave the prompt empty so the tool continues the scene, or add plain workshop wall for a calmer background. I generate, then check the new edges for repeated tools or bent lines, and download the best result.

Here is the final banner. Nino's tidy counter is on the right, and a quiet wall is on the left, ready for text in Canva.

A common mistake is to select only the object, not its shadow. The object disappears, but a shadow of nothing remains. Another mistake is to regenerate the whole image for one small problem. That wastes credits and can lose the parts you liked. Edit the area first.

Let's recap. First, generative fill, or inpainting, removes, adds or replaces objects inside a selected area, and keeps the rest of the image the same. Second, generative expand, or outpainting, extends the canvas to a new shape, like square to sixteen by nine, without stretching the subject. Third, select objects with their shadows, keep fill prompts short, and check new edges carefully.

Now it is your turn. In the exercise below, you will take one of your own square images, remove an unwanted object in Firefly, and expand it to sixteen by nine. It takes about twenty minutes. In the next lesson, we finish in Canva, with layouts, resizing and text. See you there.
```

## L08 Finishing in Canva: Layouts, Resizing and Text

- **Filename:** `ai-20-ai-image-generation-and-visual-design_M2_L08_presenter.mp4`
- **Expected length:** about 4.9 minutes (691 words). The quality gate accepts ±10%.

```text
Ask an image generator to write summer sale, twenty percent off, and you may get something like this. AI images are often great backgrounds, but they are not finished designs. The last step happens in a design tool.

Image generators are good at pictures, but often weak at exact text, logos and precise brand colours. They can misspell words, invent letters or change a logo's shape.

So professional workflows follow one simple rule. Generate the picture with AI. Add real text, logos and exact colours in a design tool.

Canva is a free design tool that works well for this. Four finishing tasks matter most. First, place your image in a layout of the right size. Second, add text in your brand fonts and colours. You enter your exact brand colour as a code in the colour picker, and design tools follow that code exactly, unlike most generators.

Third, remove backgrounds to cut out a product. In Canva this may be a paid feature, and Firefly also offers options, so check your plan. Fourth, resize for different platforms, like a square post, a tall story and a wide banner. Automatic resize may need a paid plan. On the free plan, you create a new design and copy your elements into it.

An AI image is like a freshly baked cake. It may taste excellent, but it is not ready for the party until someone adds the writing, the candles and the right plate. Canva is the decorating table.

One safety note. Do not upload confidential client files or photos of people without consent, and only use logos you own or have permission to use.

Let's help Arjun, who runs a yoga studio in Pune, India. He has a calm AI image of an empty studio with morning light, and he wants a social post for a new class. I open Canva, click create a design, and choose a square social post size.

I upload the AI image in the uploads panel, drag it onto the page, and resize it to fill the page. Then I add a text box and type the headline. Sunrise Flow, Mondays at seven in the morning.

I choose a clear font. In the colour picker, I type the brand colour code you see on screen. Then I place the headline in the empty space, so it does not cover the main subject. Last, I place a small studio logo in a corner.

Now an optional step. I select a yoga mat image, open the edit image options, and find the background remover. Notice whether it is marked as a paid feature on your plan.

Next, resizing. On a paid plan, the resize option creates copies in the story size and a wide banner size. On the free plan, I create a new design in the story size, then copy and paste the image, headline and logo into it.

In each new size, I move the headline so it stays clear and readable. In the tall story, I move it higher. In the wide banner, I move it to the side. Then I download each design as a PNG file.

The most common mistake is to accept an automatic resize without checking it. Text can end up over the subject, or the logo can fall off the edge. Always review each size by eye. And do not ask the generator for text. Leave that space empty and add text in Canva.

Let's recap. First, generate the picture with AI, then add real text, logos and exact brand colours in a design tool such as Canva. Second, background removal and automatic resizing are useful, but which features are free changes often, so check your plan. Third, review every resized version by eye, because text and subjects can move to the wrong place.

Now it is your turn. In the exercise below, you will place one of your images in a Canva social post with a headline in your brand colours, then create a story and a banner version. It takes about twenty-five minutes. In the next lesson, we learn about spotting and fixing common flaws. See you there.
```

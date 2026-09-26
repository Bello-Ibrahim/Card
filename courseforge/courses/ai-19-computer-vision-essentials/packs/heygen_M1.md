# HeyGen Batch Pack: AI-19 M1 (How Computers See)

Course: Computer Vision Essentials. Make one HeyGen video per lesson below, using these settings for every video.

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

## L01 What Is Computer Vision?

- **Filename:** `ai-19-computer-vision-essentials_M1_L01_presenter.mp4`
- **Expected length:** about 5.1 minutes (719 words). The quality gate accepts ±10%.

```text
A farmer takes a photo of a leaf and learns which disease it has. A machine reads an address and sends a parcel down the right belt. None of these systems see like we do. But all of them turn pixels into useful information.

Hi, and welcome to Computer Vision Essentials. In this first lesson, we answer a simple question. What is computer vision?

Computer vision is the part of AI that extracts information from images and video. The input is always a grid of pixel values. The output depends on the question you ask. Most real projects use one of four main tasks.

The first task is image classification. It answers the question, what is in this image? The model returns one label for the whole image, such as healthy leaf, or leaf rust. It does not say where the problem is. Picture an app that helps farmers in India check a photo of a crop leaf.

The second task is object detection. It answers, what is in this image, and where? Each object gets a class, a confidence score and a bounding box, which is a rectangle in pixel coordinates. Because each object has its own box, detection lets you count. Picture a traffic system in Nairobi that counts buses and cars in every frame.

The third task is segmentation. Instead of a rectangle, the model labels every pixel. This helps when the exact shape or area matters, for example how much of a leaf is damaged. It needs more detailed labels and more computing power, so this course covers it only here.

The fourth task is optical character recognition, or OCR. It answers, which text is in this image? It turns text into characters you can search and edit. Picture a parcel sorting centre in Germany that reads postcodes on labels.

Here is a simple way to remember them. Imagine four assistants looking at the same photo of a market stall. The first says, fruit stall. The second puts a sticky note on every mango and every orange. The third cuts out the exact shape of each fruit with scissors. The fourth reads the price labels aloud. Same photo, four questions, four amounts of work.

Let's use this in a real situation. Ana Lucía Ramírez leads a small logistics start-up in Lima, Peru. Her team has four ideas, and for each one they must choose the right vision task.

The first idea is to flag photos of damaged boxes. One answer per photo is enough, damaged or not damaged, so that is classification. The second idea is to count pallets in a loading bay. Counting needs one box per pallet, so that is detection. A classifier would only say that pallets are present.

The third idea is to measure how full a truck is. The team needs the area covered by goods, not a rough rectangle, so that is segmentation. The fourth idea is to read tracking numbers on labels. The output must be text, so that is OCR, usually after detection finds the label first.

So which idea does Ana Lucía build first? The classification idea, because it needs the least labelling work. She keeps the pallet idea for later. To choose a task, ask two questions. Do I need to know where things are? And do I need boxes, exact shapes or text?

A common mistake is to choose the most powerful task because it sounds better. Segmentation needs more detailed labels, more computing and more time. The opposite mistake happens too. A classifier can say cars, but it cannot say seven cars.

Let's recap. First, computer vision turns pixel values into information: a label, a set of boxes, a pixel mask or text. Second, classification answers what, detection answers what and where, segmentation answers which exact pixels, and OCR answers which text. Third, choose the simplest task that supports the real decision, and combine tasks when one is not enough.

Now it is your turn. In the exercise below this video, you will match eight real applications to the right task, from counting boats in a harbour to reading an electricity meter. It takes about fifteen minutes. In the next lesson, we open an image in code and look at the numbers inside. Images as Numbers: Pixels, Channels and Colour. See you there.
```

## L02 Images as Numbers: Pixels, Channels and Colour

- **Filename:** `ai-19-computer-vision-essentials_M1_L02_presenter.mp4`
- **Expected length:** about 5.3 minutes (726 words). The quality gate accepts ±10%.

```text
You paint a square red in your code. You display the image, and the square is blue. Nothing is broken. You have just met one of the most common surprises in computer vision. By the end of this lesson, you will know exactly why it happens.

Last time, we saw that every vision task starts with a grid of pixel values. Today we look inside that grid. For a computer, an image is a grid of numbers, and each cell is a pixel. OpenCV loads it as a NumPy array, so everything you know about arrays still applies.

The array has a shape of height, width and channels. Height is the number of rows. Width is the number of columns. Channels hold the colour. A colour image has three channels, and a greyscale image has only height and width.

Each value is usually an eight-bit integer, from zero to two hundred and fifty-five. Zero means none of that colour, and two hundred and fifty-five means the maximum. So a pixel with three zeros is black, and a pixel with three values of two hundred and fifty-five is white.

Now the important part. OpenCV stores colour in the order blue, green, red. Most other libraries, including Matplotlib and most deep learning models, expect red, green, blue. If you pass one order to a tool that expects the other, red and blue swap places. So always convert with one colour conversion call when you move an image out of OpenCV.

Here is a simple picture. Think of an image as a large egg box with three layers. Each cup holds a number that says how strong one colour is at that spot. OpenCV stacks the layers blue, green, red. Most other tools expect red on top. Every number is correct, but the colours come out wrong.

One more rule. To reach a pixel, you give the row first and then the column. The origin is the top-left corner, and the row number grows as you move down. We do all of this in Google Colab, which is free.

Let's try it. Hiroshi Tanaka checks photos of ceramic tiles at a small factory in Osaka, Japan. Before he trains any model, he wants to understand his data.

He opens Google Colab and creates a new notebook. Then he clicks the folder icon on the left and uploads one photo, called tile dot j p g. Menus in Colab change, so follow the idea rather than the exact screen.

He pastes a short cell. It loads the photo with OpenCV, prints the shape and the data type, and prints the top-left pixel. Then it paints a block of pixels red, using blue, green, red order, and displays the image with Matplotlib after converting it to RGB.

The output shows four hundred and eighty, six hundred and forty, three, and the type is u-int-eight. That is four hundred and eighty rows of height, six hundred and forty columns of width, and three colour channels. The top-left pixel shows three numbers, something like one hundred and eighty, in blue, green, red order.

The image shows a red square, as expected. Now he deletes the conversion call and runs the cell again. The square is blue. Matplotlib read the first channel, which is blue, as red. He puts the call back.

A common mistake is to read the shape as width and height, because we say screen sizes that way. Arrays are rows first. But careful: the resize function takes width first. Also, if the file is missing, OpenCV returns None instead of an error, so always check.

Let's recap. First, an image is a NumPy array with a shape of height, width and channels, and usually values from zero to two hundred and fifty-five. Second, OpenCV uses blue, green, red order, so convert to RGB before you display the image or pass it to most models. Third, index pixels row first, from the top-left corner, and check that the image actually loaded.

Now it is your turn. In the exercise below this video, you will load your own photo, print its shape, paint a red block and display it correctly. Choose a photo of an object with no people in it. It takes about twenty minutes. In the next lesson, we clean and shape images. Image Processing with OpenCV. See you there.
```

## L03 Image Processing with OpenCV

- **Filename:** `ai-19-computer-vision-essentials_M1_L03_presenter.mp4`
- **Expected length:** about 4.9 minutes (687 words). The quality gate accepts ±10%.

```text
Not every vision problem needs a neural network. Some can be solved with a few lines of OpenCV that run in milliseconds on any laptop. And when you do use a model, those same few lines often decide whether it succeeds or fails.

In the last lesson, we saw that an image is just an array of numbers. OpenCV gives you fast, predictable operations on those arrays. Let's meet the core ones you will use throughout this course.

Resize changes the size, because models expect a fixed input size, and smaller images are faster. Remember that resize takes width first. Crop needs no function at all. It is plain array slicing. Greyscale reduces three channels to one, and many later steps work on one channel.

Blur averages each pixel with its neighbours. It removes small noise, like paper texture or camera grain. The kernel size must be an odd number, such as five by five. Threshold turns a greyscale image into pure black and white. With the Otsu option, OpenCV chooses the cut-off value for you. When the lighting is uneven, adaptive threshold chooses a different value for each small area.

Edge detection, with the Canny function, marks pixels where brightness changes sharply. It takes a low and a high threshold. Raise them to keep only strong edges. Then find contours joins edge pixels into outlines. From an outline, you can get its area or a bounding rectangle.

Think of image processing like preparing vegetables before cooking. You wash them, which is the blur. You cut them to size, which is resize and crop. And you sort them, which is the threshold. A good cook can still manage with bad preparation, but the result is better when the preparation is done well.

You use these steps in two ways. First, as preprocessing before a model, so your inputs look more like the training data. Second, as a complete solution, when the scene is simple and controlled, like a document on a plain desk.

Here is a real case. Fatou Diop works for a microfinance office in Dakar, Senegal. Field staff photograph paper forms on their desks. She needs a clean black-and-white image of each form. She tests with a sample form that holds no real customer data.

In Colab, she uploads the photo and runs the first three lines. They load the image, turn it grey, and apply a five by five blur. Showing the blurred image next to the original, you can see the paper texture fade away.

Next, she runs edge detection and finds the contours. She keeps the largest outline, because the paper is lighter than the desk, so it forms the biggest shape. She draws its rectangle on a copy of the photo to check it.

Then she crops to that rectangle and applies Otsu's threshold. The desk is gone, and the text is black on white. The output line shows nine hundred, twelve hundred, three, turning into seven hundred and sixty, five hundred and forty.

Now watch what happens when she lowers the edge thresholds to ten and thirty. Many more edges appear, from the wood grain and small shadows. The thresholds really matter.

This is also the common mistake. Learners copy values from a tutorial and expect them to work on every photo. A blur that suits a large photo may remove the text from a small one. Display every step, and test on photos with different lighting.

Let's recap. First, the core OpenCV steps are resize, crop, greyscale, blur, threshold, edges and contours, and each one returns a new array you can inspect. Second, use them to prepare images for a model, or on their own when the scene is simple and controlled. Third, the right values depend on the image, so check every result.

Now it is your turn. In the exercise below this video, you will turn a phone photo of a document into a clean black-and-white image, with greyscale, blur, threshold and crop. It takes about thirty minutes. In the next lesson, we move from single images to moving pictures. Working with Video Frames. See you there.
```

## L04 Working with Video Frames

- **Filename:** `ai-19-computer-vision-essentials_M1_L04_presenter.mp4`
- **Expected length:** about 5.1 minutes (706 words). The quality gate accepts ±10%.

```text
A one-minute video clip can contain well over a thousand images. Every video tool, from traffic counters to sports replays, starts with the same simple loop. Read a frame, do something with it, move to the next one. Today, you write that loop.

So far, we have worked with single images. A video is a sequence of images, called frames, shown quickly one after another. Three properties matter. The frame rate, the frame size, and the frame count.

The frame rate is frames per second. A clip at twenty-five frames per second has twenty-five frames for every second of video. The frame size is the same for the whole file. And the frame count is the total, but some files report it only approximately, so do not rely on it for exact loops.

OpenCV reads video with a video capture object. Each read returns two values. The first says whether a frame was found, and becomes false at the end of the file. The second is the frame itself, a normal image array in blue, green, red order. Everything from the last lesson works on each frame.

To save a result, you create a video writer with a file name, a codec, the frame rate and the frame size. The codec decides how the frames are compressed.

Two rules prevent most problems. Every frame must have exactly the size you gave the writer. And the colour setting must match: colour frames need colour on, greyscale frames need it off. If not, OpenCV skips the frames without any error. At the end, release both the reader and the writer.

Picture a factory conveyor belt. Frames arrive one at a time. Each worker does the same job on every item, and a packer at the end puts them back in order. If one worker is slow, the whole line slows down.

Two practical points. Colab runs on a remote server, so it cannot stream your webcam. We use recorded video files, which also make results repeatable. And speed matters. At one hundred milliseconds per frame, a twenty-five frames per second clip runs four times slower than real time. Skip frames, or resize them before heavy steps.

Let's build it. Mateus Oliveira works at a fruit packing plant in Petrolina, Brazil. A fixed camera films the sorting belt. He wants a greyscale copy of each clip, with a frame number on every frame.

He uploads a ten-second clip to Colab and runs only the first few lines. They open the video and read its frame rate, width and height, which he prints to check.

Then he runs the full cell. It creates a writer with colour switched off, and loops through the frames. Each frame is turned grey, gets its number written in white, and is saved. Finally, both objects are released. The summary reads two hundred and fifty frames at twenty-five frames per second, size six hundred and forty by three hundred and sixty.

He downloads the new file from the file panel and plays it. Every frame is grey, with its number in the corner.

Now he breaks it on purpose. He switches colour on in the writer and runs the cell again. There is no error message, but the output file is broken or very small. He switches it back.

Another common mistake is to give the writer height first, because that is the array shape. The writer, like resize, expects width first. When an output video is empty, compare the writer size with the frame shape, then check the colour setting and the codec.

Let's recap. First, a video is a sequence of frames, and each frame you read is a normal image array. Second, a video writer needs a codec, the frame rate, the size as width and height, and the right colour setting, and both objects must be released. Third, in Colab, work with recorded clips, and reduce the work per frame when processing is slow.

Now it is your turn. In the exercise below this video, you will read a short public clip, add frame numbers, convert it to greyscale and save it. It takes about twenty-five minutes. Next week, we start using models. How CNNs Learn Visual Features. See you there.
```

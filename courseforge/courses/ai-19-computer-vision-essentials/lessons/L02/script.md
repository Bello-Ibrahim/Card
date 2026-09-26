# L02 Images as Numbers: Pixels, Channels and Colour | Presenter Script

Course: AI-19 · Video: 5 min · Words: 737

## Hook
You paint a square red in your code. You display the image, and the square is blue. Nothing is broken. You have just met one of the most common surprises in computer vision. By the end of this lesson, you will know exactly why it happens.

## Explain
Last time, we saw that every vision task starts with a grid of pixel values. Today we look inside that grid. For a computer, an image is a grid of numbers, and each cell is a pixel. OpenCV loads it as a NumPy array, so everything you know about arrays still applies.

The array has a shape of height, width and channels. Height is the number of rows. Width is the number of columns. Channels hold the colour. A colour image has three channels, and a greyscale image has only height and width.

Each value is usually an eight-bit integer, from zero to two hundred and fifty-five. Zero means none of that colour, and two hundred and fifty-five means the maximum. So a pixel with three zeros is black, and a pixel with three values of two hundred and fifty-five is white.

Now the important part. OpenCV stores colour in the order blue, green, red. Most other libraries, including Matplotlib and most deep learning models, expect red, green, blue. If you pass one order to a tool that expects the other, red and blue swap places. So always convert with one colour conversion call when you move an image out of OpenCV.

Here is a simple picture. Think of an image as a large egg box with three layers. Each cup holds a number that says how strong one colour is at that spot. OpenCV stacks the layers blue, green, red. Most other tools expect red on top. Every number is correct, but the colours come out wrong.

One more rule. To reach a pixel, you give the row first and then the column. The origin is the top-left corner, and the row number grows as you move down. We do all of this in Google Colab, which is free.

## Demonstrate
Let's try it. Hiroshi Tanaka checks photos of ceramic tiles at a small factory in Osaka, Japan. Before he trains any model, he wants to understand his data.

He opens Google Colab and creates a new notebook. Then he clicks the folder icon on the left and uploads one photo, called tile dot j p g. Menus in Colab change, so follow the idea rather than the exact screen.

He pastes a short cell. It loads the photo with OpenCV, prints the shape and the data type, and prints the top-left pixel. Then it paints a block of pixels red, using blue, green, red order, and displays the image with Matplotlib after converting it to RGB.

The output shows four hundred and eighty, six hundred and forty, three, and the type is u-int-eight. That is four hundred and eighty rows of height, six hundred and forty columns of width, and three colour channels. The top-left pixel shows three numbers, something like one hundred and eighty, in blue, green, red order.

The image shows a red square, as expected. Now he deletes the conversion call and runs the cell again. The square is blue. Matplotlib read the first channel, which is blue, as red. He puts the call back.

A common mistake is to read the shape as width and height, because we say screen sizes that way. Arrays are rows first. But careful: the resize function takes width first. Also, if the file is missing, OpenCV returns None instead of an error, so always check.

## Recap
Let's recap. First, an image is a NumPy array with a shape of height, width and channels, and usually values from zero to two hundred and fifty-five. Second, OpenCV uses blue, green, red order, so convert to RGB before you display the image or pass it to most models. Third, index pixels row first, from the top-left corner, and check that the image actually loaded.

## CTA
Now it is your turn. In the exercise below this video, you will load your own photo, print its shape, paint a red block and display it correctly. Choose a photo of an object with no people in it. It takes about twenty minutes. In the next lesson, we clean and shape images. Image Processing with OpenCV. See you there.

## Thumbnail
Headline: Why Is Red Blue?
Image: Navy background, a small tile photo with a bright square that is red on the left half and blue on the right half, headline in teal Inter Bold.

## Production Notes
- [VERSION] Google Colab interface: the new-notebook flow, the folder icon for uploads, and the pre-installed OpenCV and Matplotlib packages. Check against the live tool before recording and adjust screen_steps to the live labels. The voiceover avoids exact menu names except the folder icon.
- [VERSION] OpenCV function names (imread, cvtColor, colour conversion codes): check against the OpenCV version installed in Colab at recording time. Code in content.md was tested with opencv-python-headless on a synthetic image.
- Run outputs: the voiceover states the shape 480, 640, 3 and the type uint8 exactly as content.md reports. Prepare tile.jpg at exactly 640 × 480 pixels so the recorded output matches. The top-left pixel value is NOT read aloud: content.md gives it only as an example, so the voiceover says 'something like'.
- Hiroshi Tanaka and the Osaka tile factory are fictional. Use an unbranded photo of ceramic tiles with no people in it.
- Screen recording: clean browser profile, no account names, bookmarks or other tabs visible. Speed up any waiting time for the Colab runtime to connect.

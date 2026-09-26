# Screen Demo Pack: AI-19 L05 How CNNs Learn Visual Features

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L05_screen_1.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Upload fabric.jpg to a Colab notebook
2. Show the kernels dictionary: vertical_edge, blur, sharpen
3. Run the cell with cv2.filter2D and cv2.convertScaleAbs

**Narration over this clip (for pacing)**

> In Colab, she uploads the photo in greyscale and defines three small filters, one for vertical edges, one for blur and one for sharpening. A short loop applies each filter and saves the result.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L05_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Display the original and the three outputs in a 2 × 2 Matplotlib grid
2. Point to the bright vertical threads in the edge map
3. Point to a pulled thread in the sharpened image

**Narration over this clip (for pacing)**

> She shows the original and the three outputs in a two by two grid. The edge map is bright along vertical threads and stripes, and dark on flat areas. The blur softens the weave. And the sharpen filter makes a small defect, like a pulled thread, stand out.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L05_screen_3.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Change the edge kernel to its transpose, k.T
2. Run the cell again and display the new edge map
3. Show that horizontal edges are now bright

**Narration over this clip (for pacing)**

> Now she turns the edge filter on its side, by transposing it. Run it again, and the vertical lines fade, while the horizontal threads light up. Same numbers, new direction, new feature.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L05_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Show the prepared image of the first 16 first-layer filters of a pre-trained CNN
2. Point to two edge-like filters
3. Point to one colour-blob filter

**Narration over this clip (for pacing)**

> Finally, she shows the first-layer filters of a pre-trained CNN. Some look like edge detectors at different angles, similar to her hand-made ones. Others are colour blobs. Nobody drew them. They were learned from data.

## Production notes for this lesson

- [VERSION] torchvision model names, the weights="DEFAULT" argument, and whether PyTorch and torchvision are pre-installed in Colab must be checked at recording time. OpenCV function names (filter2D, convertScaleAbs) must be checked against the OpenCV version in Colab. The OpenCV code in content.md was tested with opencv-python-headless on a synthetic image.
- Run outputs: content.md gives no exact printed mean values for the three filters, so the voiceover does not state any numbers. Describe the images only.
- Scene with the first-layer filters: prepare the image in advance from a pre-trained CNN (for example resnet18 conv1 weights, first 16 filters, each normalised to 0-1). The voiceover says only that some look like edge detectors and some like colour blobs.
- Leila Haddad and the Tripoli textile workshop are fictional. The fabric photo must show no people, no brand labels and no logos.
- Screen recording: clean browser profile, no account names or other tabs visible.

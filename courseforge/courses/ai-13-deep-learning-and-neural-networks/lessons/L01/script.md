# L01 Why Deep Learning? | Presenter Script

Course: AI-13 · Video: 5 min · Words: 743

## Hook
You can already get a strong result from a gradient-boosted model on a clean table in a few minutes. So why spend hours training a neural network on a GPU? Sometimes, you should not. Let's see when deep learning is worth the cost.

## Explain
Hi, and welcome to Deep Learning and Neural Networks. In this first lesson, we decide when deep learning makes sense, and we get a GPU ready.

The classical models from the scikit-learn course, such as random forests and gradient boosting, work on features that already mean something. Age, income, the number of late payments. A person does most of the work by building those features.

Images, audio and text are different. A colour photo of two hundred and twenty-four by two hundred and twenty-four pixels is about one hundred and fifty thousand numbers. No single pixel means leaf disease or cat.

The useful features are patterns of patterns. Edges, then textures, then shapes, then objects. A neural network learns these features directly from the raw data, layer by layer. This is called representation learning, and it is why deep learning works so well on unstructured data.

But the cost is real. Networks usually need more labelled data, unless you start from a pretrained model. They need more compute. They have more settings to tune and more ways to fail. And it is harder to explain why they made a decision.

Here is a way to picture it. Classical machine learning is like a skilled tailor who works from measurements someone else has taken. Deep learning is a tailor who also learns to take the measurements from photos. More flexible, but slower to learn.

So, a practical rule. On small or medium tables, try a tree-based model first. On images, audio or text, start with a pretrained network. And why a GPU? It runs thousands of simple calculations in parallel, which is exactly what matrix multiplication inside every layer needs.

## Demonstrate
Meet Dilnoza, a data scientist at a textile company in Tashkent, Uzbekistan. Project A predicts late supplier deliveries from a table of eight thousand orders. Her gradient-boosting model already scores well, so she keeps it.

Project B detects weaving faults in fabric photos. There are no useful columns, only pixels, and hand-made features miss small holes and uneven threads. That is a good case for a convolutional network. Let's prepare the GPU.

Open a new Colab notebook. From the Runtime menu, choose Change runtime type, select a GPU hardware accelerator, and save.

Now run the check cell. It prints the PyTorch version, and whether PyTorch can see a GPU. If it says true, you are ready. If it says false, the code still runs, but on the CPU, and slowly.

Next, the timing cell. It creates a large random matrix of about four thousand by four thousand numbers, multiplies it by itself on the CPU, and then does the same on the GPU.

Run it twice, because the first GPU run includes start-up time. On the second run, you should see something like a GPU that is many times faster. Exact numbers depend on your hardware.

Notice the synchronise calls. GPU work runs in the background, so without them the timer stops too early.

One common mistake is to think deep learning is always better. On small tables, a well-tuned tree model is often just as accurate, faster and easier to explain. Choose deep learning because of the data, not because it is newer.

A quick note on access. Free GPU limits change and are not guaranteed, and Colab is not available everywhere. Every exercise in this course also finishes on a CPU with a smaller data subset, in Colab or a local notebook.

## Recap
Let's recap. First, neural networks learn features from raw, unstructured data like images, audio and text. On small tables, classical models are often just as good and cheaper. Second, deep learning costs more data, compute, tuning and explanation, so choose it for a reason. Third, check for a GPU in PyTorch, choose a device for your tensors, and synchronise before timing GPU work.

## CTA
Now it is your turn. In the exercise below this video, you will switch to a GPU runtime, time the matrix multiplication three times on each device, and write two sentences about a project of yours. It takes about twenty minutes. In the next lesson, we learn tensors, the language of PyTorch. See you there.

## Thumbnail
Headline: Is Deep Learning Worth It?
Image: Navy background, a split card: a clean data table on the left and a fabric photo with a glowing neural network on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] Check before recording: Colab free GPU access, the GPU type offered, usage limits, session timeouts and the menu path Runtime > Change runtime type. The voiceover says only that limits exist and change.
- [REGION] Google Colab and the Hugging Face Hub may not be available in every country. The voiceover points to a local Jupyter notebook on CPU as the fallback; the course page must offer it too.
- Timing output is hardware-dependent. The voiceover says 'you should see something like' and gives no fixed numbers; show the second run of the timing cell, not the first.
- Dilnoza and the Tashkent textile company are hypothetical; stock footage must not show a real company name or logo.
- Screen recording: clean Google account, browser zoomed so code and output are readable on a phone. Run every cell once before recording.

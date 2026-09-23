# L01 Why Deep Learning?

Course: AI-13 · Module: M1 · Objectives: O1 · Video: 5 min (screen demo)

## Hook
You already know how to get a strong result from a gradient-boosted model on a clean table in a few minutes. So why would you spend hours training a neural network on a GPU? Sometimes you should not. This lesson shows when deep learning is worth the cost, and gets your GPU runtime ready.

## Explanation
Classical models from AI-12, such as logistic regression, random forests and gradient boosting, work on **features that already mean something**: age, income, number of late payments. Most of the modelling work is feature engineering, and a person does it.

Images, audio and text are different. A 224×224 colour photo is about 150,000 numbers, and no single pixel means "leaf disease" or "cat". The useful features are patterns of patterns: edges, then textures, then shapes, then objects. A **neural network** learns these features directly from raw data, layer by layer. This is called **representation learning**, and it is the main reason deep learning works well on unstructured data.

The cost is real:

- **Data:** networks usually need more labelled examples, unless you start from a pretrained model (L10, L13).
- **Compute:** training involves many large matrix multiplications, so a GPU helps a lot.
- **Tuning and debugging:** there are more settings and more ways for training to fail (L08, L15).
- **Explainability:** it is harder to say why a network made a decision.

A practical rule: on small or medium **tabular** data, try a tree-based model first. On images, audio or text, start with a pretrained network.

**Analogy:** Classical ML is like a skilled tailor who works from measurements someone else has already taken. Deep learning is like a tailor who also learns how to take the measurements from photos. The second tailor can handle much more varied work, but needs more time and more examples to learn.

**Why GPUs?** A GPU runs thousands of simple arithmetic operations in parallel. Matrix multiplication, the core operation inside every layer, fits this well. In PyTorch, you choose where a tensor lives with a **device**: `"cpu"` or `"cuda"` (an NVIDIA GPU).

Google Colab offers a free GPU runtime, but the GPU type, usage limits and session timeouts change and are not guaranteed. [VERSION] Colab and the Hugging Face Hub may also not be available in every country. [REGION] Every exercise in this course is designed to also finish on a CPU with a smaller data subset, in Colab or in a local Jupyter notebook.

## Worked Example
Dilnoza is a data scientist at a hypothetical textile company in Tashkent, Uzbekistan. She has two projects.

Project A predicts late supplier deliveries from a table of 8,000 orders with 20 columns. Her gradient-boosting model from AI-12 already gives a good validation score. A neural network would take longer to tune and would probably not do much better. She keeps the classical model.

Project B detects weaving faults in fabric photos. There are no useful columns, only pixels. Hand-made features, such as colour histograms, miss small holes and uneven threads. This is a good case for a convolutional network, and later for transfer learning.

**Screen demo steps:**

1. Open a new Colab notebook.
2. Open **Runtime > Change runtime type**, choose a GPU hardware accelerator and save. [VERSION]
3. Run the check cell below.
4. Run the timing cell twice. The first GPU run includes start-up time, so compare the second run.

```python
import torch, time
print(torch.__version__, torch.cuda.is_available())
device = "cuda" if torch.cuda.is_available() else "cpu"

a = torch.randn(4096, 4096)
t0 = time.perf_counter(); a @ a
print("CPU seconds:", round(time.perf_counter() - t0, 3))

if device == "cuda":
    g = a.to(device); torch.cuda.synchronize()
    t0 = time.perf_counter(); g @ g; torch.cuda.synchronize()
    print("GPU seconds:", round(time.perf_counter() - t0, 3))
```

`torch.cuda.synchronize()` matters: GPU work runs asynchronously, so without it the timer stops before the GPU has finished. The expected output is that the GPU is many times faster, but the exact numbers depend on the hardware you receive.

## Common Mistake
Many practitioners think deep learning is always better than classical ML. On small tabular datasets, a well-tuned tree model is often as accurate, faster to train and easier to explain. Choose deep learning because of the data type and the size of the problem, not because it is newer. A second mistake is assuming the GPU is active. If `torch.cuda.is_available()` returns `False`, all code still runs, but on the CPU and slowly.

## Key Takeaways
1. Neural networks learn features from raw, unstructured data such as images, audio and text; on small tables, classical models are often just as good and cheaper.
2. Deep learning costs more data, compute, tuning and explanation effort, so choose it for a reason.
3. In PyTorch you check for a GPU with `torch.cuda.is_available()` and choose where tensors live with a device; always synchronise before timing GPU work.

## Hands-on Exercise
**Task:** Switch Colab to a GPU runtime, confirm `torch.cuda.is_available()`, and time a large matrix multiplication on CPU and GPU.
**Tools:** Google Colab (free); PyTorch (pre-installed in Colab). CPU fallback: a local Jupyter notebook with PyTorch installed.
**Steps:**
1. Create a new Colab notebook and change the runtime type to a GPU. [VERSION]
2. Run `torch.cuda.is_available()` and `torch.cuda.get_device_name(0)`, and note the GPU name.
3. Time a 4096×4096 matrix multiplication on CPU, then on GPU, using `torch.cuda.synchronize()`. Repeat each timing 3 times and record the median.
4. If no GPU is available, run the CPU timing with 1024, 2048 and 4096 sizes and describe how the time grows.
5. Write two sentences: one about the speed-up, and one about a project of yours that does or does not need deep learning.
**What good looks like:** A notebook with the device check, 3 timings per device, a correct use of synchronisation, and a short, reasoned note about when deep learning is worth it.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Colab free GPU access, GPU type, usage limits, session timeouts and the menu path for changing the runtime type must be checked before recording. Exercises must also finish on CPU.
- [REGION] Google Colab and the Hugging Face Hub may not be available in every country; the local Jupyter fallback must be offered in the course page.

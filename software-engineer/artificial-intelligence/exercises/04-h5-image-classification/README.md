# Exercise 04 — H5 Image Classification

*Practice exercise for self-study. This activity is not part of the original
university coursework; it was created to complement the portfolio.*

## Title

Image classification with a pretrained `.h5` model.

## Objective

Load a trained image-classification `.h5` model and run inference on a single
image, applying the full preprocessing pipeline: loading, resizing,
normalization, tensor conversion, prediction and interpretation.

## Background

Image models are convolutional neural networks (CNNs) trained on images with
a **fixed input size** (for example `224x224` or `32x32` pixels with 3 RGB
channels). To classify a new image you must transform it so it matches what
the model saw during training:

1. **Load** — read the image (here with Pillow).
2. **Resize** — scale it to the model's expected height and width.
3. **Convert** — normalize channels to RGB with 3 channels.
4. **Normalize** — scale pixel values (typically to `[0, 1]` by dividing by
   255, or using the model's training statistics).
5. **Add the batch axis** — a single image becomes shape
   `(1, height, width, channels)`.
6. **Predict** — run inference and read the class scores.

The class **index** in the output vector corresponds to the model's training
labels; the script prints the index and the label must be mapped by you (the
labels are not stored inside the `.h5` file).

## Concepts Covered

- CNN image input conventions (height, width, channels)
- Image loading, resizing and channel conversion with Pillow
- Normalization and its importance for correct predictions
- Model-compatible tensor conversion (`batch × H × W × C`)
- Inference and top-k output interpretation

## Requirements

- Python 3.9+
- TensorFlow 2.x
- NumPy
- Pillow

```bash
pip install tensorflow numpy pillow
```

## Installation

```bash
cd software-engineering-coursework/artificial-intelligence/exercises/04-h5-image-classification
```

## How to Run

Provide a `.h5` model and an image, then run from the `src/` directory:

```bash
cd src
python predict.py --model ../model.h5 --image ../data/sample.jpg --top-k 5
```

Run with the default arguments (expects `../model.h5` and `../data/sample.jpg`):

```bash
python predict.py
```

> The scripts are written as a small pipeline: `src/load_model.py` exposes
> `load_trained_model(...)`, and `src/predict.py` imports it — run
> `predict.py` from inside `src/` so the import resolves.

## Expected Behavior

The script explains the model's expected input size, preprocesses the image,
runs inference and prints:

- the target size used for resizing;
- the final tensor shape fed to the model;
- the top-k predictions with their confidence scores.

## Obtaining a Model and an Image

No model or image is bundled and nothing is downloaded automatically.

- **Model:** use a locally-trained classifier or another `.h5` model you are
  explicitly allowed to use. The model must accept RGB images with a fixed
  height/width (read from `model.input_shape`); if the input shape is
  variable, a default target size of `224x224` is used.
- **Image:** provide your own JPEG/PNG photo (see `data/README.md` for what
  is expected).

## Exercise

1. Run the script on an image of your choice and record the top-k results.
2. Try the same image **without** normalization (comment out the `/ 255.0`)
   and observe how predictions change. Why does normalization matter?
3. Try an image orientation/illumination change and compare predictions.
4. **Challenge:** extend `predict.py` to print the class **label** by mapping
   indices through a small dictionary `{0: "class_a", 1: "class_b", ...}`
   that you define from your model's training labels.

## Learning Outcomes

- Execute the full image preprocessing → inference pipeline.
- Convert arbitrary images into model-compatible tensors.
- Interpret top-k confidence outputs.
- Understand why normalization must match the model's training procedure.
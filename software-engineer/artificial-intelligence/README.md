# Artificial Intelligence

Practice material on machine learning and deep learning workflows with
TensorFlow / Keras: loading, inspecting and running inference with models
stored in the HDF5-based `.h5` format, plus module notes.

## Directory Structure

### `exercises`

Self-study activities (not original university coursework) that build a
complete `.h5` model workflow:

| Exercise | Content |
| --- | --- |
| [`01-h5-model-loading`](exercises/01-h5-model-loading/README.md) | Load a trained `.h5` model with `load_model` |
| [`02-h5-model-inspection`](exercises/02-h5-model-inspection/README.md) | Inspect layers, shapes and parameter counts |
| [`03-h5-model-prediction`](exercises/03-h5-model-prediction/README.md) | Run inference on model-compatible inputs |
| [`04-h5-image-classification`](exercises/04-h5-image-classification/README.md) | Full image preprocessing + classification pipeline |

Each exercise documents its dependencies (`tensorflow`, `numpy`, `pillow`)
and expects a locally-trained or otherwise permitted `.h5` model — nothing is
downloaded automatically and no model files are bundled.

### `notes`

- [`artificial-intelligence.md`](notes/artificial-intelligence.md) - module
  roadmap, course notes and pointers to related hands-on work (see
  [Data Science](../data-science/README.md)).

## Learning Objectives

- Understand the HDF5 `.h5` format and what it stores (architecture, weights)
  versus source code and datasets
- Load, inspect and reuse trained Keras models
- Run inference for tabular and image inputs
- Preprocess image tensors to match model expectations
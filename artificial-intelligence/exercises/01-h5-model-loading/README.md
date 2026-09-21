# Exercise 01 — H5 Model Loading

*Practice exercise for self-study. This activity is not part of the original
university coursework; it was created to complement the portfolio.*

## Title

Loading a trained Keras model stored as a `.h5` file.

## Objective

Load a previously trained Keras/TensorFlow model from an HDF5-based `.h5`
file and confirm it returns a working `keras.Model`.

## Background

### What HDF5 is

HDF5 (Hierarchical Data Format version 5) is a file format and library for
storing large amounts of scientific data in a hierarchical, self-describing
container: groups, datasets and attributes. It is widely used in machine
learning to bundle a trained model into a single file.

### What `.h5` represents

Keras historically used an HDF5-based format for saving models, so trained
models were commonly stored with a `.h5` (or `.hdf5`) extension. The file
contains the model architecture, trained weights, optimizer state, loss and
metrics — everything needed to reload the model **without** re-training it.

> **Note:** newer Keras versions save models to a `.keras` file by default.
> Loading legacy `.h5` files is still fully supported, which is why it is
> useful to know how to work with them.

### What a trained model contains

A saved `.h5` model bundles:

- architecture (layers, connections, activation functions);
- trained weights (the learned parameters);
- optimizer state and training configuration;
- loss and metric configuration.

This is different from:

- **weights only** (`.h5` weights via `model.save_weights`) — no architecture;
- **Python source code** — the program that loads and uses the model;
- **datasets** — the raw input data used for training or inference.

## Concepts Covered

- HDF5 for model persistence
- The legacy Keras `.h5` model format vs the modern `.keras` format
- `tf.keras.models.load_model`
- `model.summary()`

## Requirements

- Python 3.9+
- TensorFlow 2.x

```bash
pip install tensorflow
```

## Installation

```bash
git clone https://github.com/NatashaBaudelaire/software-engineering-coursework.git
cd software-engineering-coursework/artificial-intelligence/exercises/01-h5-model-loading
```

## How to Run

You must provide a compatible `.h5` file first (see "Obtaining a model"
below), then:

```bash
python load_model.py --model model.h5
```

or, with the default filename:

```bash
python load_model.py
```

## Expected Behavior

The script loads the model and prints its `model.summary()`, showing the
layer stack, output shapes and parameter counts, followed by a confirmation
line.

## Obtaining a Model

This exercise deliberately does **not** ship a binary `model.h5` file or
download one. Use one of the following options:

1. Train a small model yourself and save it with
   `model.save("model.h5")`.
2. Export an existing local model you trained previously.
3. Ask your instructor or use a model you are explicitly allowed to use.

## Exercise

1. Load the provided `.h5` model with `load_model`.
2. Print `model.summary()`.
3. Verify the loaded object is a `keras.Model`:

```python
isinstance(model, tf.keras.Model)
```

4. Describe, in your own words, what information is stored inside the `.h5`
   file you loaded.

## Learning Outcomes

- Understand HDF5 and the role of `.h5` in Keras model persistence.
- Load a pre-trained model without re-training it.
- Recognize the difference between model files, weights, source code and
  datasets.
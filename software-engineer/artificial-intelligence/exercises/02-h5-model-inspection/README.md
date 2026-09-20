# Exercise 02 — H5 Model Inspection

*Practice exercise for self-study. This activity is not part of the original
university coursework; it was created to complement the portfolio.*

## Title

Inspecting the architecture of a trained `.h5` model.

## Objective

Load a `.h5` model and inspect its architecture without modifying it:
identify layers, input/output shapes and parameter counts, and understand the
difference between trainable and non-trainable parameters.

## Background

Once a trained model is loaded (see Exercise 01), the next step is
understanding what it actually contains. `model.summary()` is the standard
tool to display the architecture, but a programmatic inspection gives you the
same information in a machine-readable way and is useful for automation,
logging and validation.

The most relevant quantities are:

- **Layers** — the building blocks (Dense, Conv2D, LSTM, Dropout, ...).
- **Output shape** of each layer — shows how data flows through the model.
- **Parameters** — the numbers learned by the model.
- **Trainable parameters** — updated during training.
- **Non-trainable parameters** — frozen (e.g., BatchNormalization moving
  statistics) or intentionally frozen layers.

## Concepts Covered

- `model.summary()`
- Iterating `model.layers`
- Input and output shapes (`model.input_shape`, `model.output_shape`)
- Total / trainable / non-trainable parameter counts
- Understanding a deep model architecture

## Requirements

- Python 3.9+
- TensorFlow 2.x

```bash
pip install tensorflow
```

## Installation

```bash
cd software-engineering-coursework/artificial-intelligence/exercises/02-h5-model-inspection
```

## How to Run

Provide a compatible `.h5` file, then:

```bash
python inspect_model.py --model model.h5
```

## Expected Behavior

The script prints:

1. the full `model.summary()`;
2. a per-layer table (name, type, output shape, parameters);
3. the input and output shape of the whole model;
4. total, trainable and non-trainable parameter counts.

## Exercise

Using the printed information (or `model.get_layer(...)`):

1. Identify the **input shape** of the model. How many features (or pixels /
   channels) does a single sample have?
2. Identify the **output shape**. How many classes (or regression targets)
   does the model predict?
3. Which layer contains the **most parameters**, and why?
4. State the **total**, **trainable** and **non-trainable** parameter counts
   and explain the source of any non-trainable parameters.
5. **Challenge:** write a short snippet that prints only the layers whose
   name contains `"dense"` together with their output shapes, using
   `model.layers`.
6. **Challenge:** inspect one specific layer's weights:

```python
layer = model.get_layer(layer_name)
print(layer.weights)
```

## Learning Outcomes

- Read and interpret `model.summary()`.
- Extract architecture information programmatically.
- Distinguish trainable from non-trainable parameters.
- Reason about model capacity from parameter counts.
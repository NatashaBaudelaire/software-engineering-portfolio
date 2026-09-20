# Exercise 03 — H5 Model Prediction

*Practice exercise for self-study. This activity is not part of the original
university coursework; it was created to complement the portfolio.*

## Title

Using a trained `.h5` model for inference (prediction).

## Objective

Load a trained model and run inference on a synthetic input sample, learning
how inputs must be shaped and normalized, and how the model output should be
interpreted.

## Background

Getting a prediction from a trained model is called **inference** (or
*forward pass*). During training the model **updates its weights** using data
and labels; during inference the weights stay **fixed** and the model only
computes an output for a new input.

The two stages differ conceptually:

| | Training | Inference |
| --- | --- | --- |
| Weights | updated via backpropagation | frozen |
| Input | training batches + labels | one sample or small batch |
| Output | used to compute loss | prediction for the user |

The model itself does not change during inference — this is why a single
`.h5` file can be reloaded and reused any number of times.

A prediction pipeline has three parts: **loading** (Exercise 01), **input
preprocessing** (shaping and normalizing data the way the model was trained
on) and **output interpretation**.

## Concepts Covered

- `model.predict(...)` and `model(...)`
- Reading the expected input shape from the model itself
- Building a compatible input tensor
- Interpreting raw logits vs probability output
- Training vs inference

## Requirements

- Python 3.9+
- TensorFlow 2.x
- NumPy

```bash
pip install tensorflow numpy
```

## Installation

```bash
cd software-engineering-coursework/artificial-intelligence/exercises/03-h5-model-prediction
```

## How to Run

Provide a compatible `.h5` file, then:

```bash
python predict.py --model model.h5
```

The script builds a **small reproducible synthetic sample** that matches the
model's expected input shape (read from `model.input_shape`), so it runs on
any model without a specific dataset. For real use, replace the synthetic
sample with your own preprocessed input (see "Providing real input" below).

## Expected Behavior

The script prints:

1. the model's expected input and output shapes;
2. a warning if the model expects image-like input (handle that with Exercise
   04);
3. the sample input shape used;
4. the numeric prediction (raw output);
5. an interpretation:
   - if the output is a single value, printed directly (regression);
   - if the output has multiple values, the top class index and confidence,
     computed with `argmax`.

## Providing Real Input

This exercise does not assume a dataset. To run inference on real data:

1. inspect `model.input_shape` to learn how many features one sample has;
2. build a `numpy` array of that shape with `dtype="float32"`;
3. **normalize** the values exactly as they were during training (e.g.
   `(x - mean) / std`), otherwise predictions become meaningless.

## Exercise

1. Run the script on your model and record the prediction.
2. Modify the sample values and observe how the prediction changes. Which
   output would correspond to the highest-confidence class?
3. Compare `model.predict(sample)` with calling the model directly:
   `model(sample)`. What are the differences?
4. **Challenge:** wrap the pipeline in a function
   `predict_one(model, features)` that accepts a single feature vector and
   returns the predicted class.

## Learning Outcomes

- Run inference with a fixed, reloadable model.
- Build model-compatible input tensors.
- Interpret single-value and multi-class outputs.
- Understand the conceptual difference between training and inference.
"""Run inference with a trained Keras .h5 model on a synthetic sample.

The input is generated programmatically to match the model's expected
`input_shape`, so this script runs on any model without a specific dataset.
For real inference, replace the sample with properly preprocessed input.

Usage:
    python predict.py [--model model.h5]

Note: if the model expects image-like input (shape with height, width,
channels), use Exercise 04 instead.
"""

import argparse
import os

import numpy as np
from tensorflow.keras.models import load_model


def load_trained_model(model_path: str):
    """Load a Keras model from an HDF5 (.h5) file."""
    if not os.path.isfile(model_path):
        raise FileNotFoundError(
            f"Model file not found: {model_path}. Provide a compatible .h5 "
            "model (see the README for how to obtain one)."
        )
    return load_model(model_path)


def build_sample(input_shape):
    """Build a small reproducible sample that matches the model input shape.

    The leading `None` batch dimension is dropped; a batch axis is added back
    so the tensor is (1, ...).

    Args:
        input_shape: tuple returned by `model.input_shape`, e.g. (None, 4).

    Returns:
        A float32 numpy array of shape (1, ...) with deterministic values.
    """
    feature_shape = tuple(size for size in input_shape if size)
    rng = np.random.default_rng(seed=42)
    sample = rng.normal(loc=0.0, scale=1.0, size=feature_shape).astype(
        np.float32
    )
    return np.expand_dims(sample, axis=0)


def interpret_output(predictions, batch_size=1):
    """Return a human-readable interpretation of the model output.

    Args:
        predictions: array returned by `model.predict(...)`.
    """
    flat = np.asarray(predictions).reshape(-1)
    if flat.size == 1:
        return f"Single-value output (regression): {flat[0]:.4f}"
    top_index = int(np.argmax(flat))
    confidence = float(flat[top_index])
    return (
        f"Multi-class output (count={flat.size}):\n"
        f"  argmax index: {top_index}\n"
        f"  confidence:   {confidence:.4f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run inference with a trained Keras .h5 model."
    )
    parser.add_argument(
        "--model",
        default="model.h5",
        help="Path to the .h5 model file (default: model.h5).",
    )
    args = parser.parse_args()

    model = load_trained_model(args.model)
    input_shape = getattr(model, "input_shape", None)
    output_shape = getattr(model, "output_shape", None)

    print(f"Expected input shape:  {input_shape}")
    print(f"Expected output shape: {output_shape}")

    if input_shape and len(input_shape) >= 3 and input_shape[-1] in (1, 3, 4):
        print(
            "Warning: this model expects image-like input "
            "(height, width, channels). Use Exercise 04 for images."
        )

    sample = build_sample(input_shape)
    print(f"Sample input shape:    {sample.shape}")
    print(f"Sample input dtype:    {sample.dtype}")

    predictions = model.predict(sample, verbose=0)
    print("Raw predictions:       ")
    print(np.asarray(predictions))
    print("Interpretation:        ")
    print(interpret_output(predictions))


if __name__ == "__main__":
    main()
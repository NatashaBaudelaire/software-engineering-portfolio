"""Inspect the architecture of a trained Keras model stored as an .h5 file.

Reads a loaded model and prints the layer stack, input/output shapes and
trainable parameter counts so the model can be understood without modifying
it.

Usage:
    python inspect_model.py [--model model.h5]
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


def inspect_architecture(model) -> None:
    """Print architecture details of the given Keras model."""
    model.summary()
    print("\n--- Per-layer inspection ---")
    for layer in model.layers:
        print(
            f"{layer.name:<24} {layer.__class__.__name__:<20} "
            f"output={layer.output_shape:<24} params={layer.count_params()}"
        )

    input_shape = getattr(model, "input_shape", None)
    output_shape = getattr(model, "output_shape", None)
    total_params = model.count_params()
    trainable_params = sum(
        int(np.prod(weight.shape.as_list()))
        for weight in model.trainable_weights
    )

    print("\n--- Model-level summary ---")
    print(f"Input shape:          {input_shape}")
    print(f"Output shape:         {output_shape}")
    print(f"Total parameters:     {total_params}")
    print(f"Trainable parameters: {trainable_params}")
    print(f"Non-trainable params: {total_params - trainable_params}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inspect the architecture of a trained Keras .h5 model."
    )
    parser.add_argument(
        "--model",
        default="model.h5",
        help="Path to the .h5 model file (default: model.h5).",
    )
    args = parser.parse_args()

    model = load_trained_model(args.model)
    inspect_architecture(model)


if __name__ == "__main__":
    main()
"""Load a previously trained Keras/TensorFlow model stored as an .h5 file.

The .h5 file is an HDF5-based container that bundles the model architecture,
trained weights, optimizer state and training configuration, so the model can
be reloaded without re-training.

Usage:
    python load_model.py [--model model.h5]
"""

import argparse
import os

from tensorflow.keras.models import load_model


def load_trained_model(model_path: str):
    """Load a Keras model from an HDF5 (.h5) file and return it.

    Args:
        model_path: Path to the .h5 file produced by `model.save(...)`.

    Returns:
        A compiled `tf.keras.Model` ready for inspection or inference.

    Raises:
        FileNotFoundError: If the model file does not exist.
    """
    if not os.path.isfile(model_path):
        raise FileNotFoundError(
            f"Model file not found: {model_path}. Provide a compatible .h5 "
            "model (see the README for how to obtain one)."
        )
    return load_model(model_path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Load a trained Keras .h5 model and print its summary."
    )
    parser.add_argument(
        "--model",
        default="model.h5",
        help="Path to the .h5 model file (default: model.h5).",
    )
    args = parser.parse_args()

    model = load_trained_model(args.model)
    model.summary()
    print(f"Model loaded from: {args.model}")


if __name__ == "__main__":
    main()
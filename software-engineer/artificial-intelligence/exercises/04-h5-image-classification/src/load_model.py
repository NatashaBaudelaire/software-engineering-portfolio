"""Load a trained Keras/TensorFlow image-classification model (.h5 file).

This module is the loading step of the image-classification pipeline and is
imported by `predict.py`. Run scripts from this `src/` directory.

Typical usage:
    from load_model import load_trained_model
    model = load_trained_model("../model.h5")
"""

import os

from tensorflow.keras.models import load_model


def load_trained_model(model_path: str):
    """Load a Keras model from an HDF5 (.h5) file.

    Args:
        model_path: Path to the .h5 file produced by `model.save(...)`.

    Returns:
        A compiled `tf.keras.Model` ready for inference.

    Raises:
        FileNotFoundError: If the model file does not exist.
    """
    if not os.path.isfile(model_path):
        raise FileNotFoundError(
            f"Model file not found: {model_path}. Provide a compatible .h5 "
            "model (see the README for how to obtain one)."
        )
    return load_model(model_path)
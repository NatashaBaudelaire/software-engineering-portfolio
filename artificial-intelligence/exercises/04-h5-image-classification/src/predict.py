"""Classify a single image with a trained Keras .h5 image model.

Pipeline: load model -> load image -> resize -> RGB -> normalize (pixel/255)
-> add batch axis -> predict -> print top-k predictions.

Run from inside this `src/` directory so the local import resolves:

    python predict.py [--model ../model.h5] [--image ../data/sample.jpg]
"""

import argparse
import os

import numpy as np
from PIL import Image

from load_model import load_trained_model

DEFAULT_TARGET_SIZE = (224, 224)


def expected_target_size(model):
    """Derive the model's expected (height, width) from `input_shape`.

    Falls back to a default square crop when the shape is not fully
    specified (e.g. `(None, None, None, 3)`).
    """
    input_shape = getattr(model, "input_shape", None)
    if input_shape and all(dim is not None for dim in input_shape[1:3]):
        return (int(input_shape[1]), int(input_shape[2]))
    return DEFAULT_TARGET_SIZE


def preprocess_image(image_path: str, target_size):
    """Convert an image file into a model-compatible tensor.

    Returns a float32 array of shape (1, height, width, channels) with pixel
    values normalized to [0, 1].
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = img.resize(target_size)

    array = np.asarray(img, dtype=np.float32)
    normalized = array / 255.0
    return np.expand_dims(normalized, axis=0)


def top_k_predictions(predictions, k: int):
    """Return the top-k (index, confidence) pairs from a single prediction."""
    probs = np.asarray(predictions).reshape(-1)
    top_indices = np.argsort(probs)[::-1][:k]
    return [(int(i), float(probs[i])) for i in top_indices]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Classify a single image with a trained Keras .h5 model."
    )
    parser.add_argument(
        "--model",
        default="../model.h5",
        help="Path to the .h5 model file (default: ../model.h5).",
    )
    parser.add_argument(
        "--image",
        default="../data/sample.jpg",
        help="Path to the input image (default: ../data/sample.jpg).",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of top predictions to print (default: 5).",
    )
    args = parser.parse_args()

    model = load_trained_model(args.model)
    target_size = expected_target_size(model)
    print(f"Expected input size:  {target_size}")
    print(f"Expected channels:    RGB (3)")

    tensor = preprocess_image(args.image, target_size)
    print(f"Input tensor shape:   {tensor.shape}")
    print(f"Input tensor dtype:   {tensor.dtype}")
    print(f"Pixel range:          [{tensor.min():.3f}, {tensor.max():.3f}]")

    predictions = model.predict(tensor, verbose=0)[0]
    print("\nTop-k predictions (index -> confidence):")
    for index, confidence in top_k_predictions(predictions, args.top_k):
        print(f"  class index {index}: {confidence:.4f}")
    print(
        "\nNote: map the class index to a label using the labels your model "
        "was trained with (the .h5 file does not store class names)."
    )


if __name__ == "__main__":
    main()
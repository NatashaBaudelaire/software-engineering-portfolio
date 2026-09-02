"""
predict.py

Loads a trained model and classifies a single image.

Usage:
    python predict.py --image path/to/image.jpg
"""

import argparse
import torch
from PIL import Image

from dataset import get_transforms, CLASS_NAMES
from model import SimpleCNN


def load_model(model_path="best_model.pt"):
    """Loads the trained CNN model."""
    model = SimpleCNN(num_classes=len(CLASS_NAMES))
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()
    return model


def predict_image(model, image_path, top_k=3):
    """Predicts the top-k classes for a given image."""
    image = Image.open(image_path).convert("RGB").resize((32, 32))
    transform = get_transforms(train=False)
    tensor = transform(image).unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        outputs = model(tensor)
        probs = torch.softmax(outputs, dim=1).squeeze(0)

    top_probs, top_ids = torch.topk(probs, top_k)
    results = [(CLASS_NAMES[i.item()], p.item()) for i, p in zip(top_ids, top_probs)]
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Classify an image using the trained model."
    )
    parser.add_argument(
        "--image",
        type=str,
        required=True,
        help="Path to the input image."
    )
    parser.add_argument("--top_k", type=int, default=3)
    args = parser.parse_args()

    model = load_model()
    results = predict_image(model, args.image, args.top_k)

    print(f"\nImage: {args.image}")
    print("Top predictions:")
    for label, prob in results:
        print(f"  {label:<12} - {prob:.2%}")
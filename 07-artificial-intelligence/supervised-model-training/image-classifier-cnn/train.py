"""
train.py

Trains the SimpleCNN model on CIFAR-10 using supervised learning. Each image
has a known label (class), and the model learns to predict that label by
minimizing the error (cross-entropy) between the prediction and the true label.

Usage:
    python train.py --epochs 15
"""

import argparse
import torch
import torch.nn as nn

from dataset import get_dataloaders, CLASS_NAMES
from model import SimpleCNN


def evaluate(model, loader, device):
    """Evaluates the model accuracy on a given dataset loader."""
    model.eval()
    correct, total = 0, 0

    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)

            outputs = model(images)
            _, predicted = torch.max(outputs, dim=1)

            correct += (predicted == labels).sum().item()
            total += labels.size(0)

    return correct / total


def train(epochs=15, batch_size=64, lr=0.001, data_dir="./data"):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    train_loader, test_loader = get_dataloaders(
        data_dir=data_dir,
        batch_size=batch_size
    )

    model = SimpleCNN(num_classes=len(CLASS_NAMES)).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    best_acc = 0.0

    for epoch in range(1, epochs + 1):
        model.train()
        running_loss = 0.0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()

            outputs = model(images)
            loss = criterion(outputs, labels)

            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        train_loss = running_loss / len(train_loader)
        test_acc = evaluate(model, test_loader, device)

        print(
            f"Epoch {epoch}/{epochs} - "
            f"Training loss: {train_loss:.4f} - "
            f"Test accuracy: {test_acc:.2%}"
        )

        if test_acc > best_acc:
            best_acc = test_acc
            torch.save(model.state_dict(), "best_model.pt")

    print(f"\nTraining completed! Best test accuracy: {best_acc:.2%}")
    print("Model saved to: best_model.pt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train an image classification CNN on CIFAR-10."
    )
    parser.add_argument("--epochs", type=int, default=15)
    parser.add_argument("--batch_size", type=int, default=64)
    parser.add_argument("--lr", type=float, default=0.001)
    parser.add_argument("--data_dir", type=str, default="./data")

    args = parser.parse_args()

    train(
        args.epochs,
        args.batch_size,
        args.lr,
        args.data_dir
    )
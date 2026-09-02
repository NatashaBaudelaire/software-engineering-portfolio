"""
dataset.py

Loads the CIFAR-10 dataset (10 image classes) using torchvision.
The dataset is automatically downloaded the first time it is used.

Classes: airplane, automobile, bird, cat, deer, dog,
frog, horse, ship, truck.
"""

import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

CLASS_NAMES = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck",
]

# Standard CIFAR-10 mean and standard deviation for normalization
MEAN = (0.4914, 0.4822, 0.4465)
STD = (0.2470, 0.2435, 0.2616)


def get_transforms(train=True):
    """Returns the image transformations for training or testing."""
    if train:
        return transforms.Compose([
            transforms.RandomCrop(32, padding=4),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(MEAN, STD),
        ])
    return transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(MEAN, STD),
    ])


def get_dataloaders(data_dir="./data", batch_size=64, num_workers=2):
    """Creates and returns the training and test data loaders."""
    train_set = torchvision.datasets.CIFAR10(
        root=data_dir,
        train=True,
        download=True,
        transform=get_transforms(train=True),
    )

    test_set = torchvision.datasets.CIFAR10(
        root=data_dir,
        train=False,
        download=True,
        transform=get_transforms(train=False),
    )

    train_loader = DataLoader(
        train_set,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
    )

    test_loader = DataLoader(
        test_set,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
    )

    return train_loader, test_loader
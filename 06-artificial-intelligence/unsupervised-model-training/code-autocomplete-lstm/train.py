"""
train.py

Trains the CodeLSTM model in a supervised manner. For each window of
code tokens, the model learns to predict the correct next token.

Usage:
    python train.py --data_dir ../../ --epochs 10
"""

import argparse
import json
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from dataset import collect_py_files, build_vocab, CodeDataset
from model import CodeLSTM


def train(data_dir, epochs=10, batch_size=64, seq_len=50, lr=0.001):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    print("Collecting .py files...")
    code_chunks = collect_py_files(data_dir)
    if not code_chunks:
        raise RuntimeError(
            f"No .py files found in '{data_dir}'. "
            "Set --data_dir to a directory containing Python source code."
        )
    print(f"Collected {len(code_chunks)} file(s).")

    print("Building vocabulary...")
    vocab = build_vocab(code_chunks)
    print(f"Vocabulary contains {len(vocab)} unique tokens.")

    dataset = CodeDataset(code_chunks, vocab, seq_len=seq_len)
    if len(dataset) == 0:
        raise RuntimeError(
            "Dataset is empty: the collected code is shorter than seq_len. "
            "Reduce --seq_len or add more source files."
        )
    print(f"Generated {len(dataset)} training example(s).")

    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = CodeLSTM(vocab_size=len(vocab)).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    model.train()
    for epoch in range(1, epochs + 1):
        total_loss = 0.0
        for x_batch, y_batch in loader:
            x_batch, y_batch = x_batch.to(device), y_batch.to(device)

            optimizer.zero_grad()
            logits, _ = model(x_batch)
            loss = criterion(logits, y_batch)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(loader)
        print(f"Epoch {epoch}/{epochs} - Average loss: {avg_loss:.4f}")

    # Save the trained model and vocabulary
    torch.save(model.state_dict(), "code_lstm.pt")
    with open("vocab.json", "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print("\nTraining completed!")
    print("Model saved to: code_lstm.pt")
    print("Vocabulary saved to: vocab.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a code autocomplete model."
    )
    parser.add_argument(
        "--data_dir",
        type=str,
        default="../../",
        help="Root directory used to collect .py files."
    )
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch_size", type=int, default=64)
    parser.add_argument("--seq_len", type=int, default=50)
    parser.add_argument("--lr", type=float, default=0.001)
    args = parser.parse_args()

    train(args.data_dir, args.epochs, args.batch_size, args.seq_len, args.lr)
"""
dataset.py

Collects .py files from a directory, tokenizes the source code, and generates
(input, target) sequences for supervised training of a code autocomplete model.

Usage:
    from dataset import CodeDataset, build_vocab

    files = collect_py_files("../../")  # points to the root of your repository
    vocab = build_vocab(files)
    dataset = CodeDataset(files, vocab, seq_len=50)
"""

import os
import re
import torch
from torch.utils.data import Dataset


def collect_py_files(root_dir, exclude_dirs=("venv", "__pycache__", ".git")):
    """Recursively traverses root_dir and returns the contents of all .py files found."""
    code_chunks = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        for fname in filenames:
            if fname.endswith(".py"):
                path = os.path.join(dirpath, fname)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        code_chunks.append(f.read())
                except Exception as e:
                    print(f"Warning: could not read {path}: {e}")
    return code_chunks


def tokenize(code):
    """
    Simple regex-based tokenizer that separates identifiers,
    numbers, operators, and punctuation into individual tokens.
    Suitable for an introductory-level code autocomplete model.
    """
    pattern = r"\w+|[^\s\w]"
    return re.findall(pattern, code)


def build_vocab(code_chunks, min_freq=1):
    """Builds a token-to-ID vocabulary from the collected source code."""
    freq = {}
    for code in code_chunks:
        for tok in tokenize(code):
            freq[tok] = freq.get(tok, 0) + 1

    tokens = [t for t, c in freq.items() if c >= min_freq]
    vocab = {"<pad>": 0, "<unk>": 1}
    for tok in tokens:
        if tok not in vocab:
            vocab[tok] = len(vocab)
    return vocab


class CodeDataset(Dataset):
    """
    Supervised dataset where each example consists of a window of `seq_len`
    input tokens and the following token as the target. The model learns to
    predict the next token given a code context.
    """

    def __init__(self, code_chunks, vocab, seq_len=50):
        self.vocab = vocab
        self.seq_len = seq_len
        self.examples = []

        for code in code_chunks:
            ids = [vocab.get(tok, vocab["<unk>"]) for tok in tokenize(code)]
            for i in range(len(ids) - seq_len):
                x = ids[i:i + seq_len]
                y = ids[i + seq_len]
                self.examples.append((x, y))

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        x, y = self.examples[idx]
        return torch.tensor(x, dtype=torch.long), torch.tensor(y, dtype=torch.long)
"""
generate.py

Loads a trained model and suggests the next token given a user-provided
code snippet. A simple command-line code autocomplete tool.

Usage:
    python generate.py --prompt "def add(a, b):\\n    return a"
"""

import argparse
import json
import torch

from dataset import tokenize
from model import CodeLSTM


def load_model(model_path="code_lstm.pt", vocab_path="vocab.json"):
    """Loads the trained model and vocabulary."""
    with open(vocab_path, "r", encoding="utf-8") as f:
        vocab = json.load(f)

    inv_vocab = {idx: tok for tok, idx in vocab.items()}

    model = CodeLSTM(vocab_size=len(vocab))
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()

    return model, vocab, inv_vocab


def suggest_next_tokens(model, vocab, inv_vocab, prompt, top_k=5, seq_len=50):
    """Returns the top-k most likely next tokens for the given prompt."""
    tokens = tokenize(prompt)
    ids = [vocab.get(tok, vocab["<unk>"]) for tok in tokens]

    # Adjust sequence length (left padding if necessary)
    if len(ids) < seq_len:
        ids = [vocab["<pad>"]] * (seq_len - len(ids)) + ids
    else:
        ids = ids[-seq_len:]

    x = torch.tensor([ids], dtype=torch.long)

    with torch.no_grad():
        logits, _ = model(x)
        probs = torch.softmax(logits, dim=-1).squeeze(0)

    top_probs, top_ids = torch.topk(probs, top_k)
    suggestions = [(inv_vocab[i.item()], p.item()) for i, p in zip(top_ids, top_probs)]
    return suggestions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Suggests the next code token."
    )
    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="Current code snippet used to generate suggestions."
    )
    parser.add_argument("--top_k", type=int, default=5)
    args = parser.parse_args()

    model, vocab, inv_vocab = load_model()
    suggestions = suggest_next_tokens(
        model, vocab, inv_vocab, args.prompt, args.top_k
    )

    print(f"\nPrompt: {args.prompt!r}")
    print("Next token suggestions:")
    for tok, prob in suggestions:
        print(f"  {tok!r:<15} - {prob:.2%}")
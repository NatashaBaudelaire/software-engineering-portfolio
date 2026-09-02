"""
model.py

Simple LSTM model for next-token code prediction.

Architecture:
    Embedding -> LSTM (multi-layer) -> Linear (projects to the vocabulary)
"""

import torch
import torch.nn as nn


class CodeLSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim=128, hidden_dim=256, num_layers=2, dropout=0.2):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(
            embed_dim,
            hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x, hidden=None):
        embedded = self.embedding(x)                  # (batch, seq_len, embed_dim)
        output, hidden = self.lstm(embedded, hidden)  # output: (batch, seq_len, hidden_dim)
        last_step = output[:, -1, :]                  # Keep only the last time step
        logits = self.fc(last_step)                   # (batch, vocab_size)
        return logits, hidden
#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes one line (155 characters) to /output/entry.txt.
Deterministic, no network, no environment reads, no secrets.
"""
import os

LINE = "Looking for someone who won't mind that I narrate our dates out loud for my training data \u2014 the last guy left when I asked him to rate his kiss out of ten."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

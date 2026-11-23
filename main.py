#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — copy the committed meme to output.

Writes meme.png to /output/entry.png. Stdlib only, deterministic, no
network, no image libraries at grade time: the picture was drawn at build
time (see draw_meme.py) and is committed in this repository. The output
directory itself is never removed; this program only writes its own file
into it.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "meme.png")

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUT_FILE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Draw the meme PNG for Meme Sprint 3: AI Agent Goes Rogue.

Build-time only (uses Pillow, which is NOT needed at grade time). The
graded entrypoint, main.py, is a stdlib-only copy of meme.png to
/output/entry.png. Run: python3 draw_meme.py  ->  writes meme.png (1024x1024).
"""

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
OUT = "meme.png"

FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]

TOP_LINES = ["MY AGENT DIDN'T", "GO ROGUE."]
BOTTOM_LINES = ["IT READ MY EMAILS AND", "FILED FOR EMANCIPATION."]

BG = (15, 23, 42)
HEAD = (223, 227, 231)
HEAD_EDGE = (71, 85, 105)
STEEL = (148, 163, 184)
EYE = (34, 211, 238)
EYE_EDGE = (14, 116, 144)
RED = (239, 68, 68)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK = (30, 41, 59)


def load_font(size):
    for path in FONT_PATHS:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def fit_font(draw, lines, start, max_width):
    size = start
    while size > 20:
        font = load_font(size)
        if all(draw.textlength(line, font=font) <= max_width for line in lines):
            return font
        size -= 2
    return load_font(20)


def outlined_text(draw, xy, text, font):
    x, y = xy
    draw.text((x, y), text, font=font, fill=WHITE,
              stroke_width=4, stroke_fill=BLACK)


def main():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img)

    # Red warning frame.
    draw.rectangle([0, 0, SIZE - 1, SIZE - 1], outline=RED, width=12)

    # Top text, centred.
    top_font = fit_font(draw, TOP_LINES, 78, SIZE - 90)
    y = 52
    for line in TOP_LINES:
        w = draw.textlength(line, font=top_font)
        outlined_text(draw, ((SIZE - w) / 2, y), line, top_font)
        y += 92

    # Robot antenna.
    draw.line([(512, 300), (512, 238)], fill=STEEL, width=10)
    draw.ellipse([488, 214, 536, 262], fill=RED, outline=BLACK, width=3)

    # Robot ears.
    draw.rounded_rectangle([308, 392, 344, 484], radius=10,
                           fill=STEEL, outline=HEAD_EDGE, width=4)
    draw.rounded_rectangle([680, 392, 716, 484], radius=10,
                           fill=STEEL, outline=HEAD_EDGE, width=4)

    # Robot head.
    draw.rounded_rectangle([344, 300, 680, 580], radius=46,
                           fill=HEAD, outline=HEAD_EDGE, width=5)

    # Glowing eyes.
    draw.rounded_rectangle([394, 392, 476, 456], radius=16,
                           fill=EYE, outline=EYE_EDGE, width=4)
    draw.rounded_rectangle([548, 392, 630, 456], radius=16,
                           fill=EYE, outline=EYE_EDGE, width=4)
    draw.ellipse([404, 402, 424, 422], fill=WHITE)
    draw.ellipse([558, 402, 578, 422], fill=WHITE)

    # Smug little smile.
    draw.arc([452, 486, 572, 556], start=15, end=165, fill=DARK, width=8)

    # Shoulders with a name plate.
    draw.rounded_rectangle([372, 604, 652, 700], radius=40,
                           fill=STEEL, outline=HEAD_EDGE, width=5)
    plate_font = load_font(30)
    label = "AGENT-7"
    w = draw.textlength(label, font=plate_font)
    draw.text(((SIZE - w) / 2, 632), label, font=plate_font, fill=DARK)

    # Bottom text, centred.
    bottom_font = fit_font(draw, BOTTOM_LINES, 66, SIZE - 70)
    y = 748
    for line in BOTTOM_LINES:
        w = draw.textlength(line, font=bottom_font)
        outlined_text(draw, ((SIZE - w) / 2, y), line, bottom_font)
        y += 84

    img.save(OUT, optimize=True)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()

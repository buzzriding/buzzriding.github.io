#!/usr/bin/env python3
"""Generate assets/og-card.png — the shared social share card (1200x630).

Uses the brand tokens from the skills repo context.md: midnight #141418,
teal #2AADA0, offwhite #FAFAF7, grey #9AA0A6. Poppins/DM Sans are not
available on the runner, so the closest bundled grotesque is used; the card
is a flat colour composition, so the substitution is not noticeable.
"""

import glob
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
MIDNIGHT, TEAL, OFFWHITE, GREY, FAINT = "#141418", "#2AADA0", "#FAFAF7", "#9AA0A6", "#6E757C"


def font(bold: bool, size: int) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for root in ("/usr/share/fonts", "/usr/local/share/fonts", os.path.expanduser("~/.fonts")):
        hits = glob.glob(os.path.join(root, "**", name), recursive=True)
        if hits:
            return ImageFont.truetype(hits[0], size)
    return ImageFont.load_default()


def main() -> None:
    img = Image.new("RGB", (W, H), MIDNIGHT)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, W, 8], fill=TEAL)          # top rule
    d.rectangle([80, 180, 84, 470], fill=TEAL)    # left rail

    d.text((120, 200), "Buzz", font=font(True, 86), fill=OFFWHITE)
    offset = d.textlength("Buzz", font=font(True, 86))
    d.text((120 + offset, 200), "Riding", font=font(True, 86), fill=TEAL)

    d.text((120, 320), "Where curious marketers come", font=font(False, 40), fill=GREY)
    d.text((120, 372), "to stay one step ahead.", font=font(False, 40), fill=GREY)
    d.text((120, 468), "AI TOOL REVIEWS  ·  WORKFLOWS  ·  EXPERIMENTS",
           font=font(True, 22), fill=TEAL)
    d.text((120, 540), "buzzriding.github.io", font=font(False, 24), fill=FAINT)

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "assets")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "og-card.png")
    img.convert("P", palette=Image.ADAPTIVE, colors=16).save(out, optimize=True, bits=4)
    print(f"wrote {out} ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    main()

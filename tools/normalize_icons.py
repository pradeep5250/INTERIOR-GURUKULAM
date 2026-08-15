"""Build the four card icons from the raw line-art in icons/src.

The raw art comes out of the generator at wildly different scales and stroke
weights, on a baked-in cream disc. Each icon is re-cut so that all four share:

  * one ink colour (the cream disc comes from CSS, not the bitmap),
  * one footprint - the art is fitted to a common *circular* envelope rather
    than a common bounding box, so a wide icon like the handshake reads at the
    same visual size inside the round frame as a squarish one like the shop,
  * one stroke weight - source thickness is measured per icon and corrected,
    since each icon is scaled by a different amount.
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

ICONS = Path(__file__).resolve().parent.parent / "icons"
SRC = ICONS / "src"

INK = (61, 74, 36)
NAMES = [
    "icon-all-courses.png",
    "icon-nri-training.png",
    "icon-business-franchise.png",
    "icon-joint-venture.png",
]

CANVAS = 256
STROKE = 5.6  # target ink thickness in canvas pixels
WORK = CANVAS * 4  # weight is corrected here, so 1px of dilation is 0.25px of ink
# Luminance window separating the dark line work from the cream backdrop.
LINE_L, BG_L = 130.0, 205.0


def line_alpha(path: Path) -> Image.Image:
    grey = Image.open(path).convert("L")
    return grey.point(
        lambda v: 0 if v >= BG_L else 255 if v <= LINE_L else int(255 * (BG_L - v) / (BG_L - LINE_L))
    )


def stroke_width(alpha: Image.Image) -> float:
    """Median horizontal ink run, which approximates the pen thickness."""
    ink = np.asarray(alpha) > 96
    runs = []
    for row in ink:
        edges = np.diff(np.concatenate(([0], row.view(np.int8), [0])))
        starts = np.nonzero(edges == 1)[0]
        ends = np.nonzero(edges == -1)[0]
        runs.extend((ends - starts).tolist())
    runs = [r for r in runs if 1 < r <= 40]  # drop specks and long horizontal rules
    return float(np.median(runs))


for name in NAMES:
    alpha = line_alpha(SRC / name)
    art = alpha.crop(alpha.point(lambda v: 255 if v > 38 else 0).getbbox())

    # Fit the art's circumscribed circle to the canvas so every icon occupies the
    # same round envelope regardless of aspect ratio.
    diagonal = (art.width**2 + art.height**2) ** 0.5
    scale = WORK / diagonal
    art = art.resize((max(1, round(art.width * scale)), max(1, round(art.height * scale))), Image.LANCZOS)

    canvas = Image.new("L", (WORK, WORK), 0)
    canvas.paste(art, ((WORK - art.width) // 2, (WORK - art.height) // 2))
    canvas = canvas.point(lambda v: 0 if v < 60 else min(255, int(v * 1.8)))

    # Each icon was scaled by a different amount, so equalise the pen weight.
    before = stroke_width(canvas)
    delta = round(STROKE * 4 - before)
    if delta >= 2:
        canvas = canvas.filter(ImageFilter.MaxFilter(2 * (delta // 2) + 1))
    elif delta <= -2:
        canvas = canvas.filter(ImageFilter.MinFilter(2 * (-delta // 2) + 1))
    after = stroke_width(canvas)

    canvas = canvas.resize((CANVAS, CANVAS), Image.LANCZOS)
    canvas = canvas.point(lambda v: min(255, int(v * 1.25)))

    icon = Image.new("RGBA", (CANVAS, CANVAS), INK + (0,))
    icon.putalpha(canvas)
    icon.save(ICONS / name, optimize=True)
    print(f"{name:30} scale={scale:.3f} stroke {before / 4:.2f} -> {after / 4:.2f}px")

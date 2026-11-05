"""Rebuild the README galleries: python scripts/build_collages.py.

Requires Pillow. Source photos stay in images/ for future rearrangements.
"""

from fractions import Fraction
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
PRINTER_ROWS = [
    ["scrapnc-router", "scrapnc-totoro-carving", "scrapnc-electronics"],
    ["workshop-overview", "nonplanar-printer-prototype", "workshop-printers"],
    ["open-frame-printer", "compact-printer-purple-toolhead", "enclosed-compact-printer"],
    ["aluminum-frame-printer", "printer-toolhead-closeup", "printer-test-print", "printer-electronics"],
    ["motion-platform-electronics", "rotating-build-platform", "motion-platform-assembly", "motion-platform-workbench"],
]

COLLAGES = [
    ("printers-and-cnc-collage.webp", 2560, PRINTER_ROWS, 88),
    ("dual-arm-printer-collage.webp", 2560, [
        ["dual-arm-printer"],
        ["nonplanar-benchmark-perspective", "nonplanar-benchmark-side"],
    ], 92),
    ("art-collage.webp", 1800, [
        ["art-1", "art-2"],
        ["art-4", "art-5"],
        ["art-6", "art-3"],
        ["art-7", "art-8"],
    ], 94),
]


def build(filename, width, rows, quality):
    rendered_rows = []
    for names in rows:
        photos = []
        for name in names:
            with Image.open(ROOT / "images" / f"{name}.webp") as source:
                photos.append(source.convert("RGB"))

        ratios = [Fraction(photo.width, photo.height) for photo in photos]
        height = round(Fraction(width) / sum(ratios))
        exact_widths = [width * ratio / sum(ratios) for ratio in ratios]
        widths = [int(value) for value in exact_widths]
        remainders = sorted(
            range(len(photos)),
            key=lambda i: exact_widths[i] - widths[i],
            reverse=True,
        )
        for i in remainders[: width - sum(widths)]:
            widths[i] += 1

        row = Image.new("RGB", (width, height))
        x = 0
        for photo, tile_width in zip(photos, widths):
            # Fit away only the tiny aspect differences from pixel rounding.
            tile = ImageOps.fit(photo, (tile_width, height), Image.Resampling.LANCZOS)
            row.paste(tile, (x, 0))
            x += tile_width
        assert x == width
        rendered_rows.append(row)

    collage = Image.new("RGB", (width, sum(row.height for row in rendered_rows)))
    y = 0
    for row in rendered_rows:
        collage.paste(row, (0, y))
        y += row.height

    destination = ROOT / "images" / filename
    collage.save(destination, "WEBP", quality=quality, method=6)
    print(f"Saved {destination.name}: {collage.width}x{collage.height}, "
          f"{destination.stat().st_size / 1048576:.2f} MiB")


if __name__ == "__main__":
    for settings in COLLAGES:
        build(*settings)

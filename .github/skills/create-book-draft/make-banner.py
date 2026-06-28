#!/usr/bin/env python3
"""
Resize a book cover image to a 1200x630 banner.
The cover is centered/fitted and padded to maintain aspect ratio.
The padding color is sampled from the dominant edge color of the cover.

Usage: python3 make-banner.py <input_image> <output_path>
"""

import sys
import os
from pathlib import Path

def make_banner(input_path: str, output_path: str, width: int = 1200, height: int = 630) -> None:
    try:
        from PIL import Image, ImageFilter
    except ImportError:
        print("Pillow not installed. Trying to install...")
        os.system(f"{sys.executable} -m pip install Pillow --quiet")
        from PIL import Image, ImageFilter

    img = Image.open(input_path).convert("RGB")

    # Scale the cover to fit within the target dimensions, maintaining aspect ratio
    img.thumbnail((width, height), Image.LANCZOS)

    # Sample background color from the four corners of the (now scaled) cover
    w, h = img.size
    corner_pixels = [
        img.getpixel((0, 0)),
        img.getpixel((w - 1, 0)),
        img.getpixel((0, h - 1)),
        img.getpixel((w - 1, h - 1)),
    ]
    bg_color = tuple(sum(c[i] for c in corner_pixels) // 4 for i in range(3))

    # Create the canvas and paste the cover centered
    canvas = Image.new("RGB", (width, height), bg_color)
    x_offset = (width - w) // 2
    y_offset = (height - h) // 2
    canvas.paste(img, (x_offset, y_offset))

    # Apply very slight blur to smooth any hard edges at the boundary
    canvas.save(output_path, "JPEG", quality=92, optimize=True)
    print(f"Banner saved to {output_path} ({width}x{height})")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} <input_image> <output_path>")
        sys.exit(1)
    make_banner(sys.argv[1], sys.argv[2])

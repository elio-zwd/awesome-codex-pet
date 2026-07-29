#!/usr/bin/env python3
"""将二格 AI 修复候选注册到现有的 16 格环视单元。"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image


RUN = Path(__file__).resolve().parents[1]
ATLAS = RUN / "final" / "spritesheet-extended.png"
SOURCE = RUN / "decoded" / "look-row-10-left-quartet-repair.png"
OUT_DIR = RUN / "qa" / "look-cells-repaired"
KEY = (106, 0, 255)
CELL = (192, 208)
LABELS = [
    "000", "022.5", "045", "067.5", "090", "112.5", "135", "157.5",
    "180", "202.5", "225", "247.5", "270", "292.5", "315", "337.5",
]


def clear_key(image: Image.Image, threshold: float = 106.0) -> Image.Image:
    """去除紫色底，并保留角色边缘的半透明像素。"""
    rgba = image.convert("RGBA")
    pixels = rgba.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            red, green, blue, alpha = pixels[x, y]
            distance = math.sqrt((red - KEY[0]) ** 2 + (green - KEY[1]) ** 2 + (blue - KEY[2]) ** 2)
            if distance <= threshold:
                pixels[x, y] = (0, 0, 0, 0)
    return rgba


def geometry(image: Image.Image) -> tuple[int, float, int]:
    alpha = image.getchannel("A")
    points = [(x, y) for y in range(image.height) for x in range(image.width) if alpha.getpixel((x, y)) > 16]
    if not points:
        raise ValueError("参考单元没有可见像素")
    top = min(y for _, y in points)
    bottom = max(y for _, y in points) + 1
    lower = [(x, y) for x, y in points if y >= top + (bottom - top) * 0.72] or points
    return bottom - top, sum(x for x, _ in lower) / len(lower), bottom


def register(candidate: Image.Image, target: tuple[int, float, int]) -> Image.Image:
    bbox = candidate.getbbox()
    if bbox is None:
        raise ValueError("候选图没有可见像素")
    crop = candidate.crop(bbox)
    src_height, src_lower_x, _ = geometry(candidate)
    target_height, target_lower_x, target_bottom = target
    scale = min(target_height / src_height, (CELL[0] - 10) / crop.width, (CELL[1] - 10) / crop.height)
    crop = crop.resize((round(crop.width * scale), round(crop.height * scale)), Image.Resampling.LANCZOS)
    lower_local = (src_lower_x - bbox[0]) * scale
    left = round(target_lower_x - lower_local)
    top = target_bottom - crop.height
    result = Image.new("RGBA", CELL, (0, 0, 0, 0))
    result.alpha_composite(crop, (left, top))
    return result


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with Image.open(ATLAS) as opened:
        atlas = opened.convert("RGBA")
    reference = atlas.crop((6 * CELL[0], 0, 7 * CELL[0], CELL[1]))
    target = geometry(reference)

    for index, label in enumerate(LABELS):
        row = 9 + index // 8
        col = index % 8
        atlas.crop((col * CELL[0], row * CELL[1], (col + 1) * CELL[0], (row + 1) * CELL[1])).save(OUT_DIR / f"{label}.png")

    with Image.open(SOURCE) as opened:
        strip = clear_key(opened)
    for label, index in (("225", 0), ("247.5", 1), ("270", 2), ("292.5", 3)):
        left = round(index * strip.width / 4)
        right = round((index + 1) * strip.width / 4)
        candidate = strip.crop((left, 0, right, strip.height))
        register(candidate, target).save(OUT_DIR / f"{label}.png")
    print(OUT_DIR)


if __name__ == "__main__":
    main()
